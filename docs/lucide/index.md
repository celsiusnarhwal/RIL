---
icon: simple/lucide
hide:
  - navigation
---

# :simple-lucide: Lucide

[Lucide](https://lucide.dev/icons) is a library of over 1,000 icons.

Reflex has a [built-in component](https://reflex.dev/docs/library/data-display/icon/) for Lucide. For your convenience,
RIL provides passthrough access to this component via `#!python icons.lucide`:

```python
import RIL as icons

icons.lucide("calendar")  # equivalent to rx.icon("calendar")
```

For detailed usage instructions, see [Reflex's documentation](https://reflex.dev/docs/library/data-display/icon/).