"""Measure peroxide-handling transcripts within untreated WWOX hippocampal nuclear classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Sepsecs Gpx4 Txnrd1 Acsl4".split(), output_dir=here)
