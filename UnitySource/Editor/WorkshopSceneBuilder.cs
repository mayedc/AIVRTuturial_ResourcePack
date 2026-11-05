// Editor-only source to copy into Assets/WorkshopStudentGenerated/Editor.
// This does not contain a prebaked .unity scene or prefab.
#if UNITY_EDITOR
using System;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.SceneManagement;
using AIVRWorkshop.Student;

namespace AIVRWorkshop.Student.EditorTools
{
    public static class WorkshopSceneBuilder
    {
        public const string SpecPath = "Assets/WorkshopStudentGenerated/Config/WorkshopSceneSpec.json";
        const string MaterialsPath = "Assets/WorkshopStudentGenerated/Materials";

        [Serializable]
        public sealed class SceneSpec
        {
            public int schemaVersion;
            public string studentScenePath, importDirectory, carFbx, robotFbx, cityFbx, jetFbx;
            public float[] carStart, driverEyeLocal, robotStart, expectedCarBounds;
            public float[] roadMainCenter, roadMainSize, roadLandingCenter, roadLandingSize;
            public float crosswalkStopZ, gapHoldZ, roadGapStartZ, roadGapEndZ, flightLandingZ, routeEndZ;
            public float defaultSpeedMps, minSpeedMps, maxSpeedMps, robotWalkSpeedMps;
        }

        public static SceneSpec ReadSpec()
        {
            if (!File.Exists(SpecPath)) throw new InvalidOperationException("Missing " + SpecPath + ". Copy the file from UnitySource/Config first.");
            var spec = JsonUtility.FromJson<SceneSpec>(File.ReadAllText(SpecPath));
            if (spec == null || spec.schemaVersion != 1)
                throw new InvalidOperationException("Unsupported WorkshopSceneSpec schemaVersion.");
            if (spec.studentScenePath != "Assets/WorkshopStudentGenerated/Scenes/Workshop_Desktop_Student.unity" ||
                spec.importDirectory != "Assets/WorkshopStudentGenerated/Imported")
                throw new InvalidOperationException("Refusing a spec outside the student-owned output paths.");
            if (spec.carStart == null || spec.carStart.Length != 3 ||
                spec.driverEyeLocal == null || spec.driverEyeLocal.Length != 3 ||
                spec.expectedCarBounds == null || spec.expectedCarBounds.Length != 3 ||
                spec.roadMainCenter == null || spec.roadMainCenter.Length != 3 ||
                spec.roadLandingCenter == null || spec.roadLandingCenter.Length != 3 ||
                spec.roadMainSize == null || spec.roadMainSize.Length != 3 ||
                spec.roadLandingSize == null || spec.roadLandingSize.Length != 3)
                throw new InvalidOperationException("Incomplete three-component vectors in scene specification.");
            if (Mathf.Abs(spec.roadGapStartZ - 37f) > 0.01f || Mathf.Abs(spec.roadGapEndZ - 43f) > 0.01f)
                throw new InvalidOperationException("Expected an open roadway gap between z=37 and z=43.");
            return spec;
        }

        static Vector3 V(float[] a) => new Vector3(a[0], a[1], a[2]);
        static void EnsureFolder(string path)
        {
            var parts = path.Split('/');
            var current = parts[0];
            for (int i = 1; i < parts.Length; i++)
            {
                var next = current + "/" + parts[i];
                if (!AssetDatabase.IsValidFolder(next)) AssetDatabase.CreateFolder(current, parts[i]);
                current = next;
            }
        }

        static GameObject Prefab(string path, Scene scene)
        {
            var asset = AssetDatabase.LoadAssetAtPath<GameObject>(path);
            if (asset == null) throw new InvalidOperationException("Required FBX is absent or invalid: " + path);
            var instance = PrefabUtility.InstantiatePrefab(asset, scene) as GameObject;
            if (instance == null) throw new InvalidOperationException("Failed to instantiate: " + path);
            return instance;
        }

