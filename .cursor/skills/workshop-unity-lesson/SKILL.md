---
name: workshop-unity-lesson
description: Adjust the speed component on a student copy of the desktop teaching scene and check the yield and gap stops.
---

Read [Unity integration](../../../Docs/03_Unity_Integration.md). Confirm the project path and the open scene through MCP. Do not use an older project scene as the exercise.

- Edit a student copy. If the teaching folder already exists, stop. Do not merge or delete it.
- `WorkshopDrive` and `WorkshopSpeedControl` belong on the same car root. Target speed is in metres per second and stays between 0.25 and 2. Students change the target. Braking stays in the drive component.
- If the speed component is already present, change it. Do not add another. Do not put this drive component on a root that already has the older `AutoDriveRoute`.
- After the edit, wait for compilation, read the Console, then run `Workshop V4/Validate active workshop scene`. A static pass is not a Play Mode pass.
- Check three results: the speed change is visible, the car stops fully at the crosswalk until the robot has left, and the car stops again before the gap. Repair a missing reference before hiding the error.

Done means a new scene is saved and the Console and Play results are recorded. XR, an APK, and Quest frame rate follow the headset checklist. This skill does not infer those results.
