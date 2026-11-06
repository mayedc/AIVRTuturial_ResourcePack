# Stage identifiers and file naming

The course has **two bootstrapping prompts** (both `00_*`) followed by numbered instructional stages.

| Student-facing stage | Stable file ID | Purpose |
|---|---|---|
| Preparation | `00_Clone_Preflight` | Check student machine and clone |
| Preparation | `00_Install_Update_MCP` | Configure Blender/Unity MCP |
| 1.1 | `01_1` | Review Blender models |
| 1.2 | `01_2` | Choose and recolor car |
| 1.3 | `01_3` | Generate Unity scene |
| 1.4 | `01_4` | Speed control and flight |
| 2.1 | `02_1` | XR readiness and device check |
| 2.2 | `02_2` | Bind XR rig and headset test |

**Rule:** Use human-readable `1.1` / `2.1` in instructional prose; use stable, zero-padded `01_1` / `02_1` for prompt filenames, paths, links and automation. These are **two representations of the same stage**, not inconsistent version numbers. Avoid changing existing stable prompt filenames without updating every incoming link and the static validator.

- New prompt files: `NN_M_Descriptive_English_Title.md`, with the phase `NN` zero-padded and step `M` a positive integer.
- Source and documentation filenames use descriptive English; avoid experimental labels, draft numbers and machine/user names in active student-facing material.
- `schemaVersion` in JSON is a real data schema version; `Unity 6`, `Quest 2`, FBX names and versioned published software are legitimate technical identifiers and should not be removed.
- Preserve historical testing evidence in `Docs/Validation/` or Git history. Do not imply a retrospective report is proof of a current clean-room/Quest 2 test.
- New stage steps require a separate human checkpoint; never silently execute the following stage.
