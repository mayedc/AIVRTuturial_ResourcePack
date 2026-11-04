# Teacher answers

Unity imports scripts from the project's Assets folder. These answers live outside it. Students should attempt the two coding exercises before reading the reference files.

- `Original/` preserves the four source files from main at `c3aaaee8203f9905d219624266da2b9c73e89ca6`. The archived desktop probe expects those original runtime scripts and is for historical reproduction on that revision.
- `Reference/` contains two replacements that work with the student panel. Copy the content into the existing file of the same name under `Assets/AI_VR_Workshop_V4/Runtime/` on a separate teacher project copy. Keep each original `.meta` in place. Copying a second C# file into Assets would create duplicate types.

1. Apply `WorkshopSpeedControl.cs` first. Compile and compare observed cruise at 0.85 and 1.20 m/s in Play. The car should yield and still stop at the gap.
2. Apply `WorkshopDrive.cs` second. Compile and confirm that the car holds at the gap until you press **Fly across the gap**. Watch the jets, landing, final stop, pause and restart. Try flight on desktop first.
3. Use a separate checkpoint for Quest Link. Start the headset check with the vehicle stationary. Record headset results separately.

The reference preserves the car, the route and the eye anchor. Its flight uses a scripted path. The archived fade transfer is for reproducing the earlier teacher demonstration.
