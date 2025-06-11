import typing as t

import casefy
import reflex as rx
from pydantic import Field, computed_field

from RIL._core import Color, Props, SVGComponent, validate_props


class BootstrapIconProps(Props):
    color: Color = None
    """
    The color of the icon. May be:
    - a hex code
    - a integer tuple of RGB, RBGA, or HSL
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = Field("1em", exclude=True)
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`)
    """

    title: str = None
    """
    An accessible, short-text, description of the icon.
    """

    @computed_field
    @property
    def height(self) -> int | str:
        return self.size

    @computed_field
    @property
    def width(self) -> int | str:
        return self.size


class BootstrapIcon(SVGComponent):
    lib_dependencies = ["bootstrap-icons"]

    color: rx.Var[t.Any]
    width: rx.Var[t.Any]
    height: rx.Var[t.Any]
    title: rx.Var[t.Any]

    @property
    def import_var(self):
        return rx.ImportVar(self.tag, install=False, is_default=True)

    @classmethod
    @validate_props
    def create(cls, icon: str, props: BootstrapIconProps) -> rx.Component:
        props.title = props.title or icon

        component = super().create(**props.model_dump())

        component.library = f"bootstrap-icons/icons/{icon.casefold()}.svg"
        component.tag = "Bootstrap" + casefy.pascalcase(icon.casefold())

        return component


bootstrap = bi = BootstrapIcon.create
