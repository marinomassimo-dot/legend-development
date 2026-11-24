"""Measure vesicular zinc and inhibitory receptor transcripts in WWOX hippocampal nuclei."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Slc30a3 Gabrg2 Gabrd Sv2a".split(), output_dir=here)
