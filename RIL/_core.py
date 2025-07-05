import typing as t

import reflex as rx
from pydantic import (
    BaseModel,
    ConfigDict,
    GetCoreSchemaHandler,
    PlainSerializer,
    validate_call,
)
from pydantic_core import core_schema
from pydantic_extra_types.color import Color as PydanticColor
from reflex import ImportDict
from reflex.constants.colors import Color as ReflexColor

from RIL.plugins import SVGRPlugin


class Base(rx.Component):
    """
    Base class for all components in this library.
    """

    if t.TYPE_CHECKING:
        imports: dict | None

    def add_imports(self) -> ImportDict | list[ImportDict]:
        return getattr(self, "imports", {}) or {}


class SVGComponent(Base):
    """
    Base class for components that require @svgr/webpack.
    """

    @classmethod
    def create(cls, *children, **props):
        from reflex.config import get_config

        if not any((type(plugin) is SVGRPlugin for plugin in get_config().plugins)):
            raise ValueError(
                f"You must add the Reflex Icon Library's SVGR plugin (RIL.plugins.SVGRPlugin) to your "
                f"rxconfig.py to use {cls.__name__}."
            )

        return super().create(*children, **props)


class Props(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs):
        return super().model_dump(**kwargs, exclude_none=True, by_alias=True)


class _ReflexColorPydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: t.Any, _handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.is_instance_schema(ReflexColor)


Color = t.Annotated[
    PydanticColor | t.Annotated[ReflexColor, _ReflexColorPydanticAnnotation],
    PlainSerializer(
        lambda v: v.as_hex() if isinstance(v, PydanticColor) else format(v)
    ),
]


def validate_props(func):
    def wrapper(*args, **props):
        return validate_call(func)(*args, props=props)

    return wrapper
