#!/usr/bin/env python3
"""Benchmark I machinery: the pieces a label or a seed depends on, pinned on toy input.

The fixtures themselves are real history; these tests only pin the rules that turn history
into fixtures (target labeling, seed scrubbing, term extraction), so a later edit to one of them
shows up here before it silently moves a frozen result. The history-bound checks skip on a
shallow clone, where the event commits are not present.

Run: `python3 framework/scripts/test_claim_retrieval_bench.py`
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import claim_retrieval_bench as bench  # noqa: E402

ROOT = HERE.parents[1]


def has_commit(rev: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{rev}^{{commit}}"], cwd=ROOT,
                          capture_output=True).returncode == 0


class Rules(unittest.TestCase):
    def test_scrub_removes_and_counts_claim_ids_and_wikilinks(self) -> None:
        text, count = bench.scrub("see CLAIM 005 and [[claim_registry_current#CLAIM 019]] here")
        self.assertEqual(count, 2)
        self.assertNotIn("CLAIM", text)
        self.assertNotIn("[[", text)

    def test_terms_are_literal_lowercased_and_length_gated(self) -> None:
        terms = bench.terms_of("Wwox-null mice; HIF1α at P18, the Q230P allele; ok ab c.1057")
        self.assertIn("wwox-null", terms)
        self.assertIn("hif1α", terms)
        self.assertIn("p18", terms)          # three characters, one digit: kept
        self.assertIn("q230p", terms)
        self.assertNotIn("ok", terms)
        self.assertNotIn("the", terms)       # three letters, no digit: dropped
        self.assertEqual(len(terms), len(set(terms)))

    def test_claim_records_split_at_every_level_two_heading(self) -> None:
        text = "# T\n## CLAIM 001\na\n## Rules\nb\n## CLAIM 002\nc\n"
        records = bench.claim_records(text)
        self.assertEqual(sorted(records), ["CLAIM 001", "CLAIM 002"])
        self.assertNotIn("Rules", records["CLAIM 001"].split("\n", 1)[1])

    def test_diff_lines_separate_added_from_removed(self) -> None:
        added, removed = bench.diff_lines("a\nb\n", "a\nc\nd\n")
        self.assertEqual(added.splitlines(), ["c", "d"])
        self.assertEqual(removed.splitlines(), ["b"])

    def test_summary_counts_only_its_class(self) -> None:
        row = lambda klass, hit: {"class": klass, "targets": ["CLAIM 001"], "strategies": {
            name: {"targets_retrieved": ["CLAIM 001"] if hit else [], "all_targets_retrieved": hit,
                   "candidate_count": 3, "registry_fraction": 0.1}
            for name in ("CURRENT", "PROGRESSIVE")}}
        summary = bench.summarise([row("STRONG", True), row("STRONG", False),
                                   row("USABLE_WITH_LIMITATION", True)])
        self.assertEqual(summary["STRONG"]["fixtures"], 2)
        self.assertEqual(summary["STRONG"]["PROGRESSIVE"]["targets_retrieved"], 1)
        self.assertEqual(summary["USABLE_WITH_LIMITATION"]["fixtures"], 1)


@unittest.skipUnless(has_commit("2a35aec"), "shallow clone: the event history is not present")
class History(unittest.TestCase):
    def test_labeling_rule_reproduces_a_multi_target_event(self) -> None:
        label = bench.label_targets("2a35aec", "33916893")
        self.assertEqual(label["targets"], ["CLAIM 017", "CLAIM 019", "CLAIM 030", "CLAIM 033"])

    def test_a_rewritten_wikilink_line_is_not_a_reference(self) -> None:
        # PAPER 039 sits on CLAIM 030's rewritten Wikilinks line on both sides of the diff.
        self.assertEqual(bench.label_targets("2a35aec", "34268881")["targets"], [])

    def test_build_is_reproducible_from_the_spec(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "fixtures.json"
            self.assertEqual(bench.main(["build", "--out", str(out)]), 0)
            built = json.loads(out.read_text(encoding="utf-8"))
            frozen = json.loads(bench.FIXTURES.read_text(encoding="utf-8"))
            self.assertEqual(built["fixtures"], frozen["fixtures"])


class Cli(unittest.TestCase):
    def test_invalid_action_is_exit_two(self) -> None:
        done = subprocess.run([sys.executable, str(HERE / "claim_retrieval_bench.py"), "nope"],
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
