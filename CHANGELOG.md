# Changelog[^1]

Notable changes to the Reflex Icon Library will be documented here. Breaking changes are marked with a 🚩.

RIL adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="1-5-0">1.5.0 — 2025-06-03</a>

### Changed

- RIL now respects the contents of the `.npmrc` file identified by [
  `reflex.utils.prerequisites.initialize_npmrc()`](https://github.com/reflex-dev/reflex/blob/31be6458807f71de8be0cbdbef09b35d72cbdc6f/reflex/utils/prerequisites.py#L1071).

## <a name="1-4-4">1.4.4 — 2025-06-01</a>

### Fixed

- Fixed an issue that may have affected compatibility with Reflex 0.7.12 and earlier.

## <a name="1-4-3">1.4.3 — 2025-05-30</a>

### Changed

- RIL is now compatible with Reflex 0.7.13 and later. The good news is that contrary to
  [my own expectations](https://github.com/celsiusnarhwal/RIL/issues/4), I didn't have to make any breaking changes
  or drop support for Reflex 0.7.12 and earlier. The bad news is that I'm not gonna wanna test all future versions
  of RIL on both Reflex 0.7.12 and Reflex ≥0.7.13, so **support for Reflex 0.7.12 and earlier is deprecated in this
  release and will be removed in RIL 2.0.0**. You should prepare for this by upgrading to the latest versions of RIL and
  Reflex as soon
  as possible. (Resolves [#4](https://github.com/celsiusnarhwal/RIL/issues/4).)
- With the exception of `@fortawesome/react-fontawesome` and Font Awesome Kit packages, all Font Awesome NPM packages
  have been pinned to major version 6 in order to avoid unwanted surprises when Font Awesome 7 launches in June.
- Phosphor icons now have the string "Icon" suffixed to their component tags per
  [new recommendations from the Phosphor team](https://github.com/phosphor-icons/react/releases/tag/v2.1.8). This
  changes nothing for end users; you can continue using Phosphor icons with RIL as you always have.

## <a name="1-4-2">1.4.2 — 2025-05-26</a>

### Changed

- RIL is now compatible only with Reflex 0.7.12 and earlier due to a change in Reflex 0.7.13 that breaks RIL
  ([#4](https://github.com/celsiusnarhwal/RIL/issues/4)).

## <a name="1-4-1">1.4.1 — 2025-04-10</a>

### Changed

- The Simple Icons component's upstream package is
  now [maintained by yours truly](https://github.com/celsiusnarhwal/ril-simple-icons).
  This shouldn't change anything for end users, but if you run into any issues,
  please [report them](https://github.com/celsiusnarhwal/RIL/issues).

## <a name="1-4-0">1.4.0 — 2025-03-26</a>

### Changed

- When requesting Simple Icons' version history, RIL now uses the URL returned by
  [
  `reflex.utils.registry.get_npm_registry()`](https://github.com/reflex-dev/reflex/blob/5b6afb1eb87435d58ba05d92094f1392709fbc98/reflex/utils/registry.py#L60).
  This changes nothing for most users, but may improve the performance of the Simple Icons component for users in China,
  where
  network restrictions can make accessing the standard NPM registry difficult or impossible.

## <a name="1-3-3">1.3.3 — 2025-03-25</a>

### Fixed

- Fixed a recursion error that would occur when creating an icon in Reflex 0.7.2 and
  later. (Resolves [#1](https://github.com/celsiusnarhwal/RIL/issues/1).)

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
  In
  reality, [a subset of those icons is available for free](https://fontawesome.com/search?ic=free&s=regular&ip=classic).
  Users who don't subscribe to Font Awesome Pro can now use those icons through RIL.

## <a name="1-2-0">1.2.0 — 2024-12-02</a>

### Added

- This version of RIL adds support for the Regular, Light, and Thin styles of Font
  Awesome's [Duotone](https://fontawesome.com/search?ip=duotone)
  and [Sharp Duotone](https://fontawesome.com/search?ip=sharp-duotone)
  families. ([Docs](https://ril.celsiusnarhwal.dev/fontawesome/#fa-secondaryopacity4-duotone))

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
