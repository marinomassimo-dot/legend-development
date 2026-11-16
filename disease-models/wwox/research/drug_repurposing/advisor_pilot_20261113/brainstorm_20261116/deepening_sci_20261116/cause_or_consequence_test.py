#!/usr/bin/env python3
"""Candidate [4] cause or consequence: chronic seizure-model counts against the S-line hippocampus. Rule, panel and predictions: PREREGISTRATION_CAUSE_OR_CONSEQUENCE_SCI.md and AMENDMENT_1_CAUSE_OR_CONSEQUENCE_SCI.md (both hashed before any count file was opened). Hypothesis level; numpy only; seeded.
    python3 cause_or_consequence_test.py --help
    python3 cause_or_consequence_test.py run <counts.tsv.gz genes x samples> <series_matrix.txt.gz> <ww1_panel.tsv> <downloads_dir with ensembl_lookup_*.json> <chronic_tag> <species mouse|rat> <out.tsv>
chronic_tag: text that the sample TITLE must start with ('3m' for GSE330624); use '' for a series with no time tag (GSE50079: pass the treatment words through the characteristics: samples whose 'treatment' says pilocarpine vs control and 'diet' standard).
Per sample: CPM over all genes in the file, log2(CPM+1). C = mean(treated) - mean(control) of that log2 value per fraction. Bootstrap 95% interval: 10,000 draws over samples, seed 1."""
import sys
if len(sys.argv) != 9 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, json, os
import numpy as np
COUNTS, MATRIX, PANELTSV, DL, TAG, SPECIES, OUT = sys.argv[2:9]
NEG = {"Gfap", "Gja1", "Kcnj10", "Adk", "Aif1"}        # NeuN- primary fraction (amendment 1, point 2)
PRED = {"Gfap": "+", "Aif1": "+", "Npy": "+", "Sst": "-", "Slc12a5": "-", "Slc12a2": "+", "Cacna1h": "+", "Hcn2": "-", "Gabrd": "-", "Gabra5": "-", "Pvalb": "-", "Gad1": "unreadable"}
PANEL = ["Gabrd", "Gabra5", "Gabra1", "Gabrg2", "Slc6a1", "Npy", "Npy2r", "Sst", "Pvalb", "Gad1", "Grin2b", "Grin2a", "Cacna1h", "Cacna1i", "Hcn2", "Slc12a5", "Slc12a2", "Kcnk2", "Kcnq2", "Adora1", "Gfap", "Gja1", "Kcnj10", "Adk", "Wwox", "Aif1"]
# sample metadata from the series matrix
meta = {}
for l in gzip.open(MATRIX, "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "!Sample_title": meta["title"] = [x.strip('"') for x in a[1:]]
    elif a[0] == "!Sample_geo_accession": meta["gsm"] = [x.strip('"') for x in a[1:]]
    elif a[0] == "!Sample_characteristics_ch1":
        k = a[1].strip('"').split(":")[0].strip().lower(); meta.setdefault("ch_" + k, [x.strip('"').split(":", 1)[-1].strip().lower() for x in a[1:]])
        # note: the first row seen for a key wins
n = len(meta["title"])
def role(i):
    t = meta.get("ch_treatment", [""] * n)[i]
    if any(w in t for w in ("kainic", "kainate", "pilocarpine")) and "saline" not in t: return "treated"
    if any(w in t for w in ("nacl", "saline", "control", "sham")): return "control"
    return None
def frac(i): return meta.get("ch_cell type", ["all"] * n)[i]
def diet_ok(i): return meta.get("ch_diet", ["standard"] * n)[i] in ("standard", "")
h = None; genes = []; M = []
for k, l in enumerate(gzip.open(COUNTS, "rt")):
    a = l.rstrip("\n").split("\t")
    if k == 0: h = a[1:]; continue
    genes.append(a[0]); M.append([float(x) for x in a[1:]])
M = np.array(M); cols = {c: j for j, c in enumerate(h)}
def colof(i):
    for key in (meta["title"][i], meta.get("gsm", [None] * n)[i], meta["title"][i].replace(" ", "_")):
        if key in cols: return cols[key]
    for c in cols:
        if c.strip() == meta["title"][i].strip(): return cols[c]
    return None
samples = []
for i in range(n):
    if TAG and not meta["title"][i].startswith(TAG): continue
    r = role(i)
    if r is None or not diet_ok(i): continue
    j = colof(i)
    if j is None: raise SystemExit("sample %s not found among count columns (first columns: %s)" % (meta["title"][i], h[:5]))
    samples.append((i, j, r, frac(i)))
print("samples used:", len(samples), "of", n, "| per group:", {(f, r): sum(1 for s in samples if s[2] == r and s[3] == f) for f in set(s[3] for s in samples) for r in ("treated", "control")})
lib = M.sum(axis=0); L = np.log2(M / lib * 1e6 + 1.0)
sym_index = {g.lower(): k for k, g in enumerate(genes)}
def row(sym):
    if sym.lower() in sym_index: return sym_index[sym.lower()]
    fn = "%s/ensembl_lookup_%s.json" % (DL, sym)
    if SPECIES == "mouse" and os.path.exists(fn):
        gid = json.load(open(fn)).get("id")
        for cand in (gid,):
            if cand and cand.lower() in sym_index: return sym_index[cand.lower()]
    return None
S = {}
for r in csv.DictReader(open(PANELTSV), delimiter="\t"):
    if r["S_line_region"] == "hippocampus": S[r["gene"]] = float(r["S_log2"])
rng = np.random.default_rng(1)
out = [["gene", "fraction_used", "C_log2", "ci_low", "ci_high", "n_treated", "n_control", "S_line_hippocampus_log2", "readable_C(|C|>=0.4)", "readable_S(|S|>=0.4)", "same_sign", "call_vs_S", "predicted_sign", "prediction_result", "C_other_fraction"]]
def stat(rw, fr):
    t = [L[rw, s[1]] for s in samples if s[2] == "treated" and s[3] == fr]; c = [L[rw, s[1]] for s in samples if s[2] == "control" and s[3] == fr]
    if len(t) < 2 or len(c) < 2: return None
    d = np.mean(t) - np.mean(c); bt = rng.choice(t, (10000, len(t))).mean(1) - rng.choice(c, (10000, len(c))).mean(1)
    return d, np.percentile(bt, 2.5), np.percentile(bt, 97.5), len(t), len(c)
fracs = sorted(set(s[3] for s in samples)); both = 0; same = 0
for g in PANEL:
    rw = row(g)
    if rw is None: out.append([g, "unmapped"] + [""] * 13); continue
    if "neun+" in fracs or "neun-" in fracs:
        pf = "neun-" if g in NEG else "neun+"; of = "neun+" if g in NEG else "neun-"
    else: pf = fracs[0]; of = ""
    st = stat(rw, pf)
    if st is None: out.append([g, pf + " too few samples"] + [""] * 13); continue
    d, lo, hi, nt, nc = st; s = S.get(g); ro = stat(rw, of) if of in fracs else None
    readC = abs(d) >= 0.4; readS = s is not None and abs(s) >= 0.4; ss = (s is not None) and (d * s > 0)
    if g != "Wwox" and readC and readS:
        both += 1; same += 1 if ss else 0
    if s is None or not readS: call = "S not readable"
    elif d * s > 0 and abs(d) >= 0.5 * abs(s): call = "copied"
    elif d * s > 0 and abs(d) >= 0.2 * abs(s): call = "partly copied"
    elif d * s < 0 and (lo > 0 or hi < 0): call = "opposite"
    elif abs(d) < 0.2 * abs(s) and not (lo <= s <= hi): call = "not copied"
    else: call = "not separable"
    pr = PRED.get(g, ""); res = ""
    if pr == "unreadable": res = "right" if not readC else "wrong"
    elif pr: res = ("not readable" if not readC else ("right" if (pr == "+") == (d > 0) else "wrong"))
    out.append([g, pf, "%+.2f" % d, "%+.2f" % lo, "%+.2f" % hi, nt, nc, "" if s is None else "%+.2f" % s, readC, readS, ss, call, pr, res, "" if ro is None else "%+.2f" % ro[0]])
with open(OUT, "w") as f:
    for r in out: f.write("\t".join(str(x) for x in r) + "\n")
print("readable in both (excluding Wwox):", both, "| same sign as S-line:", same, "| share:", (same / both if both else float("nan")))
print("wrote", OUT)
