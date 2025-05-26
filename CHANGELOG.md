# Changelog[^1]

Notable changes to the Reflex Icon Library will be documented here. Breaking changes are marked with a 🚩.

RIL adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="1-4-2">1.4.2 — 2025-05-26</a>

### Changes

- RIL is now compatible only with Reflex 0.7.12 and earlier due to a change in Reflex 0.7.13 that breaks RIL.
([reflex-dev/reflex#5829](https://github.com/reflex-dev/reflex/pull/5289)). Assuming this problem is fixable,
the next version of RIL will almost certainly drop support for Reflex 0.7.12 and earlier.

## <a name="1-4-1">1.4.1 — 2025-04-10</a>

### Changes

- The Simple Icons component's upstream package is now [maintained by yours truly](https://github.com/celsiusnarhwal/ril-simple-icons).
This shouldn't change anything for end users, but if you run into any issues, please [report them](https://github.com/celsiusnarhwal/RIL/issues).


## <a name="1-4-0">1.4.0 — 2025-03-26</a>

### Changed

- When requesting Simple Icons' version history, RIL now uses the URL returned by
[`reflex.utils.get_npm_registry()`](https://github.com/reflex-dev/reflex/blob/5b6afb1eb87435d58ba05d92094f1392709fbc98/reflex/utils/registry.py#L60).
This changes nothing for most users, but may improve the performance of the Simple Icons component for users in China, where
network restrictions can make accessing the standard NPM registry difficult or impossible.

## <a name="1-3-3">1.3.3 — 2025-03-25</a>

### Fixed

- Fixed a recursion error that would occur when creating an icon in Reflex 0.7.2 and later. ([#1](https://github.com/celsiusnarhwal/RIL/issues/1))

## <a name="1-3-2">1.3.2 — 2025-01-17</a>

### Fixed

- Fixed a bug in which Reflex's `class_name` prop would not be applied to icons from Simple Icons, Material Symbols,
Phosphor Icons, and Bootstrap Icons.

## <a name="1-3-0">1.3.0 — 2024-12-05</a>

### Added

- Bootstrap Icons can now be used via `icons.bi` in addition to the existing `icons.bootstrap`.

### Changed

- Some Font Awesome-related error messages were improved for clarity.

## <a name="1-2-1">1.2.1 — 2024-12-03</a>

### Fixed

- Previous versions of RIL erroneously restricted all of Font Awesome's Classic Regular icons to Font Awesome Pro users.
In reality, [a subset of those icons is available for free](https://fontawesome.com/search?ic=free&s=regular&ip=classic).
Users who don't subscribe to Font Awesome Pro can now use those icons through RIL.

## <a name="1-2-0">1.2.0 — 2024-12-02</a>

### Added

- This version of RIL adds support for the Regular, Light, and Thin styles of Font Awesome's [Duotone](https://fontawesome.com/search?ip=duotone)
and [Sharp Duotone](https://fontawesome.com/search?ip=sharp-duotone) families. ([Docs](https://ril.celsiusnarhwal.dev/fontawesome/#fa-secondaryopacity4-duotone))

## <a name="1-1-1">1.1.1 — 2024-11-25</a>

### Fixed

- Fixed a bug in which RIL's Font Awesome component would attempt to use a Kit if a Kit code was specified
but the `fontawesome.pro_enabled` setting was not set to `true`.

## <a name="1-1-0">1.1.0 — 2024-11-22</a>

### Added

- The Simple Icons component now allows you choose the major version of Simple Icons on a per-icon basis.
  ([Docs](https://ril.celsiusnarhwal.dev/simple/#props))

## <a name="1-0-0">1.0.0 — 2024-11-22</a>

This is the initial release of the Reflex Icon Library.

[^1]: Format based on [Keep a Changelog](https://keepachangelog.com).
