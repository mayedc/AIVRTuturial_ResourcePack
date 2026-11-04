# Project architecture

## Scenes

| Scene | Role |
|---|---|
| `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` | Enabled build scene. Desktop camera on. |
| `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity` | Enabled build scene. Desktop camera disabled. Meta rig reference missing. |
| `Assets/AI_VR_Workshop_V4/Scenes/Workshop_XR_Setup.unity` | Not in the build list. Same bytes as the desktop scene at packaging time. Do not treat it as a finished XR setup. |

## Runtime objects

- Root `AI_VR_Workshop_V4` holds `WorkshopDesktopPanel`.
- `AsterGT` holds `WorkshopDrive` and `WorkshopSpeedControl`.
- `DriverEyeAnchor` is a child of `AsterGT`. Desktop local camera position is zero on that anchor. Anchor local position is (-0.44, 1.24, -0.12).
- `NomaRobot` is assigned to `WorkshopDrive.pedestrian` and `pedestrianWalk`.
- `JetFX` starts inactive.
- `ComfortCurtain` is assigned on the desktop scene. In the Meta scene its parent transform belongs to the missing prefab.
- `RoadCollider_Main` and `RoadCollider_Landing` are the two road colliders. The gap is not covered by one collider.
- `Workshop_Daylight` is the directional light.

## Route

`WorkshopDrive` stages: `Ready` (about 3 s), `ApproachCrossing` to 7.5 m, `Yield` while the pedestrian moves, `ApproachGap` to 32 m, `AwaitChoice`. The starter stays in `AwaitChoice`. Exercise 2B adds an explicit `JetFlight` command and the landing and arrival stages.

`WorkshopSpeedControl` supplies a fixed 0.85 m/s target until Exercise 2A implements a bounded target. Braking uses `acceleration` (saved 0.65) inside `WorkshopDrive`. Students are not asked to edit that formula.

## Rendering and input

URP asset `Assets/Settings/PC_RPAsset.asset`. Input System package is active. No Animator controller is used. `WorkshopRobotWalk` poses the armor while `walking` is true.

## XR

OpenXR loader for Standalone and Android. Meta Quest Support feature targets Quest 3 among other Quest devices. No workshop script writes tracking onto the camera.
