# Teacher guide — three lessons, 135 minutes

| Lesson | Timing | Demonstrate | Student evidence |
|---|---:|---|---|
| [1 · Cursor-first + MCP](Lesson01_Setup.md) | 15 + 30 min | Empty folder in Cursor → `git clone ... .` → software/permission preflight → empty Blender/Unity sandbox → version-aware MCP install/update and live readback. | Git remote; installed versions; two actual MCP tool responses. |
| [2 · Blender → Unity](Lesson02_Unity.md) | 25 + 20 min | Recolor in Blender **before opening workshop Unity**, export FBX; then open workshop through Hub, reverify Unity MCP, automate FBX import and student scene setup. | Saved colored Blender copy + FBX, validated Unity checkpoint, observed crossing yield and gap hold. |
| [3 · Behavior and tracked view](Lesson03_MetaQuest.md) | 22 + 23 min | Speed and flight in desktop Play; optionally attach tested Meta rig/Quest Link in a separate copy. | Speed/flight evidence and separately observed headset checks. |

Prepare one instructor reference copy, a blank Unity MCP sandbox, and a tested Unity `.unitypackage` fallback **if** needed. Preinstall compatible Cursor, Git, Blender, Unity Hub/Editor, uv, Meta Horizon Link and test package/network access. Students, not the instructor, should perform the Cursor-terminal Git clone and use MCP installation/update workflow in Lesson 1. Confirm the class-selected Cursor Agent model's Pro/subscription/quota needs; don't imply all Cursor use requires Pro.

Check each machine's file write/Agent permissions, Git access, firewall and Unity license. Back up `Packages/manifest.json`, `packages-lock.json`, and any MCP settings before upgrades. Newer tested-compatible versions are acceptable; version records are baselines, not mandatory exact pins.

For each Agent step: inspect → narrowly edit a student copy → live tool readback → application validation → save checkpoint. Use [complete procedure](Cursor_First_Workflow.md), [student checklist](StudentChecklist.md) and [acceptance matrix](Acceptance_Matrix.md). A failed MCP connection or untested Quest headset must be reported as such.
