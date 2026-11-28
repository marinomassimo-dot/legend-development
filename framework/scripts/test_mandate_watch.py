#!/usr/bin/env python3
"""Regressions for mandate_watch.py: the hourly continuity control.
Run: python3 -B framework/scripts/test_mandate_watch.py -v"""
from __future__ import annotations

import json
from datetime import datetime, timezone
import os
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock
import contextlib
import io
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mandate_watch as mw  # noqa: E402

TASK = "WATCH-TEST-1"
SID = "11111111-2222-3333-4444-555555555555"
NOW = 1_800_000_000.0


def record(state="OPEN", steps=("TODO",)):
    return {"TASK_ID": TASK, "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_X": {
        "MANDATE_STATE": state,
        "OBJ_A": {"order": 1, "steps": [{"step": f"s{i}", "status": s, "owner": "o", **({"evidence": "e1"} if s == "DONE" else {})}
                                         for i, s in enumerate(steps)]}}}


class Env:
    def __init__(self, rec, bound=True, age_minutes=120):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.root = t / "repo"
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        (self.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        self.proj = t / "projects"
        (self.proj / "p").mkdir(parents=True)
        self.tasks = t / "tasks"
        self.tasks.mkdir()
        self.tr = self.proj / "p" / f"{SID}.jsonl"
        text = f"MANDATE_BOUND: {TASK}" if bound else "hello"
        self.tr.write_text(json.dumps({"type": "assistant", "cwd": "/work/dir", "message": {"content": [{"type": "text", "text": text}]}}) + "\n"
                           + json.dumps({"type": "user", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(NOW)), "message": {"content": "hourly watch prompt"}}) + "\n")
        old = NOW - age_minutes * 60
        os.utime(self.tr, (old, old))
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = str(t / "state")

    def check(self, sessions, **kw):
        return mw.check(TASK, root=self.root, projects_dir=self.proj, tasks_root=self.tasks, sessions=sessions, now=NOW, **kw)

    def close(self):
        self.tmp.cleanup()
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)


