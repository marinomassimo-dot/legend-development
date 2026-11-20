#!/usr/bin/env python3
"""Second-system check (system H = GSE126075, human neural stem cells and neurons, WWOX shRNA), as registered in
PREREGISTRATION_INTERACTOME_AND_SECOND_SYSTEM_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md
(sha256 e818cb5bae9f40520eb1c4196a569c8c8c52d8b6a0ea009f85b079f2959e438c).

Hypothesis level; no dose; not medical advice. Held data only, no network. n = 1 per condition: descriptive.
Usage: second_system_h.py --files FILES_DIR --adv099 ADV099_DIR --out OUT_DIR
"""
import argparse
import csv
import gzip
import importlib.util
import os

import numpy as np

SEED = 20261120
NULL_N = 2000
THR_H, THR_N, THR_O = 0.5, 0.25, 0.5
NEU = "STMN2 DCX TUBB3 MAP2 SNAP25 SYT1".split()
PROG = "SOX2 PAX6 HES1 VIM NES FABP7".split()


def rank(a):
    o = np.argsort(a, kind="mergesort")
    r = np.empty(len(a))
    r[o] = np.arange(len(a))
    return r


def load_h(files):
    genes, rows = [], []
    with gzip.open(os.path.join(files, "geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz"), "rt") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        ix = {c: head.index(c) for c in ("hNSC", "Neurons", "hNSC_WWOX_del", "Neurons_WWOX_del")}
        for line in fh:
            a = line.rstrip("\n").split("\t")
            genes.append(a[0].upper())
            rows.append([float(a[ix[c]]) for c in ("hNSC", "Neurons", "hNSC_WWOX_del", "Neurons_WWOX_del")])
    first = {}
    for i, g in enumerate(genes):
        first.setdefault(g, i)
    return genes, np.array(rows), first


