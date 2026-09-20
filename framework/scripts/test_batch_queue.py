#!/usr/bin/env python3
"""Regression suite for the batch queue.

The queue is a claim about *what has been read*, so the failure that matters is
overstating coverage. The join was originally written to index every identifier appearing
in a record body; that attributed a record's read depth to every paper it merely cited and
inflated "full text read" roughly six-fold. The first test below is that bug, frozen.

The second concern is drift: the committed queue is generated, so a registry change without
a regeneration shows a reader numbers that no longer describe the repository.
"""

from __future__ import annotations

import re
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))

import batch_queue as bq  # noqa: E402
import fulltext_receipts as receipts  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REGISTRIES = ROOT / "disease-models" / "wwox" / "registries"
QUEUE = REGISTRIES / "batch_queue.md"


def _harvester():
    """The real harvester, so the end-to-end tests start from PubMed XML and not from a
    hand-written TSV that assumes the very column mapping under test."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "harvest", ROOT / "framework/scripts/pubmed_corpus_harvest.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _pubmed_xml(pmid: str, title: str, notices: list[tuple[str, str]]) -> str:
    corrections = "".join(
        f'<CommentsCorrections RefType="{ref_type}"><PMID>{other}</PMID>'
        f"<RefSource>J Test. 2026</RefSource></CommentsCorrections>"
        for ref_type, other in notices)
    block = f"<CommentsCorrectionsList>{corrections}</CommentsCorrectionsList>" if notices \
        else ""
    return (
        f"<PubmedArticle><MedlineCitation><PMID>{pmid}</PMID><Article>"
        f"<Journal><Title>J Test</Title><JournalIssue><PubDate><Year>2019</Year>"
        f"</PubDate></JournalIssue></Journal><ArticleTitle>{title}</ArticleTitle>"
        f"<PublicationTypeList><PublicationType>Journal Article</PublicationType>"
        f"</PublicationTypeList></Article>{block}</MedlineCitation>"
        f"<PubmedData><ArticleIdList>"
        f'<ArticleId IdType="pubmed">{pmid}</ArticleId>'
        f'<ArticleId IdType="doi">10.1000/{pmid}</ArticleId>'
        f"</ArticleIdList></PubmedData></PubmedArticle>")


def _pubmed_set(*articles: str) -> bytes:
    return ('<?xml version="1.0"?><PubmedArticleSet>' + "".join(articles)
            + "</PubmedArticleSet>").encode("utf-8")


def fixture(test_case: unittest.TestCase, registry_body: str) -> Path:
    temporary = TemporaryDirectory()
    test_case.addCleanup(temporary.cleanup)
    registries = Path(temporary.name) / "disease-models" / "wwox" / "registries"
    registries.mkdir(parents=True)
    (registries / "paper_registry_current.md").write_text(registry_body, encoding="utf-8")
    (registries / "fulltext_read_receipts.jsonl").touch()
    return registries


class JoinTests(unittest.TestCase):
    def test_cited_identifiers_do_not_inherit_read_depth(self) -> None:
        registries = fixture(
            self,
            textwrap.dedent(
                """\
                ## PAPER 001
                **Identifier:** PMID 11111111
                **Status:** claim_linked
                **Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
                **Note:** compares favourably with PMID 22222222 and DOI 10.1000/cited.1
                """
            )
        )
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:11111111"]["depth"], "full text")
        self.assertNotIn("pmid:22222222", index, "a cited PMID must not inherit read depth")
        self.assertNotIn("doi:10.1000/cited.1", index)

    def test_corpus_placeholder_is_catalogued_not_read(self) -> None:
        registries = fixture(
            self,
            "## CORPUS P900\n**Identifier:** PMID 33333333\n**Status:** screened — corpus placeholder\n"
        )
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:33333333"]["depth"], "catalogued only")

    def test_legacy_corpus_stub_heading_is_catalogued(self) -> None:
        registries = fixture(
            self,
            "## CORPUS-STUB-001\n**Identifier:** PMID 33333334\n"
            "**Status:** screened — corpus placeholder\n"
        )
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:33333334"]["depth"], "catalogued only")

    def test_bare_tracking_identifier_is_an_exact_pmid(self) -> None:
        registries = fixture(self, "## PAPER 001\n**Identifier:** pending normalization\n")
        (registries / "literature_tracking_log_current.md").write_text(
            "**Identifier value:** 41153369\n", encoding="utf-8"
        )
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:41153369"]["depth"], "screened")

    def test_promoted_paper_overrides_earlier_corpus_stub(self) -> None:
        registries = fixture(
            self,
            textwrap.dedent(
                """\
                ## CORPUS-STUB-001
                **Identifier:** PMID 33333335
                **Status:** screened — corpus placeholder

                ## PAPER 039
                **Identifier:** PMID 33333335
                **Evidence depth:** full text reviewed (coverage_status: complete_fulltext_read)
                """
            )
        )
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:33333335"]["depth"], "full text")
        self.assertEqual(index["pmid:33333335"]["record"], "PAPER 039")

    def test_doi_match_is_case_insensitive(self) -> None:
        registries = fixture(
            self,
            "## PAPER 002\n**Identifier:** DOI 10.1000/Mixed.Case\n**Status:** integrated\n"
        )
        index = bq.registry_index(registries)
        self.assertIn("doi:10.1000/mixed.case", index)

    def test_complete_receipt_upgrades_queue_depth_before_batch_commit(self) -> None:
        registries = fixture(
            self,
            "## PAPER 002\n**Identifier:** PMID 42193054 / DOI 10.1000/example\n"
            "**Status:** integrated\n",
        )
        receipt = {
            "event_id": "FTR-20260726-42193054-01",
            "record_kind": "contemporaneous_receipt",
            "study_id": {"pmid": "42193054", "doi": "10.1000/example"},
            "event_at": "2026-07-26T08:00:00+02:00",
            "analysis_at": "2026-07-26T07:00:00+02:00",
            "workflow": "test",
            "evidence_depth": "complete_fulltext_read",
            "source_locator": "PMC123",
            "source_fingerprint": None,
            "source_kind": "fulltext_remote",
            "analysis_time_precision": "second",
            "coverage": {key: "read" for key in receipts.COVERAGE_KEYS},
            "outputs": ["dossier.md"],
            "evidence_basis": ["coverage_map", "dossier"],
            "prior_receipt": None,
            "reread_reason": "first_read",
        }
        scratch_ledger = registries.parent.parent.parent / "receipt_fixture.jsonl"
        receipts.append_receipt(scratch_ledger, receipt)
        scratch_ledger.replace(registries / "fulltext_read_receipts.jsonl")
        index = bq.registry_index(registries)
        self.assertEqual(index["pmid:42193054"]["depth"], "full text")
        self.assertEqual(index["pmid:42193054"]["record"], f"receipt {receipt['event_id']}")

    def test_missing_receipt_ledger_fails_closed(self) -> None:
        registries = fixture(
            self,
            "## PAPER 002\n**Identifier:** PMID 42193054\n**Status:** integrated\n",
        )
        (registries / "fulltext_read_receipts.jsonl").unlink()
        with self.assertRaisesRegex(SystemExit, "missing full-text receipt ledger"):
            bq.registry_index(registries)


class QueueIntegrityTests(unittest.TestCase):
    def test_repeated_paper_across_snapshots_is_counted_once(self) -> None:
        with TemporaryDirectory() as temporary:
            registries = Path(temporary)
            header = "pmid\tyear\tfree_full_text\ttype\tdoi\ttitle\n"
            first = header + "11111111\t2025\tno\tprimary\t10.1000/x\tOld title\n"
            second = header + "11111111\t2025\tyes\tprimary\t10.1000/x\tCurrent title\n"
            (registries / "corpus_seed_pubmed_20250101.tsv").write_text(first, encoding="utf-8")
            (registries / "corpus_seed_pubmed_20260101.tsv").write_text(second, encoding="utf-8")
            seeds, occurrences = bq.load_seeds(registries)
            self.assertEqual(occurrences, 2)
            self.assertEqual(len(seeds), 1)
            self.assertEqual(seeds[0]["free_full_text"], "yes")
            self.assertEqual(len(seeds[0]["_sources"].split(";")), 2)

    def test_only_the_current_snapshot_keeps_a_tracked_jsonl(self) -> None:
        """Decided 2026-08-06: TSVs accumulate as history, the JSONL mirrors one snapshot.

        The record-level JSONL is 3.7 MB — the largest tracked file in the repository, 28% of
        its weight, and nothing reads it: `batch_queue` uses the 150 KB TSV. It is kept
        because it is the only durable record of MeSH, authors and affiliations at harvest
        time, and PubMed is not reproducible backwards. What is not acceptable is accruing
        another 3.7 MB of near-duplicate history on every refresh, which is what would have
        happened silently. Dated TSVs remain the audit trail; the JSONL tracks the newest
        snapshot only.
        """
        seeds = sorted(REGISTRIES.glob("corpus_seed_*.tsv"))
        jsonls = sorted(REGISTRIES.glob("corpus_seed_*.jsonl"))
        self.assertLessEqual(
            len(jsonls), 1,
            "more than one tracked corpus JSONL: keep the newest, the older snapshots stay "
            f"as dated TSVs. Found {[p.name for p in jsonls]}")
        if jsonls and seeds:
            self.assertEqual(jsonls[0].stem, seeds[-1].stem,
                             "the tracked JSONL must mirror the newest seed snapshot")

    def test_seed_corpus_is_present_and_dated(self) -> None:
        seeds = sorted(REGISTRIES.glob("corpus_seed_*.tsv"))
        self.assertTrue(seeds, "no seed corpus shipped")
        for seed in seeds:
            self.assertRegex(
                seed.name,
                r"corpus_seed_[a-z]+_\d{8}\.tsv",
                "a seed snapshot must carry its source and date in the filename",
            )

    def test_seed_carries_no_personal_data(self) -> None:
        """The seed is derived from a mail export; headers must never reach the repository."""
        import re

        forbidden = re.compile(r"(?i)@[a-z0-9.-]+\.[a-z]{2,}|sent by|clipboard - pubmed")
        for seed in REGISTRIES.glob("corpus_seed_*.tsv"):
            found = forbidden.findall(seed.read_text(encoding="utf-8"))
            self.assertFalse(found, f"{seed.name} carries export metadata: {found[:3]}")

    def test_totals_are_internally_consistent(self) -> None:
        report = bq.build(ROOT, "wwox")
        self.assertEqual(sum(report["counts"].values()), report["seed_total"])
        self.assertEqual(len(report["queue"]), report["seed_total"])
        self.assertEqual(
            report["seed_occurrences"] - report["duplicate_occurrences"],
            report["seed_total"],
        )
        self.assertLessEqual(report["free_full_text"], report["seed_total"])
        self.assertLessEqual(report["year_min"], report["year_max"])
        self.assertLessEqual(report["published_since_2020"], report["seed_total"])

    def test_publication_integrity_is_eligibility_not_ranking(self) -> None:
        """End to end: PubMed XML → seed TSV → queue JSON → rendered Markdown → hold.

        Publication integrity answers *may this support a claim*, which is a different
        question from *what should I read next*. Both directions of the confusion are
        expensive: sorting a retracted paper down the queue stops nobody citing it, and
        dropping it from the listing deletes the audit trail exactly when it is needed. So
        this asserts the hold appears, the ordering does not move, and the record stays.
        """
        harvest = _harvester()
        retracted = _pubmed_xml("11111111", "A retracted paper",
                                [("RetractionIn", "42464650")])
        concerned = _pubmed_xml("22222222", "A paper under concern",
                                [("ExpressionOfConcernIn", "42464651")])
        corrected = _pubmed_xml("33333333", "A paper with an erratum",
                                [("ErratumIn", "42464652")])
        clean = _pubmed_xml("44444444", "An untouched paper", [])
        records = harvest.parse(_pubmed_set(retracted, concerned, corrected, clean))

        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            registries = root / "disease-models" / "wwox" / "registries"
            registries.mkdir(parents=True)
            (registries / "fulltext_read_receipts.jsonl").touch()
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 006\n**Identifier:** PMID 11111111\n**Status:** integrated\n"
                "**Evidence depth:** full text reviewed\n", encoding="utf-8")
            harvest.write_seed(records, {r["pmid"] for r in records},
                               registries / "corpus_seed_pubmed_20260806.tsv")

            report = bq.build(root, "wwox")
            rendered = bq.render(report, limit=0)

        rows = {item["pmid"]: item for item in report["queue"]}
        self.assertEqual(rows["11111111"]["eligibility"], bq.HOLD)
        self.assertEqual(rows["22222222"]["eligibility"], bq.HOLD)
        self.assertEqual(rows["33333333"]["eligibility"], "",
                         "an erratum is not an integrity event and must not be held")
        self.assertEqual(rows["44444444"]["eligibility"], "")
        held_pmids = {item["pmid"] for item in report["held"]}
        self.assertIn("11111111", held_pmids)
        self.assertIn("22222222", held_pmids)

        # The record stays in the queue: readable for audit, not deleted from the listing.
        for pmid in ("11111111", "22222222", "33333333", "44444444"):
            with self.subTest(pmid=pmid):
                self.assertIn(pmid, rendered)
        self.assertIn(bq.HOLD, rendered)
        self.assertIn("admissibility", rendered)

    def test_a_held_record_already_integrated_triggers_a_claim_audit(self) -> None:
        """The exposure is never the future work.

        A retraction is published after the reading, so the claims at risk are the ones that
        already exist. A hold that only governs what happens next leaves them untouched.
        """
        harvest = _harvester()
        records = harvest.parse(_pubmed_set(
            _pubmed_xml("11111111", "A retracted paper", [("RetractionIn", "42464650")]),
            _pubmed_xml("55555555", "A retracted paper nobody used",
                        [("RetractionIn", "42464653")])))
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            registries = root / "disease-models" / "wwox" / "registries"
            registries.mkdir(parents=True)
            (registries / "fulltext_read_receipts.jsonl").touch()
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 006\n**Identifier:** PMID 11111111\n**Status:** integrated\n"
                "**Evidence depth:** full text reviewed\n", encoding="utf-8")
            harvest.write_seed(records, set(),
                               registries / "corpus_seed_pubmed_20260806.tsv")
            report = bq.build(root, "wwox")
            rendered = bq.render(report, limit=0)

        self.assertEqual([item["pmid"] for item in report["held_integrated"]], ["11111111"])
        self.assertIn("PAPER 006", rendered)
        self.assertIn("Re-examine every", rendered)

    def test_a_meta_citation_cannot_be_declared_unexposed_without_a_registry_record(self) -> None:
        """The paper registry is not the complete citation graph."""
        harvest = _harvester()
        records = harvest.parse(_pubmed_set(
            _pubmed_xml("11111111", "A retracted paper", [("RetractionIn", "42464650")])))
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            registries = root / "disease-models" / "wwox" / "registries"
            registries.mkdir(parents=True)
            (registries / "fulltext_read_receipts.jsonl").touch()
            (registries / "paper_registry_current.md").write_text(
                "## CORPUS P006\n**Identifier:** PMID 11111111\n"
                "**Status:** screened\n", encoding="utf-8")
            meta = root / "disease-models" / "wwox" / "meta"
            meta.mkdir(parents=True)
            (meta / "meta_index_current.md").write_text(
                "A synthesis cites PMID 11111111.\n", encoding="utf-8")
            harvest.write_seed(records, set(),
                               registries / "corpus_seed_pubmed_20260806.tsv")
            report = bq.build(root, "wwox")
            rendered = bq.render(report, limit=0)

        self.assertEqual(report["held_integrated"], [])
        self.assertEqual([item["pmid"] for item in report["held_referenced"]], ["11111111"])
        self.assertIn("meta_index_current.md", rendered)
        self.assertIn("cannot prove absence", rendered)

    def test_the_hold_does_not_reorder_the_queue(self) -> None:
        """Admissibility must not leak into priority, in either direction."""
        harvest = _harvester()
        titles = [("11111111", [("RetractionIn", "1")]), ("22222222", []),
                  ("33333333", [("ExpressionOfConcernIn", "2")]), ("44444444", [])]
        orders = []
        for corrections in (True, False):
            records = harvest.parse(_pubmed_set(*[
                _pubmed_xml(pmid, f"Paper {pmid}", notices if corrections else [])
                for pmid, notices in titles]))
            with TemporaryDirectory() as temporary:
                root = Path(temporary)
                registries = root / "disease-models" / "wwox" / "registries"
                registries.mkdir(parents=True)
                (registries / "fulltext_read_receipts.jsonl").touch()
                (registries / "paper_registry_current.md").write_text("", encoding="utf-8")
                harvest.write_seed(records, set(),
                                   registries / "corpus_seed_pubmed_20260806.tsv")
                orders.append([item["pmid"] for item in bq.build(root, "wwox")["queue"]])
        self.assertEqual(orders[0], orders[1],
                         "integrity status changed the reading order; it is an eligibility "
                         "gate, not a sort key")

    def test_no_held_records_means_no_integrity_section(self) -> None:
        """A gate that fires on every run is a gate nobody reads."""
        report = {"disease": "wwox", "held": [], "held_integrated": []}
        self.assertEqual(bq._render_integrity(report), [])

    def test_retraction_status_reaches_the_rendered_queue(self) -> None:
        """XML → TSV → queue → a row a reader cannot miss.

        The harvester carried `corrections` into the seed and the queue ignored the column,
        so "a paper under an expression of concern reaches triage looking clean" stayed true
        while the fix was reported as done. A column nothing reads is a column that does not
        exist.
        """
        with TemporaryDirectory() as temporary:
            registries = Path(temporary)
            header = ("pmid\tyear\tpubmed_free_full_text_link\ttype\tdoi\tcorrections\t"
                      "title\n")
            rows = (
                "11111111\t2025\tyes\tprimary\t10.1000/a\tRetractionIn:42464650\tRetracted\n"
                "22222222\t2025\tyes\tprimary\t10.1000/b\tExpressionOfConcernIn:9\tConcern\n"
                "33333333\t2025\tyes\tprimary\t10.1000/c\tErratumIn:8\tErratum\n"
                "44444444\t2025\tyes\tprimary\t10.1000/d\t\tClean\n"
            )
            (registries / "corpus_seed_pubmed_20260806.tsv").write_text(
                header + rows, encoding="utf-8")
            seeds, _ = bq.load_seeds(registries)
            flags = {seed["pmid"]: bq._integrity(seed) for seed in seeds}
        self.assertEqual(flags, {"11111111": "retracted", "22222222": "concern",
                                 "33333333": "corrected", "44444444": ""})

    def test_a_seed_without_the_column_is_unknown_not_clean(self) -> None:
        """The hazard the FREE_FULL_TEXT_COLUMNS comment was written about, fifty lines up.

        A snapshot harvested before `corrections` existed carries no integrity data, and
        `.get(...) or ""` reported every one of those rows as carrying no notice —
        indistinguishable from a true zero, and silent.
        """
        self.assertEqual(bq._integrity({"pmid": "1"}), "unknown")
        self.assertEqual(bq._integrity({"pmid": "1", "corrections": ""}), "")
        self.assertEqual(bq._eligibility("unknown"), "",
                         "unknown must not become a hold — it is a gap, not a finding")

    def test_a_retracted_publication_type_holds_without_a_correction_link(self) -> None:
        """This test sat below the empty-`corrections` early return, so it could never fire
        in the only case it exists for: a record PubMed types as retracted whose
        CommentsCorrections link is absent or lost in harvest. Dead code reading as a net."""
        self.assertEqual(
            bq._integrity({"corrections": "", "type": "Journal Article; Retracted Publication"}),
            "retracted")

    def test_whitespace_around_a_reftype_does_not_lose_the_hold(self) -> None:
        self.assertEqual(bq._integrity({"corrections": " RetractionIn : 42464650"}), "retracted")

    def test_the_unchecked_caveat_survives_alongside_a_finding(self) -> None:
        """It lived only in the `not held` branch, so it vanished in the mixed case — the
        reader was told 2 records were held and nothing about 459 never looked at."""
        report = {"disease": "wwox", "held_integrated": [], "held_referenced": [],
                  "held": [{"pmid": "1", "integrity": "retracted", "record": "",
                            "integrated": False, "current_references": []}],
                  "integrity_unknown": [{"pmid": "2"}]}
        self.assertIn("no correction data", "\n".join(bq._render_integrity(report)))

    def test_unchecked_records_are_reported_even_with_no_holds(self) -> None:
        report = {"disease": "wwox", "held": [], "held_integrated": [],
                  "held_referenced": [], "integrity_unknown": [{"pmid": "1"}]}
        rendered = "\n".join(bq._render_integrity(report))
        self.assertIn("not integrity *clean*", rendered)
        self.assertIn("Re-harvest", rendered)

    def test_the_live_corpus_has_no_unchecked_records(self) -> None:
        """Today every row comes from the 2026-08-06 snapshot. If this ever fails, the
        integrity gate has gone partially blind and the report must say so."""
        report = bq.build(ROOT, "wwox")
        self.assertEqual(report["integrity_unknown"], [])

    def test_an_erratum_is_not_a_retraction(self) -> None:
        """Both are `corrections` in the XML and they mean opposite things for reading."""
        self.assertEqual(bq._integrity({"corrections": "ErratumIn:1; RetractionIn:2"}),
                         "retracted")
        self.assertEqual(bq._integrity({"corrections": "ErratumIn:1"}), "corrected")
        # A checked row with no notice. The unchecked case is `unknown` — see
        # test_a_seed_without_the_column_is_unknown_not_clean.
        self.assertEqual(bq._integrity({"corrections": ""}), "")

    def test_editorial_notice_direction_is_not_mistaken_for_the_affected_paper(self) -> None:
        """`RetractionOf` lives on the notice; `RetractionIn` lives on the paper."""
        affected = {"corrections": "RetractionIn:42464650"}
        notice = {"corrections": "RetractionOf:23446842"}
        concern_notice = {"corrections": "ExpressionOfConcernFor:16223882"}

        self.assertEqual(bq._integrity(affected), "retracted")
        self.assertEqual(bq._eligibility(bq._integrity(affected)), bq.HOLD)
        self.assertEqual(bq._integrity(notice), "retraction_notice")
        self.assertEqual(bq._eligibility(bq._integrity(notice)), "")
        self.assertEqual(bq._integrity(concern_notice), "concern_notice")
        self.assertEqual(bq._eligibility(bq._integrity(concern_notice)), "")

        # 🔴 THE ARM THIS SUITE WAS MISSING, AND THE ONE THE CORPUS ACTUALLY EXERCISES.
        # `ErratumFor` lives on the correction notice; `ErratumIn` lives on the paper it
        # corrects. Until 2026-09-20 both returned `corrected`, so PMID 38355659
        # (`Correction: WWOX promotes osteosarcoma development via upregulation of Myc`,
        # `ErratumFor:38182577`) was indistinguishable from PMID 38182577 itself — in a
        # function whose docstring promises to preserve the direction of the link. Two of the
        # three editorial notices in this corpus are errata, and neither retraction nor
        # concern arm above could ever have caught it.
        erratum_notice = {"corrections": "ErratumFor:38182577"}
        affected_by_erratum = {"corrections": "ErratumIn:38355659"}
        self.assertEqual(bq._integrity(erratum_notice), "erratum_notice")
        self.assertEqual(bq._integrity(affected_by_erratum), "corrected")
        self.assertNotEqual(bq._integrity(erratum_notice),
                            bq._integrity(affected_by_erratum),
                            "the notice and the paper it annotates are different objects")
        # Eligibility is unchanged in both directions: an erratum is not an integrity event,
        # so this repair renames nothing that gates anything.
        self.assertEqual(bq._eligibility(bq._integrity(erratum_notice)), "")
        self.assertEqual(bq._eligibility(bq._integrity(affected_by_erratum)), "")
        # Every value the classifier can return is printable, or the queue renders a row
        # whose integrity is known to the code and invisible to the reader.
        for state in ("retracted", "concern", "retraction_notice", "concern_notice",
                      "erratum_notice", "corrected"):
            self.assertIn(state, bq.INTEGRITY_PREFIX)
            self.assertIn(state, bq.INTEGRITY_ACTION)

    def test_the_live_corpus_separates_the_three_editorial_notices_it_holds(self) -> None:
        """Not a fixture: the three notices in the 2026-08-06 seed, classified from their own
        `corrections` column, each distinct from the paper it annotates."""
        seeds, _ = bq.load_seeds(REGISTRIES)
        by_pmid = {item.get("pmid"): item for item in seeds}
        pairs = (("38355659", "38182577", "erratum_notice", "corrected"),
                 ("30470736", "29724996", "erratum_notice", "corrected"),
                 ("28373548", "16223882", "concern_notice", "concern"))
        for notice, affected, notice_state, affected_state in pairs:
            with self.subTest(notice=notice):
                self.assertIn(notice, by_pmid)
                self.assertIn(affected, by_pmid)
                self.assertEqual(bq._integrity(by_pmid[notice]), notice_state)
                self.assertEqual(bq._integrity(by_pmid[affected]), affected_state)
                # The notice never inherits the hold of what it documents.
                self.assertEqual(bq._eligibility(bq._integrity(by_pmid[notice])), "")

    def test_the_rendered_table_shows_the_integrity_flag(self) -> None:
        report = {
            "disease": "wwox", "seed_files": ["s.tsv"], "seed_occurrences": 1,
            "duplicate_occurrences": 0, "seed_total": 1, "free_full_text": 1,
            "year_min": 2025, "year_max": 2025, "published_since_2020": 1,
            "counts": {"screened": 1}, "actions": {"NEW": 1}, "outstanding": 1,
            "ready_now": 1,
            "queue": [{"triage_class": "NEW", "action": "read", "pmid": "11111111",
                       "year": "2025", "title": "A paper", "free_full_text": "yes",
                       "integrity": "retracted", "type": "primary", "depth": "screened",
                       "record": "", "source": "s.tsv"}],
        }
        self.assertIn("🛑 RETRACTED", bq.render(report, limit=0))

    def test_the_free_full_text_summary_matches_the_rows_it_summarises(self) -> None:
        """`0 <= 706` was true and useless.

        The summary read `seed["free_full_text"]` while the rows went through
        `_free_full_text`, so after the harvester renamed the column the generated queue
        announced "706 records, 0 with free full text" directly above 468 rows marked `yes`.
        A total that cannot disagree with its own rows is the only version worth asserting.
        """
        report = bq.build(ROOT, "wwox")
        self.assertEqual(
            report["free_full_text"],
            sum(1 for item in report["queue"] if item["free_full_text"] == "yes"))
        self.assertGreaterEqual(report["free_full_text"], report["ready_now"])

    def test_committed_markdown_lists_every_seed_record_with_status(self) -> None:
        report = bq.build(ROOT, "wwox")
        rendered = bq.render(report, limit=0)
        queue_tables = rendered.split("## Complete outstanding queue", 1)[1]
        self.assertEqual(
            queue_tables.count("https://pubmed.ncbi.nlm.nih.gov/"), report["seed_total"])
        self.assertIn("| full text | PAPER ", rendered)
        self.assertIn("| abstract only | PAPER ", rendered)

    # 🔴 EVERY HEADING IS A BOUNDARY; ONLY SOME BLOCKS ARE COUNTABLE RECORDS. The two jobs are
    # separated because conflating them is how the previous cut mis-measured: using only `paper N`
    # as a boundary let a PAPER block run to the NEXT PAPER, swallowing whatever records sat
    # between them. It happens not to change today's figure (59 either way), and a latent
    # over-count in a denominator makes the guard weaker, silently, on the day it does.
    # The boundary rule is the one `registry_records.py` already carries and that the independent
    # verification of 2026-09-11 corrected there; the countable shapes are that file's vocabulary
    # for this registry, restated here rather than imported so the suite keeps no dependency on
    # the tool it is not testing.
    _ANY_HEADING = re.compile(r"^#{1,4}[ \t]+\S.*$", re.M)
    _COUNTABLE_RECORD = re.compile(
        r"^(?:paper\s+\d+|corpus\s+pmid\s+\d+|corpus\s+p\d+)\b")

    _IDENTIFIER_LINE = re.compile(r"(?m)^\*\*identifier:\*\*\s*(.*)$")

    @classmethod
    def _registered_study_pmids(cls, registry_text: str,
                                notice_pmids: frozenset = frozenset()) -> dict:
        """PMID -> record id, for every registry record declaring full text that is a STUDY.

        🔴 A COUNT CANNOT SAY *WHICH*, AND ON 2026-09-20 THAT MATTERED. The comparison read
        77 against 77 and was green, while one study was read and unregistered (42082822) and
        one record was registered and matched no seed (`PAPER 059`). Two identity mismatches
        cancelled in the cardinality and the guard could not see either. The set is built here
        and the count is derived from it, so the two can never disagree again.
        """
        found: dict[str, str] = {}
        for record_id, block in cls._countable_blocks(registry_text, notice_pmids):
            if not any(marker in block for marker in bq.FULL_TEXT_MARKERS):
                continue
            identifier = cls._IDENTIFIER_LINE.search(block)
            pmids = bq.identifiers(identifier.group(1))[0] if identifier else []
            for pmid in pmids:
                found.setdefault(pmid, record_id)
            if not pmids:
                found.setdefault(f"(no PMID) {record_id}", record_id)
        return found

    @classmethod
    def _countable_blocks(cls, registry_text: str, notice_pmids: frozenset):
        """Every `(record_id, block)` that is a countable study record, notices excluded."""
        heads = [match.start() for match in cls._ANY_HEADING.finditer(registry_text)]
        for start, end in zip(heads, heads[1:] + [len(registry_text)]):
            block = registry_text[start:end]
            record_id = block.split("\n", 1)[0].lstrip("#").strip()
            if not cls._COUNTABLE_RECORD.match(record_id):
                continue
            if notice_pmids:
                identifier = cls._IDENTIFIER_LINE.search(block)
                if identifier and any(pmid in notice_pmids
                                      for pmid in bq.identifiers(identifier.group(1))[0]):
                    continue
            yield record_id, block

    @classmethod
    def _papers_claiming_full_text(cls, registry_text: str,
                                   notice_pmids: frozenset = frozenset()) -> int:
        """Count REGISTRY RECORDS carrying at least one full-text marker — not marker occurrences.

        The unit matters and was wrong twice, in the same direction both times: the denominator
        described a narrower population than the numerator.

        2026-09-09 — markers are not papers. `report["counts"]["full text"]` is a count of
        STUDIES; a substring tally over the registry is a count of STRINGS, and a single record
        routinely carries two markers (one carried six). That let the registry side read 89 where
        only 59 records actually claimed full text, so the guard passed while the queue overstated
        coverage by 21 studies — green on exactly the condition it exists to refuse.

        2026-09-20 — records are not only PAPER records. `registry_index` resolves read depth from
        EVERY record in this file, `CORPUS P###` included: three CORPUS records declare a
        `complete_fulltext_read` today and are counted as read by the numerator. The denominator
        counted `paper N` alone, so those three reads could never appear on the registry side of
        the comparison. `CORPUS P261` states the reason they are not simply renamed — *"corpus
        placeholder, deliberately not promoted to a PAPER record"*: the classification is a
        scientific decision, so the measurement is what moves to meet it, never the other way.

        🔴 THIS DOES NOT RELAX THE GUARD. The invariant is unchanged — counted-as-read may never
        exceed what the registry itself claims — and each record still contributes at most once.
        What changed is that both sides now enumerate the same population. `CORPUS-STUB-###` stays
        out: a stub is a placeholder by construction, and none of the 168 in this file declares a
        full-text marker, so including them would only widen the denominator with records that can
        never claim a read.

        2026-09-20, second arm — records are not only studies. An editorial notice is a
        publication and is not a study: a correction, an erratum and an expression-of-concern
        notice are readable, citable and worth a receipt, and none of them reports a result.
        `PAPER 092` is one — `Source type: published erratum, attached to PMID 38182577` — and it
        declares full text, so it sat on the registry side of a comparison whose other side the
        operator has ruled must not contain notices. `notice_pmids` comes from
        `batch_queue.editorial_notice_pmids`, which derives it from the same `_integrity`
        classifier the queue side uses: ONE definition, so the two populations cannot drift apart
        by disagreeing about the term. The notice keeps its record, its receipt, its provenance
        and its link to the paper it annotates — it is excluded from a count, not from the
        repository.
        """
        return sum(
            1 for _record_id, block in cls._countable_blocks(registry_text, notice_pmids)
            if any(marker in block for marker in bq.FULL_TEXT_MARKERS))

    @staticmethod
    def _read_study_pmids(report: dict, notice_pmids: frozenset) -> set:
        """The PMIDs the queue counts as STUDIES read in full."""
        return {item["pmid"] for item in report["queue"]
                if item["depth"] == "full text" and item["pmid"]
                and item["pmid"] not in notice_pmids}

    def test_coverage_is_not_overstated_against_the_registry(self) -> None:
        """Two invariants over the same two populations, because one of them is not enough.

        CARDINALITY — studies counted as read may never exceed the registry's own full-text
        study claims. IDENTITY — every study actually read must be findable in the registry by
        its own PMID.

        🔴 WHY BOTH. On 2026-09-20 this read 77 against 77 and was green while PMID 42082822 was
        read and unregistered and `PAPER 059` was registered and matched no seed. One mismatch
        on each side, cancelling in the count: a study with no canonical representation was
        hidden behind an unrelated record that happened to balance the arithmetic. A count
        cannot say *which*, so it cannot notice that.

        The asymmetry is deliberate and is the repository's own rule about negatives. A read
        study with no record is a FAILURE — the reading exists and the registry does not carry
        it. A registered study outside the current read set is NOT: `PAPER 059` (PMID 17803050)
        was supplied by the operator and read in full, and it is simply absent from the
        2026-08-06 PubMed seed. So the second set is REPORTED, never asserted, and the counts
        are allowed to differ.
        """
        registry = (REGISTRIES / "paper_registry_current.md").read_text(encoding="utf-8").lower()
        notices = frozenset(bq.editorial_notice_pmids(REGISTRIES))
        registered = self._registered_study_pmids(registry, notices)
        report = bq.build(ROOT, "wwox")
        read = self._read_study_pmids(report, notices)

        # The set and the census must agree, or one of them is measuring something else.
        self.assertEqual(len(read), report["study_counts"].get("full text", 0))

        read_not_registered = sorted(read - set(registered))
        registered_not_read = sorted(set(registered) - read)
        summary = (f"READ_STUDIES={len(read)} REGISTERED_STUDIES={len(registered)} · "
                   f"READ_NOT_REGISTERED={read_not_registered or '{}'} · "
                   f"REGISTERED_NOT_IN_READ_SET="
                   f"{[f'{pmid} ({registered[pmid]})' for pmid in registered_not_read] or '{}'}")

        self.assertLessEqual(
            len(read), len(registered) + len(registered_not_read),
            f"CARDINALITY: more studies are counted as read than the registry claims. {summary}")
        self.assertEqual(
            [], read_not_registered,
            f"IDENTITY: these studies were read in full and no registry record carries their "
            f"PMID. Only a BATCH_COMMIT closes this, and a matching count elsewhere does not. "
            f"{summary}")

    def test_a_normal_full_text_study_is_in_the_study_numerator(self) -> None:
        """Arm 1 — anti-vacuity. If the exclusion removed studies too, every arm below would
        pass while the measurement collapsed."""
        report = bq.build(ROOT, "wwox")
        self.assertGreater(report["study_counts"]["full text"], 70,
                           "the study numerator must still hold the corpus's real reading")
        seeds, _ = bq.load_seeds(REGISTRIES)
        by_pmid = {item.get("pmid"): item for item in seeds}
        # PMID 38182577 is a study AND is annotated by a correction notice: being pointed at by
        # a notice must not remove a paper from the study population (arm 6).
        self.assertFalse(bq.is_editorial_notice(by_pmid["38182577"]))
        self.assertFalse(bq.is_editorial_notice(by_pmid["16223882"]))
        self.assertFalse(bq.is_editorial_notice(by_pmid["29724996"]))

    def test_the_three_editorial_notices_leave_the_study_numerator_and_only_them(self) -> None:
        """Arms 2, 3 and 4 — erratum notice, correction notice and expression-of-concern notice.

        Asserted on the live corpus rather than a fixture, and by NAME rather than by count: the
        difference between the two censuses must be exactly the read notices, so the arm fails
        both if a notice stays in and if a study is dropped.
        """
        report = bq.build(ROOT, "wwox")
        removed = report["counts"]["full text"] - report["study_counts"]["full text"]
        seeds, _ = bq.load_seeds(REGISTRIES)
        index = bq.registry_index(REGISTRIES)
        read_notices = set()
        for seed in seeds:
            if not bq.is_editorial_notice(seed):
                continue
            hit = index.get(f"pmid:{seed.get('pmid','')}")
            if hit and hit["depth"] == "full text":
                read_notices.add(seed["pmid"])
        self.assertEqual({"38355659", "30470736", "28373548"}, read_notices)
        self.assertEqual(len(read_notices), removed)
        by_pmid = {item.get("pmid"): item for item in seeds}
        self.assertEqual(bq._integrity(by_pmid["38355659"]), "erratum_notice")
        self.assertEqual(bq._integrity(by_pmid["30470736"]), "erratum_notice")
        self.assertEqual(bq._integrity(by_pmid["28373548"]), "concern_notice")
        for state in bq.EDITORIAL_NOTICE_STATES:
            self.assertIn(state, bq.INTEGRITY_PREFIX, "a notice state must stay printable")

    def test_a_retraction_notice_is_excluded_and_a_retracted_study_is_not(self) -> None:
        """Arm 4, and the boundary that keeps it honest. `RetractionOf` marks the notice;
        `RetractionIn` marks the paper. A RETRACTED STUDY IS STILL A STUDY — one that may not
        support a claim, which is a hold, not a change of kind."""
        self.assertTrue(bq.is_editorial_notice({"corrections": "RetractionOf:23446842"}))
        self.assertFalse(bq.is_editorial_notice({"corrections": "RetractionIn:42464650"}))
        self.assertFalse(bq.is_editorial_notice({"corrections": "ExpressionOfConcernIn:28373548"}))
        self.assertFalse(bq.is_editorial_notice({"corrections": "ErratumIn:38355659"}))
        # Arm 7 — eligibility and direction are untouched by the study/notice split.
        self.assertEqual(bq._eligibility(bq._integrity({"corrections": "RetractionIn:42464650"})),
                         bq.HOLD)
        self.assertEqual(bq._eligibility(bq._integrity({"corrections": "RetractionOf:23446842"})),
                         "")
        self.assertEqual(bq._eligibility(bq._integrity({"corrections": "ExpressionOfConcernIn:1"})),
                         bq.HOLD)

    def test_a_notice_already_held_as_a_paper_record_leaves_the_denominator(self) -> None:
        """Arm 5 — `PAPER 092` is PMID 38355659, `Source type: published erratum`, and it
        declares full text. Excluded from the study denominator by the same definition the
        numerator uses, and by exactly one record, so the arm fails if the filter over- or
        under-reaches."""
        registry = (REGISTRIES / "paper_registry_current.md").read_text(encoding="utf-8").lower()
        notices = frozenset(bq.editorial_notice_pmids(REGISTRIES))
        self.assertIn("38355659", notices)
        with_notices = self._papers_claiming_full_text(registry)
        without = self._papers_claiming_full_text(registry, notices)
        self.assertEqual(with_notices - 1, without,
                         "exactly one registry record claiming full text is an editorial notice")
        # And it is that record, not some other one: the block still exists and still declares
        # what it is. Excluded from a count, never deleted.
        self.assertIn("## paper 092", registry)
        self.assertIn("published erratum", registry)

    def test_the_paper_a_notice_annotates_stays_in_both_populations(self) -> None:
        """Arm 6 — the corrected study is counted normally on both sides.

        PMID 38182577 carries `ErratumIn:38355659`. It is a study, it is eligible, and it must
        appear in the study numerator once its record declares the reading — which is what
        `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01` proposes. What this arm pins today is that
        nothing about the notice removed it.
        """
        seeds, _ = bq.load_seeds(REGISTRIES)
        by_pmid = {item.get("pmid"): item for item in seeds}
        self.assertEqual(bq._integrity(by_pmid["38182577"]), "corrected")
        self.assertEqual(bq._eligibility(bq._integrity(by_pmid["38182577"])), "")
        self.assertFalse(bq.is_editorial_notice(by_pmid["38182577"]))
        notices = frozenset(bq.editorial_notice_pmids(REGISTRIES))
        self.assertNotIn("38182577", notices)
        # 16223882 is under an expression of concern: HELD, and still a study.
        self.assertEqual(bq._eligibility(bq._integrity(by_pmid["16223882"])), bq.HOLD)
        self.assertNotIn("16223882", notices)

    def test_the_two_censuses_partition_the_seed_and_neither_hides_a_reading(self) -> None:
        """Arm 7, the structural half. `counts` is untouched — same totals, same depths, every
        receipt still visible in the rendered queue — and `study_counts` plus the notices
        partition the same corpus. A census that reclassified rows would have hidden evidence
        to move a number."""
        report = bq.build(ROOT, "wwox")
        self.assertEqual(sum(report["counts"].values()), report["seed_total"])
        self.assertEqual(sum(report["study_counts"].values()) + report["editorial_notices"],
                         report["seed_total"])
        for depth, total in report["study_counts"].items():
            self.assertLessEqual(total, report["counts"][depth],
                                 "the study census can never exceed the census it is drawn from")
        # The reading of a notice is not erased: its row keeps its depth and names its receipt.
        rendered = bq.render(report, limit=0)
        self.assertIn("FTR-20260909-30470736-01", rendered)
        self.assertIn("CORRECTION NOTICE", rendered)

    def test_a_paper_with_two_markers_counts_once(self) -> None:
        """The regression for the unit error itself: markers are not papers."""
        one = "#### paper 001\nstatus: full text reviewed\ndepth: complete_fulltext_read\n"
        two = one + "#### paper 002\nstatus: abstract only\n"
        self.assertEqual(self._papers_claiming_full_text(one), 1)
        self.assertEqual(self._papers_claiming_full_text(two), 1)
        self.assertEqual(
            self._papers_claiming_full_text(two + "#### paper 003\nfull text reviewed\n"), 2)

    def test_equal_counts_can_hide_two_opposite_identity_mismatches(self) -> None:
        """🔴 THE FAILURE MODE ITSELF, as a fixture, because it shipped green.

        READ = {A, B} and REGISTERED = {A, C}. Both have cardinality 2, so a guard that
        compares only counts reports agreement — and the real 2026-09-20 state was exactly this
        shape: 42082822 read and unregistered, PAPER 059 registered and outside the read set,
        77 against 77.

        The count is asserted equal here ON PURPOSE. That assertion is what the guard used to
        be, and it passes; the two below are what it could not see.
        """
        registry = (
            "## paper 900\n**identifier:** pmid 11111111\n**evidence depth:** full text reviewed\n"
            "## paper 901\n**identifier:** pmid 33333333\n**evidence depth:** full text reviewed\n"
        )
        report = {"queue": [
            {"pmid": "11111111", "depth": "full text"},
            {"pmid": "22222222", "depth": "full text"},
        ]}
        registered = self._registered_study_pmids(registry, frozenset())
        read = self._read_study_pmids(report, frozenset())

        self.assertEqual({"11111111", "33333333"}, set(registered))
        self.assertEqual({"11111111", "22222222"}, read)
        # The old guard, verbatim in spirit: equal counts, no complaint.
        self.assertEqual(len(read), len(registered),
                         "the fixture must be cardinality-balanced or it proves nothing")
        # The two properties the count cannot carry.
        self.assertEqual({"22222222"}, read - set(registered), "READ_NOT_REGISTERED")
        self.assertEqual({"33333333"}, set(registered) - read, "REGISTERED_NOT_IN_READ_SET")
        # And the record is named, not just the PMID: a diagnostic that cannot be acted on is
        # a diagnostic nobody acts on.
        self.assertEqual("paper 901", registered["33333333"])

    def test_a_post_harvest_corpus_record_is_countable_by_its_pmid(self) -> None:
        """The new identity form, and the old ones beside it, in one population.

        `CORPUS PMID n` carries no corpus-paper number because it has none; it is countable on
        exactly the same terms as `CORPUS Pn`, and adding it must not disturb either historical
        form or start matching prose.
        """
        registry = (
            "# paper registry current\n"
            "## corpus pmid 42082822\n**identifier:** pmid 42082822\n"
            "**evidence depth:** complete_fulltext_read\n"
            "## corpus p261\n**identifier:** pmid 21731849\n**evidence depth:** full text reviewed\n"
            "## corpus-stub-004\n**identifier:** pmid 33255508\n**evidence depth:** full text reviewed\n"
            "## corpus overview\nfull text reviewed\n"
        )
        registered = self._registered_study_pmids(registry, frozenset())
        self.assertEqual({"42082822": "corpus pmid 42082822",
                          "21731849": "corpus p261"}, registered,
                         "the post-harvest form counts; the stub and the prose section do not")

    def test_a_read_corpus_record_is_counted_once(self) -> None:
        """The 2026-09-20 arm: the numerator counts a read CORPUS record, so the denominator must.

        Two markers in one CORPUS record are still one record, for the same reason two markers in
        one PAPER record are.
        """
        one = "## CORPUS P308\nstatus: read\ndepth: full text reviewed\n"
        self.assertEqual(self._papers_claiming_full_text(one.lower()), 1)
        both = one + "## CORPUS P309\ndepth: full text reviewed — complete_fulltext_read\n"
        self.assertEqual(self._papers_claiming_full_text(both.lower()), 2)

    def test_paper_and_corpus_stay_distinct_records(self) -> None:
        """Adjacent records of different kinds are two records, and neither absorbs the other.

        The boundary arm: with `paper N` as the only boundary, the PAPER block ran to the next
        PAPER and swallowed the CORPUS record between them — so an unread PAPER inherited a
        CORPUS record's marker and the denominator grew by a record that claims nothing.
        """
        text = ("## paper 001\nstatus: abstract only\n"
                "## corpus p222\ndepth: full text reviewed\n"
                "## corpus p223\ndepth: complete_fulltext_read\n"
                "## paper 002\ndepth: full text reviewed\n")
        # Two CORPUS and one PAPER declare a read; `paper 001` declares none and must not inherit
        # the markers of the two records that follow it. The count is what separates the two
        # rules: under `paper N`-only boundaries this reads 2 — one for the span `paper 001`
        # absorbed, one for `paper 002` — so the arm fails against the helper it replaces.
        self.assertEqual(self._papers_claiming_full_text(text), 3)

    def test_the_denominator_is_not_inflated_by_prose_or_placeholders(self) -> None:
        """Anti-inflation. A denominator that grows for free is a guard that stops refusing.

        Three shapes that must never count: the file's own title (`# Paper Registry Current`
        lower-cases to a heading beginning `paper `, which a naive `paper|corpus` alternation
        matches), a prose section, and `CORPUS-STUB-###` — a placeholder, never a read.
        """
        noise = ("# paper registry current\n\n> public edition — full text reviewed\n"
                 "## corpus overview\nfull text reviewed\n"
                 "## CORPUS-STUB-004\ndepth: full text reviewed\n".lower())
        self.assertEqual(self._papers_claiming_full_text(noise), 0)
        # And the guard still counts the real thing when it is there, so this is not vacuous.
        self.assertEqual(
            self._papers_claiming_full_text(noise + "## paper 007\nfull text reviewed\n"), 1)

    def test_committed_queue_is_current(self) -> None:
        self.assertTrue(QUEUE.is_file(), f"missing generated queue: {QUEUE}")
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "framework" / "scripts" / "batch_queue.py"),
                "--root",
                str(ROOT),
                "--check",
                str(QUEUE),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            "The committed batch queue has drifted. Regenerate it:\n"
            "  python3 framework/scripts/batch_queue.py "
            "--out disease-models/wwox/registries/batch_queue.md\n"
            f"{result.stdout}{result.stderr}",
        )


class ActionabilityTests(unittest.TestCase):
    """The queue must answer "what is unprocessed?", not delegate it back to the reader."""

    def test_every_record_carries_an_authoritative_triage_verdict(self) -> None:
        report = bq.build(ROOT, "wwox")
        for item in report["queue"]:
            self.assertIn(
                item["triage_class"],
                bq.ACTION,
                f"{item['pmid']} has no recognised intake verdict",
            )

    def test_no_record_is_left_in_an_unresolved_bucket(self) -> None:
        """Regression on the earlier design, where 45% of the corpus meant 'go find out'."""
        report = bq.build(ROOT, "wwox")
        undecided = [item for item in report["queue"] if item["triage_class"] == "unmatched"]
        self.assertFalse(undecided, "the start-here answer must not contain an unmatched bucket")

    def test_start_here_total_matches_the_two_actionable_classes(self) -> None:
        report = bq.build(ROOT, "wwox")
        expected = report["actions"].get("NEW", 0) + report["actions"].get("CORPUS_CATALOGUED", 0)
        self.assertEqual(report["outstanding"], expected)
        self.assertLessEqual(report["ready_now"], report["outstanding"])

    def test_verdicts_agree_with_the_intake_gate_itself(self) -> None:
        """One classifier, not two: this file must reuse the gate, never approximate it."""
        report = bq.build(ROOT, "wwox")
        records = bq.triage.build_index(ROOT)
        index = bq.triage.build_identifier_index(ROOT)
        sample = report["queue"][:25]
        for item in sample:
            line = f"{item['title']}. — PMID {item['pmid']} · DOI  · YEAR {item['year']}"
            verdict = bq.triage.match_row(
                {"line": line, "raw": "", "aggregate": "no"}, records, index
            )
            self.assertEqual(verdict["class"], item["triage_class"], item["pmid"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
