"""Recompute WWOX expression of receptor, editing, chloride and fuel markers."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "thiamine"))
from screen import run

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("inputs", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
genes = "Gabra1 Gabra3 Gabrb3 Gabrg2 Gabrd Adar Adarb1 Slc12a2 Slc12a5 Ldha Ldhb".split()
run(args.inputs, target_genes=genes, output=args.output, missing_value="NA")
