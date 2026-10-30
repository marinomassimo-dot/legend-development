#!/usr/bin/env python3
"""Signature route of the IT9 P2 engine (secondary arm): opposition of the seed vector in LINCS GSE92742 level 5 compound signatures of neural-lineage cells.

For each trt_cp signature in a progenitor-like (NPC*) or neuron-like (NEU*, MNEU.E) context: O = - sum_g s_g z_g / sum |s_g| over seed genes present in the L1000 space,
z divided by the signature's MAD scale (as IT7). Family score = median over its signatures in the class. Two uncertain-direction arms (U+, U-) as in the network arms.
Informative only if (i) its seed-specificity beats random matched readouts and (ii) cross-context reproducibility (progenitor-like vs neuron-like) exceeds the 95th percentile of
random matched readouts (IT7 C1 logic). Reports, never evaluates against the IT7 held-out outcome (evaluation_guard of P1 Q2). Wild-type cells: it measures compound response
of a normal neural context against the seed signature, not any WWOX-deficient response.

  seed_sig_arm.py --seeds FILE --geo DIR --cache DIR --catalog PATH --label L --out DIR [--nnull 300]
  geo: GSE92742_Broad_LINCS_{sig_info,pert_info,gene_info}.txt.gz ; cache: extract.npy, extract_rows.tsv, extract_genes.json (IT3 extract of level 5)
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, gzip, json, os, math
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.argv_backup = sys.argv
import importlib.util
spec = importlib.util.spec_from_file_location("seed_engine", HERE / "seed_engine.py")
# seed_engine prints its docstring when argv[1] is -h; here argv[1] is a flag of this script, so load with a neutral argv
_saved = sys.argv; sys.argv = ["seed_engine.py", "selftest"]
se = importlib.util.module_from_spec(spec); spec.loader.exec_module(se); sys.argv = _saved
ap = argparse.ArgumentParser()
for k in ("seeds", "geo", "cache", "catalog", "label", "out"):
    ap.add_argument("--" + k, required=True)
ap.add_argument("--nnull", type=int, default=300)
a = ap.parse_args()
BC, EC = {"NPC", "NPC.CAS9", "NPC.TAK"}, {"NEU", "NEU.KCL", "MNEU.E"}
rd = lambda p: csv.DictReader(gzip.open(p, "rt", encoding="utf-8"), delimiter="\t")
seeds = se.load_seeds(a.seeds)
n_all = len(seeds)
seeds = se.Seeds(se.sig_eligible(seeds.units))     # guard_tag exclusion (Amendment 4): IT7_READOUT6, ISR_SIGN_UNRESOLVED, HELD_OUT_ENDPOINT units never enter the signature arm
if len(seeds) == 0:
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    (out / f"sig_{a.label}.json").write_text(json.dumps(dict(label=a.label, seed_units_total=n_all, seed_units_excluded_by_guard=n_all, error="no eligible seed units after guard_tag exclusion"), indent=1) + "\n")
    print("no eligible seed units after guard exclusion"); raise SystemExit(0)
# family of each perturbagen via the catalogue skeleton key
sys.path.insert(0, str(se.REPO / "framework/scripts"))
import compound_catalog as cc, repurposing_search as rs
entries = cc.load(Path(a.catalog)); idx = rs.Index(entries, rs.load_artefacts())
skel2fam = collections.defaultdict(set)
for e in entries:
    k = (e.get("ids") or {}).get("skeleton_key")
    if k: skel2fam[k].add(idx.family[e["id"]])
pert2fam = {}
for r in rd(Path(a.geo) / "GSE92742_Broad_LINCS_pert_info.txt.gz"):
    if r["pert_type"] == "trt_cp" and r["inchi_key"] not in ("-666", ""):
        f = skel2fam.get(r["inchi_key"].split("-")[0])
        if f: pert2fam[r["pert_id"]] = f
rowidx = {r["sig_id"]: int(r["row"]) for r in csv.DictReader(open(Path(a.cache) / "extract_rows.tsv"), delimiter="\t")}
sigs = []
for r in rd(Path(a.geo) / "GSE92742_Broad_LINCS_sig_info.txt.gz"):
    if r["pert_type"] != "trt_cp" or r["pert_id"] not in pert2fam or r["sig_id"] not in rowidx: continue
    cl = "B" if r["cell_id"] in BC else "E" if r["cell_id"] in EC else None
    if cl:
        for f in sorted(pert2fam[r["pert_id"]]): sigs.append((rowidx[r["sig_id"]], cl, f))
sigs.sort()
ent = json.load(open(Path(a.cache) / "extract_genes.json"))["entrez_columns"]
gi = {r["pr_gene_symbol"]: r["pr_gene_id"] for r in rd(Path(a.geo) / "GSE92742_Broad_LINCS_gene_info.txt.gz")}
col = {e: i for i, e in enumerate(ent)}
symcol = {s: col[e] for s, e in gi.items() if e in col}
arr = np.load(Path(a.cache) / "extract.npy", mmap_mode="r")
rows_u = sorted({s[0] for s in sigs}); ru = {r: i for i, r in enumerate(rows_u)}
Zu = np.asarray(arr[rows_u, :], dtype=np.float32)
Z = Zu[[ru[s[0]] for s in sigs]]
mad = np.median(np.abs(Z - np.median(Z, axis=1, keepdims=True)), axis=1)
Zn = Z / (1.4826 * mad)[:, None]
cls = np.array([s[1] for s in sigs]); fam = [s[2] for s in sigs]
famlist = sorted(set(fam)); fpos = {f: i for i, f in enumerate(famlist)}
fidx = np.array([fpos[f] for f in fam])
G = Zn.shape[1]
sd = Z.std(0); dec = np.digitize(sd, np.quantile(sd, np.linspace(0.1, 0.9, 9)))
def wvec(unc):
    """seed weights over L1000 columns; genes missing from L1000 are listed."""
    w = np.zeros(G); miss = []
    for u in seeds.units:
        c = symcol.get(u["gene"])
        if c is None: miss.append(u["gene"]); continue
        w[c] += (u["sign"] if u["sign"] != 0 else unc) * u["level"]
    return w, miss
def fam_scores(W):
    """W: (G x M) weights -> (nfam x M) medians for class B and E"""
    O = -(Zn @ W) / np.abs(W).sum(0)[None, :]
    out = {}
    for c in ("B", "E"):
        m = np.full((len(famlist), W.shape[1]), np.nan)
        for f in range(len(famlist)):
            sel = np.flatnonzero((fidx == f) & (cls == c))
            if len(sel): m[f] = np.median(O[sel], axis=0)
        out[c] = m
    return out
res = dict(label=a.label, seed_units_total=n_all, seed_units_excluded_by_guard=n_all - len(seeds), signatures=len(sigs), families=len(famlist), signatures_B=int((cls == "B").sum()), signatures_E=int((cls == "E").sum()))
arms = {}
for nm, unc in (("Uplus", 1.0), ("Uminus", -1.0)):
    w, miss = wvec(unc)
    res["seed_genes_missing_from_L1000"] = sorted(set(miss)); res["seed_units_in_L1000"] = len(seeds) - len(miss)
    if np.abs(w).sum() == 0:
        res["error"] = "no seed gene in the L1000 space"; print(json.dumps(res)); raise SystemExit(0)
    fs = fam_scores(w[:, None]); arms[nm] = fs
    both = ~np.isnan(fs["B"][:, 0]) & ~np.isnan(fs["E"][:, 0])
    res[f"{nm}_families_with_B_and_E"] = int(both.sum())
    res[f"{nm}_rho_B_vs_E"] = se.spearman(fs["B"][both, 0], fs["E"][both, 0])
    # random matched readouts: each seed gene replaced by a random L1000 gene of the same SD decile, signed levels kept
    rng = np.random.default_rng(se.SEED0 + 5)
    real_cols = [symcol[u["gene"]] for u in seeds.units if u["gene"] in symcol]
    units = [u for u in seeds.units if u["gene"] in symcol]
    pools = {d: np.flatnonzero(dec == d) for d in range(10)}
    Wn = np.zeros((G, a.nnull))
    for k in range(a.nnull):
        used = set(real_cols)
        for u, rc in zip(units, real_cols):
            while True:
                c = int(rng.choice(pools[dec[rc]]))
                if c not in used: used.add(c); break
            Wn[c, k] += (u["sign"] if u["sign"] != 0 else unc) * u["level"]
    fn = fam_scores(Wn)
    rho_null = []; spec = []
    for k in range(a.nnull):
        bk = ~np.isnan(fn["B"][:, k]) & ~np.isnan(fn["E"][:, k])
        rho_null.append(se.spearman(fn["B"][bk, k], fn["E"][bk, k]))
        ek = ~np.isnan(fn["E"][:, k]) & ~np.isnan(fs["E"][:, 0])
        spec.append(se.spearman(fs["E"][ek, 0], fn["E"][ek, k]))
    res[f"{nm}_null_rho_B_vs_E_p95"] = float(np.nanpercentile(rho_null, 95)); res[f"{nm}_null_rho_B_vs_E_median"] = float(np.nanmedian(rho_null))
    res[f"{nm}_emp_p_reproducibility"] = float((np.array(rho_null) >= res[f"{nm}_rho_B_vs_E"]).mean())
    res[f"{nm}_spearman_real_vs_random_readout_E_median"] = float(np.nanmedian(spec))
    # mutation: all signs flipped -> scores negate
    fl = fam_scores(-w[:, None])
    res[f"{nm}_flip_all_max_abs_err"] = float(np.nanmax(np.abs(fl["E"][:, 0] + fs["E"][:, 0])))
    res[f"{nm}_informative"] = bool(res[f"{nm}_rho_B_vs_E"] > res[f"{nm}_null_rho_B_vs_E_p95"] and res[f"{nm}_spearman_real_vs_random_readout_E_median"] <= 0.5)
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
(out / f"sig_{a.label}.json").write_text(json.dumps(res, indent=1) + "\n")
names = {}
for e in entries:
    names.setdefault(idx.family[e["id"]], e.get("name"))
with gzip.open(out / f"sig_{a.label}_families.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
    w_ = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w_.writerow(["family_id", "name", "O_E_Uplus", "O_E_Uminus", "O_B_Uplus", "O_B_Uminus", "n_sig_B", "n_sig_E"])
    for f in range(len(famlist)):
        w_.writerow([famlist[f], names.get(famlist[f]), *(("%.5g" % arms[n][c][f, 0]) if not np.isnan(arms[n][c][f, 0]) else "" for c in ("E", "B") for n in ("Uplus", "Uminus")),
                     int(((fidx == f) & (cls == "B")).sum()), int(((fidx == f) & (cls == "E")).sum())])
print(json.dumps(res, indent=1))
