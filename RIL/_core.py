import copy
import importlib.metadata
import sys
import typing as t

import pydantic.v1
import reflex as rx
import semver
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, model_serializer, validate_call


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
            return type(
                cls.__name__,
                (cls,),
                {
                    "__module__": __name__,
                    "custom_attrs": props_to_override,
                    "lib_dependencies": lib_dependencies,
                },
            )


def validate_props(func):
    def wrapper(*args, **props):
        return validate_call(func)(*args, props=props)

    return wrapper


log_level = rx.config.get_config().loglevel

if log_level.casefold() == "default":
    log_level = "warning"

logger.remove()
logger.add(sink=sys.stderr, level=log_level.upper(), colorize=True)
