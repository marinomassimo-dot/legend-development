"""Reproduce the neuronal cell-class check from pooled WWOX hippocampal nuclei."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Nmnat2 Sarm1 Nampt Nmrk1 Parp1".split(), output_dir=Path(sys.argv[2]))
