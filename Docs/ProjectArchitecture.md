# the current teaching package source-first architecture

The **Cursor/Git repository** is a source bundle: Blender/FBX models, instructions, Config JSON, four Starter C# scripts, two Editor C# files, teacher answers and validators. It is **not** a Unity project. The student's **blank URP Unity project is a separate local directory**; it receives imported FBXs and source code under Assets/WorkshopStudentGenerated.

The Editor builder creates student scene Workshop_Desktop_Student.unity with a WorkshopStudentRoot containing MeridianCity, AsterGT, NomaRobot, RoadCollider_Main, RoadCollider_Landing and daylight. AsterGT has one StudentVisual, DriverEyeAnchor/DesktopCamera, JetFX (off), WorkshopSpeedControl and WorkshopDrive. WorkshopDesktopPanel lives on the root. Robot walking uses WorkshopRobotWalk attached to imported bones.

**Starter 1.3**: fixed 0.85 m/s, stop at z=7.5 for robot, hold at z=32 before a real open collision gap z=37–43, pause/restart. **Exercise 1.4A** adds finite speed inputs clamped to 0.25–2m/s. **1.4B** adds explicit user-commanded jet arc z=32→48 (3m lift, ~10s) then z=58 stop. The scene parameter source is [WorkshopSceneSpec.json](../UnitySource/Config/WorkshopSceneSpec.json).

**VR 02_1** installs/verifies Standalone OpenXR, an actual Meta tracked XR camera prefab and a physical Quest Link session. **VR 02_2** makes a new VR student scene copied from the completed *student-generated* desktop scene, binds one tracked rig to DriverEyeAnchor and requires student-worn stereo/head-tracking evidence.

Old previous Unity scenes and package settings are historical only, not classroom dependencies. [Build contract](../UnitySource/README.md) · [Acceptance](Acceptance_Matrix.md).
