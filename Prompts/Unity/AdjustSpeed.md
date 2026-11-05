# Speed implementation specification — subtask of Prompt 1.4

**Only invoke after a verified full Unity Play checkpoint in [Prompt 1.3](../01_3_Export_And_Build_Unity.md).** The controlling prompt is [Prompt 1.4](../01_4_Speed_And_Gap_Flight.md); do not run this in isolation or work on the teacher project.

Via Unity MCP inspect the student `Workshop_Desktop_Student` scene and the **student project copy** of `WorkshopSpeedControl.cs`. Implement `SetSpeedMps(float)` with initial target 0.85 m/s and finite-target clamp to 0.25–2.0 m/s; non-finite input retains the previous valid target. Enable `CanAdjustSpeed` for the existing desktop slider and preserve the drive/braking/yield, single mover and references.

Compile and read the Console. The student then manually plays to compare 0.85 with their chosen target (default 1.20 m/s) and confirms yielding and pre-gap hold. Report **OBSERVED / NOT TESTED** faithfully. Continue to commanded flight within 1.4 only after the speed subtask passes.
