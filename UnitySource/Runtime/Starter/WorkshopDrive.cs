using UnityEngine;

namespace AIVRWorkshop.Student
{
    // One scripted route mover. The car root faces Unity +Z.
    [DisallowMultipleComponent]
    [RequireComponent(typeof(WorkshopSpeedControl))]
    public sealed class WorkshopDrive : MonoBehaviour
    {
        public enum Stage { Ready, ApproachCrossing, Yield, ApproachGap, AwaitChoice, JetFlight, Arrive, Complete }
        public Transform pedestrian;
        public WorkshopRobotWalk pedestrianWalk;
        public GameObject jets;
        public Renderer comfortCurtain;
        [Min(0.1f)] public float acceleration = 0.65f;
        public bool paused;
        [SerializeField] private Stage stage = Stage.Ready;
        public Stage CurrentStage => stage;
        public float CurrentSpeedMps { get; private set; }
        public bool CanFly => false; // Exercise 1.4B.

        private WorkshopSpeedControl speed;
        private Vector3 origin, pedestrianOrigin;
        private float timer, crossingX;
        private const float Crossing = 7.5f, GapHold = 32f, Landing = 48f, End = 58f;

        private void Awake()
        {
            speed = GetComponent<WorkshopSpeedControl>();
            origin = transform.position;
            if (pedestrian != null) pedestrianOrigin = pedestrian.position;
            Restart();
        }

        public void Restart()
        {
            if (!Application.isPlaying) return;
            transform.position = origin;
            stage = Stage.Ready; timer = 0f; crossingX = -4.5f;
            paused = false; CurrentSpeedMps = 0f;
            if (pedestrian != null) pedestrian.position = pedestrianOrigin;
            if (pedestrianWalk != null) pedestrianWalk.ResetPose();
            if (jets != null) jets.SetActive(false);
            if (comfortCurtain != null) comfortCurtain.enabled = false;
        }
        public void SetPaused(bool value) => paused = value;
        public void TogglePause() => paused = !paused;

        public void BeginJetFlight()
        {
            // TODO (1.4B): only while playing, unpaused, and at Stage.AwaitChoice.
            // On an explicit UI command, fly z=32 -> 48 in ~10s, peak +3m.
        }

        private void Advance(float target, float dt)
        {
            float remaining = Mathf.Max(0f, target - (transform.position.z - origin.z));
            float brakingSpeed = Mathf.Sqrt(2f * Mathf.Max(0.1f, acceleration) * remaining);
            float goal = Mathf.Min(speed.TargetSpeedMps, brakingSpeed);
            CurrentSpeedMps = Mathf.MoveTowards(CurrentSpeedMps, goal, Mathf.Max(0.1f, acceleration) * dt);
            transform.position += Vector3.forward * Mathf.Min(remaining, CurrentSpeedMps * dt);
            if (At(target))
            {
                transform.position = origin + Vector3.forward * target;
                CurrentSpeedMps = 0f;
            }
        }

        private bool At(float z) => transform.position.z - origin.z >= z - 0.011f;

        private void Update()
        {
            if (paused) { if (pedestrianWalk != null) pedestrianWalk.walking = false; return; }
            float dt = Mathf.Min(Time.deltaTime, 0.05f);
            timer += dt;
            switch (stage)
            {
                case Stage.Ready:
                    if (timer >= 3f) { stage = Stage.ApproachCrossing; timer = 0f; }
                    break;
                case Stage.ApproachCrossing:
                    Advance(Crossing, dt);
                    if (At(Crossing)) { stage = Stage.Yield; timer = 0f; }
                    break;
                case Stage.Yield:
                    CurrentSpeedMps = 0f;
                    if (pedestrian == null) { paused = true; Debug.LogError("Missing pedestrian: vehicle held at crossing."); break; }
                    if (timer < 1f) break;
                    crossingX = Mathf.MoveTowards(crossingX, 4.5f, 0.6f * dt);
                    pedestrian.position = new Vector3(
                        origin.x + crossingX - 1.8f,
                        pedestrianOrigin.y - 0.12f +
                          Mathf.SmoothStep(0f, 0.12f, Mathf.InverseLerp(3.9f, 4.3f, Mathf.Abs(crossingX))),
                        pedestrianOrigin.z);
                    if (pedestrianWalk != null) pedestrianWalk.walking = crossingX < 4.5f;
                    if (crossingX >= 4.5f) { stage = Stage.ApproachGap; timer = 0f; }
                    break;
                case Stage.ApproachGap:
                    Advance(GapHold, dt);
                    if (At(GapHold)) { stage = Stage.AwaitChoice; timer = 0f; }
                    break;
                case Stage.AwaitChoice:
                    // Wait for the future explicit 1.4B button, never auto-launch.
                    CurrentSpeedMps = 0f;
                    break;
                case Stage.JetFlight:
                    // Implemented only in student exercise 1.4B.
                    break;
                case Stage.Arrive:
                    Advance(End, dt);
                    if (At(End)) { stage = Stage.Complete; CurrentSpeedMps = 0f; }
                    break;
                case Stage.Complete:
                    CurrentSpeedMps = 0f;
                    break;
            }
        }
    }
}
