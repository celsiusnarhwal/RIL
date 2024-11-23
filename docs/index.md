---
icon: fontawesome/solid/house
hide:
  - navigation
---

# The Reflex Icon Library

The Reflex Icon Library (RIL) is your one-stop icon shop for [Reflex](https://reflex.dev) projects.
It includes the icon libraries of [Font Awesome](https://fontawesome.com), [Simple Icons](https://simpleicons.org),
Google's [Material Symbols](https://fonts.google.com/icons),
GitHub's [Octicons](https://primer.style/octicons), [Phosphor](https://phosphoricons.com/),
and [Bootstrap Icons](https://icons.getbootstrap.com/), packaging over 12,000 icons in total.

## Installation

```shell
pip install reflex-icon-library
```

## Usage

```python
import reflex as rx
import RIL as icons


def index() -> rx.Component:
    return rx.container(
        icons.fontawesome.solid("house"),
        icons.simple("python"),
        icons.material("Search"),
        icons.octicons("check-circle-fill"),
        icons.phosphor("acorn"),
        icons.bootstrap("airplane"),
    )


app = rx.App()
app.add_page(index)
```

!!! warning "RIL does not validate icon names"
    Passing the name of an icon that doesn't exist will get you a cryptic error from React, but RIL itself
    won't complain. If you're passing an icon name that's not working and you're _confident_ it should, please
    [open an issue](https://github.com/celsiusnarhwal/RIL/issues/new).

This is just a basic example. For detailed usage instructions, see the documentation for each icon library:

- [:fontawesome-brands-font-awesome: Font Awesome](fontawesome/index.md)
- [:simple-simpleicons: Simple Icons](simple/index.md)
- [:simple-materialdesign: Material Symbols](material/index.md)
- [:fontawesome-brands-github: Octicons](octicons/index.md)
- [:simple-phosphoricons: Phosphor](phosphor/index.md)
- [:fontawesome-brands-bootstrap: Bootstrap Icons](bootstrap/index.md)

RIL also includes a convenience wrapper for
Reflex's [built-in icon compoment](https://reflex.dev/docs/library/data-display/icon/):

- [:simple-lucide: Lucide](lucide/index.md)

## Configuration

Some of RIL's icon libraries have globally-configurable settings. Each of them will be reintroduced as they become
relevant, but here's a quick overview of them all.

=== ":fontawesome-brands-font-awesome: Font Awesome"

    | <div style="width:200px">**Setting**</div> | **Description**                                                                                                                                                                                                       | **Default**                 |
    |-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
    | `pro_enabled`                             | Whether or not to enable the use of Font Awesome Pro icons. ([More](fontawesome/pro.md))                                                                                                                              | `#!python False`            |
    | `kit_code`                                | A Font Awesome Kit code. If provided, the corresponding Kit will be used for all Font Awesome icons. ([More](fontawesome/pro.md#using-a-kit))                                                                         | N/A                         |
    | `npm_registry`                 | The URL of a registry from which Reflex should install packages in the `@fortawesome` and `@awesome.me` namespaces when Font Awesome Pro is enabled. ([More](fontawesome/pro.md#using-alternate-registries-advanced)) | https://npm.fontawesome.com |

=== ":simple-simpleicons: Simple Icons"

    | <div style="width:200px">**Setting**</div> | **Description**                                                                                                                                                                                                       | **Default**                 |
    |----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
    | `version`                    | The newest major version of Simple Icons that RIL may use, or `latest` for the latest version. ([More](simple/index.md/#versioning))                                                                                  | `latest`                    |
    

=== ":simple-phosphoricons: Phosphor"

    | <div style="width:200px">**Setting**</div> | **Description**                                                                                 |
    |--------------------------------------------|-------------------------------------------------------------------------------------------------|
    | `weight`, `color`, `size`                   | Default styling options to apply to Phosphor icons. ([More](phosphor/index.md/#global-context)) |

### Configuration sources

RIL can be configured through a `pyproject.toml` file, an `ril.toml` file, or environment variables.

=== "pyproject.toml"

    If your project uses a
    [`pyproject.toml` file](https://packaging.python.org/en/latest/guides/writing-pyproject-toml),
    you can configure RIL via the `#!toml [tool.ril.library]` table, where `library` is one of
    `fontawesome`, `simple`, or `phosphor`:

    ```toml
    [tool.ril.library]
    setting_name = value "(1)!"
    ```

    1. Setting names should be written in `snake_case` rather than `kebab-case`. `kebab-case` names will cause an error.

    `pyproject.toml` must be in your current working directory for RIL to see it.

=== "ril.toml"

    If you don't want to use `pyproject.toml`, you can use RIL's own `ril.toml`. This works identically to
    `pyproject.toml`, except the table is simply named `#!toml [library]`, where `library` is one of
    `fontawesome`, `simple`, or `phosphor`:

    ```toml
    [library]
    setting_name = value "(1)!"
    ```

    1. Setting names should be written in `snake_case` rather than `kebab-case`. `kebab-case` names will cause an error.

    `ril.toml` must be in your current working directory for RIL to see it.

=== "Environment variables / .env"

    You can configure RIL's settings via environment variables of the name `RIL_{LIBRARY}__{SETTING_NAME}`, where
    `{LIBRARY}` is one of `FONTAWESOME`, `SIMPLE`, or `PHOSPHOR` and `{SETTING_NAME}` is the name of the setting you 
    want to configure. Variable names are case-insensitive.

    Note that there are two underscores between `{LIBRARY}` and `{SETTING_NAME}`.

    If you put your environment variables in a `.env` file located in the current working directory,
    `RIL` will read and apply it automatically without the need for additional libraries or tools.

RIL reads configuration sources with the following priority:

1. Environment variables
2. `.env`
3. `pyproject.toml`
4. `ril.toml`

## Updating icon libraries

Whenever new icons are added to any of RIL's supported libraries, you don't need to wait for an RIL update to use them.
Just have Reflex to reinstall your project's frontend packages and you'll be good to go:

```shell
reflex init && reflex run
```
