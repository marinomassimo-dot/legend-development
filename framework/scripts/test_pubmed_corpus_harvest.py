#!/usr/bin/env python3
"""Parsing and completeness regressions for the PubMed corpus harvester.

Every case here is a defect that produced a *plausible* corpus, not a crash. A parser that
raises is fixed the same minute; one that quietly drops a record type, or truncates a date to
"Wint", ships a corpus nobody can tell is wrong.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "harvest", ROOT / "framework/scripts/pubmed_corpus_harvest.py")
harvest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(harvest)


ARTICLE = """
 <PubmedArticle>
  <MedlineCitation>
   <PMID>36779245</PMID>
   <Article>
    <Journal><Title>Epilepsia</Title><ISOAbbreviation>Epilepsia</ISOAbbreviation>
     <ISSN>1528-1167</ISSN>
     <JournalIssue><Volume>64</Volume><Issue>5</Issue>
      <PubDate><Year>2023</Year></PubDate></JournalIssue></Journal>
    <ArticleTitle>WWOX developmental and epileptic encephalopathy</ArticleTitle>
    <Pagination><MedlinePgn>1351-1367</MedlinePgn></Pagination>
    <ELocationID EIdType="doi">10.1111/epi.17542</ELocationID>
    <Abstract><AbstractText Label="OBJECTIVE" NlmCategory="OBJECTIVE">Recessive.</AbstractText>
     <AbstractText Label="METHODS">Thirteen patients.</AbstractText>
     <CopyrightInformation>(c) 2023 the authors.</CopyrightInformation></Abstract>
    <AuthorList>
     <Author><LastName>Oliver</LastName><ForeName>Karen L</ForeName><Initials>KL</Initials>
      <AffiliationInfo><Affiliation>Epilepsy Research Centre</Affiliation></AffiliationInfo>
      <Identifier Source="ORCID">0000-0002-0000-0001</Identifier></Author>
     <Author><CollectiveName>The WWOX Study Group</CollectiveName></Author>
    </AuthorList>
    <Language>eng</Language>
    <PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList>
   </Article>
   <OtherAbstract Type="Publisher" Language="fre">
    <AbstractText>Un resume en francais.</AbstractText></OtherAbstract>
   <CommentsCorrectionsList>
    <CommentsCorrections RefType="RetractionIn"><PMID>42464650</PMID>
     <RefSource>Int J Mol Med. 2026</RefSource></CommentsCorrections>
   </CommentsCorrectionsList>
  </MedlineCitation>
  <PubmedData>
   <PublicationStatus>ppublish</PublicationStatus>
   <ArticleIdList>
    <ArticleId IdType="pubmed">36779245</ArticleId>
    <ArticleId IdType="pmc">PMC10952634</ArticleId>
    <ArticleId IdType="doi">10.1111/epi.17542</ArticleId>
   </ArticleIdList>
   <ReferenceList><Reference><ArticleIdList>
    <ArticleId IdType="pmc">PMC9068835</ArticleId>
    <ArticleId IdType="doi">10.1111/epi.17547</ArticleId>
   </ArticleIdList></Reference></ReferenceList>
  </PubmedData>
 </PubmedArticle>"""

# A record type the first version ignored entirely: requested {1, 2}, returned {1}.
BOOK = """
 <PubmedBookArticle>
  <BookDocument>
   <PMID>29262231</PMID>
   <Book><BookTitle>GeneReviews</BookTitle>
    <PubDate><MedlineDate>Winter 2024</MedlineDate></PubDate></Book>
   <ArticleTitle>WWOX-Related Disorders</ArticleTitle>
   <Abstract><AbstractText>A chapter abstract.</AbstractText></Abstract>
   <AuthorList><Author><LastName>Aldaz</LastName><ForeName>C Marcelo</ForeName></Author>
   </AuthorList>
   <PublicationTypeList><PublicationType>Review</PublicationType></PublicationTypeList>
  </BookDocument>
  <PubmedBookData><PublicationStatus>epublish</PublicationStatus>
   <ArticleIdList><ArticleId IdType="pubmed">29262231</ArticleId></ArticleIdList>
  </PubmedBookData>
 </PubmedBookArticle>"""

PLAIN = """
 <PubmedArticle>
  <MedlineCitation><PMID>11111111</PMID>
   <Article><Journal><Title>Journal of Things</Title>
     <JournalIssue><PubDate><MedlineDate>Winter 2024</MedlineDate></PubDate></JournalIssue>
    </Journal>
    <ArticleTitle>Markup <i>inside</i> the title</ArticleTitle>
    <PublicationTypeList><PublicationType>Review</PublicationType></PublicationTypeList>
   </Article></MedlineCitation>
  <PubmedData><ArticleIdList>
   <ArticleId IdType="pubmed">11111111</ArticleId></ArticleIdList></PubmedData>
 </PubmedArticle>"""


def document(*bodies: str) -> bytes:
    return ('<?xml version="1.0"?><PubmedArticleSet>' + "".join(bodies)
            + "</PubmedArticleSet>").encode("utf-8")


class RecordTypes(unittest.TestCase):
    def test_book_records_are_parsed_not_dropped(self) -> None:
        """The reviewer's adversarial case: ask for two records, get one back."""
        rows = harvest.parse(document(ARTICLE, BOOK))
        self.assertEqual({r["pmid"] for r in rows}, {"36779245", "29262231"})
        book = next(r for r in rows if r["pmid"] == "29262231")
        self.assertEqual(book["record_type"], "PubmedBookArticle")
        self.assertEqual(book["title"], "WWOX-Related Disorders")
        self.assertTrue(book["authors"])

    def test_an_unknown_record_tag_is_visible(self) -> None:
        payload = document(ARTICLE).replace(
            b"</PubmedArticleSet>", b"<PubmedFutureThing/></PubmedArticleSet>")
        self.assertIn("PubmedFutureThing", harvest.unparsed_record_tags(payload))


