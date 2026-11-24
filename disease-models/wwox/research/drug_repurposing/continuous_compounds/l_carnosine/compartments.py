"""Measure CARNS1 and both glyoxalase steps in assigned hippocampal nuclear classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run

run(Path(sys.argv[1]), genes=['Carns1', 'Glo1', 'Hagh'], output_dir=Path(sys.argv[2]))
