# Quest PC Link + driver-eye acceptance on the generated student scene

**Prerequisite:** Prompt 1.3 generated a new desktop scene from FBXs and Prompt 1.4 speed/flight work passed a real Unity Play. There is **no teacher Meta VR scene or prefab bundled in GitHub**. This lesson uses a **Windows PCVR** Quest 3/3S connected through USB-C **data** cable.

## 02_1: XR package/device readiness (do not bind camera yet)

Run [02_1](../Prompts/02_1_XR_Setup_And_Device_Check.md) on the student's separate Unity URP project (a VR project copy if needed). Via live Unity MCP and Project Settings inspect Standalone XR Plug-in Management, OpenXR enabled/initialized, project validation and **a real available tracked Meta XR camera rig prefab**. An OpenXR loader alone is not a usable camera.

If the Meta package or tracking rig is missing, install through the official Unity/Meta package channels with the student completing account/license GUI prompts. Do not silently install an older XR provider, substitute a broken historical GUID, or vendor proprietary SDK assets.

The student opens Meta Quest Link/Meta Horizon Link on Windows, connects the USB data cable, **launches Link from the headset**, checks active PC OpenXR runtime and confirms that the physical headset displays the tracked PC Link environment. If not observed, mark DEVICE NOT VERIFIED. **STOP** before 02_2.

## 02_2: student-only XR scene and physical test

Only after 02_1 self-check, run [02_2](../Prompts/02_2_Attach_Driver_Camera_And_Test.md).

1. Duplicate the **completed generated** scene from Assets/WorkshopStudentGenerated/Scenes/Workshop_Desktop_Student.unity to a **new** Workshop_VR_Student.unity in the same student project. Do not overwrite the desktop original or previously modified student VR scenes.
2. Bind exactly one verified Meta tracked camera rig as a child of AsterGT/DriverEyeAnchor. Expected local reference anchor is (-0.44,1.24,-0.12) metres but the **actual** student scene must be measured. For an eye-level/seated tracking origin start with rig local position/rotation zero, scale one. For floor-origin tracking, measure neutral eye offset and compensate **once**; avoid doubling seat height.
3. In the VR scene only, disable DesktopCamera Camera and AudioListener. Confirm one active tracked HMD camera, one enabled listener, no missing scripts, correctly initialized Standalone OpenXR, and the same car/robot/jet behavior. Preserve but disable the comfort curtain for initial static tests.
4. Student **sits safely, secures cable, recenters and manually presses Unity Play**, first with car stationary. Student verifies stereo in **both eyes**, intended main driver's seat, visible windshield, realistic scale and rotation/position head tracking. Any correction is made only to the VR scene and retested.
5. Optional supervised brief motion follows stationary acceptance; VR flight is not required. Stop on discomfort.

**CP4:** Unity hierarchy, camera/listener counts, tracking origin and Console. **CP5:** student-observed real Quest headset stereo, seat placement and tracking. Record PASS/FAIL/NOT TESTED separately. No headset, no CP5 pass. [Release checklist](ReleaseChecklist.md).
