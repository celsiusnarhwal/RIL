---
icon: simple/simpleicons
hide:
  - navigation
---

# :simple-simpleicons: Simple Icons

[Simple Icons](https://simpleicons.org) is a library of over 3,000 icons for popular brands.

## Usage

<div class="annotate" markdown>

1. [Find the icon you want](https://simpleicons.org)
2. Pass its name to `#!python icons.simple` (1)

</div>

1. `#!python icons.si` works, too.
    ```python
    import RIL as icons
    
    icons.si("simple icons")
    ```
   
```python
import RIL as icons

icons.simple("simple icons")
```

!!! warning "There's just one unintuitive exception"
    The :simple-e: icon, identified by Simple Icons as "/e/", is passed as simply `#!python "e"`. 

    ```python
    import RIL as icons

    icons.simple("e")
    ```

Icon names are case-inensitive.

## Props

| **Name** | **Type**                             | **Description**                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                            |
|---------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title` | `#!python str`                       | A short, accessible, title for the icon.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                            |
| `color` | `#!python str` \| `#!python tuple`   | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. It may also be `#!python "default"`, in which case the icon will use the color it has been assigned by Simple Icons. |                                                                                                                                                                                                                                                                                            |
| `size` | `#!python int` \| `#!python str`     | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                            |
| `version` | `#!python int` \| `#!python "latest"` | The major version of Simple Icons to use for this icon. May be `#!python "latest"` or an integer greater than or equal to 10. Defaults to the value of the [`simple.version` setting](#versioning).                                                                                                     |   |

## Versioning

In addition to setting a version per-icon via the `version` prop, RIL also allows you to set a default Simple Icons
version via the `simple.version` setting.

???+ config "`simple.version`: Controls the major version of Simple Icons used by RIL."
    `simple.version` is the highest major version of Simple Icons that RIL may use (or `latest`). RIL
    will use the newest version of Simple Icons available within this constraint.

    Must be greater than or equal to 10. Defaults to `latest`.

    === "pyproject.toml"

        ```toml
        [tool.ril.simple]
        version = 13
        ```

    === "ril.toml"

        ```toml
        [simple]
        version = 13
        ```

    === "Environment variables / .env"

        ```shell
        RIL_SIMPLE__VERSION=13
        ```