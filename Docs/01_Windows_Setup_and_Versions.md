# Windows setup and versions

Share [the pre-class announcement](Student_Preclass_Announcement.md) first. The student entry point is [Cursor-first workflow](Cursor_First_Workflow.md), not a ZIP download or immediate Unity Hub import.

Start with **Unity 6.3 LTS 6000.3.27f2 or a later tested security-patched LTS update**, **Blender 5.2.2 LTS (or 5.2.3 LTS after an asset/MCP check)**, a current compatible Cursor, Git, Python 3.10+ and uv/uvx. These are starting points, not a requirement to use one patch release forever. Verify newer Unity builds against the URP project packages and newer Blender builds against the source .blend. Historic URP/Input/OpenXR/XR Management baselines are recorded in [Compatibility](Compatibility.md).

1. Create an empty local folder, open Cursor and run [clone/preflight prompt](../Prompts/00_Clone_Preflight.md). Check Cursor sign-in, classroom Pro entitlement if needed, filesystem and terminal permissions, Meta Quest Link PC app and XR hardware.
2. Open an **empty Blender scene and blank URP Unity project**; use [MCP install/update prompt](../Prompts/00_Install_Update_MCP.md) to check existing software-side connectors, install missing, update outdated compatible packages, enable services and verify actual live readbacks in Cursor.
3. Run 1.1 model review and 1.2 student color approval; export the custom car FBX in 1.3 and **generate a new Unity scene from FBXs** in a separate blank URP project.
4. Copy the source-first UnitySource Starter/Editor/Config files plus four FBXs into the student project; compile and build through Unity MCP/Editor. No old .unitypackage or teacher scene is used. Record actual versions and CP0–CP5 evidence.

Do not overwrite working global MCP config or the project manifest and lock file. Keep .cursor/mcp.json local and untracked. Historic release evidence does not establish classroom MCP success.
