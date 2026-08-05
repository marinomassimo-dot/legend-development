#!/usr/bin/env python3
"""Harvest a PubMed corpus from E-utilities: lossless JSONL, a compact seed, and a manifest.

Why not the Clipboard
---------------------
The Clipboard is a browser feature: session-bound, 200 records per page, reached by pasting an
export a human assembled by hand. `pubmed_clipboard_to_seed.py` sanitises exactly that route,
because a pasted export can carry mail headers and sender details, so it discards everything
outside a numbered record — abstracts included. E-utilities has no mailbox in the path and
therefore nothing to strip, which is why abstracts can be kept. The Clipboard tool stays as the
fallback for an export a human already has.

What this does NOT claim
------------------------
🔴 **Not "every paper on the gene".** PubMed applies Automatic Term Mapping, so a free-text
query expands in ways the caller did not write. What this produces is *every record returned by
one documented query at one moment*, and the manifest records the query as sent, the
`QueryTranslation` PubMed actually ran, the filters, the UTC timestamp and the expected count —
so the claim can be checked rather than believed.

🔴 **`free_full_text` is not "not paywalled".** It means PubMed exposes a link it classifies as
free. Its complement is *unknown retrievability*, not a paywall, and calling it reading debt
would manufacture a fact.

Completeness is asserted, not hoped
-----------------------------------
Three invariants, each a refusal:

* every record type is parsed — `PubmedArticle` **and** `PubmedBookArticle`. A book record
  parsed by neither branch disappears without a trace;
* `fetched == ESearch Count` — a dropped page or an unhandled record type shows up here;
* `unique PMIDs == fetched` — a duplicated page cannot inflate the count.

ESearch returns at most 10 000 UIDs regardless of `retstart`, so the free-full-text annotation
is refused above that ceiling rather than silently truncated. Partition by date and merge.

Losslessness
------------
The JSONL keeps what PubMed sent: personal and collective authors with affiliations, both
electronic and print dates, volume/issue/pagination/e-location, language, ISSN, publication
status, every article identifier, `CommentsCorrectionsList` (retractions, errata) and
`OtherAbstract` preserved *separately* with its language rather than folded into the abstract.
The TSV is a derived convenience for the batch queue and is allowed to be lossy; the JSONL is
not.

Usage
-----
    pubmed_corpus_harvest.py --term "WWOX OR WOREE" --out-dir files/corpus
    pubmed_corpus_harvest.py --term "SCN1A" --count-only

Set `NCBI_API_KEY` for 10 requests/second instead of 3, and `NCBI_EMAIL` so NCBI can contact
you before blocking — both are asked for by the E-utilities usage guidelines.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

HARVESTER_VERSION = "2.0"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "legend-corpus-harvest"
BATCH = 200
ESEARCH_UID_CEILING = 10000

SEED_FIELDS = ("pmid", "year", "pubmed_free_full_text_link", "pmcid", "type", "doi",
               "journal", "title", "abstract")
YEAR_RE = re.compile(r"(1[5-9]\d{2}|20\d{2}|21\d{2})")


class HarvestError(RuntimeError):
    """A refusal. Every one of these means the corpus would have been silently incomplete."""


# --------------------------------------------------------------------------- transport

def _request(endpoint: str, params: dict, retries: int = 5) -> bytes:
    params = {**params, "tool": TOOL}
    if os.environ.get("NCBI_EMAIL"):
        params["email"] = os.environ["NCBI_EMAIL"]
    key = os.environ.get("NCBI_API_KEY")
    if key:
        params["api_key"] = key
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(params)}"
    pace = 0.11 if key else 0.35
    last: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as response:
                data = response.read()
            time.sleep(pace)
            _raise_on_xml_error(data)
            return data
        except urllib.error.HTTPError as error:
            last = error
            if error.code == 429:
                wait = float(error.headers.get("Retry-After") or 0) or 2 ** attempt
            elif 500 <= error.code < 600:
                wait = 2 ** attempt
            else:
                raise HarvestError(f"E-utilities {endpoint} returned HTTP {error.code}")
            time.sleep(wait + random.uniform(0, 0.5))
        except Exception as error:                       # noqa: BLE001 — retried, then raised
            last = error
            time.sleep(2 ** attempt + random.uniform(0, 0.5))
    raise HarvestError(f"E-utilities {endpoint} failed after {retries} attempts: {last}")


def _raise_on_xml_error(data: bytes) -> None:
    """E-utilities answers HTTP 200 with an <ERROR> body. A 200 is not a success."""
    head = data[:400].lstrip()
    if head.startswith(b"<?xml") or head.startswith(b"<"):
        try:
            root = ET.fromstring(data)
        except ET.ParseError:
            return
        for tag in ("ERROR", "error"):
            node = root.find(f".//{tag}")
            if node is not None and (node.text or "").strip():
                raise HarvestError(f"E-utilities returned an error body: {node.text.strip()}")


# --------------------------------------------------------------------------- search

def search(term: str) -> dict:
    root = ET.fromstring(_request("esearch.fcgi", {
        "db": "pubmed", "term": term, "usehistory": "y", "retmax": "0"}))
    return {
        "count": int(root.findtext("Count") or 0),
        "webenv": root.findtext("WebEnv") or "",
        "query_key": root.findtext("QueryKey") or "",
        "query_translation": (root.findtext("QueryTranslation") or "").strip(),
    }


def uids(term: str) -> set[str]:
    """Every PMID for a query. Refuses above the ESearch ceiling instead of truncating."""
    result = search(term)
    if result["count"] > ESEARCH_UID_CEILING:
        raise HarvestError(
            f"{result['count']} records exceed the ESearch UID ceiling of "
            f"{ESEARCH_UID_CEILING}; retstart cannot reach past it, so this annotation would "
            "be silently partial. Partition the query by date range and merge the results.")
    root = ET.fromstring(_request("esearch.fcgi", {
        "db": "pubmed", "query_key": result["query_key"], "WebEnv": result["webenv"],
        "retstart": "0", "retmax": str(ESEARCH_UID_CEILING)}))
    return {node.text for node in root.iter("Id") if node.text}


# --------------------------------------------------------------------------- parsing

def _clean(text: str | None) -> str:
    return " ".join((text or "").split())


def _text(parent: ET.Element | None, path: str) -> str:
    """Full text of one node, markup included.

    `parent.find(path) or fallback` is a trap: an Element with no CHILDREN is falsy, so a
    plain-text title silently becomes the fallback while a title carrying <i> survives. That
    emptied 673 of 706 titles in the first version and looked like an upstream problem.
    """
    if parent is None:
        return ""
    node = parent.find(path)
    return _clean("".join(node.itertext())) if node is not None else ""


def _year(node: ET.Element | None) -> str:
    """A four-digit year, or empty. Never the first four characters.

    `MedlineDate` is free text: "Winter 2024" truncated to four characters gives "Wint".
    """
    if node is None:
        return ""
    explicit = node.findtext("Year")
    if explicit and explicit.strip().isdigit():
        return explicit.strip()
    found = YEAR_RE.search(_clean("".join(node.itertext())))
    return found.group(1) if found else ""


def _authors(article: ET.Element | None) -> list[dict]:
    people = []
    for author in (article.iter("Author") if article is not None else []):
        entry = {
            "last_name": _clean(author.findtext("LastName")),
            "fore_name": _clean(author.findtext("ForeName")),
            "initials": _clean(author.findtext("Initials")),
            "collective_name": _clean(author.findtext("CollectiveName")),
            "affiliations": [_clean("".join(node.itertext()))
                             for node in author.iter("Affiliation")],
            "identifiers": {node.attrib.get("Source", "?"): _clean(node.text)
                            for node in author.iter("Identifier")},
        }
        if any(entry[k] for k in ("last_name", "collective_name")):
            people.append(entry)
    return people


def _abstract_parts(block: ET.Element | None) -> list[dict]:
    if block is None:
        return []
    return [{"label": node.attrib.get("Label", ""),
             "category": node.attrib.get("NlmCategory", ""),
             "text": _clean("".join(node.itertext()))}
            for node in block.iter("AbstractText")]


def _other_abstracts(citation: ET.Element) -> list[dict]:
    """Translated or secondary abstracts, kept apart. Folding them in corrupts the main text."""
    return [{"type": node.attrib.get("Type", ""),
             "language": node.attrib.get("Language", ""),
             "parts": _abstract_parts(node)}
            for node in citation.iter("OtherAbstract")]


def _corrections(citation: ET.Element) -> list[dict]:
    """Retractions, errata and comments — the reason a paper may need to leave the model."""
    out = []
    for node in citation.iter("CommentsCorrections"):
        out.append({"ref_type": node.attrib.get("RefType", ""),
                    "pmid": _clean(node.findtext("PMID")),
                    "citation": _clean("".join(
                        (node.find("RefSource") or ET.Element("x")).itertext()))})
    return out


def _identifiers(record: ET.Element) -> dict:
    """Only the record's OWN ids.

    `record.iter("ArticleId")` walks the reference list too: PMID 36779245 carries 78 of them,
    three its own. Reading them all assigned it a reference's PMCID and DOI — real
    identifiers, wrong paper.
    """
    id_list = record.find("PubmedData/ArticleIdList")
    if id_list is None:
        return {}
    return {node.attrib.get("IdType", "?"): _clean(node.text) for node in id_list}


def _parse_article(record: ET.Element) -> dict:
    citation = record.find("MedlineCitation")
    article = citation.find("Article") if citation is not None else None
    journal = article.find("Journal") if article is not None else None
    issue = journal.find("JournalIssue") if journal is not None else None
    pagination = article.find("Pagination") if article is not None else None
    return {
        "record_type": "PubmedArticle",
        "pmid": _clean(citation.findtext("PMID") if citation is not None else ""),
        "title": (_text(article, "ArticleTitle")
                  or _text(article, "VernacularTitle")),
        "journal": {
            "title": _clean(journal.findtext("Title") if journal is not None else ""),
            "iso_abbreviation": _clean(
                journal.findtext("ISOAbbreviation") if journal is not None else ""),
            "issn": [_clean(node.text) for node in (journal.iter("ISSN")
                                                    if journal is not None else [])],
            "volume": _clean(issue.findtext("Volume") if issue is not None else ""),
            "issue": _clean(issue.findtext("Issue") if issue is not None else ""),
        },
        "pagination": _clean(pagination.findtext("MedlinePgn")
                             if pagination is not None else ""),
        "elocation": [{"type": node.attrib.get("EIdType", ""), "value": _clean(node.text)}
                      for node in (article.iter("ELocationID") if article is not None else [])],
        "year": _year(issue.find("PubDate") if issue is not None else None),
        "dates": {
            "article_date": [
                {"type": node.attrib.get("DateType", ""),
                 "date": "-".join(filter(None, (node.findtext("Year"), node.findtext("Month"),
                                                node.findtext("Day"))))}
                for node in (article.iter("ArticleDate") if article is not None else [])],
            "pubmed_status": [
                {"status": node.attrib.get("PubStatus", ""),
                 "date": "-".join(filter(None, (node.findtext("Year"), node.findtext("Month"),
                                                node.findtext("Day"))))}
                for node in record.iter("PubMedPubDate")],
        },
        "language": [_clean(node.text) for node in
                     (article.iter("Language") if article is not None else [])],
        "publication_types": sorted({_clean("".join(node.itertext()))
                                     for node in (article.iter("PublicationType")
                                                  if article is not None else [])} - {""}),
        "publication_status": _clean(record.findtext("PubmedData/PublicationStatus")),
        "authors": _authors(article),
        "abstract_parts": _abstract_parts(
            article.find("Abstract") if article is not None else None),
        "other_abstracts": _other_abstracts(citation) if citation is not None else [],
        "copyright": _clean(article.findtext("Abstract/CopyrightInformation")
                            if article is not None else ""),
        "corrections": _corrections(citation) if citation is not None else [],
        "identifiers": _identifiers(record),
    }


def _parse_book(record: ET.Element) -> dict:
    """A PubmedBookArticle is a first-class PubMed record and has a PMID like any other.

    Parsing only `PubmedArticle` drops these without a trace, which is exactly the shape of
    loss the completeness invariant exists to catch.
    """
    document = record.find("BookDocument")
    book = document.find("Book") if document is not None else None
    return {
        "record_type": "PubmedBookArticle",
        "pmid": _clean(document.findtext("PMID") if document is not None else ""),
        "title": (_text(document, "ArticleTitle") or _text(book, "BookTitle")),
        "journal": {"title": _text(book, "BookTitle"), "iso_abbreviation": "",
                    "issn": [], "volume": "", "issue": ""},
        "pagination": "",
        "elocation": [],
        "year": _year(book.find("PubDate") if book is not None else None),
        "dates": {"article_date": [], "pubmed_status": [
            {"status": node.attrib.get("PubStatus", ""),
             "date": "-".join(filter(None, (node.findtext("Year"), node.findtext("Month"),
                                            node.findtext("Day"))))}
            for node in record.iter("PubMedPubDate")]},
        "language": [_clean(node.text) for node in
                     (document.iter("Language") if document is not None else [])],
        "publication_types": sorted({_clean("".join(node.itertext()))
                                     for node in (document.iter("PublicationType")
                                                  if document is not None else [])} - {""}),
        "publication_status": _clean(record.findtext("PubmedBookData/PublicationStatus")),
        "authors": _authors(document),
        "abstract_parts": _abstract_parts(
            document.find("Abstract") if document is not None else None),
        "other_abstracts": _other_abstracts(document) if document is not None else [],
        "copyright": "",
        "corrections": _corrections(document) if document is not None else [],
        "identifiers": ({node.attrib.get("IdType", "?"): _clean(node.text)
                         for node in record.find("PubmedBookData/ArticleIdList")}
                        if record.find("PubmedBookData/ArticleIdList") is not None else {}),
    }


PARSERS = {"PubmedArticle": _parse_article, "PubmedBookArticle": _parse_book}


def parse(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    records = []
    for child in root:
        parser = PARSERS.get(child.tag)
        if parser is None:
            continue
        record = parser(child)
        if record["pmid"]:
            records.append(record)
    return records


def unparsed_record_tags(xml_bytes: bytes) -> set[str]:
    """Record-level tags this parser does not handle — a new DTD type must be visible."""
    root = ET.fromstring(xml_bytes)
    return {child.tag for child in root if child.tag not in PARSERS}


# --------------------------------------------------------------------------- derivation

def abstract_text(record: dict) -> str:
    return _clean(" ".join(
        f"{p['label']}: {p['text']}" if p["label"] else p["text"]
        for p in record["abstract_parts"] if p["text"]))


def to_seed_row(record: dict, free: set[str]) -> dict:
    return {
        "pmid": record["pmid"],
        "year": record["year"],
        "pubmed_free_full_text_link": "yes" if record["pmid"] in free else "no",
        "pmcid": record["identifiers"].get("pmc", ""),
        "type": "; ".join(record["publication_types"]),
        "doi": record["identifiers"].get("doi", ""),
        "journal": record["journal"]["iso_abbreviation"] or record["journal"]["title"],
        "title": record["title"],
        "abstract": abstract_text(record),
    }


# --------------------------------------------------------------------------- harvest

def harvest(term: str) -> tuple[list[dict], dict]:
    result = search(term)
    count = result["count"]
    if not count:
        raise HarvestError(f"no records for: {term}")
    records: list[dict] = []
    unknown_tags: set[str] = set()
    for start in range(0, count, BATCH):
        payload = _request("efetch.fcgi", {
            "db": "pubmed", "query_key": result["query_key"], "WebEnv": result["webenv"],
            "retstart": str(start), "retmax": str(BATCH), "retmode": "xml"})
        unknown_tags |= unparsed_record_tags(payload)
        records.extend(parse(payload))
        print(f"  fetched {min(start + BATCH, count)}/{count}", file=sys.stderr, flush=True)

    seen = [r["pmid"] for r in records]
    if unknown_tags:
        raise HarvestError(
            f"unhandled record type(s) {sorted(unknown_tags)}: records of a type this parser "
            "does not know would be dropped without a trace. Add a parser before harvesting.")
    if len(seen) != count:
        raise HarvestError(
            f"incomplete harvest: ESearch reported {count} records, {len(seen)} were parsed. "
            "A page was dropped or a record type went unparsed.")
    if len(set(seen)) != len(seen):
        raise HarvestError(
            f"duplicate records: {len(seen)} fetched, {len(set(seen))} distinct PMIDs. A page "
            "was served twice and the count cannot be trusted.")

    free = uids(f"({term}) AND ffrft[Filter]")
    records.sort(key=lambda r: int(r["pmid"]))
    free_here = {r["pmid"] for r in records if r["pmid"] in free}
    manifest = {
        "harvester_version": HARVESTER_VERSION,
        "harvested_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "query_as_sent": term,
        "query_translation": result["query_translation"],
        "expected_count": count,
        "parsed_count": len(records),
        "distinct_pmids": len(set(seen)),
        "record_types": sorted({r["record_type"] for r in records}),
        "pubmed_free_full_text_links": sum(1 for r in records if r["pmid"] in free),
        "with_abstract": sum(1 for r in records if r["abstract_parts"]),
        "with_other_abstract": sum(1 for r in records if r["other_abstracts"]),
        "with_corrections": sum(1 for r in records if r["corrections"]),
        "invariants_asserted": [
            "parsed_count == expected_count",
            "distinct_pmids == parsed_count",
            "every record-level tag has a parser",
        ],
        "not_claimed": (
            "This is every record returned by the query above at the timestamp above, not "
            "'every paper on the gene'. PubMed applies Automatic Term Mapping; the "
            "query_translation field records what was actually run. "
            "pubmed_free_full_text_link=no means PubMed exposes no link it classifies as "
            "free — it does not mean paywalled."),
        "source": "NCBI E-utilities. Abstracts may be under publisher copyright; check terms "
                  "before redistributing.",
        # 🔴 The hazard this corpus creates. Hundreds of abstracts, local and greppable, are a
        # standing temptation to answer from them — which is the exact failure the parity-of-
        # sources principle exists to prevent, and which `grep as a method of analysis` is
        # already forbidden for. The convenience is real and so is the risk, so the permitted
        # uses are declared in the artefact itself rather than left to memory.
        "evidential_status": "NOT_EVIDENCE",
        "permitted_uses": [
            "triage, deduplication and priority ranking over titles and abstracts",
            "census: counting what exists against what the model has read",
            "export pre-flight: checking whether an abstract carries a proposition BEFORE the "
            "full text is opened, so the anchor is captured while the document is open",
        ],
        "forbidden_uses": [
            "reading. An abstract is not the paper, and the decisive detail is routinely "
            "absent from it — on 2026-08-04 a figure panel reversed a conclusion the running "
            "text did not contain",
            "supporting a claim, a verbatim locator or a FULLTEXT_READ_RECEIPT. A receipt "
            "whose source is this file is refused by "
            "scripts/test_abstract_corpus_is_not_evidence.py",
            "substituting for a full-text read in the reading debt: a paper covered here is "
            "still unread",
        ],
    }
    return records, manifest, free_here


def _write_atomic(path: Path, write_body) -> str:
    """Write through a temporary file and rename. An interrupted run must not leave a stub."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".partial")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        write_body(handle)
    temporary.replace(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(records: list[dict], path: Path) -> str:
    def body(handle):
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")
    return _write_atomic(path, body)


def write_seed(records: list[dict], free: set[str], path: Path) -> str:
    def body(handle):
        writer = csv.DictWriter(handle, fieldnames=SEED_FIELDS, delimiter="\t",
                                quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(to_seed_row(r, free) for r in records)
    return _write_atomic(path, body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--term", required=True, help='PubMed query, e.g. "WWOX OR WOREE"')
    parser.add_argument("--out-dir", type=Path, help="destination directory")
    parser.add_argument("--slug", default="corpus", help="basename for the emitted files")
    parser.add_argument("--no-abstracts", action="store_true",
                        help="omit abstracts from the derived TSV (the JSONL keeps them)")
    parser.add_argument("--count-only", action="store_true")
    arguments = parser.parse_args()

    if not os.environ.get("NCBI_EMAIL"):
        print("NOTE: set NCBI_EMAIL so NCBI can contact you before blocking (E-utilities "
              "usage guidelines).", file=sys.stderr)

    try:
        if arguments.count_only:
            result = search(arguments.term)
            print(f"{result['count']} record(s)")
            print(f"query as sent   : {arguments.term}")
            print(f"PubMed ran      : {result['query_translation']}")
            return 0
        if not arguments.out_dir:
            print("ERROR: --out-dir is required unless --count-only", file=sys.stderr)
            return 2

        records, manifest, free = harvest(arguments.term)
        stem = arguments.out_dir / arguments.slug
        jsonl_sha = write_jsonl(records, stem.with_suffix(".jsonl"))
        seed_records = records
        if arguments.no_abstracts:
            seed_records = [{**r, "abstract_parts": []} for r in records]
        seed_sha = write_seed(seed_records, free, stem.with_suffix(".tsv"))
        manifest["outputs"] = {
            f"{arguments.slug}.jsonl": {"sha256": jsonl_sha, "lossless": True},
            f"{arguments.slug}.tsv": {"sha256": seed_sha, "lossless": False,
                                      "abstracts": not arguments.no_abstracts},
        }
        _write_atomic(stem.with_suffix(".manifest.json"),
                      lambda h: h.write(json.dumps(manifest, indent=2, sort_keys=True) + "\n"))
    except HarvestError as error:
        print(f"REFUSED: {error}", file=sys.stderr)
        return 1

    print(f"written under {arguments.out_dir}/ ({arguments.slug}.jsonl · .tsv · .manifest.json)")
    print(f"  {manifest['parsed_count']} record(s) · types {manifest['record_types']}")
    print(f"  {manifest['with_abstract']} with an abstract · "
          f"{manifest['with_other_abstract']} with a translated abstract · "
          f"{manifest['with_corrections']} carrying a correction/retraction notice")
    print(f"  {manifest['pubmed_free_full_text_links']} with a PubMed free-full-text link "
          f"({manifest['parsed_count'] - manifest['pubmed_free_full_text_links']} without — "
          "retrievability unknown, not necessarily paywalled)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
