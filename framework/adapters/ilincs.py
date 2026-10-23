"""iLINCS — signature metadata from the LINCS libraries, filtered by library, compound, cell line,
dose or time. REST, key-less. Measured 2026-10-22. The reversal computation itself is NOT done
here: this adapter returns which signatures exist in which context, so a query declared elsewhere
(see gse156243/) can be run against an explicit universe. SigCom LINCS is the sibling surface.

Request: {"where": {"libraryid": "LIB_5", "compound": "..."}, "limit": 50}
Output hits: one per signature (signature id, library, compound, cell line, concentration, time).
No concordance value is returned by this adapter: it is a census of signatures, not a ranking.
"""
from __future__ import annotations

import json

from . import _http

INFO = {
    "name": "ilincs",
    "gives": "which LINCS signatures exist for a compound, cell line, dose and time (a census, not a concordance)",
    "network": "GET https://www.ilincs.org/api/SignatureMeta",
    "licence": "LINCS data terms (public); API key-less, no payment",
    "inputs": "where (dict of SignatureMeta field filters), limit (optional, default 50)",
    "outputs": "hits: signatures with context fields; source_version = UNKNOWN (service undated)",
    "licence_url": "https://www.ilincs.org/help/iLINCS-paper",
    "licence_read_on": "2026-10-23",
    "licence_terms": "'iLINCS is under Creative Commons (CC BY) license.' 'Use of iLINCS is free for everyone.' 'You are free to use the results of "
                     "iLINCS analysis as you see fit, as long as attribution is given by citing the iLINCS paper below.' No API rate limit stated. "
                     "Underlying LINCS signatures carry the LINCS consortium's public data terms.",
    "citation": "Pilarczyk M., Fazel-Najafabadi M., Kouril M., Shamsaei B. et al. Connecting omics signatures and revealing biological mechanisms "
                "with iLINCS. Nat Commun 2022;13:4678. https://doi.org/10.1038/s41467-022-32205-3 "
                "(requested 'within any publication that uses any methods or results inspired by iLINCS website or APIs')",
    "attribution": "Signature metadata from iLINCS (CC BY), https://www.ilincs.org",
}

URL = "https://www.ilincs.org/api/SignatureMeta"
FIELDS = ("signatureid", "libraryid", "compound", "lincspertid", "cellline", "tissue",
          "concentration", "time", "treatment", "perturbagenID")


def query(request: dict, fetch=_http.get_json) -> dict:
    where = request.get("where") or {}
    limit = int(request.get("limit", 50))
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence; "
                   "a signature absent from LINCS is not counterevidence", "error": ""}
    if not isinstance(where, dict) or not where:
        out["error"] = "where (a non-empty dict of filters) is required"
        return out
    params = {"filter": json.dumps({"where": where, "limit": limit})}
    out["requests_sent"].append(URL + "?filter=" + params["filter"])
    status, payload = fetch(URL, params=params)
    if status != 200 or not isinstance(payload, list):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    for row in payload:
        out["hits"].append({"kind": "signature", **{f: row.get(f) for f in FIELDS if f in row}})
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"where": {"libraryid": "LIB_5"}, "limit": 1},
    "response": (200, [{"signatureid": "LINCSCP_1", "libraryid": "LIB_5", "compound": "example", "cellline": "A375",
                        "concentration": "0.5uM", "time": "24 h", "lincspertid": "LSM-0"}]),
}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=(lambda u, params=None, body=None, timeout=20: SAMPLE["response"]) if fetch is None else fetch)
    ok = result["status"] == "MATCH_FOUND" and result["hits"] and "cellline" in result["hits"][0]
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
