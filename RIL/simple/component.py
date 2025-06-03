import typing as t
from functools import partial

import reflex as rx
from loguru import logger
from pydantic import BaseModel, Field, field_serializer, field_validator
from pydantic_extra_types.color import Color
from reflex.utils.imports import ImportDict

from RIL._core import Base, Props, validate_props
from RIL.settings import settings

__all__ = ["simple", "si"]


class SimpleIconsPackage(BaseModel):
    base_package: t.ClassVar[str] = "simple-icons"

    version: int | t.Literal["latest"]

    @property
    def version_specifier(self) -> str:
        return self.version if self.version == "latest" else f"^{self.version}"

    @property
    def package_name(self):
        return f"{self.package_alias}@npm:{self.base_package}@{self.version_specifier}"

    @property
    def package_alias(self) -> str:
        return (
            self.base_package
            if self.version == "latest"
            else f"{self.base_package}-{self.version}"
        )

    @property
    def import_name(self) -> str:
        name = self.package_alias

        if self.version != "latest" and self.version <= 7:
            name += "/icons"

        return name


class SimpleIconProps(Props):
    title: str = None
    """
    A short, accessible, description of the icon.
    """

    color: Color | t.Literal["brand", "default"] = None
    """
    The color of this icon. May be:
    - a hex code (e.g., `"#03cb98"`)
    - an tuple of RGB, RBGA, or HSL values
    - `"brand"` to use the icon's brand color
    - any valid color name as determined by the CSS Color Module Level 3 specification 
    (https://www.w3.org/TR/css-color-3/#svg-color)
    
    Hex codes are case-insensitive and the leading `#` is optional.
    """

    size: int | str = None
    """
    The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
    """

    version: int | t.Literal["latest"] = Field(settings.simple.version, exclude=True)
    """
    The major version of Simple Icons to use for this icon. May be "latest" or an integer 
    greater than or equal to 10.
    
    Defaults to the value of the `simple.version` setting.
    """

    @property
    def package(self) -> SimpleIconsPackage:
        return SimpleIconsPackage(version=self.version)

    @field_validator("version")
    def validate_version(cls, v):
        if isinstance(v, int) and not v >= 5:
            raise ValueError("Simple Icons versiion must be greater than or equal to 5")

        return v

    @field_validator("color")
    def validate_color(cls, v):
        if v == "default":
            v = "brand"
            logger.warning(
                "The 'default' color for Simple Icons is deprecated, use 'brand' instead"
            )

        return v

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | t.Literal["brand"] | None):
        return color.as_hex() if color and color != "brand" else color


class SimpleIcon(Base):
    library = "$/public/" + rx.asset("SimpleIcon.jsx", shared=True)
    tag = "SimpleIcon"

    icon: rx.Var[str]

    def add_imports(self, **imports) -> ImportDict | list[ImportDict]:
        return imports

    @classmethod
    @validate_props
    def create(cls, icon: str, props: SimpleIconProps):
        component_model = cls._reproduce(
            props_to_override=props.model_dump(),
            lib_dependencies=[props.package.package_name],
        )

        tag = "si" + icon.replace(" ", "").replace(".", "dot").capitalize()

        component_model.add_imports = partial(
            component_model.add_imports,
            **{props.package.import_name: rx.ImportVar(tag, install=False)},
        )

        return super(cls, component_model).create(
            **props.model_dump(), icon=rx.Var(tag)
        )


simple = si = SimpleIcon.create
