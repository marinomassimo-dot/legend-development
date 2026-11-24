"""Run from the root of the SCI_CODEX checkout, writing all outputs alongside this file."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd() / 'disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine'))
import screen
import cell_types

out = Path(__file__).resolve().parent
genes = 'Kcnq2 Kcnq3 Kcnq5 Slc16a1 Slc16a7 Bdh1 Oxct1 Acat1'.split()
files = Path(sys.argv[1])
screen.run(files, genes, out / 'bulk.tsv')
cell_types.run(files, genes, out)
