#!/usr/bin/env python3
"""IT9 P4b group A (Q2 metabolism/glycolysis + PDK reference): live acquisition of the public records behind the qualification.

  qualify_p4b_a.py --help          this text, no network
  qualify_p4b_a.py run [--out DIR] live: ChEMBL (molecule, structure, mechanism, all activity rows), PubChem (identity by InChIKey and by name),
                                   openFDA (label, adverse-event counts), ClinicalTrials.gov v2 (counts and hits), OmniPath (edge records with
                                   references), PubMed E-utilities (counts, titles), Human Protein Atlas (per-gene JSON). Writes raw_store.json.gz,
                                   service_log.tsv (every attempt) and raw_hashes.tsv.

Standard library only. No identifying header, no e-mail address, no operator identity is sent. Retry 0,2,6,15,30 s on 5xx/429/transport; 404 is an answer.
States are kept apart: SERVICE_ERROR / NO_ROWS / ROWS. Nothing here is medical advice; a database row is not a therapeutic effect."""
import argparse, csv, gzip, hashlib, json, sys, time, urllib.parse, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKOFF = (0, 2, 6, 15, 30)
UA = "legend-public-research/1.0 (non-commercial literature and database qualification)"

COMPOUNDS = {"P3-01": ("balsalazide", "CHEMBL1201346"), "P3-02": ("ramelteon", "CHEMBL1218"), "P3-03": ("belzutifan", "CHEMBL4585668"),
             "P3-04": ("ceperognastat", "CHEMBL5095251"), "P3-14": ("AR-12", "CHEMBL1650595"), "P3-15": ("dichloroacetate", "CHEMBL306823")}
EXTRA_CHEMBL = {"mesalamine": "CHEMBL704", "dichloroacetic_acid": "CHEMBL13960"}
GENES = ["PPARG", "SLC2A1", "MTNR1A", "MTNR1B", "GNAO1", "HES1", "BNIP3", "EPAS1", "ARNT", "HIF1A", "LDHA", "OGA", "MGEA5", "OGT", "PFKP", "PDPK1", "PDK1", "PDHA1", "PDK2", "PDK3", "PDK4"]
EDGES = [("PPARG", "SLC2A1"), ("MTNR1A", "GNAO1"), ("GNAO1", "HES1"), ("HES1", "BNIP3"), ("EPAS1", "LDHA"), ("OGA", "PFKP"), ("OGT", "PFKP"), ("PPARG", "PFKP"),
         ("MTNR1B", "GNAO1"), ("HIF1A", "PDK1"), ("HIF1A", "LDHA"), ("HIF1A", "SLC2A1"), ("EPAS1", "SLC2A1"), ("EPAS1", "BNIP3")]
CTG_COND = ["epilepsy", "seizure", "developmental and epileptic encephalopathy", "hypomyelination", "neurodevelopmental disorder", "intellectual disability", "cerebral palsy"]
CTG_INTR = {"balsalazide": ["balsalazide"], "ramelteon": ["ramelteon"], "belzutifan": ["belzutifan", "MK-6482", "PT2977"],
            "ceperognastat": ["ceperognastat", "LY3372689"], "AR-12": ["AR-12", "OSU-03012"], "dichloroacetate": ["dichloroacetate", "dichloroacetic acid"]}
