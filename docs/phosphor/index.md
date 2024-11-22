---
icon: simple/phosphoricons
hide:
  - navigation
---

# :simple-phosphoricons: Phosphor

[Phosphor](https://phosphoricons.com) is a library of over 1,000 icons, each in six different styles.

## Usage

1. [Find the icon you want](https://phosphoricons.com)
2. Pass its name to `#!python icons.phosphor`

```python
import RIL as icons

icons.phosphor("acorn")
```

Icon names are case-inensitive.

## Props

| **Name** | **Type**                           | **Description**                                                                                                                                                                  |   |
|----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `weight` | `#!python str`                     | The weight of the icon. May be one of `#!python "thin"`, `#!python "light"`, `#!python "regular"`, `#!python "bold"`, `#!python "fill"`, or `#!python "duotone"`.                |   |
| `color`  | `#!python str` \| `#!python tuple` | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. |   |
| `size`   | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                              |   |
| `alt`     | `#!python str`                      | [Alt text](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt) for the icon.                                                                                  |   |

## Context

RIL supports the use of Phosphor's [Context](https://github.com/phosphor-icons/react?tab=readme-ov-file#context) feature
to apply a default style to a group of icons.

```python
import RIL as icons

icons.phosphor.context(
    icons.phosphor("horse"),  # I'm lime-green, 32px, and bold!
    icons.phosphor("heart"),  # Me too!
    icons.phosphor("cube"),  # Me three :)
    color="limegreen",
    size=32,
    weight="bold",
)
```

### Global Context 
You can configure the `phosphor` settings group to have a default style applied to all Phosphor icons
in your project.

???+ config "`phosphor.*`: Settings for configuring Phosphor icons."
    The `phosphor` settings group allows you to configure default styling options that will be applied
    to all Phosphor icons in your project.

    You can configure a default for [any prop](#props) other than `alt`.

    === "pyproject.toml"
    
        ```toml
        [tool.ril.phosphor]
        color = "limegreen"
        size = 32
        weight = "bold"
        ```

    === "ril.toml"

        ```toml
        [phosphor]
        color = "limegreen"
        size = 32
        weight = "bold"
        ```

    === "Environment variables / .env"

        ```shell
        RIL_PHOSPHOR__COLOR="limegreen"
        RIL_PHOSPHOR__SIZE=32
        RIL_PHOSPHOR__WEIGHT="bold"
        ```
