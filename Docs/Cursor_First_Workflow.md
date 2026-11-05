# Cursor-first workflow — source-first Plan B

This repository is a SOURCE BUNDLE, not a Unity project. Students open an empty folder in Cursor, clone the repository, connect real Blender/Unity MCP tools, inspect/recolor models, create an independent Unity scene from FBXs, then implement interactions and test in Quest. **Copy one prompt at a time.**

| Stage | Cursor activity | Mandatory student evidence |
|---|---|---|
| 00 preflight | Clone and check installed versions/permissions | Git remote and actual software paths |
| 00 MCP | Connect empty Blender and a separate blank URP Unity project | Live read-only MCP results for both apps |
| 1.1 | Open all eight teacher Blender models for review | Student personally examines all models |
| 1.2 | Recolor only the student copy of M_BodyPaint | Student approves chosen color |
| 1.3 | Export student car; import NomaRobot/MeridianCity/JetFX FBXs; copy UnitySource into the blank student Unity project; build scene via Editor/MCP | Compiler/structure checks and **student-operated full fixed-speed Play** with robot crossing and gap hold |
| 1.4 | Modify student-owned speed and drive scripts | Observed bounded speed, commanded jet, landing, pause/restart |
| 02_1 | XR/OpenXR/Meta camera/PC Link self-check | Student confirms real camera asset, active Link environment |
| 02_2 | Duplicate the generated desktop scene into a new VR scene and attach tracked rig | Student physically confirms stereo, driver seat and tracking |

**Never skip gates or auto-run the next prompt.** Report PASS/FAIL/NOT TESTED based on observed evidence; passing a static source check does not prove Unity Play or a Quest headset test.

## Clone and MCP

1. Create a new writable **empty** folder on Windows, open it in Cursor, and copy [00 Clone & Preflight](../Prompts/00_Clone_Preflight.md). Cursor clones the repository; do not use ZIP or delete existing work.
2. Open empty Blender and a **blank URP Unity project in a separate local directory**, not the Git repository. Copy [00 Install/Update MCP](../Prompts/00_Install_Update_MCP.md), enable both servers and obtain actual scene/project readbacks.
3. Do not commit Cursor MCP settings, Unity cache, generated student scenes, or original teacher art modifications.

## Blender and Unity

- [1.1 inspect](../Prompts/01_1_Review_All_Blender_Models.md): see eight files, stop for student review.
- [1.2 color](../Prompts/01_2_Choose_Car_Color.md): student selects body color, saves their copy, stops for approval. **FBX export happens in 1.3.**
- [1.3 scene](../Prompts/01_3_Export_And_Build_Unity.md): export approved student car FBX with Blender MCP. Copy this and three repository FBXs plus the four Starter scripts, two Editor scripts and JSON config described in [UnitySource](../UnitySource/README.md) to the student's separate Unity project. Invoke **Tools > Workshop > Build Student Scene From FBX** through Unity MCP or the real Editor menu. It creates a new Workshop_Desktop_Student scene without any old prefab or .unitypackage. Refuse to overwrite an existing scene. Run structure validation and have the student Play the whole starter route.
- [1.4 behavior](../Prompts/01_4_Speed_And_Gap_Flight.md): only after full Play, modify the student-owned speed and flight scripts; do not import the Reference solutions automatically.

## VR and evidence

- [02_1 XR readiness](../Prompts/02_1_XR_Setup_And_Device_Check.md): verify actual Standalone OpenXR, Meta tracked camera prefab and Windows wired PC Link on a VR project copy if needed; student personally confirms the headset.
- [02_2 driver cockpit](../Prompts/02_2_Attach_Driver_Camera_And_Test.md): duplicate the **student-generated desktop scene**, parent one tracked rig under DriverEyeAnchor, disable the desktop camera only in the VR copy and have the student wear the headset to verify both eyes and head tracking.

See [acceptance matrix](Acceptance_Matrix.md), [source inventory](AssetManifest.md) and [troubleshooting](Troubleshooting.md). Older reports under Docs/Validation are historical and must not be copied forward as passes.
