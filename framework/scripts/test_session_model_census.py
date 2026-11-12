#!/usr/bin/env python3
"""Regressions for session_model_census.py — what the dispatch asked for is read back, not assumed.

Synthetic transcripts only: a delegate that ran another model than the one asked for, one whose
model changed mid-run, and one that ran as asked, each with the sibling `.meta.json` the runtime writes.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import session_model_census as smc  # noqa: E402


def write_run(directory: Path, name: str, models: list[str], *, asked: str | None, effort: str | None,
              effort_read: str = "high") -> Path:
    path = directory / f"{name}.jsonl"
    rows = [{"type": "user", "message": {"role": "user", "content": "do the thing"}}]
    for index, model in enumerate(models):
        rows.append({"type": "assistant", "timestamp": f"2026-11-06T00:00:{index:02d}Z", "effort": effort_read,
                     "message": {"model": model, "usage": {"input_tokens": 2, "cache_creation_input_tokens": 100,
                                                             "cache_read_input_tokens": 50 * index,
                                                             "output_tokens": 10}}})
    path.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    meta = {"agentType": "general-purpose", "description": name}
    if asked:
        meta["model"] = asked
    if effort:
        meta["effort"] = effort
    path.with_suffix(".meta.json").write_text(json.dumps(meta), encoding="utf-8")
    return path


class Census(unittest.TestCase):
    def test_one_response_written_as_several_rows_is_counted_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dup.jsonl"
            usage = {"input_tokens": 2, "cache_creation_input_tokens": 100, "cache_read_input_tokens": 50}
            rows = [{"type": "user", "message": {"role": "user", "content": "go"}}]
            for output in (5, 40, 40):      # thinking block, text block, tool_use block of ONE response
                rows.append({"type": "assistant", "effort": "high", "message": {"id": "msg_1", "model": "m", "usage": {**usage, "output_tokens": output}}})
            rows.append({"type": "assistant", "effort": "high", "message": {"id": "msg_2", "model": "m", "usage": {**usage, "output_tokens": 7}}})
            path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            result = smc.census(path)
        self.assertEqual(result["turns"], 2)
        self.assertEqual(result["totals"]["output"], 47)
        self.assertEqual(result["totals"]["cache_creation"], 200)
        self.assertEqual(result["efforts"], {"high": 2})

    def test_asked_model_that_never_ran_is_flagged_and_fails_the_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = write_run(Path(td), "agent-a", ["claude-opus-5"] * 3, asked="fable", effort=None)
            row = smc.census(path)
            self.assertEqual(row["asked_not_ran"], "fable")
            self.assertEqual(smc.main([str(path)]), 1)

    def test_run_as_asked_with_effort_read_back_passes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = write_run(Path(td), "agent-b", ["claude-sonnet-5-5"] * 2, asked="sonnet", effort="medium",
                             effort_read="medium")
            row = smc.census(path)
            self.assertEqual(row["asked_not_ran"], "")
            self.assertEqual(row["efforts"], {"medium": 2})
            self.assertEqual(row["dispatch"]["effort"], "medium")
            self.assertEqual(smc.main([str(path)]), 0)

    def test_mid_run_change_still_fails_and_totals_are_summed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            first = write_run(Path(td), "agent-c", ["claude-fable-5-1", "claude-opus-5"], asked="fable", effort=None)
            second = write_run(Path(td), "agent-d", ["claude-sonnet-5-5"], asked=None, effort=None)
            rows = [smc.census(first), smc.census(second)]
            self.assertTrue(rows[0]["changed_mid_run"])
            text = smc.render(rows)
            self.assertIn("TOTAL 2 run(s)", text)
            self.assertIn("not a share of any plan", text)
            self.assertEqual(smc.main([str(first), str(second)]), 1)

    def test_since_slices_a_long_session_and_reports_where_the_reread_cost_sits(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "long.jsonl"
            ctx = [(10, 100), (10, 200), (900, 0), (900, 0), (950, 0), (300, 0)]   # (cache_read, cache_creation) per turn
            rows = [{"type": "assistant", "timestamp": f"2026-11-06T00:00:{i:02d}Z",
                     "message": {"id": f"m{i}", "model": "claude-sonnet-5-5",
                                 "usage": {"input_tokens": 0, "cache_creation_input_tokens": cc, "cache_read_input_tokens": cr, "output_tokens": 1}}}
                    for i, (cr, cc) in enumerate(ctx)]
            path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            whole = smc.census(path)
            part = smc.census(path, "2026-11-06T00:00:02Z")
            self.assertEqual((whole["turns"], part["turns"]), (6, 4))
            self.assertEqual(part["first_turn_context"], 900)
            self.assertEqual(part["context_drops"], 1)                 # 950 -> 300
            self.assertEqual(part["start_context_share_of_cache_read"], round(900 * 4 / 3050, 2))
            self.assertIn("start context re-read", smc.render([part]))

    def test_windows_separate_the_cost_before_and_after_a_restart(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "t.jsonl"
            rows = [("t1", 900), ("t2", 950), ("t3", 300), ("t4", 320)]
            path.write_text("\n".join(json.dumps({"type": "assistant", "timestamp": f"2026-11-11T00:00:0{i}", "message": {"id": k, "model": "m", "usage": {"input_tokens": 1, "cache_creation_input_tokens": 0, "cache_read_input_tokens": c, "output_tokens": 5}}})
                                       for i, (k, c) in enumerate(rows)) + "\n")
            part = smc.census(path)
            w = part["windows"]
            self.assertEqual([x["turns"] for x in w], [2, 2])
            self.assertEqual((w[0]["birth_context"], w[1]["birth_context"]), (901, 301))
            self.assertIn("window 2: 2 turns", smc.render([part]))

    def test_transcript_without_sibling_meta_is_still_read(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = write_run(Path(td), "agent-e", ["claude-sonnet-5-5"], asked=None, effort=None)
            path.with_suffix(".meta.json").unlink()
            row = smc.census(path)
            self.assertEqual(row["dispatch"], {})
            self.assertEqual(row["asked_not_ran"], "")


class Carry(unittest.TestCase):
    """HE47 H5: the carried-bytes proxy counts a result by its size times the turns that followed it."""
    def test_a_large_early_result_dominates_a_small_late_one(self):
        rows = []
        for i, size in enumerate((10000, 100, 100)):
            rows.append({"type": "assistant", "message": {"content": [{"type": "tool_use", "id": f"t{i}", "name": "Bash"}]}})
            rows.append({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}", "content": "x" * size}]}})
        rows.append({"type": "assistant", "message": {"content": [{"type": "text", "text": "done"}]}})
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t.jsonl"
            p.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            c = smc.carry(p, cap=3000, early=1)
        self.assertEqual((c["turns"], c["tool_results"], c["results_over_3000_bytes"]), (4, 3, 1))
        self.assertEqual(c["share_of_carried_by_tool"], {"Bash": 100})
        self.assertGreater(c["share_of_carried_in_results_over_3000_bytes"], 95)
        self.assertGreater(c["share_of_carried_read_in_the_first_1_turns"], 95)


if __name__ == "__main__":
    unittest.main(verbosity=2)
