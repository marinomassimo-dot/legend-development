#!/usr/bin/env python3
"""Run the complete public-release regression inventory from repository root."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS = (
    "scripts/test_public_release_gate.py",
    "scripts/test_independent_privacy_scan.py",
    "scripts/test_losslessness_manifest.py",
    # Enrolled with the rule it guards, in the same commit: an operating rule whose test is
    # added later is unenforced for exactly as long as that gap lasts.
    "scripts/test_stop_policy.py",
    "scripts/test_documented_commands.py",
    "scripts/test_fresh_clone_reader_journey.py",
    "scripts/test_mission_contract.py",
    "scripts/test_link_targets.py",
    "scripts/test_public_claims_contract.py",
    "scripts/test_skill_packages.py",
    "scripts/test_agent_pipeline_contract.py",
    "scripts/test_provenance_coverage.py",
    "scripts/test_freeze_scope.py",
    "scripts/test_release_runner_verdict.py",
    "scripts/test_guard_bash_command.py",
    "scripts/test_locator_obligation_reaches_every_route.py",
    "scripts/test_no_closed_world_assertions_on_live_state.py",
    "scripts/test_abstract_corpus_is_not_evidence.py",
    "scripts/test_release_surface.py",
    "scripts/test_generated_surfaces_are_regenerated.py",
    "scripts/test_structured_data_integrity.py",
    "scripts/test_external_manifest.py",
    "scripts/test_cli_smoke.py",
    "scripts/test_canonical_structure.py",
    "scripts/test_analysis_package_contract.py",
    "scripts/test_scientific_consistency.py",
    "scripts/test_public_prose_quality.py",
    "scripts/test_deepdive_method_contract.py",
    "scripts/test_fulltext_trace_contract.py",
    "scripts/test_phenotypic_neighbors.py",
    "launch/test_legend_launch.py",
    "framework/scripts/test_legend_lint.py",
    "framework/scripts/test_batch_commit.py",
    "framework/scripts/test_generate_semantic_graph.py",
    "framework/scripts/test_coverage_report.py",
    "framework/scripts/test_batch_queue.py",
    "framework/scripts/test_pubmed_clipboard_to_seed.py",
    "framework/scripts/test_pubmed_corpus_harvest.py",
    "framework/scripts/test_fulltext_receipts.py",
    # The P7 event ledger, enrolled in the commit that builds it. It reuses the receipt
    # ledger's chain-and-lock pattern, so the two suites go red together if that pattern
    # is broken — which is the point of not having invented a second one.
    "framework/scripts/test_event_ledger.py",
    "framework/scripts/test_session_self_eval.py",
    "framework/scripts/test_deepdive_manifest.py",
    "framework/scripts/test_benchmark_input_surface.py",
    "framework/scripts/test_regenerate_adjudications.py",
    "framework/scripts/test_growth_anchors.py",
    "framework/scripts/test_record_conventions.py",
    "framework/scripts/test_artifact_index.py",
    # Tracked and passing, but absent from this inventory until 2026-08-23 — found by
    # test_release_runner_verdict.py's own "every tracked suite is actually run" check,
    # which was failing for this one reason before DISCOVERY was added beside it.
    "governance/scripts/test_candidate_content_hash.py",
    "framework/scripts/test_trace_claim_foundation.py",
    "framework/scripts/test_legend_handoff.py",
    "framework/scripts/test_build_evidence_index.py",
    "framework/scripts/test_surface_census.py",
    "framework/scripts/test_locator_audit.py",
    "framework/scripts/test_dossier_quote_audit.py",
    "framework/scripts/test_reading_state.py",
    "framework/scripts/test_sync_epochs.py",
    "framework/scripts/test_figure_ppi_preflight.py",
    "framework/scripts/test_pmc_pow_fetch.py",
    "framework/scripts/test_recapture_snippets.py",
    # The runtime bridge: one guard engine registered by both runtimes, and the battery
    # that refuses the bridge when they stop agreeing. Added 2026-08-26 with the bridge.
    "framework/scripts/test_pre_tool_use_guard.py",
    "framework/scripts/test_runtime_parity.py",
    # The push permission, enrolled with the guard change it constrains. Its integration
    # cases bind the session the way the hook process does and ask guard_policy.verdict
    # itself, because a permission proved only at its own module is a permission nobody
    # has shown the guard consults.
    "framework/scripts/test_push_authorization.py",
    # The probe behind the matcher list. Its finding is a set of ZEROES — which tool names
    # never appear — and a zero from a sweep that silently parsed nothing is indistinguish-
    # able from a zero that is true. This suite is the positive control for those zeroes.
    # 🔴 `codex_runtime_probe.py` itself is NOT enrolled: it reads ~/.codex, which does not
    # exist in CI, and `mutate_guard_suite.py` is not enrolled either — it spawns a worktree
    # per mutation and takes tens of minutes. Both are operator-run instruments; only their
    # parsing is a regression.
    "framework/scripts/test_codex_runtime_probe.py",
    # Ten suites that entered the tree 2026-08-29→08-31 and were never registered. The
    # enrollment invariant in test_release_runner_verdict.py had been failing for exactly
    # this reason: 81 tracked, 71 registered, and "PASS (71 targets)" reads the same as
    # "PASS (81 targets)" to anyone not counting. They are enrolled unchanged — no skip, no
    # xfail, no NOT_RUN_BY_DESIGN entry, no edit to their contents.
    # 🔴 test_runtime_diagnostics.py enters RED and stays red: it asserts the string
    # "Blanket staging is blocked in this repository." inside scripts/guard_bash_command.py,
    # which stopped being the guard when the policy moved to guard_policy.py. That is a dead
    # premise in the test, not a regression in the guard, and repairing it here would be
    # editing a suite to make the battery green — which is the one thing enrollment must not
    # buy. It is left failing, visible, and owned by a separate repair.
    "framework/scripts/test_confinement_and_delegation.py",
    "framework/scripts/test_effect_model.py",
    "framework/scripts/test_execution_attestation.py",
    "framework/scripts/test_execution_receipt.py",
    "framework/scripts/test_guard_families_rev11.py",
    "framework/scripts/test_guard_families_rev12.py",
    "framework/scripts/test_guard_families_rev13.py",
    "framework/scripts/test_post_effect_verify.py",
    "framework/scripts/test_repo_topology.py",
    "framework/scripts/test_runtime_diagnostics.py",
    ".claude/skills/legend-study-intake-triage/scripts/"
    "test_study_dedup_triage.py",
    ".claude/skills/legend-batch-inferential-sweep/scripts/"
    "test_batch_inferential_sweep.py",
    "disease-models/wwox/analysis/scripts/test_derive_dismech_sidecar.py",
    "disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py",
    "disease-models/wwox/analysis/scripts/test_export_dismech_dryrun.py",
    "disease-models/wwox/analysis/scripts/test_structural_analysis.py",
    "disease-models/wwox/analysis/scripts/test_md_q230p_pilot.py",
    "disease-models/wwox/analysis/scripts/test_md_helix_screen.py",
    "disease-models/wwox/analysis/scripts/test_md_helix_analyze.py",
    "disease-models/wwox/analysis/scripts/test_md_status.py",
    "disease-models/wwox/analysis/scripts/test_md_run_matrix.py",
)


SKIP_REASON_RE = re.compile(r"\.\.\. skipped ['\"](.+?)['\"]\s*$")
SKIP_SUMMARY_RE = re.compile(r"OK \(skipped=(\d+)\)")


def extract_skip_reasons(output: str) -> list[str]:
    """Return one reason per unittest skip, retaining unknown reasons explicitly."""
    reasons = [match.group(1) for line in output.splitlines()
               if (match := SKIP_REASON_RE.search(line))]
    declared = sum(int(value) for value in SKIP_SUMMARY_RE.findall(output))
    if declared > len(reasons):
        reasons.extend(["reason unavailable"] * (declared - len(reasons)))
    return reasons


def format_success_verdict(target_count: int,
                           skips: list[tuple[str, str]]) -> list[str]:
    if not skips:
        return [f"REGRESSION VERDICT: PASS ({target_count} targets)"]
    lines = [
        f"REGRESSION VERDICT: PASS WITH SKIPS "
        f"({target_count} targets, {len(skips)} skipped)"
    ]
    lines.extend(f"- {target}: {reason}" for target, reason in skips)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the complete public-release regression inventory."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print the ordered test inventory without executing it",
    )
    parser.add_argument(
        "--only",
        action="append",
        metavar="RELATIVE_TEST_PATH",
        help="run only the named regression target; repeat for more than one",
    )
    args = parser.parse_args()

    if args.list:
        print("\n".join(TESTS))
        return 0

    selected = tuple(args.only) if args.only else TESTS
    unknown = [relative for relative in selected if relative not in TESTS]
    if unknown:
        print("ERROR: --only target is not in the release inventory:", file=sys.stderr)
        for relative in unknown:
            print(f"- {relative}", file=sys.stderr)
        return 2

    missing = [relative for relative in selected if not (ROOT / relative).is_file()]
    if missing:
        print("ERROR: missing regression targets:", file=sys.stderr)
        for relative in missing:
            print(f"- {relative}", file=sys.stderr)
        return 2

    failures = []
    skips: list[tuple[str, str]] = []
    for relative in selected:
        print(f"RUN {relative}", flush=True)
        result = subprocess.run(
            [sys.executable, relative], cwd=ROOT,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        sys.stdout.write(result.stdout)
        sys.stdout.flush()
        skips.extend((relative, reason) for reason in extract_skip_reasons(result.stdout))
        if result.returncode:
            failures.append((relative, result.returncode))

    if failures:
        print("REGRESSION VERDICT: FAIL", file=sys.stderr)
        for relative, returncode in failures:
            print(f"- {relative}: exit {returncode}", file=sys.stderr)
        return 1
    for line in format_success_verdict(len(selected), skips):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
