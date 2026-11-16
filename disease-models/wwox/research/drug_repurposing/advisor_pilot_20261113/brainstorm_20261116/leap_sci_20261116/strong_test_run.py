#!/usr/bin/env python3
"""Strong-test execution (PRESIDIO-020 step 2): IT's frozen thresholds (it_test_setter_20261116/test_setting.tsv, sha256 30f6109f...) applied to held data.

    python3 strong_test_run.py --help
    python3 strong_test_run.py run <repo_root> <files_dir> <xlrd_dir> <out_dir>

Executes ONLY the nine rows the setter marked could_held_data_reject = yes (M04, M08, M10, M11, M12, M17, M23, M29, M30), against the thresholds as written;
the other 22 rows are U by construction. Writes strong_test_values.tsv (every measured value) for the note. A threshold that cannot be fully executed is
reported as partial, with the reason, never changed. Held files only; no network. Descriptive: pool tables carry no variance. Not medical advice.
"""
import sys
if len(sys.argv) != 6 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, glob, gzip, importlib.util, math, os, re, statistics
from pathlib import Path
import numpy as np
REPO, FILES, XLRD, OUT = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5]); OUT.mkdir(parents=True, exist_ok=True)
DR = REPO / "disease-models/wwox/research/drug_repurposing"; RES = DR / "wwox_data_it24_p4_20261104/results"
V = []  # (row, quantity, value)
def put(m, q, v): V.append((m, q, v if isinstance(v, str) else (round(v, 4) if isinstance(v, float) else v)))
de = list(csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
def row(g, c):
    h = [r for r in de if r["symbol"] == g and r["contrast"] == c]; return h[0] if h else None
# M04: Mbp, Mobp KO/control ratio in the NULL contrast, cortex and hippocampus
for g in ("Mbp", "Mobp"):
    r = row(g, "H_null"); put("M04", f"{g} H_null KO/control TPM ratio (hippocampus null)", float(r["mean_TPM_KO"]) / float(r["mean_TPM_control"]) if r else "not among |cLFC|>=0.585 rows")
    put("M04", f"{g} cortex null contrast", "no cortex null contrast in the held table (cortex has C_S only)")
    r = row(g, "C_S"); put("M04", f"{g} C_S ratio (information only; not the rule's contrast)", float(r["mean_TPM_KO"]) / float(r["mean_TPM_control"]))
# M08: projection (reuse of the calibration loader)
spec = importlib.util.spec_from_file_location("mc", DR / "gse156243/maturation_calibration.py"); mc = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(mc)
s2e = mc.symbol_to_ensg(); TARGET = ["GRIN2B", "GRIN2A", "SLC12A2", "SLC12A5", "KCNK2", "KCNK3", "KCNK9", "CCN2"]; MP = ["NES", "VIM", "SOX2"]; MN = ["MAP2", "SYT1", "SNAP25"]
want = {g: s2e[g] for g in TARGET + MP + MN if g in s2e}; meta, cnt = mc.calibration_matrix(want); samples = [s for s in cnt if s in meta]
def val(s, g): return math.log2(cnt[s]["genes"].get(g, 0) / cnt[s]["total"] * 1e6 + 1)
lines = [meta[s]["iPSc line"] for s in samples]; days = [math.log2(float(meta[s]["differentiation day"])) for s in samples]
def slope(g):
    y = [val(s, g) for s in samples]; ym = {}; xm = {}
    for l in set(lines):
        idx = [i for i, ll in enumerate(lines) if ll == l]; ym[l] = statistics.mean(y[i] for i in idx); xm[l] = statistics.mean(days[i] for i in idx)
    xs = [days[i] - xm[lines[i]] for i in range(len(samples))]; ys = [y[i] - ym[lines[i]] for i in range(len(samples))]; den = sum(x * x for x in xs)
    return sum(a * b for a, b in zip(xs, ys)) / den if den else float("nan")
sl = {g: slope(g) for g in want}; ko = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene": cols = a[1:]; continue
    ko[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(ko.values())).sum(axis=0); ki = [i for i, c in enumerate(cols) if c.startswith("cko")]; wi = [i for i, c in enumerate(cols) if c.startswith("cwt")]
def kos(g):
    g = {"CCN2": "CTGF"}.get(g, g) if g not in ko else g; c = ko[g] / lib * 1e6; return math.log2((c[ki].mean() + 1) / (c[wi].mean() + 1))
dt = statistics.median([kos(g) / sl[g] for g in MP + MN if abs(sl[g]) > 0.05])
obs = {g: kos(g) for g in TARGET}; prj = {g: sl[g] * dt for g in TARGET}
for g in TARGET: put("M08", f"{g} observed / projected log2", f"{obs[g]:.3f} / {prj[g]:.3f}")
def agree(g):
    o, p = obs[g], prj[g]
    if abs(o) < 0.5: return abs(p) < 0.5
    return (o > 0) == (p > 0) if abs(p) >= 1e-9 else True
core = [g for g in TARGET if g != "CCN2"]; ag = [agree(g) for g in core]
named = ["GRIN2B", "GRIN2A", "SLC12A2", "SLC12A5"]
opp = [g for g in named if abs(obs[g]) >= 0.5 and (obs[g] > 0) != (prj[g] > 0)]
def spearman(gs):
    def rk(x): o = sorted(range(len(x)), key=lambda i: x[i]); r = [0] * len(x); [r.__setitem__(i, k) for k, i in enumerate(o)]; return r
    a = rk([obs[g] for g in gs]); b = rk([prj[g] for g in gs]); return float(np.corrcoef(a, b)[0, 1])
put("M08", "(a) genes in agreement (excluding CCN2)", f"{sum(ag)} of {len(core)}"); put("M08", "(a) met (fewer than half agree)", str(sum(ag) < len(core) / 2))
put("M08", "(b) named genes opposite to projection with |obs|>=0.5", f"{len(opp)} of 4 ({', '.join(opp)})"); put("M08", "(b) met (>=3 of 4)", str(len(opp) >= 3))
put("M08", "(c) Spearman observed v projected, 7 genes without CCN2 / 8 with CCN2", f"{spearman(core):.3f} / {spearman(TARGET):.3f}"); put("M08", "(c) met (<=0)", str(spearman(core) <= 0 or spearman(TARGET) <= 0))
# M10: mTORC1 hallmark
g = [r for r in csv.DictReader(open(DR / "p47t_it12_20261031/results/gsea_reimpl_it12.tsv"), delimiter="\t") if r["hallmark"] == "HALLMARK_MTORC1_SIGNALING"]
for r in g: put("M10", f"P47T {r['region']} hallmark MTORC1 NES / BH q (IT12 reimplementation)", f"{r['NES']} / {r['BH_q_over_50']}")
put("M10", "organoid and mouse P17 hallmark GSEA", "not held: the hallmark GMT (mh.gmt) is not on this host and no organoid or P17 hallmark result is held; composite-adjusted enrichment cannot be computed")
# M11
fam = list(csv.DictReader(open(DR / "network_comparison_it7_p3_20261029/results/family_scores.tsv"), delimiter="\t"))
oe = sorted(float(r["O_E"]) for r in fam if r["O_E"] not in ("", "NA")); vp = [float(r["O_E"]) for r in fam if r["name"] == "VALPROIC ACID"][0]
put("M11", "valproic acid family O_E; rank from the most negative (of %d)" % len(oe), f"{vp} ; rank {sum(1 for x in oe if x < vp) + 1}")
sg = {r["sig_id"]: r for r in csv.DictReader(open(DR / "network_comparison_it7_p3_20261029/results/signature_scores.tsv"), delimiter="\t")}
vs = [float(r["opposition_score"]) for r in sg.values() if r["pert_id"] == "BRD-K41260949" and r["context_class"] == "E"]
put("M11", "valproic acid neuron-like (context E) signature scores", "; ".join(f"{x:.3f}" for x in vs)); put("M11", "negative neuron-like signatures", f"{sum(x < 0 for x in vs)} of {len(vs)}")
# P47T tables
f = gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"); h = f.readline().rstrip("\n").split("\t"); P47 = {}
for l in f:
    r = dict(zip(h, l.rstrip("\n").split("\t"))); P47[(r["symbol"], r["region"])] = r
# M12
n12 = 0
for rg in ("CTX", "HPC", "PFC", "CB"):
    r = P47[("Erbb4", rg)]; l2 = float(r["log2FC_centred"]); ok = l2 >= -0.15; n12 += ok
    put("M12", f"P47T {rg} Erbb4 log2FC centred (ratio {2**l2:.2f}); >= -0.15", f"{l2:.2f} ; {ok}")
put("M12", "table 5 condition (>=3 of 4 regions at ratio>=0.90)", f"{n12} of 4")
put("M12", "table 3 null contrast, both regions", "Erbb4 is not among the |cLFC|>=0.585 rows of any mouse contrast (change < 1.5-fold either way or not expressed); the committed table holds no TPM below that cut and no cortex null contrast, so a ratio >= 0.90 cannot be tested")
# M17
for c in ("C_S", "H_S", "C_N", "H_N"):
    r = row("Npy", c); put("M17", f"Npy {c} KO/control TPM; log2", f"{r['mean_TPM_KO']}/{r['mean_TPM_control']}; {math.log2(float(r['mean_TPM_KO'])/float(r['mean_TPM_control'])):.2f}; flag background-confounded={r['BACKGROUND_CONFOUNDED']}" if r else "not among rows / not held")
cs, hs = row("Npy", "C_S"), row("Npy", "H_S")
d = math.log2(float(cs["mean_TPM_KO"]) / float(cs["mean_TPM_control"])) - math.log2(float(hs["mean_TPM_KO"]) / float(hs["mean_TPM_control"]))
put("M17", "S line: cortical log2 rise minus hippocampal log2 rise (reject if >= -0.5)", f"{d:.2f} ; reject={d >= -0.5}")
# M23
ch = list(csv.DictReader(open(Path(__file__).parent / "it_pretest_output/a1_both_endpoint_children.tsv"), delimiter="\t"))
expl = [c for c in ch if re.search(r"before (treatment|vigabatrin)", c["first_imaging_stated"])]
put("M23", "children with both endpoints", len(ch)); put("M23", "children whose imaging is explicitly stated as before treatment", f"{len(expl)} ({', '.join(c['child'] for c in expl)})")
put("M23", "contradicting (discordant+normal imaging, or concordant+structural abnormality), all 6 / confirming", f"{sum(c['concordance']=='concordant' for c in ch)} / {sum(c['concordance']=='discordant' for c in ch)}")
# M29, M30 via matrices and class tables
G = FILES / "geo/GSE158684"; fr = {}
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt")); gi = [i + 1 for i, x in enumerate(feats) if (x[1] if len(x) > 1 else x[0]) == "Snap25"][0]
    pos = set(); f2 = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f2:
        if l[0] != "%": break
    for l in f2:
        a = l.split()
        if int(a[0]) == gi and float(a[2]) >= 1: pos.add(int(a[1]))
    fr[arm] = (len(pos), nb); put("M29", f"{arm} Snap25-positive nuclei / nuclei", f"{len(pos)} / {nb} = {len(pos)/nb:.4f}")
p1, p2 = fr["ctrl"][0] / fr["ctrl"][1], fr["ko"][0] / fr["ko"][1]; se = math.sqrt(p1 * (1 - p1) / fr["ctrl"][1] + p2 * (1 - p2) / fr["ko"][1])
put("M29", "KO minus control fraction ; -2 SE", f"{p2 - p1:.4f} ; {-2 * se:.4f}"); put("M29", "reject (diff >= -2 SE)", str(p2 - p1 >= -2 * se))
sys.path.insert(0, XLRD); import xlrd; acc = {}
for fn in sorted(glob.glob(str(FILES / "geo/GSE52564_raw/*.xls.gz"))):
    cls = re.sub(r"\d+$", "", re.sub(r"^GSM\d+_", "", os.path.basename(fn)[:-7]))
    if cls not in ("Astrocyte", "Neuron"): continue
    s = xlrd.open_workbook(file_contents=gzip.open(fn).read()).sheet_by_index(0); names = {str(s.cell_value(r, 0)).strip().upper(): r for r in range(s.nrows)}
    for gname in ("Slc6a1", "Slc6a11"):
        if gname.upper() in names: acc.setdefault((gname, cls), []).append(float(s.cell_value(names[gname.upper()], 1)))
for gname in ("Slc6a1", "Slc6a11"):
    n, a_ = statistics.mean(acc[(gname, "Neuron")]), statistics.mean(acc[(gname, "Astrocyte")]); put("M30", f"mouse {gname} neuron / astrocyte FPKM (neuron/astrocyte ratio)", f"{n:.2f} / {a_:.2f} ({n/a_:.2f})")
hh = gzip.open(FILES / "geo/GSE73721/GSE73721_Human_and_mouse_table.csv.gz", "rt"); hd = hh.readline().rstrip("\n").split(",")
ni = [i for i, x in enumerate(hd) if x.endswith("ctx neuron")]; ai = [i for i, x in enumerate(hd) if x.endswith("astro") and not x.startswith("Mouse") and "tumor" not in x and "Fetal" not in x]
hum = {}
for l in hh:
    a = l.rstrip("\n").split(",")
    if a[0].upper() in ("SLC6A1", "SLC6A11"): hum[a[0].upper()] = a
for gname, a in hum.items():
    n = statistics.mean(float(a[i]) for i in ni); s_ = statistics.mean(float(a[i]) for i in ai); put("M30", f"human {gname} neuron(n={len(ni)}) / adult-astrocyte(n={len(ai)}) FPKM (ratio)", f"{n:.2f} / {s_:.2f} ({n/s_:.2f})")
with open(OUT / "strong_test_values.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["row", "quantity", "value"]); w.writerows(V)
print("done", len(V))
