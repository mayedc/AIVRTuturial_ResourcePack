# Asset licenses

Date: 2026-11-04. This table covers files intended for the public repository. Unity package caches under `Library` are downloaded by the Editor and are not committed.

| Asset | Author | Source | License | Redistribution | Required attribution |
|---|---|---|---|---|---|
| `SourceArt/Blender/*.blend`, `SourceArt/FBX/*.fbx`, unpacked meshes in `Assets/AI_VR_Workshop_V4` | AI-VR-Driving-Workshop contributors | Original course models. No store purchase and no extracted game asset was identified. | MIT, root `LICENSE` | Allowed with the copyright notice | Keep `LICENSE` |
| Materials on those models | Same | Flat colors and simple metal or emission values. No external texture or HDRI file is in `Assets`. | MIT | Allowed | Keep `LICENSE` |
| `WorkshopGlass.shader`, `WorkshopSurface.shader` | Same | Course shaders. Current scene materials use URP Lit and URP Unlit. | MIT | Allowed | Keep `LICENSE` |
| Runtime and editor scripts under `Assets/AI_VR_Workshop_V4` | Same | Course code, including `WorkshopDrive`, `WorkshopSpeedControl`, `WorkshopRobotWalk`, `WorkshopDesktopPanel` | MIT | Allowed | Keep `LICENSE` |
| `Docs`, `Prompts`, `.cursor/skills`, `Tools` course scripts | Same | Written for this course | MIT | Allowed | Keep `LICENSE` |
| Robot gait used in Play Mode | Same | `WorkshopRobotWalk` poses rigid armor. The FBX also contains `Noma_Walk_InPlace_1s`. It is not a Mixamo clip. | MIT | Allowed | Keep `LICENSE` |
| `Packages/manifest.json` dependencies from Unity registry | Unity Technologies | Not vendored. Users restore them with the Editor. | Unity package terms, not this MIT license | The manifest may point at them. Do not commit `Library/PackageCache`. | Unity product notices stay with those packages |
| `com.coplaydev.unity-mcp` | CoplayDev | Git dependency. Public GitHub license reported as MIT. Source is not copied into this repository. | Upstream MIT | Reference only. Do not vendor the package into `Assets`. | Upstream copyright if a copy is redistributed |
| `com.unity.pipeline` | Unity Technologies | Registry package used to validate this candidate. Not vendored. | Unity package terms | Reference only | Unity |
| Meta XR Core prefab GUID `126d619cf4daa52469682f85c1378b4a` | Meta | Not present | Not included | Do not add the prefab bytes unless the Meta license is reviewed for that exact package | Not applicable while absent |
| Fonts, audio, photographs, PSD, video | None in the release tree | No `.png`, `.jpg`, `.wav`, `.mp3`, `.ogg`, `.ttf`, `.otf`, `.psd`, or `.mp4` under `Assets` or `SourceArt` | None | Nothing to publish | None |
| Blender application and add-ons | Blender Foundation and add-on authors | Not shipped. FBX header records Blender 5.2.2 LTS exporter. | Blender is GPL; that license is not applied to these original course models by this package | Do not commit Blender itself or unknown add-ons | Not included |

## Excluded from publication

Historical workshop copies, student work, screenshots with embedded local paths, experiment notes, and the previous development project stay outside this folder. They are not given a new license by `LICENSE`.

If a later import adds a third-party model, texture, or font, stop and add a row here before publishing that file. An unclear license is a publication blocker.
