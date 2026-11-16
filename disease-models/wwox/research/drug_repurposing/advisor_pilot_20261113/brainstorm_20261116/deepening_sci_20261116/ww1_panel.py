#!/usr/bin/env python3
"""Panel-wide classification of 25 circuit genes across the S-line knockout (GSE158681/2, P17) and the P47T knock-in (GSE215425). Rule and predictions: PREREGISTRATION_WW1_PANEL.md
(hashed before any join). 'Copied' is at most 'reproduced in a line that keeps the protein'; it is not a WW1-route call and not a statement that missense variants are hypomorphic.
    python3 ww1_panel.py --help
    python3 ww1_panel.py run <downloads_dir> <p47t_table.tsv.gz> <out_tsv>
S-line values: transcript TPM summed per gene from the two public GEO tables with Ensembl REST symbol lookups (one GET per gene, cached in downloads_dir). P47T: the committed table."""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, json, math, os, statistics, time, urllib.request
D, PT, OUT = sys.argv[2], sys.argv[3], sys.argv[4]
PANEL = ["Gabrd","Gabra5","Gabra1","Gabrg2","Slc6a1","Npy","Npy2r","Sst","Pvalb","Gad1","Grin2b","Grin2a","Cacna1h","Cacna1i","Hcn2","Slc12a5","Slc12a2","Kcnk2","Kcnq2","Gja1","Kcnj10","Gfap","Adk","Adora1","Wwox"]
T975_8 = 2.306
def tids(sym):
    fn = f"{D}/ensembl_lookup_{sym}.json"
    if not os.path.exists(fn):
        raw = urllib.request.urlopen(urllib.request.Request(f"https://rest.ensembl.org/lookup/symbol/mus_musculus/{sym}?expand=1;content-type=application/json"), timeout=60).read()
        open(fn, "wb").write(raw); time.sleep(0.4)
    return [t["id"] for t in json.load(open(fn))["Transcript"]]
def load(fn):
    t = gzip.decompress(open(f"{D}/{fn}", "rb").read()).decode().splitlines(); h = t[0].split("\t")[3:]; rows = {}
    for l in t[1:]:
        a = l.split("\t"); rows[a[0].split(".")[0]] = [float(x) for x in a[3:]]
    return h, rows
H = load("GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz"); C = load("GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz")
GR = {"cortex": (C, ["CRTX_S_Ctrl_1","CRTX_S_Ctrl_2","CRTX_S_Ctrl_3","CRTX_S_Ctrl_4"], ["CRTX_S_KO_1","CRTX_S_KO_2","CRTX_S_KO_3"]),
      "hippocampus": (H, ["S_Ctrl_1","S_Ctrl_2"], ["S_KO_1","S_KO_2","S_KO_3"])}
def sval(g, reg):
    (h, rows), ctl, ko = GR[reg]; ids = tids(g); hit = [t for t in ids if t in rows]
    m = lambda cols: statistics.mean(sum(rows[t][h.index(c)] for t in hit) for c in cols)
    return m(ctl), m(ko)
P = {}
for r in csv.DictReader(gzip.open(PT, "rt"), delimiter="\t"):
    P[(r["symbol"], r["region"])] = r
def classify(S, p):
    if abs(S) < 0.4: return "not readable"
    lo, hi = p["fc"] - T975_8 * p["se"], p["fc"] + T975_8 * p["se"]
    same = p["fc"] * S > 0
    if same and abs(p["fc"]) >= 0.5 * abs(S): return "copied"
    if same and abs(p["fc"]) >= 0.2 * abs(S): return "partly copied"
    if (not same) and (lo > 0 or hi < 0): return "opposite"
    if abs(p["fc"]) < 0.2 * abs(S) and not (lo <= S <= hi): return "not copied"
    return "not separable"
rows = []
for g in PANEL:
    for reg, pregs in (("cortex", ("CTX", "PFC")), ("hippocampus", ("HPC",))):
        c, k = sval(g, reg); S = math.log2((k + 0.1) / (c + 0.1))
        for pr in pregs:
            r = P.get((g, pr))
            if not r: rows.append([g, reg, f"{c:.2f}", f"{k:.2f}", f"{S:+.2f}", pr, "NA", "NA", "NA", "NA", "NA", "no P47T row"]); continue
            fc = float(r["log2FC_centred"]); t = float(r["t"]); se = abs(fc / t) if t else float("nan")
            call = classify(S, {"fc": fc, "se": se}) if (c >= 1 or k >= 1) else "not readable"
            direction = " (direction only)" if float(r["FDR_no_sex"]) >= 0.2 and call in ("copied", "partly copied", "opposite") else ""
            rows.append([g, reg, f"{c:.2f}", f"{k:.2f}", f"{S:+.2f}", pr, f"{fc:+.2f}", f"{fc - T975_8 * se:+.2f} to {fc + T975_8 * se:+.2f}", r["FDR_no_sex"][:5], r["FDR_with_sex"][:5], r["mean_norm_count_WT"][:7], call + direction])
with open(OUT, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["gene", "S_line_region", "S_ctrl_TPM", "S_KO_TPM", "S_log2", "P47T_region", "P47T_log2FC", "P47T_95pct_interval", "FDR_no_sex", "FDR_with_sex", "P47T_WT_norm_count", "call"]); w.writerows(rows)
for r in rows: print("\t".join(r))
