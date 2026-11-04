# Unity validation

Date: 2026-11-04. Project: release candidate only. Editor: 6000.3.27f2 (6000.3.27f2, revision 22188f149405), from `ProjectSettings/ProjectVersion.txt`.

The original development project was not opened for these checks and was not modified. A second Editor was already running on that original project. Every command below was pinned to the release candidate.

## Editor and packages

| Check | Result |
|---|---|
| Editor reached ready | PASS. Pipeline port responded. `console status` reported `compilationFailed=false` and `compiling=false`. |
| `Packages/manifest.json` and `Packages/packages-lock.json` | Present. Lock matches the manifest pins used below. |
| Render pipeline | Universal Render Pipeline 17.3.0. Active asset: `Assets/Settings/PC_RPAsset.asset`. |
| Input | `com.unity.inputsystem` 1.20.1. `ProjectSettings/ProjectSettings.asset` `activeInputHandler` is 1 (Input System package). |
| XR | `com.unity.xr.management` 4.7.0 and `com.unity.xr.openxr` 1.16.1. `Assets/XR/Loaders/OpenXRLoader.asset` is assigned for Standalone and Android in `Assets/XR/XRGeneralSettingsPerBuildTarget.asset`. |
| Meta Quest feature | OpenXR Meta Quest Support is enabled for Android. Target devices include Quest, Quest 2, Quest Pro, Quest 3, and Quest 3S. |
| Meta XR Core package | Not in `Packages/manifest.json`. Prefab GUID `126d619cf4daa52469682f85c1378b4a` does not resolve. |
| Android player | `BuildPipeline.IsBuildTargetSupported` for Android returned True. Minimum SDK 32. Target architecture value 2 (ARM64). Android scripting backend is IL2CPP. Active Editor target during inspection was StandaloneWindows64. |
| Pipeline package | `com.unity.pipeline` 0.9.1-exp.1, used to run the checks. |
| Script compilation | PASS. Workshop runtime and editor scripts compiled with zero compilation errors. |

## Asset integrity (desktop scene loaded)

Scene: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`.

Edit-mode inspection after import:

- 104 mesh filters, 0 missing meshes, 271,896 triangles, no non-finite mesh report from the renderer/material pass.
- 104 renderers, 0 missing or null materials.
- 0 missing scripts. 0 missing prefab instances in this scene.
- Prefabs loaded: `Assets/AI_VR_Workshop_V4/Prefabs/AsterGT.prefab`, `NomaRobot.prefab`, `MeridianCity.prefab`, `Road_Crosswalk12.prefab`, `Road_Gap12.prefab`, `Road_Straight12.prefab`, `JetFX.prefab`.
- `WorkshopDrive` is on `AsterGT`, parent `AI_VR_Workshop_V4`. Pedestrian `NomaRobot`, walk component present, thigh and shin and foot bones assigned on both sides. `JetFX` starts inactive. `ComfortCurtain` assigned. `WorkshopSpeedControl` target 0.85 m/s. `allowJetFlight` saved value false.
- `WorkshopDesktopPanel` is on `AI_VR_Workshop_V4` and its desktop controls are enabled.
- One camera, `DesktopCamera`, enabled, tagged MainCamera, parent `DriverEyeAnchor`. One audio listener.
- No `.controller` or `.anim` files under `Assets`. The robot gait is `Assets/AI_VR_Workshop_V4/Runtime/WorkshopRobotWalk.cs`, not an Animator controller. Play Mode recorded a thigh rotation change greater than 8 degrees while the robot crossed.

`Workshop_XR_Setup.unity` is present and is not enabled in `ProjectSettings/EditorBuildSettings.asset`. Enabled scenes are `Workshop_Desktop.unity` and `Workshop_MetaVR.unity`.

## Meta VR scene (edit mode, not a headset test)

Scene: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity`.

- `AsterGT` parent is `AI_VR_Workshop_V4`. `DriverEyeAnchor` parent is `AsterGT`, local position (-0.44, 1.24, -0.12), local scale (1, 1, 1).
- `DesktopCamera` is a child of `DriverEyeAnchor`, local position (0, 0, 0), forward (0, 0, 1). Its Camera component is disabled. Its Audio Listener is disabled. Enabled camera count: 0. Enabled listener count: 0. No second active camera.
- No `TrackedPoseDriver`, XR Origin, or OVR camera component is present, because the source prefab is missing. No workshop script writes a headset pose. `WorkshopDrive` moves the car root only.
- `ComfortCurtain` exists, but its parent is an unloaded prefab transform placeholder.
- Missing scripts on loaded objects: 0.
- OVRCameraRig GUID `126d619cf4daa52469682f85c1378b4a`: MISSING. This was left unresolved on purpose in the approved archive. The Meta XR Core package was not added in this phase, because it is not part of the redistributable project content and a new registry dependency was not required for the desktop gate.

Quest 3 hardware: NOT VERIFIED. No headset was connected or tested. No APK was built.

## Play Mode

Desktop Play Mode was entered with editor auto-tick and run-in-background enabled. `editor status` reported `playMode=playing`, `playerLoopTicking=true`, and an increasing frame count (the route log reached frame 46218). The observer is `Assets/AI_VR_Workshop_V4/Editor/WorkshopDesktopProbe.cs` (menu `Workshop V4/Run desktop play mode probe`). It does not save the scene. The saved `allowJetFlight` value stayed false on disk. The probe set that existing public field at the gap so the jet path could be observed.

Full checklist: `Docs/Validation/SceneTestResults.md`.

## Gate 02

PASS for compilation, desktop scene references, and the required desktop Play Mode checklist.

The missing Meta camera prefab remains a VR-scene limitation. It is not a desktop compilation failure and not a failed desktop gameplay test. Headset playback stays NOT VERIFIED.
