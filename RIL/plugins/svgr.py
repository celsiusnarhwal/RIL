import json5
from json5 import QuoteStyle
from pydantic import ConfigDict, validate_call
from vite_config_plugin import RawJS, ViteConfigPlugin

__all__ = ["SVGRPlugin"]


class SVGRPlugin(ViteConfigPlugin):
    """
    Enables SVGs from certain icon libraries to be imported as React components.
    """

    def __init__(self, **_kwargs):
        options = {
            "svgrOptions": {
                "titleProp": True,
                "dimensions": False,
            },
            "include": [
                "**/node_modules/@material-symbols/svg-*/**/*.svg",
                "**/node_modules/bootstrap-icons/icons/*.svg",
            ],
        }

        config = {
            "plugins": [
                RawJS(
                    f"svgr({json5.dumps(options, quote_style=QuoteStyle.ALWAYS_SINGLE)})"
                )
            ]
        }
        imports = ["import svgr from 'vite-plugin-svgr';"]
        dependencies = ["vite-plugin-svgr"]

        _kwargs = {
            "config": config,
            "imports": imports,
            "dependencies": dependencies,
            **_kwargs,
        }

        super().__init__(**_kwargs)

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def __add__(self, other: ViteConfigPlugin):
        return SVGRPlugin(
            config=self.config,
            imports=self.imports + other.imports,
            dependencies=self.dependencies + other.dependencies,
            extra_configs=[other.config, *other.extra_configs, *self.extra_configs],
        )

    __radd__ = __add__