PUBMED = {
    "balsalazide_seizure": "balsalazide AND (seizure OR convulsion OR epilepsy)",
    "balsalazide_ped": "balsalazide AND (children OR pediatric OR paediatric)",
    "mesalamine_csf": "(mesalamine OR 5-aminosalicylic acid OR mesalazine) AND (cerebrospinal fluid OR brain penetration OR blood-brain barrier)",
    "mesalamine_ppar": "(mesalamine OR 5-aminosalicylic acid) AND PPAR gamma",
    "mesalamine_neuro": "(mesalamine OR mesalazine) AND (neurotoxicity OR seizure OR neurodevelopment)",
    "ramelteon_seizure": "ramelteon AND (seizure OR convulsion OR epilepsy)",
    "ramelteon_ped": "ramelteon AND (children OR pediatric OR paediatric OR adolescent)",
    "ramelteon_brain": "ramelteon AND (cerebrospinal fluid OR brain penetration OR brain concentration OR blood-brain barrier)",
    "melatonin_receptor_brain_dev": "(MT1 OR MT2 OR MTNR1A OR MTNR1B) AND melatonin receptor AND (fetal brain OR developing brain OR neural progenitor OR cortex)",
    "ramelteon_glycolysis": "(ramelteon OR melatonin receptor agonist) AND (BNIP3 OR glycolysis OR HES1)",
    "belzutifan_seizure": "belzutifan AND (seizure OR convulsion OR epilepsy OR neurotoxicity)",
    "belzutifan_ped": "belzutifan AND (children OR pediatric OR paediatric OR adolescent)",
    "belzutifan_brain": "(belzutifan OR PT2977) AND (brain OR CNS OR cerebrospinal fluid OR central nervous system)",
    "hif2a_neurodev": "(HIF-2alpha OR EPAS1) AND (neural progenitor OR neurodevelopment OR cortical development OR neuron)",
    "hif2a_ldha_neural": "(HIF-2alpha OR EPAS1) AND LDHA AND (neuron OR neural OR brain OR astrocyte)",
    "ceperognastat_pk": "(ceperognastat OR LY3372689) AND (pharmacokinetics OR cerebrospinal fluid OR target engagement OR PET)",
    "ceperognastat_safety": "(ceperognastat OR LY3372689) AND (safety OR adverse OR trial)",
    "oga_inhibitor_safety": "(O-GlcNAcase inhibitor OR OGA inhibitor) AND (seizure OR neurodevelopment OR toxicity OR safety)",
    "oga_pfkp": "(O-GlcNAcase OR OGA OR O-GlcNAc) AND (PFK1 OR phosphofructokinase)",
    "oglcnac_neurodev": "(OGT OR O-GlcNAc transferase) AND (intellectual disability OR neurodevelopmental)",
    "ar12_targets": "(AR-12 OR OSU-03012) AND (PDK1 OR PDPK1 OR kinase OR acetyl-CoA synthetase OR PAK)",
    "ar12_safety": "(AR-12 OR OSU-03012) AND (phase I OR clinical trial OR toxicity OR pharmacokinetics)",
    "ar12_pdhk": "(AR-12 OR OSU-03012) AND (pyruvate dehydrogenase kinase)",
    "pdk1_symbol_collision": "PDK1 AND (3-phosphoinositide-dependent protein kinase 1 OR pyruvate dehydrogenase kinase 1) AND nomenclature",
}
DAILY_LABEL = {"balsalazide": "balsalazide", "ramelteon": "ramelteon", "belzutifan": "belzutifan", "ceperognastat": "ceperognastat"}
FAERS_TERMS = {"balsalazide": "balsalazide", "ramelteon": "ramelteon", "belzutifan": "belzutifan"}


