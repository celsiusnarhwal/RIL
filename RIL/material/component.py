import re
import typing as t

import casefy
import inflect as ifl
import reflex as rx
from pydantic import Field, field_serializer, model_serializer
from pydantic_extra_types.color import Color
from reflex.utils.imports import ImportDict

from RIL._core import Base, Props, validate_props

__all__ = ["material"]

inflect = ifl.engine()


class MaterialSymbolProps(Props):
    variant: t.Literal["outlined", "rounded", "sharp"] = Field("outlined", exclude=True)
    """
    The variant of the icon. May be either `"outlined"`, `"rounded"`, or `"sharp"`. Defaults to `"outlined"`.
    """

    filled: bool = Field(False, exclude=True)
    """
    Whether or not to use the icon's filled appearance.
    """

    color: Color = Field(None, serialization_alias="fill")
    """
    The color of the icon. May be:
    - a hex code (e.g., `"#03cb98"`)
    - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = Field(None, exclude=True)
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
    
    See Also
        https://developer.mozilla.org/en-US/docs/Web/CSS/length
    """

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | None):
        return color.as_hex() if color else color

    @model_serializer(mode="wrap")
    def serialize(self, handler: t.Callable):
        serialized = super().serialize(handler)

        if self.size:
            serialized["height"] = serialized["width"] = self.size

        return serialized


class MaterialSymbol(Base):
    @property
    def import_var(self):
        return rx.ImportVar(tag=self.tag, alias=self.alias, install=False)

    def add_imports(self) -> ImportDict | list[ImportDict]:
        return {
            "@nine-thirty-five/material-symbols-react@^1": rx.ImportVar(
                None, render=False, transpile=True
            )
        }

    @classmethod
    @validate_props
    def create(cls, icon: str, props: MaterialSymbolProps) -> rx.Component:
        component_model = cls._reproduce(props_to_override=props.model_dump())

        component = super(cls, component_model).create(**props.model_dump())
        component.library = f"@nine-thirty-five/material-symbols-react/{props.variant}"

        if props.filled:
            component.library += "/filled"

        # The tag is the supplied icon name with whitespace removed and any numbers converted to their PascalCase
        # word forms. Consecutive numbers are treated as a group — e.g., "E911 Avatar" becomes
        # "ENineHundredElevenAvatar" and not "ENineOneOneAvatar".

        component.tag = re.sub(
            r"\d+",
            lambda m: casefy.pascalcase(inflect.number_to_words(m.group(), andword="")),
            icon,
        )

        component.tag = component.tag.replace(" ", "")

        # The alias is "Material" + the tag + the variant + "Filled" if the icon is to use its
        # filled appearance.

        component.alias = (
            "Material"
            + component.tag
            + casefy.pascalcase(" ".join(component.library.split("/")[2:]))
        )

        return component


material = MaterialSymbol.create
