#!/usr/bin/env python3
"""Harvest a complete PubMed corpus, with abstracts, straight from E-utilities.

Why not the Clipboard
---------------------
The PubMed Clipboard is a browser feature: session-bound, capped at 200 records per page,
and reached by pasting an export a human assembled by hand. `pubmed_clipboard_to_seed.py`
exists to sanitise exactly that route, because a pasted export can carry mail headers and
sender details, so it discards everything outside a numbered record — abstracts included.

E-utilities is NCBI's supported programmatic interface and is strictly better here: no
pagination ceiling, no session state, no mailbox in the path — and therefore no PII to strip,
which is why abstracts can be kept. The Clipboard tool stays for exports a human already has.

Why the whole corpus and not the free-full-text slice
----------------------------------------------------
The existing seed was harvested behind PubMed's `ffrft` filter, so it holds the retrievable
subset. Parity of sources says no filter authorises *not reading*: what is paywalled today is
reading debt, not absence. This harvests everything the query matches and records retrievability
as a column, so the debt stays countable instead of disappearing.

Why abstracts matter operationally
----------------------------------
Three consumers, none of which is "reading the paper" — reading means full text, always:

* intake triage, the inferential sweep and the priority matrix run on title + abstract, and a
  local corpus makes them offline and instant instead of hundreds of API calls;
* export pre-flight — an external knowledge base verifies a quoted snippet against a cached
  source, and for a paper that is not full-text indexed the only cacheable text is the
  abstract. Knowing in advance whether the abstract carries a proposition lets the reader
  capture that anchor while the document is open, instead of reopening it later;
* census — "every paper that exists on this gene" turns reading debt from an estimate into a
  count.

Disease-agnostic by construction: the query is an argument.

Usage
-----
    pubmed_corpus_harvest.py --term "WWOX OR WOREE" --out corpus.tsv
    pubmed_corpus_harvest.py --term "SCN1A" --out corpus.tsv --no-abstracts
    pubmed_corpus_harvest.py --term "WWOX" --count-only

Set `NCBI_API_KEY` to raise the rate limit from 3 to 10 requests per second.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
BATCH = 200
FIELDS = ("pmid", "year", "free_full_text", "pmcid", "type", "doi", "journal",
          "title", "abstract")


def _get(endpoint: str, params: dict, retries: int = 3) -> bytes:
    key = os.environ.get("NCBI_API_KEY")
    if key:
        params = {**params, "api_key": key}
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(params)}"
    delay = 0.11 if key else 0.35
    last: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                data = response.read()
            time.sleep(delay)
            return data
        except Exception as error:                      # noqa: BLE001 — retried, then raised
            last = error
            time.sleep(delay * (attempt + 2))
    raise RuntimeError(f"E-utilities failed after {retries} attempts: {last}")


def search(term: str) -> tuple[int, str, str]:
    """Return (count, WebEnv, query_key) using the history server."""
    root = ET.fromstring(_get("esearch.fcgi", {
        "db": "pubmed", "term": term, "usehistory": "y", "retmax": "0"}))
    return (int(root.findtext("Count") or 0),
            root.findtext("WebEnv") or "",
            root.findtext("QueryKey") or "")


def pmids_matching(term: str) -> set[str]:
    """Every PMID for a query, used to mark which records are free full text."""
    count, web, key = search(term)
    found: set[str] = set()
    for start in range(0, count, 10000):
        root = ET.fromstring(_get("esearch.fcgi", {
            "db": "pubmed", "query_key": key, "WebEnv": web,
            "retstart": str(start), "retmax": "10000"}))
        found.update(identifier.text or "" for identifier in root.iter("Id"))
    return {p for p in found if p}


def _clean(text: str | None) -> str:
    """TSV-safe single line. A tab or newline inside a field silently shifts every column."""
    return " ".join((text or "").split())


def _text(parent: ET.Element, path: str) -> str:
    """Full text of one node, markup included.

    `parent.find(path) or fallback` is a trap: an Element with no CHILDREN is falsy, so a
    plain-text title silently becomes the fallback while a title carrying <i> or <sup>
    survives. That emptied 673 of 706 titles in the first run and looked like an API problem.
    """
    node = parent.find(path)
    return _clean("".join(node.itertext())) if node is not None else ""


def _abstract(article: ET.Element) -> str:
    """Only the article's own abstract — never an `OtherAbstract` or a reference's."""
    block = article.find("MedlineCitation/Article/Abstract")
    if block is None:
        return ""
    parts: list[str] = []
    for node in block.iter("AbstractText"):
        label = node.attrib.get("Label")
        body = "".join(node.itertext())
        parts.append(f"{label}: {body}" if label else body)
    return _clean(" ".join(parts))


def parse(xml_bytes: bytes, want_abstract: bool) -> list[dict]:
    rows = []
    for article in ET.fromstring(xml_bytes).iter("PubmedArticle"):
        pmid = article.findtext(".//MedlineCitation/PMID") or ""
        if not pmid:
            continue
        # `article.iter("ArticleId")` walks the WHOLE record, and a PubmedArticle carries an
        # ArticleId for every entry in its reference list — 78 of them for PMID 36779245,
        # of which 3 are the article's own. Reading them all assigned Oliver 2023 the PMCID
        # and DOI of one of its references, silently and plausibly.
        id_list = article.find("PubmedData/ArticleIdList")
        ids = ({node.attrib.get("IdType"): (node.text or "") for node in id_list}
               if id_list is not None else {})
        year = ""
        for path in (".//Journal/JournalIssue/PubDate/Year",
                     ".//Journal/JournalIssue/PubDate/MedlineDate",
                     ".//PubMedPubDate[@PubStatus='pubmed']/Year"):
            value = article.findtext(path)
            if value:
                year = value.strip()[:4]
                break
        types = sorted({_clean("".join(node.itertext()))
                        for node in article.iter("PublicationType")})
        rows.append({
            "pmid": pmid,
            "year": year,
            "free_full_text": "",
            "pmcid": ids.get("pmc", ""),
            "type": "; ".join(t for t in types if t),
            "doi": ids.get("doi", ""),
            "journal": _clean(article.findtext(
                "MedlineCitation/Article/Journal/ISOAbbreviation")
                or article.findtext("MedlineCitation/Article/Journal/Title")),
            "title": (_text(article, "MedlineCitation/Article/ArticleTitle")
                      or _text(article, "MedlineCitation/Article/VernacularTitle")),
            "abstract": _abstract(article) if want_abstract else "",
        })
    return rows


def harvest(term: str, want_abstract: bool = True) -> list[dict]:
    count, web, key = search(term)
    if not count:
        return []
    rows: list[dict] = []
    for start in range(0, count, BATCH):
        rows.extend(parse(_get("efetch.fcgi", {
            "db": "pubmed", "query_key": key, "WebEnv": web,
            "retstart": str(start), "retmax": str(BATCH), "retmode": "xml"}), want_abstract))
        print(f"  fetched {min(start + BATCH, count)}/{count}", file=sys.stderr, flush=True)
    free = pmids_matching(f"({term}) AND ffrft[Filter]")
    for row in rows:
        row["free_full_text"] = "yes" if row["pmid"] in free else "no"
    # Deterministic order: the same query on the same day must produce the same bytes, or the
    # file cannot be diffed to see what the corpus actually gained.
    return sorted(rows, key=lambda r: int(r["pmid"]))


def write(rows: list[dict], destination: Path) -> None:
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t",
                                quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--term", required=True, help='PubMed query, e.g. "WWOX OR WOREE"')
    parser.add_argument("--out", type=Path, help="destination TSV")
    parser.add_argument("--no-abstracts", action="store_true",
                        help="bibliographic fields only")
    parser.add_argument("--count-only", action="store_true",
                        help="report how many records the query matches and stop")
    arguments = parser.parse_args()

    if arguments.count_only:
        count, _web, _key = search(arguments.term)
        print(f"{count} record(s) for: {arguments.term}")
        return 0
    if not arguments.out:
        print("ERROR: --out is required unless --count-only", file=sys.stderr)
        return 2

    rows = harvest(arguments.term, want_abstract=not arguments.no_abstracts)
    write(rows, arguments.out)
    with_abstract = sum(1 for r in rows if r["abstract"])
    free = sum(1 for r in rows if r["free_full_text"] == "yes")
    print(f"written: {arguments.out}")
    print(f"  {len(rows)} record(s) · {with_abstract} with an abstract · "
          f"{free} free full text · {len(rows) - free} paywalled (reading debt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
