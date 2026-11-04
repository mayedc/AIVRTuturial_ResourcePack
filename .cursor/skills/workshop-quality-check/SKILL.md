---
name: workshop-quality-check
description: Check model files, scene references, versions, and per-platform acceptance, and write an honest checkpoint.
---

Read [the acceptance matrix](../../../Docs/Acceptance_Matrix.md). Run only the checks this machine can run. Do not copy an older report forward as a pass.

- Blender: open the `.blend`, check separate parts and materials, play robot frames 1-31, and compare bounds and foot contact after an FBX round trip.
- Unity: check meshes, materials, scripts, and references. Compile, enter Play Mode, and check fixed speed, yield, gap hold, pause, and restart. After the coding exercises, test the bounded speed and commanded flight.
- Quest: check both eyes, seated height, head tracking and seated view. For an optional moving demo, record performance and discomfort separately. Record the jet separately.
- Screenshots come from the delivered model or the running scene. Record the software version, file path, action, and result. A concept drawing or a Blender render does not replace Unity or Quest evidence.

States are only: passed on this machine, failed on this machine, not run, or needs a visual decision. Checkpoints are new files. Keep the teacher originals and finished student work.
