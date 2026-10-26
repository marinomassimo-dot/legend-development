#!/usr/bin/env python3
"""Transcript signature of the HIF1A -> PDK -> PDH chain in the WWOX-KO organoid, read against culture time.

Exploratory.  Gene sets and prediction were fixed in prediction_hif1a_pdk_chain_20261025.md before any gene was read.
Reuses the line-aware functions of maturation_calibration.py; nothing is re-implemented.

    python3 hif1a_pdk_chain.py [--json]        per-gene table
    python3 hif1a_pdk_chain.py --set-level     set-level coherence test (the P values the result document quotes)

For each gene: KO-versus-WT log2 shift from the deposited counts of GSE156243 (four KO, two WT libraries) with the authors'
DESeq2 padj when the gene is on the padj<=0.05 list, and the slope of log2 CPM on log10 days in GSE150123 (WWOX-unperturbed
spheroids; elapsed culture time, NOT maturation) with a between-line t interval over the informative lines.
A transcript is not a flux: nothing here measures PDH activity, lactate or ATP.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import random
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import maturation_calibration as mc  # noqa: E402

ISR_SETS = {
    "ATF4_ISR_targets": ["ATF4", "ATF5", "DDIT3", "CHAC1", "TRIB3", "ASNS", "PSAT1", "PHGDH", "PCK2", "SLC7A11", "SESN2", "GADD45A"],
    "UPR_branches": ["XBP1", "HSPA5", "HSP90B1", "DNAJB9", "EIF2AK3", "EIF2AK4", "EIF2S1", "PPP1R15A"],
    "LDH": ["LDHA", "LDHB", "LDHC"],
    "methionine_cysteine": ["MAT2A", "MAT2B", "AHCY", "CBS", "CTH", "GCLC", "GCLM", "GSS", "SLC7A11"],
}

SETS = {
    "HIF1A_glycolytic_targets": ["SLC2A1", "HK2", "PFKP", "ALDOA", "PGK1", "ENO1", "LDHA", "PKM", "BNIP3"],
    "PDK_axis": ["PDK1", "PDK2", "PDK3", "PDK4", "PDHA1", "PDHB", "DLAT", "DLD", "PDP1", "PDP2"],
    "oxidative_arm": ["NDUFA4", "COX4I1", "COX5A", "ATP5F1A", "CS", "SDHA"],
    "HIF1A_and_regulators": ["HIF1A", "EPAS1", "EGLN1", "VHL", "ARNT"],
    "ketone_use": ["OXCT1", "ACAT1", "BDH1", "HMGCS2", "SLC16A1"],
}
LIST05 = HERE / "derived/list_padj_le_0.05.tsv"


def ko_shifts(genes):
    with gzip.open(mc.KO_COUNTS, "rt", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        next(reader)
        rows = {r[0]: [float(x) for x in r[1:]] for r in reader}
    totals = [sum(rows[g][i] for g in rows) for i in range(6)]
    out = {}
    for g in genes:
        if g not in rows:
            out[g] = None
            continue
        cpm = [rows[g][i] / totals[i] * 1e6 for i in range(6)]
        ko, wt = statistics.fmean(cpm[:4]), statistics.fmean(cpm[4:])
        out[g] = {"ko_cpm": round(ko, 2), "wt_cpm": round(wt, 2), "log2_shift": round(math.log2((ko + 1) / (wt + 1)), 3)}
    return out


def padj_table():
    t = {}
    with LIST05.open(encoding="utf-8") as handle:
        for r in csv.DictReader(handle, delimiter="\t"):
            t[r["symbol"]] = (float(r["padj"]), float(r["log2FoldChange"]))
    return t


def time_slopes(genes):
    mc.verify_inputs()
    s2e = mc.symbol_to_ensg()
    wanted = {g: s2e[g] for g in genes if g in s2e}
    meta, data = mc.calibration_matrix(wanted)
    titles = sorted(data)
    days = [float(meta[t]["differentiation day"]) for t in titles]
    lines = [meta[t]["iPSc line"] for t in titles]
    logd = [math.log10(d) for d in days]
    out = {}
    for g in genes:
        if g not in wanted:
            out[g] = None
            continue
        y = [math.log2(data[t]["genes"].get(g, 0.0) / data[t]["total"] * 1e6 + 1) for t in titles]
        mean_count = statistics.fmean(data[t]["genes"].get(g, 0.0) for t in titles)
        sl = mc._line_slopes(lines, logd, y)
        if len(sl) < 3:
            out[g] = None
            continue
        m, sd, k = statistics.fmean(sl.values()), statistics.stdev(sl.values()), len(sl)
        half = mc._T975.get(k - 1, 1.96) * sd / math.sqrt(k)
        out[g] = {"mean_count": round(mean_count, 1), "slope": round(m, 3), "t_interval": [round(m - half, 3), round(m + half, 3)],
                  "lines": k, "ci_excludes_zero": bool(m - half > 0 or m + half < 0)}
    return out


def set_level(draws: int = 10000, seed: int = 20261025) -> dict:
    """Mean KO-versus-WT log2 shift of each pre-declared set against random same-size sets from the expressed universe
    (total count >= 10).  A coherence test, post-selected by construction: the sets were fixed from the chain before reading."""
    with gzip.open(mc.KO_COUNTS, "rt", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        next(reader)
        rows = {r[0]: [float(x) for x in r[1:]] for r in reader}
    totals = [sum(rows[g][i] for g in rows) for i in range(6)]

    def shift(g):
        c = [rows[g][i] / totals[i] * 1e6 for i in range(6)]
        return math.log2((statistics.fmean(c[:4]) + 1) / (statistics.fmean(c[4:]) + 1))

    universe = [g for g in rows if sum(rows[g]) >= 10]
    sh = {g: shift(g) for g in universe}
    rng = random.Random(seed)
    out = {"universe": len(universe), "universe_mean_shift": round(statistics.fmean(sh.values()), 3), "draws": draws, "seed": seed, "sets": {}}
    for name, genes in SETS.items():
        present = [g for g in genes if g in sh]
        obs = statistics.fmean(sh[g] for g in present)
        ge = le = 0
        for _ in range(draws):
            m = statistics.fmean(sh[g] for g in rng.sample(universe, len(present)))
            ge += m >= obs
            le += m <= obs
        out["sets"][name] = {"n": len(present), "mean_shift": round(obs, 3),
                             "p_random_ge": round((ge + 1) / (draws + 1), 4), "p_random_le": round((le + 1) / (draws + 1), 4)}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--set-level", action="store_true", help="set-level coherence test against random same-size sets")
    ap.add_argument("--sets", choices=("chain", "isr"), default="chain",
                    help="chain: HIF1A-PDK-PDH sets (prediction_hif1a_pdk_chain); isr: ATF4/ISR/LDH sets (prediction_isr_ldh_chain)")
    args = ap.parse_args()
    if args.sets == "isr":
        SETS.clear()
        SETS.update(ISR_SETS)
    if args.set_level:
        res = set_level()
        if args.json:
            print(json.dumps(res, indent=1))
        else:
            print(f"expressed universe {res['universe']} genes, mean shift {res['universe_mean_shift']:+.3f}; {res['draws']} draws, seed {res['seed']}")
            for n, r in res["sets"].items():
                print(f"  {n:26s} n={r['n']:2d} mean shift {r['mean_shift']:+.3f}  P(random >= obs)={r['p_random_ge']:.4f}  P(random <= obs)={r['p_random_le']:.4f}")
        return 0
    genes = [g for gs in SETS.values() for g in gs]
    ko, padj, ts = ko_shifts(genes), padj_table(), time_slopes(genes)
    report = {}
    for name, gs in SETS.items():
        rows = []
        for g in gs:
            k = ko.get(g)
            rows.append({"gene": g, "ko": k, "deseq2_padj_log2fc": padj.get(g), "time": ts.get(g)})
        report[name] = rows
    if args.json:
        print(json.dumps(report, indent=1))
        return 0
    for name, rows in report.items():
        print(f"\n== {name}")
        print(f"  {'gene':8s} {'KOcpm':>8s} {'WTcpm':>8s} {'log2shift':>9s} {'padj(<=.05 list)':>17s}   time slope per log10 day [between-line t interval]")
        for r in rows:
            k, t = r["ko"], r["time"]
            pa = f"{r['deseq2_padj_log2fc'][0]:.3g}" if r["deseq2_padj_log2fc"] else "-"
            ks = f"{k['ko_cpm']:8.1f} {k['wt_cpm']:8.1f} {k['log2_shift']:+9.2f}" if k else f"{'absent':>8s} {'':>8s} {'':>9s}"
            ts_ = (f"{t['slope']:+.2f} [{t['t_interval'][0]:+.2f},{t['t_interval'][1]:+.2f}]{'*' if t['ci_excludes_zero'] else ' '} "
                   f"(mean count {t['mean_count']})") if t else "n/a (absent or too few lines)"
            print(f"  {r['gene']:8s} {ks} {pa:>17s}   {ts_}")
    print("\n* = between-line interval excludes zero.  Transcript only; no flux, lactate, ATP or PDH activity is measured.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
