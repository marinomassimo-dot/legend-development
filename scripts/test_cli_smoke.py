#!/usr/bin/env python3
"""Smoke-test every declared public command without network or writes.

🔴 A MISSING OPTIONAL DEPENDENCY IS NOT A BROKEN COMMAND, AND IT IS NOT A PASS EITHER.

Three of these commands import `numpy` or `PyMuPDF`, which `requirements-analysis.txt` declares
as OPTIONAL. On a deployment without them this suite reported `exit 1` for each — indistinguishable
in the release battery from a command whose argparse had been broken. That violates the rule
`test_repository_surface_determinism.py` exists to enforce: *same tracked tree, same verdict,
whatever else is on the disk.* The verdict was following the machine, not the tree.

So a `--help` that dies on `ModuleNotFoundError` for a module **this repository does not ship**
is reported as SKIPPED with the module named. Anything else — a syntax error, a broken argparse,
a failed local import — is still a failure, because a module the repository *does* ship being
unimportable is exactly the breakage this suite exists to catch. The shipped set is derived from
`git ls-files`, never listed, so a new local module is covered the day it lands.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_CLIS = (
    "scripts/public_release_gate.py",
    "scripts/independent_privacy_scan.py",
    "scripts/phenotypic_neighbors.py",
    "scripts/legend/residue_context.py",
    "framework/scripts/legend_lint.py",
    # The two commands `operator_manual.md` 1.1-1.3 now routes every scientific session
    # through. They were absent from this list until 2026-09-18 — the surface a reader is
    # told to run every session was the one surface with no --help coverage.
    "framework/scripts/registry_records.py",
    "framework/scripts/paper_packet.py",
    "framework/scripts/batch_commit.py",
    "framework/scripts/unread_gold.py",
    "framework/scripts/generate_semantic_graph.py",
    "framework/scripts/pathograph.py",
    "framework/scripts/fulltext_receipts.py",
    "framework/scripts/surface_census.py",
    "disease-models/wwox/analysis/scripts/residue_context.py",
    "disease-models/wwox/analysis/scripts/kferq_geometry.py",
    "disease-models/wwox/analysis/scripts/prepare_redteam_structures.py",
    "disease-models/wwox/analysis/scripts/md_q230p_pilot.py",
    "disease-models/wwox/analysis/scripts/md_helix_screen.py",
    "disease-models/wwox/analysis/scripts/md_helix_analyze.py",
    "disease-models/wwox/analysis/scripts/md_status.py",
    "disease-models/wwox/analysis/scripts/md_run_matrix.py",
    ".claude/skills/legend-batch-inferential-sweep/scripts/batch_inferential_sweep.py",
    ".claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py",
    ".claude/skills/legend-proband-priority-matrix/scripts/score_proband_priority.py",
    ".claude/skills/legend-study-intake-triage/scripts/retraction_check.py",
    ".claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py",
)


MISSING_MODULE = re.compile(r"ModuleNotFoundError: No module named '([A-Za-z0-9_.]+)'")


def modules_this_repository_ships() -> frozenset[str]:
    """Top-level importable names carried by the tracked tree, from the git index.

    Derived rather than listed, and from the INDEX rather than the disk, for the reasons
    `artifact_index.py` rule 3 and `test_repository_surface_determinism.py` each record.
    """
    listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*.py"],
                            capture_output=True, text=True, check=False).stdout.split()
    return frozenset(Path(item).stem for item in listed)


class PublicCliSmokeTests(unittest.TestCase):
    def test_all_declared_commands_expose_help(self) -> None:
        shipped = modules_this_repository_ships()
        absent: list[str] = []
        failures = []
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        for relative in PUBLIC_CLIS:
            path = ROOT / relative
            if not path.is_file():
                failures.append(f"{relative}: missing")
                continue
            try:
                completed = subprocess.run(
                    [sys.executable, str(path), "--help"],
                    cwd=ROOT,
                    env=environment,
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
            except subprocess.TimeoutExpired:
                failures.append(f"{relative}: --help timed out")
                continue
            if completed.returncode != 0:
                found = MISSING_MODULE.search(completed.stderr)
                if found and found.group(1).split(".")[0] not in shipped:
                    # A dependency this deployment lacks. Named, never counted as verified.
                    absent.append(f"{relative} needs {found.group(1)}")
                    continue
                failures.append(
                    f"{relative}: exit {completed.returncode}: "
                    f"{completed.stderr[-300:]}"
                )
            elif "usage:" not in completed.stdout.lower():
                failures.append(f"{relative}: no usage text")
        self.assertFalse(failures, "\n".join(failures))
        if absent:
            verified = len(PUBLIC_CLIS) - len(absent)
            self.skipTest(
                f"{verified} of {len(PUBLIC_CLIS)} declared commands verified; "
                f"{len(absent)} not run because an OPTIONAL dependency is absent from this "
                f"deployment ({'; '.join(absent)}) — declared in requirements-analysis.txt, "
                f"skipped with the module named, never passed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
