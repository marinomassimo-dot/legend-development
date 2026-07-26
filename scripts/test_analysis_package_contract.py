#!/usr/bin/env python3
"""Verify public replacements and reproducibility for the analysis package."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "disease-models" / "wwox" / "analysis"
REDTEAM = ANALYSIS / "data" / "redteam"


class AnalysisPackageContractTests(unittest.TestCase):
    def test_compressed_private_narratives_have_substantive_replacements(self) -> None:
        replacements = {
            "structural interpretation": (
                ANALYSIS / "variant_structural_pipeline.md",
            ),
            "splice interpretation": (
                ANALYSIS / "variant_triage_rescuability.md",
                ANALYSIS / "therapy_levers.md",
            ),
            "proteostasis and chaperone rationale": (
                ANALYSIS / "proteostasis_rationale.md",
            ),
            "therapy-lever interpretation": (
                ANALYSIS / "therapy_levers.md",
            ),
            "GTEx tissue-proxy interpretation": (
                ROOT
                / "disease-models"
                / "wwox"
                / "biomarker_endpoint"
                / "biomarker_candidates_current.md",
            ),
        }
        failures = []
        for label, paths in replacements.items():
            for path in paths:
                if not path.is_file():
                    failures.append(f"{label}: missing {path.relative_to(ROOT)}")
                    continue
                substantive = [
                    line
                    for line in path.read_text(encoding="utf-8").splitlines()
                    if line.strip() and not line.lstrip().startswith("#")
                ]
                if len(substantive) < 15:
                    failures.append(
                        f"{label}: {path.relative_to(ROOT)} is not substantive"
                    )
        self.assertFalse(failures, "\n".join(failures))

    def test_analysis_replacements_keep_decisive_method_anchors(self) -> None:
        paths = (
            ANALYSIS / "variant_structural_pipeline.md",
            ANALYSIS / "variant_triage_rescuability.md",
            ANALYSIS / "therapy_levers.md",
            ANALYSIS / "proteostasis_rationale.md",
            ROOT
            / "disease-models"
            / "wwox"
            / "biomarker_endpoint"
            / "biomarker_candidates_current.md",
        )
        corpus = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        anchors = {
            "orthogonal structural predictors": (
                r"\bAlphaFold\b",
                r"\bThermoMPNN\b",
                r"\bESM-?2\b",
                r"\b(?:relSASA|SASA)\b",
            ),
            "splice discrimination": (
                r"\bSpliceAI\b",
                r"\bMaxEnt",
                r"(?i)\bcryptic\b|\bcriptic",
                r"\bNMD\b",
            ),
            "proteostasis intervention space": (
                r"\b4-PBA\b",
                r"\bTUDCA\b",
                r"\b(?:HSP70|HSC70)\b",
                r"(?i)\bproteasom",
                r"(?i)\blysosom|\blisosom",
            ),
            "therapy modalities": (
                r"\bASO\b",
                r"(?i)\bgene therapy\b|\bterapia genica\b",
            ),
            "GTEx proxy calibration": (
                r"\bGTEx\b",
                r"\b0\.71\b",
                r"\b2\.24\b",
                r"\b3\.17\b",
                r"\b6\.82\b",
            ),
        }
        failures = [
            f"{label}: missing {pattern}"
            for label, patterns in anchors.items()
            for pattern in patterns
            if not re.search(pattern, corpus)
        ]
        self.assertFalse(failures, "\n".join(failures))

    def test_redteam_readme_is_honest_about_reconstructable_inputs(self) -> None:
        readme = (REDTEAM / "README.md").read_text(encoding="utf-8")
        reconstructable = {
            "AF-Q9NZC7-F1.pdb",
            "AF-Q9NZC7-F1-PAE.json",
            "AF_nohelix.pdb",
            "1WMV.pdb",
        }
        missing = [name for name in reconstructable if not (REDTEAM / name).is_file()]
        self.assertEqual(reconstructable, set(missing))
        qualifier = re.compile(
            r"(?i)(?:not shipped|reconstruct(?:ed|able)?|generated on demand|"
            r"downloaded on demand)"
        )
        self.assertRegex(
            readme,
            qualifier,
            "Red-team README lists absent structure inputs as deliverables "
            "without saying they are reconstructed/downloaded on demand.",
        )
        self.assertTrue(
            (ANALYSIS / "scripts" / "prepare_redteam_structures.py").is_file()
        )

    def test_redteam_reconstruction_commands_match_the_cli(self) -> None:
        readme = (REDTEAM / "README.md").read_text(encoding="utf-8")
        bash_blocks = "\n".join(
            match.group(1)
            for match in re.finditer(r"```bash\s*\n(.*?)```", readme, re.S)
        )
        required = ("--alphafold-pdb", "--output-dir", "--fetch-public")
        missing = [flag for flag in required if flag not in bash_blocks]
        self.assertFalse(
            missing,
            "Red-team reconstruction command uses flags not exposed by "
            "prepare_redteam_structures.py; missing:\n" + "\n".join(missing),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
