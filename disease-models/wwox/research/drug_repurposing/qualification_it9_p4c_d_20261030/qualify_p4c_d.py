#!/usr/bin/env python3
"""IT9 P4c-D qualification fetches (second round, v3 generation path): apabetalone, JTE-151, infigratinib, dimethyl fumarate, gamcemetinib, ceralasertib.

  qualify_p4c_d.py --help              this text, no network
  qualify_p4c_d.py run [--out DIR]     live fetch (ChEMBL, PubChem, openFDA, ClinicalTrials.gov v2, OmniPath edge records with references); writes
                                       collected.json.gz, service_log.tsv, raw_hashes.tsv and derived tables
  qualify_p4c_d.py rebuild [--out DIR] offline rebuild of the tables from collected.json.gz
  qualify_p4c_d.py hpa HPA_DIR [--out DIR]  per-gene adult-brain cell-type rows (nCPM) from the two HPA download tables kept outside the repository; and the two local
                                       WWOX-deficient human datasets (organoid GSE156243, hNPC GSE126075), descriptive, `--geo DIR`

Reuses qualify_p4b_c.py (ChEMBL/PubChem/openFDA/ClinicalTrials collectors) and the IT8 P3 retry layer (backoff 0/2/6/15/30 s, every attempt logged). Standard library only.
No key, no e-mail, no operator identity is sent anywhere. States are never merged: SERVICE_ERROR / NO_RECORD / NO_ROWS_UNDER_FILTERS / ROWS_RETRIEVED / ROWS_RETRIEVED_TRUNCATED.
No value is pooled across standard types or units. Nothing here is medical advice."""
import argparse, collections, csv, gzip, importlib.util, json, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.parent / "qualification_it9_p4b_c_20261030" / "qualify_p4b_c.py"
spec = importlib.util.spec_from_file_location("qualify_p4b_c", B)
Q = importlib.util.module_from_spec(spec); sys.modules["qualify_p4b_c"] = Q; spec.loader.exec_module(Q)

