# Cursor-first classroom workflow

This is the current student sequence. It replaces ZIP-first, manual MCP downloads and early opening of the finished Unity scene. It deliberately distinguishes **starting an empty Unity application/project to prove MCP connectivity** from **opening or assembling the workshop content after the Blender export**.

## Gates and ownership

| Gate | Student / Cursor action | Required evidence |
|---|---|---|
| CP-Start | Student creates an empty local folder and opens it in Cursor. Cursor clones the GitHub repository there. | `git remote -v`, branch, README accessible, writable student workspace |
| CP-Preflight | Cursor reads this repository and checks compatible software, accounts, permissions, disk space and XR prerequisites. | Actual versions and explicit passed/failed/not-tested statuses |
| CP0 | Student starts an empty Blender scene and a new blank URP Unity project. Cursor installs/upgrades MCP components; student enables in-app services. | Both apps independently return live file/project identity, versions, object/scene summaries and Unity Console status through MCP |
| CP1 | Cursor uses Blender MCP to append Aster GT, recolor `M_BodyPaint`, save student copy and export FBX. | Reopened `.blend`; material and mesh checks; real FBX path |
| CP2 | **After CP1** Cursor uses Unity MCP to import assets and assemble a student scene. | Correct car orientation, one student visual, robot/road/camera and route references, zero compile errors |
| CP3 | Cursor validates and student observes desktop Play Mode. | Yield, speed, gap hold, pause and restart; record what actually ran |
| CP3 · interaction | After starter Play, student separately runs 1.4 for speed and commanded flight. | Speed/flight observed in desktop Play |
| CP4 · VR readiness | Student runs 02_1 for XR/OpenXR/Meta rig and PC Link self-check. | Real installed prefab and Link session confirmed |
| CP5 · VR cockpit | Student runs 02_2 for driver-eye tracking rig, then wears Quest for Play. | Scene hierarchy plus student-observed stereo/head tracking |

## 1. Clone from Cursor (not ZIP)

1. In File Explorer, create an empty, writable folder such as `D:\AI_VR_Workshop`. Do not precreate `.git`, `Assets` or `Packages`.
2. Open **Cursor > File > Open Folder** and select it. Authorize terminal execution for the local student workspace, not the entire drive.
3. Paste [Prompt: clone and preflight](../Prompts/00_Clone_Preflight.md). Cursor checks for Git and an empty directory, then executes `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .`. If the folder is not empty, it must stop rather than erase or overwrite it; use a new empty child folder.
4. After cloning, re-open/reload the Cursor workspace so the repository skills and instructions are discovered. Keep student outputs in `StudentWork/<group>` outside teacher source directories.

## 2. Preflight: check before installation

- **Hardware/OS:** compatible Windows PC and GPU, sufficient disk for Unity package cache and FBX; Windows write permission, Git and outbound GitHub/UPM/PyPI connectivity; headset data cable/USB and Meta Quest Link PC app for Lesson 3.
- **Software minimum for this pack:** Unity Editor `6000.3.27f2` or a newer compatible Unity 6 version, URP project template and required Input System/OpenXR/XR Management dependencies; Blender `5.2.2` or a newer version proven to open the supplied `.blend`; Git, Cursor, Python 3.10+ and `uv/uvx` compatible with upstream MCPs. Do not downgrade a working editor solely to match a recorded patch.
- **Accounts and permissions:** Cursor signed in; confirm whether class access to **Cursor Pro** is required and active, but do not assert a paid MCP subscription is compulsory. Check free space, terminal approval, read/write rights in student work, Unity Package Manager and Blender add-on preferences.
- **XR:** compatible Quest Link PC app, available Quest 3/3S and tested cable; OpenXR runtime selection and Meta XR Core package are a separate Lesson 3 check, not prerequisites for CP0 desktop MCP.
- **Safety:** never request tokens or credentials in a prompt; do not commit `.cursor/mcp.json`, `Library`, `Logs`, generated Unity project files, or third-party packages. Do not overwrite teacher art or the original scenes.

## 3. Install / update / verify MCP from Cursor

Paste [Prompt: install or update both MCPs](../Prompts/00_Install_Update_MCP.md).

