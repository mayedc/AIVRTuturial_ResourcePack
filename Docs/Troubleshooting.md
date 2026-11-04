# Troubleshooting

## Unity will not compile

Open this repository root, not a parent folder and not an older project. Read the first Console error. Do not delete `Packages/packages-lock.json` to silence it. `Workshop` scripts use Unity 6 APIs `FindAnyObjectByType` and `FindObjectsByType`.

## The car sits at the gap

`allowJetFlight` is false. That is the saved teaching default. The panel offers fade transfer at `AwaitChoice`. Jet flight appears only after the flag is enabled. The release Play Mode test enabled the flag at runtime and did not save the scene.

## Pause does nothing

The panel object is `AI_VR_Workshop_V4`, not the car. `WorkshopDesktopPanel.drive` must reference the `WorkshopDrive` on `AsterGT`.

## Robot does not walk

`WorkshopRobotWalk` runs while `WorkshopDrive` is in `Yield` and the car is not paused. There is no Animator controller in `Assets`. The FBX clip `Noma_Walk_InPlace_1s` is not the tested playback path.

## Blender MCP shows success but the teacher file changed

Stop. Restore `SourceArt/Blender/AsterGT.blend` from git. Future edits start with Save As.

## Quest view is black or the rig is missing

The Meta prefab is not in this pack. `DesktopCamera` is disabled on purpose in `Workshop_MetaVR.unity`. Do not enable it and call the result VR. Hardware result stays NOT VERIFIED until a headset is used.

## Validator fails before a push

Run `Tools/ValidateRepository.ps1` from the repository root. It prints categories and relative paths. It does not print secrets. `Library`, `Logs`, `UserSettings`, and generated `*.csproj` files are local warnings when gitignored.
