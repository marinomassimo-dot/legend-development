"""Re-use the native WWOX expression comparisons for the two target classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

if __name__ == "__main__":
    _, files, output = sys.argv
    targets = ("Sv2a", "Sv2b", "Sv2c", "Gabra1", "Gabra2", "Gabra3", "Gabra5",
               "Gabrg2", "Slc12a5", "Slc12a2")
    compare_expression(here.parents[1], Path(files), Path(output), targets, "native_bulk.tsv")
