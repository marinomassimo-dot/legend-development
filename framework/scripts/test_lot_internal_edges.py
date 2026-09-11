#!/usr/bin/env python3
"""Regressions for `lot_internal_edges.py`. Offline: the network routes are stubbed.

The property worth protecting is the one measured before the tool was written: a detector
built on citation alone reports three of the four edges the 2026-09-09 retrospective named
and looks complete, because an editor's introduction does not cite the chapter it
introduces. SAME_CONTAINER is therefore pinned here, and so is the distinction between a
member whose reference list could not be screened and a member that cites nothing.
"""

from __future__ import annotations

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import lot_internal_edges as tool


class LotEdges(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for directory in tool.DOSSIER_DIRS:
            (self.root / directory).mkdir(parents=True)
        self._refs = dict(tool.fetch_references.__dict__)
        self.real_refs = tool.fetch_references
        self.real_summaries = tool.fetch_summaries

    def tearDown(self) -> None:
        tool.fetch_references = self.real_refs
        tool.fetch_summaries = self.real_summaries
        self._tmp.cleanup()

    def stub(self, references: dict[str, tuple[list[str], str]],
             summaries: dict[str, dict]) -> None:
        tool.fetch_references = lambda pmid: references.get(pmid, ([], "not stubbed"))
        tool.fetch_summaries = lambda pmids: ({p: summaries[p] for p in pmids
                                               if p in summaries}, "")

    def test_a_lot_of_one_is_void_not_edgeless(self) -> None:
        self.assertEqual("INSUFFICIENT_DATA", tool.screen(["1"], offline=True).verdict)
        self.assertEqual(3, tool.main(["--offline", "1"]))

    def test_a_citation_between_members_is_an_edge(self) -> None:
        self.stub({"a": (["b", "z"], ""), "b": ([], "")}, {})
        edges = tool.screen(["a", "b"], root=self.root, pause=0).edges
        self.assertEqual([("a", "b", "CITES")],
                         [(e.source, e.target, e.kind) for e in edges])

    def test_the_container_edge_survives_when_no_citation_exists(self) -> None:
        """25238781 <-> 25245215: same issue, and neither cites the other."""
        self.stub(
            {"a": ([], ""), "b": ([], "")},
            {"a": {"source": "Cell Mol Life Sci", "volume": "71", "issue": "23",
                   "sortfirstauthor": "X", "lastauthor": "X"},
             "b": {"source": "Cell Mol Life Sci", "volume": "71", "issue": "23",
                   "sortfirstauthor": "X", "lastauthor": "Y"}},
        )
        kinds = {e.kind for e in tool.screen(["a", "b"], root=self.root, pause=0).edges}
        self.assertIn("SAME_CONTAINER", kinds)
        self.assertIn("SHARED_AUTHOR", kinds)

    def test_a_partial_container_is_not_a_container(self) -> None:
        self.stub(
            {"a": ([], ""), "b": ([], "")},
            {"a": {"source": "J", "volume": "1", "sortfirstauthor": "X"},
             "b": {"source": "J", "volume": "1", "sortfirstauthor": "Y"}},
        )
        kinds = {e.kind for e in tool.screen(["a", "b"], root=self.root, pause=0).edges}
        self.assertNotIn("SAME_CONTAINER", kinds)

    def test_an_unscreenable_member_is_named_not_treated_as_edgeless(self) -> None:
        self.stub({"a": ([], "HTTPError: 503"), "b": ([], "")}, {})
        result = tool.screen(["a", "b"], root=self.root, pause=0)
        self.assertIn("a", result.unscreenable)
        self.assertIn("503", result.unscreenable["a"])
        self.assertIn("UNSCREENABLE", tool.render(result))

    def test_a_reagent_word_near_a_member_pmid_is_a_candidate(self) -> None:
        (self.root / tool.DOSSIER_DIRS[0] / "PMID111.md").write_text(
            "Both antibodies come from PMID 222.", encoding="utf-8")
        edges = tool.local_reagent_edges(["111", "222"], self.root)
        self.assertEqual(1, len(edges))
        self.assertEqual("REAGENT_CANDIDATE", edges[0].kind)

    def test_a_bare_mention_is_not_a_reagent_edge(self) -> None:
        (self.root / tool.DOSSIER_DIRS[0] / "PMID111.md").write_text(
            "A survival curve discussed in 222 and nothing else. " * 20, encoding="utf-8")
        self.assertEqual([], tool.local_reagent_edges(["111", "222"], self.root))

    def test_one_edge_per_source_target_kind(self) -> None:
        (self.root / tool.DOSSIER_DIRS[0] / "PMID111.md").write_text(
            "antibodies from PMID 222", encoding="utf-8")
        (self.root / tool.DOSSIER_DIRS[1] / "PMID111.json").write_text(
            '{"n": "antibodies from PMID 222"}', encoding="utf-8")
        edges = tool.screen(["111", "222"], root=self.root, offline=True).edges
        self.assertEqual(1, len(edges))
        self.assertIn("more surface", edges[0].evidence)

    def test_the_contract_block_carries_what_was_screened(self) -> None:
        self.stub({"a": (["b"], ""), "b": ([], "")}, {})
        block = tool.as_contract_block(tool.screen(["a", "b"], root=self.root, pause=0))
        self.assertEqual(2, block["screened"]["lot_size"])
        self.assertEqual(1, len(block["internal_edges"]))
        self.assertIn("references_seen", block["screened"])

    def test_edges_do_not_turn_the_run_into_a_failure(self) -> None:
        (self.root / tool.DOSSIER_DIRS[0] / "PMID111.md").write_text(
            "antibodies from PMID 222", encoding="utf-8")
        self.assertEqual(0, tool.main(["--offline", "--root", str(self.root), "111", "222"]))

    def test_the_modules_own_self_test_passes(self) -> None:
        self.assertEqual(0, tool.self_test())


class TheRealDossiersAreScreened(unittest.TestCase):
    """Two real dossiers as a lot, offline, through ``main`` — read and screened, unchanged."""

    ROOT = Path(__file__).resolve().parents[2]

    def test_a_lot_of_two_real_papers_is_screened_offline(self) -> None:
        dossiers = sorted((self.ROOT / tool.DOSSIER_DIRS[0]).glob("PMID*.md"))
        if len(dossiers) < 2:
            self.skipTest(f"skipped: fewer than two dossiers under {tool.DOSSIER_DIRS[0]}")
        pair = dossiers[:2]
        before = [d.read_bytes() for d in pair]
        pmids = [d.stem.removeprefix("PMID") for d in pair]
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = tool.main(["--offline", "--root", str(self.ROOT), *pmids])
        out = buffer.getvalue()
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"^screened: lot=2 digest=[0-9a-f]{16} references_seen=\d+")
        self.assertTrue("no internal edges found" in out or " -> " in out, out)
        self.assertEqual([d.read_bytes() for d in pair], before, "the screen wrote a dossier")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = tool.main(["--offline", "--root", str(self.ROOT), "--json", *pmids])
        block = __import__("json").loads(buffer.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(block["screened"]["lot_size"], 2)
        self.assertIn("internal_edges", block)


if __name__ == "__main__":
    unittest.main(verbosity=2)
