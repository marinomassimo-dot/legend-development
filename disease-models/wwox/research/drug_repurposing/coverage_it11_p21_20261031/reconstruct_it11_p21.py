#!/usr/bin/env python3
"""IT11 P2.1: reconstruct, for the five molecules with a recorded WWOX-system result, why the IT9 v3 / IT10 v4 generation path did not return them.

  reconstruct_it11_p21.py --out DIR

Read-only toward every earlier package. Needs LEGEND_CATALOG_CACHE only if the catalogue cache is opened (it is not: the catalogue is read from catalog.jsonl.gz).
Writes in DIR: targets.tsv (compound side: every target of every family of a molecule, signed or not, in the network or not), pairs.tsv (target to seed-gene pairs, per seed set,
under three edge regimes: all = no mode filter and no junction rule; v3 = F1 mode typing; v4 = F1 + F5 junction), universe.tsv (family membership in the engine universe per seed set).
The edge regimes are switched at run time on the loaded v4 engine (MODE in v3, JUNCTION in v4); nothing is written to the earlier packages.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, glob, gzip, importlib.util, os
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
DR = HERE.parent
V4 = DR / "generation_it10_p1_20261031" / "engine_v4" / "seed_engine_v4.py"
ACT = DR / "generation_it9_p2_20261030" / "v3" / "results" / "actions"
SEEDS = DR / "generation_it9_p2_20261030" / "seeds_p1"
PROP = DR / "generation_it10_p1_20261031" / "results_v4"

# molecule -> catalogue families (ids verified in the README; name twins listed, never merged)
MOL = {
    "ethosuximide": ["FAM:CAT:CHEMBL696", "FAM:CAT:DGIDB:6998a1a2d947"],
    "lithium": ["FAM:CAT:CHEMBL1201333", "FAM:CAT:CHEMBL1200826", "FAM:CAT:CHEMBL1201170", "FAM:CAT:CHEMBL3707288",
                "FAM:CAT:DGIDB:be65bb20ae7f", "FAM:CAT:DGIDB:50ccc7b5c33e", "FAM:CAT:DGIDB:cfa5bd0a6c8c", "FAM:CAT:DGIDB:0408436e6031", "FAM:CAT:DGIDB:bc9225cea0c7"],
    "vigabatrin": ["FAM:CAT:CHEMBL89598", "FAM:CAT:DGIDB:358b8a817686"],
    "d-APV": ["FAM:CAT:DGIDB:b0ca5cf2303c"],
    "A51": ["FAM:CAT:CHEMBL4754493"],
}


def load_engine():
    argv = list(sys.argv); sys.argv = ["seed_engine_v4.py", "run"]
    spec = importlib.util.spec_from_file_location("seed_engine_v4_it11", V4)
    m = importlib.util.module_from_spec(spec); sys.modules["seed_engine_v4_it11"] = m; spec.loader.exec_module(m)
    sys.argv = argv
    return m


def rd(p, gz=False):
    return list(csv.DictReader(gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8"), delimiter="\t"))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    m4 = load_engine(); m3 = m4.m3; se = m4.se
    meta = {r["family_id"]: r for r in rd(ACT / "family_meta.tsv.gz", True)}
    acts = {}; sign_rows = {}
    for r in rd(ACT / "family_actions.tsv.gz", True):
        acts.setdefault(r["family_id"], {})[r["target_symbol"]] = r
    anyt = {}
    for r in rd(ACT / "family_targets_any.tsv.gz", True):
        anyt.setdefault(r["family_id"], {})[r["target_symbol"]] = int(r["n_rows_any_action"])
    flags = {}
    for r in rd(ACT / "family_flags.tsv.gz", True):
        flags.setdefault(r["family_id"], set()).add(r["flag"])
    edges = m4.read_edges4()
    outdeg = {}; indeg = {}
    for e in edges:
        outdeg[e[0]] = outdeg.get(e[0], 0) + 1; indeg[e[1]] = indeg.get(e[1], 0) + 1
    # ---- targets.tsv
    rows_t = []
    tg_all = {}
    for mol, fams in MOL.items():
        for f in fams:
            for t in sorted(set(anyt.get(f, {})) | set(acts.get(f, {}))):
                ar = acts.get(f, {}).get(t)
                rows_t.append(dict(molecule=mol, family_id=f, family_name=meta.get(f, {}).get("name", ""), target=t, signed_usable=int(ar is not None),
                                   mean_sign=ar["mean_sign"] if ar else "", hgnc_id=ar["hgnc_id"] if ar else "", groups=ar["groups"] if ar else "", scopes=ar["scopes"] if ar else "",
                                   family_flags=";".join(sorted(flags.get(f, ()))), n_rows_any_action=anyt.get(f, {}).get(t, ""),
                                   network_out_edges=outdeg.get(t, 0), network_in_edges=indeg.get(t, 0)))
                if ar:
                    tg_all.setdefault((mol, f), []).append(t)
    cols = list(rows_t[0].keys())
    with open(out / "targets.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows_t)
    # ---- engine per seed set
    rows_p, rows_u = [], []
    all_targets = {t for r in rows_t for t in [r["target"]]}
    for sf in sorted(glob.glob(str(SEEDS / "Q*.tsv"))):
        sn = os.path.basename(sf)[:-4]; q = sn.split("_")[0]
        seeds = se.load_seeds(sf)
        genes = sorted(set(seeds.genes))
        g = m4.Graph4(edges, extras=all_targets | set(genes))
        g.level = "expression" if {u["readout_level"] for u in seeds.units} == {"expression"} else "protein"
        S = seeds.unit_matrix(g.idx, g.N)
        res = {}
        for regime, (mode, junc) in dict(all=("all", False), v3=("v3", False), v4=("v3", True)).items():
            m3.MODE = mode; m4.JUNCTION = junc
            res[regime] = (g.influence_ind(S), {})
        pr = {}
        pf = PROP / f"proposals_p1_{sn}.tsv.gz"
        if pf.exists():
            pr = {r["family_id"]: r for r in rd(pf, True)}
        for (mol, f), tl in sorted(tg_all.items()):
            pass
        for mol, fams in MOL.items():
            for f in fams:
                tl = sorted(set(anyt.get(f, {})) | set(acts.get(f, {})))
                signed = set(acts.get(f, {}))
                in_net = [t for t in tl if t in g.idx and g.idx[t] < g.Ng]
                pre = pr.get(f)
                rows_u.append(dict(molecule=mol, family_id=f, seed_set=sn, question=q, seed_level=g.level, seed_genes=";".join(genes), n_signed_targets=len(signed),
                                   n_signed_targets_in_network=len([t for t in signed if t in g.idx and g.idx[t] < g.Ng]), direct_any_action_on_seed_gene=int(bool(set(tl) & set(genes))),
                                   in_proposals_table=int(pre is not None), Q_net_full=pre["Q_net_full"] if pre else "", Q_net_ind=pre["Q_net_ind"] if pre else "", Q_direct=pre["Q_direct"] if pre else "",
                                   Z_full_robust=pre["Z_full_robust"] if pre else "", Z_ind_robust=pre["Z_ind_robust"] if pre else "", compatible_action=pre["compatible_action"] if pre else ""))
                for t in tl:
                    if t not in g.idx:
                        continue
                    for ui, u in enumerate(seeds.units):
                        gene = u["gene"]
                        direct = int(t == gene)
                        vals = {r: float(res[r][0][ui, g.idx[t]]) for r in res}
                        ch = {}
                        for regime, (mode, junc) in dict(all=("all", False), v3=("v3", False), v4=("v3", True)).items():
                            m3.MODE = mode; m4.JUNCTION = junc
                            ch[regime] = (g.best_chain(t, gene) or "") if (not direct and abs(vals[regime]) > 0) else ""
                        if direct or any(abs(v) > 0 for v in vals.values()) or any(ch.values()):
                            rows_p.append(dict(molecule=mol, family_id=f, target=t, signed_usable=int(t in signed), seed_set=sn, seed_gene=gene, seed_direction=u["status"] if u["sign"] == 0 else ("up" if u["sign"] > 0 else "down"),
                                               direct_target_is_seed=direct, influence_all=f"{vals['all']:.6g}", influence_v3=f"{vals['v3']:.6g}", influence_v4=f"{vals['v4']:.6g}",
                                               chain_all=ch["all"], chain_v3=ch["v3"], chain_v4=ch["v4"]))
        m3.MODE = "v3"; m4.JUNCTION = True
    with open(out / "pairs.tsv", "w", newline="") as fh:
        c = ["molecule", "family_id", "target", "signed_usable", "seed_set", "seed_gene", "seed_direction", "direct_target_is_seed", "influence_all", "influence_v3", "influence_v4", "chain_all", "chain_v3", "chain_v4"]
        w = csv.DictWriter(fh, fieldnames=c, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows_p)
    with open(out / "universe.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows_u[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows_u)
    print("targets", len(rows_t), "pairs", len(rows_p), "universe rows", len(rows_u))


if __name__ == "__main__":
    main()
