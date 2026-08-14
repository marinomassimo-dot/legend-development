#!/usr/bin/env python3
"""Adversarial coverage for the post-batch self-evaluation gate.

Per `CONTRACT_MUST_REACH_THE_GATE`, a new contract is only real if the damage it
describes actually changes the verdict. Each case below reconstructs a state the
repository genuinely produced or could produce, and asserts the gate reacts.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "framework" / "scripts" / "session_self_eval.py"

RECEIPT = {
    "event_id": "FTR-TEST-01",
    "record_kind": "contemporaneous_receipt",
    "study_id": {"pmid": "34214506", "doi": "10.1016/j.ajpath.2021.06.006"},
    "evidence_depth": "complete_fulltext_read",
    "outputs": [],
}


def build(tmp: Path, receipt: dict, ledgers: dict[str, str]) -> Path:
    root = tmp / "ws"
    (root / "disease-models/wwox/registries").mkdir(parents=True)
    (root / "disease-models/wwox/research").mkdir(parents=True)
    (root / "disease-models/wwox/registries/fulltext_read_receipts.jsonl").write_text(
        json.dumps(receipt) + "\n", encoding="utf-8"
    )
    for name, text in ledgers.items():
        target = root / "disease-models/wwox/research" / name
        if "registries" in name:
            target = root / "disease-models/wwox" / name
        target.write_text(text, encoding="utf-8")
    return root


def run(root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--workspace", str(root), "--disease", "wwox"],
        capture_output=True, text=True, check=False,
    )


class SelfEvalGate(unittest.TestCase):
    def test_diagnosis_is_wired_before_growth_and_takeaways(self) -> None:
        """A checker nobody invokes is documentation, not a workflow guarantee."""
        required = {
            "CLAUDE.md": "session_self_evaluation.md",
            "framework/instruction/LEGEND_CORE.md": "POST-BATCH SELF-DIAGNOSIS",
            ".claude/skills/legend/SKILL.md": "Phase 7 — SELF-DIAGNOSIS",
            ".claude/skills/legend-session-takeaways/SKILL.md": "session_self_evaluation.md",
        }
        for relative, marker in required.items():
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(marker, text, f"self-diagnosis is not wired into {relative}")

        orchestrator = (ROOT / ".claude/skills/legend/SKILL.md").read_text(encoding="utf-8")
        self.assertLess(
            orchestrator.index("Phase 7 — SELF-DIAGNOSIS"),
            orchestrator.index("Phase 8 — GROWTH"),
        )
        self.assertLess(
            orchestrator.index("Phase 8 — GROWTH"),
            orchestrator.index("Phase 9 — TAKEAWAYS"),
        )

    def test_orphan_complete_read_is_blocked(self) -> None:
        """The real 2026-07-26 state: read cover to cover, landed nowhere."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(Path(tmp), RECEIPT, {"discovery_ledger_current.md": "# empty\n"})
            result = run(root)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("ORPHAN_COMPLETE_READ", result.stdout)

    def test_incidental_pmid_mention_is_not_a_landing(self) -> None:
        """A process note naming the paper must not clear its scientific landing debt."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), RECEIPT,
                {"discovery_ledger_current.md":
                 "### Process note\nPMID 34214506 still needs to land.\n"},
            )
            result = run(root)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("ORPHAN_COMPLETE_READ", result.stdout)

    def test_literature_tracking_record_is_a_structured_landing(self) -> None:
        """A registry the gate reads must recognise the registry's own record IDs."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), RECEIPT,
                {"registries/literature_tracking_log_current.md":
                 "## LIT-0333\n**Identifier:** PMID 34214506\n"},
            )
            result = run(with_manifest(root, MANIFEST_OK))
            self.assertEqual(0, result.returncode, result.stdout)

    def test_corpus_placeholder_is_a_structured_landing(self) -> None:
        """A CORPUS placeholder is a real paper-registry record, not incidental prose."""
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), RECEIPT,
                {"registries/paper_registry_current.md":
                 "## CORPUS P333\n**Identifier:** PMID 34214506\n"},
            )
            result = run(with_manifest(root, MANIFEST_OK))
            self.assertEqual(0, result.returncode, result.stdout)

    def test_declared_output_id_that_does_not_exist_is_blocked(self) -> None:
        """The real defect: a hash-chained receipt naming records nobody created."""
        receipt = dict(RECEIPT, outputs=["discovery_ledger_current.md DL-MECH-061"])
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), receipt,
                {"discovery_ledger_current.md": "### DL-MECH-060 — other\nPMID 34214506\n"},
            )
            result = run(root)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("UNRESOLVED_OUTPUT_ID", result.stdout)

    def test_declared_output_file_that_does_not_exist_is_blocked(self) -> None:
        receipt = dict(RECEIPT, outputs=["staging/dossier_that_was_never_written.md"])
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), receipt,
                {"discovery_ledger_current.md":
                 "### DL-MECH-061 — landed\nPMID 34214506\n"},
            )
            result = run(root)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("UNRESOLVED_OUTPUT_FILE", result.stdout)

    def test_existing_output_for_another_study_is_blocked(self) -> None:
        """A filename collision must not satisfy a receipt for the wrong paper."""
        receipt = dict(RECEIPT, outputs=["staging/commit_candidate_002.md"])
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), receipt,
                {"discovery_ledger_current.md": "PMID 34214506 landed here\n"},
            )
            (root / "staging").mkdir()
            (root / "staging/commit_candidate_002.md").write_text(
                "# Candidate for PMID 35716775\n", encoding="utf-8"
            )
            result = run(with_manifest(root, MANIFEST_OK))
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("OUTPUT_STUDY_MISMATCH", result.stdout)

    def test_landed_paper_with_resolving_outputs_passes(self) -> None:
        receipt = dict(RECEIPT, outputs=["discovery_ledger_current.md DL-MECH-061"])
        with tempfile.TemporaryDirectory() as tmp:
            root = build(
                Path(tmp), receipt,
                {"discovery_ledger_current.md": "### DL-MECH-061 — x\nPMID 34214506\n"},
            )
            # A complete read also needs its work manifest: landing and resolving outputs
            # prove the reading produced something, not that the required steps were taken.
            result = run(with_manifest(root, MANIFEST_OK))
            self.assertEqual(0, result.returncode, result.stdout)
            self.assertIn("PASS", result.stdout)

    def test_partial_reads_are_not_required_to_land(self) -> None:
        """Only a *complete* read carries the landing obligation."""
        receipt = dict(RECEIPT, evidence_depth="retrieved_not_read")
        with tempfile.TemporaryDirectory() as tmp:
            root = build(Path(tmp), receipt, {"discovery_ledger_current.md": "# empty\n"})
            self.assertEqual(0, run(root).returncode)

    def test_live_repository_passes(self) -> None:
        self.assertEqual(0, run(ROOT).returncode, run(ROOT).stdout)


