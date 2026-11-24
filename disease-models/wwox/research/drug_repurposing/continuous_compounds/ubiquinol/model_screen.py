"""Reproduce the WWOX CoQ pathway comparison from held expression matrices."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run
from cell_types import run as compare_cell_types

GENES = "Coq2 Coq4 Coq7 Coq9 Aifm2 Gpx4 Nqo1".split()

if __name__ == "__main__":
    directory = Path(sys.argv[2])
    files = Path(sys.argv[1])
    run(files, GENES, directory / "bulk.tsv")
    compare_cell_types(files, GENES, directory)
