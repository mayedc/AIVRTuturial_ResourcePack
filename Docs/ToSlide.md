# ToSlide

Proposed slides for a course introduction. No screenshot files are stored in this repository. Every visual that is not an existing project asset is marked missing. Do not substitute concept art for a Unity capture.

## Slide 1

- Slide Number: 1
- Slide Title: AI-Assisted VR Driving Workshop
- Learning Objective: State what the pack is for.
- Key Messages: Students modify prepared assets. The repository name is AIVRTuturial_ResourcePack.
- Suggested Visual: Title card.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Say the spelling of the repository name once so clones use the published URL.
- Live Demonstration: None.
- Student Interaction: None.
- Estimated Duration: 1 minute
- Expected Outcome: Students know the course name.

## Slide 2

- Slide Number: 2
- Slide Title: What you will be able to do
- Learning Objective: List the three lesson outcomes.
- Key Messages: Recolor `M_BodyPaint`. Change `WorkshopSpeedControl`. Explain the Quest scene without inventing a headset result.
- Suggested Visual: Three bullets.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Jet flight is optional and is not a grade.
- Live Demonstration: None.
- Student Interaction: Read the three outcomes aloud.
- Estimated Duration: 2 minutes
- Expected Outcome: Outcomes are written in student notes.

## Slide 3

- Slide Number: 3
- Slide Title: Prepared assets, not a blank scene
- Learning Objective: Separate a prompt, a model, and a running scene.
- Key Messages: The car, robot, and street already exist under `SourceArt` and `Assets/AI_VR_Workshop_V4`.
- Suggested Visual: File tree.
- Existing Screenshot or Asset Path: `Docs/AssetManifest.md`
- Speaker Notes: Generation from scratch is out of scope.
- Live Demonstration: Show the Project window folders.
- Student Interaction: Find `AsterGT` in the Project window.
- Estimated Duration: 3 minutes
- Expected Outcome: Students can point at the asset folders.

## Slide 4

- Slide Number: 4
- Slide Title: Technical architecture
- Learning Objective: Name the car root and the panel root.
- Key Messages: `WorkshopDrive` and `WorkshopSpeedControl` are on `AsterGT`. The panel is on `AI_VR_Workshop_V4`.
- Suggested Visual: Hierarchy sketch.
- Existing Screenshot or Asset Path: Missing visual asset. Hierarchy is described in `Docs/ProjectArchitecture.md`.
- Speaker Notes: Do not add a second drive component.
- Live Demonstration: Select `AsterGT` and show the two components.
- Student Interaction: Read the component names from the Inspector.
- Estimated Duration: 3 minutes
- Expected Outcome: Students can find both components.

## Slide 5

- Slide Number: 5
- Slide Title: Agents and MCP
- Learning Objective: Define MCP as a connection, not a picture generator.
- Key Messages: Cursor talks to Blender or Unity only when the server returns real data. A status light is not evidence.
- Suggested Visual: Diagram of Cursor, MCP, Blender, Unity.
- Existing Screenshot or Asset Path: Missing visual asset. Example config: `.cursor/mcp.example.json`.
- Speaker Notes: `.cursor/mcp.json` stays untracked.
- Live Demonstration: None yet.
- Student Interaction: Say what a successful MCP reply must include.
- Estimated Duration: 3 minutes
- Expected Outcome: Students require a file path or scene path in the reply.

## Slide 6

- Slide Number: 6
- Slide Title: Install Cursor and this repository
- Learning Objective: Open the Unity project root.
- Key Messages: The folder that contains `Assets`, `Packages`, and `ProjectSettings` is the project. Unity version is 6000.3.27f2.
- Suggested Visual: Hub project path, without a personal username.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Do not open an older development folder.
- Live Demonstration: Show the Hub entry only if it does not reveal a local user path.
- Student Interaction: Confirm the editor version from `ProjectSettings/ProjectVersion.txt`.
- Estimated Duration: 3 minutes
- Expected Outcome: The correct project is open.

