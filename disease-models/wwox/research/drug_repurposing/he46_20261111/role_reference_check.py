#!/usr/bin/env python3
"""HE46 H6: entity roles checked against a field the role rules do not read.

Frame (what is kept apart):
  input      entity_roles_it44.tsv rows (relation, molecule, name, gtopdb_type, catalogue_status)
  rules      role_rules_it44.tsv: the role comes from gtopdb_type and catalogue_status only
  result     the `role` column
  reference  the catalogue's own `modality`, `molecule_type` and `chemistry.inorganic` (ChEMBL curation; not read by any rule)
  judgement  none here: the reference is a second field, not a ground truth. It shares a source (ChEMBL) with catalogue_status, so it is independent of the
             rules, not of the catalogue. A person or reader reviewing the disagreements is the independent judgement and is recorded apart.
A molecule that is not in the catalogue has NO_REFERENCE: the check is silent about it, it is not an agreement.

    python3 role_reference_check.py > role_reference_check.tsv
"""
import collections, csv, gzip, json, sys
from pathlib import Path

DR = Path(__file__).resolve().parents[1]


def reference_class(e):
    if e is None:
        return "NO_REFERENCE"
    if (e.get("chemistry") or {}).get("inorganic"):
        return "INORGANIC_FLAG"
    return {"small_molecule": "SMALL_MOLECULE", "unknown": "UNKNOWN"}.get(e.get("modality"), "NOT_SMALL_MOLECULE")


def verdict(role, ref):
    if role in ("candidate", "probe"):
        return {"SMALL_MOLECULE": "agrees", "NOT_SMALL_MOLECULE": "DISAGREES", "INORGANIC_FLAG": "DISAGREES", "UNKNOWN": "unverified", "NO_REFERENCE": "no_reference"}[ref]
    if role == "unqualified_entity":
        return "rules_left_a_small_molecule_unqualified" if ref == "SMALL_MOLECULE" else "silent"
    return "silent"


def main():
    cat = {}
    with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt") as f:
        for line in f:
            e = json.loads(line)
            cat[e["id"]] = e
    rows = list(csv.DictReader(open(DR / "generation_it44_20261110/entity_roles_it44.tsv", encoding="utf-8"), delimiter="\t"))
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["relation_id", "molecule", "name", "role", "role_basis", "reference_class", "modality", "molecule_type", "verdict"])
    tally = collections.Counter()
    for r in rows:
        e = cat.get(r["molecule"])
        ref = reference_class(e)
        v = verdict(r["role"], ref)
        tally[(r["role"], v)] += 1
        out.writerow([r["relation_id"], r["molecule"], r["name"], r["role"], r["role_basis"], ref, (e or {}).get("modality", ""), (e or {}).get("molecule_type", ""), v])
    sys.stderr.write(f"{len(rows)} rows\n")
    for (role, v), n in sorted(tally.items()):
        sys.stderr.write(f"  {role}: {v}: {n}\n")


if __name__ == "__main__":
    main()
