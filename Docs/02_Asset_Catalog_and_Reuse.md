# Asset catalog and reuse

## Files

| Stem | Contents | What a student may edit |
|---|---|---|
| AsterGT | Two-seat wedge, about 4.9 m long | Body surface, tires, hubs, brakes, glass, lamp strips, seats, trim, screen, yoke, jet nozzles |
| NomaRobot | Armored figure, about 1.8 m | Fifteen bones, armor regions, joints, five-finger hands, in-place walk on frames 1-31 |
| MeridianCity | 8 m road with buildings on both sides | Shopfronts, floors, facades, glass, canopies, lamps, signs, bollards, plants, crosswalk, 6 m gap |
| JetFX | Two jet beams and a shock ring | Emissive meshes toggled at runtime. This is not a particle or fluid simulation. |
| Road_Straight12 | 12 m straight module | Lane lines, curbs, sidewalk |
| Road_Crosswalk12 | 12 m crosswalk module | Nine crossing stripes and a stop line |
| Road_Gap12 | 6 m open gap inside a 12 m module | Deck ends, hazard edges, girders |
| Workshop_Master.blend | Assembly of the main assets | Full car, robot, and street for a driver view. Blender only. |

The first seven names have both `.blend` and `.fbx` under `SourceArt`. Counts of objects and triangles are in `SourceArt/asset_metrics.json` and `SourceArt/unity_asset_metrics.json`.

Unity scenes do not instance the seven prefabs. They contain an unpacked hierarchy that references the same mesh and material GUIDs. Editing a prefab does not update `Workshop_Desktop.unity` or `Workshop_MetaVR.unity`.

## Units, axes, and names

- Blender: metres, +Z up, car and robot face -Y.
- Unity native assets: metres, +Y up, car faces +Z. The wheels meet the ground and the vehicle root sits on the ground.
- FBX export already converts axes. After import, read the bounds and the nose direction. If the importer adds a rotation, correct a `Visual` child and leave the drive root on +Z.
- `VehicleRoot` is the art parent. `DriverEyeAnchor` is the driver eye point: Blender (-0.44, 0.12, 1.24), Unity (-0.44, 1.24, -0.12). It is not a per-person XR calibration.
- `M_BodyPaint` is the only classroom recolor target. Leave `M_Glass`, `M_Rubber`, `M_Trim`, and the light materials alone.
- The Unity robot uses rigid armor pieces and `WorkshopRobotWalk`. It does not depend on Humanoid retargeting.
- A Blender `.001` suffix on a repeated part is still a separate editable object.

## Classroom Blender steps

Save a student copy such as `StudentWork/S01/AsterGT_Color_v01.blend` before any MCP edit. The basic exercise does not change topology, bones, scale, or object names. Compare screenshots from the same camera. Tires, glass, and the interior must keep their colors.

To practice Append from an empty scene, append `AsterGT.blend/Collection/01_AsterGT_Editable`. That keeps curves and modifiers. An FBX import is evaluated mesh and drops the modifier stack.

## Round trip into Unity

1. From the student Blender copy, export `VehicleRoot` and its descendants to a new FBX. Omit cameras and lights. Use -Z forward and Y up, the same axes as the teacher export.
2. Import it under a student folder. Do not drop a `.blend` into `Assets`, or Unity will try its own Blender export.
3. Inspect scale, materials, and facing in a separate scene. FBX will not reproduce Blender shader nodes. Map the existing teaching materials or a student material copy.
4. Native meshes and FBX do not stay in sync. To change the look on the route, keep `WorkshopDrive`, `WorkshopSpeedControl`, `DriverEyeAnchor`, the curtain, and the jet references. Hide the original body renderers and parent the new FBX under a `StudentVisual` child. Do not show both bodies.
5. If the FBX brings its own eye point or jet anchors, keep the existing eye point as the only XR parent. Re-check the view and the nose direction.

## Robot animation

The Blender and FBX files contain a skeleton and `Noma_Walk_InPlace_1s` at 30 fps, frames 1-31, with the first and last frames repeated. The designed walk speed is 0.6 m/s. The Unity scenes drive the armor with `WorkshopRobotWalk`. `WorkshopDrive` moves the crossing root.

A teacher who wants the FBX clip must set the Rig to Generic, check the clip, Loop Time, and the feet, then disable `WorkshopRobotWalk` and use one Animator. Do not play both systems, and do not add Root Motion on top of the scripted translation. That swap is not the tested path in this package.

## Modules and cost

Road tiles repeat every 12 m along the route. The deck is 8 m wide and the outer sidewalk span is 12.6 m. The gap is real geometry. Do not cover the city with one collider that bridges the gap. The scene uses two road colliders.

Unity merges surfaces by material, keeps the robot skeleton, and groups the city in 12 m blocks. There is no LOD, lightmap, or occlusion bake. Current materials are URP Lit and Unlit. Unity lighting will not match a Blender Cycles preview.
