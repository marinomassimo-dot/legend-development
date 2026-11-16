#!/usr/bin/env python3
"""HE65 H3: a hypothesis row whose `sign` cell says aggravation is not emitted as a proposal to use its compound."""
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
import hypothesis_package as hp  # noqa: E402


def with_sign(sign):
    """hp.hypotheses_for as it is, except that every row of one package carries `sign` (a stand-in for a package that said so)."""
    real = hp.hypotheses_for

    def wrapped(pkgs, inv):
        rec = real(pkgs, inv)
        for x in rec["rows"]:
            if x["package"] == "ph_k2p_sci45_20261111":
                x["row"] = dict(x["row"], sign=sign)
                x["sign"] = hp.hyp_sign(x["row"])
        return rec
    return mock.patch.object(hp, "hypotheses_for", wrapped)


class AggravationIsASignOfItsOwn(unittest.TestCase):
    def test_the_helper_changes_only_an_aggravation_row(self):
        base = {"kind": "conditional_hypothesis_from_package", "nomination": "CONDITIONAL", "direction_stated": "none (x)"}
        for sign in ("match", "neutral", "unknown", "unclassified"):
            self.assertEqual(cp.as_aggravation(base, sign, package_row=True), base)
        out = cp.as_aggravation(base, "aggravation", package_row=True)
        self.assertEqual(out["kind"], "aggravation_hypothesis_from_package")
        self.assertTrue(out["nomination"].startswith("AGGRAVATION HYPOTHESIS"))
        self.assertIn("not a proposal to use any compound", out["nomination"])
        self.assertIn("never netted", out["nomination"])
        self.assertTrue(out["direction_stated"].startswith("aggravation hypothesis"))
        self.assertEqual(base["kind"], "conditional_hypothesis_from_package")       # the input row is not modified

    def test_a_package_row_with_the_aggravation_sign_is_not_a_conditional_proposal(self):
        with with_sign("aggravation"):
            rows, _ = cp.package_rows()
        mine = [r for r in rows if r["proposal_id"].startswith("CP-ph_k2p_sci45_20261111::")]
        self.assertTrue(mine)
        for r in mine:
            self.assertEqual(r["kind"], "aggravation_hypothesis_from_package")
            self.assertTrue(r["nomination"].startswith("AGGRAVATION HYPOTHESIS"))
            self.assertNotIn("CONDITIONAL", r["nomination"])
            self.assertNotIn("sign", r["unmapped_cells"].split(","))                # read as the sign, not left as an unmapped cell
        others = [r for r in rows if r not in mine]
        self.assertTrue(all(not r["kind"].startswith("aggravation") for r in others))

    def test_the_other_signs_leave_the_rows_byte_identical(self):
        plain, _ = cp.package_rows()
        for sign in ("match", "neutral", "unknown"):
            with with_sign(sign):
                signed, _ = cp.package_rows()
            self.assertEqual([{k: v for k, v in r.items() if k != "unmapped_cells"} for r in signed],
                             [{k: v for k, v in r.items() if k != "unmapped_cells"} for r in plain], sign)

    def test_committed_rows_carry_no_aggravation_row(self):
        rows, _ = cp.package_rows()
        self.assertFalse(any(r["kind"].startswith("aggravation") for r in rows))
        self.assertFalse(any(r["kind"].startswith("aggravation") for r in cp.rows()))
        self.assertTrue(all(r["direction_stated"].startswith("none") for r in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
