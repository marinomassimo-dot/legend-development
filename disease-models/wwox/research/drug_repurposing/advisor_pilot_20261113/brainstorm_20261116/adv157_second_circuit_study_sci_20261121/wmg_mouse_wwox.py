"""Mouse Wwox detection by cell type from the CZ CELLxGENE Discover WMG v2 API (stdlib only).
Usage: python3 -I wmg_mouse_wwox.py OUT.tsv
Measure: pc = fraction of cells with expression above 0 = n_expressing / total_cells (in the API, aggregated.n
is the number of EXPRESSING cells; the cell count is term_id_labels...aggregated.total_count), per cell type,
pooled over all mouse brain datasets and per dataset. With rollup on, child types (for example the primary motor
cortex forms) are folded into their parents. No animal-level replication, no depth adjustment."""
import json
import sys
import time
import urllib.request

B = "https://api.cellxgene.cziscience.com/wmg/v2"
GENE = "ENSMUSG00000004637"  # mouse Wwox
TISSUE = "UBERON:0000955"  # brain
CT = {
    "CL:4023018": "Pvalb", "CL:4023017": "Sst", "CL:4023011": "Lamp5", "CL:4023016": "Vip",
    "CL:4030059": "L2/3 IT", "CL:4030064": "L5 IT", "CL:4030062": "L4/5 IT", "CL:4023041": "L5 ET",
    "CL:4030067": "L5/6 NP", "CL:4023042": "L6 CT", "CL:4030065": "L6 IT", "CL:4023038": "L6b",
    "CL:0000128": "Oligodendrocyte", "CL:0002453": "OPC", "CL:0000127": "Astrocyte",
}


def call(path, body):
    req = urllib.request.Request(B + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "legend-sci/1.0"})
    last = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                return json.load(r)
        except Exception as e:  # retried; the portal returns HTTP 500 intermittently
            last = {"error": str(e)[:100]}
            time.sleep(2)
    return last


def query(dataset_ids):
    body = {"filter": {"gene_ontology_term_ids": [GENE], "organism_ontology_term_id": "NCBITaxon:10090",
                       "dataset_ids": dataset_ids, "disease_ontology_term_ids": [],
                       "self_reported_ethnicity_ontology_term_ids": [], "sex_ontology_term_ids": [],
                       "development_stage_ontology_term_ids": []}, "is_rollup": True}
    d = call("/query", body)
    es = (d.get("expression_summary") or {}).get(GENE)
    if es is None:
        return None, {}
    lab = ((d.get("term_id_labels") or {}).get("cell_types") or {}).get(TISSUE, {})
    return es.get(TISSUE, {}), lab


def main(out):
    ds = call("/filters", {"filter": {"organism_ontology_term_id": "NCBITaxon:10090",
                                      "tissue_ontology_term_ids": [TISSUE]}})["filter_dims"]["datasets"]
    rows = []
    scopes = [("POOLED", "all mouse brain datasets", [])] + [(x["id"], x["collection_label"][:60] + " | " + x["label"][:60], [x["id"]]) for x in ds]
    for sid, label, ids in scopes:
        es, lab = query(ids)
        if es is None:
            rows.append((sid, label, "NO_GENE_ROWS", "", "", ""))
            continue
        for cid, name in CT.items():
            a = (es.get(cid) or {}).get("aggregated")
            if a:
                tot = ((lab.get(cid) or {}).get("aggregated") or {}).get("total_count", "")
                rows.append((sid, label, name, tot, a["n"], round(a["pc"], 4)))
    with open(out, "w") as f:
        f.write("scope\tlabel\tcell_type\ttotal_cells\tn_expressing\tpc_fraction_above_0\n")
        for r in rows:
            f.write("\t".join(str(c) for c in r) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
