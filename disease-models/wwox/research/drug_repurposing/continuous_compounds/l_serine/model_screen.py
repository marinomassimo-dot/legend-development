"""Reproduce the WWOX serine pathway comparison from held expression matrices."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run
from cell_types import run as run_cell_types

GENES = "Phgdh Psat1 Psph Srr Sptlc1 Sptlc2 Sptlc3 Shmt1 Shmt2".split()

if __name__ == "__main__":
    directory = Path(sys.argv[2])
    run(Path(sys.argv[1]), GENES, directory / "bulk.tsv")
    run_cell_types(Path(sys.argv[1]), GENES, directory)
