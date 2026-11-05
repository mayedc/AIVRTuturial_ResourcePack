# Troubleshooting — Cursor-first workflow

## Local clone
Create an empty writable folder, open it in Cursor and let Cursor run `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .`. If the folder is not empty, stop or choose a new empty folder. Check `git --version` and network. Do not delete existing student work.

## Blender MCP fails
Check `uvx` (including absolute Windows executable path), Python version, `mcp-for-blender` add-on installed/enabled, Blender's 3D View `N` sidebar service, local port and Cursor MCP server. Update compatible older installations using `uvx mcp-for-blender@latest update` after inspecting changes; restart Blender and Cursor if needed. **Retest an actual MCP read** of scene/file/version/object count, not only a status icon.

## Unity MCP fails
Check the currently open **blank URP Unity** project, Package Manager's `com.coplaydev.unity-mcp` from CoplayDev, package restoration, Console errors and correct Unity instance. In **Window > MCP for Unity**, start/configure the service and detected client. Match Cursor endpoint/transport to the installed version; retest live project/scene/Console MCP reads. When switching Unity projects repeat verification.

## Blender to Unity import fails
The supplied repo is a **full Unity reference project**, not a tested `.unitypackage`. FBX is only a visual. Teacher must validate a Unity export package with scene, scripts, prefabs, materials and dependencies in a separate instructor Unity copy before class. Where MCP cannot install scripts or packages, students import the **verified package** manually via **Assets > Import Package > Custom Package**, then resume MCP scene assembly/checks. Do not claim success if blocked.

## Unity compile or behavior fails
Use compatible Unity 6 and required URP/Input/XR dependencies. Read first Console error; never blindly replace `Packages/manifest.json` or delete the package lock. Legacy `AI_VR_Workshop_V4` and `AIVRWorkshop.V4` require a GUID-preserving migration in Unity; do not rename only directory strings.

The starter holds at the gap intentionally. If pause/robot fails, verify `WorkshopDesktopPanel.drive`, `WorkshopDrive`, `WorkshopRobotWalk` and object references; avoid duplicate movers or FBX animation. If the body appears twice, disable duplicate mesh renderers and check student FBX axes and URP material.

## Quest Link
Follow [02_1 configuration, Meta camera prefab and PC Link diagnosis](../Prompts/02_1_XR_Setup_And_Device_Check.md) first. An OpenXR package or old rig GUID is not proof of a tracked camera. If this passes, use [02_2 driver-eye VR scene and real headset test](../Prompts/02_2_Attach_Driver_Camera_And_Test.md): preserve desktop scene, one active HMD camera/listener, seated tracking origin and no double height offset. A headset pass requires student observation of both eyes and head tracking.

Never commit `.cursor/mcp.json`, generated `Library`/`Logs`/`UserSettings` or credentials. See [acceptance matrix](Acceptance_Matrix.md).
