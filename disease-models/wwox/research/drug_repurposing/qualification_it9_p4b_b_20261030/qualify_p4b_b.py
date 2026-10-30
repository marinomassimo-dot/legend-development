#!/usr/bin/env python3
"""IT9 P4b group B (Q4 protein / Q5 glia-myelin / neuro references): live acquisition for P3-05..P3-09, P3-17, P3-18.

  qualify_p4b_b.py --help          this text, no network
  qualify_p4b_b.py run [--out DIR] live: ChEMBL (molecule record, family, mechanisms, ALL activity rows molecule-first with assay type),
                                   PubChem (structure check by InChIKey), openFDA labels, ClinicalTrials.gov v2, OmniPath (edge records),
                                   Human Protein Atlas gene JSON; writes raw_store.json.gz (raw responses), service_log.tsv, raw_hashes.tsv
  qualify_p4b_b.py rebuild [--out DIR]  offline: rebuilds the derived tables from raw_store.json.gz (deterministic)

Reuses the IT8 P3 retry layer (pharm_qualify.Net: 0, 2, 6, 15, 30 s; every attempt logged). Standard library only. States are never merged:
SERVICE_ERROR / NO_ROWS_UNDER_FILTERS / ROWS_RETRIEVED / ROWS_RETRIEVED_TRUNCATED. No e-mail address or operator identity is sent anywhere.
A measure is kept with its assay type, species, relation and units; nothing is aggregated across types or units. Not medical advice."""
import argparse, csv, gzip, hashlib, importlib.util, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
P3 = HERE.parent / "pharmacological_qualification_it8_p3_20261029"
CB = "https://www.ebi.ac.uk/chembl/api/data"

CASES = {
    "P3-05": {"name": "fosfestrol", "ids": ["CHEMBL1200598"], "names": ["fosfestrol", "diethylstilbestrol diphosphate", "diethylstilbestrol"], "fda": ["fosfestrol", "diethylstilbestrol"],
              "edges": [("ESR2", "GAD2")], "genes": ["ESR2", "ESR1", "GAD2"]},
    "P3-06": {"name": "implitapide", "ids": ["CHEMBL2105804"], "names": ["implitapide", "BAY 13-9952"], "fda": ["implitapide"],
              "edges": [("P4HB", "ERN1"), ("ERN1", "XBP1"), ("XBP1", "GAD1")], "genes": ["P4HB", "MTTP", "ERN1", "XBP1", "GAD1"]},
    "P3-07": {"name": "curcumin", "ids": ["CHEMBL140"], "names": ["curcumin"], "fda": ["curcumin"],
              "edges": [("EP300", "TNF")], "genes": ["EP300", "TNF"]},
    "P3-08": {"name": "belnacasan", "ids": ["CHEMBL2107819"], "names": ["belnacasan", "VX-765"], "fda": ["belnacasan"],
              "edges": [("CASP1", "IL1B")], "genes": ["CASP1", "IL1B"]},
    "P3-09": {"name": "JTE-151", "ids": ["CHEMBL3545357"], "names": ["JTE-151"], "fda": ["JTE-151"],
              "edges": [("RORC", "IL6")], "genes": ["RORC", "IL6"]},
    "P3-17": {"name": "felbamate", "ids": ["CHEMBL1094"], "names": ["felbamate"], "fda": ["felbamate"], "edges": [], "genes": ["GRIN2C", "GRIN2B", "GRIN2A"]},
    "P3-18": {"name": "memantine", "ids": ["CHEMBL807", "CHEMBL1699"], "names": ["memantine"], "fda": ["memantine"], "edges": [], "genes": ["GRIN2C"]},
}
ENSG = {"ESR2": "ENSG00000140009", "ESR1": "ENSG00000091831", "GAD2": "ENSG00000136750", "GAD1": "ENSG00000128683", "P4HB": "ENSG00000185624", "MTTP": "ENSG00000138823",
        "ERN1": "ENSG00000178607", "XBP1": "ENSG00000100219", "EP300": "ENSG00000100393", "TNF": "ENSG00000232810", "CASP1": "ENSG00000137752", "IL1B": "ENSG00000125538",
        "RORC": "ENSG00000143365", "IL6": "ENSG00000136244", "GRIN2C": "ENSG00000161509", "GRIN2B": "ENSG00000273079", "GRIN2A": "ENSG00000183454"}
