"""ADV-066 (IT57): the generator reads the registered comparison packages of INV-04 and INV-09 (hypotheses_only rows through PKG_MAP; comparison rows through comparison_rows()).
What is pinned: the rows are reachable and mapped, nothing already produced changes, nothing is ranked or recommended, withdrawn statements stay labelled withdrawn, no dose or schedule enters, and a missing cell
is written as missing. INVS governs only the physiological packages: adding the two investigations to it changes no output."""
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
import hypothesis_package as hp  # noqa: E402

DOSE = re.compile(r"\b\d+(\.\d+)?\s*(mg|mcg|ug|g)\s*/\s*(kg|day|d)\b|\bmg/kg\b|\bq\d+h\b|\bonce daily\b|\btwice daily\b", re.I)


class RegisteredComparisonIsRead(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pkg_rows, cls.unmapped = cp.package_rows()
        cls.cmp_rows, cls.dec_rows = cp.comparison_rows()

    def test_the_two_packages_are_mapped(self):
        self.assertNotIn(("INV-04", "inv04_ethosuximide_age_assay"), self.unmapped)
        self.assertNotIn(("INV-09", "inv09_lithium_gsk3_regimen"), self.unmapped)
        self.assertEqual(sum(1 for r in self.pkg_rows if r["inv_id"] == "INV-04"), 4)
        self.assertEqual(sum(1 for r in self.pkg_rows if r["inv_id"] == "INV-09"), 9)   # the five rows of the IT47 package are kept; four are new

    def test_the_comparison_rows_are_read_with_their_measurements_and_decisive_rows(self):
        by = {r["comparison_id"]: r for r in self.cmp_rows}
        self.assertEqual(sum(1 for r in self.cmp_rows if r["inv_id"] == "INV-04"), 7)
        self.assertEqual(sum(1 for r in self.cmp_rows if r["inv_id"] == "INV-09"), 3)
        c = by["inv04_ethosuximide_age_assay::C-EP2"]
        self.assertIn("M-1", c["new_measurements_blocking_this_row"])
        self.assertIn("D01", c["decisive_propositions_cited"])
        self.assertTrue(all(r["state"] == "COMPARISON_PRESENT" for r in self.cmp_rows))
        self.assertEqual(sum(1 for r in self.dec_rows if r["inv_id"] == "INV-04"), 12)
        self.assertEqual(sum(1 for r in self.dec_rows if r["inv_id"] == "INV-09"), 9)

    def test_nothing_is_nominated_or_ranked(self):
        for r in self.cmp_rows:
            self.assertTrue(r["nomination"].startswith("NO NOMINATION"), r["comparison_id"])
        for r in self.pkg_rows:
            if r["inv_id"] in ("INV-04", "INV-09") and "adv066" not in r["package_ref"] and "inv04_" not in r["package_ref"] and "inv09_" not in r["package_ref"]:
                continue
            self.assertIn("no therapeutic direction", r["direction_stated"], r["proposal_id"])

    def test_withdrawn_statements_stay_withdrawn(self):
        w = [r for r in self.dec_rows if str(r["status"]).lower().startswith("withdrawn")]
        self.assertEqual(sorted(r["prop_id"] for r in w), ["inv04_ethosuximide_age_assay::D10", "inv09_lithium_gsk3_regimen::D09"])
        for r in w:
            self.assertIn("WITHDRAWN", r["statement"])
            self.assertEqual(r["direction"], "not_applicable")
        for r in self.cmp_rows:
            self.assertIn("D10", r["withdrawn_statements_of_the_package"]) if r["inv_id"] == "INV-04" else None

    def test_no_dose_or_schedule_enters(self):
        for r in self.cmp_rows + self.dec_rows:
            for v in r.values():
                self.assertIsNone(DOSE.search(str(v)), (r.get("comparison_id") or r.get("prop_id"), str(v)[:80]))
        for r in self.pkg_rows:
            if r["inv_id"] in ("INV-04", "INV-09"):
                for v in r.values():
                    self.assertIsNone(DOSE.search(str(v)), (r["proposal_id"], str(v)[:80]))

    def test_the_rows_already_produced_do_not_change(self):
        ids = [r["proposal_id"] for r in self.pkg_rows]
        for pid in ("CP-gsk3_eif2b_20261107::",):
            self.assertTrue(any(i.startswith(pid) for i in ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_the_new_rows_are_appended_and_carry_their_own_provenance(self):
        # the 34 rows produced before keep their position (test_stage_it49 / test_stage_it50 pin them); the eight new rows come last and do not borrow the earlier mapping's provenance
        ids = [r["proposal_id"] for r in self.pkg_rows]
        new = ids[-8:]
        self.assertTrue(all(("inv04_ethosuximide_age_assay" in i or "inv09_lithium_gsk3_regimen" in i) for i in new), new)
        self.assertFalse(any(("inv04_ethosuximide_age_assay" in i or "inv09_lithium_gsk3_regimen" in i) for i in ids[:-8]))
        for r in self.pkg_rows[-8:]:
            self.assertIn("mapping drafted by IT with the rows (ADV-066, 2026-11-18)", r["nomination"])
            self.assertNotIn("PRESIDIO-001", r["nomination"])
        for r in self.pkg_rows[:-8]:
            self.assertNotIn("ADV-066", r["nomination"])

    def test_adding_the_investigations_to_invs_changes_nothing(self):
        # INVS drives the physiological hypothesis packages only (record_for): these two investigations have none, so the list adds no row
        pk = hp.load_all()
        for inv in ("INV-04", "INV-09"):
            self.assertEqual(hp.record_for(pk, inv)["hypotheses"], [])

    def test_a_missing_cell_is_written_as_missing(self):
        real = hp.comparison_for

        def stripped(pkgs, inv):
            rec = real(pkgs, inv)
            for r in rec["rows"]:
                r["row"] = {k: v for k, v in r["row"].items() if k != "mechanism_discriminating_control"}
            return rec
        hp.comparison_for = stripped
        try:
            rows, _ = cp.comparison_rows()
        finally:
            hp.comparison_for = real
        self.assertTrue(all(r["controls_and_discriminating_control"] == "not stated by the package" for r in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
