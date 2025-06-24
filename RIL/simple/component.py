import typing as t

import reflex as rx
from pydantic import BaseModel, Field, field_validator

from RIL._core import Base, Color, Props, validate_props
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
    def object_import(self) -> str:
        name = self.package_alias

        if self.version != "latest" and self.version <= 7:
            name += "/icons"

        return name


class SimpleIconProps(Props):
    title: str = None
    """
    A short, accessible, description of the icon.
    """

    color: Color | t.Literal["brand"] = "currentColor"
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
            raise ValueError("Simple Icons version must be greater than or equal to 5")

        return v


class SimpleIcon(Base):
    library = "$/public/" + rx.asset("SimpleIcon.jsx", shared=True)
    tag = "SimpleIcon"

    icon: rx.Var[str]
    title: rx.Var[t.Any]
    color: rx.Var[t.Any]

    @classmethod
    @validate_props
    def create(cls, icon: str, props: SimpleIconProps):
        if icon == "/e/":
            icon = "e"

        tag = "si" + icon.replace(" ", "").replace(".", "dot").capitalize()

        if props.version == "latest":
            var = rx.Var(tag)
            object_import_var = rx.ImportVar(tag, install=False)
        else:
            alias = tag + str(props.version)
            var = rx.Var(alias)
            object_import_var = rx.ImportVar(tag, alias=alias, install=False)

        component = super().create(**props.model_dump(), icon=var)
        component.imports = {
            props.package.package_name: rx.ImportVar(None, render=False),
            props.package.object_import: object_import_var,
        }

        return component


simple = si = SimpleIcon.create
