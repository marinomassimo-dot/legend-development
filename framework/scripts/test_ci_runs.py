#!/usr/bin/env python3
"""ci_runs.py: the verdict over the workflow runs of one commit (no network)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ci_runs  # noqa: E402


def run(n, status="completed", conclusion="success", name="Public release gate"):
    return {"run_number": n, "name": name, "status": status, "conclusion": conclusion, "head_sha": "142f6c5f" + "0" * 32}


class Verdict(unittest.TestCase):
    def test_all_success_is_zero(self):
        self.assertEqual(ci_runs.verdict([run(655), run(34, name="Publish the shareable view")])[0], 0)

    def test_a_run_in_progress_is_not_success(self):
        code, lines = ci_runs.verdict([run(655), run(656, status="in_progress", conclusion=None)])
        self.assertEqual(code, 124)
        self.assertIn("#656 Public release gate: in_progress", lines[1])

    def test_no_run_is_not_success(self):
        self.assertEqual(ci_runs.verdict([])[0], 3)

    def test_a_failure_wins_over_a_success(self):
        self.assertEqual(ci_runs.verdict([run(655), run(656, conclusion="failure")])[0], 1)

    def test_a_skipped_or_cancelled_run_is_not_success(self):
        self.assertEqual(ci_runs.verdict([run(655, conclusion="cancelled")])[0], 1)

    def test_a_malformed_sha_is_refused(self):
        self.assertEqual(ci_runs.main(["status", "not-a-sha"]), 2)

    def test_the_repository_is_read_from_the_remote(self):
        self.assertRegex(ci_runs.slug(), r"^[\w.-]+/[\w.-]+$")


if __name__ == "__main__":
    unittest.main(verbosity=2)
