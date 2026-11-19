#!/usr/bin/env python3
"""Tests for parametric_sensitivity.py and its adapter: scan sizes, the multiplier-scale ties, the published S-KO example, the report on a toy run directory (no simulation is run)."""
from __future__ import annotations

import csv
import math
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parametric_sensitivity as ps  # noqa: E402
import pilot_bisect_harness_model as frozen  # noqa: E402

INF = math.inf
# the published S-KO crossings: (estimate, bracket_lo, bracket_hi) per arm
PUBLISHED = {1: (0.1640625, 0.140625, 0.1875), 2: (0.9140625, 0.890625, 0.9375), 4: (1.4296875, 1.40625, 1.453125), 5: (INF, 0.0, 3.0),
             6: (1.7109375, 1.6875, 1.734375), 7: (0.5390625, 0.515625, 0.5625), 8: (1.1015625, 1.078125, 1.125)}


class Scan(unittest.TestCase):
    def test_cell_counts_and_the_fixed_block(self):
        self.assertEqual(len(ps.scan("baseline")["bisect"]["cells"]), 7)
        self.assertEqual(len(ps.scan("rest")["bisect"]["cells"]), 77)
        self.assertEqual(len(ps.scan("full")["bisect"]["cells"]), 84)
        cell = ps.scan("full")["bisect"]["cells"][-1]
        self.assertEqual(cell["fixed"]["geno"], 0)
        self.assertIn("variant joint_inhibited", cell["note"])

    def test_the_arm_table_matches_the_frozen_adapter(self):
        for arm, params in ps.ARM.items():
            self.assertEqual(params, frozen.ARM[arm])


class MultiplierScale(unittest.TestCase):
    def test_same_parameter_classes_tie_when_their_brackets_overlap(self):
        r = ps.mult_ranks(PUBLISHED)
        self.assertEqual(r[1], r[2])                          # d-APV and the pore blocker: both J_N, about -18%: the published order between them is imposed by 0.3 against 0.8
        self.assertEqual(ps.ranks({a: x[0] for a, x in PUBLISHED.items()})[1], 1.0)   # in s, d-APV is first on its own coefficient

    def test_published_order_on_the_multiplier_scale(self):
        r = ps.mult_ranks(PUBLISHED)
        self.assertEqual([a for a in sorted(r, key=r.get)], [7, 8, 1, 2, 6, 4, 5])      # neurosteroid composite, sodium, the J_N pair tied, GABA-A, AMPA, T-type last
        self.assertEqual(r[5], 7.0)

    def test_tau_and_ranks(self):
        self.assertEqual(ps.ranks({1: 0.5, 2: 0.5, 3: 2.0}), {1: 1.5, 2: 1.5, 3: 3.0})
        a = {1: 1.0, 2: 2.0, 3: 3.0}
        self.assertAlmostEqual(ps.tau(a, a), 1.0)
        self.assertAlmostEqual(ps.tau(a, {1: 3.0, 2: 2.0, 3: 1.0}), -1.0)


def write_run(root: Path, per_variant: dict[str, dict[int, tuple[float, float, float]]]) -> Path:
    with open(root / "summary.tsv", "w", newline="") as fh, open(root / "results.tsv", "w", newline="") as rh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["point", "status", "bracket_lo", "bracket_hi", "estimate"])
        r = csv.writer(rh, delimiter="\t", lineterminator="\n"); r.writerow(["point", "evaluation", "n_bursts_baseline"])
        for v, e in per_variant.items():
            for a, (s, lo, hi) in e.items():
                w.writerow([f"{v}__arm{a}", "not_in_bracket" if math.isinf(s) else "crossed", lo, hi, s])
                r.writerow([f"{v}__arm{a}", 0, 800])
    return root


class Report(unittest.TestCase):
    def test_report_on_a_toy_run_keeps_the_labels_and_flags_a_winner_change(self):
        flipped = dict(PUBLISHED); flipped[8] = (0.05, 0.04, 0.06)                       # sodium becomes the most sensitive class in one variant
        with tempfile.TemporaryDirectory() as tmp:
            text = ps.report(write_run(Path(tmp), {"base": PUBLISHED, "ji_mult_hi": PUBLISHED, "joint_inhibited": flipped}))
        self.assertIn("Kv7 is NOT in the model", text)
        self.assertIn("MULTIPLIER scale (primary)", text)
        self.assertIn("partly imposed by the listed coefficients", text)
        self.assertIn("joint_inhibited", text)                                            # the variant that changes the winner is named
        self.assertIn("d-APV-type against NMDAR pore", text)                              # an order in s that the multiplier scale ties
        self.assertNotIn("PASS", text)
        self.assertNotIn("is superior", text.lower())
        self.assertIn("beyond x0.42", text)                                                # a class outside the bracket is shown as a bound, not as a multiplier of 0

    def test_an_incomplete_baseline_is_refused_not_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = ps.report(write_run(Path(tmp), {"ji_mult_hi": PUBLISHED}))
        self.assertIn("nothing to compare", text)

    def test_a_baseline_only_run_reports_the_baseline_order_without_comparing(self):
        with tempfile.TemporaryDirectory() as tmp:
            text = ps.report(write_run(Path(tmp), {"base": PUBLISHED}))
        self.assertIn("baseline only, order: neurosteroid-type (1) < sodium (pyramidal) (2) < d-APV-type (3.5)", text)

    def test_help_is_safe(self):
        self.assertEqual(ps.main(["--help"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
