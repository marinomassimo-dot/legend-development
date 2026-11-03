#!/usr/bin/env python3
"""IT21 P4a: free-source collection for the six qualified proposals (identity, mechanism, activities, edge records, literature).

  collect_p4a_it21.py --help      this text, no network
  collect_p4a_it21.py run         live fetch (ChEMBL REST, OmniPath, Europe PMC, Human Protein Atlas); writes raw_hashes.tsv, service_log.tsv,
                                  chembl_*.tsv, edge_records_omnipath.tsv, literature_*.tsv, collected.json.gz
  collect_p4a_it21.py tables      offline: rebuild the TSV tables from collected.json.gz
  collect_p4a_it21.py pubmed      NCBI E-utilities PubMed counts and first hits for the literature questions (Europe PMC answered HTTP 503)

Standard library only. No key, no e-mail address, no operator identity, no registration is sent anywhere. Every attempt is logged; states are
never merged (SERVICE_ERROR / NO_RECORD / ROWS_RETRIEVED / NO_ROWS_UNDER_FILTERS). Values of different standard types are never pooled.
Nothing here is medical advice."""
import argparse, collections, csv, gzip, hashlib, json, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
OMNI = "https://omnipathdb.org"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = "legend-public-research/1.0 (no contact string)"

COMPOUNDS = {   # proposal -> (name, ChEMBL id or None to resolve by search, target symbols of interest for the activity table)
    "IT21P2-0006": ("NANATINOSTAT", "CHEMBL1801250", ["HDAC1", "HDAC2", "HDAC3", "HDAC4", "HDAC5", "HDAC6", "HDAC7", "HDAC8", "HDAC9", "HDAC10", "HDAC11"]),
    "IT21P2-0008": ("Iox1", "CHEMBL1230640", ["KDM4A", "KDM4B", "KDM4C", "KDM4D", "KDM4E", "KDM5A", "KDM5B", "KDM3A", "KDM2A", "KDM6B", "EGLN1", "EGLN2", "EGLN3", "HIF1AN", "FTO", "ALKBH5"]),
    "IT21P2-0057": ("Cgi1746", "CHEMBL1230541", ["BTK", "TEC", "ITK", "BMX", "TXK", "EGFR", "ERBB2", "JAK3", "BLK", "SRC", "LYN", "FYN", "LCK", "HCK"]),
    "IT21P2-0195": ("Gsk343", "CHEMBL2204995", ["EZH2", "EZH1", "EED", "SUZ12", "PRMT5", "SETD2", "SUV39H1", "EHMT2", "DOT1L", "NSD2"]),
    "IT21P2-0374": ("TIZATERKIB", None, ["MAPK1", "MAPK3", "MAPK8", "MAPK14", "BRAF", "MAP2K1"]),
    "IT21P2-0512": ("SRT-2104", "CHEMBL4297436", ["SIRT1", "SIRT2", "SIRT3", "SIRT5", "SIRT6", "SIRT7"]),
}
# decisive edges of the engine chains: (proposal, source, target, sign in the network, mode)
EDGES = [("0006", "HDAC5", "SLC2A1"), ("0008", "KDM4C", "HIF1A"), ("0008", "HIF1A", "HK2"), ("0008", "HIF1A", "SLC2A1"),
         ("0057", "BTK", "STAT3"), ("0057", "STAT3", "NPY"), ("0195", "EZH2", "IL6"), ("0195", "EZH2", "TNF"),
         ("0374", "MAPK1", "BCL3"), ("0374", "BCL3", "TNF"), ("0512", "SIRT1", "MYC")]
