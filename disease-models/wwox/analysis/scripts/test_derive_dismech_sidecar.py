#!/usr/bin/env python3
"""Adversarial tests for the Phase-2 sidecar derivation.

Each test encodes a defect that was actually present and shipped, so that a
regression is a test failure rather than a rediscovery:

  * two distinct locators collapsing into one dedup key;
  * eligibility computed from authored constants instead of the registries;
  * a byte comparison that only compared parsed objects.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("derive", HERE / "derive_dismech_sidecar.py")
derive_mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(derive_mod)


class DedupKeyTests(unittest.TestCase):
    def test_distinct_locators_do_not_share_a_dedup_key(self) -> None:
        """Two different quotes from one source must not merge."""
        a = derive_mod.fp("PAPER 056", "prop", "ctx",
                          "LF-" + derive_mod.fp("quote A", "Fig. 3c"), "DATO", "SUPPORT")
        b = derive_mod.fp("PAPER 056", "prop", "ctx",
                          "LF-" + derive_mod.fp("quote B", "Fig. 4a"), "DATO", "SUPPORT")
        self.assertNotEqual(a, b, "distinct locators produced the same dedup key")

    def test_identical_locators_do_share_a_dedup_key(self) -> None:
        """The 016/035 merge must still happen."""
        lf = "LF-" + derive_mod.fp("same quote", "Fig. 3c")
        self.assertEqual(
            derive_mod.fp("PAPER 056", "prop", "ctx", lf, "DATO", "SUPPORT"),
            derive_mod.fp("PAPER 056", "prop", "ctx", lf, "DATO", "SUPPORT"))

    def test_dedup_key_components_are_declared_in_the_manifest(self) -> None:
        records = derive_mod.derive()
        manifest = [r for r in records if r["record_kind"] == "derivation_manifest"]
        self.assertEqual(len(manifest), 1)
        self.assertIn("locator_fingerprint", manifest[0]["dedup_key_components"])


class ProvenanceTests(unittest.TestCase):
    def test_claim_status_is_read_not_authored(self) -> None:
        self.assertEqual(derive_mod.read_claim_status("024"), "consolidated baseline")
        self.assertEqual(derive_mod.read_claim_status("035"), "in observation")

    def test_unknown_claim_fails_closed(self) -> None:
        with self.assertRaises(SystemExit):
            derive_mod.read_claim_status("999")

    def test_links_are_read_in_both_directions(self) -> None:
        fwd, back, direction, _text = derive_mod.read_link("030", "PAPER 056")
        self.assertIsNotNone(fwd, "paper->claim link not read")
        self.assertIsNone(back, "CLAIM 030 does not cite PAPER 056; a return link was invented")
        self.assertEqual(direction, "paper->claim")

    def test_claim_only_link_is_classified_not_unmapped(self) -> None:
        """CLAIM 016 references PAPER 019; the paper declares no qualified role.

        It must be classified explicitly rather than falling through to UNMAPPED_ROLE,
        which would disqualify it by accident the moment a receipt arrived.
        """
        fwd, back, direction, _text = derive_mod.read_link("016", "PAPER 019")
        self.assertEqual(direction, "claim->paper")
        raw = fwd if fwd else back
        self.assertNotEqual(derive_mod.ROLE_NORM.get(raw, "UNMAPPED_ROLE"), "UNMAPPED_ROLE",
                            "a claim-only link must be classified, not left unmapped")

    def test_occurrences_record_both_raw_roles_separately(self) -> None:
        for r in derive_mod.derive():
            if r["record_kind"] == "assertion_occurrence":
                self.assertIn("raw_link_role_paper_to_claim", r)
                self.assertIn("raw_link_role_claim_to_paper", r)
                self.assertIn("claim_link_basis", r)

    def test_locator_receipt_lineage_is_validated_not_merely_found(self) -> None:
        _d, elig, locator, _s = derive_mod.read_receipts("35716775")
        rows = [json.loads(l) for l in
                derive_mod.RECEIPT_LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
        row = next(r for r in rows if r["event_id"] == locator)
        self.assertEqual(row["evidence_depth"], "queried_not_full_read")
        self.assertEqual(row["prior_receipt"], elig,
                         "the locator receipt does not descend from the selected complete read")
        self.assertTrue(any(str(o).endswith(derive_mod.SIDECAR_NAME)
                            for o in row.get("outputs", [])))

    def test_receipt_depth_and_lineage_are_read_from_the_ledger(self) -> None:
        depth, elig, locator, sha = derive_mod.read_receipts("22193544")
        self.assertEqual(depth, "complete_fulltext_read")
        self.assertTrue(elig and elig.startswith("FTR-"))
        self.assertTrue(locator and locator.startswith("FTR-"))
        self.assertTrue(sha and len(sha) == 64)

    def test_paper_without_a_receipt_yields_no_depth(self) -> None:
        depth, _elig, _loc, _sha = derive_mod.read_receipts("32000863")
        self.assertNotEqual(depth, "complete_fulltext_read")

    def test_local_artefact_audit_is_a_separate_command(self) -> None:
        """Re-hashing local files is an audit, never part of the derivation."""
        self.assertTrue(hasattr(derive_mod, "verify_artefact"))
        state = derive_mod.verify_artefact(
            derive_mod.ARTEFACT_PATH["PAPER 056"], derive_mod.read_receipts("22193544")[3])
        self.assertIn(state, {"match", "artefact_absent"},
                      "the local artefact does not match its receipt fingerprint")


SCRIPT = HERE / "derive_dismech_sidecar.py"


def run_cli(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *arguments],
                          capture_output=True, text=True)


class FailOpenTests(unittest.TestCase):
    """Each of these was a fail-open: the generator succeeded while checking nothing."""

    def _ledger_without(self, predicate) -> str:
        rows = [l for l in derive_mod.RECEIPT_LEDGER.read_text(encoding="utf-8").splitlines()
                if l.strip() and not predicate(json.loads(l))]
        return "\n".join(rows) + "\n"

    def test_missing_locator_receipt_is_not_eligible(self) -> None:
        """An occurrence with a locator decision but no receipt documenting it must not pass."""
        original = derive_mod.RECEIPT_LEDGER
        with tempfile.TemporaryDirectory() as tmp:
            stripped = Path(tmp) / "ledger.jsonl"
            stripped.write_text(
                self._ledger_without(lambda r: r.get("workflow") == "phase2_locator_extraction"),
                encoding="utf-8")
            derive_mod.RECEIPT_LEDGER = stripped
            try:
                states = {r["terminal_state"] for r in derive_mod.derive()
                          if r["record_kind"] == "assertion_occurrence"}
            finally:
                derive_mod.RECEIPT_LEDGER = original
        self.assertNotIn("ELIGIBLE_FOR_EXPORT", states,
                         "occurrences stayed eligible without a locator-extraction receipt")
        self.assertIn("LOCATOR_PROVENANCE_MISSING", states)

    def test_corrupt_locator_lineage_aborts(self) -> None:
        """A locator receipt that does not descend from the complete read must abort."""
        original = derive_mod.RECEIPT_LEDGER
        with tempfile.TemporaryDirectory() as tmp:
            broken = Path(tmp) / "ledger.jsonl"
            rows = []
            for line in derive_mod.RECEIPT_LEDGER.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                r = json.loads(line)
                if r.get("workflow") == "phase2_locator_extraction":
                    r["prior_receipt"] = "FTR-00000000-00000000-99"
                rows.append(json.dumps(r))
            broken.write_text("\n".join(rows) + "\n", encoding="utf-8")
            derive_mod.RECEIPT_LEDGER = broken
            try:
                with self.assertRaises(SystemExit):
                    derive_mod.derive()
            finally:
                derive_mod.RECEIPT_LEDGER = original

    def test_audit_returns_incomplete_when_artefacts_are_absent(self) -> None:
        """Absence must not be reported as success — checked on the aggregate result."""
        original = derive_mod.REPO_ROOT
        with tempfile.TemporaryDirectory() as tmp:
            derive_mod.REPO_ROOT = Path(tmp)          # no files/ here
            try:
                code, states, tally = derive_mod.audit_local_sources()
            finally:
                derive_mod.REPO_ROOT = original
        self.assertEqual(code, 2, "an audit that compared nothing reported success")
        self.assertEqual(tally["match"], 0)
        self.assertTrue(tally["absent"] >= 1)

    def test_audit_cli_exits_two_when_artefacts_are_absent(self) -> None:
        """The exit code is the contract; a dispatcher regression must fail here."""
        with tempfile.TemporaryDirectory() as tmp:
            stub = Path(tmp) / "derive.py"
            stub.write_text(
                "import runpy, sys, pathlib\n"
                "import importlib.util\n"
                f"spec = importlib.util.spec_from_file_location('d', r'{SCRIPT}')\n"
                "m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)\n"
                f"m.REPO_ROOT = pathlib.Path(r'{tmp}')\n"
                "sys.argv = ['derive', '--audit-local-sources']\n"
                "sys.exit(m.main())\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(stub)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2,
                         f"CLI did not exit 2 on an incomplete audit: {result.stdout}")
        self.assertIn("AUDIT INCOMPLETE", result.stdout)

    def test_audit_cli_exits_zero_when_every_artefact_verifies(self) -> None:
        result = run_cli("--audit-local-sources")
        if "artefact_absent" in result.stdout:
            self.skipTest("local full-text corpus not present in this checkout")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("AUDIT PASSED", result.stdout)

    def test_bare_wikilink_is_not_supporting_evidence(self) -> None:
        """CLAIM 016 references PAPER 019 by wikilink; its Source field names it only in prose."""
        fwd, back, direction, source_text = derive_mod.read_link("016", "PAPER 019")
        self.assertEqual(direction, "claim->paper")
        self.assertEqual(back, "wikilink_only")
        self.assertEqual(derive_mod.ROLE_NORM[back], "UNQUALIFIED_REFERENCE")
        occ = [r for r in derive_mod.derive()
               if r["record_kind"] == "assertion_occurrence" and r["source_id"] == "PAPER 019"]
        for r in occ:
            self.assertIsNone(r["raw_link_role_claim_to_paper"],
                              "a derived classification was recorded as a raw role")
            self.assertEqual(r["claim_link_basis"], "wikilink_only")
        self.assertIn("Cheng", source_text,
                      "the Source field text should still be recorded for review")

    def test_source_field_reference_is_supporting(self) -> None:
        fwd, back, direction, _text = derive_mod.read_link("016", "PAPER 056")
        self.assertEqual(back, "source_field")
        self.assertEqual(derive_mod.ROLE_NORM[back], "SUPPORTING")

    def test_manifest_describes_the_actual_provenance(self) -> None:
        manifest = next(r for r in derive_mod.derive()
                        if r["record_kind"] == "derivation_manifest")
        artefact_note = manifest["provenance_sources"]["artefact_bytes"]
        self.assertIn("not re-hashed", artefact_note)
        self.assertIn("link_claim_to_paper", manifest["provenance_sources"])


class ContractDriftTests(unittest.TestCase):
    """Rev. 6 added a state in code and not in the specification. This catches that."""

    SPEC = HERE.parents[0] / "dismech_export_spec.md"

    def test_every_ledger_a_state_appears_in_the_specification(self) -> None:
        if not self.SPEC.exists():
            self.skipTest("specification not present")
        spec_text = self.SPEC.read_text(encoding="utf-8")
        missing = [s for s in derive_mod.LEDGER_A_ORDER if s not in spec_text]
        self.assertFalse(missing, f"states in code but not in the contract: {missing}")

    def test_specification_states_the_correct_loss_count(self) -> None:
        if not self.SPEC.exists():
            self.skipTest("specification not present")
        losses = len(derive_mod.LEDGER_A_ORDER) - 1
        words = {7: "seven", 8: "eight", 9: "nine", 10: "ten"}
        self.assertIn(f"{words[losses]} Ledger-A loss states",
                      self.SPEC.read_text(encoding="utf-8"),
                      f"the accounting identity does not name {losses} loss states")


class SerialisationTests(unittest.TestCase):
    """These invoke the CLI, so a regression in the implementation is caught."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.records = derive_mod.derive()
        self.exact = Path(self.tmp.name) / "exact.jsonl"
        self.exact.write_text(derive_mod.serialise(self.records), encoding="utf-8")
        self.reformatted = Path(self.tmp.name) / "reformatted.jsonl"
        self.reformatted.write_text("".join(
            json.dumps(r, sort_keys=True, ensure_ascii=False,
                       separators=(",", ":")) + "\n" for r in self.records), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_verify_bytes_accepts_the_declared_serialisation(self) -> None:
        result = run_cli("--verify-bytes", str(self.exact))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_verify_bytes_rejects_a_reformatted_file(self) -> None:
        result = run_cli("--verify-bytes", str(self.reformatted))
        self.assertEqual(result.returncode, 1,
                         "the byte check accepted a differently serialised file")

    def test_verify_semantic_accepts_a_reformatted_file(self) -> None:
        result = run_cli("--verify-semantic", str(self.reformatted))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_committed_sidecar_reproduces_byte_for_byte(self) -> None:
        committed = HERE.parents[0] / "data" / "dismech_sidecar_016_024_035.jsonl"
        if not committed.exists():
            self.skipTest("sidecar not present")
        result = run_cli("--verify-bytes", str(committed))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class EnvironmentIndependenceTests(unittest.TestCase):
    """The sidecar must derive identically without the local full-text corpus."""

    def test_no_record_carries_a_measured_artefact_state(self) -> None:
        for r in derive_mod.derive():
            self.assertNotIn("artefact_verification", r,
                             "an environment-dependent value leaked into the sidecar")
            locator = r.get("locator") or {}
            if isinstance(locator, dict):
                self.assertNotIn("verification", locator)

    def test_artefact_fingerprint_comes_from_the_receipt_not_the_disk(self) -> None:
        _d, _e, _l, sha = derive_mod.read_receipts("22193544")
        occ = [r for r in derive_mod.derive()
               if r["record_kind"] == "assertion_occurrence" and r.get("pmid") == "22193544"]
        self.assertTrue(occ)
        for r in occ:
            self.assertEqual(r["artefact_sha256"], sha)


class AccountingTests(unittest.TestCase):
    def test_ledger_a_identity_holds(self) -> None:
        report = derive_mod.accounting(derive_mod.derive())
        self.assertTrue(report["identity_A_holds"])
        self.assertTrue(report["candidate_closure_holds"])

    def test_nothing_is_marked_exported(self) -> None:
        """No node has been emitted, so EXPORTED must not appear anywhere."""
        for r in derive_mod.derive():
            self.assertNotEqual(r.get("terminal_state"), "EXPORTED")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
