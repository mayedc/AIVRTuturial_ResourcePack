# Compatibility matrix

Verified on 2026-11-04 against the release candidate. Versions come from `ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json`, and `Packages/packages-lock.json`.

| Area | Required | Observed | Status |
|---|---|---|---|
| Unity Editor | 6000.3.27f2 | 6000.3.27f2 (22188f149405) | PASS |
| Operating system used for this validation | Windows | Windows desktop Editor, StandaloneWindows64 active target | PASS for this machine |
| Render pipeline | URP | `com.unity.render-pipelines.universal` 17.3.0, `Assets/Settings/PC_RPAsset.asset` | PASS |
| Input | Input System package | 1.20.1, Active Input Handling = Input System Package | PASS |
| XR management | OpenXR loader | `com.unity.xr.management` 4.7.0, `com.unity.xr.openxr` 1.16.1, loader assigned for Standalone and Android | PASS |
| Meta Quest OpenXR feature | Quest 3 selected | Android Meta Quest Support enabled, Quest 3 and Quest 3S enabled | PASS as project settings |
| Meta XR Core (`com.meta.xr.sdk.core`) | Not shipped | Prefab GUID `126d619cf4daa52469682f85c1378b4a` unresolved | NOT INCLUDED |
| Android build support | Player module for a later device build | Android target supported in this Editor. Min SDK 32. ARM64. IL2CPP. | PASS for module presence. No APK built. |
| Test framework | Package present | `com.unity.test-framework` 1.6.0 | PASS |
| Agent pipeline | Used for validation | `com.unity.pipeline` 0.9.1-exp.1 | PASS on this machine |
| Unity MCP package | In the manifest | `com.coplaydev.unity-mcp` git URL, lock commit `81542a7e86292b5c4c21b1782c5af23b567f45ce` | Present. Live MCP session was not part of this Play Mode test. |
| Blender | Source files are included | `.blend` files under `SourceArt/Blender/`. Blender was not launched in this phase. | NOT VERIFIED as an application run |
| Meta Quest 3 headset | Optional hardware | No device test | NOT VERIFIED |
| Desktop Play Mode | Workshop desktop scene | See `SceneTestResults.md` | PASS |

## Identifiers left as copied

`ProjectSettings/ProjectSettings.asset` still uses product name `AI_VR_Driving`, company `DefaultCompany`, Android application id `com.aivrdriving.workshop`, and the URP template Standalone application id `com.Unity-Technologies.com.unity.template.urp-blank`. Those values were already in the approved copy. They are not personal machine data. They were not rewritten during validation.

## Not claimed

- Quest 3 runtime, tracking quality, comfort, or frame time.
- A standalone APK or App Lab / store submission.
- macOS or Linux Editor runs.
- Blender MCP connected during this phase.
