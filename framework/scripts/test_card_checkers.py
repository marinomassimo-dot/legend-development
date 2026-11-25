#!/usr/bin/env python3
"""Run each card folder's own checker, so the release battery and CI judge the cards.

Until 2026-11-25 the checks of `cards/` ran in CI only by accident (`test_documented_commands.py` calls the script with `--help`, and it has no argument parser) and those of
`cards_early/` never ran there (its parser answers `--help` and exits before checking anything).
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "disease-models" / "wwox" / "research" / "drug_repurposing"


class CardCheckers(unittest.TestCase):
    def run_checker(self, folder: str, examined: str) -> None:
        checker = MODULE / folder / "check_cards.py"
        if not checker.is_file():
            self.skipTest(f"module data absent: {folder}")
        done = subprocess.run([sys.executable, "-B", str(checker)], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
        report = done.stdout[-3000:] + done.stderr[-2000:]
        self.assertEqual(done.returncode, 0, report)
        self.assertRegex(done.stdout, examined, "the checker examined no packet:\n" + report)

    def test_the_cards_pass_their_checker(self) -> None:
        self.run_checker("cards", r"\b[1-9]\d* packets checked")

    def test_the_early_cards_pass_their_checker(self) -> None:
        self.run_checker("cards_early", r"packets checked: [1-9]")


if __name__ == "__main__":
    unittest.main(verbosity=2)
