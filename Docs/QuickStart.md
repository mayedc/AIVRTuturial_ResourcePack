# Quick start — Cursor first

1. Create a **new empty local folder** and open it in Cursor. Ask Cursor to run [clone and preflight](../Prompts/00_Clone_Preflight.md), which clones `https://github.com/mayedc/AIVRTuturial_ResourcePack.git` into the folder. **Do not download ZIP** or start in Unity Hub.
2. Have Cursor inspect the repository README and check Git, compatible Cursor, Blender >= 5.2.2 (able to open source), Unity 6 >= 6000.3.27f2 (after compatibility test), Quest Link app, accounts/Cursor Pro class access and filesystem/terminal permissions.
3. Open an **empty Blender scene** and a **temporary blank URP Unity project**. Run [install/update MCP prompt](../Prompts/00_Install_Update_MCP.md); enable both software-side services, then require **live readbacks from both** in Cursor.
4. Through Blender MCP append and recolor a **student copy** of Aster GT, save the blend and export FBX.
5. **Only after that export**, use [Unity scene assembly](../Prompts/01_Agent_Blender_Unity.md) through Unity MCP. Use a teacher-tested `.unitypackage` for workshop dependencies if supplied, otherwise follow the safe fallback in [workflow](Cursor_First_Workflow.md). Never overwrite original Unity scenes.
6. Follow [Lesson 3](Lesson03_MetaQuest.md) and [acceptance matrix](Acceptance_Matrix.md) for runtime and device checks.

The repository currently contains a legacy full Unity reference project, not an already-tested `.unitypackage`. Do not claim MCP and headset checks passed until observed.
