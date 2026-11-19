#!/usr/bin/env python3
"""Tests for hindcast_separation.py on toy sets whose AUC and exact p are known (6 against 6: 924 arrangements; SCI's table in the scorer sheet, section 8)."""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hindcast_separation as hs  # noqa: E402


def run(scores: list[list], labels: list[str], ident: list[str] | None = None) -> tuple[int, str, str]:
    """Write the toy files, run main, return (exit, stdout, stderr). scores: one row per pair [c1, c2, c3, c4]."""
    with tempfile.TemporaryDirectory() as tmp:
        s, lab = Path(tmp) / "scores.tsv", Path(tmp) / "labels.tsv"
        s.write_text("id\tc1\tc2\tc3\tc4\n" + "".join(f"P{i}\t" + "\t".join(map(str, row)) + "\n" for i, row in enumerate(scores)))
        lab.write_text("id\tlabel\n" + "".join(f"P{i}\t{x}\n" for i, x in enumerate(labels)))
        args = [str(s), str(lab)]
        if ident is not None:
            idf = Path(tmp) / "ident.tsv"
            idf.write_text("id\tanswer\n" + "".join(f"P{i}\t{x}\n" for i, x in enumerate(ident)))
            args += ["--identified", str(idf)]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = hs.main(args)
        return code, out.getvalue(), err.getvalue()


LAB = ["POS"] * 6 + ["NEG"] * 6


def one_component(pos: list[float], neg: list[float]) -> list[list]:
    """C1 carries the toy values (scaled to 0..2 by the caller); C2..C4 are constant."""
    return [[v, 1, 1, 1] for v in pos + neg]


class Toy(unittest.TestCase):
    def test_perfect_separation_has_the_smallest_exact_p(self):
        code, out, _ = run(one_component([2] * 6, [0] * 6), LAB)
        line = next(l for l in out.splitlines() if l.startswith("C1:"))
        self.assertEqual(code, 0)
        self.assertIn("AUC 1.000", line)
        self.assertIn("p 0.0011", line)                       # 1 / 924

    def test_the_sheets_exact_probabilities_at_six_against_six(self):
        # NEG 1..6; five POS above all NEG; the lowest POS sits among the NEG and loses to some of them.
        neg = [1, 2, 3, 4, 5, 6]
        for lowest, auc_value, p in ((7, 1.0, 0.0011), (3.5, 33 / 36, 0.0076), (2.5, 32 / 36, 0.0130)):
            pos = [lowest, 8, 9, 10, 11, 12]
            a = hs.auc(pos, neg)
            self.assertAlmostEqual(a, auc_value, places=6)
            self.assertAlmostEqual(hs.exact_p(pos + neg, 6, a), p, places=4)      # SCI's table: 0.0011, 0.0076, 0.0130

    def test_no_signal_shows_no_separation_and_the_output_never_says_pass_or_fail(self):
        code, out, _ = run([[i % 3, 1, 1, 1] for i in range(12)], ["POS", "NEG"] * 6)
        self.assertEqual(code, 0)
        self.assertNotIn("separated", out.lower())
        self.assertNotIn("verdict", out.lower())
        self.assertIn("'No separation shown' is not 'does not separate'", out)

    def test_unknown_is_scored_zero_and_a_bad_value_is_refused(self):
        code, out, _ = run([["unknown", 1, 1, 1]] * 6 + [[0, 1, 1, 1]] * 6, LAB)
        self.assertEqual(code, 0)
        self.assertIn("AUC 0.500", next(l for l in out.splitlines() if l.startswith("C1:")))
        self.assertEqual(run([[3, 1, 1, 1]] * 12, LAB)[0], 2)

    def test_ids_and_labels_must_match_and_both_labels_are_needed(self):
        self.assertEqual(run([[1, 1, 1, 1]] * 12, ["POS"] * 12)[0], 2)
        self.assertEqual(run([[1, 1, 1, 1]] * 12, ["POS"] * 6 + ["MAYBE"] * 6)[0], 2)

    def test_at_least_half_identified_is_flagged_as_contamination(self):
        _, out, _ = run(one_component([2] * 6, [0] * 6), LAB, ["identified"] * 6 + ["not"] * 6)
        self.assertIn("AT LEAST HALF IDENTIFIED", out)
        _, out, _ = run(one_component([2] * 6, [0] * 6), LAB, ["identified"] * 5 + ["partly"] + ["not"] * 6)
        self.assertNotIn("AT LEAST HALF", out)

    def test_the_bootstrap_is_seeded_and_the_output_repeats(self):
        a = run(one_component([2, 2, 1, 2, 1, 2], [0, 1, 0, 1, 0, 0]), LAB)[1]
        self.assertEqual(a, run(one_component([2, 2, 1, 2, 1, 2], [0, 1, 0, 1, 0, 0]), LAB)[1])

    def test_help_is_safe(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(hs.main(["--help"]), 0)
        self.assertIn("never says pass or fail", out.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
