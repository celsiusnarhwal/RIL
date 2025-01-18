import typing as t

import reflex as rx

from RIL._core import Base

class PhosphorIcon(Base):
    @classmethod
    def create(
        cls,
        icon: str,
        weight: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = None,
        color: str | tuple = None,
        size: int | str = None,
        alt: str = None,
        **kwargs,
    ) -> rx.Component:
        """
        Create a Phosphor icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        weight : typing.Literal["thin", "light", "regular", "bold", "fill", "duotone"], optional
            The icon's weight (i.e., style).

        color : str | tuple, optional
            The color of the icon. May be:
            - a hex code
            - a tuple of RGB, RGBA, or HSL values
            - any valid color name as determined by the CSS Color Module Level 3 specification
            (https://www.w3.org/TR/css-color-3/#svg-color)

            Hex codes are case-insensitive and the leading `#` is optional.

        size : int | str, optional
            The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).

        alt : str, optional
            Alt text for the icon.
        """

class PhosphorIconContext(Base):
    @classmethod
    def create(
        cls,
        weight: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = None,
        color: str | tuple = None,
        size: int | str = None,
    ) -> rx.Component:
        """
        Create a container that applies a set of default styling properties to all Phosphor icons within it.

        Parameters
        ----------
        weight : {"thin", "light", "regular", "bold", "fill", "duotone"}, optional
            The weight of the icons. (i.e., style).

        color : str | tuple, optional
            The color of the icons. May be:
            - a hex code (e.g., `"#03cb98"`)
            - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
            - any valid color name as determined by the CSS Color Module Level 3 specification
            (https://www.w3.org/TR/css-color-3/#svg-color)

            Hex codes are case-insensitive and the leading `#` is optional.

        size : int | str, optional
            The size of the icons. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
        """

class Phosphor(rx.ComponentNamespace):
    context = staticmethod(PhosphorIconContext.create)

    @staticmethod
    def __call__(
        icon: str,
        weight: t.Literal["thin", "light", "regular", "bold", "fill", "duotone"] = None,
        color: str | tuple = None,
        size: int | str = None,
        alt: str = None,
    ) -> rx.Component:
        """
        Create a Phosphor icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        weight : typing.Literal["thin", "light", "regular", "bold", "fill", "duotone"], optional
            The icon's weight (i.e., style).

        color : str | tuple, optional
            The color of the icon. May be:
            - a hex code (e.g., `"#03cb98"`)
            - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
            - any valid color name as determined by the CSS Color Module Level 3 specification
            (https://www.w3.org/TR/css-color-3/#svg-color)

            Hex codes are case-insensitive and the leading `#` is optional.

        size : int | str, optional
            The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).

        alt : str, optional
            Alt text for the icon.
        """

phosphor = Phosphor()
