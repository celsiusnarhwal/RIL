---
icon: fontawesome/brands/bootstrap
hide:
  - navigation
---

# :fontawesome-brands-bootstrap: Bootstrap Icons

[Boostrap Icons](https://icons.getbootstrap.com/) is a library of over 2,000 icons designed for the 
[Bootstrap](https://getbootstrap.com/) frontend framework.

!!! info "Plugin required"
    This icon library requires the [SVGR plugin](../other/plugins#svgr).


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

| **Name** | **Type**                           | **Description**                                                                                                                                                                  |   |
|----------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `color`  | `#!python str` \| `#!python tuple` | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. |   |
| `size`   | `#!python int` \| `#!python str`   | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                              |   |
| `title`  | `#!python str`                      | An accessible, short-text, description of the icon.                                                                                                                              |   |
