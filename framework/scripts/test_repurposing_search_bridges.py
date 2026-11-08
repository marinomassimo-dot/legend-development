#!/usr/bin/env python3
"""IT35 P6: precedent relations (bridges) widen the need search with pathway members; they never change the headline links and never carry a sign."""
from __future__ import annotations

import csv
import os
import sys
import tempfile
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
        rows = rs.load_bridges(rs.BRIDGE_WORD)
        self.assertTrue(rows)
        for r in rows:
            self.assertRegex(r["hgnc_a"], r"^HGNC:\d+$")
            self.assertRegex(r["hgnc_b"], r"^HGNC:\d+$")
            self.assertTrue(r["status"].startswith(("observed_other_context", "inferred", "hypothesised")), r["status"])
            self.assertIn("not shown in", r["note"])                          # every bridge says what is not shown

    def test_the_packages_deliver_their_own_bridges_and_nothing_is_kept_twice(self):
        files = rs.bridge_files()
        self.assertGreaterEqual(len(files), 2)
        rows = rs.load_bridges(rs.BRIDGE_WORD)
        self.assertEqual({(r["gene_a"], r["gene_b"]) for r in rows} >= {("GSK3B", "EIF2B5"), ("HDAC5", "SLC2A1")}, True)
        self.assertTrue(all(r["source_file"].endswith("output/bridges.tsv") for r in rows))
        self.assertFalse((rs.DR / "needs/bridges_it35.tsv").exists())        # the hand-kept copy is gone

    def test_a_malformed_bridge_is_refused_not_guessed(self):
        def write(rows):
            f = Path(tempfile.mkdtemp()) / "bridges.tsv"
            with open(f, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
                w.writeheader()
                w.writerows(rows)
            return f
        good = dict(BR[0])
        self.assertEqual(len(rs.load_bridges(write([good]))), 1)
        for bad in (dict(good, sign="up"), dict(good, direction="down"), dict(good, hgnc_a="4617"), dict(good, status="proven"), dict(good, evidence_ref="")):
            with self.assertRaises(ValueError):
                rs.load_bridges(write([bad]))

    @unittest.skipUnless(os.environ.get("LEGEND_CATALOG_CACHE"), "needs the local catalogue cache (not distributed)")
    def test_bridged_rows_leave_the_headline_unchanged_and_carry_no_sign(self):
        cc = rs.cc
        needs = rs.load_needs(rs.DEFAULT_NEEDS)["needs"]
        idx = rs.Index(cc.load(cc.DEFAULT_CATALOG), rs.load_artefacts(rs.DEFAULT_ARTEFACTS), rs.module_intervention_symbols(needs))
        roles = rs.load_roles(rs.DEFAULT_ROLES)
        need = next(n for n in needs if n["id"] == "NEED-ISR-ATTENUATION")
        plain = rs.associations_for_need(need, idx, roles)
        bridged = rs.associations_for_need(need, idx, roles, bridges=rs.load_bridges(rs.BRIDGE_WORD))
        head = lambda r: sorted({(a["catalogue_id"], a["target"]) for a in r["associations"] if not a["excluded_from_counts"] and a["target_kind"] in rs.LINK_KINDS})
        self.assertEqual(head(plain), head(bridged))
        extra = [a for a in bridged["associations"] if a["bridge"]]
        self.assertTrue(extra)                                                # the bridge widens the list
        self.assertFalse([a for a in plain["associations"] if a["bridge"]])   # and only when asked
        for a in extra:
            self.assertIn(a["consistency"], ("direction_unresolved", "not_evaluable"))
            self.assertTrue(any("HYPOTHESISED BRIDGE" in l for l in a["limits"]))


PROBE = {"probe": "ISRIB-like", "catalogue_id": "CHEMBL0", "identity_key": "KEY", "identity_source": "a record", "target_group": "eIF2B complex (five subunit genes)",
         "target_members": "EIF2B1;EIF2B2;EIF2B3;EIF2B4;EIF2B5", "action_term": "as the source words it", "kind": "experimental_tool", "evidence_ref": "x", "limits": "l", "not_shown": "n"}
ISR = {"id": "N2", "targets": [{"symbol": f"EIF2B{i}", "hgnc_id": f"HGNC:{i}", "target_kind": "intervention_target"} for i in (1, 2, 3, 4, 5)]
       + [{"symbol": "ATF4", "hgnc_id": "HGNC:9", "target_kind": "pathway_member"}]}


class Probes(unittest.TestCase):
    """IT36 P4: a probe the catalogue holds without a mechanism row is joined at read time, as one row for its target group."""

    def test_a_complex_probe_is_one_row_with_every_matched_subunit_and_no_member_chosen(self):
        rows = rs.probes_for_need(ISR, [PROBE])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["matched_in_need"], ["EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5"])
        self.assertFalse(rows[0]["counted_in_headline"])
        self.assertEqual(rows[0]["consistency"], "not_assessed")
        self.assertIn("not a treatment", rows[0]["label"])

    def test_a_probe_does_not_reach_a_need_through_a_pathway_member_or_an_unrelated_gene(self):
        only_member = dict(PROBE, target_members="ATF4")
        self.assertEqual(rs.probes_for_need(ISR, [only_member]), [])
        self.assertEqual(rs.probes_for_need(NEED, [PROBE]), [])
        self.assertEqual(rs.probes_for_need(ISR, None), [])

    def test_a_probe_row_with_a_sign_or_a_missing_identity_is_refused(self):
        for bad in (dict(PROBE, sign="up"), dict(PROBE, identity_key=""), dict(PROBE, kind="drug"), dict(PROBE, target_members="the complex")):
            with self.assertRaises(ValueError):
                rs.check_probe_row(bad, "t")


    def test_the_isrib_row_reaches_the_isr_need_once_and_not_through_epsilon_alone(self):
        needs = {n["id"]: n for n in rs.load_needs(rs.DEFAULT_NEEDS)["needs"]}
        probes = rs.load_probes(rs.BRIDGE_WORD)
        self.assertIn("ISRIB", [p["probe"] for p in probes])
        rows = [r for r in rs.probes_for_need(needs["NEED-ISR-ATTENUATION"], probes) if r["probe"] == "ISRIB"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["matched_in_need"], ["EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5"])
        self.assertEqual(rows[0]["catalogue_id"], "NOT_IN_CATALOGUE")
        for other in ("NEED-GSK3B-DEREPRESSION", "NEED-PDH-PYRUVATE-AXIS"):
            self.assertFalse([r for r in rs.probes_for_need(needs[other], probes) if r["probe"] == "ISRIB"], other)


if __name__ == "__main__":
    unittest.main(verbosity=2)
