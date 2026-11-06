# Teacher answer key — not part of a student's initial Unity import

- **Student Starter:** `UnitySource/Runtime/Starter` is the only code imported during Prompt 1.3.
- **Reference solution:** the two files in `Answers/Reference` implement 1.4 speed control and explicit gap flight with **the same namespace** `AIVRWorkshop.Student`. In a **teacher/student project backup only**, replace the content of the matching existing runtime script while preserving its Unity `.meta` GUID. Never add them as second .cs files with duplicate class names.
- `Answers/Original` is a **historical archive** from the previous previous release Unity project; it has a different namespace/contract and is not a build input for source-first workflow.
- `WorkshopRobotWalk.cs` and `WorkshopDesktopPanel.cs` are complete in the Starter and remain unchanged in 1.4.

The reference solution is not permission to skip the student's independent Play checks. Build/validate the **fresh scene from FBXs**, verify the 1.3 fixed-speed gap hold, then test 1.4 on another safe checkpoint. No Quest HMD result can be inferred from desktop Play.
