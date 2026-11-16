#!/usr/bin/env python3
"""I3 regional baseline: control-animal and knockout/control TPM of circuit genes in the held mouse P17 bulk tables
GSE158681 (hippocampus: null, S line, N line) and GSE158682 (cortex, S line). Public GEO supplementary tables
(transcript level) plus Ensembl REST symbol lookups (generic client, one GET per gene, no account).

    python3 regional_baseline.py --help
    python3 regional_baseline.py run <downloads_dir> <out_tsv>

Descriptive: 2 to 4 animals per group, no test. Cortex and hippocampus are different preparations (different tables, possibly
different batches), so a ratio between regions is a pointer, not a measurement. Not medical advice; mechanism-level only."""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, hashlib, json, os, statistics, time, urllib.request
D = sys.argv[2]
GENES = ["Atp1a2","Atp1a3","Gja1","Aqp4","Kcnj10","Kcnj16","Slc1a2","Slc1a3","Gfap","Slc12a2","Wwox"]
def tids(sym):
    fn = f"{D}/ensembl_lookup_{sym}.json"
    if not os.path.exists(fn):
        req = urllib.request.Request(f"https://rest.ensembl.org/lookup/symbol/mus_musculus/{sym}?expand=1;content-type=application/json")
        raw = urllib.request.urlopen(req, timeout=60).read(); open(fn, "wb").write(raw); time.sleep(0.4)
    return [t["id"] for t in json.load(open(fn))["Transcript"]]
def load(fn):
    t = gzip.decompress(open(f"{D}/{fn}", "rb").read()).decode().splitlines(); h = t[0].split("\t")[3:]; rows = {}
    for l in t[1:]:
        a = l.split("\t"); rows[a[0].split(".")[0]] = [float(x) for x in a[3:]]
    return h, rows
H = load("GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz"); C = load("GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz")
GRP = {"cortex S ctrl": (C, ["CRTX_S_Ctrl_1","CRTX_S_Ctrl_2","CRTX_S_Ctrl_3","CRTX_S_Ctrl_4"]), "cortex S KO": (C, ["CRTX_S_KO_1","CRTX_S_KO_2","CRTX_S_KO_3"]),
       "hippo S ctrl": (H, ["S_Ctrl_1","S_Ctrl_2"]), "hippo S KO": (H, ["S_KO_1","S_KO_2","S_KO_3"]),
       "hippo N ctrl": (H, ["N_Ctrl_1","N_Ctrl_2"]), "hippo N KO": (H, ["N_KO_1","N_KO_2"]),
       "hippo WT (null set)": (H, ["WT_1","WT_2","WT_3"]), "hippo null KO": (H, ["KO_1","KO_2"])}
out = []
for g in GENES:
    ids = tids(g); row = [g]
    for name, ((h, rows), cols) in GRP.items():
        hit = [t for t in ids if t in rows]
        vals = [sum(rows[t][h.index(c)] for t in hit) for c in cols]; row.append(round(statistics.mean(vals), 2))
    row.append(f"{len([t for t in ids])} transcripts listed")
    cc, ck, hc, hk = row[1], row[2], row[3], row[4]
    row += [round(ck / cc, 2) if cc else "NA", round(hk / hc, 2) if hc else "NA", round(hc / cc, 2) if cc else "NA"]
    out.append(row)
with open(sys.argv[3], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["gene"] + list(GRP) + ["ensembl_note", "cortex_S_KO_over_ctrl", "hippo_S_KO_over_ctrl", "hippo_over_cortex_S_ctrl"]); w.writerows(out)
for r in out: print("\t".join(str(x) for x in r))
