#!/usr/bin/env python3
"""IT19 P5 step 1: select a small, bounded, outcome-blind set of unresolved (need, compound) pairs.

Rule (SELECTION.md, this directory). Reads only module-side files and the IT18 per-row reference
category already published (which rows were determinate); opens no new reference source.

  select_pairs.py --answers F --it18-eval-ref F --it18-dev-determinate F --catalog F --needs F --out F

Offline; --help and import do nothing else.
"""
import argparse
import csv
import gzip
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

SALT = "IT19P5|"
DOWN = {"ANTAGONIST", "BLOCKER", "INHIBITOR", "NEGATIVE ALLOSTERIC MODULATOR"}
UP_PAM = {"POSITIVE ALLOSTERIC MODULATOR"}
PARTIAL = {"PARTIAL AGONIST"}
AMBIG = {"MODULATOR"}

# stratum -> (description, quota per stratum in COMPOUNDS, needs taken per compound)
# quota None = every compound of the stratum.
STRATA = [
    ("S01", "heterogeneous group record, clean blocker", None, "both"),
    ("S02", "heterogeneous group record, ambiguous MODULATOR", 1, "both"),
    ("S03", "homogeneous family record, clean blocker", 2, "both"),
    ("S04", "single-protein record, clean blocker, calcium need", None, "own"),
    ("S05", "homogeneous receptor group, clean down action, one ChEMBL mechanism", 4, "own"),
    ("S06", "homogeneous receptor group, clean down action, other mechanisms off the directed needs", 2, "own"),
    ("S07", "homogeneous receptor group, partial agonist", None, "own"),
    ("S08", "NMDA receptor group, positive allosteric modulator", None, "own"),
    ("S09", "defined two-subunit complex record, clean antagonist", 2, "own"),
    ("S10", "AMPA receptor group, clean antagonist", 2, "own"),
    ("S11", "AMPA receptor group, positive allosteric modulator", 2, "own"),
    ("S12", "single-protein record(s), glutamate need", None, "own"),
]


def h(parent):
    return hashlib.sha256((SALT + parent).encode()).hexdigest()


