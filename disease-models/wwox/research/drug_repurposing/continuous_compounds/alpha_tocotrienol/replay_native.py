"""Replay WWOX expression context for Src signaling and lipid redox."""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = (
    "Src", "Fyn", "Alox15", "Alox12", "Pebp1", "Pla2g4a", "Acsl4",
    "Gpx4", "Slc7a11", "Nqo1", "Aifm2", "Plp1",
)

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