COMPOUNDS = {   # id: (display name, ChEMBL id, aliases for trials/openFDA, genes for expression)
    "P4CD-01": ("apabetalone", "CHEMBL2393130", ["apabetalone", "RVX-208", "RVX208"], ["BRD4", "BRD2", "BRD3", "BRDT", "TNF", "IL6", "IL1B", "RELA"]),
    "P4CD-02": ("JTE-151", "CHEMBL3545357", ["JTE-151", "JTE151"], ["RORC", "RORA", "IL6", "TNF"]),
    "P4CD-03": ("infigratinib", "CHEMBL1852688", ["infigratinib", "BGJ398"], ["FGFR3", "FGFR1", "FGFR2", "FGFR4", "MAP3K7", "NFKBIB", "IL1B"]),
    "P4CD-04": ("dimethyl fumarate", "CHEMBL2107333", ["dimethyl fumarate", "BG-12", "Tecfidera"], ["KEAP1", "RBX1", "NFKBIB", "NFE2L2", "HCAR2", "TNF"]),
    "P4CD-04b": ("monomethyl fumarate", "CHEMBL589586", ["monomethyl fumarate"], ["HCAR2"]),
    "P4CD-05": ("gamcemetinib", "CHEMBL5314585", ["gamcemetinib", "CC-99677"], ["MAPKAPK2", "CDC25A", "FOXO1", "NPY"]),
    "P4CD-06": ("ceralasertib", "CHEMBL4285417", ["ceralasertib", "AZD6738"], ["ATR", "ETV1", "GRIN2C"]),
    "P4CD-01b": ("molibresib (BET class reference)", "CHEMBL1232461", ["molibresib", "I-BET762", "GSK525762"], ["BRD4"]),
}
FDA_NAMES = {"dimethyl fumarate": "dimethyl fumarate", "infigratinib": "infigratinib", "monomethyl fumarate": "monomethyl fumarate"}
EDGES = [  # (source, target, candidate): the decisive chain edges and alternatives from the same main target to the seeds
    ("BRD4", "TNF", "P4CD-01"), ("BRD4", "IL6", "P4CD-01"), ("BRD4", "IL1B", "P4CD-01"), ("BRD3", "TNF", "P4CD-01"),
    ("RORC", "IL6", "P4CD-02"), ("RORC", "TNF", "P4CD-02"), ("RORC", "IL1B", "P4CD-02"),
    ("FGFR3", "MAP3K7", "P4CD-03"), ("MAP3K7", "NFKBIB", "P4CD-03"), ("NFKBIB", "IL1B", "P4CD-03"), ("FGFR3", "IL1B", "P4CD-03"), ("FGFR3", "IL6", "P4CD-03"), ("FGFR3", "TNF", "P4CD-03"),
    ("KEAP1", "RBX1", "P4CD-04"), ("RBX1", "NFKBIB", "P4CD-04"), ("NFKBIB", "TNF", "P4CD-04"), ("KEAP1", "TNF", "P4CD-04"), ("KEAP1", "IL1B", "P4CD-04"), ("KEAP1", "IL6", "P4CD-04"),
    ("KEAP1", "NFE2L2", "P4CD-04"), ("NFE2L2", "IL1B", "P4CD-04"), ("NFE2L2", "IL6", "P4CD-04"), ("NFE2L2", "TNF", "P4CD-04"),
    ("MAPKAPK2", "CDC25A", "P4CD-05"), ("CDC25A", "FOXO1", "P4CD-05"), ("FOXO1", "NPY", "P4CD-05"), ("MAPKAPK2", "NPY", "P4CD-05"), ("MAPKAPK2", "FOXO1", "P4CD-05"), ("MAPKAPK2", "TNF", "P4CD-05"),
    ("ATR", "ETV1", "P4CD-06"), ("ETV1", "GRIN2C", "P4CD-06"), ("ATR", "GRIN2C", "P4CD-06"),
    ("HMGB1", "IL1B", "HMGB1-axis"), ("HMGB1", "TNF", "HMGB1-axis"), ("HMGB1", "IL6", "HMGB1-axis"),
]
COND = {
    "epilepsy_seizure": "epilepsy OR seizure OR epileptic encephalopathy OR infantile spasms",
    "hypomyelination_leuko": "hypomyelination OR leukodystrophy",
    "neurodevelopment": "neurodevelopmental disorder OR intellectual disability OR autism OR microcephaly OR developmental delay OR achondroplasia",
    "neuroinflammation_ms": "multiple sclerosis OR neuroinflammation OR Alzheimer disease OR Parkinson disease OR amyotrophic lateral sclerosis OR Friedreich ataxia",
    "wwox": "WWOX OR WOREE OR SCAR12",
}
Q.COND = COND


def collect_edges(net):
    net.case = "omnipath"
    res = {}
    for a, b, cand in EDGES:
        s, p = net.get("https://omnipathdb.org/interactions", params={"sources": a, "targets": b, "genesymbols": "yes", "fields": "sources,references,curation_effort,type",
                                                                          "format": "json", "datasets": "omnipath,pathwayextra,kinaseextra,collectri,tf_target,dorothea"}, timeout=120)
        key = f"{a}->{b}"
        if s == 200 and isinstance(p, list):
            rows = [r for r in p if r.get("source_genesymbol") == a and r.get("target_genesymbol") == b]
            res[key] = {"cand": cand, "state": "ROWS_RETRIEVED" if rows else "NO_MATCHING_RECORD", "n_returned": len(p), "rows": rows}
        else:
            res[key] = {"cand": cand, "state": "SERVICE_ERROR", "http": s, "detail": str(p)[:200], "rows": []}
    return res


def collect(net):
    orig = net.get
    def traced(url, *a, **k):
        t0 = time.time(); r = orig(url, *a, **k)
        print(f"{time.strftime('%H:%M:%S')} {r[0]} {round(time.time()-t0,1)}s [{net.case}] {url[:110]}", file=sys.stderr, flush=True)
        return r
    net.get = traced
    res = {"compounds": {}, "trials": {}, "labels": {}, "hpa": {}}
    for wid, (name, mid, aliases, gs) in COMPOUNDS.items():
        res["compounds"][wid] = Q.collect_compound(net, wid, name, mid, aliases, gs)
        if wid not in ("P4CD-01b",):
            res["trials"][name] = Q.collect_trials(net, name, aliases)
        if name in FDA_NAMES:
            res["labels"][name] = Q.collect_label(net, FDA_NAMES[name])
    res["edges"] = collect_edges(net)
    return res


