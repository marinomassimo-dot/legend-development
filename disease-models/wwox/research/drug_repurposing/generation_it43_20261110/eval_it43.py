#!/usr/bin/env python3
"""IT43 P4 scorer, run after eval_protocol_it43.md was written. Questions not used to correct the method in IT42: Q7 = S2 (HCN), Q8 = S4 (connexin/pannexin), Q9 = S9 (PDK inhibition).
Per question and condition: distinct units; clean units; units with an unflagged error (E1 direction, E2 site class, E3 subunit transfer, E5 identity: the IT42 scorer rules, copied
unchanged, applied to each row's own fields); units added by the DGIdb listing (A2) and how many carry a typed action; verdicts of B (CANDIDATE kept, UNKNOWN, EXCLUDED with reason);
clean units lost from B without a record. The scorer shares facts with the engine for these rows: independence rests on the independent reader of the protocol, not on this table."""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent; IT41 = DR / "generation_it41_20261109"
sys.path.insert(0, str(IT41)); import action_search as A  # noqa: E402
def tsv(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))
rel = {r["relation_id"]: r for r in tsv(IT41 / "relations_it41.tsv") + tsv(HERE / "relations_it43.tsv")}
ident = A.load_identity(DR)
QS = {"Q7": ("S2", IT41 / "search_rows.tsv"), "Q8": ("S4", IT41 / "search_rows.tsv"), "Q9": ("S9", HERE / "s9" / "search_rows.tsv")}
DOWN = re.compile(r"inverse agonist|antagon|inhibit|block|negative|blocker", re.I); UP = re.compile(r"(?<!ant)(?<!inverse )agonist|activat|positive|potentiat|opener", re.I)
def wdir(rid, sym):
    w = rel[rid]["wanted_direction"]
    return dict(x.split(":") for x in w.split(";")).get(sym.upper(), "") if ":" in w else w
def errors(rid, r):
    e = set(); parts = (r["action"] or "").split("/"); act = parts[-1] if parts[-1].strip().lower() not in ("none", "") else parts[0]
    w = wdir(rid, r["target_symbol"].split("|")[0].strip() if r["source"].startswith("GtoPdb") else r["target_symbol"])
    if w == "down" and UP.search(act) and not DOWN.search(act): e.add("E1")
    if w == "up" and DOWN.search(act) and not UP.search(act): e.add("E1")
    if rel[rid]["site_policy"] == "allosteric_subunit" and (r["site_or_granularity"] in ("glutamate site", "glycine site", "family_record_subunit_unresolved") or (r["action"] or "").startswith("Channel blocker")): e.add("E2")
    if rel[rid]["subunit_out"] and re.search(rel[rid]["subunit_out"], r["assay_or_note"] or "", re.I): e.add("E3")
    for nm in (r["name"] or "").lower().split(" | "):
        if any(x.get("label_conflict") == "yes" for x in ident.get(nm, [])): e.add("E5")
    return e
dg = tsv(HERE / "dgidb_rows_it43.tsv"); out = []; lost = []
H = ["question", "relation", "condition", "units", "clean_units", "units_with_unflagged_error", "units_added_by_listing", "listing_units_with_typed_action", "B_candidates", "B_unknown", "B_excluded_with_reason", "clean_lost_without_record"]
for q, (rid, path) in QS.items():
    R = [r for r in tsv(path) if r["relation_id"] == rid and r["labelled_form"] != "yes"]
    L = [r for r in dg if r["relation_id"] == rid and r["in_simple_search"] == "no"]
    added = {r["catalogue_id"] for r in L}; typed = {r["catalogue_id"] for r in L if r["interaction_type"]}
    for cond, rows in (("A0", [r for r in R if r["source"].startswith("ChEMBL")]), ("A1", R), ("A2", R), ("B", [r for r in R if r["qualification"] == "CANDIDATE"])):
        par = defaultdict(list)
        for r in rows: par[r["molecule"]].append(r)
        clean = unfl = 0
        for p, rs in par.items():
            es = set.intersection(*[errors(rid, r) for r in rs])
            if not es: clean += 1
            elif cond != "B": unfl += 1
        units = len(par) + (len(added) if cond == "A2" else 0)
        cand = len({r["molecule"] for r in rows}) if cond == "B" else ""
        unk = len({r["molecule"] for r in R if r["qualification"] == "UNKNOWN"}) if cond == "B" else ""
        exc = len({r["molecule"] for r in R if r["qualification"] == "EXCLUDED" and r["reason"]}) if cond == "B" else ""
        out.append([q, rid, cond, units, clean, unfl if cond != "B" else 0, len(added) if cond == "A2" else "", len(typed) if cond == "A2" else "", cand, unk, exc, ""])
    par = defaultdict(list)
    for r in R: par[r["molecule"]].append(r)
    n = 0
    for p, rs in par.items():
        if not set.intersection(*[errors(rid, r) for r in rs]) and not any(r["qualification"] == "CANDIDATE" for r in rs):
            n += 1; lost.append([q, p, rs[0]["name"], ";".join(sorted({r["qualification"] + ":" + r["reason"] for r in rs}))])
    out[-1][-1] = n
with open(HERE / "eval_results.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(H); w.writerows(out)
with open(HERE / "eval_lost_candidates.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["question", "unit", "name", "B_verdicts"]); w.writerows(lost)
print("\t".join(H)); [print("\t".join(str(x) for x in o)) for o in out]; print("lost:", len(lost)); [print(*l, sep=" | ") for l in lost]
