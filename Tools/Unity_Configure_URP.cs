using AIVRWorkshop.V4;
using UnityEditor.SceneManagement;
var root="Assets/AI_VR_Workshop_V4";
foreach(var g in AssetDatabase.FindAssets("t:Material",new[]{root+"/Materials"})) {
 var m=AssetDatabase.LoadAssetAtPath<Material>(AssetDatabase.GUIDToAssetPath(g));
 var color=m.GetColor("_Color");var emission=m.HasProperty("_Emission")?m.GetFloat("_Emission"):0;var metal=m.HasProperty("_Metallic")?m.GetFloat("_Metallic"):0;
 var transparent=m.name=="M_Glass"||m.name=="M_Curtain";
 m.shader=Shader.Find(transparent?"Universal Render Pipeline/Unlit":"Universal Render Pipeline/Lit");
 m.SetColor("_BaseColor",color);m.SetColor("_Color",color);
 if(transparent){m.SetFloat("_Surface",1);m.SetFloat("_Blend",0);m.SetFloat("_SrcBlend",5);m.SetFloat("_DstBlend",10);m.SetFloat("_ZWrite",0);m.SetFloat("_Cull",0);m.EnableKeyword("_SURFACE_TYPE_TRANSPARENT");m.SetOverrideTag("RenderType","Transparent");m.renderQueue=m.name=="M_Curtain"?3999:3000;}
 else {m.SetFloat("_Metallic",metal);m.SetFloat("_Smoothness",.35f);if(emission>0){m.EnableKeyword("_EMISSION");m.SetColor("_EmissionColor",color*emission);}}
 EditorUtility.SetDirty(m);
}
var sun=GameObject.Find("Workshop_Daylight")?.GetComponent<Light>() ?? new GameObject("Workshop_Daylight").AddComponent<Light>();sun.type=LightType.Directional;sun.intensity=1.4f;sun.transform.rotation=Quaternion.Euler(40,-30,0);sun.shadows=LightShadows.Soft;
RenderSettings.ambientMode=UnityEngine.Rendering.AmbientMode.Flat;RenderSettings.ambientLight=new Color(.42f,.48f,.55f);
var curtain=GameObject.Find("ComfortCurtain").GetComponent<Renderer>();curtain.enabled=false;
AssetDatabase.SaveAssets();EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene());
return "URP materials normalized and independent scene saved";
