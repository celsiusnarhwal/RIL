# Styling

RIL supports the nearly entire Font Awesome [styling toolkit](https://docs.fontawesome.com/web/use-with/react/style).

## Size

Font Awesome supports "T-shirt" sizes from `2xs` to `2xl` as well as literal sizing from `1x` to `10x`. (1)
{ .annotate }

1. In full, that's:

    - `2xs`, `xs`, `sm`, `lg`, `xl`, and `2xl`
    - `1x`, `2x`, `3x`, `4x`, `5x`, `6x`, `7x`, `8x`, `9x`, and `10x`

```python
import RIL as icons

# T-shirt sizing
icons.fa.solid("coffee", size="xs")
icons.fa.solid("coffee", size="lg")

# X-factor sizing
icons.fa.solid("coffee", size="6x")
```

## Automatic Width

Use the `automatic_width` prop to set an icon's width to its symbol rather than the entire [Icon Canvas](https://docs.fontawesome.com/web/style/icon-canvas).

```python
import RIL as icons

icons.fa.solid("coffee", automatic_width=True)
```

??? tip "Migrating from RIL v1?"
    The `automatic_width` prop is the inverse of the old `fixed_width` prop; i.e., `#!python automatic_width=True` does
    what `#!python fixed_width=False` did, and vice versa. `fixed_width` still works, but `automatic_width` is preferred
    and will override `fixed_width` whenever the two are in conflict.

## Icons in a List

You can use icons in lists by setting `#!python list_item=True` and wrapping them in an `#!python rx.list`:

```python
import reflex as rx
import RIL as icons

rx.list.unordered(
    icons.fa.solid("coffee", list_item=True),
    icons.fa.solid("check-square", list_item=True),
)
```

## Rotate and Flip Icons

Rotate on quarter turns and flip horizontally, vertically, or both. Or try [power transforms](#power-transforms)
for more granularity.

```python
import RIL as icons

icons.fa.solid("coffee", rotation=90)
icons.fa.solid("coffee", rotation=180)
icons.fa.solid("coffee", rotation=270)

icons.fa.solid("coffee", flip="horizontal")
icons.fa.solid("coffee", flip="vertical")
icons.fa.solid("coffee", flip="both")
```

## Animate Icons

You can use the animate utilities as a way to indicate loading or processing, especially when paired with 
icons like `spinner` or `sync`.

```python
import RIL as icons

icons.fa.solid("coffee", animation="beat")
icons.fa.solid("coffee", animation="beatFade")
icons.fa.solid("coffee", animation="bounce")
icons.fa.solid("coffee", animation="fade")
icons.fa.solid("coffee", animation="flip")
icons.fa.solid("coffee", animation="shake")
icons.fa.solid("coffee", animation="spin")
icons.fa.solid("coffee", animation="spin spinReverse")
icons.fa.solid("coffee", animation="spinPulse")
```

## Bordered Icons

Add a border around an icon with the `border` prop.

```python
import RIL as icons

icons.fa.solid("coffee", border=True)
```

## Pulled Icons

The `pull` prop is useful for wrapping text around icons.

```python
import RIL as icons

icons.fa.solid("coffee", pull="left")
icons.fa.solid("coffee", pull="right")
```

## Power Transforms

Power Transforms are just that — powerful! You can scale, position, rotate, and flip all with this one styling tool.

- To scale icons up or down, use `grow-#` and `shrink-#` with any arbitrary value, including decimals.
- To move icons up, down, left, or right, use `up-#`, `down-#`, `left-#`, and `right-#` with any arbitrary value, including decimals.
- To rotate or flip icons, use any combination of `flip-v`, `flip-h`, or `rotate-#` with any arbitrary value.

```python
import RIL as icons

icons.fa.solid("coffee", transform="shrink-6 left-4")
icons.fa.solid("coffee", transform="rotate-42")
```

## Mask

Use the `mask` prop when you want to layer two icons but have the inner icon cut out from the icon below so the 
parent element’s background shows through.

```python
import RIL as icons

icons.fa.solid("coffee", mask=icons.fa.regular("circle"))
```

!!! tip
    Props passed to the masking icon will have no effect.

## Swap Opacity (Duotone only)

Duotone icons allow you to swap the opacity of their layers.

```python
import RIL as icons

icons.fa.duotone.solid("coffee", swap_opacity=True)
icons.fa.sharp_duotone.solid("house", swap_opacity=True)
```

## Layering

You can use the layering utilities to layer icons, text, or add counters. You can also invert an icon to get a cut-out effect.

### Layer Icons

Layer one or more icons to create a new icon. Include the `#!python fixed_width=True` prop to have the layers align.

```python
import reflex as rx
import RIL as icons

rx.el.span(
    icons.fa.solid("circle"),
    icons.fa.solid("check", transform="shrink-6", inverse=True),
    class_name="fa-layers fa-fw fa-lg"
)
```

### Color Inversion

This can be useful when layering icons, or on its own.

```python
import RIL as icons

icons.fa.solid("coffee", inverse=True)
```

## CSS

Reflex's [`class_name` prop](https://reflex.dev/docs/components/props/#html-props) can be used to apply any of Font Awesome's 
[CSS style utility classes](https://docs.fontawesome.com/web/style/style-cheatsheet).
