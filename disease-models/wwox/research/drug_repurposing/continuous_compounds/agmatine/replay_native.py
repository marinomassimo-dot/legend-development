"""Reproduce WWOX gene-level context for agmatine metabolism, NOS and NMDAR subunits."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cannabidivarin"))
from replay_trp_expression import compare_expression

TARGETS = tuple("Agmat Nos1 Nos2 Nos3 Grin1 Grin2a Grin2b Grin2c Grin2d Slc7a1 Slc7a2 Odc1 Srm Sms".split())

if __name__ == "__main__":
    _, files, output = sys.argv
    compare_expression(HERE.parents[1], Path(files), Path(output), TARGETS, "native_bulk.tsv")
