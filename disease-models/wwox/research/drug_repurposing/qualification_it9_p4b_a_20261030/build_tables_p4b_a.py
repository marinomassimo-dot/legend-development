#!/usr/bin/env python3
"""Offline, deterministic tables for the IT9 P4b group-A qualification, built from collected.json.gz and collected_supp.json.gz.

  build_tables_p4b_a.py --help     this text
  build_tables_p4b_a.py build      writes chembl_rows_selected.tsv, chembl_row_counts.tsv, trials_registry_search.tsv, edge_provenance_live.tsv,
                                   hpa_adult_expression.tsv, faers_counts.tsv
No network. Measures are kept per assay type, species and relation; nothing is aggregated across types or units. A state (ROWS / NO_ROWS /
SERVICE_ERROR) is written wherever a query returned nothing, because absent data, a service error and a negative result are different things."""
import csv, gzip, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEEP_TARGETS = {
    "balsalazide": {"CHEMBL2163183": "SIRT5", "CHEMBL235": "PPARG", "CHEMBL215": "ALOX5", "CHEMBL221": "PTGS1", "CHEMBL230": "PTGS2"},
    "mesalamine": {"CHEMBL235": "PPARG", "CHEMBL215": "ALOX5", "CHEMBL4261": "HIF1A", "CHEMBL2094253": "COX"},
    "ramelteon": {"CHEMBL1945": "MTNR1A", "CHEMBL1946": "MTNR1B", "CHEMBL2094268": "MT receptor (group)", "CHEMBL613617": "rat brain level", "CHEMBL613652": "rat plasma level", "CHEMBL340": "CYP3A4"},
    "belzutifan": {"CHEMBL1744522": "EPAS1 (HIF-2alpha)", "CHEMBL340": "CYP3A4", "CHEMBL240": "hERG"},
    "ceperognastat": {"CHEMBL5921": "OGA"},
    "AR-12": {"CHEMBL2534": "PDPK1", "CHEMBL5859": "AKT1 (mouse cells)", "CHEMBL384": "HT-29 cells", "CHEMBL4766": "PDK1 (PDH kinase)", "CHEMBL3861": "PDK2 (PDH kinase)",
              "CHEMBL3893": "PDK3 (PDH kinase)", "CHEMBL4141": "PDK4 (PDH kinase)", "CHEMBL2096665": "PDK (PDH kinase, group)"},
}


def tsv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for r in rows:
            w.writerow(["" if v is None else str(v).replace("\t", " ").replace("\n", " ") for v in r])