class Identifiers(unittest.TestCase):
    def test_identifiers_come_from_the_record_not_its_references(self) -> None:
        """PMID 36779245 carries 78 ArticleId elements live; three are its own."""
        row = harvest.parse(document(ARTICLE))[0]
        self.assertEqual(row["identifiers"]["pmc"], "PMC10952634")
        self.assertEqual(row["identifiers"]["doi"], "10.1111/epi.17542")
        self.assertNotIn("PMC9068835", row["identifiers"].values())


class TitlesAndDates(unittest.TestCase):
    def test_a_plain_text_title_survives(self) -> None:
        """An Element with no children is falsy; `find(...) or fallback` discarded 673/706."""
        row = harvest.parse(document(ARTICLE))[0]
        self.assertEqual(row["title"], "WWOX developmental and epileptic encephalopathy")

    def test_a_title_with_markup_keeps_its_words(self) -> None:
        row = harvest.parse(document(PLAIN))[0]
        self.assertEqual(row["title"], "Markup inside the title")

    def test_a_free_text_date_yields_a_year_not_four_characters(self) -> None:
        """`"Winter 2024"[:4]` gives "Wint". A year is a year or it is nothing."""
        rows = {r["pmid"]: r for r in harvest.parse(document(PLAIN, BOOK))}
        self.assertEqual(rows["11111111"]["year"], "2024")
        self.assertEqual(rows["29262231"]["year"], "2024")


class Losslessness(unittest.TestCase):
    def setUp(self) -> None:
        self.row = harvest.parse(document(ARTICLE))[0]

    def test_a_translated_abstract_is_kept_apart_not_discarded(self) -> None:
        self.assertNotIn("resume", harvest.abstract_text(self.row))
        other = self.row["other_abstracts"]
        self.assertEqual(other[0]["language"], "fre")
        self.assertIn("resume", other[0]["parts"][0]["text"])

    def test_abstract_labels_and_categories_are_preserved(self) -> None:
        first = self.row["abstract_parts"][0]
        self.assertEqual(first["label"], "OBJECTIVE")
        self.assertEqual(first["category"], "OBJECTIVE")

    def test_retraction_notices_are_structured(self) -> None:
        correction = self.row["corrections"][0]
        self.assertEqual(correction["ref_type"], "RetractionIn")
        self.assertEqual(correction["pmid"], "42464650")

    def test_authors_keep_affiliations_collectives_and_orcid(self) -> None:
        people = self.row["authors"]
        self.assertEqual(people[0]["affiliations"], ["Epilepsy Research Centre"])
        self.assertEqual(people[0]["identifiers"]["ORCID"], "0000-0002-0000-0001")
        self.assertEqual(people[1]["collective_name"], "The WWOX Study Group")

    def test_bibliographic_detail_is_kept(self) -> None:
        self.assertEqual(self.row["journal"]["volume"], "64")
        self.assertEqual(self.row["journal"]["issue"], "5")
        self.assertEqual(self.row["journal"]["issn"], ["1528-1167"])
        self.assertEqual(self.row["pagination"], "1351-1367")
        self.assertEqual(self.row["language"], ["eng"])
        self.assertEqual(self.row["publication_status"], "ppublish")
        self.assertIn("2023", self.row["copyright"])


class Naming(unittest.TestCase):
    def test_the_free_full_text_column_does_not_claim_a_paywall(self) -> None:
        """`no` means PubMed exposes no link it classifies as free — not 'paywalled'."""
        self.assertIn("pubmed_free_full_text_link", harvest.SEED_FIELDS)
        self.assertNotIn("free_full_text", harvest.SEED_FIELDS)


