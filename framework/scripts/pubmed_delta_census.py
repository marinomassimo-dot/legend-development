#!/usr/bin/env python3
"""Print the PubMed WWOX records that no disease-model file mentions, by PMID, DOI or title.

Why this exists
---------------
The weekly harness scout had no PubMed delta step: a record that appeared on PubMed could stay
unseen by the repository until someone happened to search. This tool is that step: it reads, it
compares, it prints. It is a small weekly check, not a claim that a corpus is missing.

🔴 Correction recorded 2026-11-24. The first run of this idea used a query that included
`WOX1[Title/Abstract]` and reported 39 to 44 absent records. Most were not WWOX at all: `WOX1`
is also the name of plant WUSCHEL-related homeobox genes (37 of 40 in that run). With the
WWOX-only term PubMed returned 708 records on 2026-11-24, 700 registered and 7 never
registered, plus one *false absent*: a preprint registered by DOI before its PMID existed. So
the standing term is WWOX-only, WOX1 is a separate probe, and the comparison is not by PMID
alone.

What it is, and what it is not
------------------------------
A **census, not evidence**. A PMID on this list is a lead for the Orchestrator's intake, not a
claim, and an absent PMID is not an unread paper. Equally, a PMID that appears in a file is not
"read" (see `gold_is_in_the_details.md`): presence is all this tool measures.

It **prints and never writes**. `pubmed_corpus_harvest.py` writes corpus folders under the
evidence firewall; this tool deliberately has no output path, so there is nothing to refuse.

The queries
-----------
`STANDING_TERM`, a documented constant, overridable with `--term`: WWOX or the long name
"WW domain-containing oxidoreductase" in title or abstract. No Automatic Term Mapping, so the
count is the count of that query at that moment and nothing more.

`WOX1_PROBE` is run apart (`--no-wox1-probe` skips it): `WOX1` in title or abstract **with** the
co-term `oxidoreductase` or `WWOX`, which removes the plant homeobox genes. Its records that the
standing term did not return are reported in their own block, never added to the count, because
a human-only alias is a lead about the alias, not about WWOX.

Comparison: PMID, then DOI, then title
--------------------------------------
For each returned PMID: (1) a PMID token in the repository means registered. Tokens are the
labelled form `PMID` plus 6 to 8 digits read by `unread_gold.py`, `trace_claim_foundation.py`
and `session_self_eval.py` (`legend_lint.py` accepts 6 to 8, and so does this tool), a list after
one label (`PMIDs 123456, 234567 and 345678`) and a PubMed address. A bare number is **not** a
token. The `pmid` column of a TSV (the corpus seed files) is read apart: a PMID found only there
is `seed_only`, harvested and never cited. (2) For the PMIDs still absent, one small `esummary`
call fetches their title and DOI, and the repository is searched for the DOI, then for the
normalised title (lower case, letters and digits only, at least 30 characters). A hit is a
**false absent**: registered under another key. Only what survives all three is a **true miss**.
The scope is every text file under `disease-models/wwox/`, repeatable with `--scope`.

Transport
---------
One `esearch` call per query (PMIDs only), plus one `esummary` call for the PMIDs absent by
PMID (titles and DOIs, no abstracts): unauthenticated, no e-mail and no API key sent to any
service, whatever the environment holds (NCBI_EMAIL and NCBI_API_KEY are deliberately not
read). Rate-limit polite: a 429 honours `Retry-After`, a 5xx backs off, a refusal that cannot
succeed on retry is reported at once. No network at all in the tests.

Exit status
-----------
    0   no true misses: every PMID is registered by PMID, DOI or title
    1   true misses: the count and the PMIDs are printed
    3   the route failed: no claim about the delta is made (network, an error element,
        a count that disagrees with the identifiers returned, or more than 10,000 results)
    2   usage error (argparse)

Usage
-----
    pubmed_delta_census.py                      # the standing query, this repository
    pubmed_delta_census.py --json               # the same, machine-readable
    pubmed_delta_census.py --term "WWOX AND 2026[dp]"
    pubmed_delta_census.py --scope disease-models/wwox/registries
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo_root import repo_root  # noqa: E402

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "legend-pubmed-delta"
ESEARCH_UID_CEILING = 10000
SUMMARY_BATCH = 150
RETRIES = 4
PACE_SECONDS = 0.35
MIN_TITLE_CHARS = 30
DEFAULT_SCOPE = "disease-models/wwox"
TEXT_SUFFIXES = frozenset({".md", ".tsv", ".txt", ".json", ".jsonl", ".csv", ".yml", ".yaml"})

# The standing query: WWOX and the long name, in the title or the abstract. WOX1 is NOT here:
# it is also the name of plant WUSCHEL-related homeobox genes.
STANDING_TERM = ('(WWOX[Title/Abstract] OR '
                 '"WW domain-containing oxidoreductase"[Title/Abstract])')
# The human-only probe for the alias: WOX1 with a co-term that removes the plant genes.
WOX1_PROBE = ('(WOX1[Title/Abstract] AND '
              '(oxidoreductase[Title/Abstract] OR WWOX[Title/Abstract]))')

EXIT_NONE, EXIT_NEW, EXIT_ROUTE_FAILED = 0, 1, 3

# `PMID 12345678`, `PMID: 12345678`, and a list after one label: `PMIDs 1234567, 2345678 and ...`.
LABELLED_RE = re.compile(r"\bPMIDs?\s*[:#]?\s*(\d{6,8}(?:\s*(?:,|;|/|and|&|–|-)\s*\d{6,8})*)\b",
                         re.IGNORECASE)
NUMBER_RE = re.compile(r"\d{6,8}")
URL_RE = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,8})\b")
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


class RouteFailed(RuntimeError):
    """The delta cannot be stated: say so, make no claim."""


def tokens(text: str) -> set[str]:
    """Every PMID the repository's own notation writes in `text`."""
    found: set[str] = set()
    for match in LABELLED_RE.finditer(text):
        found.update(NUMBER_RE.findall(match.group(1)))
    found.update(URL_RE.findall(text))
    return found


