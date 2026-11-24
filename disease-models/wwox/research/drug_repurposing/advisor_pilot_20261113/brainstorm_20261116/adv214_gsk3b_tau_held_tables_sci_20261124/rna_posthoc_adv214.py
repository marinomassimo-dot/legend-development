"""ADV-214 POST HOC (not in the PREREG): bulk RNA direction of the frozen genes in the three held bulk tables, so the RNA-ONLY classification is not mute.
Usage: python3 -I rna_posthoc_adv214.py REPO FILES OUT_TSV"""
import sys
from pathlib import Path
repo, files, out = map(Path, sys.argv[1:4])
sys.path.insert(0, str(repo / "disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine"))
from screen import run
genes = "Gsk3b Gsk3a Mapt Ppp2ca Akt1 Akt2 Akt3 Mapk8 Mapk9 Mapk10 Dyrk1a Cdk5 Cdk5r1 Map2k1 Mapk1 Mapk3 Dpysl2 Axin1 Axin2 Ctnnb1".split()
run(files, target_genes=genes, output=out, missing_value="NA")
