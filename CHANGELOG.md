# Changelog

## Unreleased — Source-first Unity rebuild (Plan B, review PR)

- Separated the GitHub **source bundle** from student-created blank URP Unity projects: removed old root Assets/Packages/ProjectSettings and obsolete premade-scene installation tools **in this review branch only**.
- Introduced UnitySource scene spec, four Starter scripts, two Editor scene-building/structure-check scripts and teacher Reference implementations under AIVRWorkshop.Student.
- Updated 1.3 to export the chosen car FBX and build a new student scene from four FBXs without teacher .unity, prefab or .unitypackage. Preserved independent 1.1/1.2 and 1.4 student checkpoints.
- Updated 02_1/02_2 to operate on the **student-generated** scene, with separate VR copy and physical headset gate.
- Reworked README, setup, workflow, safety rules, validation entry points, ignored student outputs, XR docs and historical report labeling. Added a source-only Python static validator and GitHub Actions.
- **Release gate still open:** new builder not yet compiled/tested on a fresh Unity URP project; no source-first Play or Quest device retest in this GitHub review. Do not merge on static checks alone.

## 1.0.0 — 2026-11-04 (historical release)

The original release contained prebuilt Assets/AI_VR_Workshop_V4 scenes and V4 runtime code, plus Blender/FBX assets. Its archived Windows Unity tests and known missing Meta prefab GUID belong to that release only; see [historical validation](Docs/Validation/FinalReleaseReport.md).

The current Plan B source-only branch does not ship these old Unity scenes. They remain recoverable via Git history.
