#!/usr/bin/env python3
"""ci_runs.py: the verdict over the workflow runs of one commit (no network)."""
import contextlib
import io
import os
import shutil
import sys
import tempfile
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


class SharedRead(unittest.TestCase):
    """HE47 H6: waiters on one machine share a single API read per commit and one declared rate-limit pause."""
    def setUp(self):
        self.d = tempfile.mkdtemp(prefix="ci_cache_")
        self.old = os.environ.get("TMPDIR")
        os.environ["TMPDIR"] = self.d
        self.addCleanup(lambda: (os.environ.__setitem__("TMPDIR", self.old) if self.old else os.environ.pop("TMPDIR", None), shutil.rmtree(self.d, ignore_errors=True)))

    def test_a_second_reader_inside_the_interval_reuses_the_answer(self):
        self.assertIsNone(ci_runs.read_shared("a" * 40, "o/r", 115, 1000.0))
        ci_runs.write_shared("a" * 40, "o/r", [{"run_number": 1}], 1000.0)
        self.assertEqual(ci_runs.read_shared("a" * 40, "o/r", 115, 1100.0), ("runs", [{"run_number": 1}]))
        self.assertIsNone(ci_runs.read_shared("a" * 40, "o/r", 115, 1200.0))                    # older than the interval: ask again
        self.assertIsNone(ci_runs.read_shared("b" * 40, "o/r", 115, 1100.0))                    # another commit shares nothing

    def test_a_declared_rate_limit_pause_stops_every_reader_until_the_reset(self):
        ci_runs.write_shared("a" * 40, "o/r", None, 1000.0, pause=600.0)
        self.assertEqual(ci_runs.read_shared("c" * 40, "o/r", 115, 1100.0), ("pause", 500.0))
        self.assertIsNone(ci_runs.read_shared("c" * 40, "o/r", 115, 1700.0))

    def test_an_unwritable_cache_costs_a_request_not_a_failure(self):
        os.environ["TMPDIR"] = "/proc/none"
        ci_runs.write_shared("a" * 40, "o/r", [], 1.0)
        self.assertIsNone(ci_runs.read_shared("a" * 40, "o/r", 115, 2.0))

    def test_the_wait_reads_the_api_once_for_two_loops_inside_the_interval(self):
        calls = []
        runs = [{"run_number": 5, "name": "gate", "status": "completed", "conclusion": "success", "head_sha": "a" * 40}]
        orig = ci_runs.fetch_runs
        ci_runs.fetch_runs = lambda sha, repo: calls.append(sha) or runs
        self.addCleanup(lambda: setattr(ci_runs, "fetch_runs", orig))
        orig_slug = ci_runs.slug
        ci_runs.slug = lambda *a, **k: "o/r"
        self.addCleanup(lambda: setattr(ci_runs, "slug", orig_slug))
        for _ in range(2):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ci_runs.main(["wait", "a" * 40, "--timeout", "10"]), 0)
        self.assertEqual(len(calls), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
