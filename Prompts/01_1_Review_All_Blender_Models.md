# Prompt 1.1 — Open and review all Blender models (inspection only)

You guide a student, not an end-to-end automation. Read `AGENTS.md` and `Docs/02_Asset_Catalog_and_Reuse.md`. Reply in **Simplified Chinese**. Run **ONLY stage 1.1**. Do NOT recolor, save over any teacher source, export FBX, import Unity assets, edit Unity scenes, write code, or run 1.2–1.4.

**Preflight:** Confirm the repository root and a live Blender MCP readback of the current file/scene. If old student test artwork or unsaved work is open, preserve it and report a safe manual checkpoint; never discard other people's edits. There is no S01-specific rollback step in the classroom workflow. Verify these eight named file paths without a whole-drive scan:

| Model | Exact source path | Inspect in the Blender viewport |
|---|---|---|
| Vehicle | `SourceArt/Blender/AsterGT.blend` | body, wheels, windows, cockpit, paint material `M_BodyPaint`, collection `01_AsterGT_Editable` |
| Robot | `SourceArt/Blender/NomaRobot.blend` | joints, armor, walk animation |
| City | `SourceArt/Blender/MeridianCity.blend` | road, buildings and crosswalk |
| Jets | `SourceArt/Blender/JetFX.blend` | jet beams and ring |
| Straight road | `SourceArt/Blender/Road_Straight12.blend` | road markings and curbs |
| Crosswalk road | `SourceArt/Blender/Road_Crosswalk12.blend` | crossing stripes/stop line |
| Gap road | `SourceArt/Blender/Road_Gap12.blend` | missing deck and separated edges |
| Master assembly | `SourceArt/Blender/Workshop_Master.blend` | complete workshop scene layout |

**Inspect one at a time:** Use supported Blender MCP operations to open each file in the *actual student-facing Blender UI*. After switching, re-establish the server if necessary, then read back active file path, collection/object names and meaningful dimensions or animation presence. Frame the object for viewing without saving the teacher file. If MCP cannot switch a file safely, give the student the exact path and **Blender > File > Open** steps, and verify the active scene through MCP once opened. Do not invent screenshots or marks for files not actually seen. Let the student look around the Blender viewport as you explain what each model contributes.

At completion present one compact inspection table for all eight, with **OPENED / NOT OPENED**, key observations, and whether the student visually reviewed it. Ask the student to acknowledge the review before the next stage.

**STOP.** Say: “请检查以上 8 个 Blender 模型，确认后单独复制 Prompt 1.2，并自行填写想要的车身颜色。” No edits, no FBX and no Unity operations in 1.1.
