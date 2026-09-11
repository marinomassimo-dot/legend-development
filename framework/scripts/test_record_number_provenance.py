#!/usr/bin/env python3
"""Regressions for `record_number_provenance.py` — a number in a record table sits beside its
producer, or it is listed. The module's self-test is one of the cases."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import record_number_provenance as tool

HEADER = "| a | b |\n|---|---|\n"


class NumberProvenance(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.dir = self.root / "disease-models" / "x" / "analysis" / "orchestration_reviews"
        self.dir.mkdir(parents=True)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def write(self, rows: str) -> None:
        (self.dir / "r.md").write_text(HEADER + rows, encoding="utf-8")

    def test_an_empty_tree_is_void_not_clean(self) -> None:
        empty = self.root / "nothing"; empty.mkdir()
        self.assertEqual("INSUFFICIENT_DATA", tool.screen(empty).verdict)
        self.assertEqual(3, tool.main(["--root", str(empty)]))

    def test_a_ratio_beside_a_tool_is_anchored(self) -> None:
        self.write("| x | 17/1458 by `locator_contradiction_audit.py` |\n")
        r = tool.screen(self.root)
        self.assertEqual(1, r.numbered); self.assertEqual([], r.unanchored)

    def test_an_arrow_beside_a_commit_hash_is_anchored(self) -> None:
        self.write("| x | 13 → 10 at `2a26a25` |\n")
        self.assertEqual([], tool.screen(self.root).unanchored)

    def test_a_struck_value_is_anchored_by_its_correction(self) -> None:
        self.write("| x | ~~26/46~~ quoted from a report |\n")
        self.assertEqual([], tool.screen(self.root).unanchored)

    def test_a_bare_number_is_listed(self) -> None:
        self.write("| x | 26/46 called; 13 → 10 |\n")
        r = tool.screen(self.root)
        self.assertEqual(1, len(r.unanchored)); self.assertEqual(3, r.unanchored[0].line)

    def test_prose_outside_a_table_is_not_screened(self) -> None:
        self.write("a bare 3/4 in prose\n")
        self.assertEqual(0, tool.screen(self.root).numbered)

    def test_findings_never_fail_the_run(self) -> None:
        self.write("| x | 26/46 |\n")
        self.assertEqual(0, tool.main(["--root", str(self.root), "--queue"]))

    def test_the_modules_own_self_test_passes(self) -> None:
        self.assertEqual(0, tool.self_test())


if __name__ == "__main__":
    unittest.main(verbosity=2)
