#!/usr/bin/env python3
"""ci_runs.py: the verdict over the workflow runs of one commit (no network)."""
import contextlib
import io
import json
import urllib.error
from unittest import mock
import os
import shutil
import sys
import tempfile
import time
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


class FailingTests(unittest.TestCase):
    """2026-11-21 (HE): a red gate run names its failing tests through the public annotations; recorded from run 1713 (nine annotations, two of them the item-17 tests)."""

    JOBS = {"jobs": [{"id": 11, "conclusion": "failure"}, {"id": 12, "conclusion": "success"}]}
    NOTES = [
        {"title": "", "message": "Node.js 20 is deprecated."},
        {"title": "", "message": "Process completed with exit code 1."},
        {"title": "release regression", "message": "- framework/scripts/test_repurposing_view.py: exit 1 (FAILED)"},
        {"title": "release regression", "message": "FAIL: test_prose_policy_pairs_names_status_and_paths_are_gone (__main__.ShareableAudit.x)"},
        {"title": "release regression", "message": "AssertionError: 'x' unexpectedly found in '" + "<p>" * 400 + "'"},
    ]

    def fetch(self, calls):
        def f(url):
            calls.append(url)
            return self.JOBS if url.endswith("/jobs") else self.NOTES
        return f

    def test_only_the_release_regression_annotations_of_the_failed_job_are_listed_and_long_lines_are_cut(self):
        calls = []
        names = ci_runs.failing_tests(7, "o/r", self.fetch(calls))
        self.assertEqual(len(names), 3)
        self.assertTrue(all(len(n) <= 170 for n in names))
        self.assertIn("test_prose_policy_pairs", names[1])
        self.assertEqual(len(calls), 2)                                    # one request for the jobs, one for the single failed job: the success job is not asked
        self.assertTrue(calls[1].endswith("/check-runs/11/annotations?per_page=100"))

    def test_a_green_or_unfinished_run_asks_nothing(self):
        calls = []
        runs = [dict(run(1), id=1), dict(run(2, status="in_progress", conclusion=None), id=2), dict(run(3, conclusion="failure", name="Publish the shareable view"), id=3)]
        self.assertEqual(ci_runs.failure_lines(runs, "o/r", self.fetch(calls)), [])
        self.assertEqual(calls, [])

    def test_a_red_gate_run_prints_its_tests_and_an_unreadable_answer_is_said_not_hidden(self):
        red = dict(run(1713, conclusion="failure"), id=99)
        lines = ci_runs.failure_lines([red], "o/r", self.fetch([]))
        self.assertTrue(lines[0].startswith("  #1713 - framework/scripts/test_repurposing_view.py"))

        def broken(url):
            raise OSError("rate limit")
        said = ci_runs.failure_lines([red], "o/r", broken)
        self.assertEqual(len(said), 1)
        self.assertIn("failing tests not read (OSError: rate limit)", said[0])                  # the verdict was already printed and is not touched

    def test_a_red_run_without_a_regression_annotation_says_so(self):
        red = dict(run(5, conclusion="failure"), id=5)
        empty = lambda url: self.JOBS if url.endswith("/jobs") else [{"title": "", "message": "x"}]  # noqa: E731
        self.assertIn("no 'release regression' annotation", ci_runs.failure_lines([red], "o/r", empty)[0])


