#!/usr/bin/env python3
"""IT17 P3 task: direction of action of a compound at a human target, module relation vs an independent curated source.

Module relation = ChEMBL curated mechanism rows carried in catalog.jsonl.gz (direct rows, human targets).
Independent source = Guide to PHARMACOLOGY interactions.csv / ligands.csv (release in cache_manifest.json).
Design and decision rules: PRE_REGISTRATION_DIRECTION.md. Offline: reads local files only; --help and import do nothing else.

  dev   --catalog F --gtopdb-dir D     label tables and unmapped labels on DEV compounds only (eval compounds never read out)
  eval  --catalog F --gtopdb-dir D --card-links F [--out JSON] [--discordant TSV]   the registered evaluation, once
"""
import argparse
import csv
import gzip
import hashlib
import json
import sys
from math import comb, sqrt
from pathlib import Path

DEC, INC = "DECREASE", "INCREASE"
# Fixed on DEV (see PRE_REGISTRATION_DIRECTION.md, amendment log). Anything not listed is OTHER (unresolved, never an error).
CHEMBL_DEC = {"INHIBITOR", "ANTAGONIST", "BLOCKER", "NEGATIVE ALLOSTERIC MODULATOR", "NEGATIVE MODULATOR", "INVERSE AGONIST",
              "ANTISENSE INHIBITOR", "RNAI INHIBITOR", "ALLOSTERIC ANTAGONIST", "GENE EDITING NEGATIVE MODULATOR"}
CHEMBL_INC = {"AGONIST", "ACTIVATOR", "OPENER", "POSITIVE ALLOSTERIC MODULATOR", "POSITIVE MODULATOR"}
GTOPDB_ACTION_DEC = {"Inhibition", "Antagonist", "Irreversible inhibition", "Feedback inhibition", "Pore blocker",
                     "Voltage-dependent inhibition", "Inverse agonist", "Negative"}
GTOPDB_ACTION_INC = {"Agonist", "Full agonist", "Biased agonist", "Irreversible agonist", "Activation",
                     "Positive", "Potentiation"}
GTOPDB_TYPE_DEC = {"Inhibitor", "Antagonist", "Channel blocker", "Gating inhibitor"}
GTOPDB_TYPE_INC = {"Agonist", "Activator"}
DEV_DIGITS = set("01234567")  # first hex digit of sha256(parent ChEMBL id): dev; 8-f: eval


def chembl_class(a):
    a = (a or "").upper()
    return DEC if a in CHEMBL_DEC else INC if a in CHEMBL_INC else None


def gtopdb_class(typ, action):
    if action in GTOPDB_ACTION_DEC:
        return DEC
    if action in GTOPDB_ACTION_INC:
        return INC
    if action in ("Competitive", "Non-competitive", "None", ""):  # mode of action only: fall back to the type
        return DEC if typ in GTOPDB_TYPE_DEC else INC if typ in GTOPDB_TYPE_INC else None
    return None  # Binding, Neutral, Mixed, Slows inactivation, Unknown, Biphasic: no direction


def split_of(cid):
    return "dev" if hashlib.sha256(cid.encode()).hexdigest()[0] in DEV_DIGITS else "eval"


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _split_ids(s):
    return {x.strip() for x in (s or "").replace(";", "|").split("|") if x.strip()}


def load_module(catalog):
    """-> {(parent_chembl, uniprot): {"classes": set, "raw": set, "pmids": set}} for human direct ChEMBL mechanisms."""
    out = {}
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            parent = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
            if not cid:
                continue
            for t in d.get("targets", []):
                if t.get("source") != "ChEMBL curated mechanism" or t.get("organism") != "Homo sapiens" or t.get("inherited_from_parent"):
                    continue
                pm = {r.split(":", 1)[1] for r in t.get("reference_ids", []) if r.startswith("PubMed:")}
                for u in t.get("uniprot") or []:
                    e = out.setdefault((parent, u), {"classes": set(), "raw": set(), "pmids": set()})
                    e["classes"].add(chembl_class(t.get("action_type")))
                    e["raw"].add(t.get("action_type"))
                    e["pmids"] |= pm
    return out


