# Exercise 2B — Implement a commanded gap crossing

Confirm the active scene is our desktop checkpoint and that the starter yields and holds at the gap. Edit WorkshopDrive.cs. Allow BeginJetFlight only while playing, unpaused, and waiting at the gap. Implement a smooth scripted arc from 32 m to 48 m along the route, about 3 m high over 10 seconds. Turn on the existing jets during flight, switch them off at landing, then continue to the end at 58 m. Make CanFly true to expose the desktop button. Preserve the crossing, eye anchor, pause and restart. Work from the starter code and these requirements.

Compile, read the Console, and test on the desktop. Verify an uncommanded hold, one explicit flight, landing, final stop, and a clean restart. Report checks as observed or not run.
