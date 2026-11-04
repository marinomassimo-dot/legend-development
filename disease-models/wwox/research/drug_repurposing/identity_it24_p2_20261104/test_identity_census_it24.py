#!/usr/bin/env python3
"""IT24 P2 regressions on the committed routes table: a structure known for a record is not a merge, related forms stay apart, unknown stays unknown.
Skipped unless the committed table is present (no network, no cache needed to READ it)."""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, unittest
from pathlib import Path
T = Path(__file__).resolve().parent / "q248" / "identity_routes.tsv"
ROWS = list(csv.DictReader(open(T, encoding="utf-8"), delimiter="\t")) if T.exists() else []


@unittest.skipUnless(ROWS, "routes table absent")
class Routes(unittest.TestCase):
    def test_every_row_has_exactly_one_route_and_unresolved_has_no_structure(self):
        for r in ROWS:
            self.assertTrue(r["route"])
            if r["route"] == "none_unresolved":
                self.assertEqual(r["inchikey"], "")
            else:
                self.assertTrue(r["inchikey"])

    def test_related_forms_are_never_reported_as_a_merge(self):
        for r in ROWS:
            if r["route"] == "R1_merged_bridge":
                self.assertTrue(r["via"].startswith("claim-name ligand -> FAM:CAT:CHEMBL"))
        by = {r["compound"].lower(): r for r in ROWS}
        for name in ("valemetostat", "tulmimetostat"):
            if name in by:      # stereoisomers or isotopologues differ in the reconciliation: structure known, not the ChEMBL family
                self.assertEqual(by[name]["route"], "R2_structure_known_not_merged")

    def test_the_route_counts_add_up_to_the_stage_table(self):
        self.assertEqual(len(ROWS), 158)
        self.assertEqual(sum(r["route"].startswith("R") for r in ROWS) + sum(r["route"] == "none_unresolved" for r in ROWS), 158)


if __name__ == "__main__":
    unittest.main()
