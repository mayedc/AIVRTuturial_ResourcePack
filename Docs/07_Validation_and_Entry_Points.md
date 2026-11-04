# Validation and entry points

Packaged from the Windows project on 2026-11-04. Confirm the shapes and the lesson scope before any Quest session. This page separates files that are present from tests that were not repeated during packaging.

## Present in this folder

- Seven Blender scenes and seven FBX files, plus `SourceArt/Blender/Workshop_Master.blend`.
- Native Unity meshes, 17 materials, seven prefabs, and three scene files under `Assets/AI_VR_Workshop_V4`.
- Runtime scripts for speed, the route, the robot gait, and the desktop panel.
- `packages-lock.json` for Unity `6000.3.27f2`, URP 17.3.0, and OpenXR 1.16.1.

`Workshop_Desktop.unity` and `Workshop_XR_Setup.unity` share the SHA-256 hash `3930A95FC6FF2377589F015ABBA8264FC1FEA792E756BA85C1E3081F029475DD`. `Workshop_MetaVR.unity` is `20079211AEB738F30D7E9233ACB3766C5FD61C62D49ED484795ADCE59D0D4852`.

## Recorded earlier, not re-run while copying

Archived teacher notes describe a Blender reopen, an FBX reimport, a color-only checkpoint, and a desktop Play Mode route on another editor: Ready, ApproachCrossing, Yield, ApproachGap, AwaitChoice, JetFlight, Arrive, Complete. They also describe a Meta camera attached in a macOS project that already had Meta XR Core. Those notes are not in this folder and are not a result from this copy.

This copy still has the Meta prefab reference and does not have the Meta package. A missing-prefab warning on `Workshop_MetaVR.unity` is the expected file state.

## How to open it

1. Desktop: open `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` and press Play. Use the panel to pause and restart. The starter holds at the gap. Complete [Lesson 3](Lesson03_MetaQuest.md) for speed and flight.
2. VR file check: open `Workshop_MetaVR.unity` and inspect `AsterGT/DriverEyeAnchor`. The recorded world eye point is about (1.36, 1.24, -0.12) m. Headset seat height is a device calibration. Do not add another 1.24 m on top of a floor-origin rig.
3. Model edit: open `SourceArt/Blender/AsterGT.blend` or `NomaRobot.blend`. Keep the teacher file. Students use Save As.
4. Lessons: follow [the teacher guide](04_Three_Lesson_Teacher_Guide.md) and Prompts 00 through 04. Students do not run `Tools/build_teacher_art.py` or `Tools/build_unity_assets.py`. Those generators rewrite source files.

## Not verified on this copy

Windows Blender and Unity MCP round trips, both-eye rendering, head tracking, controller buttons, seated calibration, frame time, sustained play, comfort, and an Android APK. An untested item stays untested. A macOS Play Mode log does not prove this Windows project or a Quest device.

Look at the car silhouette and cabin, the robot and street style, and the speed and timing in Play before freezing a device version.

Three checks worth doing first: the car and cabin are acceptable for class, the robot and city match the intended style, and a real Play session accepts the eye line, the speed, and the pacing.
