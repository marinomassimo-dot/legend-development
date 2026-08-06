#!/usr/bin/env python3
"""Harvest a PubMed corpus from E-utilities: a record-level JSONL, a seed TSV, and a manifest.

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

Fidelity
--------
The JSONL is a **structured record-level projection**, not a copy of the DTD. It keeps
personal and collective authors with affiliations *and the role of the list they came from*,
both electronic and print dates, volume/issue/pagination/e-location, language, ISSN,
publication status, every article identifier, MeSH headings with their qualifiers, keywords,
chemicals, `CommentsCorrectionsList` (retractions, errata) with the source citation, and
`OtherAbstract` preserved *separately* with its language rather than folded into the abstract.
The TSV is a derived convenience for the batch queue and is lossy by design.

🔴 **The word "lossless" is retired.** It was in this docstring while every MeSH heading was
being dropped, and nothing could tell — an unqualified fidelity claim cannot be checked, so it
is not a claim, it is a mood. What is deliberately excluded is enumerated in `NOT_CAPTURED`
and republished in the manifest, and `test_every_pubmed_element_is_captured_or_named` fails on
any element that is neither captured nor named there.

Usage
-----
    pubmed_corpus_harvest.py --term "WWOX OR WOREE" --out-dir files/corpus
    pubmed_corpus_harvest.py --term "SCN1A" --count-only
    pubmed_corpus_harvest.py --verify files/corpus/corpus.manifest.json

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
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from corpus_firewall import CORPUS_ARTEFACT, names_a_corpus  # noqa: E402

HARVESTER_VERSION = "3.0"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "legend-corpus-harvest"
BATCH = 200
ESEARCH_UID_CEILING = 10000
RETRY_CEILING_SECONDS = 60.0

SEED_FIELDS = ("pmid", "year", "pubmed_free_full_text_link", "pmcid", "type", "doi",
               "journal", "corrections", "title", "abstract")
YEAR_RE = re.compile(r"(1[5-9]\d{2}|20\d{2}|21\d{2})")
SHA256_RE = re.compile(r"[a-f0-9]{64}")

# Record-level tags that are not records. `DeleteCitation` is how PubMed reports a UID
# withdrawn between the search and the fetch; treating it as an unknown type refused the whole
# harvest and blamed the parser for an upstream deletion.
NON_RECORD_TAGS = frozenset({"DeleteCitation"})

# 🔴 The guards that keep this corpus out of the evidence path recognise it by name AND, since
# 2026-08-06, by contents. Both live in `corpus_firewall`: one shared definition instead of
# four hand-maintained copies of one regex, which drift silently on both sides.
MANIFEST_SCHEMA_VERSION = 2
SUPPORTED_MANIFEST_SCHEMAS = (2,)

# What the JSONL deliberately does not carry. Enumerated, so the fidelity claim is checkable
# rather than asserted — and pinned by `test_every_pubmed_element_is_captured_or_named`, which
# walks a fixture and fails on any element that is neither captured nor listed here.
NOT_CAPTURED = (
    "MedlineCitation/@Owner",
    "MedlineCitation/@Status",
    "MedlineCitation/CitationSubset",
    "MedlineCitation/CoiStatement",
    "MedlineCitation/GeneralNote",
    "MedlineCitation/GeneSymbolList",
    "MedlineCitation/InvestigatorList",
    "MedlineCitation/MedlineJournalInfo",
    "MedlineCitation/NumberOfReferences",
    "MedlineCitation/PersonalNameSubjectList",
    "MedlineCitation/SpaceFlightMission",
    "MedlineCitation/SupplMeshList",
    "MedlineCitation/Article/Abstract/@CopyrightInformation is kept; the rest of "
    "Article/DataBankList is not",
    "MedlineCitation/Article/GrantList",
    "MedlineCitation/Article/VernacularTitle when an ArticleTitle exists",
    "PubmedData/ReferenceList",
    "PubmedData/History beyond PubMedPubDate",
    "PubmedBookData/@ objects beyond PublicationStatus and ArticleIdList",
)


class HarvestError(RuntimeError):
    """A refusal. Every one of these means the corpus would have been silently incomplete."""


class TransientHarvestError(HarvestError):
    """A response that may succeed on retry — a truncated body, a reset connection.

    Distinct from `HarvestError` because the retry loop must retry it and must NOT retry a
    permanent refusal: five backoffs against "Invalid db name" waste fifteen seconds and
    report a transport failure for a query error.
    """


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
                wait = _retry_after(error.headers.get("Retry-After"), attempt)
            elif 500 <= error.code < 600:
                wait = min(2 ** attempt, RETRY_CEILING_SECONDS)
            else:
                raise HarvestError(f"E-utilities {endpoint} returned HTTP {error.code}")
            time.sleep(wait + random.uniform(0, 0.5))
        except TransientHarvestError as error:
            last = error
            time.sleep(min(2 ** attempt, RETRY_CEILING_SECONDS) + random.uniform(0, 0.5))
        except HarvestError:
            # A malformed query does not become well-formed by asking again.
            raise
        except Exception as error:                       # noqa: BLE001 — retried, then raised
            last = error
            time.sleep(min(2 ** attempt, RETRY_CEILING_SECONDS) + random.uniform(0, 0.5))
    raise HarvestError(f"E-utilities {endpoint} failed after {retries} attempts: {last}")


def _retry_after(header: str | None, attempt: int) -> float:
    """Seconds to wait after a 429. `Retry-After` may be a count OR an HTTP-date.

    `float("Wed, 21 Oct 2015 07:28:00 GMT")` raises inside the exception handler, so a 429 —
    the one response this loop exists to survive — crashed the harvest with a ValueError
    traceback instead of backing off. The cap matters too: a header of 86400 is a day-long
    sleep no operator is watching.
    """
    fallback = min(2 ** attempt, RETRY_CEILING_SECONDS)
    if not header or not header.strip():
        return fallback
    try:
        seconds = float(header.strip())
    except ValueError:
        try:
            moment = parsedate_to_datetime(header.strip())
        except (TypeError, ValueError):
            return fallback
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=timezone.utc)
        seconds = (moment - datetime.now(timezone.utc)).total_seconds()
    return max(0.0, min(seconds, RETRY_CEILING_SECONDS))


def _raise_on_xml_error(data: bytes) -> None:
    """E-utilities answers HTTP 200 with an <ERROR> body. A 200 is not a success.

    A body that does not parse is not a success either. The first version returned quietly on
    `ParseError`, so a truncated page — the ordinary failure of a long efetch — passed the
    check and crashed later inside `parse()` with a bare traceback, unretried. Every response
    on this path is XML by construction (`retmode=xml`), so unparseable means damaged.
    """
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise TransientHarvestError(
            f"response body is not parseable XML ({error}); it was truncated or damaged in "
            "transit") from error
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
    """Every `Author`, carrying the role of the list it came from.

    A `BookDocument` has two `AuthorList` elements — `Type="authors"` and `Type="editors"`.
    `iter("Author")` flattens both, so the editors of GeneReviews were recorded as authors of
    every chapter: real names, wrong relationship to the work, and nothing in the record said
    which was which.
    """
    people = []
    for group in (article.iter("AuthorList") if article is not None else []):
        role = _clean(group.attrib.get("Type", "")) or "authors"
        for author in group.iter("Author"):
            entry = {
                "role": role,
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


def _mesh(citation: ET.Element | None) -> list[dict]:
    """MeSH headings with their qualifiers and major-topic flags.

    The field a census actually ranks on, and the one the `lossless` claim quietly excluded:
    706 records were harvested with no MeSH at all and nothing said so.
    """
    headings = []
    for heading in (citation.iter("MeshHeading") if citation is not None else []):
        descriptor = heading.find("DescriptorName")
        if descriptor is None or not _clean(descriptor.text):
            continue
        headings.append({
            "descriptor": _clean(descriptor.text),
            "ui": descriptor.attrib.get("UI", ""),
            "major": descriptor.attrib.get("MajorTopicYN", "N") == "Y",
            "qualifiers": [{"name": _clean(node.text),
                            "ui": node.attrib.get("UI", ""),
                            "major": node.attrib.get("MajorTopicYN", "N") == "Y"}
                           for node in heading.iter("QualifierName") if _clean(node.text)],
        })
    return headings


def _keywords(citation: ET.Element | None) -> list[dict]:
    """Author keywords. `Owner` lives on the list, not on the term."""
    terms = []
    for group in (citation.iter("KeywordList") if citation is not None else []):
        owner = group.attrib.get("Owner", "")
        for node in group.iter("Keyword"):
            term = _clean("".join(node.itertext()))
            if term:
                terms.append({"term": term, "owner": owner,
                              "major": node.attrib.get("MajorTopicYN", "N") == "Y"})
    return terms


def _chemicals(citation: ET.Element | None) -> list[dict]:
    """Substances PubMed indexed the record under — the closest thing to a drug annotation."""
    out = []
    for node in (citation.iter("Chemical") if citation is not None else []):
        substance = node.find("NameOfSubstance")
        if substance is None or not _clean(substance.text):
            continue
        out.append({"name": _clean(substance.text),
                    "ui": substance.attrib.get("UI", ""),
                    "registry_number": _clean(node.findtext("RegistryNumber"))})
    return out


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
    """Retractions, errata and comments — the reason a paper may need to leave the model.

    🔴 `node.find("RefSource") or ET.Element("x")` is the exact trap `_text` documents three
    functions above: a `RefSource` has text and no CHILDREN, so it is falsy, so the fallback
    won every time. All 40 correction notices in the 2026-08-05 harvest carried an empty
    `citation` inside a file the manifest called lossless, and nothing looked wrong: the
    `ref_type` and the `pmid` were right, and only the human-readable source was gone.
    """
    out = []
    for node in citation.iter("CommentsCorrections"):
        out.append({"ref_type": node.attrib.get("RefType", ""),
                    "pmid": _clean(node.findtext("PMID")),
                    "citation": _text(node, "RefSource")})
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
        "mesh_headings": _mesh(citation),
        "keywords": _keywords(citation),
        "chemicals": _chemicals(citation),
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
        "mesh_headings": _mesh(document),
        "keywords": _keywords(document),
        "chemicals": _chemicals(document),
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
    return {child.tag for child in root
            if child.tag not in PARSERS and child.tag not in NON_RECORD_TAGS}


def deleted_pmids(xml_bytes: bytes) -> set[str]:
    """UIDs PubMed reports as deleted between the search and the fetch.

    These arrive as `<DeleteCitation>`, which is not a record and has no parser. Treating it as
    an unknown record type refused the entire harvest and told the operator to write a parser
    for it — for a tag whose whole content is "this PMID no longer exists". Counting them keeps
    the completeness invariant exact instead of blocking on an upstream deletion.
    """
    root = ET.fromstring(xml_bytes)
    return {_clean(node.text) for child in root if child.tag == "DeleteCitation"
            for node in child.iter("PMID") if _clean(node.text)}


# --------------------------------------------------------------------------- derivation

def abstract_text(record: dict) -> str:
    return _clean(" ".join(
        f"{p['label']}: {p['text']}" if p["label"] else p["text"]
        for p in record["abstract_parts"] if p["text"]))


def strip_abstracts(record: dict) -> dict:
    """Every surface an abstract can reach: the main text, translations, and the copyright
    line that comes attached to it. Removing one of three is not removing the abstract."""
    return {**record, "abstract_parts": [], "other_abstracts": [], "copyright": ""}


def correction_flags(record: dict) -> str:
    """`RetractionIn:12345678; ExpressionOfConcernIn:87654321`, or empty.

    The JSONL has carried these all along and the triage surface did not, so a paper under an
    expression of concern reached the queue looking exactly like a clean one. 40 of 706
    records carry a notice; the ones that matter are unreadable from the TSV alone.
    """
    return "; ".join(
        f"{item['ref_type'] or 'Correction'}:{item['pmid'] or item['citation'] or '?'}"
        for item in record.get("corrections", []))


def to_seed_row(record: dict, free: set[str]) -> dict:
    return {
        "pmid": record["pmid"],
        "year": record["year"],
        "pubmed_free_full_text_link": "yes" if record["pmid"] in free else "no",
        "pmcid": record["identifiers"].get("pmc", ""),
        "type": "; ".join(record["publication_types"]),
        "doi": record["identifiers"].get("doi", ""),
        "journal": record["journal"]["iso_abbreviation"] or record["journal"]["title"],
        "corrections": correction_flags(record),
        "title": record["title"],
        "abstract": abstract_text(record),
    }


# --------------------------------------------------------------------------- harvest

def harvest(term: str) -> tuple[list[dict], dict, set[str]]:
    result = search(term)
    count = result["count"]
    if not count:
        raise HarvestError(f"no records for: {term}")
    records: list[dict] = []
    unknown_tags: set[str] = set()
    deleted: set[str] = set()
    for start in range(0, count, BATCH):
        payload = _request("efetch.fcgi", {
            "db": "pubmed", "query_key": result["query_key"], "WebEnv": result["webenv"],
            "retstart": str(start), "retmax": str(BATCH), "retmode": "xml"})
        unknown_tags |= unparsed_record_tags(payload)
        deleted |= deleted_pmids(payload)
        records.extend(parse(payload))
        print(f"  fetched {min(start + BATCH, count)}/{count}", file=sys.stderr, flush=True)

    seen = [r["pmid"] for r in records]
    if unknown_tags:
        raise HarvestError(
            f"unhandled record type(s) {sorted(unknown_tags)}: records of a type this parser "
            "does not know would be dropped without a trace. Add a parser before harvesting.")
    if len(seen) + len(deleted) != count:
        raise HarvestError(
            f"incomplete harvest: ESearch reported {count} records, {len(seen)} were parsed "
            f"and {len(deleted)} were reported deleted by PubMed. A page was dropped or a "
            "record type went unparsed.")
    if len(set(seen)) != len(seen):
        raise HarvestError(
            f"duplicate records: {len(seen)} fetched, {len(set(seen))} distinct PMIDs. A page "
            "was served twice and the count cannot be trusted.")

    free = uids(f"({term}) AND ffrft[Filter]")
    records.sort(key=lambda r: int(r["pmid"]))
    free_here = {r["pmid"] for r in records if r["pmid"] in free}
    manifest = {
        "harvester_version": HARVESTER_VERSION,
        "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
        "harvested_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "query_as_sent": term,
        "query_translation": result["query_translation"],
        "expected_count": count,
        "parsed_count": len(records),
        "distinct_pmids": len(set(seen)),
        "deleted_by_pubmed": sorted(deleted),
        "record_types": sorted({r["record_type"] for r in records}),
        "pubmed_free_full_text_links": sum(1 for r in records if r["pmid"] in free),
        "with_abstract": sum(1 for r in records if r["abstract_parts"]),
        "with_abstract_text": sum(1 for r in records if abstract_text(r)),
        "with_other_abstract": sum(1 for r in records if r["other_abstracts"]),
        "with_mesh": sum(1 for r in records if r["mesh_headings"]),
        "with_corrections": sum(1 for r in records if r["corrections"]),
        "invariants_asserted": [
            "parsed_count + len(deleted_by_pubmed) == expected_count",
            "distinct_pmids == parsed_count",
            "every record-level tag has a parser",
        ],
        # An abstract PubMed never had and an abstract this parser failed to read are
        # different facts, and one count cannot carry both. `with_abstract` counts records
        # holding an <Abstract> block; `with_abstract_text` counts those whose block yields
        # text. A gap between them is a parsing failure, not an absent abstract.
        "not_captured": list(NOT_CAPTURED),
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


def output_path(out_dir: Path, slug: str, extension: str) -> Path:
    """`out_dir/slug.extension`, by concatenation.

    `(out_dir / slug).with_suffix(".jsonl")` REPLACES everything after the last dot in the
    slug: `--slug wwox.v2` wrote `wwox.jsonl` while the manifest recorded a checksum under the
    key `wwox.v2.jsonl` — a manifest describing files that do not exist.
    """
    return out_dir / f"{slug}{extension}"


def refuse_bad_slug(slug: str) -> None:
    """A slug is a filename, not a path.

    `--slug ../../staging/wwox` walked out of the destination while every name-based check
    still saw the directory it was told about. A slug that is not a bare basename is refused
    rather than sanitised: silently rewriting what the operator asked for is how you get a
    corpus somewhere nobody looks.
    """
    if not slug or slug != Path(slug).name or slug in {".", ".."} or slug.startswith("."):
        raise HarvestError(
            f"--slug must be a bare filename, got {slug!r}. Separators and `..` let the "
            "output escape the destination the firewall was shown.")


def refuse_unrecognised_destination(paths: list[Path]) -> None:
    """Refuse to write a corpus where the evidence firewall cannot see it.

    🔴 Reviewed 2026-08-06: this check read the path as a *string*, so
    `files/corpus/../../staging/wwox.jsonl` passed — it contains `files/corpus/` and is not in
    `files/corpus/` at all. A check that accepts the one input it exists to refuse is worse
    than no check, because it is reported as a closed risk. `names_a_corpus` resolves first.

    This remains the weaker half of the firewall by construction: it enforces the naming
    convention where corpora are created, so the paths the guards match are the paths that
    exist. It cannot survive a later `cp` or `mv`, which is why the writers now also refuse by
    file *contents* — see `corpus_firewall.looks_like_corpus`.
    """
    unseen = [str(path) for path in paths if not names_a_corpus(str(path))]
    if unseen:
        raise HarvestError(
            "destination not recognised as a corpus by the evidence firewall: "
            f"{unseen}. Write under a `files/corpus/` directory, or use a slug containing "
            "`corpus_seed_pubmed` (the naming the registry seeds already use).")


def _stage(path: Path, write_body) -> Path:
    """Write the body to `<path>.partial`. Nothing is visible under its real name yet.

    A body that raises mid-write must take its own temporary with it: the caller never
    received the path, so nobody else can clean it up.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    # Process-unique: a fixed `.partial` name means two harvests of the same slug write the
    # same temporary and one promotes the other's half-written bytes.
    temporary = path.with_name(f"{path.name}.{os.getpid()}.partial")
    try:
        with temporary.open("w", encoding="utf-8", newline="") as handle:
            write_body(handle)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    return temporary


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_atomic(path: Path, write_body) -> str:
    """Write through a temporary file and rename. An interrupted run must not leave a stub."""
    temporary = _stage(path, write_body)
    temporary.replace(path)
    return _digest(path)


