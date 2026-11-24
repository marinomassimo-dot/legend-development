"""Measure pyruvate transporter transcripts within assigned hippocampal nuclear classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Slc16a1 Slc16a7 Slc16a3 Mpc1 Mpc2".split(), output_dir=here)
