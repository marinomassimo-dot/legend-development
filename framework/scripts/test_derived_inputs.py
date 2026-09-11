#!/usr/bin/env python3
"""Regressions for `derived_inputs.py` — the C22 guard.

The fixture is a throwaway git repository holding a registries directory, a receipt ledger
and a manifest directory, so BOUND / DIRTY / UNBOUND are exercised against real git state and
not simulated. One case drives a real generator (`reading_state.py --out`) as a subprocess in
that repository: the refusal must reach the entry point a scientist actually runs, not only
the helper's unit tests.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import derived_inputs as guard

ROOT = Path(__file__).resolve().parents[2]
READING_STATE = ROOT / "framework" / "scripts" / "reading_state.py"


class GitFixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.registries = self.root / "disease-models" / "wwox" / "registries"
        self.manifests = self.root / "disease-models" / "wwox" / "research" / "deepdive_manifests"
        self.registries.mkdir(parents=True)
        self.manifests.mkdir(parents=True)
        (self.registries / "paper_registry_current.md").write_text("# papers\n", encoding="utf-8")
        (self.registries / "fulltext_read_receipts.jsonl").write_text("", encoding="utf-8")
        (self.manifests / "PMID11111111.json").write_text(json.dumps({"pmid": "11111111"}), encoding="utf-8")
        self._git("init", "-q", "-b", "main")
        self._git("config", "user.email", "fixture@invalid")
        self._git("config", "user.name", "fixture")
        self._git("add", "-A")
        self._git("commit", "-q", "-m", "fixture")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _git(self, *args: str) -> None:
        subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def _state(self, exclude=None) -> guard.InputState:
        return guard.input_state(self.root, [self.registries, self.manifests], exclude=exclude)


class TheThreeStates(GitFixture):
    def test_committed_inputs_are_bound_to_head(self) -> None:
        state = self._state()
        self.assertEqual(guard.BOUND, state.verdict)
        self.assertEqual(40, len(state.head))
        self.assertEqual([], state.dirty)
        self.assertIsNone(guard.refuse_if_dirty(state, reason=None, stream=open(os.devnull, "w")))

    def test_a_modified_input_is_dirty_and_refused(self) -> None:
        (self.manifests / "PMID11111111.json").write_text(json.dumps({"pmid": "11111111", "x": 1}),
                                                          encoding="utf-8")
        state = self._state()
        self.assertEqual(guard.DIRTY, state.verdict)
        self.assertEqual([("M", "disease-models/wwox/research/deepdive_manifests/PMID11111111.json")],
                         state.dirty)
        self.assertEqual(2, guard.refuse_if_dirty(state, reason=None, stream=open(os.devnull, "w")))

    def test_an_untracked_input_is_dirty_too(self) -> None:
        """C22's exact shape: a peer's manifest that exists on disk and in no commit."""
        (self.manifests / "PMID22222222.json").write_text("{}", encoding="utf-8")
        state = self._state()
        self.assertEqual(guard.DIRTY, state.verdict)
        self.assertEqual("??", state.dirty[0][0])

    def test_a_stated_reason_proceeds_and_is_printed(self) -> None:
        (self.manifests / "PMID22222222.json").write_text("{}", encoding="utf-8")
        state = self._state()
        import io
        out = io.StringIO()
        self.assertIsNone(guard.refuse_if_dirty(state, reason="BATCH_COMMIT phase 4.7", stream=out))
        self.assertIn("BATCH_COMMIT phase 4.7", out.getvalue())
        self.assertIn("PMID22222222.json", out.getvalue())

    def test_a_blank_reason_is_no_reason(self) -> None:
        (self.manifests / "PMID22222222.json").write_text("{}", encoding="utf-8")
        self.assertEqual(2, guard.refuse_if_dirty(self._state(), reason="   ",
                                                  stream=open(os.devnull, "w")))

    def test_the_surface_being_written_and_its_generated_siblings_are_not_inputs(self) -> None:
        out = self.registries / "coverage_report.md"
        out.write_text("stale\n", encoding="utf-8")
        (self.registries / "batch_queue.md").write_text("stale\n", encoding="utf-8")
        self.assertEqual(guard.BOUND, self._state(exclude=[out]).verdict)

    def test_no_git_repository_is_unbound_and_proceeds_named(self) -> None:
        with tempfile.TemporaryDirectory() as plain:
            d = Path(plain) / "registries"
            d.mkdir()
            state = guard.input_state(Path(plain), [d])
            self.assertEqual(guard.UNBOUND, state.verdict)
            import io
            out = io.StringIO()
            self.assertIsNone(guard.refuse_if_dirty(state, reason=None, stream=out))
            self.assertIn("UNBOUND", out.getvalue())

    def test_the_cli_reports_the_state_and_the_exit_code(self) -> None:
        self.assertEqual(0, guard.main(["--root", str(self.root), "disease-models/wwox/registries"]))
        (self.registries / "paper_registry_current.md").write_text("# papers\n- one\n", encoding="utf-8")
        self.assertEqual(2, guard.main(["--root", str(self.root), "disease-models/wwox/registries"]))
        self.assertEqual(0, guard.main(["--root", str(self.root), "disease-models/wwox/registries",
                                        guard.FLAG, "the batch's own edit"]))


class TheGuardReachesAGenerator(GitFixture):
    """A helper nobody calls is not a control: drive reading_state.py through its entry point."""

    def _run(self, *extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(READING_STATE), "--root", str(self.root), "--disease", "wwox",
             "--out", str(self.registries / "reading_state.md"), *extra],
            capture_output=True, text=True)

    def test_a_clean_ledger_is_derived(self) -> None:
        result = self._run()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("inputs BOUND", result.stderr)
        self.assertTrue((self.registries / "reading_state.md").is_file())

    def test_an_uncommitted_ledger_refuses_the_write(self) -> None:
        (self.registries / "fulltext_read_receipts.jsonl").write_text(
            json.dumps({"event_id": "in-flight"}) + "\n", encoding="utf-8")
        result = self._run()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("REFUSED", result.stderr)
        self.assertIn("fulltext_read_receipts.jsonl", result.stderr)
        self.assertFalse((self.registries / "reading_state.md").exists())

    def test_the_stated_reason_lets_the_batch_through(self) -> None:
        (self.registries / "fulltext_read_receipts.jsonl").write_text("", encoding="utf-8")
        (self.registries / "paper_registry_current.md").write_text("# papers\n- one\n", encoding="utf-8")
        # The registry is not this page's input; only the ledger is. Untouched ledger -> BOUND.
        result = self._run()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
