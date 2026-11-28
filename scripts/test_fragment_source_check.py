#!/usr/bin/env python3
"""Regression for framework/scripts/fragment_source_check.py: the three IT28 defect classes are flagged."""
import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "framework" / "scripts"))
import fragment_source_check as f


class T(unittest.TestCase):
    SRC = f.normalise("<p>The 28-year-old son and the 31-year-old daughter. A serine 12 amino acids upstream of YNRSK 293-297. "
                      "ETX had no effects in WT.</p>")

    def test_wrong_age_and_derived_residue_are_flagged(self):
        nums = f.source_numbers([self.SRC])
        u, _, _ = f.check("two carriers aged about 29 and 31 years; S281 is reported", nums)
        self.assertIn("29", u)
        self.assertIn("281", u)
        self.assertNotIn("31 years", u)

    def test_negative_and_absolute_words_are_listed(self):
        nums = f.source_numbers([self.SRC])
        u, a, n = f.check("no such effect is reported in wild-type mice; only one line", nums)
        self.assertIn("no such", n)
        self.assertIn("only", a)

    def test_cli_strict_exit(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "s.txt"
            p.write_text("aged 28 and 31", encoding="utf-8")
            self.assertEqual(f.main(["--fragment", "aged 29", "--source", str(p), "--strict"]), 1)
            self.assertEqual(f.main(["--fragment", "aged 28", "--source", str(p), "--strict"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
