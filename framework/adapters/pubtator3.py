"""PubTator 3 — literature relations for one gene (optionally one relation type), with the
publication count per pair. REST, key-less, NCBI public domain. Measured 2026-10-22.

Request: {"gene": "WWOX", "type": "treat"}   (type optional; the index's own vocabulary)
Output hits: one per relation (type, source entity, target entity, publications count). A count is
a census of the index, not evidence; zero relations of a type is NO_MATCH_FOUND, never absence.
NCBI asks for at most 3 requests per second unkeyed; this adapter makes one per query.
"""
from __future__ import annotations

from . import _http

INFO = {
    "name": "pubtator3",
    "gives": "pre-computed gene-chemical-disease-variant relations over PubMed and PMC-OA with publication counts",
    "network": "GET https://www.ncbi.nlm.nih.gov/research/pubtator3-api/relations",
    "licence": "NCBI public domain; key-less, no payment; 3 req/s limit",
    "inputs": "gene (symbol, required), type (optional relation type)",
    "outputs": "hits: relations with publications count; source_version = UNKNOWN (service undated)",
    "licence_url": "https://www.ncbi.nlm.nih.gov/home/about/policies/",
    "licence_read_on": "2026-10-23",
    "licence_terms": "NCBI policies: 'Information that is created by or for the US government on this site is within the public domain'; "
                     "NLM asks for acknowledgment when reused; 'Make no more than 3 requests every 1 second'; large series on weekends or "
                     "overnight US Eastern; the government 'does not warrant or assume any legal liability or responsibility for the accuracy'. "
                     "The PubTator3 web pages themselves render no terms text (measured 2026-10-23, three pages); the policy above is NCBI-wide. "
                     "This adapter sends one request per query and names itself in the User-Agent; no e-mail is sent (none may be recorded here).",
    "citation": "Wei C-H. et al. PubTator 3.0: an AI-powered literature resource for unlocking biomedical knowledge. "
                "Nucleic Acids Res 2024;52(W1):W540-W546. https://doi.org/10.1093/nar/gkae235",
    "attribution": "Relations from PubTator 3 (NCBI/NLM/NIH), public domain, https://www.ncbi.nlm.nih.gov/research/pubtator3/",
}

URL = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/relations"


def query(request: dict, fetch=_http.get_json) -> dict:
    gene = str(request.get("gene", "")).strip()
    rtype = str(request.get("type", "")).strip()
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}
    if not gene:
        out["error"] = "gene is required"
        return out
    params = {"e1": f"@GENE_{gene}"}
    if rtype:
        params["type"] = rtype
    out["requests_sent"].append(URL + "?" + "&".join(f"{k}={v}" for k, v in params.items()))
    status, payload = fetch(URL, params=params)
    if status != 200 or not isinstance(payload, list):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    for row in payload:
        out["hits"].append({"kind": "relation", "type": row.get("type"), "source": row.get("source"),
                            "target": row.get("target"), "publications": row.get("publications")})
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"gene": "WWOX"},
    "response": (200, [{"type": "inhibit", "source": "@DISEASE_Neoplasms", "target": "@GENE_WWOX", "publications": 219}]),
    "empty_request": {"gene": "WWOX", "type": "treat"},
    "empty_response": (200, []),
}


def selftest(fetch=None) -> dict:
    if fetch is None:
        hit = query(SAMPLE["request"], fetch=lambda u, params=None, body=None, timeout=20: SAMPLE["response"])
        empty = query(SAMPLE["empty_request"], fetch=lambda u, params=None, body=None, timeout=20: SAMPLE["empty_response"])
    else:
        hit = query(SAMPLE["request"], fetch=fetch)
        empty = query(SAMPLE["empty_request"], fetch=fetch)
    ok = hit["status"] == "MATCH_FOUND" and empty["status"] == "NO_MATCH_FOUND" and "never absence" in empty["note"]
    return {"ok": bool(ok), "status": hit["status"], "hits": len(hit["hits"]),
            "empty_status": empty["status"], "source_version": hit["source_version"], "error": hit["error"] or empty["error"]}
