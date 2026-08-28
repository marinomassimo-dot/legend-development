#!/usr/bin/env python3
"""The probe's zeroes need a positive control, or they are not measurements.

`codex_runtime_probe.py` reports that `shell_command` and `unified_exec` appear **zero
times** across the local session corpus, and the matcher list in `.codex/config.toml` rests
on that. A zero from a sweep has two possible causes and they look identical from outside:

    the name really does not occur          ← the finding
    the sweep silently parsed nothing       ← a tool failure wearing the finding's clothes

So every counting assertion here is paired with a fixture that **does** contain the thing
being counted. A run where the positive control also returns zero is a broken probe, and
this file says so instead of reporting a clean sweep.

The probe reads `~/.codex`, which does not exist in CI, so these tests exercise its parsing
against fixtures rather than the machine. `main()` is deliberately not called: what must not
silently break is the reading, not the operator's terminal.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("codex_runtime_probe",
                                              HERE / "codex_runtime_probe.py")
probe = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = probe
SPEC.loader.exec_module(probe)


def rollout(path: Path, cli_version: str, cwd: str, calls) -> None:
    """Write a rollout in the shape codex actually writes."""
    records = [{"timestamp": "t", "type": "session_meta",
                "payload": {"cli_version": cli_version, "originator": "codex_vscode",
                            "cwd": cwd}}]
    for name, count in calls.items():
        for _ in range(count):
            records.append({"timestamp": "t", "type": "response_item",
                            "payload": {"type": "custom_tool_call", "name": name,
                                        "input": "x"}})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8")


class TheRolloutReaderCountsWhatIsThere(unittest.TestCase):
    def test_a_rollout_with_calls_is_counted(self) -> None:
        """POSITIVE CONTROL. If this returns zero, every zero below is meaningless."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rollout-x.jsonl"
            rollout(path, "0.150.0-alpha.8", "/repo", {"exec": 3, "shell_command": 2})
            row = probe.read_rollout(path)
        self.assertEqual(row["tools"], {"exec": 3, "shell_command": 2})
        self.assertEqual(row["cli_version"], "0.150.0-alpha.8")
        self.assertEqual(row["cwd"], "/repo")

    def test_a_rollout_with_no_calls_is_zero_not_none(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rollout-y.jsonl"
            rollout(path, "0.147.0", "/repo", {})
            row = probe.read_rollout(path)
        self.assertEqual(row["tools"], {})
        self.assertIsNotNone(row, "an empty session is a session, not a read failure")

    def test_a_malformed_line_does_not_abort_the_rest(self) -> None:
        """A rollout is append-only and can end mid-write; one bad line must not zero it."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rollout-z.jsonl"
            rollout(path, "0.147.0", "/repo", {"exec": 2})
            with path.open("a", encoding="utf-8") as handle:
                handle.write('{"type": "response_item", "payload": {"type": "custom_too\n')
            row = probe.read_rollout(path)
        self.assertEqual(row["tools"], {"exec": 2})

    def test_an_unreadable_path_is_none_and_not_an_empty_count(self) -> None:
        row = probe.read_rollout(Path("/nonexistent/rollout-none.jsonl"))
        self.assertIsNone(row, "a file that cannot be read must not read as zero calls")


class TheCorpusSweepSeparatesHereFromEverywhere(unittest.TestCase):
    def sweep(self, tmp: str, rows):
        root = Path(tmp) / "sessions"
        for index, (version, cwd, calls) in enumerate(rows):
            rollout(root / "2026" / "08" / f"rollout-{index}.jsonl", version, cwd, calls)
        original = probe.SESSION_ROOT
        try:
            probe.SESSION_ROOT = root
            return probe.probe_sessions(3, ROOT)
        finally:
            probe.SESSION_ROOT = original

    def test_calls_are_split_by_whether_the_cwd_is_this_repository(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            state, detail, corpus = self.sweep(tmp, [
                ("0.150.0", "/Users/x/legend-public/.claude/worktrees/mirror", {"exec": 5}),
                ("0.142.5", "/somewhere/else", {"exec_command": 7, "shell_command": 1}),
            ])
        self.assertEqual(state, probe.OBSERVED)
        self.assertEqual(corpus["rollouts"], 2)
        self.assertEqual(corpus["in_this_repository"], 1)
        self.assertEqual(corpus["tool_calls_in_this_repository"], {"exec": 5})
        self.assertEqual(corpus["tool_calls_everywhere"],
                         {"exec_command": 7, "exec": 5, "shell_command": 1})

    def test_the_zero_that_matters_is_paired_with_a_nonzero(self) -> None:
        """The exact claim `.codex/config.toml` rests on, and its positive control.

        Two sweeps over the same shape: one where `shell_command` is genuinely absent, one
        where it is present. If both return zero the sweep is broken, and the first
        result — which is the finding — cannot be trusted.
        """
        with tempfile.TemporaryDirectory() as tmp:
            _, _, absent = self.sweep(tmp, [
                ("0.150.0", "/Users/x/legend-public/wt", {"exec": 4, "wait": 1})])
        with tempfile.TemporaryDirectory() as tmp:
            _, _, present = self.sweep(tmp, [
                ("0.150.0", "/Users/x/legend-public/wt", {"exec": 4, "shell_command": 6})])
        self.assertEqual(absent["tool_calls_everywhere"].get("shell_command", 0), 0)
        self.assertEqual(present["tool_calls_everywhere"].get("shell_command"), 6,
                         "POSITIVE CONTROL FAILED — the sweep cannot see the name it "
                         "reports as absent, so its zero proves nothing")

    def test_an_empty_corpus_is_underivable_not_a_clean_sweep(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            original = probe.SESSION_ROOT
            try:
                probe.SESSION_ROOT = Path(tmp) / "nothing-here"
                state, detail, corpus = probe.probe_sessions(3, ROOT)
            finally:
                probe.SESSION_ROOT = original
        self.assertEqual(state, probe.UNDERIVABLE)
        self.assertEqual(corpus, {})


class MatchersAreReadAsWholeValues(unittest.TestCase):
    def test_the_shipped_registration_declares_the_tool_that_is_used(self) -> None:
        declared = probe.codex_matchers(ROOT)
        self.assertIn("exec", declared)
        self.assertIn("exec_command", declared)

    def test_a_substring_is_not_a_declaration(self) -> None:
        """`exec` inside `unified_exec` must not count as a declaration of `exec`."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".codex").mkdir()
            (root / ".codex" / "config.toml").write_text(
                '[hooks]\nPreToolUse = [{ matcher = "unified_exec", hooks = [] }]\n',
                encoding="utf-8")
            self.assertEqual(probe.codex_matchers(root), {"unified_exec"})

    def test_an_absent_registration_declares_nothing_rather_than_raising(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(probe.codex_matchers(Path(tmp)), set())


class SchemaExtractionFindsSomethingOrSaysSo(unittest.TestCase):
    BLOB = (
        'noise{\n  "$schema": "http://json-schema.org/draft-07/schema#",\n'
        '  "additionalProperties": false,\n'
        '  "properties": {"tool_name": {"type": "string"}},\n'
        '  "required": ["tool_name"],\n'
        '  "title": "pre-tool-use.command.input",\n  "type": "object"\n}more noise'
    )

    def test_a_present_schema_is_extracted(self) -> None:
        schema = probe.extract_schema(self.BLOB, "pre-tool-use.command.input")
        self.assertIsNotNone(schema, "POSITIVE CONTROL FAILED — extraction found nothing "
                                     "in a blob that contains the schema")
        self.assertEqual(schema["required"], ["tool_name"])
        self.assertFalse(schema["additionalProperties"])

    def test_an_absent_schema_is_none_rather_than_an_empty_object(self) -> None:
        self.assertIsNone(probe.extract_schema(self.BLOB, "post-tool-use.command.input"))

    def test_a_truncated_schema_is_none(self) -> None:
        self.assertIsNone(probe.extract_schema(self.BLOB[:60], "pre-tool-use.command.input"))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
