using UnityEngine;
namespace AIVRWorkshop.V4
{
    /// Desktop teaching controls only. VR uses teacher Inspector/UnityEvents, not OnGUI.
    public sealed class WorkshopDesktopPanel : MonoBehaviour
    {
        public WorkshopDrive drive;
        public WorkshopSpeedControl speed;
        public bool showDesktopControls = true;
        private void OnGUI()
        {
            if (!showDesktopControls || drive == null || speed == null) return;
            GUILayout.BeginArea(new Rect(16,16,310,250), GUI.skin.box);
            GUILayout.Label("ASTER / AI VR DRIVING WORKSHOP");
            GUILayout.Label("State: " + drive.CurrentStage);
            GUILayout.Label("Speed target: " + speed.TargetSpeedMps.ToString("0.00") + " m/s");
            speed.SetSpeedMps(GUILayout.HorizontalSlider(speed.TargetSpeedMps, .25f, 2f));
            if (GUILayout.Button(drive.paused ? "Resume" : "Pause")) drive.TogglePause();
            if (GUILayout.Button("Restart route")) drive.Restart();
            if (drive.CurrentStage == WorkshopDrive.Stage.AwaitChoice)
            {
                if (GUILayout.Button("Comfort: fade transfer")) drive.BeginComfortTransfer();
                if (drive.allowJetFlight && GUILayout.Button("Teacher-enabled jet flight")) drive.BeginJetFlight();
            }
            GUILayout.EndArea();
        }
    }
}
