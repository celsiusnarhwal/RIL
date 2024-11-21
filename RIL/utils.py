import typing as t
from types import GenericAlias

from pydantic import TypeAdapter


def is_instance(obj: t.Any, tp: t.Any | GenericAlias, **config) -> bool:
    """
    A more powerful substitute for the built-in `isinstance` that can compare against generic types and aliases.
    """
    try:
        TypeAdapter(tp, config=dict(**config, strict=True)).validate_python(obj)
    except ValueError:
        return False

    return True