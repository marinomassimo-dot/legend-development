"""Replay WWOX gene-level context for glycolytic pyruvate and lactate handling."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Pkm", "Pklr", "Slc2a1", "Slc2a3", "Hk1", "Hk2", "Pfkp", "Gapdh",
           "Eno1", "Eno2", "Ldha", "Ldhb", "Slc16a1", "Slc16a3", "Slc16a7",
           "Mpc1", "Mpc2", "Pdha1", "Pdk1", "Pdk4")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
