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

| **Name**  | **Type**                              | **Description**                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                            |
|-----------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`   | `#!python str`                        | A short, accessible, title for the icon.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                            |
| `color`   | `#!python str` \| `#!python tuple`    | The color of the icon. May be a hex code, a tuple of RGB, RGBA, or HSL values, or any valid [CSS Color Module Level 3](https://www.w3.org/TR/css-color-3/#svg-color) color name. It may also be `#!python "default"`, in which case the icon will use the color it has been assigned by Simple Icons. |                                                                                                                                                                                                                                                                                            |
| `size`    | `#!python int` \| `#!python str`      | The size of the icon. May be an integer (in pixels) or a CSS size string (e.g., `#!python "1rem"`).                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                            |
| `version` | `#!python int` \| `#!python "latest"` | The major version of Simple Icons to use for this icon. May be `#!python "latest"` or an integer greater than or equal to 10. Defaults to the value of the [`simple.version` setting](#global-version-switching).                                                                                     |                                                                                                                                                                                                                                                                                            |


## Version switching

Simple Icons periodically remove icons for various reasons — for example, if their associated entity rebrands
or ceases operations. To prevent icon removals from breaking your project, the `version` prop allows you to choose
which major version of Simple Icons a particular icon should use. RIL supports everything
back to Simple Icons 10.

For example, to use the Twitter icon that
was [removed in Simple Icons 12](https://github.com/simple-icons/simple-icons/pull/9748):

```python
import RIL as icons

icons.simple("twitter", version=11)
```

Or to use icons for Microsoft brands, which
were [removed in Simple Icons 13](https://github.com/simple-icons/simple-icons/pull/10019):

```python
import RIL as icons

icons.simple("microsoft", version=12)
```

!!! warning "Removed icons aren't on the website"
    Simple Icons doesn't list removed icons on its website, so you won't be able to search for them, know their names,
    or see what they look like before using them in your project.

### Global version switching

The `simple.version` setting allows you to globally set a major version of Simple Icons that will be used for all icons
in your project
that do not explicitly set the `version` prop.

???+ config "`simple.version`: Controls the major version of Simple Icons used by RIL."
    `simple.version` is the highest major version of Simple Icons that RIL may use (or `latest`). RIL
    will use the newest version of Simple Icons available within this constraint.

    If this is an integer, it must be greater than or equal to 10. Defaults to `latest`.

    === "pyproject.toml"

        ```toml
        [tool.ril.simple]
        version = 14
        ```

    === "ril.toml"

        ```toml
        [simple]
        version = 14
        ```

    === "Environment variables / .env"

        ```shell
        RIL_SIMPLE__VERSION=14
        ```
