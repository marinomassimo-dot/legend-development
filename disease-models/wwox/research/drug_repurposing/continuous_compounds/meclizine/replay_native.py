"""Reproduce gene-level context for phosphoethanolamine handling across WWOX datasets."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Etnk1", "Etnk2", "Pcyt2", "Etnppl", "Selenoi", "Cept1", "Pisd", "Ptdss1", "Ptdss2")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
