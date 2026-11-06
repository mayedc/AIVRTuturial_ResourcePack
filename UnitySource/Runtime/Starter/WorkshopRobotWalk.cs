using UnityEngine;

namespace AIVRWorkshop.Student
{
    // One animation owner: an in-place procedural pose driven by WorkshopDrive's walking flag.
    // The imported FBX Animator/Animation components must remain disabled (no double playback/root motion).
    [DisallowMultipleComponent]
    public sealed class WorkshopRobotWalk : MonoBehaviour
    {
        public bool walking;
        public Transform leftThigh, rightThigh, leftShin, rightShin, leftFoot, rightFoot;
        public Transform leftArm, rightArm, leftForearm, rightForearm;
        [Tooltip("World-space height of the workshop road; the generated colliders have a top surface at Y=0.")]
        public float roadSurfaceY = 0f;

        private float phase;
        private bool hasRestPose;
        private bool reportedGroundingProblem;
        private Quaternion[] restPose;
        private Renderer leftSole, rightSole;

        private Transform[] Bones => new[]
        {
            leftThigh, rightThigh, leftShin, rightShin, leftFoot, rightFoot,
            leftArm, rightArm, leftForearm, rightForearm
        };

        private void Awake()
        {
            CaptureRestPose();
            ResetPose();
        }

        private void CaptureRestPose()
        {
            if (hasRestPose) return;
            var bones = Bones;
            restPose = new Quaternion[bones.Length];
            for (int i = 0; i < bones.Length; i++)
                restPose[i] = bones[i] == null ? Quaternion.identity : bones[i].localRotation;
            foreach (var renderer in GetComponentsInChildren<Renderer>(true))
            {
                if (renderer.name == "Foot_Sole_L") leftSole = renderer;
                if (renderer.name == "Foot_Sole_R") rightSole = renderer;
            }
            hasRestPose = true;
        }

        public void ResetPose()
        {
            CaptureRestPose();
            phase = 0f;
            walking = false;
            var bones = Bones;
            for (int i = 0; i < bones.Length; i++)
                if (bones[i] != null) bones[i].localRotation = restPose[i];
        }

        private void Update()
        {
            if (!walking) return;
            // The source FBX's authored cycle lasts one second and remains in place.
            phase = Mathf.Repeat(phase + Mathf.Min(Time.deltaTime, 0.05f), 1f);
            Pose(phase, leftThigh, leftShin, leftFoot, leftArm, leftForearm, 0, 2, 4, 6, 8);
            Pose(Mathf.Repeat(phase + 0.5f, 1f), rightThigh, rightShin, rightFoot,
                rightArm, rightForearm, 1, 3, 5, 7, 9);
        }

        private void LateUpdate()
        {
            // Ground the lowest sole, not the pelvis. Never snap the walking root back on cycle wrap.
            if (leftSole == null || rightSole == null)
            {
                if (!reportedGroundingProblem)
                {
                    Debug.LogError("Robot sole renderers are missing; verify the imported NomaRobot FBX.");
                    reportedGroundingProblem = true;
                }
                return;
            }
            float soleY = Mathf.Min(leftSole.bounds.min.y, rightSole.bounds.min.y);
            float correction = roadSurfaceY - soleY;
            if (!float.IsNaN(correction) && !float.IsInfinity(correction) && Mathf.Abs(correction) <= 0.30f)
                transform.position += Vector3.up * correction;
            else if (!reportedGroundingProblem)
            {
                Debug.LogError("Robot foot grounding needs more than 30 cm; inspect FBX scale, axes, rest pose and ground.");
                reportedGroundingProblem = true;
            }
        }

        private void Pose(float t, Transform thigh, Transform shin, Transform foot,
            Transform arm, Transform forearm, int thighIndex, int shinIndex,
            int footIndex, int armIndex, int forearmIndex)
        {
            if (thigh == null || shin == null || foot == null) return;
            float forward, lift;
            if (t < 0.6f)
            {
                forward = Mathf.Lerp(0.18f, -0.18f, t / 0.6f);
                lift = 0f;
            }
            else
            {
                float u = (t - 0.6f) / 0.4f;
                forward = Mathf.Lerp(-0.18f, 0.18f, u);
                lift = 0.075f * Mathf.Sin(Mathf.PI * u);
            }
            // Match the Blender-authored in-place foot trajectory, not an absolute bone rotation.
            const float upperLength = 0.42f, lowerLength = 0.40f;
            float vertical = -0.80f + lift;
            float distance = Mathf.Min(0.819f, Mathf.Sqrt(forward * forward + vertical * vertical));
            float direction = Mathf.Atan2(-forward, -vertical);
            float a = Mathf.Acos(Mathf.Clamp((upperLength * upperLength + distance * distance - lowerLength * lowerLength) /
                (2f * upperLength * Mathf.Max(0.0001f, distance)), -1f, 1f));
            float bend = Mathf.PI - Mathf.Acos(Mathf.Clamp(
                (upperLength * upperLength + lowerLength * lowerLength - distance * distance) /
                (2f * upperLength * lowerLength), -1f, 1f));
            float upper = direction - a;
            // Preserve imported FBX bind transforms and rotate around each bone's authored local axis.
            thigh.localRotation = restPose[thighIndex] * Quaternion.Euler(upper * Mathf.Rad2Deg, 0f, 0f);
            shin.localRotation = restPose[shinIndex] * Quaternion.Euler(bend * Mathf.Rad2Deg, 0f, 0f);
            foot.localRotation = restPose[footIndex] * Quaternion.Euler(-(upper + bend) * Mathf.Rad2Deg, 0f, 0f);
            if (arm != null)
                arm.localRotation = restPose[armIndex] * Quaternion.Euler(
                    18f * Mathf.Sin(2f * Mathf.PI * t), 0f, 0f);
            if (forearm != null)
                forearm.localRotation = restPose[forearmIndex] * Quaternion.Euler(-8f, 0f, 0f);
        }
    }
}