def read_tsv(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_needs(p):
    out = {}
    for n in json.loads(Path(p).read_text(encoding="utf-8"))["needs"]:
        out[n["id"]] = {t["symbol"] for t in n.get("targets", []) if t.get("target_kind") == "intervention_target"}
    return out


def family_records(catalog, parents):
    """parent -> list of human direct ChEMBL mechanism records over the parent and its child (salt) records."""
    out = defaultdict(list)
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            par = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
            p = cid if cid in parents else par if par in parents else None
            if not p:
                continue
            for t in d.get("targets", []):
                if t.get("source") == "ChEMBL curated mechanism" and t.get("organism") == "Homo sapiens" and not t.get("inherited_from_parent"):
                    out[p].append({"target_id": t["target_id"], "target_type": t.get("target_type"),
                                   "genes": frozenset(t.get("gene_symbols") or []), "action": (t.get("action_type") or "").upper()})
    return out


def record_class(rec, module_genes):
    if rec["target_type"] == "SINGLE PROTEIN":
        return "single"
    if rec["target_type"] == "PROTEIN COMPLEX":
        return "complex"
    share = len(rec["genes"] & module_genes) / max(1, len(rec["genes"]))
    return "homogeneous" if share >= 0.5 else "heterogeneous"


def stratum(need_id, recs, others_off_needs):
    """Stratum of a pair from the ChEMBL records that reach the need (module side only)."""
    cls = {r["class"] for r in recs}
    acts = {r["action"] for r in recs}
    tids = {r["target_id"] for r in recs}
    glut = need_id == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR"
    if "single" in cls:
        return "S12" if glut else "S04"
    if cls == {"heterogeneous"}:
        return "S01" if acts <= {"BLOCKER"} else "S02" if acts <= AMBIG else None
    if cls == {"complex"}:
        return "S09" if acts <= DOWN else None
    if not glut and cls == {"homogeneous"}:
        return "S03" if acts <= {"BLOCKER"} else None
    if glut and cls == {"homogeneous"}:
        ampa = any(len(r["genes"]) == 4 and all(g.startswith("GRIA") for g in r["genes"]) for r in recs)
        if ampa:
            return "S10" if acts <= DOWN else "S11" if acts <= UP_PAM else None
        if acts <= PARTIAL:
            return "S07"
        if acts <= UP_PAM:
            return "S08"
        if acts <= DOWN:
            return "S06" if others_off_needs else "S05"
    return None


def select(rows, needs, fam, determinate):
    directed = {n for n in needs if n in {r["need_id"] for r in rows if r["need_direction"] in ("down", "up")}}
    module_genes = set().union(*(needs[n] for n in needs))
    directed_genes = set().union(*(needs[n] for n in directed))
    pairs = []
    for r in rows:
        if r["need_direction"] not in ("down", "up"):
            continue
        key = (r["need_id"], r["parent_chembl_id"])
        if key in determinate:
            continue
        recs = []
        for x in fam.get(r["parent_chembl_id"], []):
            if x["genes"] & needs[r["need_id"]]:
                recs.append(dict(x, **{"class": record_class(x, module_genes)}))
        recs = list({(x["target_id"], x["action"]): x for x in recs}.values())
        off = any(not (x["genes"] & directed_genes) for x in fam.get(r["parent_chembl_id"], []))
        pairs.append({"need": r["need_id"], "parent": r["parent_chembl_id"], "split": r["split"], "L": r["L"], "L_v2": r["L_v2"],
                      "stratum": stratum(r["need_id"], recs, off), "recs": recs})
    by = defaultdict(list)
    for p in pairs:
        by[p["stratum"]].append(p)
    chosen = []
    for sid, desc, quota, needs_mode in STRATA:
        comps = sorted({p["parent"] for p in by.get(sid, [])}, key=h)
        take = comps if quota is None else comps[:quota]
        for p in sorted(by.get(sid, []), key=lambda p: (h(p["parent"]), p["need"])):
            if p["parent"] in take:
                chosen.append(dict(p, stratum_desc=desc, available_compounds=len(comps), available_pairs=len(by.get(sid, []))))
    unplaced = sorted({(p["need"], p["parent"]) for p in by.get(None, [])})
    return chosen, pairs, unplaced


HEADER = ["pair_id", "stratum", "stratum_description", "need_id", "parent_chembl_id", "it18_split", "it18_L_v1", "it18_L_v2",
          "chembl_records_reaching_need", "available_compounds_in_stratum", "available_pairs_in_stratum", "selection_hash"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--answers", required=True, help="IT18 locked answers.tsv")
    ap.add_argument("--it18-eval-ref", required=True, help="IT18 reference.tsv (EVAL per-row category)")
    ap.add_argument("--it18-dev-determinate", required=True, help="IT18 controls_result.json (lists all 8 determinate rows)")
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--needs", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    rows = read_tsv(a.answers)
    needs = load_needs(a.needs)
    det = {(r["need_id"], r["parent_chembl_id"]) for r in read_tsv(a.it18_eval_ref) if not r["reference_category"].startswith("unknown")}
    ctl = json.loads(Path(a.it18_dev_determinate).read_text(encoding="utf-8"))
    det |= {(n, c) for n, c, *_ in ctl["C1_popularity"]["reference_bias"]["determinate"]}
    parents = {r["parent_chembl_id"] for r in rows}
    fam = family_records(a.catalog, parents)
    chosen, pairs, unplaced = select(rows, needs, fam, det)
    out = []
    for i, p in enumerate(chosen, 1):
        recs = ";".join(sorted(f'{x["target_id"]}|{x["target_type"]}|n={len(x["genes"])}|{x["action"]}' for x in p["recs"]))
        out.append([f"P{i:02d}", p["stratum"], p["stratum_desc"], p["need"], p["parent"], p["split"], p["L"], p["L_v2"], recs,
                    p["available_compounds"], p["available_pairs"], h(p["parent"])[:12]])
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(HEADER)
        w.writerows(out)
    print(json.dumps({"directed_rows": sum(1 for r in rows if r["need_direction"] in ("down", "up")),
                      "determinate_excluded": len(det), "unresolved_pairs": len(pairs), "selected_pairs": len(out),
                      "selected_compounds": len({p["parent"] for p in chosen}), "unplaced_pairs": unplaced}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
