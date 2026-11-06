# Validation entry points — source-first the current teaching package

**Current release candidate:** GitHub source files and new UnitySource C# builder; **no distributed Unity scene**.

| Check | Source | What it proves |
|---|---|---|
| Repository static test | Run python Tools/Validation/validate_source_first.py from repository root | Required Blender/FBX files, staged prompts, scene spec, markdown links, source code presence |
| Live MCP | Prompts 00_Clone_Preflight and 00_Install_Update_MCP | Real Blender/Unity application connections |
| Scene build | Prompt 1.3 + UnitySource Editor builder/validator in student's blank URP project | One generated scene and script references; **not** proof of full Play |
| Student desktop | Full Play after 1.3 and again after 1.4 | Yield/robot/gap hold, speed, explicit flight, pause/restart |
| Student XR | 02_1 and 02_2 | Live Quest Link, correct driver-seat stereo/head tracking |

The old [2026-11-04 tests](Validation/FinalReleaseReport.md), including original Unity scene hashes and prior build/runtime observations, are historical results for a different repository layout. **Do not use them to claim the current source-first Unity builder, VR rig, or clean-clone test passed.**

New the current teaching package release is blocked until a fresh clone, blank-project Unity compile, scene construction, full Play and physical headset test are recorded. See [Release Checklist](ReleaseChecklist.md).
