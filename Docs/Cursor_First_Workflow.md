# Cursor-first classroom workflow (Windows)

**Canonical student order:** empty local folder → Cursor clones GitHub → preflight → empty Blender + temporary empty Unity project → Cursor checks/installs/updates MCP → start the application-side services → live MCP verification → Blender body-color edit + FBX export → open the cloned **workshop** Unity project → MCP-driven FBX import/scene construction → desktop exercise → optional package fallback → Quest Link.

The temporary empty Unity project is only an MCP connection sandbox. **Do not open the workshop Unity project until after the Blender recolor exercise.** The GitHub repository already includes `Assets`, `Packages`, and `ProjectSettings`; do not delete or re-create them.

## CP0 · Before the class starts

Check each student computer and record *observed* versions and status; versions below are minimum **compatible baselines**, not a demand to install one exact patch:

| Requirement | Compatibility baseline / action |
|---|---|
| Windows, GPU, disk | Supported 64-bit Windows PC with sufficient GPU/USB performance for Meta Horizon Link; verify against Meta's live PC compatibility checker. |
| Cursor + Git | Current working Cursor with Agent and terminal enabled, and Git on PATH; sign in. Confirm whether the class's chosen Agent/model needs an active **Cursor Pro** subscription or quota. Do not claim Pro is necessary for all Cursor use. |
| Blender | Blender **5.2.2 LTS or a later version confirmed to open the provided** `.blend` source files and preserve materials. Do not assume every newer major release is automatically compatible. |
| Unity + Hub | Unity **6.3 LTS (6000.3)**, at least the project's recorded **6000.3.27f2** patch, or a newer editor **validated with this project**, URP/OpenXR and MCP. Prefer a later patch in the same LTS line; do not upgrade major versions blindly. |
| Python + uv | Python **3.10+** for MCP; use `uv` and, if needed, uv-managed **Python 3.11** for reproducible Blender MCP. |
| Meta | Meta **Horizon Link** PC app, Quest 3/3S, tested USB data cable, active PC OpenXR runtime and a compatible Meta XR Core SDK for the optional VR lesson. The Meta SDK is not bundled. |
| Access | Folder is writable; Cursor terminal, Agent tool permissions, trusted workspace and local `.cursor` MCP settings are enabled. Confirm GitHub read access, package registry/network access, Unity license, Windows Firewall/Defender permissions and USB access. |
| Safety | Use a student branch/copy. Keep teacher originals untouched; never commit credentials or `.cursor/mcp.json`. Disable unused paid asset-generation integrations. |

Read `ProjectSettings/ProjectVersion.txt` and `Packages/manifest.json` for the shipped baseline. Future compatible patches are acceptable only after a real import/compile/Play test. `Docs/Compatibility.md` records **historical build versions**, not a fixed software ceiling.

## CP0A · Create the folder in Cursor and clone

1. Create a new **empty** local folder, e.g. `Documents/AI_VR_Workshop`. In Cursor, select **File → Open Folder** and open it.
2. Open the Cursor terminal. Check `git --version`, `git status` and directory contents; if the folder is not a Git checkout and is empty, run:

   ```powershell
   git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .
   ```

   The final `.` means clone **into the already-open empty folder**; do not create another nested directory.
3. Verify `README.md`, `SourceArt/Blender`, `Assets`, `Packages` and `ProjectSettings`. Read `AGENTS.md`; set up a personal working branch or separate checkpoint directory. Never overwrite non-empty local work.
4. Use [Cursor preflight prompt](../Prompts/00A_Clone_and_Preflight.md). If Git authentication or write access fails, stop and report the exact issue before proceeding.

## CP0B · Start two empty applications and install MCP from Cursor

