#!/usr/bin/env python3
"""Regression suite for the surface census.

Three things are guarded, in descending order of how quietly they would fail.

**A suffix is not a surface.** Two files in the live corpus are the article's PDF text layer
wrapped in `<article><section><pre>` — an `.html` extension over a dump, no JATS metadata
behind it. Calling them `structured` would tell every future session that the corrupt text
layer of `PMID 17803050` is publisher markup, which is the failure of 2026-08-09 with a
friendlier filename. The rule is pinned from both sides here: a dump must not read as
markup, and markup that merely *contains* a `<pre>` must not read as a dump.

**The sentinel answers for the surface you would open.** Half the structured papers keep the
publisher's PDF beside the XML and most of those PDFs are corrupt. Scoring a paper on its
worst file marks papers `SUSPECT` whose XML is fine — an alarm that sends readers away from
the one surface rule 5d sends them to.

**A queue entry that cannot be identified is declared, not dropped.** The identity regex is
anchored deliberately; the loose form resolves `FT-020` to the paper that *cites* the three
works it is asking for. Under-resolving lands in a ledger a human reads. Mis-resolving
attaches a surface verdict to the wrong paper and nothing downstream ever questions it.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))

import surface_census as census  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
# 🔴 Derived, with an override — never a path pinned to one machine. The corpus is gitignored
# and lives once, in the main checkout, while sessions now run in per-session worktrees where
# `ROOT/files/fulltext` does not exist. Without the override the live class would skip in every
# worktree, and skipping is how a suite stays green in an environment that cannot exhibit the
# defect it is testing for. Point `LEGEND_CORPUS_DIR` at the corpus and the class runs.
LIVE_CORPUS = Path(os.environ.get("LEGEND_CORPUS_DIR", ROOT / "files" / "fulltext"))

JATS = (b'<?xml version="1.0"?><article><front><journal-meta><journal-title>J</journal-title>'
        b"</journal-meta><article-meta><title-group><article-title>T</article-title>"
        b"</title-group></article-meta></front><body><p>Body text.</p></body></article>")
DUMP = (b'<article><section class="front-matter"><pre>Journal of Things\nVol 1\n'
        b"Body text as extracted from the page.</pre></section></article>")
PUBLISHER_HTML = b"<html><body><h1>Title</h1><p>Body text.</p></body></html>"


def corpus(directory: Path, **files: bytes) -> Path:
    for name, payload in files.items():
        (directory / name.replace("__", ".")).write_bytes(payload)
    return directory


def build_fixture(test: unittest.TestCase, queue: str = None, **files: bytes):
    """A census over a throwaway root, so no test depends on the live repository."""
    temp = TemporaryDirectory()
    test.addCleanup(temp.cleanup)
    root = Path(temp.name)
    research = root / "disease-models" / "wwox" / "research"
    research.mkdir(parents=True)
    (research / "full_text_queue_current.md").write_text(
        queue if queue is not None else "## FT-001\n**Paper:** PMID 1111111 — a\n",
        encoding="utf-8")
    corpus_dir = root / "files" / "fulltext"
    corpus_dir.mkdir(parents=True)
    corpus(corpus_dir, **(files or {"PMID1111111_a__xml": JATS}))
    return census.build(root, corpus_dir, "wwox")


class FileClassification(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)

    def classify(self, name: str, payload: bytes) -> str:
        path = self.dir / name
        path.write_bytes(payload)
        return census.classify_file(path)

    def test_jats_markup_is_structured(self) -> None:
        self.assertEqual("structured", self.classify("PMID1_a_PMC.xml", JATS))

    def test_publisher_html_without_jats_is_still_structured(self) -> None:
        self.assertEqual("structured", self.classify("PMID2_a.html", PUBLISHER_HTML))

    def test_pre_block_without_jats_is_a_text_dump(self) -> None:
        self.assertEqual("text_dump", self.classify("PMID3_a.html", DUMP))

    def test_jats_containing_a_pre_block_is_not_demoted(self) -> None:
        """The other side of the rule. Demotion must need *both* signals, or a listing that
        happens to quote a `<pre>` would strip a real PMC deposit of its class."""
        payload = JATS.replace(b"<body><p>Body text.</p>", b"<body><pre>code</pre>")
        self.assertEqual("structured", self.classify("PMID4_a_PMC.xml", payload))

    def test_pdf_and_supplements_are_told_apart(self) -> None:
        self.assertEqual("pdf", self.classify("PMID5_a.pdf", b"%PDF-1.4"))
        self.assertEqual("other", self.classify("PMID5_a.handoff.md", b"# notes"))
        self.assertEqual("other", self.classify("PMID5_a_supplement.docx", b"PK\x03\x04"))


class SurfaceClassification(unittest.TestCase):
    def surface(self, *files) -> str:
        return census.Paper(pmid="1", files=list(files)).surface

    def test_structured_wins_over_a_companion_pdf(self) -> None:
        self.assertEqual("structured", self.surface(("a.xml", "structured"), ("a.pdf", "pdf")))

    def test_a_text_dump_does_not_make_a_paper_structured(self) -> None:
        self.assertEqual("pdf_only", self.surface(("a.html", "text_dump"), ("a.pdf", "pdf")))

    def test_a_paper_with_only_non_surfaces_is_absent(self) -> None:
        self.assertEqual("absent", self.surface(("a.handoff.md", "other")))

    def test_a_paper_with_no_local_file_is_absent(self) -> None:
        self.assertEqual("absent", self.surface())


class SentinelScope(unittest.TestCase):
    """The verdict describes the surface a reader would open, not the worst file present."""

    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        # A C0 control is the residue of a glyph that did not survive extraction — the
        # signature that made `P < 0.05` read as `P 5 0.05` on 2026-08-09.
        corpus(self.dir, PMID1_a__xml=JATS, PMID1_a__txt="Wwox\x01/\x01 mice".encode())

    def test_a_corrupt_derived_text_is_suspect_when_it_is_the_reading_surface(self) -> None:
        paper = census.Paper(pmid="1", files=[("PMID1_a.txt", "derived_text")])
        verdict, _detail = census.screen_paper(paper, self.dir, have_extractor=False)
        self.assertEqual("SUSPECT", verdict)

    def test_a_corrupt_companion_does_not_condemn_a_clean_structured_paper(self) -> None:
        paper = census.Paper(pmid="1", files=[("PMID1_a.xml", "structured"),
                                              ("PMID1_a.txt", "derived_text")])
        self.assertEqual("structured", paper.surface)
        verdict, _detail = census.screen_paper(paper, self.dir, have_extractor=False)
        self.assertEqual("clean", verdict)

    def test_a_pdf_without_an_extractor_is_not_screened_never_clean(self) -> None:
        (self.dir / "PMID2_a.pdf").write_bytes(b"%PDF-1.4")
        paper = census.Paper(pmid="2", files=[("PMID2_a.pdf", "pdf")])
        verdict, detail = census.screen_paper(paper, self.dir, have_extractor=False)
        self.assertEqual("not_screened", verdict)
        self.assertIn("extractor", detail)

    def test_a_paper_with_nothing_local_gets_no_verdict(self) -> None:
        self.assertEqual(("", ""), census.screen_paper(
            census.Paper(pmid="3"), self.dir, have_extractor=True))


class QueueResolution(unittest.TestCase):
    def test_an_anchored_pmid_resolves(self) -> None:
        resolved, losses = census.resolve_queue(
            "## FT-008\n**Paper:** PMID 30290271 — Hussain 2019\n")
        self.assertEqual({"30290271": ["FT-008"]}, resolved)
        self.assertEqual([], losses)

    def test_a_citing_pmid_in_prose_does_not_resolve(self) -> None:
        """FT-020, verbatim. The entry says in the same sentence that it is *not* resolved."""
        resolved, losses = census.resolve_queue(
            "## FT-020\n**Paper:** riferimenti 38, 39 e 87 di PMID 34214506 — "
            "non risolti a PMID\n**Priority:** HIGH\n")
        self.assertEqual({}, resolved)
        self.assertEqual([("FT-020", "no_pmid_declared",
                           "riferimenti 38, 39 e 87 di PMID 34214506 — non risolti a PMID")],
                         losses)

    def test_an_entry_without_an_identity_line_is_its_own_loss_state(self) -> None:
        _resolved, losses = census.resolve_queue("## FT-032\n**Priority:** HIGH\n")
        self.assertEqual([("FT-032", "no_identity_line", "—")], losses)

    def test_the_last_entry_is_not_swallowed(self) -> None:
        resolved, _losses = census.resolve_queue(
            "## FT-001\n**Paper:** PMID 1111111 — A\n\n---\n\n"
            "## FT-002\n**Paper:** PMID 2222222 — B\n")
        self.assertEqual({"1111111": ["FT-001"], "2222222": ["FT-002"]}, resolved)


class Accounting(unittest.TestCase):
    """`candidates == emitted + merged + duplicates + lost`, on a fixture built to strain it."""

    def assert_balances(self, result) -> None:
        self.assertEqual(
            result.corpus_papers + result.queue_entries,
            len(result.papers) + result.merged + result.duplicate_entries
            + len(result.losses),
        )

    def test_a_queue_that_overlaps_duplicates_and_misses_the_corpus(self) -> None:
        queue = (
            "## FT-001\n**Paper:** PMID 1111111 — local\n\n"      # merged with the corpus
            "## FT-002\n**Paper:** PMID 1111111 — local again\n\n"  # duplicate entry
            "## FT-003\n**Paper:** PMID 9999999 — never retrieved\n\n"  # absent
            "## FT-004\n**Paper:** 93 — Cheng 2020\n\n"           # unresolved
            "## FT-005\n**Priority:** HIGH\n"                     # no identity line
        )
        result = build_fixture(self, queue,
                               PMID1111111_a__xml=JATS, PMID2222222_b__pdf=b"%PDF-1.4")
        self.assert_balances(result)
        self.assertEqual(2, result.corpus_papers)
        self.assertEqual(1, result.merged)
        self.assertEqual(1, result.duplicate_entries)
        self.assertEqual(2, len(result.losses))
        self.assertEqual(3, len(result.papers))

    def test_the_rendered_page_states_the_identity_and_it_holds(self) -> None:
        text = census.render(build_fixture(self), "2026-08-10")
        self.assertIn("The two agree.", text)
        self.assertNotIn("THE TWO DISAGREE", text)


class TheCensusStaysOutOfTheQueue(unittest.TestCase):
    """🔴 The defect this file exists to prevent from coming back.

    The first version wrote the table into `full_text_queue_current.md`, where the operator
    asked for it. `session_self_eval.py` reads a PMID's presence in that queue as *declared
    reading debt* — so a derived table naming every corpus PMID cleared five unread premises
    that nobody had read, and `batch_queue.py`, which scans every `*_current.md` for PMIDs,
    drifted at the same time. Both checks were doing their job; the table was lying to them.

    The census is a whole generated file, like `coverage_report.md` and `batch_queue.md`,
    both of which `session_self_eval.LANDING_FILES` already excludes by name and for exactly
    this reason.
    """

    def test_the_queue_carries_no_generated_census(self) -> None:
        queue = (ROOT / "disease-models" / "wwox" / "research"
                 / "full_text_queue_current.md").read_text(encoding="utf-8")
        self.assertNotIn("Surface census", queue)
        self.assertNotIn("surface_census.py", queue)

    def test_the_census_is_not_a_landing_file(self) -> None:
        import session_self_eval  # noqa: PLC0415 — imported for its declared list only

        for pattern in session_self_eval.LANDING_FILES:
            self.assertNotIn("surface_census", pattern)

    def test_the_page_declares_itself_generated_and_says_where_it_belongs(self) -> None:
        """The header is what stops the next reader hand-editing a derived table, and what
        `test_generated_surfaces_are_regenerated.py` discovers. The destination it prints
        must not be a `*_current.md` file — that suffix is what `batch_queue.py` scans."""
        page = census.render(build_fixture(self), "2026-08-10")
        self.assertIn("Generated file — do not edit by hand", page)
        self.assertIn("--out disease-models/wwox/research/surface_census.md", page)
        self.assertNotIn("_current.md\n", page.split("```")[1])


class MissingCorpusIsNotAnEmptyCorpus(unittest.TestCase):
    def test_a_missing_corpus_refuses_rather_than_reporting_everything_absent(self) -> None:
        with TemporaryDirectory() as temp:
            completed = subprocess.run(
                [sys.executable, str(ROOT / "framework" / "scripts" / "surface_census.py"),
                 "--corpus", str(Path(temp) / "nowhere")],
                capture_output=True, text=True, check=False,
            )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("", completed.stdout)
        self.assertIn("not the same fact", completed.stderr)


@unittest.skipUnless(LIVE_CORPUS.is_dir(),
                     "local full-text corpus is gitignored and absent from this checkout")
class LiveCorpus(unittest.TestCase):
    """The two facts this census exists to state, checked against the real corpus."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.result = census.build(ROOT, LIVE_CORPUS, "wwox")

    def paper(self, pmid: str) -> census.Paper:
        return next(item for item in self.result.papers if item.pmid == pmid)

    def test_the_suzuki_html_is_a_text_dump_and_its_paper_is_not_structured(self) -> None:
        """`CLAUDE.md` rule 5d says PMID 17803050 has no structured deposit — no DOI, no
        PMCID — and had to be adjudicated against the printed page. A local `.html` exists
        anyway, and it is that page's text layer in markup. The census must agree with the
        rule, not with the filename."""
        self.assertIn("PMID17803050_Suzuki2007.html", self.result.text_dumps)
        self.assertEqual("pdf_only", self.paper("17803050").surface)

    def test_the_corpus_holds_both_classes_and_the_accounting_balances(self) -> None:
        surfaces = {paper.surface for paper in self.result.papers}
        self.assertEqual({"structured", "pdf_only", "absent"}, surfaces)
        self.assertEqual(
            self.result.corpus_papers + self.result.queue_entries,
            len(self.result.papers) + self.result.merged
            + self.result.duplicate_entries + len(self.result.losses),
        )

    def test_the_screen_finds_corruption_and_does_not_find_it_everywhere(self) -> None:
        """A screen that flagged nothing would be decorative; one that flagged everything
        would be useless. Bounded, not pinned to a constant the corpus will outgrow."""
        verdicts = [verdict for verdict, _detail in self.result.sentinel.values()]
        self.assertGreater(verdicts.count("SUSPECT"), 0)
        self.assertGreater(verdicts.count("clean"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
