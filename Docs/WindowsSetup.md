# Windows setup — preflight for Cursor-first workshop

The **student starts in Cursor, not Unity Hub**. Read [Cursor-first workflow](Cursor_First_Workflow.md) and [Prompt 00A](../Prompts/00A_Clone_and_Preflight.md) for the order, permission checks and actual application/MCP readback requirements.

## Compatible baseline (not an exact-version ceiling)

| Application/dependency | Shipped baseline / requirement |
|---|---|
| Windows | Supported 64-bit Windows PC with GPU and USB capabilities checked for Meta Horizon Link |
| Cursor | Working recent Cursor Agent and terminal; check course-selected model's Pro plan/quota, trusted workspace and file/terminal permissions |
| Git | Installed and accessible from Cursor terminal |
| Unity | Unity 6.3 (6000.3) LTS at least the recorded 6000.3.27f2 patch, or a later version actually verified to import/compile/Play this project |
| URP / Input / OpenXR | Shipped references: URP 17.3.0, Input System 1.20.1, OpenXR 1.16.1; allow package-compatible updates only after validation |
| Blender | 5.2.2 as recorded in the shipped asset metadata, or newer if it can correctly open the supplied .blend and preserves materials |
| Unity MCP | Installed through official Unity Package Manager Git URL: `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`. Existing shipped historical commit is not necessarily current |
| Blender MCP | Official `mcp-for-blender` with `uv`/`uvx` and compatible Blender add-on; Python 3.10+; uv-managed Python 3.11 if needed |
| Meta VR | Meta Horizon Link PC app, actual Quest 3/3S, compatible Meta XR Core SDK, working USB data cable and PC OpenXR runtime; optional and externally installed |

## Student setup

1. Create and open an **empty local folder in Cursor**. In its terminal execute `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .` only when empty. Check `git remote -v`, `git status`, the README and file permissions. **Do not open the Unity teaching project yet**.
2. Run the software/account/permissions checks from [Prompt 00A](../Prompts/00A_Clone_and_Preflight.md).
3. Open an **empty Blender scene** and a **separate temporary blank Unity project**. Run [Prompt 00B](../Prompts/00B_MCP_Setup_and_Recovery.md). Cursor inspects existing connectors and updates missing/old versions through the supported upstream mechanisms, backing up settings and testing compatibility. Let the student start the Blender and Unity application-side MCP services and let Cursor query both **live** scenes.
4. Save the student Blender recolor and FBX **before** opening the cloned workshop Unity project.
5. Only then open the cloned project with Unity Hub. The temporary project's Unity MCP does **not** guarantee the workshop has a compatible package: inspect the workshop's Package Manager, start/reconfigure its MCP and demand a second live readback.
6. Use [Unity automation prompt](../Prompts/01A_Unity_Automation.md) and the [package fallback](../Prompts/01B_ExportPackage_Fallback.md) if required.

Do not expose local MCP ports publicly. Do not commit `.cursor/mcp.json`, credentials, `Library`, `Logs` or `UserSettings`. Preserve student files when updating. Version records are evidence, not proof of functionality. Verify Console, Blender scene, Unity Play and Quest Link separately.