def build_edges(res, out):
    rows = []
    for key, e in res["edges"].items():
        if not e["rows"]:
            rows.append([key, e["cand"], e["state"], "", "", "", "", "", "", ""]); continue
        for r in e["rows"]:
            refs = [x for x in (r.get("references") or "").split(";") if x]
            pm = sorted({x.split(":", 1)[1] for x in refs if ":" in x})
            rows.append([key, e["cand"], e["state"], r.get("type"), r.get("is_stimulation"), r.get("is_inhibition"), ";".join(r.get("sources") or []), r.get("curation_effort"), len(pm), ";".join(pm)])
    Q.wr(out / "edge_records_omnipath.tsv", ["edge", "candidate", "state", "omnipath_type", "is_stimulation", "is_inhibition", "sources", "curation_effort", "n_distinct_references", "reference_ids"], rows)
    return len(rows)


def build(res, out, stamp):
    res.setdefault("edges", {})
    saved = res["edges"]; res["edges"] = {}
    n = Q.build(res, out, stamp)
    res["edges"] = saved
    n["edge_rows"] = build_edges(res, out)
    return n


def cmd_run(out):
    m = Q.pq(); net = m.Net(); res = Q.slim(collect(net)); res.pop("hpa", None); res["hpa"] = {}
    stamp = time.strftime("%Y-%m-%d", time.gmtime())
    out.mkdir(exist_ok=True)
    Q.wr(out / "raw_hashes.tsv", ["item", "sha256", "bytes"], [[k[:170], m.sha(net.raw[k]), len(json.dumps(net.raw[k]))] for k in sorted(net.raw)])
    Q.wr(out / "service_log.tsv", ["case", "attempt", "status", "seconds", "url", "error"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]] for l in net.log])
    col = gzip.compress(json.dumps({"retrieved_on": stamp, "collected": res}, sort_keys=True).encode(), mtime=0)
    (out / "collected.json.gz").write_bytes(col)
    raw_gz = gzip.compress(json.dumps({"retrieved_on": stamp, "responses": net.raw}, sort_keys=True).encode(), mtime=0)
    (out / "raw_store.json.gz").unlink(missing_ok=True)
    if len(raw_gz) < Q.RAW_LIMIT: (out / "raw_store.json.gz").write_bytes(raw_gz)
    n = build(res, out, stamp)
    summ = {"retrieved_on": stamp, "attempts": len(net.log), "non200_attempts": sum(1 for l in net.log if l["status"] not in (200, 404)), "raw_gz_bytes": len(raw_gz), "raw_kept": len(raw_gz) < Q.RAW_LIMIT, **n}
    (out / "run_summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n"); print(json.dumps(summ))


def cmd_rebuild(out):
    d = json.loads(gzip.decompress((out / "collected.json.gz").read_bytes()))
    print(json.dumps(build(Q.slim(d["collected"]), out, d["retrieved_on"])))


BRAIN_NUC = ["astrocyte", "central nervous system macrophage", "oligodendrocyte", "oligodendrocyte precursor cell", "committed oligodendrocyte precursor", "endothelial cell", "pericyte", "leukocyte",
             "upper-layer intratelencephalic", "deep-layer intratelencephalic", "MGE interneuron", "CGE interneuron", "hippocampal dentate gyrus", "hippocampal CA1-3", "Bergmann glia", "cerebellar inhibitory", "ependymal cell"]
SC = ["microglia", "macrophages", "monocytes", "t-cells", "b-cells", "nk-cells", "neutrophils", "astrocytes", "oligodendrocytes", "oligodendrocyte progenitor cells", "brain excitatory neurons", "brain inhibitory neurons", "hofbauer cells", "kupffer cells", "platelets", "megakaryocytes", "hepatocytes", "vascular endothelial cells"]
GENES_ALL = sorted({g for v in COMPOUNDS.values() for g in v[3]} | {"WWOX", "HMGB1", "BRD3", "RELA", "NFKB1"})


