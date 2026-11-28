"""Reproduce the contextual receptor and cotransporter expression audit."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Gabra1", "Gabra2", "Gabra3", "Gabra4", "Gabra5", "Gabra6",
           "Gabrb2", "Gabrb3", "Gabrg2", "Gabrd", "Slc12a5", "Slc12a2")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
