#!/usr/bin/env python3
"""IT43 P2: read the DGIdb claims the catalogue already holds, for the relations of generation_it41 (S1-S8), as LISTING rows.
A DGIdb claim says a source listed a gene-drug pair; it carries no potency, species or site, and passing through DGIdb gives it no direction, selectivity or independence.
So every row here is verdict UNKNOWN (reason listing_only) whatever its interaction_type; a typed claim is recorded as 'documented action' only.
Compared with the simple search (the molecule x relation table of IT41/IT42, ChEMBL mechanisms plus GtoPdb) on the same relations, five things are counted apart:
new molecules reached, identities reconciled (the DGIdb-only record maps to a record of another source), documented actions (a non-null interaction type),
qualification improved (always 0 by rule), new hypotheses (always 0 by rule). A reached known compound shows path coverage, not predictive value.
  python3 dgidb_listing.py  -> dgidb_rows_it43.tsv, dgidb_summary_it43.tsv"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import compound_catalog as cc  # noqa: E402
S41 = DR / "generation_it41_20261109"

SALT = re.compile(r"\b(hydrochloride|hcl|hemi\w*|tartrate|maleate|mesylate|sodium|potassium|citrate|sulfate|sulphate|phosphate|fumarate|besylate|acetate|bromide|dihydrate|monohydrate)\b", re.I)
RACEMATE = re.compile(r"\((?:r\s*,\s*s|rs|\+/-|\+-|\u00b1|rac|dl)\)-?", re.I)   # only a racemate mark merges with the parent; a single (R)/(S)/(+)/(-) names a distinct enantiomer (HE43: parent_form keeps stereo apart)
import compound_identity as _ci  # noqa: E402  (HE43 parent_form: salts merge, stereo/isotope prefixes stay apart)
def key(n):
    p = _ci.parent_form(n)
    return p["key"] + ("|" + p["stereo_isotope"] if p.get("stereo_isotope") else "")

def main():
    rel = list(csv.DictReader(open(S41 / "relations_it41.tsv", encoding="utf-8"), delimiter="\t")) + list(csv.DictReader(open(HERE / "relations_it43.tsv", encoding="utf-8"), delimiter="\t"))
    base = defaultdict(set)                       # simple search: names per relation from the molecule tables (IT41 for S1-S8, IT43 s9/ for S9)
    for mt in (S41 / "molecules.tsv", HERE / "s9" / "molecules.tsv", HERE / "s10" / "molecules.tsv"):
        for r in csv.DictReader(open(mt, encoding="utf-8"), delimiter="\t"):
            base[r["relation_id"]] |= {key(n) for n in r["names"].split("|")}
    es = cc.load(cc.DEFAULT_CATALOG); rows = []
    for r in rel:
        syms = {s.upper() for s in r["target_symbols"].replace(":down", "").replace(":up", "").split(";") if s}
        for e in es:
            for t in e.get("targets") or []:
                if t.get("source") != "DGIdb interaction" or (t.get("gene") or "").upper() not in syms: continue
                if re.match(r"^\[?<?sup|^\[\d?[A-Z0-9]*\]|^\[3H\]|^\[\w+\]", e["name"]) or e["name"].strip().lower() in ("null", "none", ""): continue   # radiolabelled forms and empty names are not molecules
                rows.append(dict(relation_id=r["relation_id"], name=e["name"], catalogue_id=e["id"], origin=e.get("origin", ""), gene=t["gene"], claim_source=t.get("claim_source", ""),
                    interaction_type=t.get("interaction_type") or "", qualification="UNKNOWN", reason="listing_only",
                    in_simple_search="yes" if key(e["name"]) in base[r["relation_id"]] else "no",
                    reconciled=("yes" if e.get("origin") != "dgidb_only" else "n/a_has_other_source")))
    with open(HERE / "dgidb_rows_it43.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(rows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    out = []
    for rid in sorted({x["relation_id"] for x in rows}):
        rr = [x for x in rows if x["relation_id"] == rid]; mol = {x["catalogue_id"] for x in rr}
        new = {x["catalogue_id"] for x in rr if x["in_simple_search"] == "no"}
        out.append(dict(relation_id=rid, listing_molecules=len(mol), already_in_simple_search=len(mol - new), new_molecules=len(new),
                        new_dgidb_only_records=len({x["catalogue_id"] for x in rr if x["in_simple_search"] == "no" and x["origin"] == "dgidb_only"}),
                        documented_actions_new=len({x["catalogue_id"] for x in rr if x["in_simple_search"] == "no" and x["interaction_type"]}),
                        qualification_improved=0, new_hypotheses=0))
    with open(HERE / "dgidb_summary_it43.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(out[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    for o in out: print(o)

if __name__ == "__main__": main()
