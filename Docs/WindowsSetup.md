# Windows setup

Open this repository root in Unity. Do not replace `Packages/manifest.json` with an older project manifest.

| Item | Value |
|---|---|
| Unity | `6000.3.27f2` in `ProjectSettings/ProjectVersion.txt` |
| URP | 17.3.0, asset `Assets/Settings/PC_RPAsset.asset` |
| Input | Input System package 1.20.1. Active Input Handling is the Input System package. |
| OpenXR | 1.16.1. Loader assigned for Standalone and Android. Standalone starts in desktop mode until the instructor enables Initialize XR on Startup in the VR copy. |
| Quest feature | Android Meta Quest Support enabled for Quest, Quest 2, Quest Pro, Quest 3, and Quest 3S. |
| Android player | Min SDK 32, ARM64, IL2CPP. Present on the validation Editor. No APK was produced. |
| Blender | The source uses Blender 5.2.2 LTS. Verify it opens on the classroom machine. |
| Unity MCP | `com.coplaydev.unity-mcp` git URL. Lock commit `81542a7e86292b5c4c21b1782c5af23b567f45ce`. Upstream license: MIT. Not vendored. |
| Blender MCP example | `.cursor/mcp.example.json` runs `uvx` with Python 3.11 and `mcp-for-blender`. |

## Blender MCP

1. Install uv and a Blender build that opens `SourceArt/Blender/AsterGT.blend`.
2. Install the Blender MCP add-on that matches the server you tested. This pack does not include that add-on.
3. Merge the example server entry into Cursor by hand. Keep the real `.cursor/mcp.json` untracked.
4. Connection evidence is a returned file path, Blender version, and the material name `M_BodyPaint`. A status dot alone is not evidence.

## Unity MCP

1. Open the project and use Window > MCP for Unity.
2. Point Cursor at the local URL shown by that window. The example is `http://localhost:8080/mcp`.
3. Ask for the open scene path and the Console error count before any edit.

## Quest Link preparation

Before Lesson 3, check the PC app, USB data cable, active OpenXR runtime, and compatible Meta XR Core package. See the [XR checklist](05_XR_and_Quest_Acceptance.md).

## Classroom record

Write down the Windows version, GPU driver, Unity version, Blender version, Cursor version, and both MCP versions before class. Leave a cell blank if it was not tested.