class SuiteTimes(unittest.TestCase):
    def test_a_concluded_gate_run_prints_its_published_suite_times_and_nothing_else_is_asked(self):
        asked = []

        def fetch(url):
            asked.append(url)
            if url.endswith("/jobs"):
                return {"jobs": [{"id": 11, "conclusion": "success"}]}
            return [{"title": "release regression", "message": "x"}, {"title": "suite time", "message": "total 34s over 3 suite(s); 30s b.py"}]

        runs = [{"name": ci_runs.GATE, "status": "completed", "conclusion": "success", "id": 7, "run_number": 5, "head_sha": "a" * 40},
                {"name": ci_runs.GATE, "status": "in_progress", "id": 8, "run_number": 6, "head_sha": "a" * 40}]
        self.assertEqual(ci_runs.suite_times(runs, "o/r", fetch), ["#5 success (aaaaaaaa)", "  total 34s over 3 suite(s)", "  30s b.py"])
        self.assertEqual(len(asked), 2)
        self.assertEqual(ci_runs.suite_times(runs[1:], "o/r", fetch), [])


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
        orig = ci_runs.fetch_recent
        ci_runs.fetch_recent = lambda repo: calls.append(repo) or runs
        self.addCleanup(lambda: setattr(ci_runs, "fetch_recent", orig))
        orig_slug = ci_runs.slug
        ci_runs.slug = lambda *a, **k: "o/r"
        self.addCleanup(lambda: setattr(ci_runs, "slug", orig_slug))
        for _ in range(2):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ci_runs.main(["wait", "a" * 40, "--timeout", "10"]), 0)
        self.assertEqual(len(calls), 1)


    def patch(self, **fns):
        for name, fn in fns.items():
            orig = getattr(ci_runs, name)
            setattr(ci_runs, name, fn)
            self.addCleanup(lambda n=name, o=orig: setattr(ci_runs, n, o))

    def test_one_list_read_serves_every_commit_in_flight_and_each_verdict_keeps_its_own_commit(self):
        """HE56: six commits waited by several sessions used one request per commit per interval and exhausted the unauthenticated hour; one read of the latest runs serves them all."""
        a, b = "a" * 40, "b" * 40
        recent = [{"run_number": 7, "name": "gate", "status": "in_progress", "conclusion": None, "head_sha": a},
                  {"run_number": 8, "name": "gate", "status": "completed", "conclusion": "success", "head_sha": b}]
        calls = []
        self.patch(fetch_recent=lambda repo: calls.append("list") or recent, fetch_runs=lambda sha, repo: calls.append("sha") or [], slug=lambda *x, **k: "o/r")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(ci_runs.main(["status", a]), 124)          # a is still running
            self.assertEqual(ci_runs.main(["status", b]), 0)            # b concluded: from the same read, no second request
        self.assertEqual(calls, ["list"])
        self.assertIn("#7 gate: in_progress (aaaaaaaa)", out.getvalue()); self.assertIn("#8 gate: completed success (bbbbbbbb)", out.getvalue())
        self.assertNotIn("#8 gate: completed success (aaaaaaaa)", out.getvalue())                       # a run is never attributed to another commit

    def test_a_concluded_verdict_is_final_and_costs_no_request_later(self):
        ci_runs.write_shared("c" * 40, "o/r", [{"run_number": 3, "status": "completed", "conclusion": "success", "head_sha": "c" * 40}], 1000.0)
        self.assertEqual(ci_runs.read_shared("c" * 40, "o/r", 115, 10**7)[0], "runs")             # far later, no TTL applies
        ci_runs.write_shared("d" * 40, "o/r", [{"run_number": 4, "status": "in_progress", "head_sha": "d" * 40}], 1000.0)
        self.assertIsNone(ci_runs.read_shared("d" * 40, "o/r", 115, 10**7))                          # a running one expires as before

    def test_a_commit_older_than_the_latest_list_is_asked_alone_and_attention_is_progressive(self):
        calls = []
        old = [{"run_number": 1, "name": "gate", "status": "completed", "conclusion": "success", "head_sha": "e" * 40}]
        self.patch(fetch_recent=lambda repo: calls.append("list") or [], fetch_runs=lambda sha, repo: calls.append("sha") or old, slug=lambda *x, **k: "o/r")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ci_runs.main(["status", "e" * 40]), 0)
        self.assertEqual(calls, ["list", "sha"])
        self.assertEqual([ci_runs.interval(w) for w in (0, 599, 600, 2399, 2400, 5000)], [120, 120, 240, 240, 480, 480])


    def test_status_during_a_declared_pause_shows_the_last_answer_as_old_not_as_current(self):
        sha = "f" * 40
        ci_runs.write_shared(sha, "o/r", [{"run_number": 9, "name": "gate", "status": "in_progress", "conclusion": None, "head_sha": sha}], 1000.0)
        ci_runs.write_shared(sha, "o/r", None, time.time(), pause=600.0)
        self.patch(slug=lambda *x, **k: "o/r")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(ci_runs.main(["status", sha]), 124)
        self.assertIn("#9 gate: in_progress", out.getvalue()); self.assertIn("not current", out.getvalue())


NOW = ci_runs.parse_time("2026-11-24T22:00:00Z")


def gate(n, status, created, conclusion=None, name="Public release gate", branch="main"):
    return {"run_number": n, "name": name, "status": status, "conclusion": conclusion, "head_sha": f"{n:08x}" + "0" * 32,
            "head_branch": branch, "event": "push", "created_at": created}


