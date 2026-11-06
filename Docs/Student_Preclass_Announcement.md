# Course Announcement — Prepare Your Windows Laptop Before Class

**Course:** AI-Assisted VR Driving Scene Workshop (Cursor + Blender + Unity)

**Please bring your own Windows laptop, charger and mouse to every workshop session.** Install and test the following software **before the first class**, while you have reliable internet. You will create your own Unity project during class; **the GitHub resource pack is not itself a Unity project**. Do not import the repository folder directly in Unity Hub.

## Required on every student's Windows development laptop

| Tool | Classroom recommendation | Install / verify |
|---|---|---|
| Cursor | Current stable Windows release; **active Cursor Pro subscription as required by this course** | https://cursor.com/downloads — sign in, check your Pro plan and Agent/terminal access |
| Unity Hub | Current official **international/Global** Unity Hub | https://unity.com/download — sign in with a valid Unity account and license |
| Unity Editor | **Unity 6.3 LTS 6000.3.27f2** (the repository's previously observed and security-patched baseline); a later 6000.3 LTS patch only after checking MCP and package compatibility | Install through Unity Hub; include **Microsoft Visual Studio** if offered, **Windows Build Support (IL2CPP)** if building standalone Windows applications. This lesson's wired PCVR Play does not require an Android build |
| Blender | **Blender 5.2.2 LTS** baseline; 5.2.3 LTS is available but must be checked with this course's .blend files and Blender MCP | https://www.blender.org/download/ |
| Git for Windows | Current stable 64-bit | https://git-scm.com/install/windows — verify `git --version` in Cursor terminal |
| Python | Python 3.11 (compatible with repository's Python 3.10+ minimum) | https://www.python.org/downloads/windows/ — verify `py -3.11 --version`; avoid mixing store/venv installations |
| uv / uvx | Current stable (MCP process launcher) | https://docs.astral.sh/uv/getting-started/installation/ — verify `uv --version` and `uvx --version` |
| Meta Horizon Link / Quest Link PC app | Current compatible official Windows application | https://developers.meta.com/vr/documentation/unity/unity-link/ — sign in and perform the cable/device check if you will use a Quest headset |
| Graphics drivers | Stable Windows drivers from the GPU manufacturer | Update if VR compatibility or Unity/Blender rendering fails; confirm discrete GPU and adequate disk space |

**Unity international edition:** Please use the official international Unity Hub/Editor, **not Unity China/Tuanjie Engine**. Official Unity download is preferred. The optional community version-search reference https://github.com/DanKE123abc/NoUnityCN is **not an official Unity installer, license source or endorsement**; use only if appropriate under your location's license/availability terms, and get binaries from Unity's official download infrastructure.

**Course compatibility:** This repository is source-first; do **not** install a historical Unity `Packages/manifest.json` from past lesson reports. Start a separate **blank Universal 3D (URP)** project with the selected Unity Editor. The live installer prompt will check and install compatible **CoplayDev Unity MCP** and **ahujasid Blender MCP** packages. Avoid guessing MCP transport addresses or installing several competing copies.

## VR headset requirements (Lesson 3)

The wired **Windows PCVR** exercise is intended for **Quest 2, Quest 3 and Quest 3S**, subject to the particular PC's GPU, Meta Link app and USB-C **data** cable. Quest 2 is an explicit support target, **not yet physically verified by this repository**. Students without headsets can complete the desktop Blender and Unity lessons; actual headset acceptance must be marked NOT TESTED until performed with hardware.

For headset participants, charge your headset and controllers, bring the headset and compatible USB-C **data** cable (not a charging-only cable), install Meta Horizon Link and confirm you can **enter the Link environment in the headset**. Check that the Meta app has selected its PC OpenXR runtime when running the Windows Link workflow. **Do not use Android-only OpenXR settings as a substitute for Standalone OpenXR.** Do not enable both Meta and unrelated XR camera rigs simultaneously.

## Before the first class — quick self-check

1. Open Cursor, confirm you are signed in to the required **Pro** plan, and check that Agent can use the integrated terminal (with your approval).
2. Open Unity Hub and create/open a **separate blank URP project**. Confirm the Editor launches without compile errors. Record the **exact Editor version**.
3. Launch Blender and confirm its version; don't edit any original course model yet.
4. In the Cursor Windows terminal, run `git --version`, `py -3.11 --version`, `uv --version`, and `uvx --version`. Fix PATH/install issues before class.
5. Confirm internet access to GitHub, Unity Package Manager, and Python package servers. Keep **at least 30 GB** free as a practical preparation allowance; more may be required by Unity modules.
6. If using VR, open Meta Horizon Link, connect the Quest through a **data** cable, launch Link from the headset, and verify tracking. Do not claim successful testing from charging alone.
7. Have your own Windows laptop, charger, mouse and login details ready. Never post account passwords, access tokens, device serials or machine-specific paths to the public repository.

**Course repository:** https://github.com/mayedc/AIVRTuturial_ResourcePack

**At the start of class:** Open a new empty folder in Cursor and follow `Prompts/00_Clone_Preflight.md`; then `Prompts/00_Install_Update_MCP.md`. The first-stage prompts guide the remaining setup. You do not need to build the full driving scene before class.

**Support:** If something fails, bring a screenshot of the error and its software version to class, with personal information removed. Please do not replace your working environment with experimental updates immediately before the workshop.
