#!/usr/bin/env python3
"""P12 resource comparison on one real question: which compounds are recorded on GRIN2B (GluN2B), and what does
each resource say about each one? Resources: ChEMBL live REST (adapter, target CHEMBL1904, human single protein),
GtoPdb 2026.3.1 CSV (catalog cache), DGIdb 2024 TSV (catalog cache). Equivalent units: distinct named compounds with
>=1 record on the target entity; per-record content is compared apart. Writes grin2b_comparison.json."""
import csv, json, sys, time
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__); sys.exit(0)
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from framework.adapters import chembl  # noqa: E402
import os
# the gitignored cache lives in the main checkout; a task worktree reaches it through LEGEND_CATALOG_CACHE
CACHE = Path(os.environ.get("LEGEND_CATALOG_CACHE") or ROOT / "disease-models/wwox/research/drug_repurposing/catalog/cache")
HERE = Path(__file__).parent
out = {"retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

t0 = time.time()
a = chembl.query({"target": "CHEMBL1904", "types": ["IC50", "Ki", "Kd", "EC50"], "max_rows": 2000})
mols = {}
for h in a["hits"]:
    mols.setdefault(h["parent_molecule_chembl_id"] or h["molecule_chembl_id"], []).append(h)
out["chembl_live"] = {"source_version": a["source_version"], "rows_total": a.get("total_count"), "rows_retrieved": a.get("retrieved"), "truncated": a.get("truncated"),
    "distinct_molecules_in_retrieved": len(mols), "named_molecules_in_retrieved": sum(1 for v in mols.values() if v[0].get("molecule_pref_name")),
    "rows_with_assay_context": sum(1 for h in a["hits"] if h["assay_context"]), "assay_organisms": sorted({(h["assay_context"] or {}).get("assay_organism") or "NA" for h in a["hits"]}),
    "seconds": round(time.time() - t0, 1), "requests": len(a["requests_sent"])}

g = csv.reader(open(CACHE / "gtopdb/interactions.csv")); version = next(g)[0]; head = next(g)
rows = [dict(zip(head, r)) for r in g]
gt = [r for r in rows if "GRIN2B" in (r["Target Gene Symbol"] or "").split("|")]
out["gtopdb"] = {"version": version.strip('"# '), "records_on_GRIN2B": len(gt), "distinct_ligands": len({r["Ligand"] for r in gt}),
    "records_with_numeric_affinity": sum(1 for r in gt if r["Affinity Median"] not in ("", "-")), "with_action": sum(1 for r in gt if r["Action"] not in ("", "None")),
    "with_receptor_site": sum(1 for r in gt if r["Receptor Site"]), "species": sorted({r["Target Species"] for r in gt}),
    "pubmed_ids_present": sum(1 for r in gt if r["PubMed ID"])}

d = csv.DictReader(open(CACHE / "dgidb/interactions.tsv"), delimiter="\t")
dg = [r for r in d if r["gene_name"] == "GRIN2B"]
out["dgidb"] = {"records_on_GRIN2B": len(dg), "distinct_drugs": len({r["drug_name"] for r in dg}), "sources": sorted({f"{r['interaction_source_db_name']} {r['interaction_source_db_version']}" for r in dg}),
    "records_with_interaction_type": sum(1 for r in dg if r["interaction_type"] not in ("", "NULL")), "records_with_potency": 0,
    "note": "DGIdb carries no potency, assay or species column; its ChEMBL rows come from the imported release named above"}

def norm(s): return "".join(ch for ch in (s or "").lower() if ch.isalnum())
names = {"chembl": {norm(v[0].get("molecule_pref_name")) for v in mols.values() if v[0].get("molecule_pref_name")},
         "gtopdb": {norm(r["Ligand"]) for r in gt}, "dgidb": {norm(r["drug_name"]) for r in dg}}
names["dgidb"] = {n for n in names["dgidb"]}
inter = {f"{a_}&{b_}": len(names[a_] & names[b_]) for a_, b_ in (("chembl", "gtopdb"), ("chembl", "dgidb"), ("gtopdb", "dgidb"))}
out["name_overlap_normalised"] = {"sizes": {k: len(v) for k, v in names.items()}, "pairwise_intersections": inter,
    "caveat": "name-normalised overlap only (salts and synonyms not merged); ChEMBL set is from retrieved rows, a lower bound when truncated"}
(HERE / "grin2b_comparison.json").write_text(json.dumps(out, indent=1, sort_keys=True))
print(json.dumps(out, indent=1)[:3500])
