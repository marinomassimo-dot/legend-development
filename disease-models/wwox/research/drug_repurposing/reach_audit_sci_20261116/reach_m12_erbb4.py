#!/usr/bin/env python3
"""Reach audit, M12 table-3 half: Erbb4 KO/control TPM ratio in the mouse P17 bulk tables GSE158681 (hippocampus: null KO, S-line, N-line) and GSE158682 (cortex, S-line).

    python3 reach_m12_erbb4.py --help
    python3 reach_m12_erbb4.py run <downloads_dir> <out_tsv>

Reads the two public GEO supplementary TPM tables (transcript level) and two Ensembl REST lookup files (Erbb4 and Wwox transcript ids; ids matched without version), sums
transcript TPM per gene per sample, and prints group means and ratios. Descriptive: 2 to 4 animals per group, no test. Not medical advice.
"""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, json, statistics
D = sys.argv[2]
tids = {s: [t["id"] for t in json.load(open(f"{D}/ensembl_lookup_{s}.json"))["Transcript"]] for s in ("Erbb4", "Wwox")}
def load(fn):
    t = gzip.decompress(open(f"{D}/{fn}", "rb").read()).decode().splitlines(); h = t[0].split("\t")[3:]; rows = {}
    for l in t[1:]:
        a = l.split("\t"); rows[a[0].split(".")[0]] = [float(x) for x in a[3:]]
    return h, rows
G = [("hippocampus null (KO v WT)", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"]),
     ("hippocampus S line", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"]),
     ("hippocampus N line", "GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"]),
     ("cortex S line", "GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"])]
out = []
for name, fn, ko, ct in G:
    h, rows = load(fn)
    for sym in ("Erbb4", "Wwox"):
        hit = [t for t in tids[sym] if t in rows]; v = lambda c: sum(rows[t][h.index(c)] for t in hit)
        k = [v(c) for c in ko]; c_ = [v(c) for c in ct]
        out.append((name, sym, f"{len(hit)} of {len(tids[sym])} transcripts", f"KO {statistics.mean(k):.2f} (n{len(k)}; {', '.join(f'{x:.2f}' for x in k)})", f"control {statistics.mean(c_):.2f} (n{len(c_)}; {', '.join(f'{x:.2f}' for x in c_)})", f"ratio {statistics.mean(k)/statistics.mean(c_):.2f}"))
with open(sys.argv[3], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["contrast", "gene", "transcripts_matched", "KO_mean_TPM", "control_mean_TPM", "ratio"]); w.writerows(out)
for r in out: print(r)
