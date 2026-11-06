# Repository rules — source-first teaching pack 

This GitHub repository is a **course source bundle**, not an already-assembled Unity project.

- Default to English for repository-facing files and code. Reply to students in Simplified Chinese when an exercise prompt asks for it.
- Respect explicit student checkpoints: **00 → 1.1 review → 1.2 color → 1.3 source-built scene + student Play → 1.4 speed + jet → 02_1 XR readiness → 02_2 headset**. Stop after each. Do not automatically skip stages.
- Never regenerate or overwrite original `SourceArt/Blender` models and `SourceArt/FBX` files as part of student lessons. Do not replace a student-selected color with red.
- The approved vehicle FBX goes in `StudentWork/<group>/` locally. Student Unity projects must live **outside** this repository; the only authorized generated assets path in a student's project is `Assets/WorkshopStudentGenerated/`.
- **No dependency** on `historical prebuilt Unity asset folders`, historical `Workshop_Desktop.unity`, `.unitypackage`, historical prefab GUIDs or an existing reference Unity project. Build through `UnitySource/Editor/WorkshopSceneBuilder.cs` and its JSON config, using actual Unity MCP/Editor.
- Do not blindly overwrite an existing student Unity scene, scripts, materials or `.meta` IDs. Check project identity, back up before changes, do not remove unrelated user work. Repeated builds are non-destructive.
- Starter scripts belong to 1.3. Speed changes and a student-commanded flight belong **only to 1.4**, and teachers' reference answers must not be automatically copied in.
- Imported robot animation must use **one** owner (scripted rigid walk OR Animator); preserve crossing/road gap and driver's eye.
- Quest CP5 requires real student-observed stereo/head tracking. No static Unity read proves headset comfort or a live connection.
- No credentials, paid SDK redistribution, local `.cursor/mcp.json`, caches, private machine paths, or students' output files in Git.
- The archived old validation records are **historical**. Never carry old test passes forward to this source-first version.
