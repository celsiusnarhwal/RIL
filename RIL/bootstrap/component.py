from functools import partial

import casefy
import reflex as rx
from pydantic import field_serializer
from pydantic_extra_types.color import Color
from reflex import ImportDict

from RIL import utils
from RIL._core import Base, Props, validate_props


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

    size: int | str = "1em"
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`)
    """

    title: str = None
    """
    An accessible, short-text, description of the icon.
    """

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | None):
        return color.as_hex() if color else color


class BootstrapIcon(Base):
    lib_dependencies = ["bootstrap-icons", "@svgr/webpack"]

    def add_imports(self, **imports) -> ImportDict | list[ImportDict]:
        return imports

    @classmethod
    @validate_props
    @utils.require_turbopack
    def create(cls, icon: str, props: BootstrapIconProps) -> rx.Component:
        component_model = cls._reproduce(
            props_to_override=props.model_dump(),
        )

        tag = "Bootstrap" + casefy.pascalcase(icon.casefold())

        component_model.add_imports = partial(
            component_model.add_imports,
            **{
                f"bootstrap-icons/icons/{icon.casefold()}.svg": rx.ImportVar(
                    tag, install=False, is_default=True
                )
            },
        )

        component = super(cls, component_model).create(**props.model_dump())

        component.tag = tag

        return component


bootstrap = bi = BootstrapIcon.create
