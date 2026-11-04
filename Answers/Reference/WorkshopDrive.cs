using UnityEngine;

namespace AIVRWorkshop.V4
{
    [DisallowMultipleComponent]
    [RequireComponent(typeof(WorkshopSpeedControl))]
    public sealed class WorkshopDrive : MonoBehaviour
    {
        public enum Stage { Ready, ApproachCrossing, Yield, ApproachGap, AwaitChoice, JetFlight = 5, Arrive = 8, Complete }
        public Transform pedestrian;
        public WorkshopRobotWalk pedestrianWalk;
        public GameObject jets;
        [Tooltip("Assign an opaque overlay renderer on the XR camera; see XR guide.")]
        public Renderer comfortCurtain;
        public bool CanFly => true;
        [Min(0.1f)] public float acceleration = 0.65f;
        public bool paused;
        [SerializeField] private Stage stage;
        public Stage CurrentStage => stage;
        public float CurrentSpeedMps { get; private set; }
        private WorkshopSpeedControl speed;
        private float timer, crossingX;
        private Vector3 origin, pedestrianOrigin;
        private Material curtainMaterial;
        private const float StopAt = 7.5f, GapHold = 32f, Landing = 48f, End = 58f;

        private void Awake()
        {
            speed = GetComponent<WorkshopSpeedControl>(); origin = transform.position;
            if (pedestrian != null) pedestrianOrigin = pedestrian.position;
            if (comfortCurtain != null) curtainMaterial = comfortCurtain.material;
            Restart();
        }
        [ContextMenu("Restart workshop route")]
        public void Restart()
        {
            if (!Application.isPlaying) return;
            transform.position = origin; stage = Stage.Ready; timer = 0;
            CurrentSpeedMps = 0; crossingX = -4.5f; paused = false;
            if (pedestrian != null) pedestrian.position = pedestrianOrigin;
            if (pedestrianWalk != null) pedestrianWalk.ResetPose();
            if (jets != null) jets.SetActive(false);
            Curtain(0);
        }
        public void SetPaused(bool value) => paused = value;
        public void TogglePause() => paused = !paused;
        public void BeginJetFlight()
        {
            if (!Application.isPlaying || paused || stage != Stage.AwaitChoice) return;

            CurrentSpeedMps = 0;
            stage = Stage.JetFlight;
            timer = 0;
            if (jets != null) jets.SetActive(true);
        }

        private void Curtain(float alpha)
        {
            if (curtainMaterial == null) return;
            curtainMaterial.SetColor("_Color", new Color(0, 0, 0, alpha));
            if (curtainMaterial.HasProperty("_BaseColor")) curtainMaterial.SetColor("_BaseColor", new Color(0, 0, 0, alpha));
            comfortCurtain.enabled = alpha > 0;
        }
        private void Advance(float target, float dt)
        {
            float remaining = Mathf.Max(0, target - (transform.position.z - origin.z));
            float safeSpeed = Mathf.Sqrt(2f * Mathf.Max(.1f, acceleration) * remaining);
            float goal = Mathf.Min(speed.TargetSpeedMps, safeSpeed);
            CurrentSpeedMps = Mathf.MoveTowards(CurrentSpeedMps, goal, Mathf.Max(.1f, acceleration) * dt);
            float step = Mathf.Min(remaining, CurrentSpeedMps * dt);
            transform.position += Vector3.forward * step;
            if (At(target))
            {
                transform.position = origin + Vector3.forward * target;
                CurrentSpeedMps = 0;
            }
        }
        private bool At(float z) => transform.position.z - origin.z >= z - .011f;
        private void Update()
        {
            if (paused) { if (pedestrianWalk != null) pedestrianWalk.walking = false; return; }
            // Clamp long editor stalls; the state machine never jumps across safety holds.
            float dt = Mathf.Min(Time.deltaTime, .05f); timer += dt;
            switch (stage)
            {
                case Stage.Ready:
                    if (timer >= 3) { stage = Stage.ApproachCrossing; timer = 0; } break;
                case Stage.ApproachCrossing:
                    Advance(StopAt, dt);
                    if (At(StopAt)) { stage = Stage.Yield; timer = 0; } break;
                case Stage.Yield:
                    CurrentSpeedMps = 0;
                    if (pedestrian == null) { paused = true; Debug.LogError("Missing pedestrian: route held at crossing."); break; }
                    if (timer < 1) break;
                    crossingX = Mathf.MoveTowards(crossingX, 4.5f, .6f * dt);
                    pedestrian.position = new Vector3(origin.x + crossingX - 1.8f, pedestrianOrigin.y - .12f + Mathf.SmoothStep(0, .12f, Mathf.InverseLerp(3.9f, 4.3f, Mathf.Abs(crossingX))), pedestrianOrigin.z);
                    if (pedestrianWalk != null) pedestrianWalk.walking = crossingX < 4.5f;
                    if (crossingX >= 4.5f) { stage = Stage.ApproachGap; timer = 0; } break;
                case Stage.ApproachGap:
                    Advance(GapHold, dt);
                    if (At(GapHold)) { stage = Stage.AwaitChoice; timer = 0; }
                    break;
                case Stage.AwaitChoice:
                    break;
                case Stage.JetFlight:
                    float t = Mathf.Clamp01(timer / 10f);
                    float progress = t * t * (3f - 2f * t);
                    float height = 3f * Mathf.Pow(Mathf.Sin(Mathf.PI * t), 2);
                    transform.position = origin + new Vector3(0, height, Mathf.Lerp(GapHold, Landing, progress));
                    if (t >= 1f)
                    {
                        transform.position = origin + Vector3.forward * Landing;
                        if (jets != null) jets.SetActive(false);
                        stage = Stage.Arrive;
                        timer = 0;
                    }
                    break;
                case Stage.Arrive:
                    Advance(End, dt);
                    if (At(End)) stage = Stage.Complete;
                    break;
            }
        }
        private void OnDestroy() { if (curtainMaterial != null) Destroy(curtainMaterial); }
    }
}
