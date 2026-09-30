#!/usr/bin/env python3
"""The mandate record, not the chat, decides whether an Orchestrator turn may end.

Expected actions were fixed before the code ran (cross_session_transport.md §12 acceptance
scenarios): a finished wave with steps left → CONTINUE; every step blocked with a named
impediment → stop allowed, mandate INCOMPLETE; every step DONE with evidence → stop allowed,
COMPLETE pending; MANDATE_STATE PAUSED/COMPLETE → released; a session with no marker → never
touched; a bound session → blocked with the next step, bounded so it cannot be trapped; any
malformed input → allowed (fail open). None of this measures live model obedience.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mandate_continuity as mc  # noqa: E402

ROOT = HERE.parents[1]


def queue(steps_by_obj: dict[str, list], state: str | None = None) -> dict:
    q = {"_note": "fixture"}
    if state:
        q["MANDATE_STATE"] = state
    for i, (name, steps) in enumerate(steps_by_obj.items(), 1):
        q[name] = {"order": i, "steps": steps}
    return q


def record(q: dict, task: str = "T-1") -> dict:
    return {"TASK_ID": task, "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_20260914": q}


class Verdicts(unittest.TestCase):
    def test_finished_wave_with_unread_papers_continues(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [
            {"step": "wave 1", "status": "DONE", "evidence": "commit abc"},
            {"step": "read PMID 1", "status": "TODO"}]})))
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertFalse(v["stop_allowed"])
        self.assertEqual(v["next"]["step"], "read PMID 1")

    def test_in_progress_step_is_the_next_one(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [
            {"step": "a", "status": "TODO"}, {"step": "b", "status": "IN_PROGRESS"}]})))
        self.assertEqual(v["next"]["step"], "b")

    def test_objective_order_not_key_order(self) -> None:
        q = {"OBJ_Z": {"order": 1, "steps": [{"step": "first", "status": "TODO"}]},
             "OBJ_A": {"order": 2, "steps": [{"step": "second", "status": "TODO"}]}}
        self.assertEqual(mc.verdict(record(q))["next"]["step"], "first")

    def test_string_steps_are_unreconciled_todo(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": ["propagate batch", "phase 5 LINT"]})))
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertEqual(v["unreconciled"], 2)

    def test_all_blocked_with_named_blockers_allows_stop_incomplete(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [
            {"step": "R4 on entries[19]", "status": "BLOCKED", "blocker": "0/6 artefacts",
             "unblock": "re-acquisition"},
            {"step": "done one", "status": "DONE", "evidence": "x"}]})))
        self.assertEqual(v["verdict"], "ALL_BLOCKED")
        self.assertTrue(v["stop_allowed"])
        self.assertEqual(v["blockers"][0]["unblock"], "re-acquisition")

    def test_blocked_without_blocker_is_not_a_block(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "BLOCKED"}]})))
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertIn("BLOCKED without a named blocker", v["findings"][0])

    def test_all_done_with_evidence_is_complete_pending(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "c1"}]})))
        self.assertEqual(v["verdict"], "COMPLETE_PENDING")
        self.assertTrue(v["stop_allowed"])

    # ---- Codex review of the second version, 2026-09-14: five ways a declaration could
    # still end the turn while the record contradicted it.
    def test_done_without_evidence_holds_the_session_for_the_pointer_not_the_work(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE"},
                                               {"step": "y", "status": "DONE", "evidence": "c2"}]})))
        self.assertEqual(v["verdict"], "EVIDENCE_PENDING")
        self.assertFalse(v["stop_allowed"])
        self.assertIn("DONE without evidence", v["findings"][0])
        self.assertEqual([u["step"] for u in v["unevidenced"]], ["x"])
        self.assertIn("do not redo the work", v["message"])
        self.assertIn("evidence needed: OBJ_1[0] x", mc.render(v))
        # with executable steps still present the verdict stays CONTINUE and the finding rides along
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE"}, {"step": "y", "status": "TODO"}]})))
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertIn("DONE without evidence", v["findings"][0])

    def test_pause_and_cancel_release_against_any_state_but_complete_must_be_consistent(self) -> None:
        for state in ("PAUSED", "CANCELLED"):
            v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}, state)))
            self.assertEqual(v["verdict"], "RELEASED", state)
        for steps in ([{"step": "x", "status": "TODO"}], [{"step": "x", "status": "DONE"}]):
            v = mc.verdict(record(queue({"OBJ_1": steps}, "COMPLETE")))
            self.assertEqual(v["verdict"], "INCONSISTENT_COMPLETE", steps)
            self.assertFalse(v["stop_allowed"])
        # A BLOCKED step contradicts COMPLETE as much as a TODO one: §12's table keeps a
        # mandate with a demonstrable impediment INCOMPLETE (found by plan, 2026-09-17).
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "BLOCKED", "blocker": "b"}]}, "COMPLETE")))
        self.assertEqual(v["verdict"], "INCONSISTENT_COMPLETE")
        self.assertIn("1 BLOCKED", v["message"])
        for state in ("PAUSED", "CANCELLED"):
            v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "BLOCKED", "blocker": "b"}]}, state)))
            self.assertEqual(v["verdict"], "RELEASED", state)
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "e"}]}, "COMPLETE")))
        self.assertEqual(v["verdict"], "RELEASED")

    def test_an_objective_without_steps_is_malformed_not_empty(self) -> None:
        q = {"OBJ_1": {"order": 1}, "OBJ_2": {"order": 2, "steps": [{"step": "y", "status": "DONE", "evidence": "e"}]}}
        v = mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": q})
        self.assertEqual(v["verdict"], "MALFORMED")
        self.assertIn("OBJ_1 has no `steps`", v["message"])
        q["OBJ_1"]["steps"] = []                                  # deliberately empty is fine
        self.assertEqual(mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": q})["verdict"], "COMPLETE_PENDING")

    def test_every_open_queue_binds_key_order_extinguishes_nothing(self) -> None:
        r = {"TASK_ID": "T",
             "AUTHORISED_QUEUE_20260913": queue({"OBJ_1": [{"step": "old pending", "status": "TODO"}]}),
             "AUTHORISED_QUEUE_20260914": queue({"OBJ_1": [{"step": "new", "status": "DONE", "evidence": "e"}]})}
        v = mc.verdict(r)
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertEqual(v["next"]["objective"], "AUTHORISED_QUEUE_20260913/OBJ_1")
        self.assertEqual(v["queue_key"], ["AUTHORISED_QUEUE_20260913", "AUTHORISED_QUEUE_20260914"])
        r["AUTHORISED_QUEUE_20260913"]["MANDATE_STATE"] = "PAUSED"   # explicit replacement releases it
        self.assertEqual(mc.verdict(r)["verdict"], "COMPLETE_PENDING")

    def test_invalid_status_counts_todo_with_finding(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "MAYBE"}]})))
        self.assertEqual(v["verdict"], "CONTINUE")
        self.assertIn("invalid status", v["findings"][0])

    def test_no_queue_and_empty_queue(self) -> None:
        self.assertEqual(mc.verdict({"TASK_ID": "T"})["verdict"], "NO_QUEUE")
        self.assertEqual(mc.verdict(record(queue({})))["verdict"], "EMPTY")

    def test_last_queue_key_wins_among_released_but_an_open_queue_outranks_them(self) -> None:
        r = record(queue({"OBJ_1": [{"step": "old", "status": "TODO"}]}, "PAUSED"))
        r["AUTHORISED_QUEUE_20260915"] = queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "e"}]}, "COMPLETE")
        self.assertEqual(mc.verdict(r)["verdict"], "RELEASED")
        # Junior case 16: a dashed newer key sorts BEFORE an older undashed one; the older
        # COMPLETE queue must not release the newer open one.
        r = {"TASK_ID": "T", "AUTHORISED_QUEUE_20260901": queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "e"}]}, "COMPLETE"),
             "AUTHORISED_QUEUE_2026-09-15": queue({"OBJ_1": [{"step": "y", "status": "TODO"}]})}
        self.assertEqual(mc.verdict(r)["verdict"], "CONTINUE")

    # ---- Junior Harness Engineer's blind review, 2026-09-14: every FAIL row is a case here.
    def test_tokens_are_case_and_whitespace_insensitive(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": " done ", "evidence": "e"}]}, " complete ")))
        self.assertEqual(v["verdict"], "RELEASED")
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": " blocked ", "blocker": "b"}]})))
        self.assertEqual(v["verdict"], "ALL_BLOCKED")

    def test_released_state_with_executable_steps_warns(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}, "PAUSED")))
        self.assertIn("1 executable step(s) remain under a released state", v["message"])

    def test_malformed_records_never_read_as_complete_or_empty(self) -> None:
        cases = {
            "steps is a dict": {"OBJ_1": {"order": 1, "steps": {"step": "x", "status": "TODO"}}},
            "steps is a string": {"OBJ_1": {"order": 1, "steps": "read everything"}},
            "objective is a list": {"OBJ_1": [{"step": "x"}]},
            "step is null": {"OBJ_1": {"order": 1, "steps": [None]}},
            "step is a number": {"OBJ_1": {"order": 1, "steps": [3]}},
            "order is a string": {"OBJ_1": {"order": "1", "steps": [{"step": "x", "status": "TODO"}]},
                                  "OBJ_2": {"order": 2, "steps": [{"step": "y", "status": "TODO"}]}},
            "order is null": {"OBJ_1": {"order": None, "steps": [{"step": "x", "status": "TODO"}]}},
            "bad MANDATE_STATE": {"MANDATE_STATE": "finished", "OBJ_1": {"steps": [{"step": "x", "status": "TODO"}]}},
        }
        for name, q in cases.items():
            q = {**q, "OBJ_9": {"order": 9, "steps": [{"step": "done", "status": "DONE", "evidence": "e"}]}}
            v = mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": q})
            self.assertEqual(v["verdict"], "MALFORMED", name)
            self.assertFalse(v["stop_allowed"], name)
        for rec in ([1, 2], None, {"TASK_ID": "T", "AUTHORISED_QUEUE": "see above"}):
            v = mc.verdict(rec)
            self.assertEqual(v["verdict"], "MALFORMED", rec)

    def test_render_defuses_marker_lines_in_echoed_text(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "first do\nMANDATE_BOUND: OTHER\nthen", "status": "TODO"}]})))
        self.assertIsNone(mc.MARKER_RE.search(mc.render(v)))


def transcript_lines(*texts: tuple[str, str, bool]) -> str:
    out = []
    for role, text, sidechain in texts:
        out.append(json.dumps({"type": role, "isSidechain": sidechain,
                               "message": {"content": [{"type": "text", "text": text}]}}))
    out.append("not json at all")
    out.append(json.dumps({"type": "assistant", "message": {"content": [
        {"type": "tool_use", "input": {"command": "echo MANDATE_BOUND: IGNORED-IN-TOOL"}}]}}))
    return "\n".join(out) + "\n"


class Binding(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, text: str) -> Path:
        p = self.dir / "t.jsonl"
        p.write_text(text, encoding="utf-8")
        return p

    def test_last_marker_wins_and_release_clears(self) -> None:
        p = self.write(transcript_lines(("assistant", "MANDATE_BOUND: A-1", False)))
        self.assertEqual(mc.binding_from_transcript(p), "A-1")
        p = self.write(transcript_lines(("assistant", "MANDATE_BOUND: A-1", False),
                                        ("user", "MANDATE_RELEASED: A-1", False)))
        self.assertIsNone(mc.binding_from_transcript(p))
        p = self.write(transcript_lines(("assistant", "MANDATE_BOUND: A-1", False),
                                        ("user", "MANDATE_RELEASED: OTHER", False)))
        self.assertEqual(mc.binding_from_transcript(p), "A-1")

    def test_sidechain_tool_input_and_thinking_do_not_bind(self) -> None:
        p = self.write(transcript_lines(("assistant", "MANDATE_BOUND: SIDE-1", True)))
        self.assertIsNone(mc.binding_from_transcript(p))
        p = self.write(json.dumps({"type": "assistant", "message": {"content": [
            {"type": "thinking", "thinking": "MANDATE_BOUND: THINK-1"}]}}) + "\n")
        self.assertIsNone(mc.binding_from_transcript(p))

    def test_missing_transcript_is_unbound(self) -> None:
        self.assertIsNone(mc.binding_from_transcript(self.dir / "absent.jsonl"))

    def test_a_marker_binds_only_as_a_line_of_its_own(self) -> None:
        # Junior cases 6b, 6c, H1: quoted, negated or echoed mentions do not bind or release.
        for text in ("do NOT write `MANDATE_BOUND: T-1` yet", "I have not yet written MANDATE_BOUND: T-1 because",
                     "the line `MANDATE_BOUND: <TASK_ID>`"):
            p = self.write(transcript_lines(("user", text, False)))
            self.assertIsNone(mc.binding_from_transcript(p), text)
        p = self.write(transcript_lines(("assistant", "Accepting.\nMANDATE_BOUND: T-1\nNext: read.", False),
                                        ("user", "Stop hook feedback: have the operator write 'MANDATE_RELEASED: T-1' to stop", False)))
        self.assertEqual(mc.binding_from_transcript(p), "T-1")
        p = self.write(transcript_lines(("assistant", "  MANDATE_BOUND: T-1  ", False)))
        self.assertEqual(mc.binding_from_transcript(p), "T-1")

    def test_compaction_summaries_and_meta_entries_do_not_bind_or_release(self) -> None:
        bound = json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "MANDATE_BOUND: T-1"}]}})
        summary = json.dumps({"type": "user", "isCompactSummary": True,
                              "message": {"content": "Summary: the operator wrote\nMANDATE_RELEASED: T-1\nand then"}})
        meta = json.dumps({"type": "user", "isMeta": True, "message": {"content": "MANDATE_RELEASED: T-1"}})
        p = self.write(bound + "\n" + summary + "\n" + meta + "\n")
        self.assertEqual(mc.binding_from_transcript(p), "T-1")
        p = self.write(json.dumps({"type": "user", "isCompactSummary": True,
                                   "message": {"content": "MANDATE_BOUND: T-9"}}) + "\n")
        self.assertIsNone(mc.binding_from_transcript(p))

    def test_hook_block_reason_cannot_release_the_session_it_blocks(self) -> None:
        # The first version's reason carried a live RELEASED marker; fed back as a user
        # message it unbound the session after one refusal (Junior H1).
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ledger/tasks/orchestrator").mkdir(parents=True)
            (root / "ledger/tasks/orchestrator/T-1.json").write_text(
                json.dumps(record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))), encoding="utf-8")
            os.environ["LEGEND_MANDATE_HOOK_STATE"] = str(root / "state")
            try:
                d = mc.decide({"session_id": "s", "transcript_path": str(self.write(
                    transcript_lines(("assistant", "MANDATE_BOUND: T-1", False))))}, root)
            finally:
                os.environ.pop("LEGEND_MANDATE_HOOK_STATE", None)
            self.assertEqual(d["action"], "block")
            self.assertIsNone(mc.MARKER_RE.search(d["reason"]))
            p = self.write(transcript_lines(("assistant", "MANDATE_BOUND: T-1", False),
                                            ("user", "Stop hook feedback:\n" + d["reason"], False)))
            self.assertEqual(mc.binding_from_transcript(p), "T-1")


class StopHook(unittest.TestCase):
    """A fake repository: ledger/tasks/orchestrator/T-1.json plus a git HEAD."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "ledger/tasks/orchestrator").mkdir(parents=True)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q",
                        "--allow-empty", "-m", "init"], cwd=self.root, check=True)
        self.state = self.root / "hookstate"
        os.environ["LEGEND_MANDATE_HOOK_STATE"] = str(self.state)
        os.environ.pop(mc.DISABLE_ENV, None)
        self.transcript = self.root / "session.jsonl"
        self.transcript.write_text(transcript_lines(("assistant", "MANDATE_BOUND: T-1", False)))
        self.payload = {"session_id": "s-1", "transcript_path": str(self.transcript),
                        "cwd": str(self.root), "hook_event_name": "Stop", "stop_hook_active": False}

    def tearDown(self) -> None:
        os.environ.pop("LEGEND_MANDATE_HOOK_STATE", None)
        os.environ.pop(mc.DISABLE_ENV, None)
        self.tmp.cleanup()

    def put_record(self, q: dict) -> None:
        (self.root / "ledger/tasks/orchestrator/T-1.json").write_text(
            json.dumps(record(q)), encoding="utf-8")

    def run_hook(self) -> tuple[int, str, str]:
        return mc.stop_hook(json.dumps(self.payload), self.root)

    def test_bound_session_with_executable_work_is_blocked_with_next_step(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "propagate batch 005", "status": "TODO"}]}))
        code, out, err = self.run_hook()
        self.assertEqual(code, 0)
        decision = json.loads(out)
        self.assertEqual(decision["decision"], "block")
        self.assertIn("propagate batch 005", decision["reason"])
        self.assertIn("release line for this task", decision["reason"])
        self.assertIsNone(mc.MARKER_RE.search(decision["reason"]))

    def test_unbound_session_is_never_touched(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        self.transcript.write_text(transcript_lines(("assistant", "hello", False)))
        self.assertEqual(self.run_hook(), (0, "", ""))

    def test_released_paused_all_blocked_and_complete_allow(self) -> None:
        for q in (queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}, "PAUSED"),
                  queue({"OBJ_1": [{"step": "x", "status": "BLOCKED", "blocker": "bytes gone"}]}),
                  queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "c"}]})):
            self.put_record(q)
            code, out, err = self.run_hook()
            self.assertEqual((code, out), (0, ""), q)
            self.assertIn("MANDATE T-1", err)

    def test_missing_record_or_malformed_payload_fails_open(self) -> None:
        code, out, err = self.run_hook()          # bound to T-1, no record on disk
        self.assertEqual((code, out), (0, ""))
        self.assertIn("NO_RECORD", err)
        self.assertEqual(mc.stop_hook("{not json", self.root)[:2], (0, ""))
        self.assertEqual(mc.stop_hook("[]", self.root)[:2], (0, ""))
        (self.root / "ledger/tasks/orchestrator/T-1.json").write_text("{broken", encoding="utf-8")
        self.assertEqual(self.run_hook()[:2], (0, ""))

    def test_block_is_bounded_and_progress_resets_the_bound(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        for i in range(mc.MAX_CONSECUTIVE_BLOCKS):
            code, out, err = self.run_hook()
            self.assertIn(f"block {i + 1}/{mc.MAX_CONSECUTIVE_BLOCKS}", json.loads(out)["reason"], i)
        code, out, err = self.run_hook()
        self.assertEqual(out, "")
        self.assertIn("consecutive blocks", err)
        # progress on the record resets the count
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "IN_PROGRESS"}, {"step": "y", "status": "TODO"}]}))
        code, out, err = self.run_hook()
        self.assertIn("block 1/", json.loads(out)["reason"])
        # a commit alone does NOT reset it (Codex review: any commit, even unrelated, did)
        for _ in range(mc.MAX_CONSECUTIVE_BLOCKS):
            self.run_hook()
        self.assertEqual(self.run_hook()[1], "")
        subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q",
                        "--allow-empty", "-m", "progress"], cwd=self.root, check=True)
        self.assertEqual(self.run_hook()[1], "")
        # evidence written on a DONE step is progress
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "c9"}, {"step": "y", "status": "TODO"}]}))
        self.assertIn("block 1/", json.loads(self.run_hook()[1])["reason"])

    def test_absolute_ceiling_survives_progress_resets(self) -> None:
        # Progress resets the consecutive count; nothing resets the per-session total.
        blocks = 0
        for round_ in range(20):
            # a status flip is progress; step text alone is not part of the signature
            self.put_record(queue({"OBJ_1": [{"step": "s", "status": ("TODO", "IN_PROGRESS")[round_ % 2]}]}))
            out = self.run_hook()[1]
            if out:
                blocks += 1
                self.assertEqual(json.loads(out)["decision"], "block")
            else:
                break
        self.assertEqual(blocks, mc.MAX_TOTAL_BLOCKS)
        self.assertIn("absolute ceiling", self.run_hook()[2])

    def test_evidence_pending_and_inconsistent_complete_are_held_bounded(self) -> None:
        for q, needle in ((queue({"OBJ_1": [{"step": "x", "status": "DONE"}]}), "EVIDENCE_PENDING"),
                          (queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}, "COMPLETE"), "INCONSISTENT_COMPLETE")):
            self.payload["session_id"] = needle
            self.put_record(q)
            for _ in range(mc.MAX_CONSECUTIVE_BLOCKS):
                d = json.loads(self.run_hook()[1])
                self.assertEqual(d["decision"], "block")
                self.assertIn(needle, d["reason"])
            self.assertEqual(self.run_hook()[1], "")

    def test_logging_the_stop_in_the_record_does_not_reset_the_bound(self) -> None:
        # Junior case A1: a STOP_LOG line, a timestamp or reformatting is not progress.
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        p = self.root / "ledger/tasks/orchestrator/T-1.json"
        for i in range(mc.MAX_CONSECUTIVE_BLOCKS):
            self.assertIn("block", json.loads(self.run_hook()[1])["decision"], i)
            rec = json.loads(p.read_text())
            rec.setdefault("STOP_LOG", []).append({"reason_class": 3, "n": i})
            p.write_text(json.dumps(rec, indent=1))
        self.assertEqual(self.run_hook()[1], "")

    def test_unwritable_state_directory_allows_instead_of_blocking_forever(self) -> None:
        # Junior case 18: the count could not be persisted and the block was unbounded.
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        self.state.write_text("i am a file, not a directory")
        for _ in range(mc.MAX_CONSECUTIVE_BLOCKS + 3):
            code, out, err = self.run_hook()
            self.assertEqual(out, "")
            self.assertIn("cannot persist the block count", err)

    def test_malformed_record_blocks_bounded_not_silently_releases(self) -> None:
        # Junior cases 13, 16c, 42: a malformed record must not let a bound session go.
        (self.root / "ledger/tasks/orchestrator/T-1.json").write_text(
            json.dumps({"TASK_ID": "T-1", "AUTHORISED_QUEUE": {"OBJ_1": {"steps": {"step": "x"}}}}))
        for i in range(mc.MAX_CONSECUTIVE_BLOCKS):
            d = json.loads(self.run_hook()[1])
            self.assertEqual(d["decision"], "block")
            self.assertIn("MALFORMED", d["reason"])
        self.assertEqual(self.run_hook()[1], "")

    def test_duplicate_task_id_across_actors_is_ambiguous_not_released(self) -> None:
        # Junior case 38b: a stale COMPLETE copy under an earlier actor must not win.
        (self.root / "ledger/tasks/a-actor").mkdir()
        (self.root / "ledger/tasks/a-actor/T-1.json").write_text(
            json.dumps(record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": "e"}]}, "COMPLETE"))))
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        d = json.loads(self.run_hook()[1])
        self.assertEqual(d["decision"], "block")
        self.assertIn("ambiguous TASK_ID", d["reason"])   # never a silent winner
        (self.root / "ledger/tasks/b-actor").mkdir()
        (self.root / "ledger/tasks/b-actor/T-1.json").write_text(
            json.dumps(record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))))
        (self.root / "ledger/tasks/orchestrator/T-1.json").unlink()
        d = json.loads(self.run_hook()[1])
        self.assertIn("ambiguous TASK_ID", d["reason"])   # two non-orchestrator copies: MALFORMED, bounded

    def test_non_utf8_stdin_fails_open_through_the_cli(self) -> None:
        # Junior case 32b: the stdin read sat outside the try.
        r = subprocess.run([sys.executable, str(HERE / "mandate_continuity.py"), "stop-hook",
                            "--root", str(self.root)], input=b'{"transcript_path":"\xff\xfe"}',
                           capture_output=True, env={**os.environ, "LC_ALL": "en_US.UTF-8"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, b"")

    def test_d3_a_second_mandate_starts_with_its_own_block_count(self) -> None:
        # The signature hashed the queue SHAPE only, so a second record with an identical
        # shape inherited the first's spent count and was allowed on its first stop.
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        for _ in range(mc.MAX_CONSECUTIVE_BLOCKS):
            self.run_hook()
        self.assertEqual(self.run_hook()[1], "")
        (self.root / "ledger/tasks/orchestrator/T-2.json").write_text(
            json.dumps(record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}), "T-2")))
        self.transcript.write_text(transcript_lines(("assistant", "MANDATE_BOUND: T-2", False)))
        self.assertIn("block 1/", json.loads(self.run_hook()[1])["reason"])

    def test_q5_status_exit_code_says_whether_it_answered(self) -> None:
        script = HERE / "mandate_continuity.py"
        self.put_record(queue({}))                                   # EMPTY, but an answer
        r = subprocess.run([sys.executable, str(script), "status", "--task", "T-1",
                            "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual((r.returncode, "EMPTY" in r.stdout), (0, True), r.stdout)
        r = subprocess.run([sys.executable, str(script), "status", "--task", "ABSENT",
                            "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)

    def test_sessions_are_counted_separately(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        for _ in range(mc.MAX_CONSECUTIVE_BLOCKS):
            self.run_hook()
        self.payload["session_id"] = "s-2"
        self.assertIn("block 1/", json.loads(self.run_hook()[1])["reason"])

    def test_disable_switch(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        os.environ[mc.DISABLE_ENV] = "off"
        self.assertEqual(self.run_hook(), (0, "", ""))

    def test_cli_status_and_hook_entry_points(self) -> None:
        self.put_record(queue({"OBJ_1": [{"step": "x", "status": "TODO"}]}))
        script = HERE / "mandate_continuity.py"
        r = subprocess.run([sys.executable, str(script), "status", "--task", "T-1",
                            "--root", str(self.root), "--json"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout)["verdict"], "CONTINUE")
        r = subprocess.run([sys.executable, str(script), "stop-hook", "--root", str(self.root)],
                           input=json.dumps(self.payload), capture_output=True, text=True,
                           env={**os.environ, "LEGEND_MANDATE_HOOK_STATE": str(self.state)})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout)["decision"], "block")


class Wiring(unittest.TestCase):
    """The hook is installed in the project settings and reachable from the instructions."""

    HOOK_COMMAND = "python3 framework/scripts/mandate_continuity.py stop-hook"

    @staticmethod
    def _stop_commands(path: Path) -> list[str]:
        settings = json.loads(path.read_text(encoding="utf-8"))
        return [h["command"] for group in settings.get("hooks", {}).get("Stop", [])
                for h in group.get("hooks", [])]

    def test_deployment_snippet_carries_the_stop_hook(self) -> None:
        # The active .claude/settings.json is the operator's to write (harness self-modification
        # is refused to actors); the snippet is what they merge. Its command must be the script.
        self.assertIn(self.HOOK_COMMAND,
                      self._stop_commands(ROOT / "deployment/claude_settings_mandate_hook.json"))

    def test_active_settings_when_installed_run_the_same_command(self) -> None:
        active = ROOT / ".claude/settings.json"
        commands = self._stop_commands(active) if active.exists() else []
        if not commands:
            self.skipTest("Stop hook not installed in .claude/settings.json on this checkout")
        self.assertIn(self.HOOK_COMMAND, commands)

    def test_instruction_surfaces_name_the_command_and_the_marker(self) -> None:
        for relative in ("framework/protocols/cross_session_transport.md", "roles/orchestrator.md",
                         "CLAUDE.md", "framework/instruction/LEGEND_CORE.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("mandate_continuity.py", text, relative)
        proto = (ROOT / "framework/protocols/cross_session_transport.md").read_text(encoding="utf-8")
        self.assertIn("MANDATE_BOUND:", proto)
        self.assertIn("MANDATE_RELEASED:", proto)
        annex = (ROOT / "governance/annex_a_task_contract.md").read_text(encoding="utf-8")
        self.assertIn("AUTHORISED_QUEUE", annex)
        self.assertIn("MANDATE_STATE", annex)

    def test_the_live_orchestrator_record_parses_under_the_schema(self) -> None:
        live = ROOT / "ledger/tasks/orchestrator/ALDAZ-EXEC-20260913.json"
        if not live.exists():
            self.skipTest("no live record in this checkout")
        v = mc.verdict(json.loads(live.read_text(encoding="utf-8")))
        self.assertIn(v["verdict"], ("CONTINUE", "ALL_BLOCKED", "COMPLETE_PENDING", "RELEASED",
                                     "EVIDENCE_PENDING", "INCONSISTENT_COMPLETE"))
        # The record is the orchestrator's; converting its prose queue to statuses is that
        # actor's act (roles/orchestrator.md, step 1). Unreconciled strings still count TODO.


class Normalise(unittest.TestCase):
    def test_strings_become_todo_steps_and_state_defaults_open(self) -> None:
        r = record(queue({"OBJ_1": ["a", {"step": "b", "status": "DONE", "evidence": "e"}]}))
        changed = mc.normalise_record(r)
        self.assertTrue(changed)
        q = r["AUTHORISED_QUEUE_20260914"]
        self.assertEqual(q["MANDATE_STATE"], "OPEN")
        self.assertEqual(q["OBJ_1"]["steps"][0], {"step": "a", "status": "TODO"})
        self.assertEqual(q["OBJ_1"]["steps"][1]["status"], "DONE")
        self.assertFalse(mc.normalise_record(r), "idempotent")

    def test_cli_normalise_writes_only_with_flag(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ledger/tasks/orchestrator").mkdir(parents=True)
            p = root / "ledger/tasks/orchestrator/T-1.json"
            p.write_text(json.dumps(record(queue({"OBJ_1": ["a"]}))), encoding="utf-8")
            script = HERE / "mandate_continuity.py"
            r = subprocess.run([sys.executable, str(script), "normalise", "--task", "T-1",
                                "--root", str(root)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("would change", r.stdout)
            self.assertEqual(json.loads(p.read_text())["AUTHORISED_QUEUE_20260914"]["OBJ_1"]["steps"], ["a"])
            r = subprocess.run([sys.executable, str(script), "normalise", "--task", "T-1",
                                "--root", str(root), "--write"], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            steps = json.loads(p.read_text())["AUTHORISED_QUEUE_20260914"]["OBJ_1"]["steps"]
            self.assertEqual(steps, [{"step": "a", "status": "TODO"}])


class SecondBlindReview(unittest.TestCase):
    """The Junior Harness Engineer's second blind review, 2026-09-17. Three of its findings
    were a single JSON line away from buying a stop with pending work in the record."""

    def test_d1_a_complete_block_cannot_hide_behind_an_open_sibling(self) -> None:
        real = queue({"OBJ_1": [{"step": "todo step", "status": "TODO"}]}, "COMPLETE")
        for sibling in ({"MANDATE_STATE": "OPEN", "OBJ_1": {"order": 1, "steps": []}},
                        queue({"OBJ_1": [{"step": "done", "status": "DONE", "evidence": "c1"}]}),
                        {"MANDATE_STATE": "OPEN", "_note": "free text only"}):
            v = mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE_REAL": real,
                            "AUTHORISED_QUEUE_Z": sibling})
            self.assertEqual(v["verdict"], "INCONSISTENT_COMPLETE", sibling)
            self.assertFalse(v["stop_allowed"], sibling)
            self.assertIn("AUTHORISED_QUEUE_REAL", v["message"])

    def test_d2_objective_names_are_matched_like_every_other_token(self) -> None:
        v = mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": {"MANDATE_STATE": "OPEN",
                        " obj_1 ": {"order": 1, "steps": [{"step": "todo", "status": "TODO"}]}}})
        self.assertEqual(v["verdict"], "CONTINUE")
        for name in ("OBJECTIVE_1", "2_OBJ", "AUTHORISED_QUEUE_A/OBJ_1", "objective"):
            v = mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": {"MANDATE_STATE": "OPEN",
                            "OBJ_9": {"order": 9, "steps": [{"step": "d", "status": "DONE",
                                                             "evidence": "c1"}]},
                            name: {"order": 1, "steps": [{"step": "todo", "status": "TODO"}]}}})
            self.assertEqual(v["verdict"], "MALFORMED", name)
            self.assertIn("is not named OBJ_", v["message"])

    def test_d5_evidence_is_a_pointer_not_a_placeholder(self) -> None:
        # "done" and "x" are deliberately NOT refused: the set holds only the unambiguous
        # placeholders, because a false hold costs more than a rare weak pointer.
        for ev in ("null", "TBD", " pending ", "n/a", "-", True, False, 1, 0, [], None, "  "):
            v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": ev}]})))
            self.assertEqual(v["verdict"], "EVIDENCE_PENDING", repr(ev))
        for ev in ("commit da2b4c7", ["ledger/tasks/plan/x.json"], "FTR-20260913-36828035-03"):
            v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE", "evidence": ev}]})))
            self.assertEqual(v["verdict"], "COMPLETE_PENDING", repr(ev))

    def test_q1_an_unevidenced_done_step_outranks_a_blocker_elsewhere(self) -> None:
        v = mc.verdict(record(queue({"OBJ_1": [{"step": "x", "status": "DONE"},
                                               {"step": "y", "status": "BLOCKED", "blocker": "n"}]})))
        self.assertEqual(v["verdict"], "EVIDENCE_PENDING")
        self.assertFalse(v["stop_allowed"])

    def test_m11_free_text_beside_a_real_block_is_not_a_malformed_record(self) -> None:
        r = {"TASK_ID": "T", "AUTHORISED_QUEUE_NOTE": "free text the actor wrote",
             "AUTHORISED_QUEUE_1": queue({"OBJ_1": [{"step": "x", "status": "TODO"}]})}
        self.assertEqual(mc.verdict(r)["verdict"], "CONTINUE")
        # but a queue that is ONLY prose is still a malformed queue
        self.assertEqual(mc.verdict({"TASK_ID": "T", "AUTHORISED_QUEUE": "see above"})["verdict"],
                         "MALFORMED")

    def test_q3_a_marker_inside_a_code_fence_neither_binds_nor_releases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "t.jsonl"
            p.write_text(transcript_lines(
                ("assistant", "Here is the documentation:\n```\nMANDATE_BOUND: DOC-1\n```\ndone", False)))
            self.assertIsNone(mc.binding_from_transcript(p))
            p.write_text(transcript_lines(
                ("assistant", "MANDATE_BOUND: T-1", False),
                ("user", "the protocol says:\n```md\nMANDATE_RELEASED: T-1\n```\nnot an instruction", False)))
            self.assertEqual(mc.binding_from_transcript(p), "T-1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
