#!/usr/bin/env python3
"""Join the names of a compound view to identity_table.tsv through compound_identity.join_names (EXACT / QUALIFIED / MULTI_PART attach a row;
PROPOSED_ONLY and NO_CANDIDATE attach none). Replaces the substring fallback of consume_reader.py; same output columns plus link, key, qualifier, proposed_keys.
  python3 identity_join.py <compound_view.tsv> <identity_table.tsv> <out.tsv>"""
import csv, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "framework/scripts"))
import compound_identity as ci  # noqa: E402

def main(view, table, out):
    ident = {}
    for r in csv.DictReader(open(table, encoding="utf-8"), delimiter="\t"):
        ident.setdefault(r["query_name"].lower(), []).append(r)
    rows = []
    for c in csv.DictReader(open(view, encoding="utf-8"), delimiter="\t"):
        for nm in [x.strip() for x in c["name_full"].split(";") if x.strip()]:
            for j in ci.join_names(nm, ident):
                base = [c["item_id"], j["part"], j["link"], j["key"] or "", j["qualifier"], "|".join(j.get("proposed_keys") or [])]
                hits = ident.get(j["key"]) if j["key"] else None
                if not hits:
                    rows.append(base + ["NO_IDENTITY_ROW", "", "", "", ""]); continue
                for h in hits:
                    rows.append(base + [h["identity_state"], h["label_conflict"], h["expected_gene"], h["evidence_level"], h["selectivity"]])
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["item_id", "name", "link", "key", "qualifier", "proposed_keys", "identity_state", "label_conflict", "expected_gene", "evidence_level", "selectivity"]); w.writerows(rows)
    print(len(rows), "rows")

if __name__ == "__main__":
    main(*sys.argv[1:4])