def main(files, adv099, out):
    os.makedirs(out, exist_ok=True)
    rng = np.random.default_rng(SEED)
    genes, T, first = load_h(files)
    L = np.log2(T + 1.0)
    # columns: 0 hNSC, 1 Neurons, 2 hNSC_del, 3 Neurons_del
    h_neu = L[:, 3] - L[:, 1]
    h_nsc = L[:, 2] - L[:, 0]
    an_neu = (T[:, 1] >= 1) | (T[:, 3] >= 1)
    an_nsc = (T[:, 0] >= 1) | (T[:, 2] >= 1)
    c_neu = h_neu - np.median(h_neu[an_neu])
    c_nsc = h_nsc - np.median(h_nsc[an_nsc])
    expr_neu = (L[:, 1] + L[:, 3]) / 2
    # maturity flag
    def panel(col):
        n = np.mean([L[first[g], col] for g in NEU if g in first])
        p = np.mean([L[first[g], col] for g in PROG if g in first])
        return n - p
    mat = {"native_neurons": panel(1), "silenced_neurons": panel(3), "native_NSC": panel(0), "silenced_NSC": panel(2)}
    flag = "maturity-confounded" if abs(mat["silenced_neurons"] - mat["native_neurons"]) > 0.5 else "not flagged"
    facts = [["genes_in_table", len(genes)], ["analysed_neuron_pair", int(an_neu.sum())], ["analysed_NSC_pair", int(an_nsc.sum())],
             ["neuron_pair_median_shift", f"{np.median(h_neu[an_neu]):.4f}"], ["NSC_pair_median_shift", f"{np.median(h_nsc[an_nsc]):.4f}"],
             ["NEU_minus_PROG_native_neurons", f"{mat['native_neurons']:.3f}"], ["NEU_minus_PROG_silenced_neurons", f"{mat['silenced_neurons']:.3f}"],
             ["NEU_minus_PROG_native_NSC", f"{mat['native_NSC']:.3f}"], ["NEU_minus_PROG_silenced_NSC", f"{mat['silenced_NSC']:.3f}"],
             ["maturity_flag_neuron_pair", flag]]
    WWOX = first.get("WWOX")
    if WWOX is not None:
        facts.append(["WWOX_TPM_native_neurons_silenced_neurons", f"{T[WWOX,1]:.2f} / {T[WWOX,3]:.2f}"])
        facts.append(["WWOX_TPM_native_NSC_silenced_NSC", f"{T[WWOX,0]:.2f} / {T[WWOX,2]:.2f}"])
    # earlier systems
    spec = importlib.util.spec_from_file_location("adv099", os.path.join(adv099, "adv099_neuron_discovery.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    genes_o, gi_o, an_o, cprime_o, g1, g2, _ = mod.organoid(files)
    o_eff, o_up, o_dn, o_an = {}, {}, {}, {}
    for g, j in gi_o.items():
        if an_o[j]:
            o_eff[g.upper()] = cprime_o[j]
            o_up[g.upper()] = bool(cprime_o[j] >= THR_O and g1[j] >= 0.25 and g2[j] >= 0.25)
            o_dn[g.upper()] = bool(cprime_o[j] <= -THR_O and g1[j] <= -0.25 and g2[j] <= -0.25)
    nuc = {}
    for cls in ("excitatory", "inhibitory"):
        d = {}
        for r in csv.DictReader(open(os.path.join(adv099, "out", f"nuclei_effects_{cls}.tsv")), delimiter="\t"):
            u = r["gene"].upper()
            if u in d:
                continue
            c = float(r["centred_coef"])
            st = int(r["stable_splits_of_20"])
            d[u] = (c, c >= THR_N and st >= 18, c <= -THR_N and st >= 18)
        nuc[cls] = d
    # concordance (Spearman) of h with each system
    conc = []
    def bins_of(idx, vals):
        order = idx[np.argsort(vals[idx])]
        return np.array_split(order, 10)
    for label, eff in [("nuclei_excitatory", {g: v[0] for g, v in nuc["excitatory"].items()}),
                       ("nuclei_inhibitory", {g: v[0] for g, v in nuc["inhibitory"].items()}), ("organoid", o_eff)]:
        common = [g for g in eff if g in first and an_neu[first[g]]]
        a = np.array([eff[g] for g in common])
        b = np.array([c_neu[first[g]] for g in common])
        e = np.array([expr_neu[first[g]] for g in common])
        rho = float(np.corrcoef(rank(a), rank(b))[0, 1])
        bins = np.array_split(np.argsort(e), 10)
        ra = rank(a)
        nulls = np.empty(NULL_N)
        rb0 = rank(b)
        for k in range(NULL_N):
            rb = np.empty(len(b))
            for bn in bins:
                rb[bn] = rb0[bn][rng.permutation(len(bn))]
            nulls[k] = np.corrcoef(ra, rb)[0, 1]
        lo, hi = np.percentile(nulls, [2.5, 97.5])
        # also NSC pair for reference
        common2 = [g for g in eff if g in first and an_nsc[first[g]]]
        rho2 = float(np.corrcoef(rank(np.array([eff[g] for g in common2])), rank(np.array([c_nsc[first[g]] for g in common2])))[0, 1]) if len(common2) > 10 else float("nan")
        conc.append([label, len(common), f"{rho:.3f}", f"{lo:.3f}", f"{hi:.3f}", f"{rho2:.3f}"])
    # pair and triple counts
    h_up = np.array([bool(c_neu[i] >= THR_H and an_neu[i]) for i in range(len(genes))])
    h_dn = np.array([bool(c_neu[i] <= -THR_H and an_neu[i]) for i in range(len(genes))])
    rows = []
    def count_block(name, universe, flagsA, hflag):
        """universe: list of gene symbols (upper); flagsA: bool array aligned to universe; hflag: bool array over H table."""
        idx = np.array([first[g] for g in universe])
        hf = hflag[idx]
        obs = int((flagsA & hf).sum())
        bins = np.array_split(np.argsort(expr_neu[idx]), 10)
        nulls = np.empty(NULL_N, int)
        for k in range(NULL_N):
            c = 0
            for bn in bins:
                c += int((flagsA[bn] & hf[bn][rng.permutation(len(bn))]).sum())
            nulls[k] = c
        p975 = float(np.percentile(nulls, 97.5))
        rows.append(name + [int(flagsA.sum()), int(hf.sum()), obs, f"{np.mean(nulls):.2f}", f"{p975:.1f}",
                            "REPLICATES_BEYOND_CHANCE" if obs > p975 else "NOTHING_REPLICATES_BEYOND_CHANCE"])
    for cls in ("excitatory", "inhibitory"):
        for d, (hflag, nidx) in (("UP", (h_up, 1)), ("DOWN", (h_dn, 2))):
            uni = [g for g in nuc[cls] if g in first and an_neu[first[g]]]
            fl = np.array([nuc[cls][g][nidx] for g in uni])
            count_block(["N_and_H", cls, d], uni, fl, hflag)
            uni3 = [g for g in uni if g in o_eff]
            fl3 = np.array([nuc[cls][g][nidx] and (o_up[g] if d == "UP" else o_dn[g]) for g in uni3])
            count_block(["N_and_O_and_H", cls, d], uni3, fl3, hflag)
    for d, (hflag, od) in (("UP", (h_up, o_up)), ("DOWN", (h_dn, o_dn))):
        uni = [g for g in o_eff if g in first and an_neu[first[g]]]
        fl = np.array([od[g] for g in uni])
        count_block(["O_and_H", "organoid", d], uni, fl, hflag)
    def wr(name, header, rws):
        with open(os.path.join(out, name), "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(header)
            w.writerows([list(r) + [""] * (len(header) - len(r)) for r in rws])
    wr("system_h_facts.tsv", ["fact", "value"], facts)
    wr("concordance_spearman.tsv", ["against", "n_genes", "spearman_h_neuron_pair", "null_p2.5", "null_p97.5", "spearman_h_NSC_pair"], conc)
    wr("replication_counts.tsv", ["test", "class", "direction", "n_pass_A", "n_pass_H", "observed", "null_mean", "null_p97.5", "verdict"], rows)
    for r in conc:
        print("\t".join(str(x) for x in r))
    for r in rows:
        print("\t".join(str(x) for x in r))
    for f in facts:
        print(f[0], f[1])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Second-system check on GSE126075 (registered rule, held data only).")
    ap.add_argument("--files", required=True, help="the files/ directory of the checkout")
    ap.add_argument("--adv099", required=True, help="the adv099_neuron_discovery_sci_20261120 directory (script and out/)")
    ap.add_argument("--out", required=True, help="output directory")
    a = ap.parse_args()
    main(a.files, a.adv099, a.out)
