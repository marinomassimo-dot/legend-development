#!/usr/bin/env python3
"""Compatibility entrypoint for the public KFERQ geometry analyser.

The implementation lives with the WWOX analysis package. This thin launcher
preserves commands cited by the cumulative discovery record without
duplicating scientific logic.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


TARGET = (
    Path(__file__).resolve().parents[2]
    / "disease-models"
    / "wwox"
    / "analysis"
    / "scripts"
    / "kferq_geometry.py"
)


def main() -> int:
    if not TARGET.is_file():
        print(f"ERROR: KFERQ geometry analyser not found: {TARGET}", file=sys.stderr)
        return 1
    sys.argv[0] = str(TARGET)
    runpy.run_path(str(TARGET), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
