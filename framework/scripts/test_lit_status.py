#!/usr/bin/env python3
"""Regressions for the LIT `Status` vocabulary: validator and migration (`lit_status.py`).

Measured 2026-09-14 before this suite existed (`HARNESS-P-20260914` P9a):
`literature_tracking_log_current.md` declares its own `## Status vocabulary` table of ten values,
and nothing checked a record against it. 397 records; 386 carry `**Status:**` with 28 distinct
raw values; 11 older records carry their state under `**Current status:**`. Outside the table:
17 `processed — complete_fulltext_read`, 1 `processed — partial_fulltext_read`, 17
`completed — [[paper_registry_current#PAPER n]] (…)`, 1 `archived`, and 2 `filtered_in — …`.
LINT validated CLAIM and PAPER statuses and no LIT status at all.

The canonical home of the vocabulary is that table, inside a scientific current file that moves
only through BATCH_COMMIT. So the harness reads it; it does not keep a copy. Expectations below
were fixed before `lit_status.py` existed. The migration is never run against the canonical log
by this suite or by the harness.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

TABLE = """# Literature Tracking Log

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `discovered` | Found by discovery engine, not yet screened |
| `screened` | Quickly reviewed but not yet filtered |
| `filtered_in` | Passed quality + relevance filter, queued for processing |
| `filtered_out` | Excluded — reason logged |
| `processed` | Fully read, tagged, extracted |
| `claim_linked` | Associated with at least one claim in Claim Registry |
| `integrated` | Used to update or support Working Model |
| `flagged_for_review` | Triggered a review flag, not yet resolved |
| `background_only` | Archived as context, no operative function |
| `superseded` | Replaced by a stronger or more recent paper |

---

## Record template

```
## LIT-[NNN]
**Status:**
```
"""

RECORDS = """
## LIT-0001
**Short title:** clean
**Status:** screened
**Next action:** none

## LIT-0002
**Short title:** qualifier
**Status:** processed — complete_fulltext_read
**Next action:** none

