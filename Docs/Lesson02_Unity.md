# Lesson 2 — From Blender material to a running Unity scene (45 minutes)

Use the first 25 minutes for the [Blender lab](Lesson01_Blender.md). Use the remaining 20 minutes to integrate the vehicle visual into the prepared desktop scene.

1. In Unity, use **Workshop V4 > Save active scene as new checkpoint**. Open the copy under `Assets/AI_VR_Workshop_V4/Scenes/`.
2. Import the group's FBX into a separate folder such as `Assets/StudentWork/Group03`. Confirm scale, direction and materials. If needed, extract or remap the imported body material to a separate URP Lit material using the chosen base color.
3. Ask the Agent to add the FBX as the new `StudentVisual` child of `AsterGT`. Align it with the original. Disable the old vehicle mesh renderers individually as needed. Keep the car root, drive and speed components, the eye anchor, and the jet and curtain references. Keep both road colliders and the robot.
4. Run **Workshop V4 > Validate active workshop scene**. Check the Console and the Game view for material problems, duplicate geometry and placement. Save CP2.
5. In Play, observe the fixed 0.85 m/s target, full stop at the crossing, robot clearance, and wait at the gap. Try pause and restart. Save the run notes with CP3. See [desktop checks](Acceptance_Matrix.md).

The Unity scenes use native meshes. Editing the original Blender asset, source FBX, or prefab does not update the unpacked scene objects automatically.
