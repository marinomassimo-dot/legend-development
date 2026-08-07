#!/usr/bin/env python3
"""Adversarial regressions for the blind independent-derivation protocol."""
from __future__ import annotations

import importlib.util
import hashlib
import json
import re
import shutil
import subprocess
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
        if not protocol._git_ok(protocol.REPO_ROOT, "rev-parse", "--is-inside-work-tree"):
            self.skipTest("Git object database absent; verify-baseline must fail closed here")
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
                self.assertEqual(protocol.verify_phase2_baseline(verify_git=False), [])
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
                              protocol.verify_phase2_baseline(verify_git=False))
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
                errors = protocol.verify_phase2_baseline(verify_git=False)
                with self.assertRaisesRegex(ValueError, "sealed baseline failed"):
                    protocol.build_blind_bundle(root / "leakbundle")
            finally:
                protocol.REPO_ROOT = original_root
                protocol.BLIND_MANIFEST = original_manifest
        self.assertIn("blind_input_manifest: sha256 mismatch", errors)

    def test_two_file_reseal_disagrees_with_pinned_git_tree(self) -> None:
        """Changing allowlist + declared hash cannot rewrite the frozen Git tree."""
        baseline = json.loads(protocol.BASELINE.read_text(encoding="utf-8"))
        original_root = protocol.REPO_ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for record in baseline["inputs"].values():
                source = original_root / record["path"]
                target = root / record["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            output = root / baseline["output"]["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original_root / baseline["output"]["path"], output)
            baseline_path = root / protocol.BASELINE.relative_to(original_root)
            baseline_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(protocol.BASELINE, baseline_path)

            def git(*args: str) -> str:
                result = subprocess.run(["git", *args], cwd=root, check=True,
                                        capture_output=True, text=True)
                return result.stdout.strip()

            git("init", "-q")
            git("config", "user.email", "protocol-test@example.invalid")
            git("config", "user.name", "Protocol Test")
            git("add", ".")
            git("commit", "-qm", "frozen inputs")
            frozen = git("rev-parse", "HEAD")
            temp_baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
            temp_baseline["git_head_at_freeze"] = frozen
            baseline_path.write_text(json.dumps(temp_baseline, indent=2, sort_keys=True) + "\n",
                                     encoding="utf-8")
            git("add", baseline_path.relative_to(root).as_posix())
            git("commit", "-qm", "anchor baseline")

            protocol.REPO_ROOT = root
            try:
                self.assertEqual(protocol.verify_phase2_baseline(baseline_path), [])
                manifest_path = root / temp_baseline["inputs"]["blind_input_manifest"]["path"]
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest["bundle_files"].append({
                    "bundle_path": "inputs/leak.jsonl", "role": "leaked_first_pass",
                    "sha256": temp_baseline["output"]["sha256"],
                    "source_path": temp_baseline["output"]["path"],
                })
                manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
                temp_baseline["inputs"]["blind_input_manifest"]["sha256"] = hashlib.sha256(
                    manifest_path.read_bytes()).hexdigest()
                baseline_path.write_text(json.dumps(temp_baseline, indent=2, sort_keys=True) + "\n",
                                         encoding="utf-8")
                errors = protocol.verify_phase2_baseline(baseline_path)
            finally:
                protocol.REPO_ROOT = original_root
        self.assertIn("baseline working bytes differ from HEAD", errors)
        self.assertIn("blind_input_manifest: frozen git blob disagrees with declared hash", errors)


