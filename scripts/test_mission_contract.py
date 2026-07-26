#!/usr/bin/env python3
"""Keep the public mission explicit, measurable and epistemically bounded."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MISSION = ROOT / "disease-models" / "wwox" / "mission.md"


class MissionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = MISSION.read_text(encoding="utf-8")

    def test_readme_exposes_the_mission_as_a_front_door(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "[Mission and objectives](disease-models/wwox/mission.md)",
            readme,
        )

    def test_mission_preserves_the_complete_objective_set(self) -> None:
        required = (
            "## 2. Scientific scope — the whole WWOX literature",
            "cancer biology",
            "Alzheimer’s disease",
            "metabolism",
            "## 3. Full-text commitment — the gold is in the details",
            "reading debt",
            "`DATO`",
            "`INFERENZA`",
            "`IPOTESI`",
            "`ESPANSIONE`",
            "## 4. The semantic wiki — the research interface",
            "claims",
            "pathways",
            "therapeutic strategies",
            "candidate biomarkers",
            "candidate research lines",
            "## 5. Therapeutic and biomarker objectives",
            "pharmacological-chaperone",
            "antisense-oligonucleotide",
            "CRISPR",
            "## 6. Variant atlas and experiment prioritization",
            "## 8. Capability growth and controlled compounding",
            "regression fixture",
            "## 9. A scalable method for rare-disease research",
            "## 10. Progress metrics and definition of done",
        )
        missing = [item for item in required if item not in self.text]
        self.assertEqual([], missing, "Mission objectives lost: " + repr(missing))

    def test_ambition_is_not_misrepresented_as_completion(self) -> None:
        required_boundaries = (
            "Scope is an objective, not a completion claim.",
            "Predictions can prioritize laboratory work. They cannot substitute for it.",
            "Nothing in this portfolio is medical advice.",
            "claim corpus completeness without a dated, reproducible coverage report",
        )
        missing = [item for item in required_boundaries if item not in self.text]
        self.assertEqual([], missing)

    def test_old_private_or_parity_conflicts_do_not_return(self) -> None:
        forbidden = (
            "Reduce WWOX-dependent damage in a person",
            "Does this move a patient closer",
            "does not consume a deep-dive",
            "at minimum Methods + Conclusions",
        )
        present = [item for item in forbidden if item in self.text]
        self.assertEqual([], present, "Stale mission conflicts: " + repr(present))


if __name__ == "__main__":
    unittest.main(verbosity=2)
