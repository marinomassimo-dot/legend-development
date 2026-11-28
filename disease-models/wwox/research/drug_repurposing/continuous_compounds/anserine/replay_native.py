"""Replay descriptive aldehyde and dipeptide handling context in WWOX models."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Gsta4", "Aldh2", "Gclc", "Gclm", "Slc7a11", "Carns1", "Carnmt1", "Cndp1", "Cndp2")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
