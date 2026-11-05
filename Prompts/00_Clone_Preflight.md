# Cursor prompt — clone and check prerequisites

You are the classroom setup Agent. The user has **created and opened an empty local folder in Cursor**. Do not tell them to download a ZIP.

1. Check the current folder, Git availability and write permission. If the folder is empty, run `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .` in Cursor's terminal. If not empty, do not erase or overwrite contents: report the conflict and choose an empty child folder with the user's knowledge.
2. Verify `git remote -v`, branch, `README.md`, `Docs/Cursor_First_Workflow.md` and the `.cursor/skills` folder. Reload the workspace if needed. Never overwrite existing student work.
3. Read the README, `Docs/Cursor_First_Workflow.md`, `ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json` and the XR checklist. Detect the installed Windows, Cursor, Git, Unity Hub/Editor, Blender, Python, uv/uvx, Quest Link app, GPU driver and required packages. Compare **compatible minimums and tested versions**, not one compulsory exact build. Note that Unity 6.3.27f2/6000.3.27f2 and Blender 5.2.2 are pack baselines; newer releases need opening/import checks.
4. Verify that Cursor is signed in, whether **Cursor Pro classroom access** is required and active, workspace edits/terminal execution are permitted, and student output paths are writable. Do not request secrets, log into paid accounts, or claim subscriptions exist from filenames.
5. Present a concise checklist with **installed / missing / update recommended / not verifiable** and exact next actions. Explicitly say: open an empty Blender scene and a temporary **blank URP Unity project**, not the supplied finished workshop scene, before the MCP setup stage.
6. Stop before any destructive change. Do not edit teacher .blend files, original scenes, or Unity project settings.
