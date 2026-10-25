#!/usr/bin/env python3
"""How much do the canonical Wnt readouts move with maturation ALONE, and could that account for the
WWOX-KO elevation in GSE156243?  Exploratory.  Prediction and calculation were fixed in
prediction_maturation_calibration_20261025.md BEFORE the data were opened.

    python3 maturation_calibration.py [--json]

GSE150123 (wild-type human cortical spheroids, 62 samples, six iPSC lines, 25 to 650+ days) supplies the slope of
each Wnt readout against each maturation marker.  GSE156243 supplies the KO-versus-WT shift of each marker.
Log-scale slopes only; absolute values are never compared across the two datasets.

TERMINOLOGY. GSE150123 holds WWOX-UNPERTURBED samples: no WWOX manipulation, WWOX genotype not otherwise
characterised. They are not "wild type" in any verified sense and they are not WWOX-null.  ELAPSED culture time is what
the dataset records; cellular maturation is not measured, and the two are not the same thing.

    python3 maturation_calibration.py --time-course [--json]

reproduces every statement the result document makes about the time course: per-line slopes with a between-line
interval, a line-cluster bootstrap, the slope restricted to day >= 60, the quadratic (nonlinearity) test, leave-one-
line-out, and the day-bin means.  The 62 samples come from six iPSC lines and are NOT 62 independent replicates: after
centring on the line, one line (a single sample) carries no information and one carries two, so the informative
clusters are five.  Uncertainty is therefore reported between lines, and with five clusters it is wide and said so.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import random
import re
import statistics
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def _files_root() -> Path:
    """`files/` is gitignored and lives in the main checkout, not in a task worktree."""
    for base in (ROOT, *ROOT.parents):
        if (base / "files/geo").is_dir():
            return base / "files"
    raise SystemExit("no files/geo found above " + str(ROOT))


FILES = _files_root()
CAL_TAR = FILES / "geo/GSE150123/GSE150123_RAW.tar"
CAL_META = FILES / "geo/GSE150123/GSE150123_series_matrix.txt.gz"
KO_COUNTS = FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"
HGNC = FILES / "geo/GSE156243/hgnc_complete_set_20261022.json"

# Inputs are pinned by digest: "reproducible from retained data" has to fail loudly if the data changed.
PINNED = {"GSE150123_RAW.tar": "347efe3e75ba167488cbe058645ffab1a1921869bc9ef161b6106a8374470a72",
          "GSE150123_series_matrix.txt.gz": "f02bfae912706f622f550ac94b31e79744e71a45a1a3f6d79fbfcf3ed793093c"}

WNT = ["AXIN2", "LEF1", "NKD1", "APCDD1"]
PROGENITOR = ["VIM", "NES", "SOX9", "SOX2", "PAX6", "HES1"]
NEURONAL = ["STMN2", "MAP2", "SYT1", "RBFOX3", "TUBB3", "SNAP25"]
MIN_MEAN_COUNT = 5.0


def symbol_to_ensg() -> dict[str, str]:
    docs = json.loads(HGNC.read_text(encoding="utf-8"))
    docs = (docs.get("response") or docs).get("docs") or docs.get("docs") or []
    return {d["symbol"]: d["ensembl_gene_id"] for d in docs if d.get("ensembl_gene_id")}


def calibration_matrix(wanted: dict[str, str]):
    """sample title -> {symbol: count}, plus library size, from the per-sample count files."""
    meta = {}
    with gzip.open(CAL_META, "rt", encoding="utf-8") as handle:
        rows = [l.rstrip("\n").split("\t") for l in handle if l.startswith("!Sample_")]
    titles = [x.strip('"') for x in next(r for r in rows if r[0] == "!Sample_title")[1:]]
    chars = [r for r in rows if r[0] == "!Sample_characteristics_ch1"]
    for i, t in enumerate(titles):
        rec = {}
        for r in chars:
            k, _, v = r[1 + i].strip('"').partition(":")
            rec[k.strip()] = v.strip()
        meta[t] = rec
    inv = {v: k for k, v in wanted.items()}
    data = {}
    with tarfile.open(CAL_TAR) as tar:
        for member in tar.getmembers():
            if not member.name.endswith(".csv.gz"):
                continue
            with gzip.open(tar.extractfile(member), "rt", encoding="utf-8") as handle:
                reader = csv.reader(handle)
                header = next(reader)
                title = header[1]
                total = 0.0
                got = {}
                for row in reader:
                    c = float(row[1])
                    total += c
                    if row[0] in inv:
                        got[inv[row[0]]] = c
                data[title] = {"genes": got, "total": total}
    return meta, data


def ols(x: list[float], y: list[float]):
    n = len(x)
    mx, my = statistics.fmean(x), statistics.fmean(y)
    sxx = sum((a - mx) ** 2 for a in x)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    slope = sxy / sxx
    resid = [b - (my + slope * (a - mx)) for a, b in zip(x, y)]
    s2 = sum(r * r for r in resid) / (n - 2)
    se = math.sqrt(s2 / sxx)
    ss_tot = sum((b - my) ** 2 for b in y)
    r2 = 1 - sum(r * r for r in resid) / ss_tot if ss_tot else float("nan")
    return slope, se, r2


def demean_by(groups: list[str], v: list[float]) -> list[float]:
    """Within-line demeaning: removes the line effect so the slope is not carried by line differences."""
    by: dict[str, list[float]] = {}
    for g, x in zip(groups, v):
        by.setdefault(g, []).append(x)
    mean = {g: statistics.fmean(xs) for g, xs in by.items()}
    return [x - mean[g] for g, x in zip(groups, v)]


def _sha256(path: Path) -> str:
    import hashlib
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_inputs() -> None:
    for name, want in PINNED.items():
        path = next(p for p in (CAL_TAR, CAL_META) if p.name == name)
        got = _sha256(path)
        if got != want:
            raise SystemExit(f"{name}: sha256 {got} != pinned {want}; the retained data changed, the result is not reproducible")


def _line_slopes(lines, x, y):
    """One within-line slope per line that has at least two distinct x values; returns {line: slope}."""
    out = {}
    for L in sorted(set(lines)):
        idx = [i for i, l in enumerate(lines) if l == L]
        xs = [x[i] for i in idx]
        if len(idx) < 2 or len(set(xs)) < 2:
            continue
        mx, my = statistics.fmean(xs), statistics.fmean(y[i] for i in idx)
        sxx = sum((a - mx) ** 2 for a in xs)
        out[L] = sum((a - mx) * (y[i] - my) for a, i in zip(xs, idx)) / sxx
    return out


# two-sided 97.5th percentile of Student t by degrees of freedom (1..9), enough for the handful of lines here
_T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}


def _pooled(lines, x, y):
    """Within-line pooled OLS slope (line effects removed), the estimator used throughout."""
    return ols(demean_by(lines, x), demean_by(lines, y))[0]


def _cluster_bootstrap(lines, x, y, draws, seed):
    rng = random.Random(seed)
    ls = [l for l in sorted(set(lines)) if sum(1 for q in lines if q == l) >= 2]
    by = {l: [i for i, q in enumerate(lines) if q == l] for l in ls}
    vals = []
    for _ in range(draws):
        pick = [rng.choice(ls) for _ in ls]
        idx, lab = [], []
        for k, l in enumerate(pick):
            for i in by[l]:
                idx.append(i)
                lab.append(f"{l}#{k}")
        try:
            vals.append(_pooled(lab, [x[i] for i in idx], [y[i] for i in idx]))
        except ZeroDivisionError:
            continue
    vals.sort()
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals))], len(ls)


def time_course(draws: int = 4000, seed: int = 20261025) -> dict:
    verify_inputs()
    s2e = symbol_to_ensg()
    wanted = {g: s2e[g] for g in WNT}
    meta, data = calibration_matrix(wanted)
    titles = sorted(data)
    days = [float(meta[t]["differentiation day"]) for t in titles]
    lines = [meta[t]["iPSc line"] for t in titles]
    logd = [math.log10(d) for d in days]
    per_line_n = {l: lines.count(l) for l in sorted(set(lines))}
    informative = [l for l, n in per_line_n.items() if n >= 2]

    def l2(t, g):
        d = data[t]
        return math.log2(d["genes"].get(g, 0.0) / d["total"] * 1e6 + 1)

    out = {"n_samples": len(titles), "samples_per_line": per_line_n, "informative_lines": informative,
           "day_range": [min(days), max(days)], "bootstrap_draws": draws, "seed": seed, "genes": {}}
    for g in WNT:
        y = [l2(t, g) for t in titles]
        rec = {}
        # (a) full range: pooled slope, per-line slopes + between-line t interval, line-cluster bootstrap
        pooled = _pooled(lines, logd, y)
        sl = _line_slopes(lines, logd, y)
        m, sd, k = statistics.fmean(sl.values()), statistics.stdev(sl.values()), len(sl)
        half = _T975.get(k - 1, 1.96) * sd / math.sqrt(k)
        lo, hi, nclu = _cluster_bootstrap(lines, logd, y, draws, seed)
        rec["full_range"] = {"pooled_slope": round(pooled, 3), "per_line_slopes": {l: round(v, 3) for l, v in sl.items()},
                             "mean_of_line_slopes": round(m, 3), "between_line_t_interval": [round(m - half, 3), round(m + half, 3)],
                             "lines_used": k, "cluster_bootstrap_95": [round(lo, 3), round(hi, 3)], "bootstrap_clusters": nclu}
        # (b) restricted to day >= 60 (the window a 15-week organoid sits in)
        keep = [i for i, d in enumerate(days) if d >= 60]
        ly, lx, lyy = [lines[i] for i in keep], [logd[i] for i in keep], [y[i] for i in keep]
        sl60 = _line_slopes(ly, lx, lyy)
        m60, sd60, k60 = statistics.fmean(sl60.values()), statistics.stdev(sl60.values()), len(sl60)
        half60 = _T975.get(k60 - 1, 1.96) * sd60 / math.sqrt(k60)
        lo60, hi60, _ = _cluster_bootstrap(ly, lx, lyy, draws, seed)
        rec["day_ge_60"] = {"n_samples": len(keep), "pooled_slope": round(_pooled(ly, lx, lyy), 3),
                            "mean_of_line_slopes": round(m60, 3), "between_line_t_interval": [round(m60 - half60, 3), round(m60 + half60, 3)],
                            "lines_used": k60, "cluster_bootstrap_95": [round(lo60, 3), round(hi60, 3)],
                            "interval_includes_zero": bool((m60 - half60) <= 0 <= (m60 + half60))}
        # (c) nonlinearity: quadratic term in log10 day, with a cluster bootstrap for its sign
        q = [v * v for v in logd]
        lin_res = demean_by(lines, y)
        xs, qs = demean_by(lines, logd), demean_by(lines, q)
        b1 = ols(xs, lin_res)[0]
        resid = [a - b1 * c for a, c in zip(lin_res, xs)]
        bq, seq, _ = ols(qs, resid)
        rec["quadratic"] = {"coefficient": round(bq, 3), "naive_t_treating_samples_as_independent": round(bq / seq, 2),
                            "note": "the naive t is shown only to be compared with the line-level view; it overstates precision"}
        # (d) leave-one-line-out of the pooled slope
        loo = {}
        for L in informative:
            idx = [i for i, l in enumerate(lines) if l != L]
            loo[L] = round(_pooled([lines[i] for i in idx], [logd[i] for i in idx], [y[i] for i in idx]), 3)
        rec["leave_one_line_out_pooled_slope"] = loo
        rec["loo_sign_stable"] = bool(all(v * pooled > 0 for v in loo.values()))
        # (e) day-bin means (line-centred)
        yc = demean_by(lines, y)
        bins = {}
        for lo_d, hi_d in ((25, 60), (60, 110), (110, 230), (230, 400), (400, 700)):
            idx = [i for i, d in enumerate(days) if lo_d <= d < hi_d]
            bins[f"{lo_d}-{hi_d}"] = {"n": len(idx), "mean": round(statistics.fmean(yc[i] for i in idx), 3)}
        rec["day_bins_line_centred_mean"] = bins
        out["genes"][g] = rec
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--time-course", action="store_true", help="the line-aware time-course analysis the result document reports")
    args = ap.parse_args()
    if args.time_course:
        res = time_course()
        if args.json:
            print(json.dumps(res, indent=1))
            return 0
        print(f"{res['n_samples']} samples from {len(res['samples_per_line'])} lines {res['samples_per_line']}; "
              f"informative lines {res['informative_lines']}; days {res['day_range'][0]:.0f}-{res['day_range'][1]:.0f}")
        for g, r in res["genes"].items():
            f, d = r["full_range"], r["day_ge_60"]
            print(f"\n{g}\n  full range : pooled {f['pooled_slope']:+.2f}  mean of {f['lines_used']} line slopes {f['mean_of_line_slopes']:+.2f} "
                  f"t-int {f['between_line_t_interval']}  cluster-boot {f['cluster_bootstrap_95']}  per-line {f['per_line_slopes']}")
            print(f"  day >= 60  : pooled {d['pooled_slope']:+.2f}  mean of {d['lines_used']} line slopes {d['mean_of_line_slopes']:+.2f} "
                  f"t-int {d['between_line_t_interval']}  cluster-boot {d['cluster_bootstrap_95']}  includes 0: {d['interval_includes_zero']}")
            print(f"  quadratic  : {r['quadratic']['coefficient']:+.3f} (naive t {r['quadratic']['naive_t_treating_samples_as_independent']})")
            print(f"  leave-one-line-out pooled slope: {r['leave_one_line_out_pooled_slope']}  sign stable: {r['loo_sign_stable']}")
            print(f"  day-bin means: {r['day_bins_line_centred_mean']}")
        return 0

    s2e = symbol_to_ensg()
    genes = WNT + PROGENITOR + NEURONAL
    wanted = {g: s2e[g] for g in genes if g in s2e}
    missing = [g for g in genes if g not in wanted]

    meta, data = calibration_matrix(wanted)
    titles = sorted(data)
    days = [float(meta[t]["differentiation day"]) for t in titles]
    lines = [meta[t]["iPSc line"] for t in titles]
    logd = [math.log10(d) for d in days]

    def l2cpm(t, g):
        d = data[t]
        return math.log2(d["genes"].get(g, 0.0) / d["total"] * 1e6 + 1)

    expr = {g: [l2cpm(t, g) for t in titles] for g in wanted}
    expressed = {g: statistics.fmean(data[t]["genes"].get(g, 0.0) for t in titles) >= MIN_MEAN_COUNT for g in wanted}

    report = {"n_samples": len(titles), "lines": sorted(set(lines)), "day_range": [min(days), max(days)],
              "missing_symbols": missing, "not_expressed_in_calibration": [g for g in wanted if not expressed[g]],
              "slope_vs_log10_days": {}, "coupling": {}, "predicted": {}}

    for g in wanted:
        if not expressed[g]:
            continue
        sl, se, r2 = ols(demean_by(lines, logd), demean_by(lines, expr[g]))
        report["slope_vs_log10_days"][g] = {"slope": round(sl, 3), "se": round(se, 3), "r2_within_line": round(r2, 3)}

    # KO-versus-WT log2 shift of each marker in GSE156243, from library-size-normalised counts
    ko = {}
    with gzip.open(KO_COUNTS, "rt", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        next(reader)
        rows = {r[0]: [float(x) for x in r[1:]] for r in reader}
    totals = [sum(rows[g][i] for g in rows) for i in range(6)]
    for g in wanted:
        if g not in rows:
            continue
        cpm = [rows[g][i] / totals[i] * 1e6 for i in range(6)]
        ko[g] = math.log2((statistics.fmean(cpm[:4]) + 1) / (statistics.fmean(cpm[4:]) + 1))
    report["ko_vs_wt_log2_shift"] = {g: round(v, 3) for g, v in ko.items()}

    for w in WNT:
        if w not in report["slope_vs_log10_days"] or w not in ko:
            continue
        for panel_name, panel in (("progenitor", PROGENITOR), ("neuronal", NEURONAL)):
            for m in panel:
                if m not in wanted or not expressed.get(m) or m not in ko:
                    continue
                sl, se, r2 = ols(demean_by(lines, expr[m]), demean_by(lines, expr[w]))
                pred = sl * ko[m]
                report["coupling"].setdefault(w, {})[m] = {
                    "panel": panel_name, "slope_wnt_on_marker": round(sl, 3), "r2": round(r2, 3),
                    "marker_ko_shift": round(ko[m], 3), "predicted_wnt_shift": round(pred, 3)}
        preds = [v["predicted_wnt_shift"] for v in report["coupling"].get(w, {}).values()]
        if preds:
            obs = ko[w]
            report["predicted"][w] = {
                "observed_ko_shift": round(obs, 3), "n_markers": len(preds),
                "predicted_median": round(statistics.median(preds), 3),
                "predicted_min": round(min(preds), 3), "predicted_max": round(max(preds), 3),
                "fraction_explained_median": round(statistics.median(preds) / obs, 2) if obs else None}

    if args.json:
        print(json.dumps(report, indent=1))
        return 0
    print(f"calibration: {report['n_samples']} samples, lines {report['lines']}, day {report['day_range'][0]:.0f}-{report['day_range'][1]:.0f}")
    print("missing symbols:", missing, "| not expressed in calibration:", report["not_expressed_in_calibration"])
    print("\nWithin-line slope of log2 CPM on log10 days:")
    for g, v in report["slope_vs_log10_days"].items():
        print(f"  {g:7s} {v['slope']:+.3f} (se {v['se']:.3f}, r2 {v['r2_within_line']:.2f})")
    print("\nKO-vs-WT log2 shift in GSE156243:", report["ko_vs_wt_log2_shift"])
    print("\nWnt shift predicted from maturation alone:")
    for g, v in report["predicted"].items():
        print(f"  {g:7s} observed {v['observed_ko_shift']:+.2f}  predicted median {v['predicted_median']:+.2f} "
              f"[{v['predicted_min']:+.2f}, {v['predicted_max']:+.2f}] over {v['n_markers']} markers  "
              f"fraction explained {v['fraction_explained_median']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
