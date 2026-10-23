"""Orphadata — ORPHAcode cross-referencing for one disorder name or gene-named disorder.
REST, key-less, CC BY 4.0 (the licence is returned inside the payload). Measured 2026-10-22.

Request: {"name": "WWOX"}
Output hits: one per disorder found (ORPHAcode, preferred term, external references by source).
This is nosology: a code is not a precedent, and NO_MATCH_FOUND is never absence of a disorder.
"""
from __future__ import annotations

from . import _http

INFO = {
    "name": "orphadata",
    "gives": "ORPHAcodes, preferred terms and ICD/OMIM/MONDO cross-references for rare disorders",
    "network": "GET https://api.orphadata.com/rd-cross-referencing/orphacodes/names/{name}",
    "licence": "CC BY 4.0; key-less, no payment",
    "inputs": "name (disorder name or gene-named disorder, required)",
    "outputs": "hits: disorders with external references; source_version = payload Date",
    "licence_url": "https://www.orphadata.com/legal-notice/ and https://sciences.orphadata.com/ ; the API payload's own __licence field",
    "licence_read_on": "2026-10-23",
    "licence_terms": "The API response declares '__licence: CC-BY-4.0' in every payload (measured 2026-10-22 and 2026-10-23); Orphadata Science: "
                     "'All files are available under the Commons Attribution 4.0 International (CC BY 4.0) licence'. The legal notice adds for CC BY 4.0 data: "
                     "cite the provenance, 'You must indicate if you have made changes to the data', and 'Any use of our data distributed under the CC BY 4.0 "
                     "licence in LLM/AI-based tools/services' must state that Orphanet/Orphadata data was used; Orphanet is not responsible for outputs built on it. "
                     "Orphadata Products (bulk services) are under a Data Transfer Agreement and are NOT used here. Logos need prior approval and are not used.",
    "citation": "Orphanet: an online rare disease and orphan drug data base. © INSERM 1999. Available on https://www.orpha.net. "
                "Accessed (date in retrieved_at). Data via Orphadata, https://www.orphadata.com, data version as in source_version",
    "attribution": "This output uses Orphanet/Orphadata data (© INSERM 1999, CC BY 4.0) in an AI-assisted research tool; "
                   "the data are copied unchanged and Orphanet is not responsible for this tool's outputs",
}

BASE = "https://api.orphadata.com/rd-cross-referencing/orphacodes/names/"


def _refs(block) -> list[dict]:
    refs = []
    for ref in block or []:
        if isinstance(ref, dict):
            refs.append({"source": ref.get("Source"), "reference": ref.get("Reference"),
                         "relation": ref.get("DisorderMappingRelation")})
    return refs


def query(request: dict, fetch=_http.get_json) -> dict:
    name = str(request.get("name", "")).strip()
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}
    if not name:
        out["error"] = "name is required"
        return out
    url = BASE + name
    out["requests_sent"].append(url)
    status, payload = fetch(url)
    if status == 404:
        out["status"] = "NO_MATCH_FOUND"
        return out
    if status != 200 or not isinstance(payload, dict):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    data = payload.get("data") or {}
    results = data.get("results")
    rows = results if isinstance(results, list) else ([results] if isinstance(results, dict) else [])
    for row in rows:
        out["hits"].append({"kind": "disorder", "orphacode": row.get("ORPHAcode"),
                            "preferred_term": row.get("Preferred term"), "group": row.get("DisorderGroup"),
                            "type": row.get("DisorderType"), "external_references": _refs(row.get("ExternalReference")),
                            "licence": (data.get("__licence") or {}).get("identifier")})
        if row.get("Date"):
            out["source_version"] = str(row.get("Date"))
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"name": "WWOX"},
    "response": (200, {"data": {"__count": 1, "__licence": {"identifier": "CC-BY-4.0"},
                                "results": {"Date": "2026-06-23 07:53:50", "ORPHAcode": 0, "Preferred term": "example disorder",
                                            "DisorderGroup": "Disorder", "DisorderType": "Disease",
                                            "ExternalReference": [{"Source": "OMIM", "Reference": "000000", "DisorderMappingRelation": "E"}]}}}),
}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=(lambda u, params=None, body=None, timeout=20: SAMPLE["response"]) if fetch is None else fetch)
    ok = result["status"] == "MATCH_FOUND" and result["hits"] and result["hits"][0].get("licence") in ("CC-BY-4.0", None)
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
