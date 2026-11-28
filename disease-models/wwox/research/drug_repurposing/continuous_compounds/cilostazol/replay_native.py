"""Reproduce WWOX gene-level context for PDE3 signaling and oligodendrocyte lineage."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = tuple("Pde3a Pde3b Prkaca Prkacb Creb1 Pdgfra Olig2 Sox10 Tcf7l2 Myrf Mbp Plp1 Mog Cnp".split())

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