class Watch(unittest.TestCase):
    def tearDown(self):
        getattr(self, "e", None) and self.e.close()

    def env(self, *a, **k):
        self.e = Env(*a, **k)
        return self.e

    def test_claude_is_found_without_a_path_in_cron(self):
        old = os.environ.get("PATH")
        os.environ["PATH"] = "/usr/bin:/bin"          # what cron provides
        try:
            self.assertTrue(mw.claude_bin().endswith("claude"))
            self.assertTrue(os.path.isabs(mw.claude_bin()))
        finally:
            os.environ["PATH"] = old

    def test_busy_session_is_running_and_never_asked(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "busy"}], deliver="resume")
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))

    def test_all_discovers_mandates_for_every_actor(self):
        e = self.env(record())
        for actor in ("plan", "scientist-a"):
            p = e.root / "ledger" / "tasks" / actor / f"{actor}-work.json"
            p.parent.mkdir(parents=True)
            rec = record()
            rec.update(TASK_ID=f"{actor}-work", ACTOR_ID=actor)
            p.write_text(json.dumps(rec))
        self.assertEqual(set(mw.open_tasks(e.root)), {TASK, "plan-work", "scientist-a-work"})

    def test_all_says_once_in_the_log_and_every_run_when_its_checkout_lacks_published_records(self):
        e = self.env(record())
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
        def git(*args):
            return subprocess.run(["git", *args], cwd=e.root, check=True, capture_output=True, text=True, env=env).stdout.strip()
        git("init", "-q", "-b", "main"); git("add", "."); git("commit", "-q", "-m", "base")
        base = git("rev-parse", "HEAD")
        git("update-ref", "refs/remotes/development/main", base)
        self.assertEqual(mw.note_checkout_behind(e.root, say=False), [])
        (e.root / "ledger/tasks/orchestrator/NEW.json").write_text("{}\n")
        git("add", "."); git("commit", "-q", "-m", "published record")
        git("update-ref", "refs/remotes/development/main", git("rev-parse", "HEAD"))
        git("reset", "-q", "--hard", base)                                   # this fixture checkout is the lagging one
        out = io.StringIO()
        with mock.patch.object(mw, "log_event") as logged, contextlib.redirect_stdout(out):
            self.assertEqual(mw.note_checkout_behind(e.root), ["ledger/tasks/orchestrator/NEW.json"])
            mw.note_checkout_behind(e.root)
        self.assertEqual(out.getvalue().count("CHECKOUT_BEHIND"), 2)
        self.assertEqual(logged.call_count, 1)

    def test_all_observes_failed_runtime_once_and_reports_json_without_revival(self):
        e = self.env(record())
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "open_tasks", return_value=[TASK, "OTHER"]), \
                mock.patch.object(mw, "registered_worktrees", return_value=[e.root]), \
                mock.patch.object(mw, "list_sessions", return_value=None) as listing, \
                mock.patch.object(mw, "find_bound_transcript", return_value=None), \
                mock.patch.object(mw.subprocess, "run") as process, contextlib.redirect_stdout(output):
            self.assertEqual(mw._check_all(args), 0)
        self.assertEqual(listing.call_count, 1)
        process.assert_not_called()
        rows = json.loads(output.getvalue())
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(r["state"] == "UNKNOWN" for r in rows))

    def test_existing_hourly_watch_catches_up_only_executable_mandates_and_readonly_stays_readonly(self):
        e = self.env(record())
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check", return_value={"state": "RUNNING", "action": "NONE"}) as checked, \
                mock.patch.object(mw, "retire_released", return_value=[{"verdict": "RETIRED"}]) as retire, \
                contextlib.redirect_stdout(io.StringIO()):
            mw._check_all(args)
            retire.assert_called_once_with(TASK, [], execute=True)
            retire.reset_mock(); args.deliver = "none"
            mw._check_all(args)
            retire.assert_called_once_with(TASK, [], execute=False)
            # 2026-11-20: a released predecessor is housekeeping about THAT host, independent of the successor's queue: BLOCKED (waiting) and COMPLETE
            # (complete pending, the standing mandates) are looked at as well; PAUSED, UNKNOWN and DUPLICATE_HOST are not.
            for state in ("BLOCKED", "COMPLETE", "STOPPED_RESUMABLE"):
                retire.reset_mock(); checked.return_value = {"state": state, "action": "NONE"}
                mw._check_all(args)
                retire.assert_called_once_with(TASK, [], execute=False)
            for state in ("PAUSED", "UNKNOWN", "DUPLICATE_HOST"):
                retire.reset_mock(); checked.return_value = {"state": state, "action": "NONE"}
                mw._check_all(args)
                retire.assert_not_called()

    def test_the_states_a_real_classification_gives_to_waiting_and_complete_pending_mandates_are_the_ones_that_retire(self):
        """Tie the set to the real classifier: COMPLETE_PENDING and ALL_BLOCKED must land in a state that reaches the catch-up; a PAUSED or CANCELLED record must not."""
        kw = dict(session=None, session_list_ok=True, bound=True, idle_seconds=None, pending={}, signature="s", now=0.0)
        waiting = mw.classify({"verdict": "ALL_BLOCKED", "message": "all steps blocked"}, **kw)
        pending = mw.classify({"verdict": "COMPLETE_PENDING", "message": "every step is DONE"}, **kw)
        self.assertEqual((waiting["state"], pending["state"]), ("BLOCKED", "COMPLETE"))
        self.assertTrue({waiting["state"], pending["state"]} <= set(mw.RETIRE_STATES))
        for word in ("PAUSED", "CANCELLED"):
            stopped = mw.classify({"verdict": "COMPLETE_PENDING", "message": "block is " + word}, **kw)
            self.assertEqual(stopped["state"], "PAUSED")
            self.assertNotIn(stopped["state"], mw.RETIRE_STATES)
        self.assertNotIn("UNKNOWN", mw.RETIRE_STATES)
        self.assertNotIn("DUPLICATE_HOST", mw.RETIRE_STATES)

    def test_new_unmerged_task_is_checked_in_its_registered_worktree(self):
        e = self.env(record())
        tree = Path(e.tmp.name) / "science-worktree"
        p = tree / "ledger/tasks/scientist-a/SCI-NEW.json"
        p.parent.mkdir(parents=True)
        rec = record()
        rec.update(TASK_ID="SCI-NEW", ACTOR_ID="scientist-a")
        p.write_text(json.dumps(rec))
        args = SimpleNamespace(root=str(e.root), deliver="none", quiet_minutes=25, resume_arg=[], json=True)
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, tree]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check", return_value={"state": "UNKNOWN", "action": "NONE"}) as checked, \
                contextlib.redirect_stdout(io.StringIO()):
            mw._check_all(args)
        roots = {c.args[0]: c.kwargs["root"] for c in checked.call_args_list}
        self.assertEqual(roots["SCI-NEW"], tree)
        self.assertEqual(roots[TASK], e.root)

    def test_stale_open_worktree_does_not_reopen_a_paused_main_record(self):
        e = self.env(record("PAUSED"))
        tree = Path(e.tmp.name) / "old-worktree"
        p = tree / "ledger/tasks/orchestrator" / f"{TASK}.json"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps(record()))
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, tree]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "find_bound_transcript", return_value=None), \
                contextlib.redirect_stdout(output):
            mw._check_all(args)
        rows = json.loads(output.getvalue())
        self.assertEqual((rows[0]["state"], rows[0]["action"]), ("PAUSED", "NONE"))
        self.assertEqual(rows[0]["record_root"], str(e.root))

    def test_ambiguous_unmerged_records_never_start_a_session(self):
        e = self.env(record())
        (e.root / "ledger/tasks/orchestrator" / f"{TASK}.json").unlink()
        trees = []
        for name in ("copy-a", "copy-b"):
            tree = Path(e.tmp.name) / name
            p = tree / "ledger/tasks/plan" / f"{TASK}.json"
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps(record()))
            trees.append(tree)
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, *trees]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check") as checked, contextlib.redirect_stdout(output):
            mw._check_all(args)
        checked.assert_not_called()
        row = json.loads(output.getvalue())[0]
        self.assertEqual((row["state"], row["action"]), ("UNKNOWN", "NONE"))
        self.assertIn("multiple unmerged", row["why"])

    def test_a_published_record_missing_from_a_lagging_root_says_so(self):
        e = self.env(record())
        rel = f"ledger/tasks/plan/{TASK}.json"
        (e.root / "ledger/tasks/orchestrator" / f"{TASK}.json").unlink()
        trees = []
        for name in ("copy-a", "copy-b"):
            tree = Path(e.tmp.name) / name
            (tree / rel).parent.mkdir(parents=True)
            (tree / rel).write_text(json.dumps(record()))
            trees.append(tree)
        git = lambda *a: subprocess.run(["git", "-C", str(e.root), "-c", "user.email=t@example.invalid", "-c", "user.name=t", *a], check=True, capture_output=True)
        git("init", "-q")
        (e.root / rel).parent.mkdir(parents=True, exist_ok=True)
        (e.root / rel).write_text(json.dumps(record()))
        git("add", rel)
        git("commit", "-q", "-m", "x")
        git("update-ref", "refs/remotes/development/main", "HEAD")
        (e.root / rel).unlink()                                                 # the root checkout lags: the record is published, not here
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, *trees]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check") as checked, contextlib.redirect_stdout(output):
            mw._check_all(args)
        checked.assert_not_called()                                              # still nothing is guessed or started
        row = json.loads(output.getvalue())[0]
        self.assertEqual((row["state"], row["action"], row.get("published")), ("UNKNOWN", "NONE", True))
        self.assertIn("merge --ff-only development/main", row["why"])

    def test_waiting_for_science_does_not_block_an_independent_step(self):
        rec = record(steps=("BLOCKED", "TODO"))
        rec["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0]["blocker"] = "waiting for the science batch"
        e = self.env(rec)
        r = e.check([])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
        self.assertIn("s1", r["why"])

    def test_bound_session_reconciles_missing_evidence_instead_of_unknown(self):
        for state in ("OPEN", "COMPLETE"):
            rec = record(state, ("DONE",))
            rec["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0].pop("evidence")
            e = self.env(rec)
            r = e.check([])
            self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
            self.assertIn(r["record_verdict"], ("EVIDENCE_PENDING", "INCONSISTENT_COMPLETE"))
            e.close()

    def test_a_running_mandate_still_leaves_a_trace_in_the_event_log(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "busy"}], deliver="resume")
        self.assertEqual(r["state"], "RUNNING")
        lines = [json.loads(l) for l in (Path(os.environ["LEGEND_MANDATE_WATCH_STATE"]) / mw.EVENTS_FILE).read_text().splitlines() if l.strip()]
        self.assertTrue(any(x.get("task") == TASK and x.get("state") == "RUNNING" for x in lines))

    def test_recent_background_task_output_is_running_even_when_idle(self):
        e = self.env(record())
        d = e.tasks / "proj" / SID / "tasks"
        d.mkdir(parents=True)
        f = d / "a.output"
        f.write_text("x")
        os.utime(f, (NOW - 60, NOW - 60))
        r = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))

    def test_idle_and_silent_session_with_open_work_is_resumable(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))

    def test_live_session_is_not_resumed_from_outside(self):
        e = self.env(record())
        calls = []
        r = e.check([{"sessionId": SID, "status": "idle"}], deliver="resume", runner=lambda c, cwd=None: calls.append(c))
        self.assertEqual(calls, [])
        self.assertIn("alive", r["delivery"])

    def test_dead_session_is_revived_under_its_own_id_and_only_once(self):
        e = self.env(record())
        calls = []
        run = lambda c, cwd=None: (calls.append(c), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1]
        r = e.check([], deliver="resume", runner=run)
        self.assertEqual(r["delivery"], "sent")
        self.assertEqual([os.path.basename(calls[0][0])] + calls[0][1:4], ["claude", "--bg", "--resume", SID])
        self.assertEqual(mw.transcript_cwd(e.tr), "/work/dir")
        r2 = e.check([], deliver="resume", runner=run)            # same queue state: request still pending
        self.assertEqual(r2["action"], "NONE")
        self.assertEqual(len(calls), 1)

    def test_a_failed_revival_logs_why_it_failed(self):
        """IT19 P1: `claude --bg --resume` exits 1 with 'Workspace not trusted' until the operator accepts trust; the event must say so."""
        e = self.env(record())
        run = lambda c, cwd=None: SimpleNamespace(returncode=1, stdout="", stderr="Workspace not trusted. Run `claude` in /work/dir once and accept the trust prompt")
        r = e.check([], deliver="resume", runner=run)
        self.assertTrue(r["delivery"].startswith("failed rc=1"))
        events = [json.loads(l) for l in (mw.state_dir() / mw.EVENTS_FILE).read_text().splitlines()]
        self.assertIn("Workspace not trusted", events[-1].get("delivery_output", ""))

    def test_progress_in_the_record_allows_a_new_request(self):
        e = self.env(record(steps=("TODO", "TODO")))
        run = lambda c, cwd=None: SimpleNamespace(returncode=0, stdout="", stderr="")
        e.check([], deliver="resume", runner=run)
        rec = record(steps=("DONE", "TODO"))
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        self.assertEqual(e.check([], deliver="resume", runner=run)["action"], "RESUME")

    def test_complete_paused_and_blocked_are_never_restarted(self):
        for rec, want in ((record("COMPLETE", ("DONE",)), "COMPLETE"), (record("PAUSED"), "PAUSED"),
                          (record("OPEN", ("DONE",)), "COMPLETE")):
            e = self.env(rec)
            r = e.check([])
            self.assertEqual((r["state"], r["action"]), (want, "NONE"), rec)
            e.close()
        blocked = record("OPEN", ("BLOCKED",))
        blocked["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0]["blocker"] = "waiting for an external dataset"
        e = self.env(blocked)
        r = e.check([])
        self.assertEqual((r["state"], r["action"]), ("BLOCKED", "NONE"))

    def test_unknown_when_nothing_binds_the_task_or_the_listing_fails(self):
        e = self.env(record(), bound=False)
        self.assertEqual(e.check([])["state"], "UNKNOWN")
        e.close()
        e = self.env(record())
        r = e.check(None) if False else mw.classify({"verdict": "CONTINUE", "message": ""}, None, False, True, 9999, {}, "s", NOW)
        self.assertEqual((r["state"], r["action"]), ("UNKNOWN", "NONE"))

    def test_a_marker_inside_a_sentence_is_refused_and_the_diagnosis_names_the_session(self):
        # 2026-11-11, IT46: `MANDATE_BOUND: <id>. Identity: ... ` as the start of a sentence left the mandate UNKNOWN with no hint why
        e = self.env(record(), bound=False)
        e.tr.write_text(json.dumps({"type": "assistant", "timestamp": "2026-11-11T21:48:36.000Z", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}. Identity: orchestrator. The residue is clean."}]}}) + "\n")
        r = e.check([])
        self.assertEqual((r["state"], r["session"]), ("UNKNOWN", None))
        self.assertEqual(r["near_marker"]["session"], SID)
        self.assertIn(f"session {SID} wrote", r["why"])
        self.assertIn("must write that plain line again", r["why"])
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        bound = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual(bound["session"], SID)                   # the plain line binds, and the near-miss is no longer reported
        self.assertNotIn("near_marker", bound)

    def test_a_fenced_or_unrelated_mention_is_not_a_near_marker(self):
        e = self.env(record(), bound=False)
        e.tr.write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"```\nMANDATE_BOUND: {TASK} extra\n```\nand MANDATE_BOUND: OTHER-TASK. Hello"}]}}) + "\n")
        self.assertNotIn("near_marker", e.check([]))

    def test_self_call_ignores_its_own_work_but_not_subagents_running_before_the_turn(self):
        e = self.env(record(), age_minutes=0)
        d = e.tasks / "proj" / SID / "tasks"
        d.mkdir(parents=True)
        own = d / "own_foreground_command.output"
        own.write_text("x")
        os.utime(own, (NOW + 5, NOW + 5))              # written after the cron turn began: the caller's own command
        r = e.check([{"sessionId": SID, "status": "busy"}], self_call=True)
        self.assertEqual(r["action"], "RESUME")
        agent = d / "agent.output"
        agent.write_text("x")
        os.utime(agent, (NOW - 30, NOW - 30))           # an agent was writing just before the turn began
        self.assertEqual(e.check([{"sessionId": SID, "status": "busy"}], self_call=True)["state"], "RUNNING")
        os.utime(agent, (NOW - 3600, NOW - 3600))       # an hour earlier: finished long ago
        self.assertEqual(e.check([{"sessionId": SID, "status": "busy"}], self_call=True)["state"], "STOPPED_RESUMABLE")   # (the request is already pending: dedupe)


