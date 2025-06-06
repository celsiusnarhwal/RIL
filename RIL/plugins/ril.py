import string
import sys
from typing import Unpack

import json5 as json
from loguru import logger
from reflex.plugins import CommonContext, Plugin, PreCompileContext

__all__ = ["RILPlugin"]


def _configure_logging():
    from reflex.config import get_config

    log_level = get_config().loglevel

    if log_level.casefold() == "default":
        log_level = "warning"

    logger.remove()
    logger.add(
        sink=sys.stderr,
        level=log_level.upper(),
        colorize=True,
        format="<lvl>[Reflex Icon Library] {level}: {message}</>",
    )


def _update_next_config(next_config_contant: str):
    next_config = json.loads(
        next_config_contant.lstrip(string.printable.replace("{", "")).rstrip(";")
    )

    next_config.update(
        {
            "turbopack": {
                "rules": {
                    "*.svg": {
                        "loaders": [
                            {
                                "loader": "@svgr/webpack",
                                "options": {"dimensions": False, "titleProp": True},
                            }
                        ],
                        "as": "*.js",
                    }
                }
            }
        }
    )

    return f"module.exports = {json.dumps(next_config)}"


class RILPlugin(Plugin):
    def get_frontend_development_dependencies(
        self, **context: Unpack[CommonContext]
    ) -> list[str] | set[str] | tuple[str, ...]:
        return ["@svgr/webpack"]

    def pre_compile(self, **context: Unpack[PreCompileContext]) -> None:
        context["add_save_task"](_configure_logging)
        context["add_modify_task"]("next.config.js", _update_next_config)
