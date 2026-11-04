#!/usr/bin/env python3
"""IT25 A1 regressions on the regenerated stage tables (results_s6) against the IT23 ones (results_s5).

  python3 test_stage_it25.py          (unittest; offline; seconds)

Pinned: the only proposals that leave are the four whose sign rests on a named, source-checked listing pair; the only rows whose z or eligibility moves belong to the
two families IT24 P1 touched; the hand-over loses exactly the sorafenib proposal and gains none; a phase is read from the sibling family only where the family's own is
blank, and says so; the engine effect is confined to the six families; the attribution annotation does not move eligibility or any blocker.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
OLD = DR / "generation_it23_p2_20261103" / "results_s5"
NEW = HERE / "results_s6"
SIX = {"FAM:CAT:DGIDB:0bc1cf72f3bb", "FAM:CAT:DGIDB:18c39af2d48d", "FAM:CAT:DGIDB:304d32aabb7a", "FAM:CAT:DGIDB:7cbc364139ee", "FAM:CAT:DGIDB:be0d8ea27925", "FAM:CAT:DGIDB:b34c953dc1fa"}


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def key(r):
    return (r["question"], r["seed_set"], r["hypothesis"], r["compound"])


class StageTables(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.A = {key(r): r for r in rd(OLD / "proposals_it21.tsv")}
        cls.B = {key(r): r for r in rd(NEW / "proposals_it21.tsv")}

    def test_only_proposals_resting_on_a_named_listing_pair_leave(self):
        gone = {k for k in self.A if k not in self.B}
        self.assertEqual({k[3] for k in gone}, {"Sorafenib", "Regorafenib", "Pictilisib", "Buparlisib"})
        self.assertFalse(set(self.B) - set(self.A))                         # nothing new appears
        excl = {r["family_id"] for r in rd(DR / "generation_it21_p2_20261103" / "source_exclusions_it24.tsv")}
        self.assertTrue({self.A[k]["family_id"] for k in gone} <= excl)

    def test_z_and_eligibility_move_only_for_the_two_families_of_the_it24_p1_check(self):
        moved = {k[3] for k in self.A if k in self.B and any(self.A[k][c] != self.B[k][c] for c in ("z_total", "z_reach", "handoff_eligible", "handoff_blocker"))}
        self.assertEqual(moved, {"Panobinostat", "Idronoxil"})
        for k in self.A:
            if k in self.B and k[3] not in moved:
                self.assertEqual((self.A[k]["handoff_eligible"], self.A[k]["handoff_blocker"]), (self.B[k]["handoff_eligible"], self.B[k]["handoff_blocker"]), k)

    def test_a_threshold_crossing_caused_by_removed_data_is_not_a_finding(self):
        """panobinostat z_reach 2.93 -> 3.16 and idronoxil 2.78 -> 3.38 cross the reach convention (3) because unsupported contrary signs were withheld; the table says so."""
        for k, b in self.B.items():
            if k[3] in ("Panobinostat", "Idronoxil"):
                self.assertGreaterEqual(float(b["z_reach"]), 3.0)
        pan = [b for k, b in self.B.items() if k[3] == "Panobinostat" and k[0] == "Q2"][0]
        self.assertEqual(pan["status"], "CONDITIONAL_H_HARM")
        self.assertEqual(pan["qualified"], "no")

    def test_the_handover_loses_exactly_sorafenib_and_gains_none(self):
        ha = {r["proposal_id"] for r in rd(OLD / "handoff_it21.tsv")}
        hb = {r["proposal_id"] for r in rd(NEW / "handoff_it21.tsv")}
        self.assertEqual(ha - hb, {"IT21P2-0035"})
        self.assertEqual(hb - ha, set())

    def test_a_phase_is_read_from_the_sibling_only_when_the_own_one_is_blank_and_says_so(self):
        for k, b in self.B.items():
            a = self.A.get(k)
            src = b["max_phase_source"]
            if src == "sibling_family":
                self.assertEqual(a["max_phase"], "", k)                    # the own phase was blank
                self.assertNotEqual(b["max_phase"], "", k)
                self.assertTrue(b["sibling_family"], k)
            elif src == "own":
                self.assertEqual(a["max_phase"], b["max_phase"], k)
            else:
                self.assertEqual(b["max_phase"], "", k)

    def test_the_attribution_annotation_moves_no_eligibility(self):
        for k, b in self.B.items():
            a = self.A[k]
            if k[3] not in ("Panobinostat", "Idronoxil"):
                self.assertEqual(a["handoff_eligible"], b["handoff_eligible"], k)


class EngineEffect(unittest.TestCase):
    def test_the_effect_is_confined_to_the_six_families(self):
        rows = rd(HERE / "engine_effect_it25.tsv")
        self.assertEqual({r["family_id"] for r in rows}, SIX)
        self.assertTrue(all(int(r["contribution_rows_removed"]) > 0 for r in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