class Jobs(unittest.TestCase):
    """Background jobs are judged by their own process identity, not by output recency."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = self.tmp.name
        self.cont = {"verdict": "CONTINUE", "message": "work remains"}

    def tearDown(self):
        for j in mw.load_jobs(TASK):
            if j["state"] == "ALIVE":
                try:
                    os.kill(j["pid"], 9)
                except OSError:
                    pass
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)
        self.tmp.cleanup()

    def wait_state(self, want, secs=8):
        end = time.time() + secs
        while time.time() < end:
            js = mw.load_jobs(TASK)
            if js and js[-1]["state"] == want:
                return js[-1]
            time.sleep(0.1)
        self.fail(f"job never reached {want}: {mw.load_jobs(TASK)}")

    def classify(self, **kw):
        return mw.classify(self.cont, None, True, True, 99999, {}, "sig", NOW, jobs=mw.summarise_jobs(mw.load_jobs(TASK)), **kw)

    def test_silent_long_job_is_running_even_when_the_session_is_idle_and_silent(self):
        mw.job_run(TASK, "battery", ["sleep", "30"])
        r = self.classify()
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))
        self.assertIn("alive", r["why"])

    def test_same_label_is_not_started_twice(self):
        a = mw.job_run(TASK, "battery", ["sleep", "30"])
        b = mw.job_run(TASK, "battery", ["sleep", "30"])
        self.assertTrue(a["started"])
        self.assertFalse(b["started"])
        self.assertEqual(a["pid"], b["pid"])

    def test_finished_job_is_collected_once(self):
        mw.job_run(TASK, "quick", ["true"])
        j = self.wait_state("DONE")
        r = self.classify()
        self.assertEqual(r["action"], "RESUME")
        self.assertIn("finished job", r["why"])
        self.assertTrue(mw.job_collect(TASK, j["id"]))
        self.assertNotIn("finished job", self.classify()["why"])

    def test_job_killed_without_an_exit_status_is_dead_not_finished(self):
        j = mw.job_run(TASK, "doomed", ["sleep", "30"])
        os.kill(j["pid"], 9)
        self.wait_state("DEAD")
        r = self.classify()
        self.assertEqual(r["action"], "RESUME")
        self.assertIn("DIED", r["why"])

    def test_reused_pid_with_another_start_time_is_not_alive(self):
        j = mw.job_run(TASK, "reuse", ["sleep", "30"])
        job = mw.load_jobs(TASK)[-1]
        job["start_ticks"] += 1                       # the recorded start time no longer matches the process
        self.assertEqual(mw.job_state(job), "DEAD")

    def test_complete_record_without_the_push_is_not_complete(self):
        done = {"verdict": "RELEASED", "message": "MANDATE_STATE COMPLETE"}
        r = mw.classify(done, None, True, True, 99999, {}, "sig", NOW, push_missing="the closing commit is not on development/main")
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
        self.assertIn("COMPLETE but", r["why"])
        ok = mw.classify(done, None, True, True, 99999, {}, "sig", NOW)
        self.assertEqual((ok["state"], ok["action"]), ("COMPLETE", "NONE"))
        paused = mw.classify({"verdict": "RELEASED", "message": "MANDATE_STATE PAUSED"}, None, True, True, 99999, {}, "sig", NOW, push_missing="x")
        self.assertEqual((paused["state"], paused["action"]), ("PAUSED", "NONE"))


class MetadataIsNotProgress(unittest.TestCase):
    """ADV-206 (Codex review 22): runtime metadata appended to a transcript's tail moves its mtime with nobody working. With no live process behind the
    transcript that is not progress; a live busy session, a live job, a real recent turn and the pending-request grace still are."""

    def setUp(self):
        self.e = Env(record())
        iso = lambda t: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))
        self.iso = iso
        lines = [{"type": "assistant", "cwd": "/work/dir", "timestamp": iso(NOW - 5 * 3600), "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}},
                 {"type": "assistant", "timestamp": iso(NOW - 5 * 3600 + 30), "message": {"content": [{"type": "text", "text": "last real turn"}]}},
                 # what the runtime writes afterwards: timestamped queue record, untimestamped title/cost/bridge records
                 {"type": "queue-operation", "timestamp": iso(NOW - 120)}, {"type": "custom-title", "customTitle": "IT"}, {"type": "cost-state"}, {"type": "last-prompt"}]
        self.e.tr.write_text("".join(json.dumps(x) + "\n" for x in lines))
        os.utime(self.e.tr, (NOW - 120, NOW - 120))                    # metadata moved the mtime two minutes ago

    def tearDown(self):
        self.e.close()

    def real_turn_two_minutes_ago(self):
        with self.e.tr.open("a") as fh:
            fh.write(json.dumps({"type": "assistant", "timestamp": self.iso(NOW - 120), "message": {"content": [{"type": "text", "text": "working"}]}}) + "\n")
        os.utime(self.e.tr, (NOW - 120, NOW - 120))

    def test_the_four_outcomes(self):
        # 1. no live session, no live job, metadata-only mtime: the quiet threshold must not hide the stop
        r = self.e.check([])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"), r)
        # 2. the same, with a real turn two minutes ago (a listing that cannot see the process): still RUNNING
        self.real_turn_two_minutes_ago()
        r = self.e.check([])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"), r)
        # 3. a live busy session over a metadata-only transcript
        self.e.close()
        self.setUp()
        r = self.e.check([{"sessionId": SID, "status": "busy"}])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"), r)
        # 4. a known live job with no live session
        with mock.patch.object(mw, "load_jobs", return_value=[{"state": "ALIVE", "label": "battery", "pid": 1}]):
            r = self.e.check([])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"), r)

    def test_a_live_idle_session_is_judged_by_its_turns_too(self):
        """The real IT59 case of 2026-11-24 (live, idle, last turn 367 min old, mtime 10 min old): it must not read RUNNING either."""
        r = self.e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"), r)
        self.real_turn_two_minutes_ago()
        r = self.e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"), r)

    def test_the_startup_grace_and_pending_suppression_are_unchanged(self):
        mw._save(TASK, {"requested_at": NOW - 120, "signature": mw.mc._queue_signature(self.e.root, mw.mc.status_for(self.e.root, TASK).get("record")), "session": SID})
        r = self.e.check([])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "NONE"), r)
        self.assertIn("pending", r["why"])

    def test_a_transcript_without_a_timestamped_turn_keeps_its_mtime(self):
        self.e.tr.write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        os.utime(self.e.tr, (NOW - 120, NOW - 120))
        self.assertEqual(self.e.check([])["state"], "RUNNING")

    def test_last_real_turn_reads_back_across_blocks_and_skips_metadata(self):
        self.assertEqual(mw.last_real_turn(self.e.tr), NOW - 5 * 3600 + 30)
        self.assertEqual(mw.last_real_turn(self.e.tr, block=40), NOW - 5 * 3600 + 30)       # lines cut by every block boundary
        self.assertIsNone(mw.last_real_turn(self.e.tr.with_name("absent.jsonl")))


class BusyIsNotProgress(unittest.TestCase):
    """IT39: a session reported busy while its record still lists authorised work must say so (a session that stopped to wait on a monitor read 'session busy' as progress)."""

    def test_the_busy_answer_names_the_work_the_record_still_lists_and_the_self_call_flag(self):
        st = {"verdict": "CONTINUE", "message": "MANDATE T CONTINUE \u2014 3 executable step(s) remain; next: A"}
        out = mw.classify(st, {"status": "busy"}, True, True, 0, {}, "sig", 0, 10, jobs=None, push_missing=None)
        self.assertEqual((out["state"], out["action"]), ("RUNNING", "NONE"))
        self.assertIn("3 executable step(s)", out["why"])
        self.assertIn("--self-call", out["why"])

    def test_without_remaining_work_the_busy_answer_is_unchanged(self):
        st = {"verdict": "CONTINUE", "message": "MANDATE T CONTINUE"}
        out = mw.classify(st, {"status": "busy"}, True, True, 0, {}, "sig", 0, 10, jobs=None, push_missing=None)
        self.assertEqual(out["why"], "session busy")



class Routing(unittest.TestCase):
    """HE53: a message's recipients are the sends actually made, resolved to live sessions; a name in the text is only a claim (IT answered 'IT to ADV and HE' and the transport receipt named HE alone)."""
    ADV_ID = "e6526331-6b7c-4631-8c9b-9e9d79867e90"
    OTHER_ID = "99999999-aaaa-bbbb-cccc-dddddddddddd"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        rec = {"TASK_ID": "ORCH-ADV-X", "SESSION_NAME": "ADV \u2014 Strategic Advisor", "SESSION_BINDING": {"session_id": self.ADV_ID, "pid_at_start": 1}}
        (self.root / "ledger" / "tasks" / "orchestrator" / "ORCH-ADV-X.json").write_text(json.dumps(rec), encoding="utf-8")
        self.live = [{"name": "HE", "sessionId": "11111111-0000-0000-0000-000000000001"}, {"name": "IT Orchestrator", "sessionId": "11111111-0000-0000-0000-000000000002"},
                     {"name": "legend-development-39", "sessionId": self.ADV_ID}]

    def test_a_role_resolves_to_the_session_the_record_binds_and_not_to_another_name(self):
        r = mw.route("ADV", self.live, self.root)
        self.assertEqual((r["status"], r["recipient"], r["session_id"]), ("RESOLVED", "legend-development-39", self.ADV_ID))
        self.assertEqual(mw.route("IT", self.live, self.root)["recipient"], "IT Orchestrator")             # a whole-word alias of a live name
        self.assertEqual(mw.route("legend-development-39", self.live, self.root)["session_id"], self.ADV_ID)

    def test_two_recipients_declared_and_one_send_is_a_mismatch_naming_the_missing_one(self):
        res = mw.check_recipients("IT to ADV and HE: baseline", ["HE"], self.live, self.root)       # the 14 Nov case: the receipt named HE only
        self.assertEqual((res["verdict"], res["missing_send_to"]), ("MISMATCH", ["ADV"]))
        self.assertEqual(mw.check_recipients("IT to ADV and HE: baseline", ["HE", "legend-development-39"], self.live, self.root)["verdict"], "OK")

    def test_an_address_no_longer_associated_with_the_awaited_session_is_not_reused(self):
        live = [dict(x) for x in self.live]
        live[2] = {"name": "legend-development-39", "sessionId": self.OTHER_ID}                       # the name now belongs to another session
        r = mw.route("ADV", live, self.root)
        self.assertEqual((r["status"], r["recipient"]), ("UNRESOLVED", None))
        self.assertEqual(r["bound_not_live"], [{"task": "ORCH-ADV-X", "session_id": self.ADV_ID}])    # said, not guessed
        res = mw.check_recipients("HE to ADV: ping", ["legend-development-39"], live, self.root)
        self.assertEqual(res["verdict"], "MISMATCH")

    def test_two_live_sessions_answering_to_one_role_are_ambiguous_and_none_is_chosen(self):
        live = self.live + [{"name": "IT scratch", "sessionId": "11111111-0000-0000-0000-000000000003"}]
        r = mw.route("IT", live, self.root)
        self.assertEqual((r["status"], r["recipient"]), ("AMBIGUOUS", None))
        self.assertEqual(len(r["candidates"]), 2)

    def test_an_unreadable_listing_is_not_a_guess_and_the_first_line_forms_are_read(self):
        self.assertEqual(mw.route("ADV", None, self.root)["status"], "UNRESOLVED")
        self.assertEqual(mw.declared_recipients("HE to ADV (cc IT): delivery"), ["ADV", "IT"])
        self.assertEqual(mw.declared_recipients("ORCH to HE (cc ADV): BASELINE ACQUIRED."), ["HE", "ADV"])
        self.assertEqual(mw.declared_recipients("no addressing line here"), [])
        self.assertEqual(mw.check_recipients("no addressing line here", ["HE"], self.live, self.root)["verdict"], "NO_DECLARED_RECIPIENT")


