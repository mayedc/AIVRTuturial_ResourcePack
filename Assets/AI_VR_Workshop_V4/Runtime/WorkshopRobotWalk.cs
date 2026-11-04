using UnityEngine;

namespace AIVRWorkshop.V4
{
    /// Rigid armour rig, matching the delivered rest meshes; independent of Humanoid retargeting.
    public sealed class WorkshopRobotWalk : MonoBehaviour
    {
        public bool walking;
        public Transform leftThigh, rightThigh, leftShin, rightShin, leftFoot, rightFoot;
        public Transform leftArm, rightArm, leftForearm, rightForearm;
        private float phase;
        private void Awake() => ResetPose();
        public void ResetPose()
        {
            phase = 0; walking = false;
            Pose(0, leftThigh, leftShin, leftFoot, leftArm, leftForearm);
            Pose(.5f, rightThigh, rightShin, rightFoot, rightArm, rightForearm);
        }
        private void Update()
        {
            if (!walking) return;
            phase = Mathf.Repeat(phase + Mathf.Min(Time.deltaTime, .05f), 1f);
            Pose(phase, leftThigh, leftShin, leftFoot, leftArm, leftForearm);
            Pose(Mathf.Repeat(phase + .5f, 1f), rightThigh, rightShin, rightFoot, rightArm, rightForearm);
        }
        private static void Pose(float t, Transform thigh, Transform shin, Transform foot, Transform arm, Transform forearm)
        {
            if (thigh == null || shin == null || foot == null) return;
            float forward, lift;
            if (t < .6f) { forward = Mathf.Lerp(.18f, -.18f, t / .6f); lift = 0; }
            else { float u = (t - .6f) / .4f; forward = Mathf.Lerp(-.18f, .18f, u); lift = .075f * Mathf.Sin(Mathf.PI * u); }
            float vertical = -.80f + lift; // crouched 2cm for reachable stance targets
            const float upperLength = .42f, lowerLength = .40f;
            float distance = Mathf.Min(.819f, Mathf.Sqrt(forward * forward + vertical * vertical));
            float direction = Mathf.Atan2(-forward, -vertical);
            float a = Mathf.Acos(Mathf.Clamp((upperLength*upperLength + distance*distance - lowerLength*lowerLength)/(2*upperLength*distance), -1, 1));
            float bend = Mathf.PI - Mathf.Acos(Mathf.Clamp((upperLength*upperLength + lowerLength*lowerLength - distance*distance)/(2*upperLength*lowerLength), -1, 1));
            float upper = direction - a;
            thigh.localRotation = Quaternion.Euler(upper * Mathf.Rad2Deg, 0, 0);
            shin.localRotation = Quaternion.Euler(bend * Mathf.Rad2Deg, 0, 0);
            foot.localRotation = Quaternion.Euler(-(upper+bend) * Mathf.Rad2Deg, 0, 0);
            if (arm != null) arm.localRotation = Quaternion.Euler(18 * Mathf.Sin(2*Mathf.PI*t), 0, 0);
            if (forearm != null) forearm.localRotation = Quaternion.Euler(-8, 0, 0);
        }
    }
}