# literature questions (Europe PMC title/abstract searches; counts and ids only, the abstract text is fetched for the hits we cite)
LIT = {
    "L01_nanatinostat_HDAC_selectivity": '(nanatinostat OR "CHR-3996" OR "VRx-3996") AND (HDAC OR "histone deacetylase")',
    "L02_HDAC5_SLC2A1": '(HDAC5) AND (GLUT1 OR SLC2A1 OR "glucose transporter 1")',
    "L03_nanatinostat_CNS": '(nanatinostat OR "CHR-3996" OR "VRx-3996") AND (brain OR CNS OR neuron OR "blood-brain")',
    "L04_IOX1_PHD_HIF": '(IOX1 OR "5-carboxy-8-hydroxyquinoline") AND (HIF OR "prolyl hydroxylase" OR PHD2 OR EGLN OR "2-oxoglutarate")',
    "L05_IOX1_cell": '(IOX1 OR "5-carboxy-8-hydroxyquinoline") AND (cell OR permeab OR "ester")',
    "L06_KDM4C_HIF1A": '(KDM4C OR JMJD2C) AND (HIF1A OR HIF-1alpha OR "HIF-1")',
    "L07_WWOX_KDM4": 'WWOX AND (KDM4 OR JMJD2 OR "histone demethylase")',
    "L08_CGI1746_BTK": '(CGI1746 OR CGI-1746) AND (BTK OR "Bruton")',
    "L09_BTK_STAT3": '(BTK OR "Bruton") AND STAT3 AND (phosphorylation OR "tyrosine kinase")',
    "L10_STAT3_NPY": 'STAT3 AND (NPY OR "neuropeptide Y") AND (promoter OR transcription OR regulat)',
    "L11_BTK_neuron_brain": '(BTK OR "Bruton") AND (neuron OR microglia OR brain) AND (expression OR inhibitor)',
    "L12_GSK343_selectivity": 'GSK343 AND (EZH2 OR EZH1 OR selectiv)',
    "L13_EZH2_IL6": 'EZH2 AND (IL6 OR "interleukin-6") AND (inhibit OR knockdown OR repress)',
    "L14_EZH2_inhibitor_brain_development": '(EZH2 OR PRC2) AND (inhibitor OR deletion OR knockout) AND (cortex OR neural progenitor OR neurogenesis)',
    "L15_GSK343_microglia": 'GSK343 AND (microglia OR astrocyte OR neuroinflammation OR LPS)',
    "L16_tizaterkib": '(tizaterkib OR AZD0364 OR "AZ13767370")',
    "L17_ERK_inhibitor_TNF": '(ERK OR MAPK1 OR "MAPK3") AND (inhibitor) AND (TNF OR "tumor necrosis factor") AND (macrophage OR microglia)',
    "L18_BCL3_TNF": 'BCL3 AND (TNF OR "tumor necrosis factor") AND (repress OR inhibit OR suppress)',
    "L19_ERK_WWOX": 'WWOX AND (ERK OR MAPK OR "MAPK1" OR "p-ERK")',
    "L20_SRT2104_SIRT1_activation": '(SRT2104 OR SRT-2104) AND (SIRT1 OR sirtuin)',
    "L21_SIRT1_activators_artefact": '(resveratrol OR SRT1720 OR SRT2104 OR SRT1460) AND SIRT1 AND (fluorophore OR artifact OR artefact OR "direct activat" OR "not direct")',
    "L22_SIRT1_MYC": 'SIRT1 AND (MYC OR "c-Myc") AND (deacetyl OR stability OR degradation OR "protein")',
    "L23_SRT2104_brain": '(SRT2104 OR SRT-2104) AND (brain OR CNS OR Huntington OR "blood-brain" OR neuro)',
    "L24_WWOX_SIRT1": 'WWOX AND (SIRT1 OR sirtuin)',
    "L25_WWOX_HDAC": 'WWOX AND (HDAC OR "histone deacetylase")',
    "L26_WWOX_EZH2": 'WWOX AND (EZH2 OR PRC2 OR polycomb)',
    "L27_WWOX_BTK": 'WWOX AND (BTK OR "Bruton")',
}


