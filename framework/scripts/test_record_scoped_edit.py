#!/usr/bin/env python3
"""record_scoped_edit.py — the edit lands where it is addressed, every other byte stays, or it refuses.

Each refusal is asserted by its own code and each fixture is built so the defect can occur: a
duplicate id is really duplicated, a fenced heading really exists only in a fence, a replacement
really carries an `#` heading. A suite whose fixtures cannot exhibit the defect proves nothing
(learned_gates_registry, PATTERN_ALREADY_SOLVED_GATE, third variant).

Run: python3 framework/scripts/test_record_scoped_edit.py
"""
from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import record_scoped_edit as rse  # noqa: E402
import registry_records as rr  # noqa: E402

TOOL = HERE / "record_scoped_edit.py"
H2 = (2,)
REG = """# Claim Registry Current

> preamble note

## WWOX Claim Registry
**Version:** v1

---

## CLAIM 001
**Title:** one
**Status:** in observation

---

## CLAIM 002
**Title:** two

### Addendum 2026-09-01
appended note

---

## CLAIM 003
**Title:** three
"""


def op(**kw):
    return rse.Op(**kw)


class Partition(unittest.TestCase):
    def test_blocks_tile_the_text_exactly(self):
        blocks = rr.partition(REG, H2)
        self.assertEqual("".join(REG[b.start:b.end] for b in blocks), REG)
        self.assertEqual([b.key for b in blocks],
                         ["Claim Registry Current", "WWOX Claim Registry", "CLAIM 001", "CLAIM 002",
                          "CLAIM 003"])

    def test_real_surfaces_tile_and_every_record_is_addressable(self):
        for stem, rel in rr.SOURCES.items():
            path = ROOT / "disease-models/wwox" / rel
            text = path.read_bytes().decode("utf-8")
            levels = rr.IDENTITY_LEVELS[stem]
            blocks = rr.partition(text, levels)
            self.assertEqual("".join(text[b.start:b.end] for b in blocks), text, stem)
            ids = [k for _o, _l, k in rse.identity_headings(text, levels)]
            self.assertEqual(len(ids), len(set(map(str.lower, ids))), f"{stem}: duplicate ids")

    def test_fenced_heading_is_not_a_block(self):
        text = "## A\nx\n```\n## CLAIM 009\n```\n## CLAIM 010\ny\n"
        self.assertEqual([b.key for b in rr.partition(text, H2)], ["A", "CLAIM 010"])


class Operations(unittest.TestCase):
    def test_replace_changes_only_the_record(self):
        new = "## CLAIM 002\n**Title:** two, narrowed\n\n---\n\n"
        out, _ = rse.apply_ops(REG, [op(op="replace", id="CLAIM 002", text=new)], H2)
        start = REG.index("## CLAIM 002")
        end = REG.index("## CLAIM 003")
        self.assertEqual(out, REG[:start] + new + REG[end:])

    def test_replace_is_byte_identical_when_text_is_unchanged(self):
        blocks = {b.key: REG[b.start:b.end] for b in rr.partition(REG, H2)}
        out, _ = rse.apply_ops(REG, [op(op="replace", id="CLAIM 001", text=blocks["CLAIM 001"])], H2)
        self.assertEqual(out, REG)

    def test_replace_within_edits_one_unique_range(self):
        out, _ = rse.apply_ops(REG, [op(op="replace-within", id="CLAIM 001",
                                        old="**Status:** in observation",
                                        new="**Status:** consolidated baseline")], H2)
        self.assertEqual(out, REG.replace("in observation", "consolidated baseline"))

    def test_heading_anchor_reaches_a_nested_sub_block(self):
        out, _ = rse.apply_ops(REG, [op(op="replace-within", heading="Addendum 2026-09-01",
                                        old="appended note", new="appended note, amended")], H2)
        self.assertIn("appended note, amended", out)
        self.assertEqual(out.replace(", amended", ""), REG)

    def test_insert_after_with_separator_keeps_neighbour_bytes(self):
        new = "\n---\n\n## CLAIM 004\n**Title:** four\n"
        out, report = rse.apply_ops(REG, [op(op="insert-after", id="CLAIM 003", text=new)], H2)
        self.assertEqual(out, REG + new)
        self.assertEqual(report.ops[0]["new_records"], ["CLAIM 004"])

    def test_insert_before_and_append(self):
        new ="## CLAIM 005\n**Title:** five\n\n---\n\n"
        out, _ = rse.apply_ops(REG, [op(op="insert-before", id="CLAIM 002", text=new)], H2)
        self.assertEqual(out, REG.replace("## CLAIM 002", new + "## CLAIM 002"))
        out, _ = rse.apply_ops(REG, [op(op="append", text="\n## CLAIM 006\nx\n")], H2)
        self.assertEqual(out, REG + "\n## CLAIM 006\nx\n")

    def test_delete(self):
        out, report = rse.apply_ops(REG, [op(op="delete", id="CLAIM 001")], H2)
        self.assertNotIn("CLAIM 001", out)
        self.assertEqual(report.ops[0]["removed_records"], ["CLAIM 001"])

    def test_rename_needs_rename_to(self):
        new = "## CLAIM 007\n**Title:** one\n\n---\n\n"
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(REG, [op(op="replace", id="CLAIM 001", text=new)], H2)
        self.assertEqual(caught.exception.code, "IDENTITY_CHANGED")
        out, _ = rse.apply_ops(REG, [op(op="replace", id="CLAIM 001", text=new,
                                        rename_to="CLAIM 007")], H2)
        self.assertIn("## CLAIM 007", out)
        self.assertNotIn("## CLAIM 001", out)

    def test_bytes_are_preserved_including_crlf(self):
        crlf = REG.replace("\n", "\r\n")
        out, _ = rse.apply_ops(crlf, [op(op="replace-within", id="CLAIM 003", old="three",
                                         new="3")], H2)
        self.assertEqual(out, crlf.replace("three", "3"))