MANIFEST_OK = {
    "pmid": "34214506", "receipt": "FTR-TEST-01",
    "group_assessment": {"total_publications": 207, "publications_on_gene": 1,
                         "research_type": "experimental_lab",
                         "is_primary_group_for_disease": False,
                         "weighting": "unbiased hit strengthens the observation, inexperience weakens the interpretation"},
    "field_density": {"queries": [{"query": "WWOX AND calpain", "count": 2}], "verdict": "near-empty"},
    "multihop": {"gene_direct_refs_in_source": [], "resolved": [], "queued": [],
                 "references_enumerated": 87},
    "corpus_crossquery": {"query": "calpain", "hits": 0, "verdict": "new territory"},
    "retraction_check": {"method": "PubMed record", "result": "none"},
    "verbatim_locators": {"entries": [{"proposition": "fixture proposition",
                                       "snippet": "a verbatim sentence long enough to be a real locator",
                                       "anchor": "Results, Fig. 1"}]},
    "landing": ["DL-MECH-061"],
    "skills_considered": [{"skill": "find-fulltext", "used": True}],
}


def with_manifest(root, manifest, pmid="34214506"):
    d = root / "disease-models/wwox/research/deepdive_manifests"
    d.mkdir(parents=True, exist_ok=True)
    if manifest is not None:
        (d / f"PMID{pmid}.json").write_text(json.dumps(manifest), encoding="utf-8")
    return root


