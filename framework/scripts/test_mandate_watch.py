#!/usr/bin/env python3
"""Regressions for mandate_watch.py: the hourly continuity control.
Run: python3 -B framework/scripts/test_mandate_watch.py -v"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import time
import unittest
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
