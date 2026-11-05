#!/usr/bin/env python3
"""Dependency-free repository checks for Plan B; run from repository root.
This cannot compile Unity C# or test a headset. Only structural/source checks.
"""
from pathlib import Path
import json
import re
import sys
import ast

ROOT = Path(__file__).resolve().parents[2]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

required = [
    "README.md", "AGENTS.md", ".gitignore",
    "UnitySource/Config/WorkshopSceneSpec.json",
    "UnitySource/Editor/WorkshopSceneBuilder.cs",
    "UnitySource/Editor/WorkshopSceneValidator.cs",
    "UnitySource/Runtime/Starter/WorkshopDrive.cs",
    "UnitySource/Runtime/Starter/WorkshopSpeedControl.cs",
    "UnitySource/Runtime/Starter/WorkshopRobotWalk.cs",
    "UnitySource/Runtime/Starter/WorkshopDesktopPanel.cs",
    "Answers/Reference/WorkshopDrive.cs",
    "Answers/Reference/WorkshopSpeedControl.cs",
]
prompts = [
    "00_Clone_Preflight", "00_Install_Update_MCP", "01_1_Review_All_Blender_Models",
    "01_2_Choose_Car_Color", "01_3_Export_And_Build_Unity",
    "01_4_Speed_And_Gap_Flight", "02_1_XR_Setup_And_Device_Check",
    "02_2_Attach_Driver_Camera_And_Test",
]
required += [f"Prompts/{name}.md" for name in prompts]
for name in ("AsterGT", "NomaRobot", "MeridianCity", "JetFX",
             "Road_Straight12", "Road_Crosswalk12", "Road_Gap12"):
    required += [f"SourceArt/Blender/{name}.blend", f"SourceArt/FBX/{name}.fbx"]
required.append("SourceArt/Blender/Workshop_Master.blend")
for name in required:
    p = ROOT / name
    check(p.is_file() and p.stat().st_size > 0, f"Required file missing or empty: {name}")

check(not (ROOT / "Assets/AI_VR_Workshop_V4").exists(), "Plan B must not contain the old ready-made Unity asset pack.")

spec_path = ROOT / "UnitySource/Config/WorkshopSceneSpec.json"
if spec_path.exists():
    try:
        s = json.loads(spec_path.read_text(encoding="utf-8"))
        check(s.get("schemaVersion") == 1, "Scene spec schemaVersion must equal 1.")
        check(s.get("studentScenePath") == "Assets/WorkshopStudentGenerated/Scenes/Workshop_Desktop_Student.unity",
              "Unexpected student scene output path.")
        check(s.get("importDirectory") == "Assets/WorkshopStudentGenerated/Imported", "Unexpected import path.")
        check(s.get("roadGapStartZ") == 37 and s.get("roadGapEndZ") == 43, "Road gap must remain 37–43m.")
        check(s.get("gapHoldZ") == 32 and s.get("routeEndZ") == 58, "Route hold/end changed unexpectedly.")
        check(s.get("driverEyeLocal") == [-0.44, 1.24, -0.12], "DriverEyeAnchor baseline changed.")
        check(s.get("expectedCarBounds") == [2.41, 1.61, 5.14], "Car bounds baseline changed.")
    except (ValueError, UnicodeError) as e:
        errors.append(f"Invalid scene spec JSON: {e}")

# Relative markdown link check across all tracked-like Markdown (including docs and prompts).
markdown_files = list(ROOT.rglob("*.md"))
for md in markdown_files:
    if ".git" in md.parts or "StudentWork" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", text):
        url = link.strip().split("#", 1)[0].split("?", 1)[0]
        if not url or url.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        if not (md.parent / url).exists():
            errors.append(f"Broken Markdown link: {md.relative_to(ROOT)} -> {link}")

# Syntax-parse repository-owned Python without importing bpy or launching Unity.
for python_source in (ROOT / "Tools").rglob("*.py"):
    try:
        ast.parse(python_source.read_text(encoding="utf-8"), filename=str(python_source))
    except (SyntaxError, UnicodeError) as err:
        errors.append(f"Invalid Python source: {python_source.relative_to(ROOT)}: {err}")

# Stage gates and trusted code copies.
p13 = (ROOT / "Prompts/01_3_Export_And_Build_Unity.md").read_text(encoding="utf-8") if (ROOT / "Prompts/01_3_Export_And_Build_Unity.md").exists() else ""
p14 = (ROOT / "Prompts/01_4_Speed_And_Gap_Flight.md").read_text(encoding="utf-8") if (ROOT / "Prompts/01_4_Speed_And_Gap_Flight.md").exists() else ""
build = (ROOT / "UnitySource/Editor/WorkshopSceneBuilder.cs").read_text(encoding="utf-8") if (ROOT / "UnitySource/Editor/WorkshopSceneBuilder.cs").exists() else ""
check("WorkshopSceneBuilder" in p13 and "student" in p13.lower(), "1.3 must invoke source-built editor builder.")
check("StudentWork" in p13 and "NomaRobot.fbx" in p13, "1.3 must import student car and source FBXs.")
check("Workshop_Desktop_Student.unity" in p13, "1.3 must save separate student scene.")
check("only after" in p14.lower() and "BeginJetFlight" in p14, "1.4 stage gate or flight is missing.")
check("AssetDatabase.LoadAssetAtPath<SceneAsset>(spec.studentScenePath)" in build and
      "Build was skipped" in build, "Builder must reject overwriting an existing scene.")
check("PrefabUtility.InstantiatePrefab" in build, "Builder must instantiate source FBX models.")
validator = (ROOT / "UnitySource/Editor/WorkshopSceneValidator.cs").read_text(encoding="utf-8")
check("Validate Student Scene (1.4)" in validator, "Missing post-exercise structural validation entry point.")
check("Validate Student Scene (1.4)" in p14, "1.4 must invoke the correct post-exercise validator.")
for suffix in ("WorkshopDrive", "WorkshopSpeedControl"):
    ref = ROOT / f"Answers/Reference/{suffix}.cs"
    start = ROOT / f"UnitySource/Runtime/Starter/{suffix}.cs"
    if ref.exists() and start.exists():
        check("namespace AIVRWorkshop.Student" in ref.read_text(encoding="utf-8"),
              f"Reference namespace mismatch: {suffix}")
        check("namespace AIVRWorkshop.Student" in start.read_text(encoding="utf-8"),
              f"Starter namespace mismatch: {suffix}")

# Report no physical Unity/Quest pass from these checks.
print(f"Source-first static check: {len(required)} required files, {len(markdown_files)} Markdown files")
if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)
print("PASS: repository structure, scene spec, links and stage guards.")
print("NOT TESTED: live Unity C# compilation, imported FBX orientation, Unity Play and Quest headset.")
