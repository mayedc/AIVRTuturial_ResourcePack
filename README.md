# AIVRTuturial_ResourcePack

## AI-Assisted VR Driving Workshop

A reusable Unity and Blender teaching resource pack for AI-assisted VR development. Students modify prepared assets. They do not generate the car, the robot, or the street from scratch.

## Overview

The desktop scene drives a prepared car along a straight futuristic street. The car starts, stops for a robot at the crosswalk, continues, and can cross a road gap with a teacher-enabled jet or a fade transfer. A second scene is prepared for Meta Quest 3 and OpenXR. Headset playback was not verified for this release.

## Learning objectives

- Tell a reference idea, a prepared 3D model, and a running Unity scene apart.
- Use Cursor with Blender to recolor one named material on a student copy.
- Use Cursor with Unity to change `WorkshopSpeedControl` and watch the yield still happen.
- Read an XR camera hierarchy and state what is, and is not, proven on Quest 3.

## Key features

- Prepared vehicle `AsterGT`, cockpit materials, and `DriverEyeAnchor`.
- Prepared robot `NomaRobot` with `WorkshopRobotWalk`.
- Street content from `MeridianCity` plus road modules for a straight, a crosswalk, and a gap.
- Autonomous route in `WorkshopDrive`: approach, yield, gap, optional jet, landing, final stage.
- Desktop panel for speed, pause, and restart.
- OpenXR settings with Quest 3 selected. Meta XR Core camera prefab is not included.

## Software requirements

| Software | Version used for this pack |
|---|---|
| Unity Editor | 6000.3.27f2 |
| URP | 17.3.0 (`Assets/Settings/PC_RPAsset.asset`) |
| Input System | 1.20.1 |
| OpenXR | 1.16.1 |
| Blender | 5.2.2 LTS recorded in the FBX creator string. This release did not launch Blender. |
| Cursor | Current desktop app. MCP examples are in `.cursor/mcp.example.json`. |
| Git | Needed only to clone the public repository. |

## Hardware requirements

- Desktop lesson: a Windows PC that can open this Unity project. The validation machine used a Standalone Windows editor target.
- Lesson 3 headset: a Meta Quest 3 or Quest 3S is listed in the OpenXR feature. A physical headset test is NOT VERIFIED for this release.
- Android build support was present on the validation Editor (min SDK 32, ARM64, IL2CPP). No APK was built.

## Architecture

`WorkshopDrive` and `WorkshopSpeedControl` sit on `AsterGT`. The panel sits on `AI_VR_Workshop_V4`. The eye anchor is a child of the car at local position (-0.44, 1.24, -0.12). The route distances are 7.5 m at the crossing, 32 m at the gap hold, 48 m at the landing, and 58 m at the end. Details: `Docs/ProjectArchitecture.md`.

## Installation and quick start

1. Clone the repository. Open the repository root in Unity `6000.3.27f2`.
2. Wait until package restore and script compilation finish. Console compile errors must be zero.
3. Open `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`.
4. Enter Play. The upper-left panel can change speed, pause, and restart.
5. The car yields at the crosswalk. Jet flight stays off until `allowJetFlight` is enabled on `WorkshopDrive`.

See `Docs/QuickStart.md` and `Docs/WindowsSetup.md`.

## Three-lesson curriculum

| Lesson | Document | Students change |
|---|---|---|
| 1. Blender | `Docs/Lesson01_Blender.md` | A copy of `M_BodyPaint` on `SourceArt/Blender/AsterGT.blend` |
| 2. Unity | `Docs/Lesson02_Unity.md` | `WorkshopSpeedControl.targetSpeedMps` in the desktop scene |
| 3. Quest | `Docs/Lesson03_MetaQuest.md` | Inspection and, only with hardware, a device test. Do not claim a pass without a headset. |

## Blender MCP and Unity MCP

Example config: `.cursor/mcp.example.json`. Do not commit a machine-local `.cursor/mcp.json`. Package `com.coplaydev.unity-mcp` is a git dependency, not vendored source. Setup steps are in `Docs/WindowsSetup.md`.

## Exercises

- Vehicle recolor: `Docs/Lesson01_Blender.md` and `Prompts/Blender/RecolorBody.md`.
- Speed control: `Docs/Lesson02_Unity.md` and `Prompts/Unity/AdjustSpeed.md`.

## Desktop scenario testing

Play Mode on `Workshop_Desktop.unity` was executed for this release. Results are in `Docs/Validation/SceneTestResults.md`. Menu `Workshop V4/Run desktop play mode probe` repeats the timed observation and writes a log under `Logs/`, which is gitignored.

## Meta Quest 3 preparation

`Workshop_MetaVR.unity` keeps `DesktopCamera` disabled under `DriverEyeAnchor`. The Meta rig GUID `126d619cf4daa52469682f85c1378b4a` does not resolve because `com.meta.xr.sdk.core` is not in the manifest. Quest 3 hardware validation: NOT VERIFIED.

## Known limitations

- Jet flight is serialized off. Enabling it is a teacher control, not a comfort certification.
- No LOD, occlusion bake, or device frame-time measurement.
- No screenshots are shipped. Missing images are marked missing in `Docs/ToSlide.md`.
- Product name in Player Settings is still `AI_VR_Driving`.
- `Workshop_XR_Setup.unity` matches the desktop scene and is not an enabled build scene.

## Troubleshooting

`Docs/Troubleshooting.md`.

## Asset credits and license

Original course models, scripts, shaders, notes, prompts, and skills are under the MIT `LICENSE`. Unity, Blender, Cursor, and Meta software are not relicensed. Table: `Docs/AssetLicenses.md`.

## More documents

- `Docs/TeacherGuide.md`
- `Docs/StudentChecklist.md`
- `Docs/Compatibility.md`
- `Docs/ReleaseChecklist.md`
- `CHANGELOG.md`
