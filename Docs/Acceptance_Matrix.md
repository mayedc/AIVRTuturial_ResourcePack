# Acceptance matrix

Use only these states: passed on this machine, failed on this machine, not run, or needs a visual decision. A report from another computer is evidence about that computer.

| Gate | State of this package | Still required before class |
|---|---|---|
| Older starter and image references | Reviewed. Reference images are not in the package. | Compare this tree with the classroom Windows machine. |
| Source models | `.blend` and `.fbx` files are in `SourceArt`. | Reopen them in Blender on the classroom machine. |
| Geometry, skeleton, animation | Not remeasured during packaging. | Visual check, hidden faces, and joint limits. |
| Unity file consistency | Scenes, meshes, materials, and `.meta` files were copied together. | Import in the editor and read the Console. |
| CP0 tools and versions | Not run in this packaging step. | Read both MCP connections and write the version record. |
| CP1 import and recolor | Not run as a student MCP exercise on this copy. | One student-copy import, recolor, save, and reopen. |
| CP2 compile and import | Not recompiled during packaging. | No compile errors, missing scripts, empty meshes, or magenta materials. Run the validate menu. |
| CP3 desktop route | Not played during packaging. | Both sample speeds, a full yield, the gap stop, pause, restart, and both ways to continue. |
| CP4 XR baseline | Meta prefab reference is present and unresolved. No headset was connected. | Tracking, scale, seat height, both eyes, curtain, and pause input. |
| CP5 Quest session | Not run. | Frame time, sustained play, and a separate jet comfort note. |
| Visual acceptance | Needs a visual decision. | Judge the models in Blender or Unity. Preview PNGs were withheld because they contained a local user path. |

## CP3 cases

1. At 0.25, 0.85, and 2 m/s the car stops at z = 7.5. It stays still until the robot reaches x = 4.5.
2. Negative, oversized, and non-finite speed inputs: finite values clamp to the range, and non-finite values leave the last valid value.
3. Pause and resume in Ready, while moving, Yield, AwaitChoice, JetFlight, FadeOut, and FadeIn. The timer and the robot both stop.
4. Restart from each stage returns the car, resets the robot pose and position, turns the jets off, and clears the curtain.
5. `BeginJetFlight` does nothing while jet flight is disabled. Fade transfer is refused when the curtain is missing. A missing robot reference holds the car and reports an error.
6. No road surface or bridging collider covers z = 37 to 43. At the landing z = 48 the whole car is past the gap.

## Restore points

- CP0: version record and the untouched teacher tree.
- CP1: the student's own `.blend` and FBX.
- CP2: a scene copy saved after the first clean import.
- CP3: a scene copy saved after the desktop route.
- CP4: a scene copy saved after the headset picture is actually shown.
- CP5: device notes. If you only have a desktop, leave CP5 as not run.

Each row needs the date, the person, the software versions, the file path, and either the success evidence or the original error text. Restore a copy. Do not pour a clean package over a student folder. A file hash shows that a copy is intact. It does not show that a headset is compatible.
