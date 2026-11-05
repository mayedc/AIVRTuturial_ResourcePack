# Controlled removal of historical V4 suffixes — Unity verification required

The **human-facing course** is now referred to as **AI VR Workshop** (no V4/V5/debug suffix). The repository still contains a **legacy physical Unity folder** `Assets/AI_VR_Workshop_V4`, namespace `AIVRWorkshop.V4`, assembly definitions, serialized scenes/prefabs and Editor menus. Merely renaming it through GitHub's text API is unsafe without opening and validating the actual Unity project.

**This document is a migration plan, not a claim the files have been renamed.** After migration, the canonical asset folder should be `Assets/AI_VR_Workshop`, namespace `AIVRWorkshop`, assemblies `AIVRWorkshop.Runtime` and `AIVRWorkshop.Editor`, Editor menu `Workshop`, and root GameObject `AI_VR_Workshop`. Scene and public script filenames can remain `Workshop_Desktop.unity`, etc.

## Cursor migration prompt for a machine with Unity installed

> Make a clean Git branch and back up the original Unity project before renaming. First inventory **every path and content occurrence** of `AI_VR_Workshop_V4`, `AIVRWorkshop.V4`, `Workshop V4` (including case variants) in `Assets`, `Tools`, `Prompts`, `Docs`, `.cursor` and `ProjectSettings`. Also locate serialized scene/prefab text, Unity root GameObject names, assembly definitions and scripts. Distinguish historical release *version numbers* from **debug suffixes in asset identities**—preserve genuine release histories.
>
> With Unity **closed**, use **`git mv` or filesystem rename** to move `Assets/AI_VR_Workshop_V4` to `Assets/AI_VR_Workshop` and rename its sibling `.meta` file without changing the Unity GUID. Rename both `AIVRWorkshop.V4.*.asmdef` files and their matching `.meta` files while keeping their GUIDs. Change assembly names/references, namespaces in C# and relevant C# `using` directives; update Editor menu labels and validation path. Search for explicit C# fully-qualified names in serialized objects and settings. Avoid bulk-regenerating any `.meta`; don't edit embedded `guid:` or `fileID:` references. Fix human-readable root GameObject names by a Unity Editor operation on **copies** of teacher scenes/prefabs, not a blind YAML rewrite.
>
> Update all active README, docs, prompts, install/validator scripts, asset manifests and tests to the new names, but preserve clearly marked historical hashes and release notes. Check any generated files/paths for assumptions about the old root. Do not modify unrelated 3D geometry, images or large generated `ArtData/*.json` files solely for cosmetic version replacement without inspecting their schema and actual dependencies.
>
> Reopen the project in a tested compatible Unity Editor; allow package restore and script compilation. Check **no missing scripts**, no broken material/mesh/prefab references, expected GUIDs, scene object hierarchy, and all three scenes and seven prefabs. Run Editor validation, desktop Play, crosswalk yield, gap stop, pause/restart, and verify any repaired XR references only if the required SDK is installed. Run repo validators/grep to find remaining unwanted suffixes. Preserve a before/after report and submit a PR; do **not** merge if any migration acceptance check fails.

## Acceptance gates

- No **active** V4 suffixes in public folder names, menu labels, type names, assembly names, paths and student-facing instructions. Historical changelogs may retain genuine version records.
- Unity GUIDs stable; no missing scripts/prefabs/materials/meshes, no duplicate root/mover, no unexpected package changes.
- Unity Editor compile and desktop Play verified on a real machine. Headset/Quest results explicitly tested or NOT TESTED.
- All class-facing workflow instructions point to the **new** names after migration. Until then, use the actual legacy filesystem path rather than pretend the rename has happened.