class ReceiptProjectionTests(unittest.TestCase):
    def test_committed_projection_is_generated_byte_for_byte(self) -> None:
        self.assertEqual(protocol.verify_receipt_projection(), [])

    def test_projection_is_complete_for_target_claims_only(self) -> None:
        """The rule, not the roster.

        This asserted the exact set {"055", "056"} and the exact receipt ids behind them.
        Both were true of the data at the time. When PAPER 019 was read to complete depth on
        2026-08-04 the test failed for the right reason but with the wrong message — it
        reported an unexpected paper rather than a rule violation, because it was testing the
        roster. Now it re-derives the expected roster from the same two inputs the rule names:
        papers cited by the target claims, intersected with papers holding a complete receipt.
        """
        rows = protocol.derive_receipt_projection()
        by_paper = {row["paper_id"]: row for row in rows}

        claims = (protocol.REPO_ROOT
                  / "disease-models/wwox/registries/claim_registry_current.md"
                  ).read_text(encoding="utf-8")
        papers = (protocol.REPO_ROOT
                  / "disease-models/wwox/registries/paper_registry_current.md"
                  ).read_text(encoding="utf-8")
        manifest = protocol.load_json(protocol.BLIND_MANIFEST)
        ledger = protocol.load_jsonl(
            protocol.REPO_ROOT
            / "disease-models/wwox/registries/fulltext_read_receipts.jsonl")
        complete_pmids = {str(e.get("study_id", {}).get("pmid", "")) for e in ledger
                          if e.get("evidence_depth") == "complete_fulltext_read"}

        cited: set[str] = set()
        for claim_id in manifest["target_claim_ids"]:
            block = protocol._registry_block(claims, "CLAIM", claim_id)
            cited.update(re.findall(r"\bPAPER\s+(\d{3})\b", block))
        expected = set()
        for paper_id in cited:
            block = protocol._registry_block(papers, "PAPER", paper_id)
            pmid = re.search(r"^\*\*Identifier:\*\*.*?\bPMID\s+([0-9]{7,8})\b",
                             block, re.MULTILINE)
            if pmid and pmid.group(1) in complete_pmids:
                expected.add(paper_id)

        self.assertEqual(set(by_paper), expected,
                         "the projection must be exactly the target-cited papers that hold a "
                         "complete receipt — no more, and no fewer")
        self.assertTrue(expected, "the fixture must contain at least one projected paper")
        for row in rows:
            self.assertEqual(row["evidence_depth"], "complete_fulltext_read")
            self.assertTrue(row["active_complete_receipt_event"].startswith("FTR-"))

    def test_complete_read_outside_the_target_claims_never_projects(self) -> None:
        """The firewall that matters: a complete read of a non-target paper must not leak."""
        rows = protocol.derive_receipt_projection()
        projected_pmids = {row["study_id"]["pmid"] for row in rows}
        for pmid in ("21212533", "34214506", "39507621", "36779245", "40875931"):
            self.assertNotIn(pmid, projected_pmids,
                             f"complete read of non-target PMID {pmid} leaked into the bundle")

    def test_cited_paper_without_complete_receipt_is_absent_by_rule(self) -> None:
        """Named PAPER 019 until it was read on 2026-08-04. Derive the case instead."""
        rows = protocol.derive_receipt_projection()
        projected = {row["paper_id"] for row in rows}
        manifest = protocol.load_json(protocol.BLIND_MANIFEST)
        claims = (protocol.REPO_ROOT
                  / "disease-models/wwox/registries/claim_registry_current.md"
                  ).read_text(encoding="utf-8")
        cited: set[str] = set()
        for claim_id in manifest["target_claim_ids"]:
            cited.update(re.findall(
                r"\bPAPER\s+(\d{3})\b",
                protocol._registry_block(claims, "CLAIM", claim_id)))
        for paper_id in sorted(cited - projected):
            with self.subTest(paper=paper_id):
                bundle = {e["paper_id"] for e in manifest["bundle_files"]
                          if e.get("role") == "locator_source"}
                self.assertNotIn(
                    paper_id, bundle,
                    f"PAPER {paper_id} is cited by a target claim and is not projected, so it "
                    "holds no complete receipt — it must not be bundled as a locator source")


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
        # Row count is data, not firewall: it was 2 until PAPER 019 was read on 2026-08-04.
        # What must hold regardless of how many papers qualify is that no row carries a
        # first-pass result. Asserting the count made a legitimate reading look like a leak.
        self.assertTrue(rows, "the projection must not be empty")
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
            projection_path = bundle / "inputs/receipt_eligibility_projection.jsonl"
            projection_path.parent.mkdir(parents=True)
            projection = {
                "active_complete_receipt_event": "FTR-COMPLETE",
                "evidence_depth": "complete_fulltext_read",
                "paper_id": "056",
                "projection_kind": "eligibility_only",
                "source_fingerprint": "a" * 64,
                "source_locator": "PMC | sources/PAPER056.xml",
                "study_id": {"pmid": "22193544"},
            }
            write_jsonl(projection_path, [projection])
            manifest = {"bundle_files": [{
                "bundle_path": "inputs/receipt_eligibility_projection.jsonl",
                "role": "eligibility_only_receipt_projection",
                "sha256": protocol.sha256_file(projection_path),
                "source_path": "unused",
            }], "allowed_outputs": [
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
            authored["eligibility_receipt_event"] = "FTR-COMPLETE"
            authored["locator"] = {"snippet": "short extract",
                                   "source_fingerprint": "a" * 64,
                                   "structural_anchor": "Results"}
            authored["unreached_tests"] = ["SOURCE_SUPPORT_NOT_FOUND",
                                            "ELIGIBLE_FOR_EXPORT"]
            reconciled = dict(authored)
            reconciled["locator_extraction_receipt_event"] = "FTR-LOCATOR-2"
            reconciled["terminal_state"] = "ELIGIBLE_FOR_EXPORT"
            reconciled["unreached_tests"] = []
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
            ledger_path = root / "ledger.jsonl"
            write_jsonl(ledger_path, [
                {"event_id": "FTR-COMPLETE", "prior_receipt": None,
                 "workflow": "deep_dive", "evidence_depth": "complete_fulltext_read",
                 "study_id": {"pmid": "22193544"}, "source_fingerprint": "a" * 64,
                 "outputs": ["paper_registry_current.md"]},
                {"event_id": "FTR-LOCATOR-1", "prior_receipt": "FTR-COMPLETE",
                 "workflow": "phase2_locator_extraction",
                 "evidence_depth": "queried_not_full_read",
                 "study_id": {"pmid": "22193544"}, "source_fingerprint": "a" * 64,
                 "outputs": ["first-sidecar.jsonl"]},
                {"event_id": "FTR-LOCATOR-2", "prior_receipt": "FTR-LOCATOR-1",
                 "workflow": "phase2_independent_locator_extraction",
                 "evidence_depth": "queried_not_full_read",
                 "study_id": {"pmid": "22193544"}, "source_fingerprint": "a" * 64,
                 "outputs": [protocol.ARCHIVED_AUTHORED_REL]},
            ])
            original = protocol.BLIND_MANIFEST
            protocol.BLIND_MANIFEST = sealed
            try:
                self.assertEqual(protocol.verify_reconciliation(bundle, ledger_path), [])
                reconciled["proposition"] = "rewritten"
                write_jsonl(reconciled_path, [reconciled])
                attestation["reconciled_sha256"] = protocol.sha256_file(reconciled_path)
                (bundle / "output/reconciliation_attestation.json").write_text(
                    json.dumps(attestation), encoding="utf-8")
                self.assertIn("reconciliation rewrote authored content at record 1",
                              protocol.verify_reconciliation(bundle, ledger_path))
            finally:
                protocol.BLIND_MANIFEST = original

    def test_locator_receipt_may_descend_through_prior_extraction(self) -> None:
        receipts = {
            "complete": {"event_id": "complete", "prior_receipt": None},
            "first": {"event_id": "first", "prior_receipt": "complete"},
            "second": {"event_id": "second", "prior_receipt": "first"},
        }
        self.assertTrue(protocol.receipt_descends_from(receipts, "second", "complete"))
        self.assertFalse(protocol.receipt_descends_from(receipts, "first", "second"))


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

    def test_same_structural_id_with_different_content_is_explicit(self) -> None:
        report = self._compare(
            [occurrence("shared", "WWOX binds GSK3β", 0)],
            [occurrence("shared", "L404 is required", 0)])
        axis3 = report["axis_3_proposition_correspondence"]
        self.assertEqual(
            [row["occurrence_id"] for row in axis3["structural_id_content_collisions"]],
            ["shared"])
        self.assertEqual(
            report["axis_4_deduplication"]["measurement_status"],
            "NOT_MEASURABLE_EMPTY_CORRESPONDENCE")
        self.assertTrue(report["review_required"])

    def test_dedup_partition_uses_only_unambiguous_correspondence(self) -> None:
        left = [occurrence("b1", "p1", 0, dedup_key="same"),
                occurrence("b2", "p2", 1, dedup_key="same")]
        right = [occurrence("s1", "p1", 0, dedup_key="one"),
                 occurrence("s2", "p2", 1, dedup_key="two")]
        report = self._compare(left, right)
        axis4 = report["axis_4_deduplication"]
        self.assertEqual(axis4["comparison_universe"], "unambiguous cross-run matches only")
        self.assertEqual(axis4["measurement_status"], "MEASURED")
        self.assertEqual(len(axis4["production_partition_disagreements"]), 1)
        self.assertFalse(axis4["production_key_modified"])


class SealedScopeTests(unittest.TestCase):
    """A freeze over a living registry must pin what was consumed, not the container.

    Re-sealed 2026-08-06. The previous whole-file hash reported an edit to CLAIM 005 — a claim
    this experiment never reads — as identical to an edit inside the export scope, so it fired
    on every registry commit and could not fire harder on the one that mattered.
    """

    REGISTRY = (
        "# Claim registry\n\n"
        "## CLAIM 005\n**Status:** consolidated baseline\n**Summary:** out of scope.\n\n"
        "## CLAIM 016\n**Status:** in observation\n**Summary:** in scope.\n\n"
        "## CLAIM 024\n**Status:** in observation\n**Summary:** also in scope.\n"
    )
    SCOPE = ["CLAIM 016", "CLAIM 024"]

    def digest(self, text: str) -> str:
        return protocol.sha256_bytes(protocol.registry_scope_bytes(text, self.SCOPE))

    def test_an_edit_outside_the_scope_is_not_a_violation(self) -> None:
        """The exact case that broke the seal: CLAIM 005 moved, the export scope did not."""
        edited = self.REGISTRY.replace("**Summary:** out of scope.",
                                       "**Summary:** narrowed, medication caution deleted.")
        self.assertNotEqual(edited, self.REGISTRY)
        self.assertEqual(self.digest(edited), self.digest(self.REGISTRY))

    def test_an_edit_inside_the_scope_is_a_violation(self) -> None:
        """And the check is worthless unless this one fails."""
        edited = self.REGISTRY.replace("**Summary:** in scope.", "**Summary:** reworded.")
        self.assertNotEqual(self.digest(edited), self.digest(self.REGISTRY))

    def test_a_vanished_scope_block_is_reported_not_ignored(self) -> None:
        with self.assertRaises(ValueError):
            protocol.registry_scope_bytes(
                self.REGISTRY.replace("## CLAIM 016", "## CLAIM 999"), self.SCOPE)

    def test_appending_a_sibling_block_is_not_a_violation(self) -> None:
        """The test that was missing, and the case that fired on 2026-08-06.

        `CLAIM 024` is last in this fixture, so its extraction runs to end-of-file. Appending
        `CLAIM 036` after it inserts the separator that necessarily sits between two records
        — and the previous extractor counted that separator as part of CLAIM 024. A growing
        registry appends constantly, so an extractor that cannot tell *"a record was added
        after mine"* from *"my record changed"* reports the first as the second forever.
        """
        appended = self.REGISTRY + (
            "\n---\n\n## CLAIM 036\n**Status:** in observation\n**Summary:** brand new.\n")
        self.assertNotEqual(appended, self.REGISTRY)
        self.assertEqual(self.digest(appended), self.digest(self.REGISTRY))

    def test_trailing_separator_variants_all_normalise(self) -> None:
        """Whichever separator style a future batch uses, the sealed digest must not move."""
        for tail in ("\n---\n", "\n\n---\n\n", "\n\n---\n\n---\n\n", "\n\n\n"):
            with self.subTest(tail=repr(tail)):
                self.assertEqual(self.digest(self.REGISTRY + tail),
                                 self.digest(self.REGISTRY))

    def test_appending_still_cannot_hide_a_real_edit(self) -> None:
        """Separator tolerance must not become content tolerance."""
        appended = (self.REGISTRY.replace("**Summary:** also in scope.",
                                          "**Summary:** also in scope, reworded.")
                    + "\n---\n\n## CLAIM 036\n**Summary:** new.\n")
        self.assertNotEqual(self.digest(appended), self.digest(self.REGISTRY))

    def test_the_live_baseline_pins_no_living_file_by_whole_hash(self) -> None:
        baseline = protocol.load_json(protocol.BASELINE)
        living = {"claim_registry_current.md", "paper_registry_current.md",
                  "fulltext_read_receipts.jsonl"}
        for name, record in baseline["inputs"].items():
            if Path(record["path"]).name in living:
                with self.subTest(input=name):
                    self.assertIn(record.get("verification_policy"),
                                  {"sealed_scope", "append_only_prefix"},
                                  f"{name} is pinned by whole file — see FREEZE_SCOPE_GATE")

    def test_the_verifier_is_not_sealed_by_the_baseline_it_checks(self) -> None:
        """Otherwise the seal can only ever be abandoned, never repaired."""
        baseline = protocol.load_json(protocol.BASELINE)
        sealed = {Path(record["path"]).name for record in baseline["inputs"].values()}
        self.assertNotIn("dismech_independent_protocol.py", sealed)
        self.assertNotIn("test_dismech_independent_protocol.py", sealed)

    def test_the_window_declares_itself_closed(self) -> None:
        window = protocol.load_json(protocol.BASELINE).get("window") or {}
        self.assertEqual(window.get("state"), "closed")
        self.assertIn("axes", window.get("rationale", ""))
        self.assertTrue(window.get("before_phase5_pr"))


class DriftReportsAndTheExportGateTests(unittest.TestCase):
    """A freeze over living state informs; the gate bites at export time.

    Exports are periodic and in principle endless, and the model keeps being corrected —
    correction is the product, not an exception. So each past seal would otherwise go red at
    its own moment, correctly and uselessly, until nobody read the suite. These tests pin the
    two halves of that split: historical drift must NOT fail the baseline, and unresolved
    drift MUST stop a new export.
    """

    REGISTRY = (
        "# Claim registry\n\n"
        "## CLAIM 016\n**Summary:** as consumed.\n\n"
        "## CLAIM 024\n**Summary:** also as consumed.\n"
    )

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        registry = self.root / "registries/claims.md"
        registry.parent.mkdir(parents=True)
        registry.write_text(self.REGISTRY, encoding="utf-8")
        self.registry = registry
        self.log = self.root / "acks.jsonl"

        def digest(block: str, text: str) -> str:
            kind, _, ident = block.partition(" ")
            body = protocol._registry_block(text, kind, ident)
            return protocol.sha256_bytes((f"## {kind} {ident}" + body).encode("utf-8"))

        self.digest = digest
        # `output` is verified against the repository root rather than the injected one, so
        # the fixture borrows the real record. The property under test is the scope half; the
        # output half is held constant instead of being fought.
        real_output = protocol.load_json(protocol.BASELINE)["output"]
        self.baseline_path = self.root / "baseline.json"
        self.baseline_path.write_text(json.dumps({
            "inputs": {"claim_registry": {
                "path": "registries/claims.md",
                "scope_blocks": ["CLAIM 016", "CLAIM 024"],
                "verification_policy": "sealed_scope",
                "scope_block_sha256": {
                    "CLAIM 016": digest("CLAIM 016", self.REGISTRY),
                    "CLAIM 024": digest("CLAIM 024", self.REGISTRY),
                },
            }},
            "output": real_output,
        }), encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def drift(self):
        return protocol.scope_drift(self.baseline_path, self.root)

    def gate(self):
        return protocol.assert_exportable(self.baseline_path, self.root, self.log)

    def move_one_block(self) -> str:
        self.registry.write_text(
            self.REGISTRY.replace("**Summary:** as consumed.",
                                  "**Summary:** corrected by a later reading."),
            encoding="utf-8")
        return self.digest("CLAIM 016", self.registry.read_text(encoding="utf-8"))

    def test_no_drift_when_nothing_moved(self) -> None:
        self.assertEqual([], self.drift())
        self.assertEqual([], self.gate())

    def test_drift_is_reported_per_block_not_per_file(self) -> None:
        self.move_one_block()
        drifted = self.drift()
        self.assertEqual(1, len(drifted), "one block moved, so one record — not 'the scope'")
        self.assertEqual("CLAIM 016", drifted[0]["block"])
        self.assertEqual("changed", drifted[0]["state"])

    def test_a_vanished_block_drifts_rather_than_raising(self) -> None:
        self.registry.write_text(self.REGISTRY.replace("## CLAIM 024", "## CLAIM 099"),
                                 encoding="utf-8")
        states = {item["block"]: item["state"] for item in self.drift()}
        self.assertEqual("missing", states.get("CLAIM 024"))

    def test_unresolved_drift_blocks_a_new_export(self) -> None:
        self.move_one_block()
        problems = self.gate()
        self.assertEqual(1, len(problems))
        self.assertIn("UNRESOLVED_DRIFT", problems[0])
        self.assertIn("CLAIM 016", problems[0])

    def test_acknowledging_the_drift_clears_the_gate(self) -> None:
        live = self.move_one_block()
        self.log.write_text(json.dumps({
            "block": "CLAIM 016", "live_sha256": live,
            "verdict": "no_reissue_needed",
            "reason": "the export cites this claim for a sentence the correction did not touch",
        }) + "\n", encoding="utf-8")
        self.assertEqual([], self.gate())
        self.assertEqual(1, len(self.drift()), "the drift itself still shows in the report")

    def test_an_acknowledgement_expires_when_the_block_moves_again(self) -> None:
        """Otherwise 'resolved' decays into 'ignored once, ignored forever'."""
        live = self.move_one_block()
        self.log.write_text(json.dumps({
            "block": "CLAIM 016", "live_sha256": live, "verdict": "no_reissue_needed",
            "reason": "reviewed",
        }) + "\n", encoding="utf-8")
        self.assertEqual([], self.gate())
        self.registry.write_text(
            self.REGISTRY.replace("**Summary:** as consumed.", "**Summary:** corrected twice."),
            encoding="utf-8")
        self.assertEqual(1, len(self.gate()),
                         "a second correction must need a second look")

    def test_an_unknown_verdict_does_not_count_as_acknowledgement(self) -> None:
        live = self.move_one_block()
        self.log.write_text(json.dumps({
            "block": "CLAIM 016", "live_sha256": live, "verdict": "looks fine to me",
        }) + "\n", encoding="utf-8")
        self.assertEqual(1, len(self.gate()),
                         "free-text verdicts must not open the gate")

    def test_historical_drift_does_not_fail_the_baseline_verifier(self) -> None:
        """The whole point: a corrected registry is not a broken freeze."""
        self.move_one_block()
        errors = protocol.verify_phase2_baseline(self.baseline_path, verify_git=False)
        self.assertEqual([], [e for e in errors if "scope" in e.lower()])


if __name__ == "__main__":
    unittest.main(verbosity=2)
