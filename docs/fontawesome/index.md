---
icon: fontawesome/brands/font-awesome
---

# :fontawesome-brands-font-awesome: Font Awesome

[Font Awesome](https://fontawesome.com) is a library of over 50,000[^1] icons in several different styles,
including over 400 icons for popular brands.

## Usage

Font Awesome icons can be used via `#!python icons.fontawesome` or `#!python icons.fa`. There's no functional
difference between the two, but the latter is shorter, so it is preferred and is what will be used throughout
the rest of the documentation.

Each of Font Awesome's [styles](style-reference.md) is available as a method of `#!python icons.fa`. To use an icon,
pass its name to the method of your desired style.

=== ":fontawesome-solid-icons: Classic"

    ```python
    import RIL as icons

    icons.fa.solid("house") 
    icons.fa.regular("magnifying-glass") 
    icons.fa.light("user")
    icons.fa.thin("check")  
    ```

=== ":fontawesome-sharp-solid-icons: Sharp"

    ```python
    import RIL as icons

    icons.fa.sharp.solid("download")  
    icons.fa.sharp.regular("image")  
    icons.fa.sharp.light("phone")  
    icons.fa.sharp.thin("bars") 
    ```

=== ":fontawesome-duotone-icons: Duotone"

    ```python
    import RIL as icons

    icons.fa.duotone.solid("envelope") 
    icons.fa.duotone.regular("wand-magic-sparkles") 
    icons.fa.duotone.light("bomb")  
    icons.fa.duotone.thin("camera-retro") 
    ```

=== ":fontawesome-sharp-duotone-solid-icons: Sharp Duotone"

    ```python
    import RIL as icons

    icons.fa.sharp_duotone.solid("music")  
    icons.fa.sharp_duotone.regular("comment")  
    icons.fa.sharp_duotone.light("hippo") 
    icons.fa.sharp_duotone.thin("calendar-days") 
    ```

=== ":fontawesome-brands-font-awesome: Brands"

    ```python
    import RIL as icons

    icons.fa.brands("python")
    ```

=== ":fontawesome-solid-box: Icon Packs"

    !!! info
        These styles require a Font Awesome Pro+ subscription and a [Kit](pro.md#using-a-kit).

    === "Chisel"
        ```python
        import RIL as icons

        icons.fa.chisel("house") 
        ```

    === "Etch"
        ```python
        import RIL as icons

        icons.fa.etch("house")
        ```

    === "Jelly"
        ```python
        import RIL as icons

        icons.fa.jelly("house")
        icons.fa.jelly.fill("circle-user")
        icons.fa.jelly.duo("image")
        ```

    === "Notdog"
        ```python
        import RIL as icons

        icons.fa.notdog("house")
        icons.fa.notdog.duo("circle-user")
        ```

    === "Slab"
        ```python
        import RIL as icons

        icons.fa.slab("house")
        icons.fa.slab.press("circle-user")
        ```

    === "Thumbprint"
        ```python
        import RIL as icons

        icons.fa.thumbprint("house")
        ```

    === "Whiteboard"
        ```python
        import RIL as icons

        icons.fa.whiteboard("house")
        ```

    === "Utility"
        ```python
        import RIL as icons

        icons.fa.utility("house")
        icons.fa.utility.fill("circle-user")
        icons.fa.utility.duo("image")
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

