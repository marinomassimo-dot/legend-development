#!/usr/bin/env python3
"""ADV-007, part A: CTGF/CCN2 in the held human organoid contrast (GSE156243) and its maturation calibration (GSE150123).

Reads only files already held (gitignored files/geo in the main checkout) and the committed gse156243 helper
maturation_calibration.py, whose within-line estimators are reused unchanged. No network. Standard library only.
Not medical advice; nothing here is WWOX evidence about a patient; expression is not secretion.

    python3 ctgf_organoid_maturation.py --help
    python3 ctgf_organoid_maturation.py run <out_dir>

Writes organoid_per_library.tsv, maturation_ctgf.json, coupling_ctgf.tsv, symbol_trace.tsv into <out_dir>.
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv, gzip, importlib.util, json, math, os, statistics
from pathlib import Path

OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
HERE = Path(__file__).resolve().parent
DR = HERE.parent
spec = importlib.util.spec_from_file_location("mc", DR / "gse156243" / "maturation_calibration.py")
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)

GENE_NEW, GENE_OLD, ENSG = "CCN2", "CTGF", "ENSG00000118523"

# ---- 1. the contrast in the six libraries (counts are the authors' Salmon table; list values are the authors' DESeq2 as held)
rows = {}
with gzip.open(mc.KO_COUNTS, "rt", encoding="utf-8") as h:
    rd = csv.reader(h, delimiter="\t")
    hdr = next(rd)
    for r in rd:
        rows[r[0]] = [float(x) for x in r[1:]]
tot = [sum(v[i] for v in rows.values()) for i in range(6)]
libs = hdr[1:]
cpm = [rows[GENE_OLD][i] / tot[i] * 1e6 for i in range(6)]
with open(OUT / "organoid_per_library.tsv", "w", encoding="utf-8") as f:
    f.write("library\tgenotype\tcount\tlibrary_total\tcpm\n")
    for i, l in enumerate(libs):
        f.write(f"{l}\t{'KO' if l.startswith('cko') else 'WT'}\t{rows[GENE_OLD][i]:.0f}\t{tot[i]:.0f}\t{cpm[i]:.2f}\n")
ko_cpm, wt_cpm = cpm[:4], cpm[4:]
obs_shift = math.log2((statistics.fmean(ko_cpm) + 1) / (statistics.fmean(wt_cpm) + 1))
res = {"gene_in_deposit_table": GENE_OLD, "current_symbol": GENE_NEW, "ensg": ENSG,
       "cpm_ko": [round(x, 1) for x in ko_cpm], "cpm_wt": [round(x, 1) for x in wt_cpm],
       "every_ko_library_above_every_wt_library": bool(min(ko_cpm) > max(wt_cpm)),
       "min_ko_over_max_wt": round(min(ko_cpm) / max(wt_cpm), 2),
       "ko_vs_wt_log2_shift_cpm_plus1": round(obs_shift, 3),
       "authors_deseq2_as_held": {"log2FC": 1.32, "padj": 0.00707, "pvalue": 0.00031, "gene_position_in_lists": "line 360 of list_padj_le_0.05.tsv; line 199 of list_padj_le_0.01.tsv",
       "exact_permutation_floor_4_v_2": {"arrangements": 15, "one_sided_min_p": round(1 / 15, 3), "two_sided_min_p": round(2 / 15, 3),
       "note": "with 4 v 2 libraries no rank test can go below 0.13 two-sided; the DESeq2 padj rests on a fitted dispersion model, not on this design"}}}

# ---- 2. why composition_class.tsv has blanks for this gene: a symbol trace
tr = []
S1 = json.load(open(DR / "gse156243" / "derived" / "query_sets.json"))["S1"]
up_list = set(S1["up"])
l05 = {r["symbol"] for r in csv.DictReader(open(DR / "gse156243" / "derived" / "list_padj_le_0.05.tsv"), delimiter="\t")}
comp = {r["symbol"]: r for r in csv.DictReader(open(DR / "signature_it23_20261103" / "composition_class.tsv"), delimiter="\t")}
tr.append(("symbol in the authors' list (list_padj_le_0.05.tsv, key of the script's log2FC and ENSG lookups)", GENE_OLD, GENE_OLD in l05))
tr.append(("symbol in S1 up set (query_sets.json, after symbol validation)", GENE_NEW, GENE_NEW in up_list))
tr.append(("old symbol in S1 up set", GENE_OLD, GENE_OLD in up_list))
tr.append(("row in composition_class.tsv under the new symbol", GENE_NEW, GENE_NEW in comp))
tr.append(("row in composition_class.tsv under the old symbol", GENE_OLD, GENE_OLD in comp))
# every blank-log2fc row: is its old symbol in the list while the new one is not?
blank = [s for s, r in comp.items() if r["log2fc"] == ""]
sv = list(csv.DictReader(open(DR / "gse156243" / "derived" / "symbol_validation.tsv"), delimiter="\t"))
renamed_to = {r["hgnc_symbol_for_ensg"]: r["list_symbol"] for r in sv if r["symbol_status"].startswith("previous_symbol")}
res["blank_rows_that_are_symbol_renames"] = {s: renamed_to.get(s) for s in blank}
res["blank_rows_total"] = len(blank)
res["blank_rows_explained_by_rename"] = sum(1 for s in blank if s in renamed_to)
with open(OUT / "symbol_trace.tsv", "w", encoding="utf-8") as f:
    f.write("check\tsymbol\tresult\n")
    for a, b, c in tr:
        f.write(f"{a}\t{b}\t{c}\n")
    f.write("rows in composition_class.tsv with a blank log2fc\t-\t" + str(len(blank)) + "\n")
res["composition_class_blank_log2fc_rows"] = blank

# ---- 3. calibration: CTGF against elapsed culture time, within line (reused estimators), and coupling to the marker panels
mc.verify_inputs()
s2e = mc.symbol_to_ensg()
wanted = {g: s2e[g] for g in (mc.PROGENITOR + mc.NEURONAL) if g in s2e}
wanted[GENE_NEW] = ENSG
meta, data = mc.calibration_matrix(wanted)
titles = sorted(data)
days = [float(meta[t]["differentiation day"]) for t in titles]
lines = [meta[t]["iPSc line"] for t in titles]
logd = [math.log10(d) for d in days]
l2 = lambda t, g: math.log2(data[t]["genes"].get(g, 0.0) / data[t]["total"] * 1e6 + 1)
y = [l2(t, GENE_NEW) for t in titles]
mean_count = statistics.fmean(data[t]["genes"].get(GENE_NEW, 0.0) for t in titles)
sl, se, r2 = mc.ols(mc.demean_by(lines, logd), mc.demean_by(lines, y))
lsl = mc._line_slopes(lines, logd, y)
m, sd, k = statistics.fmean(lsl.values()), statistics.stdev(lsl.values()), len(lsl)
half = mc._T975.get(k - 1, 1.96) * sd / math.sqrt(k)
lo, hi, nclu = mc._cluster_bootstrap(lines, logd, y, 4000, 20261114)
keep = [i for i, d in enumerate(days) if d >= 60]
ly, lx, lyy = [lines[i] for i in keep], [logd[i] for i in keep], [y[i] for i in keep]
sl60 = mc._line_slopes(ly, lx, lyy)
m60, sd60, k60 = statistics.fmean(sl60.values()), statistics.stdev(sl60.values()), len(sl60)
half60 = mc._T975.get(k60 - 1, 1.96) * sd60 / math.sqrt(k60)
lo60, hi60, _ = mc._cluster_bootstrap(ly, lx, lyy, 4000, 20261114)
loo = {}
for L in sorted(set(lines)):
    idx = [i for i, l in enumerate(lines) if l != L]
    try:
        loo[L] = round(mc._pooled([lines[i] for i in idx], [logd[i] for i in idx], [y[i] for i in idx]), 3)
    except ZeroDivisionError:
        loo[L] = None
yc = mc.demean_by(lines, y)
bins = {}
for a, b in ((25, 60), (60, 110), (110, 230), (230, 400), (400, 700)):
    ii = [i for i, d in enumerate(days) if a <= d < b]
    bins[f"{a}-{b}"] = {"n": len(ii), "mean_line_centred_log2cpm": round(statistics.fmean(yc[i] for i in ii), 3)} if ii else {"n": 0}
res["calibration_GSE150123"] = {
    "n_samples": len(titles), "samples_per_line": {l: lines.count(l) for l in sorted(set(lines))},
    "mean_count_per_sample": round(mean_count, 1),
    "pooled_within_line_slope_per_log10_day": round(sl, 3), "naive_se_treating_samples_independent": round(se, 3), "r2_within_line": round(r2, 3),
    "mean_of_line_slopes": round(m, 3), "between_line_t_interval": [round(m - half, 3), round(m + half, 3)], "lines_used": k,
    "per_line_slopes": {l: round(v, 3) for l, v in lsl.items()}, "cluster_bootstrap_95": [round(lo, 3), round(hi, 3)],
    "day_ge_60": {"n": len(keep), "mean_of_line_slopes": round(m60, 3), "between_line_t_interval": [round(m60 - half60, 3), round(m60 + half60, 3)],
                  "cluster_bootstrap_95": [round(lo60, 3), round(hi60, 3)], "lines_used": k60,
                  "interval_includes_zero": bool((m60 - half60) <= 0 <= (m60 + half60))},
    "leave_one_line_out_pooled_slope": loo, "day_bins": bins}

# the flags the original composition-class script (signature_it23_20261103) WOULD have set had the symbol resolved:
# Spearman rho of log2(CPM+1) against log10(day) over all 62 samples, no line adjustment, as in reproduce_dseqr_cmap_comparison.py
def _rk(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
            j += 1
        for q in range(i, j + 1):
            r[o[q]] = (i + j) / 2 + 1
        i = j + 1
    return r
_a, _b = _rk(logd), _rk(y)
_ma, _mb = statistics.fmean(_a), statistics.fmean(_b)
rho = sum((u - _ma) * (v - _mb) for u, v in zip(_a, _b)) / math.sqrt(sum((u - _ma) ** 2 for u in _a) * sum((v - _mb) ** 2 for v in _b))
res["original_method_flags_if_computed"] = {"rho_vs_log10_day_62_samples": round(rho, 3), "mean_count_filter_ge_5": mean_count >= 5,
    "broad_class_abs_rho_ge_0.4": abs(rho) >= 0.4, "maturation_consistent_abs_rho_ge_0.6_and_KO_up_with_rho_negative": bool(abs(rho) >= 0.6 and rho < 0),
    "in_declared_markers": False}

# coupling to progenitor / neuronal markers, as in maturation_calibration.py: slope(CCN2 on marker, within line) x KO shift of the marker
ko_shift = {}
for g in wanted:
    if g == GENE_NEW or g not in rows:
        continue
    c = [rows[g][i] / tot[i] * 1e6 for i in range(6)]
    ko_shift[g] = math.log2((statistics.fmean(c[:4]) + 1) / (statistics.fmean(c[4:]) + 1))
cp = []
for pname, panel in (("progenitor", mc.PROGENITOR), ("neuronal", mc.NEURONAL)):
    for g in panel:
        if g not in wanted or g not in ko_shift:
            continue
        if statistics.fmean(data[t]["genes"].get(g, 0.0) for t in titles) < mc.MIN_MEAN_COUNT:
            continue
        x = [l2(t, g) for t in titles]
        s, sse, rr2 = mc.ols(mc.demean_by(lines, x), mc.demean_by(lines, y))
        cp.append((pname, g, s, rr2, ko_shift[g], s * ko_shift[g]))
with open(OUT / "coupling_ctgf.tsv", "w", encoding="utf-8") as f:
    f.write("panel\tmarker\tslope_ccn2_on_marker_within_line\tr2_within_line\tmarker_ko_vs_wt_log2_shift\tpredicted_ccn2_shift_from_marker\tobserved_ccn2_shift\n")
    for p, g, s, rr2, ks, pr in cp:
        f.write(f"{p}\t{g}\t{s:.3f}\t{rr2:.3f}\t{ks:.3f}\t{pr:.3f}\t{obs_shift:.3f}\n")
# composite: mean z of the six progenitor markers minus mean z of the six neuronal markers (z against the calibration samples)
def _sd(v):
    return statistics.pstdev(v)
zc = {}
for g in wanted:
    if g == GENE_NEW or g not in ko_shift or statistics.fmean(data[t]["genes"].get(g, 0.0) for t in titles) < mc.MIN_MEAN_COUNT:
        continue
    v = [l2(t, g) for t in titles]
    zc[g] = (statistics.fmean(v), _sd(v), v)
prog = [g for g in mc.PROGENITOR if g in zc]
neur = [g for g in mc.NEURONAL if g in zc]
comp = [statistics.fmean((zc[g][2][i] - zc[g][0]) / zc[g][1] for g in prog) - statistics.fmean((zc[g][2][i] - zc[g][0]) / zc[g][1] for g in neur) for i in range(len(titles))]
cs, _, cr2 = mc.ols(mc.demean_by(lines, comp), mc.demean_by(lines, y))
comp_ko_shift = statistics.fmean(ko_shift[g] / zc[g][1] for g in prog) - statistics.fmean(ko_shift[g] / zc[g][1] for g in neur)
res["composite_projection"] = {"definition": "mean z of 6 progenitor markers minus mean z of 6 neuronal markers; z = (log2CPM+1 - calibration mean) / calibration sd; KO shift of each marker divided by the same sd",
    "calibration_slope_within_line": round(cs, 3), "calibration_r2_within_line": round(cr2, 3), "composite_ko_shift_z_units": round(comp_ko_shift, 3),
    "predicted_ccn2_shift": round(cs * comp_ko_shift, 3), "observed_ccn2_shift": round(obs_shift, 3),
    "caveat": "calibration is an unperturbed spheroid time course, not a KO v WT contrast; the marker shifts rest on 4 v 2 libraries; this projects what a progenitor-state shift of this size would carry, it does not show that one occurred"}
res["coupling_summary"] = {
    "markers_used": len(cp),
    "predicted_shift_range": [round(min(c[5] for c in cp), 3), round(max(c[5] for c in cp), 3)],
    "predicted_shift_median": round(statistics.median(c[5] for c in cp), 3),
    "markers_with_prediction_same_sign_as_observed": sum(1 for c in cp if c[5] > 0),
    "markers_whose_prediction_reaches_half_of_observed": sum(1 for c in cp if c[5] >= 0.5 * obs_shift),
    "observed_shift": round(obs_shift, 3)}
json.dump(res, open(OUT / "organoid_maturation_ctgf.json", "w"), indent=1)
print(json.dumps(res, indent=1))