        static bool TryBounds(GameObject go, out Bounds bounds)
        {
            var renderers = go.GetComponentsInChildren<Renderer>(true);
            bounds = new Bounds();
            bool found = false;
            foreach (var r in renderers)
            {
                if (r is ParticleSystemRenderer) continue;
                if (!found) { bounds = r.bounds; found = true; }
                else bounds.Encapsulate(r.bounds);
            }
            return found;
        }

        // Different Unity importers may apply a 0.01 unit factor or an axis correction.
        // Choose a plausible uniform scale/orientation using measured renderer bounds.
        // Direction of the nose still requires a student visual check.
        static void CalibrateCar(GameObject visual, Vector3 expected)
        {
            var options = new [] {
                Quaternion.identity,
                Quaternion.Euler(-90f, 0f, 0f),
                Quaternion.Euler(90f, 0f, 0f),
                Quaternion.Euler(0f, 90f, 0f),
                Quaternion.Euler(0f, -90f, 0f),
                Quaternion.Euler(0f, 180f, 0f)
            };
            var bestScore = float.PositiveInfinity;
            var bestRotation = Quaternion.identity;
            var bestScale = 1f;
            foreach (var rotation in options)
            {
                visual.transform.localRotation = rotation;
                visual.transform.localScale = Vector3.one;
                if (!TryBounds(visual, out var b) || b.size.x < 0.001f ||
                    b.size.y < 0.001f || b.size.z < 0.001f) continue;
                float scale = expected.z / b.size.z;
                float xError = Mathf.Abs(b.size.x * scale / expected.x - 1f);
                float yError = Mathf.Abs(b.size.y * scale / expected.y - 1f);
                float score = xError + yError;
                if (scale > 0.0001f && scale < 10001f && score < bestScore)
                { bestScore = score; bestRotation = rotation; bestScale = scale; }
            }
            if (bestScore > 0.3f)
                throw new InvalidOperationException("Car FBX axes/dimensions cannot be calibrated safely. Inspect import settings and run again in a clean project. Score=" + bestScore);
            visual.transform.localRotation = bestRotation;
            visual.transform.localScale = Vector3.one * bestScale;
            Debug.Log("Workshop car bounds calibration: scale=" + bestScale + ", rotation=" + bestRotation.eulerAngles +
                ". Student must visually confirm nose faces +Z and wheels contact the road.");
        }

        static Transform FindBone(Transform root, string name)
        {
            foreach (var t in root.GetComponentsInChildren<Transform>(true))
                if (string.Equals(t.name, name, StringComparison.Ordinal)) return t;
            return null;
        }

        static void RequireLegs(WorkshopRobotWalk walk)
        {
            if (walk.leftThigh == null || walk.rightThigh == null ||
                walk.leftShin == null || walk.rightShin == null ||
                walk.leftFoot == null || walk.rightFoot == null)
                throw new InvalidOperationException("NomaRobot FBX lacks required rigid walk bones (Thigh_L/R, Shin_L/R, Foot_Sole_L/R). Inspect imported hierarchy; do not claim animation passed.");
        }

        static void BindRobot(WorkshopRobotWalk walk, Transform root)
        {
            walk.leftThigh = FindBone(root, "Thigh_L"); walk.rightThigh = FindBone(root, "Thigh_R");
            walk.leftShin = FindBone(root, "Shin_L"); walk.rightShin = FindBone(root, "Shin_R");
            walk.leftFoot = FindBone(root, "Foot_Sole_L"); walk.rightFoot = FindBone(root, "Foot_Sole_R");
            walk.leftArm = FindBone(root, "UpperArm_L"); walk.rightArm = FindBone(root, "UpperArm_R");
            walk.leftForearm = FindBone(root, "Forearm_L"); walk.rightForearm = FindBone(root, "Forearm_R");
            RequireLegs(walk);
            foreach (var animator in root.GetComponentsInChildren<Animator>(true)) animator.enabled = false;
        }

        static string SafeName(string source)
        {
            var chars = source.ToCharArray();
            for (int i = 0; i < chars.Length; i++)
                if (!char.IsLetterOrDigit(chars[i]) && chars[i] != '_' && chars[i] != '-') chars[i] = '_';
            return new string(chars);
        }

