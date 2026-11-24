"""Reproduce the acetate-pathway screen from the archived WWOX GEO inputs."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run
from cell_types import run as run_cell_types

GENES = ["Nat8l", "Aspa", "Acss2", "Acss1", "Mbp"]

if __name__ == "__main__":
    files, output = map(Path, sys.argv[1:])
    run(files, GENES, output / "bulk.tsv")
    run_cell_types(files, GENES, output)
