---
icon: fontawesome/solid/plug
hide:
  - navigation
---

# Plugins

## SVGR

The [SVGR](https://react-svgr.com) plugin allows RIL to import certain SVG files as React components. This plugin
is required for the following icon libraries:

- [:simple-materialdesign: Material Symbols](../material/index.md)
- [:fontawesome-brands-bootstrap: Bootstrap Icons](../bootstrap/index.md)

### Usage

=== ":octicons-file-code-16: `rxconfig.py`"
    ```python
    import reflex as rx
    
    from RIL import SVGRPlugin
    
    config = rx.Config(
        app_name="my_app",
        plugins=[SVGRPlugin()]
    )
    ```

This plugin does not have any configuration options.
