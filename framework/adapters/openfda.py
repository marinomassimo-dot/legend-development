"""openFDA — the SPL label sections for one drug (generic name) and the FAERS reaction counts
reported with it. REST, key-less (an optional key only raises the rate limit and is NOT used),
US public domain. Measured 2026-10-22. DailyMed is the documented fallback for labels.

Request: {"drug": "sodium phenylbutyrate", "sections": ["indications_and_usage", ...], "faers_limit": 10}
Output hits: one `label` hit per SPL (sections requested, verbatim text, truncated at 2000 chars
each, with the SPL set id) and one `faers_counts` hit. A FAERS count is a count of spontaneous
reports — never a rate, never a causal signal. HTTP 404 from openFDA means no match for the query:
NO_MATCH_FOUND, never absence of a label.
"""
from __future__ import annotations

from . import _http

INFO = {
    "name": "openfda",
    "gives": "SPL label sections (indications, contraindications, pediatric use, interactions) and "
             "FAERS spontaneous-report reaction counts per drug",
    "network": "GET https://api.fda.gov/drug/label.json and /drug/event.json",
    "licence": "US public domain (CC0); key-less, no payment (optional key not used)",
    "inputs": "drug (generic name, required), sections (optional list), faers_limit (optional)",
    "outputs": "hits: label per SPL + faers_counts; source_version = meta.last_updated",
    "licence_url": "https://open.fda.gov/terms/ and https://open.fda.gov/apis/authentication/",
    "licence_read_on": "2026-10-23",
    "licence_terms": "'made available with a Creative Commons CC0 1.0 Universal dedication'; works where CC0 does not apply 'will be clearly marked'; "
                     "attribution requested, not required: 'we ask that proper credit be given' with the text 'Data provided by the U.S. Food and Drug Administration'; "
                     "'FDA makes no warranty that openFDA data will be error free'; every payload carries 'Do not rely on openFDA to make decisions regarding medical care'. "
                     "Rate limits without a key: 240 requests per minute and 1,000 per day per IP (with a key 120,000 per day; no key is used).",
    "citation": "Data provided by the U.S. Food and Drug Administration (openFDA), https://open.fda.gov — the credit line the terms page asks for",
    "attribution": "Data provided by the U.S. Food and Drug Administration",
}

LABEL = "https://api.fda.gov/drug/label.json"
EVENT = "https://api.fda.gov/drug/event.json"
DEFAULT_SECTIONS = ("indications_and_usage", "contraindications", "warnings", "pediatric_use",
                    "drug_interactions", "mechanism_of_action")


def query(request: dict, fetch=_http.get_json) -> dict:
    drug = str(request.get("drug", "")).strip()
    sections = list(request.get("sections") or DEFAULT_SECTIONS)
    faers_limit = int(request.get("faers_limit", 10))
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence; "
                   "FAERS counts are spontaneous reports, never a rate; openFDA: do not rely on it for medical care decisions", "error": ""}
    if not drug:
        out["error"] = "drug is required"
        return out
    params = {"search": f'openfda.generic_name:"{drug}"', "limit": 3}
    out["requests_sent"].append(LABEL + "?" + str(params))
    status, payload = fetch(LABEL, params=params)
    if status == 404:
        out["status"] = "NO_MATCH_FOUND"
    elif status != 200 or not isinstance(payload, dict):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    else:
        out["source_version"] = f"label last_updated {(payload.get('meta') or {}).get('last_updated')}"
        for spl in payload.get("results") or []:
            hit = {"kind": "label", "set_id": spl.get("set_id"), "effective_time": spl.get("effective_time"),
                   "brand_name": (spl.get("openfda") or {}).get("brand_name"),
                   "generic_name": (spl.get("openfda") or {}).get("generic_name"), "sections": {}}
            for name in sections:
                value = spl.get(name)
                if value:
                    text = " ".join(value) if isinstance(value, list) else str(value)
                    hit["sections"][name] = text[:2000]
            out["hits"].append(hit)
        out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    params = {"search": f'patient.drug.medicinalproduct:"{drug}"',
              "count": "patient.reaction.reactionmeddrapt.exact", "limit": faers_limit}
    out["requests_sent"].append(EVENT + "?" + str(params))
    status, payload = fetch(EVENT, params=params)
    if status == 200 and isinstance(payload, dict):
        out["hits"].append({"kind": "faers_counts", "reports_by_reaction": payload.get("results") or [],
                            "caveat": "spontaneous reports; not a rate, not causal"})
    elif status == 404:
        out["hits"].append({"kind": "faers_counts", "reports_by_reaction": [], "caveat": "NO_MATCH for this product string"})
    else:
        out["hits"].append({"kind": "faers_counts", "reports_by_reaction": [], "caveat": f"QUERY_ERROR HTTP {status}"})
    return out


SAMPLE = {
    "request": {"drug": "sodium phenylbutyrate", "sections": ["indications_and_usage", "pediatric_use"], "faers_limit": 2},
    "responses": {
        LABEL: (200, {"meta": {"last_updated": "2026-10-15"},
                      "results": [{"set_id": "example-set", "effective_time": "20250101",
                                   "openfda": {"brand_name": ["EXAMPLE"], "generic_name": ["SODIUM PHENYLBUTYRATE"]},
                                   "indications_and_usage": ["1 INDICATIONS AND USAGE ..."],
                                   "pediatric_use": ["8.4 Pediatric Use ..."]}]}),
        EVENT: (200, {"results": [{"term": "DIARRHOEA", "count": 26}, {"term": "DEATH", "count": 25}]}),
    },
    "missing_request": {"drug": "amlexanox"},
    "missing_responses": {LABEL: (404, {"error": {"code": "NOT_FOUND"}}), EVENT: (404, {"error": {"code": "NOT_FOUND"}})},
}


def selftest(fetch=None) -> dict:
    if fetch is None:
        hit = query(SAMPLE["request"], fetch=lambda u, params=None, body=None, timeout=20: SAMPLE["responses"][u])
        missing = query(SAMPLE["missing_request"], fetch=lambda u, params=None, body=None, timeout=20: SAMPLE["missing_responses"][u])
    else:
        hit = query(SAMPLE["request"], fetch=fetch)
        missing = query(SAMPLE["missing_request"], fetch=fetch)
    ok = (hit["status"] == "MATCH_FOUND" and any(h["kind"] == "label" for h in hit["hits"])
          and missing["status"] == "NO_MATCH_FOUND" and not missing["error"])
    return {"ok": bool(ok), "status": hit["status"], "hits": len(hit["hits"]), "missing_status": missing["status"],
            "source_version": hit["source_version"], "error": hit["error"] or missing["error"]}
