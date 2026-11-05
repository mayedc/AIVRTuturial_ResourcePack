# Cursor prompt — clone and check prerequisites

You are the classroom setup Agent. The user has **created and opened an empty local folder in Cursor**. Do not tell them to download a ZIP.

## Clone and workspace gates

1. Check the current folder, Git availability and write permission. If the folder is empty, run `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .` in Cursor's terminal. If the folder already contains this repository (remote/README present), do **not** re-clone; continue with verification. If the folder is non-empty for another reason, do not erase or overwrite contents: report the conflict and choose an empty child folder with the user's knowledge.
2. Verify `git remote -v`, branch, `README.md`, `Docs/Cursor_First_Workflow.md` and the `.cursor/skills` folder. Reload the workspace if needed. Never overwrite existing student work.
3. Read the README, `Docs/Cursor_First_Workflow.md`, `ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json` and the XR checklist. Note that Unity **6.3.27f2 / 6000.3.27f2** and Blender **5.2.2** are pack baselines; newer releases may be accepted after opening/import checks. Compare **compatible minimums and tested versions**, not one compulsory exact build.
4. Verify that Cursor is signed in, whether **Cursor Pro classroom access** is required and active, workspace edits/terminal execution are permitted, and student output paths are writable. Do not request secrets, log into paid accounts, or claim subscriptions exist from filenames.
5. Present a concise checklist with **installed / missing / update recommended / not verifiable / PATH NOT FOUND** and exact next actions. Explicitly say: open an empty Blender scene and a temporary **blank URP Unity project**, not the supplied finished workshop scene, before the MCP setup stage.
6. Stop before any destructive change. Do not edit teacher .blend files, original scenes, or Unity project settings.

## Fast software preflight — path-first detection

Optimize the software compatibility check for speed and accuracy. This stage is **quick executable-path and version detection only**. Distinguish it from later live MCP verification.

### Discovery rules

1. **Never perform recursive filesystem searches** to discover installed software. Do not scan entire drives, user directories, Unity project caches, or Program Files recursively.
2. Use this discovery priority:
   1. User-provided executable paths.
   2. Previously validated local path configuration (see cache below).
   3. Windows registry and PATH.
   4. Known installation directories (**non-recursive**; list only the immediate children of known roots).
   5. Ask the student to locate the executable if unresolved.
3. Check **Cursor**, **Blender**, **Unity Editor**, **Unity Hub**, **Meta Quest Link**, **Git**, **Python**, and **uv/uvx**. Use parallel, read-only checks where independent. Also report Windows build, free disk space on the workspace drive, and GPU driver when available from WMI/registry without launching apps.
4. When executable paths are available, use PowerShell `Test-Path` and executable version metadata first (`VersionInfo`, `FileVersion`, product version, or a lightweight CLI such as `git --version` / `uv --version`). **Avoid launching Unity Editor, Blender, or other heavyweight applications solely to identify their versions.**
5. For Unity installations, inspect only the **immediate subdirectories** of the Unity Hub Editor install root (for example Hub `secondaryInstallPath` / Editor folder). Select a compatible installed Editor. Do **not** scan all Unity projects.
6. Cache validated application paths in the local, Git-ignored file `.cursor/local-app-paths.json` (see `.cursor/local-app-paths.example.json`). On subsequent runs, reuse paths after `Test-Path` confirms they still exist; rewrite the cache only with verified paths. Never commit this file.
7. Compare detected versions against the project's minimum compatible baselines. Newer versions may be accepted after appropriate compatibility verification (open/import/live-tool checks in later stages).
8. If an executable cannot be found after the priority list above, report **`PATH NOT FOUND`**. Do not silently initiate an exhaustive search.
9. Return a compact table containing: application name, detected version, executable path, compatibility status, and required action.
10. Do **not** launch applications during preflight unless necessary for a lightweight CLI version. Perform actual MCP verification in the subsequent connection stage (`Prompts/00_Install_Update_MCP.md`) after the student opens an empty Blender scene and a blank URP Unity project.

### Local path cache format

Write or update `.cursor/local-app-paths.json` only after validating paths on **this machine**. Keep values machine-local and never put a student's real paths into this prompt or the committed example. The shipped template starts with empty strings; discovery fills them locally.

```json
{
  "updated": "",
  "apps": {
    "cursor": "",
    "blender": "",
    "unityHub": "",
    "unityEditor": "",
    "questLink": "",
    "git": "",
    "python": "",
    "uv": "",
    "uvx": ""
  }
}
```

### Compatibility status labels

Use one of: `compatible`, `update recommended`, `missing`, `PATH NOT FOUND`, `not verifiable`. For Cursor Pro classroom entitlement, report account evidence without claiming classroom seat assignment from filenames alone.
