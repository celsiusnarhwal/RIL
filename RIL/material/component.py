import typing as t

import casefy
import inflect as ifl
import reflex as rx
from pydantic import Field, field_serializer, model_serializer
from pydantic_extra_types.color import Color

from RIL import utils
from RIL._core import Base, Props, validate_props

__all__ = ["material"]

inflect = ifl.engine()


class MaterialSymbolProps(Props):
    weight: t.Literal[100, 200, 300, 400, 500, 600, 700] = Field(400, exclude=True)
    """
    The weight of the icon. May be 100, 200, 300, 400, 500, 600, or 700.
    """

    variant: t.Literal["outlined", "rounded", "sharp"] = Field("outlined", exclude=True)
    """
    The variant of the icon. May be either `"outlined"`, `"rounded"`, or `"sharp"`. Defaults to `"outlined"`.
    """

    filled: bool = Field(False, exclude=True)
    """
    Whether or not to use the icon's filled appearance.
    """

    color: Color = Field("currentColor", serialization_alias="fill")
    """
    The color of the icon. May be:
    - a hex code (e.g., `"#03cb98"`)
    - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = Field("1em", exclude=True)
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
    
    See Also
        https://developer.mozilla.org/en-US/docs/Web/CSS/length
    """

    @property
    def package(self) -> str:
        return f"@material-symbols/svg-{self.weight}"

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | None):
        return color if color == "currentColor" else color.as_hex()

    @model_serializer(mode="wrap")
    def serialize(self, handler: t.Callable):
        serialized = super().serialize(handler)

        if self.size:
            serialized["height"] = serialized["width"] = self.size

        return serialized


class MaterialSymbol(Base):
    fill: rx.Var[str]
    width: rx.Var[str]
    height: rx.Var[str]

    @property
    def import_var(self):
        return rx.ImportVar(tag=self.tag, install=False, is_default=True)

    @classmethod
    @validate_props
    @utils.require_turbopack
    def create(cls, icon: str, props: MaterialSymbolProps) -> rx.Component:
        component = super().create(**props.model_dump())

        component.tag = "Material" + casefy.pascalcase(icon.casefold())

        library = f"{props.package}/{props.variant}/{casefy.snakecase(icon.casefold())}"

        if props.filled:
            library += "-fill"

        library += ".svg"

        component.library = library

        return component


material = MaterialSymbol.create
