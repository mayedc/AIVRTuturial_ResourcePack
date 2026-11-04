using System;
using System.Globalization;
using System.IO;
using System.Text.RegularExpressions;
using AIVRWorkshop.V4;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace AIVRWorkshop.V4.Editor
{
    /// Observes the desktop route in Play Mode and writes a sanitized log. Does not save the scene.
    [InitializeOnLoad]
    public static class WorkshopDesktopProbe
    {
        const string ActiveKey = "AIVR.Probe.Active";
        const string LogKey = "AIVR.Probe.Log";
        const string ScenePath = "Assets/AI_VR_Workshop_V4/Scenes/Workshop_Desktop.unity";

        static string logPath;
        static double startedAt;
        static double nextSample;
        static double pauseUntil;
        static double speedDeadline;
        static bool pauseIssued;
        static bool pauseHeld;
        static bool resumeMoved;
        static bool jetArmed;
        static bool restartIssued;
        static bool speedSeen;
        static bool stopping;
        static bool startedMoving;
        static bool sawApproach;
        static bool sawYield;
        static bool sawGapApproach;
        static bool sawAwait;
        static bool sawJet;
        static bool sawArrive;
        static bool sawComplete;
        static bool sawReadyAfterRestart;
        static bool stoppedAtCrosswalk;
        static bool waitedWhileCrossing;
        static bool resumedAfterCrossing;
        static bool robotCrossed;
        static bool jumped;
        static bool crossedGap;
        static bool landed;
        static bool finalStop;
        static bool walkPosed;
        static bool frameAdvanced;
        static int errors;
        static int lastFrame = -1;
        static float pauseZ;
        static float yieldZ;
        static float minPedX = 999f;
        static float maxPedX = -999f;
        static float maxCruise = 0f;
        static float maxJetY;
        static float maxZ = -999f;
        static float speedAfterChange;
        static float thighAtYield = 999f;
        static Vector3 origin;
        static bool haveOrigin;
        static WorkshopDrive.Stage lastStage;
        static bool haveStage;

        static WorkshopDesktopProbe()
        {
            if (!SessionState.GetBool(ActiveKey, false)) return;
            logPath = SessionState.GetString(LogKey, "");
            EditorApplication.update += Tick;
            Application.logMessageReceived += OnLog;
        }

        [MenuItem("Workshop V4/Run desktop play mode probe")]
        public static void Run()
        {
            if (EditorApplication.isPlaying)
            {
                Debug.LogError("Desktop probe refused because Play Mode is already active.");
                return;
            }
            logPath = Path.GetFullPath(Path.Combine(Application.dataPath, "..", "Logs", "DesktopPlayModeProbe.log"));
            Directory.CreateDirectory(Path.GetDirectoryName(logPath) ?? ".");
            File.WriteAllText(logPath, "probe=start\nscene=" + ScenePath + "\n");
            SessionState.SetString(LogKey, logPath);
            SessionState.SetBool(ActiveKey, true);
            EditorSceneManager.OpenScene(ScenePath);
            EditorApplication.isPlaying = true;
        }

        static void OnLog(string condition, string stackTrace, LogType type)
        {
            if (type != LogType.Error && type != LogType.Exception && type != LogType.Assert) return;
            errors++;
            Write("runtime-error=" + Sanitize(condition));
        }

        static void Tick()
        {
            if (!SessionState.GetBool(ActiveKey, false) || stopping) return;
            if (!EditorApplication.isPlaying)
            {
                if (startedAt > 0 && EditorApplication.timeSinceStartup - startedAt > 2)
                    Finish("play-mode-exited-early");
                return;
            }
            if (startedAt <= 0) startedAt = EditorApplication.timeSinceStartup;
            if (EditorApplication.timeSinceStartup < nextSample) return;
            nextSample = EditorApplication.timeSinceStartup + 0.25;
            var drive = UnityEngine.Object.FindAnyObjectByType<WorkshopDrive>();
            if (drive == null)
            {
                if (EditorApplication.timeSinceStartup - startedAt > 20) Finish("drive-missing");
                return;
            }
            if (Time.frameCount != lastFrame)
            {
                if (lastFrame >= 0 && Time.frameCount > lastFrame) frameAdvanced = true;
                lastFrame = Time.frameCount;
            }
            if (!haveOrigin)
            {
                origin = drive.transform.position;
                haveOrigin = true;
                Write("origin=" + F(origin.x) + "," + F(origin.y) + "," + F(origin.z));
                Write("savedAllowJet=" + drive.allowJetFlight);
                var speed = drive.GetComponent<WorkshopSpeedControl>();
                Write("savedTargetSpeed=" + (speed != null ? F(speed.TargetSpeedMps) : "missing"));
                var panel = UnityEngine.Object.FindAnyObjectByType<WorkshopDesktopPanel>();
                Write("panel=" + (panel != null ? panel.gameObject.name + " controls=" + panel.showDesktopControls : "missing"));
            }
            float z = drive.transform.position.z - origin.z;
            float y = drive.transform.position.y - origin.y;
            if (z > maxZ) maxZ = z;
            if (y > maxJetY) maxJetY = y;
            var stage = drive.CurrentStage;
            if (!haveStage || stage != lastStage)
            {
                Write("stage=" + stage + " t=" + F((float)(EditorApplication.timeSinceStartup - startedAt)) + " z=" + F(z) + " y=" + F(y) + " speed=" + F(drive.CurrentSpeedMps) + " frame=" + Time.frameCount);
                lastStage = stage;
                haveStage = true;
            }
            if (stage == WorkshopDrive.Stage.ApproachCrossing) sawApproach = true;
            if (stage == WorkshopDrive.Stage.ApproachCrossing && drive.CurrentSpeedMps > 0.15f && z > 0.4f) startedMoving = true;
            if (pauseIssued && !drive.paused && drive.CurrentSpeedMps > maxCruise) maxCruise = drive.CurrentSpeedMps;
            if (!pauseIssued && stage == WorkshopDrive.Stage.ApproachCrossing && z > 1.2f && drive.CurrentSpeedMps > 0.2f)
            {
                pauseZ = drive.transform.position.z;
                drive.SetPaused(true);
                pauseUntil = EditorApplication.timeSinceStartup + 1.0;
                pauseIssued = true;
                Write("event=pause z=" + F(z));
            }
            if (pauseIssued && drive.paused && EditorApplication.timeSinceStartup >= pauseUntil)
            {
                float drift = Mathf.Abs(drive.transform.position.z - pauseZ);
                pauseHeld = drift < 0.03f && drive.CurrentStage == WorkshopDrive.Stage.ApproachCrossing;
                drive.SetPaused(false);
                Write("event=resume drift=" + F(drift) + " held=" + pauseHeld);
            }
            if (pauseIssued && !drive.paused && !resumeMoved && drive.transform.position.z > pauseZ + 0.45f)
            {
                resumeMoved = true;
                Write("event=moved-after-resume z=" + F(z));
            }
            if (stage == WorkshopDrive.Stage.Yield)
            {
                if (!sawYield)
                {
                    sawYield = true;
                    yieldZ = z;
                    stoppedAtCrosswalk = z > 7.2f && z < 7.9f && drive.CurrentSpeedMps < 0.05f;
                    if (drive.pedestrianWalk != null && drive.pedestrianWalk.leftThigh != null)
                        thighAtYield = drive.pedestrianWalk.leftThigh.localEulerAngles.x;
                }
                if (Mathf.Abs(z - yieldZ) < 0.05f && drive.CurrentSpeedMps < 0.05f) waitedWhileCrossing = true;
                if (drive.pedestrian != null)
                {
                    float px = drive.pedestrian.position.x;
                    if (px < minPedX) minPedX = px;
                    if (px > maxPedX) maxPedX = px;
                }
                if (drive.pedestrianWalk != null && drive.pedestrianWalk.leftThigh != null && thighAtYield < 900f)
                {
                    float delta = Mathf.DeltaAngle(thighAtYield, drive.pedestrianWalk.leftThigh.localEulerAngles.x);
                    if (Mathf.Abs(delta) > 8f) walkPosed = true;
                }
            }
            if (maxPedX - minPedX > 4f) robotCrossed = true;
            if (stage == WorkshopDrive.Stage.ApproachGap)
            {
                sawGapApproach = true;
                if (z > 8.5f && drive.CurrentSpeedMps > 0.15f) resumedAfterCrossing = true;
            }
            if (stage == WorkshopDrive.Stage.AwaitChoice) sawAwait = true;
            if (!jetArmed && stage == WorkshopDrive.Stage.AwaitChoice)
            {
                drive.allowJetFlight = true;
                jetArmed = true;
                Write("event=enable-existing-jet-flag");
            }
            bool jetsOn = drive.jets != null && drive.jets.activeSelf;
            if (stage == WorkshopDrive.Stage.JetFlight)
            {
                sawJet = true;
                if (y > 1.0f && jetsOn) jumped = true;
                if (z > 40f) crossedGap = true;
            }
            if (sawJet && y < 0.2f && !jetsOn && (stage == WorkshopDrive.Stage.Arrive || stage == WorkshopDrive.Stage.Complete))
                landed = true;
            if (stage == WorkshopDrive.Stage.Arrive) sawArrive = true;
            if (stage == WorkshopDrive.Stage.Complete)
            {
                sawComplete = true;
                finalStop = z > 56f && drive.CurrentSpeedMps < 0.05f;
            }
            if (sawComplete && !restartIssued)
            {
                var speed = drive.GetComponent<WorkshopSpeedControl>();
                drive.Restart();
                if (speed != null) speed.SetSpeedMps(1.6f);
                restartIssued = true;
                speedDeadline = EditorApplication.timeSinceStartup + 30;
                Write("event=restart targetSpeed=1.60 z=" + F(drive.transform.position.z - origin.z));
            }
            if (restartIssued && stage == WorkshopDrive.Stage.Ready) sawReadyAfterRestart = true;
            if (restartIssued && !speedSeen && stage == WorkshopDrive.Stage.ApproachCrossing && drive.CurrentSpeedMps >= 1.15f)
            {
                speedSeen = true;
                speedAfterChange = drive.CurrentSpeedMps;
                Write("event=faster-cruise speed=" + F(speedAfterChange));
                Finish("completed");
                return;
            }
            if (restartIssued && !speedSeen && EditorApplication.timeSinceStartup > speedDeadline)
            {
                Finish("speed-timeout");
                return;
            }
            if (!restartIssued && EditorApplication.timeSinceStartup - startedAt > 170)
                Finish("route-timeout");
        }

        static void Finish(string reason)
        {
            if (stopping) return;
            stopping = true;
            Write("result=reason:" + reason
                + " started=" + startedMoving
                + " autoRoute=" + (sawApproach && sawYield && sawGapApproach && sawAwait)
                + " stopCrosswalk=" + stoppedAtCrosswalk
                + " robotCrossed=" + robotCrossed
                + " pedSpan=" + F(maxPedX > minPedX ? maxPedX - minPedX : 0f)
                + " waited=" + waitedWhileCrossing
                + " resumed=" + resumedAfterCrossing
                + " jumped=" + jumped
                + " crossedGap=" + crossedGap
                + " maxY=" + F(maxJetY)
                + " maxZ=" + F(maxZ)
                + " landed=" + landed
                + " finalStop=" + finalStop
                + " pauseHeld=" + pauseHeld
                + " resumeMoved=" + resumeMoved
                + " restartReady=" + sawReadyAfterRestart
                + " speedChanged=" + speedSeen
                + " speedAfter=" + F(speedAfterChange)
                + " cruiseBefore=" + F(maxCruise)
                + " walkPosed=" + walkPosed
                + " framesAdvanced=" + frameAdvanced
                + " errors=" + errors
                + " sawJet=" + sawJet
                + " sawArrive=" + sawArrive
                + " sawComplete=" + sawComplete);
            Write("probe=done");
            SessionState.SetBool(ActiveKey, false);
            Application.logMessageReceived -= OnLog;
            EditorApplication.update -= Tick;
            EditorApplication.isPlaying = false;
        }

        static void Write(string line)
        {
            if (string.IsNullOrEmpty(logPath)) return;
            File.AppendAllText(logPath, line + "\n");
        }

        static string F(float value) => value.ToString("0.00", CultureInfo.InvariantCulture);

        static string Sanitize(string value)
        {
            if (string.IsNullOrEmpty(value)) return "";
            var line = value.Split('\n')[0];
            line = Regex.Replace(line, @"[A-Za-z]:\\[^\s]+", "[local-path]");
            line = Regex.Replace(line, "/" + "Users" + @"/[^\s]+", "[local-path]");
            return line;
        }
    }
}
