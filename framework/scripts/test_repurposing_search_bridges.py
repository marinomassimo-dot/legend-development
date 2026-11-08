#!/usr/bin/env python3
"""IT35 P6: precedent relations (bridges) widen the need search with pathway members; they never change the headline links and never carry a sign."""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_search as rs  # noqa: E402

NEED = {"id": "N", "targets": [{"symbol": "AAA", "hgnc_id": "HGNC:1", "target_kind": "intervention_target"}]}
BR = [{"gene_a": "BBB", "hgnc_a": "HGNC:2", "relation": "phosphorylates", "gene_b": "AAA", "hgnc_b": "HGNC:1", "status": "observed_other_context",
       "context": "other tissue", "evidence_ref": "x", "note": "n"}]


class Bridges(unittest.TestCase):
    def test_the_other_gene_is_added_as_a_pathway_member_carrying_the_bridge(self):
        t = rs.targets_with_bridges(NEED, BR)
        self.assertEqual([x["symbol"] for x in t], ["AAA", "BBB"])
        self.assertEqual(t[1]["target_kind"], "pathway_member")
        self.assertNotIn(t[1]["target_kind"], rs.LINK_KINDS)                 # never a headline link
        self.assertEqual(t[1]["bridge"]["via"], "AAA")
        self.assertEqual(NEED["targets"], [NEED["targets"][0]])              # the need itself is not modified

    def test_a_bridge_touching_no_target_adds_nothing_and_a_known_gene_is_not_duplicated(self):
        self.assertEqual(len(rs.targets_with_bridges(NEED, [dict(BR[0], gene_a="CCC", gene_b="DDD")])), 1)
        both = {"id": "N", "targets": NEED["targets"] + [{"symbol": "BBB", "hgnc_id": "HGNC:2", "target_kind": "intervention_target"}]}
        self.assertEqual(len(rs.targets_with_bridges(both, BR)), 2)
        self.assertEqual(rs.targets_with_bridges(NEED, None), NEED["targets"])

    def test_the_shipped_bridge_table_is_well_formed_and_makes_no_wwox_claim(self):
        rows = rs.load_bridges(rs.DEFAULT_BRIDGES)
        self.assertTrue(rows)
        for r in rows:
            self.assertRegex(r["hgnc_a"], r"^HGNC:\d+$")
            self.assertRegex(r["hgnc_b"], r"^HGNC:\d+$")
            self.assertTrue(r["status"].startswith(("observed_other_context", "inferred", "hypothesised")), r["status"])
            self.assertIn("not shown in", r["note"])                          # every bridge says what is not shown

    @unittest.skipUnless(os.environ.get("LEGEND_CATALOG_CACHE"), "needs the local catalogue cache (not distributed)")
    def test_bridged_rows_leave_the_headline_unchanged_and_carry_no_sign(self):
        cc = rs.cc
        needs = rs.load_needs(rs.DEFAULT_NEEDS)["needs"]
        idx = rs.Index(cc.load(cc.DEFAULT_CATALOG), rs.load_artefacts(rs.DEFAULT_ARTEFACTS), rs.module_intervention_symbols(needs))
        roles = rs.load_roles(rs.DEFAULT_ROLES)
        need = next(n for n in needs if n["id"] == "NEED-ISR-ATTENUATION")
        plain = rs.associations_for_need(need, idx, roles)
        bridged = rs.associations_for_need(need, idx, roles, bridges=rs.load_bridges(rs.DEFAULT_BRIDGES))
        head = lambda r: sorted({(a["catalogue_id"], a["target"]) for a in r["associations"] if not a["excluded_from_counts"] and a["target_kind"] in rs.LINK_KINDS})
        self.assertEqual(head(plain), head(bridged))
        extra = [a for a in bridged["associations"] if a["bridge"]]
        self.assertTrue(extra)                                                # the bridge widens the list
        self.assertFalse([a for a in plain["associations"] if a["bridge"]])   # and only when asked
        for a in extra:
            self.assertIn(a["consistency"], ("direction_unresolved", "not_evaluable"))
            self.assertTrue(any("HYPOTHESISED BRIDGE" in l for l in a["limits"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
