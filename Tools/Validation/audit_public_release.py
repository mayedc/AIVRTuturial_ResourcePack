#!/usr/bin/env python3
"""Public-release hygiene checks. Run on the checked-out repository before publishing.

This checks tracked content (git ls-files), not ignored Unity caches; Git history
may still contain old material and requires a separate history audit before claiming
historical deletion. The script prints only paths/categories, never matched secrets.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ("Docs/Validation/", "CHANGELOG.md")
TEXT_SUFFIXES = {".md", ".cs", ".py", ".json", ".yml", ".yaml", ".ps1", ".txt", ".xml", ".gitignore", ".editorconfig"}
PATH_PATTERNS = {
    "Windows user directory": re.compile(r"[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/][^\\/\s]+", re.I),
    "macOS home directory": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "Linux home directory": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "Email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "Likely GitHub token": re.compile(r"\b(?:ghp_|gho_|ghu_|ghs_|github_pat_)[A-Za-z0-9_-]{16,}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
}
LEGACY = re.compile(r"\bPlan\s+B\b|\bV4\b|AI_VR_Workshop_V4")
UNTRACKED_LOCAL = re.compile(r"(?:^|/)(?:Library|Temp|Logs|Obj|UserSettings|\.vs|StudentWork)/|(?:^|/)\.cursor/mcp\.json$", re.I)

def main():
    try:
        files = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8").split("\0")
    except (OSError, subprocess.CalledProcessError) as exc:
        print("FAIL: git ls-files unavailable:", type(exc).__name__)
        return 2
    failures = []
    for rel in filter(None, files):
        p = ROOT / rel
        if UNTRACKED_LOCAL.search(rel):
            failures.append((rel, "Tracked machine-local/generated artifact"))
        if not p.is_file() or (p.suffix.lower() not in TEXT_SUFFIXES and p.name not in {"AGENTS.md", "README.md"}):
            continue
        try:
            data = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append((rel, "Unreadable text file"))
            continue
        for label, pattern in PATH_PATTERNS.items():
            matches = list(pattern.finditer(data))
            if label == "Email address" and p.suffix == ".py":
                # Blender matrix multiplication uses @ and can resemble an email.
                matches = [m for m in matches if not m.group(0).endswith(("me.corner_normals", "v.co"))]
            if matches:
                failures.append((rel, label))
        if not (rel.startswith(ARCHIVE[0]) or rel == ARCHIVE[1] or rel.startswith("Answers/Original/") or rel == "Docs/00_Production_Plan_and_Source_Review.md" or rel == "Tools/Validation/audit_public_release.py") and LEGACY.search(data):
            # Historical examples in narrative documentation should be reviewed individually,
            # not rewritten blindly where preserving context is instructional.
            failures.append((rel, "Historical development label in active file"))
    for rel, kind in failures:
        print("REVIEW:", kind, "in", rel)
    if failures:
        print("REVIEW REQUIRED:", len(failures), "findings; do not describe public-release privacy as fully passed.")
        return 1
    print("PASS: tracked text checks for machine paths, emails, token patterns and active legacy labels")
    print("NOT TESTED: historical Git objects, image/binary metadata and external student machines")
    return 0

if __name__ == "__main__":
    sys.exit(main())
