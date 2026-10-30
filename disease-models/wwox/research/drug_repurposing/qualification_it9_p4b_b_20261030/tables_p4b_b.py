"""Derived tables for qualify_p4b_b.py (offline, deterministic from raw_store.json.gz). Standard library only. Not medical advice."""
import csv, re
from pathlib import Path

# which ChEMBL rows are KEPT as target measures (compound-level target regex per case); everything else stays in raw_store
KEEP = {"P3-05": r"[Ee]strogen receptor", "P3-07": r"p300|CREB-binding|Histone acetyltransferase p300|TRPV4", "P3-08": r"[Cc]aspase|J774|IL-1",
        "P3-09": r"ROR", "P3-17": r"NMDA|Glutamate", "P3-18": r"NMDA|Glutamate"}
NUMT = ("IC50", "Ki", "Kd", "EC50", "Kb", "Kapp", "RBA", "Inhibition", "Activity")


def w(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header)
        wr.writerows(rows)


def build(d, out):
    out = Path(out)
    rows = []
    for cid, e in sorted(d["cases"].items()):
        for fid, a in e["activities"].items():
            for r in a["rows"]:
                if cid in KEEP and re.search(KEEP[cid], (r["target_pref_name"] or "") + " " + (r["assay_description"] or "")) and r["standard_type"] in NUMT:
                    rows.append([cid, e["name"], fid, "case", r["target_pref_name"], r["target_organism"] or "NA", r["assay_type"], r["standard_type"], r["standard_relation"] or "NA",
                                 r["standard_value"] if r["standard_value"] is not None else "NA", r["standard_units"] or "NA", r["document_chembl_id"], (r["assay_description"] or "")[:110]])
    for cid, rel in sorted(d.get("related", {}).items()):
        for mid, x in rel["molecules"].items():
            if (cid == "P3-05" and mid != "CHEMBL411") or (cid == "P3-08" and mid != "CHEMBL4802237"):
                continue
            for r in x["activities"]["rows"]:
                if r["standard_type"] in NUMT:
                    rows.append([cid, d["cases"][cid]["name"], mid, "related:" + rel["why"][:40], r["target_pref_name"], r["target_organism"] or "NA", r["assay_type"], r["standard_type"],
                                 r["standard_relation"] or "NA", r["standard_value"] if r["standard_value"] is not None else "NA", r["standard_units"] or "NA", r["document_chembl_id"], (r["assay_description"] or "")[:110]])
    w(out / "measures_kept.tsv", ["cand_id", "name", "molecule", "record", "target", "species", "assay_type", "standard_type", "relation", "value", "units", "document", "assay"], rows)
    rows = []
    for k, v in sorted(d["edges"].items()):
        for r in v["rows"]:
            rows.append([k, r["source_genesymbol"], r["target_genesymbol"], r["type"], "stim" if r["is_stimulation"] else "", "inh" if r["is_inhibition"] else "", r["curation_effort"],
                         ";".join(r["sources"]), r["references"][:300]])
    w(out / "edges_omnipath.tsv", ["edge", "source", "target", "type", "stimulation", "inhibition", "curation_effort", "sources", "references"], rows)
    rows = []
    for g, v in sorted(d["hpa"].items()):
        h = v["data"] or {}
        rows.append([g, v["http"], h.get("RNA tissue specificity") or "NA", (h.get("RNA tissue specific nTPM") or {}).get("brain", "not listed"), h.get("RNA single cell type specificity") or "NA",
                     "; ".join(f"{k}={x}" for k, x in (h.get("RNA single cell type specific nCPM") or {}).items() if re.search("rain|euron|strocyt|ligodend|icroglia|OPC", k)) or "none listed",
                     h.get("RNA single nuclei brain specificity") or "NA", "; ".join(f"{k}={x}" for k, x in list((h.get("RNA single nuclei brain specific nCPM") or {}).items())[:8]) or "none listed"])
    w(out / "expression_hpa.tsv", ["gene", "http", "tissue_specificity", "brain_nTPM_if_enriched", "sc_specificity", "sc_brain_cells_listed_nCPM", "snRNA_brain_specificity", "snRNA_listed_nCPM"], rows)
    rows = []
    for cid, e in sorted(d["cases"].items()):
        for t in e["trials"]:
            rows.append([cid, e["name"], t["term"], t["tag"], t["http"], t["total"], t["returned"], ";".join(h["nct"] for h in t["hits"] if t["tag"] == "intr_x_neuro" or (t["total"] or 0) <= 8)])
    w(out / "trials_ctgov.tsv", ["cand_id", "name", "query_term", "query_kind", "http", "total_count", "returned", "nct_ids_listed"], rows)
    rows = []
    for cid, e in sorted(d["cases"].items()):
        for f in e["fda"]:
            labs = sorted(f["labels"], key=lambda l: l["effective_time"], reverse=True)
            if not labs:
                rows.append([cid, e["name"], f["generic"], f["http"], 0, "NO_MATCH" if f["http"] == 404 else "SERVICE_ERROR", "", "", "", ""])
            else:
                l = labs[0]
                rows.append([cid, e["name"], f["generic"], f["http"], len(labs), ";".join(l["openfda"].get("brand_name") or []), l["openfda"].get("product_type", [""])[0], l["effective_time"], "yes" if l["sections"].get("boxed_warning") else "no", "; ".join(sorted(l["sections"]))])
    w(out / "labels_openfda.tsv", ["cand_id", "name", "query", "http", "n_labels", "newest_brand", "product_type", "effective_time", "boxed_warning_text", "sections_present"], rows)
    rows = []
    for cid, e in sorted(d["cases"].items()):
        for m in e["molecules"]:
            ex = m.get("extra") or {}
            rows.append([cid, e["name"], m["id"], m.get("pref_name"), m.get("parent"), m.get("inchikey") or "NONE_IN_CHEMBL", m.get("max_phase"), m.get("type"), (ex.get("properties") or {}).get("full_mwt"), (ex.get("properties") or {}).get("psa"), (ex.get("properties") or {}).get("alogp"), m.get("black_box_warning")])
    w(out / "identity_chembl.tsv", ["cand_id", "name", "chembl_id", "pref_name", "parent", "inchikey", "max_phase", "molecule_type", "mwt", "psa", "alogp", "chembl_black_box_flag"], rows)
    rows = []
    for k, v in sorted(d["pubchem"].items()):
        pl = v["payload"]
        p = ((pl.get("PropertyTable") or {}).get("Properties") or [{}])[0] if isinstance(pl, dict) else {}
        rows.append([k, v["http"], p.get("CID", "NA"), p.get("Title", "NA"), p.get("InChIKey", "NA")])
    w(out / "identity_pubchem.tsv", ["key", "http", "cid", "title", "inchikey"], rows)
