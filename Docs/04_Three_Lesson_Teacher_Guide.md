# Three-lesson teacher guide

Each lesson is 90 minutes for pairs. Downloads, MCP install, Unity compilation, and Quest developer setup happen before class. If a lesson is shorter, cut the demonstration or the extension. Do not move modeling or device installation back into class time.

## Lesson 1: change a real model through an agent

Outcome: a student can tell a reference image, a 3D model, and a running scene apart, can show that MCP is connected, and can recolor one named material.

| Time | Activity | Checkpoint |
|---|---|---|
| 0-10 | Show the real models and the difference from earlier failed attempts. Students edit prepared assets only. | Task scope is stated |
| 10-25 | Prompt 00. Read the Blender file and its objects. | CP0: actual MCP return values |
| 25-40 | Append the teacher car collection into an empty scene and save a student copy. | Original parts and scale remain |
| 40-60 | Prompt 01. Change the silver-blue body to red, read `M_BodyPaint` back, compare screenshots. | CP1: only the body color changes |
| 60-75 | Export a new FBX and discuss source data versus an evaluated mesh. | The file exists and opens again |
| 75-90 | Partners check glass, tires, and the eye point. Submit the `.blend`, before and after images, and a short log. | Done without the teacher driving the tools |

Expected mistake: the wrong material is selected. Do not rebuild the mesh in class. Extension: change an emission color or hide the yoke, name the object, and leave the eye point still.

## Lesson 2: change observable Unity behavior

Outcome: a student can find the car root, set the target speed, and see that acceleration and braking still work.

| Time | Activity | Checkpoint |
|---|---|---|
| 0-15 | Open the desktop scene. Show prefabs, components, and the Inspector. | Desktop baseline runs |
| 15-30 | Read the project, scene, and Console through MCP. Save a scene copy. | CP2: no missing script |
| 30-50 | Prompt 02. Add `WorkshopSpeedControl` only if it is missing. Otherwise set 1.2 m/s. | The Inspector value matches |
| 50-65 | Compare 0.6 and 1.2 m/s and the time to the stop. | The speed change is visible |
| 65-80 | Prompt 03. The car stops for the robot and stops again before the gap. | CP3: full yield and stop |
| 80-90 | Record both speeds, the stop positions, the Console, and one sentence on the mechanism. | Another person can repeat it |

Do not add a second copy of a component that is already there. A teacher may demonstrate Add Component on a static car. The route car already has the speed component because `WorkshopDrive` requires it. An extension may add a button that calls `SetSpeedMps` on the student copy. It must not edit the drive state machine.

## Lesson 3: VR observation and checks

Outcome: a student can separate a desktop result from a headset result, can experience the yield, and knows when to use the fade and when a teacher may enable the jet.

| Time | Activity | Checkpoint |
|---|---|---|
| 0-15 | Show the XR wiring that actually exists, and re-check seat height, forward axis, and how to stop. | CP4: device baseline |
| 15-30 | Prompt 04. Read XR state and the safe defaults. | Do not reinstall plugins |
| 30-55 | Groups experience the yield and the fade. A partner can pause from the desktop panel. | State and discomfort notes |
| 55-70 | Only a willing person, after a comfort check, tries the jet. | CP5: jet recorded separately |
| 70-85 | Students explain "I saw it" versus "it is verified on this device". | Notes stay per platform |
| 85-90 | Submit the scene copy, parameters, and experience notes. | Lesson complete |

If no headset is available, lesson 3 is a desktop observation plus an XR wiring review, and the grade record says "headset experience not done". Do not spend class time waiting for an APK. A teacher brings an already accepted build or uses a tested PCVR path.

## Score (100)

MCP round trip 20. Import and recolor only the named material 20. Files that reopen, with clear names, 15. Speed control and its limits 20. Yield and gap evidence 15. Honest split between tested and untested platforms 10. Original modeling is not a student score.

## Freeze and restore

Verify CP0 through CP5 before class. Students save into their own numbered folders. `Workshop V4 > Save active scene as new checkpoint` writes a new scene and does not overwrite the current one. Restore the previous checkpoint and keep the broken copy for review. Rehearse once from a clean Windows user before the course and write the time and failures into the acceptance matrix.
