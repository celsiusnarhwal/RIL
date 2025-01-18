import typing as t

from RIL._core import Base

class MaterialSymbol(Base):
    @classmethod
    def create(
        cls,
        icon: str,
        variant: t.Literal["outlined", "rounded", "sharp"] = None,
        filled: bool = None,
        color: str | tuple = None,
        size: int | str = None,
        **kwargs,
    ):
        """
        Create a Material Symbol.

        Parameters
        ----------
        icon : str
            The name of the icon.

        variant : {"outlined", "rounded", "sharp"}, optional
            The variant of the icon.

        filled : bool, optional
            Whether or not to use the icon's filled appearance.

        color : str | tuple, optional
            The color of the icon. May be:
            - a hex code (e.g., `"#03cb98"`)
            - a integer tuple of RGB values, with an optional fourth value for transparency (e.g., `(3, 203, 152, 1)`)
            - any valid color name as determined by the CSS Color Module Level 3 specification
            (https://www.w3.org/TR/css-color-3/#svg-color)

            Hex codes are case-insensitive and the leading `#` is optional.

        size : int | str, optional
            The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).

        Returns
        -------

        """

material = MaterialSymbol.create
