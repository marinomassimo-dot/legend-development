"""Profile lysine import, charging, stress sensing and catabolism using the shared GEO screen."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "thiamine"))
from screen import run

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("inputs", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
genes = "Slc7a1 Slc7a2 Slc7a3 Slc7a6 Slc7a7 Kars Aass Aldh7a1 Eif2ak4 Atf4 Asns".split()
run(args.inputs, target_genes=genes, output=args.output, missing_value="NA")
