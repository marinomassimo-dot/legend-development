"""Sensitivity of the bulk transporter-to-inhibitory-marker contrast to its denominator."""
from pathlib import Path
import sys
import numpy as np

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "creatine"))
from assess import MODELS, load_target, reference, tsv

files, output = map(Path, sys.argv[1:3])
gene_map, _ = reference(files)
rows = []
for model, accession, wt_prefix, ko_prefix in MODELS:
    human = model == "human_organoid"
    genes = ["Slc6a1", "Gad1", "Slc32a1"]
    if human:
        genes = [gene.upper() for gene in genes]
    pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
    source, = (files / "geo" / accession).glob(pattern)
    names, values = load_target(source, genes, None if human else gene_map)
    wt = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
    ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
    for marker in genes[1:]:
        for offset in (0.1, 1, 5):
            balance = np.log2((values[genes[0]] + offset) / (values[marker] + offset))
            def contrast(omit=None):
                control = [i for i in wt if i != omit]
                knockout = [i for i in ko if i != omit]
                return balance[knockout].mean() - balance[control].mean()
            omissions = [contrast(i) for i in wt + ko]
            rows.append([model, accession, marker.upper(), offset, len(wt), len(ko),
                         contrast(), min(omissions), max(omissions)])
tsv(output, "model accession denominator offset wt_n ko_n log2_balance_shift omit_min omit_max".split(), rows)
