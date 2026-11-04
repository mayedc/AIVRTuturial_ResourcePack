# Asset manifest

Scenes do not stay linked to prefab instances for the city and vehicle. They contain unpacked objects that share mesh and material GUIDs with the prefabs. Editing a prefab does not update the teaching scenes. See `Docs/02_Asset_Catalog_and_Reuse.md`.

| Teaching name | Blender | FBX | Prefab | Scene objects |
|---|---|---|---|---|
| AsterGT vehicle and cockpit materials | `SourceArt/Blender/AsterGT.blend` | `SourceArt/FBX/AsterGT.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/AsterGT.prefab` | `AsterGT` and `AsterGT_Surface_M_*` including `M_BodyPaint` |
| Noma robot | `SourceArt/Blender/NomaRobot.blend` | `SourceArt/FBX/NomaRobot.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/NomaRobot.prefab` | `NomaRobot` bone chain `Pelvis` through hands |
| Meridian city | `SourceArt/Blender/MeridianCity.blend` | `SourceArt/FBX/MeridianCity.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/MeridianCity.prefab` | `MeridianCity` and block materials |
| Straight road | `SourceArt/Blender/Road_Straight12.blend` | `SourceArt/FBX/Road_Straight12.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/Road_Straight12.prefab` | Used as source art; the live street is the city mesh plus `RoadCollider_Main` |
| Crosswalk | `SourceArt/Blender/Road_Crosswalk12.blend` | `SourceArt/FBX/Road_Crosswalk12.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/Road_Crosswalk12.prefab` | Source module. The stop is the drive distance 7.5 m, not a separate waypoint object. |
| Gap | `SourceArt/Blender/Road_Gap12.blend` | `SourceArt/FBX/Road_Gap12.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/Road_Gap12.prefab` | Source module. Colliders are `RoadCollider_Main` and `RoadCollider_Landing`. |
| Jet effect | `SourceArt/Blender/JetFX.blend` | `SourceArt/FBX/JetFX.fbx` | `Assets/AI_VR_Workshop_V4/Prefabs/JetFX.prefab` | `JetFX`, anchors `JetAnchor_L` and `JetAnchor_R` |
| Assembly | `SourceArt/Blender/Workshop_Master.blend` | None | None | Blender only |

Counts from the desktop scene import check: 104 meshes, 271,896 triangles, 0 missing materials.

No texture, font, or audio files are part of this manifest.
