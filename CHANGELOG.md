# Changelog[^1]

Notable changes to the Reflex Icon Library will be documented here. Breaking changes are marked with a 🚩.

RIL adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="1-3-0">1.3.0 — 2024-12-05</a>

### Added

- Bootstrap Icons can now be used via `icons.bi` in addition to the existing `icons.bootstrap`.

### Changed

- Some Font Awesome-related error messages were improved for clarity.

## <a name="1-2-1">1.2.1 — 2024-12-03</a>

### Fixed

- Previous versions of RIL erroneously restricted all of Font Awesome's Classic Regular icons to Font Awesome Pro users.
In reality, [a subset of those icons is available for free](https://fontawesome.com/search?m=free&s=regular&ip=classic).
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
