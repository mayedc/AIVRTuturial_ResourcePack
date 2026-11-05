# Safe local recovery — previous S01 all-in-one run (teacher-only)

This prompt must run **in Cursor on the Windows computer that actually has the prior outputs**. GitHub cannot revert local Blender/Unity state. Use this as a **reversible backup-and-isolate operation**, not a destructive repository reset. Reply in Simplified Chinese.

The previous execution report identified:
- `StudentWork/S01/AsterGT_Color.blend`: red car material (linear 0.55, 0.025, 0.045, 1).
- `StudentWork/S01/AsterGT_Color.fbx`: reportedly **1,151,724 bytes**, 186 objects, -Z forward/Y up.
- Student Unity project `VRAITest1`, where `Tools/Install-Workshop.ps1` copied `Assets/AI_VR_Workshop_V4`.
- Student scene inside that copied folder: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop_Student.unity`.
- Only the first ~8 seconds of Play sampled; **full drive never verified**.

## Safety and inspection

1. Determine absolute real paths for both the **repository** and the separate **VRAITest1** project. Ensure they are not accidentally the same root. Read `git status --short`, `git diff --name-only` and branch/remote without modifying Git. Verify each listed artifact's existence, size and time. Do **not** run `git reset --hard`, `git clean -fd`, any forced checkout, or delete `Library`/settings.
2. Stop Unity Play and let the student save other unsaved work. Close Unity (after preserving the student scene in backup) before moving its Assets folder or `.meta` files. Preserve any unrelated unsaved Blender work before loading an empty scene.
3. Create an **external timestamped backup** such as `Documents/Workshop_Backups/S01_<timestamp>`, **outside** both Git repo and `VRAITest1`. Write an inventory with source paths, sizes, timestamps, available hashes and restore destinations. Do not put backup under Unity `Assets`.
4. Move **only positively identified prior S01 test files** to backup, never delete: `StudentWork/S01/AsterGT_Color.blend`, its run-generated `.blend1` if clearly linked, `AsterGT_Color.fbx` and its known local sidecars. Leave other `StudentWork/S01` files untouched.
5. In `VRAITest1` **only**, compare copied `Assets/AI_VR_Workshop_V4` against the teacher original and inventory all extra files. The copied folder should contain the generated student scene. If another student edited it or it includes unrelated files, **STOP this part** and report the conflict; do not sweep it. Otherwise move this copied folder **and its matching root `.meta`** into the external backup. Never touch the original repository `Assets/AI_VR_Workshop_V4` or original `Workshop_Desktop.unity`.
6. Keep `VRAITest1` itself, its `Packages`, `ProjectSettings`, Unity MCP installation, local Cursor MCP configuration, Blender MCP add-on, and caches. Reopen a **blank Blender scene and blank Unity scene**, then test read-only Blender and Unity MCP calls. If a previous student-only Build Settings scene reference causes an error, back up settings and remove only that explicitly identified stale entry.
7. Show a table: each known test path, FOUND/MOVED/BLOCKED, external backup destination, original teacher paths unchanged, `git status` before/after, both live MCP statuses. Supply the reverse move instructions and mark incomplete checks **NOT VERIFIED**.

**STOP after recovery. Do not automatically execute Prompt 1.1.** The teacher/student will separately paste `Prompts/01_1_Review_All_Blender_Models.md` for a clean first test.
