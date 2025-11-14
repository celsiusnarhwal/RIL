---
icon: simple/materialdesign
hide:
  - navigation
---

# :simple-materialdesign: Material Symbols

[Material Symbols](https://fonts.google.com/icons) is a library of icons designed by [Google](https://opensource.google)
for use with its [Material](https://material.io) design system.

!!! info "Plugin required"
    This icon library requires the [SVGR plugin](../plugins/index.md#svgr).

## Usage

1. [Find the icon you want](https://fonts.google.com/icons)
2. Pass its name to `#!python icons.material`

```python
import RIL as icons

icons.material("search")
```

## Props

| **Name**  | **Type**                           | **Description**                                                                                                                                                                                                     |   |
|-----------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `weight`  | `#!python int`                     | The weight of the icon. May be a multiple of 100 from `100` to `700`. Defaults to `400`.                                                                                                                            |   |
| `variant` | `#!python str`                     | The variant of the icon. May be one of `#!python "outlined"`, `#!python "rounded"`, or `#!python "sharp"`.                                                                                                          |   |
| `filled`  | `#!python bool`                    | Whether to use the icon's filled appearance.                                                                                                                                                                        |   |
| `color`   | `#!python str` \| `#!python tuple` | The color of the icon. May be an [`rx.color` object](https://reflex.dev/docs/styling/theming/#shades) or [Pydantic-recognized color definition](https://docs.pydantic.dev/2.0/usage/types/extra_types/color_types/). |   |
| `size`    | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                 |   |
