using UnityEngine;

namespace AIVRWorkshop.V4
{
    [DisallowMultipleComponent]
    public sealed class WorkshopSpeedControl : MonoBehaviour
    {
        public bool CanAdjustSpeed => false;
        public float TargetSpeedMps => 0.85f;

        public void SetSpeedMps(float metresPerSecond)
        {
            // Exercise 2A: store a finite target clamped to 0.25–2.0 m/s.
        }
    }
}
