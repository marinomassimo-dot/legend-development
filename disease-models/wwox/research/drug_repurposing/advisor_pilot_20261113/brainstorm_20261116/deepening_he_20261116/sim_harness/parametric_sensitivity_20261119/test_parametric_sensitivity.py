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


def write_run(root: Path, per_variant: dict[str, dict[int, tuple[float, float, float]]], seeds_below: bool = True) -> Path:
    with open(root / "summary.tsv", "w", newline="") as fh, open(root / "results.tsv", "w", newline="") as rh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["point", "status", "bracket_lo", "bracket_hi", "estimate"])
        r = csv.writer(rh, delimiter="\t", lineterminator="\n"); r.writerow(["point", "evaluation", "strength", "seed", "rel_bursts", "n_bursts_baseline"])
        for v, e in per_variant.items():
            for a, (s, lo, hi) in e.items():
                w.writerow([f"{v}__arm{a}", "not_in_bracket" if math.isinf(s) else "crossed", lo, hi, s])
                for seed in (1000, 1001, 1002):
                    r.writerow([f"{v}__arm{a}", 0, 3.0, seed, 0.1, 800]); r.writerow([f"{v}__arm{a}", 5, hi, seed, 0.3 if seeds_below else 0.7, 800])
                    r.writerow([f"{v}__arm{a}", 5, lo, seed, 0.8, 800])
    return root


class Report(unittest.TestCase):
    def run_text(self, per_variant, **kw) -> str:
        with tempfile.TemporaryDirectory() as tmp:
            return ps.report([write_run(Path(tmp), per_variant, **kw)])

    def test_the_labels_and_limits_are_always_printed(self):
        text = self.run_text({"base": PUBLISHED})
        for needle in ("Kv7 is NOT in the model", "not a confidence interval", "not a validation on alternative biological structures", "No ranks, no rank correlation, no winner",
                       "Not identifiable here", "an explored-range result, not an impossibility of effect", "numerical resolution"):
            self.assertIn(needle, text)

    def test_nothing_is_ranked_and_no_correlation_or_winner_is_computed(self):
        text = self.run_text({"base": PUBLISHED, "ji_mult_hi": PUBLISHED})
        for banned in ("tau ", "Kendall", "winner (rank", "superior to", "PASS", "FAIL"):
            self.assertNotIn(banned, text)

    def test_the_same_parameter_pair_is_indistinguishable_on_the_multiplier_scale(self):
        self.assertIn("same-parameter pair (J_N): d-APV-type", self.run_text({"base": PUBLISHED}))
        self.assertIn("indistinguishable on the multiplier scale", self.run_text({"base": PUBLISHED}))

    def test_a_shift_beyond_the_bracket_is_named_and_an_overlap_is_not(self):
        moved = dict(PUBLISHED); moved[8] = (2.0, 1.95, 2.05); same = dict(PUBLISHED)
        text = self.run_text({"base": PUBLISHED, "nmda_mult_hi": moved, "ji_mult_lo": same})
        self.assertIn("sodium (pyramidal): s 2.000", text)
        self.assertIn("needs a larger parameter change", text)
        self.assertIn("indistinguishable at this resolution", text)

    def test_the_baseline_burst_count_of_each_variant_is_printed_as_a_multiple(self):
        text = self.run_text({"base": PUBLISHED, "ji_mult_hi": PUBLISHED})
        self.assertIn("Baseline burst count of each variant", text)
        self.assertIn("ji_mult_hi 1.00x", text)

    def test_missing_cells_are_listed_not_guessed(self):
        partial = {a: x for a, x in PUBLISHED.items() if a != 5}
        text = self.run_text({"base": PUBLISHED, "kv7_offset_hi": partial})
        self.assertIn("missing: kv7_offset_hi__arm5", text)

    def test_seed_agreement_is_shown_separately_from_the_bracket(self):
        self.assertIn("seeds below 0.5 at the crossed end 0/3", self.run_text({"base": PUBLISHED}, seeds_below=False))

    def test_help_is_safe(self):
        self.assertEqual(ps.main(["--help"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
