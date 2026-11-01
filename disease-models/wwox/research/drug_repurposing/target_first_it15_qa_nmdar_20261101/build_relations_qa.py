#!/usr/bin/env python3
"""Offline: raw/act_*.json (framework/adapters/chembl.py output) + GtoPdb + DGIdb + DrugCentral file -> relations_qa.tsv, assay_context_qa.tsv,
perimeter_log.tsv. Then grades with scout_it14_p6_20261101/selectivity_p6.py (collect/grade_group imported, unchanged) -> graded_comparisons_qa.tsv.
Reads only; --help is safe. Paths: DR cache is the main checkout cache (untracked data)."""
import argparse, csv, glob, gzip, json, os, re, statistics, sys, collections
ap = argparse.ArgumentParser(description=__doc__); ap.parse_args()
H = os.path.dirname(os.path.abspath(__file__)); DR = os.path.abspath(os.path.join(H, ".."))
CACHE = "/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache"
DCF = os.environ.get("DC_FILE", "")
sys.path.insert(0, os.path.join(DR, "scout_it14_p6_20261101"))
import selectivity_p6 as S
NM = {"nM": 1.0, "uM": 1e3, "mM": 1e6, "pM": 1e-3}
rows, ctx, plog = [], {}, []
def add(*a): rows.append(a)
# ChEMBL
for fn in sorted(glob.glob(os.path.join(H, "raw", "act_*.json"))) + sorted(glob.glob(os.path.join(H, "raw", "mol_*.json"))):
    o = json.load(open(fn)); b = os.path.basename(fn)[:-5]
    plog.append([b, ("chembl adapter target=%s types=[%s] max_rows=2000" % tuple(b[4:].rsplit("_", 1))) if b.startswith("act_") else "chembl adapter molecule=%s (all targets) types=IC50,Ki,Kd,EC50 max_rows=2000" % b[4:], o.get("source_version", ""), o.get("status"), o.get("total_count"), o.get("retrieved"), o.get("truncated"), (o.get("error") or "")[:80], (o.get("note") or "")[:160]])
    for h in o["hits"]:
        if h.get("kind") != "activity": continue
        u = h["standard_units"]; v = h["standard_value"]
        val = float(v) * NM[u] if (v not in (None, "") and u in NM) else None
        g = "|".join(sorted(x.upper() for x in (h.get("target_gene_symbols") or [])))
        comp = h["parent_molecule_chembl_id"] or h["molecule_chembl_id"]
        if b.startswith("mol_") and not ("GRIN" in g or "NMDA" in (h["target_pref_name"] or "").upper()): continue
        add("chembl_activity", comp, g, h["target_pref_name"], "", h["standard_type"], h["standard_relation"] or "", "" if val is None else val, h["target_organism"] or "",
            f"{h['target_chembl_id']};{h['document_chembl_id']};{h['assay_chembl_id']}", h["molecule_chembl_id"], h.get("molecule_pref_name") or "", u or "", h.get("data_validity_comment") or "", h.get("target_type") or "", h["activity_id"])
        a = h.get("assay_context")
        if a and h["assay_chembl_id"] not in ctx:
            ctx[h["assay_chembl_id"]] = [h["assay_chembl_id"], h["document_chembl_id"], a.get("assay_type") or "", a.get("assay_cell_type") or "", a.get("assay_organism") or "", a.get("confidence_score") or "", a.get("relationship_type") or "", h.get("data_validity_comment") or "", h.get("potential_duplicate") or "", (a.get("description") or "").replace("\t", " ").replace("\n", " "), "framework/adapters/chembl.py"]
# dedupe on activity_id (same row may appear twice across target-types)
seen, out = set(), []
for r in rows:
    if r[15] in seen: continue
    seen.add(r[15]); out.append(r)
