using UnityEngine;

namespace AIVRWorkshop.V4
{
    /// Student exercise: this component exposes one bounded, visible control.
    [DisallowMultipleComponent]
    public sealed class WorkshopSpeedControl : MonoBehaviour
    {
        [Range(0.25f, 2f)] public float targetSpeedMps = 0.85f;
        public float TargetSpeedMps => float.IsNaN(targetSpeedMps) || float.IsInfinity(targetSpeedMps) ? 0.85f : Mathf.Clamp(targetSpeedMps, 0.25f, 2f);
        public void SetSpeedMps(float metresPerSecond)
        {
            if (!float.IsNaN(metresPerSecond) && !float.IsInfinity(metresPerSecond))
                targetSpeedMps = Mathf.Clamp(metresPerSecond, 0.25f, 2f);
        }
        private void OnValidate() => targetSpeedMps = TargetSpeedMps;
    }
}
