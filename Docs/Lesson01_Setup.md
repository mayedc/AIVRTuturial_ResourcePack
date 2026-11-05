# Lesson 1 — Cursor-first Agent and MCP setup (45 minutes)

## 00–15 | GitHub through Cursor + software preflight

1. Student creates a **new empty** Windows folder and opens it in **Cursor** before touching Unity. In its terminal use `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .`. Do not use GitHub Download ZIP, and do not open the workshop project in Unity Hub yet.
2. Run [Prompt 00A](../Prompts/00A_Clone_and_Preflight.md). Cursor reads the README and records software versions, compatibility, Git availability, write permissions, workspace trust, local MCP permissions, licenses, accounts and any required Cursor Pro quota.
3. Discuss terminal Git, Agent permissions and MCP as distinct capabilities. Show why a JSON setting or a running port is not proof that Cursor can manipulate an application.

## 15–45 | Empty applications → MCP install/update → real verification

1. Open a blank **Blender** scene. Create/open a **separate empty 3D/URP Unity sandbox** in Unity Hub, not the cloned workshop project.
2. Run [Prompt 00B](../Prompts/00B_MCP_Setup_and_Recovery.md). Cursor inventories current Blender and Unity MCP, installs missing ones, updates an older connector to a **compatible stable version** using upstream install methods, and protects existing config/lock files.
3. In Blender, enable/start the MCP add-on's local service if needed. In Unity, open **Window → MCP for Unity**, start/check the service and configure Cursor. Restart Cursor when required.
4. Cursor must **actually query** Blender and Unity through MCP, returning versions, scene/project paths, counts and Unity Console errors. If the query fails, troubleshoot and retry; mark outstanding failures instead of reporting success.

**Lesson 1 checkpoint CP0:** cloned repository URL/path, installed software/permissions, current MCP versions, and two independent live connection statuses. [Full procedure](Cursor_First_Workflow.md). In Lesson 2, color the vehicle **before** opening the workshop Unity project.
