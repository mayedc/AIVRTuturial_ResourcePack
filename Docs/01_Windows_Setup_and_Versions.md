# Windows setup and versions

This folder is a Unity project. Open `AIVRTutorial_ResourcePack` itself. Do not copy an older starter `Packages/manifest.json` over this one.

| Item | Recorded choice |
|---|---|
| Unity | Project version file says `6000.3.27f2`. A separate macOS note in the archived teacher pack mentioned `6000.3.28f1`. Repeat import and Play on the editor you will teach with. |
| Render pipeline | URP 17.3.0. Current materials use URP Lit and URP Unlit. `WorkshopSurface.shader` and `WorkshopGlass.shader` remain as teaching source and are not assigned by the current materials. Built-in and HDRP were not accepted. |
| Blender | Source files were saved from Blender 5.2. Open the same minor version when you can. Older Blender may not open the `.blend` files; use the FBX and then check materials and the skeleton. |
| OpenXR | 1.16.1 is in `Packages/packages-lock.json`. Android Meta Quest Support is enabled for Quest, Quest 2, Quest Pro, Quest 3, and Quest 3S. |
| Meta XR Core | Not installed. `Workshop_MetaVR.unity` still references its camera rig. See [XR and Quest acceptance](05_XR_and_Quest_Acceptance.md). |
| Cursor / MCP | Install on the classroom machine and record the tested version. Do not change a working global configuration during a lesson. |

Before class, fill a CP0 record: Windows version, GPU and driver, Blender version, Unity version, URP version, Cursor version, Python or uv version, both MCP versions or commit hashes, OpenXR and XR Management versions, Quest system version, and the connection method. A blank cell is not a locked version.

## Blender MCP

Use the [mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) server. On Windows, `uvx` can start it. If the Blender add-on cannot find the command, point it at the full `uvx.exe` path. Order: install uv, install the matching add-on, enable it and start the local connection, then enable the project MCP entry in Cursor.

`.cursor/mcp.example.json` is an example to merge by hand. Pin `mcp-for-blender` to the version you tested. Do not overwrite an existing `.cursor/mcp.json`. Keep the example on local Python 3.11 and turn off unused online asset search, paid generation, and telemetry.

Blender Python can change the open scene. Class work uses a student copy: read the scene, recolor, then save a new file.

## Unity MCP

The project manifest includes [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp). `packages-lock.json` currently pins commit `81542a7e86292b5c4c21b1782c5af23b567f45ce`. The manifest line still says `#main`. Do not ask a class to float on `main`.

Start the local MCP service from the Unity window and put its address in Cursor. The example is `http://localhost:8080/mcp`. Match that address to the [transport documentation](https://github.com/CoplayDev/unity-mcp/blob/beta/website/docs/architecture/transports.md) and to the value shown by the installed package. Do not expose the port on the public internet.

## Evidence of a real connection

Run [Prompt 00](../Prompts/00_Connection_and_Scope.md). The agent must return the Blender file path, version, object count, and whether `VehicleRoot` exists, plus the Unity project path, editor version, active scene, and Console error count. A green status light or a generated config file is not that evidence.

If MCP is down, teach the concept from the desktop applications and mark the practical as "connection not finished". Command-line art tools are for teachers. They are not a substitute for the MCP lesson.
