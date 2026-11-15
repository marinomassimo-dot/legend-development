#!/usr/bin/env python3
"""One known window of trial_window_table.py against hand counts, on a fixture repository (no real transcript is read)."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import trial_window_table as tw  # noqa: E402

tw.sa._agents = lambda: None            # never ask the real runtime for its session list
SINCE, UNTIL = "2026-11-14T15:29:29Z", "2026-11-15T15:29:29Z"
CAMPAIGN = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113"


def turn(mid: str, at: str, out: int, cw: int, cr: int) -> dict:
    return {"type": "assistant", "timestamp": at, "uuid": mid + "-u", "message": {"id": mid, "model": "m", "usage": {"input_tokens": 1, "output_tokens": out, "cache_creation_input_tokens": cw, "cache_read_input_tokens": cr}}}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def jsonl(rows: list[dict]) -> str:
    return "\n".join(json.dumps(r) for r in rows) + "\n"


class KnownWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = Path(tempfile.mkdtemp(prefix="twt_"))
        r = cls.root = cls.tmp / "repo"
        r.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=r, check=True)
        subprocess.run(["git", "config", "user.email", "t" + chr(64) + "example.org"], cwd=r, check=True)
        subprocess.run(["git", "config", "user.name", "t"], cwd=r, check=True)

        def commit(when: str, files: dict[str, str]) -> None:
            for name, text in files.items():
                write(r / name, text)
            subprocess.run(["git", "add", "-A"], cwd=r, check=True)
            env = {**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
            subprocess.run(["git", "commit", "-q", "-m", "c"], cwd=r, check=True, env=env)

        rec = json.dumps({"TASK_ID": "T-1", "CURRENT_STATE": "COMPLETE"})
        commit("2026-11-14T10:00:00+00:00", {"ledger/tasks/plan/T-0.json": rec, f"{CAMPAIGN}/assignments/PRESIDIO-003.md": "# PRESIDIO-003 (presidio)\n"})         # before the window
        commit("2026-11-14T17:00:00+01:00", {"ledger/tasks/plan/T-1.json": rec, f"{CAMPAIGN}/assignments/PRESIDIO-001.md": "# PRESIDIO-001 (OPERATOR-DIRECTED, 2026-11-15)\n"})   # 16:00Z, inside
        commit("2026-11-15T10:00:00+00:00", {"ledger/tasks/plan/T-2.json": rec, f"{CAMPAIGN}/assignments/PRESIDIO-002.md": "# PRESIDIO-002 (presidio decision)\n"})         # inside
        commit("2026-11-16T00:00:00+00:00", {"ledger/tasks/plan/T-3.json": rec})                                                                                              # after
        write(r / CAMPAIGN / "assignments.jsonl", jsonl([
            {"id": "ADV-001", "state": "DRAFTED", "utc": "2026-11-14T16:00:00Z"}, {"id": "ADV-001", "state": "SENT", "utc": "2026-11-14T16:05:00Z"},
            {"id": "ADV-002", "state": "DRAFTED", "utc": "2026-11-15T09:00:00Z"}, {"id": "ADV-003", "state": "DRAFTED", "utc": "2026-11-13T09:00:00Z"}]))
        write(r / tw.RECEIPTS, jsonl([{"event_at": "2026-11-14T16:00:00Z", "record_kind": "a"}, {"event_at": "2026-11-15T09:00:00Z", "record_kind": "a"}, {"event_at": "2026-11-13T09:00:00Z", "record_kind": "a"}]))
        census = {"turns": 2, "totals": {"output": 10, "cache_creation": 20, "cache_read": 30}}
        write(r / CAMPAIGN / "P1/meta.json", json.dumps({"started_utc": "2026-11-14T20:00:00Z", "capture": {"source_session_id": "sidP1"}, "tool_calls": [1] * 9, "runtime_readback": {"census": census, "refusal_fallbacks": []}}))
        write(r / CAMPAIGN / "P2/meta.json", json.dumps({"started_utc": "2026-11-15T01:00:00Z", "capture": {}, "tool_calls": [1] * 2, "runtime_readback": {"census": census, "refusal_fallbacks": [{"x": 1}]}}))
        write(r / CAMPAIGN / "holds.jsonl", jsonl([{"utc": "2026-11-14T10:00:00Z", "reason": "before"}, {"utc": "2026-11-15T12:00:00Z", "reason": "inside"}, {"utc": "2026-11-16T01:00:00Z", "reason": "after"}]))   # HE64
        write(r / CAMPAIGN / "P0/meta.json", json.dumps({"started_utc": "2026-11-13T01:00:00Z", "runtime_readback": {"census": census}}))
        pr = cls.projects = cls.tmp / "projects" / "-home-desktop-legend-development"
        write(pr / "sid1.jsonl", jsonl([turn("m3", "2026-11-14T10:00:00Z", 999, 9, 9), turn("m1", "2026-11-14T16:00:00Z", 100, 10, 1000), turn("m2", "2026-11-15T10:00:00Z", 50, 5, 2000),
                                       turn("m2", "2026-11-15T10:00:00Z", 50, 5, 2000), turn("m4", "2026-11-16T00:00:00Z", 999, 9, 9)]))
        write(pr / "sid1" / "custom-title.json", json.dumps({"customTitle": "IT"}))
        write(pr / "sid1" / "subagents" / "agent-a.jsonl", jsonl([turn("s1", "2026-11-15T11:00:00Z", 7, 1, 70)]))
        write(pr / "sidP1.jsonl", jsonl([turn("p1", "2026-11-14T20:01:00Z", 10, 20, 30)]))
        write(pr / "sid2.jsonl", jsonl([turn("z", "2026-11-10T00:00:00Z", 5, 5, 5)]))                    # no turn in the window: absent

    def table(self) -> tuple[list[dict], list[dict], dict]:
        c = self.root / CAMPAIGN
        tw.CAMPAIGN_ROOT = c
        return tw.sessions(self.projects.parent, SINCE, UNTIL), tw.evaluations(self.root, c, SINCE, UNTIL), tw.counts(self.root, "main", c, SINCE, UNTIL)

    def test_sessions_by_hand(self) -> None:
        sess, _, _ = self.table()
        by = {s["session"]: s for s in sess}
        self.assertEqual(set(by), {"IT", "Advisor evaluation P1"})                                          # sid2 had no turn in the window
        it = by["IT"]
        self.assertEqual((it["turns"], it["output"], it["cache_written"], it["cache_read"]), (2, 150, 15, 3000))   # m3 and m4 are outside; the repeated m2 row counts once
        self.assertEqual((it["subagent_runs"], it["sub_turns"], it["sub_output"], it["sub_cache_read"]), (1, 1, 7, 70))

    def test_evaluations_by_hand(self) -> None:
        _, ev, _ = self.table()
        self.assertEqual([(e["evaluation"], e["state"], e["output"]) for e in ev], [("P1", "complete", 10), ("P2", "incomplete", 10)])   # P0 is before the window

    def test_a_hold_is_counted_on_its_own_line_and_never_as_an_evaluation(self) -> None:
        _, ev, c = self.table()
        self.assertEqual(c["holds_recorded"], 1)                                                                    # only the one inside the window
        self.assertEqual([e["evaluation"] for e in ev], ["P1", "P2"])                                                 # evaluations read P<n>/meta.json; holds.jsonl never enters

    def test_counts_by_hand(self) -> None:
        _, _, c = self.table()
        self.assertEqual((c["commits"], c["merge_commits"], c["task_records_created"]), (2, 0, 2))                  # the +01:00 commit is 16:00Z, inside
        self.assertEqual(sum(c["task_final_states"].values()), 2)
        self.assertEqual(c["assignment_events_by_state"], {"DRAFTED": 2, "SENT": 1})
        self.assertEqual(c["assignment_ids_by_latest_state"], {"SENT": 1, "DRAFTED": 1})
        self.assertEqual((c["operator_directed"], c["presidio_decided"]), (["PRESIDIO-001"], ["PRESIDIO-002"]))     # PRESIDIO-003 predates the window
        self.assertEqual((c["receipts_appended"], c["receipts_by_record_kind"]), (2, {"a": 2}))

    def test_the_command_line_runs_and_is_read_only(self) -> None:
        before = subprocess.run(["git", "status", "--porcelain"], cwd=self.root, capture_output=True, text=True).stdout
        tw.sa._agents = lambda: None
        out = subprocess.run([sys.executable, "-I", str(Path(tw.__file__)), "--root", str(self.root), "--projects", str(self.projects.parent), "--since", SINCE, "--until", UNTIL], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("commits\t2", out.stdout)
        self.assertEqual(subprocess.run(["git", "status", "--porcelain"], cwd=self.root, capture_output=True, text=True).stdout, before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
