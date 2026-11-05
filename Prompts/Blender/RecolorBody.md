# Blender body paint — helper for student Prompt 1.2 only

This is a **reference specification**, not permission to execute other lesson stages. Students must first finish [Prompt 1.1](../01_1_Review_All_Blender_Models.md), then fill their color in [Prompt 1.2](../01_2_Choose_Car_Color.md). **Do not override student choice with hardcoded red.**

- Original teacher source: `SourceArt/Blender/AsterGT.blend` (read-only).
- Collection: `01_AsterGT_Editable`.
- Sole recolor target: `M_BodyPaint`.
- Default if the student leaves the selection empty: red linear RGBA `(0.55, 0.025, 0.045, 1)`.
- Allow a written color name or hex sRGB color, converting to the Blender shader color space correctly.
- Save As to a new `StudentWork/<group>/AsterGT_Color.blend` **before** editing, never overwrite existing student work.
- No geometry, bones, glass, rubber, trim, lighting, eye anchor, or scale changes. Do not run art generators or rebuild the model.
- Through Blender MCP read back color, object count and scale. Give the student a chance to visually approve.

**STOP after recolor. No FBX export and no Unity operations in Prompt 1.2.**
