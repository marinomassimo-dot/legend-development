#!/usr/bin/env python3
"""Print the PubMed records on the standing WWOX query that no disease-model file mentions.

Why this exists
---------------
On 2026-11-24 one E-utilities call found 39 current WWOX PubMed records (several from 2024 to
2026) that appear in no file of the repository. The weekly harness scout had no PubMed delta
step, so nobody would have seen them. This tool is that step: it reads, it compares, it prints.

What it is, and what it is not
------------------------------
A **census, not evidence**. A PMID on this list is a lead for the Orchestrator's intake, not a
claim, and an absent PMID is not an unread paper: a record can be known under a DOI or a title
only. Equally, a PMID that appears in a file is not "read" (see `gold_is_in_the_details.md`):
presence is all this tool measures, and it measures it as a *token*.

It **prints and never writes**. `pubmed_corpus_harvest.py` writes corpus folders under the
evidence firewall; this tool deliberately has no output path, so there is nothing to refuse.

The query
---------
`STANDING_TERM` below, a documented constant, overridable with `--term`. It searches the title
and the abstract only, so it is narrower than a free-text query (no Automatic Term Mapping into
MeSH, no author or affiliation hits). The count it prints is the count of that query at that
moment and nothing more.

Tokenisation (the same as the existing parsers)
-----------------------------------------------
A PMID is a labelled token, `PMID` followed by 6 to 8 digits, the form read by
`unread_gold.py`, `trace_claim_foundation.py` and `session_self_eval.py` (`legend_lint.py`
accepts 6 to 8, and so does this tool: PubMed identifiers below 10 million are not zero-padded
anywhere in the repository). Two additions, both because the repository writes PMIDs in those
ways and the labelled form alone would call them absent:

* a list after one label, `PMIDs 123456, 234567 and 345678`, counts every number of the list;
* a PubMed address, `pubmed.ncbi.nlm.nih.gov/12345678`.

A bare 7-digit or 8-digit number is **not** a token: counting it would make any measurement or
accession look like a known paper and hide a real delta. The scope is every text file under
`disease-models/wwox/` (registries, research, analysis, therapeutics and the rest), repeatable
with `--scope`.

One more source is read, and kept apart: the `pmid` column of a TSV (the corpus seed files
`pubmed_corpus_harvest.py` writes). A PMID found only there was harvested and **never
registered or cited**; it is reported as `seed_only`, a second count, not as absent. `new` means
absent from the labelled tokens and from every `pmid` column.

Transport
---------
One `esearch` call, PMIDs only (no abstracts, no efetch), unauthenticated, no e-mail and no API
key sent to any service, whatever the environment holds: NCBI_EMAIL and NCBI_API_KEY are
deliberately not read. Rate-limit polite: a 429 honours `Retry-After`, a 5xx backs off, and a
refusal that cannot succeed on retry is reported at once. No network at all in the tests.

Exit status
-----------
    0   no new records: every PMID the query returned is in the repository
    1   new records: the list is printed (the count and the PMIDs)
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

EUTILS_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
TOOL = "legend-pubmed-delta"
ESEARCH_UID_CEILING = 10000
RETRIES = 4
PACE_SECONDS = 0.35
DEFAULT_SCOPE = "disease-models/wwox"
TEXT_SUFFIXES = frozenset({".md", ".tsv", ".txt", ".json", ".jsonl", ".csv", ".yml", ".yaml"})

# The standing query: WWOX, WOX1 and the long name, in the title or the abstract.
STANDING_TERM = ('(WWOX[Title/Abstract] OR WOX1[Title/Abstract] OR '
                 '"WW domain-containing oxidoreductase"[Title/Abstract])')

EXIT_NONE, EXIT_NEW, EXIT_ROUTE_FAILED = 0, 1, 3

# `PMID 12345678`, `PMID: 12345678`, and a list after one label: `PMIDs 1234567, 2345678 and ...`.
LABELLED_RE = re.compile(r"\bPMIDs?\s*[:#]?\s*(\d{6,8}(?:\s*(?:,|;|/|and|&|–|-)\s*\d{6,8})*)\b",
                         re.IGNORECASE)
NUMBER_RE = re.compile(r"\d{6,8}")
URL_RE = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,8})\b")


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
    return {c[index].strip() for c in cells if len(c) > index and re.fullmatch(r"\d{6,8}", c[index].strip())}


def known_pmids(root: Path, scopes: list[str]) -> tuple[set[str], set[str], int]:
    """(labelled PMID tokens, `pmid`-column cells, number of files read) below the scopes."""
    found: set[str] = set()
    columns: set[str] = set()
    files = 0
    for scope in scopes:
        base = (root / scope)
        paths = [base] if base.is_file() else sorted(base.rglob("*")) if base.is_dir() else []
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            files += 1
            found |= tokens(text)
            if path.suffix.lower() == ".tsv":
                columns |= column_pmids(text)
    return found, columns, files


def esearch_url(term: str) -> str:
    """The one request. No e-mail, no key: neither is read from the environment."""
    return EUTILS_ESEARCH + "?" + urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmax": str(ESEARCH_UID_CEILING),
        "retmode": "xml", "tool": TOOL})


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


def fetch_pmids(term: str, urlopen: Callable = urllib.request.urlopen,
                sleep: Callable[[float], None] = time.sleep) -> set[str]:
    url = esearch_url(term)
    last: Exception | None = None
    for attempt in range(RETRIES):
        try:
            with urlopen(url, timeout=60) as response:
                data = response.read()
            sleep(PACE_SECONDS)
            return parse_esearch(data)
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
        except RouteFailed:
            raise
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last = error
            sleep(min(2 ** attempt, 60))
    raise RouteFailed(f"E-utilities unreachable after {RETRIES} attempts: {last}")


def build_report(term: str, root: Path, scopes: list[str],
                 fetcher: Callable[[str], set[str]]) -> dict:
    returned = fetcher(term)
    labelled, columns, files = known_pmids(root, scopes)
    new = sorted(returned - labelled - columns, key=int, reverse=True)
    seed_only = sorted((returned & columns) - labelled, key=int, reverse=True)
    return {"term": term, "scopes": scopes, "files_read": files,
            "known_tokens": len(labelled), "pmid_column_cells": len(columns),
            "returned": len(returned),
            "new_count": len(new), "new_pmids": new,
            "seed_only_count": len(seed_only), "seed_only_pmids": seed_only,
            "status": "NEW_RECORDS" if new else "NO_NEW_RECORDS"}


def render(report: dict) -> str:
    lines = [f"PUBMED DELTA CENSUS — {report['status']}",
             f"query: {report['term']}",
             f"scope: {', '.join(report['scopes'])} ({report['files_read']} text files, "
             f"{report['known_tokens']} labelled PMID tokens, {report['pmid_column_cells']} "
             f"`pmid` column cells)",
             f"PubMed returned {report['returned']}; absent from the repository: "
             f"{report['new_count']}",
             f"present only as a harvested seed row, never cited (see --json seed_only_pmids): "
             f"{report['seed_only_count']}"]
    lines += [f"  {pmid}  https://pubmed.ncbi.nlm.nih.gov/{pmid}/" for pmid in report["new_pmids"]]
    lines.append("A census, not evidence: a PMID here is a lead for intake, never a claim. "
                 "Nothing was written.")
    return "\n".join(lines)


def main(argv: list[str] | None = None,
         fetcher: Callable[[str], set[str]] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print PubMed WWOX records absent from every disease-model file "
                    "(read-only; exit 0 none, 1 new, 3 route failed).")
    parser.add_argument("--term", default=STANDING_TERM,
                        help="the PubMed query (default: the standing WWOX/WOX1 title-abstract query)")
    parser.add_argument("--scope", action="append", default=None,
                        help=f"a path under the repository to read for PMIDs (repeatable; "
                             f"default {DEFAULT_SCOPE})")
    parser.add_argument("--root", default=None, help="repository root (default: found from here)")
    parser.add_argument("--json", action="store_true", help="print one JSON object")
    args = parser.parse_args(argv)
    root = Path(args.root) if args.root else repo_root()
    scopes = args.scope or [DEFAULT_SCOPE]
    try:
        report = build_report(args.term, root, scopes, fetcher or fetch_pmids)
    except RouteFailed as error:
        message = f"ROUTE FAILED: {error}. No claim about the delta is made."
        print(json.dumps({"status": "ROUTE_FAILED", "error": str(error)}) if args.json else message)
        return EXIT_ROUTE_FAILED
    print(json.dumps(report, indent=2) if args.json else render(report))
    return EXIT_NEW if report["new_pmids"] else EXIT_NONE


if __name__ == "__main__":
    sys.exit(main())
