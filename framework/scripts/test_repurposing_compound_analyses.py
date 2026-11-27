import tempfile
import unittest
from pathlib import Path

import repurposing_compound_analyses as analyses


class CompoundAnalyses(unittest.TestCase):
    def test_publication_deduplicates_updates_and_preserves_priorities(self):
        with tempfile.TemporaryDirectory() as directory:
            dr = Path(directory)
            files = {
                "continuous_compounds/README.md": (
                    "| 1 | Lead, circuit biology | What changes the decision? |\n"
                    "## Current checkpoint\n"
                    "**Active compound: New.** An independent Codex Strategy review. [Read](new/README.md)\n"
                    "**Older parked.** Reopen when functional evidence arrives. [Read](older/README.md)\n"
                    "**Older parked.** [Second analysis](older/followup.md)\n"
                    "**Comparator parked for a trial.** Retained as a mechanistic probe. [Read](comparator/README.md)\n"
                    "**Counterexample parked.** [Outside](../../private/README.md)\n"
                    "\n## Comparisons by research question\n"
                    "| lead | Lead | Circuit | INV-05 | A functional probe | Source observation. | Unknown transfer. | Compare matched conditions. | [Read](../lead_20261123/README.md) |\n"
                ),
                "cycle_20261123/README.md": (
                    "| Lead | Highest priority for a specific comparison. | [Evidence](../lead_20261123/README.md) |\n"
                    "| Low | Lower priority for timing. | [Evidence](../low_20261123/README.md) |\n"
                ),
                "continuous_compounds/new/README.md": "",
                "continuous_compounds/older/README.md": "",
                "continuous_compounds/older/followup.md": "",
                "continuous_compounds/comparator/README.md": "",
                "continuous_compounds/unreviewed/README.md": "",
                "lead_20261123/README.md": "",
                "low_20261123/README.md": "",
            }
            for name, content in files.items():
                path = dr / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            public_compounds = [{"names_public": [{"label": "A new public compound"}],
                                 "next_test": "Check target engagement."},
                                {"name_full": "An unpublished compound", "names_public": []}]
            cards = analyses.load_cards(dr, public_compounds)
            html = analyses.render(dr, {"lead"}, cards)
        self.assertEqual(set(cards), {"lead", "low", "new", "older", "comparator", "unreviewed", "a_new_public_compound"})
        self.assertEqual([cards[k]["group"] for k in ("lead", "low", "new", "older", "unreviewed")],
                         ["priority", "lower", "active", "deferred", "unranked"])
        self.assertEqual(html.count('id="analysis-older"'), 1)
        self.assertEqual(cards["comparator"]["group"], "comparison")
        self.assertIn("older/followup.md", html)
        self.assertIn('href="reports/lead.pdf"', html)
        self.assertIn('href="#INV-05">Related investigation', html)
        self.assertIn("Where to look next", html)
        self.assertIn("Unknown transfer.", html)
        self.assertIn("Compare matched conditions.", html)
        self.assertIn("Check target engagement.", html)
        self.assertNotIn("An unpublished compound", html)
        self.assertEqual(cards["a_new_public_compound"]["group"], "pending")
        self.assertLess(html.index('id="ca-priority"'), html.index('id="ca-deferred"'))
        self.assertNotIn("private/README", html)
        self.assertIn("An independent review.", html)
        self.assertNotIn("Codex", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
