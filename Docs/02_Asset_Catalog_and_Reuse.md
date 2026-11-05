# Blender/FBX source catalog — no prebuilt Unity scene

This GitHub repo contains the teacher-original Blender and FBX sources, not a Unity scene, native mesh asset bundle or ready-made Prefab.

| Model | Teacher sources | Student use |
|---|---|---|
| AsterGT | SourceArt/Blender/AsterGT.blend + SourceArt/FBX/AsterGT.fbx | Review car body/cockpit, then recolor the student's own Blender copy and export AsterGT_Color.fbx |
| NomaRobot | Blender + FBX | Inspect skeleton and in-place walk; import FBX in Unity |
| MeridianCity | Blender + FBX | Inspect street, crosswalk and real gap; import FBX in Unity |
| JetFX | Blender + FBX | Inspect jet beams; import FBX inactive in Unity until 1.4 |
| Road_Straight12 | Blender + FBX | Optional road module, not imported by default |
| Road_Crosswalk12 | Blender + FBX | Optional road module, not imported by default |
| Road_Gap12 | Blender + FBX | Optional road module, not imported by default |
| Workshop_Master | SourceArt/Blender/Workshop_Master.blend | Visual reference only, not a Unity scene |

First seven models are available as .blend and .fbx in SourceArt. Historical geometry statistics live in SourceArt/asset_metrics.json.

## Orientation and student art

Blender uses metres, +Z up, vehicle -Y forward. The approved student FBX is exported -Z Forward / Y Up. In Unity the car root moves +Z; expected renderer bounds are approximately 2.41 × 1.61 × 5.14 metres. Unity importers can introduce 0.01 scaling or extra rotations, so inspect the **real** bounds and nose direction, not just the file name.

Blender driver point: (-0.44,0.12,1.24); expected Unity driver eye: (-0.44,1.24,-0.12), relative to the vehicle root. This is a scene reference, not a personal headset calibration.

Only M_BodyPaint changes in 1.2; keep windows, rubber, trim, geometry, bones and eye point. The student color is not necessarily red. FBX import does not carry all Blender node shaders: the source-first builder creates student-owned URP materials. Verify transparent glass and body paint visually.

## Robot and road

The builder expects imported rigid walk bones Thigh_L/R, Shin_L/R and Foot_Sole_L/R; WorkshopRobotWalk animates limbs and WorkshopDrive translates the crossing root. Disable an imported Animator that would double-animate those same bones. If the FBX names differ, inspect/repair rather than marking animation passed.

MeridianCity is the default visible road; do not stack Road_* models at the same coordinates. The builder creates two collider segments with a **real collision gap from z=37 to z=43**; student Play must show a stable hold before the gap.

Student outputs stay in Git-ignored StudentWork/<group> and in a **separate URP project**, according to [UnitySource](../UnitySource/README.md). Do not regenerate teacher meshes during class with old build scripts.
