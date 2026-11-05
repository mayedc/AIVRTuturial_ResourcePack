using UnityEngine;

namespace AIVRWorkshop.Student
{
    // Optional rigid-bone walking pose. A root crossing translation is handled by WorkshopDrive.
    // Do not combine this with an enabled Animator/root motion controller on the same armature.
    public sealed class WorkshopRobotWalk : MonoBehaviour
    {
        public bool walking;
        public Transform leftThigh, rightThigh, leftShin, rightShin, leftFoot, rightFoot;
        public Transform leftArm, rightArm, leftForearm, rightForearm;
        private float phase;
        private void Awake() => ResetPose();
        public void ResetPose()
        {
            phase = 0f; walking = false;
            Pose(0f, leftThigh, leftShin, leftFoot, leftArm, leftForearm);
            Pose(0.5f, rightThigh, rightShin, rightFoot, rightArm, rightForearm);
        }
        private void Update()
        {
            if (!walking) return;
            phase = Mathf.Repeat(phase + Mathf.Min(Time.deltaTime, 0.05f), 1f);
            Pose(phase, leftThigh, leftShin, leftFoot, leftArm, leftForearm);
            Pose(Mathf.Repeat(phase + 0.5f, 1f), rightThigh, rightShin, rightFoot, rightArm, rightForearm);
        }
        private static void Pose(float t, Transform thigh, Transform shin, Transform foot, Transform arm, Transform forearm)
        {
            if (thigh == null || shin == null || foot == null) return;
            float forward, lift;
            if (t < 0.6f) { forward = Mathf.Lerp(0.18f, -0.18f, t / 0.6f); lift = 0f; }
            else { float u = (t - 0.6f) / 0.4f; forward = Mathf.Lerp(-0.18f, 0.18f, u); lift = 0.075f * Mathf.Sin(Mathf.PI * u); }
            float vertical = -0.80f + lift;
            const float upperLength = 0.42f, lowerLength = 0.40f;
            float distance = Mathf.Min(0.819f, Mathf.Sqrt(forward * forward + vertical * vertical));
            float direction = Mathf.Atan2(-forward, -vertical);
            float a = Mathf.Acos(Mathf.Clamp((upperLength * upperLength + distance * distance - lowerLength * lowerLength) /
                (2 * upperLength * Mathf.Max(0.0001f, distance)), -1f, 1f));
            float bend = Mathf.PI - Mathf.Acos(Mathf.Clamp((upperLength * upperLength + lowerLength * lowerLength - distance * distance) /
                (2 * upperLength * lowerLength), -1f, 1f));
            float upper = direction - a;
            thigh.localRotation = Quaternion.Euler(upper * Mathf.Rad2Deg, 0f, 0f);
            shin.localRotation = Quaternion.Euler(bend * Mathf.Rad2Deg, 0f, 0f);
            foot.localRotation = Quaternion.Euler(-(upper + bend) * Mathf.Rad2Deg, 0f, 0f);
            if (arm != null) arm.localRotation = Quaternion.Euler(18f * Mathf.Sin(2f * Mathf.PI * t), 0f, 0f);
            if (forearm != null) forearm.localRotation = Quaternion.Euler(-8f, 0f, 0f);
        }
    }
}
