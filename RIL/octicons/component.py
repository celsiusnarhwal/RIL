import re
import typing as t

import casefy
import reflex as rx
import reflex.constants.colors
from pydantic import Field

from RIL._core import Base, Color, Props, validate_props

__all__ = ["octicons"]


class OcticonProps(Props):
    color: Color = Field("currentColor", serialization_alias="fill")
    """
    The color of the icon. May be:
    - a hex code
    - a tuple of RGB, RGBA, or HSL values
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str | t.Literal["small", "medium", "large"] = None
    """
    The size of the icon. May be `"small"`, `"medium"`, or `"large"`. May also be an integer (in pixels) or 
    a CSS size string (e.g., `'1rem'`),
    """


class Octicon(Base):
    library = "@primer/octicons-react@^19"

    fill: rx.Var[t.Any]
    size: rx.Var[t.Any]

    @classmethod
    @validate_props
    def create(cls, icon: str, props: OcticonProps):
        component = super().create(**props.model_dump())

        icon = re.sub(r"icon$", "", icon, flags=re.I)
        component.tag = casefy.pascalcase(icon.casefold()) + "Icon"
        component.alias = "Octicons" + component.tag

        return component


octicons = Octicon.create
