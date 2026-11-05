# Windows setup and versions

**Start with Cursor, not Unity.** Follow [the complete student workflow](Cursor_First_Workflow.md), [Windows setup](WindowsSetup.md) and [Prompt 00A](../Prompts/00A_Clone_and_Preflight.md). A student first creates an empty local folder in Cursor and clones GitHub using its terminal.

## Teaching order

1. Check Git, installed Cursor/Blender/Unity/Meta Horizon Link, accounts, course model Pro/quota, workspace trust, Agent terminal/write permission, disk, network and Unity license. Record compatible minimum baselines and *observed* installed versions. Newer compatible software is acceptable after validation.
2. Open a **blank Blender scene** and a **separate temporary blank Unity project** (not the cloned teaching project).
3. Use [Prompt 00B](../Prompts/00B_MCP_Setup_and_Recovery.md). Let Cursor inspect existing Blender add-on/server and Unity package. If missing or older than the latest compatible stable release, install/update by supported upstream methods, preserving config and enabling rollback.
4. Start the Blender MCP service from the add-on panel and Unity MCP from **Window → MCP for Unity**. Configure Cursor with the actual live services. If config changed restart Cursor. Query both applications through **real MCP tools**; record version, scene/path, object counts and Unity Console status. Diagnose failed connections and retry. A running port or configuration file is not evidence.
5. Recolor the vehicle in the student's Blender copy, save `.blend` and FBX. **Only after this** open the cloned Unity teaching project using Unity Hub, check its own MCP package and reverify its connection.
6. Import the FBX and construct the scene with Unity MCP (or reviewed Editor script), validate desktop Play; resort to a teacher-exported `.unitypackage` only when required.

## Source and software compatibility

- Unity 6.3 (6000.3 LTS), baseline 6000.3.27f2, or a newer tested-compatible editor. URP, OpenXR and Input System versions are shipped in `Packages/manifest.json`.
- Blender source assets record Blender 5.2.2; use this or a later build verified to open files without material/data loss.
- Unity MCP upstream: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp); UPM install `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`. The shipped workshop project is historically commit-pinned. Avoid untested development-branch upgrades.
- Blender MCP upstream: [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender); check/install `uv` (Windows `winget install --id=astral-sh.uv -e`), use `uvx mcp-for-blender setup` for supported Cursor/add-on setup and `uvx --refresh mcp-for-blender setup` when an upstream refresh is appropriate. Python 3.10+; uv-managed 3.11 if required.
- Meta XR Core/Meta Horizon Link are **external**; check the current Quest Link PC compatibility requirements on the target machine and run an actual headset test.

Keep local MCP servers on localhost, keep credentials out of Git, and do not overwrite existing student work. Record status as CONNECTED, FAILED or NOT TESTED for each application. For historical assets named V4, see [version suffix migration](Version_Suffix_Migration.md).