def column_pmids(text: str) -> set[str]:
    """The cells of a TSV column headed exactly `pmid` (a harvested census, not a citation)."""
    lines = text.splitlines()
    if not lines or "\t" not in lines[0]:
        return set()
    header = lines[0].split("\t")
    if "pmid" not in header:
        return set()
    index = header.index("pmid")
    cells = (row.split("\t") for row in lines[1:])
    return {c[index].strip() for c in cells
            if len(c) > index and re.fullmatch(r"\d{6,8}", c[index].strip())}


def normalise_title(title: str) -> str:
    return NON_ALNUM_RE.sub(" ", title.lower()).strip()


def repository_files(root: Path, scopes: list[str]):
    for scope in scopes:
        base = root / scope
        paths = [base] if base.is_file() else sorted(base.rglob("*")) if base.is_dir() else []
        for path in paths:
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                try:
                    yield path, path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue


def known_pmids(root: Path, scopes: list[str]) -> tuple[set[str], set[str], int]:
    """(labelled PMID tokens, `pmid`-column cells, number of files read) below the scopes."""
    found: set[str] = set()
    columns: set[str] = set()
    files = 0
    for path, text in repository_files(root, scopes):
        files += 1
        found |= tokens(text)
        if path.suffix.lower() == ".tsv":
            columns |= column_pmids(text)
    return found, columns, files


def locate(root: Path, scopes: list[str], candidates: dict[str, dict]) -> dict[str, list[str]]:
    """For each candidate PMID, the other keys under which the repository already holds it."""
    via: dict[str, list[str]] = {pmid: [] for pmid in candidates}
    wanted = {pmid: (info.get("doi", "").lower(), normalise_title(info.get("title", "")))
              for pmid, info in candidates.items()}
    for _path, text in repository_files(root, scopes):
        lowered = text.lower()
        normalised = normalise_title(text)
        for pmid, (doi, title) in wanted.items():
            if doi and "doi" not in via[pmid] and doi in lowered:
                via[pmid].append("doi")
            if len(title) >= MIN_TITLE_CHARS and "title" not in via[pmid] and title in normalised:
                via[pmid].append("title")
    return via


