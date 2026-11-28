"""Reuse LEGEND's classification to check uptake and target transcripts by cell class."""
from pathlib import Path
import sys

repo, files, out = map(Path, sys.argv[1:])
sys.path.insert(0, str(repo / "disease-models/wwox/research/drug_repurposing"
                       / "continuous_compounds/thiamine"))
from cell_types import run

genes = ["Slc5a8", "Slc16a1", "Slc16a3", "Slc16a7", "Dlat", "Pdk2", "Pdk3", "Pdk4"]
run(files, genes=genes, output_dir=out)
