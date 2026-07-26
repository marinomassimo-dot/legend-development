#!/usr/bin/env python3
"""Run the complete public-release regression inventory from repository root."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS = (
    "scripts/test_public_release_gate.py",
    "scripts/test_independent_privacy_scan.py",
    "scripts/test_losslessness_manifest.py",
    "scripts/test_documented_commands.py",
    "scripts/test_fresh_clone_reader_journey.py",
    "scripts/test_mission_contract.py",
    "scripts/test_link_targets.py",
    "scripts/test_public_claims_contract.py",
    "scripts/test_skill_packages.py",
    "scripts/test_agent_pipeline_contract.py",
    "scripts/test_provenance_coverage.py",
    "scripts/test_release_surface.py",
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
    "framework/scripts/test_legend_lint.py",
    "framework/scripts/test_batch_commit.py",
    "framework/scripts/test_generate_semantic_graph.py",
    "framework/scripts/test_coverage_report.py",
    "framework/scripts/test_batch_queue.py",
    "framework/scripts/test_pubmed_clipboard_to_seed.py",
    "framework/scripts/test_fulltext_receipts.py",
    "framework/scripts/test_session_self_eval.py",
    ".claude/skills/legend-study-intake-triage/scripts/"
    "test_study_dedup_triage.py",
    ".claude/skills/legend-batch-inferential-sweep/scripts/"
    "test_batch_inferential_sweep.py",
    "disease-models/wwox/analysis/scripts/test_structural_analysis.py",
    "disease-models/wwox/analysis/scripts/test_md_q230p_pilot.py",
    "disease-models/wwox/analysis/scripts/test_md_helix_screen.py",
    "disease-models/wwox/analysis/scripts/test_md_helix_analyze.py",
    "disease-models/wwox/analysis/scripts/test_md_status.py",
    "disease-models/wwox/analysis/scripts/test_md_run_matrix.py",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the complete public-release regression inventory."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print the ordered test inventory without executing it",
    )
    args = parser.parse_args()

    if args.list:
        print("\n".join(TESTS))
        return 0

    missing = [relative for relative in TESTS if not (ROOT / relative).is_file()]
    if missing:
        print("ERROR: missing regression targets:", file=sys.stderr)
        for relative in missing:
            print(f"- {relative}", file=sys.stderr)
        return 2

    failures = []
    for relative in TESTS:
        print(f"RUN {relative}", flush=True)
        result = subprocess.run([sys.executable, relative], cwd=ROOT)
        if result.returncode:
            failures.append((relative, result.returncode))

    if failures:
        print("REGRESSION VERDICT: FAIL", file=sys.stderr)
        for relative, returncode in failures:
            print(f"- {relative}: exit {returncode}", file=sys.stderr)
        return 1
    print(f"REGRESSION VERDICT: PASS ({len(TESTS)} targets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
