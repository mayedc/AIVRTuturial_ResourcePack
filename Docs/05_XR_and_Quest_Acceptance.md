# Quest Link and cockpit acceptance: 02_1 then 02_2

The class uses **Windows PCVR** with Quest 3/3S and a USB-C **data cable**. An installed OpenXR package alone is not a real tracked camera.

## 02_1: XR project and device self-check

Run [02_1 XR Plug-in/Meta SDK/Quest Link](../Prompts/02_1_XR_Setup_And_Device_Check.md) on the **active student Unity VR project**, preserving the passed 1.1–1.4 desktop checkpoint. Through live Unity MCP, check **XR Plug-in Management > Standalone > OpenXR**, project validation, **Initialize XR on Startup** in a VR project copy, Meta XR Core SDK and a **resolved tracked rig prefab** such as OVRCameraRig. Distinguish a package in the manifest from a scene/camera that actually works. If missing, use the official Unity/Meta package routes; student completes login and license prompts.

The student opens the Meta Quest Link / Meta Horizon Link Windows app, connects a data-capable USB cable, launches **Link inside the headset**, checks the PC OpenXR runtime, and confirms a tracked **PC Link environment** appears. Cursor cannot infer that from USB power. Stage 02_1 stops for student self-check; camera binding is **not** done here.

## 02_2: Seat alignment and real headset Play

Only after 02_1 is confirmed, run [02_2 attach tracked driver camera and test in headset](../Prompts/02_2_Attach_Driver_Camera_And_Test.md):

1. Duplicate the student-tested desktop scene into a **VR-only student scene**. Never overwrite `Workshop_Desktop.unity` or `Workshop_Desktop_Student.unity`.
2. Parent **one** verified Meta XR rig under `AsterGT/DriverEyeAnchor`. The reference local anchor is approximately `(-0.44, 1.24, -0.12)` m in Unity, but read the student's actual current scene. An **eye-level** rig may use zero local offset with unit scale; a **floor-origin** rig requires measured tracking compensation rather than adding an extra blind 1.24 m offset.
3. Disable `DesktopCamera` Camera and AudioListener only in the VR scene; keep **one active HMD camera** and **one AudioListener**. Preserve car/robot/road/jet scripts and `ComfortCurtain` reference. Keep the curtain disabled for stationary tests.
4. Student sits safely, recenters the headset and manually presses Unity Play with car **stationary**. Verify both eyes, main-driver view, scale, forward view, rotation and positional head tracking. Fix misalignment only in the VR scene and retry.
5. Optionally check a short supervised movement after stationary success; headset flight is not required.

**CP4:** exact scene, project/packages, rig parent, tracking origin, offsets, camera/listener and Console. **CP5:** student-observed Link session, stereo image, driver-eye alignment and head tracking. Record each as PASS/FAIL/NOT TESTED. **No headset, no CP5 pass.**

## Historical reference

The shipped `Workshop_MetaVR.unity` references an unbundled Meta rig GUID in [ExternalPackageReferences.json](ExternalPackageReferences.json). It does not prove a tracked camera is currently usable; make a new student VR copy instead.

Official sources: [Unity XR Plug-in Management](https://docs.unity.com/en-us/engine/6000.3/manual/xr/configuring-project-for/plugin-management), [Meta XR Core SDK](https://developers.meta.com/vr/documentation/unity/unity-core-sdk/), [Meta XR Plugin Management](https://developers.meta.com/vr/documentation/unity/unity-xr-plugin/).
