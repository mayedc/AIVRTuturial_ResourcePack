# Compatibility and minimum starting points

Newer software is welcome **when the existing project and upstream MCP packages still import, run and report a live connection**. Do not describe a historical exact patch as the only supported version.

| Component | Starting baseline / requirement | Acceptance |
|---|---|---|
| Unity Editor | Unity 6 **6000.3.27f2 or newer compatible Unity 6** | Open/compile/import URP project, assets, input, XR and MCP without errors. |
| Blender | **5.2.2 or newer compatible** | Opens the provided `.blend`, preserves materials/geometry and exports the student FBX. |
| Cursor | Current release compatible with local terminal and MCP | Agent, terminal permission, workspace skills and both live server tools work. |
| Git | Installed, usable by Cursor terminal | Clone and remote verification. |
| Python + uv | Python **3.10+** supported by upstream MCP; `uvx` available | Blender server installs/updates and runs; Python 3.11 can be used if interpreter conflicts occur. |
| Blender MCP | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) latest **compatible** release | Blender add-on/service + Cursor live readback. |
| Unity MCP | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) latest **compatible** release | UPM package, Unity service + Cursor live scene/Console readback. |
| URP / Input / OpenXR / XR Management | Legacy project: URP 17.3.0 / Input 1.20.1 / OpenXR 1.16.1 / XR Management 4.7.0 | Restore the required compatible packages in the target Unity Editor; do not mix manifest/lock arbitrarily. |
| Quest Link + Meta XR Core | Compatible Windows Quest Link PC application, OpenXR runtime and tested external Meta package | Verify with actual Quest 3/3S headset; no device pass is claimed by repo history. |
| Cursor Pro | Check the **class's** entitlement requirement | User confirms status if Pro features are needed; open-source Blender/Unity MCP do not inherently require Pro. |

The `ProjectVersion.txt` editor and the existing Unity MCP commit in `Packages/manifest.json` are historical **reference-project pins**. Student blank-project setup should compare to latest compatible upstream before installation/updating; the instructor must validate changes before replacing reference pins.

Read [Cursor-first workflow](Cursor_First_Workflow.md), [Windows setup](WindowsSetup.md) and [historical compatibility matrix](Validation/CompatibilityMatrix.md). The legacy folder/namespace identifiers ending in `V4` are scheduled for **Unity-verified migration**, not cosmetic replacement in GitHub. Existing Cursor skills are already inside `.cursor/skills`.