def build():
    R = json.load(gzip.open(HERE / "collected.json.gz", "rt"))
    S = json.load(gzip.open(HERE / "collected_supp.json.gz", "rt"))
    # ChEMBL: rows on kept targets, then counts
    rows, counts = [], []
    for name, tg in KEEP_TARGETS.items():
        d = R["chembl"][name]
        a = d["activity"]
        counts.append([name, d["molecule"]["molecule_chembl_id"], a["state"], a.get("total"), len(a["rows"]), "yes" if a.get("total") == len(a["rows"]) else "TRUNCATED",
                       len(d["mechanism"]["rows"]), "; ".join(f'{m["mechanism_of_action"]} ({m["target_chembl_id"]})' for m in d["mechanism"]["rows"])])
        found = set()
        for r in a["rows"]:
            t = r.get("target_chembl_id")
            if t not in tg:
                continue
            found.add(t)
            ac = d["assays"].get(r["assay_chembl_id"]) or {}
            rows.append([name, tg[t], t, r["standard_type"], r.get("standard_relation") or "", r.get("standard_value") or "", r.get("standard_units") or "", ac.get("assay_type") or "",
                         ac.get("assay_organism") or r.get("target_organism") or "", ac.get("assay_cell_type") or "", r["assay_chembl_id"], r["document_chembl_id"], r.get("document_year") or "",
                         (r.get("assay_description") or "")[:200], "ROWS"])
        for t, lab in tg.items():
            if t not in found:
                rows.append([name, lab, t, "", "", "", "", "", "", "", "", "", "", "no activity row for this molecule on this target in the complete molecule-first pull", "NO_ROWS_FOR_THIS_TARGET"])
    tsv(HERE / "chembl_rows_selected.tsv", ["molecule", "target_label", "target_chembl_id", "standard_type", "relation", "value", "units", "assay_type", "assay_organism", "assay_cell_type", "assay_id", "document_id", "year", "assay_description", "state"], rows)
    tsv(HERE / "chembl_row_counts.tsv", ["molecule", "chembl_id", "state", "total_count", "rows_retrieved", "complete", "curated_mechanism_rows", "curated_mechanism"], counts)
    # trials
    trows = []
    for comp, res in R["ctg"].items():
        if comp.startswith("_"):
            continue
        for k, v in res.items():
            term, cond = k.split("|")
            if cond == "ALL":
                trows.append([comp, term, "(any condition)", v[0], v[1], "", "2026-10-30"])
            else:
                tc = v[1].get("totalCount") if isinstance(v[1], dict) else None
                ids = ";".join(s["protocolSection"]["identificationModule"]["nctId"] for s in (v[1].get("studies") or [])) if isinstance(v[1], dict) else ""
                trows.append([comp, term, cond, v[0], tc, ids, "2026-10-30"])
    tsv(HERE / "trials_registry_search.tsv", ["compound", "intervention_term", "condition_term", "http_status", "hits", "nct_ids_if_any", "query_date"], trows)
    # live omnipath records
    erows = []
    for k, v in R["omnipath"].items():
        s_, t_ = k.split(">")
        for lab in ("main", "collectri"):
            st, p = v[lab]
            lines = [l.split("\t") for l in p.strip().split("\n")] if st == 200 and p else []
            hit = [r for r in lines[1:] if r[2] == s_ and r[3] == t_]
            if not hit:
                erows.append([k, lab, st, "NO_MATCHING_RECORD", "", "", "", "", ""])
            for r in hit:
                erows.append([k, lab, st, "RECORD", r[12], "stimulation" if r[5] == "True" and r[6] != "True" else ("inhibition" if r[6] == "True" and r[5] != "True" else "both"), r[10], r[11], r[13]])
    tsv(HERE / "edge_provenance_live.tsv", ["edge", "query", "http_status", "state", "interaction_type", "sign", "sources", "references", "curation_effort"], erows)
    # HPA
    hrows = []
    for g, d in R["hpa"].items():
        rec = d.get("record") or {}
        hrows.append([g, d.get("ensembl") or "", d["search_status"], rec.get("RNA tissue specificity", ""), rec.get("RNA single nuclei brain specificity", ""),
                      json.dumps(rec.get("RNA single nuclei brain specific nCPM"), sort_keys=True) if rec.get("RNA single nuclei brain specific nCPM") else "",
                      rec.get("RNA brain regional specificity", ""), rec.get("RNA brain regional distribution", ""), json.dumps(rec.get("RNA single cell type specific nCPM"), sort_keys=True)[:200] if rec.get("RNA single cell type specific nCPM") else "",
                      "ROWS" if rec else "NO_RECORD (symbol not resolved by the HPA search)"])
    tsv(HERE / "hpa_adult_expression.tsv", ["gene", "ensembl", "search_status", "rna_tissue_specificity", "rna_brain_snRNA_specificity", "rna_brain_snRNA_specific_nCPM", "rna_brain_region_specificity", "rna_brain_region_distribution", "rna_single_cell_specific_nCPM_trunc200", "state"], hrows)
    # FAERS counts
    frows = []
    for name, v in S["faers_total"].items():
        frows.append([name, "ALL reports matched", v[0], v[1].get("total") if isinstance(v[1], dict) else v[1]])
    for k, v in S["faers_seizure"].items():
        n, t = k.split("|")
        frows.append([n, t, v[0], v[1]])
    tsv(HERE / "faers_counts.tsv", ["drug", "reaction_term_or_total", "http_status", "report_count"], frows)
    print("built")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build()
    else:
        print(__doc__)
