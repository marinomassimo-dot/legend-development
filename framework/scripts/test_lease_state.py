#!/usr/bin/env python3
"""Regression suite for `lease_state.py` — the one mechanized clause of GATE 0.

Why this file exists. `lease_state.py`'s own docstring calls the singleton *"an invariant, not
a finding … checked in EVERY mode and always exits non-zero"*, on Mirror's blocking instruction
(`REV-SUNSET-DEC3-MIRROR-001`). Until this suite existed nothing re-verified that sentence after
an edit: the tool was one of two governance tools with no test and in no release inventory, while
a FROZEN gate reads its exit code as a boolean.

**A PASS without an exercised path to FAIL is not a validation.** Every arm below that asserts a
clean exit is paired with a mutation of the same fixture that must exit non-zero, so a green run
here means the derivation discriminates rather than that it never refuses.

What this suite deliberately does NOT claim. It exercises the singleton **within one record**.
Two ACTIVE leases sitting on two different refs are invisible to this tool by construction — it
reads exactly one file — and no test here can mount that condition. That gap is real, it is
recorded elsewhere as a population problem rather than a derivation problem, and pretending a
green suite covers it would be the more dangerous outcome.

    python3 framework/scripts/test_lease_state.py
"""

from __future__ import annotations

import io
import contextlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lease_state  # noqa: E402


PAST = "2026-01-01T00:00:00Z"
SOON = "2999-01-01T00:00:00Z"
NOW = "2026-08-26T12:00:00Z"


def block(**fields: str) -> str:
    """One LEASE block in the record's own two-space-indented field syntax."""
    lines = ["LEASE:"]
    lines.extend(f"  {key}: {value}" for key, value in fields.items())
    return "\n".join(lines) + "\n"


def record(*blocks: str, preamble: str = "# ORCHESTRATOR LEASE\n\n") -> str:
    return preamble + "\n".join(blocks)


ACTIVE = block(LEASE_ID="1", ACTIVATED_AT="2026-08-20T00:00:00Z",
               EXPIRES_AT=SOON, STATUS="ACTIVE")
RELEASED = block(LEASE_ID="2", ACTIVATED_AT="2026-08-19T00:00:00Z",
                 EXPIRES_AT=SOON, RELEASED_AT="2026-08-19T06:00:00Z", STATUS="RELEASED")
EXPIRED = block(LEASE_ID="3", ACTIVATED_AT="2026-01-01T00:00:00Z",
                EXPIRES_AT=PAST, STATUS="STALE")


