import typing as t

import casefy
import reflex as rx
from pydantic import ConfigDict, field_serializer, model_serializer
from pydantic_extra_types.color import Color
from reflex import Component
from reflex.utils.imports import ImportDict

from RIL._core import Base, Props, validate_props
from RIL.settings import settings

__all__ = ["phosphor"]


NPM_PACKAGE = "@phosphor-icons/react@^2"


class PhosphorIconProps(Props):
    weight: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = None
    """
    The icon's weight (i.e., style). May be one of `"thin"`, `"light"`, `"regular"`, `"bold"`, `"fill"`, or `"duotone"`.
    """

    color: Color = None
    """
    The color of the icon. May be:
    - a hex code
    - a tuple of RGB, RGBA, or HSL values
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = None
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
    
    See Also
        https://developer.mozilla.org/en-US/docs/Web/CSS/length
    """

    alt: str = None
    """
    Alt text for the icon.
    """

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | None):
        return color.as_hex() if color else color


class PhosphorIconContextProps(PhosphorIconProps):
    model_config = ConfigDict(extra="ignore")

    # If we don't set a default here then context-wrapped icons will be *huge*.
    size: int | str = "1em"

    @model_serializer(mode="wrap")
    def serialize(self, handler: t.Callable):
        serialized = super().serialize(handler)
        return {"value": serialized}


class PhosphorIconContext(Base):
    tag = "PhosphorIconContext.Provider"

    def add_imports(self) -> ImportDict | list[ImportDict]:
        return {NPM_PACKAGE: [rx.ImportVar("IconContext", alias="PhosphorIconContext")]}

    @classmethod
    @validate_props
    def create(cls, *children, props: PhosphorIconContextProps) -> rx.Component:
        component_model = cls._reproduce(props_to_override=props.model_dump())
        return super(cls, component_model).create(**props.model_dump())


class PhosphorIcon(Base):
    library = NPM_PACKAGE

    @classmethod
    @validate_props
    def create(cls, icon: str, props: PhosphorIconProps) -> rx.Component:
        component_model = cls._reproduce(props_to_override=props.model_dump())

        component = super(cls, component_model).create(**props.model_dump())
        component.tag = casefy.pascalcase(icon.casefold()) + "Icon"
        component.alias = "Phosphor" + component.tag

        return component

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        if settings.phosphor.provider_settings:
            return {
                (1, "PhosphorIconContext.Provider"): PhosphorIconContext.create(
                    **settings.phosphor.provider_settings
                )
            }

        return {}


class Phosphor(rx.ComponentNamespace):
    __call__ = staticmethod(PhosphorIcon.create)
    context = staticmethod(PhosphorIconContext.create)


phosphor = Phosphor()
