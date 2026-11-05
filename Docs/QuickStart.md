# Quick start — source-first Cursor classroom

1. Open a new **empty local folder** in Cursor. Paste [00 clone/preflight](../Prompts/00_Clone_Preflight.md) so Cursor clones the repository (do not use a ZIP).
2. Open **empty Blender** and an independent **blank Unity URP** project; paste [00 install/update MCP](../Prompts/00_Install_Update_MCP.md). Both applications must provide live MCP readbacks.
3. Paste [1.1 inspect eight models](../Prompts/01_1_Review_All_Blender_Models.md) and let the student review them. Then separately paste [1.2 choose car color](../Prompts/01_2_Choose_Car_Color.md); the student approves their own Blender file.
4. Paste [1.3 create scene from the student FBX and three course FBXs](../Prompts/01_3_Export_And_Build_Unity.md). Cursor brings `UnitySource` into the **blank student Unity project** and builds `Workshop_Desktop_Student.unity` **without a teacher .unity scene, prefab bundle or .unitypackage**. The student must personally Play the entire fixed-speed route.
5. Only after that passes, paste [1.4 speed and jet flight](../Prompts/01_4_Speed_And_Gap_Flight.md), and test both interactions.
6. Paste [02_1 XR/Meta/Quest Link self-check](../Prompts/02_1_XR_Setup_And_Device_Check.md), then separately [02_2 attach tracked driver's-eye rig and wear the headset](../Prompts/02_2_Attach_Driver_Camera_And_Test.md).

The new `UnitySource/Editor` source builder is being prepared for real Unity/Quest regression testing. A source code or repository check is **not** a complete Unity Play or headset pass. See [UnitySource guide](../UnitySource/README.md) and [acceptance matrix](Acceptance_Matrix.md).
