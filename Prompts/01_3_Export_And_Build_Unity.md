# Prompt 1.3 — Build the entire Unity desktop scene from FBX sources 

Run **only after** the student has inspected eight Blender files in 1.1 and visually approved the recolored **student** Aster GT in 1.2. This is a **source-first build**, not a copy of a teacher scene or `.unitypackage`. Reply in **Simplified Chinese**. **STOP at the 1.3 student Play gate**; do not automatically execute 1.4 or 02_1/02_2.

## A. Identify the right projects and outputs

1. Read `AGENTS.md`, `UnitySource/README.md`, `UnitySource/Config/WorkshopSceneSpec.json`, `Docs/03_Unity_Integration.md`, and `Docs/Acceptance_Matrix.md`. Via live Blender and Unity MCP readbacks confirm the **Git repository root**, the active **separate student blank URP Unity project**, exact scene, Unity version and Console. Refuse to modify the repository's teacher originals or an unrelated existing Unity project.
2. Locate the actually approved `StudentWork/<group>/AsterGT_Color.blend` and its chosen `M_BodyPaint` value (default red only if the student did not choose a color). From Blender MCP export **only the car hierarchy** to `StudentWork/<group>/AsterGT_Color.fbx`, metres, **-Z Forward / Y Up**, applied modifiers, no camera/lights. If that FBX path contains unrelated student work, use a unique checkpoint. Read back the exported file; do not substitute the teacher's `AsterGT.fbx`.
3. Confirm the **three repository FBX sources** exist: `SourceArt/FBX/NomaRobot.fbx`, `MeridianCity.fbx`, `JetFX.fbx`. The optional Road_* FBXs are for inspection/extensions; do not layer road tiles onto an existing city road without a placement plan. **There is deliberately no `Assets/AI_VR_Workshop_V4`, `Workshop_Desktop.unity`, reference Prefab or .unitypackage in the source-first workflow.** Do not call `Tools/Install-Workshop.ps1`.

## B. Copy minimal source code and import the FBXs

4. In the **student Unity project only**, create `Assets/WorkshopStudentGenerated/` with `Runtime/`, `Editor/`, `Config/`, `Imported/`, `Materials/`, and `Scenes/`. After checking for conflicts and creating a checkpoint, copy:
   - `UnitySource/Runtime/Starter/*.cs` → `Runtime/` (four scripts: `WorkshopDrive`, `WorkshopSpeedControl`, `WorkshopRobotWalk`, `WorkshopDesktopPanel`).
   - `UnitySource/Editor/*.cs` → `Editor/` (the editor builder + structural validator).
   - `UnitySource/Config/WorkshopSceneSpec.json` → `Config/`.
   - The approved student `AsterGT_Color.fbx` and the three other course FBXs → `Imported/`.
   Never overwrite an existing student C# file, scene, or `.meta` without a deliberate conflict resolution. Do not import both Starter and Reference types. The `Answers` folder is outside the active Unity project and is **not** a 1.3 import source.
5. Through Unity MCP refresh/import the assets and wait for recompilation. Verify the source-first scripts compile in the **active** student project; report missing-package or shader errors rather than masking them. The URP project should use its own compatible Package Manager dependencies; never overwrite an entire student's manifest with repository historical pins.

## C. Build and verify a new student-only scene

6. Through supported Unity MCP editor invocation, or by calling the reviewed **Tools > Workshop > Build Student Scene From FBX** menu item, run `AIVRWorkshop.Student.EditorTools.WorkshopSceneBuilder.Build`. This tool creates `Assets/WorkshopStudentGenerated/Scenes/Workshop_Desktop_Student.unity` from those four FBXs and `WorkshopSceneSpec.json`; it does **not** load a preexisting Unity teaching scene or use a `.unitypackage`. If the editor tool cannot be invoked through MCP, explain the exact Unity menu action to the student and then verify its result with Unity MCP.
7. Verify: city, car and robot actually visible; **one** `AsterGT` root and **one** `StudentVisual` car art; vehicle approximate bounds **2.41 × 1.61 × 5.14 m**, **nose faces Unity +Z**, wheels meet the road; **one** robot skeleton with walk-bone bindings, no competing Animator; `JetFX` under the car initially inactive; `DriverEyeAnchor` at the configured car-local driver position and one `DesktopCamera`; desktop control panel; two separate road colliders ending/starting at z=37/43 with an **open 6 m gap**. **Use actual Unity Scene/Game views**, not only serialized file paths, to confirm orientation and visual fidelity. If bounds, skeleton or material appearance are wrong, stop and repair only the generated student scene/import settings; never copy a teacher prefab as a shortcut.
8. Run **Tools > Workshop > Validate Student Scene (1.3)** through the editor/Unity MCP, and separately verify Console compilation with zero blocking errors. The validator checks **structure, not visually correct materials or real-time motion**. Save only the new student scene.

## D. Mandatory student-operated Play gate

9. Hand control to the student: **manually press Unity Play** in `Workshop_Desktop_Student.unity`; inspect the **entire starter route**, not only the first seconds: a stable 0.85 m/s target, yielding before the crosswalk, visible walking robot with both soles meeting the road, no floating, no foot penetration, no end-of-cycle reset or unintended teleport, clearance, holding at **z=32** before the unbridged gap, Pause/Resume and Restart. The vehicle must **not fly** yet and the speed slider must remain locked. Mark each check **STUDENT OBSERVED PASS / FAIL / NOT TESTED**.
10. Return actual created paths and readback evidence (FBX, scene, importer, scripts, Console), unresolved issues and a compact gate checklist. Use [the robot gait regression protocol](../Docs/Robot_Walk_Regression_Check.md) for at least three complete gait loops. A static compile or the first 8s of Play does **not** satisfy full route/robot verification. Explicitly wait for the student's confirmation.

**STOP.** The student independently copies `Prompts/01_4_Speed_And_Gap_Flight.md` **only after 1.3 Play passes**.
