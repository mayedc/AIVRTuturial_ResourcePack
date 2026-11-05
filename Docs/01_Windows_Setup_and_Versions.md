# Windows setup and versions

The student entry point is [Cursor-first workflow](Cursor_First_Workflow.md), not a ZIP download or immediate Unity Hub import.

Start with **Unity 6 6000.3.27f2 or newer compatible**, **Blender 5.2.2 or newer compatible**, a current compatible Cursor, Git, Python 3.10+ and uv/uvx. These are starting points, not a requirement to use one patch release forever. Verify newer Unity builds against the URP project packages and newer Blender builds against the source .blend. Historic URP/Input/OpenXR/XR Management baselines are recorded in [Compatibility](Compatibility.md).

1. Create an empty local folder, open Cursor and run [clone/preflight prompt](../Prompts/00_Clone_Preflight.md). Check Cursor sign-in, classroom Pro entitlement if needed, filesystem and terminal permissions, Meta Quest Link PC app and XR hardware.
2. Open an **empty Blender scene and blank URP Unity project**; use [MCP install/update prompt](../Prompts/00_Install_Update_MCP.md) to check existing software-side connectors, install missing, update outdated compatible packages, enable services and verify actual live readbacks in Cursor.
3. Save and recolor a student Aster GT copy and export an FBX **before** assembling the Unity workshop scene through MCP.
4. Import a teacher-verified workshop .unitypackage manually only if required; recheck Unity MCP after switching projects. Record actual versions and CP0–CP5 evidence.

Do not overwrite working global MCP config or the project manifest and lock file. Keep .cursor/mcp.json local and untracked. Historic release evidence does not establish classroom MCP success.
