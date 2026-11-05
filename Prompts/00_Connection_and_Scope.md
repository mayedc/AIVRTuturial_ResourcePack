# Prompt 00 — verify live connections and project scope

Read [workflow](../Docs/Cursor_First_Workflow.md) and [MCP setup](00_Install_Update_MCP.md). Discover the Blender and Unity MCP tools that are actually available in Cursor. Do not create geometry, edit the teacher project, or infer that terminal access equals MCP connectivity.

The expected **CP0** setup is an empty Blender scene and a blank Unity URP project. Through real **read-only MCP tool calls**, return Blender application version, current file or unsaved state, object count and whether `VehicleRoot` is present; return Unity project path, editor version, active scene and Console error count. A blank scene may legitimately have no `VehicleRoot`.

If a connection is absent, identify missing add-on/server/UPM package, Cursor configuration, service, transport, permissions or wrong Unity instance. Apply safe reversible fixes from [MCP setup prompt](00_Install_Update_MCP.md) and retry live reads. Preserve user config and student files. Report CONNECTED/FAILED/NOT TESTED with actual evidence. Once the Blender work is saved and the workshop Unity scene is later assembled, recheck the Unity MCP target and full scene references.
