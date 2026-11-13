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

    def test_a_proposition_that_does_not_measure_the_mechanism_does_not_raise_the_tier(self):
        """IT46 P5 / HE47 H1: monomethyl fumarate was derived PRIMARY probe from a statement about a route other than NRF2. The package author's `relation` cell says so; the wording is not consulted."""
        import comparison_engine as ce
        self.assertFalse(hasattr(ce, "INDEPENDENT_ROUTE"))
        rows = {(r["item_id"], r["name"]): r for r in csv.DictReader(open(ce.HERE / "compound_decisions_inv08_it44.tsv", encoding="utf-8"), delimiter="\t")}
        self.assertEqual(("PRIMARY", "probe"), (rows[("V19", "KI-696")]["evidence_tier"], rows[("V19", "KI-696")]["role_derived"]))
        mmf = rows[("V19", "monomethyl fumarate")]
        self.assertEqual(("unresolved", "NONE"), (mmf["role_derived"], mmf["evidence_tier"]))
        self.assertIn("D14 other_route", mmf["role_reason"])                       # named, not 'no proposition in the package names it'
        self.assertIn("keap1:D14=other_route", mmf["uncounted_props"])
        self.assertIn("keap1:D14=opposes", mmf["counter_props"])                    # the counter-evidence stays for the consumers that need it
        self.assertEqual("unresolved", rows[("V19", "dimethyl fumarate")]["role_derived"])

    def test_direction_never_changes_the_tier_and_a_negative_probe_is_still_a_probe(self):
        nega = prop("D01", "Compound Zed at 10 uM did not change the current (n = 6)")
        nega.update(relation="mechanism", direction="null")
        r = ce.derive([item("V1", "Zed")], pkg([nega]))[0]
        self.assertEqual((r["evidence_tier"], r["role_derived"], r["counter_props"]), ("PRIMARY", "probe", ":D01=null"))

    def test_a_mention_marked_context_or_other_route_is_listed_not_counted(self):
        a = prop("D01", "Zed is the compound used in the study"); a.update(relation="context")
        b = prop("D02", "Zed acts through a second receptor"); b.update(relation="other_route", direction="not_applicable")
        r = ce.derive([item("V1", "Zed")], pkg([a, b]))[0]
        self.assertEqual((r["evidence_tier"], r["tier_props"], r["uncounted_props"]), ("NONE", "", ":D01=context,:D02=other_route"))
        self.assertIn("D01 context", r["role_reason"])

    def test_an_unclassified_proposition_counts_as_before_and_is_named(self):
        r = ce.derive([item("V1", "Zed")], pkg([prop("D01", "Zed inhibits the current with IC50 5 uM")]))[0]
        self.assertEqual((r["evidence_tier"], r["unclassified_props"]), ("PRIMARY", ":D01"))

    def test_a_state_names_the_failing_pairs_and_how_many_pairs_there_were(self):
        mk = lambda i, sysm: prop(i, "Zed inhibits the current with IC50 5 uM", system=sysm)
        r = ce.derive([item("V1", "Zed")], pkg([mk("D01", "Xenopus oocytes, -40 mV, 50 uM glycine"), mk("D02", "Xenopus oocytes, -40 mV, 50 uM glycine"), mk("D03", "HEK293 cells, -70 mV, 10 uM glycine")]))[0]
        self.assertTrue(r["comparison_state"].startswith("NOT_COMPARABLE:"))
        self.assertTrue(r["comparison_state"].endswith("[pairs: 2 incompatible, 0 insufficient, 1 agreeing, of 3]"), r["comparison_state"])


