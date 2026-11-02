#!/usr/bin/env python3
"""Tests for select_pairs.py (IT19 P5 step 1). Run: python3 test_select_pairs.py"""
import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import select_pairs as sp  # noqa: E402

G26 = frozenset(["CACNA1G", "CACNA1H", "CACNA1I"] + ["X%d" % i for i in range(23)])
TT = frozenset(["CACNA1G", "CACNA1H", "CACNA1I"])
NEEDS = {"NEED-T": {"CACNA1G", "CACNA1H", "CACNA1I"}, "NEED-S": {"CACNA1G", "ABAT"},
         "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR": {"GRIN1", "GRIN2A", "GRIA1", "GRIA2", "GRIA3", "GRIA4"}}


def rec(tid, ttype, genes, action):
    return {"target_id": tid, "target_type": ttype, "genes": frozenset(genes), "action": action}


class Selection(unittest.TestCase):
    def test_record_class(self):
        mg = set().union(*NEEDS.values())
        self.assertEqual(sp.record_class(rec("a", "PROTEIN COMPLEX GROUP", G26, "BLOCKER"), mg), "heterogeneous")
        self.assertEqual(sp.record_class(rec("b", "PROTEIN FAMILY", TT, "BLOCKER"), mg), "homogeneous")
        self.assertEqual(sp.record_class(rec("c", "SINGLE PROTEIN", ["CACNA1H"], "BLOCKER"), mg), "single")
        self.assertEqual(sp.record_class(rec("d", "PROTEIN COMPLEX", ["GRIN1", "GRIN2B"], "ANTAGONIST"), mg), "complex")

    def test_strata(self):
        het = [dict(rec("a", "PROTEIN COMPLEX GROUP", G26, "BLOCKER"), **{"class": "heterogeneous"})]
        self.assertEqual(sp.stratum("NEED-T", het, False), "S01")
        mod = [dict(rec("a", "PROTEIN COMPLEX GROUP", G26, "MODULATOR"), **{"class": "heterogeneous"})]
        self.assertEqual(sp.stratum("NEED-T", mod, False), "S02")
        ampa = [dict(rec("x", "PROTEIN COMPLEX GROUP", ["GRIA1", "GRIA2", "GRIA3", "GRIA4"], "POSITIVE ALLOSTERIC MODULATOR"), **{"class": "homogeneous"})]
        self.assertEqual(sp.stratum("NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", ampa, False), "S11")

    def test_selection_is_hash_ordered_and_skips_determinate(self):
        rows = [{"need_id": "NEED-T", "need_direction": "down", "parent_chembl_id": c, "split": "dev", "L": "compatible", "L_v2": "compatible"}
                for c in ("C1", "C2", "C3")]
        fam = {c: [rec("f", "PROTEIN FAMILY", TT, "BLOCKER")] for c in ("C1", "C2", "C3")}
        chosen, pairs, unplaced = sp.select(rows, NEEDS, fam, {("NEED-T", "C1")})
        self.assertEqual(len(pairs), 2)
        self.assertEqual([p["parent"] for p in chosen], sorted(["C2", "C3"], key=sp.h))  # S03 quota 2 takes both
        self.assertEqual(unplaced, [])

    def test_help_is_safe(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, str(HERE / "select_pairs.py"), "--help"], cwd=d, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0)
            self.assertIn("select", r.stdout)
            self.assertEqual(list(Path(d).iterdir()), [])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            sp.main([])


if __name__ == "__main__":
    unittest.main(verbosity=2)
