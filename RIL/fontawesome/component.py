import copy
import typing as t
from functools import partial

import casefy
import reflex as rx
from deepmerge import always_merger
from reflex.utils.imports import ImportDict

from RIL import utils
from RIL._core import Base
from RIL.settings import settings

__all__ = ["fontawesome", "fa"]


class FontAwesomeIcon(Base):
    library = "@fortawesome/react-fontawesome"
    tag = "FontAwesomeIcon"

    icon: rx.Var[str]
    """
    The name of the icon.
    """

    size: rx.Var[
        t.Literal[
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
        ]
    ]
    """
    The size of the icon.
    """

    fixed_width: rx.Var[bool]
    """
    Whether the icon should have fixed with.
    """

    list_item: rx.Var[bool]
    """
    Whether the icon should be displayed as a list item.
    """

    rotation: rx.Var[t.Literal[90, 180, 270]]
    """
    The icon's angle of rotation.
    """

    flip: rx.Var[t.Literal["horizontal", "vertical", "both"]]
    """
    How the icon should be flipped.
    """

    animation: rx.Var[str]
    """
    An animation to apply to the icon.

    For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons
    """

    border: rx.Var[bool]
    """
    Whether to add a border around the icon.
    """

    pull: rx.Var[t.Literal["left", "right"]]
    """
    Pull the icon to the left or right. Useful for wrapping text around an icon.
    """

    transform: rx.Var[str]
    """
    A space-separated list of transforms to apply to the icon. (e.g., "shrink-6 left-4 rotate-42").

    For possible values, see: https://docs.fontawesome.com/web/use-with/react/style#animate-icons
    """

    mask: rx.Var["FontAwesomeIcon"]
    """
    Another icon to mask this one with. This must be a `FontAwesomeIcon` component, and not simply the name of an icon.
    Styling options passed to the masking icon will have no effect.
    """

    swap_opacity: rx.Var[bool]
    """
    If this is a duotone icon, whether to swap the opacity of its layers. Has no effect on non-duotone icons.
    """

    inverse: rx.Var[bool]
    """
    Whether to invert the icon's colors.
    """

    def add_imports(self, **imports) -> ImportDict | list[ImportDict]:
        return imports

    @classmethod
    def _get_package_for_style(cls, style: str) -> str:
        # If a Kit exists, we use it.
        if settings.fontawesome.kit_package:
            # For custom icons, the module path is "kit/custom".
            if style == "kit":
                module_path = "kit/custom"
            else:
                # The module path is determined by replacing the last hyphen (-) in a style's name
                # with a forward slash (/) (e.g., "sharp-duotone-solid" becomes "sharp-duotone/solid"). We do this
                # by reversing the style name, replacing the *first* hyphen in the reversed string, and then
                # re-reversing the result.
                module_path = style[::-1].replace("-", "/", 1)[::-1]

            return f"{settings.fontawesome.kit_package}/icons/{module_path}"

        # At this point, we know we aren't using a Kit, so we need to figure out what package
        # we *are* using.

        # Since we're not using a Kit, custom icons should raise a `ValueError`.
        if style == "kit":
            raise ValueError(
                f"Additional configuration is required to use custom Font Awesome icons. "
                f"{utils.docs('fontawesome/pro/#using-a-kit')}"
            )

        # Brand icons always use @fortawesome/free-brands-svg-icons.
        if style == "classic-brands":
            return "@fortawesome/free-brands-svg-icons"

        # If Font Awesome Pro is enabled, we use the appropriate Pro package.
        if settings.fontawesome.pro_enabled:
            # Duotone Solid is currently a special case.
            if style == "duotone-solid":
                return "@fortawesome/pro-duotone-svg-icons"

            # Classic styles need to be prefixed with "pro-" to get the package name.
            style = style.replace("classic-", "pro-", 1)

            return f"@fortawesome/{style}-svg-icons"

        # If we still haven't returned, our only remaining options are the free Classic Solid and
        # Classic Regular packages.

        if style == "classic-solid":
            return "@fortawesome/free-solid-svg-icons"

        if style == "classic-regular":
            return "@fortawesome/free-regular-svg-icons"

        # Only thing left to do at this point is raise an exception.
        raise ValueError(
            f"The {' '.join(style.split('-')).title()} style requires Font Awesome Pro. {utils.docs('fontawesome/pro')}"
        )

    @classmethod
    def _normalize_icon_name(cls, icon_name: str) -> str:
        return "fa" + "".join(
            [i.capitalize() for i in icon_name.removeprefix("fa-").split("-")]
        )

    @classmethod
    def _get_icon_alias(cls, icon_name: str, icon_style: str) -> str:
        return (
            "fa"
            + casefy.pascalcase(icon_style)
            + cls._normalize_icon_name(icon_name).removeprefix("fa")
        )

    @classmethod
    def create(cls, icon: str = None, _icon_style: str = None, **props) -> t.Self:
        props_to_override = {}

        # The icon name is normalized to fa{Icon} and given an alias to avoid
        # collisions with any sister icons in different styles.

        tag = cls._normalize_icon_name(icon)
        alias = cls._get_icon_alias(icon, _icon_style)

        # Determine the package this icon should be imported from.
        package = cls._get_package_for_style(_icon_style)

        props["icon"] = rx.Var(alias)

        # The component will depend on @fortawesome/fontawesome-svg-core and the Kit package (if a Kit exists)
        # or the appropriate @fortawesome package (if no Kit exists).

        if settings.fontawesome.kit_package:
            second_dependency = f"{settings.fontawesome.kit_package}@latest"
        else:
            second_dependency = f"{package}@^6"

        lib_dependencies = [
            "@fortawesome/fontawesome-svg-core@^6",
            second_dependency,
        ]

        # The component needs to import the icon from the appropriate package.
        imports = {package: [rx.ImportVar(tag, alias=alias, install=False)]}

        # The `animation` prop is applied as a boolean prop of the animation's name.
        animation = props.get("animation")
        if isinstance(animation, str):
            props.pop("animation")
            props_to_override.update(
                {animation: (bool, True) for animation in animation.split(" ")}
            )

        # If a mask was provided, we need to combine the component's dependencies and imports with those
        # of the mask.
        mask = props.get("mask")
        if isinstance(mask, cls):
            props.pop("mask")
            lib_dependencies.extend(mask.lib_dependencies)
            # noinspection PyArgumentList
            imports = always_merger.merge(
                copy.deepcopy(imports), mask.add_imports(mask)
            )

            # The actual value of the mask prop is the raw JSX reference to the masking icon.
            props_to_override["mask"] = mask.icon
        elif mask is not None:
            raise TypeError(
                f"The mask of a Font Awesome icon must be another Font Awesome icon and not {type(mask)}"
            )

        # We create a new component class as a subclass of this one, overriding props as necessary.
        component_model = cls._reproduce(
            props_to_override=props_to_override,
            lib_dependencies=lib_dependencies,
        )

        # We override `add_imports` to import the icon.
        component_model.add_imports = partial(component_model.add_imports, **imports)

        # Finally, we return an instance of the new component class.
        return super(cls, component_model).create(**props)


