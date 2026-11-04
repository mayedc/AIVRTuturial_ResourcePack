---
name: workshop-blender-edit
description: Import the prepared car through Blender MCP, recolor one material, and save a student copy.
---

Read [the asset catalog](../../../Docs/02_Asset_Catalog_and_Reuse.md) for axes and file boundaries. The task uses models that already exist.

1. With the MCP tools that are actually available, read the current file path, the object list, and `M_BodyPaint`. Record the call. If a tool is missing, report the connection problem. Terminal output is not an MCP success.
2. If the current file is a teacher original, save a copy under `StudentWork/<student-id>/` first. If that name exists, add a numeric suffix.
3. Make only the visible change the user asked for. Recoloring may use `Tools/blender_safe_recolor.py`. Do not run the teacher art generators.
4. Compare the same camera before and after. Object count, bounds, wheels, skeleton, and the eye point stay put. Only the target material changes.
5. Save a new `.blend`. For a Unity round trip, export `VehicleRoot` and its children to a new FBX. Report the paths, the material name, and the screenshot files.

The native Unity meshes and the FBX are separate imports. Editing an FBX does not update the native meshes. Follow the catalog and replace only the art child. Keep the drive root, the eye point, and the serialized references.
