#!/usr/bin/env python3
"""Pull ChEMBL activity rows on the EBP-orthologue targets and resolve compound names (ADV-001 / IT51-Q05).

Plain urllib, default user agent, public ChEMBL REST, no key, no contact. Writes ebp_activity_rows.tsv and
name_resolution.tsv next to this file. Run: python3 ebp_pull.py [--help]
"""
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.ebi.ac.uk/chembl/api/data"
TARGETS = ["CHEMBL4931", "CHEMBL5525", "CHEMBL3774293", "CHEMBL2311238"]
COMPOUNDS = ["benztropine", "clemastine", "atropine", "ipratropium", "oxybutynin", "quetiapine", "miconazole",
             "ketoconazole", "clobetasol", "amorolfine", "tamoxifen", "ifenprodil", "liothyronine", "bexarotene",
             "sobetirome", "trichostatin A", "apicidin", "fimepinostat", "mevastatin", "neostigmine"]


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa
            last = e
            time.sleep(3)
    raise SystemExit(f"failed {url}: {last}")


def pull_rows():
    rows = []
    for t in TARGETS:
        url = f"{BASE}/activity.json?target_chembl_id={t}&limit=1000"
        while url:
            d = get(url)
            for a in d["activities"]:
                rows.append([t, a.get("activity_id"), a.get("molecule_chembl_id"), a.get("parent_molecule_chembl_id"),
                             a.get("molecule_pref_name") or "", a.get("canonical_smiles") or "",
                             a.get("standard_type") or "", a.get("standard_relation") or "",
                             a.get("standard_value") or "", a.get("standard_units") or "",
                             a.get("assay_chembl_id") or "", (a.get("assay_description") or "")[:200].replace("\t", " "),
                             a.get("document_chembl_id") or "", a.get("assay_type") or ""])
            nxt = d["page_meta"].get("next")
            url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
    return rows


def resolve(name):
    url = f"{BASE}/molecule/search.json?q={urllib.parse.quote(name)}&limit=10"
    d = get(url)
    out = []
    for m in d["molecules"]:
        out.append((m["molecule_chembl_id"], (m.get("molecule_hierarchy") or {}).get("parent_chembl_id") or "",
                    m.get("pref_name") or "", m.get("max_phase")))
    return out


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    rows = pull_rows()
    with open(os.path.join(HERE, "ebp_activity_rows.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["target", "activity_id", "molecule", "parent_molecule", "pref_name", "smiles", "type", "relation", "value",
                    "units", "assay", "assay_description", "document", "assay_type"])
        w.writerows(rows)
    with open(os.path.join(HERE, "name_resolution.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["query_name", "molecule", "parent_molecule", "pref_name", "max_phase"])
        for n in COMPOUNDS:
            for m in resolve(n):
                w.writerow([n, *m])
    print(len(rows), "EBP rows")


if __name__ == "__main__":
    main()
