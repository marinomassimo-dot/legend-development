#!/usr/bin/env python3
"""IT9 P4c-e: derived tables from the committed raw files of this folder (offline, deterministic).
  tables_p4c_e.py --help | build
Reads expression_hpa_raw.tsv; writes expression_hpa_summary_E.tsv (one row per gene: bulk-tissue RNA class, single-cell nCPM for the brain cell types, single-nuclei brain class,
protein class; values as published by the Human Protein Atlas on the run date, adult tissue; a field that is null in the HPA answer is written NULL, never zero)."""
import csv, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
if len(sys.argv) < 2 or sys.argv[1] != "build":
    print(__doc__); sys.exit(0)
rows = {}
for r in csv.reader(open(HERE / "expression_hpa_raw.tsv"), delimiter="\t"):
    if len(r) < 4 or r[0] == "gene": continue
    rows.setdefault(r[0], {})[r[2]] = r[3]
def js(v):
    try: return json.loads(v)
    except Exception: return v
BR = ["Astrocytes", "Brain excitatory neurons", "Brain inhibitory neurons", "Oligodendrocyte progenitor cells", "Oligodendrocytes", "Other brain neurons", "Microglial cells"]
out = [["gene", "rna_tissue_specificity", "rna_tissue_distribution", "sc_type_specificity"] + ["nCPM_" + b.replace(" ", "_") for b in BR] + ["single_nuclei_brain_specificity", "single_nuclei_brain_distribution", "brain_regional_specificity", "protein_cell_type_distribution"]]
for g in sorted(rows):
    d = rows[g]; sc = js(d.get("RNA single cell type specific nCPM", "null")); sc = sc if isinstance(sc, dict) else {}
    f = lambda k: (js(d.get(k, "null")) if js(d.get(k, "null")) is not None else "NULL")
    out.append([g, f("RNA tissue specificity"), f("RNA tissue distribution"), f("RNA single cell type specificity")] + [sc.get(b, "NULL") for b in BR] +
               [f("RNA single nuclei brain specificity"), f("RNA single nuclei brain distribution"), f("RNA brain regional specificity"), f("Protein cell type distribution")])
with open(HERE / "expression_hpa_summary_E.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerows(out)
print(len(out) - 1, "genes")