def esearch_url(term: str) -> str:
    """The one request per query. No e-mail, no key: neither is read from the environment."""
    return EUTILS + "/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmax": str(ESEARCH_UID_CEILING),
        "retmode": "xml", "tool": TOOL})


def esummary_url(pmids: list[str]) -> str:
    return EUTILS + "/esummary.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids), "retmode": "json", "tool": TOOL})


def parse_esearch(data: bytes) -> set[str]:
    """PMIDs of one esearch answer; a count that disagrees with the ids is a failed route."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise RouteFailed(f"the answer is not XML ({error})") from error
    problem = root.findtext("ERROR")
    if problem:
        raise RouteFailed(f"E-utilities answered with an error: {problem.strip()}")
    try:
        count = int(root.findtext("Count") or "")
    except ValueError as error:
        raise RouteFailed("the answer carries no Count") from error
    if count > ESEARCH_UID_CEILING:
        raise RouteFailed(f"{count} results exceed the esearch ceiling of {ESEARCH_UID_CEILING}; "
                          "narrow the query by date and merge")
    ids = {node.text.strip() for node in root.iter("Id") if node.text and node.text.strip()}
    if len(ids) != count:
        raise RouteFailed(f"Count says {count} but {len(ids)} identifiers came back")
    return ids


def parse_esummary(data: bytes, asked: list[str]) -> dict[str, dict]:
    """{pmid: {title, doi}} from one esummary JSON answer; a missing id is a failed route."""
    try:
        result = json.loads(data)["result"]
    except (ValueError, KeyError, TypeError) as error:
        raise RouteFailed(f"the esummary answer is not the expected JSON ({error})") from error
    out: dict[str, dict] = {}
    for pmid in asked:
        entry = result.get(pmid)
        if not isinstance(entry, dict):
            raise RouteFailed(f"esummary returned nothing for PMID {pmid}")
        doi = next((a.get("value", "") for a in entry.get("articleids", [])
                    if a.get("idtype") == "doi"), "")
        out[pmid] = {"title": entry.get("title", "") or "", "doi": doi or ""}
    return out


def _get(url: str, urlopen: Callable, sleep: Callable[[float], None]) -> bytes:
    last: Exception | None = None
    for attempt in range(RETRIES):
        try:
            with urlopen(url, timeout=60) as response:
                data = response.read()
            sleep(PACE_SECONDS)
            return data
        except urllib.error.HTTPError as error:
            last = error
            if error.code == 429:
                header = error.headers.get("Retry-After") if error.headers else None
                wait = float(header) if header and header.isdigit() else 2 ** attempt
            elif 500 <= error.code < 600:
                wait = 2 ** attempt
            else:
                raise RouteFailed(f"E-utilities returned HTTP {error.code}") from error
            sleep(min(wait, 60))
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last = error
            sleep(min(2 ** attempt, 60))
    raise RouteFailed(f"E-utilities unreachable after {RETRIES} attempts: {last}")


def fetch_pmids(term: str, urlopen: Callable = urllib.request.urlopen,
                sleep: Callable[[float], None] = time.sleep) -> set[str]:
    return parse_esearch(_get(esearch_url(term), urlopen, sleep))


def fetch_summaries(pmids: list[str], urlopen: Callable = urllib.request.urlopen,
                    sleep: Callable[[float], None] = time.sleep) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for start in range(0, len(pmids), SUMMARY_BATCH):
        batch = pmids[start:start + SUMMARY_BATCH]
        out.update(parse_esummary(_get(esummary_url(batch), urlopen, sleep), batch))
    return out


def classify(returned: set[str], root: Path, scopes: list[str],
             summariser: Callable[[list[str]], dict[str, dict]]) -> dict:
    """PMID, then DOI, then title: registered, false absent (other key), true miss."""
    labelled, columns, files = known_pmids(root, scopes)
    absent = sorted(returned - labelled - columns, key=int, reverse=True)
    seed_only = sorted((returned & columns) - labelled, key=int, reverse=True)
    false_absent: list[dict] = []
    misses: list[str] = []
    if absent:
        info = summariser(absent)
        via = locate(root, scopes, info)
        for pmid in absent:
            if via[pmid]:
                false_absent.append({"pmid": pmid, "via": via[pmid],
                                     "doi": info[pmid]["doi"], "title": info[pmid]["title"]})
            else:
                misses.append(pmid)
    return {"returned": len(returned), "files_read": files, "known_tokens": len(labelled),
            "pmid_column_cells": len(columns), "new_count": len(misses), "new_pmids": misses,
            "false_absent_count": len(false_absent), "false_absent": false_absent,
            "seed_only_count": len(seed_only), "seed_only_pmids": seed_only}


def build_report(term: str, root: Path, scopes: list[str],
                 fetcher: Callable[[str], set[str]],
                 summariser: Callable[[list[str]], dict[str, dict]],
                 probe: str | None = WOX1_PROBE) -> dict:
    returned = fetcher(term)
    report = {"term": term, "scopes": scopes, **classify(returned, root, scopes, summariser)}
    if probe:
        extra = fetcher(probe) - returned
        report["wox1_probe"] = {"term": probe, **classify(extra, root, scopes, summariser)}
    report["status"] = "NEW_RECORDS" if report["new_pmids"] else "NO_NEW_RECORDS"
    return report


def _block(report: dict) -> list[str]:
    lines = [f"  true misses (no PMID, DOI or title in the repository): {report['new_count']}"]
    lines += [f"    {pmid}  https://pubmed.ncbi.nlm.nih.gov/{pmid}/" for pmid in report["new_pmids"]]
    lines.append(f"  false absent (registered under another key): {report['false_absent_count']}")
    lines += [f"    {r['pmid']}  via {'+'.join(r['via'])}  {r['title'][:70]}"
              for r in report["false_absent"]]
    lines.append(f"  present only as a harvested seed row, never cited: {report['seed_only_count']}")
    return lines


def render(report: dict) -> str:
    lines = [f"PUBMED DELTA CENSUS — {report['status']}",
             f"query: {report['term']}",
             f"scope: {', '.join(report['scopes'])} ({report['files_read']} text files, "
             f"{report['known_tokens']} labelled PMID tokens, {report['pmid_column_cells']} "
             f"`pmid` column cells)",
             f"PubMed returned {report['returned']}"]
    lines += _block(report)
    probe = report.get("wox1_probe")
    if probe:
        lines.append(f"WOX1 probe, not part of the count ({probe['term']}): "
                     f"{probe['returned']} records the standing term did not return")
        lines += _block(probe)
    lines.append("A census, not evidence: a PMID here is a lead for intake, never a claim. "
                 "Nothing was written.")
    return "\n".join(lines)


def main(argv: list[str] | None = None,
         fetcher: Callable[[str], set[str]] | None = None,
         summariser: Callable[[list[str]], dict[str, dict]] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print PubMed WWOX records absent from every disease-model file by PMID, "
                    "DOI and title (read-only; exit 0 none, 1 true misses, 3 route failed).")
    parser.add_argument("--term", default=STANDING_TERM,
                        help="the PubMed query (default: the standing WWOX-only title-abstract query)")
    parser.add_argument("--no-wox1-probe", action="store_true",
                        help="skip the separate human-only WOX1 probe")
    parser.add_argument("--scope", action="append", default=None,
                        help=f"a path under the repository to read (repeatable; "
                             f"default {DEFAULT_SCOPE})")
    parser.add_argument("--root", default=None, help="repository root (default: found from here)")
    parser.add_argument("--json", action="store_true", help="print one JSON object")
    args = parser.parse_args(argv)
    root = Path(args.root) if args.root else repo_root()
    scopes = args.scope or [DEFAULT_SCOPE]
    try:
        report = build_report(args.term, root, scopes, fetcher or fetch_pmids,
                              summariser or fetch_summaries,
                              None if args.no_wox1_probe else WOX1_PROBE)
    except RouteFailed as error:
        message = f"ROUTE FAILED: {error}. No claim about the delta is made."
        print(json.dumps({"status": "ROUTE_FAILED", "error": str(error)}) if args.json else message)
        return EXIT_ROUTE_FAILED
    print(json.dumps(report, indent=2) if args.json else render(report))
    return EXIT_NEW if report["new_pmids"] else EXIT_NONE


if __name__ == "__main__":
    sys.exit(main())
