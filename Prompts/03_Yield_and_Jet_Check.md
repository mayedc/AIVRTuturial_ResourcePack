# Legacy exercise entry — gap flight

**Not a standalone early-stage task.** The student implements flight in [Prompt 1.4](01_4_Speed_And_Gap_Flight.md), after the 1.3 desktop starter **full Play** observation and speed control implementation.

The flight acceptance contract is: `BeginJetFlight` only when playing, unpaused and holding at the gap; a student click starts a smooth arc from z=32 to 48 m over ~10 s, up to 3 m high; use existing jets during flight only, land with jets off, stop at z=58 m and preserve crossing, pause/restart and eye anchor.

**STOP.** Do not independently edit the original teacher `WorkshopDrive.cs` or automatically run Prompt 1.4.
