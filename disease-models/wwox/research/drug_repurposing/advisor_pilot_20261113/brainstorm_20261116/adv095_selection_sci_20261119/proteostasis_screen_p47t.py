#!/usr/bin/env python3
"""ADV-095: proteostasis and HSP70-type premise screen in the held P47T tables, as registered in
PREREGISTRATION_PROTEOSTASIS_SCREEN_P47T_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md
(sha256 04168139622376cb0e2f367eefc48dd6dd2cd34ad02540b82051d12a15db5ef7).

Hypothesis level; no dose; not medical advice. Held data only, no network.
Usage: proteostasis_screen_p47t.py --table PATH_TO_GSE215425_processed_data.csv.gz --out OUT_DIR
"""
import argparse
import csv
import gzip
import os

import numpy as np

SETS = {
    "HSR": "Hspa1a Hspa1b Hsph1 Dnajb1 Hspb1 Hsp90aa1 Dnaja4 Bag3".split(),
    "HSP70_CONSTITUTIVE": "Hspa8 Hspa4 Hspa9 Hspa2 Dnaja1 Dnajb6 Stip1 Hsp90ab1".split(),
    "ER_CHAPERONE_UPR": "Hspa5 Hsp90b1 Pdia3 Pdia4 Pdia6 Calr Canx Hyou1 Dnajb9 Herpud1 Sel1l Edem1".split(),
    "AUTOPHAGY_LYSOSOME": "Lamp1 Lamp2 Ctsd Ctsb Ctsz Hexa Hexb Gusb Npc2 Sqstm1 Map1lc3b Tfeb".split(),
    "PROTEASOME": "Psma1 Psma2 Psma3 Psmb5 Psmb6 Psmc1 Psmd1 Psmd2".split(),
}
COV = {
    "ASTRO_REACT": "Gfap Serpina3n Lcn2 C3 Vim".split(),
    "MICROGLIA": "Aif1 Cd68 Tyrobp Trem2 Itgam".split(),
    "NEURON": "Snap25 Rbfox3 Syt1 Stmn2 Map2".split(),
}
REGIONS = ["PFC", "HPC", "CTX", "CB"]
CEREBRAL = ["PFC", "HPC", "CTX"]
NULL_N = 5000
SEED = 20261120
SD_FLOOR = 0.5


def load(path):
    with gzip.open(path, "rt") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        samples = head[2:]
        symbols, rows = [], []
        for line in fh:
            a = line.rstrip("\n").split("\t")
            symbols.append(a[1])
            rows.append([float(x) for x in a[2:]])
    return samples, symbols, np.array(rows)


def design(samples, region):
    idx = [i for i, s in enumerate(samples) if s.startswith(region + "_")]
    ko = np.array([1.0 if "P47T/P47T" in samples[i] else 0.0 for i in idx])
    sex = np.array([1.0 if samples[i].split("_")[-1].startswith("F") else 0.0 for i in idx])
    return idx, ko, sex


def ols_coef(y, X):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    return beta, resid


