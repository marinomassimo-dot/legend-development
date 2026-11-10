#!/usr/bin/env python3
"""Tests for measurement.py. Fixtures are the DQP-1105 registry case (rows reconstructed from the registry's columns and the primary table's values as recorded in
the SCI42 S5 package) and real registry rows of the same class; nothing here is an interlocutor's data."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import measurement as m  # noqa: E402

COND = dict(species="Rat", system="oocyte TEVC", conditions="100 uM glutamate + 30 uM glycine, pH 7.4, 23 C")


def row(ligand, target, species, p_unit, p, kind, nm, rel="=", low="", high=""):
    return {"Ligand": ligand, "Target": target, "Target Species": species, "Affinity Units": p_unit, "Affinity Median": str(p), "Affinity Low": low, "Affinity High": high,
            "Original Affinity Units": kind, "Original Affinity Median nm": str(nm), "Original Affinity Low nm": "", "Original Affinity High nm": "", "Original Affinity Relation": rel}


class Conversion(unittest.TestCase):
    def test_p_form_and_concentration_units_convert_with_the_transformation_kept(self):
        a = m.measure("pIC50", 6.95)
        self.assertAlmostEqual(a["converted_nM"], 112.2, places=1)
        self.assertEqual(a["transform"], "nM = 10^(9 - p)")
        self.assertEqual(a["original"]["value"], 6.95)          # the original is kept next to the conversion
        b = m.measure("IC50", 113, "µM")
        self.assertEqual(b["converted_nM"], 113000)
        self.assertEqual(m.measure("IC50", 113, "μM")["converted_nM"], 113000)   # the two micro signs

    def test_missing_or_unknown_unit_is_a_flag_not_a_default(self):
        self.assertIn("UNIT_MISSING", m.measure("IC50", 113)["flags"])
        self.assertIsNone(m.measure("IC50", 113)["converted_nM"])
        self.assertIn("UNIT_UNRECOGNISED", m.measure("IC50", 113, "ug/ml")["flags"])
        self.assertIn("VALUE_MISSING", m.measure("IC50", None, "nM")["flags"])

    def test_censored_approximate_and_range_are_marked(self):
        self.assertIn("CENSORED", m.measure("IC50", 30, "uM", ">")["flags"])
        self.assertIn("APPROXIMATE", m.measure("Ki", 5, "nM", "~")["flags"])
        self.assertIn("RANGE", m.measure("IC50", 5, "nM", low=3, high=9)["flags"])


class Comparison(unittest.TestCase):
    def test_dqp1105_unit_slip_is_flagged_when_the_source_row_is_set_beside_the_registry_row(self):
        registry = m.measure("IC50", 113, "nM", target="GluN2B", **COND)
        source = m.measure("IC50", 113, "µM", target="GluN2B", **COND)
        c = m.compare(registry, source)
        self.assertTrue(c["unit_conflict_suspect"])
        self.assertAlmostEqual(c["ratio_b_over_a"], 1000)
        self.assertEqual(c["comparable"], "YES")                  # same quantity, target, species, system and conditions; it is the scale that disagrees

    def test_the_registry_row_alone_cannot_show_it(self):
        """The slipped DQP-1105 row has a pIC50 and a nanomolar column that agree with each other: the internal check must not claim to find it."""
        r = row("DQP-1105", "GluN2B", "Rat", "pIC50", 6.949999809265137, "IC50", 113.0)
        self.assertEqual(m.from_gtopdb(r)["internal"]["state"], "AGREE")

    def test_correct_conversion_is_not_a_conflict(self):
        registry = m.measure("IC50", 2700, "nM", target="GluN2D", **COND)
        source = m.measure("IC50", 2.7, "uM", target="GluN2D", **COND)
        c = m.compare(registry, source)
        self.assertFalse(c["unit_conflict_suspect"])
        self.assertEqual(c["comparable"], "YES")

    def test_a_converted_value_is_not_comparable_when_the_measure_is_not_equivalent(self):
        a = m.measure("IC50", 100, "nM", target="GluN2B", **COND)
        for other, why in ((m.measure("Ki", 100, "nM", target="GluN2B", **COND), "quantity"),
                           (m.measure("IC50", 100, "nM", target="GluN2C", **COND), "target"),
                           (m.measure("IC50", 100, "nM", target="GluN2B", species="Rat", system="HEK293 patch", conditions=COND["conditions"]), "system")):
            c = m.compare(a, other)
            self.assertEqual(c["comparable"], "NO", why)
            self.assertTrue(any(why in r for r in c["not_equivalent"]))

    def test_unstated_conditions_give_unknown_not_a_block_and_not_a_yes(self):
        a = m.measure("IC50", 100, "nM", target="GluN2B", species="Rat")
        b = m.measure("IC50", 120, "nM", target="GluN2B", species="Rat", system="oocyte")
        c = m.compare(a, b)
        self.assertEqual(c["comparable"], "UNKNOWN")
        self.assertIn("system", c["unstated"])
        self.assertIsNotNone(c["ratio_b_over_a"])                  # the numbers are still shown

    def test_missing_unit_and_censoring_stay_unknown(self):
        plain = m.measure("IC50", 100, "nM", target="T", **COND)
        self.assertEqual(m.compare(plain, m.measure("IC50", 100, None, target="T", **COND))["comparable"], "UNKNOWN")
        cens = m.compare(plain, m.measure("IC50", 30, "uM", ">", target="T", **COND))
        self.assertEqual(cens["comparable"], "UNKNOWN")
        self.assertFalse(cens["unit_conflict_suspect"])            # a bound is never read as a slip


class RegistryRows(unittest.TestCase):
    def test_cs_hcn_row_is_a_unit_conflict_suspect_and_a_consistent_row_agrees(self):
        slip = row("Cs+", "HCN1", "Human", "pIC50", 3.700000047683716, "IC50", 201.0)
        ok = row("[3H]NLX-112", "5-HT1A", "Human", "pKd", 8.9, "Kd", 1.4)   # rounding of the p-value only
        self.assertEqual(m.from_gtopdb(slip)["internal"]["state"], "UNIT_CONFLICT_SUSPECT")
        self.assertEqual(m.from_gtopdb(ok)["internal"]["state"], "AGREE")
        self.assertEqual(m.from_gtopdb(row("x", "t", "Human", "pIC50", 7, "IC50", 100.0))["internal"]["state"], "AGREE")

    def test_a_row_without_a_nanomolar_column_is_not_checkable(self):
        r = row("x", "t", "Human", "pIC50", 7, "IC50", "")
        self.assertEqual(m.from_gtopdb(r)["internal"]["state"], "NOT_CHECKABLE")

    def test_scan_reads_a_file_that_opens_with_a_quoted_comment_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "interactions.csv"
            fields = list(row("a", "b", "c", "d", 1, "IC50", 1))
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write('"# GtoPdb Version: test"\n')
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerow(row("Cs+", "HCN1", "Human", "pIC50", 3.7, "IC50", 201.0))
                w.writerow(row("fine", "T", "Human", "pIC50", 7, "IC50", 100.0))
            got = [r["Ligand"] for r, _ in m.scan_gtopdb(p)]
            self.assertEqual(got, ["Cs+"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