        static void ConvertMaterials(GameObject root)
        {
            EnsureFolder(MaterialsPath);
            var shader = Shader.Find("Universal Render Pipeline/Lit");
            if (shader == null) throw new InvalidOperationException("URP Lit shader missing. Create a blank URP Unity project first.");
            foreach (var r in root.GetComponentsInChildren<Renderer>(true))
            {
                var sourceMaterials = r.sharedMaterials;
                for (int i = 0; i < sourceMaterials.Length; i++)
                {
                    var src = sourceMaterials[i];
                    if (src == null) throw new InvalidOperationException("Missing imported material on " + r.name);
                    var path = MaterialsPath + "/" + SafeName(src.name) + ".mat";
                    var mat = AssetDatabase.LoadAssetAtPath<Material>(path);
                    if (mat == null)
                    {
                        mat = new Material(shader) { name = src.name };
                        var color = src.HasProperty("_BaseColor") ? src.GetColor("_BaseColor") :
                            src.HasProperty("_Color") ? src.GetColor("_Color") : Color.white;
                        mat.SetColor("_BaseColor", color);
                        if (src.HasProperty("_Metallic")) mat.SetFloat("_Metallic", src.GetFloat("_Metallic"));
                        var glass = src.name.IndexOf("Glass", StringComparison.OrdinalIgnoreCase) >= 0;
                        if (glass)
                        {
                            mat.SetFloat("_Surface", 1f);
                            mat.SetFloat("_Blend", 0f);
                            mat.SetFloat("_SrcBlend", 5f);
                            mat.SetFloat("_DstBlend", 10f);
                            mat.SetFloat("_ZWrite", 0f);
                            mat.EnableKeyword("_SURFACE_TYPE_TRANSPARENT");
                            mat.SetOverrideTag("RenderType", "Transparent");
                            mat.renderQueue = 3000;
                            var c = mat.GetColor("_BaseColor");
                            c.a = Mathf.Min(c.a, 0.35f);
                            mat.SetColor("_BaseColor", c);
                        }
                        AssetDatabase.CreateAsset(mat, path);
                    }
                    sourceMaterials[i] = mat;
                }
                r.sharedMaterials = sourceMaterials;
            }
        }

        static GameObject AddBox(string name, Transform parent, Vector3 center, Vector3 size)
        {
            var go = new GameObject(name);
            go.transform.SetParent(parent, false);
            go.transform.localPosition = center;
            go.AddComponent<BoxCollider>().size = size;
            return go;
        }

