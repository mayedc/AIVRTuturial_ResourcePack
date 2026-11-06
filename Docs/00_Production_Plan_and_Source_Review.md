# Historical production plan and source review (historical)

> Archived narrative for the earlier 2026 release. The **current** student workflow is [source-first](Cursor_First_Workflow.md), creating a scene from FBXs in a separate blank URP Unity project; the time allocations, original scene and teacher assembly statements below are historical.

The workshop has three 90-minute lessons. Students import, recolor, adjust speed, and experience a prepared route. Teachers own modeling, animation, scene assembly, and device setup.

## Sources that were reviewed

- An earlier starter kit contained a simple car OBJ, an older drive script, scene builders, and lesson notes. It had no Blender or FBX teaching models. Its Unity label was 6000.3.0f1. That label is not proof that this package was tested on that editor.
- Seven reference images were used only to judge shape and failed results. They are not in this package and were not converted into textures.
- The car, robot, city, roads, and jet geometry in `SourceArt` were generated for this course. This package does not include a downloaded commercial model or a Mixamo clip.

## How the teaching module was built

1. Aster GT is an original two-seat wedge. Body, glass, lamps, wheels, seats, instruments, trim, and jet nozzles are separate surfaces.
2. Noma is an original armored figure with a skeleton and an in-place walk. The route script moves the figure across the street.
3. Meridian is a straight street with shopfronts, a crosswalk, and a real gap in the road deck.
4. Blender files were saved and exported to FBX. Unity then uses native mesh assets in `Assets/AI_VR_Workshop_V4`, not a live link back to Blender.
5. Runtime behavior is `WorkshopDrive`, `WorkshopSpeedControl`, `WorkshopRobotWalk`, and `WorkshopDesktopPanel`.

## Delivery boundary

The art is stylized teaching geometry. It is not a brand-vehicle replica, a scan, or a promise of commercial-game image quality. Static checks, editor checks, and headset checks are separate. An item that was not run stays unchecked.

Jet flight is off by default. A teacher enables it only after a comfort review.
