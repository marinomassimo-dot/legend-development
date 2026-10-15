#!/usr/bin/env python3
"""The op-count reconciliation refuses the silent zero and the mismatch, and reads every authoring
format BATCH_20261004_007 received — plus the two the same month's candidates added.

Each fixture below is cut down from a real candidate of the 2026-10-02 .. 2026-10-04 waves, with
the scientific text replaced by placeholders; the STRUCTURE is what is under test. The last class
runs the tool over the batch's own twenty candidates on disk, which is the population it was
written for: none of them may be refused, and the two no-op candidates must read as NO_OPS, not
as SILENT_ZERO."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import candidate_ops_reconcile as cor  # noqa: E402

ROOT = HERE.parents[1]
SCRIPT = HERE / "candidate_ops_reconcile.py"
CANDIDATES = ROOT / "disease-models" / "wwox" / "research" / "commit_candidates"

FORMAT_A = """# CC-TEST-A

**Target records:** `claim_registry_current.md` `CLAIM 032`: two `replace-within` ops on carrier observation (b).

## Op list — claim_registry_current.md (record-scoped)

```json
[
 {"op": "replace-within", "id": "CLAIM 032", "old": "alpha", "new": "alpha [corrected]"},
 {"op": "replace-within", "id": "CLAIM 032", "old": "beta", "new": "beta [corrected]"}
]
```
"""

FORMAT_B = """# CC-TEST-B

**Target records:** `paper_registry_current.md` `PAPER 213` (two `replace-within` ops on its Role field).

## 2 - Ops (record-scoped)

### Op 1 - `PAPER 213`, `replace-within` (Role)
- `old` (verbatim, measured unique in the file): `the spinal cord was injured`
- `new`: `the spinal cord was injured (8 animals)`

### Op 2 - `PAPER 213`, `replace-within` (Role)
- `old` (verbatim, measured unique in the file): `was not reported`
- `new`: `was not reported (no ganglion panel)`

## 4 - Defaults taken
- nothing else
"""

FORMAT_B_UNNUMBERED_WITH_APPEND = """# CC-TEST-B2

**Target records:** `claim_registry_current.md` `CLAIM 047` (one `replace-within`), `discovery_ledger_current.md` `DL-METH-120` (one `append`).

## 3 - Op (record-scoped)
`CLAIM 047`, `replace-within` (paragraph "Bound"):
- `old` (verbatim, measured unique in CLAIM 047 and in the file): `covering **five** NHP studies)`
- `new`: `covering **five** NHP studies; re-read every panel)`

### Op 2 - `DL-METH-120`, `APPEND` (after the last bullet before Links)
`- 🟢 **Append-only, 2026-10-04:** the silence survives a term search.`

## 4 - Defaults taken
"""

FORMAT_C_TABLE = """# CC-TEST-C

Record-scoped, one op per statement. All three ops (2 + 1) were dry-run.

## 2 · Ops

### 2.1 `disease-models/wwox/registries/paper_registry_current.md` — record `CORPUS P263`

| # | op | old (verbatim, unique in record) | new |
|---|---|---|---|
| P1 | replace-within | `**Status:** screened` | `**Status:** read` |
| P2 | replace-within | `**Model/species:** rat` | `**Model/species:** review` |

### 2.2 `disease-models/wwox/research/full_text_queue_current.md` — record `FT-142`

| # | op | old | new |
|---|---|---|---|
| Q1 | replace-within | `Neither paper is a WWOX paper.` | `Neither paper is a WWOX-function paper.` |
"""

FORMAT_C_FENCES = """# CC-TEST-C2

## 2 · Ops — file `disease-models/wwox/registries/literature_tracking_log_current.md`, record `LIT-0306`

### 2.1 · `Status`

```
**Status:** screened
```

```
**Status:** background_only
```

### 2.2 · `Flags`

```
flag: none
```

```
flag: provenance map
```
"""

FORMAT_VTABLE = """# CC-TEST-V

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/research/discovery_ledger_current.md`, record `DL-MECH-114`

| field | value |
|---|---|
| op | `replace` |
| old | `the grading is in an unread supplement` |
| new | `the grading is not printed in the paper` |

| field | value |
|---|---|
| op | `replace` |
| old | `both unread` |
| new | `both read` |

## BATCH DISPOSITION
All six ops applied as declared.
"""

SILENT_ZERO = """# CC-TEST-Z

**Target records:** `claim_registry_current.md` `CLAIM 010` (three `replace-within` ops).

## Ops

The three edits are described in prose below, in a layout nobody parses.

First, in `CLAIM 010` replace the status line. Second, replace the summary. Third, the boundary.
"""

GENUINE_NO_OPS = """# CC-TEST-N

**Status:** `PROPOSED — NOT PROPAGATED` · **outcome: NO OPS**

## Why this file exists
The registry already carries the finding, so the absence of ops is a finding rather than an omission.

## Op list
None.
"""

DRY_RUN_ECHO = """# CC-TEST-E

## Op list

```json
[{"op": "replace-within", "id": "DIS-028", "old": "x", "new": "y"},
 {"op": "replace-within", "id": "DIS-029", "old": "p", "new": "q"}]
