# Lesson 1 — Cursor, Agent and MCP setup (45 minutes)

## 00–20 | Agent and local workspace

Explain CLI vs MCP, read/write permissions and verification. Students **create an empty local folder and open it in Cursor before any repository download**. Run [clone/preflight prompt](../Prompts/00_Clone_Preflight.md); Cursor clones the repository and reads README and the preflight checklist. Confirm installed compatible Cursor, Blender, Unity Hub/Editor, Quest Link app, required class Pro access and local write permission. The GitHub repository deliberately does **not** supply a workshop Unity scene; students create a separate blank URP project.

## 20–45 | Connect two empty applications

Students open an **empty Blender scene** and a **new blank URP Unity project**, then paste [MCP setup prompt](../Prompts/00_Install_Update_MCP.md). Cursor inspects whether Blender/Unity MCP components exist, installs missing or updates outdated compatible versions through upstream package tools; the student enables and starts the in-app services. Cursor then performs **actual read-only MCP calls** to both apps.

Record CP0: Blender version and object count, Unity project path/editor version/scene/Console errors, both MCP versions and live tool readbacks. On failure, diagnose, repair and retry. An installation or a green status icon alone is not a pass. Do not alter teacher Blender sources; generated Unity scenes must be built only in the student's separate project after 1.2 visual approval. See [end-to-end workflow](Cursor_First_Workflow.md).
