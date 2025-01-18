"""
A Reflex component providing access to GitHub's Octicons.

https://ril.celsiusnarhwal.dev/octicons
"""

import typing as t

from RIL._core import Base

__all__ = ["octicons"]

class Octicon(Base):
    @classmethod
    def create(
        cls,
        icon: str,
        color: str | tuple = None,
        size: int | str | t.Literal["small", "medium", "large"] = None,
        **kwargs,
    ):
        """
        Create an Octicon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        color : str | tuple, optional
            The color of the icon. May be:
            - a hex code (e.g., `"#03cb98"`)
            - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
            - any valid color name as determined by the CSS Color Module Level 3 specification
            (https://www.w3.org/TR/css-color-3/#svg-color)

            Hex codes are case-insensitive and the leading `#` is optional.

        size : int | str | {"small", "medium", "large"}, optional
            The size of the icon. May be `"small"`, `"medium"`, or `"large"`. May also be an integer (in pixels) or
            a CSS size string (e.g., `'1rem'`).
        """

octicons = Octicon.create
