"""Reproduce the WWOX folate transport and compartment-marker comparison."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run as compare_bulk

GENES = "Folr1 Slc46a1 Slc19a1 Mthfs Ttr Aqp1 Otx2".split()

if __name__ == "__main__":
    compare_bulk(Path(sys.argv[1]), GENES, Path(sys.argv[2]), missing_value="NA")
