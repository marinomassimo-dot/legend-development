#!/usr/bin/env python3
"""Regressions for safe_push.py — every one is a refusal path, because the refusals are the tool."""
from __future__ import annotations
import os, subprocess, sys, unittest
from pathlib import Path
from tempfile import TemporaryDirectory

TOOL = Path(__file__).resolve().parent / "safe_push.py"

GATE_PASS = "import sys\nprint('VERDICT: PASS')\nprint('BLOCKS: 0')\nsys.exit(0)\n"
GATE_BLOCK = ("import sys\nprint('VERDICT: BLOCK_PUBLICATION')\n"
              "print('[BLOCK] EMAIL_ADDRESS somewhere')\nsys.exit(2)\n")


class SafePushRefusals(unittest.TestCase):
    def _repo(self, td: str, gate_src: str) -> Path:
        root = Path(td) / "repo"
        (root / "scripts").mkdir(parents=True)
        (root / "scripts" / "gate.py").write_text(gate_src, encoding="utf-8")
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "t@e.st"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "t"], check=True)
        (root / "a.txt").write_text("a\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "init"], check=True)
        return root

    def _run(self, root: Path, *args: str):
        env = dict(os.environ,
                   LEGEND_SAFE_PUSH_ROOT=str(root),
                   LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"))
        return subprocess.run([sys.executable, str(TOOL), *args],
                              capture_output=True, text=True, env=env)

    def test_a_dirty_tree_is_refused_before_the_gate_runs(self) -> None:
        with TemporaryDirectory() as td:
            root = self._repo(td, GATE_PASS)
            (root / "dirt.txt").write_text("x\n", encoding="utf-8")
            r = self._run(root, "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("working tree is not clean", r.stderr)

    def test_a_blocking_gate_refuses_the_push(self) -> None:
        """The defect of 2026-09-09: the gate said BLOCK and the push went anyway."""
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_BLOCK), "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("not PASS", r.stderr)
            self.assertIn("Nothing was pushed", r.stderr)

    def test_force_spellings_are_refused(self) -> None:
        with TemporaryDirectory() as td:
            root = self._repo(td, GATE_PASS)
            for bad in ("+main", "--force", "-f"):
                with self.subTest(bad=bad):
                    r = self._run(root, "origin", bad)
                    self.assertEqual(r.returncode, 1)
                    self.assertIn("fast-forward only", r.stderr)

    def test_usage_is_refused_rather_than_guessed(self) -> None:
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_PASS))
            self.assertEqual(r.returncode, 1)
            self.assertIn("usage", r.stderr)

    def test_a_passing_gate_reaches_the_push_step(self) -> None:
        """Control: the PASS path is not refused early — it fails at the absent remote instead."""
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_PASS), "nosuchremote", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("git push exited", r.stderr)
            self.assertNotIn("working tree", r.stderr)
            self.assertNotIn("not PASS", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
