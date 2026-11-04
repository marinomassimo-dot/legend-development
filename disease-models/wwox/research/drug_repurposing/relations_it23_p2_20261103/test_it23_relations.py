#!/usr/bin/env python3
"""IT23 regressions on what the new relations and the simulation probe may and may not do.

  python3 test_it23_relations.py          (unittest; offline; seconds)

Pinned: an adverse-event signal keeps its source, licence and event terms and is joined by compound id; it is carried as a limit and moves no eligibility; an unknown or conflicting
action never becomes an edge in the simulation input; an assumed rule is never mixed with a qualified one; the known conversion defect of the external aggregator stays documented
with its lines (so nobody imports it); a sign discordance is a prompt, listed with LEGEND's own row.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, json, re, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
SEIZURE = re.compile(r"seiz|convuls|epilep|status epilepticus", re.I)


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


class HarmSignals(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = rd(HERE / "harm_signals_it23.tsv")

    def test_every_row_is_a_faers_seizure_report_joined_by_id_with_its_licence(self):
        self.assertTrue(self.rows)
        for r in self.rows:
            self.assertEqual(r["source"], "infores:faers")
            self.assertTrue(r["licence"].strip())
            self.assertTrue(r["family_id"].startswith("FAM:"))
            self.assertTrue(r["compound_id"])
            self.assertTrue(all(SEIZURE.search(e) for e in r["events"].split("; ")))
            self.assertIn("not a safety verdict", r["reading"])          # an association, and absence is no evidence of safety

    def test_only_permissive_licence_rows_are_in_the_committed_extract(self):
        ext = rd(HERE / "extract_ecKG_wwox.tsv")
        bad = [r for r in ext if not re.search(r"CC0|CC BY|MIT|Apache|BSD|public", r["source_licence_stated"] or "CC BY", re.I) and r["source_licence_stated"]]
        self.assertEqual(bad, [])

    def test_sign_discordances_are_prompts_with_legends_own_row(self):
        d = rd(HERE / "sign_discordance_it23.tsv")
        self.assertEqual(len(d), 15)
        for r in d:
            self.assertTrue(r["legend_group"] and r["legend_scope"])
            self.assertIn("prompt to read the source", r["reading"])
            self.assertNotEqual(r["legend_sign"][:1] == "-", r["eckg_sign"][:1] == "-")      # they really disagree in sign


class GeneratorUsesTheLimitWithoutMovingSelection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = DR / "generation_it23_p2_20261103" / "results_s5" / "proposals_it21.tsv"
        old = DR / "generation_it22_p1_20261103" / "results_p4" / "proposals_it21.tsv"
        if not base.exists() or not old.exists():
            raise unittest.SkipTest("stage tables absent")
        cls.new = {r["proposal_id"]: r for r in rd(base)}
        cls.old = {r["proposal_id"]: r for r in rd(old)}
        cls.fam = {r["family_id"] for r in rd(HERE / "harm_signals_it23.tsv")}

    def test_the_flag_is_exactly_the_families_with_a_signal(self):
        for r in self.new.values():
            self.assertEqual(r["harm_signal_faers_seizure"] == "yes", r["family_id"] in self.fam, r["proposal_id"])
            self.assertEqual("FAERS_SEIZURE_REPORTS" in r["carried_limits"], r["family_id"] in self.fam, r["proposal_id"])

    def test_eligibility_and_blockers_are_unchanged(self):
        self.assertEqual(set(self.new), set(self.old))
        for i, r in self.new.items():
            self.assertEqual((r["handoff_eligible"], r["handoff_blocker"]), (self.old[i]["handoff_eligible"], self.old[i]["handoff_blocker"]), i)


class HandOverIsDeterministic(unittest.TestCase):
    def test_direct_hits_are_ordered_by_phase_then_name_not_by_set_order(self):
        h = DR / "generation_it23_p2_20261103" / "results_s5" / "handoff_it21.tsv"
        if not h.exists():
            self.skipTest("stage tables absent")
        seen = 0
        for r in rd(h):
            items = [x for x in r["direct_acting_hits_same_set"].split(" - diagnostic only")[0].split("; ") if x]
            keys = [(-float(re.search(r"phase (-?[\d.]+)", x).group(1)), x.split(" (phase")[0]) for x in items]
            self.assertEqual(keys, sorted(keys), r["proposal_id"])          # a tie among phase-4 compounds used to follow set order, which depends on PYTHONHASHSEED
            seen += bool(items)
        self.assertGreater(seen, 0)


class SimulationInputsKeepUnknownUnknown(unittest.TestCase):
    S = DR / "simulation_it23_p3_20261103"

    def test_no_unknown_or_conflicting_action_becomes_an_edge(self):
        if not (self.S / "inputs_q5").exists():
            self.skipTest("simulation inputs absent")
        acts = rd(self.S / "inputs_q5" / "actions_explicit.tsv")
        self.assertTrue(acts)
        for r in acts:
            self.assertIn(r["action_used_in_sim"], ("inhibit", "activate", "mixed_by_family"))
            self.assertGreaterEqual(int(r["n_explicit_minus1"]) + int(r["n_explicit_plus1"]), 1)         # at least one EXPLICIT signed row stands behind each action
        q = rd(self.S / "inputs_q5" / "edges_qualified.tsv")
        a = rd(self.S / "inputs_q5" / "edges_assumed.tsv")
        self.assertTrue(all(r["status"] == "ASSUMED_NOT_QUALIFIED" for r in a))
        self.assertFalse({(r["source"], r["target"]) for r in q} & {(r["source"], r["target"]) for r in a})   # an assumed rule is never filed as qualified

    def test_the_external_conversion_defect_stays_documented_with_its_lines(self):
        d = json.loads((self.S / "results" / "defect_repro.json").read_text(encoding="utf-8"))
        lines = d["responsible_lines"]
        self.assertEqual(set(lines), {"unsigned_to_inhibition", "minus_beats_plus", "ttd_unlisted_moa_to_plus"})
        unknown = [r for r in d["nordic_output"] if "unknown" in r["correct"]]
        self.assertTrue(unknown and all(r["nordic_value"] != 0 for r in unknown))         # the defect: an unknown became a signed action


if __name__ == "__main__":
    unittest.main(verbosity=2)
