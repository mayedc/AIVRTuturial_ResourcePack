# Windows setup — Cursor first

**Do not download this repository as a ZIP.** Create an empty student folder, open it in Cursor and clone through [Prompt 00: preflight](../Prompts/00_Clone_Preflight.md). Read [compatibility baselines](Compatibility.md) and [full workflow](Cursor_First_Workflow.md). The GitHub repository is **not** a Unity project and does not include a prebuilt teaching scene. The student separately creates a blank URP project in Unity Hub.

See the [pre-class student announcement](Student_Preclass_Announcement.md) for all Windows installers, Cursor Pro, Unity International and Quest 2 preparations.

## Preflight

- Confirm Windows PC/GPU, writable local folder, working Cursor terminal and Git, Cursor sign-in and the class's **Cursor Pro** policy (if applicable); avoid asserting all MCP services are paid.
- Confirm Unity Hub and a **Unity 6 editor at or above the compatible 6000.3.27f2 baseline**, plus a **Blender version at or above compatible 5.2.2** that opens the supplied files. Newer versions need actual validation.
- Confirm Python 3.10+ and `uv/uvx` if not yet installed. For Lesson 3: compatible Quest Link PC app, USB data cable, OpenXR runtime and Meta XR Core package. Headset testing is separate.
- Historical URP/Input/OpenXR/XR Management versions belong to older validation reports. In the current source-first workflow, the **student blank URP project** owns all package versions. Never blindly paste the old repository manifest.
- Check network to GitHub/Unity registry/Python registry, folder/terminal/package permissions and enough disk space. Never commit credentials, local MCP JSON or Unity-generated caches.

## MCP setup on two empty applications

Open an **empty Blender scene** and create an **empty URP Unity project**; do not open the finished workshop scene until after Blender recoloring/export. Run [Cursor MCP install/update prompt](../Prompts/00_Install_Update_MCP.md).

**Blender:** source [mcp-for-blender](https://github.com/ahujasid/mcp-for-blender). Cursor checks existing server and add-on, installs missing with `uvx mcp-for-blender install-addon`, or updates compatible installed releases with `uvx mcp-for-blender@latest update`; it safely merges local Cursor config. Student enables the add-on in Blender Preferences and starts the MCP service from the sidebar (`N`). Verify by reading live Blender version/file/object count.

**Unity:** source [unity-mcp](https://github.com/CoplayDev/unity-mcp). Cursor checks current UPM package; if absent it installs the reviewed compatible Git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main` (or compatible stable tag), and upgrades outdated compatible versions through UPM. Student opens **Window > MCP for Unity**, starts/configures service and Cursor client. Verify through live Unity project/editor/scene/Console readback; discover endpoint/transport from the installed version rather than assuming `http://localhost:8080/mcp` universally.

For failures: check `uvx` executable PATH, Blender add-on/service, UPM import/Console, Cursor tool discovery, local ports, wrong Unity instance, antivirus/firewall and permissions. Make one safe fix and retest real MCP calls. Do not mark completed after installation alone.

## Moving on

Once both connections pass, follow [Blender lab](Lesson01_Blender.md). After the student's 1.2 visual approval, export the custom FBX and **build the entire Unity scene from sources** through [Prompt 1.3](../Prompts/01_3_Export_And_Build_Unity.md) and [UnitySource](../UnitySource/README.md), without any .unitypackage.

Record actual app/MCP versions and connection status. Earlier validation reports are archival, not proof of live classroom success.
