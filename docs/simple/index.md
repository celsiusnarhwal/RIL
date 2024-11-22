---
icon: simple/simpleicons
hide:
  - navigation
---

# :simple-simpleicons: Simple Icons

[Simple Icons](https://simpleicons.org) is a library of over 3,000 icons for popular brands.

## Usage

Icons from Simple Icons can be used via `#!python icons.simple` or `#!python icons.si`.

1. [Find the icon you want](https://simpleicons.org)
2. Pass its name to `#!python icons.simple`

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

| **Name**  | **Type**                           | **Description**                                                                                                                                                                                                                                                                                    |   |
|-----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| ``title`` | `#!python str`                     | A short, accessible, title for the icon.                                                                                                       |   |
| ``color`` | `#!python str` \| `#!python tuple` | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. It may also be `#!python "default"`, in which case the icon will use the color it has been assigned by Simple Icons. |   |
| ``size``    | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                                                                                                |   |

## Versioning

Simple Icons routinely releases major versions that remove icons. RIL allows you to avoid surprise icon removals by
setting the `simple.version` setting to the major version of Simple Icons you want to use.

???+ config "`simple.version`: Controls the major version of Simple Icons used by RIL."
    `simple.version` places an upper boundary on the major version of Simple Icons that
    RIL will use. If set, RIL will use the newest version of 
    [@icons-pack/react-simple-icons](https://npmjs.org/@icons-pack/react-simple-icons) that depends on
    a version of Simple Icons with a major verion number less than or equal to `simple.version`.

    `simple.version` must be greater than or equal to 10.

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