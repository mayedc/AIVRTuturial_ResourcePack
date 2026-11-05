#if UNITY_EDITOR
using System;
using System.Linq;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.SceneManagement;
using AIVRWorkshop.Student;

namespace AIVRWorkshop.Student.EditorTools
{
    public static class WorkshopSceneValidator
    {
        static GameObject Child(Transform parent, string name)
        {
            var t = parent.Find(name);
            if (t == null) throw new InvalidOperationException("Missing child: " + parent.name + "/" + name);
            return t.gameObject;
        }

        public static void ValidateOrThrow(Scene scene, WorkshopSceneBuilder.SceneSpec spec, bool requireStarter = true)
        {
            if (!scene.IsValid() || !scene.isLoaded) throw new InvalidOperationException("Student scene must be open and loaded.");
            var roots = scene.GetRootGameObjects();
            var world = roots.SingleOrDefault(x => x.name == "WorkshopStudentRoot");
            if (world == null) throw new InvalidOperationException("No WorkshopStudentRoot in the active scene.");
            var car = Child(world.transform, "AsterGT");
            var visual = Child(car.transform, "StudentVisual");
            var robot = Child(world.transform, "NomaRobot");
            var eye = Child(car.transform, "DriverEyeAnchor");
            var camera = Child(eye.transform, "DesktopCamera");
            var mainRoad = Child(world.transform, "RoadCollider_Main").GetComponent<BoxCollider>();
            var landingRoad = Child(world.transform, "RoadCollider_Landing").GetComponent<BoxCollider>();
            var drive = car.GetComponent<WorkshopDrive>();
            var speed = car.GetComponent<WorkshopSpeedControl>();
            var walk = robot.GetComponent<WorkshopRobotWalk>();
            if (drive == null || speed == null || walk == null ||
                drive.pedestrian != robot.transform || drive.pedestrianWalk != walk || drive.jets == null)
                throw new InvalidOperationException("Driving or robot component references are missing.");
            if (mainRoad == null || landingRoad == null)
                throw new InvalidOperationException("Road colliders missing.");
            if (mainRoad.bounds.max.z > spec.roadGapStartZ + 0.02f ||
                landingRoad.bounds.min.z < spec.roadGapEndZ - 0.02f)
                throw new InvalidOperationException("Collider crosses the 6m road gap.");
            if (scene.GetRootGameObjects().Sum(x => x.GetComponentsInChildren<WorkshopDrive>(true).Length) != 1 ||
                scene.GetRootGameObjects().Sum(x => x.GetComponentsInChildren<WorkshopSpeedControl>(true).Length) != 1)
                throw new InvalidOperationException("Multiple car movers/speed components.");
            if (camera.GetComponent<Camera>() == null || camera.GetComponent<AudioListener>() == null)
                throw new InvalidOperationException("Desktop camera or AudioListener missing.");
            if (!camera.activeInHierarchy || camera.GetComponent<Camera>().enabled == false)
                throw new InvalidOperationException("Starter desktop camera not active.");
            var renderers = visual.GetComponentsInChildren<Renderer>(true);
            if (renderers.Length == 0) throw new InvalidOperationException("Student car contains no renderers.");
            if (walk.leftThigh == null || walk.rightThigh == null || walk.leftFoot == null ||
                walk.rightFoot == null || walk.leftShin == null || walk.rightShin == null)
                throw new InvalidOperationException("Robot bones unassigned.");
            if (requireStarter && (drive.CanFly || speed.CanAdjustSpeed))
                throw new InvalidOperationException("This is a 1.3 starter. Do not implement 1.4 features before Play approval.");
            Debug.Log("Student scene structure PASS (" + (requireStarter ? "1.3 starter" : "1.4 interactive") +
                "). This does NOT establish Play, driver-view, robot motion or headset acceptance.");
        }

        [MenuItem("Tools/Workshop/Validate Student Scene (1.3)")]
        public static void Validate()
        {
            var spec = WorkshopSceneBuilder.ReadSpec();
            ValidateOrThrow(SceneManager.GetActiveScene(), spec);
        }

        [MenuItem("Tools/Workshop/Validate Student Scene (1.4)")]
        public static void ValidateInteractive()
        {
            var spec = WorkshopSceneBuilder.ReadSpec();
            var scene = SceneManager.GetActiveScene();
            ValidateOrThrow(scene, spec, false);
            var car = scene.GetRootGameObjects().Single(x => x.name == "WorkshopStudentRoot")
                .transform.Find("AsterGT");
            if (!car.GetComponent<WorkshopSpeedControl>().CanAdjustSpeed)
                throw new InvalidOperationException("1.4 speed adjustment has not been enabled.");
            Debug.Log("1.4 STRUCTURAL checks passed. The student must separately Play-test speed, explicit flight, landing, pause and restart.");
        }
    }
}
#endif