        [MenuItem("Tools/Workshop/Build Student Scene From FBX")]
        public static void Build()
        {
            if (EditorApplication.isPlayingOrWillChangePlaymode)
                throw new InvalidOperationException("Exit Play Mode before scene construction.");
            var spec = ReadSpec();
            if (File.Exists(spec.studentScenePath))
            {
                Debug.LogWarning("Student scene already exists: " + spec.studentScenePath +
                    ". Build was skipped; no objects were duplicated and no student work was overwritten. Use Validate Student Scene.");
                return;
            }
            if (SceneManager.GetActiveScene().isDirty)
                throw new InvalidOperationException("Active scene contains unsaved edits. Save or close it before generating a new scene.");

            foreach (var fbx in new [] { spec.carFbx, spec.robotFbx, spec.cityFbx, spec.jetFbx })
                if (AssetDatabase.LoadAssetAtPath<GameObject>(spec.importDirectory + "/" + fbx) == null)
                    throw new InvalidOperationException("Required model missing: " + spec.importDirectory + "/" + fbx);
            EnsureFolder("Assets/WorkshopStudentGenerated/Scenes");
            EnsureFolder(MaterialsPath);

            var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
            var world = new GameObject("WorkshopStudentRoot");
            var city = Prefab(spec.importDirectory + "/" + spec.cityFbx, scene);
            city.name = "MeridianCity";
            city.transform.SetParent(world.transform, false);
            city.transform.localPosition = Vector3.zero;
            ConvertMaterials(city);

            var car = new GameObject("AsterGT");
            car.transform.SetParent(world.transform, false);
            car.transform.localPosition = V(spec.carStart);
            var visualRoot = new GameObject("StudentVisual");
            visualRoot.transform.SetParent(car.transform, false);
            var carAsset = Prefab(spec.importDirectory + "/" + spec.carFbx, scene);
            carAsset.name = "AsterGT_Imported";
            carAsset.transform.SetParent(visualRoot.transform, false);
            CalibrateCar(visualRoot, V(spec.expectedCarBounds));
            ConvertMaterials(carAsset);

            var robot = Prefab(spec.importDirectory + "/" + spec.robotFbx, scene);
            robot.name = "NomaRobot";
            robot.transform.SetParent(world.transform, false);
            robot.transform.localPosition = V(spec.robotStart);
            robot.transform.localRotation = Quaternion.Euler(0f, 90f, 0f);
            ConvertMaterials(robot);
            var walk = robot.AddComponent<WorkshopRobotWalk>();
            BindRobot(walk, robot.transform);

            var jets = Prefab(spec.importDirectory + "/" + spec.jetFbx, scene);
            jets.name = "JetFX";
            jets.transform.SetParent(car.transform, false);
            jets.transform.localPosition = new Vector3(0f, 0f, -2.62f);
            ConvertMaterials(jets);
            jets.SetActive(false);

            var eye = new GameObject("DriverEyeAnchor");
            eye.transform.SetParent(car.transform, false);
            eye.transform.localPosition = V(spec.driverEyeLocal);
            var cameraObject = new GameObject("DesktopCamera");
            cameraObject.transform.SetParent(eye.transform, false);
            cameraObject.tag = "MainCamera";
            cameraObject.AddComponent<Camera>().fieldOfView = 80f;
            cameraObject.AddComponent<AudioListener>();

            var curtain = GameObject.CreatePrimitive(PrimitiveType.Quad);
            curtain.name = "ComfortCurtain";
            curtain.transform.SetParent(cameraObject.transform, false);
            curtain.transform.localPosition = new Vector3(0f, 0f, 0.10f);
            curtain.transform.localScale = new Vector3(0.20f, 0.20f, 1f);
            var curtainCollider = curtain.GetComponent<Collider>();
            if (curtainCollider != null) UnityEngine.Object.DestroyImmediate(curtainCollider);
            var curtainRenderer = curtain.GetComponent<Renderer>();
            curtainRenderer.enabled = false;

            AddBox("RoadCollider_Main", world.transform, V(spec.roadMainCenter), V(spec.roadMainSize));
            AddBox("RoadCollider_Landing", world.transform, V(spec.roadLandingCenter), V(spec.roadLandingSize));

            var sunObject = new GameObject("Workshop_Daylight");
            sunObject.transform.SetParent(world.transform, false);
            sunObject.transform.rotation = Quaternion.Euler(40f, -30f, 0f);
            var sun = sunObject.AddComponent<Light>();
            sun.type = LightType.Directional; sun.intensity = 1.4f;

            var speed = car.AddComponent<WorkshopSpeedControl>();
            var drive = car.AddComponent<WorkshopDrive>();
            drive.pedestrian = robot.transform;
            drive.pedestrianWalk = walk;
            drive.jets = jets;
            drive.comfortCurtain = curtainRenderer;
            drive.acceleration = 0.65f;
            var panel = world.AddComponent<WorkshopDesktopPanel>();
            panel.drive = drive; panel.speed = speed;

            WorkshopSceneValidator.ValidateOrThrow(scene, spec);
            EditorSceneManager.SaveScene(scene, spec.studentScenePath);
            AssetDatabase.SaveAssets();
            Debug.Log("Student scene created from four FBXs (no teacher scene): " +
                spec.studentScenePath + ". Check car nose (+Z), driver view, robot rig, road geometry and the complete Play route before 1.4.");
        }
    }
}
#endif
