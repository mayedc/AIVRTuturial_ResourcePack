# Teacher guide — source-first workshop

Students construct a new Unity scene from FBXs with Cursor; they **do not** open a supplied Unity project.

| Lesson | Student tasks | Required observation |
|---|---|---|
| [1 · Cursor/MCP](Lesson01_Setup.md) | Clone; prepare empty Blender and separate blank URP Unity; install and connect MCP tools | Real read-only MCP readbacks |
| [2 · Blender → Unity](Lesson02_Unity.md) | 1.1 inspect, 1.2 custom car color, 1.3 import four FBXs/build full Unity scene, 1.4 change speed and implement flight | Student .blend/.fbx, generated Unity scene, complete Play and interactive tests |
| [3 · VR](Lesson03_MetaQuest.md) | 02_1 OpenXR/Meta/PC Link; 02_2 attach tracked rig and wear headset | Student-confirmed device and CP5 stereo/head tracking |

The previous three-by-45-minute schedule is a teaching **target**, not a measured time for installing Unity/Meta packages. Prepare compatible Windows GPU/Quest Link setup, USB-C data cable, Unity 6 URP, Blender, Cursor, Git and uv/uvx **before class**, or allocate recovery time.

**Teacher release gate:** perform a clean Git clone and open a fresh blank Unity project at a separate path. Ensure no previously generated Assets/AI_VR_Workshop_V4 scripts or Prefabs exist on that machine. Copy/import four FBXs and UnitySource, compile C#, build the scene through the real Editor, verify car nose, glass, Noma skeleton, walking animation and gap, then full Play and headset. Static link/spec checks do not prove runtime. Store any emergency teacher demo separately; students must never depend on it.

[Acceptance matrix](Acceptance_Matrix.md) · [Troubleshooting](Troubleshooting.md) · [Source-first architecture](ProjectArchitecture.md).
