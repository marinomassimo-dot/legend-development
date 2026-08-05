#!/usr/bin/env python3
"""Closed-world assertions about append-only state go stale in silence.

Four times in two days, the same defect: a value measured when the code was written, frozen
as a literal, which stopped being true and broke nothing. The exporter's
`basis_is_exportable = False`, and three tests pinning `PMID 32000863 has no receipt`,
`the projection is exactly {"055","056"}`, `the row count is 2`. Each was true when written.
Each was silently false afterwards. `HonestEmptiness` in the DisMech exporter's own test suite
already carried the warning in a docstring — *"a test that breaks when data legitimately
changes was testing the data"* — and the warning did not prevent four recurrences in the same
repository. A rule that is only written down is not a mechanism.

**The rule, and why it is exactly this rule.** LEGEND's state grows by appending: the receipt
ledger, the registries, the queues. On append-only state the two directions are not symmetric,
the same way `epistemic_discipline` says positives and negatives are not symmetric:

  * `X has a complete receipt`      — once true, stays true. Safe to pin.
  * `X has NO complete receipt`     — becomes false the moment X is read. Never safe to pin.
  * `the set is exactly {A, B}`     — closed world; false when C is added. Never safe to pin.
  * `the count is N`                — the same claim wearing a number. Never safe to pin.

A test may assert that something *is* there. It may not assert that nothing else is, unless it
says why that is a permanent property rather than today's data.

**What this does NOT cover**, stated so the guard is not mistaken for complete coverage: it
inspects test functions only. A module-level constant encoding live state — the shape the
routing justification had — is not detected here. That instance was repaired by computing the
value instead of declaring it, which is the better fix and the one to prefer.
"""
from __future__ import annotations

import ast
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCOPES = ("disease-models/wwox/analysis/scripts", "framework/scripts", "scripts")

# Names that reach the real registries, the real ledger or the committed sidecar. A test that
# never touches these is working on a fixture and may assert whatever it likes about it.
LIVE_STATE = re.compile(
    r"RECEIPT_LEDGER|read_receipts|\.derive\(|SIDECAR|derive_receipt_projection"
    r"|verify_phase2_baseline|BLIND_MANIFEST|MANIFESTS\.glob|registries/"
    r"|fulltext_read_receipts|state_manifest_current|routing_justification|load\(exporter")

PATTERNS = (
    ("negative-on-append-only",
     re.compile(r"assertNotIn\(\s*[\"'][^\"']+[\"']"),
     "asserts a literal is ABSENT from state that only ever grows"),
    ("closed-world-set",
     re.compile(r"assertEqual\(\s*set\([^)]*\)\s*,\s*\{|assertEqual\(\s*\{[^}]*\}\s*,"),
     "asserts an exact set — it becomes false the moment a member is added"),
    ("cardinality",
     re.compile(r"assertEqual\(\s*len\([^)]*\)\s*,\s*\d+"),
     "asserts an exact count of live records"),
)

# Each entry needs an argument a reviewer can disagree with. "It is fine" is not one.
ALLOWED = {
    "test_derive_dismech_sidecar.py::test_dedup_key_components_are_declared_in_the_manifest"
    "::cardinality":
        "counts derivation_manifest records, of which there is exactly one by construction. "
        "This is a structural invariant of the record kinds, not a count of data: it does not "
        "grow when a paper is read.",
    "test_derive_dismech_sidecar.py::test_missing_locator_receipt_is_not_eligible"
    "::negative-on-append-only":
        "the assertion runs against a ledger deliberately stripped in a temporary directory, "
        "not against the live one. The absence is created by the fixture, so it is a property "
        "of the experiment rather than of today's data.",
    "test_derive_dismech_sidecar.py::test_no_record_carries_a_measured_artefact_state"
    "::negative-on-append-only":
        "asserts the absence of a KEY, not of a value: no record may ever carry "
        "`artefact_verification`, because an environment-measured field must not enter a "
        "reproducible sidecar. That is a permanent schema rule.",
    "test_export_dismech_dryrun.py::test_routing_states_whether_its_own_basis_is_backed_by_a_"
    "receipt::negative-on-append-only":
        "asserts that the key `basis_blocked_by` is absent in the branch where the basis IS "
        "backed — a schema contract about the report's shape, inside a conditional on the "
        "measured value, not a pin on which value it takes.",
}


def offences() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for scope in SCOPES:
        for path in sorted((ROOT / scope).glob("test_*.py")):
            if path.name == Path(__file__).name:
                continue
            source = path.read_text(encoding="utf-8", errors="replace")
            try:
                tree = ast.parse(source)
            except SyntaxError:
                continue
            lines = source.splitlines()
            for node in ast.walk(tree):
                if not (isinstance(node, ast.FunctionDef)
                        and node.name.startswith("test_")):
                    continue
                body = "\n".join(lines[node.lineno - 1:node.end_lineno])
                if not LIVE_STATE.search(body):
                    continue
                for kind, pattern, why in PATTERNS:
                    if pattern.search(body):
                        found.append((f"{path.name}::{node.name}::{kind}", why))
    return found


class ClosedWorldAssertions(unittest.TestCase):
    def test_no_unjustified_closed_world_assertion_on_live_state(self) -> None:
        unlisted = [(key, why) for key, why in offences() if key not in ALLOWED]
        self.assertFalse(
            unlisted,
            "these assert a closed world over state that only grows:\n  "
            + "\n  ".join(f"{key}\n      {why}" for key, why in sorted(unlisted))
            + "\n\nRe-derive the expected value from the same source the code reads, or add "
              "the key to ALLOWED with an argument for why it is a permanent property.")

    def test_every_allowance_still_describes_something_real(self) -> None:
        """An allowance for an assertion that was rewritten is stale and must be removed."""
        live = {key for key, _why in offences()}
        for key in sorted(ALLOWED):
            with self.subTest(allowance=key):
                self.assertIn(key, live, f"allowance no longer matches anything: {key}")

    def test_every_allowance_carries_an_argument(self) -> None:
        for key, reason in sorted(ALLOWED.items()):
            with self.subTest(allowance=key):
                self.assertGreater(len(reason), 60,
                                   "an allowance needs an argument, not a label")

    def test_the_detector_actually_fires(self) -> None:
        """A guard nobody has seen fail is a guard nobody knows works."""
        sample = (
            "def test_example(self):\n"
            "    rows = protocol.derive_receipt_projection()\n"
            "    self.assertEqual(len(rows), 2)\n")
        kinds = [kind for kind, pattern, _why in PATTERNS if pattern.search(sample)]
        self.assertIn("cardinality", kinds)
        self.assertTrue(LIVE_STATE.search(sample))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
