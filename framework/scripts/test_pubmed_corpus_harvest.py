#!/usr/bin/env python3
"""Parsing regressions for the PubMed corpus harvester.

Both cases below are real defects from the first run, not hypotheticals. Each produced a
plausible corpus that was silently wrong, which is the only kind worth a regression: a parser
that crashes gets fixed the same minute.
"""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "harvest", ROOT / "framework/scripts/pubmed_corpus_harvest.py")
harvest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(harvest)


# One article whose own IDs differ from the IDs of the reference it cites, and whose title is
# plain text. Both traits were mishandled.
SAMPLE = b"""<?xml version="1.0"?>
<PubmedArticleSet>
 <PubmedArticle>
  <MedlineCitation>
   <PMID>36779245</PMID>
   <Article>
    <Journal><ISOAbbreviation>Epilepsia</ISOAbbreviation>
     <JournalIssue><PubDate><Year>2023</Year></PubDate></JournalIssue></Journal>
    <ArticleTitle>WWOX developmental and epileptic encephalopathy</ArticleTitle>
    <Abstract><AbstractText Label="OBJECTIVE">WWOX is autosomal recessive.</AbstractText>
     <AbstractText Label="METHODS">We ascertained 13 patients.</AbstractText></Abstract>
    <PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList>
   </Article>
   <OtherAbstract><AbstractText>Un resume en francais.</AbstractText></OtherAbstract>
  </MedlineCitation>
  <PubmedData>
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
 </PubmedArticle>
 <PubmedArticle>
  <MedlineCitation>
   <PMID>11111111</PMID>
   <Article>
    <Journal><Title>Journal of Things</Title>
     <JournalIssue><PubDate><Year>2001</Year></PubDate></JournalIssue></Journal>
    <ArticleTitle>Markup <i>inside</i> the title</ArticleTitle>
    <PublicationTypeList><PublicationType>Review</PublicationType></PublicationTypeList>
   </Article>
  </MedlineCitation>
  <PubmedData><ArticleIdList>
   <ArticleId IdType="pubmed">11111111</ArticleId>
  </ArticleIdList></PubmedData>
 </PubmedArticle>
</PubmedArticleSet>"""


class Parsing(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = {r["pmid"]: r for r in harvest.parse(SAMPLE, want_abstract=True)}

    def test_identifiers_come_from_the_article_not_its_references(self) -> None:
        """`iter("ArticleId")` walks the reference list too, and quietly wins.

        PMID 36779245 carries 78 ArticleId elements in the live record; three are its own.
        Reading them all gave it a reference's PMCID and DOI — both real identifiers, both
        for a different paper.
        """
        row = self.rows["36779245"]
        self.assertEqual(row["pmcid"], "PMC10952634")
        self.assertEqual(row["doi"], "10.1111/epi.17542")
        self.assertNotEqual(row["pmcid"], "PMC9068835")

    def test_a_plain_text_title_survives(self) -> None:
        """An Element with no children is falsy, so `find(...) or fallback` discards it.

        That emptied 673 of 706 titles: exactly those without inline markup.
        """
        self.assertEqual(self.rows["36779245"]["title"],
                         "WWOX developmental and epileptic encephalopathy")

    def test_a_title_with_markup_keeps_its_words(self) -> None:
        self.assertEqual(self.rows["11111111"]["title"], "Markup inside the title")

    def test_abstract_sections_are_labelled_and_joined(self) -> None:
        abstract = self.rows["36779245"]["abstract"]
        self.assertIn("OBJECTIVE: WWOX is autosomal recessive.", abstract)
        self.assertIn("METHODS: We ascertained 13 patients.", abstract)

    def test_a_translated_other_abstract_is_not_mixed_in(self) -> None:
        self.assertNotIn("resume", self.rows["36779245"]["abstract"])

    def test_a_record_without_an_abstract_is_kept_not_dropped(self) -> None:
        """A paper with no abstract is still part of the census."""
        self.assertIn("11111111", self.rows)
        self.assertEqual(self.rows["11111111"]["abstract"], "")

    def test_no_field_can_break_the_tsv(self) -> None:
        for pmid, row in self.rows.items():
            for field, value in row.items():
                with self.subTest(pmid=pmid, field=field):
                    self.assertNotIn("\t", value)
                    self.assertNotIn("\n", value)

    def test_abstracts_can_be_suppressed(self) -> None:
        rows = harvest.parse(SAMPLE, want_abstract=False)
        self.assertTrue(all(r["abstract"] == "" for r in rows))
        self.assertTrue(all(r["title"] for r in rows))


class OutputContract(unittest.TestCase):
    def test_field_order_is_fixed(self) -> None:
        """The seed is diffed across harvests; a reordered header makes every row differ."""
        self.assertEqual(harvest.FIELDS[:3], ("pmid", "year", "free_full_text"))
        self.assertIn("abstract", harvest.FIELDS)

    def test_written_rows_round_trip(self) -> None:
        import csv
        import tempfile
        rows = harvest.parse(SAMPLE, want_abstract=True)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "corpus.tsv"
            harvest.write(rows, out)
            back = list(csv.DictReader(out.open(encoding="utf-8"), delimiter="\t"))
        self.assertEqual(len(back), len(rows))
        self.assertEqual([r["pmid"] for r in back], [r["pmid"] for r in rows])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
