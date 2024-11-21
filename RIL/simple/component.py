"""
A Reflex component providing access to the library of Simple Icons.

https://ril.celsiusnarhwal.dev/simple
"""

import typing as t

from pydantic import field_serializer
from pydantic_extra_types.color import Color

from RIL._core import Base, Props, validate_props
from RIL.settings import settings

__all__ = ["simple", "si"]


class SimpleIconProps(Props):
    title: str = None
    """
    A short, accessible, description of the icon.
    """

    color: Color | t.Literal["default"] = None
    """
    The color of this icon. May be:
    - a hex code (e.g., `"#03cb98"`)
    - an tuple of RGB, RBGA, or HSL values
    - `"default"`, which makes the icon use whatever color Simple Icons has chosen as its default
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = None
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
    """

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | t.Literal["default"] | None):
        return color.as_hex() if color and color != "default" else color


class SimpleIcon(Base):
    library = settings.simple.package

    @classmethod
    @validate_props
    def create(cls, icon: str, props: SimpleIconProps):
        component_model = cls._reproduce(props=props.model_dump())

        component = component_model._create(**props.model_dump())
        component.tag = "Si" + icon.replace(" ", "").replace(".", "dot").capitalize()

        return component


simple = SimpleIcon.create
si = simple
