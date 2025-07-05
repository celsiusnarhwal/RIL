import hashlib
from typing import Unpack

import reflex as rx
from reflex.plugins import CommonContext, Plugin, PreCompileContext
from reflex.utils.path_ops import cp as copy_file
from reflex.utils.prerequisites import get_web_dir

from RIL import templates

__all__ = ["SVGRPlugin"]


def _update_vite_config():
    reflex_vite_configs = {
        "source": rx.constants.Templates.Dirs.WEB_TEMPLATE / "vite.config.js",
        "destination": get_web_dir() / "vite.reflex.config.js",
    }

    ril_vite_configs = {
        "source": templates.directory / "vite.config.js",
        "destination": get_web_dir() / "vite.config.js",
    }

    for config_set in [reflex_vite_configs, ril_vite_configs]:
        src_hash = hashlib.sha256(config_set["source"].read_bytes()).hexdigest()

        if config_set["destination"].exists():
            dst_hash = hashlib.sha256(
                config_set["destination"].read_bytes()
            ).hexdigest()
        else:
            dst_hash = None

        if src_hash != dst_hash:
            copy_file(config_set["source"], config_set["destination"])


class SVGRPlugin(Plugin):
    def get_frontend_development_dependencies(
        self, **context: Unpack[CommonContext]
    ) -> list[str] | set[str] | tuple[str, ...]:
        return ["vite-plugin-svgr"]

    def pre_compile(self, **context: Unpack[PreCompileContext]) -> None:
        context["add_save_task"](_update_vite_config)