def jsonl_body(records: list[dict]):
    def body(handle):
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")
    return body


def seed_body(records: list[dict], free: set[str], *, include_abstract: bool = True):
    def body(handle):
        fields = SEED_FIELDS if include_abstract else tuple(
            field for field in SEED_FIELDS if field != "abstract")
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t",
                                quoting=csv.QUOTE_MINIMAL, extrasaction="ignore",
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(to_seed_row(r, free) for r in records)
    return body


def write_jsonl(records: list[dict], path: Path) -> str:
    return _write_atomic(path, jsonl_body(records))


def write_seed(records: list[dict], free: set[str], path: Path) -> str:
    return _write_atomic(path, seed_body(records, free))


def write_corpus(records: list[dict], manifest: dict, free: set[str],
                 out_dir: Path, slug: str, *, abstracts: bool = True) -> dict:
    """Emit the three artefacts as a set, or emit none of them.

    Each file was already written atomically, but not the *set*: a manifest that failed to
    write left a JSONL and a TSV on disk carrying no terms of use, no query translation and no
    checksums — exactly the artefact the firewall assumes cannot exist, because its whole
    design is that the corpus declares its own status. Staging all three and promoting last
    shrinks that window from a network round-trip to a rename.

    Three renames are still three renames, and POSIX gives no way to make them one. What
    closes the remaining window is the *order* plus a reader that checks: the manifest is
    promoted last and carries the checksums of the other two, so a set torn between the first
    and third rename has a manifest that no longer describes its own files, and `verify()`
    says so. A partial set is detectable rather than prevented — claiming otherwise would be
    the same kind of overstatement as calling the JSONL lossless.
    """
    refuse_bad_slug(slug)
    targets = {extension: output_path(out_dir, slug, extension)
               for extension in (".jsonl", ".tsv", ".manifest.json")}
    refuse_unrecognised_destination(list(targets.values()))

    # 🔴 `--no-abstracts` used to strip the TSV and leave every abstract in the JSONL beside
    # it. The flag was documented that way, which made it worse rather than better: the
    # documented refresh command sends `--no-abstracts` to `disease-models/wwox/registries`,
    # a *tracked* directory, so an operator asking for a safe bibliographic export got 706
    # publisher-copyright abstracts written into the publishable tree. A flag named for what
    # it removes must remove it from everything it writes.
    emitted = records if abstracts else [strip_abstracts(r) for r in records]
    staged: dict[str, Path] = {}
    try:
        staged[".jsonl"] = _stage(targets[".jsonl"], jsonl_body(emitted))
        staged[".tsv"] = _stage(
            targets[".tsv"], seed_body(emitted, free, include_abstract=abstracts))
        manifest["outputs"] = {
            f"{slug}.jsonl": {"sha256": _digest(staged[".jsonl"]),
                              "content": "full record, minus not_captured"},
            f"{slug}.tsv": {"sha256": _digest(staged[".tsv"]),
                            "content": "derived triage convenience — lossy by design",
                            "abstracts": abstracts},
        }
        staged[".manifest.json"] = _stage(
            targets[".manifest.json"],
            lambda handle: handle.write(json.dumps(manifest, indent=2, sort_keys=True) + "\n"))
        for extension, temporary in staged.items():
            temporary.replace(targets[extension])
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)
    return {extension: path for extension, path in targets.items()}