class ReleasedCheck(unittest.TestCase):
    """The successor's check that the old session released the task: exit 0 only for RELEASED; a wrong id or folder is MISSING (exit 2), never a release."""

    def run_cli(self, path):
        buf = io.StringIO()
        with mock.patch.object(mw, "transcript_for_session", return_value=path), contextlib.redirect_stdout(buf):
            rc = mw.main(["released", "--session", "11111111-2222-3333-4444-555555555555", "--task", "T-1"])
        return rc, buf.getvalue()

    def test_states_and_exit_codes(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "t.jsonl"
            text = lambda t: json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": t}]}}) + "\n"
            self.assertEqual(self.run_cli(None)[0], 2)                                                  # no transcript found for that id
            self.assertEqual(self.run_cli(Path(td) / "absent.jsonl")[0], 2)
            f.write_text(text("MANDATE_BOUND: T-1"), encoding="utf-8")
            rc, out = self.run_cli(f)
            self.assertEqual((rc, out.split()[0]), (1, "BOUND"))
            f.write_text(f.read_text() + text("MANDATE_RELEASED: T-1"), encoding="utf-8")
            rc, out = self.run_cli(f)
            self.assertEqual((rc, out.split()[0]), (0, "RELEASED"))

    def test_a_malformed_release_line_is_named_and_releases_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "t.jsonl"
            entry = lambda t, kind="assistant": json.dumps({"type": kind, "message": {"content": [{"type": "text", "text": t}]}}) + "\n"
            bound = entry("MANDATE_BOUND: T-1")
            for bad in ("Done.\n\nMANDATE_RELEASED", "MANDATE_RELEASED: T-1.", "**MANDATE_RELEASED: T-1**"):
                f.write_text(bound + entry(bad), encoding="utf-8")
                rc, out = self.run_cli(f)
                self.assertEqual((rc, out.split()[0]), (1, "BOUND"), bad)
                self.assertIn("NEAR_MISS", out, bad)
                self.assertTrue(out.rstrip().endswith("MANDATE_RELEASED: T-1"), out)
            # a request quoted by the peer, a prose mention, a fenced quote and a line written before a new binding are not attempts
            for quiet in (bound + entry("MANDATE_RELEASED", "user"), bound + entry("I will write MANDATE_RELEASED later"),
                          bound + entry("```\nMANDATE_RELEASED\n```"), entry("MANDATE_RELEASED") + bound):
                f.write_text(quiet, encoding="utf-8")
                self.assertNotIn("NEAR_MISS", self.run_cli(f)[1], quiet)


class HandoffCheck(unittest.TestCase):
    """2026-11-20: the successor of SCI checkpoint L bound with a text-only message and sat 41 minutes; the check reads the transcripts: RUNNING only after a tool call that follows the bind line."""
    NOW = datetime(2026, 11, 20, 8, 0, tzinfo=timezone.utc)

    def entry(self, minute, kind, text=None, tool=False):
        stamp = f"2026-11-20T07:{minute:02d}:00.000Z"
        content = ([{"type": "text", "text": text}] if text else []) + ([{"type": "tool_use", "name": "Bash"}] if tool else [])
        return json.dumps({"type": kind, "timestamp": stamp, "message": {"content": content}}) + "\n"

    def write(self, td, name, lines):
        f = Path(td) / name
        f.write_text("".join(lines), encoding="utf-8")
        return f

    def state(self, old, new, within=5, sessions=None):
        return mw.handoff_state("T-1", old, new, self.NOW, within, sessions, "bbbbbbbb")

    def test_every_step_has_its_own_verdict(self):
        with tempfile.TemporaryDirectory() as td:
            old_bound = self.write(td, "o1.jsonl", [self.entry(1, "assistant", "MANDATE_BOUND: T-1")])
            old_rel = self.write(td, "o2.jsonl", [self.entry(1, "assistant", "MANDATE_BOUND: T-1"), self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
            fresh = self.write(td, "n0.jsonl", [self.entry(41, "user", "launch brief")])
            self.assertEqual(self.state(old_rel, None)["verdict"], "NEW_NOT_FOUND")
            self.assertEqual(self.state(old_bound, fresh)["verdict"], "WAITING_FOR_RELEASE")
            r = self.state(old_rel, fresh)                                                               # released 20 minutes ago, successor silent
            self.assertEqual((r["verdict"], r["waited_min"]), ("WAITING_FOR_BIND", 20))
            self.assertIn("send it the follow-up now", r["next"])
            both = self.write(td, "n1.jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1")])
            self.assertEqual(self.state(old_bound, both)["verdict"], "BOTH_BOUND")

    def test_a_successor_that_works_without_the_marker_is_told_why_it_is_not_bound(self):
        with tempfile.TemporaryDirectory() as td:
            old = self.write(td, "o.jsonl", [self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
            claims = self.write(td, "n.jsonl", [self.entry(41, "user", "launch brief")] + [self.entry(41 + i, "assistant", "I am bound on T-1", tool=True) for i in range(4)])
            r = self.state(old, claims)
            self.assertEqual(r["verdict"], "WAITING_FOR_BIND")
            self.assertEqual(r["successor_turns_since_release"], 4)
            self.assertIn("no plain `MANDATE_BOUND: T-1` line", r["next"])
            quiet = self.write(td, "q.jsonl", [self.entry(41, "user", "launch brief"), self.entry(42, "assistant", "reading")])
            r = self.state(old, quiet)
            self.assertNotIn("successor_turns_since_release", r)
            self.assertIn("send it the follow-up now", r["next"])

    def test_a_text_only_bind_is_stalled_after_the_allowed_minutes_and_a_bind_with_a_tool_call_is_running(self):
        with tempfile.TemporaryDirectory() as td:
            old = self.write(td, "o.jsonl", [self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
            text_only = self.write(td, "n1.jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1")])
            r = self.state(old, text_only)
            self.assertEqual((r["verdict"], r["bound_min"]), ("STALLED", 19))
            self.assertEqual(self.state(old, text_only, within=30)["verdict"], "BOUND_WAITING_FIRST_ACTION")
            same_response = self.write(td, "n2.jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1"), self.entry(41, "assistant", tool=True)])   # the marker entry, then a tool call of the same response
            self.assertEqual(self.state(old, same_response)["verdict"], "RUNNING")
            before = self.write(td, "n3.jsonl", [self.entry(38, "assistant", tool=True), self.entry(41, "assistant", "MANDATE_BOUND: T-1")])
            self.assertEqual(self.state(old, before)["verdict"], "STALLED")                              # a tool call BEFORE the bind does not count

    def test_the_stalled_answer_names_the_row_by_its_age_when_two_sessions_share_a_name(self):
        with tempfile.TemporaryDirectory() as td:
            old = self.write(td, "o.jsonl", [self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
            new = self.write(td, "n.jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1")])
            now_ms = self.NOW.timestamp() * 1000
            rows = [{"sessionId": "aaaaaaaa-1", "name": "SCI", "startedAt": now_ms - 3 * 3600_000}, {"sessionId": "bbbbbbbb-2", "name": "SCI", "startedAt": now_ms - 25 * 60_000}]
            text = self.state(old, new, sessions=rows)["next"]
            self.assertIn("name SCI, started 25 min ago", text)
            self.assertIn("180 min ago", text)
            self.assertIn("take the row whose 'started' matches", text)
            self.assertIn("not in the live listing", self.state(old, new, sessions=[])["next"])


class SessionNames(unittest.TestCase):
    """Labels follow a completed handoff, including predecessors already stopped."""
    entry = HandoffCheck.entry
    write = HandoffCheck.write
    OLD = "aaaaaaaa-1111-2222-3333-444444444444"
    NEW = "bbbbbbbb-1111-2222-3333-444444444444"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        (self.base / "project").mkdir()
        self.old = self.write(self.base / "project", self.OLD + ".jsonl", [
            self.entry(1, "assistant", "MANDATE_BOUND: T-1"),
            self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
        self.new = self.write(self.base / "project", self.NEW + ".jsonl", [
            self.entry(41, "assistant", "MANDATE_BOUND: T-1"),
            self.entry(42, "assistant", tool=True)])
        self.live = [{"sessionId": self.NEW, "name": "HE - CANDIDATE bbbbbbbb"}]
        self.inventory = [{"sessionId": self.OLD, "name": "HE - CURRENT aaaaaaaa"}, *self.live]

    def state(self):
        return mw.session_name_state("T-1", self.live, self.inventory, self.base)

    def test_stopped_predecessor_is_demoted_before_successor_is_promoted_without_writes(self):
        before = self.old.read_bytes(), self.new.read_bytes()
        with mock.patch.object(mw.subprocess, "run") as process:
            result = self.state()
        self.assertEqual(result["state"], "PENDING")
        self.assertEqual([(r["session_id"], r["to"]) for r in result["renames"]], [
            (self.OLD, "HE - PREVIOUS aaaaaaaa"), (self.NEW, "HE - CURRENT bbbbbbbb")])
        self.assertEqual(before, (self.old.read_bytes(), self.new.read_bytes()))
        process.assert_not_called()

    def test_repeated_completed_reconciliation_is_empty(self):
        self.inventory[0]["name"] = "HE - PREVIOUS aaaaaaaa"
        self.inventory[1]["name"] = "HE - CURRENT bbbbbbbb"
        self.assertEqual((self.state()["state"], self.state()["renames"]), ("CURRENT", []))

    def test_current_title_on_newest_chat_does_not_elect_it(self):
        self.live.append({"sessionId": self.OLD, "name": "HE - CURRENT aaaaaaaa", "startedAt": 9999999999999})
        self.assertEqual(self.state()["current_session"], self.NEW)
        self.old.write_text(self.old.read_text() + self.entry(43, "assistant", "MANDATE_BOUND: T-1"))
        self.assertEqual((self.state()["state"], self.state()["renames"]), ("UNKNOWN", []))

    def test_no_promotion_before_first_action_and_no_change_to_other_mandate(self):
        original = self.new.read_bytes()
        self.new.write_text(self.entry(41, "assistant", "MANDATE_BOUND: T-1"))
        self.assertEqual(self.state()["renames"], [])
        self.new.write_bytes(original)
        self.old.write_text(self.old.read_text() + self.entry(43, "assistant", "MANDATE_BOUND: OTHER"))
        self.assertEqual([r["session_id"] for r in self.state()["renames"]], [self.NEW])
        self.old.write_text(self.entry(0, "assistant", "MANDATE_BOUND: OTHER")
                           + self.entry(1, "assistant", "MANDATE_BOUND: T-1")
                           + self.entry(40, "assistant", "MANDATE_RELEASED: T-1"))
        self.assertEqual([r["session_id"] for r in self.state()["renames"]], [self.NEW])

    def test_missing_inventory_is_unknown_and_cli_never_renames(self):
        with mock.patch.object(mw, "session_name_inventory", return_value=None):
            self.assertEqual(mw.session_name_state("T-1", self.live, projects_dir=self.base)["state"], "UNKNOWN")
        with mock.patch.object(mw, "list_sessions", return_value=[]), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(mw.main(["labels", "--task", "T-1"]), 0)
        self.assertEqual(json.loads(output.getvalue())["state"], "UNKNOWN")

    def test_runtime_inventory_includes_completed_rows_and_failed_call_is_unknown(self):
        with mock.patch.object(mw.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout=json.dumps(self.inventory))) as process:
            self.assertEqual(mw.session_name_inventory(), self.inventory)
        self.assertEqual(process.call_args.args[0][-3:], ["agents", "--all", "--json"])
        with mock.patch.object(mw.subprocess, "run", return_value=SimpleNamespace(returncode=1, stdout="[]")):
            self.assertIsNone(mw.session_name_inventory())


class PredecessorRetirement(unittest.TestCase):
    entry = HandoffCheck.entry
    write = HandoffCheck.write
    OLD = "aaaaaaaa-1111-2222-3333-444444444444"
    NEW = "bbbbbbbb-1111-2222-3333-444444444444"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        (self.base / "project").mkdir()
        self.old = self.write(self.base / "project", self.OLD + ".jsonl", [self.entry(1, "assistant", "MANDATE_BOUND: T-1"), self.entry(40, "assistant", "MANDATE_RELEASED: T-1")])
        self.new = self.write(self.base / "project", self.NEW + ".jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1"), self.entry(42, "assistant", tool=True)])
        self.rows = [{"sessionId": self.OLD, "id": "old-runtime-id", "pid": 12345, "kind": "background", "status": "idle", "state": "done"},
                     {"sessionId": self.NEW, "id": "new-runtime-id", "pid": 12346, "kind": "background", "status": "busy", "state": "working"}]
        self.stopped = False
        self.listing = self.patch("list_sessions", side_effect=lambda: self.rows[1:] if self.stopped else self.rows)
        self.ticks = self.patch("_start_ticks", side_effect=lambda pid: None if self.stopped and pid == 12345 else 100)
        self.patch("_proc_state", return_value="S")
        self.children = self.patch("_descendants", return_value=[])
        self.jobs = self.patch("load_jobs", return_value=[])
        self.patch("claude_bin", return_value="/supported/claude")
        sleeper = mock.patch.object(mw.time, "sleep")
        sleeper.start(); self.addCleanup(sleeper.stop)
        env = mock.patch.dict(os.environ, {"LEGEND_MANDATE_WATCH_STATE": str(self.base / "state")})
        env.start(); self.addCleanup(env.stop)
        self.runner = mock.patch.object(mw.subprocess, "run", side_effect=self.stop)
        self.command = self.runner.start(); self.addCleanup(self.runner.stop)

    def patch(self, name, **kwargs):
        p = mock.patch.object(mw, name, **kwargs)
        value = p.start(); self.addCleanup(p.stop)
        return value

    def stop(self, cmd, **kwargs):
        self.assertEqual(cmd, ["/supported/claude", "stop", "old-runtime-id"])
        self.assertNotIn("shell", kwargs)
        self.stopped = True
        return SimpleNamespace(returncode=0, stdout="stopped", stderr="")

    def retire(self, execute=True):
        return mw.retire_predecessor("T-1", self.OLD, self.NEW, execute=execute, projects_dir=self.base)

    def test_dry_run_and_repeated_verified_stop_preserve_both_transcripts_and_worktree(self):
        tree = self.base / "worktree"; tree.mkdir()
        (tree / "unique.txt").write_text("keep")
        before = (self.old.read_bytes(), self.new.read_bytes())
        self.assertEqual(self.retire(False)["verdict"], "ELIGIBLE")
        self.command.assert_not_called()
        self.assertEqual(self.retire()["verdict"], "RETIRED")
        self.assertEqual(self.retire()["verdict"], "ALREADY_STOPPED")
        self.assertEqual(self.command.call_count, 1)
        self.assertEqual(before, (self.old.read_bytes(), self.new.read_bytes()))
        self.assertEqual((tree / "unique.txt").read_text(), "keep")

    def test_active_interactive_unknown_or_ambiguous_predecessors_are_never_stopped(self):
        original = dict(self.rows[0])
        for change in ({"kind": "interactive"}, {"status": "busy"}, {"state": "working"}, {"id": None}, {"pid": None}, {"id": "new-runtime-id"}):
            with self.subTest(change=change):
                self.rows[0] = dict(original, **change)
                self.assertEqual(self.retire()["verdict"], "KEPT")
        self.rows[0] = original
        self.rows.append(dict(original))
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_missing_release_other_mandate_and_nonacting_successor_are_kept(self):
        old, new = self.old.read_text(), self.new.read_text()
        cases = [
            (old.replace("MANDATE_RELEASED: T-1", "not a release"), new),
            (self.entry(40, "assistant", "MANDATE_RELEASED: T-1"), new),
            (old + self.entry(43, "assistant", "MANDATE_BOUND: OTHER-TASK"), new),
            (old, self.entry(41, "assistant", "MANDATE_BOUND: T-1")),
            (old, self.entry(38, "assistant", "MANDATE_BOUND: T-1") + self.entry(39, "assistant", tool=True)),
        ]
        for a, b in cases:
            self.old.write_text(a); self.new.write_text(b)
            self.assertEqual(self.retire()["verdict"], "KEPT")
        self.old.unlink()
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_past_overlap_is_reported_but_recoverable_after_release_and_actual_successor_work(self):
        self.new.write_text(self.entry(38, "assistant", "MANDATE_BOUND: T-1") + self.entry(39, "assistant", tool=True) + self.entry(42, "assistant", tool=True))
        result = self.retire()
        self.assertEqual(result["verdict"], "RETIRED")
        self.assertTrue(result["overlap_observed"])

    def test_same_name_is_not_a_host_identity_and_duplicate_hosts_block_retirement(self):
        self.rows[0]["name"] = self.rows[1]["name"] = "SCI"
        third = "cccccccc-1111-2222-3333-444444444444"
        self.write(self.base / "project", third + ".jsonl", [self.entry(41, "assistant", "MANDATE_BOUND: T-1")])
        self.rows.append({"sessionId": third, "name": "SCI"})
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_live_jobs_descendants_and_unknown_process_inventory_are_kept(self):
        self.jobs.return_value = [{"state": "ALIVE"}]
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.jobs.return_value = []
        for children in ([321], None):
            self.children.return_value = children
            self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_corrupt_job_metadata_is_unknown_instead_of_no_live_work(self):
        d = mw.jobs_dir("T-1"); d.mkdir(parents=True)
        (d / "unreadable.json").write_text("not JSON")
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_pending_stop_after_a_crash_is_not_reissued(self):
        mw._save("retirement-" + self.OLD, {"verdict": "STOP_PENDING"})
        self.assertEqual(self.retire()["verdict"], "STOP_UNVERIFIED")
        self.command.assert_not_called()

    def test_changed_pid_or_new_turn_before_stop_aborts(self):
        calls = 0
        def change():
            nonlocal calls
            calls += 1
            if calls > 1:
                self.rows[0]["pid"] = 54321
            return self.rows
        self.listing.side_effect = change
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_reused_pid_with_same_runtime_row_aborts(self):
        self.ticks.side_effect = [100, 200]
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_refusal_or_false_success_is_persisted_and_never_retried(self):
        self.command.side_effect = None
        self.command.return_value = SimpleNamespace(returncode=1, stdout="", stderr="permission denied")
        self.assertEqual(self.retire()["verdict"], "STOP_REFUSED")
        self.assertTrue(self.retire()["retry_suppressed"])
        self.assertEqual(self.command.call_count, 1)

    def test_exit_zero_without_process_exit_is_not_success(self):
        self.command.side_effect = None
        self.command.return_value = SimpleNamespace(returncode=0, stdout="stopped", stderr="")
        self.assertEqual(self.retire()["verdict"], "STOP_UNVERIFIED")
        self.assertTrue(self.retire()["retry_suppressed"])
        self.assertEqual(self.command.call_count, 1)

    def test_delayed_teardown_is_observed_without_a_second_stop(self):
        def listing():
            if self.stopped and self.listing.call_count >= 5:
                return self.rows[1:]
            return self.rows
        self.listing.side_effect = listing
        self.assertEqual(self.retire()["verdict"], "RETIRED")
        self.assertEqual(self.command.call_count, 1)

    def test_runtime_failure_and_unwritable_attempt_state_issue_no_stop(self):
        self.listing.side_effect = None; self.listing.return_value = None
        self.assertEqual(self.retire()["verdict"], "KEPT")
        self.listing.return_value = self.rows
        with mock.patch.object(mw, "_save"):
            self.assertEqual(self.retire()["verdict"], "KEPT")
        self.command.assert_not_called()

    def test_catchup_discovers_released_predecessors_without_a_prompt_or_display_name(self):
        find = mw.transcript_for_session
        with mock.patch.object(mw, "transcript_for_session", side_effect=lambda sid, projects_dir=None: find(sid, self.base)):
            self.assertEqual(mw.retire_released("T-1", self.rows, execute=True)[0]["verdict"], "RETIRED")
        self.command.assert_called_once()

    def test_catchup_does_not_pick_interactive_or_still_bound_sessions_by_name(self):
        self.rows[0]["kind"] = "interactive"
        self.rows[0]["name"] = self.rows[1]["name"] = "SCI"
        find = mw.transcript_for_session
        with mock.patch.object(mw, "transcript_for_session", side_effect=lambda sid, projects_dir=None: find(sid, self.base)):
            self.assertEqual(mw.retire_released("T-1", self.rows, execute=True), [])
        self.command.assert_not_called()

    def test_cli_keeps_running_successor_distinct_from_unretired_predecessor(self):
        running = {"verdict": "RUNNING"}
        with mock.patch.object(mw, "handoff_state", return_value=running), \
                mock.patch.object(mw, "retire_predecessor", return_value={"verdict": "KEPT"}) as retire, \
                contextlib.redirect_stdout(io.StringIO()):
            args = ["handoff", "--task", "T-1", "--old", self.OLD, "--new", self.NEW]
            self.assertEqual(mw.main(args), 0)
            self.assertFalse(retire.call_args.kwargs["execute"])
            self.assertEqual(mw.main(args + ["--retire-old"]), 5)
            self.assertTrue(retire.call_args.kwargs["execute"])


