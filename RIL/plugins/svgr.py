import string
from typing import Unpack

import json5 as json
from reflex.plugins import CommonContext, Plugin, PreCompileContext

__all__ = ["SVGRPlugin"]


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


class SVGRPlugin(Plugin):
    def get_frontend_development_dependencies(
        self, **context: Unpack[CommonContext]
    ) -> list[str] | set[str] | tuple[str, ...]:
        return ["@svgr/webpack"]

    def pre_compile(self, **context: Unpack[PreCompileContext]) -> None:
        context["add_modify_task"]("next.config.js", _update_next_config)
