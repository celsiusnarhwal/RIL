---
icon: fontawesome/brands/github
hide:
  - navigation
---

# :fontawesome-brands-github: Octicons

[Octicons](https://primer.style/octicons) is a library of icons designed by [GitHub](https://github.com) as part of
its [Primer](https://primer.style) design system.

## Usage

1. [Find the icon you want](https://primer.style/octicons)
2. Pass its name to `#!python icons.octicons`

```python
import RIL as icons

icons.octicons("check-circle-fill")
```

Icon names are case-inensitive.

## Props

| **Name** | **Type**                           | **Description**                                                                                                                                                                  |   |
|----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `color`  | `#!python str` \| `#!python tuple` | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. |   |
| `size`   | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                              |   |
