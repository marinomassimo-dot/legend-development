"""Reproduce WWOX gene-level context for ER-to-mitochondrial calcium coupling."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Sigmar1", "Itpr1", "Itpr2", "Itpr3", "Hspa5", "Vdac1",
           "Mcu", "Micu1", "Micu2", "Slc8b1", "Atp2a2", "Ryr2")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