## LIT-0003
**Short title:** promoted
**Status:** completed — [[paper_registry_current#PAPER 064]] (`BATCH_20260815_001`)
**Next action:** none

## LIT-0004
**Short title:** old field name
**Current status:** filtered_in — queued per full text
**Next action:** read

## LIT-0005
**Short title:** retracted
**Status:** archived
**Next action:** never use as evidence

## LIT-0006
**Short title:** promoted to an unknown paper
**Status:** completed — [[paper_registry_current#PAPER 999]] (`BATCH_X`)

## LIT-0007
**Short title:** no state at all
**Next action:** none
"""

PAPERS = """# Paper Registry
## PAPER 064
**Identifier:** PMID 21318118
**Status:** processed
"""

LOG = TABLE + RECORDS


class TheVocabularyIsReadFromItsOneHome(unittest.TestCase):
    def setUp(self) -> None:
        import lit_status  # noqa: PLC0415 - absent before the fix, by design
        self.mod = lit_status

    def test_the_vocabulary_is_the_log_table(self) -> None:
        self.assertEqual(
            {"discovered", "screened", "filtered_in", "filtered_out", "processed",
             "claim_linked", "integrated", "flagged_for_review", "background_only",
             "superseded"},
            self.mod.vocabulary(LOG))

    def test_no_table_means_unchecked_not_empty(self) -> None:
        self.assertIsNone(self.mod.vocabulary(RECORDS))

    def test_the_module_keeps_no_copy_of_the_vocabulary(self) -> None:
        """A second copy is how VALID_PAPER_STATES came to restate the same ten values."""
        source = (HERE / "lit_status.py").read_text(encoding="utf-8")
        for value in ("flagged_for_review", "claim_linked", "filtered_out"):
            self.assertNotIn(f'"{value}"', source)

    def test_each_record_is_classified(self) -> None:
        kinds = {r.record: r.kind for r in self.mod.validate(LOG)}
        self.assertEqual({
            "LIT-0001": self.mod.VALID,
            "LIT-0002": self.mod.LEGACY_FORM,
            "LIT-0003": self.mod.LEGACY_FORM,
            "LIT-0004": self.mod.LEGACY_FIELD,
            "LIT-0005": self.mod.NOT_IN_VOCABULARY,
            "LIT-0006": self.mod.LEGACY_FORM,
            "LIT-0007": self.mod.MISSING_STATUS,
        }, kinds)
        self.assertNotIn("LIT-[NNN]", kinds)


class TheMigrationIsConservativeAndLossless(unittest.TestCase):
    def setUp(self) -> None:
        import lit_status  # noqa: PLC0415
        self.mod = lit_status
        self.out, self.report = lit_status.migrate(LOG, PAPERS)

    def record(self, text: str, rid: str) -> str:
        start = text.index(f"## {rid}\n")
        nxt = text.find("\n## ", start + 1)
        return text[start: nxt if nxt != -1 else len(text)]

    def test_a_qualifier_moves_to_a_note_and_the_status_becomes_the_base_value(self) -> None:
        block = self.record(self.out, "LIT-0002")
        self.assertIn("**Status:** processed\n", block)
        self.assertIn("**Status note:** complete_fulltext_read", block)

    def test_a_promotion_takes_the_promoted_paper_status_and_keeps_the_link(self) -> None:
        block = self.record(self.out, "LIT-0003")
        self.assertIn("**Status:** processed\n", block)
        self.assertIn("[[paper_registry_current#PAPER 064]]", block)
        self.assertIn("BATCH_20260815_001", block)

    def test_the_old_field_name_is_renamed(self) -> None:
        block = self.record(self.out, "LIT-0004")
        self.assertIn("**Status:** filtered_in\n", block)
        self.assertNotIn("**Current status:**", block)
        self.assertIn("**Status note:** queued per full text", block)

    def test_a_value_no_table_entry_makes_true_is_left_and_named(self) -> None:
        """`archived` on a retracted primary: `background_only` means context, which a
        retracted paper is not. When no admitted value is true, the defect is the vocabulary,
        and the table is a BATCH_COMMIT change — so the script refuses to choose."""
        self.assertIn("**Status:** archived\n", self.record(self.out, "LIT-0005"))
        self.assertIn("**Status:** completed — [[paper_registry_current#PAPER 999]]",
                      self.record(self.out, "LIT-0006"))
        unmapped = {row["record"] for row in self.report["unmapped"]}
        self.assertEqual({"LIT-0005", "LIT-0006", "LIT-0007"}, unmapped)

    def test_nothing_but_status_lines_changes_and_nothing_is_lost(self) -> None:
        before = LOG.splitlines()
        after = self.out.splitlines()
        removed = [line for line in before if line not in after]
        added = [line for line in after if line not in before]
        self.assertTrue(all(line.startswith(("**Status:**", "**Current status:**")) for line in removed),
                        removed)
        self.assertTrue(all(line.startswith(("**Status:**", "**Status note:**")) for line in added), added)
        for line in removed:
            original = line.split(":**", 1)[1].strip()
            tail = original.split(" — ", 1)[1] if " — " in original else original
            self.assertIn(tail, self.out)

    def test_it_is_idempotent(self) -> None:
        again, report = self.mod.migrate(self.out, PAPERS)
        self.assertEqual(self.out, again)
        self.assertEqual([], report["changed"])

    def test_migrated_records_validate(self) -> None:
        kinds = {r.record: r.kind for r in self.mod.validate(self.out)}
        for rid in ("LIT-0001", "LIT-0002", "LIT-0003", "LIT-0004"):
            self.assertEqual(self.mod.VALID, kinds[rid], rid)

    def test_the_cli_does_not_write_unless_told_to(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "log.md"
            papers = Path(tmp) / "papers.md"
            log.write_text(LOG, encoding="utf-8")
            papers.write_text(PAPERS, encoding="utf-8")
            done = subprocess.run(
                [sys.executable, str(HERE / "lit_status.py"), "migrate", "--log", str(log),
                 "--papers", str(papers)], capture_output=True, text=True)
            self.assertEqual(0, done.returncode, done.stderr)
            self.assertEqual(LOG, log.read_text(encoding="utf-8"))
            self.assertIn("+**Status:** processed", done.stdout)
            written = subprocess.run(
                [sys.executable, str(HERE / "lit_status.py"), "migrate", "--log", str(log),
                 "--papers", str(papers), "--write"], capture_output=True, text=True)
            self.assertEqual(0, written.returncode, written.stderr)
            self.assertNotEqual(LOG, log.read_text(encoding="utf-8"))


class LintValidatesTheLitStatus(unittest.TestCase):
    """The proof of the defect: LINT said nothing about a LIT status outside the table."""

    def test_a_new_value_outside_the_vocabulary_blocks(self) -> None:
        import legend_lint  # noqa: PLC0415
        log = TABLE + "\n## LIT-0900\n**Status:** analyzed\n"
        findings: list = []
        legend_lint._check_lit_statuses(findings, log, grandfathered={})
        blocks = [f for f in findings if f.code == "INVALID_LIT_STATUS"]
        self.assertEqual(1, len(blocks), findings)
        self.assertEqual("BLOCK_BATCH_COMMIT", blocks[0].severity)
        self.assertIn("LIT-0900", blocks[0].message)

    def test_grandfathered_legacy_values_warn_until_migrated(self) -> None:
        import legend_lint  # noqa: PLC0415
        import lit_status  # noqa: PLC0415
        grandfathered = lit_status.legacy_snapshot(LOG)
        findings: list = []
        legend_lint._check_lit_statuses(findings, LOG, grandfathered=grandfathered)
        self.assertFalse([f for f in findings if f.severity.startswith("BLOCK")], findings)
        self.assertTrue([f for f in findings if f.code == "LIT_STATUS_LEGACY"
                         and f.severity == "WARN_BUT_PROCEED"], findings)

    def test_a_grandfathered_record_that_changes_to_another_bad_value_blocks(self) -> None:
        import legend_lint  # noqa: PLC0415
        import lit_status  # noqa: PLC0415
        grandfathered = lit_status.legacy_snapshot(LOG)
        drifted = LOG.replace("**Status:** archived", "**Status:** analyzed")
        findings: list = []
        legend_lint._check_lit_statuses(findings, drifted, grandfathered=grandfathered)
        self.assertTrue([f for f in findings if f.code == "INVALID_LIT_STATUS"
                         and "LIT-0005" in f.message], findings)

    def test_the_committed_snapshot_covers_the_live_log_exactly(self) -> None:
        """Grandfathering is by identity AND value, so the snapshot can only shrink."""
        import lit_status  # noqa: PLC0415
        live = (HERE.parents[1] / "disease-models/wwox/registries/"
                "literature_tracking_log_current.md")
        if not live.is_file():
            self.skipTest("no live log in this checkout")
        committed = json.loads((HERE / "lit_status_legacy.json").read_text(encoding="utf-8"))
        current = lit_status.legacy_snapshot(live.read_text(encoding="utf-8"))
        self.assertTrue(set(current.items()) <= set(committed["records"].items()),
                        sorted(set(current.items()) - set(committed["records"].items())))


if __name__ == "__main__":
    unittest.main(verbosity=2)
