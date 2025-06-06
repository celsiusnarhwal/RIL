import re
from typing import Unpack

import json5 as json
from deepmerge import always_merger
from reflex.plugins import CommonContext, Plugin, PreCompileContext

__all__ = ["SVGRPlugin"]


def _update_next_config(next_config_content: str):
    next_config = json.loads(
        re.search("{.*}", next_config_content, flags=re.DOTALL).group(0)
    )

    loader_config = {
        "loaders": [
            {
                "loader": "@svgr/webpack",
                "options": {"dimensions": False, "titleProp": True},
            }
        ],
        "as": "*.js",
    }

    turbopack_config = {
        "turbopack": {
            "rules": {
                "**/node_modules/@material-symbols/svg-*/**/*.svg": loader_config,
                "**/node_modules/bootstrap-icons/icons/*.svg": loader_config,
            }
        }
    }

    always_merger.merge(next_config, turbopack_config)

    return f"module.exports = {json.dumps(next_config)}"


class SVGRPlugin(Plugin):
    def get_frontend_development_dependencies(
        self, **context: Unpack[CommonContext]
    ) -> list[str] | set[str] | tuple[str, ...]:
        return ["@svgr/webpack"]

    def pre_compile(self, **context: Unpack[PreCompileContext]) -> None:
        context["add_modify_task"]("next.config.js", _update_next_config)
