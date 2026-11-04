# AI Era: VR Development with AI Agent, Blender, and Unity

A three-lesson driving workshop for MDIT 310. Open the prepared Unity project, recolor Aster GT in Blender, change its driving behavior in Unity, and attach a tracked cockpit view for wired Quest Link.

## Start here

1. Follow the [Windows and Cursor setup](Docs/WindowsSetup.md). Use the Unity Editor version in `ProjectSettings/ProjectVersion.txt` and open the repository root in Unity Hub.
2. Follow [Lesson 1](Docs/Lesson01_Setup.md) to download the pack, open the project, and read back Blender and Unity state through MCP.
3. In [Lesson 2](Docs/Lesson02_Unity.md), recolor a copy of the car, export FBX, and bring the visual into a copy of `Workshop_Desktop.unity`. In Play, the starter drives at a fixed 0.85 m/s target, yields to the robot, and waits before the gap.
4. In [Lesson 3](Docs/Lesson03_MetaQuest.md), implement the speed and flight exercises, verify the desktop run, and set up the cockpit rig in a separate scene copy.

The [teacher guide](Docs/TeacherGuide.md) covers timing and recovery points. Use the [acceptance matrix](Docs/Acceptance_Matrix.md) to record the checks you actually ran.

## What's in the pack

- `SourceArt/Blender` and `SourceArt/FBX`: Aster GT, Noma Robot, Meridian City, JetFX, and three road modules. The Blender folder also has an assembled master.
- `Assets/AI_VR_Workshop_V4`: Unity meshes, materials, prefabs, route scripts, and scenes. See the [asset catalogue](Docs/02_Asset_Catalog_and_Reuse.md) and [project architecture](Docs/ProjectArchitecture.md).
- `Prompts`: scoped instructions for each Agent exercise.
- `Answers`: teacher reference scripts and archived originals, outside Unity's imported Assets. Start the exercises from the runtime files.

## Classroom platform

Windows, Cursor, Blender, Unity, and one Quest 3 or 3S with a tested data cable per group. Set up Quest Link, the PC OpenXR runtime, and the compatible Meta XR Core package before class. The Meta SDK is an external dependency. The shipped Meta scene is a historical rig reference, and the class starts from a copy of the desktop scene. See the [XR checklist](Docs/05_XR_and_Quest_Acceptance.md).

Previous release runs are under [historical validation](Docs/Validation/FinalReleaseReport.md). Record current desktop, live MCP, and headset results separately.

Original course models, code, and material are under the MIT [license](LICENSE). See [asset credits](Docs/AssetLicenses.md) for third-party boundaries.
