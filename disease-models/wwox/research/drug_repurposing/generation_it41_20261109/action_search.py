"""IT41 P4: action-and-context-guided search, driven by relations_it41.tsv (a new relation is a new row, not new code).
For each relation it reads (a) the ChEMBL curated mechanism rows through the search layer and (b) the GtoPdb interaction table of the catalogue cache
(species, type, action, receptor site, selectivity comment, primary-target flag, affinity, assay text). Source rows stay separate; molecules are counted distinct;
nothing is scored or ranked. A catalogue row on a receptor family is not subunit selectivity; an absent row is not an absent action.
  python3 action_search.py   -> writes search_rows.tsv (one row per source row) and molecules.tsv (one row per distinct molecule per relation)"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework/scripts"))
import compound_catalog as cc, repurposing_search as rs  # noqa: E402
CACHE = HERE.parent / "catalog/cache/gtopdb/interactions.csv"
if not CACHE.exists(): CACHE = Path("/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache/gtopdb/interactions.csv")

def gtopdb_rows():
    with open(CACHE, encoding="utf-8", newline="") as f:
        f.readline(); return list(csv.DictReader(f))

def main():
    rel = list(csv.DictReader(open(HERE / "relations_it41.tsv", encoding="utf-8"), delimiter="\t"))
    es = cc.load(cc.DEFAULT_CATALOG); idx = rs.Index(es)
    gt_to_cat = {}
    for e in es:
        for sr in e.get("source_records", []):
            if sr.get("source") in ("gtopdb", "GtoPdb"): gt_to_cat[str(sr["id"])] = e["id"]
    G = gtopdb_rows(); out = []
    for r in rel:
        syms = {s.upper() for s in r["target_symbols"].split(";")}
        for s in syms:
            for e, t in idx.chembl_human.get(s, []):
                ca = t.get("action_type") or ""
                ng = len(t.get("gene_symbols") or [])
                out.append(dict(relation_id=r["relation_id"], source="ChEMBL curated mechanism", molecule=(e.get("relations") or {}).get("parent") or e["id"], name=e["name"], catalogue_id=e["id"], species="Homo sapiens", action=ca, direction=rs.action_direction(ca),
                    site_or_granularity=("single_protein_record" if ng == 1 else "two_gene_assembly_record" if ng == 2 else "family_record_subunit_unresolved"), primary_target="", selectivity_comment="", affinity="", assay_or_note=t.get("mechanism_of_action") or "", pubmed="", target_symbol=s))
        for g in G:
            gs = {x.strip().upper() for x in re.split(r"[|;,]", g["Target Gene Symbol"] or "") if x.strip()}
            if not gs & syms: continue
            act = f"{g['Type']}/{g['Action']}"
            low = act.lower()
            cid = gt_to_cat.get(g["Ligand ID"], "")
            par = ((idx.by_id.get(cid) or {}).get("relations") or {}).get("parent") or cid
            out.append(dict(relation_id=r["relation_id"], source="GtoPdb interaction", molecule=(par or "GTOPDB:" + g["Ligand ID"]), name=g["Ligand"], catalogue_id=cid, species=g["Target Species"], action=act,
                direction=("down" if re.search(r"inverse agonist|antagon|inhibit|block|negative", low) else "up" if re.search(r"agonist|activat|positive|potentiat", low) else "unclear"),
                site_or_granularity=g["Receptor Site"] or "", primary_target=g["Primary Target"], selectivity_comment=g["Selectivity"] + (" | " + g["Action comment"] if g["Action comment"] else ""),
                affinity=" ".join(x for x in (g["Affinity Median"], g["Affinity Units"], "(" + g["Original Affinity Relation"] + ")" if g["Original Affinity Relation"] else "") if x), assay_or_note=g["Assay Description"], pubmed=g["PubMed ID"], target_symbol=g["Target Gene Symbol"]))
    for o in out: o["labelled_form"] = "yes" if re.match(r"^\[?<sup>|^\[<sup>", o["name"]) or "[<sup>" in o["name"] else ""
    F = list(out[0].keys())
    with open(HERE / "search_rows.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, F, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    M = defaultdict(list)
    for o in out:
        if o["labelled_form"] == "yes": continue      # radiolabelled forms duplicate another record of the same ligand
        M[(o["relation_id"], o["molecule"])].append(o)
    rows = []
    for (rid, mol), rs_ in sorted(M.items()):
        rows.append(dict(relation_id=rid, molecule=mol, names=" | ".join(sorted({x["name"] for x in rs_}))[:160], sources=";".join(sorted({x["source"] for x in rs_})), n_source_rows=len(rs_), directions=";".join(sorted({x["direction"] for x in rs_})),
            species=";".join(sorted({x["species"] for x in rs_})), sites=";".join(sorted({x["site_or_granularity"] for x in rs_ if x["site_or_granularity"]}))[:120]))
    with open(HERE / "molecules.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(rows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print(len(out), "source rows;", len(rows), "molecule x relation rows")
if __name__ == "__main__": main()
