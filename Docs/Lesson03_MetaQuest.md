# Lesson 3 — VR configuration and driver's seat cockpit

**Prerequisite:** the student has already tested and passed 1.1–1.4, including speed control and the commanded gap flight on the desktop. Do not re-run those scripts here.

## 02_1 — XR/Meta SDK/Quest Link readiness

Copy [02_1 XR setup and device self-check](../Prompts/02_1_XR_Setup_And_Device_Check.md). Cursor reads the active Unity project through MCP, examines **XR Plug-in Management > Standalone > OpenXR**, OpenXR settings, the installed **Meta XR Core SDK**, and a real supported **tracked XR rig/camera prefab**. If all are compatible and healthy, report without reinstalling. Otherwise install via Unity Package Manager and the **official Meta XR Core SDK**, with user sign-in and license steps done manually.

The student connects Quest 2/3/3S with a USB-C **data cable**, starts the Windows Meta Quest Link / Meta Horizon Link desktop app, **launches Link from the headset**, checks the PC OpenXR runtime and personally confirms they are seeing the **PC Link environment**. Cursor must stop for this check: do not attach a VR camera yet.

## 02_2 — Attach driver's XR camera and test while wearing headset

After 02_1 succeeds, copy [02_2 attach driver XR camera and Play](../Prompts/02_2_Attach_Driver_Camera_And_Test.md). Cursor duplicates the verified desktop student scene into a VR-only scene and parents **one** tested tracked rig to `AsterGT/DriverEyeAnchor`, verifying local transforms and **eye-level vs floor origin** without double height offset. The desktop camera and listener are disabled **only** in the VR scene.

The student then sits safely, wears the headset, verifies the PC Link session, recenters and manually presses Unity Play **first with the car stationary**. Confirm both eyes, correct driver-seat position, forward view, natural head rotation and positional tracking. Cursor checks the hierarchy and fixes VR-only alignment if needed; never pretend the Editor can observe what the student sees.

Record **CP4 structural configuration** and **CP5 student-observed headset testing** separately as PASS/FAIL/NOT TESTED. For the detailed checklist, see [Quest Link and cockpit acceptance](05_XR_and_Quest_Acceptance.md).
