# Inspect the Quest scene

Objective: describe the prepared VR hierarchy without claiming a headset result.

Paths:

- Scene: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity`
- Eye anchor: `AsterGT/DriverEyeAnchor`
- Disabled camera: `DesktopCamera`
- Missing prefab GUID: `126d619cf4daa52469682f85c1378b4a`
- Settings: `Assets/XR/XRGeneralSettingsPerBuildTarget.asset`

Rules:

- Do not delete the missing prefab instance.
- Do not enable `DesktopCamera` and call it VR.
- Do not install packages into the teacher project during class without a checkpoint.
- Do not write a tracking script that copies the car pose onto the head.

Success:

- You can name the eye-anchor parent, the disabled camera, and the missing rig.
- Your note says Quest 3 hardware validation: NOT VERIFIED, unless a headset test actually happened.
