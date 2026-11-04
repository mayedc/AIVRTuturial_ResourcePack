# Exercise 2A — Implement speed control

Through Unity MCP, confirm the open scene is our copy of Workshop_Desktop. Read the Console and inspect AsterGT. Edit the existing WorkshopSpeedControl.cs. Implement a target initially at 0.85 m/s, clamp finite inputs to 0.25–2.0 m/s, and keep the last valid target if the input is NaN or infinity. Make CanAdjustSpeed true so the existing desktop slider can call SetSpeedMps. Keep the drive, braking and references. Work from the starter code and these requirements.

Compile and report the Console result. In Play, compare observed cruise at 0.85 and 1.20 m/s. Verify that the car still yields to the robot and holds before the gap. Record the changed file and what you actually observed.