class HandoffNextLine(unittest.TestCase):
    """2026-11-21: the handoff to the HE successor printed `session_names` in the log and `KEPT` for an old interactive chat with two bound lines left; nobody was told to apply the renames or which records already
    closed those mandates. The `next` line and `legacy_bound_tasks` now carry both to the launcher."""

    def test_pending_names_and_legacy_bound_lines_reach_the_launcher_and_no_window_is_left_to_close(self):
        names = {"task": "T-1", "state": "PENDING", "renames": [{"session_id": "x", "from": "A", "to": "A - CURRENT x"}]}
        legacy = [{"task": "OLD-1", "record_verdict": "COMPLETE_PENDING"}, {"task": "OLD-2", "record_verdict": "RELEASED"}]
        text = mw.handoff_next("KEPT", names, legacy, False)
        for part in ("SESSION NAMES PENDING (1)", "labels --task T-1", "OLD-1 (record COMPLETE_PENDING)", "OLD-2 (record RELEASED)", "never by a release line", "no window is left to close"):
            self.assertIn(part, text)
        self.assertNotIn("operator", text.lower())

    def test_a_clean_handoff_says_only_what_is_true(self):
        text = mw.handoff_next("RETIRED", {"task": "T-1", "state": "CURRENT", "renames": []}, [], True)
        self.assertEqual(text, "successor running; predecessor retirement RETIRED")

    def test_legacy_bound_tasks_reads_the_records_not_the_chat(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            old = base / "old.jsonl"
            lines = [{"timestamp": "2026-11-20T10:00:00Z", "type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {t}"}]}} for t in ("T-1", "OLD-1")]
            old.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")
            (base / "ledger" / "tasks" / "plan").mkdir(parents=True)
            (base / "ledger" / "tasks" / "plan" / "OLD-1.json").write_text(json.dumps({"TASK_ID": "OLD-1", "ACTOR_ID": "plan", "MANDATE_STATE": "COMPLETE"}), encoding="utf-8")
            got = mw.legacy_bound_tasks("T-1", old, base)
        self.assertEqual([x["task"] for x in got], ["OLD-1"])
        self.assertIsNotNone(got[0]["record_verdict"])


