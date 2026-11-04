#!/usr/bin/env python3
"""IT25 A3 offline regressions for gsrs_trial_it25.evaluate on a tiny cached-response fixture (no network)."""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import importlib.util, unittest
from pathlib import Path
spec = importlib.util.spec_from_file_location("g", Path(__file__).resolve().parent / "gsrs_trial_it25.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)


def rec(unii, name, syn=(), cls="chemical"):
    return {"substanceClass": cls, "approvalID": unii, "_name": name, "names": [{"name": s} for s in syn], "structure": {"smiles": "CCO"}}


class Evaluate(unittest.TestCase):
    def test_firm_needs_independent_corroboration(self):
        resp = {"content": [rec("U1", "BERZOSERTIB", ["VX-970", "VE-822"])], "total": 1}
        o = g.evaluate("Berzosertib", resp, ["VE-822", "IUPHAR.LIGAND:8003"], None, {"U1": {"CHEMBL1"}}, {"CHEMBL1": "AAAAAAAAAAAAAA-BBBBBBBBBB-N"})
        self.assertEqual(o["verdict"], "firm"); self.assertEqual(o["catalogue_inchikey"], "AAAAAAAAAAAAAA-BBBBBBBBBB-N")

    def test_name_alone_is_weak(self):
        o = g.evaluate("Foo", {"content": [rec("U2", "FOO")]}, [], None, {}, {})
        self.assertEqual(o["verdict"], "weak")

    def test_salt_names_do_not_match_and_two_substances_are_ambiguous(self):
        self.assertEqual(g.evaluate("Foo", {"content": [rec("U3", "FOO HYDROCHLORIDE")]}, [], None, {}, {})["verdict"], "no_hit")
        two = {"content": [rec("U4", "FOO"), rec("U5", "BAR", ["Foo"])]}
        self.assertEqual(g.evaluate("Foo", two, [], None, {}, {})["verdict"], "ambiguous")

    def test_row_chembl_contradiction_is_ambiguous(self):
        o = g.evaluate("Foo", {"content": [rec("U6", "FOO")]}, [], "CHEMBL9", {"U6": {"CHEMBL1"}}, {})
        self.assertEqual(o["verdict"], "ambiguous")

    def test_non_chemical_ignored(self):
        self.assertEqual(g.evaluate("Foo", {"content": [rec("U7", "FOO", cls="protein")]}, [], None, {}, {})["verdict"], "no_hit")


if __name__ == "__main__":
    unittest.main(verbosity=2)