def verify(manifest_path: Path) -> list[str]:
    """Re-check a corpus already on disk against its own manifest.

    Nothing did this. The manifest recorded a SHA-256 for every output and no code ever read
    it back, so a truncated, hand-edited or half-copied corpus was indistinguishable from a
    good one — and the corpus harvested on 2026-08-05 carried `harvester_version: 2.0` while
    holding none of the terms of use that version was supposed to write, because the schema
    changed without the version moving. A version that does not move is not a version.
    """
    problems: list[str] = []
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"manifest unreadable: {error}"]

    for field in ("evidential_status", "permitted_uses", "forbidden_uses", "not_claimed",
                  "query_as_sent", "query_translation", "harvested_at_utc", "expected_count"):
        if not manifest.get(field):
            problems.append(f"manifest carries no `{field}` — it predates the terms of use "
                            "the evidence firewall assumes every corpus declares")
    if manifest.get("evidential_status") not in (None, "NOT_EVIDENCE"):
        problems.append(f"evidential_status is {manifest['evidential_status']!r}, not "
                        "NOT_EVIDENCE")

    # A snapshot is history: it does not become wrong because the harvester moved on. What
    # must be current is the *schema*, so the version check is a supported range, not equality
    # — otherwise every compatible release retroactively invalidates every archived corpus and
    # the check trains people to ignore it.
    schema = manifest.get("manifest_schema_version")
    if schema is None:
        problems.append(
            "manifest declares no `manifest_schema_version`; it predates the schema that "
            "carries the terms of use. Re-harvest before relying on the record-level fields.")
    elif schema not in SUPPORTED_MANIFEST_SCHEMAS:
        problems.append(f"manifest schema {schema!r} is outside the supported range "
                        f"{list(SUPPORTED_MANIFEST_SCHEMAS)}")

    expected_total = manifest.get("expected_count")
    parsed = manifest.get("parsed_count")
    deleted = manifest.get("deleted_by_pubmed") or []
    if isinstance(expected_total, int) and isinstance(parsed, int):
        if parsed + len(deleted) != expected_total:
            problems.append(
                f"the manifest contradicts its own invariant: parsed {parsed} + deleted "
                f"{len(deleted)} != expected {expected_total}")

    outputs = manifest.get("outputs") or {}
    if not outputs:
        problems.append("manifest records no outputs — nothing can be checked against it")
    for name, entry in sorted(outputs.items()):
        path = manifest_path.parent / name
        if not path.is_file():
            problems.append(f"{name}: declared in the manifest, absent from disk")
            continue
        expected = (entry or {}).get("sha256", "")
        if not SHA256_RE.fullmatch(str(expected)):
            # An absent checksum silently skipped the comparison, so the weakest manifest got
            # the cleanest verdict.
            problems.append(f"{name}: manifest records no usable sha256, so this file cannot "
                            "be verified at all")
        elif _digest(path) != expected:
            problems.append(f"{name}: sha256 {_digest(path)} does not match the manifest "
                            f"{expected}")
        if name.endswith(".jsonl"):
            problems.extend(_verify_jsonl(path, name, parsed))
    return problems


