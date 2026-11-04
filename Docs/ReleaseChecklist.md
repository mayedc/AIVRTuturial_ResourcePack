# Release checklist

Updated through documentation. Git publication fields are filled when the repository is pushed.

| Check | Status |
|---|---|
| Unity version | 6000.3.27f2 |
| Required dependencies | URP 17.3.0, Input System 1.20.1, OpenXR 1.16.1, XR Management 4.7.0, test framework 1.6.0, unity-mcp git lock recorded in `Packages/packages-lock.json` |
| Desktop test | PASS. See `Docs/Validation/SceneTestResults.md`. |
| Meta Quest hardware | NOT VERIFIED |
| Documentation | Lesson, teacher, and ToSlide files added in English |
| Privacy | PASS. `Tools/ValidateRepository.ps1` failures 0 on the pre-git scan. Local `Library`, `Temp`, `Logs`, `UserSettings`, and generated project files are warnings and gitignored. |
| License | PASS for files in this folder. Meta prefab excluded. See `Docs/AssetLicenses.md`. |
| File count | Validator PASS: 464 scanned files outside forbidden directories. |
| Repository size | 106,673,238 bytes outside `Library`, `Temp`, `Obj`, `Logs`, `UserSettings`, `Build`, `Builds`, and `.vs`. No file at or above 50 MB in that set. |
| Git LFS | Not used. No binary reached the 50 MB warning or the 100 MB GitHub limit. |
| Remote | Pushed to `https://github.com/mayedc/AIVRTuturial_ResourcePack` on `main`. Verified clone SHA `0f92c6c672e94f56d72681e982f0851b129b339d`. |
