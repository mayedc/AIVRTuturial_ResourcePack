# Lesson 01 — Blender vehicle color

## Objectives

- Open the prepared car through Cursor and Blender MCP.
- Identify `M_BodyPaint`.
- Change only that material on a student copy.
- Save a separate `.blend`. Do not overwrite `SourceArt/Blender/AsterGT.blend`.

## Prerequisites

Desktop Unity scene has been opened once so students know the car they are editing. Blender MCP is connected, or the teacher marks the connection as unfinished and demonstrates the material in Blender directly.

## Duration

90 minutes.

## Required software

Blender 5.2.2 LTS when available, Cursor, and the Blender MCP server from `.cursor/mcp.example.json`. Unity is not required for the color edit.

## Steps

1. In Blender, save a copy such as `StudentWork/<student-id>/AsterGT_Color_v01.blend`. Create `StudentWork` outside `SourceArt`.
2. Append or open that copy. The teacher collection name is `01_AsterGT_Editable` inside `SourceArt/Blender/AsterGT.blend`.
3. Select the body material `M_BodyPaint`. Leave `M_Glass`, `M_Rubber`, `M_Trim`, and the light materials unchanged.
4. Set the base color. One checked example is linear RGBA 0.55, 0.025, 0.045, 1. Students may pick another visible color if they record the values.
5. Optional helper, on the copy only: `Tools/blender_safe_recolor.py`. It does not save to disk by itself.
6. Save As again if you iterate. Compare object count and bounds with the teacher file.

## Copyable prompt

Use `Prompts/Blender/RecolorBody.md`.

## Expected results

The student file shows a new body color. Tire, glass, skeleton, eye point, and scale match the teacher file. The teacher `.blend` is unchanged.

## Validation checklist

- Student path is not `SourceArt/Blender/AsterGT.blend`.
- Material name read back is `M_BodyPaint`.
- No new mesh objects were required for the color change.
- Screenshot: missing visual asset unless the student captures one locally. Do not invent a render.

## Troubleshooting

If MCP returns no file path, stop and fix the add-on connection. If `M_BodyPaint` is missing, the wrong file is open.

## Deliverable

A student `.blend` plus a short note: Blender version, material name, color values, and confirmation that the teacher file was not overwritten.
