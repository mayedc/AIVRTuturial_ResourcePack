# Quick start

1. Install Unity `6000.3.27f2` with the Android Build Support module only if lesson 3 will build an APK later.
2. Clone this repository and open the folder that contains `Assets`, `Packages`, and `ProjectSettings`.
3. Let the Editor restore packages from `Packages/manifest.json`. Compilation must finish with no errors.
4. Open `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`.
5. Press Play. Confirm the panel `ASTER / AI VR DRIVING WORKSHOP` appears.
6. Watch the car leave `Ready`, stop at the crosswalk while `NomaRobot` crosses, then stop again at the gap (`AwaitChoice`).
7. Optional teacher step: enable `allowJetFlight` on `AsterGT` and enter Play again to see the jet arc. Leave the saved teaching default off unless the class has accepted that motion.
8. For Blender, open a copy of `SourceArt/Blender/AsterGT.blend`. Do not save over the teacher file.

Expected first Play result with the saved scene: the route holds at the gap because `allowJetFlight` is false.
