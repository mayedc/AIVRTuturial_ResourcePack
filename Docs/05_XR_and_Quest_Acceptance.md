# XR and Quest acceptance

This package contains editable scenes. It does not contain a finished Quest project, an APK, or a passed headset test. Finish the steps below on a project copy before lesson 3.

## Project configuration

Use Package Manager versions that match the editor: XR Plug-in Management, OpenXR, and, if you choose the Meta camera rig, the Meta XR Core package that provides `OVRCameraRig.prefab`. Follow the [OpenXR project configuration](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.16/manual/project-configuration.html) and the [Meta project setup](https://developers.meta.com/vr/documentation/unity/unity-project-setup/) for the device. Write the resolved package versions into CP0. Do not copy a version number from an old zip and call it tested.

This Windows copy already enables OpenXR for Standalone and Android, with Meta Quest Support targeting Quest 3 and Quest 3S among other Quest devices. Android minimum API is 32 and the target architecture is ARM64. `com.meta.xr.sdk.core` is not in `Packages/manifest.json`.

PCVR Link and a standalone APK are different paths. Pick one before class. PCVR needs a tested Link setup. An APK needs the Android build modules, the SDK, NDK, and JDK, the OpenXR Android settings, and a developer-authorized device. Do not switch paths in the middle of an undiagnosed failure.

## Current Meta scene

`Workshop_MetaVR.unity` expects `Workshop_OVRCameraRig` under `DriverEyeAnchor`, with local position and rotation at zero and local scale (1, 1, 1). The prefab GUID is `126d619cf4daa52469682f85c1378b4a`, recorded in [ExternalPackageReferences.json](ExternalPackageReferences.json). Until that package is installed, the Hierarchy shows a missing prefab. `CenterEyeAnchor` is not instantiated. The only camera serialized in the scene is `DesktopCamera`, and its Camera and Audio Listener are disabled. The comfort curtain is parented inside the missing rig, so it cannot be checked as a live child while the prefab is missing.

`Workshop_XR_Setup.unity` matches `Workshop_Desktop.unity` byte for byte. Do not open it as if it were a finished XR setup. Save a new scene if you wire a rig, and leave both teacher scenes untouched.

## Attach a rig you already have

1. Confirm the desktop scene has passed Play Mode.
2. Duplicate the scene to a checkpoint name. Parent one existing, tracking XR rig under `DriverEyeAnchor`. Keep local scale at (1, 1, 1). Do not add a second XR loader.
3. Set seat height from the tracking mode. Eye-level tracking can use the eye point as a neutral head origin. Floor tracking must subtract the seated eye height so the 1.24 m eye point is not applied twice. Trust the headset picture, not the scene coordinate alone.
4. Disable `DesktopCamera`'s Camera and Audio Listener. Keep the curtain object so it can be reparented. One active HMD camera and one listener.
5. Parent `ComfortCurtain` to the HMD camera at local position (0, 0, 0.10), zero rotation, and scale (1, 1, 1). The drive component must still reference that renderer. Both eyes must be covered when the curtain is opaque, and the curtain must follow the head.
6. The car body follows the car root. The HMD pose comes from tracking. Do not write the car pose onto the HMD camera, and do not scale the XR origin away from 1.
7. `WorkshopDesktopPanel` is a desktop IMGUI panel. It is not a VR UI. Controller buttons, if you add them, should call `SetPaused`, `BeginComfortTransfer`, or `BeginJetFlight` only after a device test.

`Tools/Unity_Attach_MetaRig.cs` is a teacher script for a project that already has the Meta prefab. It refuses to run when `Workshop_MetaVR.unity` already exists. Do not run it against this release copy.

## Comfort

`allowJetFlight` stays false until the yield and the fade have been tried. The jet is a 10 second, 3 m arc. It is not a comfort certification. First tries are seated, short, supervised, and easy to pause. Stop if someone is uncomfortable. Do not require the jet for a grade.

The fade must be checked on the device: the view goes black, then the car is already at the far side before the view returns. A missing curtain reference refuses the transfer. Pause the demo if the frame rate collapses, the view is blocked, tracking is lost, or the curtain leaks.

## Performance table

Pick the real target, such as 72 Hz (about 13.9 ms) or 90 Hz (about 11.1 ms), and record the measured frame time. Watch the start, the crosswalk, the closest robot, the gap, the jet or fade, and the end, for 30 seconds each. Record CPU and GPU time, dropped frames, temperature, sustained play, and both eyes. A target number is not a measured result.

This scene has no LOD or occlusion bake. Fewer shadow casters, less transparent glass, a shorter view distance, lower MSAA, and less repeated detail are the first cuts. The teaching shaders' stereo macros still need a check on the OpenXR runtime you actually use.

## After a real pass

Archive the editor version, `packages-lock.json`, the project copy, any build output, the device identity, the report, and the captures in the teacher's own course records. Distribute only content you have the right to share.
