# Lesson 3 — Speed, flight, and the tracked cockpit (45 minutes)

## 00–22 | Exercise 2 — Implement and test vehicle behavior

- **7 minutes**. Open the Lesson 2 checkpoint, record the baseline cruise, and use the [speed prompt](../Prompts/Unity/AdjustSpeed.md) to implement the bounded control. Compare 0.85 and 1.20 m/s in Play and verify the crosswalk and gap stops.
- **10 minutes**. Use the [flight prompt](../Prompts/03_Yield_and_Jet_Check.md) to implement a scripted arc from the gap hold to the landing. Require an explicit command at the gap. Reuse the existing car and jet objects.
- **5 minutes**. Check Console, flight, landing, final stop and restart in the desktop scene. Save a checkpoint. The instructor can restore a working copy from the reference answers if a group needs to move on.

## 22–45 | Exercise 3 — Attach a tracked cockpit

- **5 minutes**. Start the prepared Windows Quest Link session. Confirm the headset, installed package and selected PC runtime.
- **3 minutes**. Locate `DriverEyeAnchor` and `DesktopCamera` and explain what the car root and headset tracking each control.
- **7 minutes**. Duplicate the last good scene. Use the [XR prompt](../Prompts/04_XR_and_Quest.md) to attach the tested rig and disable the desktop camera and listener.
- **5 minutes**. With the car stationary and the user seated, confirm picture in both eyes, neutral view and head tracking. Use [the XR checklist](05_XR_and_Quest_Acceptance.md).
- **3 minutes**. Record CP4/CP5 results and wrap up. If Link fails, inspect the hierarchy, record the failure and preserve the desktop result.
