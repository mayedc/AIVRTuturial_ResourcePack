# Troubleshooting

## Unity will not compile

Open this repository root, not a parent folder and not an older project. Read the first Console error. Do not delete `Packages/packages-lock.json` to silence it. `Workshop` scripts use Unity 6 APIs `FindAnyObjectByType` and `FindObjectsByType`.

## The car sits at the gap

A steady hold before the gap is the expected starter result. Complete [Exercise 2B](Lesson03_MetaQuest.md) to add the command and flight path.

## Pause does nothing

The panel object is `AI_VR_Workshop_V4`, not the car. `WorkshopDesktopPanel.drive` must reference the `WorkshopDrive` on `AsterGT`.

## Robot does not walk

`WorkshopRobotWalk` runs while `WorkshopDrive` is in `Yield` and the car is not paused. There is no Animator controller in `Assets`. The FBX clip `Noma_Walk_InPlace_1s` is not the tested playback path.

## Blender MCP shows success but the teacher file changed

Stop. Restore `SourceArt/Blender/AsterGT.blend` from git. Future edits start with Save As.

## Quest view is black or the rig is missing

Start from a copy of the current desktop checkpoint. Verify the installed rig, Link session, selected OpenXR runtime and Standalone initialization in the VR copy. See the [XR checklist](05_XR_and_Quest_Acceptance.md).

## Validator fails before a push

Run `Tools/ValidateRepository.ps1` from the repository root. It prints categories and relative paths. It does not print secrets. `Library`, `Logs`, `UserSettings`, and generated `*.csproj` files are local warnings when gitignored.