class Refusals(unittest.TestCase):
    def refused(self, code, text, ops, levels=H2):
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(text, ops, levels)
        self.assertEqual(caught.exception.code, code, str(caught.exception))

    def test_missing(self):
        self.refused("ANCHOR_MISSING", REG, [op(op="delete", id="CLAIM 099")])

    def test_duplicate_id_is_ambiguous(self):
        dup = REG + "\n## CLAIM 001\nsecond definition\n"
        self.refused("ANCHOR_AMBIGUOUS", dup, [op(op="delete", id="CLAIM 001")])

    def test_duplicate_heading_is_ambiguous(self):
        dup = REG.replace("### Addendum 2026-09-01", "### Note") + "### Note\nx\n"
        self.refused("ANCHOR_AMBIGUOUS", dup, [op(op="delete", heading="Note")])

    def test_fenced_heading_is_not_an_anchor(self):
        fenced = REG + "\n```\n## CLAIM 042\ntemplate\n```\n"
        self.refused("FENCED_ANCHOR", fenced, [op(op="delete", id="CLAIM 042")])

    def test_nested_record_protects_the_child(self):
        text = "## Active\n\n### DIS-001\nparent\n\n#### DIS-002\nchild\n\n### DIS-003\nz\n"
        levels = (3, 4)
        self.refused("NESTED_RECORD", text, [op(op="replace-within", id="DIS-001", old="parent",
                                                new="P")], levels)
        out, _ = rse.apply_ops(text, [op(op="replace-within", id="DIS-002", old="child",
                                         new="C")], levels)
        self.assertEqual(out, text.replace("child", "C"))

    def test_h1_in_replacement_would_swallow(self):
        new = "## CLAIM 002\n**Title:** two\n\n# BLOCK 9 — range heading\n\n"
        self.refused("RESEGMENTATION", REG, [op(op="replace", id="CLAIM 002", text=new)])

    def test_same_level_heading_in_replacement_resegments(self):
        new = "## CLAIM 002\n**Title:** two\n\n## Notes\nx\n\n"
        self.refused("RESEGMENTATION", REG, [op(op="replace", id="CLAIM 002", text=new)])

    def test_replace_within_cannot_create_a_heading(self):
        self.refused("RESEGMENTATION", REG, [op(op="replace-within", id="CLAIM 001",
                                                old="**Title:** one",
                                                new="**Title:** one\n# BLOCK 7")])

    def test_old_string_must_be_unique(self):
        self.refused("OLD_NOT_UNIQUE", REG, [op(op="replace-within", heading="WWOX Claim Registry",
                                                old="\n", new="\n\n")])
        self.refused("OLD_ABSENT", REG, [op(op="replace-within", id="CLAIM 001", old="nope",
                                            new="x")])

    def test_insert_of_existing_id(self):
        self.refused("DUPLICATE_ID", REG, [op(op="insert-after", id="CLAIM 003",
                                              text="\n## CLAIM 001\nagain\n")])

    def test_insert_must_be_a_complete_block(self):
        self.refused("RESEGMENTATION", REG, [op(op="insert-after", id="CLAIM 001",
                                                text="loose line\n")])
        self.refused("RESEGMENTATION", REG, [op(op="insert-after", id="CLAIM 001",
                                                text="## CLAIM 008\nno newline")])

    def test_editing_a_section_that_contains_records_is_refused(self):
        self.refused("NESTED_RECORD", REG, [op(op="replace-within", heading="Claim Registry Current",
                                               old="> preamble note", new="> x")])

    def test_batch_is_all_or_nothing(self):
        with self.assertRaises(rse.Refusal):
            rse.apply_ops(REG, [op(op="replace-within", id="CLAIM 001", old="one", new="1"),
                                op(op="delete", id="CLAIM 099")], H2)


class Command(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True)

    def test_dry_run_writes_nothing_and_apply_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "claim_registry_current.md"
            path.write_bytes(REG.encode())
            done = self.run_tool("replace-within", "--file", str(path), "--id", "CLAIM 003",
                                 "--old", "three", "--new", "3")
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertIn("DRY RUN", done.stdout)
            self.assertEqual(path.read_bytes(), REG.encode())
            done = self.run_tool("replace-within", "--file", str(path), "--id", "CLAIM 003",
                                 "--old", "three", "--new", "3", "--apply")
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertEqual(path.read_bytes(), REG.replace("three", "3").encode())

    def test_refusal_exits_3_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "claim_registry_current.md"
            path.write_bytes(REG.encode())
            ops = Path(tmp) / "ops.json"
            ops.write_text(json.dumps([
                {"op": "replace-within", "id": "CLAIM 001", "old": "one", "new": "1"},
                {"op": "delete", "id": "CLAIM 404"}]))
            done = self.run_tool("apply", "--file", str(path), "--ops", str(ops), "--apply")
            self.assertEqual(done.returncode, 3)
            self.assertIn("ANCHOR_MISSING", done.stderr)
            self.assertEqual(path.read_bytes(), REG.encode())

    def test_real_registry_round_trip_in_a_copy(self):
        source = ROOT / "disease-models/wwox/registries/claim_registry_current.md"
        text = source.read_bytes().decode("utf-8")
        blocks = {b.key: text[b.start:b.end] for b in rr.partition(text, H2)}
        out, _ = rse.apply_ops(text, [op(op="replace", id="CLAIM 006", text=blocks["CLAIM 006"])],
                               H2)
        self.assertEqual(out, text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
