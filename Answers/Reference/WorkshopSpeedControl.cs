using UnityEngine;

namespace AIVRWorkshop.V4
{
    [DisallowMultipleComponent]
    public sealed class WorkshopSpeedControl : MonoBehaviour
    {
        private float targetSpeedMps = 0.85f;
        public bool CanAdjustSpeed => true;
        public float TargetSpeedMps => float.IsNaN(targetSpeedMps) || float.IsInfinity(targetSpeedMps) ? 0.85f : Mathf.Clamp(targetSpeedMps, 0.25f, 2f);
        public void SetSpeedMps(float metresPerSecond)
        {
            if (!float.IsNaN(metresPerSecond) && !float.IsInfinity(metresPerSecond))
                targetSpeedMps = Mathf.Clamp(metresPerSecond, 0.25f, 2f);
        }
    }
}