## Slide 7

- Slide Number: 7
- Slide Title: Connect Blender
- Learning Objective: Start from the example MCP entry.
- Key Messages: Windows example uses `uvx`, Python 3.11, and `mcp-for-blender`. The add-on is not in this pack.
- Suggested Visual: The example JSON.
- Existing Screenshot or Asset Path: `.cursor/mcp.example.json`
- Speaker Notes: Pin the server version you tested. This release did not launch Blender.
- Live Demonstration: If the teacher machine is connected, read back the open file path.
- Student Interaction: Record connected or not finished.
- Estimated Duration: 3 minutes
- Expected Outcome: A truthful connection status.

## Slide 8

- Slide Number: 8
- Slide Title: Connect Unity
- Learning Objective: Use Window > MCP for Unity or the Editor directly.
- Key Messages: The manifest references `com.coplaydev.unity-mcp`. The example URL is `http://localhost:8080/mcp`. Do not publish that port.
- Suggested Visual: Unity MCP window.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Lock commit is `81542a7e86292b5c4c21b1782c5af23b567f45ce`.
- Live Demonstration: Ask the agent for the active scene path, or read it in the Hierarchy.
- Student Interaction: Write the scene path `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`.
- Estimated Duration: 3 minutes
- Expected Outcome: The desktop scene path is recorded.

## Slide 9

- Slide Number: 9
- Slide Title: Prepared vehicle
- Learning Objective: Identify the body material.
- Key Messages: `AsterGT` is the car. Recolor `M_BodyPaint` only. Sources: `SourceArt/Blender/AsterGT.blend` and `SourceArt/FBX/AsterGT.fbx`.
- Suggested Visual: Car in the scene.
- Existing Screenshot or Asset Path: Missing visual asset. Model file: `SourceArt/Blender/AsterGT.blend`.
- Speaker Notes: About 4.9 m long. Doors and the hood do not open.
- Live Demonstration: Select a body renderer and show the material name.
- Student Interaction: Find `M_BodyPaint` in the material list.
- Estimated Duration: 3 minutes
- Expected Outcome: The material name is written down.

## Slide 10

- Slide Number: 10
- Slide Title: Prepared cockpit
- Learning Objective: Leave interior materials alone.
- Key Messages: Seat, glass, screen, and trim materials exist on `AsterGT`. `DriverEyeAnchor` is the eye point, not a personal calibration.
- Suggested Visual: Eye anchor transform.
- Existing Screenshot or Asset Path: Missing visual asset. Local position is documented in `Docs/ProjectArchitecture.md`.
- Speaker Notes: Unity local position (-0.44, 1.24, -0.12), scale (1, 1, 1).
- Live Demonstration: Select `DriverEyeAnchor`.
- Student Interaction: Read the local position.
- Estimated Duration: 2 minutes
- Expected Outcome: Students do not move the eye anchor.

## Slide 11

- Slide Number: 11
- Slide Title: Robot pedestrian
- Learning Objective: Explain how the robot moves in Unity.
- Key Messages: `NomaRobot` uses `WorkshopRobotWalk`. There is no Animator controller in `Assets`. The FBX also contains `Noma_Walk_InPlace_1s`, which is not the tested playback path.
- Suggested Visual: Robot hierarchy.
- Existing Screenshot or Asset Path: Missing visual asset. Prefab: `Assets/AI_VR_Workshop_V4/Prefabs/NomaRobot.prefab`.
- Speaker Notes: Play Mode measured an 8.86 m pedestrian span during the yield.
- Live Demonstration: Enter Play and watch the yield, or describe the recorded test if time is short.
- Student Interaction: Name one bone, such as `Thigh_L`.
- Estimated Duration: 3 minutes
- Expected Outcome: Students do not add a second walk system.

## Slide 12

