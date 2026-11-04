# Student starter checks

| Check | Result or next action |
|---|---|
| Base and dependencies | Project declares Unity 6000.3.27f2. Unity MCP manifest and lock use the same Git commit. |
| Static consistency | Run `python Tools/validate_kit.py` with PyYAML. Check the scene, material, mesh and document results. |
| Blender on macOS | Blender 5.2.2 LTS reopened all eight blend files and imported the seven source FBXs. The student-car test appended the collection, changed M_BodyPaint, reopened the saved copy and reimported the export. |
| Unity on macOS | In Unity 6000.3.28f1 batch Play Mode, the starter held at 32 m with a 0.85 m/s cruise. The reference reached 58 m at rest after a commanded flight, with a 1.20 m/s ground cruise and a 3.00 m peak. The recolored FBX imported with bounds about 2.41 × 1.61 × 5.14 m. |
| Unity test scope | The editor updated the Collab Proxy package on the temporary macOS copy and logged an unrelated Unity Search indexing exception. Route assertions ran in batch mode. Inspect the rendered scene and confirm the intended Windows editor separately. |
| Windows and live MCP | Verify Unity import and Play, Blender-to-Unity visual replacement, and both live Cursor readbacks on classroom PCs. |
| Quest 3 / 3S | Verify wired Link, the tested external SDK, eye-level tracking and both-eye seated view on the actual classroom equipment. |
| History | [v1.0.0 evidence](Validation/FinalReleaseReport.md) applies to the earlier release. See [Answers](../Answers/README.md) for the archived code. |
