"""SCI43 S3: catalogue lookup by K+ family BEFORE any compound is named. Read-only, offline, no score, no ranking.
Lists, per target symbol group, the parent molecules the catalogue holds, the catalogue action and direction, the granularity of the
target record (one protein, a two-gene assembly, a family) and max phase. A catalogue row is a source-level annotation, not selectivity,
exposure or function in a neuron.
  python3 catalogue_by_family.py  -> output/catalogue_by_family.tsv, output/catalogue_family_summary.tsv"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework/scripts"))
sys.path.insert(0, str(ROOT / "disease-models/wwox/research/drug_repurposing/mechsearch_it40_20261109"))
import compound_catalog as cc, repurposing_search as rs  # noqa: E402

FAMILIES = [
 ("F-Kv7", "Kv7 / M-current (KCNQ2-5)", ["KCNQ2", "KCNQ3", "KCNQ4", "KCNQ5"]),
 ("F-Kir2", "Kir2 inward rectifier (KCNJ2, KCNJ12, KCNJ4, KCNJ14)", ["KCNJ2", "KCNJ12", "KCNJ4", "KCNJ14"]),
 ("F-GIRK", "GIRK (KCNJ3, KCNJ6, KCNJ9, KCNJ5)", ["KCNJ3", "KCNJ6", "KCNJ9", "KCNJ5"]),
 ("F-K2P-TASK", "K2P TASK (KCNK3, KCNK9, KCNK1, KCNK5, KCNK16, KCNK17)", ["KCNK3", "KCNK9", "KCNK1", "KCNK5", "KCNK16", "KCNK17"]),
 ("F-K2P-TREK", "K2P TREK/TRAAK (KCNK2, KCNK10, KCNK4)", ["KCNK2", "KCNK10", "KCNK4"]),
 ("F-HCN", "HCN (comparison arm, not K+)", ["HCN1", "HCN2", "HCN3", "HCN4"]),
]

def main():
    es = cc.load(cc.DEFAULT_CATALOG); idx = rs.Index(es)
    out, summ = [], []
    for fid, label, syms in FAMILIES:
        seen = {}
        for s in syms:
            for e, t in idx.chembl_human.get(s.upper(), []):
                phase = max([r.get("max_phase") or 0 for r in e.get("status_records", [])] or [0])
                ca = t.get("action_type") or t.get("action") or ""
                ng = len(t.get("gene_symbols") or [])
                gran = "single_protein_record" if ng == 1 else ("two_gene_assembly_record" if ng == 2 else "family_record_subunit_unresolved")
                parent = (e.get("relations") or {}).get("parent") or e["id"]
                seen[(e["id"], s)] = [fid, label, s, e["id"], e["name"], ca, rs.action_direction(ca), (t.get("target_chembl_id") or ""), ng, gran, parent, phase]
        rows = sorted(seen.values(), key=lambda r: (r[2], -float(r[11] or 0), r[4]))
        out += rows
        parents = {r[10] for r in rows}
        by_dir = {}
        for r in rows: by_dir.setdefault(r[6], set()).add(r[10])
        summ.append([fid, label, len(rows), len(parents), "; ".join(f"{d}={len(p)}" for d, p in sorted(by_dir.items())) or "none"])
        if not rows: out.append([fid, label, ",".join(syms), "", "NO_CATALOGUE_MECHANISM_ROW", "", "", "", "", "", "", ""])
    hdr = ["family", "label", "target_symbol", "catalogue_id", "name", "catalogue_action", "direction", "catalogue_target_id", "target_n_genes", "target_record_granularity", "parent_molecule", "max_phase"]
    with open(HERE / "output/catalogue_by_family.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(hdr); w.writerows(out)
    with open(HERE / "output/catalogue_family_summary.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["family", "label", "rows", "distinct_parent_molecules", "parents_by_direction"]); w.writerows(summ)
    print(len(out), "rows"); [print(s) for s in summ]
main()
