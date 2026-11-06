# Source-first release checklist — must be rerun after this source-first revision

1. [ ] Clone the candidate revision into a **new empty Cursor folder**. No old student files, source-built scenes, Unity package cache or teacher previous-generation asset pack are imported.
2. [ ] Run python Tools/Validation/validate_source_first.py. Fix required files, JSON schema and relative Markdown links.
3. [ ] Open eight original Blender .blend files; verify the student color copy and export FBX using live Blender MCP.
4. [ ] Open a **new blank URP Unity project outside this Git repository**, connect Unity MCP and copy only the four required FBXs, Starter scripts, Editor scripts and config.
5. [ ] Compile **all** new UnitySource C# in the real Editor with zero blocking errors; create one student scene via the actual builder and validate hierarchy/camera/material/bones and the open 6m road gap.
6. [ ] Manually Play 1.3 fixed-speed route to completion of the gap hold and pause/restart; record real observations (including visible robot animation).
7. [ ] Modify student scripts in 1.4; Play the bounded speed and explicit 10s jet arc, landing z=48, final stop z=58, pause/restart.
8. [ ] Execute 02_1 XR/Meta package and Link self-check, then 02_2 on a **new VR scene copy**. Student **wears Quest** to observe stereo, seated driver position and head tracking.
9. [ ] Rerun builder on existing scene and verify that it **does not duplicate or overwrite** student assets. Check Git status for untracked student work.
10. [ ] Record OS, hardware, Unity/Blender/MCP/package versions, exact scene/FBX paths, PASS/FAIL/NOT TESTED and any manually approved calibration. Merge PR only after review.

**Current status:** source-first branch contains static source and checks, but current branch **has not been compiled/Played in a physical Unity/Quest session**. Historical Docs/Validation evidence belongs to older revisions.
