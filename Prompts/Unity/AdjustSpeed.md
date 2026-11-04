# Adjust prepared speed

Objective: change the existing speed component and keep the crosswalk yield.

Paths:

- Scene: `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity`
- Component: `WorkshopSpeedControl` on `AsterGT`
- Drive: `WorkshopDrive` on the same object
- Panel: `WorkshopDesktopPanel` on `AI_VR_Workshop_V4`

Rules:

- If you must save, duplicate the scene first with `Workshop V4/Save active scene as new checkpoint`.
- Do not delete the teacher scene.
- Do not add a second `WorkshopDrive`.
- Do not change route distances.
- Leave `allowJetFlight` false unless the teacher asks for the jet.

Success:

- The target stays inside 0.25 to 2 metres per second.
- Play Mode still reaches `Yield` near 7.5 m and `AwaitChoice` near 32 m.
- The Console has no new compile errors.
