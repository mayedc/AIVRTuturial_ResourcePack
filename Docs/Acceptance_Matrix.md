# Acceptance matrix

Record the date, machine, software versions, scene or file, and the result. Use passed, failed, not run, or needs visual review for each check. Earlier release results are recorded in [historical validation](Validation/FinalReleaseReport.md).

| Gate | Evidence |
|---|---|
| CP0 · Setup | Both MCP readbacks, editor and package versions, zero compile errors, Windows and Link preparation recorded separately |
| CP1 · Blender | Student blend reopens, only M_BodyPaint changed, FBX exports with expected bounds and orientation |
| CP2 · Unity import | Scene checkpoint, one car visual, correct scale and materials, route references retained |
| CP3 · Desktop starter | Cruise at 0.85 m/s, full crossing stop, robot clearance, stable wait at z = 32 m, pause and restart. No speed or flight control before coding. |
| CP3 · Desktop exercise | Target is bounded, actual cruise changes, crossing yield is retained, explicit flight lands at z = 48 m and comes to rest at z = 58 m. Pause and restart are checked. |
| CP4 · Cockpit | Rig on a scene copy, one active HMD camera and one listener, unit rig scale and documented tracking origin |
| CP5 · Device | Wired Link, both eyes, seated view and responsive head tracking witnessed on the headset |

## Desktop details

- A finite out-of-range speed clamps after Exercise 2A. A non-finite input leaves the last valid value. Test the 0.85 and 1.20 m/s cruise separately.
- Trigger flight outside the gap hold and confirm that the car continues its current stage. At the gap, verify a hold before the explicit flight command.
- Pause keeps the route and robot still. Restart restores the starting position, robot pose, and jets off.
- The road has separate colliders on both sides of the gap. Verify that no added collider bridges z = 37 to 43.
