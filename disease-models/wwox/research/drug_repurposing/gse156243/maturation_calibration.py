#!/usr/bin/env python3
"""How much do the canonical Wnt readouts move with maturation ALONE, and could that account for the
WWOX-KO elevation in GSE156243?  Exploratory.  Prediction and calculation were fixed in
prediction_maturation_calibration_20261025.md BEFORE the data were opened.

    python3 maturation_calibration.py [--json]

GSE150123 (wild-type human cortical spheroids, 62 samples, six iPSC lines, 25 to 650+ days) supplies the slope of
each Wnt readout against each maturation marker.  GSE156243 supplies the KO-versus-WT shift of each marker.
Log-scale slopes only; absolute values are never compared across the two datasets.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

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