def main(table, out):
    os.makedirs(out, exist_ok=True)
    samples, symbols, counts = load(table)
    lib = counts.sum(axis=0)
    lcpm = np.log2(counts / lib * 1e6 + 1.0)
    # gene index: sum counts of duplicated symbols is not needed; keep first occurrence, record duplicates
    seen, dup = {}, set()
    for i, s in enumerate(symbols):
        if s in seen:
            dup.add(s)
        else:
            seen[s] = i
    rng = np.random.default_rng(SEED)
    summary, genelist = [], []
    for region in REGIONS:
        idx, ko, sex = design(samples, region)
        L = lcpm[:, idx]
        mean_l = L.mean(axis=1)
        mean_cpm = (counts[:, idx] / lib[idx] * 1e6).mean(axis=1)
        z = (L - L.mean(axis=1, keepdims=True)) / np.where(L.std(axis=1, keepdims=True) > 0, L.std(axis=1, keepdims=True), 1.0)
        X0 = np.column_stack([np.ones(len(idx)), ko, sex])
        ctrl = ko == 0
        covscore = {}
        for cname, genes in COV.items():
            gi = [seen[g] for g in genes if g in seen and mean_cpm[seen[g]] >= 1.0]
            covscore[cname] = z[gi].mean(axis=0) if gi else np.zeros(len(idx))
        Xadj = np.column_stack([X0] + [covscore[c] for c in COV])
        pool = np.where(mean_cpm >= 1.0)[0]
        for sname, genes in SETS.items():
            present = [g for g in genes if g in seen]
            missing = [g for g in genes if g not in seen]
            use = [seen[g] for g in present if mean_cpm[seen[g]] >= 1.0]
            low = [g for g in present if mean_cpm[seen[g]] < 1.0]
            for g in present:
                gi = seen[g]
                beta, _ = ols_coef(z[gi], X0)
                genelist.append([region, sname, g, f"{mean_cpm[gi]:.2f}", f"{beta[1]:.3f}", "" if mean_cpm[gi] >= 1.0 else "below floor"])
            if len(use) < 3:
                summary.append([region, sname, len(use), ";".join(missing + low), "", "", "", "", "", "", "UNDECIDED (fewer than three genes)"])
                continue
            score = z[use].mean(axis=0)
            beta, resid = ols_coef(score, X0)
            sd_c = float(np.std(resid[ctrl], ddof=1)) if ctrl.sum() > 1 else float("nan")
            # use the residual SD of the whole fit if the control arm SD is degenerate
            sd = sd_c if sd_c == sd_c and sd_c > 0 else float(np.std(resid, ddof=1))
            raw = float(beta[1])
            shift_sd = raw / sd
            betaA, _ = ols_coef(score, Xadj)
            adj = float(betaA[1])
            # matched null
            nulls = np.empty(NULL_N)
            for k in range(NULL_N):
                pick = []
                for gi in use:
                    d = np.abs(mean_l[pool] - mean_l[gi])
                    near = pool[np.argsort(d)[:200]]
                    near = near[~np.isin(near, use)]
                    pick.append(int(rng.choice(near)))
                sc = z[pick].mean(axis=0)
                b, _ = ols_coef(sc, X0)
                nulls[k] = b[1]
            lo_e, hi_e = np.percentile(nulls, [2.5, 97.5])
            outside = raw < lo_e or raw > hi_e
            if outside and abs(shift_sd) >= SD_FLOOR:
                call = "SHIFT_UP" if raw > 0 else "SHIFT_DOWN"
            else:
                call = "FLAT"
            same_sign = (adj > 0) == (raw > 0)
            summary.append([region, sname, len(use), ";".join(missing + low), f"{raw:.3f}", f"{shift_sd:.2f}", f"{lo_e:.3f}",
                            f"{hi_e:.3f}", f"{adj:.3f}", "same" if same_sign else "differs", call])
    # per-set verdicts over the three cerebral regions
    verdicts = []
    for sname in SETS:
        rows = {r[0]: r for r in summary if r[1] == sname}
        calls = {reg: rows[reg][10] for reg in CEREBRAL if reg in rows}
        ups = [reg for reg, c in calls.items() if c == "SHIFT_UP" and rows[reg][9] == "same"]
        downs = [reg for reg, c in calls.items() if c == "SHIFT_DOWN" and rows[reg][9] == "same"]
        if sname in ("HSR", "ER_CHAPERONE_UPR"):
            if len(ups) >= 2:
                v = "PREMISE_SUPPORTED_T (load premise: engaged in %s)" % ",".join(ups)
            elif len(downs) >= 2:
                v = "PREMISE_OPPOSITE_T (reduced in %s)" % ",".join(downs)
            else:
                v = "NOT_SUPPORTED_T"
        elif sname == "AUTOPHAGY_LYSOSOME":
            if len(ups) >= 2:
                v = "PREMISE_SUPPORTED_T (load premise: engaged in %s)" % ",".join(ups)
            elif len(downs) >= 2:
                v = "PREMISE_OPPOSITE_T (reduced in %s)" % ",".join(downs)
            else:
                v = "NOT_SUPPORTED_T"
        else:  # HSP70_CONSTITUTIVE, PROTEASOME: direction read as capacity; no opposite verdict is registered
            if len(ups) >= 2 or len(downs) >= 2:
                v = "SHIFT_REPORTED (%s)" % (",".join(ups) + "|up" if len(ups) >= 2 else ",".join(downs) + "|down")
            else:
                v = "NOT_SUPPORTED_T"
        reg_one = [reg for reg, c in calls.items() if c in ("SHIFT_UP", "SHIFT_DOWN")]
        note = "region-specific only" if len(reg_one) == 1 else ""
        cb = rows.get("CB")
        verdicts.append([sname, ";".join(f"{r}:{c}" for r, c in calls.items()), f"CB:{cb[10]}" if cb else "", v, note])
    with open(os.path.join(out, "proteostasis_set_summary.tsv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["region", "set", "n_genes_scored", "missing_or_below_floor", "raw_coef_z", "raw_shift_in_control_resid_SD",
                    "null_p2.5", "null_p97.5", "adjusted_coef_z", "adjusted_sign_vs_raw", "registered_call"])
        w.writerows(summary)
    with open(os.path.join(out, "proteostasis_gene_level.tsv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["region", "set", "gene", "mean_cpm", "genotype_coef_z_unadjusted_sex_only", "note"])
        w.writerows(genelist)
    with open(os.path.join(out, "proteostasis_verdicts.tsv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["set", "cerebral_region_calls", "cerebellum_call", "registered_verdict", "note"])
        w.writerows(verdicts)
    print("duplicated symbols in table (first occurrence used):", len(dup))
    for v in verdicts:
        print("\t".join(v))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Proteostasis premise screen in the held P47T tables (registered rule, held data only).")
    ap.add_argument("--table", required=True, help="path to GSE215425_processed_data.csv.gz")
    ap.add_argument("--out", required=True, help="output directory")
    a = ap.parse_args()
    main(a.table, a.out)
