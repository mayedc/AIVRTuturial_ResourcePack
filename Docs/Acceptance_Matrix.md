# Acceptance matrix

Record the date, machine, software versions, scene or file, and the result. Use passed, failed, not run, or needs visual review for each check. Earlier release results are recorded in [historical validation](Validation/FinalReleaseReport.md).

| Gate | Evidence |
|---|---|
| CP0 · Setup | Both MCP readbacks, editor and package versions, zero compile errors, Windows and Link preparation recorded separately |
| CP1 · Blender | Student blend reopens, only M_BodyPaint changed, FBX exports with expected bounds and orientation |
| CP2 · Unity source build | **Fresh blank URP student project**, approved car FBX + three other source FBXs, compiled UnitySource Editor/Starter files, independently generated student scene, one correctly oriented/painted car, robot bones, colliders and camera. **No teacher .unity or .unitypackage**. |
| CP3 · Desktop starter | Cruise at 0.85 m/s, full crossing stop, robot clearance, stable wait at z = 32 m, pause and restart. No speed or flight control before coding. |
| CP3 · Desktop exercise | Target is bounded, actual cruise changes, crossing yield is retained, explicit flight lands at z = 48 m and comes to rest at z = 58 m. Pause and restart are checked. |
| CP4 · XR readiness and cockpit | [02_1](../Prompts/02_1_XR_Setup_And_Device_Check.md): Standalone OpenXR, installed Meta Core and **resolved camera prefab**, active Quest Link self-check; [02_2](../Prompts/02_2_Attach_Driver_Camera_And_Test.md): rig on a new student VR scene under DriverEyeAnchor, one tracked camera/listener, unit scale and documented tracking origin |
| CP5 · Device | Student actually wears headset during 02_2, confirms working wired PC Link, stereo image, seated driver view and head rotation/position tracking; otherwise NOT TESTED |

## Desktop details

- A finite out-of-range speed clamps after Prompt 1.4A. A non-finite input leaves the last valid value. Test the 0.85 and 1.20 m/s cruise separately.
- Trigger flight outside the gap hold and confirm that the car continues its current stage. At the gap, verify a hold before the explicit flight command.
- Pause keeps the route and robot still. Restart restores the starting position, robot pose, and jets off.
- The road has separate colliders on both sides of the gap. Verify that no added collider bridges z = 37 to 43.
