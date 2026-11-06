# Troubleshooting — source-first Blender / Unity / Quest

## Clone / MCP
Open an empty local folder in Cursor; use [preflight](../Prompts/00_Clone_Preflight.md), which refuses destructive reclones. Start blank Blender and an independent blank URP Unity project. Use [MCP setup](../Prompts/00_Install_Update_MCP.md). Verify live object/scene/project readback from both applications, not only a green icon. For failures, check uvx PATH, Blender add-on N-panel, Unity MCP Package Manager, correct Unity project/instance, firewall/permissions and Console.

## Import/Unity build
**There is no provided Unity scene, .unitypackage or historical prebuilt asset folder.** Copy exactly the four FBXs, Starter scripts, Editor scripts and JSON spec listed in [UnitySource](../UnitySource/README.md) to the **student's separate blank URP Unity project**. Confirm correct case-sensitive filenames under Assets/WorkshopStudentGenerated/Imported. Do not import Reference scripts in addition to Starter scripts.

If the Editor menu item is missing, wait for Unity compilation; check the first C# Console error, Editor script path and assemblies. If the builder reports that the scene already exists, it is **protecting student edits**: inspect the existing scene, do not delete or overwrite it. If it reports invalid FBX dimensions or missing Noma bone names, inspect the imported object hierarchy, scale/axes, material and model rig. Never restore an old teacher scene as a hidden shortcut.

The scene validator checks structure only. Car paint, glass transparency, nose direction, two distinct road colliders and robot animation require **actual** Unity Scene view and Play checks.

## Vehicle behavior
In 1.3 the speed is fixed at 0.85 m/s and the car is **meant to stop at z=32**. Do not implement flight before Play passes. In 1.4 edit only student-owned WorkshopSpeedControl.cs and WorkshopDrive.cs, preserving namespace and script references; do not copy duplicate C# classes or rerun the builder after editing. Flight requires an explicit button click from AwaitChoice while unpaused. Check that JetFX is on only in the air and z=58 ends at rest.

## XR and Link
Use [02_1](../Prompts/02_1_XR_Setup_And_Device_Check.md) to verify **actual Meta rig prefab**, Standalone OpenXR and physical PC Link environment, then [02_2](../Prompts/02_2_Attach_Driver_Camera_And_Test.md) on a **new student VR scene**. Avoid duplicate tracked cameras, double eye-height offsets and second movement components. CP5 passes only if the student wears the headset and confirms stereo and head tracking. Stop movement on discomfort.

Do not commit Unity caches, local MCP credentials or student outputs. The old reports in Docs/Validation are historical, not current runtime passes.