CT_COND = '(epilepsy OR seizure OR "developmental and epileptic encephalopathy" OR hypomyelination OR "neurodevelopmental disorder" OR "leukodystrophy")'
OMNI_DS = "omnipath,pathwayextra,kinaseextra,ligrecextra,collectri,tf_target,dorothea,mirnatarget,lncrna_mrna"
FDA_SECTIONS = ("boxed_warning", "indications_and_usage", "pharmacokinetics", "clinical_pharmacology", "pediatric_use", "warnings", "warnings_and_cautions",
                "contraindications", "dosage_and_administration", "mechanism_of_action", "drug_interactions", "use_in_specific_populations")


def pq():
    spec = importlib.util.spec_from_file_location("pharm_qualify", P3 / "pharm_qualify.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def all_activities(net, mid, cap=6000):
    rows, off, total = [], 0, None
    while off < cap:
        s, p = net.get(f"{CB}/activity.json?molecule_chembl_id={mid}&limit=1000&offset={off}", timeout=90)
        if s != 200 or not isinstance(p, dict):
            return {"state": "SERVICE_ERROR", "http": s, "total": total, "rows": rows}
        total = (p.get("page_meta") or {}).get("total_count", total)
        page = p.get("activities") or []
        rows += [{k: r.get(k) for k in ("activity_id", "molecule_chembl_id", "standard_type", "standard_relation", "standard_value", "standard_units", "target_chembl_id",
                                         "target_pref_name", "target_organism", "assay_chembl_id", "assay_type", "assay_description", "document_chembl_id", "document_year", "pchembl_value")} for r in page]
        off += len(page)
        if not page or not (p.get("page_meta") or {}).get("next"):
            break
    st = "ROWS_RETRIEVED_TRUNCATED" if (total or 0) > len(rows) else ("ROWS_RETRIEVED" if rows else "NO_ROWS_UNDER_FILTERS")
    return {"state": st, "total": total, "retrieved": len(rows), "rows": rows}


RELATED = {"P3-05": {"ids": ["CHEMBL411"], "keep": r"[Ee]strogen receptor", "why": "active species of the phosphate prodrug (diethylstilbestrol)"},
           "P3-08": {"ids": [], "search": ["VRT-043198", "VRT 043198", "belnacasan active metabolite"], "why": "active acid of the prodrug"}}
TARGETS = ["CHEMBL2093866", "CHEMBL2364681", "CHEMBL4801", "CHEMBL1741186", "CHEMBL2094124", "CHEMBL206", "CHEMBL242"]


def collect(net):
    pqm = pq()
    res = {"cases": {}, "edges": {}, "hpa": {}, "pubchem": {}, "targets": {}}
    for cid, c in CASES.items():
        net.case = cid
        e = {"molecules": [], "mechanisms": [], "activities": {}, "fda": [], "trials": [], "name": c["name"]}
        seen = []
        for mid in c["ids"]:
            mol = pqm.chembl_molecule(net, mid)
            e["molecules"].append(mol)
            s, m = net.get(f"{CB}/molecule/{mid}.json")
            if s == 200 and isinstance(m, dict):
                mol["extra"] = {k: m.get(k) for k in ("first_approval", "withdrawn_flag", "therapeutic_flag", "parenteral", "topical", "natural_product", "usan_stem", "prodrug", "molecule_synonyms")}
                mol["extra"]["synonyms"] = sorted({x.get("molecule_synonym") for x in (m.get("molecule_synonyms") or [])})[:25]
                mol["extra"].pop("molecule_synonyms")
                mol["extra"]["atc"] = m.get("atc_classifications")
                mol["extra"]["properties"] = {k: (m.get("molecule_properties") or {}).get(k) for k in ("full_mwt", "alogp", "psa", "hba", "hbd", "num_ro5_violations", "molecular_species")}
            fam = [mid] + ([mol["parent"]] if mol.get("parent") else []) + [k for k, _ in mol.get("family", [])]
            for fid in fam:
                if fid in seen:
                    continue
                seen.append(fid)
                s2, mm = net.get(f"{CB}/mechanism.json?molecule_chembl_id={fid}&limit=50")
                e["mechanisms"].append({"molecule": fid, "http": s2, "rows": [{k: x.get(k) for k in ("action_type", "mechanism_of_action", "target_chembl_id", "mechanism_comment", "selectivity_comment", "direct_interaction", "max_phase")} for x in (mm.get("mechanisms") or [])] if s2 == 200 and isinstance(mm, dict) else []})
                e["activities"][fid] = all_activities(net, fid)
        # PubChem by structure (InChIKey of every ChEMBL record) and by name
        for mol in e["molecules"]:
            ik = mol.get("inchikey")
            if ik:
                s3, p3 = net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/property/Title,InChIKey,MolecularFormula,CanonicalSMILES/JSON")
                res["pubchem"][f"{cid}:{mol['id']}:inchikey"] = {"http": s3, "payload": p3}
        for nm in c["names"][:1]:
            s3, p3 = net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nm.replace(' ', '%20')}/property/Title,InChIKey,MolecularFormula/JSON")
            res["pubchem"][f"{cid}:name:{nm}"] = {"http": s3, "payload": p3}
        for g in c["fda"]:
            s4, p4 = net.get("https://api.fda.gov/drug/label.json", params={"search": f'openfda.generic_name:"{g}"', "limit": 10})
            ent = {"generic": g, "http": s4, "labels": []}
            if s4 == 200 and isinstance(p4, dict):
                for lab in p4.get("results") or []:
                    ent["labels"].append({"openfda": {k: (lab.get("openfda") or {}).get(k) for k in ("brand_name", "generic_name", "manufacturer_name", "route", "product_type")},
                                          "effective_time": lab.get("effective_time"), "set_id": lab.get("set_id"),
                                          "sections": {k: " ".join(lab.get(k, []))[:6000] for k in FDA_SECTIONS if lab.get(k)}})
            e["fda"].append(ent)
        # ClinicalTrials.gov v2: (a) intervention only (count), (b) intervention x neurological conditions
        for nm in c["names"]:
            for tag, params in (("intr_only", {"query.intr": nm, "pageSize": 100, "countTotal": "true"}),
                                ("intr_x_neuro", {"query.intr": nm, "query.cond": CT_COND, "pageSize": 100, "countTotal": "true"})):
                s5, p5 = net.get("https://clinicaltrials.gov/api/v2/studies", params=params, timeout=60)
                hits = []
                if s5 == 200 and isinstance(p5, dict):
                    for st in p5.get("studies") or []:
                        ps = st.get("protocolSection") or {}
                        idm, sm, dm = ps.get("identificationModule") or {}, ps.get("statusModule") or {}, ps.get("designModule") or {}
                        hits.append({"nct": idm.get("nctId"), "title": idm.get("briefTitle"), "status": sm.get("overallStatus"), "phases": dm.get("phases"),
                                     "conditions": (ps.get("conditionsModule") or {}).get("conditions"), "start": (sm.get("startDateStruct") or {}).get("date"),
                                     "ages": (ps.get("eligibilityModule") or {}).get("stdAges")})
                e["trials"].append({"term": nm, "tag": tag, "http": s5, "total": (p5 or {}).get("totalCount") if isinstance(p5, dict) else None, "returned": len(hits), "hits": hits})
        res["cases"][cid] = e
    # related molecules (active species) and target records
    res["related"] = {}
    for cid, rel in RELATED.items():
        net.case = cid + "-related"
        ids = list(rel["ids"])
        srch = {}
        for q in rel.get("search", []):
            s6, p6 = net.get(f"{CB}/molecule/search.json?q={q.replace(' ', '%20')}&limit=10")
            srch[q] = {"http": s6, "hits": [(m.get("molecule_chembl_id"), m.get("pref_name"), sorted({x.get("molecule_synonym") for x in (m.get("molecule_synonyms") or [])})[:12],
                                             (m.get("molecule_structures") or {}).get("standard_inchi_key")) for m in (p6.get("molecules") or [])] if s6 == 200 and isinstance(p6, dict) else []}
            for h in srch[q]["hits"]:
                if h[0] not in ids:
                    ids.append(h[0])
        ent = {"why": rel["why"], "search": srch, "molecules": {}}
        for mid in ids:
            mol = pqm.chembl_molecule(net, mid)
            a = all_activities(net, mid)
            if rel.get("keep"):
                a["rows"] = [r for r in a["rows"] if re.search(rel["keep"], r.get("target_pref_name") or "")]
                a["kept_by"] = rel["keep"]
            ent["molecules"][mid] = {"molecule": mol, "activities": a}
        res["related"][cid] = ent
    net.case = "targets"
    for t in TARGETS:
        s7, p7 = net.get(f"{CB}/target/{t}.json")
        res["targets"][t] = {"http": s7, "name": (p7 or {}).get("pref_name") if isinstance(p7, dict) else None, "type": (p7 or {}).get("target_type") if isinstance(p7, dict) else None,
                             "components": [(c.get("accession"), c.get("component_description")) for c in (p7.get("target_components") or [])] if isinstance(p7, dict) else None}
    # edges: OmniPath records (all datasets), filtered client-side on the target symbol
    net.case = "edges"
    for cid, c in CASES.items():
        for a, b in c["edges"]:
            s, p = net.get("https://omnipathdb.org/interactions", params={"sources": a, "genesymbols": "yes", "fields": "sources,references,curation_effort,type", "datasets": OMNI_DS, "format": "json"}, timeout=90)
            rows = [r for r in p if r.get("target_genesymbol") == b] if s == 200 and isinstance(p, list) else []
            res["edges"][f"{a}->{b}"] = {"http": s, "n_source_rows": len(p) if isinstance(p, list) else None, "rows": rows}
    net.case = "HPA"
    for g, ens in ENSG.items():
        s, p = net.get(f"https://www.proteinatlas.org/{ens}.json", timeout=90)
        keep = ("Gene", "Ensembl", "Gene description", "Evidence", "RNA tissue specificity", "RNA tissue specific nTPM", "RNA single cell type specificity", "RNA single cell type specific nCPM",
                "RNA single nuclei brain specificity", "RNA single nuclei brain specific nCPM", "RNA brain regional specificity", "RNA brain regional specific nTPM",
                "Protein cell type specific Intensity", "Protein tissue specific Intensity", "Reliability (IH)")
        res["hpa"][g] = {"http": s, "data": {k: p.get(k) for k in keep} if s == 200 and isinstance(p, dict) else None}
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rebuild"])
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    out = Path(a.out)
    if a.cmd == "rebuild":
        sys.path.insert(0, str(HERE))
        import tables_p4b_b
        tables_p4b_b.build(json.loads(gzip.open(out / "raw_store.json.gz", "rt").read()), out)
        return
    net = pq().Net()
    res = collect(net)
    data = json.dumps(res, ensure_ascii=False)
    with gzip.open(out / "raw_store.json.gz", "wt", encoding="utf-8") as f:
        f.write(data)
    with open(out / "service_log.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["case", "attempt", "status", "seconds", "url", "error"], delimiter="\t")
        w.writeheader()
        w.writerows(net.log)
    with open(out / "raw_hashes.tsv", "w", encoding="utf-8") as f:
        f.write("key\tstatus\tsha256\n")
        for k, (s, p) in sorted(net.raw.items()):
            f.write(f"{k[:180]}\t{s}\t{sha(p)}\n")
    print("attempts", len(net.log), "non200", sum(1 for x in net.log if x["status"] != 200), "store bytes", len(data))


if __name__ == "__main__":
    main()
