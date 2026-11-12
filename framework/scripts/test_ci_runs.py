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
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["git", "init", "-q", d], check=True)
            self.assertRaises(SystemExit, ci_runs.slug, "development", Path(d))                     # a repository with no GitHub remote is named as such
            subprocess.run(["git", "-C", d, "remote", "add", "origin", "https://github.com/owner/some-repo.git"], check=True)
            self.assertEqual(ci_runs.slug("development", Path(d)), "owner/some-repo")                # falls back to origin
            subprocess.run(["git", "-C", d, "remote", "add", "development", "https://github.com/other/name.git"], check=True)
            self.assertEqual(ci_runs.slug("development", Path(d)), "other/name")

    def test_a_rate_limit_answer_is_a_pause_until_the_reset_not_a_verdict(self):
        self.assertEqual(ci_runs.reset_wait({"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1000"}, 940.0), 62.0)
        self.assertIsNone(ci_runs.reset_wait({"X-RateLimit-Remaining": "7", "X-RateLimit-Reset": "1000"}, 940.0))     # a 403 with quota left is something else
        self.assertIsNone(ci_runs.reset_wait({}, 940.0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
