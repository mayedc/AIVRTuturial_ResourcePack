# Quest Link and cockpit acceptance

The class path is wired PCVR with a Quest 3 or Quest 3S on Windows. Use a USB data cable. Prepare the Quest Link PC app, the selected PC OpenXR runtime and an instructor-tested Meta XR Core version before class. Record the actual editor, package, headset and runtime versions in CP0. Follow [Unity's OpenXR setup](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.16/manual/project-configuration.html) and [Meta's Unity setup](https://developers.meta.com/vr/documentation/unity/unity-project-setup/).

## Set up the VR copy

1. Save the tested desktop scene as a new checkpoint under `Assets/AI_VR_Workshop_V4/Scenes/`. Use a separate VR project copy if the desktop checkpoint must stay ready for machines without a headset.
2. Connect Quest Link and confirm the headset can enter the PC session. In the VR project copy, enable **Initialize XR on Startup** under **XR Plug-in Management > Standalone**. The student starter has this option off so desktop Play can start without a runtime. The configured Standalone loader is OpenXR.
3. Place one tested tracking rig under `AsterGT/DriverEyeAnchor`. Its neutral transform uses local position and rotation zero and scale one. The eye anchor is at (-0.44, 1.24, -0.12) m. Use the class-tested eye-level mode and recenter while seated. With floor tracking, account for the origin height before judging the eye point.
4. Disable the Camera and Audio Listener components on `DesktopCamera`. Retain one enabled HMD camera and one listener. Preserve the route and keep the head pose driven by tracking.
5. Keep `ComfortCurtain` disabled for this lesson and preserve its reference. The desktop panel is a desktop control. Start the first headset check with the car stationary, for example by pausing in the desktop Game view before the route starts.

## Record CP4 and CP5

- CP4: project and scene, tracking origin, parent hierarchy, scale, active camera and listener.
- CP5: actual Link connection, both eyes, seated neutral view and head turns. Record who checked each item and mark missing checks as not run.
- The flight exercise is tested on desktop first. A seated stationary headset check completes the class exercise. Any moving or flight demo is supervised, optional, and recorded separately.

## Historical scene reference

`Workshop_MetaVR.unity` refers to the unbundled Meta rig GUID listed in [ExternalPackageReferences.json](ExternalPackageReferences.json). Its desktop camera is disabled and the missing rig cannot provide a live tracked camera. `Workshop_XR_Setup.unity` duplicates the desktop scene. Use a new copy of the class checkpoint for the exercise. The [archived release report](Validation/FinalReleaseReport.md) records the earlier validation scope.