def cmd_hpa(hpa_dir, out, geo):
    rows = []
    for fn, col, keep in (("rna_single_nuclei_cluster_type.tsv", "Cluster type", BRAIN_NUC), ("rna_single_cell_type.tsv", "Cell type", SC)):
        with open(Path(hpa_dir) / fn) as f:
            r = csv.DictReader(f, delimiter="\t")
            for x in r:
                if x["Gene name"] in GENES_ALL and x[col] in keep:
                    rows.append([x["Gene name"], x["Gene"], fn.replace(".tsv", ""), x[col], x["nCPM"]])
    seen = {(r[0], r[2]) for r in rows}
    miss = [[g, "", fn, "GENE_NOT_IN_TABLE", ""] for fn in ("rna_single_nuclei_cluster_type", "rna_single_cell_type") for g in GENES_ALL if (g, fn) not in seen]
    Q.wr(out / "expression_hpa_cells.tsv", ["gene", "ensembl", "hpa_table", "cell_type", "nCPM"], sorted(rows) + miss)
    if geo:
        sys.path.insert(0, str(HERE))
        subprocess.run([sys.executable, str(HERE.parent / "gse156243" / "gene_rows_cpm.py"), str(Path(geo) / "GSE156243" / "GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"), str(out / "organoid_gene_rows.tsv")] + GENES_ALL, check=True)
        rows2 = {}
        with gzip.open(Path(geo) / "GSE126075" / "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz", "rt") as f:
            r = csv.reader(f, delimiter="\t"); h = next(r)
            for x in r:
                if x[0] in GENES_ALL: rows2[x[0]] = x[1:]
        Q.wr(out / "hnpc_gene_rows.tsv", ["gene"] + h[1:], [[g] + ([f"{float(a):.2f}" for a in rows2[g]] if g in rows2 else ["ABSENT"] * (len(h) - 1)) for g in GENES_ALL])
    print(len(rows), "HPA rows;", len(miss), "gene-table misses")


def cmd_supp(out):
    """Complex-level SIGNOR records behind the split chain KEAP1 -> (CUL3,RBX1,SKP1) and (CUL1,RBX1,SKP1) -> NFKBIB: the engine splits complexes into members and joins them on RBX1."""
    m = Q.pq(); net = m.Net(); net.case = "omnipath_complex"; rows = []
    for tag, params, flt in (("to_NFKBIB_from_RBX1_complex", {"targets": "NFKBIB"}, lambda r: "RBX1" in (r.get("source_genesymbol") or "")),
                             ("from_KEAP1_to_RBX1_complex", {"sources": "KEAP1"}, lambda r: "RBX1" in (r.get("target_genesymbol") or "") or "CUL3" in (r.get("target_genesymbol") or ""))):
        p0 = {"genesymbols": "yes", "fields": "sources,references,curation_effort,type", "format": "json", "datasets": "omnipath,pathwayextra,kinaseextra"}; p0.update(params)
        s, p = net.get("https://omnipathdb.org/interactions", params=p0, timeout=120)
        if s == 200 and isinstance(p, list):
            for r in p:
                if flt(r): rows.append([tag, r.get("source"), r.get("source_genesymbol"), r.get("target"), r.get("target_genesymbol"), r.get("type"), r.get("is_stimulation"), r.get("is_inhibition"), ";".join(r.get("sources") or []), r.get("references")])
            rows.append([tag, "", "", "", "", "QUERY_OK", "", "", "", f"{len(p)} rows returned"])
        else:
            rows.append([tag, "", "", "", "", "SERVICE_ERROR", "", "", "", str(p)[:100]])
    Q.wr(out / "edge_records_complex.tsv", ["query", "source_id", "source_genes", "target_id", "target_genes", "omnipath_type", "is_stimulation", "is_inhibition", "sources", "references"], rows)
    Q.wr(out / "service_log_supp.tsv", ["case", "attempt", "status", "seconds", "url", "error"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]] for l in net.log])
    print(len(rows), "rows")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rebuild", "hpa", "supp"], nargs="?"); ap.add_argument("hpa_dir", nargs="?")
    ap.add_argument("--out", default=str(HERE)); ap.add_argument("--geo", default=None)
    a = ap.parse_args()
    if not a.cmd: ap.print_help(); return
    out = Path(a.out)
    if a.cmd == "run": cmd_run(out)
    elif a.cmd == "rebuild": cmd_rebuild(out)
    elif a.cmd == "supp": cmd_supp(out)
    else: cmd_hpa(a.hpa_dir, out, a.geo)


if __name__ == "__main__":
    main()
