# Privacy audit

Date: 2026-11-04. Scope: the release candidate tree. Generated Unity caches were not treated as publication content.

## Method

`Tools/ValidateRepository.ps1` walks the tree, skips `Library`, `Temp`, `Obj`, `Logs`, `UserSettings`, `Build`, `Builds`, and `.vs`, and scans the remaining text plus ASCII strings inside `.blend` and `.fbx` files. It reports categories and repository-relative paths. It does not print secret values.

A separate string search looked for machine-specific directory markers, a known archive folder name, and token prefixes. Matches were classified before any report text was written.

## Result

Validator status: PASS. Failures: 0. Scanned files: 464. Bytes outside forbidden directories: 106,673,238 before the final checklist edit.

| Check | Result |
|---|---|
| Personal absolute paths in publication text | None. |
| Email addresses | None. Two `@` hits in teacher Python were Blender attribute expressions, not mailboxes. |
| Credentials | None. `ProjectSettings/ProjectSettings.asset` contains an empty `metroCertificatePassword` field. The value is blank. |
| Device serials, crash dumps, tokens | None found in the scanned set. |
| Archive folder inside the release tree | Absent. `.gitignore` excludes that sibling archive name. |
| User paths inside Blender and FBX ASCII strings | None. FBX creator text identifies Blender (stable FBX IO) 5.2.2 LTS and does not include a user directory. |
| Generated project files | `AIVRTutorial_ResourcePack.slnx`, `AIVRWorkshop.V4.Editor.csproj`, and `AIVRWorkshop.V4.Runtime.csproj` exist locally and contain machine paths. They match `.gitignore` (`*.csproj`, `*.sln`, `*.slnx`) and are warnings, not publication files. Their path values are not copied here. |
| Local cache directories | `Library`, `Temp`, `Logs`, and `UserSettings` exist on this machine and are gitignored. |

## Publication rule

Do not force-add generated project files or cache directories. The public tree must stay limited to the scanned content that passed this audit.
