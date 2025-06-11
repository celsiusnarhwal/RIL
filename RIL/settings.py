import os
import typing as t
from pathlib import Path

import reflex.utils.prerequisites as rxp
from jinja2 import Environment, FileSystemLoader
from pydantic import (
    AnyHttpUrl,
    BaseModel,
    Field,
    field_validator,
    model_validator,
)
from pydantic_extra_types.color import Color
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

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
        if self.pro_enabled and self.kit_code:
            return f"@awesome.me/kit-{self.kit_code}"

    @model_validator(mode="after")
    def write_npmrc(self):
        """
        Write Font Awesome Pro-specific configuration to .npmrc as needed.
        """
        rxp.initialize_npmrc()

        if self.pro_enabled:
            npmrc_template = jinja.get_template(".npmrc.jinja")
            reference_npmrc = npmrc_template.render(registry=self.npm_registry)

            rxp.get_web_dir().joinpath(".npmrc").open("a").write("\n" + reference_npmrc)

        return self


class SimpleIconsSettings(BaseModel):
    """
    Settings for RIL's Simple Icons component.
    """

    version: int | t.Literal["latest"] = Field("latest", ge=5)

    @field_validator("version")
    def validate_version(cls, v):
        if isinstance(v, int) and not v >= 5:
            raise ValueError("Simple Icons version must be greater than or equal to 5")

        return v


class PhosphorSettings(BaseModel):
    """
    Settings for RIL's Phosphor Icons component.
    """

    color: Color = None
    size: int | str = "1em"
    variant: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = (
        "regular"
    )

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

    # @model_validator(mode="after")
    # def configure_logging(self) -> t.Self:
    #     log_level = rx.config.get_config().loglevel
    #
    #     if log_level.casefold() == "default":
    #         log_level = "warning"
    #
    #     logger.remove()
    #     logger.add(
    #         sink=sys.stderr,
    #         level="WARNING",
    #         colorize=True,
    #         format="<lvl>[Reflex Icon Library] {level}: {message}</>",
    #     )
    #
    #     return self

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
