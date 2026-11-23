"""Reproduce the WWOX carnitine gene comparisons in juvenile hippocampal nuclei."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from levocarnitine.screen import GENES
from thiamine.cell_types import run

if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE)
