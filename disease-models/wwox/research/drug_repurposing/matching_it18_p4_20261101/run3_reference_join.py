#!/usr/bin/env python3
"""IT18 P4 run 3: resolution-aware GtoPdb reference for the locked T/X/L labels.

Design: PRE_REGISTRATION_RUN3.md. Labels are never recomputed: they are read from the locked answers.tsv.
Offline; --help and import do nothing else.

  run3 --catalog F --needs F --chembl-targets F --gtopdb-dir D --split dev|eval [--outdir D] [--allow-uncommitted]
      R3a orthologue-aware join on the need's genes (primary), R3b family-level join (descriptive).
      --split dev drops every EVAL ligand row on read (dry run); --split eval is the registered read, done once.
"""
import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import matching_task as m  # noqa: E402

dt = m.dt


def target_id_to_human_uniprot(gdir):
    out = {}
    with open(Path(gdir) / "targets_and_families.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows)
        h = next(rows)
        for r in rows:
            d = dict(zip(h, r))
            for u in dt._split_ids(d.get("Human SwissProt", "")):
                out.setdefault(d["Target id"], set()).add(u)
    return out


def load_gtopdb_any_species(gdir, pmap, keep, tid2u):
    """-> gt {(parent, human uniprot): entry with 'species' set}, ligand_parents (parents with any GtoPdb ligand, kept splits)."""
    gdir = Path(gdir)
    lig = {}
    with open(gdir / "ligands.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows)
        h = next(rows)
        for r in rows:
            d = dict(zip(h, r))
            if d["ChEMBL ID"]:
                lig[d["Ligand ID"]] = d["ChEMBL ID"]
    ligand_parents = {pmap.get(c, c) for c in lig.values() if dt.split_of(pmap.get(c, c)) in keep}
    out = {}
    with open(gdir / "interactions.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows)
        h = next(rows)
        for r in rows:
            d = dict(zip(h, r))
            if d["Ligand ID"] not in lig:
                continue
            c = lig[d["Ligand ID"]]
            parent = pmap.get(c, c)
            if dt.split_of(parent) not in keep:
                continue
            us = set(tid2u.get(d["Target ID"], set()))
            if d["Target Species"] == "Human":
                us |= dt._split_ids(d["Target UniProt ID"])
            for u in us:
                e = out.setdefault((parent, u), {"classes": set(), "raw": set(), "pmids": set(), "species": set()})
                e["classes"].add(dt.gtopdb_class(d["Type"], d["Action"]))
                e["raw"].add((d["Type"], d["Action"]))
                e["pmids"] |= dt._split_ids(d["PubMed ID"])
                e["species"].add(d["Target Species"])
    return out, ligand_parents


def family_uniprots(row):
    """R3b: components of the ChEMBL records reaching the need, for records mostly inside the module's targets."""
    us = set()
    for rs in row.get("rowsets") or ():
        if len(rs & row["module_uniprots"]) / len(rs) >= 0.5:
            us |= rs
    return us


def human_only(gt):
    out = {}
    for k, e in gt.items():
        if "Human" in e["species"]:
            out[k] = e
    return out


def absence_cause(row, gt, ligand_parents, uniprots):
    if row["parent"] not in ligand_parents:
        return "no_gtopdb_ligand_with_chembl_id"
    if not any((row["parent"], u) in gt for u in uniprots):
        return "ligand_present_no_interaction_on_these_genes"
    return "interactions_present"


def evaluate(universe, labels, gt, ligand_parents, level, split):
    """Score with row-specific reference genes (need genes for R3a; need genes plus family for R3b)."""
    def ref_u(r):
        base = set(r["need_uniprots_list"])
        return sorted(base | family_uniprots(r)) if level == "R3b" else sorted(base)
    orig = m.truth
    m.truth = lambda r, g, nu: orig(r, g, ref_u(r))
    try:
        res, tr = _score(universe, labels, gt, split)  # score_split calls m.truth, patched to row-specific genes
    finally:
        m.truth = orig
    directed = [r for r in universe if r["need_direction"] in m.NEED_DIR and r["split"] == split]
    res["absence_causes"] = dict(Counter(absence_cause(r, gt, ligand_parents, ref_u(r)) for r in directed
                                         if tr[(r["need"], r["parent"])] == "unknown_no_counterpart"))
    hum = human_only(gt)
    det_keys = [k for k, v in tr.items() if v in (m.COMPAT, m.OPPOS)]
    by_r = {(r["need"], r["parent"]): r for r in directed}
    res["determinate_only_through_non_human_rows"] = sorted(
        "%s|%s" % k for k in det_keys if orig(by_r[k], hum, ref_u(by_r[k]))[0] not in (m.COMPAT, m.OPPOS))
    res["reference_by_row"] = {"%s|%s" % k: v for k, v in sorted(tr.items())}
    return res


def _score(universe, labels, gt, split):
    class NU(dict):
        def __missing__(self, k):
            return []
    return m.score_split(universe, labels, gt, NU(), split)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("run3")
    for a in ("--catalog", "--needs", "--chembl-targets", "--gtopdb-dir"):
        s.add_argument(a, required=True)
    s.add_argument("--split", choices=("dev", "eval"), required=True)
    s.add_argument("--outdir", default=str(HERE))
    s.add_argument("--allow-uncommitted", action="store_true", help="tests only")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    out = Path(a.outdir)
    lock = json.loads((out / "answers_lock.json").read_text(encoding="utf-8"))
    if lock.get("answers_tsv_sha256") != m.sha256(out / "answers.tsv") or lock.get("catalog_sha256") != m.sha256(a.catalog):
        print("REFUSED: locked answers or catalogue changed", file=sys.stderr)
        return 2
    if a.split == "eval" and not a.allow_uncommitted:
        for p in (Path(__file__), out / "PRE_REGISTRATION_RUN3.md"):
            if not m.git_committed(p):
                print("REFUSED: %s is not committed and clean" % p.name, file=sys.stderr)
                return 2
    needs, sym2u, module, pmap, universe = m.load_common(a)
    nu = m.need_uniprots(needs, sym2u)
    for r in universe:
        r["need_uniprots_list"] = nu[r["need"]]
    labels = {"X": {}, "L": {}, "L_v2": {}}
    with open(out / "answers.tsv", newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f, delimiter="\t"):
            k = (d["need_id"], d["parent_chembl_id"])
            labels["X"][k] = (d["X"], d["X_reason"])
            labels["L"][k] = (d["L"], d["L_reason"])
            labels["L_v2"][k] = (d["L_v2"], d["L_v2_reason"])
    keep = {"dev"} if a.split == "dev" else {"dev", "eval"}
    tid2u = target_id_to_human_uniprot(a.gtopdb_dir)
    gt, lp = load_gtopdb_any_species(a.gtopdb_dir, pmap, keep, tid2u)
    res = {"run_label": "run3_reference_join_20261101", "split": a.split, "script_sha256": m.sha256(__file__),
           "preregistration_sha256": m.sha256(out / "PRE_REGISTRATION_RUN3.md"), "answers_lock_sha256": m.sha256(out / "answers_lock.json"),
           "gtopdb_files_sha256": {f: m.sha256(Path(a.gtopdb_dir) / f) for f in ("interactions.csv", "ligands.csv", "targets_and_families.csv")}}
    for level in ("R3a", "R3b"):
        for rule in ("L", "L_v2"):
            lab = {"X": labels["X"], "L": labels[rule]}
            r = evaluate(universe, lab, gt, lp, level, a.split)
            if level == "R3a" and rule == "L":
                r["decision"] = m.decide(r)
            res["%s_%s" % (level, rule)] = r
    if a.split == "eval":
        (out / "results_run3_reference_join_20261101.json").write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
