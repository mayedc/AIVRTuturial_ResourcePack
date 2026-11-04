# Clean-clone reproduction

Date: 2026-11-04.

## Test environment

Windows desktop. Unity Editor 6000.3.27f2. The clone is a new directory outside the original development project and outside the release-candidate folder. No username, machine path, or device serial is recorded here. Git LFS reported no files.

## Clone

| Check | Result |
|---|---|
| URL | https://github.com/mayedc/AIVRTuturial_ResourcePack |
| HEAD | `0f92c6c672e94f56d72681e982f0851b129b339d` |
| Branch | `main` tracking `origin/main` |
| Working tree after clone | Clean aside from ignored Editor caches created when the clone was opened |
| Desktop scene | `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` present |
| Meta scene | `Assets/AI_VR_Workshop_V4/Scenes/Workshop_MetaVR.unity` present |
| Blender car | `SourceArt/Blender/AsterGT.blend` present |
| Assets copied by hand from the original project | None |

## Package restoration and compilation

The clone Editor reached ready in about 224 seconds and restored packages from `Packages/manifest.json`. `console status` reported `compilationFailed=false`, `compiling=false`, and `consoleErrors=0`.

## Desktop gameplay

Play Mode on the published desktop scene, with editor auto-tick and run-in-background. `editor status` showed `playerLoopTicking=true` and the frame count advanced. The observer shipped in the repository is `Assets/AI_VR_Workshop_V4/Editor/WorkshopDesktopProbe.cs`.

Result line:

`result=reason:completed started=True autoRoute=True stopCrosswalk=True robotCrossed=True pedSpan=8.86 waited=True resumed=True jumped=True crossedGap=True maxY=3.00 maxZ=57.99 landed=True finalStop=False pauseHeld=True resumeMoved=True restartReady=True speedChanged=True speedAfter=1.31 cruiseBefore=1.31 walkPosed=True framesAdvanced=True errors=0 sawJet=True sawArrive=True sawComplete=True`

| Item | Result |
|---|---|
| Start, route, crosswalk stop, robot cross, wait, resume | PASS |
| Jet, gap, landing, complete stage | PASS. The saved `allowJetFlight` value was false. The probe enabled that existing field at the gap and did not save the scene. `Complete` was reached at z=57.99. |
| Pause, restart | PASS |
| Speed change | PASS. `SetSpeedMps(1.6)` produced an observed cruise of 1.31 m/s, above the saved 0.85 m/s target. |
| Workshop runtime errors | PASS. `errors=0` on this clone run. |

## Teaching exercises

| Exercise | Result |
|---|---|
| Open the prepared Blender car and recolor a copy | NOT VERIFIED. Blender was not available as a command on this machine, so the file was not opened in Blender and no student recolor file was saved. The teacher blend in the clone was not modified. |
| Unity speed control | PASS, as in the Play Mode row above. The yield and the later stages still occurred. |
| Markdown links in the clone | 0 broken relative links among the repository Markdown files. |

## Hardware

Quest 3 hardware validation: NOT VERIFIED. No headset was connected. No APK was built.

## Known limitations

The Meta camera prefab GUID `126d619cf4daa52469682f85c1378b4a` is still unresolved. Jet flight remains off in the saved scene. GitHub's repository size statistic was still 0 KB immediately after the push and is not used as the working-tree size.
