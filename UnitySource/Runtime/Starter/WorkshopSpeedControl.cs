using UnityEngine;

namespace AIVRWorkshop.Student
{
    // Exercise 1.4A: implement a bounded, finite target speed and enable the UI slider.
    [DisallowMultipleComponent]
    public sealed class WorkshopSpeedControl : MonoBehaviour
    {
        public bool CanAdjustSpeed => false; // Student changes in 1.4A.
        public float TargetSpeedMps => 0.85f;

        public void SetSpeedMps(float metresPerSecond)
        {
            // TODO (1.4A): reject NaN/infinity, clamp to 0.25–2.0, preserve last valid value.
        }
    }
}
