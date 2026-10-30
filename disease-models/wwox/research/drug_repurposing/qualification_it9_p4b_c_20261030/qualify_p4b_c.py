#!/usr/bin/env python3
"""IT9 P4b-c: qualification fetches for harmine, pomalidomide, defosbarasertib, pinometostat, sirolimus, lenalidomide, AT9283.

  qualify_p4b_c.py --help            this text, no network
  qualify_p4b_c.py run [--out DIR]   live fetch (ChEMBL, PubChem, openFDA, ClinicalTrials.gov v2, OmniPath, Human Protein Atlas, Europe PMC);
                                     writes raw_store.json.gz, service_log.tsv, raw_hashes.tsv and the derived tables
  qualify_p4b_c.py rebuild [--out DIR]  offline rebuild of the tables from raw_store.json.gz

Reuses the IT8 P3 retry layer (pharm_qualify.Net: backoff 0/2/6/15/30 s, every attempt logged). Standard library only. No key, no e-mail, no operator
identity is sent anywhere. States are never merged: SERVICE_ERROR / NO_RECORD / NO_ROWS_UNDER_FILTERS / ROWS_RETRIEVED / ROWS_RETRIEVED_TRUNCATED.
No value is pooled across standard types or units. Nothing here is medical advice."""
import argparse, collections, csv, gzip, hashlib, importlib.util, json, re, statistics, sys, time, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
P3 = HERE.parent / "pharmacological_qualification_it8_p3_20261029"
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
RAW_LIMIT = 1_000_000
ACT_CAP = 3000

COMPOUNDS = {   # work-order id: (display name, ChEMBL id from the catalogue, aliases for trials and openFDA, key targets for expression)
    "P3-10": ("harmine", "CHEMBL269538", ["harmine"], ["DYRK1A", "MAOA"]),
    "P3-11": ("pomalidomide", "CHEMBL43452", ["pomalidomide"], ["CRBN", "IKZF1", "IKZF3", "CUL4A"]),
    "P3-12": ("defosbarasertib", "CHEMBL215152", ["defosbarasertib", "barasertib", "AZD1152", "AZD2811"], ["AURKB"]),
    "P3-13": ("pinometostat", "CHEMBL3414626", ["pinometostat", "EPZ-5676"], ["DOT1L"]),
    "P3-16": ("sirolimus", "CHEMBL413", ["sirolimus", "rapamycin"], ["MTOR", "FKBP1A"]),
    "P3-19": ("lenalidomide", "CHEMBL848", ["lenalidomide"], ["CRBN", "IKZF1", "IKZF3"]),
    "P3-20": ("AT9283", "CHEMBL495727", ["AT9283"], ["AURKB", "AURKA", "JAK2"]),
}
FDA_NAMES = {"pomalidomide": "pomalidomide", "lenalidomide": "lenalidomide", "sirolimus": "sirolimus"}
EDGES = [("DYRK1A", "MYC"), ("CUL4A", "MYC"), ("AURKB", "MYC"), ("DOT1L", "MYC"), ("MTOR", "MYC"), ("CRBN", "MYC"), ("IKZF1", "MYC"), ("IKZF3", "MYC"), ("FKBP1A", "MYC")]
COND = {
    "epilepsy_seizure": "epilepsy OR seizure OR epileptic encephalopathy OR infantile spasms",
    "hypomyelination_leuko": "hypomyelination OR leukodystrophy",
    "neurodevelopment": "neurodevelopmental disorder OR intellectual disability OR autism OR microcephaly OR developmental delay OR Down syndrome",
    "wwox": "WWOX OR WOREE OR SCAR12",
    "cns_tumour": "glioma OR glioblastoma OR central nervous system lymphoma OR brain metastases OR medulloblastoma",
}
UA = None


