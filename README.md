# AI Era — Build a VR Driving Scene with Cursor, Blender and Unity

**A student-led, source-first AI Agent workshop.** Students use Cursor + Blender MCP + Unity MCP to inspect eight Blender models, customize a car, **build their own Unity scene from four FBXs**, implement an interactive speed control and gap flight, and test the driver's view with a Quest headset.

> **Source-first workshop — instructor-tested:** This repository does **not** ship a ready-made Unity scene, prefab bundle or `.unitypackage`. Students build their own scene in a **separate blank Unity URP project**. The instructor has reported a successful test of the updated workflow after the November 6, 2026 fixes. See [Validation status](#validation-status) for the distinction between instructor confirmation, automated checks and device-specific evidence.

For consistent stage IDs and file naming, see [Stage naming convention](Docs/Stage_Naming_Convention.md): stage **1.1** is the student-facing label and `01_1` is its stable prompt file ID. The latest changes also address robot gait grounding, crossing continuity, and Quest 2 PCVR preparation.

## Learning outcomes

- **3D asset editing:** read real Blender models through MCP and recolor only the student car's `M_BodyPaint`.
- **Agent-assisted scene construction:** import the approved car + NomaRobot/MeridianCity/JetFX FBXs; create and validate Unity objects, colliders, scripts, material mappings and the camera.
- **Interactive behavior:** implement bounded speed control and an explicitly commanded flight over a real 6m road gap.
- **Immersive validation:** enable Standalone OpenXR/Meta XR and check a tracked driver's-eye view **in the physical Quest headset**.

## Start here (students)

1. Create a new **empty local folder**, open it in **Cursor**, and copy [00 Clone & preflight](Prompts/00_Clone_Preflight.md). Cursor clones this repository into the folder; do not download a ZIP first.
2. Open **empty Blender** and a **separate blank Unity URP project**. Copy [00 MCP installation & live verification](Prompts/00_Install_Update_MCP.md) to connect both applications. Confirm live scene/project reads.
3. Independently copy each prompt in the sequence below. **Cursor stops at every student checkpoint; never execute the entire list automatically.**

| Stage | Copy this prompt | Student checkpoint |
|---|---|---|
| 1.1 | [Inspect all 8 Blender models](Prompts/01_1_Review_All_Blender_Models.md) | Student examines every model |
| 1.2 | [Choose and recolor the car](Prompts/01_2_Choose_Car_Color.md) | Student approves their chosen paint (blank = red) |
| 1.3 | [Build the Unity scene from FBXs](Prompts/01_3_Export_And_Build_Unity.md) | Student Plays the full route, checks planted robot feet and no unexpected loop teleport, then verifies gap hold |
| 1.4 | [Implement speed and jet flight](Prompts/01_4_Speed_And_Gap_Flight.md) | Student tests speed, explicit jet, landing, pause/restart |
| 2.1 | [XR/Meta/Quest Link readiness](Prompts/02_1_XR_Setup_And_Device_Check.md) | Student verifies the actual Meta rig, Standalone OpenXR and active PC Link session |
| 2.2 | [Attach driver's XR camera](Prompts/02_2_Attach_Driver_Camera_And_Test.md) | Student confirms stereo, seated driver-eye alignment and head tracking in the physical headset |

See [quick start](Docs/QuickStart.md), [teacher guide](Docs/TeacherGuide.md), [student checklist](Docs/StudentChecklist.md), [acceptance matrix](Docs/Acceptance_Matrix.md) and [troubleshooting](Docs/Troubleshooting.md).

## Required software and equipment

**Before class:** Share the [Windows student pre-class announcement](Docs/Student_Preclass_Announcement.md) with students. It includes installer links, software versions, sign-in requirements, command-line checks and the requirement to bring their **own Windows laptop, charger and mouse**.

- **Windows PC**, supported GPU, local write permissions and internet access to GitHub, Blender MCP package registry and Unity Package Manager.
- **Unity international/Global Hub + Unity 6.3 LTS**: recommended reference Editor `6000.3.27f2` or a later compatible, verified 6000.3 patch; start with a **blank Universal 3D (URP)** project. **Blender 5.2.2 LTS** is the source baseline; verify newer releases against the provided `.blend` files and Blender MCP.
- **Cursor (course Pro account)**, Git for Windows, Python 3.11 (Python 3.10+ supported), and `uv` / `uvx`, with terminal commands working before class.
- CoplayDev Unity MCP and ahujasid Blender MCP, installed/verified through Prompt 00.
- For VR only: compatible Quest 2 / 3 / 3S, USB-C **data** cable, Windows Meta Quest Link/Meta Horizon Link app, verified Standalone OpenXR and compatible Meta XR rig package. **Headset hardware is not needed to complete the desktop portion.**
- **Cursor Pro**: prepare an active Pro account as requested for this course. The Blender/Unity MCP projects themselves are open source and do not inherently require a paid Cursor subscription.

Historical package versions are in [compatibility](Docs/Compatibility.md). A higher version number alone is not an execution pass.

## Repository map

| Location | Purpose |
|---|---|
| `SourceArt/Blender/` | Eight editable original Blender files (read-only teacher sources during student exercises) |
| `SourceArt/FBX/` | Seven source exports; students independently export their custom car |
| `Prompts/` | Eight student-operated instructions and explicit stage gates |
| `UnitySource/Config/` | Single JSON scene specification: expected geometry, paths, speeds and driver eye point |
| `UnitySource/Runtime/Starter/` | Four C# starter scripts with exercises 1.4A/1.4B intentionally unfinished |
| `UnitySource/Editor/` | Unity Editor-only source for safe scene construction and structural validation |
| `Answers/Reference/` | Teacher-only replacement solutions; **not imported in 1.3** |
| `Tools/Validation/` | Dependency-free repository, Markdown-link and tracked-text public-release privacy checks |
| `Docs/Validation/` | Archived evidence from a **previous project layout**; it is not the instructor's new post-fix test log |
| `.cursor/skills/` | Additional scoped instructions for the teaching Agent |

**Student outputs** go into Git-ignored `StudentWork/<group>/` for Blender/FBX, and the student-selected **separate Unity project** in `Assets/WorkshopStudentGenerated/`. Do not create a second Unity project inside the Git repository, commit local Unity caches, or overwrite teacher originals.

### 1.3 construction contract

Cursor copies four approved FBXs and `UnitySource` into the **blank student Unity project**, then invokes **Tools > Workshop > Build Student Scene From FBX**. The Editor code creates `Workshop_Desktop_Student.unity`, one vehicle root, robot and city hierarchy, jets, driver's eye, camera, colliders and Starter controls, then checks them using **Tools > Workshop > Validate Student Scene (1.3)**.

The builder **does not overwrite an existing student scene**. The revised robot setup uses one animation owner, preserves the imported FBX bone rest rotations, aligns the sole meshes to the road surface and avoids artificial crossing-height changes. The instructor reports that the updated workflow passed testing; **each student must still perform the real Unity Play checks** in the [robot gait regression protocol](Docs/Robot_Walk_Regression_Check.md), including three gait loops, ground contact, crossing completion and intentional Restart. [Build contract](UnitySource/README.md) · [Scene integration guide](Docs/03_Unity_Integration.md).

## Validation status

**Updated November 6, 2026.** After [PR #4](https://github.com/mayedc/AIVRTuturial_ResourcePack/pull/4) was merged, the instructor confirmed that the updated project had **passed testing**. This is an **instructor-reported result**, not a Unity/Quest test log produced by GitHub Actions. The exact Editor patch, GPU, headset model and test screenshots for that confirmation are not recorded in this repository.

| Scope | Status | Evidence / limitation |
|---|---|---|
| Repository structure, required sources, scene spec, Markdown links and stage guards | **PASS — automated** | [GitHub Actions on merged `main`](https://github.com/mayedc/AIVRTuturial_ResourcePack/actions/runs/42159367508); [source validator](Tools/Validation/validate_source_first.py) |
| Tracked-text privacy and development-label audit | **PASS — automated** | Same GitHub Actions run; [release audit script](Tools/Validation/audit_public_release.py). Does not independently inspect every Git-history object or binary metadata block |
| Updated source-first Unity workflow | **PASS — instructor-reported** | Instructor confirmed successful testing after the robot and documentation fixes; no machine-specific Unity Console or batch-mode report is committed |
| Robot gait and crossing behavior | **PASS — instructor-reported** | Fixes cover imported rest pose, sole grounding, a single animation owner, no unwanted crossing Y offset and completion behavior; [repeatable Play checks](Docs/Robot_Walk_Regression_Check.md) remain mandatory for each student project |
| Speed control, explicit jet flight, landing, pause and restart | **Instructor-reported workflow pass; no separate test artifact archived** | These remain student exercise 1.4 acceptance checks; do not treat source compilation or the Editor validator as a behavioral pass |
| Quest PCVR configuration / headset interaction | **Supported workflow documented; device-specific test evidence not archived** | [Quest 2/3/3S setup and headset acceptance](Docs/05_XR_and_Quest_Acceptance.md); record actual headset model, Standalone OpenXR, stereo and head tracking before claiming a device-specific PASS |
| Fresh student's own Windows/Unity/Quest configuration | **Must be verified individually** | The instructor's pass does not automatically validate each student's Unity packages, MCP connections, GPU, Meta Link session or headset |

**Run the automated checks** from a fresh repository clone:

```powershell
python Tools/Validation/validate_source_first.py
python Tools/Validation/audit_public_release.py
```

**Run the interactive checks** in Unity Editor: import the four approved FBXs into a separate URP project, build the scene, confirm the robot's feet remain grounded and its crossing has no unintended reset, and complete Play Mode stages 1.3 and 1.4. For VR, first verify Windows Standalone OpenXR and Meta Link, then test the real headset in stage 2.2. Record PASS / FAIL / NOT TESTED for the actual hardware in the [release checklist](Docs/ReleaseChecklist.md).

**Evidence policy:** Static CI success proves repository checks; the instructor's report records their hands-on test; and a device-specific XR pass requires an observed headset session. Previous-release logs under `Docs/Validation/` are historical reference only.

## License and credits

Original course materials are MIT licensed under [LICENSE](LICENSE); Unity, Blender, Meta XR SDK and MCP packages have their own terms. Review [asset licenses](Docs/AssetLicenses.md) before importing new third-party models. Do not commit software installations or proprietary SDK assets.
