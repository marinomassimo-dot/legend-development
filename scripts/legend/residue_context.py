#!/usr/bin/env python3
"""Compatibility entrypoint for the public structural-context analyser.

The implementation moved into the disease-model layer during the public
restructure.  Keeping this thin entrypoint preserves commands cited by the
canonical scientific record and by older automation.
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
    / "residue_context.py"
)


def main() -> int:
    if not TARGET.is_file():
        print(f"ERROR: structural analyser not found: {TARGET}", file=sys.stderr)
        return 1
    sys.argv[0] = str(TARGET)
    runpy.run_path(str(TARGET), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