def pq():
    spec = importlib.util.spec_from_file_location("pharm_qualify", P3 / "pharm_qualify.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def pages(net, url, key, cap=ACT_CAP):
    rows, off, total = [], 0, None
    sep = "&" if "?" in url else "?"
    while True:
        s, p = net.get(f"{url}{sep}limit=200&offset={off}")
        if s != 200 or not isinstance(p, dict):
            return {"state": "SERVICE_ERROR", "http": s, "total": total, "rows": rows}
        total = (p.get("page_meta") or {}).get("total_count", total)
        page = p.get(key) or []
        rows += page
        off += len(page)
        if not page or (total is not None and off >= total):
            break
        if off >= cap:
            return {"state": "ROWS_RETRIEVED_TRUNCATED", "total": total, "rows": rows}
    return {"state": "ROWS_RETRIEVED" if rows else "NO_ROWS_UNDER_FILTERS", "total": total, "rows": rows}


def collect_compound(net, wid, name, mid, aliases, genes):
    out = {"work_id": wid, "name": name, "chembl_id": mid}
    net.case = f"{wid}:{name}:chembl"
    out["molecule"] = pq().chembl_molecule(net, mid)
    s, m = net.get(f"{CHEMBL}/molecule/{mid}.json")
    out["molecule_raw"] = {k: m.get(k) for k in ("pref_name", "max_phase", "first_approval", "molecule_synonyms", "atc_classifications", "black_box_warning", "oral", "parenteral", "natural_product", "withdrawn_flag", "molecule_properties")} if s == 200 and isinstance(m, dict) else {}
    out["mechanism"] = pages(net, f"{CHEMBL}/mechanism.json?molecule_chembl_id={mid}", "mechanisms")
    out["activities"] = pages(net, f"{CHEMBL}/activity.json?molecule_chembl_id={mid}&standard_type__in=IC50,Ki,Kd,EC50,DC50,Dmax,Potency,Inhibition", "activities")
    tids = sorted({a.get("target_chembl_id") for a in out["activities"]["rows"] if a.get("target_chembl_id")})
    tinfo = {}
    for i in range(0, len(tids), 50):
        s, p = net.get(f"{CHEMBL}/target.json?target_chembl_id__in={','.join(tids[i:i+50])}&limit=100")
        if s == 200 and isinstance(p, dict):
            for t in p.get("targets", []):
                tinfo[t["target_chembl_id"]] = {"name": t.get("pref_name"), "organism": t.get("organism"), "type": t.get("target_type"), "genes": sorted({y.get("component_synonym") for c in (t.get("target_components") or []) for y in (c.get("target_component_synonyms") or []) if y.get("syn_type") == "GENE_SYMBOL"})}
    out["targets"] = tinfo
    # PubChem by name (every alias) and by InChIKey
    net.case = f"{wid}:{name}:pubchem"
    ik = (out["molecule"] or {}).get("inchikey")
    pc = {}
    for al in aliases[:2]:
        s, p = net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{urllib.parse.quote(al)}/property/InChIKey,IUPACName,MolecularFormula,CanonicalSMILES/JSON")
        pc[f"name:{al}"] = [s, ((p or {}).get("PropertyTable") or {}).get("Properties") if isinstance(p, dict) else str(p)[:200]]
    if ik:
        s, p = net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/property/InChIKey,IUPACName,MolecularFormula/JSON")
        pc["inchikey"] = [s, ((p or {}).get("PropertyTable") or {}).get("Properties") if isinstance(p, dict) else str(p)[:200]]
        s, p = net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/synonyms/JSON")
        pc["synonyms"] = [s, (((p or {}).get("InformationList") or {}).get("Information") or [{}])[0].get("Synonym", [])[:40] if isinstance(p, dict) else str(p)[:200]]
    out["pubchem"] = pc
    return out


def collect_trials(net, name, aliases):
    net.case = f"{name}:ctgov"
    res = {}
    intr = " OR ".join(aliases)
    def q(label, **kw):
        params = {"query.intr": intr, "countTotal": "true", "pageSize": "30", "format": "json"}
        params.update(kw)
        s, p = net.get("https://clinicaltrials.gov/api/v2/studies", params=params)
        if s != 200 or not isinstance(p, dict):
            res[label] = {"state": "SERVICE_ERROR", "http": s}
            return
        studs = []
        for st in p.get("studies", []):
            ps = st.get("protocolSection", {})
            ident, stat, des = ps.get("identificationModule", {}), ps.get("statusModule", {}), ps.get("designModule", {})
            elig = ps.get("eligibilityModule", {})
            studs.append({"nct": ident.get("nctId"), "title": ident.get("briefTitle"), "status": stat.get("overallStatus"), "phases": des.get("phases"),
                          "conditions": (ps.get("conditionsModule") or {}).get("conditions"), "min_age": elig.get("minimumAge"), "max_age": elig.get("maximumAge"),
                          "has_results": st.get("hasResults")})
        res[label] = {"state": "ROWS_RETRIEVED" if studs else "NO_ROWS_UNDER_FILTERS", "total": p.get("totalCount"), "listed": len(studs), "studies": studs}
    q("all_conditions")
    for k, v in COND.items():
        q(k, **{"query.cond": v})
    q("paediatric_terms", **{"query.term": "child OR children OR pediatric OR paediatric OR infant"})
    return res


def collect_label(net, name):
    net.case = f"{name}:openfda"
    s, p = net.get("https://api.fda.gov/drug/label.json", params={"search": f'openfda.generic_name:"{name}"', "limit": "10"})
    if s != 200 or not isinstance(p, dict):
        return {"state": "SERVICE_ERROR", "http": s}
    labels = []
    for r in p.get("results", []):
        labels.append({"set_id": r.get("set_id"), "effective_time": r.get("effective_time"), "brand": (r.get("openfda") or {}).get("brand_name"),
                       "manufacturer": (r.get("openfda") or {}).get("manufacturer_name"), "route": (r.get("openfda") or {}).get("route"),
                       "sections": {k: r.get(k) for k in ("boxed_warning", "pediatric_use", "pregnancy", "nursing_mothers", "pharmacokinetics", "clinical_pharmacology",
                                                           "mechanism_of_action", "warnings_and_cautions", "warnings", "adverse_reactions", "contraindications", "indications_and_usage",
                                                           "dosage_and_administration", "use_in_specific_populations", "drug_interactions", "precautions", "geriatric_use", "overdosage") if r.get(k)}})
    return {"state": "ROWS_RETRIEVED" if labels else "NO_ROWS_UNDER_FILTERS", "total": ((p.get("meta") or {}).get("results") or {}).get("total"), "labels": labels}


def collect_edges(net):
    net.case = "omnipath"
    res = {}
    s, p = net.get("https://omnipathdb.org/interactions", params={"targets": "MYC", "genesymbols": "yes", "fields": "sources,references,curation_effort,extra_attrs,type", "format": "json", "datasets": "omnipath,pathwayextra,kinaseextra"}, timeout=120)
    if s == 200 and isinstance(p, list):
        res["interactions_to_MYC"] = {"state": "ROWS_RETRIEVED", "total": len(p), "rows": [r for r in p if r.get("source_genesymbol") in {e[0] for e in EDGES} or any(x in (r.get("source_genesymbol") or "") for x in ("CUL4A", "CRBN"))]}
    else:
        res["interactions_to_MYC"] = {"state": "SERVICE_ERROR", "http": s, "detail": str(p)[:200]}
    for enz in ("DYRK1A", "AURKB", "DOT1L", "CUL4A", "MTOR"):
        s, p = net.get("https://omnipathdb.org/enzsub", params={"enzymes": enz, "substrates": "MYC", "genesymbols": "yes", "fields": "sources,references,curation_effort", "format": "json"}, timeout=60)
        res[f"enzsub_{enz}_MYC"] = {"state": "ROWS_RETRIEVED" if s == 200 and p else ("NO_ROWS_UNDER_FILTERS" if s == 200 else "SERVICE_ERROR"), "http": s, "rows": p if s == 200 else str(p)[:200]}
    return res


def collect_hpa(net, genes):
    net.case = "hpa"
    res = {}
    for g in genes:
        s, e = net.get("https://www.proteinatlas.org/api/search_download.php", params={"search": g, "format": "json", "columns": "g,eg", "compress": "no"})
        ens = next((x["Ensembl"] for x in e if x.get("Gene") == g), None) if s == 200 and isinstance(e, list) else None
        if not ens:
            res[g] = {"state": "SERVICE_ERROR" if s != 200 else "NO_RECORD", "http": s}
            continue
        s, h = net.get(f"https://www.proteinatlas.org/{ens}.json", timeout=60)
        if s != 200 or not isinstance(h, dict):
            res[g] = {"state": "SERVICE_ERROR", "http": s, "ensembl": ens}
            continue
        keep = {k: v for k, v in h.items() if re.search(r"brain|single cell|Cell type|RNA tissue|region|development|Subcellular main", k, re.I)}
        res[g] = {"state": "ROWS_RETRIEVED", "ensembl": ens, "fields": keep, "all_keys": sorted(h.keys())}
    return res


def collect(net):
    orig = net.get
    def traced(url, *a, **k):
        t0 = time.time()
        r = orig(url, *a, **k)
        print(f"{time.strftime('%H:%M:%S')} {r[0]} {round(time.time()-t0,1)}s [{net.case}] {url[:110]}", file=sys.stderr, flush=True)
        return r
    net.get = traced
    res = {"compounds": {}, "trials": {}, "labels": {}}
    genes = set()
    for wid, (name, mid, aliases, gs) in COMPOUNDS.items():
        res["compounds"][wid] = collect_compound(net, wid, name, mid, aliases, gs)
        genes |= set(gs)
        res["trials"][name] = collect_trials(net, name, aliases)
        if name in FDA_NAMES:
            res["labels"][name] = collect_label(net, FDA_NAMES[name])
    res["edges"] = collect_edges(net)
    genes |= {"MYC", "WWOX", "SALL4", "ZNF692", "GSPT1", "CSNK1A1", "FKBP1A", "MTOR", "MAOA", "MAOB", "DYRK1B", "CLK1"}
    res["hpa"] = collect_hpa(net, sorted(genes))
    return res


def num(r):
    try:
        return float(r["standard_value"])
    except (TypeError, ValueError, KeyError):
        return None


def rel(r):
    return {"=": "=", ">": ">", ">=": ">", "<": "<", "<=": "<"}.get(r.get("standard_relation") or "=", r.get("standard_relation") or "=")


def wr(path, head, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow(["" if v is None else str(v).replace("\t", " ").replace("\n", " ") for v in r])


def build(res, out, stamp):
    ident, mech, det, summ = [], [], [], []
    for wid, c in res["compounds"].items():
        m, raw = c["molecule"], c["molecule_raw"]
        pcs = c["pubchem"]
        names = {k: [x.get("InChIKey") for x in (v[1] or [])] if isinstance(v[1], list) else v[1] for k, v in pcs.items() if k.startswith("name") or k == "inchikey"}
        ident.append([wid, c["name"], c["chembl_id"], m.get("pref_name"), m.get("parent"), m.get("is_parent"), json.dumps(m.get("family")), m.get("inchikey"), m.get("smiles"),
                      m.get("chirality"), raw.get("max_phase"), raw.get("first_approval"), json.dumps(names), "; ".join((pcs.get("synonyms") or [0, []])[1][:12]) if isinstance(pcs.get("synonyms", [0, []])[1], list) else ""])
        for x in c["mechanism"]["rows"]:
            mech.append([wid, c["name"], x.get("action_type"), x.get("mechanism_of_action"), x.get("target_chembl_id"), (res["compounds"][wid]["targets"].get(x.get("target_chembl_id")) or {}).get("name"), x.get("direct_interaction"), x.get("disease_efficacy")])
        tinfo = c["targets"]
        for a in c["activities"]["rows"]:
            t = tinfo.get(a.get("target_chembl_id")) or {}
            det.append([wid, c["name"], a.get("target_chembl_id"), t.get("name"), "|".join(t.get("genes") or []), a.get("target_organism"), t.get("type"), a.get("standard_type"), rel(a), a.get("standard_value"),
                        a.get("standard_units"), a.get("assay_type"), a.get("assay_chembl_id"), a.get("document_chembl_id"), (a.get("assay_description") or "")[:200], a.get("assay_organism"), a.get("activity_comment")])
        grp = collections.defaultdict(list)
        for a in c["activities"]["rows"]:
            t = tinfo.get(a.get("target_chembl_id")) or {}
            if t.get("type") not in ("SINGLE PROTEIN", "PROTEIN COMPLEX", "PROTEIN FAMILY", "PROTEIN-PROTEIN INTERACTION"):
                continue
            grp[(a.get("target_chembl_id"), t.get("name"), "|".join(t.get("genes") or []), a.get("target_organism"), a.get("standard_type"), a.get("standard_units"), a.get("assay_type"))].append(a)
        for k, rows in grp.items():
            eq = [num(r) for r in rows if rel(r) == "=" and num(r) is not None]
            summ.append([wid, c["name"], *k, len(rows), len(eq), min(eq) if eq else "", max(eq) if eq else "",
                         sum(1 for r in rows if rel(r) == ">"), sum(1 for r in rows if rel(r) == "<"), len({r.get("document_chembl_id") for r in rows})])
    wr(out / "identity.tsv", ["work_id", "name", "chembl_id", "chembl_pref_name", "parent", "is_parent", "family_json", "chembl_inchikey", "chembl_smiles", "chirality", "max_phase", "first_approval", "pubchem_inchikeys_by_query", "pubchem_synonyms_first12"], ident)
    wr(out / "chembl_mechanism.tsv", ["work_id", "name", "action_type", "mechanism", "target_chembl_id", "target_name", "direct_interaction", "disease_efficacy"], mech)
    wr(out / "measures_detail.tsv", ["work_id", "name", "target_chembl_id", "target_name", "target_genes", "target_organism", "target_type", "standard_type", "relation", "value", "units", "assay_type", "assay_id", "document", "assay_description", "assay_organism", "activity_comment"], det)
    wr(out / "measures_by_target_type.tsv", ["work_id", "name", "target_chembl_id", "target_name", "target_genes", "target_organism", "standard_type", "units", "assay_type", "n_rows", "n_relation_eq", "min_eq", "max_eq", "n_gt", "n_lt", "n_documents"], summ)
    # trials
    tr = []
    for name, d in res["trials"].items():
        for label, e in d.items():
            tr.append([name, label, e.get("state"), e.get("total"), e.get("listed"), "|".join(f"{s['nct']}:{s['status']}" for s in e.get("studies", [])[:12])])
    wr(out / "trials_summary.tsv", ["compound", "query_slice", "state", "total_hits", "listed", "first_12_nct_status"], tr)
    trd = []
    for name, d in res["trials"].items():
        for label, e in d.items():
            if label in ("all_conditions", "paediatric_terms"):
                continue
            for s in e.get("studies", []):
                trd.append([name, label, s["nct"], s["title"], s["status"], "|".join(s.get("phases") or []), "|".join(s.get("conditions") or []), s.get("min_age"), s.get("max_age"), s.get("has_results")])
    wr(out / "trials_nervous_system_detail.tsv", ["compound", "query_slice", "nct", "title", "status", "phases", "conditions", "min_age", "max_age", "has_results"], trd)
    # labels
    lab = []
    for name, d in res["labels"].items():
        for L in d.get("labels", []):
            for k, v in L["sections"].items():
                txt = " ".join(v) if isinstance(v, list) else str(v)
                lab.append([name, L["set_id"], L["effective_time"], "|".join(L.get("brand") or []), k, len(txt), len(re.findall(r"seiz|convuls|epilep", txt, re.I)), txt[:400]])
    wr(out / "labels_sections.tsv", ["compound", "set_id", "effective_time", "brand", "section", "chars", "n_seizure_words", "first_400_chars"], lab)
    # edges
    ed = []
    ix = res["edges"].get("interactions_to_MYC", {})
    for r in ix.get("rows", []):
        ed.append(["interactions", r.get("source_genesymbol"), r.get("target_genesymbol"), r.get("is_stimulation"), r.get("is_inhibition"), ";".join(r.get("sources") or []), r.get("references"), r.get("curation_effort"), json.dumps(r.get("extra_attrs"))[:300]])
    # enzsub_* queries are kept in collected.json.gz only: the service ignored the enzyme/substrate filter (returned MYC substrates of every kinase), so they are not tabulated.
    wr(out / "edge_records_omnipath.tsv", ["table", "source", "target", "stimulation_or_residue", "inhibition_or_mod", "sources", "references", "curation_effort", "extra"], ed)
    # hpa
    hp = []
    for g, e in res["hpa"].items():
        if e.get("state") != "ROWS_RETRIEVED":
            hp.append([g, e.get("state"), "", "", ""])
            continue
        for k, v in e["fields"].items():
            hp.append([g, e["ensembl"], k, json.dumps(v)[:600], ""])
    wr(out / "expression_hpa_raw.tsv", ["gene", "ensembl_or_state", "hpa_field", "value_json", ""], hp)
    return {"identity": len(ident), "mechanism_rows": len(mech), "measure_rows": len(det), "measure_groups": len(summ), "trial_slices": len(tr), "label_sections": len(lab), "edge_rows": len(ed), "hpa_rows": len(hp)}


def slim(res, cap=12000):
    """Keeps collected.json.gz under the 1 MB rule: label sections cut at `cap` characters (all counts in the tables are computed on the cut text), HPA key list dropped. Idempotent."""
    for e in res["labels"].values():
        for L in e.get("labels", []):
            for k, v in list(L["sections"].items()):
                t = " ".join(v) if isinstance(v, list) else str(v)
                L["sections"][k] = t[:cap]
    for e in res["hpa"].values():
        e.pop("all_keys", None)
    return res


def cmd_run(out):
    m = pq()
    net = m.Net()
    res = slim(collect(net))
    stamp = time.strftime("%Y-%m-%d", time.gmtime())
    out.mkdir(exist_ok=True)
    wr(out / "raw_hashes.tsv", ["item", "sha256", "bytes"], [[k[:170], m.sha(net.raw[k]), len(json.dumps(net.raw[k]))] for k in sorted(net.raw)])
    wr(out / "service_log.tsv", ["case", "attempt", "status", "seconds", "url", "error"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]] for l in net.log])
    col = gzip.compress(json.dumps({"retrieved_on": stamp, "collected": res}, sort_keys=True).encode(), mtime=0)
    (out / "collected.json.gz").write_bytes(col)
    raw_gz = gzip.compress(json.dumps({"retrieved_on": stamp, "responses": net.raw}, sort_keys=True).encode(), mtime=0)
    (out / "raw_store.json.gz").unlink(missing_ok=True)
    if len(raw_gz) < RAW_LIMIT:
        (out / "raw_store.json.gz").write_bytes(raw_gz)
    n = build(res, out, stamp)
    summ = {"retrieved_on": stamp, "attempts": len(net.log), "non200_attempts": sum(1 for l in net.log if l["status"] not in (200, 404)), "raw_gz_bytes": len(raw_gz), "raw_kept": len(raw_gz) < RAW_LIMIT, "collected_gz_bytes": len(col), **n}
    (out / "run_summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n")
    print(json.dumps(summ))


def cmd_rebuild(out):
    p = out / "collected.json.gz"
    if not p.exists():
        sys.exit("no collected.json.gz")
    d = json.loads(gzip.decompress(p.read_bytes()))
    res = slim(d["collected"])
    (out / "collected.json.gz").write_bytes(gzip.compress(json.dumps({"retrieved_on": d["retrieved_on"], "collected": res}, sort_keys=True).encode(), mtime=0))
    print(json.dumps(build(res, out, d["retrieved_on"])))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rebuild"], nargs="?")
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return
    (cmd_run if a.cmd == "run" else cmd_rebuild)(Path(a.out))


if __name__ == "__main__":
    main()
