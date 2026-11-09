#!/usr/bin/env python3
"""Regressions for framework/scripts/compound_identity.py (offline: a synthetic catalogue and a canned ChEMBL answer).

Pinned: the match kind is carried (an exact name, a synonym and a substring are three different answers); a salt or a
differently named record never outranks an exact name; a declared identity is reachable when no record carries the name;
a label that sits on two structures keeps its source rows out of the attribution; a gene named in a record or an
activity row is evidence that it was reported, with selectivity always NOT_ASSESSED; and empty, not-read and error stay
three states.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compound_identity as ci  # noqa: E402


def entry(i, name, syn=(), chembl=None, targets=(), concept=()):
    return {"id": i, "name": name, "synonyms": list(syn), "origin": "t", "relations": {"parent": i},
            "ids": {"chembl": chembl, "chembl_from_dgidb_concept_not_enumerated": list(concept)}, "targets": list(targets)}


DG = lambda g: {"gene": g, "source": "DGIdb interaction"}  # noqa: E731
CM = lambda *g: {"gene_symbols": list(g), "source": "ChEMBL curated mechanism"}  # noqa: E731

ES = [
    entry("CAT:A", "IFENPRODIL", chembl="CHEMBL1"),
    entry("CAT:B", "IFENPRODIL TARTRATE", chembl="CHEMBL2"),
    entry("CAT:C", "Gyki53784", syn=["GYKI-52466"], targets=[DG("GRIA1")]),
    entry("CAT:D", "BRILLIANT BLUE G", chembl="CHEMBL4"),
    entry("CAT:E", "MEMANTINE", chembl="CHEMBL5", targets=[CM("GRIN2B")]),
    entry("CAT:F", "Gyki53655", chembl="CHEMBL6"),
]
RECON = [{"candidate": "CAT:C", "chembl_ref": "CHEMBL275006", "chembl_ref_in_catalogue": "no", "decision": "out_of_selection", "gtopdb_inchikey": "K"}]
DECL = [
    {"query_name": "GYKI 52466", "role": "identity", "chembl_id": "CHEMBL275006"},
    {"query_name": "GYKI 52466", "role": "label_conflict", "chembl_id": "-"},
    {"query_name": "brilliant blue FCF", "role": "identity", "chembl_id": "CHEMBL3184128"},
    {"query_name": "brilliant blue FCF", "role": "distinct_from", "chembl_id": "CHEMBL4173394"},
]


def res(name):
    return ci.resolve(ES, name, RECON, DECL)


def act(gene, org, kind="activity"):
    return {"kind": kind, "target_gene_symbols": [gene], "target_organism": org, "standard_type": "IC50"}


def stub(answers):
    return lambda req: answers[req.get("molecule_id") or req["molecule"]] if "molecule_id" in req else answers["act:" + req["molecule"]]


class Identity(unittest.TestCase):
    def test_exact_outranks_salt_and_partial_is_labelled(self):
        r = res("ifenprodil")
        self.assertEqual(r["identity_state"], "NAME_EXACT")
        self.assertEqual([(c["catalogue_id"], c["match_kind"]) for c in r["candidates"]], [("CAT:A", "NAME_EXACT"), ("CAT:B", "NAME_PARTIAL")])

    def test_synonym_hit_keeps_the_record_name_and_the_out_of_selection_twin(self):
        r = res("GYKI 52466")
        c = r["candidates"][0]
        self.assertEqual((r["identity_state"], c["match_kind"], c["record_name"]), ("SYNONYM_EXACT", "SYNONYM_EXACT", "Gyki53784"))
        self.assertEqual(c["chembl_refs"][0]["chembl_id"], "CHEMBL275006")
        self.assertEqual(c["chembl_refs"][0]["in_catalogue"], "no")
        self.assertEqual(len(r["label_conflict"]), 1)

    def test_distinct_compound_is_not_merged_and_name_prefix_is_not_identity(self):
        r = res("brilliant blue FCF")
        self.assertEqual(r["identity_state"], "DECLARED")  # no record carries the name; BRILLIANT BLUE G is not a hit
        self.assertEqual(r["candidates"], [])
        self.assertIn("CHEMBL4173394", [d["chembl_id"] for d in r["declarations"] if d["role"] == "distinct_from"])
        self.assertEqual(ci._chembl_ids(r), ["CHEMBL3184128"])

    def test_separator_variant_is_found_and_labelled_not_called_exact(self):
        r = res("GYKI 53655")                              # the record is named Gyki53655: no space
        self.assertEqual((r["identity_state"], r["candidates"][0]["match_kind"]), ("SEPARATOR_VARIANT", "SEPARATOR_VARIANT"))
        self.assertEqual(res("GYKI 52466")["candidates"][0]["match_kind"], "SYNONYM_EXACT")   # a synonym stays a synonym

    def test_unknown_name_says_nothing_about_the_compound(self):
        r = res("no such tool")
        self.assertEqual(r["identity_state"], "NOT_FOUND_BY_NAME")
        self.assertIn("not about the compound", r["note"])


class Target(unittest.TestCase):
    def test_level_is_the_highest_read_and_selectivity_is_not_assessed(self):
        t = ci.target_evidence(res("memantine"), ["GRIN2B"], ES, None)
        self.assertEqual(t["per_gene"]["GRIN2B"]["level"], "CURATED_MECHANISM")
        self.assertEqual(t["selectivity"], "NOT_ASSESSED")

    def test_measured_activity_levels_by_species(self):
        a = {"CHEMBL1": {"status": "MATCH_FOUND", "hits": []},
             "act:CHEMBL1": {"status": "MATCH_FOUND", "coverage": "COMPLETE", "total_count": 3,
                             "hits": [act("Grin2b", "Rattus norvegicus"), act("SIGMAR1", "Homo sapiens"), act("GRIN2B", "Homo sapiens")]}}
        t = ci.target_evidence(res("ifenprodil"), ["GRIN2B", "GRIN2A"], ES, stub(a))
        self.assertEqual(t["per_gene"]["GRIN2B"]["level"], "MEASURED_ACTIVITY_HUMAN")
        self.assertEqual(t["per_gene"]["GRIN2A"]["level"], "EMPTY_RESULT")   # read, nothing: not "absent"
        self.assertIn("SIGMAR1", t["other_genes_seen"])

    def test_empty_not_read_and_error_are_three_states(self):
        empty = {"CHEMBL1": {"status": "NO_MATCH_FOUND", "hits": []}, "act:CHEMBL1": {"status": "NO_MATCH_FOUND", "hits": []}}
        err = {"CHEMBL1": {"status": "QUERY_ERROR", "hits": []}, "act:CHEMBL1": {"status": "QUERY_ERROR", "hits": []}}
        got = [ci.target_evidence(res("ifenprodil"), ["GRIN2B"], ES, q)["per_gene"]["GRIN2B"]["level"] for q in (stub(empty), stub(err), None)]
        self.assertEqual(got, ["EMPTY_RESULT", "READ_ERROR", "NOT_READ"])

    def test_label_conflict_keeps_the_record_rows_out_of_the_attribution(self):
        a = {"CHEMBL275006": {"status": "MATCH_FOUND", "hits": []},
             "act:CHEMBL275006": {"status": "MATCH_FOUND", "coverage": "COMPLETE", "total_count": 1, "hits": [act("GRIA2", "Homo sapiens")]}}
        t = ci.target_evidence(res("GYKI 52466"), ["GRIA1", "GRIA2"], ES, stub(a))
        self.assertEqual(t["per_gene"]["GRIA2"]["level"], "MEASURED_ACTIVITY_HUMAN")
        self.assertEqual(t["per_gene"]["GRIA1"]["level"], "EMPTY_RESULT")      # the DGIdb GRIA1 row is not claimed for this structure
        self.assertTrue(any("GRIA1" in u for u in t["unattributed_source_rows"]))


class Committed(unittest.TestCase):
    def test_declarations_are_complete_and_dated(self):
        rows = ci._rows(ci.DECLARATIONS)
        self.assertTrue(rows)
        for r in rows:
            self.assertTrue(r["basis"] and r["retrieved_on"], r)
            self.assertIn(r["role"], ("identity", "salt_or_parent", "distinct_from", "label_conflict"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
