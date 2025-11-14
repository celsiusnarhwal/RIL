---
icon: fontawesome/brands/github
hide:
  - navigation
---

# :fontawesome-brands-github: Octicons

[Octicons](https://primer.style/octicons) is a library of icons designed by [GitHub](https://github.com/about) as part
of its [Primer](https://primer.style) design system.

## Usage

1. [Find the icon you want](https://primer.style/octicons)
2. Pass its name to `#!python icons.octicons`

```python
import RIL as icons

icons.octicons("check-circle-fill")
```

Icon names are case-inensitive.

## Props

| **Name** | **Type**                           | **Description**                                                                                                                                                                                                      |   |
|----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `color`  | `#!python str` \| `#!python tuple` | The color of the icon. May be an [`rx.color` object](https://reflex.dev/docs/styling/theming/#shades) or [Pydantic-recognized color definition](https://docs.pydantic.dev/2.0/usage/types/extra_types/color_types/). |   |
| `size`   | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                  |   |
