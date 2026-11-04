using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;

namespace AIVRWorkshop.V4.Editor
{
    public static class WorkshopValidation
    {
        private const string Root = "Assets/AI_VR_Workshop_V4";
        [MenuItem("Workshop V4/Validate active workshop scene")]
        public static void Validate()
        {
            var scene = SceneManager.GetActiveScene();
            if (!scene.path.StartsWith(Root + "/Scenes/", StringComparison.Ordinal))
            { Debug.LogError("Open a V4 teaching scene first. Existing project scenes are untouched."); return; }
            var errors = new List<string>(); var report = new StringBuilder();
            int meshes = 0, renderers = 0, missingScripts = 0; long triangles = 0;
            foreach (var root in scene.GetRootGameObjects())
            {
                foreach (var t in root.GetComponentsInChildren<Transform>(true))
                    missingScripts += GameObjectUtility.GetMonoBehavioursWithMissingScriptCount(t.gameObject);
                foreach (var mf in root.GetComponentsInChildren<MeshFilter>(true))
                {
                    if (mf.sharedMesh == null) { errors.Add("Missing mesh: " + mf.name); continue; }
                    meshes++; var mesh = mf.sharedMesh;
                    if (mesh.vertexCount == 0) errors.Add("Empty mesh: " + mf.name);
                    triangles += mesh.triangles.Length / 3;
                    foreach (var p in mesh.vertices)
                        if (float.IsNaN(p.x) || float.IsInfinity(p.x) || float.IsNaN(p.y) || float.IsInfinity(p.y) || float.IsNaN(p.z) || float.IsInfinity(p.z))
                        { errors.Add("Non-finite vertex: " + mf.name); break; }
                }
                foreach (var r in root.GetComponentsInChildren<Renderer>(true))
                {
                    renderers++;
                    foreach (var m in r.sharedMaterials)
                        if (m == null || m.shader == null || !m.shader.isSupported) errors.Add("Missing/unsupported material: " + r.name);
                }
            }
            if (missingScripts > 0) errors.Add("Missing scripts: " + missingScripts);
            WorkshopDrive drive = null;
            foreach (var root in scene.GetRootGameObjects())
                if (drive == null) drive = root.GetComponentInChildren<WorkshopDrive>(true);
            if (drive == null) errors.Add("No WorkshopDrive component");
            else
            {
                if (drive.pedestrian == null || drive.pedestrianWalk == null || drive.jets == null || drive.comfortCurtain == null)
                    errors.Add("Route reference missing");
                if (drive.allowJetFlight) report.AppendLine("CAUTION: jet flight enabled; requires comfort acceptance.");
            }
            report.AppendLine("Unity Editor validation (not runtime or Quest acceptance)");
            report.AppendLine("UTC: " + DateTime.UtcNow.ToString("O"));
            report.AppendLine("Editor: " + Application.unityVersion + " / " + Application.platform);
            report.AppendLine("Scene: " + scene.path);
            report.AppendLine($"Meshes: {meshes}; Renderers: {renderers}; Triangles: {triangles}");
            report.AppendLine("Errors: " + errors.Count);
            foreach (var e in errors) report.AppendLine("FAIL: " + e);
            report.AppendLine("UNTESTED here: Play Mode timing, both-eye VR rendering, device FPS, comfort.");
            Directory.CreateDirectory(Root + "/Validation");
            string path = Root + "/Validation/Editor_" + DateTime.UtcNow.ToString("yyyyMMdd_HHmmss") + ".txt";
            File.WriteAllText(path, report.ToString()); AssetDatabase.Refresh();
            if (errors.Count > 0) Debug.LogError(report.ToString()); else Debug.Log(report.ToString());
        }
        [MenuItem("Workshop V4/Save active scene as new checkpoint")]
        public static void SaveCheckpoint()
        {
            var scene = SceneManager.GetActiveScene();
            if (!scene.path.StartsWith(Root + "/Scenes/", StringComparison.Ordinal)) return;
            string path = AssetDatabase.GenerateUniqueAssetPath(Root + "/Scenes/Checkpoint.unity");
            EditorSceneManager.SaveScene(scene, path, true);
            Debug.Log("Saved independent scene copy: " + path);
        }
    }
}
