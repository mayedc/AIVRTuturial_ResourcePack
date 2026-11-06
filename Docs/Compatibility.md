# Compatibility and minimum starting points

Newer software is welcome **when the existing project and upstream MCP packages still import, run and report a live connection**. Do not describe a historical exact patch as the only supported version.

| Component | Starting baseline / requirement | Acceptance |
|---|---|---|
| Unity Editor | Unity 6.3 LTS **6000.3.27f2 or a later tested 6000.3 patch** | Open/compile/import URP project, assets, input, XR and MCP without errors. |
| Blender | **5.2.2 or newer compatible** | Opens the provided `.blend`, preserves materials/geometry and exports the student FBX. |
| Cursor | Current release compatible with local terminal and MCP | Agent, terminal permission, workspace skills and both live server tools work. |
| Git | Installed, usable by Cursor terminal | Clone and remote verification. |
| Python + uv | Python **3.10+** supported by upstream MCP; `uvx` available | Blender server installs/updates and runs; Python 3.11 can be used if interpreter conflicts occur. |
| Blender MCP | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) latest **compatible** release | Blender add-on/service + Cursor live readback. |
| Unity MCP | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) latest **compatible** release | UPM package, Unity service + Cursor live scene/Console readback. |
| URP / Input / OpenXR / XR Management | Legacy project: URP 17.3.0 / Input 1.20.1 / OpenXR 1.16.1 / XR Management 4.7.0 | Restore the required compatible packages in the target Unity Editor; do not mix manifest/lock arbitrarily. |
| Quest Link + Meta XR Core | Compatible Windows Quest Link PC application, OpenXR runtime and tested external Meta package | Verify with actual Quest 2 / 3 / 3S headset; no device pass is claimed by repo history. |
| Cursor Pro | Check the **class's** entitlement requirement | User confirms status if Pro features are needed; open-source Blender/Unity MCP do not inherently require Pro. |

The previously published `ProjectVersion.txt` and Unity MCP manifest pins are **historical release evidence only**; they are not part of the current source-only teaching bundle. Each student creates a blank URP Unity project and installs packages compatible with the active Editor.

Read [Cursor-first workflow](Cursor_First_Workflow.md), [Windows setup](WindowsSetup.md) and [historical compatibility matrix](Validation/CompatibilityMatrix.md). Current teaching runtime scripts use the `AIVRWorkshop.Student` namespace and are copied to a new student project. Historical namespaces remain in Git history and clearly marked archival reports. Existing Cursor skills are already inside `.cursor/skills`.
