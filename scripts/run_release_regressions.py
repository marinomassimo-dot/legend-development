#!/usr/bin/env python3
"""Run the complete public-release regression inventory from repository root."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIORITY_TESTS = (
    "scripts/test_public_release_gate.py",
    "scripts/test_independent_privacy_scan.py",
    "scripts/test_losslessness_manifest.py",
    # Enrolled with the rule it guards, in the same commit: an operating rule whose test is
    # added later is unenforced for exactly as long as that gap lasts.
    "scripts/test_stop_policy.py",
    # `test_stop_policy` pins the two sections and checks the router links to their FILE.
    # This one checks the router links to the two SECTIONS, in the part of the surface read
    # before acting — the gap a session fell through on 2026-09-04 with every check green.
    "scripts/test_stop_policy_is_reachable.py",
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
    # The runner names any suite that writes a tracked file under a guarded tree -
    # 54 dossiers were overwritten during an unattended battery on 2026-09-10 and
    # nothing could say by which suite. Enrolled beside the verdict suite it extends.
    "scripts/test_release_runner_guard.py",
    "scripts/test_repository_surface_determinism.py",
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
    # The commit wrapper three concurrent actors depend on. Enrolled in the same
    # commit that versions the tool, because a wrapper that lived in a scratchpad
    # and shipped defective twice (2026-09-09 retrospective § 4.1) is exactly the
    # kind of infrastructure whose absence from the suite is how it stayed broken.
    "scripts/test_legend_commit.py",
    "launch/test_legend_launch.py",
    "framework/scripts/test_legend_lint.py",
    "framework/scripts/test_batch_commit.py",
    "framework/scripts/test_generate_semantic_graph.py",
    "framework/scripts/test_coverage_report.py",
    "framework/scripts/test_batch_queue.py",
    "framework/scripts/test_pubmed_clipboard_to_seed.py",
    "framework/scripts/test_pubmed_corpus_harvest.py",
    "framework/scripts/test_fulltext_receipts.py",
    # Measures whether a reading that contradicted a persisted locator was audited
    # blind - the fourth Annex C.1 R4 trigger, added 2026-09-10. It reports a ratio
    # and never blocks; what the suite pins is that the ratio is honest.
    "framework/scripts/test_locator_contradiction_audit.py",
    # Parses the required ATTRIBUTION_CENSUS block and the two §21c keys. Also a
    # ratio, never a block: a measurement that can fail a build gets written to
    # pass the build.
    "framework/scripts/test_attribution_census.py",
    # Resolves a lot's internal edges before assignment. Offline in the suite;
    # its network routes are stubbed, because a regression that needs NCBI to be
    # up is a regression that will be disabled the first week it is not.
    "framework/scripts/test_lot_internal_edges.py",
    # The P7 event ledger, enrolled in the commit that builds it. It reuses the receipt
    # ledger's chain-and-lock pattern, so the two suites go red together if that pattern
    # is broken — which is the point of not having invented a second one.
    "framework/scripts/test_event_ledger.py",
    "framework/scripts/test_session_self_eval.py",
    "framework/scripts/test_deepdive_manifest.py",
    "framework/scripts/test_dependency_integrity.py",
    "framework/scripts/test_benchmark_input_surface.py",
    "framework/scripts/test_regenerate_adjudications.py",
    "framework/scripts/test_lease_state.py",
    "governance/scripts/test_governance_fingerprint.py",
    "framework/scripts/test_repo_root.py",
    # The suite above imports check_needles and never calls run(); every fail-open state
    # lived in run(). This one drives the script as a subprocess and asserts the exit code
    # a gate would read. It needs no PDF corpus — it builds its own single-page source.
    "framework/scripts/test_regenerate_adjudications_fails_closed.py",
    "governance/scripts/test_consolidate_approval_queue.py",
    "governance/scripts/test_consolidate_approval_queue_cli.py",
    "framework/scripts/test_growth_anchors.py",
    "framework/scripts/test_integration_matrix.py",
    "framework/scripts/test_record_conventions.py",
    "framework/scripts/test_artifact_index.py",
    # Tracked and passing, but absent from this inventory until 2026-08-23 — found by
    # test_release_runner_verdict.py's own "every tracked suite is actually run" check,
    # which was failing for this one reason before DISCOVERY was added beside it.
    "governance/scripts/test_candidate_content_hash.py",
    "framework/scripts/test_trace_claim_foundation.py",
    "framework/scripts/test_legend_handoff.py",
    "framework/scripts/test_build_evidence_index.py",
    "framework/scripts/test_pathograph.py",
    "framework/scripts/test_surface_census.py",
    "framework/scripts/test_locator_audit.py",
    "framework/scripts/test_dossier_quote_audit.py",
    "framework/scripts/test_reading_state.py",
    "framework/scripts/test_sync_epochs.py",
    "framework/scripts/test_figure_ppi_preflight.py",
    "framework/scripts/test_pmc_pow_fetch.py",
    "framework/scripts/test_recapture_snippets.py",
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


def discover_tests(root: Path) -> tuple[str, ...]:
    """Include uncommitted suites; exclude ignored files and other worktrees.

    Source archives have no index: walk them while pruning dependency/cache directories
    and nested checkouts. Git failures in an actual checkout remain errors.
    """
    if (root / ".git").exists():
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard",
             "*test_*.py"], cwd=root, capture_output=True, text=True, check=True)
        return tuple(sorted({p for p in result.stdout.split("\0")
                             if p and Path(p).name.startswith("test_")}))
    found = []
    for directory, children, files in os.walk(root):
        children[:] = sorted(child for child in children
                             if child not in {".git", "__pycache__", "node_modules", ".venv", "venv"}
                             and not (Path(directory) / child / ".git").exists()
                             and not (Path(directory) / child).is_symlink())
        found.extend((Path(directory) / name).relative_to(root).as_posix()
                     for name in files if name.startswith("test_") and name.endswith(".py"))
    return tuple(sorted(found))


#: An exclusion is a decision with a reason, never a name silently absent from the battery.
#: Keys are repo-relative paths that exist; `test_release_runner_verdict.py` checks both.
NOT_RUN_BY_DESIGN: dict[str, str] = {}


def battery(priority: tuple[str, ...], discovered: tuple[str, ...],
            excluded: dict[str, str]) -> tuple[str, ...]:
    """Established order first, then every discovered suite, minus recorded exclusions."""
    return tuple(name for name in dict.fromkeys((*priority, *discovered))
                 if name not in excluded)


DISCOVERED_TESTS = discover_tests(ROOT)
# Preserve the established execution order, but no suite needs manual enrollment.
TESTS = battery(PRIORITY_TESTS, DISCOVERED_TESTS, NOT_RUN_BY_DESIGN)


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



# Trees a regression suite may READ and must never WRITE. On 2026-09-10, during an
# unattended run, 54 tracked dossiers under disease-models/ were overwritten with the seven
# bytes "touched" while three suites were being exercised, and no suite, tool or transcript
# contained that literal. The runner had no way to say which suite did it, because it
# measured exit codes and nothing else. It now hashes every tracked file under these trees
# before the battery and after each suite; a suite that changes one is named in the output
# and fails the verdict on its own, whatever its exit code. Cheap: one `git ls-files -s`
# per suite, index-side, no content read.
GUARDED_TREES = ("disease-models", "governance", "roles", "framework/protocols",
                 "framework/instruction", "framework/state", "learning", "ledger")


def mtime_verdict(path: Path, started: float, finished: float) -> str:
    """Was the file written inside this suite's window, or by someone else outside it.

    The guard cannot tell a suite's write from a concurrent peer edit by content. It can by
    time, when the edit falls outside the suite's own run: an mtime before `started` or after
    `finished` exonerates the suite by arithmetic. Inside the window stays ambiguous and says
    so — the first false attribution, on 2026-09-11, was a peer's edit inside the window.
    """
    try:
        mtime = path.stat().st_mtime
    except OSError:
        return "mtime unavailable (deleted?)"
    clock = lambda t: time.strftime("%H:%M:%S", time.gmtime(t))  # noqa: E731
    window = f"suite ran {clock(started)}-{clock(finished)} UTC"
    if mtime < started - 1:
        return f"WRITTEN BEFORE THE SUITE at {clock(mtime)} - not this suite ({window})"
    if mtime > finished + 1:
        return f"WRITTEN AFTER THE SUITE at {clock(mtime)} - not this suite ({window})"
    return f"written INSIDE the window at {clock(mtime)} - this suite or a concurrent editor ({window})"


def tracked_state(trees: tuple[str, ...], root: Path = ROOT) -> dict[str, str]:
    """{path: blob-or-worktree hash} for every tracked file under the guarded trees.

    `git ls-files -s` reports the INDEX blob, which does not move when the working tree is
    written, so the working tree is hashed through `git hash-object --stdin-paths`: what a
    suite wrote is what a later commit would carry, and that is the thing to detect.
    """
    # Tracked files AND untracked creations: Mirror REV-EXPOST-20260911-001 F1(c) showed a new
    # file created under a guarded tree was invisible to a tracked-only state. `--others
    # --exclude-standard` lists what git would call untracked, honouring .gitignore, so files/
    # stays out and a suite that plants a dossier is caught.
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", *trees],
        cwd=root, stdout=subprocess.PIPE, text=True, check=False).stdout
    paths = [p for p in listing.split("\0") if p]
    if not paths:
        return {}
    hashed = subprocess.run(
        ["git", "hash-object", "--stdin-paths"], cwd=root, input="\n".join(paths) + "\n",
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=False).stdout
    digests = hashed.split("\n")
    return {path: digest for path, digest in zip(paths, digests)}


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
    writers: list[tuple[str, list[str]]] = []
    baseline = tracked_state(GUARDED_TREES)
    for relative in selected:
        print(f"RUN {relative}", flush=True)
        started = time.time()
        result = subprocess.run(
            [sys.executable, relative], cwd=ROOT,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        finished = time.time()
        sys.stdout.write(result.stdout)
        sys.stdout.flush()
        after = tracked_state(GUARDED_TREES)
        if after != baseline:
            changed = sorted(set(after.items()) ^ set(baseline.items()))
            paths = sorted({path for path, _ in changed})
            writers.append((relative, paths))
            print(f"TRACKED_FILES_WRITTEN_BY_SUITE {relative}: {len(paths)} path(s)",
                  flush=True)
            for path in paths[:20]:
                print(f"  wrote {path}  {mtime_verdict(ROOT / path, started, finished)}",
                      flush=True)
            baseline = after
        skips.extend((relative, reason) for reason in extract_skip_reasons(result.stdout))
        if result.returncode:
            failures.append((relative, result.returncode))

    if failures or writers:
        print("REGRESSION VERDICT: FAIL", file=sys.stderr)
        for relative, paths in writers:
            print(f"- {relative}: WROTE {len(paths)} tracked file(s) under a guarded tree",
                  file=sys.stderr)
        for relative, returncode in failures:
            print(f"- {relative}: exit {returncode}", file=sys.stderr)
        return 1
    for line in format_success_verdict(len(selected), skips):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