class Net:
    def __init__(self):
        self.raw, self.log = {}, []

    def get(self, url, params=None, timeout=60, case=""):
        full = url + ("?" + urllib.parse.urlencode(sorted((params or {}).items())) if params else "")
        for i, wait in enumerate((0, 2, 6, 15)):
            if wait:
                time.sleep(wait)
            t0, status, payload = time.time(), 0, None
            try:
                req = urllib.request.Request(full, headers={"User-Agent": UA, "Accept": "application/json"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    body = r.read()
                    status = r.status
                    payload = json.loads(body)
            except urllib.error.HTTPError as e:
                status, payload = e.code, str(e)[:120]
            except Exception as e:  # network / parse
                status, payload = 0, str(e)[:120]
            self.log.append({"case": case, "attempt": i + 1, "status": status, "seconds": round(time.time() - t0, 2), "url": full[:230]})
            print(case, i + 1, status, round(time.time() - t0, 1), full[:110], flush=True)
            if status in (200, 404):
                break
        self.raw[full] = [status, payload]
        return status, payload


def sha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def pages(net, url, key, params, case, cap=4000):
    out, p, total = [], dict(params, limit=1000, offset=0), None
    while True:
        st, d = net.get(url, p, case=case)
        if st != 200 or not isinstance(d, dict):
            return out, "SERVICE_ERROR" if st != 404 else "NO_RECORD", total
        out += d.get(key, [])
        total = d.get("page_meta", {}).get("total_count", total)
        if not d.get("page_meta", {}).get("next") or len(out) >= cap:
            break
        p["offset"] += 1000
    return out, ("ROWS_RETRIEVED" if out else "NO_ROWS_UNDER_FILTERS"), total


def collect(net):
    res = {"compounds": {}, "edges": {}, "lit": {}, "hpa": {}}
    for pid, (name, cid, genes) in COMPOUNDS.items():
        c = {"name": name}
        if cid is None:
            st, d = net.get(CHEMBL + "/molecule/search.json", {"q": name, "limit": 5}, case=pid)
            hits = [(m["molecule_chembl_id"], m.get("pref_name")) for m in d.get("molecules", [])] if st == 200 else []
            c["search_hits"] = hits
            cid = hits[0][0] if hits else None
        c["chembl_id"] = cid
        if cid:
            st, m = net.get(CHEMBL + f"/molecule/{cid}.json", case=pid)
            c["molecule"] = m if st == 200 else {"status": st}
            mech, s1, t1 = pages(net, CHEMBL + "/mechanism.json", "mechanisms", {"molecule_chembl_id": cid}, pid)
            c["mechanism"], c["mechanism_state"] = mech, s1
            acts, s2, t2 = pages(net, CHEMBL + "/activity.json", "activities", {"molecule_chembl_id": cid}, pid)
            keep = ("activity_id", "assay_chembl_id", "assay_description", "assay_type", "document_chembl_id", "standard_type", "standard_relation", "standard_value",
                    "standard_units", "pchembl_value", "target_chembl_id", "target_pref_name", "target_organism", "assay_organism", "bao_label", "document_year", "activity_comment",
                    "data_validity_comment", "potential_duplicate", "molecule_pref_name")
            c["activities"] = [{k: a.get(k) for k in keep} for a in acts]
            c["activity_state"], c["activity_total"] = s2, t2
            ids = sorted({a["target_chembl_id"] for a in acts if a.get("target_chembl_id")})
            tg = {}
            for i in range(0, len(ids), 40):
                st, d = net.get(CHEMBL + "/target.json", {"target_chembl_id__in": ",".join(ids[i:i + 40]), "limit": 100}, case=pid)
                for t in (d.get("targets", []) if st == 200 else []):
                    tg[t["target_chembl_id"]] = {"type": t.get("target_type"), "name": t.get("pref_name"), "organism": t.get("organism"),
                                                 "symbols": sorted({cc.get("component_synonym") for comp in t.get("target_components", []) for cc in comp.get("target_component_synonyms", []) if cc.get("syn_type") == "GENE_SYMBOL"})}
            c["targets"] = tg
        res["compounds"][pid] = c
    for pid, a, b in EDGES:
        st, d = net.get(OMNI + "/interactions", {"sources": a, "targets": b, "genesymbols": 1, "fields": "sources,references,curation_effort,type", "format": "json", "datasets": "omnipath,pathwayextra,kinaseextra,ligrecextra,tfregulons,collectri,dorothea,transcriptional"}, case="edge")
        res["edges"][f"{a}>{b}"] = {"status": st, "rows": d if st == 200 else str(d)[:100]}
    for k, q in LIT.items():
        st, d = net.get(EPMC, {"query": q, "format": "json", "pageSize": 25, "resultType": "lite"}, case=k)
        res["lit"][k] = {"query": q, "status": st, "count": d.get("hitCount") if st == 200 else None,
                         "hits": [{"id": r.get("id"), "src": r.get("source"), "pmid": r.get("pmid"), "pmcid": r.get("pmcid"), "title": r.get("title"), "year": r.get("pubYear"),
                                   "journal": r.get("journalTitle")} for r in (d.get("resultList", {}).get("result", []) if st == 200 else [])]}
    return res


def num(a):
    try:
        return float(a["standard_value"])
    except (TypeError, ValueError):
        return None


def write(path, head, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        w.writerows(rows)


def tables(res):
    rows_a, rows_s, rows_m, rows_e, rows_l, rows_t = [], [], [], [], [], []
    for pid, c in res["compounds"].items():
        mol = c.get("molecule", {})
        rows_m.append([pid, c["name"], c.get("chembl_id"), mol.get("pref_name"), mol.get("molecule_type"), mol.get("max_phase"), (mol.get("molecule_structures") or {}).get("canonical_smiles"),
                       (mol.get("molecule_structures") or {}).get("standard_inchi_key"), (mol.get("molecule_properties") or {}).get("full_mwt"), mol.get("therapeutic_flag"), mol.get("prodrug"),
                       json.dumps([s["molecule_synonym"] for s in mol.get("molecule_synonyms", [])][:12]), json.dumps([h["molecule_chembl_id"] for h in mol.get("molecule_hierarchy", {}) and [mol["molecule_hierarchy"]] if h]) if mol.get("molecule_hierarchy") else "",
                       c.get("mechanism_state"), c.get("activity_state"), c.get("activity_total")])
        for m in c.get("mechanism", []):
            rows_s.append([pid, c["name"], m.get("target_chembl_id"), m.get("mechanism_of_action"), m.get("action_type"), m.get("direct_interaction"), m.get("molecular_mechanism"), json.dumps([r.get("ref_id") for r in m.get("mechanism_refs", [])])])
        g = collections.defaultdict(list)
        for a in c.get("activities", []):
            if num(a) is None or a["standard_type"] not in ("IC50", "Ki", "Kd", "EC50", "Potency", "Inhibition", "AC50"):
                continue
            g[(a["target_chembl_id"], a["standard_type"], a["standard_units"], a["standard_relation"] or "=")].append(a)
        for (t, st, un, rel), L in sorted(g.items()):
            ti = c["targets"].get(t, {})
            vals = [num(a) for a in L]
            rows_a.append([pid, c["name"], t, ti.get("name"), ";".join(ti.get("symbols", [])), ti.get("type"), ti.get("organism"), st, rel, un, len(L), min(vals), max(vals), len({a["document_chembl_id"] for a in L}),
                           ";".join(sorted({a["document_chembl_id"] for a in L})[:6]), ";".join(sorted({a["bao_label"] or "" for a in L})), ";".join(sorted({a["assay_type"] or "" for a in L})),
                           " | ".join(sorted({(a["assay_description"] or "")[:110] for a in L})[:2])])
    for k, d in res["edges"].items():
        rows = d["rows"] if isinstance(d["rows"], list) else []
        a, b = k.split(">")
        for r in rows:
            if r.get("source_genesymbol") == a and r.get("target_genesymbol") == b:
                rows_e.append([k, r.get("type"), r.get("is_directed"), r.get("consensus_stimulation"), r.get("consensus_inhibition"), r.get("sources"), r.get("references"), r.get("curation_effort")])
        if not any(r.get("source_genesymbol") == a and r.get("target_genesymbol") == b for r in rows):
            rows_e.append([k, "NO_MATCHING_RECORD" if d["status"] == 200 else f"SERVICE_{d['status']}", "", "", "", "", "", ""])
    for k, d in res["lit"].items():
        rows_l.append([k, d["query"], d["status"], d["count"], ";".join(f"{h['pmid'] or h['id']}:{h['year']}" for h in d["hits"][:15])])
        for h in d["hits"][:25]:
            rows_t.append([k, h["src"], h["pmid"], h["pmcid"], h["year"], h["journal"], h["title"]])
    write(HERE / "identity_chembl.tsv", ["proposal", "name", "chembl_id", "pref_name", "molecule_type", "max_phase", "smiles", "inchikey", "mw_full", "therapeutic_flag", "prodrug_flag", "synonyms", "hierarchy", "mechanism_state", "activity_state", "activity_total_count"], rows_m)
    write(HERE / "chembl_mechanism.tsv", ["proposal", "name", "target_chembl_id", "mechanism_of_action", "action_type", "direct_interaction", "molecular_mechanism", "refs"], rows_s)
    write(HERE / "chembl_activities_by_target.tsv", ["proposal", "name", "target_chembl_id", "target_name", "gene_symbols", "target_type", "target_organism", "standard_type", "relation", "units", "n_rows", "min_value", "max_value", "n_documents", "documents", "bao_formats", "assay_types", "assay_description_examples"], rows_a)
    write(HERE / "edge_records_omnipath.tsv", ["edge", "type", "is_directed", "stimulation", "inhibition", "sources", "references", "curation_effort"], rows_e)
    write(HERE / "literature_counts.tsv", ["label", "query", "http_status", "hit_count", "first_hits(pmid:year)"], rows_l)
    write(HERE / "literature_hits.tsv", ["label", "source", "pmid", "pmcid", "year", "journal", "title"], rows_t)


def cmd_run():
    net = Net()
    res = collect(net)
    with gzip.GzipFile(HERE / "collected.json.gz", "wb", mtime=0) as f:
        f.write(json.dumps(res, sort_keys=True).encode())
    write(HERE / "service_log.tsv", ["case", "attempt", "status", "seconds", "url"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"]] for l in net.log])
    write(HERE / "raw_hashes.tsv", ["url", "status", "sha256"], [[k, v[0], sha(v[1])] for k, v in sorted(net.raw.items())])
    tables(res)
    print("attempts", len(net.log), "ok", sum(1 for l in net.log if l["status"] == 200))


NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
PUBMED = {   # label -> PubMed query (title/abstract); counts and the first hits only; the cited abstracts are fetched by PMID with efetch
    "P01_nanatinostat": "(nanatinostat[tiab] OR CHR-3996[tiab] OR VRx-3996[tiab])",
    "P02_HDAC5_GLUT1": "HDAC5[tiab] AND (GLUT1[tiab] OR SLC2A1[tiab] OR \"glucose transporter\"[tiab])",
    "P03_WWOX_HDAC": "WWOX[tiab] AND (HDAC*[tiab] OR \"histone deacetylase\"[tiab])",
    "P04_KDM4C_HIF": "(KDM4C[tiab] OR JMJD2C[tiab]) AND (HIF1A[tiab] OR HIF-1[tiab] OR \"hypoxia-inducible\"[tiab])",
    "P05_IOX1_Hopkinson": "Hopkinson 5-Carboxy-8-hydroxyquinoline",
    "P06_CGI1746": "(CGI1746[tiab] OR \"CGI-1746\"[tiab])",
    "P07_STAT3_NPY": "STAT3[tiab] AND (NPY[tiab] OR \"neuropeptide Y\"[tiab])",
    "P08_BTK_STAT3": "BTK[tiab] AND STAT3[tiab] AND phosphorylation[tiab]",
    "P09_EZH2_IL6_glia": "EZH2[tiab] AND (IL6[tiab] OR \"interleukin-6\"[tiab]) AND (macrophage[tiab] OR microglia[tiab] OR astrocyte[tiab]) AND (inhibitor[tiab] OR deletion[tiab] OR knockdown[tiab])",
    "P10_GSK343_brain": "GSK343[tiab] AND (microglia[tiab] OR astrocyte[tiab] OR neuroinflammation[tiab] OR brain[tiab])",
    "P11_tizaterkib": "(tizaterkib[tiab] OR AZD0364[tiab] OR ASTX029[tiab])",
    "P12_Bcl3_TNF": "Bcl-3[tiab] AND (TNF[tiab] OR \"tumor necrosis factor\"[tiab]) AND (macrophage[tiab] OR LPS[tiab])",
    "P13_Bcl3_ERK": "Bcl-3[tiab] AND (ERK[tiab] OR MAPK[tiab]) AND phosphorylat*[tiab]",
    "P14_ERK_TNF_Tpl2": "Tpl2[tiab] AND ERK[tiab] AND TNF[tiab] AND (translation[tiab] OR transport[tiab] OR mRNA[tiab])",
    "P15_WWOX_glia_cytokine": "Wwox[tiab] AND (microglia[tiab] OR astrocyte*[tiab]) AND (cytokine*[tiab] OR TNF[tiab] OR IL-6[tiab])",
    "P16_WWOX_ERK_brain": "ERK[tiab] AND (Wwox[tiab] OR WWOX[tiab]) AND (neuron*[tiab] OR brain[tiab] OR hippocamp*[tiab])",
    "P17_SRT2104_brain": "(SRT2104[tiab] OR SRT-2104[tiab]) AND (brain[tiab] OR neuro*[tiab] OR Huntington[tiab] OR cerebr*[tiab])",
    "P18_SRT2104_clinical": "(SRT2104[tiab] OR SRT-2104[tiab]) AND (clinical[tiab] OR healthy[tiab] OR volunteers[tiab])",
    "P19_SIRT1_activators_direct": "pacholec[au] AND SIRT1[tiab]",
    "P20_SIRT1_MYC": "SIRT1[tiab] AND (MYC[tiab] OR c-Myc[tiab]) AND (deacetyl*[tiab] OR stability[tiab] OR degradation[tiab])",
    "P21_WWOX_SIRT1": "SIRT1[tiab] AND (Wwox[tiab] OR WWOX[tiab])",
    "P22_WWOX_MYC_neural": "WWOX[tiab] AND (Myc[tiab] OR MYC[tiab]) AND (neural[tiab] OR radial glia[tiab] OR organoid*[tiab])",
    "P23_WWOX_EZH2": "WWOX[tiab] AND (EZH2[tiab] OR PRC2[tiab] OR polycomb[tiab])",
    "P24_WWOX_BTK": "WWOX[tiab] AND (BTK[tiab] OR \"Bruton\"[tiab])",
}


def cmd_pubmed():
    """NCBI E-utilities esearch + esummary for the PUBMED queries (the Europe PMC route answered HTTP 503 to all 27 queries of `run` on 2026-11-03)."""
    net, rows, hits = Net(), [], []
    for k, q in PUBMED.items():
        st, d = net.get(NCBI + "esearch.fcgi", {"db": "pubmed", "term": q, "retmode": "json", "retmax": 8, "sort": "relevance"}, case=k)
        ids = d.get("esearchresult", {}).get("idlist", []) if st == 200 and isinstance(d, dict) else []
        cnt = d.get("esearchresult", {}).get("count") if st == 200 and isinstance(d, dict) else None
        titles = {}
        if ids:
            st2, s = net.get(NCBI + "esummary.fcgi", {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}, case=k)
            titles = s.get("result", {}) if st2 == 200 and isinstance(s, dict) else {}
        rows.append([k, q, st, cnt, ";".join(ids)])
        for i in ids:
            r = titles.get(i, {})
            hits.append([k, i, (r.get("pubdate") or "")[:4], r.get("source"), r.get("title")])
        time.sleep(0.4)
    write(HERE / "literature_pubmed_counts.tsv", ["label", "query", "http_status", "hit_count", "first_pmids"], rows)
    write(HERE / "literature_pubmed_hits.tsv", ["label", "pmid", "year", "journal", "title"], hits)
    write(HERE / "service_log_pubmed.tsv", ["case", "attempt", "status", "seconds", "url"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"]] for l in net.log])
    print("pubmed attempts", len(net.log), "ok", sum(1 for l in net.log if l["status"] == 200))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", choices=["run", "tables", "pubmed"])
    a = ap.parse_args()
    if a.cmd == "pubmed":
        cmd_pubmed()
    elif a.cmd == "run":
        cmd_run()
    elif a.cmd == "tables":
        with gzip.open(HERE / "collected.json.gz", "rt") as f:
            tables(json.load(f))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
