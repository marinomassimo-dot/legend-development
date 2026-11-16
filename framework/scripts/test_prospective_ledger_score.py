#!/usr/bin/env python3
"""Tests for prospective_ledger_score.py: sidecar validation, hand-computed log scores, the locator refusal, the digest refusal."""
import hashlib, math, subprocess, sys, tempfile, unittest
from pathlib import Path

TOOL = str(Path(__file__).resolve().parent / "prospective_ledger_score.py")
SIDE = "id\twho\tbin_low\tbin_high\tprobability\n" + "\n".join([
    "A\tledger\t-inf\t0\t0.2", "A\tledger\t0\t1\t0.7", "A\tledger\t1\tinf\t0.1",
    "A\tnaive\t-inf\t0\t0.1", "A\tnaive\t0\t1\t0.8", "A\tnaive\t1\tinf\t0.1",
    "B\tledger\t0\t10\t1.0"]) + "\n"


def run(*a):
    return subprocess.run([sys.executable, TOOL, *a], capture_output=True, text=True)


class Ledger(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()); self.side = self.d / "side.tsv"; self.side.write_text(SIDE)

    def obs(self, rows):
        p = self.d / "obs.tsv"; p.write_text("id\tvalue\tlocator\n" + "\n".join(rows) + "\n"); return str(p)

    def test_check_validates_and_prints_the_digest(self):
        r = run("check", str(self.side)); self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn(hashlib.sha256(SIDE.encode()).hexdigest(), r.stdout); self.assertIn("2 ids", r.stdout)

    def test_malformed_sidecars_are_refused(self):
        for bad, msg in (("A\tl\t0\t2\t0.5\nA\tl\t1\t3\t0.5\n", "overlap"), ("A\tl\t0\t1\t0.4\nA\tl\t1\t2\t0.4\n", "sum"), ("A\tl\t1\t1\t1.0\n", "not below"), ("A\tl\t0\tx\t1.0\n", "not a number")):
            p = self.d / "bad.tsv"; p.write_text("id\twho\tbin_low\tbin_high\tprobability\n" + bad)
            r = run("check", str(p)); self.assertEqual(r.returncode, 1, bad); self.assertIn(msg, r.stderr)

    def test_scores_match_a_hand_computation_and_the_floor_applies(self):
        r = run("score", str(self.side), self.obs(["A\t0.5\tFig. 2B, row 3", "B\t11\tTable 1"])); self.assertEqual(r.returncode, 0, r.stderr)
        tot = [l for l in r.stdout.splitlines() if l.startswith("TOTAL")][0]
        self.assertIn(f"ledger={math.log(0.7) + math.log(0.001):.4f}", tot)     # B: 11 is outside every bin -> the floor
        self.assertIn(f"naive={math.log(0.8):.4f}", tot)

    def test_a_value_without_a_locator_is_refused(self):
        for loc in ("", "-", "TBD", "n/a"):
            r = run("score", str(self.side), self.obs([f"A\t0.5\t{loc}"])); self.assertEqual(r.returncode, 1); self.assertIn("no locator", r.stderr)

    def test_unknown_id_duplicate_id_and_non_numeric_value_are_refused(self):
        self.assertIn("not in the sidecar", run("score", str(self.side), self.obs(["Z\t1\tp1"])).stderr)
        self.assertIn("twice", run("score", str(self.side), self.obs(["A\t1\tp1", "A\t2\tp2"])).stderr)
        self.assertIn("not a number", run("score", str(self.side), self.obs(["A\tabc\tp1"])).stderr)

    def test_digest_frozen_before_the_data_is_enforced_and_help_is_safe(self):
        good = hashlib.sha256(SIDE.encode()).hexdigest()
        self.assertEqual(run("score", str(self.side), self.obs(["A\t0.5\tp1"]), "--expect-sha256", good).returncode, 0)
        r = run("score", str(self.side), self.obs(["A\t0.5\tp1"]), "--expect-sha256", "0" * 64); self.assertEqual(r.returncode, 1); self.assertIn("frozen before the data", r.stderr)
        self.assertEqual(run("--help").returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
