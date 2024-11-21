import re

import casefy
from pydantic import validate_call, field_serializer
from pydantic_extra_types.color import Color
import reflex as rx
from RIL._core import Base, Props, validate_props
import typing as t


NPM_PACKAGE = "react-bootstrap-icons@^1"


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

    size: int | str = None
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).h
    """

    title: str = None
    """
    An accessible, short-text, description of the icon.
    """

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | None):
        return color.as_hex() if color else color


class BootstrapIcon(Base):
    library = NPM_PACKAGE

    @classmethod
    @validate_props
    def create(cls, icon: str, props: BootstrapIconProps) -> rx.Component:
        component_model = cls._reproduce(props=props.model_dump())

        component = component_model._create(**props.model_dump())
        component.tag = casefy.pascalcase(icon.casefold())

        if re.match(r"^\d", component.tag):
            component.tag = "Icon" + component.tag

        component.alias = "Bootstrap" + component.tag

        return component


bootstrap = BootstrapIcon.create
