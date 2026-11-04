import csv, json, sys, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import stage_diff_it26 as m


def rd(p):
    return m.rd(p)


class T(unittest.TestCase):
    def test_counts(self):
        s = json.load(open(HERE / "stage_diff_summary.json"))
        self.assertEqual((s["proposals_s6"], s["proposals_s7"]), (996, 994))
        self.assertEqual((s["handoff_s6"], s["handoff_s7"]), (15, 15))
        self.assertEqual((s["eligible_s6"], s["eligible_s7"]), (215, 220))

    def test_removed_and_added(self):
        s = json.load(open(HERE / "stage_diff_summary.json"))
        self.assertEqual(sorted(s["removed"]), ["Fexagratinib AKT1", "Fexagratinib AKT2", "Rabeprazole FGFR3"])
        self.assertEqual(s["added"], ["Fexagratinib FGFR3"])

    def test_no_proposal_from_an_excluded_pair(self):
        ex = {(r["family_id"], r["gene"].upper()) for r in rd(HERE.parent / "generation_it21_p2_20261103" / "source_exclusions_it24.tsv")}
        for r in rd(HERE / "results_s7" / "proposals_it21.tsv"):
            self.assertNotIn((r["family_id"], r["main_target"].upper()), ex)

    def test_r4_identity_only_where_declared(self):
        r4 = {r["family_id"] for r in rd(HERE.parent / "identity_gsrs_it26_a1_20261104" / "identity_r4_it26.tsv")}
        for r in rd(HERE / "results_s7" / "proposals_it21.tsv"):
            if r["identity_via"].startswith("gsrs_unii_structure"):
                self.assertIn(r["family_id"], r4)

    def test_handoff_unchanged_by_r4(self):
        a = {r["proposal_id"] for r in rd(HERE.parent / "generation_it25_a1_20261104" / "results_s6" / "handoff_it21.tsv")}
        b = {r["proposal_id"] for r in rd(HERE / "results_s7" / "handoff_it21.tsv")}
        self.assertEqual(a, b)

    def test_stage_diff_reproduces(self):
        rows = m.compare(rd(m.OLD / "proposals_it21.tsv"), rd(m.NEW / "proposals_it21.tsv"))
        self.assertEqual(len(rows), len(rd(HERE / "stage_diff.tsv")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
