#!/usr/bin/env python3
"""IT15 Q-B step 4: relations_qb.tsv + assay_context_qb.tsv from the raw pulls, then same-document grading with the P6 logic
(imported, not copied: collect / grade_group / emit from ../scout_it14_p6_20261101/selectivity_p6.py). Writes graded_comparisons_qb.tsv."""
import sys, os, json, csv, glob, argparse, statistics, collections
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, "..", "scout_it14_p6_20261101"))
import selectivity_p6 as S
UNIT = {"nM": 1.0, "uM": 1e3, "mM": 1e6, "pM": 1e-3, "M": 1e9}
CACHE = "/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache"
MOLS = {"CHEMBL3545157": "TIDEGLUSIB", "CHEMBL1200826": "LITHIUM CARBONATE", "CHEMBL1234004": "LITHIUM ION", "CHEMBL412142": "LADUVIGLUSIB (CHIR-99021)",
        "CHEMBL362558": "LY-2090314", "CHEMBL1969664": "AZD-1080", "CHEMBL102714": "SB-216763", "CHEMBL296586": "KENPAULLONE",
        "CHEMBL336961": "1-AZAKENPAULLONE", "CHEMBL483465": "ELRAGLUSIB"}
def main(raw):
    rel, ctx = [], {}
    hdr = ["source", "compound", "gene", "target_label", "action", "measure_type", "relation", "value_nM", "species", "ref"]
    for mid, nm in MOLS.items():
        f = os.path.join(raw, f"mol_{mid}.json")
        if not os.path.exists(f): continue
        o = json.load(open(f))
        for h in o["hits"]:
            u, v = h.get("standard_units"), h.get("standard_value")
            nM = float(v) * UNIT[u] if (v not in (None, "") and u in UNIT) else None
            genes = "|".join(h.get("target_gene_symbols") or [])
            comp = f"{nm} [{mid}]"
            rel.append(["chembl_activity", comp, genes, h.get("target_pref_name") or "", "", h["standard_type"], h.get("standard_relation") or "=", "" if nM is None else repr(nM),
                        h.get("target_organism") or "", f'{h["target_chembl_id"]};{h["document_chembl_id"]};{h["assay_chembl_id"]}'])
            ac = h.get("assay_context") or {}
            if h["assay_chembl_id"] not in ctx:
                ctx[h["assay_chembl_id"]] = [h["assay_chembl_id"], ac.get("assay_cell_type") or "", ac.get("assay_type") or "", ac.get("assay_organism") or "",
                                             (ac.get("description") or h.get("assay_description") or "").replace("\t", " ").replace("\n", " "), h.get("data_validity_comment") or "",
                                             h["document_chembl_id"], h.get("document_year") or "", "context_present" if ac else "context_missing"]
    # mechanism rows from the name queries
    for n in ("tideglusib", "lithium_carbonate", "elraglusib"):
        o = json.load(open(os.path.join(raw, f"name_{n}.json")))
        for h in o["hits"]:
            if h["kind"] == "mechanism":
                rel.append(["chembl_mechanism", f'{h["pref_name"]} [{h["molecule_chembl_id"]}]', "", h["mechanism_of_action"], h["action_type"], "", "", "", "", h["target_chembl_id"] + ";" + ",".join(h["references"])])
    # GtoPdb
    R = list(csv.reader(open(CACHE + "/gtopdb/interactions.csv")))[2:]
    Hh = list(csv.reader(open(CACHE + "/gtopdb/interactions.csv")))[1]
    for r in R:
        x = dict(zip(Hh, r))
        if x["Target Gene Symbol"] in ("GSK3A", "GSK3B"):
            try: nM = 10 ** (9 - float(x["Affinity Median"])) if x["Affinity Units"].startswith("p") else None
            except ValueError: nM = None
            rel.append(["gtopdb", x["Ligand"].replace("<sup>", "").replace("</sup>", ""), x["Target Gene Symbol"], x["Target"], x["Action"], x["Affinity Units"].lstrip("p") if x["Affinity Units"] else "",
                        x["Original Affinity Relation"], "" if nM is None else repr(nM), x["Target Species"], "PMID:" + x["PubMed ID"] + ";sel=" + x["Selectivity"] + ";primary=" + x["Primary Target"] + ";comment=" + x["Action comment"][:80]])
    with open(os.path.join(H, "relations_qb.tsv"), "w") as f:
        f.write("\t".join(hdr) + "\n")
        for r in rel: f.write("\t".join(map(str, r)) + "\n")
    with open(os.path.join(H, "assay_context_qb.tsv"), "w") as f:
        f.write("\t".join(["assay_id", "assay_cell_type", "assay_type", "assay_organism", "description", "data_validity_comment", "document", "year", "context"]) + "\n")
        for c in ctx.values(): f.write("\t".join(map(str, c)) + "\n")
    cx = {k: {"assay_cell_type": v[1], "description": v[4], "data_validity_comment": v[5]} for k, v in ctx.items()}
    rows = [dict(zip(hdr, r)) for r in rel]
    groups = S.collect(rows)
    cols = ["compound", "document", "measure", "species", "n_targets", "grade", "limits", "targets_median_nM [n; min-max; censored]", "ratio_extreme_target_medians", "ratio_not_computed_because", "gsk3_pair"]
    n = 0
    with open(os.path.join(H, "graded_comparisons_qb.tsv"), "w") as f:
        f.write("\t".join(cols) + "\n")
        for k, obs in sorted(groups.items()):
            genes = {o[0] for o in obs}
            if len(genes) < 2: continue
            fams = collections.defaultdict(list)
            for o in obs: fams[S.family(o[0].split("|")[0])].append(o)
            parts = [(k, obs, "")] + ([((k[0], k[1] + "#" + fam, k[2], k[3]), fo, fam) for fam, fo in sorted(fams.items()) if len({o[0] for o in fo}) > 1] if len(fams) > 1 else [])
            for kk, oo, fam in parts:
                import io
                buf = io.StringIO(); S.emit(buf, kk, oo, cx, skip_if_undeterminable=bool(fam))
                line = buf.getvalue().rstrip("\n")
                if not line: continue
                gs = {o[0] for o in oo}
                pair = "GSK3A+GSK3B" if {"GSK3A", "GSK3B"} <= gs else ("GSK3 + other" if gs & {"GSK3A", "GSK3B"} else "")
                f.write(line + "\t" + pair + "\n"); n += 1
    print("relations", len(rel), "assays", len(ctx), "graded groups", n)
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--raw", required=True); main(ap.parse_args().raw)