class Harness(unittest.TestCase):
    """Run `main()` against a throw-away record and capture verdict, stdout and stderr."""

    def run_tool(self, text: str, *extra: str) -> tuple[int, str, str]:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "orchestrator_lease.md"
            home.write_text(text, encoding="utf-8")
            return self.invoke("--home", str(home), "--now", NOW, *extra)

    def invoke(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = lease_state.main(list(argv))
        return code, out.getvalue(), err.getvalue()


class ValidRecords(Harness):
    def test_one_active_lease_derives_active_and_exits_clean(self) -> None:
        code, out, _ = self.run_tool(record(ACTIVE))
        self.assertEqual(code, 0)
        self.assertIn("ACTIVE by derivation: 1", out)

    def test_a_released_lease_is_terminal_even_before_its_expiry(self) -> None:
        """RELEASED_AT wins over the clock — the first rule of the derivation."""
        code, out, _ = self.run_tool(record(RELEASED))
        self.assertEqual(code, 0)
        self.assertIn("ACTIVE by derivation: 0", out)
        self.assertIn("derived=RELEASED", out)

    def test_released_and_expired_beside_one_active_still_derives_one(self) -> None:
        """NEGATIVE CONTROL for the singleton: three blocks, one live, exit stays 0.

        Without this arm a test that only ever sees one block could not distinguish
        "counts ACTIVE states" from "counts LEASE blocks".
        """
        code, out, _ = self.run_tool(record(RELEASED, EXPIRED, ACTIVE))
        self.assertEqual(code, 0)
        self.assertIn("ACTIVE by derivation: 1", out)

    def test_derivation_is_a_function_of_the_stated_instant(self) -> None:
        """The same record derives ACTIVE before its expiry and STALE after it."""
        text = record(block(LEASE_ID="1", ACTIVATED_AT="2026-08-20T00:00:00Z",
                            EXPIRES_AT="2026-08-26T13:00:00Z", STATUS="ACTIVE"))
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "lease.md"
            home.write_text(text, encoding="utf-8")
            before = self.invoke("--home", str(home), "--now", "2026-08-26T12:00:00Z")
            after = self.invoke("--home", str(home), "--now", "2026-08-26T14:00:00Z")
        self.assertIn("ACTIVE by derivation: 1", before[1])
        self.assertIn("ACTIVE by derivation: 0", after[1])
        self.assertIn("derived=STALE", after[1])


class SingletonInvariant(Harness):
    """The clause GATE 0 reads as a boolean. Every arm here must be able to fail."""

    def test_two_active_leases_exit_three_in_default_mode(self) -> None:
        code, _, err = self.run_tool(record(ACTIVE, ACTIVE))
        self.assertEqual(code, 3, "the singleton must be fatal without --check")
        self.assertIn("INVARIANT VIOLATED", err)

    def test_two_active_leases_exit_three_under_check_too(self) -> None:
        """`--check` must not be able to downgrade the invariant to a finding."""
        code, _, err = self.run_tool(record(ACTIVE, ACTIVE), "--check")
        self.assertEqual(code, 3)
        self.assertIn("INVARIANT VIOLATED", err)

    def test_the_invariant_precedes_the_finding_scan(self) -> None:
        """A record that is BOTH doubly-active and full of findings still exits 3, not 1.

        Ordering matters: a tool that reported findings first would exit 1 on the very
        record whose defect is the one GATE 0 exists to refuse.
        """
        disagreeing = block(LEASE_ID="9", ACTIVATED_AT="2026-08-20T00:00:00Z",
                            EXPIRES_AT=SOON, STATUS="RELEASED")
        code, _, err = self.run_tool(record(disagreeing, ACTIVE), "--check")
        self.assertEqual(code, 3)
        self.assertIn("INVARIANT VIOLATED", err)

    def test_mutation_arm_removing_the_second_active_restores_a_clean_exit(self) -> None:
        """MUTATION: the same fixture minus one ACTIVE block exits 0.

        This is what makes the three arms above evidence rather than assertion — the
        difference between exit 3 and exit 0 is one block, not the harness.
        """
        violating = self.run_tool(record(ACTIVE, ACTIVE))
        repaired = self.run_tool(record(ACTIVE))
        self.assertEqual((violating[0], repaired[0]), (3, 0))


class MalformedAndMissing(Harness):
    """Never guess a lease state: every unreadable input must exit 2."""

    def test_missing_record_exits_two(self) -> None:
        code, _, err = self.invoke("--home", "/nonexistent/orchestrator_lease.md")
        self.assertEqual(code, 2)
        self.assertIn("UNDERIVABLE", err)

    def test_a_file_with_no_lease_block_exits_two(self) -> None:
        code, _, err = self.run_tool("# a record about something else\n\nno blocks here\n")
        self.assertEqual(code, 2)
        self.assertIn("no LEASE block", err)

    def test_wrong_ref_a_readable_file_that_is_not_a_lease_record(self) -> None:
        """WRONG_REF: pointing --home at a real file of the wrong kind must not derive."""
        code, _, err = self.run_tool("---\nrole_contract: orchestrator\n---\n\n# not a lease\n")
        self.assertEqual(code, 2)

    def test_unparseable_timestamp_exits_two(self) -> None:
        code, _, err = self.run_tool(record(block(LEASE_ID="1", EXPIRES_AT="soon-ish")))
        self.assertEqual(code, 2)
        self.assertIn("unparseable timestamp", err)

    def test_a_naive_timestamp_is_refused_rather_than_assumed_utc(self) -> None:
        code, _, err = self.run_tool(record(block(LEASE_ID="1",
                                                  EXPIRES_AT="2026-08-26T00:00:00")))
        self.assertEqual(code, 2)
        self.assertIn("no timezone", err)

    def test_a_block_with_neither_released_at_nor_expires_at_is_underivable(self) -> None:
        code, _, err = self.run_tool(record(block(LEASE_ID="1", STATUS="ACTIVE")))
        self.assertEqual(code, 2)
        self.assertIn("underivable", err)

    def test_mutation_arm_the_same_block_with_a_valid_expiry_derives(self) -> None:
        """MUTATION for the four arms above: add the one missing field and it derives."""
        broken = self.run_tool(record(block(LEASE_ID="1", STATUS="ACTIVE")))
        fixed = self.run_tool(record(block(LEASE_ID="1", STATUS="ACTIVE", EXPIRES_AT=SOON)))
        self.assertEqual((broken[0], fixed[0]), (2, 0))


class StoredStatusIsNeverAuthoritative(Harness):
    """The whole reason the tool exists: STATUS is a derived value stored without its recipe."""

    def test_a_stale_record_claiming_active_derives_stale(self) -> None:
        code, out, _ = self.run_tool(record(EXPIRED))
        self.assertEqual(code, 0)
        self.assertIn("derived=STALE", out)
        self.assertIn("stored=STALE", out)

    def test_disagreement_is_a_finding_under_check_and_silent_without_it(self) -> None:
        """WRONG_HASH analogue: stored field contradicts the derivation.

        Recorded as behaviour, not endorsed: a caller that never passes `--check` cannot
        see the disagreement at all, and its exit code is 0.
        """
        lying = block(LEASE_ID="1", ACTIVATED_AT="2026-08-20T00:00:00Z",
                      EXPIRES_AT=SOON, STATUS="RELEASED")
        silent = self.run_tool(record(lying))
        checked = self.run_tool(record(lying), "--check")
        self.assertEqual(silent[0], 0)
        self.assertEqual(checked[0], 1)
        self.assertIn("DISAGREEMENT", checked[1])

    def test_expired_without_renewal_is_reported_under_check(self) -> None:
        code, out, _ = self.run_tool(record(EXPIRED), "--check")
        self.assertEqual(code, 1)
        self.assertIn("EXPIRED_WITHOUT_RENEWAL", out)

    def test_mutation_arm_a_renewed_expired_lease_is_not_that_finding(self) -> None:
        """MUTATION: LAST_RENEWED distinct from ACTIVATED_AT removes exactly one finding."""
        renewed = block(LEASE_ID="3", ACTIVATED_AT="2026-01-01T00:00:00Z",
                        LAST_RENEWED="2026-02-01T00:00:00Z", EXPIRES_AT=PAST, STATUS="STALE")
        bare = self.run_tool(record(EXPIRED), "--check")
        kept = self.run_tool(record(renewed), "--check")
        self.assertEqual(bare[0], 1)
        self.assertEqual(kept[0], 0, "renewal is the only observable proxy the tool claims")


class ParserBoundaries(Harness):
    """Field syntax the record format depends on, pinned so a tidy-up cannot widen it."""

    def test_a_single_space_indent_is_not_a_field(self) -> None:
        """FIELD requires two or more leading spaces; one space yields an empty block."""
        code, _, err = self.run_tool("LEASE:\n EXPIRES_AT: " + SOON + "\n")
        self.assertEqual(code, 2, "an empty block must be underivable, never ACTIVE")

    def test_a_block_ends_at_the_first_unindented_line(self) -> None:
        text = ("LEASE:\n  LEASE_ID: 1\n  EXPIRES_AT: " + SOON + "\n"
                "\n## prose heading\n  EXPIRES_AT: " + PAST + "\n")
        code, out, _ = self.run_tool(text)
        self.assertEqual(code, 0)
        self.assertIn("ACTIVE by derivation: 1", out)

    def test_a_trailing_comment_is_stripped_from_the_value(self) -> None:
        code, out, _ = self.run_tool(record(block(LEASE_ID="1",
                                                  EXPIRES_AT=SOON + "   # renewed twice")))
        self.assertEqual(code, 0)
        self.assertIn("ACTIVE by derivation: 1", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
