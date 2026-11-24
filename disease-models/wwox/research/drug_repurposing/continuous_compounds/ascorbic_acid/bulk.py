"""Reproduce the untreated WWOX ascorbate transporter and TET transcript contrasts."""
from pathlib import Path
import sys
repo, files, out = map(Path, sys.argv[1:])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine"))
from screen import run
run(files,target_genes=["Slc23a2","Tet1","Tet2","Tet3"],output=out,missing_value="NA")
