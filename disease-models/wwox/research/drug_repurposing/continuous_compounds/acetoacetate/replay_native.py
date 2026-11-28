"""Reproduce WWOX gene-level context for vesicular glutamate transport and ketone metabolism."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = tuple("Slc17a7 Slc17a6 Slc17a8 Slc32a1 Slc16a1 Slc16a7 Slc16a3 Oxct1 Bdh1 Acat1 Slc12a2 Slc12a5 Clcn3 Atp6v1a".split())

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
