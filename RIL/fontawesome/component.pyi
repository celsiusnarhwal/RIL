import typing as t

import reflex as rx

from RIL._core import Base

class FontAwesomeIcon(Base):
    @classmethod
    def _get_package_for_style(cls, style: str) -> str: ...
    @classmethod
    def _normalize_icon_name(cls, icon_name: str) -> str: ...
    @classmethod
    def _get_icon_alias(cls, icon_name: str, icon_style: str) -> str: ...
    @classmethod
    def create(
        cls,
        icon: str,
        size: t.Literal[
            "2xs",
            "xs",
            "sm",
            "lg",
            "xl",
            "2xl",
            "1x",
            "2x",
            "3x",
            "4x",
            "5x",
            "6x",
            "7x",
            "8x",
            "9x",
            "10x",
        ] = None,
        fixed_width: bool = None,
        list_item: bool = None,
        rotation: t.Literal[90, 180, 270] = None,
        flip: t.Literal["horizontal", "vertical", "both"] = None,
        animation: str = None,
        border: bool = None,
        pull: t.Literal["left", "right"] = None,
        transform: str = None,
        mask: FontAwesomeIcon = None,
        swap_opacity: bool = None,
        inverse: bool = None,
        **kwargs,
    ) -> None:
        """
        Create a FontAwesome icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        size : {"2xs", "xs", "sm", "lg", "xl", "2xl", "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"}, optional
            The size of the icon.

        fixed_width : bool, optional
            Whether the icon should have a fixed width.

        list_item : bool, optional
            Whether the icon should be displayed as a list item.

        rotation : {90, 180, 270}, optional
            The icon's angle of rotation.

        flip : {"horizontal", "vertical", "both"}, optional
            How the icon should be flipped.

        animation : str, optional
            An animation to apply to the icon.
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        border : bool, optional
            Whether to add a border around the icon.

        pull : {"left", "right"}, optional
            Pull the icon to the left or right. Useful for wrapping text around an icon.

        transform : str, optional
            A space-separated list of transforms to apply to the icon (e.g., `"shrink-6 left-4 rotate-42"`).
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        mask : FontAwesomeIcon, optional
            Another icon to mask this one with. This must be a `FontAwesomeIcon` component, not simply the name of an icon.
            Styling options passed to the masking icon will have no effect.

        swap_opacity : bool, optional
            If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.

        inverse : bool, optional
            Whether to invert the icon's colors.
        """

class FontAwesomeSharp(rx.ComponentNamespace):
    solid = regular = light = thin = FontAwesomeIcon.create

    @staticmethod
    def __call__(
        icon: str,
        size: t.Literal[
            "2xs",
            "xs",
            "sm",
            "lg",
            "xl",
            "2xl",
            "1x",
            "2x",
            "3x",
            "4x",
            "5x",
            "6x",
            "7x",
            "8x",
            "9x",
            "10x",
        ] = None,
        fixed_width: bool = None,
        list_item: bool = None,
        rotation: t.Literal[90, 180, 270] = None,
        flip: t.Literal["horizontal", "vertical", "both"] = None,
        animation: str = None,
        border: bool = None,
        pull: t.Literal["left", "right"] = None,
        transform: str = None,
        mask: FontAwesomeIcon = None,
        swap_opacity: bool = None,
        inverse: bool = None,
        **kwargs,
    ) -> None:
        """
        Create a FontAwesome icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        size : {"2xs", "xs", "sm", "lg", "xl", "2xl", "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"}, optional
            The size of the icon.

        fixed_width : bool, optional
            Whether the icon should have a fixed width.

        list_item : bool, optional
            Whether the icon should be displayed as a list item.

        rotation : {90, 180, 270}, optional
            The icon's angle of rotation.

        flip : {"horizontal", "vertical", "both"}, optional
            How the icon should be flipped.

        animation : str, optional
            An animation to apply to the icon.
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        border : bool, optional
            Whether to add a border around the icon.

        pull : {"left", "right"}, optional
            Pull the icon to the left or right. Useful for wrapping text around an icon.

        transform : str, optional
            A space-separated list of transforms to apply to the icon (e.g., `"shrink-6 left-4 rotate-42"`).
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        mask : FontAwesomeIcon, optional
            Another icon to mask this one with. This must be a `FontAwesomeIcon` component, not simply the name of an icon.
            Styling options passed to the masking icon will have no effect.

        swap_opacity : bool, optional
            If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.

        inverse : bool, optional
            Whether to invert the icon's colors.
        """

