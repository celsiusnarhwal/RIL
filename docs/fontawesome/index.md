---
icon: fontawesome/brands/font-awesome
---

# :fontawesome-brands-font-awesome: Font Awesome

[Font Awesome](https://fontawesome.com) is a library of over 30,000[^1] icons in several different styles,
including over 400 icons for popular brands.

## Usage

Font Awesome icons can be used via `#!python icons.fontawesome` or `#!python icons.fa`. There's no functional
difference between the two, but the former is shorter, so it is preferred and is what will be used throughout
the rest of the documentaiton.

Each of Font Awesome's [styles](style-reference.md) is available as a method of `#!python icons.fa`. To use an icon,
pass its name to the method of your desired style.

=== ":fontawesome-solid-icons: Classic"

    ```python
    import RIL as icons

    icons.fa.solid("house")  # fa-solid fa-house
    icons.fa.regular("magnifying-glass")  # fa-regular fa-magnifying-glass
    icons.fa.light("user")  # fa-light fa-user
    icons.fa.thin("check")  # fa-thin fa-check
    ```

=== ":fontawesome-sharp-solid-icons: Sharp"

    ```python
    import RIL as icons

    icons.fa.sharp.solid("download")  # fa-sharp fa-solid fa-download
    icons.fa.sharp.regular("image")  # fa-sharp fa-regular fa-image
    icons.fa.sharp.light("phone")  # fa-sharp fa-light fa-phone
    icons.fa.sharp.thin("bars")  # fa-sharp fa-thin fa-bars
    ```

=== ":fontawesome-duotone-icons: Duotone"

    ```python
    import RIL as icons

    icons.fa.duotone.solid("envelope")  # fa-duotone fa-solid fa-envelope
    ```

=== ":fontawesome-sharp-duotone-solid-icons: Sharp Duotone"

    ```python
    import RIL as icons

    icons.fa.sharp_duotone.solid("music")  # fa-sharp-duotone fa-solid fa-music
    ```

=== ":fontawesome-brands-font-awesome: Brands"

    ```python
    import RIL as icons

    icons.fa.brands("python") # fa-brands fa-python
    ```

=== ":fontawesome-solid-block-question: Custom Icons"

    See [Using a Kit](pro.md/#using-a-kit) for setup instructions.

    ```python
    import RIL as icons

    icons.fa.kit("my-custom-icon")
    ```

The [Solid](https://fontawesome.com/search?f=classic&s=solid) and [Brands](https://fontawesome.com/search?f=brands)
styles are available for free[^2]; other styles require [Font Awesome Pro](pro.md).

!!! tip
    Solid is the component's default style and can also be used by calling `fa` directly:

    ```python
    import RIL as icons

    icons.fa("house")  # equivalent to fa.solid("house")
    ```
    
    Solid is also the default substyle for Sharp, Duotone, and Sharp Duotone:

    ```python
    import RIL as icons

    icons.fa.sharp("download")  # equivalent to fa.sharp.solid("download")
    icons.fa.duotone("envelope")  # equivalent to fa.duotone.solid("envelope")
    icons.fa.sharp_duotone("music")  # equivalent to fa.sharp_duotone.solid("music")
    ``` 

[^1]:
Only [just over 2,000 icons](https://fontawesome.com/search?m=free) are free, though. The rest require [Font Awesome Pro](pro.md).
[^2]:
Even within the Solid style, some individual icons require Font Awesome Pro. The Brands style is
completely free.

