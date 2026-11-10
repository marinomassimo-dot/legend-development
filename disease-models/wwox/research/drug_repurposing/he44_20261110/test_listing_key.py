#!/usr/bin/env python3
"""HE44 H3: the DGIdb listing groups names with the shared normalizer: salts merge, stereoisomers do not, and the summary says its overlap is an estimate."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
sys.path.insert(0, str(DR / "generation_it43_20261110"))
import dgidb_listing as L  # noqa: E402


class Key(unittest.TestCase):
    def test_a_salt_merges_into_its_parent_and_a_stereoisomer_stays_apart(self):
        self.assertEqual(L.key("Clorazepate Dipotassium"), L.key("Clorazepate"))
        self.assertEqual(L.key("ESKETAMINE HYDROCHLORIDE"), L.key("Esketamine"))
        self.assertNotEqual(L.key("(R)-Ef-1520"), L.key("(S)-Ef-1520"))
        self.assertNotEqual(L.key("(Rs)-(Tetrazol-5-Yl)Glycine"), L.key("Glycine"))

    def test_the_summary_states_that_overlap_is_a_name_estimate(self):
        with open(DR / "generation_it43_20261110/dgidb_summary_it43.tsv", encoding="utf-8", newline="") as f:
            self.assertEqual({r["overlap_basis"] for r in csv.DictReader(f, delimiter="\t")}, {"name_key_estimate_not_identity"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