class WorkManifestGate(unittest.TestCase):
    """The manifest turns an omission into a visible, blocking artifact."""

    def _ws(self, tmp, manifest):
        root = build(Path(tmp), dict(RECEIPT, outputs=[]),
                     {"discovery_ledger_current.md": "### DL-MECH-061 — x\nPMID 34214506\n"})
        return with_manifest(root, manifest)

    def test_complete_read_without_manifest_is_blocked(self) -> None:
        """The exact 2026-07-26 hole: steps skipped, nothing to see."""
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, None))
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("WORK_MANIFEST", result.stdout)

    def test_missing_group_assessment_is_blocked(self) -> None:
        bad = {k: v for k, v in MANIFEST_OK.items() if k != "group_assessment"}
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, bad))
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("group_assessment", result.stdout)

    def test_hollow_waiver_is_blocked(self) -> None:
        """'n/a' is how a checklist dies; a waiver must be an argument."""
        bad = dict(MANIFEST_OK, field_density={"waived": "n/a"})
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, bad))
            self.assertEqual(1, result.returncode, result.stdout)

    def test_substantive_waiver_is_accepted(self) -> None:
        ok = dict(MANIFEST_OK, field_density={
            "waived": "Field density was not measured because the mechanism is already "
                      "represented by four consolidated claims in this model."})
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(0, run(self._ws(tmp, ok)).returncode)

    def test_unqueued_gene_direct_references_are_blocked(self) -> None:
        """Naming a gene-direct reference and walking away is unrecorded debt."""
        bad = dict(MANIFEST_OK, multihop={"gene_direct_refs_in_source": ["ref 87 — WWOX binds IkBa"],
                                          "resolved": [], "queued": []})
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, bad))
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("multihop", result.stdout)

    def test_queued_but_unresolved_is_allowed_and_declared(self) -> None:
        ok = dict(MANIFEST_OK, multihop={"gene_direct_refs_in_source": ["ref 87"],
                                         "resolved": [], "queued": ["FT-020"],
                                         "references_enumerated": 87})
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, ok))
            self.assertEqual(0, result.returncode, result.stdout)
            self.assertIn("DECLARED GAP", result.stdout)

    def test_declining_a_skill_without_a_reason_is_blocked(self) -> None:
        bad = dict(MANIFEST_OK, skills_considered=[{"skill": "legend-discovery", "used": False, "reason": "no"}])
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(1, run(self._ws(tmp, bad)).returncode)


class EvidenceTypeAndReferenceList(unittest.TestCase):
    """Counting a group's papers says nothing about what KIND of evidence it can produce."""

    def _ws(self, tmp: str, manifest: dict) -> Path:
        root = build(Path(tmp), RECEIPT, {"discovery_ledger_current.md": "## DL-MECH-061\nPMID 34214506\n"})
        return with_manifest(root, manifest)

    def test_missing_research_type_is_blocked(self) -> None:
        group = dict(MANIFEST_OK["group_assessment"])
        group.pop("research_type")
        bad = dict(MANIFEST_OK, group_assessment=group)
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, bad))
            self.assertEqual(1, result.returncode)
            self.assertIn("research_type", result.stdout)

    def test_invented_research_type_is_blocked(self) -> None:
        group = dict(MANIFEST_OK["group_assessment"], research_type="reputable_journal")
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(1, run(self._ws(tmp, dict(MANIFEST_OK, group_assessment=group))).returncode)

    def test_primary_for_gene_does_not_answer_primary_for_disease(self) -> None:
        group = dict(MANIFEST_OK["group_assessment"])
        group.pop("is_primary_group_for_disease")
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, dict(MANIFEST_OK, group_assessment=group)))
            self.assertEqual(1, result.returncode)
            self.assertIn("is_primary_group_for_disease", result.stdout)

    def test_unenumerated_reference_list_is_blocked(self) -> None:
        """Multi-hop starts at the reference list; declaring debt is not enumerating it."""
        hop = dict(MANIFEST_OK["multihop"])
        hop.pop("references_enumerated")
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, dict(MANIFEST_OK, multihop=hop)))
            self.assertEqual(1, result.returncode)
            self.assertIn("references_enumerated", result.stdout)


