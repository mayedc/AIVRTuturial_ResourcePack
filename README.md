# AI Era — Build a VR Driving Scene with Cursor, Blender and Unity

**A student-led, source-first AI Agent workshop.** Students use Cursor + Blender MCP + Unity MCP to inspect eight Blender models, customize a car, **build their own Unity scene from four FBXs**, implement an interactive speed control and gap flight, and test the driver's view with a Quest headset.

> **Source-first workflow:** This repository does **not** provide a ready-made Unity scene, prefab asset bundle or `.unitypackage`. Every student's Unity scene is assembled inside **their own separate blank URP Unity project**. The first source-first version is awaiting a fresh-clone Unity/Quest retest; older validation logs apply only to historical releases.

For consistent stage IDs and file naming, see [Stage naming convention](Docs/Stage_Naming_Convention.md). Release privacy checking: `python Tools/Validation/audit_public_release.py` (review any findings before publishing).

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
| 1.3 | [Build the Unity scene from FBXs](Prompts/01_3_Export_And_Build_Unity.md) | Student personally Plays the full fixed-speed route and gap hold |
| 1.4 | [Implement speed and jet flight](Prompts/01_4_Speed_And_Gap_Flight.md) | Student tests speed, explicit jet, landing, pause/restart |
| 02_1 | [XR/Meta/Quest Link readiness](Prompts/02_1_XR_Setup_And_Device_Check.md) | Student verifies installed rig, OpenXR and active PC Link session |
| 02_2 | [Attach driver's XR camera](Prompts/02_2_Attach_Driver_Camera_And_Test.md) | Student confirms stereo, seat alignment and head tracking in headset |

See [quick start](Docs/QuickStart.md), [teacher guide](Docs/TeacherGuide.md), [student checklist](Docs/StudentChecklist.md), [acceptance matrix](Docs/Acceptance_Matrix.md) and [troubleshooting](Docs/Troubleshooting.md).

## Required software and equipment

**Before class:** Share the [Windows student pre-class announcement](Docs/Student_Preclass_Announcement.md), covering Cursor Pro, Unity International, Blender, Git, Python, uv, Quest Link and hardware checks.


- **Windows PC**, supported GPU, local write permissions and internet access to GitHub, Blender MCP package registry and Unity Package Manager.
- **Unity 6**, with the blank **URP template** and a tested-compatible Editor (historical baseline `6000.3.27f2`); **Blender 5.2.2** baseline or newer after real import checks; Cursor, Git and uv/uvx for MCP.
- CoplayDev Unity MCP and ahujasid Blender MCP, installed/verified through Prompt 00.
- For VR only: compatible Quest 2 / 3 / 3S, USB-C **data** cable, Windows Meta Quest Link/Meta Horizon Link app, verified Standalone OpenXR and compatible Meta XR rig package. **Headset hardware is not needed to complete the desktop portion.**
- Cursor Pro is required only if the course or account's selected Cursor features require it; the Blender/Unity MCP projects do not inherently require a subscription.

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
| `Tools/Validation/` | Dependency-free repository checks |
| `Docs/Validation/` | **Historical evidence**, not a claim that current source-first workflow ran in Unity/Quest |
| `.cursor/skills/` | Additional scoped instructions for the teaching Agent |

**Student outputs** go into Git-ignored `StudentWork/<group>/` for Blender/FBX, and the student-selected **separate Unity project** in `Assets/WorkshopStudentGenerated/`. Do not create a second Unity project inside the Git repository, commit local Unity caches, or overwrite teacher originals.

### 1.3 construction contract

Cursor copies four approved FBXs and `UnitySource` into the **blank student Unity project**, then invokes **Tools > Workshop > Build Student Scene From FBX**. The Editor code creates `Workshop_Desktop_Student.unity`, one vehicle root, robot and city hierarchy, jets, driver's eye, camera, colliders and Starter controls, then checks them using **Tools > Workshop > Validate Student Scene (1.3)**.

The builder **does not overwrite an existing student scene** and does not produce an HMD success claim. Imported axes, car appearance, robot animation (see [walk regression checks](Docs/Robot_Walk_Regression_Check.md)) and the full Play route must still be verified in the real Editor. [Build contract](UnitySource/README.md) · [Scene integration guide](Docs/03_Unity_Integration.md).

## Validation status

| Scope | Current evidence |
|---|---|
| Repository structure and links | [Static validator](Tools/Validation/validate_source_first.py), GitHub Actions source checks |
| Current source-first C# compilation and scene creation | **NOT TESTED on a real Unity Editor as part of this revision** |
| Current source-first full desktop Play | **NOT TESTED**; requires a clean blank-project test |
| Current source-first 02_2 Quest Link/stereo/head tracking | **NOT TESTED**; requires a real headset retest |
| Earlier Blender/Unity/VR workshop | User-tested on a prior local build, but **not equivalent to testing this new builder** |

Run `python Tools/Validation/validate_source_first.py` to validate source presence, spec, Markdown links and stage protections. This does not replace Unity compilation or a physical headset test. See [release acceptance](Docs/ReleaseChecklist.md).

## License and credits

Original course materials are MIT licensed under [LICENSE](LICENSE); Unity, Blender, Meta XR SDK and MCP packages have their own terms. Review [asset licenses](Docs/AssetLicenses.md) before importing new third-party models. Do not commit software installations or proprietary SDK assets.
