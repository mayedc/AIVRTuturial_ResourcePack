# Blender lab — Aster GT body paint (Lesson 2, first 25 minutes)

**Prerequisites:** the GitHub repository was cloned from inside Cursor; an empty Blender scene and a blank URP Unity project have passed both live MCP readbacks. The supplied finished Unity workshop scene has **not** yet been opened.

1. Use Blender MCP to append `Collection/01_AsterGT_Editable` from `SourceArt/Blender/AsterGT.blend` into an empty student scene, without duplicate imports.
2. Save student copy `StudentWork/<group>/AsterGT_Color.blend` **before editing**; never overwrite the source model.
3. Use [recolor prompt](../Prompts/Blender/RecolorBody.md); only modify `M_BodyPaint`, leaving glass, rubber, trim, geometry and eye anchor unchanged.
4. Compare before/after appearance and read back material, object count, scale and bounds through Blender MCP. Save and reopen the student .blend.
5. Export **only the car hierarchy** to `StudentWork/<group>/AsterGT_Color.fbx`, metres, **-Z Forward / Y Up**, evaluated modifiers; report actual path, orientation and bounds.

Record CP1. **Only after the FBX is saved and checked** continue to [Unity assembly](../Prompts/01_Agent_Blender_Unity.md). If MCP is down, resolve the connection instead of silently claiming the GUI action was MCP-driven.
