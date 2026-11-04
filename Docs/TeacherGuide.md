# Teacher guide

## Classroom preparation

Install Unity `6000.3.27f2`, Blender that opens the 5.2.2 LTS files, and Cursor before students arrive. Run Play on `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` once. Confirm compilation is clean. Quest developer mode, Link, or an APK toolchain is homework for the teacher, not class time.

Each lesson is 90 minutes. If time is short, cut the extension, not the rule that students edit copies.

## Install requirements

See `Docs/WindowsSetup.md`. Pin MCP versions you actually tested. The example file `.cursor/mcp.example.json` is not a live secret store.

## Demo sequence

1. Show `AsterGT`, `NomaRobot`, and the street in the desktop scene. Say these meshes already exist.
2. Enter Play. Narrate Ready, crosswalk yield, and the hold at the gap.
3. Pause and Restart from the panel.
4. Only after the class has seen the hold, enable `allowJetFlight` on a copy if you want the jet arc. The saved project leaves it off.
5. Open the Meta scene and show the disabled `DesktopCamera` and the missing rig. Say hardware is NOT VERIFIED unless you just tested a headset.

## Teacher-prepared assets

`SourceArt/Blender`, `SourceArt/FBX`, the scenes `Workshop_Desktop.unity` and `Workshop_MetaVR.unity`, prefabs under `Assets/AI_VR_Workshop_V4/Prefabs`, and the route distances inside `WorkshopDrive`.

## Student-editable components

- Blender material `M_BodyPaint` on a student copy.
- `WorkshopSpeedControl.targetSpeedMps` (0.25 to 2).
- A duplicated scene created with `Workshop V4/Save active scene as new checkpoint`.

## Protected components

Do not delete or retarget, on the teacher scenes:

- `WorkshopDrive` references: pedestrian, walk, jets, comfort curtain.
- `DriverEyeAnchor` local pose.
- Waypoint-free route constants in `WorkshopDrive` (students do not need to edit the state machine).
- OpenXR loader assets.
- The missing Meta prefab instance. Replacing it belongs on a checkpoint scene.

## Recovery checkpoints

- Git history of this repository after publication.
- `Workshop V4/Save active scene as new checkpoint` before a risky scene edit.
- Do not run `Tools` art generators (`build_unity_assets.py` and the other builders) during class. They are teacher rebuild tools.

## Classroom troubleshooting

Use `Docs/Troubleshooting.md`. If MCP is down, teach the Editor and Blender directly and mark the agent step unfinished.

## Rubric

`Docs/AssessmentRubric.md`.
