# Prompt 1.2 — Student-selected vehicle recolor (Blender ONLY)

**Student edit field (fill before pasting):**

**Desired vehicle body colour (leave blank for the default red):** ________

Default if empty/underscores: **red**; teacher example `M_BodyPaint` linear RGBA `(0.55, 0.025, 0.045, 1)`. Students may provide a Chinese/English color name, sRGB hex such as `#1E90FF`, or an explicitly labeled RGBA value. Convert hex sRGB to linear Blender shader values correctly. Do not silently assume other materials should change.

Run **ONLY stage 1.2** after the student has reviewed **all eight** Blender files in 1.1 and both parties have acknowledged that checkpoint. Read `AGENTS.md`, `Docs/02_Asset_Catalog_and_Reuse.md` and `Prompts/Blender/RecolorBody.md`. Reply in Simplified Chinese.

1. Confirm Blender MCP live readback and the chosen color. Use `SourceArt/Blender/AsterGT.blend` and append `Collection/01_AsterGT_Editable` **once** into a fresh/student scene; never edit or save the teacher original.
2. Before any recolor, save a new student copy `StudentWork/S01/AsterGT_Color.blend` (replace S01 if the group is different). If there is existing student work at this path, create a new version or obtain approval, never overwrite.
3. Change **only** the vehicle body material `M_BodyPaint` to the requested color. Preserve glass, trim, rubber, lights, geometry, scale, bones, modifiers, eye anchor and object names. Do not create a replacement car.
4. Read back the actual shader color, object count/bounds and copy path with Blender MCP. Save/reopen student copy if safe, and let the student visually inspect before/after in Blender. Report the chosen color and any uncertainty about its representation.

**STOP after the student's approval opportunity.** Do not export FBX, open/import/build a Unity scene, or write scripts. Tell the student to independently paste `Prompts/01_3_Export_And_Build_Unity.md` after they like the paint.
