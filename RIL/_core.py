import copy
import sys
import typing as t

import pydantic
import pydantic.v1
import reflex as rx
from loguru import logger
from pydantic import BaseModel, ConfigDict, model_serializer, validate_call


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
    def _reproduce(cls, *, props: dict = None, **fields):
        props = props or {}

        # Futureproofing for Reflex's planned move to Pydantic v2. https://github.com/reflex-dev/reflex/issues/1539
        if issubclass(cls, pydantic.v1.BaseModel):
            create_model = pydantic.v1.create_model
        else:
            create_model = pydantic.create_model

        if isinstance(props, Props):
            props = props.model_dump()

        for field in rx.Component.get_fields():
            props.pop(field, None)

        model = create_model(
            cls.__name__,
            __base__=cls,
            **{k: (rx.Var[t.Any], v) for k, v in props.items()},
            **fields,
        )

        return model


def validate_props(func):
    def wrapper(*args, **props):
        return validate_call(func)(*args, props=props)

    return wrapper


log_level = rx.config.get_config().loglevel

if log_level.casefold() == "default":
    log_level = "warning"

logger.remove()
logger.add(sink=sys.stderr, level=log_level.upper(), colorize=True)