def load_gtopdb(gdir):
    gdir = Path(gdir)
    lig = {}
    with open(gdir / "ligands.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    h = rows[1]
    for r in rows[2:]:
        d = dict(zip(h, r))
        if d["ChEMBL ID"]:
            lig[d["Ligand ID"]] = d["ChEMBL ID"]
    out = {}
    with open(gdir / "interactions.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    h = rows[1]
    for r in rows[2:]:
        d = dict(zip(h, r))
        if d["Target Species"] != "Human" or d["Ligand ID"] not in lig:
            continue
        for u in _split_ids(d["Target UniProt ID"]):
            e = out.setdefault((lig[d["Ligand ID"]], u), {"classes": set(), "raw": set(), "pmids": set()})
            e["classes"].add(gtopdb_class(d["Type"], d["Action"]))
            e["raw"].add((d["Type"], d["Action"]))
            e["pmids"] |= _split_ids(d["PubMed ID"])
    return out


def parent_map(catalog):
    m = {}
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            if cid:
                m[cid] = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
    return m


def join(module, gt, pmap):
    g2 = {}
    for (c, u), e in gt.items():
        k = (pmap.get(c, c), u)
        x = g2.setdefault(k, {"classes": set(), "raw": set(), "pmids": set()})
        x["classes"] |= e["classes"]
        x["raw"] |= e["raw"]
        x["pmids"] |= e["pmids"]
    pairs = []
    for k, m in module.items():
        g = g2.get(k)
        if g is None:
            pairs.append({"key": k, "split": split_of(k[0]), "gt": None, "m": m})
        else:
            pairs.append({"key": k, "split": split_of(k[0]), "gt": g, "m": m})
    return pairs


def single(e):
    """-> (class or None, reason)."""
    c = e["classes"]
    if len(c) > 1:
        # more than one row: conflicting if two determinate classes; a mix of one class and no-direction rows keeps the class
        det = {x for x in c if x}
        if len(det) == 2:
            return None, "conflict"
        if len(det) == 1:
            return next(iter(det)), "ok"
        return None, "no_direction"
    (x,) = c
    return (x, "ok") if x else (None, "no_direction")


def wilson(k, n, z=1.96):
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(c - h, 4), round(c + h, 4)]


def sign_p(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def classify(pairs):
    """Split pairs into determinate and unresolved with the reason; only pairs with a GtoPdb counterpart enter."""
    det, unres = [], {"no_gtopdb_counterpart": 0, "module_no_direction": 0, "module_conflict": 0,
                      "gtopdb_no_direction": 0, "gtopdb_conflict": 0}
    for p in pairs:
        if p["gt"] is None:
            unres["no_gtopdb_counterpart"] += 1
            continue
        mc, mr = single(p["m"])
        gc, gr = single(p["gt"])
        if mc is None:
            unres["module_conflict" if mr == "conflict" else "module_no_direction"] += 1
        elif gc is None:
            unres["gtopdb_conflict" if gr == "conflict" else "gtopdb_no_direction"] += 1
        else:
            p["mc"], p["gc"] = mc, gc
            p["shared_ref"] = bool(p["m"]["pmids"] & p["gt"]["pmids"])
            det.append(p)
    return det, unres


def score(det, train_det):
    from collections import Counter
    maj = Counter(p["gc"] for p in train_det).most_common(1)[0][0]
    per_t = {}
    for p in train_det:
        per_t.setdefault(p["key"][1], Counter())[p["gc"]] += 1
    b1 = lambda p: per_t[p["key"][1]].most_common(1)[0][0] if p["key"][1] in per_t else maj
    n = len(det)
    km = sum(p["mc"] == p["gc"] for p in det)
    k0 = sum(maj == p["gc"] for p in det)
    k1 = sum(b1(p) == p["gc"] for p in det)
    bm = sum(p["mc"] == p["gc"] and b1(p) != p["gc"] for p in det)
    cm = sum(p["mc"] != p["gc"] and b1(p) == p["gc"] for p in det)
    return {"n_determinate": n, "module_correct": km, "module_acc": round(km / n, 4) if n else None, "module_ci95": wilson(km, n),
            "B0_majority_label": maj, "B0_correct": k0, "B0_acc": round(k0 / n, 4) if n else None, "B0_ci95": wilson(k0, n),
            "B1_per_target_correct": k1, "B1_acc": round(k1 / n, 4) if n else None, "B1_ci95": wilson(k1, n),
            "module_right_B1_wrong": bm, "B1_right_module_wrong": cm, "paired_sign_p_module_vs_B1": round(sign_p(bm, cm), 6),
            "discordant_module_vs_gtopdb": n - km}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    for name in ("dev", "eval"):
        s = sub.add_parser(name)
        s.add_argument("--catalog", required=True)
        s.add_argument("--gtopdb-dir", required=True)
        if name == "eval":
            s.add_argument("--card-links", required=True)
            s.add_argument("--out")
            s.add_argument("--discordant")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    module, gt, pmap = load_module(a.catalog), load_gtopdb(a.gtopdb_dir), parent_map(a.catalog)
    pairs = join(module, gt, pmap)
    if a.cmd == "dev":
        dev = [p for p in pairs if p["split"] == "dev"]
        det, unres = classify(dev)
        from collections import Counter
        raw_m = Counter((x, chembl_class(x)) for p in dev if p["gt"] for x in p["m"]["raw"])
        raw_g = Counter((r, gtopdb_class(*r)) for p in dev if p["gt"] for r in p["gt"]["raw"])
        print(json.dumps({"dev_module_pairs": len(dev), "dev_determinate": len(det), "dev_unresolved": unres,
                          "dev_module_labels": sorted(map(str, raw_m.items())), "dev_gtopdb_labels": sorted(map(str, raw_g.items())),
                          "dev_scores_for_reference": score(det, det) if det else None}, indent=1))
        return 0
    ev = [p for p in pairs if p["split"] == "eval"]
    dev = [p for p in pairs if p["split"] == "dev"]
    det_dev, _ = classify(dev)
    det, unres = classify(ev)
    links = json.loads(Path(a.card_links).read_text(encoding="utf-8"))
    card_chembl = {l["chembl_id"] for c in links["cards"].values() for l in c.get("links", [])}
    card_parents = {pmap.get(c, c) for c in card_chembl}
    res = {"script_sha256": sha256(__file__), "catalog_sha256": sha256(a.catalog),
           "gtopdb_files_sha256": {f: sha256(Path(a.gtopdb_dir) / f) for f in ("interactions.csv", "ligands.csv")},
           "module_pairs_total": len(pairs), "eval_module_pairs": len(ev), "dev_module_pairs": len(dev),
           "eval_unresolved_by_reason": unres, "eval_determinate_all": score(det, det_dev),
           "eval_shared_reference_pairs": sum(p["shared_ref"] for p in det)}
    ind = [p for p in det if not p["shared_ref"]]
    res["eval_determinate_independent_reference_only"] = score(ind, det_dev) if ind else None
    all_det = det_dev + det
    card = [p for p in all_det if p["key"][0] in card_parents]
    res["card_linked_compounds_in_catalogue"] = len(card_parents)
    res["card_linked_pairs_with_counterpart_determinate_dev_plus_eval"] = len(card)
    res["card_linked_discordant"] = [(p["key"][0], p["key"][1], p["mc"], p["gc"]) for p in card if p["mc"] != p["gc"]]
    res["card_linked_descriptive"] = score(card, det_dev) if card else None
    if a.out:
        Path(a.out).write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if a.discordant:
        with open(a.discordant, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["split", "parent_chembl_id", "uniprot", "module_class", "gtopdb_class", "shared_reference"])
            for p in sorted(all_det, key=lambda p: p["key"]):
                if p["mc"] != p["gc"]:
                    w.writerow([p["split"], p["key"][0], p["key"][1], p["mc"], p["gc"], int(p["shared_ref"])])
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
