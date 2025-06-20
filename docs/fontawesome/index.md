---
icon: fontawesome/brands/font-awesome
---

# :fontawesome-brands-font-awesome: Font Awesome

[Font Awesome](https://fontawesome.com) is a library of over 50,000[^1] icons in several different styles,
including over 400 icons for popular brands.

!!! info "RIL only supports Font Awesome 6 for now"
    Font Awesome 7 support is planned. Keep an eye on [this GitHub issue](https://github.com/celsiusnarhwal/RIL/issues/3)
    for updates.

## Usage

Font Awesome icons can be used via `#!python icons.fontawesome` or `#!python icons.fa`. There's no functional
difference between the two, but the latter is shorter, so it is preferred and is what will be used throughout
the rest of the documentation.

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
    icons.fa.duotone.regular("wand-magic-sparkles")  # fa-duotone fa-regular fa-wand-magic-sparkles
    icons.fa.duotone.light("bomb")  # fa-duotone fa-light fa-bomb
    icons.fa.duotone.thin("camera-retro")  # fa-duotone fa-thin fa-camera-retro
    ```

=== ":fontawesome-sharp-duotone-solid-icons: Sharp Duotone"

    ```python
    import RIL as icons

    icons.fa.sharp_duotone.solid("music")  # fa-sharp-duotone fa-solid fa-music
    icons.fa.sharp_duotone.regular("comment")  # fa-sharp-duotone fa-regular fa-comment
    icons.fa.sharp_duotone.light("hippo")  # fa-sharp-duotone fa-light fa-hippo
    icons.fa.sharp_duotone.thin("calendar-days")  # fa-sharp-duotone fa-thin fa-calendar-days
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

The [Classic Solid](https://fontawesome.com/search?ip=classic&s=solid), 
[Classic Regular](https://fontawesome.com/search?ip=classic&s=regular), and [Brands](https://fontawesome.com/search?ic=brands)
styles are available for free[^2]; other styles require [Font Awesome Pro](pro.md).

!!! tip
    Classic Solid is the component's default style and can also be used by calling `#!python icons.fa` directly:

    ```python
    import RIL as icons

    icons.fa("house")  # equivalent to icons.fa.solid("house")
    ```
    
    Solid is also the default substyle for Sharp, Duotone, and Sharp Duotone:

    ```python
    import RIL as icons

    icons.fa.sharp("download")  # equivalent to icons.fa.sharp.solid("download")
    icons.fa.duotone("envelope")  # equivalent to icons.fa.duotone.solid("envelope")
    icons.fa.sharp_duotone("music")  # equivalent to icons.fa.sharp_duotone.solid("music")
    ``` 

[^1]:
Only [just over 2,000 icons](https://fontawesome.com/search?ic=free) are free, though. The rest require [Font Awesome Pro](pro.md).

[^2]:
Even within the Classic Solid and Classic Regular styles, some individual icons require Font Awesome Pro. The Brands 
style is completely free.

