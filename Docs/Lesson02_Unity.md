# Lesson 02 — Unity speed and the crosswalk

## Objectives

- Inspect `Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity` through Cursor and Unity MCP, or in the Editor if MCP is down.
- Change `WorkshopSpeedControl` on `AsterGT`.
- Show that the car still stops at the crosswalk and still reaches the gap.

## Prerequisites

Lesson 1 concept: students edit prepared content. Unity `6000.3.27f2` has compiled this project with zero errors.

## Duration

90 minutes.

## Required software

Unity `6000.3.27f2`, this project, Cursor. Unity MCP is optional if the Editor is available.

## Steps

1. Open the desktop scene. Confirm `WorkshopDrive` and `WorkshopSpeedControl` are on `AsterGT`, and `WorkshopDesktopPanel` is on `AI_VR_Workshop_V4`.
2. Read `targetSpeedMps`. The saved value is 0.85. The component clamps to 0.25–2.
3. Duplicate the scene to a student checkpoint if the class must keep the teacher scene byte-stable. Menu `Workshop V4/Save active scene as new checkpoint` writes a new scene under `Assets/AI_VR_Workshop_V4/Scenes/`. Do not delete `Workshop_Desktop.unity`.
4. Set a new target, for example 1.6, on the student copy or as a temporary Play Mode change.
5. Enter Play. The panel slider calls `SetSpeedMps`.
6. Confirm the yield: stage `Yield` near z = 7.5 m while the robot crosses, then `ApproachGap`, then `AwaitChoice` near z = 32 m.
7. Do not enable `allowJetFlight` unless the teacher asks for the jet demonstration.

## Copyable prompt

Use `Prompts/Unity/AdjustSpeed.md`.

## Expected results

A higher target produces a higher cruise than 0.85 m/s and the crosswalk stop still happens. The release test observed 1.31 m/s after `SetSpeedMps(1.6)` on the original scene in Play Mode, then restarted. That test did not save the scene.

## Validation checklist

- Console has no compile errors.
- `Workshop V4/Validate active workshop scene` reports no missing mesh, material, or drive reference.
- Play Mode shows `Yield` before the car passes the crossing.
- Pause and Restart on the panel return the car to the start.

## Troubleshooting

If the car never leaves `Ready`, Play Mode is not ticking. If it never leaves `AwaitChoice`, jet flight is still off. That is the saved default.

## Deliverable

The speed value used, the observed crosswalk stop, and whether the teacher scene was left unsaved.
