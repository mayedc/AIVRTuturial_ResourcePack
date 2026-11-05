# Source-first asset inventory

**No premade Unity scene or prefab bundle ships in this repository.** Historical V4 Unity assets were removed; they are available through Git history only. Students build a new scene in their own blank URP Unity project.

| Model | Repository source | Role in 1.3 |
|---|---|---|
| AsterGT | SourceArt/Blender/AsterGT.blend and SourceArt/FBX/AsterGT.fbx | Student exports their *custom* AsterGT_Color.fbx instead of using teacher stock FBX |
| NomaRobot | SourceArt/Blender/NomaRobot.blend and SourceArt/FBX/NomaRobot.fbx | Imported robot and rigid walk |
| MeridianCity | SourceArt/Blender/MeridianCity.blend and SourceArt/FBX/MeridianCity.fbx | Imported road/street, crosswalk, gap |
| JetFX | SourceArt/Blender/JetFX.blend and SourceArt/FBX/JetFX.fbx | Imported jet visual, initially inactive |
| Three Road_* modules | SourceArt/Blender and SourceArt/FBX | Optional reference modules, not imported by default |
| Workshop_Master | SourceArt/Blender/Workshop_Master.blend | Blender-only reference assembly |

The build also imports four Starter C# scripts, two Editor C# scripts and the JSON scene spec from [UnitySource](../UnitySource/README.md). Students create their own Unity .unity scene from these sources. Historical mesh counts in SourceArt or Docs/Validation are **not** new source-first Unity Play results.
