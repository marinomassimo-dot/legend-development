"""Measure Pgk1 and Park7 RNA with LEGEND's existing assigned-nuclei analysis."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "thiamine"))
from cell_types import run


run(Path(sys.argv[1]), genes=["Pgk1", "Park7"], output_dir=Path(sys.argv[2]))
