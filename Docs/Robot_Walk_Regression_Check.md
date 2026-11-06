# Robot gait and crossing regression protocol

**Status:** GitHub source review completed; real Unity Editor + physical foot contact are **NOT TESTED** in this GitHub-only change.

## Expected ownership

- `WorkshopRobotWalk` is the only runtime driver of robot limb poses; source-imported Animator/Animation/legacy components must be disabled on the robot.
- `WorkshopDrive` alone translates the robot across the road. The in-place gait must not translate or reset the crossing root at cycle boundaries.
- Scripted limb rotations are offsets from **imported FBX bind local rotations**, never replacements assuming world-aligned bones.
- Foot contact is judged against the actual road top surface (Y=0 for the generated scene) using the two sole renderers; the scripted grounding correction must not hide gross FBX orientation/scale errors.

## On a clean Windows URP project

1. Copy the 4 Starter and 2 Editor scripts + JSON from this repository, import the student-selected car and the three source FBXs, and build the generated scene with the Editor menu.
2. Read the Unity Console. Confirm no compile errors, a single `WorkshopRobotWalk` and no enabled competing robot Animator, Legacy Animation or root-motion controller.
3. Inspect `NomaRobot` in Scene view: correct ~1.8 m height, forward-facing walking direction, both sole meshes visible, world floor Y=0, no body buried in road. Check source FBX bone axes and importer settings if not.
4. Manually start Play. At the crossing, inspect the left and right sole over **at least 3 complete one-second gait loops**: a planted sole does not float or penetrate; a swinging sole lifts, lands and moves naturally. Watch knees and arms for inverted axes.
5. Watch the entire crosswalk from X=-4.5 to X=4.5. Verify no unexpected root teleport at loop rollover or at end; pedestrian remains at far side until the student explicitly presses Restart.
6. Pause/Resume: no walking when paused, no position jump after resume. Restart: crosswalk and pose intentionally return to initial state **only on the user-triggered Restart**.
7. Play through z=32 gap hold and then independently test exercise 1.4. Confirm the robot remains stationary after crossing and the car behavior is unchanged.
8. Capture start/mid/end position and foot-ground screenshots, log exact Unity version, importer settings, visual observations and PASS/FAIL/NOT TESTED. **The static source validator cannot replace this check.**

**Known failure patterns:** Imported bone transforms may differ across Unity FBX importer/rig configurations; if arms, knees or toe direction still look wrong, inspect actual local bone axes and use the original Blender animation clip with root motion off, not another simultaneous pose source. A >30 cm grounding correction is rejected and should prompt an asset import/scale investigation. A false-looking gait must not be reported as validated.
