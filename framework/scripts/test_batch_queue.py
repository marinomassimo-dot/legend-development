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

    def test_coverage_is_not_overstated_against_the_registry(self) -> None:
        """Records counted as read may never exceed the registry's own full-text claims."""
        registry = (REGISTRIES / "paper_registry_current.md").read_text(encoding="utf-8").lower()
        claimed = sum(registry.count(marker) for marker in bq.FULL_TEXT_MARKERS)
        report = bq.build(ROOT, "wwox")
        self.assertLessEqual(report["counts"].get("full text", 0), claimed)

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
