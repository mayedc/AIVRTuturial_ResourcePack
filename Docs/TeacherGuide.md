# Teacher guide — three lessons, 135 minutes

| Lesson | Time | Demonstrate | Student evidence |
|---|---:|---|---|
| [1 · Cursor-first setup](Lesson01_Setup.md) | 20 + 25 min | Create empty folder, open Cursor, clone repository, check software/pro/permissions; start blank Blender and URP Unity; install/update MCP through Cursor; enable services and read both live tools. | Git remote, preflight report, Blender/Unity MCP readbacks (CP0). |
| [2 · Blender then Unity](Lesson02_Unity.md) | 25 + 20 min | Append/recolor Aster GT and export FBX **before** Unity scene assembly; use Unity MCP to import needed classroom assets and build/validate scene. | Reopened .blend, FBX, correct Unity visual/scene, yield/gap test (CP1–3). |
| [3 · Code and headset](Lesson03_MetaQuest.md) | 22 + 23 min | Implement speed/flight, test desktop, attach tracked rig in separate scene and test wired Quest Link where available. | Runtime test and separate headset evidence (CP3–5). |

Before class, install/test **compatible-or-newer** Cursor, Blender, Unity Editor, Quest Link, uv/Python, and package dependencies; confirm the class's Cursor Pro entitlement policy, write and terminal permissions, GitHub access, power, GPU, USB data cables and OpenXR runtime. Never infer a paid subscription is required by either open-source MCP.

**Critical teacher preparation:** the repository holds a **full reference Unity project** and historical checks; no exported `.unitypackage` has yet been validated. Run [Cursor teacher package/refactor prompt](../Prompts/06_Cursor_Refactor_And_Package.md) on a separate Unity copy, export and **clean-import test** the package, including script/URP/robot dependencies, prior to teaching the blank-project route. Maintain a backup reference scene. The 20-minute Unity portion assumes that prepared package is available; without it, use demonstration/recovery time and do not claim a full automated build.

Use [current workflow](Cursor_First_Workflow.md), [acceptance matrix](Acceptance_Matrix.md) and [XR checks](05_XR_and_Quest_Acceptance.md) for gate definitions. Record real software/tool versions and failures rather than copying historical passes.
