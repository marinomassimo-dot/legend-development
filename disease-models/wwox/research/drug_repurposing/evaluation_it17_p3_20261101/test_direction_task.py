import unittest

import direction_task as d


def E(classes, pm=()):
    return {"classes": set(classes), "raw": set(), "pmids": set(pm)}


class T(unittest.TestCase):
    def test_labels(self):
        self.assertEqual(d.chembl_class("INHIBITOR"), d.DEC)
        self.assertEqual(d.chembl_class("AGONIST"), d.INC)
        self.assertIsNone(d.chembl_class("PARTIAL AGONIST"))
        self.assertIsNone(d.chembl_class("BINDING AGENT"))
        self.assertIsNone(d.chembl_class(None))
        self.assertEqual(d.gtopdb_class("Inhibitor", "Inhibition"), d.DEC)
        self.assertEqual(d.gtopdb_class("Agonist", "Inverse agonist"), d.DEC)
        self.assertEqual(d.gtopdb_class("Inhibitor", "Competitive"), d.DEC)
        self.assertIsNone(d.gtopdb_class("Agonist", "Partial agonist"))
        self.assertIsNone(d.gtopdb_class("Inhibitor", "Binding"))

    def test_split_is_deterministic_and_by_compound(self):
        self.assertEqual(d.split_of("CHEMBL25"), d.split_of("CHEMBL25"))
        self.assertEqual({d.split_of(c) for c in ("CHEMBL%d" % i for i in range(200))}, {"dev", "eval"})

    def test_unresolved_is_not_error_and_conflict_is_retained(self):
        pairs = [
            {"key": ("C1", "P1"), "split": "eval", "gt": None, "m": E([d.DEC])},
            {"key": ("C2", "P1"), "split": "eval", "gt": E([None]), "m": E([d.DEC])},
            {"key": ("C3", "P1"), "split": "eval", "gt": E([d.INC, d.DEC]), "m": E([d.DEC])},
            {"key": ("C4", "P1"), "split": "eval", "gt": E([d.DEC]), "m": E([None])},
            {"key": ("C5", "P1"), "split": "eval", "gt": E([d.DEC, None], ["1"]), "m": E([d.DEC], ["1"])},
            {"key": ("C6", "P2"), "split": "eval", "gt": E([d.INC]), "m": E([d.DEC])},
        ]
        det, un = d.classify(pairs)
        self.assertEqual([p["key"][0] for p in det], ["C5", "C6"])
        self.assertEqual(un, {"no_gtopdb_counterpart": 1, "module_no_direction": 1, "module_conflict": 0,
                              "gtopdb_no_direction": 1, "gtopdb_conflict": 1})
        self.assertTrue(det[0]["shared_ref"])
        self.assertFalse(det[1]["shared_ref"])

    def test_discordant_pair_counts_as_wrong_not_dropped(self):
        pairs = [{"key": ("C%d" % i, "P1"), "gt": E([d.DEC]), "m": E([d.DEC if i else d.INC]), "split": "eval"} for i in range(4)]
        det, _ = d.classify(pairs)
        s = d.score(det, det)
        self.assertEqual((s["n_determinate"], s["module_correct"], s["discordant_module_vs_gtopdb"]), (4, 3, 1))

    def test_stats(self):
        self.assertAlmostEqual(d.sign_p(0, 0), 1.0)
        self.assertLess(d.sign_p(20, 2), 0.001)
        lo, hi = d.wilson(90, 100)
        self.assertTrue(lo < 0.9 < hi)


if __name__ == "__main__":
    unittest.main()
