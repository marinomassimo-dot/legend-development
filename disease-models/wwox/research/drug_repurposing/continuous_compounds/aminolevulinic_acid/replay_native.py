"""Replay the heme and iron pathway in the established WWOX RNA sources."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = ("Alas1", "Alad", "Hmbs", "Uros", "Urod", "Cpox", "Ppox", "Fech", "Flvcr1",
           "Slc15a2", "Slc15a1", "Slc25a37", "Slc25a28", "Hmox1", "Hmox2", "Cox10",
           "Cox15", "Abcg2", "Abcb6", "Alas2", "Gypa")

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
