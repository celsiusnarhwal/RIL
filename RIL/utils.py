import typing as t

import reflex.utils.prerequisites as rxp
from decorator import decorator
from yarl import URL

from RIL._core import Base


def docs(path: str = "") -> URL:
    return URL("https://ril.celsiusnarhwal.dev").with_path(path, encoded=True)


# noinspection PyUnusedLocal
@decorator
def require_turbopack(func: t.Callable, cls: type[Base], *args, **kwargs):
    if not rxp.environment.REFLEX_USE_TURBOPACK.get():
        raise ValueError(f"Turbopack is required to use {cls.__name__}")

    return func(cls, *args, **kwargs)
