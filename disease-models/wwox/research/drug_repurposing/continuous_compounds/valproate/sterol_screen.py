"""Reproduce the WWOX bulk expression screen for the distal cholesterol pathway."""
from pathlib import Path
import sys
repo, files, output = map(Path, sys.argv[1:4])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine"))
from screen import run
genes = "Hmgcr Fdft1 Sqle Lss Dhcr24 Dhcr7".split()
run(files, target_genes=genes, output=output, missing_value="NA")
