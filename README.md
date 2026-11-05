# AI Era: VR Development with AI Agent, Blender, and Unity

A three-lesson MDIT 310 driving workshop. **Start in Cursor, connect Blender and Unity through MCP, recolor Aster GT, then assemble and validate the Unity scene with the Agent.** A ready-made desktop scene remains as a teacher/reference fallback, not the student's first step.

## Student start (Cursor-first)

1. Create a **new, empty local folder** (for example `D:\AI_VR_Workshop`), open that folder in Cursor, and ask Cursor to clone this repository **into that empty folder**. Do not download/extract a ZIP or start by opening the provided Unity project in Unity Hub. See [Quick start](Docs/QuickStart.md) and [Cursor-first workflow](Docs/Cursor_First_Workflow.md).
2. Have Cursor read this README and run the [preflight prompt](Prompts/00_Clone_Preflight.md). Check Git, compatible Cursor, Blender, Unity Editor/Hub, Quest Link (Meta Link PC app), Windows/USB/OpenXR, required account or classroom Cursor Pro access, write permissions, and required package versions **before** proceeding.
3. Open an **empty Blender scene** and a **temporary blank URP Unity project** for the MCP connection check (not the supplied workshop scene). In Cursor, run the [MCP install/update/verification prompt](Prompts/00_Install_Update_MCP.md). Cursor installs or updates compatible MCP components, students start/enable the in-app services, and Cursor reads back both applications. Do not infer connection from a green icon alone.
4. Run [1.1 inspect eight Blender models](Prompts/01_1_Review_All_Blender_Models.md) and [1.2 choose vehicle paint](Prompts/01_2_Choose_Car_Color.md), stopping for student review and color approval.
5. Run [1.3 export and build Unity](Prompts/01_3_Export_And_Build_Unity.md); after the student's complete Play check, independently run [1.4 speed and flight](Prompts/01_4_Speed_And_Gap_Flight.md).
6. Start VR only after desktop completion: [02_1 XR/Meta/Link setup](Prompts/02_1_XR_Setup_And_Device_Check.md), then [02_2 driver's tracked camera and headset Play](Prompts/02_2_Attach_Driver_Camera_And_Test.md). Each step stops for student confirmation.

[Teacher guide](Docs/TeacherGuide.md) · [Student checklist](Docs/StudentChecklist.md) · [Acceptance matrix](Docs/Acceptance_Matrix.md) · [Troubleshooting](Docs/Troubleshooting.md)

## Contents and migration status

- `SourceArt/Blender` and `SourceArt/FBX`: Aster GT, Noma Robot, Meridian City, JetFX and three road modules.
- `Assets/AI_VR_Workshop_V4`: **legacy internal Unity asset path** containing reusable meshes, materials, scripts and scenes. Do not rename it by hand: scene GUIDs, assembly definitions, namespaces, menus and references must migrate together and compile in Unity. Any migration of the old asset path must be done in Unity with preserved `.meta` GUIDs, assembly references and full scene tests; it is outside the student sequence.
- `Prompts` and `.cursor/skills`: scoped Agent instructions. `Answers`: instructor reference code outside imported Assets.
- `ProjectSettings/ProjectVersion.txt` and `Packages/manifest.json`: **historical project compatibility inputs**, not a command to overwrite a student's newer working configuration.

The repository currently includes a full Unity reference project, **not a verified, exported Unity package**. Do not claim that MCP import or a classroom `.unitypackage` has already been tested. The teacher must produce and test that package using Unity before distributing it. The old desktop scene and prior validation remain available as recovery references.

## Compatibility

Start from Unity **6.3.27f2 / 6000.3.27f2 or a newer compatible Unity 6 editor** (with the project URP/Input/OpenXR packages validated), Blender **5.2.2 or newer capable of opening these source files**, a current compatible Cursor release, and a compatible Windows Quest Link PC app for the available Quest 3/3S. Newer versions are acceptable **after** package import and live-tool checks; a higher version number alone is not proof of compatibility. Cursor Pro is a classroom/account requirement only if the teaching plan needs Pro features; MCP itself does not imply a paid Blender/Unity service.

Historical validation does not prove current live MCP, Windows-machine portability or headset operation. See [Compatibility](Docs/Compatibility.md) and [XR acceptance](Docs/05_XR_and_Quest_Acceptance.md). Original course assets/code are under [MIT](LICENSE); third-party limits are in [asset credits](Docs/AssetLicenses.md).