class Queue(unittest.TestCase):
    RUNS = [gate(12, "in_progress", "2026-11-24T21:30:00Z"), gate(10, "in_progress", "2026-11-24T20:00:00Z"),
            gate(13, "queued", "2026-11-24T21:59:00Z"), gate(9, "completed", "2026-11-24T19:00:00Z", "success"),
            gate(8, "completed", "2026-11-24T18:00:00Z", "cancelled"), gate(7, "completed", "2026-11-24T17:00:00Z", "failure"),
            gate(3, "in_progress", "2026-11-24T21:00:00Z", name="Publish the shareable view")]

    def test_timestamps_are_utc_and_not_the_local_zone(self):
        self.assertEqual(ci_runs.parse_time("1970-01-01T00:00:00Z"), 0.0)
        self.assertEqual(ci_runs.parse_time("2026-11-24T22:00:00Z") - ci_runs.parse_time("2026-11-24T21:00:00Z"), 3600.0)
        self.assertIsNone(ci_runs.parse_time("nonsense"))

    def test_open_runs_are_ordered_oldest_first_with_positions_and_ages(self):
        view = ci_runs.queue_view(self.RUNS, NOW)
        self.assertEqual([(r["position"], r["run"]) for r in view["rows"]], [(1, 10), (2, 12), (3, 13)])
        self.assertEqual((view["open"], view["in_progress"], view["queued"]), (3, 2, 1))
        self.assertEqual(view["oldest_age_seconds"], 7200.0)
        self.assertEqual(view["rows"][2]["age_seconds"], 60.0)

    def test_another_workflow_is_not_counted_and_can_be_asked_for(self):
        self.assertEqual(ci_runs.queue_view(self.RUNS, NOW)["open"], 3)
        other = ci_runs.queue_view(self.RUNS, NOW, "Publish the shareable view")
        self.assertEqual([r["run"] for r in other["rows"]], [3])

    def test_the_window_counts_conclusions_so_a_cancelled_share_can_be_read(self):
        view = ci_runs.queue_view(self.RUNS, NOW)
        self.assertEqual(view["window"], {"success": 1, "cancelled": 1, "failure": 1})
        self.assertEqual(view["window_runs"], 6)
        self.assertEqual(view["window_span_seconds"], 5 * 3600.0)

    def test_an_empty_queue_is_a_line_not_an_error(self):
        view = ci_runs.queue_view([gate(9, "completed", "2026-11-24T19:00:00Z", "success")], NOW)
        lines = ci_runs.render_queue(view)
        self.assertTrue(lines[0].startswith("QUEUE Public release gate: 0 open (0 in progress, 0 queued)"))
        self.assertNotIn("oldest", lines[0])

    def test_render_names_position_run_sha_branch_and_age(self):
        lines = ci_runs.render_queue(ci_runs.queue_view(self.RUNS, NOW))
        self.assertIn("oldest 2h00m", lines[0])
        self.assertIn("1. #10 0000000a main push in_progress age 2h00m", lines[1])

    def test_the_command_reads_one_list_prints_and_exits_zero_without_network(self):
        out = io.StringIO()
        with mock.patch.object(ci_runs, "slug", return_value="o/r"), mock.patch.object(ci_runs, "fetch_recent", return_value=self.RUNS) as fetched, \
                mock.patch.object(ci_runs, "write_recent"), contextlib.redirect_stdout(out):
            self.assertEqual(ci_runs.main(["queue", "--json"]), 0)
        self.assertEqual(fetched.call_count, 1)
        self.assertEqual(json.loads(out.getvalue())["open"], 3)

    def test_an_unreadable_api_is_exit_2_never_an_empty_queue(self):
        err = io.StringIO()
        denied = urllib.error.HTTPError("", 403, "rate limit", {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(time.time() + 600)}, None)
        with mock.patch.object(ci_runs, "slug", return_value="o/r"), mock.patch.object(ci_runs, "fetch_recent", side_effect=denied), contextlib.redirect_stderr(err):
            self.assertEqual(ci_runs.main(["queue"]), 2)
        self.assertIn("rate limit", err.getvalue())
        with mock.patch.object(ci_runs, "slug", return_value="o/r"), mock.patch.object(ci_runs, "fetch_recent", side_effect=OSError("down")), contextlib.redirect_stderr(err):
            self.assertEqual(ci_runs.main(["queue"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
