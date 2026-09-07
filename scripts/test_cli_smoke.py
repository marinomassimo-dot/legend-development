#!/usr/bin/env python3
"""Smoke-test every declared public command without network or writes."""

from __future__ import annotations

import os
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


class PublicCliSmokeTests(unittest.TestCase):
    def test_all_declared_commands_expose_help(self) -> None:
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
                failures.append(
                    f"{relative}: exit {completed.returncode}: "
                    f"{completed.stderr[-300:]}"
                )
            elif "usage:" not in completed.stdout.lower():
                failures.append(f"{relative}: no usage text")
        self.assertFalse(failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
