"""ChEMBL — mechanism of action and target components for one drug name, or the targets
ChEMBL knows for one gene symbol. REST, key-less, CC BY-SA 3.0. Measured 2026-10-22 (ChEMBL_37).

Request: {"drug": "bortezomib"}  or  {"gene": "WWOX"}
Output hits: one per mechanism (action_type, mechanism_of_action, target_chembl_id, references)
or one per target found. `max_phase` is carried as the source states it (a development stage,
not a score).
"""
from __future__ import annotations

from urllib.parse import quote

from . import _http

INFO = {
    "name": "chembl",
    "gives": "curated mechanism of action per drug with its reference; ChEMBL targets per gene",
    "network": "GET https://www.ebi.ac.uk/chembl/api/data/{status,molecule/search,mechanism,target/search}.json",
    "licence": "CC BY-SA 3.0; key-less, no payment",
    "inputs": "drug (name) or gene (symbol); one of the two",
    "outputs": "hits: mechanisms or targets; source_version = chembl_db_version",
    "licence_url": "https://chembl.gitbook.io/chembl-interface-documentation/about (Data Licensing) and "
                   "https://www.ebi.ac.uk/about/terms-of-use",
    "licence_read_on": "2026-10-23",
    "licence_terms": "'The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License' "
                     "(share-alike: an adaptation of the data is redistributed under the same licence; this module copies "
                     "fields verbatim and does not redistribute a derived database). Web services under the EMBL-EBI terms of use: "
                     "'EMBL-EBI expects attribution'; no numeric rate limit, use must not prevent service to others. "
                     "Calculated compound properties come from commercial software and carry their own terms (not consumed here).",
    "citation": "Zdrazil B. et al. The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity "
                "data types and time periods. Nucleic Acids Res 2024;52(D1):D1180-D1192. https://doi.org/10.1093/nar/gkad1004; "
                "web services: Davies M. et al. 2015 (Nucleic Acids Res 43:W612)",
    "attribution": "Data from ChEMBL (EMBL-EBI), CC BY-SA 3.0, https://www.ebi.ac.uk/chembl/",
}

BASE = "https://www.ebi.ac.uk/chembl/api/data"


def _new(request: dict) -> dict:
    return {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
            "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
            "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
            "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}


def query(request: dict, fetch=_http.get_json) -> dict:
    out = _new(request)
    drug = str(request.get("drug", "")).strip()
    gene = str(request.get("gene", "")).strip()
    if not drug and not gene:
        out["error"] = "drug or gene is required"
        return out
    url = f"{BASE}/status.json"
    out["requests_sent"].append(url)
    status, payload = fetch(url)
    if status == 200 and isinstance(payload, dict):
        out["source_version"] = f"{payload.get('chembl_db_version')} {payload.get('chembl_release_date')}"
    if gene:
        url = f"{BASE}/target/search.json?q={quote(gene)}&limit=20"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        for t in payload.get("targets") or []:
            out["hits"].append({"kind": "target", "target_chembl_id": t.get("target_chembl_id"),
                                "pref_name": t.get("pref_name"), "organism": t.get("organism"),
                                "target_type": t.get("target_type")})
        out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
        return out
    url = f"{BASE}/molecule/search.json?q={quote(drug)}&limit=5"  # a name with spaces is a valid query
    out["requests_sent"].append(url)
    status, payload = fetch(url)
    if status != 200 or not isinstance(payload, dict):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    molecules = payload.get("molecules") or []
    if not molecules:
        out["status"] = "NO_MATCH_FOUND"
        return out
    for mol in molecules[:1]:
        mid = mol.get("molecule_chembl_id")
        url = f"{BASE}/mechanism.json?molecule_chembl_id={mid}&limit=20"
        out["requests_sent"].append(url)
        status, payload = fetch(url)
        if status != 200 or not isinstance(payload, dict):
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        for m in payload.get("mechanisms") or []:
            out["hits"].append({"kind": "mechanism", "molecule_chembl_id": mid,
                                "pref_name": mol.get("pref_name"), "max_phase": mol.get("max_phase"),
                                "action_type": m.get("action_type"),
                                "mechanism_of_action": m.get("mechanism_of_action"),
                                "target_chembl_id": m.get("target_chembl_id"),
                                "references": [f"{r.get('ref_type')}:{r.get('ref_id')}" for r in m.get("mechanism_refs") or []]})
        if not out["hits"]:
            out["hits"].append({"kind": "molecule_without_mechanism", "molecule_chembl_id": mid,
                                "pref_name": mol.get("pref_name"), "max_phase": mol.get("max_phase")})
    out["status"] = "MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"drug": "bortezomib"},
    "responses": {
        "status.json": (200, {"chembl_db_version": "ChEMBL_37", "chembl_release_date": "2026-05-01"}),
        "molecule/search": (200, {"molecules": [{"molecule_chembl_id": "CHEMBL325041", "pref_name": "BORTEZOMIB", "max_phase": 4.0}]}),
        "mechanism.json": (200, {"mechanisms": [{"action_type": "INHIBITOR", "mechanism_of_action": "26S proteasome inhibitor",
                                                 "target_chembl_id": "CHEMBL2364701",
                                                 "mechanism_refs": [{"ref_type": "DailyMed", "ref_id": "setid=example"}]}]}),
    },
}


def _canned(url, params=None, body=None, timeout=20):
    for key, value in SAMPLE["responses"].items():
        if key in url:
            return value
    return 404, {}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=_canned if fetch is None else fetch)
    ok = result["status"] == "MATCH_FOUND" and any(h.get("kind") == "mechanism" for h in result["hits"])
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
