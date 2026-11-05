# Software compatibility and evidence

For the setup sequence use [Cursor-first workflow](Cursor_First_Workflow.md). **The following are recorded source/project baselines, not exclusive version pins.** A newer version is acceptable if it opens the supplied assets, resolves required packages and passes real compile/Play/connection tests.

| Component | Source baseline / compatibility rule |
|---|---|
| Unity Editor | ProjectVersion records `6000.3.27f2` (Unity 6.3 LTS); use that patch or a newer tested-compatible editor |
| URP | 17.3.0 in existing project; keep aligned with the chosen Unity Editor |
| Input System | 1.20.1 in existing manifest |
| OpenXR | 1.16.1 in existing manifest |
| XR Management | 4.7.0 in existing project |
| Unity MCP | The shipped project pins `81542a7e86292b5c4c21b1782c5af23b567f45ce`; this is **historical**, not a latest-version guarantee. Inspect current stable upstream, upgrade cautiously and revalidate in the blank sandbox **and** the workshop project |
| Blender source | Recorded creator Blender 5.2.2; use that version or newer versions verified to open the provided files correctly |
| Blender MCP | Upstream `mcp-for-blender`, requires Python 3.10+, `uv`/`uvx`; verify addon/server and readback |
| Cursor | Current working Agent/client + terminal permissions; check whether classroom model needs Pro or other subscription/quota |
| Meta Horizon Link and Meta XR Core | External, not bundled; verify official current support, Quest headset, USB, SDK and OpenXR runtime |
| Desktop Play | Historical report is not a pass on the student machine |
| Quest 3/3S | **NOT VERIFIED** for this repository copy until actual device test |

Three existing project Cursor skills are bundled: `workshop-blender-edit`, `workshop-unity-lesson` and `workshop-quality-check` in `.cursor/skills`. No separate download is needed for those.

**Version suffix note:** historical Unity folder/namespace/assembly names still contain `V4`. Remove them only through the coordinated, live-tested procedure in [Version suffix migration](Version_Suffix_Migration.md), not by renaming individual files in Explorer.
