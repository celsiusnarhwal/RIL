import os
import typing as t
from pathlib import Path

import hishel
import httpx
import semver
from jinja2 import Environment, FileSystemLoader
from loguru import logger
from pydantic import AnyHttpUrl, BaseModel, Field, model_validator
from pydantic_extra_types.color import Color
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)
from reflex.utils.prerequisites import get_web_dir

__all__ = ["settings"]

jinja = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))


class FontAwesomeSettings(BaseModel):
    """
    Settings for RIL's Font Awesome component.
    """

    pro_enabled: bool = False
    kit_code: str = None
    npm_registry: AnyHttpUrl = "https://npm.fontawesome.com"

    @property
    def kit_package(self) -> str | None:
        """
        Return the name of the Kit package if Font Awesome Pro is enabled and a Kit code is provided,
        or `None` otherwise.
        """
        if self.kit_code and self.kit_code:
            logger.debug(f"Using Font Awesome Kit {self.kit_code}")
            return f"@awesome.me/kit-{self.kit_code}"

    @model_validator(mode="after")
    def write_npmrc(self):
        """
        Write a .npmrc file to the Reflex web directory if Font Awesome Pro is enabled, or remove that file if
        it isn't.
        """
        userland_npmrc = get_web_dir() / ".npmrc"

        if not self.pro_enabled:
            userland_npmrc.unlink(missing_ok=True)
        else:
            npmrc_template = jinja.get_template(".npmrc.jinja")
            reference_npmrc = npmrc_template.render(registry=self.npm_registry)

            if userland_npmrc.parent.exists():
                userland_npmrc.write_text(reference_npmrc)

        return self


class SimpleIconsSettings(BaseModel):
    """
    Settings for RIL's Simple Icons component.
    """

    version: int | t.Literal["latest"] = Field("latest", ge=10)

    @property
    def package(self) -> str:
        """
        If the `version` setting is set, return the highest version of @icons-pack/react-simple-icons that
        depends on a version of Simple Icons with a major version number that less than or equal to the value of that
        setting.

        If the `version` setting it not set, return `"@icons-pack/react-simple-icons"`.
        """
        base_package = "@icons-pack/react-simple-icons"

        if self.version == "latest":
            return base_package

        with hishel.CacheClient(base_url="https://registry.npmjs.org") as npm:
            try:
                resp = npm.get("@icons-pack/react-simple-icons")
                resp.raise_for_status()
            except httpx.HTTPError:
                logger.critical(
                    "RIL could not determine the version of @icons-pack/react-simple-icons to install "
                    "because it could not access the NPM registry. You can suppress this error "
                    "by setting the simple.version setting to @latest, but if NPM is "
                    "truly inaccessible then Reflex is not going to work anyway."
                )

                exit(1)

            package_info = resp.json()

            for release in reversed(package_info["versions"].values()):
                package_version = semver.Version.parse(release["version"])

                if package_version.prerelease:
                    continue

                package_si_version = semver.Version.parse(
                    release["devDependencies"]["simple-icons"]
                )

                if package_si_version.major <= self.version:
                    logger.debug(
                        f"Using {base_package}@{package_version} "
                        f"with Simple Icons {package_si_version}"
                    )

                    return f"{base_package}@{package_version}"
            else:
                logger.critical(
                    f"No version of {base_package} could be sound for Simple Icons <= {self.version}."
                )


class PhosphorSettings(BaseModel):
    """
    Settings for RIL's Phosphor Icons component.
    """

    color: Color = None
    size: int | str = None
    weight: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = None

    @property
    def provider_settings(self) -> dict:
        return self.model_dump(exclude_none=True)


class FontAwesomePackageTokenSetting(BaseSettings):
    """
    A special settings class that exists solely to consume the `FONTAWESOME_PACKAGE_TOKEN` environment variable
    via the current process or a `.env` file.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    fontawesome_package_token: str = ""

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (dotenv_settings,)

    @model_validator(mode="after")
    def set_token(self):
        os.environ.setdefault(
            "FONTAWESOME_PACKAGE_TOKEN", self.fontawesome_package_token
        )
        return self


class RILSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RIL_",
        env_file=".env",
        env_nested_delimiter="__",
        pyproject_toml_table_header=("tool", "ril"),
        toml_file="ril.toml",
        extra="ignore",
    )

    fontawesome: FontAwesomeSettings = Field(default_factory=FontAwesomeSettings)
    simple: SimpleIconsSettings = Field(default_factory=SimpleIconsSettings)
    phosphor: PhosphorSettings = Field(default_factory=PhosphorSettings)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            dotenv_settings,
            PyprojectTomlConfigSettingsSource(settings_cls),
            TomlConfigSettingsSource(settings_cls),
        )


settings = RILSettings()

# This just needs to be initialized.
FontAwesomePackageTokenSetting()
