# Cursor prompt · Blender FBX → Unity scene via MCP

Prerequisites: CP1 Blender `StudentWork/<group>/AsterGT_Color.blend` and FBX exist; both current MCP connections have been live-tested. **Only now** close the temporary Unity sandbox and open the cloned repository root (`Assets/Packages/ProjectSettings`) through Unity Hub. Re-check/upgrade `com.coplaydev.unity-mcp` **in this workshop project**, start its service and verify the new Unity project path/scene/Console through live MCP.

Use `workshop-unity-lesson`; do not overwrite teacher originals.

1. Inspect the actual scene and existing components using Unity MCP. Duplicate `Assets/AI_VR_Workshop/Scenes/Workshop_Desktop.unity` to a unique student checkpoint and make that copy active. Do not alter original `.unity` or `.meta` GUIDs.
2. Import the exported FBX into `Assets/StudentWork/<group>` via Unity MCP if supported. Verify file existence, metres, forward direction, renderer hierarchy and materials. Create/remap a separate URP Lit body material so the edited color is visible.
3. Under `AsterGT`, add exactly one `StudentVisual` child referencing the new FBX; align it with original visuals, avoid double bodies by disabling only old mesh renderers. Preserve `WorkshopDrive`, `WorkshopSpeedControl`, robot/yield references, `DriverEyeAnchor`, jets, `ComfortCurtain`, the gap and both road colliders. Never duplicate an entire moving car.
4. Use current **actual Unity MCP tools** to build/edit scene, assets, hierarchy and components. If a specific tool cannot import/copy/attach, **explain the gap** and create a minimal reviewed Editor script under the student folder (never edit raw scene YAML), run and verify it through Unity. If scripting also fails, request instructor's validated Unity export package and follow `01B_ExportPackage_Fallback.md`.
5. Save; compile; read Console; run **Workshop → Validate active workshop scene**; Play and verify fixed-speed baseline, yield, robot crossing, stop before the gap, pause and restart. Provide a CP2/CP3 checklist of actual tool evidence, screenshots, paths and any untested items. Do not describe a successful import until it appears in the live Editor.