class UnreadPremiseRatchet(unittest.TestCase):
    """A conclusion may not start leaning on a paper nobody opened.

    The damage this describes is the one that let PMID 22193544 be load-bearing in five
    reasoning files while unread, with every other check passing. It writes nothing anywhere,
    so it has to be measured.
    """

    def _ws(self, tmp: Path, meta_text: str, baseline: int | None, queue: str = "") -> Path:
        root = build(Path(tmp), RECEIPT, {"discovery_ledger_current.md": ""})
        with_manifest(root, MANIFEST_OK)
        landing = root / "disease-models/wwox/research/discovery_ledger_current.md"
        landing.write_text("## DL-MECH-061\nPMID 34214506 landed here.\n", encoding="utf-8")
        (root / "disease-models/wwox/meta").mkdir(parents=True, exist_ok=True)
        (root / "disease-models/wwox/meta/meta_test_current.md").write_text(meta_text, encoding="utf-8")
        (root / "disease-models/wwox/research/full_text_queue_current.md").write_text(queue, encoding="utf-8")
        state = root / "framework/state"
        state.mkdir(parents=True, exist_ok=True)
        text = "" if baseline is None else f"unread_premise_baseline: {baseline}\n"
        (state / "state_manifest_current.md").write_text(text, encoding="utf-8")
        return root

    def test_new_unread_premise_above_baseline_is_blocked(self) -> None:
        meta = "Therefore the axis holds (PMID 30290271, PMID 31340538)."
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, meta, baseline=1))
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("UNREAD_PREMISE", result.stdout)

    def test_declared_reading_debt_clears_the_citation(self) -> None:
        """Declared debt is legitimate work in progress; silence is not."""
        meta = "Therefore the axis holds (PMID 30290271)."
        with tempfile.TemporaryDirectory() as tmp:
            queue = "## FT-099\n**Paper:** PMID 30290271\n**Priority:** HIGH\n"
            result = run(self._ws(tmp, meta, baseline=0, queue=queue))
            self.assertEqual(0, result.returncode, result.stdout)

    def test_missing_baseline_warns_without_blocking(self) -> None:
        meta = "Therefore the axis holds (PMID 30290271)."
        with tempfile.TemporaryDirectory() as tmp:
            result = run(self._ws(tmp, meta, baseline=None))
            self.assertEqual(0, result.returncode, result.stdout)
            self.assertIn("UNREAD_PREMISE_BASELINE_MISSING", result.stdout)

    def test_live_baseline_is_not_padded(self) -> None:
        """A ratchet set above the real count is a wall that never bites. Keep them equal."""
        measured = subprocess.run(
            [sys.executable, str(SCRIPT), "--workspace", str(ROOT), "--disease", "wwox"],
            capture_output=True, text=True, check=False,
        ).stdout
        count = int(measured.split("unread_premises: ")[1].split("/")[0].split()[0])
        declared = (ROOT / "framework/state/state_manifest_current.md").read_text(encoding="utf-8")
        self.assertIn(f"unread_premise_baseline: {count}", declared)


if __name__ == "__main__":
    unittest.main(verbosity=2)
