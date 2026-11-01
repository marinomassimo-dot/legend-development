"""DrugCentral — drug-target rows with the ORIGIN of each action label (MOA_SOURCE, else ACT_SOURCE).
Bulk TSV download, key-less, CC BY-SA 4.0. Measured 2026-11-01 (IT18 P3).

Why it exists: ChEMBL and GtoPdb share literature, so their agreement on a compound's action direction
is not independent. DrugCentral rows say where an action label came from (CHEMBL, IUPHAR, DRUG LABEL,
SCIENTIFIC LITERATURE, KEGG DRUG, ...); rows whose origin is neither ChEMBL nor IUPHAR are a third,
differently curated direction. Measured value and limits:
disease-models/wwox/research/drug_repurposing/capability_it18_p3_20261101/README.md.

Request: {"chembl_id": "CHEMBL709"}  (identity through the UniChem ChEMBL->DrugCentral map)
         {"struct_id": "403"}        (declared DrugCentral identity; the UniChem map misses some structs)
         {"gene": "CACNA1G"}         (target-first: rows whose GENE field names the symbol)
Output hits: one per DrugCentral row, fields verbatim, plus action_origin and action_origin_class
(SHARED = CHEMBL or IUPHAR; INDEPENDENT = DRUG LABEL, SCIENTIFIC LITERATURE, KEGG DRUG, EXPERT CURATOR;
OTHER). A different curation origin is not proof of truth.
"""
from __future__ import annotations

import csv
import gzip
import io
import urllib.error
import urllib.request

from . import _http

INFO = {
    "name": "drugcentral",
    "gives": "drug-target rows with action type and the origin of the action label (a third direction source beside ChEMBL and GtoPdb)",
    "network": "GET https://unmtid-dbs.net/download/DrugCentral/2027/drug.target.interaction.tsv.gz ; "
               "GET https://ftp.ebi.ac.uk/pub/databases/chembl/UniChem/data/wholeSourceMapping/src_id1/src1src34.txt.gz (chembl_id requests only)",
    "licence": "CC BY-SA 4.0 (DrugCentral); UniChem map under EMBL-EBI Terms of Use; key-less, no payment",
    "inputs": "one of chembl_id, struct_id, gene",
    "outputs": "hits: DrugCentral rows verbatim plus action_origin, action_origin_class; source_version = download directory",
    "licence_url": "https://drugcentral.org/privacy",
    "licence_read_on": "2026-11-01",
    "licence_terms": "'DrugCentral is available under Creative Commons license, download and use of this resource evidences your agreement to all "
                     "the terms and conditions of license.' The link is the CC BY-SA 4.0 legal code: attribution, indicate changes, share-alike "
                     "on any redistributed derived table. Rows whose ACT_SOURCE is WOMBAT-PK carry no separate terms on the page. The UniChem "
                     "whole-source map is used under the EMBL-EBI Terms of Use (https://www.ebi.ac.uk/about/terms-of-use), as in the catalogue.",
    "citation": "DrugCentral, https://drugcentral.org ; 'Citing DrugCentral' links https://doi.org/10.1093/nar/gkac1085 (About page) and "
                "https://doi.org/10.1093/nar/gkw993 (licence page), read 2026-11-01",
    "attribution": "Drug-target action labels from DrugCentral (University of New Mexico), CC BY-SA 4.0, https://drugcentral.org; "
                   "rows copied unchanged, origin class added by LEGEND",
}

TSV_URL = "https://unmtid-dbs.net/download/DrugCentral/2027/drug.target.interaction.tsv.gz"
MAP_URL = "https://ftp.ebi.ac.uk/pub/databases/chembl/UniChem/data/wholeSourceMapping/src_id1/src1src34.txt.gz"
SHARED = {"CHEMBL", "IUPHAR"}
INDEPENDENT = {"DRUG LABEL", "SCIENTIFIC LITERATURE", "KEGG DRUG", "EXPERT CURATOR"}


