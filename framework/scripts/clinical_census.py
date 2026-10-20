#!/usr/bin/env python3
"""Read-only clinical census against the public ClinicalTrials.gov API v2.

🔴 WHAT THIS TOOL IS, AND WHAT IT IS NOT
----------------------------------------
It asks the public registry a fixed list of queries, one query at a time, and records what
came back: the query itself, the date, every page, the path of the original response, and the
records keyed by identifier with the synonym that found each one. It is a **retrieval record**,
never evidence and never a scientific claim.

Four states exist and are never merged:

  ``MATCH``                at least one record was returned for that query
  ``NO_MATCH``             the query ran, completed its pagination, and returned zero records
  ``QUERY_ERROR``          the query did not complete (transport, HTTP, decode or shape)
  ``COVERAGE_INCOMPLETE``  the query ran but the census of it is partial — pagination was
                           truncated, or the registry's own ``totalCount`` exceeds what was
                           collected

``NO_MATCH`` is an answer about **this query against this registry on this date**. It is not
evidence that no study exists: a study may be unregistered, registered under wording none of
these synonyms reaches, or registered after this run. Equally, an identifier proves
registration and nothing else — not authorisation, not recruitment, not a first dose. Those
events are distinct and the ones this tool cannot see stay ``UNKNOWN`` in whatever record
cites it.

🔴 NO PRE-FILTERING
-------------------
No phase filter, no masking/placebo filter, no status filter, no recruiting-only filter is
ever sent, and none is applied to the response. A rare-disease first-in-human study is
typically phase 1 or 1–2 and open-label — exactly what the 2022 ``spectrum-drug-tracker``
snapshot discarded in code (``_external_repos/MANIFEST.md``), which is why that route is not
a WOREE trial source and this one exists.

Network: one or more key-less HTTPS GETs to ``clinicaltrials.gov``. Zero spend, no account,
no service, standard library only, and nothing is ever sent but the public query terms below.

Usage:
  python3 framework/scripts/clinical_census.py --out <census.json> [--raw-dir <dir>]
  python3 framework/scripts/clinical_census.py --list-queries
  python3 framework/scripts/clinical_census.py --query WOREE --query WWOX --out <census.json>

Exit: 0 every query terminal (MATCH/NO_MATCH) · 1 at least one QUERY_ERROR ·
      3 no QUERY_ERROR but at least one COVERAGE_INCOMPLETE · 2 usage
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCHEMA_VERSION = 2
TOOL_VERSION = "clinical_census/1.0.0"
API = "https://clinicaltrials.gov/api/v2/studies"
# Above this many bytes an original response is stored gzipped (see write_original_response).
GZIP_OVER = 1_000_000
API_REFERENCE = "https://www.nlm.nih.gov/pubs/techbull/ma24/ma24_clinicaltrials_api.html"
REGISTRY_OWNER = "NLM/NIH ClinicalTrials.gov — not an FDA archive"

# The seven queries the WOREE census fixes. Each runs SEPARATELY: an OR-joined expression
# would lose which wording found which record, and the synonym that found a record is part
# of the record's provenance.
DEFAULT_QUERIES: tuple[dict[str, str], ...] = (
    {"label": "WOREE", "field": "query.term", "value": "WOREE"},
    {"label": "WWOX-related epileptic encephalopathy", "field": "query.term",
     "value": "WWOX-related epileptic encephalopathy"},
    {"label": "EIEE28", "field": "query.term", "value": "EIEE28"},
    {"label": "DEE28", "field": "query.term", "value": "DEE28"},
    {"label": "WWOX", "field": "query.term", "value": "WWOX"},
    {"label": "MZ-9138", "field": "query.term", "value": "MZ-9138"},
    # The sponsor of CIRM award CLIN1-14825 (MZ-9138, AAV9 gene therapy for WOREE), queried
    # through the sponsor field rather than free text so a sponsor hit is distinguishable
    # from an incidental mention of the company's name.
    {"label": "sponsor:Mahzi Therapeutics", "field": "query.spons",
     "value": "Mahzi Therapeutics"},
)

# A request may carry ONLY these keys. The guard is mechanical because the defect it prevents
# is a quiet one: a filter added for convenience silently narrows a census.
ALLOWED_PARAMETERS = frozenset({"query.term", "query.spons", "query.intr", "query.cond",
                                "pageSize", "pageToken", "countTotal", "format"})
FORBIDDEN_PREFIXES = ("filter.", "aggFilters", "postFilter")


class CensusError(RuntimeError):
    """A query did not complete. Distinct from a query that completed with zero records."""


def http_get_json(url: str, timeout: int = 60) -> dict:
    """One key-less GET. Raises CensusError for every failure mode, never returns partial."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:  # pragma: no cover - network shape
        raise CensusError(f"HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, OSError) as exc:  # pragma: no cover - network shape
        raise CensusError(f"transport failure for {url}: {exc}") from exc
    try:
        decoded = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CensusError(f"undecodable response for {url}: {exc}") from exc
    if not isinstance(decoded, dict) or not isinstance(decoded.get("studies"), list):
        raise CensusError(f"response for {url} carries no studies list")
    return decoded


def build_url(query: dict[str, str], page_size: int, page_token: str | None) -> str:
    parameters: dict[str, str] = {query["field"]: query["value"],
                                  "pageSize": str(page_size),
                                  "countTotal": "true",
                                  "format": "json"}
    if page_token:
        parameters["pageToken"] = page_token
    for key in parameters:
        if key.startswith(FORBIDDEN_PREFIXES) or key not in ALLOWED_PARAMETERS:
            raise CensusError(f"refused: {key} would pre-filter the census")
    return f"{API}?{urllib.parse.urlencode(parameters)}"


def summarise_study(study: dict) -> dict:
    """The fields a census card needs. The ORIGINAL response is kept on disk regardless."""
    protocol = study.get("protocolSection") or {}
    identification = protocol.get("identificationModule") or {}
    status = protocol.get("statusModule") or {}
    design = protocol.get("designModule") or {}
    sponsor = (protocol.get("sponsorCollaboratorsModule") or {}).get("leadSponsor") or {}
    conditions = (protocol.get("conditionsModule") or {}).get("conditions") or []
    return {
        "nct_id": identification.get("nctId"),
        "brief_title": identification.get("briefTitle"),
        "overall_status": status.get("overallStatus"),
        "phases": design.get("phases") or [],
        "study_type": design.get("studyType"),
        "conditions": conditions,
        "lead_sponsor": sponsor.get("name"),
        "study_first_post_date": (status.get("studyFirstPostDateStruct") or {}).get("date"),
        "start_date": (status.get("startDateStruct") or {}).get("date"),
        "last_update_post_date": (status.get("lastUpdatePostDateStruct") or {}).get("date"),
    }


REDACTED = "[REDACTED_CONTACT]"
# Key fragments whose VALUES are personal contact details of trial staff. The registry serves
# them in the clear; this repository is public material and `scripts/public_release_gate.py`
# blocks a non-placeholder e-mail address anywhere in it — correctly. So the stored response is
# the registry's document with these values replaced, declared as redacted wherever its path is
# recorded, never passed off as byte-faithful. Nothing scientific is removed: identifier,
# title, status, phase, design, conditions, sponsor, outcomes and dates all survive untouched.
CONTACT_KEY_FRAGMENTS = ("email", "phone", "fax")


def redact_personal_contacts(payload):
    """Replace personal contact values, returning (document, redaction count)."""
    if isinstance(payload, dict):
        redacted: dict = {}
        count = 0
        for key, value in payload.items():
            if (isinstance(key, str)
                    and any(fragment in key.lower() for fragment in CONTACT_KEY_FRAGMENTS)
                    and isinstance(value, str)):
                redacted[key] = REDACTED
                count += 1
                continue
            redacted[key], nested = redact_personal_contacts(value)
            count += nested
        return redacted, count
    if isinstance(payload, list):
        items = []
        count = 0
        for value in payload:
            item, nested = redact_personal_contacts(value)
            items.append(item)
            count += nested
        return items, count
    return payload, 0


def write_original_response(raw_dir: Path, label: str, page: int, payload: dict, *,
                            gzip_over: int = GZIP_OVER) -> tuple[str, int]:
    """Persist one page's original response and return the path recorded in the census.

    A response above ``gzip_over`` bytes is stored gzipped — the broad ``WWOX`` free-text
    query alone returns ~4.8 MB of registry records, and a provenance artefact that is too
    heavy to keep is a provenance artefact that gets deleted. The path recorded is always
    the path actually written, extension included.

    Personal contact values are redacted before the bytes land (see CONTACT_KEY_FRAGMENTS)
    and the count is returned beside the path, so no record can present the stored file as a
    byte-faithful copy of what the registry served.
    """
    raw_dir.mkdir(parents=True, exist_ok=True)
    safe = "".join(character if character.isalnum() else "_" for character in label)
    document, redactions = redact_personal_contacts(payload)
    body = json.dumps(document, indent=2, sort_keys=True).encode("utf-8")
    if len(body) > gzip_over:
        target = raw_dir / f"{safe}_page{page}.json.gz"
        with gzip.GzipFile(filename="", mode="wb", fileobj=target.open("wb"), mtime=0) as out:
            out.write(body)
    else:
        target = raw_dir / f"{safe}_page{page}.json"
        target.write_bytes(body)
    return str(target), redactions


def run_query(query: dict[str, str], *, page_size: int, max_pages: int,
              raw_dir: Path | None, fetch=http_get_json,
              gzip_over: int = GZIP_OVER) -> dict:
    """Run one query to exhaustion or to an EXPLICIT truncation. Never raises."""
    pages: list[dict] = []
    studies: list[dict] = []
    total_count: int | None = None
    token: str | None = None
    state = "NO_MATCH"
    error: str | None = None
    truncated = False
    for index in range(max_pages):
        url: str | None = None
        try:
            url = build_url(query, page_size, token)
            payload = fetch(url)
        except CensusError as exc:
            state, error = "QUERY_ERROR", str(exc)
            pages.append({"index": index, "url": url, "state": "QUERY_ERROR",
                          "error": str(exc)})
            break
        raw_path: str | None = None
        redactions = 0
        if raw_dir is not None:
            raw_path, redactions = write_original_response(
                raw_dir, query["label"], index + 1, payload, gzip_over=gzip_over)
        returned = payload.get("studies") or []
        if isinstance(payload.get("totalCount"), int):
            total_count = payload["totalCount"]
        pages.append({"index": index, "url": url, "state": "OK",
                      "returned": len(returned), "original_response_path": raw_path,
                      "original_response_contact_redactions": redactions,
                      "original_response_is_contact_redacted": raw_path is not None,
                      "next_page_token": payload.get("nextPageToken")})
        studies.extend(summarise_study(study) for study in returned)
        token = payload.get("nextPageToken")
        if not token:
            break
    else:
        truncated = bool(token)
    if state != "QUERY_ERROR":
        if truncated:
            state = "COVERAGE_INCOMPLETE"
        elif total_count is not None and total_count > len(studies):
            state = "COVERAGE_INCOMPLETE"
        elif studies:
            state = "MATCH"
        else:
            state = "NO_MATCH"
    return {
        "synonym": query["label"],
        "parameters": {query["field"]: query["value"], "pageSize": page_size,
                       "countTotal": True},
        "state": state,
        "error": error,
        "registry_total_count": total_count,
        "collected": len(studies),
        "truncated": truncated,
        "pages": pages,
        "studies": studies,
        "pre_filtered_by_phase_or_masking": False,
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }


def deduplicate(queries: list[dict]) -> dict[str, dict]:
    """One entry per identifier; every synonym that reached it is kept, in query order."""
    records: dict[str, dict] = {}
    for result in queries:
        for study in result["studies"]:
            identifier = study.get("nct_id") or f"UNIDENTIFIED::{result['synonym']}"
            existing = records.get(identifier)
            if existing is None:
                records[identifier] = dict(study, found_by_synonyms=[result["synonym"]])
            elif result["synonym"] not in existing["found_by_synonyms"]:
                existing["found_by_synonyms"].append(result["synonym"])
    return records


def run_census(queries: list[dict[str, str]], *, page_size: int = 100, max_pages: int = 20,
               raw_dir: Path | None = None, fetch=http_get_json,
               gzip_over: int = GZIP_OVER) -> dict:
    results = [run_query(query, page_size=page_size, max_pages=max_pages, raw_dir=raw_dir,
                         fetch=fetch, gzip_over=gzip_over) for query in queries]
    states = {result["synonym"]: result["state"] for result in results}
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_VERSION,
        "registry": {"endpoint": API, "api_version": "v2", "owner": REGISTRY_OWNER,
                     "reference": API_REFERENCE, "authentication": "none"},
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "epistemic_status": "RETRIEVAL_RECORD",
        "pre_filters_applied": [],
        "queries": results,
        "states_by_query": states,
        "records": deduplicate(results),
        "interpretation_limits": [
            "NO_MATCH means this query returned zero records on this date; it does not "
            "establish that no study exists.",
            "COVERAGE_INCOMPLETE is not NO_MATCH: part of the answer was not retrieved.",
            "An identifier evidences registration only — not sponsor authorisation, not "
            "public regulatory confirmation, not enrolment, not a first dose.",
            "Programme active, sponsor-declared authorisation, public regulatory "
            "confirmation, registration, enrolment and first dose are distinct events; the "
            "ones this retrieval cannot observe stay UNKNOWN.",
            "No scientific claim follows from this file, and nothing in it is DATO.",
            "Stored original responses have personal contact values (e-mail, phone, fax) "
            "replaced by [REDACTED_CONTACT]; every scientific field is untouched, and the "
            "count of replacements is recorded with each page.",
        ],
    }