class FontAwesomeDuotone(rx.ComponentNamespace):
    solid = regular = light = thin = FontAwesomeIcon.create

    @staticmethod
    def __call__(
        icon: str,
        size: t.Literal[
            "2xs",
            "xs",
            "sm",
            "lg",
            "xl",
            "2xl",
            "1x",
            "2x",
            "3x",
            "4x",
            "5x",
            "6x",
            "7x",
            "8x",
            "9x",
            "10x",
        ] = None,
        fixed_width: bool = None,
        list_item: bool = None,
        rotation: t.Literal[90, 180, 270] = None,
        flip: t.Literal["horizontal", "vertical", "both"] = None,
        animation: str = None,
        border: bool = None,
        pull: t.Literal["left", "right"] = None,
        transform: str = None,
        mask: FontAwesomeIcon = None,
        swap_opacity: bool = None,
        inverse: bool = None,
        **kwargs,
    ) -> None:
        """
        Create a FontAwesome icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        size : {"2xs", "xs", "sm", "lg", "xl", "2xl", "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"}, optional
            The size of the icon.

        fixed_width : bool, optional
            Whether the icon should have a fixed width.

        list_item : bool, optional
            Whether the icon should be displayed as a list item.

        rotation : {90, 180, 270}, optional
            The icon's angle of rotation.

        flip : {"horizontal", "vertical", "both"}, optional
            How the icon should be flipped.

        animation : str, optional
            An animation to apply to the icon.
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        border : bool, optional
            Whether to add a border around the icon.

        pull : {"left", "right"}, optional
            Pull the icon to the left or right. Useful for wrapping text around an icon.

        transform : str, optional
            A space-separated list of transforms to apply to the icon (e.g., `"shrink-6 left-4 rotate-42"`).
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        mask : FontAwesomeIcon, optional
            Another icon to mask this one with. This must be a `FontAwesomeIcon` component, not simply the name of an icon.
            Styling options passed to the masking icon will have no effect.

        swap_opacity : bool, optional
            If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.

        inverse : bool, optional
            Whether to invert the icon's colors.
        """

class FontAwesomeSharpDuotone(rx.ComponentNamespace):
    solid = regular = light = thin = FontAwesomeIcon.create

    @staticmethod
    def __call__(
        icon: str,
        size: t.Literal[
            "2xs",
            "xs",
            "sm",
            "lg",
            "xl",
            "2xl",
            "1x",
            "2x",
            "3x",
            "4x",
            "5x",
            "6x",
            "7x",
            "8x",
            "9x",
            "10x",
        ] = None,
        fixed_width: bool = None,
        list_item: bool = None,
        rotation: t.Literal[90, 180, 270] = None,
        flip: t.Literal["horizontal", "vertical", "both"] = None,
        animation: str = None,
        border: bool = None,
        pull: t.Literal["left", "right"] = None,
        transform: str = None,
        mask: FontAwesomeIcon = None,
        swap_opacity: bool = None,
        inverse: bool = None,
        **kwargs,
    ) -> None:
        """
        Create a FontAwesome icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        size : {"2xs", "xs", "sm", "lg", "xl", "2xl", "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"}, optional
            The size of the icon.

        fixed_width : bool, optional
            Whether the icon should have a fixed width.

        list_item : bool, optional
            Whether the icon should be displayed as a list item.

        rotation : {90, 180, 270}, optional
            The icon's angle of rotation.

        flip : {"horizontal", "vertical", "both"}, optional
            How the icon should be flipped.

        animation : str, optional
            An animation to apply to the icon.
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        border : bool, optional
            Whether to add a border around the icon.

        pull : {"left", "right"}, optional
            Pull the icon to the left or right. Useful for wrapping text around an icon.

        transform : str, optional
            A space-separated list of transforms to apply to the icon (e.g., `"shrink-6 left-4 rotate-42"`).
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        mask : FontAwesomeIcon, optional
            Another icon to mask this one with. This must be a `FontAwesomeIcon` component, not simply the name of an icon.
            Styling options passed to the masking icon will have no effect.

        swap_opacity : bool, optional
            If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.

        inverse : bool, optional
            Whether to invert the icon's colors.
        """

class FontAwesome(rx.ComponentNamespace):
    solid = regular = light = thin = brands = kit = FontAwesomeIcon.create
    sharp = FontAwesomeSharp()
    duotone = FontAwesomeDuotone()
    sharp_duotone = FontAwesomeSharpDuotone()

    @staticmethod
    def __call__(
        icon: str,
        size: t.Literal[
            "2xs",
            "xs",
            "sm",
            "lg",
            "xl",
            "2xl",
            "1x",
            "2x",
            "3x",
            "4x",
            "5x",
            "6x",
            "7x",
            "8x",
            "9x",
            "10x",
        ] = None,
        fixed_width: bool = None,
        list_item: bool = None,
        rotation: t.Literal[90, 180, 270] = None,
        flip: t.Literal["horizontal", "vertical", "both"] = None,
        animation: str = None,
        border: bool = None,
        pull: t.Literal["left", "right"] = None,
        transform: str = None,
        mask: FontAwesomeIcon = None,
        swap_opacity: bool = None,
        inverse: bool = None,
        **kwargs,
    ) -> None:
        """
        Create a FontAwesome icon.

        Parameters
        ----------
        icon : str
            The name of the icon.

        size : {"2xs", "xs", "sm", "lg", "xl", "2xl", "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"}, optional
            The size of the icon.

        fixed_width : bool, optional
            Whether the icon should have a fixed width.

        list_item : bool, optional
            Whether the icon should be displayed as a list item.

        rotation : {90, 180, 270}, optional
            The icon's angle of rotation.

        flip : {"horizontal", "vertical", "both"}, optional
            How the icon should be flipped.

        animation : str, optional
            An animation to apply to the icon.
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        border : bool, optional
            Whether to add a border around the icon.

        pull : {"left", "right"}, optional
            Pull the icon to the left or right. Useful for wrapping text around an icon.

        transform : str, optional
            A space-separated list of transforms to apply to the icon (e.g., `"shrink-6 left-4 rotate-42"`).
            For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons

        mask : FontAwesomeIcon, optional
            Another icon to mask this one with. This must be a `FontAwesomeIcon` component, not simply the name of an icon.
            Styling options passed to the masking icon will have no effect.

        swap_opacity : bool, optional
            If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.

        inverse : bool, optional
            Whether to invert the icon's colors.
        """

fontawesome = fa = FontAwesome()
