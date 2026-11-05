# Prompt 1.3 — Export approved Blender vehicle and build a Unity starter scene

Only run this after the student completed **1.1 (all-model review)** and approved **1.2 (their own body color)**. Verify Blender MCP and Unity MCP through *actual live reads*. Reply in Simplified Chinese. **DO NOT implement speed control or jet flight: those belong to 1.4.**

## A. Export student's approved car

1. Read `AGENTS.md`, `Docs/02_Asset_Catalog_and_Reuse.md`, `Docs/03_Unity_Integration.md` and `Docs/Acceptance_Matrix.md`. Locate the approved `StudentWork/S01/AsterGT_Color.blend` (adapt S01 to the group). Stop if missing/unapproved. Do not replace the student's color with a hardcoded red.
2. Through Blender MCP verify body material, mesh hierarchy, scale, bounds and `DriverEyeAnchor`. Export **only the car** to `StudentWork/S01/AsterGT_Color.fbx`, metres, **-Z Forward / Y Up**, evaluated modifiers, no unrelated cameras/lights. Detect any existing FBX and avoid overwriting unrelated work. Verify actual output path, size, orientation and approximate bounds.

## B. Unity import and assembly

3. Verify the **student blank URP Unity project** is the correct active instance (project path, packages, scene and Console). Check whether required class assets are already installed. The GitHub repo contains a full reference Unity project, not a verified .unitypackage.
4. Prefer a teacher-tested `.unitypackage`, if supplied. Otherwise if the target asset folder is absent, review the path/expected effects and run the existing `Tools/Install-Workshop.ps1` to copy `Assets/AI_VR_Workshop_V4` into the verified **student** Unity project. Preserve `.meta` references; never copy twice, overwrite teacher data, or claim FBX alone includes roads/robot/scripts. If an MCP operation is unsupported, identify it and instruct a **manual Assets > Import Package > Custom Package** only if a verified package exists; then reverify MCP.
5. With Unity MCP, duplicate the reference desktop scene into **student-only** `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop_Student.unity` (or safely reuse a confirmed separate student checkpoint); never overwrite `Workshop_Desktop.unity`. Import the approved FBX to a student asset folder and attach **one** `StudentVisual` under `AsterGT`; hide only duplicate native body renderers in the student scene.
6. Preserve one `WorkshopDrive`, one `WorkshopSpeedControl`, `WorkshopRobotWalk`, city, robot, jets, camera and eye anchor. Check vehicle forward **+Z**, metres (about 2.41 × 1.61 × 5.14 in Unity), student's paint, no second mover, and two road colliders leaving the **z=37 to 43 gap** uncovered. Do not blindly add a second -90° rotation or 0.01 scaling after values have been corrected.
7. Check missing scripts and Unity Console errors (expected zero), validate scene references and save the student scene. Preserve **starter** speed control/flight code unchanged.

## C. Mandatory student Play checkpoint

8. Explicitly hand control to the student to **press Unity Play manually** and observe the **whole route**, not just start-up: cruise target eventually **0.85 m/s**, vehicle yields before crossing, robot crosses, car holds at **z=32 m** before the 6 m gap, Pause/Resume and Restart work. Ask the student to confirm custom body look and heading.
9. Present a **PASS / FAIL / NOT TESTED** list, only marking items actually seen by the student or measured across the relevant time span. An 8-second `ApproachCrossing` sample at 0.44 m/s does **not** validate the route; mark this **WAITING FOR STUDENT PLAY**. Do not fabricate visual success.
10. **STOP**. Tell the student: “先亲自完成 Unity Play（让行、机器人、缺口停车、暂停、重开）。确认后再独立复制 Prompt 1.4。” Never autonomously run 1.4 or modify runtime scripts in this step.
