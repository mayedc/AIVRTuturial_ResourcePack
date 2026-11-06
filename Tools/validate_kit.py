#!/usr/bin/env python3
"""Compatibility entrypoint for the old validation command.
No legacy historical prebuilt Unity asset folder scenes or PyYAML are required.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent / "Validation" / "validate_source_first.py"), run_name="__main__")