- Slide Number: 12
- Slide Title: Futuristic street
- Learning Objective: Locate the road, the crossing, and the gap.
- Key Messages: `MeridianCity` is the street. Road modules exist as source art. Two colliders cover the near road and the landing, not the gap.
- Suggested Visual: Scene view along +Z.
- Existing Screenshot or Asset Path: Missing visual asset. Colliders: `RoadCollider_Main`, `RoadCollider_Landing`.
- Speaker Notes: No LOD and no occlusion bake.
- Live Demonstration: Frame the city in the Scene view.
- Student Interaction: Find both collider names.
- Estimated Duration: 2 minutes
- Expected Outcome: Students know the gap is open geometry.

## Slide 13

- Slide Number: 13
- Slide Title: Autonomous driving event sequence
- Learning Objective: Order the stages.
- Key Messages: `Ready`, `ApproachCrossing` at 7.5 m, `Yield`, `ApproachGap` at 32 m, `AwaitChoice`, then jet or fade, landing at 48 m, end at 58 m.
- Suggested Visual: Stage list from `WorkshopDrive`.
- Existing Screenshot or Asset Path: `Assets/AI_VR_Workshop_V4/Runtime/WorkshopDrive.cs`
- Speaker Notes: The release Play Mode log is summarized in `Docs/Validation/SceneTestResults.md`.
- Live Demonstration: Play until `AwaitChoice`.
- Student Interaction: Call out the stage label on the panel.
- Estimated Duration: 4 minutes
- Expected Outcome: Students can order the stops.

## Slide 14

- Slide Number: 14
- Slide Title: Blender color exercise
- Learning Objective: Save a copy before editing.
- Key Messages: Use `Prompts/Blender/RecolorBody.md`. Never overwrite the teacher blend.
- Suggested Visual: Before and after of the body. Both captures are student work.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Helper script `Tools/blender_safe_recolor.py` does not save by itself.
- Live Demonstration: Change the copy if Blender is connected. Otherwise show the material slot only.
- Student Interaction: Start the student file name.
- Estimated Duration: 3 minutes
- Expected Outcome: A student filename is chosen.

## Slide 15

- Slide Number: 15
- Slide Title: Unity speed exercise
- Learning Objective: Change speed without breaking the yield.
- Key Messages: Saved target is 0.85 m/s. Clamp is 0.25 to 2. A Play Mode check reached 1.31 m/s after `SetSpeedMps(1.6)` and still completed the route logic.
- Suggested Visual: Inspector field `targetSpeedMps`.
- Existing Screenshot or Asset Path: Missing visual asset. Script: `Assets/AI_VR_Workshop_V4/Runtime/WorkshopSpeedControl.cs`.
- Speaker Notes: Duplicate the scene before a saved edit.
- Live Demonstration: Move the panel slider and show the label.
- Student Interaction: Predict whether a faster car should still stop.
- Estimated Duration: 3 minutes
- Expected Outcome: Students expect a stop at 7.5 m.

## Slide 16

