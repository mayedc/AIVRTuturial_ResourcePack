# Unity integration — Plan B source-first construction contract

**There is no delivered `Workshop_Desktop.unity`, prebuilt Unity Prefab, native mesh bundle or .unitypackage.** A student creates a blank URP Unity project in a separate folder, then Cursor uses Unity MCP and the reviewed [Editor builder](../UnitySource/Editor/WorkshopSceneBuilder.cs) to assemble the scene from real FBXs.

## Source inputs and build stages

1. The student approves their recolored Aster GT in 1.2. Cursor uses Blender MCP to export `StudentWork/<group>/AsterGT_Color.fbx` (-Z Forward/Y Up). Other source FBXs: `SourceArt/FBX/NomaRobot.fbx`, `MeridianCity.fbx`, `JetFX.fbx`.
2. Copy only the four Starter C# scripts, two Editor scripts, JSON spec, and the four FBXs to the **student's** `Assets/WorkshopStudentGenerated/`, preserving any existing student work or `.meta` references.
3. Through Unity Editor/MCP compile the scripts; run **Tools > Workshop > Build Student Scene From FBX**. It refuses to overwrite a preexisting output scene.
4. Run **Tools > Workshop > Validate Student Scene (1.3)**, then inspect real Scene/Game views and personally Play the entire route. Do not mark Play PASS from Editor structure alone.
5. 1.4 changes only **student-owned** `WorkshopSpeedControl.cs` and `WorkshopDrive.cs`. 02_2 creates another **student VR scene copy**, never overwriting the desktop one.

## Scene reference geometry

All geometry, stage and path values come from [WorkshopSceneSpec.json](../UnitySource/Config/WorkshopSceneSpec.json).

| Item | Expected result |
|---|---|
| Car root | `AsterGT`, start Unity (1.8,0,0), moving on +Z |
| Student visual | one `StudentVisual` child, approx **2.41 × 1.61 × 5.14 m** (XYZ); student confirms nose and wheel contact |
| Driver eye | `AsterGT/DriverEyeAnchor` local `(-0.44,1.24,-0.12)` m |
| Robot | `NomaRobot`, root starts x=-4.5, z=14, crosses to x=+4.5; rigid-bone `WorkshopRobotWalk` |
| Crossing | stopped vehicle at z=7.5 before robot walk |
| Gap | main collider ends z=37; landing begins z=43; **no collider bridge** |
| Gap hold | car center z=32, velocity zero until explicit student command |
| 1.4 flight | z=32 → 48, peak +3m, ~10s, jets only during flight; route ends z=58 |
| Starter | fixed speed 0.85 m/s; `CanAdjustSpeed` and `CanFly` disabled |

The builder creates student-owned URP material copies from imported materials and attempts scale/axis normalization based on measured vehicle bounds. **Color fidelity, glass transparency, car nose direction, robot bone mapping and street visual topology require real Unity visual inspection**. If an imported FBX hierarchy differs, stop and repair the generated student scene; do not silently use an old teacher Prefab.

## Code architecture

- `AIVRWorkshop.Student.WorkshopDrive`: only car root mover, scripted approach/yield/gap hold and future explicit jet flight.
- `WorkshopSpeedControl`: intentionally fixed 0.85 m/s in 1.3, implements finite bounded speed 0.25–2m/s in 1.4A.
- `WorkshopRobotWalk`: rotates imported rigid bones; **disable imported Animator** to avoid double animation; `WorkshopDrive` handles root crossing translation.
- `WorkshopDesktopPanel`: simple desktop buttons and status; gated 1.4 UI appears only when code enables it.
- `AIVRWorkshop.Student.EditorTools.WorkshopSceneBuilder`: editor-only scene creation; never install this under Runtime.
- `WorkshopSceneValidator`: structure/prefab-bound reference check for **Starter 1.3**, intentionally rejects 1.4 feature-enabled scripts.

This scripted route is a teaching demonstration, **not** an actual autonomous driving planner, rigid-body dynamics model or safety certification.

## Unity verification and VR continuation

- Check Console compilation (0 blocking errors), object hierarchy, rendered mesh/materials, bone bindings, one mover, crossing and road gap.
- Student manually Play observes 0.85m/s travel, yield, walking robot, z=32 hold, pause/resume/restart. Then separate 1.4 Play validates speed and flight.
- 02_1 verifies OpenXR/Meta package and wired Quest Link. 02_2 duplicates **the student-built** `Workshop_Desktop_Student.unity` to `Workshop_VR_Student.unity` and binds one verified tracked XR rig under `DriverEyeAnchor`; student wears Quest for CP5.

[Acceptance matrix](Acceptance_Matrix.md) · [Build source guide](../UnitySource/README.md) · [Troubleshooting](Troubleshooting.md).
