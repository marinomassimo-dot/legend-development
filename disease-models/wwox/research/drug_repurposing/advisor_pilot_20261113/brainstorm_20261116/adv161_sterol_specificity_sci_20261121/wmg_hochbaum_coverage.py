"""ADV-161 coverage check: detection of the pre-registered gene sets in the Hochbaum 2024 T3-vs-control M2 dataset
(CELLxGENE WMG v2, dataset 12990215-ad1a-4106-8536-7388327a616f; stdlib only). Usage: python3 -I wmg_hochbaum_coverage.py OUT.tsv
pc = fraction of cells with expression above 0 (n_expressing / total cells), per cell type, T3 and vehicle cells POOLED (WMG does not
split by condition): this is a COVERAGE (power) check only, never a contrast. me = WMG mean of log-normalised expression among expressing
cells; it is a different quantity from pc and is reported in its own column."""
import json
import sys
import time
import urllib.request

B = "https://api.cellxgene.cziscience.com/wmg/v2"
DATASET = "12990215-ad1a-4106-8536-7388327a616f"
TISSUE = "UBERON:0000955"
A = "Hmgcs1 Hmgcr Mvk Pmvk Mvd Idi1 Fdps Fdft1 Sqle Lss Cyp51 Tm7sf2 Msmo1 Nsdhl Hsd17b7 Dhcr24 Ebp Sc5d Dhcr7".split()
Bs = "Srebf2 Scap Insig1 Ldlr Pcsk9 Stard4 Acat2".split()
C = "Mbp Plp1 Mog Mag Mobp Cnp Opalin Cldn11 Ugt8a Gpr37 Enpp6 Tcf7l2 Bcas1 Fyn".split()
T = "Hr Klf9 Dio3 Ier5".split()
SETS = [("A", A), ("B", Bs), ("C", C), ("T", T)]


def call(path, body=None):
    req = urllib.request.Request(B + path, data=None if body is None else json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "legend-sci/1.0"})
    last = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                return json.load(r)
        except Exception as e:
            last = e
            time.sleep(2)
    raise last


def main(out):
    genes = {}
    for d in call("/primary_filter_dimensions")["gene_terms"]["NCBITaxon:10090"]:
        for k, v in d.items():
            genes[v] = k
    ids = []
    for _, g in SETS:
        ids += [genes[x] for x in g if x in genes]
    missing = [x for _, g in SETS for x in g if x not in genes]
    d = {"expression_summary": {}}
    labs = {}
    for i in range(0, len(ids), 6):  # small chunks: the portal returns HTTP 500 on larger requests
        body = {"filter": {"gene_ontology_term_ids": ids[i:i + 6], "organism_ontology_term_id": "NCBITaxon:10090",
                           "dataset_ids": [DATASET], "disease_ontology_term_ids": [],
                           "self_reported_ethnicity_ontology_term_ids": [], "sex_ontology_term_ids": [],
                           "development_stage_ontology_term_ids": []}, "is_rollup": True}
        r = call("/query", body)
        d["expression_summary"].update(r.get("expression_summary") or {})
        labs.update(((r.get("term_id_labels") or {}).get("cell_types") or {}).get(TISSUE, {}))
    names = {}
    for cid, v in labs.items():
        names[cid] = (v.get("aggregated") or {}).get("cell_type") or v.get("cell_type") or cid
    rows = []
    for sname, g in SETS:
        for x in g:
            gid = genes.get(x)
            es = ((d.get("expression_summary") or {}).get(gid) or {}).get(TISSUE, {})
            for cid, v in es.items():
                a = v.get("aggregated") or {}
                tot = ((labs.get(cid) or {}).get("aggregated") or {}).get("total_count", "")
                rows.append((sname, x, cid, names.get(cid, ""), tot, a.get("n", ""), round(a.get("pc", 0), 4), round(a.get("me", 0), 4)))
    with open(out, "w") as f:
        f.write("set\tgene\tcell_type_id\tcell_type\ttotal_cells\tn_expressing\tpc_detection_fraction\tme_mean_expression_of_expressing\n")
        for r in rows:
            f.write("\t".join(str(c) for c in r) + "\n")
    print("rows", len(rows), "genes not in WMG gene list:", missing)
    print("cell types:", sorted({(r[2], r[3], r[4]) for r in rows}, key=lambda z: str(z[1]))[:40])


if __name__ == "__main__":
    main(sys.argv[1])
