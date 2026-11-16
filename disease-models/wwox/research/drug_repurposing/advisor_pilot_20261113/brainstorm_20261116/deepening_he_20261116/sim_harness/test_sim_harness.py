#!/usr/bin/env python3
"""Tests for sim_harness.py with the toy model: freeze determinism, hash-before-result refusals, worker-count invariance, designs, scoring, check."""
import csv, hashlib, json, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
H = str(HERE / "sim_harness.py")


def sh(*a, ok=True):
    r = subprocess.run([sys.executable, H, *a], capture_output=True, text=True)
    if ok:
        assert r.returncode == 0, r.stderr + r.stdout
    return r


def freeze(out, scan="scan_toy.json", seeds=4, model="toy_rebound.py", base=100):
    sh("freeze", "--model", str(HERE / model), "--scan", str(HERE / scan) if not Path(scan).is_absolute() else scan, "--seeds", str(seeds), "--base-seed", str(base), "--out", str(out))
    return (Path(out) / "freeze.sha256").read_text().split()[0]


class Harness(unittest.TestCase):
    def tmp(self):
        return Path(tempfile.mkdtemp()) / "o"

    def test_freeze_is_deterministic_and_never_overwritten(self):
        a, b = self.tmp(), self.tmp()
        self.assertEqual(freeze(a), freeze(b))
        self.assertNotEqual(sh("freeze", "--model", str(HERE / "toy_rebound.py"), "--scan", str(HERE / "scan_toy.json"), "--seeds", "4", "--base-seed", "100", "--out", str(a), ok=False).returncode, 0)

    def test_worker_count_does_not_change_the_bytes(self):
        a, b = self.tmp(), self.tmp(); ha, hb = freeze(a), freeze(b)
        sh("run", "--out", str(a), "--expect-freeze-sha256", ha, "--workers", "1"); sh("run", "--out", str(b), "--expect-freeze-sha256", hb, "--workers", "2")
        self.assertEqual((a / "results.tsv").read_bytes(), (b / "results.tsv").read_bytes())
        self.assertEqual((a / "results.sha256").read_text(), (b / "results.sha256").read_text())

    def test_refuses_wrong_digest_modified_model_modified_scan_and_overwrite(self):
        o = self.tmp(); h = freeze(o)
        self.assertNotEqual(sh("run", "--out", str(o), "--expect-freeze-sha256", "0" * 64, ok=False).returncode, 0)
        (o / "model_files" / "toy_rebound.py").write_text((o / "model_files" / "toy_rebound.py").read_text() + "\n# edited after the freeze\n")
        r = sh("run", "--out", str(o), "--expect-freeze-sha256", h, ok=False); self.assertNotEqual(r.returncode, 0); self.assertIn("REFUSED", r.stderr)
        o2 = self.tmp(); h2 = freeze(o2); (o2 / "scan.json").write_text((o2 / "scan.json").read_text().replace("100", "101") + " ")
        self.assertIn("REFUSED", sh("run", "--out", str(o2), "--expect-freeze-sha256", h2, ok=False).stderr)
        o3 = self.tmp(); h3 = freeze(o3); sh("run", "--out", str(o3), "--expect-freeze-sha256", h3)
        self.assertNotEqual(sh("run", "--out", str(o3), "--expect-freeze-sha256", h3, ok=False).returncode, 0)

    def test_oat_and_lhs_designs(self):
        d = Path(tempfile.mkdtemp())
        (d / "oat.json").write_text(json.dumps({"design": "oat", "oat": {"params": ["J_T", "tau_c"], "fraction": 0.4}}))
        (d / "lhs.json").write_text(json.dumps({"design": "lhs", "lhs": {"params": {"J_T": [0.5, 2.0], "tau_c": [10, 40]}, "n": 8, "seed": 3}}))
        o, l1, l2 = self.tmp(), self.tmp(), self.tmp()
        h = freeze(o, str(d / "oat.json"), seeds=2); sh("run", "--out", str(o), "--expect-freeze-sha256", h)
        labels = [r["point"] for r in csv.DictReader(open(o / "summary.tsv"), delimiter="\t")]
        self.assertEqual(labels, ["base", "J_T-40", "J_T+40", "tau_c-40", "tau_c+40"])
        rows = {r["point"]: r for r in csv.DictReader(open(o / "results.tsv"), delimiter="\t")}
        self.assertAlmostEqual(float(rows["J_T-40"]["J_T"]), 0.6); self.assertAlmostEqual(float(rows["tau_c+40"]["tau_c"]), 28.0)
        self.assertEqual(freeze(l1, str(d / "lhs.json"), seeds=1), freeze(l2, str(d / "lhs.json"), seeds=1))
        fr = json.loads((l1 / "freeze.json").read_text()); self.assertEqual(fr["points"], 8); self.assertEqual(fr["points_outside_declared_bounds"], [])

    def test_score_check_and_silent_fraction(self):
        o = self.tmp(); h = freeze(o, seeds=6); sh("run", "--out", str(o), "--expect-freeze-sha256", h); r = sh("score", "--out", str(o))
        sc = list(csv.DictReader(open(o / "predictions_scored.tsv"), delimiter="\t"))
        self.assertEqual(sc[0]["id"], "T1"); self.assertIn(sc[0]["verdict"], ("PASS", "FAIL"))
        self.assertEqual(sc[0]["n_undefined_seeds"], "0")
        self.assertEqual(sc[0]["verdict"], "FAIL")                      # the toy's modulator SHORTENS the interval: the frozen prediction was wrong, and the harness says so
        self.assertIn("fraction_silent", (o / "summary.tsv").read_text().splitlines()[0])
        c = sh("check", "--out", str(o), "--point", "J_T=0.5|pam=0"); self.assertIn("byte-identical True", c.stdout)

    def test_prediction_label_must_exist_and_harness_is_frozen(self):
        d = Path(tempfile.mkdtemp()); sc = json.loads((HERE / "scan_toy.json").read_text()); sc["predictions"][0]["a"] = "J_T=9|pam=9"; (d / "s.json").write_text(json.dumps(sc))
        r = sh("freeze", "--model", str(HERE / "toy_rebound.py"), "--scan", str(d / "s.json"), "--seeds", "1", "--base-seed", "1", "--out", str(self.tmp()), ok=False)
        self.assertNotEqual(r.returncode, 0); self.assertIn("is not a point of this scan", r.stderr)
        o = self.tmp(); freeze(o); self.assertIn("harness_sha256", json.loads((o / "freeze.json").read_text()))

    def test_unknown_parameter_is_refused_and_help_is_safe(self):
        d = Path(tempfile.mkdtemp()); (d / "bad.json").write_text(json.dumps({"design": "grid", "grid": {"nope": [1, 2]}}))
        r = sh("freeze", "--model", str(HERE / "toy_rebound.py"), "--scan", str(d / "bad.json"), "--seeds", "1", "--base-seed", "1", "--out", str(self.tmp()), ok=False)
        self.assertNotEqual(r.returncode, 0); self.assertIn("not in the model PARAMS", r.stderr)
        self.assertEqual(sh("--help").returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
