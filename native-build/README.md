# Native components

The corresponding-source release archive contains the pinned upstream tarballs
under `upstream/`. Their URLs and SHA-256 values are in SOURCE_PROVENANCE.json.
The repo overlay contains RG DS package recipes and patches. This folder also
contains the Flip GB frontend/FFmpeg recipes and generated configuration records.
Use the pinned ROCKNIX build system with the corresponding package overrides,
architecture/toolchain and configuration. The application package builder takes
an audited staging root of native output; it does not silently pick host binaries.

The RG DS app uses an AArch64 GBA frontend/core and an isolated qualified GB
frontend/core with private FFmpeg 7.1.1 libraries. The baseline OS libraries stay
unchanged. Their checksums and link profiles are retained in each app package.
These build configurations are records, with local build paths normalized.
Commercial game ROMs, player saves and signing keys are excluded.
