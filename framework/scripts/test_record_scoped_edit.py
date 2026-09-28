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


#: The real `working_model_current.md` shape: identity level 1, three `#` BLOCKs, and the file's
#: own `##` sections — `Changelog` among them — sitting after the LAST `#` BLOCK with no `#`
#: heading to close it. `id: BLOCK 3` therefore spanned to EOF and covered the whole changelog.
WM = """# Working Model Current

> not medical advice

# BLOCK 1 — one-pager
**Version:** WM_v7.1

---

# BLOCK 2 — claim mirror
| id | claim |
|---|---|
| 001 | x |

---

# BLOCK 3 — flowchart logic summary
step one

## Monitoring endpoints
an endpoint

## Changelog

a historical row

## BATCH_20260928_001 — WM_v7.0 → WM_v7.1
what that batch did
"""


class UnboundedSpan(unittest.TestCase):
    """The last block at its level has no following heading, so its end was ASSUMED to be EOF.
    An assumed end that covers headings is not a record boundary and must not pass silently."""

    LEVELS = (1,)

    def refusal(self, ops, text=WM, levels=None):
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(text, ops, levels or self.LEVELS)
        return caught.exception

    def test_the_span_is_measured_and_reported(self):
        span = rse.resolve(WM, op(op="replace", id="BLOCK 3"), self.LEVELS)
        self.assertEqual(span.end, len(WM))
        self.assertTrue(span.to_eof)
        self.assertEqual([t for _lv, t in span.swallowed],
                         ["Monitoring endpoints", "Changelog",
                          "BATCH_20260928_001 — WM_v7.0 → WM_v7.1"])
        # a block whose end the file DOES state is bounded and carries nothing
        bounded = rse.resolve(WM, op(op="replace", id="BLOCK 2"), self.LEVELS)
        self.assertFalse(bounded.to_eof)
        self.assertEqual(bounded.swallowed, ())

    def test_every_end_sensitive_op_on_the_last_record_is_refused(self):
        for one in (op(op="replace", id="BLOCK 3", text="# BLOCK 3 — flowchart logic summary\nx\n"),
                    op(op="replace-within", id="BLOCK 3", old="step one", new="step 1"),
                    op(op="delete", id="BLOCK 3"),
                    op(op="insert-after", id="BLOCK 3", text="# BLOCK 4 — new\nx\n")):
            with self.subTest(one.op):
                refusal = self.refusal([one])
                self.assertEqual(refusal.code, "UNBOUNDED_SPAN", str(refusal))
                self.assertIn("## Changelog", str(refusal))

    def test_an_edit_anchored_on_the_last_record_could_reach_the_changelog(self):
        """The defect, not merely its symptom: without the refusal, `id: BLOCK 3` edits the
        changelog, because the changelog is inside the span the tool called BLOCK 3."""
        refusal = self.refusal([op(op="replace-within", id="BLOCK 3", old="a historical row",
                                   new="a rewritten row")])
        self.assertEqual(refusal.code, "UNBOUNDED_SPAN")
        out, _ = rse.apply_ops(WM, [op(op="replace-within", id="BLOCK 3", to_eof=True,
                                       old="a historical row", new="a rewritten row")],
                               self.LEVELS)
        self.assertIn("a rewritten row", out)   # --to-eof is the caller SAYING it meant this

    def test_to_eof_lifts_the_refusal_and_the_report_says_it_was_asserted(self):
        _out, report = rse.apply_ops(WM, [op(op="replace-within", id="BLOCK 3", to_eof=True,
                                             old="step one", new="step 1")], self.LEVELS)
        self.assertTrue(report.ops[0]["span_end_assumed"])
        self.assertTrue(report.ops[0]["to_eof_asserted"])
        self.assertIn("## Changelog", report.ops[0]["span_swallows"])

    def test_eof_really_is_the_end_when_nothing_follows(self):
        """A genuinely-last record with no heading after it is not refused: the assumption is
        only unsafe where there is something to be wrong about."""
        plain = "## CLAIM 001\n**Title:** one\n\n---\n\n## CLAIM 002\n**Title:** two\n"
        span = rse.resolve(plain, op(op="replace", id="CLAIM 002"), H2)
        self.assertTrue(span.to_eof)
        self.assertEqual(span.swallowed, ())
        out, report = rse.apply_ops(plain, [op(op="replace-within", id="CLAIM 002", old="two",
                                               new="2")], H2)
        self.assertEqual(out, plain.replace("two", "2"))
        self.assertFalse(report.ops[0]["to_eof_asserted"])

    def test_appending_to_a_genuinely_last_record_still_works(self):
        out, _ = rse.apply_ops(WM, [op(op="append", text="\n---\n\n# BLOCK 4 — new\nx\n")],
                               self.LEVELS)
        self.assertTrue(out.endswith("# BLOCK 4 — new\nx\n"))
        # and a new neighbour may still be put BEFORE the unbounded record: insert-before uses
        # only the block's start, which the file does state.
        out2, _ = rse.apply_ops(WM, [op(op="insert-before", id="BLOCK 3",
                                        text="# BLOCK 2b — new\nx\n\n---\n\n")], self.LEVELS)
        self.assertIn("# BLOCK 2b — new", out2)

    def test_the_sub_block_remains_addressable_by_its_own_heading(self):
        """The refusal's first remedy: `## Changelog` has its own bounded span."""
        span = rse.resolve(WM, op(op="replace", heading="Changelog"), self.LEVELS)
        self.assertFalse(span.to_eof)
        out, _ = rse.apply_ops(WM, [op(op="replace-within", heading="Changelog",
                                       old="a historical row", new="a corrected row")],
                              self.LEVELS)
        self.assertEqual(out, WM.replace("a historical row", "a corrected row"))

    def test_a_nested_record_in_the_tail_is_still_the_sharper_refusal(self):
        text = "# Title\n\n## CLAIM 001\nx\n"
        self.refusal([op(op="delete", heading="Title")], text=text, levels=H2)
        self.assertEqual(self.refusal([op(op="delete", heading="Title")], text=text,
                                      levels=H2).code, "NESTED_RECORD")

    def test_the_live_working_model_exhibits_the_shape(self):
        """Not a fixture: the canonical file this defect was measured on."""
        source = ROOT / "disease-models/wwox/registries/working_model_current.md"
        text = source.read_bytes().decode("utf-8")
        span = rse.resolve(text, op(op="replace", id="BLOCK 3"), (1,))
        self.assertTrue(span.to_eof)
        self.assertEqual(span.end, len(text))
        self.assertIn("Changelog", [t for _lv, t in span.swallowed])
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(text, [op(op="replace-within", id="BLOCK 3", old="Changelog",
                                    new="Changelog")], (1,))
        self.assertEqual(caught.exception.code, "UNBOUNDED_SPAN")
        # and the records at the end of the other canonical surfaces are NOT affected
        for name, levels in (("claim_registry_current", (2,)), ("paper_registry_current", (2,)),
                             ("literature_tracking_log_current", (2,))):
            other = (ROOT / f"disease-models/wwox/registries/{name}.md").read_bytes().decode()
            last = rse.identity_headings(other, levels)[-1]
            with self.subTest(name):
                self.assertEqual(rse._span_from(other, last[0], last[1], last[2],
                                                "record").swallowed, ())


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
