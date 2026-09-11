#!/usr/bin/env python3
"""Regressions for `attribution_census.py`.

The properties pinned here are the ones that decide whether the ratio means anything: an
incomplete block must not be counted as a census, a wave carrying one of the two required
keys must not be counted as compliant, a contract that records its waves in prose must be
its own state rather than a silent zero, and an empty tree must be void rather than clean.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import attribution_census as tool

FULL_BLOCK = (
    "ATTRIBUTION_CENSUS\n"
    "incidents: 10\n"
    "machine: 4   blind_auditor: 1   peer: 1   self: 4\n"
    "severity_high: 2   of which self: 1\n"
    "undetected_known: 0\n"
)


class AttributionCensus(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.evals = self.root / "disease-models" / "wwox" / "research" / "session_evaluations"
        self.evals.mkdir(parents=True)
        self.tasks = self.root / "ledger" / "tasks" / "actor"
        self.tasks.mkdir(parents=True)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_an_empty_tree_is_void_not_clean(self) -> None:
        empty = Path(self._tmp.name) / "nothing"
        empty.mkdir()
        self.assertEqual("INSUFFICIENT_DATA", tool.screen(empty).verdict)
        self.assertEqual(3, tool.main(["--root", str(empty)]))

    def test_a_complete_block_is_parsed_with_both_severity_values(self) -> None:
        (self.evals / "a.md").write_text(FULL_BLOCK, encoding="utf-8")
        census = tool.screen(self.root).complete_censuses
        self.assertEqual(1, len(census))
        self.assertEqual(2, census[0].counts["severity_high"])
        self.assertEqual(1, census[0].severity_self)
        self.assertEqual(4, census[0].counts["self"])

    def test_a_block_missing_a_field_is_not_a_census(self) -> None:
        (self.evals / "a.md").write_text(
            "ATTRIBUTION_CENSUS\nincidents: 3\nmachine: 3\n", encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual([], result.complete_censuses)
        self.assertEqual(1, result.eval_files)

    def test_impossible_arithmetic_is_inconsistent_not_complete(self) -> None:
        """Mirror F5: `incidents: 3 / machine: 5 / severity_high: 1 / of which self: 4` parsed
        as complete and printed 4/1."""
        (self.evals / "a.md").write_text(
            "ATTRIBUTION_CENSUS\nincidents: 3\nmachine: 5   blind_auditor: 0   peer: 0   "
            "self: 0\nseverity_high: 1   of which self: 4\nundetected_known: 0\n",
            encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual([], result.complete_censuses)
        self.assertIn("catchers sum to 5", result.censuses[0].inconsistency)
        self.assertIn("CENSUS_INCONSISTENT", tool.render(result, True))

    def test_self_high_above_high_is_inconsistent(self) -> None:
        (self.evals / "a.md").write_text(
            "ATTRIBUTION_CENSUS\nincidents: 4\nmachine: 2   blind_auditor: 0   peer: 0   "
            "self: 2\nseverity_high: 1   of which self: 2\nundetected_known: 0\n",
            encoding="utf-8")
        self.assertEqual([], tool.screen(self.root).complete_censuses)

    def test_the_denominator_counts_diagnoses_without_a_block(self) -> None:
        (self.evals / "a.md").write_text(FULL_BLOCK, encoding="utf-8")
        (self.evals / "b.md").write_text("no census here\n", encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual(2, result.eval_files)
        self.assertEqual(1, len(result.complete_censuses))

    def test_a_wave_with_only_one_of_the_two_keys_is_not_compliant(self) -> None:
        (self.tasks / "T.json").write_text(json.dumps({
            "WAVE_1_RESULT": {"DEFAULTS_TAKEN": [], "STOP_LOG": []},
            "WAVE_2_RESULT": {"DEFAULTS_TAKEN": []},
            "WAVE_3_RESULT": {"STOP_LOG": []},
        }), encoding="utf-8")
        waves = tool.screen(self.root).waves
        self.assertEqual(3, len(waves))
        self.assertEqual(1, len([w for w in waves if w.has_defaults and w.has_stop_log]))

    def test_a_single_wave_contract_records_the_keys_at_the_top_level(self) -> None:
        """The instrument's own defect, found by the record on 2026-09-10.

        Three actors complied - single-wave tasks carrying DEFAULTS_TAKEN and STOP_LOG at
        the top level of the contract - and the first version of this parser counted only
        WAVE_n_RESULT keys, reported 0 of 4, and did not show them at all. Invisible
        compliance is worse than visible non-compliance: it teaches the actor that the
        rule is not read.
        """
        (self.tasks / "T.json").write_text(json.dumps({
            "TASK_ID": "T", "DEFAULTS_TAKEN": [], "STOP_LOG": [],
        }), encoding="utf-8")
        waves = tool.screen(self.root).waves
        self.assertEqual(1, len(waves))
        self.assertEqual("SINGLE_WAVE", waves[0].shape)
        self.assertTrue(waves[0].has_defaults and waves[0].has_stop_log)

    def test_a_single_wave_contract_with_one_key_is_not_compliant(self) -> None:
        (self.tasks / "T.json").write_text(
            json.dumps({"TASK_ID": "T", "DEFAULTS_TAKEN": []}), encoding="utf-8")
        waves = tool.screen(self.root).waves
        self.assertEqual(1, len(waves))
        self.assertFalse(waves[0].has_stop_log)

    def test_wave_keys_win_over_the_top_level_shape(self) -> None:
        """A multi-wave contract is measured per wave, not once for the whole task."""
        (self.tasks / "T.json").write_text(json.dumps({
            "TASK_ID": "T", "DEFAULTS_TAKEN": [], "STOP_LOG": [],
            "WAVE_1_RESULT": {"outcome": "closed"},
        }), encoding="utf-8")
        waves = tool.screen(self.root).waves
        self.assertEqual(1, len(waves))
        self.assertEqual("WAVE", waves[0].shape)
        self.assertFalse(waves[0].has_defaults)

    def test_prose_waves_are_their_own_state_not_a_zero(self) -> None:
        (self.tasks / "T.json").write_text(
            json.dumps({"TASK_CLAIM": {"wave": "wave 3 of the lot"}}), encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual([], result.waves)
        self.assertEqual(1, len(result.unstructured_contracts))

    def test_a_contract_with_no_waves_at_all_is_neither(self) -> None:
        (self.tasks / "T.json").write_text(
            json.dumps({"TASK_ID": "T", "CURRENT_STATE": "ASSIGNED"}), encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual([], result.waves)
        self.assertEqual([], result.unstructured_contracts)

    def test_an_all_zero_undetected_column_is_reported_as_a_finding(self) -> None:
        (self.evals / "a.md").write_text(FULL_BLOCK, encoding="utf-8")
        self.assertIn("undetected_known is 0", tool.render(tool.screen(self.root), False))

    def test_every_verdict_carries_the_digest_of_what_was_screened(self) -> None:
        (self.evals / "a.md").write_text(FULL_BLOCK, encoding="utf-8")
        result = tool.screen(self.root)
        self.assertEqual(64, len(result.digest))
        self.assertGreater(result.screened_bytes, 0)

    def test_findings_do_not_turn_the_run_into_a_failure(self) -> None:
        (self.evals / "a.md").write_text("no census\n", encoding="utf-8")
        self.assertEqual(0, tool.main(["--root", str(self.root), "--queue"]))

    def test_the_modules_own_self_test_passes(self) -> None:
        self.assertEqual(0, tool.self_test())


if __name__ == "__main__":
    unittest.main(verbosity=2)