def _tracked_destination(path: Path) -> bool:
    """True when git would keep this file — so abstracts must not be written there.

    Fails toward `True`: if git cannot answer, the advice is to strip the abstracts. Being
    told to drop them from a gitignored corpus costs a re-harvest; the other error publishes
    700 abstracts under publisher copyright.
    """
    try:
        completed = subprocess.run(
            ["git", "check-ignore", "-q", str(path)],
            cwd=path.parent if path.parent.exists() else Path.cwd(),
            capture_output=True, timeout=10, check=False)
    except (OSError, subprocess.SubprocessError):
        return True
    return completed.returncode != 0


def _verify_jsonl(path: Path, name: str, parsed: Any) -> list[str]:
    """Count and de-duplicate the records, reporting damage instead of raising it.

    A corrupt corpus is exactly the input this command exists for; answering it with a
    JSONDecodeError traceback tells the operator the *checker* is broken.
    """
    pmids: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8",
                                                 errors="replace").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            return [f"{name}: line {number} is not valid JSON ({error.msg}); the file is "
                    "damaged and its counts cannot be checked"]
        if not isinstance(record, dict) or not record.get("pmid"):
            return [f"{name}: line {number} carries no pmid; this is not a corpus record"]
        pmids.append(record["pmid"])
    problems = []
    if isinstance(parsed, int) and parsed != len(pmids):
        problems.append(f"{name}: holds {len(pmids)} records, manifest claims {parsed}")
    if len(set(pmids)) != len(pmids):
        problems.append(f"{name}: {len(pmids) - len(set(pmids))} duplicate PMID(s)")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--term", help='PubMed query, e.g. "WWOX OR WOREE"')
    parser.add_argument("--out-dir", type=Path, help="destination directory")
    parser.add_argument("--slug", default="corpus", help="basename for the emitted files")
    parser.add_argument("--no-abstracts", action="store_true",
                        help="omit abstracts, translated abstracts and the abstract copyright "
                             "line from BOTH emitted files — use it for any destination that "
                             "is tracked by git")
    parser.add_argument("--count-only", action="store_true")
    parser.add_argument("--verify", type=Path, metavar="MANIFEST",
                        help="re-check a corpus already on disk against its own manifest")
    arguments = parser.parse_args()

    if arguments.verify:
        problems = verify(arguments.verify)
        for problem in problems:
            print(f"  ✗ {problem}")
        print(f"{arguments.verify}: {'FAIL' if problems else 'OK'} "
              f"({len(problems)} problem(s))")
        # A checker that reports a corpus red and stops has handed the operator a problem, not
        # a finding. Both corpora on disk predate the schema that carries the terms of use;
        # the remediation is one command and it belongs here, next to the verdict.
        if any("predates" in problem for problem in problems):
            manifest = json.loads(arguments.verify.read_text(encoding="utf-8"))
            slug = arguments.verify.name.replace(".manifest.json", "")
            print("\nThis corpus predates the current schema. Re-harvest it in place:\n"
                  f"  python3 {Path(__file__).name} \\\n"
                  f"      --term {manifest.get('query_as_sent', '<term>')!r} \\\n"
                  f"      --out-dir {arguments.verify.parent} \\\n"
                  f"      --slug {slug}"
                  f"{' --no-abstracts' if _tracked_destination(arguments.verify) else ''}"
                  "\nThe old snapshot stays valid as dated history; re-harvesting produces a "
                  "new one, it does not repair the old.")
        return 1 if problems else 0

    if not arguments.term:
        print("ERROR: --term is required unless --verify", file=sys.stderr)
        return 2

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
        write_corpus(records, manifest, free, arguments.out_dir, arguments.slug,
                     abstracts=not arguments.no_abstracts)
    except HarvestError as error:
        print(f"REFUSED: {error}", file=sys.stderr)
        return 1

    print(f"written under {arguments.out_dir}/ ({arguments.slug}.jsonl · .tsv · .manifest.json)")
    print(f"  {manifest['parsed_count']} record(s) · types {manifest['record_types']}"
          + (f" · {len(manifest['deleted_by_pubmed'])} deleted upstream"
             if manifest["deleted_by_pubmed"] else ""))
    print(f"  {manifest['with_abstract_text']} with abstract text · "
          f"{manifest['with_mesh']} with MeSH · "
          f"{manifest['with_other_abstract']} with a translated abstract · "
          f"{manifest['with_corrections']} carrying a correction/retraction notice")
    print(f"  {manifest['pubmed_free_full_text_links']} with a PubMed free-full-text link "
          f"({manifest['parsed_count'] - manifest['pubmed_free_full_text_links']} without — "
          "retrievability unknown, not necessarily paywalled)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
