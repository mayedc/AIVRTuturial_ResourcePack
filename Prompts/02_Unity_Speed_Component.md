Use the workshop-unity-lesson skill for the speed exercise.

Through Unity MCP, confirm the open scene is a student copy of `Workshop_Desktop`. Read the Console and the components on the Aster GT root. If `WorkshopSpeedControl` is missing, add it once. If it exists, reuse it. Set `targetSpeedMps` to 1.2 and read the Inspector value back. Keep `WorkshopDrive` and every reference on it. Do not add the older `AutoDriveRoute`.

Wait until compilation finishes, run `Workshop V4/Validate active workshop scene`, then enter Play Mode. Compare 0.6 and 1.2 m/s. The speed change must be visible, the car must still stop at the crosswalk, and it must wait until the robot has passed. Save a new scene after you exit Play. Report the compile and Play results you actually got. Anything you could not run stays not tested.
