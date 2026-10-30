#!/usr/bin/env python3
"""IT9 P4-part-1: the decisive acquisitions that IT8 P3 truncated or lacked. Reuses the IT8 P3 retry layer (pharm_qualify.Net) and adapter.

  qualify_p4a.py --help              this text, no network
  qualify_p4a.py run [--out DIR]     live: (1) LDHA complete (no truncation) and LDHB for every nanomolar human-LDHA inhibitor, same-document pairs,
                                     molecule identity; (2) the documents that hold the dichloroacetate PDK values, all rows, per isoform;
                                     (3) stiripentol, type-unfiltered; (4) bumetanide NKCC1 rows (re-read from the IT8 P3 store) and the label
  qualify_p4a.py rebuild [--out DIR] offline rebuild of the tables from collected.json.gz (deterministic)

Needs LEGEND_CATALOG_CACHE (GtoPdb cache). Standard library only. States are never merged: SERVICE_ERROR / NO_ROWS_UNDER_FILTERS / ROWS_RETRIEVED /
ROWS_RETRIEVED_TRUNCATED. UNKNOWN is a datum the sources do not hold, never a zero. A ratio is formed ONLY between two rows of the SAME document, the
same standard type and units, both relation '='; a censored row gives a bound and is labelled one. No IC50 is derived from single-concentration
percentages. Nothing here is medical advice."""
import argparse, collections, csv, gzip, hashlib, importlib.util, json, os, re, statistics, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
P3 = HERE.parent / "pharmacological_qualification_it8_p3_20261029"
RAW_LIMIT = 1_000_000
BASE = "https://www.ebi.ac.uk/chembl/api/data"
LDHA_T, LDHB_T = "CHEMBL4835", None   # LDHB resolved from accession P07195
DCA_DOCS = ["CHEMBL1131823", "CHEMBL1132309", "CHEMBL1133665", "CHEMBL1133733", "CHEMBL3813671", "CHEMBL4007440", "CHEMBL4177695", "CHEMBL4308888", "CHEMBL5346893", "CHEMBL5370584", "CHEMBL6121009"]
PDK_RX = re.compile(r"[Pp]yruvate dehydrogenase.*kinase|PDK|PDHK")


