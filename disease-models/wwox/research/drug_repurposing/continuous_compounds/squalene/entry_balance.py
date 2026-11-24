"""KO minus control difference in within-library log2(SQLE+1) minus log2(FDFT1+1)."""
from pathlib import Path
import sys
import numpy as np
repo, files, output = map(Path, sys.argv[1:])
sys.path.insert(0,str(repo / "disease-models/wwox/research/drug_repurposing/continuous_compounds/creatine"))
from assess import MODELS, load_target, reference, tsv
mapping, _ = reference(files)
rows = []
for model, accession, wt_prefix, ko_prefix in MODELS:
    human = model == "human_organoid"
    genes = ["SQLE","FDFT1"] if human else ["Sqle","Fdft1"]
    source, = (files / "geo" / accession).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz")
    names, expr = load_target(source, genes, None if human else mapping)
    balance = np.log2(1 + expr[genes[0]]) - np.log2(1 + expr[genes[1]])
    wt = [i for i,n in enumerate(names) if n.startswith(wt_prefix)]
    ko = [i for i,n in enumerate(names) if n.startswith(ko_prefix)]
    def contrast(skip=None):
        return balance[[i for i in ko if i != skip]].mean() - balance[[i for i in wt if i != skip]].mean()
    sensitivity = [contrast(i) for i in wt + ko]
    rows.append([model,accession,len(wt),len(ko),contrast(),min(sensitivity),max(sensitivity)])
tsv(output,"model accession wt_n ko_n delta_log2_balance omit_min omit_max".split(),rows)
