"""Reproduce the untreated WWOX channel transcript contrasts."""
from pathlib import Path
import sys
repo, files, out = map(Path, sys.argv[1:])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine"))
from screen import run
run(files,target_genes=["Cacna1h","Cacna1g","Cacna1i","Scn1a","Scn2a","Scn3a","Scn8a"],output=out,missing_value="NA")
