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

    def test_the_last_record_of_every_registry_reaches_eof_and_only_one_is_refused(self) -> None:
        """🔴 THE REFUSAL MUST NOT BE BLUNT, measured on the live files, not reasoned about.

        `BLOCK 3`, `PAPER 118` and `LIT-0420` are ALL EOF-spanning — the last record of every
        registry is, by construction — and BATCH_20260928_002 edited the latter two legitimately.
        A refusal keyed on "the span reaches EOF" alone would have refused two of that batch's
        nine ops, and editing the newest PAPER or LIT record is the commonest edit here. What
        makes the difference is whether the assumed tail COVERS anything: only `BLOCK 3` does.
        """
        cases = (("working_model_current.md", "BLOCK 3", (1,), True),
                 ("paper_registry_current.md", "PAPER 118", (2,), False),
                 ("literature_tracking_log_current.md", "LIT-0420", (2,), False))
        for name, record, levels, refused in cases:
            path = ROOT / "disease-models/wwox/registries" / name
            text = path.read_bytes().decode("utf-8")
            span = rse.resolve(text, op(op="replace", id=record), levels)
            with self.subTest(record):
                self.assertTrue(span.to_eof, f"{record} must be the EOF-spanning last record")
                self.assertEqual(span.end, len(text))
                # the commonest edit in the repository: a replace-within on the newest record
                needle = text[span.start:span.start + 24]
                ops = [op(op="replace-within", id=record, old=needle, new=needle)]
                if refused:
                    self.assertNotEqual(span.swallowed, ())
                    with self.assertRaises(rse.Refusal) as caught:
                        rse.apply_ops(text, ops, levels)
                    self.assertEqual(caught.exception.code, "UNBOUNDED_SPAN")
                else:
                    self.assertEqual(span.swallowed, (),
                                     f"{record} covers nothing, so nothing may be refused")
                    out, report = rse.apply_ops(text, ops, levels)
                    self.assertEqual(out, text)
                    self.assertTrue(report.ops[0]["span_end_assumed"],
                                    "the assumed end is still REPORTED where it is not refused")
                    self.assertEqual([], report.ops[0]["span_swallows"])

    def test_appending_to_the_genuinely_last_record_of_each_registry_still_works(self) -> None:
        """The other half of the same guarantee, on all three real files: a new PAPER / LIT /
        BLOCK still lands after the record that is currently last."""
        cases = (("working_model_current.md", (1,), "# BLOCK 9 — test\nx\n"),
                 ("paper_registry_current.md", (2,), "## PAPER 999\n**Identifier:** PMID 1\n"),
                 ("literature_tracking_log_current.md", (2,), "## LIT-9999\n**Status:** x\n"))
        for name, levels, block in cases:
            path = ROOT / "disease-models/wwox/registries" / name
            text = path.read_bytes().decode("utf-8")
            with self.subTest(name):
                out, _ = rse.apply_ops(text, [op(op="append", text="\n---\n\n" + block)], levels)
                self.assertTrue(out.startswith(text))
                self.assertTrue(out.endswith(block))


TWO_PURPOSES = """# Paper Registry Current

## Purpose
first purpose

## PAPER 001
PMID-free body

# Triage Corpus

## Purpose
second purpose

## PAPER 002
another body
"""


