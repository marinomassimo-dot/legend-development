"""Open Targets Platform — target-disease associations, tractability, drug and clinical
candidates for one target. GraphQL, key-less, data CC0. Measured 2026-10-22 against API 26.9.0.

Request: {"ensembl_id": "ENSG00000186153", "size": 25}
Output hits: one per associated disease (id, name, evidence datatypes WITHOUT the score), plus one
`target_summary` hit with tractability flags and the drug/clinical candidate count. The association
score is dropped on purpose: the module emits no score.
"""
from __future__ import annotations

from . import _http

INFO = {
    "name": "opentargets",
    "gives": "target-disease associations by evidence type, tractability buckets, "
             "drug and clinical candidates per target",
    "network": "POST https://api.platform.opentargets.org/api/v4/graphql",
    "licence": "data CC0; API key-less, no payment",
    "inputs": "ensembl_id (required), size (optional, default 25)",
    "outputs": "hits: associated diseases (no score) + target_summary; source_version = apiVersion/dataVersion",
    "licence_url": "https://platform-docs.opentargets.org/licence",
    "licence_read_on": "2026-10-23",
    "licence_terms": "Data: 'Open Targets Platform is marked with CC0 1.0' (public domain dedication). "
                     "API and code: Apache License 2.0. No rate limit stated; questions to the Open Targets Community. "
                     "Individual upstream sources carry their own licences (CC BY 4.0, CC BY-SA 3.0) and 'have agreed to unrestricted use by Open Targets users'.",
    "citation": "Buniello A. et al. Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. "
                "Nucleic Acids Research 2025;53(D1):D1467-D1475. https://doi.org/10.1093/nar/gkae1128 "
                "(the page asks: 'If you use our code and/or our data, please cite our latest publication')",
    "attribution": "Data from the Open Targets Platform (CC0 1.0), https://platform.opentargets.org",
}

URL = "https://api.platform.opentargets.org/api/v4/graphql"
QUERY = """query ($id: String!, $size: Int!) {
  meta { apiVersion { x y z } dataVersion { year month } }
  target(ensemblId: $id) {
    id approvedSymbol
    tractability { label modality value }
    drugAndClinicalCandidates { count }
    associatedDiseases(page: {size: $size, index: 0}) {
      count rows { disease { id name } datatypeScores { id } }
    }
  }
}"""


def query(request: dict, fetch=_http.get_json) -> dict:
    ensembl_id = str(request.get("ensembl_id", "")).strip()
    size = int(request.get("size", 25))
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [URL], "status": "QUERY_ERROR", "hits": [], "source_version": "UNKNOWN",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence", "error": ""}
    if not ensembl_id:
        out["error"] = "ensembl_id is required"
        return out
    status, payload = fetch(URL, body={"query": QUERY, "variables": {"id": ensembl_id, "size": size}})
    if status != 200 or not isinstance(payload, dict) or payload.get("errors"):
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    data = payload.get("data") or {}
    meta = data.get("meta") or {}
    api = meta.get("apiVersion") or {}
    dv = meta.get("dataVersion") or {}
    out["source_version"] = (f"api {api.get('x')}.{api.get('y')}.{api.get('z')} "
                             f"data {dv.get('year')}.{dv.get('month')}")
    target = data.get("target")
    if not target:
        out["status"] = "NO_MATCH_FOUND"
        return out
    assoc = target.get("associatedDiseases") or {}
    for row in assoc.get("rows") or []:
        out["hits"].append({"kind": "associated_disease", "disease_id": row["disease"]["id"],
                            "disease_name": row["disease"]["name"],
                            "evidence_datatypes": [d["id"] for d in row.get("datatypeScores") or []]})
    out["hits"].append({"kind": "target_summary", "target_id": target.get("id"),
                        "symbol": target.get("approvedSymbol"),
                        "associated_diseases_total": assoc.get("count"),
                        "drug_and_clinical_candidates": (target.get("drugAndClinicalCandidates") or {}).get("count"),
                        "tractability_true": [f"{t['modality']}:{t['label']}" for t in target.get("tractability") or [] if t.get("value")]})
    out["status"] = "MATCH_FOUND" if assoc.get("rows") else "NO_MATCH_FOUND"
    return out


SAMPLE = {
    "request": {"ensembl_id": "ENSG00000186153", "size": 2},
    "response": (200, {"data": {"meta": {"apiVersion": {"x": "26", "y": "9", "z": "0"},
                                         "dataVersion": {"year": "26", "month": "09"}},
                                "target": {"id": "ENSG00000186153", "approvedSymbol": "WWOX",
                                           "tractability": [{"label": "GO CC high conf", "modality": "AB", "value": True},
                                                            {"label": "Approved Drug", "modality": "SM", "value": False}],
                                           "drugAndClinicalCandidates": {"count": 0},
                                           "associatedDiseases": {"count": 2012, "rows": [
                                               {"disease": {"id": "MONDO_0014288", "name": "developmental and epileptic encephalopathy, 28"},
                                                "datatypeScores": [{"id": "genetic_association"}, {"id": "literature"}]}]}}}}),
}


def selftest(fetch=None) -> dict:
    canned = (lambda url, params=None, body=None, timeout=20: SAMPLE["response"]) if fetch is None else fetch
    result = query(SAMPLE["request"], fetch=canned)
    ok = (result["status"] == "MATCH_FOUND" and result["hits"] and "score" not in str(result["hits"][0])
          and any(h["kind"] == "target_summary" for h in result["hits"]))
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
