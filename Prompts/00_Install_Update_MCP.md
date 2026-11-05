# Cursor prompt — install, update, connect, retry

The student has Blender open on an **empty scene** and Unity open on a **temporary blank URP project**. Work only on this machine. Read `Docs/Cursor_First_Workflow.md` and `Docs/Compatibility.md`. Do not open the supplied full workshop scene yet.

**Inspect first:** discover existing Cursor MCP definitions and live tools; check `git`, `uvx`, Python, installed Blender add-on and server version, Unity Package Manager's `com.coplaydev.unity-mcp` entry and Git ref, editor version, active Unity project, ports and Console. Back up any local Cursor MCP configuration before merging; do not overwrite or commit `.cursor/mcp.json`.

**Blender MCP** (official source https://github.com/ahujasid/mcp-for-blender):
- If missing, install uv through an appropriate official method (on Windows `winget install --id=astral-sh.uv -e` if permitted), then use `uvx mcp-for-blender install-addon` (or `uvx mcp-for-blender setup` only after explaining its wider config changes). Configure Cursor's server using `uvx` / a verified absolute `uvx.exe` path and the `mcp-for-blender` package.
- If present and outdated, inspect the proposed change first, then run `uvx mcp-for-blender@latest update`. Restart Cursor and Blender if necessary. Preserve custom add-on modifications and use the upstream dry-run if available.
- Ask the student to enable **Interface: MCP for Blender** in Preferences and start/verify the sidebar service in the Blender 3D View (`N` key). Avoid online generation services; do not assume a separate premium subscription.

**Unity MCP** (official source https://github.com/CoplayDev/unity-mcp):
- Check whether the Unity project already has the package. If absent, install via Unity Package Manager Git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main` or a reviewed compatible stable tag. Use the Unity editor/UPM or a carefully validated manifest edit, not arbitrary files copied into `Assets`. If present, compare its current Git ref with the latest compatible upstream release; back up manifest and lock files, update through UPM only if compatible, and let Unity restore dependencies. Do not blindly switch a functioning class project to an untested beta.
- Ask the student to open **Window > MCP for Unity**, start the service and use **Configure All Detected Clients** or the instructions displayed by this installed version. Confirm Cursor's actual endpoint/transport and restart/re-enable the client if needed.

**Prove live connections:** make read-only MCP calls for Blender (application version, active .blend/unsaved state, object count) and Unity (project path, editor version, active scene, Console errors). Never use only CLI version output, server indicators or guessed tools as proof.

**Recovery loop:** on a failure, identify which of client/tool discovery, uvx PATH/Python, Blender add-on/service, Unity package/Console/instance, port/transport, firewall or permissions failed; apply a single safe fix; retry both real MCP readbacks. If blocked by a user GUI action, give the precise menu and resume after the student completes it. End with a connection table **CONNECTED / FAILED / NOT TESTED**, evidence, versions and next actions. Only print **BOTH MCP CONNECTIONS VERIFIED** if both live reads succeed. When the real Unity workshop project is opened later, repeat the Unity readback.