class HeadingUnderItsParent(unittest.TestCase):
    """Benchmark J · J5: `--under` names the enclosing heading of a duplicated section heading."""

    def test_the_bare_heading_is_still_refused(self):
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(TWO_PURPOSES, [op(op="replace-within", heading="Purpose",
                                            old="first", new="1st")], H2)
        self.assertEqual(caught.exception.code, "ANCHOR_AMBIGUOUS")

    def test_under_reaches_one_section_and_leaves_its_twin_byte_equal(self):
        for parent, old, new in (("Paper Registry Current", "first purpose", "first aim"),
                                 ("Triage Corpus", "second purpose", "second aim")):
            with self.subTest(parent=parent):
                out, _ = rse.apply_ops(TWO_PURPOSES, [op(
                    op="replace-within", heading="Purpose", under=parent, old=old, new=new)], H2)
                self.assertEqual(out, TWO_PURPOSES.replace(old, new))

    def test_an_insert_after_the_qualified_section_lands_under_that_parent(self):
        out, _ = rse.apply_ops(TWO_PURPOSES, [op(
            op="insert-after", heading="Purpose", under="Triage Corpus",
            text="## Legend\nadded\n\n")], H2)
        self.assertEqual(out, TWO_PURPOSES.replace("second purpose\n\n",
                                                   "second purpose\n\n## Legend\nadded\n\n"))

    def test_a_parent_that_does_not_enclose_it_is_missing(self):
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(TWO_PURPOSES, [op(op="replace-within", heading="Purpose",
                                            under="PAPER 001", old="first", new="1st")], H2)
        self.assertEqual(caught.exception.code, "ANCHOR_MISSING")

    def test_under_alone_names_nothing(self):
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(TWO_PURPOSES, [op(op="append", under="Triage Corpus", text="x\n")], H2)
        self.assertEqual(caught.exception.code, "ANCHOR_MISSING")

    def test_two_hits_under_one_parent_stay_ambiguous(self):
        doubled = TWO_PURPOSES + "\n## Purpose\nthird purpose\n"
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(doubled, [op(op="replace-within", heading="Purpose",
                                       under="Triage Corpus", old="third", new="3rd")], H2)
        self.assertEqual(caught.exception.code, "ANCHOR_AMBIGUOUS")

    def test_the_command_line_and_an_ops_file_both_carry_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "paper_registry_current.md"
            path.write_bytes(TWO_PURPOSES.encode())
            done = subprocess.run(
                [sys.executable, str(TOOL), "replace-within", "--file", str(path), "--heading",
                 "Purpose", "--under", "Triage Corpus", "--old", "second", "--new", "2nd",
                 "--apply"], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertEqual(path.read_text(), TWO_PURPOSES.replace("second", "2nd"))
            ops = Path(tmp) / "ops.json"
            ops.write_text(json.dumps([{"op": "replace-within", "heading": "Purpose",
                                        "under": "Paper Registry Current", "old": "first",
                                        "new": "1st"}]))
            done = subprocess.run([sys.executable, str(TOOL), "apply", "--file", str(path),
                                   "--ops", str(ops), "--apply"], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertEqual(path.read_text(),
                             TWO_PURPOSES.replace("second", "2nd").replace("first", "1st"))


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


class TheDocumentedRefusalConditionIsTheImplementedOne(unittest.TestCase):
    """🔴 `UNBOUNDED_SPAN` is keyed on COVERING HEADINGS, never on reaching EOF.

    The shipped condition is right and `Op.to_eof`'s documentation described a stricter tool
    than the one that ships — "an op on a span whose end the file does not state" — which is the
    overbroad design someone could re-implement from the text alone. It would refuse the
    commonest edit in the repository, because the LAST record of every registry reaches EOF.
    This case pins the doc to the behaviour the cases above already pin.
    """

    def test_the_to_eof_documentation_names_the_headings_condition(self) -> None:
        # The attribute docstring is not introspectable, so the source of the class is read.
        source = (Path(rse.__file__).read_text(encoding="utf-8")
                  .split("to_eof: bool = False", 1)[1].split('"""')[1])
        self.assertIn("COVERING HEADINGS", source)
        self.assertNotIn("Only then may an op", source)
        self.assertIn("swallowed", source,
                      "the doc must point at the predicate a reader can check")

    def test_and_the_behaviour_it_documents(self) -> None:
        """The same claim, executed: EOF alone does not refuse; a covered heading does."""
        reaches_eof = "## CLAIM 001\nbody\n\n---\n\n## CLAIM 002\nbody two\n"
        rse.apply_ops(reaches_eof,
                      [op(op="replace-within", id="CLAIM 002", old="two", new="2")], H2)
        covers_a_heading = reaches_eof + "\n### A sub-heading the record may not own\nx\n"
        span = rse.resolve(covers_a_heading, op(op="replace", id="CLAIM 002"), H2)
        self.assertTrue(span.to_eof)
        self.assertNotEqual(span.swallowed, ())
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(covers_a_heading,
                          [op(op="replace-within", id="CLAIM 002", old="two", new="2")], H2)
        self.assertEqual(caught.exception.code, "UNBOUNDED_SPAN")


class CrossLineMove(unittest.TestCase):
    """🔴 The `B2` shape: content re-parented from one statement of a record onto another.

    `BATCH_20260928_005` op `B2` survived a full batch cycle because every proof this repository
    runs is about the record's OUTSIDE. These fixtures are built so the defect can actually occur
    — two real statement lines, a real ≥ 200-byte run moving verbatim from one to the other — and
    the passes are built from the edits that must stay possible: a line changing length, an
    append, a reorder, a blockquote, a deletion.
    """

    #: The 488 bytes `B2` moved, in the shape it moved them: the grounds of a `DO_NOT_INFER`
    #: prohibition, which argue about a null/wild-type genotype.
    GROUNDS = (
        "L'evidenza di questa claim e il topo `Wwox^+/-` e i portatori umani: un genotipo "
        "**null/wild-type**, con un allele **pienamente funzionale**. La classe che sopravvive "
        "meglio in `CLAIM 033` porta **un allele missense** di funzione residua **non misurata**. "
        "Concatenarle in un allele basta implica una equivalenza funzionale che nessuna delle due "
        "fonti misura, e la catena e percio vietata in qualunque eterozigote WWOX."
    )
    INFER = ("[RED] **`DO_NOT_INFER` (2026-09-27, `CENSUS-03`) — questa claim e `CLAIM 033` "
             "concordano, e proprio per questo la catena fra loro e vietata.**")
    CITE = ("[RED] **`DO_NOT_CITE` — the `P47T/WT` heterozygote is not a demonstrated negative "
            "for haploinsufficiency.** Three separate reasons, each sufficient on its own, and "
            "a REVIVAL_TRIGGER: a powered survival comparison in that genotype.")

    def record(self, *lines: str) -> str:
        return "## CLAIM 032\n**Title:** thirty-two\n" + "".join(f"{line}\n" for line in lines)

    def file(self, *lines: str) -> str:
        return self.record(*lines) + "\n---\n\n## CLAIM 033\n**Title:** thirty-three\n"

    def block(self, text: str) -> str:
        """The addressed record's own span, separator included, as `replace` must be given it."""
        return text[:text.index("## CLAIM 033")]

    def test_the_grounds_are_long_enough_for_the_fixture_to_exhibit_the_defect(self) -> None:
        """A suite whose fixture is under the floor proves nothing about the floor."""
        self.assertGreaterEqual(len(self.GROUNDS.encode()), rse.MOVED_BYTES_FLOOR)

    def test_b2_is_refused(self) -> None:
        """Two statements in one record, N bytes moving from one to the other, total conserved."""
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        after = self.file(self.INFER, f"{self.CITE} {self.GROUNDS}")
        self.assertEqual(len(before.encode()), len(after.encode()),
                         "the fixture must be byte-conserving, or it is not the B2 shape")
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                      text=self.block(after))], H2)
        self.assertEqual(caught.exception.code, "CROSS_LINE_MOVE")
        self.assertIn("reflow", str(caught.exception))

    def test_b2_as_it_actually_happened_is_refused(self) -> None:
        """`da250b5`: a NEW statement spliced INSIDE an existing line, whose tail it re-parents.

        Not byte-conserving — the new prohibition is new prose — which is why a check keyed on the
        record's total would have caught only the repair and not the op that did the damage. What
        moved is the 488 bytes of grounds, and that is what is detected.
        """
        before = self.file(f"{self.INFER} {self.GROUNDS}")
        after = self.file(self.INFER, f"{self.CITE} {self.GROUNDS}")
        self.assertNotEqual(len(before.encode()), len(after.encode()))
        with self.assertRaises(rse.Refusal) as caught:
            rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                      text=self.block(after))], H2)
        self.assertEqual(caught.exception.code, "CROSS_LINE_MOVE")

    def test_reflow_is_the_declared_escape(self) -> None:
        """The escape exists, is explicit, and is recorded in the op report."""
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        after = self.file(self.INFER, f"{self.CITE} {self.GROUNDS}")
        out, report = rse.apply_ops(
            before, [op(op="replace", id="CLAIM 032", reflow=True, text=self.block(after))], H2)
        self.assertEqual(out, after)
        self.assertTrue(report.ops[0]["reflow_asserted"])

    def test_reflow_arrives_through_an_ops_file(self) -> None:
        """`propagate` reads an ops file, so the declaration must survive `Op.from_dict`."""
        self.assertTrue(rse.Op.from_dict({"op": "replace", "id": "X", "reflow": True}).reflow)
        self.assertFalse(rse.Op.from_dict({"op": "replace", "id": "X"}).reflow)

    def test_a_replace_within_that_changes_a_line_length_passes(self) -> None:
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        out, report = rse.apply_ops(before, [op(op="replace-within", id="CLAIM 032",
                                                old="vietata.**", new="vietata e lo resta.**")],
                                    H2)
        self.assertIn("vietata e lo resta", out)
        # heading, Title, the two prohibitions, and the trailing `---` the span carries.
        self.assertEqual(report.ops[0]["lines"], [5, 5])

    def test_adding_a_line_passes(self) -> None:
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        after = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE, "**Wikilinks:** none")
        out, _report = rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                                 text=self.block(after))], H2)
        self.assertEqual(out, after)

    def test_a_line_relocated_intact_is_a_reorder_and_passes(self) -> None:
        before = self.file(self.INFER, self.CITE, "**Wikilinks:** none")
        after = self.file(self.CITE, self.INFER, "**Wikilinks:** none")
        out, _report = rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                                 text=self.block(after))], H2)
        self.assertEqual(out, after)

    def test_blockquoting_a_line_does_not_move_it(self) -> None:
        """`419b6803` prefixed `> ` onto an existing flag; the statement did not move."""
        long_line = f"{self.INFER} {self.GROUNDS}"
        before = self.file(long_line, self.CITE)
        after = self.file(f"> {long_line}", self.CITE)
        out, _report = rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                                 text=self.block(after))], H2)
        self.assertEqual(out, after)

    def test_a_deletion_is_not_a_move_when_no_line_gained_the_text(self) -> None:
        """Both halves are required: text that leaves and arrives nowhere is a deletion."""
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        after = self.file(self.INFER, self.CITE)
        out, _report = rse.apply_ops(before, [op(op="replace", id="CLAIM 032",
                                                 text=self.block(after))], H2)
        self.assertEqual(out, after)

    def test_the_floor_is_load_bearing_in_both_directions(self) -> None:
        """Under the floor a move passes; over it, it is refused. The constant is not decoration."""
        for payload, expected in (("x" * 150, None), ("y" * 250, "CROSS_LINE_MOVE")):
            before = self.file(f"{self.INFER} {payload}", self.CITE)
            after = self.file(self.INFER, f"{self.CITE} {payload}")
            ops = [op(op="replace", id="CLAIM 032", text=self.block(after))]
            if expected is None:
                rse.apply_ops(before, ops, H2)
                continue
            with self.assertRaises(rse.Refusal) as caught:
                rse.apply_ops(before, ops, H2)
            self.assertEqual(caught.exception.code, expected)

    def test_the_floor_records_what_it_was_measured_against(self) -> None:
        """A constant with no measurement beside it is a constant the next reader will retune."""
        source = Path(rse.__file__).read_text(encoding="utf-8")
        comment = source.split("MOVED_BYTES_FLOOR = 200")[0].rsplit("SEPARATOR_RUN", 1)[1]
        for token in ("j0_corpus.json", "72 historical", "120 B", "da250b5"):
            self.assertIn(token, comment,
                          "the floor must carry the replay it was chosen from")

    def test_the_rejected_invariants_are_executed_and_not_merely_argued(self) -> None:
        """`B2` leaves both the paragraph count and the line count unchanged; content moved."""
        before = self.file(f"{self.INFER} {self.GROUNDS}", self.CITE)
        after = self.file(self.INFER, f"{self.CITE} {self.GROUNDS}")
        self.assertEqual(before.count("\n\n"), after.count("\n\n"))
        self.assertEqual(len(rse.statement_lines(before)), len(rse.statement_lines(after)))
        self.assertTrue(rse.cross_line_moves(before, after))


if __name__ == "__main__":
    unittest.main(verbosity=1)
