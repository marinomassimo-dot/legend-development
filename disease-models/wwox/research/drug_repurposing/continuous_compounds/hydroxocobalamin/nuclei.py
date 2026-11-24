"""Measure cobalamin-branch transcripts within the established WWOX nuclear classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Mtr Mtrr Mmaa Mut".split(), output_dir=here)