def pq():
    spec = importlib.util.spec_from_file_location("pharm_qualify", P3 / "pharm_qualify.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def num(r):
    try:
        return float(r["standard_value"])
    except (TypeError, ValueError, KeyError):
        return None


def rel(r):
    return {"=": "=", ">": ">", ">=": ">", "<": "<", "<=": "<"}.get(r.get("standard_relation") or "=", r.get("standard_relation") or "=")


def fmt(v):
    return "" if v is None else f"{v:g}"


def doc_rows(net, doc):
    """ALL activity rows of one ChEMBL document (any type), with assay context. Returns (state, total, rows)."""
    rows, off, total = [], 0, None
    while True:
        s, p = net.get(f"{BASE}/activity.json?document_chembl_id={doc}&limit=200&offset={off}")
        if s != 200 or not isinstance(p, dict):
            return "SERVICE_ERROR", total, rows
        total = (p.get("page_meta") or {}).get("total_count", total)
        page = p.get("activities") or []
        rows += page
        off += len(page)
        if not page or not (p.get("page_meta") or {}).get("next"):
            break
    assays, ids = {}, sorted({r["assay_chembl_id"] for r in rows if r.get("assay_chembl_id")})
    for i in range(0, len(ids), 40):
        s, p = net.get(f"{BASE}/assay.json?assay_chembl_id__in={','.join(ids[i:i+40])}&limit=100")
        if s == 200 and isinstance(p, dict):
            for a in p.get("assays") or []:
                assays[a["assay_chembl_id"]] = {k: a.get(k) for k in ("assay_organism", "assay_cell_type", "assay_type", "description")}
    out = [{k: r.get(k) for k in ("activity_id", "molecule_chembl_id", "molecule_pref_name", "standard_type", "standard_relation", "standard_value", "standard_units", "target_chembl_id",
                                  "target_pref_name", "target_organism", "assay_chembl_id", "assay_description", "document_chembl_id", "document_year")} | {"assay_context": assays.get(r.get("assay_chembl_id"))} for r in rows]
    return ("ROWS_RETRIEVED" if rows else "NO_ROWS_UNDER_FILTERS"), total, out


def collect(net, cache):
    from framework.adapters import chembl
    res = {"ldh": {}, "pdk": {}, "stiripentol": {}, "bumetanide": {}}
    # (1) LDHA complete, LDHB complete
    net.case = "LDHA"
    a = chembl.query({"target": LDHA_T, "types": ["IC50", "Ki", "Kd"], "max_rows": 2000}, fetch=net.get)
    res["ldh"]["ldha"] = {"state": pq_state(a), "total": a.get("total_count"), "retrieved": a.get("retrieved"), "truncated": a.get("truncated"), "error": a["error"], "rows": a["hits"]}
    net.case = "LDHB"
    t = chembl.query({"uniprot": "P07195"}, fetch=net.get)
    ldhb_ids = [h["target_chembl_id"] for h in t["hits"] if h.get("target_type") == "SINGLE PROTEIN" and h.get("organism") == "Homo sapiens"]
    b = {"state": "NO_ROWS_UNDER_FILTERS", "total": 0, "retrieved": 0, "truncated": False, "error": "", "rows": [], "targets": ldhb_ids}
    for tid in ldhb_ids:
        r = chembl.query({"target": tid, "types": ["IC50", "Ki", "Kd"], "max_rows": 2000}, fetch=net.get)
        b["rows"] += r["hits"]
        b["total"] += r.get("total_count") or 0
        b["retrieved"] += r.get("retrieved") or 0
        b["truncated"] = b["truncated"] or bool(r.get("truncated"))
        b["error"] = b["error"] or r["error"]
    b["state"] = pq_state({"error": b["error"], "hits": b["rows"], "truncated": b["truncated"]})
    res["ldh"]["ldhb"] = b
    # nanomolar human-LDHA set (same definition as IT8 P3: '=' value, nM, IC50/Ki/Kd, <= 100 nM)
    nm = sorted({r["molecule_chembl_id"] for r in a["hits"] if r.get("standard_units") == "nM" and rel(r) == "=" and num(r) is not None and num(r) <= 100})
    res["ldh"]["nm_set"] = nm
    net.case = "LDH-molecules"
    mols = {}
    for mid in nm:
        s, m = net.get(f"{BASE}/molecule/{mid}.json")
        if s == 200 and isinstance(m, dict):
            h = m.get("molecule_hierarchy") or {}
            mols[mid] = {"pref_name": m.get("pref_name"), "parent": h.get("parent_chembl_id"), "max_phase": m.get("max_phase"), "availability_type": m.get("availability_type"),
                         "first_approval": m.get("first_approval"), "molecule_type": m.get("molecule_type"), "chirality": m.get("chirality"), "withdrawn": m.get("withdrawn_flag"),
                         "inchikey": (m.get("molecule_structures") or {}).get("standard_inchi_key")}
        else:
            mols[mid] = {"state": "SERVICE_ERROR" if s != 404 else "NO_RECORD", "http": s}
    res["ldh"]["molecules"] = mols
    res["ldh"]["gtopdb"] = gtopdb_targets(cache, ("LDHA", "LDHB"))
    res["ldh"]["gtopdb_ligands"] = gtopdb_ligands(cache)
    # (2) PDK documents, all rows
    net.case = "PDK"
    for d in DCA_DOCS:
        st, tot, rows = doc_rows(net, d)
        res["pdk"][d] = {"state": st, "total": tot, "rows": [r for r in rows]}
    res["pdk_gtopdb"] = gtopdb_targets(cache, ("PDK1", "PDK2", "PDK3", "PDK4"))
    # named GtoPdb PDK inhibitors -> ChEMBL ids -> all rows on PDK targets, by document; document metadata for every document used
    lig = gtopdb_ligand_ids(cache, {r["ligand_id"] for r in res["pdk_gtopdb"]})   # name -> {chembl_id, inchikey}
    res["pdk_probe_ids"] = {}
    for nm_, e_ in lig.items():
        ids_ = [e_["chembl_id"]] if e_["chembl_id"] else []
        how = "GtoPdb ligand table ChEMBL ID" if ids_ else "none"
        if not ids_ and e_["inchikey"]:
            s3, p3 = net.get(f"{BASE}/molecule.json?molecule_structures__standard_inchi_key={e_['inchikey']}&limit=5")
            ids_ = [m["molecule_chembl_id"] for m in (p3.get("molecules") or [])] if s3 == 200 and isinstance(p3, dict) else []
            how = f"ChEMBL lookup by the full InChIKey of the GtoPdb ligand (HTTP {s3})"
        res["pdk_probe_ids"][nm_] = {"chembl_ids": ids_, "identity_method": how, "inchikey": e_["inchikey"]}
    probes = sorted({i for v in res["pdk_probe_ids"].values() for i in v["chembl_ids"]})
    res["pdk_probe_rows"] = {}
    for mid in probes:
        if not mid:
            continue
        st, tot, rows = doc_rows_by_molecule(net, mid)
        res["pdk_probe_rows"][mid] = {"state": st, "total": tot, "rows": [r for r in rows if PDK_RX.search(r.get("target_pref_name") or "")]}
    docs = sorted({r["document_chembl_id"] for e in res["pdk_probe_rows"].values() for r in e["rows"]} | set(DCA_DOCS) | {r["document_chembl_id"] for e in res["ldh"]["ldha"]["rows"][:0] for r in []})
    res["documents"] = {}
    for d in docs:
        s2, p2 = net.get(f"{BASE}/document/{d}.json")
        res["documents"][d] = ({k: p2.get(k) for k in ("title", "journal", "year", "doi", "pubmed_id")} if s2 == 200 and isinstance(p2, dict) else {"state": "SERVICE_ERROR" if s2 != 404 else "NO_RECORD"})
    # (3) stiripentol, type-unfiltered
    net.case = "stiripentol"
    st, tot, rows = doc_rows_by_molecule(net, "CHEMBL1983350")
    res["stiripentol"] = {"state": st, "total": tot, "rows": rows}
    # (4) bumetanide label
    net.case = "bumetanide"
    s, p = net.get("https://api.fda.gov/drug/label.json", params={"search": 'openfda.generic_name:"bumetanide"', "limit": 10})
    lab = {"http": s, "snippets": [], "n": 0}
    if s == 200 and isinstance(p, dict):
        labs = p.get("results") or []
        lab["n"] = len(labs)
        pick = labs[0]
        text = " ".join(pick.get("pharmacokinetics", []) + pick.get("clinical_pharmacology", []))
        lab["snippets"] = [x[:300] for x in re.split(r"(?<=[.;])\s+", text) if re.search(r"ng/mL|mcg/mL|µg/mL|peak|C ?max|binding|half-life", x, re.I)][:6]
        lab["effective_time"] = pick.get("effective_time")
        lab["product_type"] = (pick.get("openfda", {}).get("product_type") or ["UNKNOWN"])[0]
        lab["boxed_warning"] = bool(pick.get("boxed_warning"))
    res["bumetanide"]["label"] = lab
    ba = chembl.query({"molecule": "CHEMBL1072", "types": ["IC50", "Ki", "Kd", "EC50", "Kb", "Potency", "Inhibition"], "max_rows": 2000}, fetch=net.get)
    res["bumetanide"]["state"] = pq_state(ba)
    res["bumetanide"]["slc12"] = [r for r in ba["hits"] if re.search(r"Solute carrier family 12|NKCC|Na-K-Cl|cotransport", r.get("target_pref_name") or "")]
    return res


def pq_state(r):
    if r.get("error"):
        return "SERVICE_ERROR"
    if not r.get("hits"):
        return "NO_ROWS_UNDER_FILTERS"
    return "ROWS_RETRIEVED_TRUNCATED" if r.get("truncated") else "ROWS_RETRIEVED"


def doc_rows_by_molecule(net, mid):
    rows, off, total = [], 0, None
    while True:
        s, p = net.get(f"{BASE}/activity.json?molecule_chembl_id={mid}&limit=200&offset={off}")
        if s != 200 or not isinstance(p, dict):
            return "SERVICE_ERROR", total, rows
        total = (p.get("page_meta") or {}).get("total_count", total)
        page = p.get("activities") or []
        rows += [{k: r.get(k) for k in ("molecule_chembl_id", "standard_type", "standard_relation", "standard_value", "standard_units", "target_pref_name", "target_organism",
                                         "assay_chembl_id", "assay_description", "document_chembl_id", "document_year", "type", "value", "units")} for r in page]
        off += len(page)
        if not page or not (p.get("page_meta") or {}).get("next"):
            break
    return ("ROWS_RETRIEVED_TRUNCATED" if total is not None and len(rows) < total else "ROWS_RETRIEVED"), total, rows


def gtopdb_targets(cache, genes):
    p = Path(cache) / "gtopdb" / "interactions.csv"
    out = []
    with open(p, newline="", encoding="utf-8") as f:
        f.readline()
        for r in csv.DictReader(f):
            if r["Target Gene Symbol"] in genes:
                out.append({"gene": r["Target Gene Symbol"], "ligand": r["Ligand"], "ligand_id": r["Ligand ID"], "species": r["Target Species"], "action": r["Action"], "units": r["Affinity Units"],
                            "median": r["Affinity Median"][:6], "nM": r["Original Affinity Median nm"], "relation": r["Original Affinity Relation"], "pmid": r["PubMed ID"], "assay": r["Assay Description"][:120]})
    return out


def gtopdb_ligand_ids(cache, ids):
    p = Path(cache) / "gtopdb" / "ligands.csv"
    out = {}
    with open(p, newline="", encoding="utf-8") as f:
        f.readline()
        for r in csv.DictReader(f):
            if r["Ligand ID"] in ids:
                out[r["Name"]] = {"chembl_id": r["ChEMBL ID"], "inchikey": r["InChIKey"]}
    return out


def gtopdb_ligands(cache):
    p = Path(cache) / "gtopdb" / "ligands.csv"
    out = {}
    with open(p, newline="", encoding="utf-8") as f:
        f.readline()
        for r in csv.DictReader(f):
            if r["ChEMBL ID"]:
                out[r["ChEMBL ID"]] = {"gtopdb_id": r["Ligand ID"], "name": r["Name"], "approved": r["Approved"], "type": r["Type"]}
    return out


# ---------------------------------------------------------------------------------------------------------------- tables
def pairs_and_selectivity(ldh):
    a_rows, b_rows = ldh["ldha"]["rows"], ldh["ldhb"]["rows"]
    A = collections.defaultdict(list)
    B = collections.defaultdict(list)
    for r in a_rows:
        A[r["molecule_chembl_id"]].append(r)
    for r in b_rows:
        B[r["molecule_chembl_id"]].append(r)
    pairs, sel = [], []
    for mid in ldh["nm_set"]:
        mol = ldh["molecules"].get(mid, {})
        gt = ldh["gtopdb_ligands"].get(mid, {})
        nm_a = sorted(num(r) for r in A[mid] if r.get("standard_units") == "nM" and rel(r) == "=" and num(r) is not None)
        ldhb_any = B.get(mid, [])
        n_pair = 0
        same_doc_ratios = []
        docs_a = {r["document_chembl_id"] for r in A[mid]}
        for d in sorted(docs_a):
            for ra in [r for r in A[mid] if r["document_chembl_id"] == d]:
                for rb in [r for r in B.get(mid, []) if r["document_chembl_id"] == d]:
                    if ra["standard_type"] != rb["standard_type"] or ra.get("standard_units") != rb.get("standard_units") or ra.get("standard_units") != "nM":
                        continue
                    va, vb = num(ra), num(rb)
                    if va is None or vb is None:
                        continue
                    ra_rel, rb_rel = rel(ra), rel(rb)
                    if ra_rel == "=" and rb_rel == "=":
                        kind, ratio = "ratio_equals", vb / va
                        same_doc_ratios.append(ratio)
                    elif ra_rel == "=" and rb_rel == ">":
                        kind, ratio = "lower_bound_ratio (LDHB censored)", vb / va
                    else:
                        kind, ratio = "not_formed (LDHA censored or other relation)", None
                    n_pair += 1
                    pairs.append([mid, mol.get("pref_name") or "", d, ra["standard_type"], ra_rel, fmt(va), rb_rel, fmt(vb), kind, fmt(ratio),
                                  (ra.get("assay_description") or "")[:110], (rb.get("assay_description") or "")[:110]])
        sel.append([mid, mol.get("pref_name") or "", mol.get("parent") or "", "parent" if mol.get("parent") == mid else "child/salt-or-other-record", mol.get("max_phase"),
                    mol.get("availability_type"), mol.get("first_approval") or "", gt.get("gtopdb_id", ""), gt.get("approved", ""),
                    fmt(nm_a[0]) if nm_a else "", len(A[mid]), len(ldhb_any), n_pair, ";".join(fmt(x) for x in same_doc_ratios[:4]),
                    "same-document LDHA/LDHB pair" if n_pair else ("LDHB rows only in other documents" if ldhb_any else "no LDHB row in ChEMBL (UNKNOWN, not non-selective)")])
    return pairs, sel


PAIR_HEAD = ["molecule_chembl_id", "pref_name", "document", "type", "ldha_relation", "ldha_nM", "ldhb_relation", "ldhb_nM", "ratio_kind", "ldhb_over_ldha", "ldha_assay", "ldhb_assay"]
SEL_HEAD = ["molecule_chembl_id", "pref_name", "parent_chembl_id", "record_role", "max_phase", "chembl_availability_type", "first_approval", "gtopdb_ligand_id", "gtopdb_approved",
            "ldha_best_nM_equals", "n_ldha_rows", "n_ldhb_rows", "n_same_document_pairs", "same_document_ldhb_over_ldha_equals", "reading"]


def pdk_table(pdk):
    rows = []
    for d, e in sorted(pdk.items()):
        for r in e["rows"]:
            if PDK_RX.search(r.get("target_pref_name") or "") and r.get("standard_type") in ("IC50", "EC50", "Ki", "Kd", "Inhibition"):
                c = r.get("assay_context") or {}
                iso = re.search(r"isozyme (\d)", r.get("target_pref_name") or "")
                rows.append([d, r.get("document_year"), r["molecule_chembl_id"], r.get("molecule_pref_name") or "", "PDK" + iso.group(1) if iso else "PDK?", r["standard_type"], rel(r), fmt(num(r)),
                             r.get("standard_units") or "", r.get("target_organism") or "", c.get("assay_organism") or "NA", c.get("assay_type") or "NA", (r.get("assay_description") or "")[:150]])
    rows.sort(key=lambda x: (x[0], x[2], x[4], x[5], x[6], x[7]))
    return rows


PDK_HEAD = ["document", "year", "molecule_chembl_id", "pref_name", "isoform", "type", "relation", "value", "units", "target_organism", "assay_organism", "assay_type", "assay_description"]


def pdk_matched(pdk):
    """Within one document: dichloroacetate vs every other molecule, per isoform, both '=' nM IC50 only."""
    out = []
    DCA = {"CHEMBL13960", "CHEMBL306823"}
    for d, e in sorted(pdk.items()):
        rows = [r for r in e["rows"] if PDK_RX.search(r.get("target_pref_name") or "") and r.get("standard_type") == "IC50" and r.get("standard_units") == "nM" and num(r) is not None]
        by = collections.defaultdict(list)
        for r in rows:
            iso = re.search(r"isozyme (\d)", r.get("target_pref_name") or "")
            by[(iso.group(1) if iso else "?", r["molecule_chembl_id"])].append(r)
        isos = sorted({k[0] for k in by})
        for iso in isos:
            dca = [r for k, v in by.items() if k[0] == iso and k[1] in DCA for r in v]
            if not dca:
                continue
            for (i2, mid), v in sorted(by.items()):
                if i2 != iso or mid in DCA:
                    continue
                for ra in dca:
                    for rb in v:
                        if rel(ra) == "=" and rel(rb) == "=":
                            kind, ratio = "ratio_equals", num(ra) / num(rb)
                        elif rel(ra) == ">" and rel(rb) == "=":
                            kind, ratio = "lower_bound_ratio (DCA censored)", num(ra) / num(rb)
                        else:
                            continue
                        out.append([d, "PDK" + iso, mid, rb.get("molecule_pref_name") or "", fmt(num(rb)), rel(ra), fmt(num(ra)), kind, fmt(ratio),
                                    (rb.get("assay_description") or "")[:110]])
    return out


MATCH_HEAD = ["document", "isoform", "molecule_chembl_id", "pref_name", "inhibitor_IC50_nM", "dca_relation", "dca_IC50_nM", "ratio_kind", "dca_over_inhibitor", "inhibitor_assay"]


def stir_summary(s):
    cnt = collections.Counter(r["standard_type"] for r in s["rows"])
    ldh = [r for r in s["rows"] if re.search(r"LDH|lactate dehydrogenase", r.get("assay_description") or "", re.I)]
    return cnt, ldh


def build(res, out, stamp):
    pairs, sel = pairs_and_selectivity(res["ldh"])
    wr(out / "ldha_ldhb_pairs.tsv", PAIR_HEAD, pairs)
    wr(out / "ldha_nanomolar_selectivity.tsv", SEL_HEAD, sel)
    wr(out / "pdk_documents.tsv", PDK_HEAD, pdk_table(res["pdk"]))
    wr(out / "pdk_matched_to_dca.tsv", MATCH_HEAD, pdk_matched(res["pdk"]))
    keyrows = []
    for mid in ("CHEMBL3335794", "CHEMBL3335792", "CHEMBL3359440"):
        for tag, src in (("LDHA", res["ldh"]["ldha"]["rows"]), ("LDHB", res["ldh"]["ldhb"]["rows"])):
            for r in src:
                if r["molecule_chembl_id"] == mid:
                    c = r.get("assay_context") or {}
                    keyrows.append([mid, tag, r["document_chembl_id"], r["standard_type"], rel(r), fmt(num(r)), r.get("standard_units") or "", c.get("assay_organism") or "NA", (r.get("assay_description") or "")[:120]])
    keyrows.sort()
    wr(out / "ldh_key_compounds_rows.tsv", ["molecule_chembl_id", "isoform_target", "document", "type", "relation", "value", "units", "assay_organism", "assay_description"], keyrows)
    pr = []
    for mid, e in sorted(res["pdk_probe_rows"].items()):
        for r in e["rows"]:
            iso = re.search(r"isozyme (\d)", r.get("target_pref_name") or "")
            pr.append([mid, r["document_chembl_id"], r.get("document_year"), "PDK" + iso.group(1) if iso else "PDK?", r["standard_type"], rel(r), fmt(num(r)), r.get("standard_units") or "",
                       r.get("target_organism") or "", (r.get("assay_description") or "")[:150]])
    pr.sort(key=lambda x: (x[0], x[1], x[3], x[4], x[5], x[6]))
    wr(out / "pdk_named_probe_rows.tsv", ["molecule_chembl_id", "document", "year", "isoform", "type", "relation", "value", "units", "target_organism", "assay_description"], pr)
    wr(out / "documents_used.tsv", ["document", "year", "journal", "doi", "pubmed_id", "title"],
       [[d, v.get("year", ""), v.get("journal", ""), v.get("doi", ""), v.get("pubmed_id", ""), (v.get("title") or v.get("state") or "")[:140]] for d, v in sorted(res["documents"].items())])
    bt = []
    for r in res["bumetanide"]["slc12"]:
        c = r.get("assay_context") or {}
        bt.append([r["target_pref_name"], r["target_organism"], r["standard_type"], rel(r), fmt(num(r)), r.get("standard_units") or "", c.get("assay_organism") or "NA", c.get("assay_cell_type") or "NA",
                   r["document_chembl_id"], (r.get("assay_description") or "")[:160]])
    wr(out / "bumetanide_nkcc_rows.tsv", ["target", "target_organism", "type", "relation", "value", "units", "assay_organism", "assay_cell_type", "document", "assay_description"], bt)
    # arithmetic (assumptions stated in the row text; NOT a prediction for any human or mouse exposure)
    ic = sorted(num(r) for r in res["bumetanide"]["slc12"] if r["standard_type"] == "IC50" and rel(r) == "=" and r.get("standard_units") == "nM" and num(r) is not None)
    ar = []
    for lo_hi, ic50 in (("NKCC1 IC50 ChEMBL HT-29 cells", ic[0] / 1000 if ic else None), ("NKCC1 IC50 GtoPdb pIC50 5.6 (human, PMID 11882915)", 10 ** (9 - 5.6) / 1000)):
        if ic50 is None:
            continue
        for fu in (0.06, 0.17):
            tot = ic50 / fu
            ar.append([lo_hi, f"{ic50:.2f}", f"{fu:g}", f"{tot:.1f}", f"{tot / 0.02:.0f}", f"{tot / 0.015:.0f}"])
    wr(out / "bumetanide_exposure_arithmetic.tsv", ["nkcc1_ic50_source", "free_brain_target_uM", "fraction_unbound_in_brain (PMID 33279441 abstract: 6-17 percent for the 3 drugs)",
                                                    "total_brain_uM = free / fu", "total_plasma_uM if brain:plasma = 0.02 (PMID 25449033, mouse, total/total)", "total_plasma_uM if brain:plasma = 0.015"], ar)
    cnt, ldh = stir_summary(res["stiripentol"])
    rows = [[t, n] for t, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))]
    wr(out / "stiripentol_types.tsv", ["standard_type", "n_rows"], rows)
    wr(out / "stiripentol_ldh_rows.tsv", ["type", "relation", "value", "units", "document", "target", "assay_description"],
       [[r["standard_type"], rel(r), r["standard_value"] if r["standard_value"] is not None else "", r["standard_units"] or "", r["document_chembl_id"], r["target_pref_name"] or "", (r["assay_description"] or "")[:200]] for r in ldh])
    return {"n_nm": len(res["ldh"]["nm_set"]), "n_pairs": len(pairs), "n_sel": len(sel), "n_stir": len(res["stiripentol"]["rows"])}


