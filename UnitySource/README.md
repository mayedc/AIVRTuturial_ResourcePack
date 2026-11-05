# Source-first Unity construction kit (Plan B)

This directory contains **no** preassembled Unity scene, native mesh Prefab, imported Meta SDK binary or `.unitypackage`. Students build their own scene from the 1.2-approved `AsterGT_Color.fbx` and three course source FBXs with **Cursor + Unity MCP**.

## Copy into the student's blank URP Unity project

The student project is a **separate directory** from this Git repository.

| Repository source | Student Unity destination |
|---|---|
| `Runtime/Starter/*.cs` | `Assets/WorkshopStudentGenerated/Runtime/*.cs` |
| `Editor/*.cs` | `Assets/WorkshopStudentGenerated/Editor/*.cs` |
| `Config/WorkshopSceneSpec.json` | `Assets/WorkshopStudentGenerated/Config/WorkshopSceneSpec.json` |
| `StudentWork/<group>/AsterGT_Color.fbx` | `Assets/WorkshopStudentGenerated/Imported/AsterGT_Color.fbx` |
| `SourceArt/FBX/NomaRobot.fbx`, `MeridianCity.fbx`, `JetFX.fbx` | `Assets/WorkshopStudentGenerated/Imported/...` |

Copy dependencies only **after checking project identity and destination conflicts**. Preserve imported FBX `.meta` files on subsequent runs; do not overwrite a student's modified scripts. Allow Unity to compile, then use **Tools > Workshop > Build Student Scene From FBX** (or call the menu method through verified Unity MCP). Use **Tools > Workshop > Validate Student Scene (1.3)** to check the starter structure. After 1.4 edits, use **Tools > Workshop > Validate Student Scene (1.4)** for non-Play structural checks; only real student Play counts as behavioral acceptance.

The builder refuses to overwrite an existing `Workshop_Desktop_Student.unity`; this deliberately prevents wiping student work in 1.4. It does not regenerate scene content on rerun.

## Known runtime contracts

- Vehicle root +Z, start (1.8,0,0), driver's eye relative (-0.44,1.24,-0.12); real mesh axes and scale must be checked in Scene view after import.
- Crossing stop z=7.5; robot x=-4.5 to 4.5; open collider gap z=37–43; hold at z=32; route end z=58.
- Starter: fixed 0.85 m/s, no flight. **1.4A** enables speed changes, **1.4B** enables a user-click-only jet arc.
- `WorkshopRobotWalk` expects rigid FBX bones `Thigh_L/R`, `Shin_L/R`, `Foot_Sole_L/R`. This must be validated with imported hierarchy. Disable any imported Animator to avoid double animation.
- Imported FBX materials are mapped to generated **student-only URP Lit** material assets; confirm glass/transparency and selected paint by sight. Imported geometry is not a native mesh or a prebuilt Unity prefab.
- If builder fails because of unexpected import hierarchy, **stop and inspect**, do not claim success or silently substitute the old teacher scene.

## Checks

The editor validator confirms object references/colliders/script boundaries; it does not prove that geometry, material appearance, movement, the robot or the Quest headset works. A student must actually Play the full starter route before attempting 1.4, and wear the headset after 02_2 for a VR pass.

The builder and C# files have not been compiled in a live Unity Editor within this GitHub-only change; record the first clean-project test results before merging the PR.
