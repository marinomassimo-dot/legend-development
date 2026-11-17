#!/usr/bin/env python3
"""Structure test for ENGINE_MEASURES.tsv (the engine's append-only measure table): fixed header, 12 columns on every row, unique ascending ids, ISO dates, numeric value, and
APPEND-ONLY against the committed copy (the lines already in HEAD must be an unchanged prefix of the working copy). A correction is a new row, never an edit."""
import csv, re, subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/ENGINE_MEASURES.tsv"
COLS = ["measure_id", "date_utc", "measure", "value", "unit", "numerator", "denominator", "scope", "definition", "source_locator", "counted_by", "limit"]


def rows():
    with open(ROOT / REL, newline="", encoding="utf-8") as h:
        return list(csv.reader(h, delimiter="\t"))


class EngineMeasures(unittest.TestCase):
    def test_header_and_width(self):
        r = rows()
        self.assertEqual(r[0], COLS)
        self.assertGreater(len(r), 1)
        bad = [x[0] for x in r[1:] if len(x) != len(COLS)]
        self.assertFalse(bad, f"rows with the wrong number of cells: {bad}")

    def test_ids_dates_and_numbers(self):
        r = rows()[1:]
        ids = [x[0] for x in r]
        self.assertEqual(len(ids), len(set(ids)), "duplicate measure_id")
        self.assertEqual(ids, sorted(ids), "ids must be ascending (append-only)")
        for x in r:
            self.assertRegex(x[0], r"^M\d{3,}$"); self.assertRegex(x[1], r"^\d{4}-\d\d-\d\d$")
            self.assertRegex(x[3], r"^-?\d+(\.\d+)?$", f"{x[0]}: value must be numeric")
            for k in (5, 6):
                self.assertTrue(x[k] == "" or re.fullmatch(r"-?\d+(\.\d+)?", x[k]), f"{x[0]}: numerator and denominator are numbers or empty")
            self.assertTrue(x[9].strip() and x[10].strip() and x[11].strip(), f"{x[0]}: source_locator, counted_by and limit are required")

    def test_append_only_against_head(self):
        r = subprocess.run(["git", "show", f"HEAD:{REL}"], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            self.skipTest("the table is not committed yet")
        old = r.stdout.splitlines(); new = (ROOT / REL).read_text(encoding="utf-8").splitlines()
        self.assertEqual(new[:len(old)], old, "committed lines were changed or removed: append a correcting row instead")


if __name__ == "__main__":
    unittest.main(verbosity=2)
