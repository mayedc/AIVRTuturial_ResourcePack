# Lesson 2 — Blender first, then MCP-built Unity scene (45 minutes)

Use the first 25 minutes for [Blender recolor and export](Lesson01_Blender.md); do **not** open the original workshop Unity scene before the Blender checkpoint.

In the remaining 20 minutes, run [the Unity build prompt](../Prompts/01_Agent_Blender_Unity.md):

1. Reverify Unity MCP is attached to the **correct active blank URP student project**; check project path, editor and Console.
2. Import the student FBX and the **necessary workshop dependencies** (scene/prefabs, materials, scripts, road/city/robot/jet). Prefer a **teacher-tested Unity export package** if available; the GitHub repo currently carries a full reference Unity project, not a verified `.unitypackage`.
3. Through MCP, build a new desktop teaching scene or an independent checkpoint using the original prepared meshes rather than generating new ones. Add one `StudentVisual` car child, keep `AsterGT` mover and script references, separate road colliders and the robot. Validate car orientation (+Z), eye anchor, URP materials and crossing/gap.
4. Use Unity MCP to refresh, inspect hierarchy, check missing scripts and Console, save scene, enter Play and observe 0.85 m/s cruise, crossing yield, robot clearance, gap hold, pause and restart. Record CP2/CP3 as **observed** or **not tested**.
5. If MCP cannot insert scripts, import dependencies or complete a specific step, report the blockage. A teacher may export the contents with [package prompt](../Prompts/06_Cursor_Refactor_And_Package.md); students can manually import it with **Assets > Import Package > Custom Package**, then return to MCP scene checks. Do not mark blocked automation as done.

For a reference-only fallback after the Blender checkpoint, the legacy Unity scene is at `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`. This internal path will be migrated in Unity after the teacher validates the rename.
