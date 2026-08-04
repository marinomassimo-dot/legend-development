#!/usr/bin/env python3
"""Adversarial regressions for the blind independent-derivation protocol."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "independent_protocol", HERE / "dismech_independent_protocol.py")
protocol = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(protocol)


def occurrence(occurrence_id: str, proposition: str, ordinal: int, *,
               anchor: str = "claim_registry_current.md#CLAIM 035|Summary|sent[0]",
               dedup_key: str | None = None) -> dict:
    return {
        "record_kind": "assertion_occurrence",
        "claim_id": "035",
        "registry_anchor": anchor,
        "registry_ordinal": ordinal,
        "occurrence_id": occurrence_id,
        "proposition": proposition,
        "context": "human protein in vitro",
        "source_id": "PAPER 056",
        "epistemic_type": "DATO",
        "evidence_relation": "SUPPORT",
        "terminal_state": "ELIGIBLE_FOR_EXPORT",
        "dedup_key": dedup_key,
    }


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


class BaselineTests(unittest.TestCase):
    def test_current_phase2_baseline_verifies(self) -> None:
        self.assertEqual(protocol.verify_phase2_baseline(), [])

    def test_append_only_suffix_does_not_invalidate_prefix(self) -> None:
        baseline = json.loads(protocol.BASELINE.read_text(encoding="utf-8"))
        ledger_record = baseline["inputs"]["receipt_ledger"]
        original_root = protocol.REPO_ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger = root / ledger_record["path"]
            ledger.parent.mkdir(parents=True)
            source = original_root / ledger_record["path"]
            ledger.write_bytes(source.read_bytes() + b'{"event_id":"FTR-FUTURE"}\n')
            # Materialise the other sealed inputs and output unchanged.
            for record in baseline["inputs"].values():
                if record is ledger_record:
                    continue
                target = root / record["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((original_root / record["path"]).read_bytes())
            output = root / baseline["output"]["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes((original_root / baseline["output"]["path"]).read_bytes())
            protocol.REPO_ROOT = root
            try:
                self.assertEqual(protocol.verify_phase2_baseline(), [])
            finally:
                protocol.REPO_ROOT = original_root

    def test_mutated_sealed_prefix_fails(self) -> None:
        baseline = json.loads(protocol.BASELINE.read_text(encoding="utf-8"))
        ledger_record = baseline["inputs"]["receipt_ledger"]
        original_root = protocol.REPO_ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for record in baseline["inputs"].values():
                source = original_root / record["path"]
                target = root / record["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
            output = root / baseline["output"]["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes((original_root / baseline["output"]["path"]).read_bytes())
            ledger = root / ledger_record["path"]
            data = bytearray(ledger.read_bytes())
            data[10] = ord("X") if data[10] != ord("X") else ord("Y")
            ledger.write_bytes(bytes(data))
            protocol.REPO_ROOT = root
            try:
                self.assertIn("receipt_ledger: sealed prefix bytes changed",
                              protocol.verify_phase2_baseline())
            finally:
                protocol.REPO_ROOT = original_root

    def test_phase2_occurrences_obey_the_declared_hash_contract(self) -> None:
        sidecar = protocol.DATA / "dismech_sidecar_016_024_035.jsonl"
        self.assertEqual(protocol.verify_occurrence_hash_contract(sidecar), [])

    def test_wrong_occurrence_hash_is_rejected(self) -> None:
        source = protocol.DATA / "dismech_sidecar_016_024_035.jsonl"
        rows = protocol.load_jsonl(source)
        target = next(row for row in rows if row.get("record_kind") == "assertion_occurrence")
        target["occurrence_id"] = "OCC-wrong"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "wrong.jsonl"
            write_jsonl(path, rows)
            errors = protocol.verify_occurrence_hash_contract(path)
        self.assertTrue(any("occurrence_id violates" in error for error in errors))

    def test_repository_allowlist_tamper_breaks_the_root_of_trust(self) -> None:
        """Reproduce Claude's Rev. 8 bypass: authorising the first sidecar must fail."""
        baseline = json.loads(protocol.BASELINE.read_text(encoding="utf-8"))
        original_root = protocol.REPO_ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for record in baseline["inputs"].values():
                source = original_root / record["path"]
                target = root / record["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
            output = root / baseline["output"]["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes((original_root / baseline["output"]["path"]).read_bytes())
            manifest_path = root / baseline["inputs"]["blind_input_manifest"]["path"]
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["bundle_files"].append({
                "bundle_path": "inputs/leak.jsonl",
                "role": "leaked_first_pass",
                "sha256": baseline["output"]["sha256"],
                "source_path": baseline["output"]["path"],
            })
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            original_manifest = protocol.BLIND_MANIFEST
            protocol.REPO_ROOT = root
            protocol.BLIND_MANIFEST = manifest_path
            try:
                errors = protocol.verify_phase2_baseline()
                with self.assertRaisesRegex(ValueError, "sealed baseline failed"):
                    protocol.build_blind_bundle(root / "leakbundle")
            finally:
                protocol.REPO_ROOT = original_root
                protocol.BLIND_MANIFEST = original_manifest
        self.assertIn("blind_input_manifest: sha256 mismatch", errors)


class ReceiptProjectionTests(unittest.TestCase):
    def test_committed_projection_is_generated_byte_for_byte(self) -> None:
        self.assertEqual(protocol.verify_receipt_projection(), [])

    def test_projection_is_complete_for_target_claims_only(self) -> None:
        rows = protocol.derive_receipt_projection()
        by_paper = {row["paper_id"]: row for row in rows}
        self.assertEqual(set(by_paper), {"055", "056"})
        self.assertEqual(by_paper["055"]["active_complete_receipt_event"],
                         "FTR-20260726-35716775-03")
        self.assertEqual(by_paper["056"]["active_complete_receipt_event"],
                         "FTR-20260726-22193544-03")
        projected_pmids = {row["study_id"]["pmid"] for row in rows}
        self.assertNotIn("21212533", projected_pmids, "non-target complete read leaked in")
        self.assertNotIn("34214506", projected_pmids, "non-target complete read leaked in")

    def test_cited_paper_without_complete_receipt_is_absent_by_rule(self) -> None:
        rows = protocol.derive_receipt_projection()
        self.assertNotIn("019", {row["paper_id"] for row in rows})


class BlindInputFirewallTests(unittest.TestCase):
    def test_manifest_excludes_contaminating_material(self) -> None:
        manifest = protocol.load_json(protocol.BLIND_MANIFEST)
        paths = {row["source_path"] for row in manifest["bundle_files"]}
        forbidden_fragments = {"dismech_sidecar_016_024_035", "derive_dismech_sidecar.py",
                               "dismech_export_spec.md", "fulltext_read_receipts.jsonl",
                               "dismech_phase2_baseline.json",
                               "dismech_independent_derivation_design.md"}
        for fragment in forbidden_fragments:
            self.assertFalse(any(fragment in path for path in paths), fragment)

    def test_receipt_projection_contains_no_first_pass_results(self) -> None:
        rows = protocol.load_jsonl(protocol.DATA / "dismech_blind_receipt_projection.jsonl")
        self.assertEqual(len(rows), 2)
        forbidden = {"outputs", "evidence_basis", "workflow", "locator",
                     "locator_extraction_receipt_event"}
        for row in rows:
            self.assertFalse(forbidden & row.keys())
            self.assertEqual(row["projection_kind"], "eligibility_only")

    def test_blind_contract_does_not_enumerate_known_answers(self) -> None:
        text = (protocol.ANALYSIS / "dismech_blind_derivation_contract.md").read_text(
            encoding="utf-8")
        leaked_answers = ["035-a1", "024-a1", "016-c1", "DK-c46285700983",
                          "14 ELIGIBLE_FOR_EXPORT", "SOURCE_SUPPORT_NOT_FOUND = 3"]
        for answer in leaked_answers:
            self.assertNotIn(answer, text)

    def test_bundle_verifier_rejects_extra_and_tampered_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "bundle"
            bundle.mkdir()
            payload = b"allowed"
            manifest = {"bundle_files": [{"bundle_path": "inputs/a.txt",
                                            "sha256": protocol.sha256_bytes(payload)}],
                        "allowed_outputs": []}
            (bundle / "inputs").mkdir()
            (bundle / "inputs/a.txt").write_bytes(payload)
            manifest_text = json.dumps(manifest)
            (bundle / "MANIFEST.json").write_text(manifest_text, encoding="utf-8")
            sealed = root / "sealed.json"
            sealed.write_text(manifest_text, encoding="utf-8")
            original = protocol.BLIND_MANIFEST
            protocol.BLIND_MANIFEST = sealed
            try:
                self.assertEqual(protocol.verify_blind_bundle(bundle, stage="pre"), [])
                (bundle / "secret.txt").write_text("leak", encoding="utf-8")
                self.assertIn("undeclared file: secret.txt",
                              protocol.verify_blind_bundle(bundle, stage="pre"))
                (bundle / "secret.txt").unlink()
                (bundle / "inputs/a.txt").write_text("changed", encoding="utf-8")
                self.assertIn("hash mismatch: inputs/a.txt",
                              protocol.verify_blind_bundle(bundle, stage="pre"))
            finally:
                protocol.BLIND_MANIFEST = original

    def test_replaced_manifest_cannot_authorise_a_leak(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "bundle"
            bundle.mkdir()
            sealed = root / "sealed.json"
            sealed.write_text(json.dumps({"bundle_files": [], "allowed_outputs": []}),
                              encoding="utf-8")
            (bundle / "MANIFEST.json").write_text(
                json.dumps({"bundle_files": [{"bundle_path": "secret.txt", "sha256": "x"}],
                            "allowed_outputs": []}), encoding="utf-8")
            (bundle / "secret.txt").write_text("leak", encoding="utf-8")
            original = protocol.BLIND_MANIFEST
            protocol.BLIND_MANIFEST = sealed
            try:
                self.assertEqual(protocol.verify_blind_bundle(bundle, stage="pre"),
                                 ["MANIFEST.json does not match the sealed repository allowlist"])
            finally:
                protocol.BLIND_MANIFEST = original

    def test_reconciliation_may_change_only_provenance_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "bundle"
            (bundle / "output").mkdir(parents=True)
            manifest = {"bundle_files": [], "allowed_outputs": [
                "output/reconciliation_attestation.json", "output/run_attestation.json",
                "output/second_derivation_authored.jsonl",
                "output/second_derivation_reconciled.jsonl"]}
            manifest_text = json.dumps(manifest)
            (bundle / "MANIFEST.json").write_text(manifest_text, encoding="utf-8")
            sealed = root / "sealed.json"
            sealed.write_text(manifest_text, encoding="utf-8")
            authored = occurrence("o1", "WWOX binds GSK3β", 0)
            authored["locator_extraction_receipt_event"] = None
            authored["terminal_state"] = "LOCATOR_PROVENANCE_MISSING"
            reconciled = dict(authored)
            reconciled["locator_extraction_receipt_event"] = "FTR-NEW"
            reconciled["terminal_state"] = "ELIGIBLE_FOR_EXPORT"
            authored_path = bundle / "output/second_derivation_authored.jsonl"
            reconciled_path = bundle / "output/second_derivation_reconciled.jsonl"
            write_jsonl(authored_path, [authored])
            write_jsonl(reconciled_path, [reconciled])
            (bundle / "output/run_attestation.json").write_text("{}", encoding="utf-8")
            attestation = {
                "authored_sha256": protocol.sha256_file(authored_path),
                "reconciled_sha256": protocol.sha256_file(reconciled_path),
                "allowed_changed_fields": sorted({"locator_extraction_receipt_event",
                                                   "terminal_state", "unreached_tests"}),
            }
            (bundle / "output/reconciliation_attestation.json").write_text(
                json.dumps(attestation), encoding="utf-8")
            original = protocol.BLIND_MANIFEST
            protocol.BLIND_MANIFEST = sealed
            try:
                self.assertEqual(protocol.verify_reconciliation(bundle), [])
                reconciled["proposition"] = "rewritten"
                write_jsonl(reconciled_path, [reconciled])
                attestation["reconciled_sha256"] = protocol.sha256_file(reconciled_path)
                (bundle / "output/reconciliation_attestation.json").write_text(
                    json.dumps(attestation), encoding="utf-8")
                self.assertIn("reconciliation rewrote authored content at record 1",
                              protocol.verify_reconciliation(bundle))
            finally:
                protocol.BLIND_MANIFEST = original


class CanonicalisationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = protocol.load_canonicalisation()

    def test_declared_positive_and_negative_fixtures_hold(self) -> None:
        self.assertEqual(protocol.verify_canonicalisation(self.config), [])

    def test_nfc_does_not_compatibility_fold_superscripts(self) -> None:
        value, _trace = protocol.canonicalise("Ca²⁺", self.config)
        self.assertEqual(value, "Ca²⁺")

    def test_aliases_require_whole_tokens(self) -> None:
        value, _trace = protocol.canonicalise("XGSK3betaY", self.config)
        self.assertEqual(value, "XGSK3betaY")

    def test_trace_explains_candidate_collision(self) -> None:
        value, trace = protocol.canonicalise("  GSK3beta  ", self.config)
        self.assertEqual(value, "GSK3β")
        self.assertEqual([row["transform"] for row in trace],
                         ["whitespace_collapse_and_trim", "closed_biomedical_aliases"])


class CrossRunMatchingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = protocol.load_canonicalisation()

    def _compare(self, left: list[dict], right: list[dict]) -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a.jsonl", Path(tmp) / "b.jsonl"
            write_jsonl(a, left)
            write_jsonl(b, right)
            return protocol.compare_derivations(a, b, self.config)

    def test_swapped_ordinals_match_by_content_not_position(self) -> None:
        left = [occurrence("base-0", "WWOX binds GSK3β", 0),
                occurrence("base-1", "L404 is required", 1)]
        right = [occurrence("second-0", "L404 is required", 0),
                 occurrence("second-1", "WWOX binds GSK3β", 1)]
        report = self._compare(left, right)
        matches = report["axis_3_proposition_correspondence"]["unambiguous_matches"]
        pairs = {(m["baseline_occurrence_id"], m["second_occurrence_id"]) for m in matches}
        self.assertEqual(pairs, {("base-0", "second-1"), ("base-1", "second-0")})
        self.assertFalse(report["axis_3_proposition_correspondence"]["ordinal_used_as_join_key"])

    def test_canonical_candidate_is_review_not_identity(self) -> None:
        report = self._compare(
            [occurrence("base", "WWOX binds GSK3β", 0)],
            [occurrence("second", "WWOX binds GSK3beta", 0)])
        match = report["axis_3_proposition_correspondence"]["unambiguous_matches"][0]
        self.assertEqual(match["band"], "CANONICAL_CANDIDATE")
        self.assertIn("canonical_review", match)
        self.assertTrue(match["canonical_review"]["second"]["transform_trace"]["proposition"])
        self.assertTrue(report["review_required"])

    def test_extra_atom_is_unmatched_not_forced_into_a_pair(self) -> None:
        report = self._compare(
            [occurrence("base", "WWOX binds GSK3β", 0)],
            [occurrence("second", "WWOX binds GSK3β", 0),
             occurrence("extra", "L404 is required", 1)])
        unmatched = report["axis_3_proposition_correspondence"]["second_unmatched"]
        self.assertEqual([row["occurrence_id"] for row in unmatched], ["extra"])

    def test_dedup_partition_uses_only_unambiguous_correspondence(self) -> None:
        left = [occurrence("b1", "p1", 0, dedup_key="same"),
                occurrence("b2", "p2", 1, dedup_key="same")]
        right = [occurrence("s1", "p1", 0, dedup_key="one"),
                 occurrence("s2", "p2", 1, dedup_key="two")]
        report = self._compare(left, right)
        axis4 = report["axis_4_deduplication"]
        self.assertEqual(axis4["comparison_universe"], "unambiguous cross-run matches only")
        self.assertEqual(len(axis4["production_partition_disagreements"]), 1)
        self.assertFalse(axis4["production_key_modified"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
