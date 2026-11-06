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

    def test_transcript_without_sibling_meta_is_still_read(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = write_run(Path(td), "agent-e", ["claude-sonnet-5-5"], asked=None, effort=None)
            path.with_suffix(".meta.json").unlink()
            row = smc.census(path)
            self.assertEqual(row["dispatch"], {})
            self.assertEqual(row["asked_not_ran"], "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