class StatedRoles(unittest.TestCase):
    """HE50: a package's own role table can lower a derived role, never raise it; context travels with the role; a row about several compounds is assigned to none."""
    def table(self, rows, tmp=None):
        import tempfile
        from unittest import mock
        d = Path(tempfile.mkdtemp(prefix="ce_roles_"))
        self.addCleanup(lambda: __import__("shutil").rmtree(d, ignore_errors=True))
        (d / "zedpkg" / "engine").mkdir(parents=True); (d / "zedpkg" / "output").mkdir()
        (d / "zedpkg" / "output" / "roles.tsv").write_text("row_id\treagent\trole\tsystem\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
        m = mock.patch.dict(ce.ROLE_TABLES, {"zedpkg": ("output/roles.tsv", "reagent", "role", ("system",))})
        m.start(); self.addCleanup(m.stop)
        return {"dec": {}, "cmp": {}, "meas": {}, "dir": d / "zedpkg" / "engine"}

    def run_zed(self, rows, props=None):
        pk = self.table(rows); pk["dec"] = {x["prop_id"]: x for x in (props or [prop("D01", "Zed inhibits the current with IC50 5 uM", system="mouse BMDM")])}
        return ce.merge(ce.derive([item("V1", "Zed")], pk))[0]

    def test_a_comparator_the_tier_would_call_a_probe_is_shown_as_a_comparator(self):
        r = self.run_zed([["M1", "Zed", "comparator (rule 2: class myeloid, loss unverified)", "mouse BMDM; molecular"]])
        self.assertEqual((r["evidence_tier"], r["role_derived"]), ("PRIMARY", "comparator"))
        self.assertIn("capped from probe to comparator", r["role_reason"])
        self.assertIn("M1 comparator", r["package_roles"]); self.assertIn("mouse BMDM", r["package_roles"])   # the system it was stated for travels with it

    def test_the_package_never_raises_a_role_above_what_the_evidence_tier_carries(self):
        r = self.run_zed([["M1", "Zed", "probe (rule 1)", "primary rat microglia"]], props=[prop("D01", "Zed inhibits the current with IC50 5 uM", depth="abstract_only")])
        self.assertEqual((r["evidence_tier"], r["role_derived"]), ("ABSTRACT", "unresolved"))
        self.assertIn("M1 probe", r["package_roles"])                                 # the disagreement is visible, not resolved upward

    def test_a_probe_in_one_system_keeps_the_other_systems_beside_it(self):
        r = self.run_zed([["M1", "Zed", "probe (rule 1: loss verified, glial class)", "primary rat microglia; molecular"],
                          ["M2", "Zed", "comparator (rule 2: partial loss)", "LUHMES line; viability"],
                          ["M3", "Zed", "not interpretable (rule 4)", "NHBE; molecular"]])
        self.assertEqual(r["role_derived"], "probe")
        for part in ("M1 probe", "primary rat microglia", "M2 comparator", "LUHMES line", "M3 unresolved", "NHBE"):
            self.assertIn(part, r["package_roles"])

    def test_a_row_naming_several_compounds_is_assigned_to_none(self):
        r = self.run_zed([["M1", "Zed and Beta", "comparator (Zed unqualified here)", "cortical cultures"]])
        self.assertEqual(r["role_derived"], "probe")                                  # the tier stands: the shared row does not cap it
        self.assertIn("shared row, not assigned", r["package_roles"])

    def test_a_similar_name_does_not_lend_its_role(self):
        r = self.run_zed([["M1", "Zed-2 (an enantiomer)", "unqualified", "LUHMES"]])
        self.assertEqual((r["role_derived"], r["package_roles"]), ("probe", ""))

    def test_an_unrecognised_leading_word_is_an_unresolved_role_not_a_guess(self):
        r = self.run_zed([["M1", "Zed", "tentatively useful as a probe (not shown)", "x"]])
        self.assertEqual(r["role_derived"], "unresolved")
        self.assertEqual(ce.role_word("probe (conditional: with a loss arm)"), "probe")  # only the leading word is read; the rest of the cell is carried, not interpreted
        self.assertEqual(ce.role_word("conditional pharmacological hypothesis"), "unresolved")

    def test_a_package_without_a_role_table_reads_as_before(self):
        pk = pkg([prop("D01", "Zed inhibits the current with IC50 5 uM")])
        r = ce.merge(ce.derive([item("V1", "Zed")], pk))[0]
        self.assertEqual((r["role_derived"], r["package_roles"]), ("probe", ""))

    def test_the_real_nrf2_case_keeps_comparators_comparators_and_the_probe_in_its_context(self):
        with open(HERE / "compound_decisions_inv08_it44.tsv", encoding="utf-8", newline="") as fh:
            rows = {r["name"]: r for r in csv.DictReader(fh, delimiter="\t")}
        self.assertEqual((rows["RA839"]["role_derived"], rows["sulforaphane"]["role_derived"]), ("comparator", "comparator"))
        ki = rows["KI-696"]
        self.assertEqual(ki["role_derived"], "probe")
        self.assertIn("probe (conditional: with a verified NRF2-loss arm", ki["package_roles"])      # the package's condition is not dropped
        self.assertIn("primary rat microglia", ki["package_roles"]); self.assertIn("comparator", ki["package_roles"])
        self.assertIn("shared row, not assigned", rows["dimethyl fumarate"]["package_roles"])
        self.assertEqual(rows["bardoxolone methyl"]["role_derived"], "unresolved")                    # lower than the package's comparator: a ceiling is not lifted


if __name__ == "__main__": unittest.main(verbosity=2)
