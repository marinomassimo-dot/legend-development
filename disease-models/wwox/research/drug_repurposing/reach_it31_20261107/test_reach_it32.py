#!/usr/bin/env python3
"""Regression for reach_it32.has_id: an identifier is matched whole, never as a prefix of a longer one."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reach_it32 as r  # noqa: E402


class HasId(unittest.TestCase):
    def test_a_shorter_chembl_id_does_not_match_a_longer_one(self):
        self.assertFalse(r.has_id("FAM:CAT:CHEMBL4000123", "CAT:CHEMBL40"))
        self.assertFalse(r.has_id("FAM:CAT:CHEMBL980", "CAT:CHEMBL98"))

    def test_the_exact_id_matches_alone_or_in_a_list(self):
        self.assertTrue(r.has_id("FAM:CAT:CHEMBL98", "CAT:CHEMBL98"))
        self.assertTrue(r.has_id("FAM:CAT:CHEMBL98;CAT:DGIDB:316b73312895", "CAT:CHEMBL98"))
        self.assertTrue(r.has_id("FAM:CAT:DGIDB:316b73312895", "CAT:DGIDB:316b73312895"))


if __name__ == "__main__":
    unittest.main()
