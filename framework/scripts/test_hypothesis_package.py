#!/usr/bin/env python3
"""Regressions for framework/scripts/hypothesis_package.py (the reader that carries physiological hypotheses to a consumer).

Pinned: rows are carried verbatim and none is lost; rivals, experiments and matrix columns are reached by literal
ids only; a link that needs interpretation is a committed row validated against real ids; a physiological
hypothesis is never a gene arc; a missing link or experiment is UNLINKED / NO_EXPERIMENT, not evidence against;
a CARRIED_IN_TEXT claim fails when the text it names is gone; the reader writes nothing.
"""
from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hypothesis_package as hp  # noqa: E402


def _digest(root: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(root.rglob("*")):
        if f.is_file():
            h.update(f.read_bytes())
    return h.hexdigest()


class Committed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pkgs = hp.load_all()
        cls.phys = [p for p in cls.pkgs if p["role"] == "physiological_hypotheses"]

    def rec(self, inv):
        return hp.record_for(self.pkgs, inv)

    def test_committed_links_validate(self):
        self.assertEqual(hp.validate_manifest(), [])
        self.assertEqual([e for p in self.pkgs for e in hp.validate(p)], [])

    def test_every_hypothesis_is_linked_and_verbatim(self):
        for p in self.phys:
            linked = {l["hyp_id"] for l in p["links"]}
            self.assertEqual(linked, set(p["hyps"]), "a hypothesis with no link row would be silently dropped")
        got = {h["hyp_id"]: h for i in ("INV-05", "INV-18") for h in self.rec(i)["hypotheses"]}
        for p in self.phys:
            for hid, row in p["hyps"].items():
                self.assertEqual(got[hid]["hypothesis"], row)

    def test_experiments_are_not_lost(self):
        # independent count: an experiment belongs to a hypothesis when its cell names the id as a whole word
        import re
        for p in self.phys:
            for hid in p["hyps"]:
                want = sorted(e for e, r in p["exps"].items() if re.search(rf"\b{hid}\b", r["hypothesis"]))
                inv = next(l["inv_id"] for l in p["links"] if l["hyp_id"] == hid)
                h = next(x for x in self.rec(inv)["hypotheses"] if x["hyp_id"] == hid)
                self.assertEqual(sorted(e["row"]["exp_id"] for e in h["experiments"]), want)

    def test_physiological_without_gene_pair(self):
        for h in self.rec("INV-18")["hypotheses"]:
            self.assertIs(h["gene_arc"], False)
            self.assertEqual(h["kind"], "physiological_hypothesis")
            self.assertFalse([k for k in h if "hgnc" in k.lower() or k in ("gene_a", "gene_b", "relation")])
        mh1 = next(h for h in self.rec("INV-18")["hypotheses"] if h["hyp_id"] == "MH1")
        self.assertTrue({"A04", "A05", "A06"} <= {a["alt_id"] for a in mh1["alternatives"]})

    def test_ampa_nmda_keeps_rivals_and_matrix(self):
        bh2 = next(h for h in self.rec("INV-05")["hypotheses"] if h["hyp_id"] == "BH2")
        self.assertTrue({"AB04", "AB05"} <= {a["alt_id"] for a in bh2["alternatives"]})
        arms = {a["arm_id"] for e in bh2["experiments"] for a in e["arms"]}
        self.assertTrue({"M04", "M05", "M06"} <= arms)
        a = next(x for e in bh2["experiments"] for x in e["arms"] if x["arm_id"] == "M05")
        self.assertIn("INFERENZA", a["prediction_label"])  # the label that says no cell is a measured result survives

    def test_unresolved_rival_link_is_reported_not_guessed(self):
        # BH1 cites no alternative id in any cell; its rivals are matrix columns only. The reader must not map them.
        bh1 = next(h for h in self.rec("INV-05")["hypotheses"] if h["hyp_id"] == "BH1")
        self.assertEqual(bh1["alternatives"], [])
        self.assertIn("H1_AMPA_dependent_drive", bh1["matrix_columns_cited"].values())

    def test_carried_case_stays_carried(self):
        for inv, hid in (("INV-18", "MH2"), ("INV-05", "BH2")):
            h = next(x for x in self.rec(inv)["hypotheses"] if x["hyp_id"] == hid)
            self.assertEqual(h["link_state"], "CARRIED_IN_TEXT")

    def test_absent_link_is_unlinked_not_negative(self):
        r = self.rec("INV-01")
        self.assertEqual((r["state"], r["hypotheses"]), ("UNLINKED", []))
        self.assertIn("not evidence against", hp._brief(r))

    def test_reader_writes_nothing(self):
        before = _digest(hp.DR)
        hp.record_for(self.pkgs, "INV-05")
        hp.main(["check"])
        self.assertEqual(before, _digest(hp.DR))


class Synthetic(unittest.TestCase):
    def pkg(self, tmp: Path, links: str, exps: str = "exp_id\thypothesis\tcomparison_arms\nE1\tX1\tnone\n") -> dict:
        o = tmp / "p" / "output"
        o.mkdir(parents=True)
        (o / "hypotheses.tsv").write_text("hyp_id\tstatus\tchain\tcompeting_explanation\tcounter_evidence\tweakening_result\tdiscriminating_experiment\twhat_would_change_the_decision\nX1\ts\tc\tA01 and Q9\t\t\t\t\nX2\ts\tc\t\t\t\t\t\n")
        (o / "alternatives.tsv").write_text("alt_id\texplanation\nA01\trival\n")
        (o / "experiments.tsv").write_text(exps)
        (o / "consumer_links.tsv").write_text(links)
        return hp.load_package(tmp / "p")

    L = "hyp_id\tkind\tneed_id\tinv_id\tcard_ids\tlink_state\tcarried_check\tsource\n"
    INVS = {"INV-9": {"next_test": "a d-APV arm", "intervention": "tool"}}

    def test_missing_experiment_is_no_experiment(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X2\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n")
            h = hp.record_for([p], "INV-9")["hypotheses"][0]
            self.assertEqual((h["experiment_state"], h["experiments"]), ("NO_EXPERIMENT", []))

    def test_unknown_token_is_unresolved(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X1\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n")
            h = hp.record_for([p], "INV-9")["hypotheses"][0]
            self.assertEqual([a["alt_id"] for a in h["alternatives"]], ["A01"])
            self.assertEqual(h["unresolved_refs"], ["Q9"])

    def test_validation_refuses_bad_rows(self):
        bad = ("X9\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n"      # unknown hypothesis
               "X1\tgene_bridge\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n"                       # not a physiological hypothesis
               "X1\tphysiological_hypothesis\tNOPE\tINV-0\tNOCARD\tAPPLIED\t\ts\n"               # need, inv, card, state
               "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\t\ts\n"               # no check
               "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\tnext_test:gone\ts\n")  # check not in text
        with tempfile.TemporaryDirectory() as t:
            errs = hp.validate(self.pkg(Path(t), self.L + bad), needs={"N1"}, invs=self.INVS, cards=Path(t))
        for frag in ("hypothesis id not in", "kind 'gene_bridge'", "need 'NOPE'", "investigation 'INV-0'", "card 'NOCARD'",
                     "link_state 'APPLIED'", "without a carried_check", "carried_check 'next_test:gone'"):
            self.assertTrue(any(frag in e for e in errs), frag)

    def test_good_carried_row_passes(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\tnext_test:d-APV\ts\n")
            self.assertEqual(hp.validate(p, needs={"N1"}, invs=self.INVS, cards=Path(t)), [])


class Reader(unittest.TestCase):
    """The H3/H4 paths on a small synthetic package: rows, references, matrix_column, classes, comparison, manifest."""
    HY = "hyp_id\tstatus\tchain\tcompeting_explanation\tcounter_evidence\tweakening_result\tdiscriminating_experiment\twhat_would_change_the_decision\n"
    AL = "alt_id\texplanation\tmatrix_column\n"
    EX = "exp_id\thypothesis\tcomparison_arms\nE1\tX1\tM01 and M09\n"
    MX = "arm_id\tH1_first\tH2_second\tprediction_label\nM01\tfalls\tstays\tINFERENZA\n"

    def make(self, tmp, alt_rows, links=None, comp=False):
        o = Path(tmp) / "p" / "output"
        o.mkdir(parents=True)
        (o / "hypotheses.tsv").write_text(self.HY + "X1\ts\tc\tH1 rivals A01 and A09 at P13, F04, Z944 and A77\t\t\t\t\n")
        (o / "alternatives.tsv").write_text(self.AL + alt_rows)
        (o / "experiments.tsv").write_text(self.EX)
        (o / "prediction_matrix.tsv").write_text(self.MX)
        (o / "probes.tsv").write_text("probe\nZ944\n")
        (o / "consumer_links.tsv").write_text("hyp_id\tkind\tneed_id\tinv_id\tcard_ids\tlink_state\tcarried_check\tsource\nX1\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n")
        return hp.load_package(Path(tmp) / "p")

    def test_matrix_column_reaches_the_alternative_and_the_expected_result(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.make(t, "A01\tfirst rival\tH1_first\nA02\tcolumn rival\tH1_first\nA03\tunmapped\t\n")
            h = hp.record_for([p], "INV-9")["hypotheses"][0]
            self.assertEqual([a["alt_id"] for a in h["alternatives"]], ["A01"])                    # cited by id
            self.assertEqual([a["alt_id"] for a in h["alternatives_via_matrix_column"]], ["A02"])  # reached by its column
            exp = h["experiments"][0]["expected_results"]
            self.assertEqual([(e["arm_id"], e["column"], e["predicted"], e["prediction_label"]) for e in exp], [("M01", "H1_first", "falls", "INFERENZA")])
            self.assertEqual(hp.validate(p, needs={"N1"}, invs={"INV-9": {}}, cards=Path(t)), [])

    def test_blank_matrix_column_stays_unmapped_and_a_wrong_one_is_refused(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.make(t, "A01\tr\t\n")
            self.assertEqual(hp.alt_columns(p), {})
        with tempfile.TemporaryDirectory() as t:
            p = self.make(t, "A01\tr\tH9_nothing\n")
            self.assertTrue(any("H9_nothing" in e for e in hp.validate(p, needs={"N1"}, invs={"INV-9": {}}, cards=Path(t))))

    def test_rows_carry_their_file_and_line(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.make(t, "A01\tr\tH1_first\nA02\tr\t\n")
            refs = hp.record_for([p], "INV-9")["hypotheses"][0]["source_refs"]
            self.assertTrue(refs["hyp:X1"].endswith("hypotheses.tsv:2"))
            self.assertTrue(refs["alt:A01"].endswith("alternatives.tsv:2"))
            self.assertTrue(refs["arm:M01"].endswith("prediction_matrix.tsv:2"))

    def test_unresolved_tokens_are_classified_and_only_broken_is_a_defect(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.make(t, "A01\tr\t\n")
            (Path(t) / "cards").mkdir()
            (Path(t) / "cards" / "F04_x.card.json").write_text("{}")
            known = set(p["alts"]) | set(p["hyps"]) | set(p["arms"]) | set(p["exps"])
            cl = {tok: hp.classify_ref(tok, known, p["probe_text"], Path(t) / "cards") for tok in ("P13", "F04", "Z944", "A77", "X9z".upper(), "S1")}
            self.assertEqual(cl["P13"], "AGE")
            self.assertEqual(cl["F04"], "CARD_ID")
            self.assertEqual(cl["Z944"], "PROBE_NAME")
            self.assertEqual(cl["A77"], "BROKEN_REFERENCE")   # the A family exists, that number does not
            self.assertEqual(cl["S1"], "UNCLASSIFIED")        # no rule applies: not guessed, not a defect

    def test_comparison_is_a_separate_record_and_keeps_its_qualifiers(self):
        with tempfile.TemporaryDirectory() as t:
            o = Path(t) / "c" / "output"
            o.mkdir(parents=True)
            (o / "comparison.tsv").write_text("hyp_id\tcompound_or_probe_qualified_or_identity_unresolved\toutcome_weakens\nH_a (first)\tidentity unresolved; see D01 and D77\tw1\nH_b (second)\tq2\tw2\n")
            (o / "new_measurements.tsv").write_text("meas_id\tmeasurement\tblocks_which_comparison_row\nM-1\tm1\tH_a; H_b\nM-2\tm2\tall rows\nM-3\tm3\tH_zzz\n")
            (o / "decisive.tsv").write_text("prop_id\tstatement\nD01\ts1\n")
            c = hp.load_comparison(Path(t) / "c")
            c.update({"inv_id": "INV-9"})
            rec = hp.comparison_for([c], "INV-9")
            rows = {r["key"]: r for r in rec["rows"]}
            self.assertEqual(rec["state"], "COMPARISON_PRESENT")
            self.assertEqual([m["meas_id"] for m in rows["H_a"]["new_measurements"]], ["M-1", "M-2"])   # 'all rows' reaches every key
            self.assertEqual([m["meas_id"] for m in rows["H_b"]["new_measurements"]], ["M-1", "M-2"])
            self.assertEqual([d["prop_id"] for d in rows["H_a"]["decisive_cited"]], ["D01"])
            self.assertEqual(rows["H_a"]["broken_decisive_refs"], ["D77"])
            self.assertIn("identity unresolved", rows["H_a"]["qualifier_cells"]["compound_or_probe_qualified_or_identity_unresolved"])
            self.assertIs(rows["H_a"]["gene_arc"], False)
            self.assertEqual(rows["H_a"]["kind"], "pharmacological_comparison")
            self.assertTrue(any("H_zzz" in e for e in hp.validate(c, invs={"INV-9": {}})))             # a block on no key is refused
            self.assertEqual(hp.comparison_for([c], "INV-0")["state"], "NO_COMPARISON_LISTED")

    def test_comparison_key_column_may_be_row_id(self):
        with tempfile.TemporaryDirectory() as t:
            o = Path(t) / "c" / "output"
            o.mkdir(parents=True)
            (o / "comparison.tsv").write_text("row_id\tcompound_or_probe\tidentity_status\nC1\tNBQX\tunresolved\nC2\tGYKI 53655\tname_mismatch\n")
            (o / "new_measurements.tsv").write_text("meas_id\tmeasurement\tblocks_which_comparison_row\nM-A1\tm\tC1; C2\n")
            c = hp.load_comparison(Path(t) / "c")
            c["inv_id"] = "INV-9"
            rows = {r["key"]: r for r in hp.comparison_for([c], "INV-9")["rows"]}
            self.assertEqual(sorted(rows), ["C1", "C2"])
            self.assertEqual(rows["C2"]["row"]["identity_status"], "name_mismatch")   # the qualifier survives verbatim
            self.assertEqual([m["meas_id"] for m in rows["C2"]["new_measurements"]], ["M-A1"])
            self.assertEqual(hp.validate(c, invs={"INV-9": {}}), [])

    def test_only_manifest_packages_are_read(self):
        listed = {m["dir"] for m in hp.read_manifest()}
        self.assertEqual({p["dir"].parent.name for p in hp.load_all()}, listed)
        self.assertTrue(set(hp.unlisted_packages()).isdisjoint(listed))

    def test_manifest_validation_refuses_a_missing_reason_or_inv(self):
        with tempfile.TemporaryDirectory() as t:
            m = Path(t) / "m.tsv"
            m.write_text("package\tdir\trole\tinv_id\twhy\nx\tno_such_dir\tpharmacological_comparison\t\t\n")
            errs = hp.validate_manifest(m)
            for frag in ("required", "not found", "names the investigation"):
                self.assertTrue(any(frag in e for e in errs), frag)

    def test_comparison_on_real_data_stays_apart_from_hypotheses(self):
        pkgs = hp.load_all()
        rec = hp.record_for(pkgs, "INV-05")
        cmp_ = hp.comparison_for(pkgs, "INV-05")
        self.assertEqual({h["kind"] for h in rec["hypotheses"]}, {"physiological_hypothesis"})
        self.assertEqual({r["kind"] for r in cmp_["rows"]}, {"pharmacological_comparison"})
        # a reference must point at the row it names: line 2 is the first data row after the header
        first = cmp_["rows"][0]
        path, _, line = first["source_refs"]["cmp:" + first["key"]].rpartition(":")
        self.assertEqual(Path(hp.REPO / path).read_text(encoding="utf-8").split("\n")[int(line) - 1].split("\t")[0], first["row"]["hyp_id"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