rows = out
HDR = ["source", "compound", "gene", "target_label", "action", "measure_type", "relation", "value_nM", "species", "ref", "molecule_chembl_id", "molecule_pref_name", "units_raw", "validity_comment", "target_type", "activity_id"]
with open(os.path.join(H, "relations_qa.tsv"), "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(HDR)
    for r in rows: w.writerow(r)
    # GtoPdb
    ver = "GtoPdb 2026.3.1"
    G = open(CACHE + "/gtopdb/interactions.csv", encoding="utf8"); G.readline()
    for x in csv.DictReader(G):
        if not (x["Target Gene Symbol"] or "").startswith("GRIN"): continue
        v = x["Affinity Median"]; px = x["Affinity Units"].startswith("p") and v
        w.writerow(["gtopdb", x["Ligand"], x["Target Gene Symbol"], x["Target"], x["Action"], x["Affinity Units"], x["Original Affinity Relation"], (10 ** (9 - float(v))) if px else "", x["Target Species"], "PMID:" + x["PubMed ID"], "gtopdb:" + x["Ligand ID"], "", "", "", "", ""])
    # DGIdb (direction only)
    for x in csv.DictReader(open(CACHE + "/dgidb/interactions.tsv"), delimiter="\t"):
        if x["gene_name"].startswith("GRIN") and x["gene_name"] != "GRINA":
            w.writerow(["dgidb", x["drug_name"], x["gene_name"], "", x["interaction_type"], "", "", "", "", x["interaction_source_db_name"], x["drug_concept_id"], "", "", "", "", ""])
    if DCF and os.path.exists(DCF):
        for x in csv.DictReader(gzip.open(DCF, "rt", encoding="utf8", errors="ignore"), delimiter="\t"):
            if "GRIN" in x["GENE"].upper():
                w.writerow(["drugcentral", x["DRUG_NAME"], x["GENE"].upper(), x["TARGET_NAME"], x["ACTION_TYPE"], x["ACT_TYPE"], x["RELATION"], (10 ** (9 - float(x["ACT_VALUE"]))) if x["ACT_VALUE"] else "", x["ORGANISM"], x["ACT_SOURCE"] + ";" + (x["ACT_SOURCE_URL"] or x["MOA_SOURCE"]), "dc:" + x["STRUCT_ID"], "", "", "", "", ""])
with open(os.path.join(H, "assay_context_qa.tsv"), "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["assay_id", "document_id", "assay_type", "assay_cell_type", "assay_organism", "confidence_score", "relationship_type", "data_validity_comment", "potential_duplicate", "description", "fetched_from"])
    for k in sorted(ctx): w.writerow(ctx[k])
with open(os.path.join(H, "perimeter_log.tsv"), "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["query_id", "parameters", "source_version", "status", "total_count", "retrieved", "truncated", "error", "note"])
    for p in plog: w.writerow(p)
print(len(rows), "chembl rows;", len(ctx), "assays;", len(plog), "queries")
# grade
rr = [dict(zip(HDR, r)) for r in csv.reader(open(os.path.join(H, "relations_qa.tsv")), delimiter="\t")][1:]
for r in rr: r["ref"] = r["ref"]
S.H = H
# verifier item 1: reference-value rows (79 nM for all four GluN2 subunits) are not a subunit comparison; ignored for grading
rr = [r for r in rr if not (r['compound'] == 'CHEMBL5095095' and r['ref'].split(';')[1:2] == ['CHEMBL6134891'])]
cx = {}
for r in csv.DictReader(open(os.path.join(H, "assay_context_qa.tsv")), delimiter="\t"):
    cx[r["assay_id"]] = {"assay_cell_type": r["assay_cell_type"], "description": r["description"], "data_validity_comment": r["data_validity_comment"]}
groups = S.collect(rr)
with open(os.path.join(H, "graded_comparisons_qa.tsv"), "w") as f:
    f.write("\t".join(["compound", "document", "measure", "species", "n_targets", "grade", "limits", "targets_median_nM [n; min-max; censored]", "ratio_extreme_target_medians", "ratio_not_computed_because"]) + "\n")
    for k, obs in sorted(groups.items()):
        if len({o[0] for o in obs}) < 2: continue
        fams = collections.defaultdict(list)
        for o in obs: fams[S.family(o[0].split("|")[0])].append(o)
        parts = [(k, obs, "")]
        if len(fams) > 1:
            parts += [((k[0], k[1] + "#" + fam, k[2], k[3]), fo, fam) for fam, fo in sorted(fams.items()) if len({o[0] for o in fo}) > 1]
        for kk, oo, fam in parts: S.emit(f, kk, oo, cx, skip_if_undeterminable=bool(fam))