1. In Blender, open an **empty startup scene**. In Unity Hub, create/open a **separate temporary blank 3D/URP Unity project** for MCP setup; this is **not** the cloned workshop project.
2. Ask Cursor to run [MCP setup prompt](../Prompts/00B_MCP_Setup_and_Recovery.md). It must inspect installed versions/configurations before installing/updating. Use official upstreams: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) and [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender). **Prefer the upstream supported installer/package manager**, not an arbitrary repository ZIP or a `git clone` into Unity `Assets`.
3. Blender MCP: check `uv`/`uvx` and existing add-on; if missing or outdated, use the **official `uvx mcp-for-blender setup` flow** (and `uvx --refresh mcp-for-blender setup` for an upstream refresh). Let setup install/upgrade the Blender add-on and configure **Cursor**, while preserving/backing up existing MCP entries. If needed use `uvx mcp-for-blender install-addon`. Close and restart Cursor fully if configuration changed.
4. Unity MCP: check Package Manager for `com.coplaydev.unity-mcp`. If absent, use the official UPM Git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`, or the latest **verified compatible stable** release. If an older commit is pinned, update it **only in the student copy**, allow Unity to update `packages-lock.json`, and restore the previous package lock if compilation fails. Do not assume the upstream development `beta` branch is class-safe. The repository currently carries a historical pinned commit, so simply reopening the project is not a latest-version check.
5. In the Blender **MCP for Blender** sidebar, make sure its service is running (start it if needed). In the Unity **Window → MCP for Unity** window, start/check the local service and use **Configure All Detected Clients** or the endpoint shown there. Keep transport/port settings matched; never expose MCP ports publicly.
6. Cursor must now query **both live applications** through their MCP tools, not simply report that a port or JSON file exists. For the initially empty scenes return: application versions, file/project path, active scene, object/GameObject count and Unity Console error count. Mark each **CONNECTED / FAILED / NOT TESTED**. If failed, diagnose and repeat until a live query works or report an explicit blocker.

## CP1 · Blender color before opening the workshop Unity project

Use [the Blender exercise](Lesson01_Blender.md) and [recolor prompt](../Prompts/01_Blender_Import_and_Recolor.md). Through Blender MCP append the instructor car collection into the **empty Blender scene**, save a personal `.blend`, change **only `M_BodyPaint`**, read the value back, compare object counts/bounds and export selected vehicle parts to `StudentWork/<group>/AsterGT_Color.fbx`. Preserve the original `SourceArt` files. Reopen/check the new file. If Blender MCP fails, do not claim an automated result.

## CP2–CP3 · Open Unity after CP1; automate import and scene setup

1. Stop/close the temporary blank Unity project. In Unity Hub choose **Add project from disk**, select the **cloned GitHub folder** (it contains `Assets`, `Packages`, `ProjectSettings`) and open it with a compatible editor.
2. Check `com.coplaydev.unity-mcp` in the workshop project's Package Manager; the installed temporary project's MCP does **not** automatically install into another Unity project. Check for/update the older pin using the same compatibility and rollback procedure. Start its local MCP service and let Cursor read back this **new project's** path, active scene and Console status.
3. Ask Cursor to use [Unity round-trip prompt](../Prompts/01A_Unity_Automation.md). First create a personal copy of `Assets/AI_VR_Workshop/Scenes/Workshop_Desktop.unity`; then import the exported FBX, map its material to URP Lit, create/replace **one `StudentVisual` child** on `AsterGT`, align axes and scale, disable duplicate original renderers, preserve all gameplay scripts, `DriverEyeAnchor`, robot, jets, road colliders and serialized references.
4. All possible actions should be issued through **Unity MCP**, including scene creation and component/asset edits. If a tool cannot perform a specific action, Cursor may generate a minimal reviewed **Unity Editor script** and run it through the editor on a checkpoint. Do **not** silently edit scene YAML or invent an MCP API.
5. Compile, inspect Console, validate the active scene from **Workshop → Validate active workshop scene**, and run desktop Play: stop for robot crossing, resume, hold before the gap, pause/restart. Save screenshots and the new scene as CP2/CP3. A stale successful report is not a pass.

## Fallback: teacher-exported Unity package

If MCP or an Editor script cannot reliably complete scene/script insertion, the instructor prepares a **validated** scene in Unity, selects the required scene/assets/scripts and uses **Assets → Export Package… → Include dependencies**, saving a named `.unitypackage`. During class students choose **Assets → Import Package → Custom Package…**, review the manifest and imported paths, and import into a **copy** of their project; avoid replacing newer student work. The instructor's package is not pre-bundled and must not be marked available until it exists. See [fallback prompt](../Prompts/01B_ExportPackage_Fallback.md).

## CP4–CP5 · Script exercise and optional Quest Link

Continue [Lesson 3](Lesson03_MetaQuest.md) from the validated desktop checkpoint. First verify speed/flight in desktop Play, then copy the scene for a tracked rig. Check the Meta package, Link connection, two eyes, head tracking and seated height **on actual hardware**; do not claim a Quest pass based on a scene screenshot.

## Recovery loop (repeat live verification)

- **No tools in Cursor:** inspect MCP settings, run setup/configure for the detected Cursor client, restart Cursor, check that the server is enabled and trusted.
- **Blender no response:** check Blender add-on version/enabled state, N-panel service, matching localhost port, Python/`uvx` PATH, Windows firewall; retry a read-only scene query. Don't run duplicate Blender servers.
- **Unity no response:** verify the **currently open Unity project**, package compile, Window → MCP for Unity service, exact transport URL and Console errors; reconfigure/restart local endpoint, retry a read-only scene query.
- **Old or conflicting package:** back up manifest/lock/config first, update **one** plugin at a time to a current compatible release, restore known-working revision on failure and record the mismatch. Do not delete an existing `mcp.json` or override all settings.
- **Permission failure:** verify workspace trust and Cursor Agent terminal/file permission, disk write access, Git credentials and restricted network/proxy rules.
- **FBX/scene failure:** inspect file exists, import path, transform, material/shader, duplicated visuals, script references, Console and active scene. Retry one scoped fix at a time.
- **No real MCP readback:** status remains FAILED/NOT TESTED; provide the blocking output and teacher fallback rather than a fictitious connection success.
