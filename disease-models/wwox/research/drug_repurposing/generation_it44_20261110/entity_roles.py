#!/usr/bin/env python3
"""IT44 P4: a role for every returned entity, from data, so that a non-drug entity is not shown as a drug candidate and a physiologically relevant one is not lost.
Roles: candidate | probe | control_or_reagent | physiological_intervention | unqualified_entity (a modality outside small-molecule repurposing, or an entity no rule classified: role_basis says which). Inputs per molecule: the GtoPdb ligand type (ligands.csv, by ligand id), the catalogue status (tracked catalogue, by ChEMBL id),
the engine's own verdicts on its rows. Rules live in role_rules_it44.tsv (first match in file order); a reviewer's change is a row in role_overrides_it44.tsv (name, role, reason, source), which wins and keeps the rule's role in `rule_role`.
A role is not a verdict: an EXCLUDED row stays excluded for its relation; its role says what the entity is, so an excluded physiological ion is still visible as a manipulation of the preparation.
  python3 entity_roles.py  -> entity_roles_it44.tsv"""
import csv, gzip, json, os, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
SOURCES = [DR / "generation_it41_20261109/search_rows.tsv", DR / "generation_it43_20261110/s9/search_rows.tsv", DR / "generation_it43_20261110/s10/search_rows.tsv", HERE / "s11/search_rows.tsv", HERE / "s12/search_rows.tsv", HERE / "s13/search_rows.tsv"]

def tsv(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))
def clean(n): return re.sub(r"<[^>]+>", "", n or "").strip()

def load():
    croot = Path(os.environ.get("LEGEND_CATALOG_CACHE", DR / "catalog/cache"))
    lig = {}
    with open(croot / "gtopdb/ligands.csv", encoding="utf-8", newline="") as f:
        f.readline(); 
        for r in csv.DictReader(f): lig[r["Ligand ID"]] = r["Type"]
    cat = {}
    with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt") as f:
        for line in f:
            e = json.loads(line); cat[e["id"]] = (e.get("status_class") or "", e.get("origin") or "")
    return lig, cat

def role_of(gtype, status, rules):
    for r in rules:
        if (r["field"] == "gtopdb_type" and gtype == r["value"]) or (r["field"] == "catalogue_status" and status == r["value"]): return r["role"], r["rule_id"]
    return "unqualified_entity", "default"   # HE45: no rule classified it. Not a candidate by omission: the engine verdict still lists it, the role only says that nothing qualified it

def main():
    lig, cat = load(); rules = tsv(HERE / "role_rules_it44.tsv"); over = {clean(o["name"]).lower(): o for o in tsv(HERE / "role_overrides_it44.tsv")}
    by = defaultdict(list)
    for p in SOURCES:
        if p.exists():
            for r in tsv(p): by[(r["relation_id"], r["molecule"], clean(r["name"]))].append(r)
    out = []
    for (rid, mol, name), rows in sorted(by.items()):
        gid = mol.split(":", 1)[1] if mol.startswith("GTOPDB:") else ""; gtype = lig.get(gid, "")
        cid = rows[0].get("catalogue_id", ""); status, origin = cat.get(cid, ("", ""))
        role, rule = role_of(gtype, status or ("tool_probe" if origin == "tool_probe" else ""), rules)
        verd = ";".join(sorted({r["qualification"] for r in rows})); o = over.get(name.lower()); final, basis = (role, rule)
        if o: final, basis = o["role"], "override: " + o["reason"][:120]
        out.append(dict(relation_id=rid, molecule=mol, name=name, gtopdb_type=gtype, catalogue_status=status, engine_verdicts=verd, rule_role=role, role=final, role_basis=basis if o else f"rule {rule}"))
    with open(HERE / "entity_roles_it44.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(out[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    from collections import Counter
    print(Counter(r["role"] for r in out))
if __name__ == "__main__": main()
