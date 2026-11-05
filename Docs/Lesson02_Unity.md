# Lesson 2 — Blender recolor first, then MCP-driven Unity integration (45 minutes)

**Important:** the cloned Unity workshop project is opened **only after the Blender color is modified and exported.** The temporary blank Unity project used for MCP connection checks is separate.

## 00–25 | Blender material change (CP1)

Follow [Blender lab](Lesson01_Blender.md) and [Prompt 01](../Prompts/01_Blender_Import_and_Recolor.md). In an initially blank Blender scene, use live Blender MCP to append `01_AsterGT_Editable`, save a student copy, change only `M_BodyPaint`, verify readback and export FBX.

## 25–45 | Unity project open, MCP reconnection and automated scene (CP2–CP3)

1. Close the temporary empty Unity sandbox. Through Unity Hub, **add/open the cloned repository root** containing `Assets`, `Packages` and `ProjectSettings` with a compatible editor.
2. Check the workshop project's installed `com.coplaydev.unity-mcp` dependency, update only if needed/compatible, start the local MCP service and have Cursor read back this **workshop** project and its Console.
3. Run [Prompt 01A](../Prompts/01A_Unity_Automation.md). Cursor uses **Unity MCP** to duplicate the prepared scene, import the Blender-exported FBX, map URP materials, and add a single `StudentVisual` under `AsterGT`. Do not overwrite original teacher scenes or disturb drive, speed, robot, eye anchor, jets or road collider references.
4. For an operation not covered by MCP, use the smallest reviewed Editor script on a checkpoint, then validate in Unity. If that is blocked too, have the teacher export and validate a `.unitypackage`; students use **Assets → Import Package → Custom Package…** with manual conflict review. See [fallback](../Prompts/01B_ExportPackage_Fallback.md).
5. Check Console, run **Workshop V4 → Validate active workshop scene** while the legacy physical path is still in use, then Play. Confirm 0.85 m/s baseline, crossing yield and gap stop, pause and restart. Save CP2/CP3.

Historical path names have a V4 suffix in the distributed Unity project. Do not rename files independently before [the coordinated migration](Version_Suffix_Migration.md).
