---
icon: fontawesome/brands/bootstrap
hide:
  - navigation
---

# :fontawesome-brands-bootstrap: Bootstrap Icons

[Boostrap Icons](https://icons.getbootstrap.com/) is a library of over 2,000 icons designed for the
[Bootstrap](https://getbootstrap.com/) frontend framework.

!!! info "Plugin required"
    This icon library requires the [SVGR plugin](../plugins/index.md#svgr).

## Usage

<div class="annotate" markdown>

1. [Find the icon you want](https://icons.getbootstrap.com)
2. Pass its name to `#!python icons.bootstrap` (1)

</div>

1. `#!python icons.bi` works, too.

    ```python
    import RIL as icons
    
    icons.bi("arrow-right-square-fill")
    ```

```python
import RIL as icons

icons.bootstrap("arrow-right-square-fill")
```

Icon names are case-inensitive.

## Props

| **Name** | **Type**                           | **Description**                                                                                                                                                                                                      |   |
|----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `color`  | `#!python str` \| `#!python tuple` | The color of the icon. May be an [`rx.color` object](https://reflex.dev/docs/styling/theming/#shades) or [Pydantic-recognized color definition](https://docs.pydantic.dev/2.0/usage/types/extra_types/color_types/). |   |
| `size`   | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                  |   |
| `title`  | `#!python str`                     | An accessible, short-text, description of the icon.                                                                                                                                                                  |   |
