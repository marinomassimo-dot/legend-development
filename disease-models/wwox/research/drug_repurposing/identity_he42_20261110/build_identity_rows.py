#!/usr/bin/env python3
"""Rows for identity_table.tsv from a spec (query_name, expected_genes): one row per name and expected gene, so a value under one
subunit is never read as a measure on another. Uses compound_identity (resolve + target_evidence) and the ChEMBL adapter online.
  python3 build_identity_rows.py spec.tsv identity_table_additions.tsv"""
import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "framework/scripts"))
import compound_catalog as cc, compound_identity as ci, repurposing_adapter as ad  # noqa: E402
HDR = ["query_name", "identity_state", "best_catalogue_id", "record_name", "record_chembl_refs", "declared_chembl_id", "label_conflict",
       "expected_gene", "evidence_level", "n_rows", "selectivity", "other_genes_seen_top5", "chembl_read_status"]

def main(spec, out):
    es = cc.load(cc.DEFAULT_CATALOG); q = lambda req: ad.load("chembl").query(req)
    rows = []
    for s in csv.DictReader(open(spec, encoding="utf-8"), delimiter="\t"):
        genes = s["expected_genes"].split(","); res = ci.resolve(es, s["query_name"]); t = ci.target_evidence(res, genes, es, q)
        c = res["candidates"][0] if res["candidates"] else {}
        for g in genes:
            pg = t["per_gene"][g]
            rows.append([s["query_name"], res["identity_state"], c.get("catalogue_id", ""), c.get("record_name", ""), ";".join(r["chembl_id"] for r in c.get("chembl_refs", [])),
                         ";".join(d["chembl_id"] for d in res["declarations"] if d["role"] == "identity"), "yes" if res["label_conflict"] else "no", g, pg["level"], pg["n_rows"],
                         t["selectivity"], "|".join(f"{k}:{v}" for k, v in list(t["other_genes_seen"].items())[:5]),
                         "|".join(f"{r['chembl_id']}:{r['mechanism_status']}/{r['activity_coverage']}/{r['activity_rows']}" for r in t["chembl_read"])])
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(HDR); w.writerows(rows)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
