# Cursor prompt · Unity export-package fallback

Use only if the Blender→Unity scene integration or script attachment cannot be completed reliably through Unity MCP or a minimal reviewed Unity Editor script.

**Instructor preparation (inside a verified Unity project):** Save a clean new scene checkpoint, include the FBX/materials/scripts and their exact dependencies, inspect duplicate GUID/name issues, run Compile + scene validation + desktop Play. In Unity use **Assets → Export Package…**, tick **Include dependencies**, export a named `Workshop_Student_Fallback.unitypackage` to the instructor's distribution location. Do not claim this package exists until it has been exported and checked.

**Student classroom step:** Keep a copy of current project and student assets. In Unity choose **Assets → Import Package → Custom Package…**, select the instructor-supplied `.unitypackage`, review the file list and conflict paths before importing. Do not overwrite newer work without review. Open the imported **new scene copy**, recheck scripts, model, color, references and Console; perform desktop Play acceptance. Never substitute an untrusted download or a renamed ZIP for a Unity export package.

Tell the student exactly what to click in Unity when a manual UI step is required. Report missing package, import failures and untested behaviors rather than a fake success.