- Slide Number: 16
- Slide Title: XR Origin and the eye anchor
- Learning Objective: See that this pack does not contain a loaded XR Origin.
- Key Messages: The Meta scene parents the missing `Workshop_OVRCameraRig` under `DriverEyeAnchor`. No tracking driver is loaded. Desktop camera is disabled.
- Suggested Visual: Meta scene hierarchy.
- Existing Screenshot or Asset Path: Missing visual asset. Scene: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity`.
- Speaker Notes: Do not scale the eye anchor away from 1.
- Live Demonstration: Show the disabled Camera checkbox.
- Student Interaction: Count enabled cameras. The validation count was 0.
- Estimated Duration: 3 minutes
- Expected Outcome: Students see why the Game view can be empty.

## Slide 17

- Slide Number: 17
- Slide Title: Meta Quest 3 preparation
- Learning Objective: Separate project settings from a device test.
- Key Messages: Quest 3 is enabled in OpenXR. Android min SDK is 32. No APK and no headset test are in this release.
- Suggested Visual: Player Settings Android section, cropped so no machine name shows.
- Existing Screenshot or Asset Path: Missing visual asset.
- Speaker Notes: Say NOT VERIFIED out loud.
- Live Demonstration: None on hardware unless a headset is connected today.
- Student Interaction: Write the hardware line.
- Estimated Duration: 2 minutes
- Expected Outcome: The notebook says NOT VERIFIED or a real device result.

## Slide 18

- Slide Number: 18
- Slide Title: Testing the desktop route
- Learning Objective: Know what PASS means.
- Key Messages: PASS requires Play Mode or a log with advancing frames. The release probe is `Workshop V4/Run desktop play mode probe`.
- Suggested Visual: Stage log excerpt.
- Existing Screenshot or Asset Path: `Docs/Validation/SceneTestResults.md`
- Speaker Notes: `finalStop` in the raw probe used a strict speed threshold. The car did reach `Complete` at z=57.99.
- Live Demonstration: Optional probe if time allows. It takes about two minutes.
- Student Interaction: Match one log line to a checklist row.
- Estimated Duration: 3 minutes
- Expected Outcome: Students can read a stage line.

## Slide 19

- Slide Number: 19
- Slide Title: Troubleshooting
- Learning Objective: Use the first real error.
- Key Messages: Gap hold is the default. Missing Meta prefab is expected. Do not delete teacher files to fix either one.
- Suggested Visual: Troubleshooting headings.
- Existing Screenshot or Asset Path: `Docs/Troubleshooting.md`
- Speaker Notes: Keep the class on one XR path.
- Live Demonstration: Show the `allowJetFlight` checkbox still off.
- Student Interaction: Pick one failure and the matching fix.
- Estimated Duration: 2 minutes
- Expected Outcome: Students do not enable the desktop camera in the VR scene.

## Slide 20

- Slide Number: 20
- Slide Title: Reproduce the pack from GitHub
- Learning Objective: Clone and open the same root.
- Key Messages: Public repository name uses the spelling Tuturial. Do not commit `Library` or generated project files.
- Suggested Visual: Repository file list.
- Existing Screenshot or Asset Path: `README.md`
- Speaker Notes: Fill the URL after publication. Do not invent a commit SHA on the slide.
- Live Demonstration: Show `gh repo view` only after the repository exists.
- Student Interaction: Find `LICENSE` and `Docs/ToSlide.md` in the tree.
- Estimated Duration: 2 minutes
- Expected Outcome: Students know which folder to open.

## Slide 21

- Slide Number: 21
- Slide Title: Credits and licenses
- Learning Objective: Keep third-party software separate from the MIT course files.
- Key Messages: Course models and scripts are MIT. Unity, Blender, Cursor, and Meta are not. The Meta prefab is not in the repo.
- Suggested Visual: License table.
- Existing Screenshot or Asset Path: `Docs/AssetLicenses.md` and `LICENSE`
- Speaker Notes: An unclear new asset is a stop, not a guess.
- Live Demonstration: None.
- Student Interaction: Name one file covered by MIT.
- Estimated Duration: 2 minutes
- Expected Outcome: Students leave downloaded models out of the repo.

## Slide 22

- Slide Number: 22
- Slide Title: Learning check
- Learning Objective: Finish the student checklist.
- Key Messages: Copy, color, speed, yield, hierarchy, honest hardware line.
- Suggested Visual: Checklist.
- Existing Screenshot or Asset Path: `Docs/StudentChecklist.md`
- Speaker Notes: Use `Docs/AssessmentRubric.md` after class.
- Live Demonstration: None.
- Student Interaction: Tick the rows they can already defend.
- Estimated Duration: 3 minutes
- Expected Outcome: Unfinished rows are visible before lab time.
