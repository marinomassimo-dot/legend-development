#!/usr/bin/env python3
"""The CLI, driven as a subprocess — the surface that was carrying the worst defect untested.

🔴 Why this file exists, stated plainly. `test_consolidate_approval_queue.py` calls
`consolidate()` with a dict the test builds itself. It therefore never executed the line that
turned a list of files INTO that dict:

    sources = {path.stem: load(path) for path in arguments.sources}

Three real lineages of 6, 14 and 10 records, copied into three directories and all named
`queue.jsonl`, produced:

    sources: queue=10
    consolidated: 10 records from 10 input line(s); 0 deduped, 0 conflicts
    exit 0

**Twenty of thirty records were discarded before `consolidate()` was called**, and the summary
described a clean, conflict-free consolidation. Twenty-seven passing tests said nothing about it,
because the tested surface and the defective surface were disjoint — the same shape as the
adjudication script, whose every fail-open state lived in the one function its suite never
called.

Exit codes under test: **0** consolidated · **1** governance conflict, an operator decides ·
**2** source error, there is nothing to decide.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "consolidate_approval_queue.py"

HEADER = {"_schema": "LEGEND governance v3.1.1 · Annex J.3 HUMAN_APPROVAL_QUEUE"}


def approval(ident, when="2026-08-16", state="PENDING", **extra):
    record = {"APPROVAL_ID": ident, "REQUESTED_AT": when, "STATE": state}
    record.update(extra)
    return record


PREFIX = [HEADER, approval("APR-A-001"), approval("APR-A-002")]


class CliCase(unittest.TestCase):
    def setUp(self):
        self.box = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.box, ignore_errors=True)

    def write(self, relative: str, records: list[dict]) -> Path:
        path = self.box / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
        return path

    def run_tool(self, *paths: Path):
        result = subprocess.run([sys.executable, str(TOOL), *[str(p) for p in paths]],
                                capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

    def consolidated_count(self, output: str) -> int:
        for line in output.splitlines():
            if line.startswith("consolidated:"):
                return int(line.split()[1])
        self.fail(f"no consolidated line in:\n{output}")

    def input_lines(self, output: str) -> int:
        for line in output.splitlines():
            if line.startswith("consolidated:"):
                return int(line.split("from")[1].split()[0])
        self.fail(f"no consolidated line in:\n{output}")


class SameBasename(CliCase):
    def test_three_directories_one_basename_keeps_all_three_lineages(self):
        a = self.write("d1/queue.jsonl", PREFIX)
        b = self.write("d2/queue.jsonl", PREFIX + [approval("APR-B-001", "2026-08-17")])
        c = self.write("d3/queue.jsonl", PREFIX + [approval("APR-C-001", "2026-08-18"),
                                                   approval("APR-C-002", "2026-08-18")])
        code, output = self.run_tool(a, b, c)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.input_lines(output), 3 + 4 + 5)
        self.assertEqual(self.consolidated_count(output), 6)
        for label in ("d1/queue.jsonl", "d2/queue.jsonl", "d3/queue.jsonl"):
            self.assertIn(label, output, "a lineage lost its label")

    def test_two_directories_one_basename(self):
        """The output count alone does not discriminate here, and the first draft of this test
        therefore passed against the defect: with the collision only the last file survived,
        4 records in and 4 out. **The input count is what exposes it** — 7 lines were supplied.
        A test that passes on both arms of a battery has tested nothing."""
        a = self.write("x/queue.jsonl", PREFIX)
        b = self.write("y/queue.jsonl", PREFIX + [approval("APR-B-001", "2026-08-17")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.input_lines(output), 7, "a lineage was dropped before consolidation")
        self.assertEqual(self.consolidated_count(output), 4)
        self.assertIn("x/queue.jsonl", output)
        self.assertIn("y/queue.jsonl", output)

    def test_same_basename_same_content_still_counts_both_inputs(self):
        """Identical content is not a reason to lose an input: the DEDUP must be visible."""
        a = self.write("x/queue.jsonl", PREFIX)
        b = self.write("y/queue.jsonl", PREFIX)
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.input_lines(output), 6)
        self.assertEqual(self.consolidated_count(output), 3)

    def test_same_basename_different_content_conflicting_is_refused(self):
        a = self.write("x/queue.jsonl", PREFIX)
        b = self.write("y/queue.jsonl", [HEADER, approval("APR-A-001", state="APPROVED")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 1, output)
        self.assertIn("CONFLICT", output)

    def test_unique_names_still_get_short_labels(self):
        """The control: the repair must not make every label a full path."""
        a = self.write("L1.jsonl", PREFIX)
        b = self.write("L2.jsonl", PREFIX + [approval("APR-B-001", "2026-08-17")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 0, output)
        self.assertIn("L1.jsonl=3", output)
        self.assertIn("L2.jsonl=4", output)

    def test_the_same_file_twice_is_a_source_error(self):
        a = self.write("q.jsonl", PREFIX)
        code, output = self.run_tool(a, a)
        self.assertEqual(code, 2, output)
        self.assertIn("more than once", output)


class IdentityAndPayload(CliCase):
    def test_same_id_same_payload_across_lineages_dedupes(self):
        a = self.write("a.jsonl", [HEADER, approval("APR-X")])
        b = self.write("b.jsonl", [HEADER, approval("APR-X")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.consolidated_count(output), 2)

    def test_same_id_different_payload_fails_closed_as_a_conflict(self):
        a = self.write("a.jsonl", [HEADER, approval("APR-X", state="APPROVED")])
        b = self.write("b.jsonl", [HEADER, approval("APR-X", state="DENIED")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 1, output)
        self.assertIn("APR-X", output)

    def test_approved_and_rejected_under_one_id_is_never_merged(self):
        """The case the whole tool exists to refuse."""
        a = self.write("a.jsonl", [HEADER, approval("APR-DEC", state="APPROVED")])
        b = self.write("b.jsonl", [HEADER, approval("APR-DEC", state="REJECTED")])
        code, output = self.run_tool(a, b)
        self.assertEqual(code, 1, output)
        self.assertNotIn("consolidated:", output)

    def test_an_integer_id_does_not_silently_become_an_unidentified_record(self):
        a = self.write("a.jsonl", [HEADER, {"APPROVAL_ID": 12345, "REQUESTED_AT": "2026-08-16"}])
        code, output = self.run_tool(a)
        self.assertEqual(code, 0, output)
        # content-addressed rather than dropped; the record must still reach the view
        self.assertEqual(self.consolidated_count(output), 2)

    def test_a_malformed_id_is_kept_not_dropped(self):
        a = self.write("a.jsonl", [HEADER, {"APPROVAL_ID": "", "REQUESTED_AT": "2026-08-16"}])
        code, output = self.run_tool(a)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.consolidated_count(output), 2)


class TimestampsAndVocabulary(CliCase):
    def test_a_malformed_timestamp_is_a_source_error_not_a_sort_key(self):
        a = self.write("a.jsonl", [HEADER, {"APPROVAL_ID": "APR-T", "REQUESTED_AT": 20260816}])
        code, output = self.run_tool(a)
        self.assertEqual(code, 2, output)
        self.assertIn("not a string", output)

    def test_date_only_timestamps_are_accepted_and_ordered_by_file_position(self):
        a = self.write("a.jsonl", [HEADER,
                                   approval("APR-1", "2026-08-17"),
                                   approval("APR-2", "2026-08-17"),
                                   approval("APR-3", "2026-08-17")])
        code, output = self.run_tool(a)
        self.assertEqual(code, 0, output)
        order = [l.split()[1] for l in output.splitlines() if l.strip().startswith("2026-08-17")]
        self.assertEqual(order, ["APR-1", "APR-2", "APR-3"])

    def test_an_unknown_status_is_carried_through(self):
        a = self.write("a.jsonl", [HEADER, approval("APR-U", state="MOON_PHASE")])
        code, output = self.run_tool(a)
        self.assertEqual(code, 0, output)
        self.assertIn("MOON_PHASE", output)

    def test_a_future_field_is_carried_through(self):
        a = self.write("a.jsonl", [HEADER, approval("APR-F", FIELD_FROM_LATER_SCHEMA={"n": 1})])
        code, output = self.run_tool(a)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.consolidated_count(output), 2)

    def test_a_non_object_line_is_a_source_error(self):
        path = self.box / "bad.jsonl"
        path.write_text(json.dumps(HEADER) + "\n" + '"a bare string"\n')
        code, output = self.run_tool(path)
        self.assertEqual(code, 2, output)

    def test_invalid_json_is_a_source_error_not_an_operator_decision(self):
        path = self.box / "bad.jsonl"
        path.write_text("{ not json\n")
        code, output = self.run_tool(path)
        self.assertEqual(code, 2, output)
        self.assertNotIn("CONFLICT", output)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
