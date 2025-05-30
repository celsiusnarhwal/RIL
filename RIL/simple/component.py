import typing as t
from functools import partial

import hishel
import httpx
import reflex as rx
import semver
from loguru import logger
from pydantic import BaseModel, Field, field_serializer
from pydantic_extra_types.color import Color
from reflex.utils.imports import ImportDict
from reflex.utils.registry import get_npm_registry

from RIL._core import Base, Props, validate_props
from RIL.settings import settings

__all__ = ["simple", "si"]


class SimpleIconsPackage(BaseModel):
    base_package: t.ClassVar[str] = "@celsiusnarhwal/ril-simple-icons"

    name: str

    @property
    def component_library(self) -> str:
        return self.name.split("@npm:")[0]

    @property
    def import_dict(self) -> dict:
        return {self.name: rx.ImportVar(None, render=False)}

    @classmethod
    def at(cls, version: semver.Version | t.Literal["latest"]) -> t.Self:
        return cls(
            name=f"{cls.base_package}-{version}@npm:{cls.base_package}@{version}"
        )


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

    version: int | t.Literal["latest"] = Field(
        settings.simple.version, ge=10, exclude=True
    )
    """
    The major version of Simple Icons to use for this icon. May be "latest" or an integer 
    greater than or equal to 10.
    
    Defaults to the value of the `simple.version` setting.
    """

    @property
    def package(self) -> SimpleIconsPackage:
        if self.version == "latest":
            return SimpleIconsPackage.at("latest")

        with hishel.CacheClient(base_url=get_npm_registry()) as npm:
            try:
                resp = npm.get(SimpleIconsPackage.base_package)
                resp.raise_for_status()
            except httpx.HTTPError:
                logger.critical(
                    f"RIL could not determine the version of {SimpleIconsPackage.base_package} to install "
                    "because it could not access the NPM registry. You can suppress this error "
                    'by setting the simple.version setting to "latest".'
                )

                exit(1)

        package_info = resp.json()
        versions = [
            semver.Version.parse(v)
            for v in sorted(
                package_info["versions"], key=semver.Version.parse, reverse=True
            )
        ]

        for version in versions:
            if version.major <= self.version and not version.prerelease:
                return SimpleIconsPackage.at(version)
        else:
            logger.critical(
                f"No version of {SimpleIconsPackage.base_package} could be sound for "
                f"Simple Icons <= {self.version}."
            )

            exit(1)

    @field_serializer("color")
    def serialize_color_as_hex(self, color: Color | t.Literal["default"] | None):
        return color.as_hex() if color and color != "default" else color


class SimpleIcon(Base):
    @property
    def import_var(self):
        return rx.ImportVar(self.tag, install=False)

    def add_imports(self, **imports) -> ImportDict | list[ImportDict]:
        return imports

    @classmethod
    @validate_props
    def create(cls, icon: str, props: SimpleIconProps):
        component_model = cls._reproduce(props_to_override=props.model_dump())
        component_model.add_imports = partial(
            component_model.add_imports, **props.package.import_dict
        )

        component = super(cls, component_model).create(**props.model_dump())
        component.library = props.package.component_library
        component.tag = "Si" + icon.replace(" ", "").replace(".", "dot").capitalize()

        return component


simple = si = SimpleIcon.create