def get_bytes(url, params=None, body=None, timeout=60.0):
    """Same signature as _http.get_json, but returns the raw body (these are gzip files)."""
    req = urllib.request.Request(url, headers={"User-Agent": _http.USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as exc:
        return exc.code, (exc.read() if exc.fp else b"").decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        return 0, f"{type(exc).__name__}: {exc}"


def _text(payload):
    if isinstance(payload, bytes):
        return gzip.decompress(payload).decode("utf-8") if payload[:2] == b"\x1f\x8b" else payload.decode("utf-8")
    return payload if isinstance(payload, str) else None


def origin_class(origin: str) -> str:
    return "SHARED" if origin in SHARED else "INDEPENDENT" if origin in INDEPENDENT else "OTHER"


def query(request: dict, fetch=get_bytes) -> dict:
    if fetch is _http.get_json:  # the CLI's live self-test passes the JSON door; these files are gzip bytes
        fetch = get_bytes
    out = {"adapter": INFO["name"], "retrieved_at": _http.now_utc(), "request": dict(request),
           "requests_sent": [], "status": "QUERY_ERROR", "hits": [], "source_version": "DrugCentral download directory 2027",
           "evidence_label": "NOT WWOX EVIDENCE", "licence": INFO["licence"], "citation": INFO["citation"],
           "note": "NO_MATCH_FOUND is an answer about this query on this date, never absence; a ChEMBL id absent from the UniChem map "
                   "may still be in DrugCentral (try struct_id); an INDEPENDENT origin is a different curation, not proof", "error": ""}
    chembl = str(request.get("chembl_id", "")).strip().upper()
    structs = {str(request.get("struct_id", "")).strip()} - {""}
    gene = str(request.get("gene", "")).strip().upper()
    if not (chembl or structs or gene):
        out["error"] = "one of chembl_id, struct_id, gene is required"
        return out
    if chembl:
        out["requests_sent"].append(MAP_URL)
        status, payload = fetch(MAP_URL)
        text = _text(payload) if status == 200 else None
        if text is None:
            out["error"] = f"HTTP {status}: {str(payload)[:300]}"
            return out
        lines = text.splitlines()[1:]
        structs |= {p[1].strip() for p in (ln.split("\t") for ln in lines) if len(p) == 2 and p[0].strip() == chembl}
        out["identity_basis"] = "unichem_src1src34" if structs else "chembl_id not in the UniChem map"
        if not structs:
            out["status"] = "NO_MATCH_FOUND"
            return out
    out["requests_sent"].append(TSV_URL)
    status, payload = fetch(TSV_URL)
    text = _text(payload) if status == 200 else None
    if text is None:
        out["error"] = f"HTTP {status}: {str(payload)[:300]}"
        return out
    rows = csv.DictReader(io.StringIO(text), delimiter="\t")
    if not rows.fieldnames or "STRUCT_ID" not in rows.fieldnames or "ACTION_TYPE" not in rows.fieldnames:
        out["error"] = "payload is not the DrugCentral drug.target.interaction table"
        return out
    for row in rows:
        if structs and row["STRUCT_ID"].strip() not in structs:
            continue
        if gene and gene not in {g.strip().upper() for g in (row.get("GENE") or "").split("|")}:
            continue
        origin = (row.get("MOA_SOURCE") or "").strip() or (row.get("ACT_SOURCE") or "").strip() or "UNKNOWN"
        out["hits"].append({"kind": "drug_target_row", **row, "action_origin": origin, "action_origin_class": origin_class(origin)})
    out["status"] = "MATCH_FOUND" if out["hits"] else "NO_MATCH_FOUND"
    return out


_SAMPLE_TSV = ('"DRUG_NAME"\t"STRUCT_ID"\t"TARGET_NAME"\t"TARGET_CLASS"\t"ACCESSION"\t"GENE"\t"SWISSPROT"\t"ACT_VALUE"\t"ACT_UNIT"\t"ACT_TYPE"\t'
               '"ACT_COMMENT"\t"ACT_SOURCE"\t"RELATION"\t"MOA"\t"MOA_SOURCE"\t"ACT_SOURCE_URL"\t"MOA_SOURCE_URL"\t"ACTION_TYPE"\t"TDL"\t"ORGANISM"\n'
               '"example"\t403\t"Example receptor"\t"GPCR"\t"P00000"\t"EXMPL"\t"EXMPL_HUMAN"\t8.0\t\t"Ki"\t\t"SCIENTIFIC LITERATURE"\t"="\t1\t'
               '"DRUG LABEL"\t\t\t"ANTAGONIST"\t"Tclin"\t"Homo sapiens"\n')

SAMPLE = {"request": {"struct_id": "403"}, "response": (200, gzip.compress(_SAMPLE_TSV.encode("utf-8"), mtime=0))}


def selftest(fetch=None) -> dict:
    result = query(SAMPLE["request"], fetch=(lambda u, params=None, body=None, timeout=60: SAMPLE["response"]) if fetch is None else fetch)
    ok = result["status"] == "MATCH_FOUND" and result["hits"] and all("action_origin_class" in h for h in result["hits"])
    if fetch is None:
        ok = ok and result["hits"][0]["action_origin"] == "DRUG LABEL" and result["hits"][0]["action_origin_class"] == "INDEPENDENT"
    return {"ok": bool(ok), "status": result["status"], "hits": len(result["hits"]),
            "source_version": result["source_version"], "error": result["error"]}
