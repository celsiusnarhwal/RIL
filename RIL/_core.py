import copy
import importlib.metadata
import typing as t

import pydantic.v1
import reflex as rx
import reflex.utils.prerequisites as rxp
import semver
from loguru import logger
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_serializer,
    validate_call,
)
from reflex.components.component import T

from RIL.plugins import SVGRPlugin


class Props(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs):
        return super().model_dump(**kwargs, exclude_none=True, by_alias=True)

    @model_serializer(mode="wrap")
    def serialize(self, handler: t.Callable):
        serialized = handler(self)
        reserialized = copy.deepcopy(serialized)

        return reserialized


class Base(rx.Component):
    """
    Base class for all components in this library.
    """

    @classmethod
    @validate_call
    def _reproduce(
        cls,
        *,
        props_to_override: t.Annotated[dict | Props, Field(default_factory=dict)],
        lib_dependencies: t.Annotated[list[str], Field(default_factory=list)],
    ):
        if isinstance(props_to_override, Props):
            props_to_override = props_to_override.model_dump()

        if semver.Version.parse(importlib.metadata.version("reflex")) < "0.7.13":
            logger.warning(
                "Support for your version of Reflex is deprecated and will be removed in RIL 2.0.0. "
                "Please upgrade to the latest versions of Reflex and RIL."
            )
            for field in rx.Component.get_fields():
                props_to_override.pop(field, None)

            model = pydantic.v1.create_model(
                cls.__name__,
                __base__=cls,
                lib_dependencies=(list[str], lib_dependencies),
                **{k: (rx.Var[t.Any], v) for k, v in props_to_override.items()},
            )

            return model
        else:
            if isinstance(cls.lib_dependencies, list):
                lib_dependencies += cls.lib_dependencies

            return type(
                cls.__name__,
                (cls,),
                {
                    "__module__": __name__,
                    "custom_attrs": props_to_override,
                    "lib_dependencies": lib_dependencies,
                },
            )


class SVGComponent(Base):
    """
    Base class for components that require @svgr/webpack.
    """

    @classmethod
    def create(cls: type[T], *children, **props) -> T:
        from reflex.config import get_config

        if not any((isinstance(plugin, SVGRPlugin) for plugin in get_config().plugins)):
            raise ValueError(
                f"You must add the Reflex Icon Library's SVGR plugin (RIL.plugins.SVGRPlugin) to your "
                f"rxconfig.py to use {cls.__name__}."
            )

        if not rxp.environment.REFLEX_USE_TURBOPACK.get():
            raise ValueError(f"Turbopack is required to use {cls.__name__}")

        return super().create(*children, **props)


def validate_props(func):
    def wrapper(*args, **props):
        return validate_call(func)(*args, props=props)

    return wrapper
