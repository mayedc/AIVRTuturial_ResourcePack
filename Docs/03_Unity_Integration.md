# Unity integration

Open `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` after the project compiles. The meshes are assets in this folder. They are not built from images at runtime.

The teaching root contains the city, the car, the robot, and two road colliders. The `AsterGT` root has the speed and drive components, the jets, the eye point, and the desktop camera. Save a student scene copy before editing.

## Route values

| Item | Value |
|---|---|
| Car start | Unity (1.8, 0, 0), moving on +Z |
| Ready hold | 3 s |
| Target speed | 0.85 m/s, adjustable from 0.25 to 2 m/s |
| Acceleration | 0.65 m/s². Braking speed is limited by the distance that remains. |
| Yield stop | z = 7.5 m. The crosswalk center is z = 14 m. The nose must not enter the crossing. |
| Robot | x = -4.5 to +4.5 at 0.6 m/s, starting 1 s after the car is fully stopped |
| Gap | Road deck missing from z = 37 m to 43 m. The car center stops at z = 32 m. |
| Jet flight | After the teacher enables it: z = 32 m to 48 m in 10 s, peak height 3 m, no camera pitch or roll |
| Comfort transfer | Fade to black, move to z = 48 m, fade in. If the curtain reference is missing, the transfer is refused. |
| Route end | z = 58 m |

The starter uses a fixed target and holds before the gap. Exercise 2A implements `WorkshopSpeedControl.SetSpeedMps(float)` for ground movement. Exercise 2B adds a commanded flight. Pause and restart remain on the existing route.

This is a teaching sequence. It is not a driving dynamics model, a planner, or a safety certification.

## Using the module in another project

1. Work in a full copy of that project. Keep its packages, project settings, XR origin, and older drive scripts until you have a reason to change them.
2. The scripts use the namespace `AIVRWorkshop.V4` and their own folder. Do not overwrite an older `AutoDriveRoute`.
3. To reuse only the art, parent the Aster GT prefab or FBX under the old car's `Visual` child. Do not also add `WorkshopDrive`.
4. To use this route, open these scenes or a new car root. One transform should have one mover. Old waypoint lists are not migrated onto this straight route.
5. For an existing XR rig, pass the desktop route first, then parent the rig to `DriverEyeAnchor` as described in the XR note. Keep one active HMD camera and one audio listener.
6. `Tools/Install-Workshop.ps1` copies `Assets/AI_VR_Workshop_V4` into another project and stops if that folder already exists.

## Fault finding

| What you see | Check first |
|---|---|
| Magenta materials | Shader import, Console, and whether the project is HDRP. Do not regenerate every mesh to hide the message. |
| Missing or inside-out mesh | Mesh reference, bounds, and winding. Re-check on any editor other than the one that saved the scene. |
| A second speed component | `WorkshopDrive` already requires `WorkshopSpeedControl` on the same object. |
| Robot does not cross | The drive stage is Yield, and `pedestrian` plus `pedestrianWalk` are assigned. |
| Car waits at the gap | `AwaitChoice` is the checkpoint. Continue with comfort transfer, or enable jet flight. |
| Jet button is hidden | Complete Exercise 2B to enable the button. |
| An FBX edit does not change the scene | The scene shows the native meshes. Replace only the `StudentVisual` child. |
| Pose is wrong after restart | Two animators may both be active. Use the reset on the teaching components. |

The validator menu is `Workshop V4 > Validate active workshop scene`. Its script looks for scenes under `Assets/AI_VR_Workshop_V4/Scenes`.