def verdict(census: dict) -> int:
    states = set(census["states_by_query"].values())
    if "QUERY_ERROR" in states:
        return 1
    if "COVERAGE_INCOMPLETE" in states:
        return 3
    return 0


def main(argv: list[str] | None = None, fetch=http_get_json) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", help="write the census JSON here (default: stdout)")
    parser.add_argument("--raw-dir", help="directory for the original responses; their paths "
                                          "are recorded in the census")
    parser.add_argument("--query", action="append", default=[],
                        help="replace the default query set with these free-text terms")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=20,
                        help="pagination ceiling; reaching it yields COVERAGE_INCOMPLETE, "
                             "never a silent truncation")
    parser.add_argument("--list-queries", action="store_true",
                        help="print the default query set and exit without any network call")
    arguments = parser.parse_args(argv)

    if arguments.page_size < 1 or arguments.max_pages < 1:
        parser.error("--page-size and --max-pages must be positive")
    if arguments.list_queries:
        for query in DEFAULT_QUERIES:
            print(f"{query['label']}\t{query['field']}={query['value']}")
        return 0

    queries = ([{"label": term, "field": "query.term", "value": term}
                for term in arguments.query] or list(DEFAULT_QUERIES))
    census = run_census(queries, page_size=arguments.page_size, max_pages=arguments.max_pages,
                        raw_dir=Path(arguments.raw_dir) if arguments.raw_dir else None,
                        fetch=fetch)
    serialised = json.dumps(census, indent=2, sort_keys=True)
    if arguments.out:
        Path(arguments.out).write_text(serialised + "\n", encoding="utf-8")
        for result in census["queries"]:
            print(f"{result['state']}\t{result['synonym']}\t"
                  f"{result['collected']} collected\t"
                  f"registry total {result['registry_total_count']}")
        print(f"# {len(census['records'])} distinct identifiers -> {arguments.out}")
    else:
        print(serialised)
    return verdict(census)


if __name__ == "__main__":
    raise SystemExit(main())
