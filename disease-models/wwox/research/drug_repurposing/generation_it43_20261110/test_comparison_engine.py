#!/usr/bin/env python3
"""IT43 P1 regressions: the comparison rows reach the role; three contrast cases on synthetic packages; the view obeys the engine."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import comparison_engine as ce  # noqa: E402
import hypothesis_package as hp  # noqa: E402

def pkg(dec, cmp_=None, meas=None):
    return {"dec": {d["prop_id"]: d for d in dec}, "cmp": cmp_ or {}, "meas": meas or {}}
def prop(i, stmt, depth="partial_fulltext_read", cls="compound/class", system="Xenopus oocytes, -40 mV, 50 uM glycine"):
    return {"prop_id": i, "statement": stmt, "depth": depth, "class": cls, "species_system_age_prep_exposure_readout": system}
def item(i, name, kind="probe"): return {"item_id": i, "name_full": name, "kind": kind}

class Contrast(unittest.TestCase):
    def test_measure_does_not_transfer_to_another_molecule(self):
        p = pkg([prop("D01", "DATO: alpha inhibits recombinant GluN1/GluN2B with IC50 72 nM"), prop("D02", "DATO: alpha and beta inhibit GluN1/GluN2B, IC50 72 nM and 9 nM")])
        r = {x["name"]: x for x in ce.derive([item("V1", "alpha; beta")], p)}
        self.assertEqual(r["alpha"]["evidence_tier"], "PRIMARY")
        self.assertEqual(r["beta"]["evidence_tier"], "TRANSFER")      # named only in a statement shared with another compound
        self.assertEqual(r["beta"]["role_derived"], "unresolved")
    def test_incompatible_conditions_give_no_merged_comparison(self):
        p = pkg([prop("D01", "DATO: alpha IC50 72 nM"), prop("D02", "DATO: alpha IC50 0.34 uM", system="Xenopus oocytes, -70 mV, 50 uM glycine")])
        self.assertTrue(ce.derive([item("V1", "alpha")], p)[0]["comparison_state"].startswith("NOT_COMPARABLE"))
        q = pkg([prop("D01", "DATO: alpha IC50 72 nM"), prop("D02", "DATO: alpha IC50 80 nM")])
        self.assertEqual(ce.derive([item("V1", "alpha")], q)[0]["comparison_state"], "COMPARABLE")
    def test_assay_scaffold_and_atp_make_values_not_comparable(self):
        p = pkg([prop("D01", "DATO: alpha IC50 87 nM with the E2p/E3BP core", system="human PDK1, with the E2p/E3BP core, 5 uM ATP"), prop("D02", "DATO: alpha IC50 stimulation core-free, 10 fold", system="human PDK3, core-free, 5 uM ATP")])
        self.assertTrue(ce.derive([item("V1", "alpha")], p)[0]["comparison_state"].startswith("NOT_COMPARABLE"))
        q = pkg([prop("D01", "DATO: alpha IC50 87 nM", system="purified human PDK1 kinase assay, with the E2p/E3BP core, 5 uM ATP"), prop("D02", "DATO: alpha IC50 90 nM", system="purified human PDK1 kinase assay, with the E2p/E3BP core, 5 uM ATP")])
        self.assertEqual(ce.derive([item("V1", "alpha")], q)[0]["comparison_state"], "COMPARABLE")
        r = pkg([prop("D01", "DATO: alpha IC50 87 nM", system="purified human PDK1 kinase assay, 1 mM ATP"), prop("D02", "DATO: alpha IC50 90 nM", system="purified human PDK1 kinase assay, 1000 uM ATP")])
        self.assertEqual(ce.derive([item("V1", "alpha")], r)[0]["comparison_state"], "COMPARABLE")   # IT45 P1: units are converted before they are compared (HE45)
        u = pkg([prop("D01", "DATO: alpha IC50 87 nM", system="purified human PDK1 kinase assay, 1 mM ATP"), prop("D02", "DATO: alpha IC50 90 nM", system="purified human PDK1 kinase assay, 1 uM ATP")])
        self.assertTrue(ce.derive([item("V1", "alpha")], u)[0]["comparison_state"].startswith("NOT_COMPARABLE"))
        w = pkg([prop("D01", "DATO: alpha IC50 87 nM", system="purified human PDK1 kinase assay, 1 mM ATP"), prop("D02", "DATO: alpha IC50 90 nM", system="purified human PDK1 kinase assay")])
        self.assertTrue(ce.derive([item("V1", "alpha")], w)[0]["comparison_state"].startswith("CONDITIONS_INSUFFICIENT"))   # a missing condition is neither agreement nor refutation
    def test_unknown_premise_stays_conditional_never_refuted(self):
        r = ce.derive([item("V1", "gamma")], pkg([prop("D01", "DATO: alpha IC50 72 nM")]))[0]
        self.assertEqual((r["evidence_tier"], r["role_derived"]), ("NONE", "unresolved"))
        self.assertNotIn("weak", r["role_derived"])                    # not stated is not tested and absent
    def test_limit_proposition_caps_the_limited_datum(self):
        p = pkg([prop("D15", "DATO: nbqx Ki 0.077 uM at GluA2"), prop("D16", "INFERENZA (limit of D15): nbqx used only as a comparator", cls="absence")])
        self.assertEqual(ce.derive([item("V1", "nbqx")], p)[0]["evidence_tier"], "NONE")

class Conditions(unittest.TestCase):
    """HE45: the reported behaviours of the ATP / unit / missing / generic-system cases, through the engine."""
    def state(self, sys_a, sys_b, role="PRIMARY"):
        p = pkg([prop("D01", "DATO: alpha IC50 72 nM", system=sys_a), prop("D02", "DATO: alpha IC50 80 nM", system=sys_b)])
        r = ce.derive([item("V1", "alpha")], p)[0]
        return r["comparison_state"], r["role_derived"]
    def test_one_mM_against_one_uM_atp_is_not_comparable(self):
        self.assertTrue(self.state("recombinant kinase assay, 1 mM ATP", "recombinant kinase assay, 1 uM ATP")[0].startswith("NOT_COMPARABLE"))
    def test_one_mM_equals_1000_uM_atp(self):
        self.assertEqual(self.state("purified kinase assay, 1 mM ATP", "purified kinase assay, 1000 uM ATP")[0], "COMPARABLE")
    def test_atp_declared_against_missing_is_insufficient_and_does_not_block_the_role(self):
        st, role = self.state("purified kinase assay, 5 uM ATP", "purified kinase assay")
        self.assertTrue(st.startswith("CONDITIONS_INSUFFICIENT") and "ATP" in st)
        self.assertEqual(role, "probe")   # a proposal stays possible; the premise is named in the state
    def test_two_unrecognised_preparations_are_not_equivalent(self):
        self.assertTrue(self.state("a hepatic preparation, 5 uM ATP", "a mitochondrial preparation, 5 uM ATP")[0].startswith("CONDITIONS_INSUFFICIENT"))
    def test_two_propositions_without_a_potency_pair_are_not_called_comparable(self):
        p = pkg([prop("D01", "DATO: alpha binds GluN2B"), prop("D02", "DATO: alpha reduces seizures")])
        self.assertEqual(ce.derive([item("V1", "alpha")], p)[0]["comparison_state"], "NO_POTENCY_PAIR")
    def test_merge_keeps_the_weakest_answer(self):
        a = {"item_id": "V1", "name": "alpha", "evidence_tier": "PRIMARY", "role_derived": "probe", "role_reason": "", "public_source_work": "", "tier_props": "", "premise_needed": "", "discriminating_measure": "", "relaunch_question": "", "comparison_state": "COMPARABLE"}
        b = dict(a, comparison_state="CONDITIONS_INSUFFICIENT: x"); c = dict(a, comparison_state="NOT_COMPARABLE: y")
        self.assertTrue(ce.merge([a, b])[0]["comparison_state"].startswith("CONDITIONS_INSUFFICIENT"))
        self.assertTrue(ce.merge([b, c, a])[0]["comparison_state"].startswith("NOT_COMPARABLE"))

class RealPackages(unittest.TestCase):
    def rows(self):
        items = [r for r in csv.DictReader(open(HERE.parent / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == "INV-05"]
        pk = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == "INV-05"]
        return items, ce.merge([x for p in pk for x in ce.derive(items, p, p["dir"].parent.name.split("_")[0])])
    def test_view_never_exceeds_the_engine(self):
        items, res = self.rows(); kind = {i["item_id"]: i["kind"] for i in items}; src = {i["item_id"]: i["source_rows"] for i in items}
        for r in res:
            if r["evidence_tier"] == "NONE" and kind[r["item_id"]] in ("probe", "known_requalified"):
                # outside the registered packages the engine cannot adjudicate: the view must cite where its evidence lives (SCI42 package, not a registered comparison)
                self.assertRegex(src[r["item_id"]], r"(?i)search_rows|PMID|sci42", f'{r["item_id"]} {r["name"]} has no cited source outside the perimeter'); continue
            if kind[r["item_id"]] in ("probe", "known_requalified"):
                self.assertEqual(r["role_derived"] in ("probe", "known_requalified"), True, f'{r["item_id"]} {r["name"]}: view says {kind[r["item_id"]]}, engine tier {r["evidence_tier"]}')
    def test_ro_25_6981_follows_its_evidence(self):
        """IT43: only abstract-level values and a transferred behaviour, so unresolved. IT44b: SCI44 package B (primary potency and site) is registered for INV-05 and the engine re-derives the role by itself."""
        _, res = self.rows(); d = {r["name"]: r for r in res}
        self.assertEqual(d["ifenprodil"]["role_derived"], "probe")
        registered = {p["dir"].parent.name for p in hp.load_all()}
        if "ro25_6981_sci44_20261110" in registered:
            self.assertEqual((d["Ro 25-6981"]["evidence_tier"], d["Ro 25-6981"]["role_derived"]), ("PRIMARY", "probe"))
            self.assertIn("M-R1", d["Ro 25-6981"]["premise_needed"]); self.assertTrue(d["Ro 25-6981"]["comparison_state"].startswith("NOT_COMPARABLE"))   # potencies at different holding potentials are not merged
        else:
            self.assertEqual(d["Ro 25-6981"]["role_derived"], "unresolved")
        self.assertEqual(d["d-APV"]["role_derived"], "control")
    def test_decisions_file_is_current(self):
        _, res = self.rows(); got = list(csv.DictReader(open(HERE / "compound_decisions_it43.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual([(r["item_id"], r["name"], r["role_derived"]) for r in res], [(r["item_id"], r["name"], r["role_derived"]) for r in got])

class SecondInvestigation(unittest.TestCase):
    def test_inv07_items_are_derived_and_their_file_is_current(self):
        items = [r for r in csv.DictReader(open(HERE.parent / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == "INV-07"]
        pk = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == "INV-07"]
        res = ce.merge([x for p in pk for x in ce.derive(items, p, p["dir"].parent.name.split("_")[0])])
        got = list(csv.DictReader(open(HERE / "compound_decisions_inv07_it44.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual([(r["item_id"], r["name"], r["role_derived"]) for r in res], [(r["item_id"], r["name"], r["role_derived"]) for r in got])
        self.assertTrue({r["name"] for r in res} >= {"dichloroacetate", "AZD7545", "VER-246608"})

class CardRoles(unittest.TestCase):
    def test_the_view_loader_carries_the_engine_roles_so_a_card_never_merges_roles_silently(self):
        sys.path.insert(0, str(HERE.parents[4] / "framework/scripts")); import repurposing_view as rv
        cv = {c["item_id"]: c for c in rv.compound_view(HERE.parent, True)}
        roles = {x["name"]: x["role"] for x in cv["V13"]["roles"]}
        self.assertEqual(roles["dichloroacetate"], "control"); self.assertEqual(roles["AZD7545"], "known_requalified")
        self.assertTrue({x["role"] for x in cv["V16"]["roles"]} >= {"known_requalified", "unresolved"} or len({x["role"] for x in cv["V16"]["roles"]}) >= 2)

    def test_a_statement_about_an_independent_route_does_not_raise_the_tier(self):
        """IT46 P5 (SCI46 delta row 3): monomethyl fumarate was derived PRIMARY probe from a statement about a route independent of NRF2"""
        import comparison_engine as ce
        self.assertTrue(ce.INDEPENDENT_ROUTE.search("An NRF2-independent route exists for monomethyl fumarate in a microglial line"))
        self.assertFalse(ce.INDEPENDENT_ROUTE.search("The binder raised NQO1 in a line with intact NRF2"))
        import csv
        rows = {(r["item_id"], r["name"]): r for r in csv.DictReader(open(ce.HERE / "compound_decisions_inv08_it44.tsv", encoding="utf-8"), delimiter="\t")}
        self.assertEqual(("PRIMARY", "probe"), (rows[("V19", "KI-696")]["evidence_tier"], rows[("V19", "KI-696")]["role_derived"]))
        self.assertEqual("unresolved", rows[("V19", "monomethyl fumarate")]["role_derived"])
        self.assertEqual("unresolved", rows[("V19", "dimethyl fumarate")]["role_derived"])


if __name__ == "__main__": unittest.main(verbosity=2)