class TranscriptPrefix(unittest.TestCase):
    """2026-11-19: `released --session <short id>` answered MISSING, and a wait loop on it could never turn true. A unique prefix of at least 8 characters now finds the transcript; an ambiguous or too short one does not."""

    def test_unique_prefix_finds_the_transcript_and_ambiguity_or_shortness_does_not(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            for folder, sid in (("proj-a", "aaaaaaaa-1111-2222-3333-444444444444"), ("proj-b", "aaaaaaaa-9999-8888-7777-666666666666"), ("proj-b", "bbbbbbbb-1111-2222-3333-444444444444")):
                (base / folder).mkdir(exist_ok=True); (base / folder / f"{sid}.jsonl").write_text("{}\n")
            find = lambda x: mw.transcript_for_session(x, base)
            self.assertEqual(find("bbbbbbbb-1111-2222-3333-444444444444").name, "bbbbbbbb-1111-2222-3333-444444444444.jsonl")
            self.assertEqual(find("bbbbbbbb").name, "bbbbbbbb-1111-2222-3333-444444444444.jsonl")      # unique prefix of 8
            self.assertIsNone(find("aaaaaaaa"))                                                       # two sessions share it: never a guess
            self.assertIsNone(find("bbbbbb"))                                                         # shorter than 8
            self.assertIsNone(find("../bbbbbbbb"))                                                    # no path tricks


class FreshWindowRoute(unittest.TestCase):
    """ADV-078 trial, measured 2026-11-19: a fresh window of a record with NO SESSION_NAME left two live sessions named SCI; route said AMBIGUOUS although the old one had written MANDATE_RELEASED."""
    OLD = "9400b253-25a0-4b03-8822-96361325fc16"
    NEW = "f630dd25-a894-445c-85fa-ee15a01b9ec9"

    def make(self):
        t = tempfile.TemporaryDirectory(); self.addCleanup(t.cleanup)
        root = Path(t.name)
        rec = record(state="OPEN", steps=("TODO",)); rec.update({"TASK_ID": "ORCH-SCI-X", "ACTOR_ID": "orchestrator"})
        d = root / "ledger" / "tasks" / "orchestrator"; d.mkdir(parents=True)
        (d / "ORCH-SCI-X.json").write_text(json.dumps(rec), encoding="utf-8")
        return root, [listed(self.OLD, "SCI"), listed(self.NEW, "SCI")]

    def test_the_live_marker_host_of_an_open_record_is_the_target_and_the_released_one_is_listed(self):
        root, live = self.make()
        with mock.patch.object(mw, "live_bound_sessions", side_effect=lambda task, sessions, projects_dir=None: [{"session_id": self.NEW}] if task == "ORCH-SCI-X" else []):
            r = mw.route("SCI", live, root)
        self.assertEqual((r["status"], r["session_id"]), ("RESOLVED", self.NEW))
        self.assertEqual([x["session_id"] for x in r["surplus_name_matches"]], [self.OLD])          # listed, never silently dropped

    def test_with_no_marker_host_or_two_the_answer_stays_ambiguous(self):
        root, live = self.make()
        with mock.patch.object(mw, "live_bound_sessions", return_value=[]):
            self.assertEqual(mw.route("SCI", live, root)["status"], "AMBIGUOUS")
        with mock.patch.object(mw, "live_bound_sessions", return_value=[{"session_id": self.OLD}, {"session_id": self.NEW}]):
            self.assertEqual(mw.route("SCI", live, root)["status"], "AMBIGUOUS")                    # two hosts: DUPLICATE_HOST territory, nothing is chosen


class ActorAlias(unittest.TestCase):
    """DEC-20261118-ADVISOR-ACTOR: an ACTOR_ID as recipient resolves to the live session bound to an OPEN record of that actor, and to nothing when two sessions answer."""
    ADV = "e6526331-6b7c-4631-8c9b-9e9d79867e90"
    IT = "11111111-0000-0000-0000-000000000002"

    def make(self, adv_actor, adv_dir):
        t = tempfile.TemporaryDirectory(); self.addCleanup(t.cleanup)
        root = Path(t.name)
        for actor, task, sid, state in ((adv_actor, "ORCH-ADV-FOLLOWTHROUGH", self.ADV, "OPEN"), ("orchestrator", "ORCH-IT-OLD", self.ADV, "COMPLETE")):
            rec = record(state=state, steps=("DONE",) if state == "COMPLETE" else ("TODO",))
            rec.update({"TASK_ID": task, "ACTOR_ID": actor, "SESSION_BINDING": {"session_id": sid}})
            d = root / "ledger" / "tasks" / (adv_dir if task.startswith("ORCH-ADV") else "orchestrator")
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{task}.json").write_text(json.dumps(rec), encoding="utf-8")
        live = [listed(self.ADV, "ADV"), listed(self.IT, "IT Orchestrator")]
        return root, live

    def test_before_the_passage_orchestrator_is_ambiguous_and_names_both_sessions(self):
        root, live = self.make("orchestrator", "orchestrator")
        r = mw.route("orchestrator", live, root)
        self.assertEqual(r["status"], "AMBIGUOUS")
        self.assertEqual({c["session_id"] for c in r["candidates"]}, {self.ADV, self.IT})

    def test_after_the_passage_each_alias_resolves_to_one_session(self):
        root, live = self.make("advisor", "advisor")
        a = mw.route("advisor", live, root)
        self.assertEqual((a["status"], a["session_id"]), ("RESOLVED", self.ADV))
        o = mw.route("orchestrator", live, root)
        self.assertEqual((o["status"], o["session_id"]), ("RESOLVED", self.IT))      # a COMPLETE record of that actor bound to another live session does not count

    def test_a_substitute_session_with_the_advisor_binding_is_still_one_host(self):
        root, live = self.make("advisor", "advisor")
        rec_path = root / "ledger/tasks/advisor/ORCH-ADV-FOLLOWTHROUGH.json"
        rec = json.loads(rec_path.read_text()); rec["SESSION_BINDING"]["session_id"] = "22222222-0000-0000-0000-000000000009"
        rec_path.write_text(json.dumps(rec))
        live = [listed("22222222-0000-0000-0000-000000000009", "ADV"), listed(self.IT, "IT Orchestrator")]
        self.assertEqual(mw.route("advisor", live, root)["session_id"], "22222222-0000-0000-0000-000000000009")
        self.assertEqual(mw.route("advisor", [listed(self.IT, "IT Orchestrator")], root)["status"], "UNRESOLVED")      # unreachable reads as unreachable


SID2 = "99999999-aaaa-bbbb-cccc-dddddddddddd"


def listed(sid, name, pid=None, status="idle", kind="background"):
    return {"sessionId": sid, "name": name, "pid": os.getpid() if pid is None else pid, "status": status, "kind": kind}


class Continuity20261118(unittest.TestCase):
    """The defects of 2026-11-18 (OOM of the desktop service): a dead session still LISTED, two hosts, an alias that follows a display name, a revival that renames the session, a substitute that nobody
    authorised, and work accepted by message that no record listed. Fixtures: they do not show the real runtime; the scratch-session demonstration (governance/design_records/wakeup_continuity_20261118.md) does."""

    def tearDown(self):
        getattr(self, "e", None) and self.e.close()

    def env(self, *a, **k):
        self.e = Env(*a, **k)
        return self.e

    def test_a_listed_session_without_a_running_process_is_not_live(self):
        """Measured with a scratch session: after `claude stop` and after a kill, `claude agents --json` still listed it, with no pid and no status."""
        self.assertTrue(mw.session_is_live({"pid": os.getpid()}))
        self.assertFalse(mw.session_is_live({"pid": None, "state": "working"}))
        self.assertFalse(mw.session_is_live({"name": "x"}))
        self.assertFalse(mw.session_is_live({"pid": 2 ** 22 + 12345}))                 # no such process
        raw = json.dumps([{"sessionId": SID, "name": "DEAD", "state": "working"}, {"sessionId": SID2, "name": "ALIVE", "pid": os.getpid(), "status": "idle"}])
        with mock.patch.object(mw.subprocess, "run", return_value=SimpleNamespace(stdout=raw, returncode=0)):
            self.assertEqual([x["name"] for x in mw.list_sessions()], ["ALIVE"])

    def test_a_dead_but_listed_bound_session_is_revived_not_called_alive(self):
        e = self.env(record())
        before = e.check([{"sessionId": SID, "name": "H", "state": "working"}], deliver="none")      # the old reading of the listing: this entry would count as a session
        self.assertEqual(before["state"], "STOPPED_RESUMABLE")                      # the check itself reads only what it is given: the filter is in list_sessions
        with mock.patch.object(mw, "list_sessions", return_value=[]):
            out = e.check(mw._SESSIONS_UNSET, deliver="resume", runner=lambda cmd, cwd=None: SimpleNamespace(returncode=0, stdout="ok", stderr=""))
        self.assertEqual((out["action"], out["delivery"]), ("RESUME", "sent"))

    def test_two_live_sessions_that_carry_the_marker_are_a_duplicate_host_and_nothing_is_resumed(self):
        e = self.env(record())
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        out = e.check([listed(SID, "ADV"), listed(SID2, "ADV chat")], deliver="resume")
        self.assertEqual((out["state"], out["action"]), ("DUPLICATE_HOST", "NONE"))
        self.assertEqual(len(out["live_bound_sessions"]), 2)
        self.assertIn("MANDATE_RELEASED", out["why"])

    def test_two_sessions_that_only_share_a_name_are_not_a_duplicate_host(self):
        """The legitimate case seen on 2026-11-18: the bound session and an operator chat that investigated both answered to 'ADV'. Only the marker makes a host."""
        e = self.env(record(), age_minutes=1)
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "an investigation, unbound"}]}}) + "\n")
        out = e.check([listed(SID, "ADV", status="busy"), listed(SID2, "ADV")], deliver="resume")
        self.assertEqual((out["state"], out["action"]), ("RUNNING", "NONE"))
        self.assertNotIn("live_bound_sessions", out)

    def test_the_record_binding_chooses_the_host_among_live_bound_sessions_and_the_rest_are_named(self):
        e = self.env(record())
        rec = record(); rec["SESSION_BINDING"] = {"session_id": SID2}
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        out = e.check([listed(SID, "one"), listed(SID2, "two")], deliver="none")
        self.assertEqual(out["state"], "DUPLICATE_HOST")
        self.assertEqual(out["session"], SID2)                                       # the record's binding is the one the answer names as the host

    def test_route_prefers_a_whole_name_and_the_record_binding_over_token_matches(self):
        root = Path(tempfile.mkdtemp())
        rec = record(); rec.update(TASK_ID="ADV-TASK", SESSION_NAME="ADV — Strategic Advisor", SESSION_BINDING={"session_id": SID})
        (root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        (root / "ledger" / "tasks" / "orchestrator" / "ADV-TASK.json").write_text(json.dumps(rec))
        live = [listed(SID, "ADV"), listed(SID2, "ORCH-ADV-FOLLOWTHROUGH-20261114"), listed("33333333-4444-5555-6666-777777777777", "HE-PROBE")]
        res = mw.route("ADV", live, root)
        self.assertEqual((res["status"], res["session_id"]), ("RESOLVED", SID))
        self.assertEqual([c["session_id"] for c in res["surplus_name_matches"]], [SID2])
        self.assertEqual(mw.route("HE", live, root)["session_id"], "33333333-4444-5555-6666-777777777777")      # the only 'HE' token match here, listed as such
        live2 = [listed(SID, "something else"), listed(SID2, "ADV")]                # the bound session was renamed, another session took the name
        res2 = mw.route("ADV", live2, root)
        self.assertEqual((res2["status"], res2["session_id"]), ("RESOLVED", SID))   # identity follows the binding, not the name
        self.assertTrue(res2["surplus_name_matches"])

    def test_a_role_alias_follows_the_marker_of_its_record_after_a_rename(self):
        e = self.env(record())
        rec = record(); rec["SESSION_NAME"] = "SCI — Scientist"
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        with mock.patch.object(mw, "transcript_for_session", lambda sid, pd=None: e.tr if sid == SID else None):
            res = mw.route("SCI", [listed(SID, "orch-adv004-mandate-reconciliation")], e.root)
        self.assertEqual((res["status"], res["session_id"]), ("RESOLVED", SID))

    def test_a_revival_never_passes_a_flag_to_a_session_that_has_saved_options(self):
        """Measured: a flag on a background session with saved options starts a COPY under a new id; without flags the same command continues the session itself."""
        e = self.env(record())
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "custom-title", "customTitle": "SCI"}) + "\n")
        jobs = Path(e.tmp.name) / "jobs"
        (jobs / SID[:8]).mkdir(parents=True)
        (jobs / SID[:8] / "state.json").write_text("{}")
        os.environ["LEGEND_CLAUDE_JOBS"] = str(jobs)
        self.addCleanup(os.environ.pop, "LEGEND_CLAUDE_JOBS", None)
        seen = {}
        out = e.check([], deliver="resume", runner=lambda cmd, cwd=None: (seen.update(cmd=cmd), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1])
        self.assertEqual(out["delivery"], "sent")
        self.assertNotIn("--name", seen["cmd"])
        self.assertEqual(seen["cmd"][1:4], ["--bg", "--resume", SID])

    def test_the_revival_passes_the_chosen_name_and_the_recall_clause_and_never_a_second_recall(self):
        e = self.env(record())
        os.environ["LEGEND_CLAUDE_JOBS"] = str(Path(e.tmp.name) / "no_jobs")                  # an interactive session: no saved options, the chosen name is passed
        self.addCleanup(os.environ.pop, "LEGEND_CLAUDE_JOBS", None)
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "custom-title", "customTitle": "SCI"}) + "\n")
        rec = record(); rec["RECALL"] = {"mark": "Proactive Strategic Advisor pilot, hourly mechanical check", "command": "strategic_advisor.py recall --campaign X", "renew_days": 6}
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        seen = {}
        def runner(cmd, cwd=None):
            seen["cmd"] = cmd
            return SimpleNamespace(returncode=0, stdout="ok", stderr="")
        out = e.check([], deliver="resume", runner=runner)
        self.assertEqual(out["delivery"], "sent")
        cmd = seen["cmd"]
        self.assertEqual(cmd[cmd.index("--name") + 1], "SCI")                          # a revived session keeps the name the operator gave it
        text = cmd[-1]
        self.assertIn("call CronList", text)
        self.assertIn("do NOT create another", text)
        self.assertIn("before day 6", text)
        self.assertEqual(mw.recall_clause(None), "")                                  # a mandate without a recall field gets no recall sentence

    def test_revival_gets_the_current_repo_guidance_not_the_previous_chat(self):
        e = self.env(record())
        path = e.root / mw.mc.GUIDANCE_PATH
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("<!-- OPERATOR_ROADMAP:BEGIN -->\n" + mw.mc.GUIDANCE_BEGIN
                        + "\nClosed increment: select the next useful question. Why: research continuity.\n"
                        + mw.mc.GUIDANCE_END + "\n<!-- OPERATOR_ROADMAP:END -->\nSuperseded: wait for the operator.")
        calls = []
        runner = lambda c, cwd=None: (calls.append(c), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1]
        e.check([], deliver="resume", runner=runner)
        self.assertEqual(len(calls), 1)
        self.assertIn("Why: research continuity", calls[0][-1])
        self.assertNotIn("Superseded: wait", calls[0][-1])

    def test_a_session_that_died_again_after_its_revival_is_revived_again_but_not_while_it_may_still_be_starting(self):
        e = self.env(record())
        calls = []
        run = lambda c, cwd=None: (calls.append(c), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1]
        e.check([], deliver="resume", runner=run)
        mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[], now=NOW + 5 * 60, deliver="resume", runner=run)     # five minutes later: the revival may still be starting
        self.assertEqual(len(calls), 1)
        later = mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[], now=NOW + 40 * 60, deliver="resume", runner=run)
        self.assertEqual((later["action"], later["delivery"]), ("RESUME", "sent"))          # forty minutes later and still not live: it died again, ask again
        self.assertEqual(len(calls), 2)
        live = mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[listed(SID, "H")], now=NOW + 80 * 60, deliver="resume", runner=run)
        self.assertEqual(len(calls), 2)                                                      # a live session that was asked is left alone for the long window

    def test_rebind_needs_an_explicit_authorisation_a_single_live_target_and_no_second_host(self):
        e = self.env(record())
        live = [listed(SID, "ADV", status="idle"), listed(SID2, "substitute")]
        with self.assertRaises(PermissionError):
            mw.rebind(TASK, SID2, "", root=e.root, sessions=live, projects_dir=e.proj)                          # no pointer: nothing happens
        with self.assertRaises(PermissionError) as c:
            mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=live, projects_dir=e.proj)   # SID still carries the marker and is live
        self.assertIn("exactly one host", str(c.exception))
        with self.assertRaises(ValueError):
            mw.rebind(TASK, "nobody", "operator message 2026-11-18 20:10Z", root=e.root, sessions=live, projects_dir=e.proj)
        out = mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=[listed(SID2, "substitute")], projects_dir=e.proj)   # the old host is gone
        self.assertEqual(out["session_id"], SID2)
        saved = json.loads((e.root / out["record"]).read_text())
        self.assertEqual(saved["SESSION_BINDING"]["session_id"], SID2)
        self.assertEqual(saved["SESSION_BINDING"]["authorised_by"], "operator message 2026-11-18 20:10Z")
        self.assertFalse(out["marker_present"])                                       # the substitute has not yet written its own marker line
        ev = mw.state_dir() / mw.EVENTS_FILE
        self.assertIn('"kind": "rebind"', ev.read_text())

    def test_rebind_never_reopens_an_operator_stop(self):
        e = self.env(record(state="PAUSED"))
        with self.assertRaises(PermissionError):
            mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=[listed(SID2, "substitute")], projects_dir=e.proj)