- **Blender source:** [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender). Cursor checks `uvx`, uses the upstream `mcp-for-blender` distribution (no manual ZIP download), installs the add-on if missing, or updates existing components using `uvx mcp-for-blender@latest update` after reviewing changes. Student enables the add-on under Blender Preferences and starts the **MCP for Blender** service in the `N` sidebar.
- **Unity source:** [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp). The upstream Unity package is installed/updated via Package Manager Git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`, **only after compatibility and dependency review**. This clones source through UPM; a separate manual Git checkout is unnecessary. Student uses **Window > MCP for Unity** to start/configure the service and detected Cursor client.
- Keep existing `.cursor/mcp.json` entries, back them up before edits, and merge only missing entries. `.cursor/mcp.example.json` is illustrative, not authoritative for the Unity endpoint or transport; prefer the live Unity window.
- Check both connections with actual **read-only MCP calls**. For blank Blender report version, blend filepath (may be unsaved) and object count. For blank Unity report project path, editor, active scene and Console errors. Repeat the readbacks after switching Unity projects.
- If failure, diagnose in order: tool discovery/client enabled state, PATH to `uvx`, Python/uv and add-on version, in-app services, localhost port and transport, wrong Unity instance, package/Console errors, file permissions, firewall and restart. Make one fix, then **retry live reads**. Never declare success based on an install log or port alone.

## 4. Blender first, Unity scene second

With CP0 passed, run [1.1 review all models](../Prompts/01_1_Review_All_Blender_Models.md), stop, then [1.2 student-selected car color](../Prompts/01_2_Choose_Car_Color.md), stop for student approval. Only then run [1.3 FBX export and Unity scene](../Prompts/01_3_Export_And_Build_Unity.md) and student-operated full Play. After that passes, separately run [1.4 speed and flight](../Prompts/01_4_Speed_And_Gap_Flight.md).

After CP1, Cursor should use Unity MCP to create a **new scene or checkpoint** in the blank URP student project, transfer/reuse required class assets, import the actual FBX and construct the hierarchy. The repository still contains Unity-native meshes and scripted scene references. **Do not pretend a raw FBX contains the whole workshop**: robot, roads, drive scripts, URP materials, colliders, jets and eye anchor must also be imported/created and validated. Prefer the instructor-produced `.unitypackage` for dependencies once available; if not available, the teacher/reference Unity project may be opened **only after CP1** to produce a package or a checkpoint, and its live MCP connection must be reverified.

Through Unity MCP, validate the scene, attach the student car as `StudentVisual`, preserve one mover, robot and two road colliders (with the gap left open), check `DriverEyeAnchor`, and test desktop Play. The agent must distinguish **tool-driven success**, **manual import fallback**, and **not tested**.

## 5. When a .unitypackage is needed

The teacher exports any necessary package **outside the student Prompts**, using a **separate verified local Unity copy**. Export a package with the asset directory, scripts, prefabs, materials, referenced scenes, and dependencies, then import it into a clean compatible URP project and run checks. If the Unity MCP cannot reliably add scripts or import a particular package, the student manually uses **Assets > Import Package > Custom Package**, checks dependencies, and asks Cursor to resume MCP validation and assembly. Do not claim that a package exists in this GitHub repository until one is committed/released and retested.

## Version suffix cleanup

The existing `AI_VR_Workshop_V4` path, `AIVRWorkshop.V4` C# namespace, `AIVRWorkshop.V4.*.asmdef` names and `Workshop V4` menu are **legacy identifiers**. Removing only the visible `V4` text breaks real references. Any future migration must update GUID-aware references and assembly/scene assets in a separate Unity Editor copy, then compile and test it; this is outside the student sequence. Historical release numbers (e.g. `v1.0.0`) are archival release tags and should not be erased.

## 6. VR stages 02_1 and 02_2

After desktop 1.4 passes, student independently copies [02_1 XR/Meta/Link readiness](../Prompts/02_1_XR_Setup_And_Device_Check.md) and confirms the **real PC Link session**. Only then copy [02_2 driver-eye XR camera and headset Play](../Prompts/02_2_Attach_Driver_Camera_And_Test.md). A Unity package's existence does not prove a working Meta rig or live headset. XR startup is a project-level setting: protect the desktop project with a separate VR copy.
