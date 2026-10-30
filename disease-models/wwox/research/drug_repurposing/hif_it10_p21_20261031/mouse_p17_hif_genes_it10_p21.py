#!/usr/bin/env python3
import sys as _s
if len(_s.argv) > 1 and _s.argv[1] in ("-h", "--help"):
    print("IT10 P2.1 research script; reads inputs named in README.md of this folder; no options. Run with python3 -I from this folder.")
    raise SystemExit(0)
"""IT10 P2.1, premise (a), mouse neural data: are HIF-axis and glycolysis transcripts different in Wwox-deleted mouse brain (P17)?
Inputs (public, key-less, sha256-pinned; same files as mouse_wwox_p17_it6_p4_20261029/inputs/SHA256SUMS), placed in ONE directory:
  GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz  GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz  Mus_musculus.GRCm38.cdna.all.fa.gz (Ensembl 92)
Usage: python3 -I mouse_p17_hif_genes_it10_p21.py <input_dir>     Transcript TPM only; no protein, no lactate, no flux."""
import csv, gzip, hashlib, math, re, statistics, sys
from pathlib import Path
D = Path(sys.argv[1]); HERE = Path(__file__).resolve().parent
PIN = {"GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz": "52ff4f078fc3d7600dceb716ddb26bbb2c6bb4134736a388a39d10915399e483",
       "GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz": "77aecf5cdd194ad638e2e7c5886e04f2583d6c425c6dea22ed3b131be2e8060f",
       "Mus_musculus.GRCm38.cdna.all.fa.gz": "7d2fcb0cbe069c08eff61a77a056f76baadad5f112dcc4e9dd7888832084e3e7"}
for f, h in PIN.items():
    assert hashlib.sha256((D / f).read_bytes()).hexdigest() == h, f
GENES = ["Wwox", "Hif1a", "Epas1", "Arnt", "Egln1", "Egln3", "Hk1", "Hk2", "Slc2a1", "Slc2a3", "Ldha", "Ldhb", "Pdk1", "Bnip3", "Vegfa", "Bhlhe40", "Adm", "P4ha1", "Ndrg1", "Pgk1", "Gfap", "Aqp4"]
t2g = {}
with gzip.open(D / "Mus_musculus.GRCm38.cdna.all.fa.gz", "rt") as h:
    for l in h:
        if l[0] == ">":
            tid = l[1:].split()[0]; m = re.search(r"gene_symbol:(\S+)", l)
            if m: t2g[tid.split(".")[0]] = m.group(1)
CONTR = [("H_S_neuron-targeted", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"]),
         ("H_N_progenitor-targeted", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"]),
         ("H_germline_null", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"]),
         ("Cortex_S_neuron-targeted", "GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"])]
rows = [["contrast", "gene", "mean_TPM_KO", "mean_TPM_ctl", "log2_KO_over_ctl_(+0.1)", "animal_separated", "TPM_KO_animals", "TPM_ctl_animals"]]
cache = {}
for name, f, kon, ctn in CONTR:
    if f not in cache:
        tab = {}
        with gzip.open(D / f, "rt") as h:
            r = csv.reader(h, delimiter="\t"); hdr = next(r)
            for x in r:
                g = t2g.get(x[0].split(".")[0])
                if g in GENES:
                    a = tab.setdefault(g, [0.0] * (len(hdr) - 3))
                    for i, v in enumerate(x[3:]): a[i] += float(v)
        cache[f] = (hdr[3:], tab)
    cols, tab = cache[f]
    for g in GENES:
        if g not in tab: rows.append([name, g, "NA", "NA", "NA", "NA", "gene not found in key", ""]); continue
        k = [tab[g][cols.index(c)] for c in kon]; c_ = [tab[g][cols.index(c)] for c in ctn]
        mk, mc_ = statistics.fmean(k), statistics.fmean(c_)
        rows.append([name, g, f"{mk:.2f}", f"{mc_:.2f}", f"{math.log2((mk+0.1)/(mc_+0.1)):+.2f}", "yes" if (min(k) > max(c_) or max(k) < min(c_)) else "no",
                     ";".join(f"{v:.2f}" for v in k), ";".join(f"{v:.2f}" for v in c_)])
with (HERE / "mouse_p17_hif_genes_it10_p21.tsv").open("w", newline="") as h: csv.writer(h, delimiter="\t").writerows(rows)
for r in rows: print("\t".join(r[:6]))
