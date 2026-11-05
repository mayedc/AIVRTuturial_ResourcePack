# AI Era: VR Development with AI Agent, Blender, and Unity

A three-lesson MDIT 310 workshop: Cursor first, live Blender/Unity MCP, vehicle recolor, Unity scene integration, desktop behavior, and optional wired Quest Link.

## Start here — Cursor-first sequence

**Do not download a GitHub ZIP or open the workshop Unity project as your first action.**

1. Create an **empty folder** on your PC, open that folder in **Cursor**, and clone the repository **into the open folder** using its terminal:

   ```powershell
   git clone https://github.com/mayedc/AIVRTuturial_ResourcePack.git .
   ```

2. Ask Cursor to read [the complete student workflow](Docs/Cursor_First_Workflow.md) and execute [Prompt 00A](Prompts/00A_Clone_and_Preflight.md). It checks Cursor/Blender/Unity/Meta Horizon Link compatibility, Git, versions, student file permissions, account sign-in, any course-selected Cursor Pro entitlement or quota, Unity license, and network access. A newer **validated-compatible** release is allowed; listed versions are baselines, not absolute ceilings.
3. Start **an empty Blender scene and a separate temporary blank Unity project**. Ask Cursor to execute [Prompt 00B](Prompts/00B_MCP_Setup_and_Recovery.md): inspect existing MCP connectors, install or update [Blender MCP](https://github.com/ahujasid/mcp-for-blender) and [Unity MCP](https://github.com/CoplayDev/unity-mcp) through their **supported** installer/package manager, help start each application-side MCP service, and verify both using actual live tool calls. If a connection fails, diagnose and retry.
4. Follow [Lesson 2's Blender lab](Docs/Lesson01_Blender.md): use Blender MCP to append the prepared Aster GT, recolor only `M_BodyPaint`, save a **student copy**, and export the vehicle as FBX. **Only after the recolor** open the cloned workshop project through Unity Hub.
5. Reverify Unity MCP **in the cloned project**, then use [Prompt 01A](Prompts/01A_Unity_Automation.md) to import the edited FBX, construct the student visual in a **copy** of the desktop scene and run the validator/Play test. If MCP/Editor scripting cannot finish a step, use the teacher's [Unity export-package fallback](Prompts/01B_ExportPackage_Fallback.md) and import it manually in class.
6. Implement [speed and flight exercises](Docs/Lesson03_MetaQuest.md). Optionally use the compatible Meta XR SDK and wired Quest Link for the seated cockpit test. Never treat a prior report as a current hardware pass.

**For students:** [Full workflow](Docs/Cursor_First_Workflow.md) · [checklist](Docs/StudentChecklist.md) · [troubleshooting](Docs/Troubleshooting.md)

**For instructors:** [Three-lesson guide](Docs/TeacherGuide.md) · [acceptance matrix](Docs/Acceptance_Matrix.md) · [historical release validation](Docs/Validation/FinalReleaseReport.md)

## What's in this pack

- `SourceArt/Blender` and `SourceArt/FBX`: prepared car, robot, city, jet and road assets.
- `Assets/AI_VR_Workshop_V4`: **legacy physical folder** containing prepared Unity meshes, materials, prefabs, scripts and scenes. In this documentation-only transition, paths and assembly identities remain unchanged to protect GUIDs and serialized scene references; see [version-suffix migration procedure](Docs/Version_Suffix_Migration.md).
- `Prompts`: four new Cursor-first prompts plus existing exercise prompts.
- `.cursor/skills`: Blender edit, Unity lesson and quality-check instructions.
- `Answers`: instructor reference code, not student starting code.

## Compatibility and evidence

The provided project records Unity 6.3.27f2, URP 17.3 and Blender-created assets from Blender 5.2.2 LTS. Use these or newer **versions proven compatible on the target machine**; read [compatibility](Docs/Compatibility.md). The existing Unity MCP dependency is pinned to a historical commit, **not guaranteed latest**. Meta XR Core is external and the archived Meta scene contains an unresolved rig reference. A current Quest pass requires actual headset testing.

Original course models and code: MIT [LICENSE](LICENSE). See [asset credits](Docs/AssetLicenses.md) for third-party boundaries.
