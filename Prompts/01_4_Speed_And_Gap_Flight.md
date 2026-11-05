# Prompt 1.4 — Editable speed and manual flight over the road gap

**Gate:** run only when the student has personally completed and confirmed the **entire 1.3 Unity Play** (0.85 m/s cruise, crossing yield, robot, z=32 m gap hold, pause and restart). If it was only sampled at 8 seconds or any item is untested, **STOP and return to 1.3**. Reply in Simplified Chinese.

**学生希望测试的速度（留空为 1.20 m/s）：** ________

Keep the original teacher scene and original repository scripts unchanged. Work only in the verified student Unity project's `Workshop_Desktop_Student.unity` and its student-owned code copy, backed up first. Read `AGENTS.md`, `Docs/03_Unity_Integration.md`, `Prompts/Unity/AdjustSpeed.md` and the original/runtime code, using `Answers/Original` for comparison; do not blindly paste ready-made `Answers/Reference`. Verify active Unity project and Console through Unity MCP.

**1.4A — Speed control**
1. Edit the student copy of `Assets/AI_VR_Workshop_V4/Runtime/WorkshopSpeedControl.cs` only after checking whether the reference pack is copied outside the teacher source. Implement `SetSpeedMps(float)` with `CanAdjustSpeed` enabled and existing UI slider wired. Default cruise target **0.85 m/s**; clamp finite targets to **0.25–2.0 m/s**, reject NaN/infinity without changing last valid target. Retain acceleration, braking, yield, gap hold and pause/restart behavior.
2. Compile and check Console. Let student Play to compare **0.85** with the requested target (default **1.20 m/s**) and confirm that pedestrian yield and gap hold still work. Report only actually observed results.

**1.4B — Commanded jet flight**
3. In the **student** copy of `Assets/AI_VR_Workshop_V4/Runtime/WorkshopDrive.cs`, enable `CanFly` only when safe to display the button. Make `BeginJetFlight` work only while Play is running, unpaused and car is **waiting at the gap**. An approach to the gap must **not** auto-launch.
4. After a student button click, animate a smooth arc **z=32 → 48 m**, ~**3 m** maximum height, ~**10 s** duration, jets on only while flying, jets off on landing, then continue until stop at **z=58 m**. Keep the existing robot, eye anchor, pause/restart and controls. Do not bridge the physical gap with a collider or introduce a second mover.
5. Compile, check runtime scripts and Console with Unity MCP. Student manually Play-checks: speed slider and clamping, stop/yield preserved, stable gap hold without command, commanded flight over the gap, landing and jets off, endpoint, Pause/Restart. Report as **OBSERVED PASS / FAIL / NOT TESTED**.

**STOP.** Only report “Desktop Blender → Unity lesson complete” after BOTH interactive exercises and regressions have been actually checked. Do not proceed to the separate VR/Quest prompt in this run.