def wr(path, head, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([re.sub(r"[\t\r\n]+", " ", str(c)) for c in r])


def cmd_run(out):
    cache = os.environ.get("LEGEND_CATALOG_CACHE", "")
    if not cache:
        sys.exit("set LEGEND_CATALOG_CACHE")
    m = pq()
    net = m.Net()
    res = collect(net, cache)
    stamp = time.strftime("%Y-%m-%d", time.gmtime())
    hashes = [[k[:170], m.sha(net.raw[k]), len(json.dumps(net.raw[k]))] for k in sorted(net.raw)]
    for rp in ("gtopdb/interactions.csv", "gtopdb/ligands.csv"):
        pth = Path(cache) / rp
        hashes.append([f"cache:{rp}", hashlib.sha256(pth.read_bytes()).hexdigest(), pth.stat().st_size])
    wr(out / "raw_hashes.tsv", ["item", "sha256", "bytes"], hashes)
    wr(out / "service_log.tsv", ["case", "attempt", "status", "seconds", "url", "error"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]] for l in net.log])
    raw_gz = gzip.compress(json.dumps({"retrieved_on": stamp, "responses": net.raw}, sort_keys=True).encode(), mtime=0)
    (out / "raw_store.json.gz").unlink(missing_ok=True)
    if len(raw_gz) < RAW_LIMIT:
        (out / "raw_store.json.gz").write_bytes(raw_gz)
    col = gzip.compress(json.dumps({"retrieved_on": stamp, "collected": res}, sort_keys=True).encode(), mtime=0)
    (out / "collected.json.gz").unlink(missing_ok=True)
    kept = len(col) < RAW_LIMIT
    if kept:
        (out / "collected.json.gz").write_bytes(col)
    n = build(res, out, stamp)
    summ = {"retrieved_on": stamp, "raw_gz_bytes": len(raw_gz), "raw_kept": len(raw_gz) < RAW_LIMIT, "collected_gz_bytes": len(col), "collected_kept": kept, "attempts": len(net.log),
            "non200_attempts": sum(1 for l in net.log if l["status"] not in (200, 404)),
            "ldha": {k: res["ldh"]["ldha"][k] for k in ("state", "total", "retrieved", "truncated")}, "ldhb": {k: res["ldh"]["ldhb"][k] for k in ("state", "total", "retrieved", "truncated", "targets")},
            "stiripentol": {"state": res["stiripentol"]["state"], "total": res["stiripentol"]["total"], "rows": len(res["stiripentol"]["rows"])},
            "pdk_docs": {d: {"state": e["state"], "total": e["total"]} for d, e in res["pdk"].items()}, "bumetanide_label": res["bumetanide"]["label"], **n}
    (out / "run_summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n")
    print(json.dumps(summ)[:1500])


def cmd_rebuild(out):
    p = out / "collected.json.gz"
    if not p.exists():
        sys.exit("collected.json.gz not kept (>= 1 MB): rebuild needs a live run; compare raw_hashes.tsv")
    d = json.loads(gzip.decompress(p.read_bytes()))
    print(build(d["collected"], out, d["retrieved_on"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rebuild"])
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    {"run": cmd_run, "rebuild": cmd_rebuild}[a.cmd](Path(a.out))


if __name__ == "__main__":
    main()