class Output(unittest.TestCase):
    def test_seed_rows_cannot_break_the_tsv(self) -> None:
        rows = harvest.parse(document(ARTICLE, BOOK, PLAIN))
        for record in rows:
            for field, value in harvest.to_seed_row(record, set()).items():
                with self.subTest(pmid=record["pmid"], field=field):
                    self.assertNotIn("\t", value)
                    self.assertNotIn("\n", value)

    def test_writes_are_atomic_and_leave_no_partial_file(self) -> None:
        rows = harvest.parse(document(ARTICLE))
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "corpus.jsonl"
            digest = harvest.write_jsonl(rows, target)
            self.assertEqual(len(digest), 64)
            self.assertFalse(list(Path(tmp).glob("*.partial")))
            back = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(back), 1)

    def test_seed_round_trips(self) -> None:
        rows = harvest.parse(document(ARTICLE, BOOK))
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "corpus.tsv"
            harvest.write_seed(rows, {"36779245"}, target)
            with target.open(encoding="utf-8") as handle:
                back = {r["pmid"]: r for r in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual(back["36779245"]["pubmed_free_full_text_link"], "yes")
        self.assertEqual(back["29262231"]["pubmed_free_full_text_link"], "no")


class Refusals(unittest.TestCase):
    """Every one of these is a corpus that would otherwise have shipped silently short."""

    def test_the_ceiling_is_a_refusal_not_a_truncation(self) -> None:
        original = harvest.search
        harvest.search = lambda term: {"count": 10001, "webenv": "W", "query_key": "1",
                                       "query_translation": term}
        try:
            with self.assertRaises(harvest.HarvestError) as caught:
                harvest.uids("anything")
        finally:
            harvest.search = original
        self.assertIn("ceiling", str(caught.exception))

    def test_an_xml_error_body_is_not_a_success(self) -> None:
        """E-utilities answers HTTP 200 with an <ERROR> body."""
        with self.assertRaises(harvest.HarvestError):
            harvest._raise_on_xml_error(b"<eSearchResult><ERROR>Invalid db name</ERROR>"
                                        b"</eSearchResult>")

    def test_a_clean_body_passes(self) -> None:
        harvest._raise_on_xml_error(document(ARTICLE))


class CompletenessInvariants(unittest.TestCase):
    """The invariant the first version lacked entirely: it printed "written" regardless.

    A page dropped by the network, or a record type the parser skips, produced a corpus that
    was short by an unknown amount and said nothing. These three refusals are the difference
    between a harvest and a guess.
    """

    def _run(self, payload: bytes, count: int) -> None:
        original_search, original_request, original_uids = (
            harvest.search, harvest._request, harvest.uids)
        harvest.search = lambda term: {"count": count, "webenv": "W", "query_key": "1",
                                       "query_translation": term}
        harvest._request = lambda endpoint, params, retries=5: payload
        harvest.uids = lambda term: set()
        try:
            harvest.harvest("anything")
        finally:
            harvest.search, harvest._request, harvest.uids = (
                original_search, original_request, original_uids)

    def test_a_short_harvest_is_refused(self) -> None:
        with self.assertRaises(harvest.HarvestError) as caught:
            self._run(document(ARTICLE), count=2)
        self.assertIn("incomplete harvest", str(caught.exception))

    def test_duplicate_records_are_refused(self) -> None:
        with self.assertRaises(harvest.HarvestError) as caught:
            self._run(document(ARTICLE, ARTICLE), count=2)
        self.assertIn("duplicate", str(caught.exception))

    def test_an_unparsed_record_type_is_refused_before_the_count_check(self) -> None:
        payload = document(ARTICLE).replace(
            b"</PubmedArticleSet>", b"<PubmedFutureThing/></PubmedArticleSet>")
        with self.assertRaises(harvest.HarvestError) as caught:
            self._run(payload, count=1)
        self.assertIn("unhandled record type", str(caught.exception))

    def test_a_complete_harvest_records_its_invariants(self) -> None:
        original_search, original_request, original_uids = (
            harvest.search, harvest._request, harvest.uids)
        harvest.search = lambda term: {"count": 2, "webenv": "W", "query_key": "1",
                                       "query_translation": "expanded(" + term + ")"}
        harvest._request = lambda endpoint, params, retries=5: document(ARTICLE, BOOK)
        harvest.uids = lambda term: {"36779245"}
        try:
            records, manifest, free = harvest.harvest("WWOX")
        finally:
            harvest.search, harvest._request, harvest.uids = (
                original_search, original_request, original_uids)
        self.assertEqual(len(records), 2)
        self.assertEqual(manifest["parsed_count"], manifest["expected_count"])
        self.assertEqual(manifest["distinct_pmids"], 2)
        self.assertEqual(free, {"36779245"})
        self.assertEqual(manifest["record_types"],
                         ["PubmedArticle", "PubmedBookArticle"])
        self.assertEqual(manifest["query_translation"], "expanded(WWOX)")
        self.assertIn("not 'every paper on the gene'", manifest["not_claimed"])
        self.assertEqual(manifest["with_other_abstract"], 1)
        self.assertEqual(manifest["with_corrections"], 1)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