class MemoryContainment(unittest.TestCase):
    """The opt-in memory scope of `job run` and the read-only `resources` view. The real-kernel
    proof (a capped job OOM-killed alone while the desktop service stays untouched) is recorded in
    governance/design_records/wakeup_continuity_20261118.md; these are fixtures."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = str(Path(self.tmp.name) / "state")
        self.bin = Path(self.tmp.name) / "bin"
        self.bin.mkdir()
        fake = self.bin / "systemd-run"                       # records its arguments, then runs the command after `--`
        fake.write_text('#!/bin/sh\necho "$@" > "%s/args"\nwhile [ "$1" != "--" ]; do shift; done\nshift\nexec "$@"\n' % self.tmp.name)
        fake.chmod(0o755)

    def tearDown(self):
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)
        self.tmp.cleanup()

    def test_value_is_validated_and_a_missing_systemd_run_never_means_uncapped(self):
        for bad in ("3GB", "0", "", "-1G", "3 G", "G"):
            with self.assertRaises(ValueError, msg=bad):
                mw.memory_scope(["true"], bad)
        with mock.patch.object(mw.shutil, "which", return_value=None):
            with self.assertRaises(RuntimeError):
                mw.memory_scope(["true"], "3G")
            with self.assertRaises(RuntimeError):
                mw.job_run("T", "l", ["true"], memory_max="3G")
        self.assertFalse((mw.jobs_dir("T")).exists())            # nothing was started

    def test_wrapped_command_carries_the_cap_and_the_user_scope(self):
        with mock.patch.object(mw.shutil, "which", return_value="/usr/bin/systemd-run"):
            cmd = mw.memory_scope(["python3", "x.py"], "2.5G")
        self.assertEqual(cmd[1:6], ["--user", "--scope", "--quiet", "-p", "MemoryMax=2.5G"])
        self.assertEqual(cmd[-3:], ["--", "python3", "x.py"])

    def test_job_run_with_cap_runs_the_command_inside_the_wrapper_and_records_the_cap(self):
        with mock.patch.object(mw.shutil, "which", return_value=str(self.bin / "systemd-run")):
            j = mw.job_run("T", "capped", ["sh", "-c", "echo hello"], memory_max="1G")
        self.assertTrue(j["started"])
        self.assertEqual(j["memory_max"], "1G")
        self.assertEqual(j["cmd"], ["sh", "-c", "echo hello"])      # the caller's command is what is recorded
        for _ in range(100):
            if Path(j["exit_file"]).exists():
                break
            time.sleep(0.05)
        self.assertEqual(Path(j["exit_file"]).read_text().strip(), "0")
        self.assertIn("hello", Path(j["log"]).read_text())
        self.assertIn("MemoryMax=1G", (Path(self.tmp.name) / "args").read_text())

    def test_job_run_without_cap_is_unchanged(self):
        j = mw.job_run("T", "plain", ["true"])
        self.assertNotIn("memory_max", j)
        self.assertFalse((Path(self.tmp.name) / "args").exists())
        for _ in range(100):                                          # the detached job writes its exit file after this body returns:
            if Path(j["exit_file"]).exists():                         # wait for it, or the temp-dir teardown races it ('Directory not empty', CI 2026-11-19)
                break
            time.sleep(0.05)

    def _fake_proc(self):
        proc = Path(self.tmp.name) / "proc"
        (proc / "pressure").mkdir(parents=True)
        (proc / "meminfo").write_text("MemTotal: 16000000 kB\nMemAvailable: 8000000 kB\nSwapTotal: 0 kB\nSwapFree: 0 kB\n")
        (proc / "pressure" / "memory").write_text("some avg10=1.50 avg60=0.00 avg300=0.00 total=5\nfull avg10=0.25 avg60=0.00 avg300=0.00 total=3\n")
        (proc / "loadavg").write_text("2.50 1.00 0.50 1/100 1234\n")
        for pid, cg, rss, comm in ((10, "/system.slice/a.service", 2048, "big"), (11, "/system.slice/a.service", 1024, "small"),
                                   (12, "/user.slice/b.scope", 512, "other")):
            d = proc / str(pid)
            d.mkdir()
            (d / "cgroup").write_text(f"0::{cg}\n")
            (d / "status").write_text(f"Name:\t{comm}\nVmRSS:\t{rss} kB\n")
            (d / "comm").write_text(comm + "\n")
            if pid != 12:                                              # pid 12 has no smaps_rollup: PSS falls back to RSS, never to zero
                (d / "smaps_rollup").write_text(f"Rss: {rss} kB\nPss: {rss // 2} kB\n")
        (proc / "self").mkdir()                                     # non-numeric entries are ignored
        return proc

    def test_resources_groups_by_cgroup_and_reports_pressure_without_thresholds(self):
        proc = self._fake_proc()
        out = mw.resource_state(str(proc), top=5, jobs_base=Path(self.tmp.name) / "none",
                                sessions=[{"name": "X", "sessionId": "abcdef12-0000", "pid": 12}, {"name": "Y", "sessionId": "ff", "pid": 999}])
        self.assertEqual((out["mem_total_mb"], out["mem_available_mb"], out["swap_total_mb"]), (15625, 7812, 0))
        self.assertEqual(out["pressure"]["some"]["avg10"], "1.50")
        self.assertEqual(out["load1"], "2.50")
        self.assertEqual(out["groups"][0]["pss_mb"], 1)                               # (2048 + 1024) / 2 kB, shared pages split
        top = out["groups"][0]
        self.assertEqual((top["cgroup"], top["rss_mb"], top["procs"], top["largest"]["comm"]), ("/system.slice/a.service", 3, 2, "big"))
        self.assertEqual([s["cgroup"] for s in out["sessions"]], ["b.scope", "?"])   # a vanished pid is "?", not an error
        self.assertNotIn("verdict", out)
        self.assertNotIn("allowed", out)                                          # facts only

    def test_resources_lists_live_jobs_with_their_caps(self):
        with mock.patch.object(mw.shutil, "which", return_value=str(self.bin / "systemd-run")):
            j = mw.job_run("T", "sleeper", ["sleep", "30"], memory_max="1G")
        try:
            out = mw.resource_state(str(self._fake_proc()), jobs_base=mw.state_dir() / "jobs")
            self.assertEqual([(x["label"], x["memory_max"]) for x in out["alive_jobs"]], [("sleeper", "1G")])
        finally:
            try:
                os.killpg(j["pid"], 15)
            except OSError:
                pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
