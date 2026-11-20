# ButterflyOS Tools

Shared downloads and source for **Blink**, **Bdex**, and **Bslap**.

- **Blink:** Copy or trade Pokemon between compatible saves and replay supported gifts and events.
- **Bdex:** Build a collection from your saves, inspect Pokemon, and browse your collection through a read-only local website.
- **Bslap:** In-game trading and battling between nearby compatible ButterflyOS handhelds.

## Add a tool

On a supported ButterflyOS image, open **Tools → Y Add Tools**. Select **Add Tools**,
refresh the catalog, choose a tool and confirm **Add Tool**. It then appears in
normal Tools. **L1** selects Installed; **R1** selects Add Tools. **Back** returns
to Tools. Touch navigation is supported on the RG DS.

Installed tools can be updated, rolled back or removed. Close the app and its
web viewer first. Removal preserves saves, collections, settings and sprite
caches. Updating a tool does not require downloading another OS image.

## Supported downloads

The initial feed contains qualified **RG DS Plus** packages. The Flip installer
integration and its catalog variants will be added separately; do not copy an
RG DS package onto another handheld. Existing Flip versions have participated
in cross-device Blink and Bslap testing, but that does not make these archives
compatible with an unmodified Flip installer.

This is an application repository, not an OS image. The Miyoo Flip OS is at
[ButterflyOS](https://github.com/KeatenPerkins/butterflyOS). The RG DS port is
still under development.

## Downloads and verification

The latest release contains a signed catalog, app archives, catalog icons,
SHA-256 checksums and a corresponding-source archive. The installer verifies
the catalog signature, device requirements and each package before activating
it. Older downloaded code is retained for rollback. Installed apps work offline;
adding and updating apps requires Internet access.

The stable catalog address is:
`https://github.com/KeatenPerkins/ButterflyOS-Tools/releases/latest/download/catalog.json`

App download links within that catalog are pinned to a specific release. The
catalog uses GitHub's [documented latest-asset URL](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases).
No GitHub account or personal token is needed on the handheld.

## Game data and limitations

No commercial game ROMs, player saves, Pokemon sprite caches or private account
credentials are included. Sprites come from a matching ROM supplied by the user.
Blink and Bdex edit save data; Bslap uses in-game links. Supported languages,
revisions, game eligibility restrictions and link backends still apply. A common
app version does not guarantee compatibility with arbitrary emulator builds.

Back up important saves. Code rollback does not undo a database migration or
changes made to a save during play. Gen 3 Bslap room exits can report a
communication error if both players independently start leaving; better results
have been observed when one player initiates and the other follows the dialogue.

## Source and licensing

`overlay/` contains the application source and native build recipes. `tools/btools/`
contains the package builder and catalog tools. Releases additionally carry the
upstream source archives, patches and build configuration records used for the
included native components.

Original ButterflyOS software is GPL-2.0-or-later where marked. Third-party
components retain their own licenses. Full notices and license texts are in
`overlay/projects/ROCKNIX/packages/misc/butterflyos-pokemon/licenses/`; official
ButterflyOS branding has separate terms there. This project is not affiliated
with Nintendo, Game Freak or The Pokemon Company.