class Net:
    def __init__(self):
        self.log, self.raw, self.case, self.last = [], {}, "", 0.0

    def get(self, url, kind="json", timeout=60):
        if url in self.raw:
            return self.raw[url]["status"], self.raw[url]["payload"]
        status, payload = 0, ""
        for i, wait in enumerate(BACKOFF):
            if wait:
                time.sleep(wait)
            gap = time.time() - self.last
            if gap < 0.4:
                time.sleep(0.4 - gap)
            t0 = time.time()
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/plain, */*"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    status, body = r.status, r.read().decode("utf-8", "replace")
                payload = json.loads(body) if kind == "json" else body
            except urllib.error.HTTPError as e:
                status, payload = e.code, e.read().decode("utf-8", "replace")[:300]
            except Exception as e:  # transport or parse
                status, payload = 0, f"{type(e).__name__}: {e}"[:300]
            self.last = time.time()
            self.log.append({"case": self.case, "attempt": i + 1, "status": status, "seconds": round(time.time() - t0, 2), "url": url[:220],
                             "error": "" if status == 200 else str(payload)[:120]})
            if status == 200 or status == 404:
                break
            if status in (400, 401, 403) :
                break
        self.raw[url] = {"status": status, "payload": payload}
        return status, payload


def q(s):
    return urllib.parse.quote(s, safe="")


def chembl_all(net, path, params, key):
    rows, off = [], 0
    while True:
        u = f"https://www.ebi.ac.uk/chembl/api/data/{path}.json?{params}&limit=200&offset={off}"
        s, p = net.get(u)
        if s != 200 or not isinstance(p, dict):
            return {"state": "SERVICE_ERROR", "rows": rows, "status": s}
        page = p.get(key) or []
        rows += page
        off += len(page)
        if not page or not (p.get("page_meta") or {}).get("next"):
            return {"state": "ROWS" if rows else "NO_ROWS", "rows": rows, "total": (p.get("page_meta") or {}).get("total_count")}


def run(out):
    net = Net()
    R = {"chembl": {}, "pubchem": {}, "openfda": {}, "ctg": {}, "omnipath": {}, "pubmed": {}, "hpa": {}}
    # ---- ChEMBL
    for cid, (name, ch) in list(COMPOUNDS.items()) + [(k, (k, v)) for k, v in EXTRA_CHEMBL.items()]:
        net.case = f"chembl:{name}"
        s, m = net.get(f"https://www.ebi.ac.uk/chembl/api/data/molecule/{ch}.json")
        mech = chembl_all(net, "mechanism", f"molecule_chembl_id={ch}", "mechanisms")
        act = chembl_all(net, "activity", f"molecule_chembl_id={ch}", "activities")
        ids = sorted({r["assay_chembl_id"] for r in act["rows"] if r.get("assay_chembl_id")})
        assays = {}
        for i in range(0, len(ids), 40):
            s2, p = net.get(f"https://www.ebi.ac.uk/chembl/api/data/assay.json?assay_chembl_id__in={','.join(ids[i:i+40])}&limit=100")
            if s2 == 200 and isinstance(p, dict):
                for a in p.get("assays") or []:
                    assays[a["assay_chembl_id"]] = {k: a.get(k) for k in ("assay_organism", "assay_cell_type", "assay_type", "description", "target_chembl_id")}
        R["chembl"][name] = {"molecule_status": s, "molecule": m if s == 200 else None, "mechanism": mech, "activity": act, "assays": assays}
    # ceperognastat name searches
    net.case = "chembl:ceperognastat_name"
    R["chembl"]["_name_search_ceperognastat"] = {}
    for term in ("ceperognastat", "LY3372689", "LY-3372689"):
        s, p = net.get(f"https://www.ebi.ac.uk/chembl/api/data/molecule/search.json?q={q(term)}&limit=20")
        R["chembl"]["_name_search_ceperognastat"][term] = {"status": s, "payload": p if s == 200 else None}
    # ---- PubChem
    for cid, (name, ch) in COMPOUNDS.items():
        net.case = f"pubchem:{name}"
        mol = (R["chembl"][name]["molecule"] or {})
        ik = (mol.get("molecule_structures") or {}).get("standard_inchi_key")
        d = {"chembl_inchikey": ik}
        if ik:
            d["by_inchikey"] = dict(zip(("status", "payload"), net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/property/MolecularFormula,MolecularWeight,InChIKey,CanonicalSMILES,IUPACName/JSON")))
            d["synonyms_by_inchikey"] = dict(zip(("status", "payload"), net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/synonyms/JSON")))
        for nm in {name, "OSU-03012" if name == "AR-12" else name, "LY3372689" if name == "ceperognastat" else name}:
            d["by_name:" + nm] = dict(zip(("status", "payload"), net.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{q(nm)}/property/MolecularFormula,InChIKey,CanonicalSMILES/JSON")))
        R["pubchem"][name] = d
    # ---- openFDA labels and adverse events
    for name, g in DAILY_LABEL.items():
        net.case = f"openfda_label:{name}"
        s, p = net.get(f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22{q(g)}%22&limit=3")
        R["openfda"][f"label:{name}"] = {"status": s, "payload": p}
    for name, g in FAERS_TERMS.items():
        net.case = f"openfda_faers:{name}"
        base = f"patient.drug.openfda.generic_name:%22{q(g)}%22"
        s0, p0 = net.get(f"https://api.fda.gov/drug/event.json?search={base}&limit=1")
        s1, p1 = net.get(f"https://api.fda.gov/drug/event.json?search={base}&count=patient.reaction.reactionmeddrapt.exact&limit=1000")
        R["openfda"][f"faers:{name}"] = {"total": [s0, (p0.get("meta") if isinstance(p0, dict) else p0)], "reaction_counts": [s1, p1]}
    # ---- ClinicalTrials.gov
    for name, intrs in CTG_INTR.items():
        net.case = f"ctg:{name}"
        res = {}
        for it in intrs:
            s, p = net.get(f"https://clinicaltrials.gov/api/v2/studies?query.intr={q(it)}&countTotal=true&pageSize=1")
            res[f"{it}|ALL"] = [s, p.get("totalCount") if isinstance(p, dict) else p]
            for cond in CTG_COND:
                s, p = net.get(f"https://clinicaltrials.gov/api/v2/studies?query.intr={q(it)}&query.cond={q(cond)}&countTotal=true&pageSize=20&fields=NCTId,BriefTitle,OverallStatus,Phase,Condition,EnrollmentCount,MinimumAge")
                res[f"{it}|{cond}"] = [s, p]
        R["ctg"][name] = res
    net.case = "ctg:wwox"
    R["ctg"]["_wwox"] = {t: net.get(f"https://clinicaltrials.gov/api/v2/studies?query.term={q(t)}&countTotal=true&pageSize=5&fields=NCTId,BriefTitle,OverallStatus")
                         for t in ("WWOX", "WWOX-related epileptic encephalopathy")}
    # ---- OmniPath edge records (live, with references)
    for s_, t_ in EDGES:
        net.case = f"omnipath:{s_}>{t_}"
        s, p = net.get(f"https://omnipathdb.org/interactions?sources={s_}&targets={t_}&genesymbols=1&fields=sources,type,references,curation_effort&format=tsv&organisms=9606&datasets=omnipath,pathwayextra,kinaseextra,tf_target,collectri&license=academic", kind="text")
        s2, p2 = net.get(f"https://omnipathdb.org/interactions?sources={s_}&targets={t_}&genesymbols=1&fields=sources,type,references,curation_effort&format=tsv&organisms=9606&datasets=collectri&license=academic", kind="text")
        R["omnipath"][f"{s_}>{t_}"] = {"main": [s, p], "collectri": [s2, p2]}
    # ---- PubMed
    for k, term in PUBMED.items():
        net.case = f"pubmed:{k}"
        s, p = net.get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=25&term={q(term)}")
        ids = (p.get("esearchresult", {}).get("idlist") if isinstance(p, dict) else None) or []
        titles = {}
        if ids:
            s2, p2 = net.get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={','.join(ids)}")
            if s2 == 200 and isinstance(p2, dict):
                for i in ids:
                    r = (p2.get("result") or {}).get(i) or {}
                    titles[i] = [r.get("pubdate"), r.get("source"), r.get("title")]
        R["pubmed"][k] = {"term": term, "status": s, "count": (p.get("esearchresult", {}).get("count") if isinstance(p, dict) else None), "titles": titles}
    # ---- HPA
    for g in GENES:
        net.case = f"hpa:{g}"
        s, p = net.get(f"https://www.proteinatlas.org/api/search_download.php?search={q(g)}&format=json&columns=g,eg&compress=no")
        ens = None
        if s == 200 and isinstance(p, list):
            for r in p:
                if r.get("Gene") == g:
                    ens = r.get("Ensembl")
        d = {"search_status": s, "ensembl": ens}
        if ens:
            s2, p2 = net.get(f"https://www.proteinatlas.org/{ens}.json")
            if s2 == 200 and isinstance(p2, dict):
                d["record"] = {k: v for k, v in p2.items() if not k.startswith("Cancer prognostics")}
            d["json_status"] = s2
        R["hpa"][g] = d
    out.mkdir(parents=True, exist_ok=True)
    with gzip.open(out / "collected.json.gz", "wt") as f:
        json.dump(R, f)
    with gzip.open(out / "raw_store.json.gz", "wt") as f:
        json.dump(net.raw, f)
    with open(out / "service_log.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["case", "attempt", "status", "seconds", "url", "error"], delimiter="\t")
        w.writeheader(); w.writerows(net.log)
    with open(out / "raw_hashes.tsv", "w") as f:
        f.write("url\tstatus\tsha256\n")
        for u, v in net.raw.items():
            f.write(f"{u[:200]}\t{v['status']}\t{hashlib.sha256(json.dumps(v['payload'], sort_keys=True).encode()).hexdigest()}\n")
    print(len(net.log), "attempts;", sum(1 for l in net.log if l["status"] not in (200, 404)), "non-200/404")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    if a.cmd == "run":
        run(Path(a.out))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
