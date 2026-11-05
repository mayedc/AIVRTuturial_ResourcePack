# Quick start — Cursor before Unity

1. Create an **empty folder**, open it in Cursor, then run `git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .` in Cursor's terminal (only when that folder is empty). Verify the Git remote.
2. Use [Prompt 00A](../Prompts/00A_Clone_and_Preflight.md) to read the repo and inspect software, compatible minimums, permissions and any required Cursor Pro quota.
3. Start **empty Blender** and a **separate blank Unity sandbox**; use [Prompt 00B](../Prompts/00B_MCP_Setup_and_Recovery.md) to inspect/install or upgrade each MCP, start application-side servers and verify actual tool readback. Retry failed connections before edits.
4. Use Blender MCP to load a **student copy** of the Aster GT and change `M_BodyPaint`; export a new FBX.
5. **Only now** open the cloned repository root as the workshop Unity project in Unity Hub. Recheck the package, start Unity MCP for this project and run [Prompt 01A](../Prompts/01A_Unity_Automation.md) to import FBX and build a **copy** of the prepared desktop scene. If automation cannot finish, use the teacher [export-package fallback](../Prompts/01B_ExportPackage_Fallback.md).
6. Validate and Play the desktop scene, then proceed to the speed/flight and optional wired Quest Link exercises.

Read the [full workflow](Cursor_First_Workflow.md) for exact checks, compatible versions and recovery. The archived physical asset path `Assets/AI_VR_Workshop_V4` is retained pending a verified Unity migration; don't rename it manually.
