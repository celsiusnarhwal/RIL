import typing as t

import casefy
import reflex as rx
from pydantic import ConfigDict, Field, model_serializer
from reflex import Component
from reflex.utils.imports import ImportDict

from RIL._core import Base, Color, Props, validate_props
from RIL.settings import settings

__all__ = ["phosphor"]


NPM_PACKAGE = "@phosphor-icons/react@^2"


class PhosphorIconProps(Props):
    variant: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = Field(
        None, serialization_alias="weight"
    )
    """
    The variant of the icon. May be one of `"thin"`, `"light"`, `"regular"`, `"bold"`, `"fill"`, or 
    `"duotone"`.
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


class PhosphorIconContextProps(PhosphorIconProps):
    model_config = ConfigDict(extra="ignore")

    color: Color = settings.phosphor.color
    size: int | str = settings.phosphor.size
    variant: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = Field(
        settings.phosphor.variant, serialization_alias="weight"
    )

    @model_serializer(mode="wrap")
    def serialize(self, handler: t.Callable):
        return {"value": handler(self)}


class PhosphorIconContext(Base):
    tag = "PhosphorIconContext.Provider"

    value: rx.Var[t.Any]

    def add_imports(self) -> ImportDict | list[ImportDict]:
        return {NPM_PACKAGE: [rx.ImportVar("IconContext", alias="PhosphorIconContext")]}

    @classmethod
    @validate_props
    def create(cls, *children, props: PhosphorIconContextProps) -> rx.Component:
        return super().create(*children, **props.model_dump())


class PhosphorIcon(Base):
    library = NPM_PACKAGE

    weight: rx.Var[t.Any]
    color: rx.Var[t.Any]
    size: rx.Var[t.Any]
    alt: rx.Var[t.Any]

    @classmethod
    @validate_props
    def create(cls, icon: str, props: PhosphorIconProps) -> rx.Component:
        props.alt = props.alt or icon

        component = super().create(**props.model_dump())
        component.tag = casefy.pascalcase(icon.casefold()) + "Icon"
        component.alias = "Phosphor" + component.tag

        return component

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {(1, "PhosphorIconContext.Provider"): PhosphorIconContext.create()}


class Phosphor(rx.ComponentNamespace):
    __call__ = staticmethod(PhosphorIcon.create)
    context = staticmethod(PhosphorIconContext.create)


phosphor = Phosphor()
