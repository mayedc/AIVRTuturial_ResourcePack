# Lesson 03 — Meta Quest 3 scene

## Objectives

- Read the camera hierarchy in `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity`.
- Explain what OpenXR is configured to do, and what is missing.
- Test on a Quest 3 only when a headset is actually connected. Otherwise record NOT VERIFIED.

## Prerequisites

Lessons 1 and 2. A teacher has decided between PC VR Link and an Android APK. Do not switch paths mid-failure.

## Duration

90 minutes. Device setup happens before class.

## Required software

Unity `6000.3.27f2`, OpenXR 1.16.1, Android Build Support if an APK will be made. Meta XR Core is not in this repository. Install it only under Meta's own license, in a class copy, if you need `OVRCameraRig`.

## Steps

1. Open `Workshop_MetaVR.unity`. Do not enter Play and call it a headset test.
2. Find `AsterGT` / `DriverEyeAnchor`. Local eye position is (-0.44, 1.24, -0.12). Local scale is (1, 1, 1).
3. Find `DesktopCamera`. Its Camera and Audio Listener are disabled. Enabled camera count on the validation pass was 0.
4. Find the missing prefab named `Workshop_OVRCameraRig` (GUID `126d619cf4daa52469682f85c1378b4a`). `ComfortCurtain` is parented to that missing transform.
5. Read `Assets/XR/XRGeneralSettingsPerBuildTarget.asset` and the Android Meta Quest feature. Quest 3 is enabled.
6. If a headset is connected and a rig is installed on a class copy, check one active HMD camera, one listener, and that no script writes the car pose onto the head. Record the device result in the teacher's own notes.
7. If no headset is present, write: Quest 3 hardware validation: NOT VERIFIED.

## Copyable prompt

Use `Prompts/XR/InspectHierarchy.md`.

## Expected results

Students can point at the eye anchor, the disabled desktop camera, and the missing Meta prefab. They do not claim a Quest pass from the Editor alone.

## Validation checklist

- Desktop scene Play Mode already passed, or the teacher says it did not.
- This scene was not saved over by a student experiment.
- Hardware line is either a real device note or NOT VERIFIED.

## Troubleshooting

A missing prefab is expected in this repository. Installing a random camera rig into the teacher scene without a checkpoint will break the curtain parent. Duplicate the scene first.

## Deliverable

A hierarchy note and an explicit hardware status. No APK is required for a passing inspection grade.
