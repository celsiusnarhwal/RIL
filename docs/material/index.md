---
icon: simple/materialdesign
hide:
  - navigation
---

# :simple-materialdesign: Material Symbols

[Material Symbols](https://fonts.google.com/icons) is a library of icons designed by [Google](https://opensource.google) 
for use with its [Material](https://material.io) design system.

## Usage

1. [Find the icon you want](https://fonts.google.com/icons)
2. Pass its name to `#!python icons.material`

```python
import RIL as icons

icons.material("Search")
```

!!! warning "Icon names are case-sensitive"
    Unlike RIL's other icon libraries, Material Symbol names are case-sensitive. The name you pass must _exactly_ match
    the name on Google Fonts.

## Props

| **Name**  | **Type**                           | **Description**                                                                                                                                                                  |   |
|-----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `variant` | `#!python str`                     | The variant of the icon. May be one of `#!python "outlined"`, `#!python "rounded"`, or `#!python "sharp"`.                                                                       |   |
| `filled`   | `#!python bool`                     | Whether to use the icon's filled appearance.                                                                                                                                     |   |
| `color`   | `#!python str` \| `#!python tuple` | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. |   |
| `size`    | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                              |   |
