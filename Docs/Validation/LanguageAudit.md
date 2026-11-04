# Language audit

Date: 2026-11-04.

## Result

PASS for publication content.

`Tools/ValidateRepository.ps1` found no non-ASCII filenames and no CJK Unified Ideographs in scanned project-owned text, Unity YAML, prompts, skills, or ASCII strings extracted from `.blend` and `.fbx` files.

Comments, docs, menu labels, and the desktop IMGUI panel are English. The panel title is `ASTER / AI VR DRIVING WORKSHOP`.

`Docs/03_Unity_Integration.md` uses the unit `m/s²`. That character is U+00B2, not Chinese. It was not flagged.

Generated `*.csproj` and `*.slnx` files are local and gitignored. They are not part of the published language set.

Third-party packages resolved under `Library/PackageCache` were not rewritten and are not part of the git publication set.