class FontAwesomeSharp(rx.ComponentNamespace):
    solid = __call__ = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="sharp-solid"
    )
    regular = partial(staticmethod(FontAwesomeIcon.create), _icon_style="sharp-regular")
    light = partial(staticmethod(FontAwesomeIcon.create), _icon_style="sharp-light")
    thin = partial(staticmethod(FontAwesomeIcon.create), _icon_style="sharp-thin")


class FontAwesomeDuotone(rx.ComponentNamespace):
    solid = __call__ = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="duotone-solid"
    )
    regular = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="duotone-regular"
    )
    light = partial(staticmethod(FontAwesomeIcon.create), _icon_style="duotone-light")
    thin = partial(staticmethod(FontAwesomeIcon.create), _icon_style="duotone-thin")


class FontAwesomeSharpDuotone(rx.ComponentNamespace):
    solid = __call__ = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="sharp-duotone-solid"
    )
    regular = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="sharp-duotone-regular"
    )
    light = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="sharp-duotone-light"
    )
    thin = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="sharp-duotone-thin"
    )


class FontAwesome(rx.ComponentNamespace):
    solid = __call__ = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="classic-solid"
    )
    regular = partial(
        staticmethod(FontAwesomeIcon.create), _icon_style="classic-regular"
    )
    light = partial(staticmethod(FontAwesomeIcon.create), _icon_style="classic-light")
    thin = partial(staticmethod(FontAwesomeIcon.create), _icon_style="classic-thin")
    brands = partial(staticmethod(FontAwesomeIcon.create), _icon_style="classic-brands")
    kit = partial(staticmethod(FontAwesomeIcon.create), _icon_style="kit")
    sharp = FontAwesomeSharp()
    duotone = FontAwesomeDuotone()
    sharp_duotone = FontAwesomeSharpDuotone()


fontawesome = fa = FontAwesome()
