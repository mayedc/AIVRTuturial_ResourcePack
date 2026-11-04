# Scene test results

Date: 2026-11-04. Unity 6000.3.27f2. Scene under test: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`.

Evidence is Play Mode, not a static reading of the script. The Editor reported `playerLoopTicking=true`. The observer `Assets/AI_VR_Workshop_V4/Editor/WorkshopDesktopProbe.cs` appended stage lines while `Time.frameCount` advanced from 1 to 46218. The scene was not saved. `allowJetFlight` on disk stayed false. At `AwaitChoice` the probe set that existing public field so `WorkshopDrive` could take its jet branch.

Saved start values observed in Play Mode: origin (1.80, 0.00, 0.00), `savedAllowJet=False`, `savedTargetSpeed=0.85`, panel object `AI_VR_Workshop_V4`.

## Desktop checklist

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Vehicle starts | PASS | `stage=ApproachCrossing` at t=3.35 s, speed 0.07 m/s, frame 1457, after `Ready`. |
| 2 | Automatic route movement | PASS | Unattended stages `ApproachCrossing` -> `Yield` -> `ApproachGap` -> `AwaitChoice`. Summary `autoRoute=True`. |
| 3 | Stops before crosswalk | PASS | `stage=Yield` at t=14.40 s, z=7.49 m (route hold is 7.5 m), speed 0.00. `stopCrosswalk=True`. |
| 4 | Robot crosses | PASS | Pedestrian span 8.86 m during the yield. `robotCrossed=True`. Thigh pose changed (`walkPosed=True`). |
| 5 | Vehicle waits until crossing completes | PASS | z stayed 7.49 from Yield until `ApproachGap` at t=30.20 s. `waited=True`. |
| 6 | Vehicle resumes | PASS | `ApproachGap` then `AwaitChoice` at z=31.99 m. `resumed=True`. |
| 7 | Jet-assisted jump | PASS | After the probe enabled the existing `allowJetFlight` flag, `stage=JetFlight` at t=60.56 s. Peak height offset 3.00 m. `jumped=True` requires the jet object to be active and height above 1 m. The saved scene does not start the jet by itself. |
| 8 | Crosses road gap | PASS | Jet flight moved z from about 32 m to the arrival sample z=48.00 m. `crossedGap=True`. |
| 9 | Lands | PASS | `stage=Arrive` at t=70.35 s, y=0.00, z=48.00. `landed=True`. |
| 10 | Final stop | PASS | `stage=Complete` at t=83.14 s, z=57.99 m (route end is 58 m), frame 44522. `Complete` does not keep integrating motion. The same sample still showed `CurrentSpeedMps` 0.12 because the last approach step had not been forced to zero. The car was at the end stage and did not travel farther. |
| 11 | Pause and restart | PASS | Pause at z=1.24 m held for 1 s with drift 0.00 and stage unchanged (`pauseHeld=True`). After resume, z increased (`resumeMoved=True`). `Restart()` returned z=0.00 and `stage=Ready` (`restartReady=True`). |
| 12 | Speed-control component | PASS | After restart, `WorkshopSpeedControl.SetSpeedMps(1.6)` produced an observed cruise of 1.31 m/s. The saved target is 0.85 m/s, so the component changed the actual speed. `speedChanged=True`. |
| 13 | No extra runtime errors | PASS for workshop scripts | Console error count during the run: 1. The only error was `ArgumentOutOfRangeException` from `UnityEditor.Search.SearchInit.IndexationOnStartup` / `SearchDatabase.GetDefaultSearchDatabase`. Stack did not include `WorkshopDrive`, `WorkshopRobotWalk`, `WorkshopSpeedControl`, or `WorkshopDesktopPanel`. No missing-pedestrian error was logged. |

Summary line from the probe:

`result=reason:completed started=True autoRoute=True stopCrosswalk=True robotCrossed=True pedSpan=8.86 waited=True resumed=True jumped=True crossedGap=True maxY=3.00 maxZ=57.99 landed=True finalStop=False pauseHeld=True resumeMoved=True restartReady=True speedChanged=True speedAfter=1.31 cruiseBefore=1.31 walkPosed=True framesAdvanced=True errors=1 sawJet=True sawArrive=True sawComplete=True`

`finalStop=False` in that line is the probe's strict speed threshold (under 0.05 m/s on the first Complete sample). The checklist item is still PASS for the reason in row 10. `cruiseBefore=1.31` is not a separate baseline: the probe kept the max speed after the 1.6 m/s change, so that field is not used as the before/after comparison. The before value is the saved 0.85 m/s target.

## Meta VR scene

| Check | Result |
|---|---|
| Hierarchy and eye anchor | PASS as serialized data. See `UnityValidation.md`. |
| OpenXR settings | PASS as assets. |
| Duplicate active cameras | PASS. Enabled cameras: 0. Desktop camera and listener are disabled. |
| Script overriding headset tracking | PASS. No such script is active. No tracking driver is loaded. |
| Missing OVRCameraRig | FAIL as a live rig. GUID `126d619cf4daa52469682f85c1378b4a` has no asset. |
| Play Mode on the VR scene | NOT VERIFIED. Not entered. |
| Quest 3 hardware | NOT VERIFIED. |

## What was not tested

- Visual screenshot review. No new image was captured. Do not treat this log as a picture of the city.
- Both-eye rendering, comfort, or device frame time.
- `Workshop_XR_Setup.unity` in Play Mode. It is not in the build list.
