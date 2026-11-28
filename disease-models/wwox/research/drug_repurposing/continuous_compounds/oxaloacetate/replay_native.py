"""Replay gene-level WWOX context for glutamate transport and oxaloacetate metabolism."""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = (
    "Got1", "Got2", "Mdh1", "Mdh2", "Slc1a1", "Slc1a2", "Slc1a3",
    "Slc13a3", "Slc25a11", "Slc25a12", "Slc25a13", "Cldn5",
)

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
