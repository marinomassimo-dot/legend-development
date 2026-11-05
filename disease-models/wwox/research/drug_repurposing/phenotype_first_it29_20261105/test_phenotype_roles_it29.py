#!/usr/bin/env python3
"""Regression: the behaviours of phenotype_roles_it29.build that protect against a named mistake."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import phenotype_roles_it29 as m


def row(**k):
    base = dict(target_symbol="CHRM1", action_on_target="inhibit", direction_on_endpoint="favourable", attribution="target_controlled",
                intervention_type="compound", measure_level="function", composition_or_autonomous="cell_autonomous", source_id="S1")
    base.update(k)
    return base


class T(unittest.TestCase):
    def test_lowering_activity_with_benefit_is_opposite(self):
        self.assertEqual(m.build([row()], "N")[0]["coupling"], "opposite")

    def test_raising_activity_with_benefit_is_same(self):
        self.assertEqual(m.build([row(action_on_target="activate")], "N")[0]["coupling"], "same")

    def test_loss_that_hurts_means_same(self):
        r = row(intervention_type="genetic_loss", action_on_target="loss", direction_on_endpoint="adverse", attribution="not_applicable")
        self.assertEqual(m.build([r], "N")[0]["coupling"], "same")

    def test_compound_only_is_not_attributed_to_its_target(self):
        self.assertEqual(m.build([row(attribution="compound_only")], "N"), [])

    def test_viability_and_unknown_never_sign(self):
        self.assertEqual(m.build([row(measure_level="viability")], "N"), [])
        self.assertEqual(m.build([row(direction_on_endpoint="undetermined")], "N"), [])
        self.assertEqual(m.build([row(direction_on_endpoint="null")], "N"), [])

    def test_disagreement_is_unresolved_not_averaged(self):
        out = m.build([row(), row(source_id="S2", action_on_target="activate")], "N")
        self.assertEqual(out[0]["coupling"], "unresolved")

    def test_context_dependent_keeps_the_discordance_visible(self):
        out = m.build([row(), row(source_id="S2", direction_on_endpoint="context_dependent")], "N")
        self.assertEqual(out[0]["coupling"], "unresolved")

    def test_every_row_is_marked_external(self):
        self.assertIn("EXTERNAL_TRANSFER", m.build([row()], "N")[0]["qualifier"])


class N(unittest.TestCase):
    def test_signed_target_the_need_does_not_list_is_added_once_and_unknown_hgnc_is_skipped(self):
        import json, tempfile
        d = Path(tempfile.mkdtemp())
        (d / "n.json").write_text(json.dumps({"needs": [{"id": "N", "targets": [{"symbol": "AAA"}]}]}))
        added = m.extend_needs(d / "n.json", "N", ["AAA", "BBB", "CCC"], {"BBB": ("HGNC:1", "b")}, d / "o.json")
        out = json.loads((d / "o.json").read_text())["needs"][0]["targets"]
        self.assertEqual(added, 1)
        self.assertEqual([t["symbol"] for t in out], ["AAA", "BBB"])


if __name__ == "__main__":
    unittest.main()
