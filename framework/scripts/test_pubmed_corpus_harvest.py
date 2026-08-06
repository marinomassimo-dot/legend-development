#!/usr/bin/env python3
"""Parsing and completeness regressions for the PubMed corpus harvester.

Every case here is a defect that produced a *plausible* corpus, not a crash. A parser that
raises is fixed the same minute; one that quietly drops a record type, or truncates a date to
"Wint", ships a corpus nobody can tell is wrong.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


harvest = _module("harvest", "framework/scripts/pubmed_corpus_harvest.py")
firewall = _module("firewall", "framework/scripts/corpus_firewall.py")


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
   <ChemicalList>
    <Chemical><RegistryNumber>EC 3.1.1.-</RegistryNumber>
     <NameOfSubstance UI="C000001">WWOX protein, human</NameOfSubstance></Chemical>
   </ChemicalList>
   <MeshHeadingList>
    <MeshHeading><DescriptorName UI="D004827" MajorTopicYN="Y">Epilepsy</DescriptorName>
     <QualifierName UI="Q000235" MajorTopicYN="N">genetics</QualifierName></MeshHeading>
    <MeshHeading><DescriptorName UI="D006801" MajorTopicYN="N">Humans</DescriptorName>
    </MeshHeading>
   </MeshHeadingList>
   <KeywordList Owner="NOTNLM">
    <Keyword MajorTopicYN="N">WOREE</Keyword></KeywordList>
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
   <AuthorList Type="authors">
    <Author><LastName>Aldaz</LastName><ForeName>C Marcelo</ForeName></Author>
   </AuthorList>
   <AuthorList Type="editors">
    <Author><LastName>Adam</LastName><ForeName>Margaret P</ForeName></Author>
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


def _harvest(payload: bytes, count: int, free: set[str] | None = None, term: str = "anything"):
    """Run `harvest()` against a fixed payload, with the network stubbed out."""
    original = (harvest.search, harvest._request, harvest.uids)
    harvest.search = lambda query: {"count": count, "webenv": "W", "query_key": "1",
                                    "query_translation": "expanded(" + query + ")"}
    harvest._request = lambda endpoint, params, retries=5: payload
    harvest.uids = lambda query: set(free or set())
    try:
        return harvest.harvest(term)
    finally:
        harvest.search, harvest._request, harvest.uids = original


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

    def test_the_retraction_source_citation_survives(self) -> None:
        """`find("RefSource") or ET.Element("x")`: a childless Element is falsy.

        The fallback won every time, so all 40 correction notices in the 2026-08-05 harvest
        carried an empty citation while ref_type and pmid looked perfect. The test above
        asserted the two fields that were right.
        """
        self.assertEqual(self.row["corrections"][0]["citation"], "Int J Mol Med. 2026")

    def test_mesh_headings_are_captured_with_qualifiers(self) -> None:
        """A corpus for triage that drops MeSH has dropped the field triage ranks on."""
        headings = {h["descriptor"]: h for h in self.row["mesh_headings"]}
        self.assertEqual(set(headings), {"Epilepsy", "Humans"})
        self.assertTrue(headings["Epilepsy"]["major"])
        self.assertFalse(headings["Humans"]["major"])
        self.assertEqual(headings["Epilepsy"]["qualifiers"][0]["name"], "genetics")

    def test_keywords_and_chemicals_are_captured(self) -> None:
        self.assertEqual([k["term"] for k in self.row["keywords"]], ["WOREE"])
        self.assertEqual(self.row["keywords"][0]["owner"], "NOTNLM")
        self.assertEqual(self.row["chemicals"][0]["name"], "WWOX protein, human")
        self.assertEqual(self.row["chemicals"][0]["registry_number"], "EC 3.1.1.-")

    def test_editors_are_not_recorded_as_authors(self) -> None:
        """A BookDocument carries AuthorList Type="authors" AND Type="editors".

        `iter("Author")` flattened both, so the GeneReviews series editors became authors of
        every chapter — real names attached to the wrong relationship to the work.
        """
        book = harvest.parse(document(BOOK))[0]
        roles = {person["last_name"]: person["role"] for person in book["authors"]}
        self.assertEqual(roles, {"Aldaz": "authors", "Adam": "editors"})

    def test_a_missing_author_list_type_defaults_to_authors(self) -> None:
        self.assertEqual({p["role"] for p in self.row["authors"]}, {"authors"})

    def test_authors_keep_affiliations_collectives_and_orcid(self) -> None:
        people = self.row["authors"]
        self.assertEqual(people[0]["affiliations"], ["Epilepsy Research Centre"])
        self.assertEqual(people[0]["identifiers"]["ORCID"], "0000-0002-0000-0001")
        self.assertEqual(people[1]["collective_name"], "The WWOX Study Group")

    def test_every_pubmed_element_is_captured_or_named(self) -> None:
        """"Lossless" is a claim, so it gets a ratchet rather than a promise.

        A new DTD element must be captured, or listed in `NOT_CAPTURED`, or fail here. The
        previous version asserted losslessness in a docstring while dropping every MeSH
        heading, and nothing could tell.
        """
        import xml.etree.ElementTree as ET

        captured = {
            "PubmedArticleSet", "PubmedArticle", "MedlineCitation", "PMID", "Article",
            "Journal", "Title", "ISOAbbreviation", "ISSN", "JournalIssue", "Volume", "Issue",
            "PubDate", "Year", "Month", "Day", "MedlineDate", "ArticleTitle", "Pagination",
            "MedlinePgn", "ELocationID", "Abstract", "AbstractText", "CopyrightInformation",
            "AuthorList", "Author", "LastName", "ForeName", "Initials", "CollectiveName",
            "AffiliationInfo", "Affiliation", "Identifier", "Language", "PublicationTypeList",
            "PublicationType", "ArticleDate", "VernacularTitle", "OtherAbstract",
            "CommentsCorrectionsList", "CommentsCorrections", "RefSource", "PubmedData",
            "PublicationStatus", "ArticleIdList", "ArticleId", "History", "PubMedPubDate",
            "MeshHeadingList", "MeshHeading", "DescriptorName", "QualifierName",
            "KeywordList", "Keyword", "ChemicalList", "Chemical", "NameOfSubstance",
            "RegistryNumber", "PubmedBookArticle", "BookDocument", "Book", "BookTitle",
            "PubmedBookData",
        }
        named = " ".join(harvest.NOT_CAPTURED)
        unaccounted = set()
        for element in ET.fromstring(document(ARTICLE, BOOK, PLAIN)).iter():
            if element.tag not in captured and element.tag not in named:
                unaccounted.add(element.tag)
        self.assertEqual(unaccounted, set(),
                         "these elements are neither captured nor listed in NOT_CAPTURED")

    def test_the_fidelity_claim_is_qualified_not_absolute(self) -> None:
        source = (ROOT / "framework/scripts/pubmed_corpus_harvest.py").read_text(
            encoding="utf-8")
        self.assertIn("not_captured", source)
        for excluded in ("CoiStatement", "GeneSymbolList", "InvestigatorList",
                         "NumberOfReferences", "PersonalNameSubjectList"):
            with self.subTest(field=excluded):
                self.assertIn(excluded, source)

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


class Transport(unittest.TestCase):
    """Failures of the wire, which are the ordinary case on a 700-record efetch."""

    def test_a_truncated_body_is_retryable_not_a_crash(self) -> None:
        """`_raise_on_xml_error` returned quietly on ParseError.

        A truncated page therefore passed the check as if it were good and crashed later
        inside `parse()` with a bare ParseError traceback — after no retry at all, which is
        precisely the failure a retry loop exists for.
        """
        with self.assertRaises(harvest.TransientHarvestError):
            harvest._raise_on_xml_error(b'<?xml version="1.0"?><PubmedArticleSet><Pubmed')

    def test_a_permanent_error_body_is_not_retried(self) -> None:
        """Five backoffs do not make "Invalid db name" into a valid query."""
        attempts = []

        class _Response:
            def __enter__(self_inner):
                attempts.append(1)
                return self_inner

            def __exit__(self_inner, *_): return False

            def read(self_inner):
                return b"<eSearchResult><ERROR>Invalid db name</ERROR></eSearchResult>"

        original = harvest.urllib.request.urlopen
        harvest.urllib.request.urlopen = lambda url, timeout=0: _Response()
        try:
            with self.assertRaises(harvest.HarvestError) as caught:
                harvest._request("esearch.fcgi", {"db": "nope"}, retries=5)
        finally:
            harvest.urllib.request.urlopen = original
        self.assertEqual(len(attempts), 1, "a malformed query was retried")
        self.assertIn("Invalid db name", str(caught.exception))

    def test_a_retry_after_date_does_not_crash_the_backoff(self) -> None:
        """RFC 7231 allows an HTTP-date. `float()` on one raises inside the handler.

        The crash landed on a 429 — the single response the retry loop exists to survive.
        """
        self.assertLessEqual(harvest._retry_after("Wed, 21 Oct 2015 07:28:00 GMT", 0),
                             harvest.RETRY_CEILING_SECONDS)
        self.assertEqual(harvest._retry_after("30", 0), 30.0)
        self.assertEqual(harvest._retry_after(None, 3), 8.0)

    def test_a_hostile_retry_after_is_capped(self) -> None:
        self.assertEqual(harvest._retry_after("86400", 0), harvest.RETRY_CEILING_SECONDS)


class DeletedUpstream(unittest.TestCase):
    """A PMID withdrawn between the search and the fetch is not a parser defect."""

    DELETED = "<DeleteCitation><PMID>99999999</PMID></DeleteCitation>"

    def test_a_delete_citation_is_not_an_unknown_record_type(self) -> None:
        payload = document(ARTICLE, self.DELETED)
        self.assertEqual(harvest.unparsed_record_tags(payload), set())
        self.assertEqual(harvest.deleted_pmids(payload), {"99999999"})

    def test_the_count_invariant_accounts_for_deletions(self) -> None:
        records, manifest, _ = _harvest(document(ARTICLE, self.DELETED), count=2)
        self.assertEqual(len(records), 1)
        self.assertEqual(manifest["deleted_by_pubmed"], ["99999999"])
        self.assertEqual(manifest["parsed_count"] + len(manifest["deleted_by_pubmed"]),
                         manifest["expected_count"])

    def test_a_real_shortfall_is_still_refused(self) -> None:
        with self.assertRaises(harvest.HarvestError):
            _harvest(document(ARTICLE, self.DELETED), count=3)


class TheFirewallMustBeAbleToSeeTheCorpus(unittest.TestCase):
    """The guards recognise a corpus by PATH. `--out-dir` is a free parameter."""

    def test_every_guard_uses_the_one_shared_definition(self) -> None:
        """Four hand-maintained copies of one regex drift, and the drift is silent."""
        for relative in ("framework/scripts/pubmed_corpus_harvest.py",
                         "framework/scripts/fulltext_receipts.py",
                         "framework/scripts/deepdive_manifest.py"):
            with self.subTest(guard=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("corpus_firewall", text,
                              f"{relative} does not use the shared firewall definition")
                self.assertNotIn('r"files/corpus/', text,
                                 f"{relative} still carries its own copy of the pattern")

    def test_a_destination_the_guards_cannot_see_is_refused(self) -> None:
        for destination in ("staging/wwox.jsonl", "files/fulltext/wwox_20260805.jsonl",
                            "files/corpus2/wwox.jsonl"):
            with self.subTest(destination=destination):
                with self.assertRaises(harvest.HarvestError) as caught:
                    harvest.refuse_unrecognised_destination([Path(destination)])
                self.assertIn("firewall", str(caught.exception))

    def test_dot_dot_cannot_walk_out_of_a_recognised_directory(self) -> None:
        """`files/corpus/../../staging/wwox.jsonl` contains `files/corpus/` and is not in it.

        The check read the path as a string, so it accepted the single input it exists to
        refuse — and reported the risk as closed.
        """
        for destination in ("files/corpus/../../staging/wwox.jsonl",
                            "files/corpus/../fulltext/wwox.jsonl",
                            "a/corpus_seed_pubmed/../../../tmp/x.jsonl"):
            with self.subTest(destination=destination):
                with self.assertRaises(harvest.HarvestError):
                    harvest.refuse_unrecognised_destination([Path(destination)])

    def test_a_slug_is_a_filename_not_a_path(self) -> None:
        for slug in ("../../staging/wwox", "sub/wwox", "..", "", "."):
            with self.subTest(slug=slug):
                with self.assertRaises(harvest.HarvestError):
                    harvest.refuse_bad_slug(slug)
        harvest.refuse_bad_slug("corpus_seed_pubmed_20260806")

    def test_a_renamed_corpus_is_still_recognised_by_its_contents(self) -> None:
        """The move anyone makes when a name check refuses them: copy it somewhere else."""
        records = harvest.parse(document(ARTICLE, BOOK))
        with tempfile.TemporaryDirectory() as tmp:
            innocent = Path(tmp) / "files/fulltext/PMID36779245_paper.jsonl"
            innocent.parent.mkdir(parents=True)
            harvest.write_jsonl(records, innocent)
            self.assertFalse(firewall.names_a_corpus(str(innocent)),
                             "the name check is not supposed to catch this one")
            self.assertTrue(firewall.looks_like_corpus(innocent))
            self.assertTrue(firewall.corpus_objection(str(innocent)))

    def test_json_packaging_cannot_bypass_content_recognition(self) -> None:
        """Whitespace and an outer array do not change what the records are."""
        record = harvest.parse(document(ARTICLE))[0]
        with tempfile.TemporaryDirectory() as tmp:
            pretty = Path(tmp) / "pretty.data"
            array = Path(tmp) / "array.data"
            pretty.write_text(json.dumps(record, indent=2), encoding="utf-8")
            array.write_text(json.dumps([record], indent=2), encoding="utf-8")
            self.assertTrue(firewall.looks_like_corpus(pretty))
            self.assertTrue(firewall.looks_like_corpus(array))

    def test_common_metadata_keys_do_not_make_an_unrelated_jsonl_a_corpus(self) -> None:
        """A guard that rejects legitimate structured data will eventually be disabled."""
        experiment = {
            "record_type": "experiment",
            "pmid": "36779245",
            "identifiers": {"run": "R1"},
            "measurements": [{"gene": "WWOX", "value": 1.2}],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "experiment.jsonl"
            path.write_text(json.dumps(experiment) + "\n", encoding="utf-8")
            self.assertFalse(firewall.looks_like_corpus(path))

    def test_a_renamed_seed_tsv_is_recognised_too(self) -> None:
        records = harvest.parse(document(ARTICLE))
        with tempfile.TemporaryDirectory() as tmp:
            innocent = Path(tmp) / "notes.tsv"
            harvest.write_seed(records, set(), innocent)
            self.assertTrue(firewall.looks_like_corpus(innocent))

    def test_a_real_paper_is_not_mistaken_for_a_corpus(self) -> None:
        """A guard that refuses the papers is worse than no guard: it gets switched off."""
        with tempfile.TemporaryDirectory() as tmp:
            for name, body in (("paper.xml", "<article><body><p>WWOX is a gene.</p></body>"
                                             "</article>"),
                               ("paper.html", "<html><body>WWOX</body></html>"),
                               ("notes.md", "# Reading notes\n\npmid 36779245 was read."),
                               ("data.tsv", "gene\tvalue\nWWOX\t1.2\n"),
                               ("results.jsonl", '{"gene": "WWOX", "value": 1.2}\n')):
                path = Path(tmp) / name
                path.write_text(body, encoding="utf-8")
                with self.subTest(file=name):
                    self.assertFalse(firewall.looks_like_corpus(path))

    def test_the_conventional_destinations_are_accepted(self) -> None:
        harvest.refuse_unrecognised_destination([
            Path("files/corpus/wwox_20260805.jsonl"),
            Path("disease-models/wwox/registries/corpus_seed_pubmed_20260805.tsv")])

    def test_the_writer_refuses_before_it_writes_anything(self) -> None:
        records = harvest.parse(document(ARTICLE))
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "elsewhere"
            with self.assertRaises(harvest.HarvestError):
                harvest.write_corpus(records, {}, set(), destination, "wwox")
            self.assertFalse(destination.exists(), "a refused harvest left files behind")


class OutputSet(unittest.TestCase):
    def test_a_dotted_slug_does_not_rename_the_outputs(self) -> None:
        """`(dir / "wwox.v2").with_suffix(".jsonl")` is `wwox.jsonl` — a manifest describing
        files that do not exist."""
        self.assertEqual(harvest.output_path(Path("files/corpus"), "wwox.v2", ".jsonl").name,
                         "wwox.v2.jsonl")

    def test_the_three_artefacts_are_promoted_together(self) -> None:
        records = harvest.parse(document(ARTICLE, BOOK))
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "files/corpus"
            harvest.write_corpus(records, {"parsed_count": 2}, {"36779245"}, out, "wwox")
            self.assertFalse(list(out.glob("*.partial")))
            manifest = json.loads((out / "wwox.manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(sorted(manifest["outputs"]), ["wwox.jsonl", "wwox.tsv"])
            for name, entry in manifest["outputs"].items():
                self.assertEqual(
                    hashlib.sha256((out / name).read_bytes()).hexdigest(), entry["sha256"])

    def test_a_manifest_failure_leaves_no_orphan_corpus(self) -> None:
        """Data on disk with no terms of use is the one artefact the firewall assumes away."""
        records = harvest.parse(document(ARTICLE))
        unserialisable = {"parsed_count": 1, "boom": object()}
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "files/corpus"
            with self.assertRaises(TypeError):
                harvest.write_corpus(records, unserialisable, set(), out, "wwox")
            self.assertEqual(sorted(p.name for p in out.iterdir()), [])

    def test_no_abstracts_strips_the_jsonl_too(self) -> None:
        """The documented refresh sends `--no-abstracts` into a TRACKED directory.

        Stripping only the TSV meant an operator asking for a safe bibliographic export wrote
        706 publisher-copyright abstracts into the publishable tree, and the flag's own help
        text said so — which made it worse, not better.
        """
        records, manifest, free = _harvest(document(ARTICLE, BOOK), count=2)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "files/corpus"
            harvest.write_corpus(records, manifest, free, out, "wwox", abstracts=False)
            for name in ("wwox.jsonl", "wwox.tsv"):
                body = (out / name).read_text(encoding="utf-8")
                with self.subTest(file=name):
                    self.assertNotIn("Thirteen patients", body)
                    self.assertNotIn("Un resume en francais", body)
                    self.assertNotIn("chapter abstract", body)
            self.assertIn("36779245", (out / "wwox.jsonl").read_text(encoding="utf-8"))
            header = (out / "wwox.tsv").read_text(encoding="utf-8").splitlines()[0]
            self.assertNotIn("abstract", header.split("\t"))

    def test_the_default_run_still_keeps_abstracts(self) -> None:
        records, manifest, free = _harvest(document(ARTICLE), count=1)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "files/corpus"
            harvest.write_corpus(records, manifest, free, out, "wwox")
            self.assertIn("Thirteen patients",
                          (out / "wwox.jsonl").read_text(encoding="utf-8"))

    def test_concurrent_runs_do_not_share_a_temporary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "corpus.jsonl"
            captured = []
            harvest._stage(target, lambda h: captured.append(h) or h.write("{}\n"))
            leftovers = list(Path(tmp).glob("*.partial"))
            self.assertEqual(len(leftovers), 1)
            self.assertNotEqual(leftovers[0].name, "corpus.jsonl.partial")

    def test_the_seed_exposes_retraction_status(self) -> None:
        """40 of 706 records carry a notice and the triage surface showed none of them."""
        row = harvest.to_seed_row(harvest.parse(document(ARTICLE))[0], set())
        self.assertEqual(row["corrections"], "RetractionIn:42464650")
        self.assertIn("corrections", harvest.SEED_FIELDS)


class VerifyAnExistingCorpus(unittest.TestCase):
    """Nothing read the checksums back, so a damaged corpus looked exactly like a good one."""

    def _corpus(self, tmp: Path) -> Path:
        records, manifest, free = _harvest(document(ARTICLE, BOOK), count=2)
        out = tmp / "files/corpus"
        harvest.write_corpus(records, manifest, free, out, "wwox")
        return out / "wwox.manifest.json"

    def test_an_untouched_corpus_verifies(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(harvest.verify(self._corpus(Path(tmp))), [])

    def test_an_edited_corpus_is_caught(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            jsonl = manifest_path.parent / "wwox.jsonl"
            jsonl.write_text(jsonl.read_text(encoding="utf-8").splitlines()[0] + "\n",
                             encoding="utf-8")
            problems = harvest.verify(manifest_path)
            self.assertTrue(any("sha256" in p for p in problems))
            self.assertTrue(any("holds 1 records" in p for p in problems))

    def test_a_missing_checksum_is_not_a_pass(self) -> None:
        """The comparison ran only `if expected`, so the weakest manifest verified cleanest."""
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["outputs"]["wwox.jsonl"].pop("sha256")
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertTrue(any("no usable sha256" in p
                                for p in harvest.verify(manifest_path)))

    def test_a_damaged_jsonl_is_reported_not_raised(self) -> None:
        """A corrupt corpus is the input this command exists for; a traceback answers it by
        saying the checker is broken."""
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            (manifest_path.parent / "wwox.jsonl").write_text('{"pmid": "1"}\n{oops\n',
                                                             encoding="utf-8")
            problems = harvest.verify(manifest_path)
            self.assertTrue(any("not valid JSON" in p for p in problems))

    def test_a_manifest_that_contradicts_its_own_invariant_is_caught(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["expected_count"] = 99
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertTrue(any("its own invariant" in p
                                for p in harvest.verify(manifest_path)))

    def test_a_later_harvester_version_does_not_invalidate_a_snapshot(self) -> None:
        """A snapshot is history. It does not become wrong because the tool moved on — and a
        check that says otherwise trains people to ignore it."""
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["harvester_version"] = "3.1"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertEqual(harvest.verify(manifest_path), [])

    def test_an_unsupported_schema_is_caught(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["manifest_schema_version"] = 99
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertTrue(any("outside the supported range" in p
                                for p in harvest.verify(manifest_path)))

    def test_a_torn_output_set_is_detectable(self) -> None:
        """Three renames cannot be one. The manifest is promoted last and carries the other
        two checksums, so a set torn mid-promotion no longer describes itself."""
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            jsonl = manifest_path.parent / "wwox.jsonl"
            jsonl.write_text(jsonl.read_text(encoding="utf-8") + '{"pmid": "999"}\n',
                             encoding="utf-8")
            self.assertTrue(any("sha256" in p for p in harvest.verify(manifest_path)))

    def test_a_corpus_predating_the_terms_of_use_is_caught(self) -> None:
        """The live 2026-08-05 corpus: version 2.0, and none of the terms 2.0 was to write."""
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = self._corpus(Path(tmp))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for field in ("evidential_status", "permitted_uses", "forbidden_uses",
                          "manifest_schema_version"):
                manifest.pop(field)
            manifest["harvester_version"] = "2.0"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            problems = harvest.verify(manifest_path)
            self.assertTrue(any("evidential_status" in p for p in problems))
            self.assertTrue(any("manifest_schema_version" in p for p in problems))


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
        _harvest(payload, count)

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
        records, manifest, free = _harvest(
            document(ARTICLE, BOOK), count=2, free={"36779245"}, term="WWOX")
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
