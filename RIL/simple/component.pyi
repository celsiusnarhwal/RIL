from RIL._core import Base

class SimpleIcon(Base):
    @classmethod
    def create(
        cls,
        icon: str,
        title: str = None,
        color: str | tuple = None,
        size: str | int = None,
    ):
        """
        Create a Simple Icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        title : str, optional
         A short, accessible, description of the icon.

        color : str | tuple, optional
            The color of this icon. May be:
            - a hex code
            - a tuple of RGB, RGBA or HSL values
            - `"default"`, which makes the icon use whatever color Simple Icons has chosen as its default
            - any valid color name as determined by the CSS Color Module Level 3 specification

            Hex codes are case-insensitive and the leading `#` is optional..

        size : str | int, optional
            The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `'1rem'`).
        """

simple = SimpleIcon.create
si = simple
