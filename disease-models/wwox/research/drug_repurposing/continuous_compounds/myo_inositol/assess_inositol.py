"""Reproduce the WWOX inositol pathway comparisons from held GEO matrices."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run as compare_bulk
from cell_types import run as compare_classes

GENES = "Slc5a3 Isyna1 Impa1 Cdipt Kcnq2 Kcnq3".split()

if __name__ == "__main__":
    files, output = map(Path, sys.argv[1:])
    compare_bulk(files, GENES, output / "bulk.tsv", missing_value="NA")
    compare_classes(files, GENES, output)
