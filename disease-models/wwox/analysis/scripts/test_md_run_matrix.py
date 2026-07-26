#!/usr/bin/env python3
"""Synthetic tests for the resumable exploratory MD matrix runner."""

from __future__ import annotations

import importlib.util
import json
import stat
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("md_run_matrix.py")
spec = importlib.util.spec_from_file_location("md_run_matrix", SCRIPT)
runner = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(runner)


def fake_screen(path: Path) -> None:
    path.write_text(
        "import argparse, json\n"
        "from pathlib import Path\n"
        "p=argparse.ArgumentParser()\n"
        "p.add_argument('--variant'); p.add_argument('--seed', type=int)\n"
        "p.add_argument('--output-root', type=Path)\n"
        "p.add_argument('--ns'); p.add_argument('--temp-k'); p.add_argument('--platform')\n"
        "p.add_argument('--implicit', action='store_true')\n"
        "a=p.parse_args()\n"
        "d=a.output_root / f'{a.variant}_seed{a.seed}'; d.mkdir(parents=True, exist_ok=True)\n"
        "(d/'summary.json').write_text(json.dumps({'status':'EXPLO'}))\n",
        encoding="utf-8",
    )
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


class MdRunMatrixTests(unittest.TestCase):
    def test_dry_run_builds_full_default_matrix(self) -> None:
        args = runner.parse_args(["--dry-run"])
        payload = runner.execute(args)
        self.assertEqual(12, payload["planned_runs"])
        self.assertEqual("dry-run", payload["mode"])

    def test_execute_and_resume_skip_completed_runs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = root / "fake_screen.py"
            fake_screen(fake)
            output = root / "output"
            argv = [
                "--variants",
                "WT,Q230P",
                "--seeds",
                "1",
                "--output-root",
                str(output),
                "--screen-script",
                str(fake),
                "--python",
                sys.executable,
            ]
            first = runner.execute(runner.parse_args(argv))
            second = runner.execute(runner.parse_args(argv))
        self.assertEqual(0, first["failures"])
        self.assertEqual(
            ["complete", "complete"],
            [item["status"] for item in first["runs"]],
        )
        self.assertEqual(
            ["skipped_complete", "skipped_complete"],
            [item["status"] for item in second["runs"]],
        )

    def test_invalid_screen_path_fails_before_execution(self) -> None:
        args = runner.parse_args(
            ["--screen-script", "/definitely/missing.py", "--dry-run"]
        )
        with self.assertRaisesRegex(ValueError, "does not exist"):
            runner.execute(args)


if __name__ == "__main__":
    unittest.main(verbosity=2)