```

Dry runs: both `DRY RUN — nothing written; 1 op(s)`, at commit `b07016a0`.
"""


def write(tmp: Path, name: str, text: str) -> Path:
    p = tmp / name
    p.write_text(text, encoding="utf-8")
    return p


class EveryObservedFormatIsRead(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def check(self, text: str, parsed: int, verdict: str, formats: set[str] | None = None) -> dict:
        r = cor.reconcile(write(self.tmp, "c.md", text))
        self.assertEqual((r["ops_parsed"], r["verdict"]), (parsed, verdict), json.dumps(r, indent=1)[:1500])
        if formats is not None:
            self.assertEqual(set(r["formats"]), formats)
        return r

    def test_a_fenced_json_op_array(self) -> None:
        r = self.check(FORMAT_A, 2, "MATCH", {"A"})
        self.assertEqual([o["id"] for o in r["ops"]], ["CLAIM 032", "CLAIM 032"])

    def test_b_numbered_op_headings_with_old_new_bullets(self) -> None:
        r = self.check(FORMAT_B, 2, "MATCH", {"B-bullets"})
        self.assertEqual(r["ops"][1]["old"], "was not reported")

    def test_b_unnumbered_op_heading_record_on_next_line_and_an_append(self) -> None:
        """`## 3 - Op (record-scoped)` with the record on the body's first line, then an APPEND with no
        old/new pair; the declaration «(one `replace-within`), ... (one `append`)» sums to two."""
        r = self.check(FORMAT_B_UNNUMBERED_WITH_APPEND, 2, "MATCH")
        self.assertEqual([(o["op"], o["id"]) for o in r["ops"]],
                         [("replace-within", "CLAIM 047"), ("append", "DL-METH-120")])

    def test_c_numbered_headings_over_a_table_one_op_per_row(self) -> None:
        r = self.check(FORMAT_C_TABLE, 3, "MATCH", {"C-table"})
        self.assertEqual([o["id"] for o in r["ops"]], ["CORPUS P263", "CORPUS P263", "FT-142"])

    def test_c_numbered_headings_over_paired_fences_record_from_the_parent_heading(self) -> None:
        r = self.check(FORMAT_C_FENCES, 2, "UNDECLARED", {"C-fences"})
        self.assertEqual({o["id"] for o in r["ops"]}, {"LIT-0306"})
        self.assertFalse(r["refused"])
        self.assertTrue(cor.reconcile(write(self.tmp, "s.md", FORMAT_C_FENCES), strict=True)["refused"])

    def test_vertical_field_tables_one_op_per_op_row(self) -> None:
        """Two vertical tables under one N.M heading are two ops; the disposition's «six» is a
        MISMATCH against them — the Thomsen case, where the file carries one more op than the
        disposition says were applied."""
        r = self.check(FORMAT_VTABLE, 2, "MISMATCH", {"C-vtable"})
        self.assertTrue(r["refused"])


class TheTwoDangerousOutcomesAreRefused(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def test_silent_zero_is_refused_not_reported_as_processed(self) -> None:
        r = cor.reconcile(write(self.tmp, "z.md", SILENT_ZERO))
        self.assertEqual((r["ops_parsed"], r["verdict"], r["refused"]), (0, "SILENT_ZERO", True))

    def test_a_genuinely_op_less_candidate_is_not_a_silent_zero(self) -> None:
        r = cor.reconcile(write(self.tmp, "n.md", GENUINE_NO_OPS))
        self.assertEqual((r["verdict"], r["refused"]), ("NO_OPS", False))

    def test_a_dry_run_echo_is_not_a_declaration(self) -> None:
        """`1 op(s)` is record_scoped_edit's own output quoted back; counting it would turn a
        two-op candidate into a MISMATCH against a number nobody declared."""
        r = cor.reconcile(write(self.tmp, "e.md", DRY_RUN_ECHO))
        self.assertEqual((r["ops_parsed"], r["declared"], r["verdict"]), (2, [], "UNDECLARED"))

    def test_the_cli_exit_code_carries_the_refusal(self) -> None:
        z = write(self.tmp, "z.md", SILENT_ZERO)
        a = write(self.tmp, "a.md", FORMAT_A)
        ok = subprocess.run([sys.executable, str(SCRIPT), str(a)], capture_output=True, text=True)
        bad = subprocess.run([sys.executable, str(SCRIPT), str(a), str(z)], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertEqual(bad.returncode, 3, bad.stdout + bad.stderr)
        self.assertIn("SILENT_ZERO", bad.stdout)

    def test_ops_out_writes_apply_shaped_ops_without_private_keys(self) -> None:
        a = write(self.tmp, "a.md", FORMAT_A)
        out = self.tmp / "ops.json"
        subprocess.run([sys.executable, str(SCRIPT), "--ops-out", str(out), str(a)], check=True,
                       capture_output=True, text=True)
        ops = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(len(ops), 2)
        self.assertFalse(any(k.startswith("_") for o in ops for k in o))


class TheBatchItWasWrittenForIsNotRefused(unittest.TestCase):
    """The twenty candidates of BATCH_20261004_007, on disk."""

    def test_population_is_present(self) -> None:
        self.assertTrue(sorted(CANDIDATES.glob("CC-20261004W13-*.md")), f"no W13 candidates under {CANDIDATES}")

    def test_no_batch_007_candidate_is_refused_and_the_no_op_ones_read_as_no_ops(self) -> None:
        verdicts = {p.name: cor.reconcile(p)["verdict"] for p in sorted(CANDIDATES.glob("CC-20261004W13-*.md"))}
        refused = {k: v for k, v in verdicts.items() if v in ("SILENT_ZERO", "MISMATCH")}
        self.assertEqual({}, refused)
        self.assertEqual(verdicts.get("CC-20261004W13-A-REGISTRY-01.md"), "NO_OPS")
        self.assertGreaterEqual(sum(v == "MATCH" for v in verdicts.values()), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
