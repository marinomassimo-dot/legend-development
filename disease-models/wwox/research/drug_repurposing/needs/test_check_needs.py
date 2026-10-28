#!/usr/bin/env python3
"""Offline regression for needs.json and its checker. Run from anywhere: python3 test_check_needs.py"""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("check_needs", HERE / "check_needs.py")
cn = importlib.util.module_from_spec(spec)
sys.modules["check_needs"] = cn
spec.loader.exec_module(cn)
DOC = json.loads((HERE / "needs.json").read_text(encoding="utf-8"))


def need(doc, nid):
    return next(n for n in doc["needs"] if n["id"] == nid)


def first_manifest(doc):
    return next(l for n in doc["needs"] for o in n["observed"] for l in o["locators"] if l["kind"] == "manifest")


class Shipped(unittest.TestCase):
    def test_shipped_table_passes(self):
        self.assertEqual(cn.check(DOC)[0], [])

    def test_track_and_goal_vary_independently(self):
        pairs = {(n["track"]["value"], n["goal"]["value"]) for n in DOC["needs"]}
        self.assertEqual(pairs, {("A", "deep_recovery"), ("B", "deep_recovery"), ("A", "partial_benefit")})
        self.assertEqual(need(DOC, "NEED-WWOX-GENE-ADDITION")["track"]["value"], "A")  # gene addition is not Track B for aiming deep

    def test_scope_vocabulary_is_the_bridges(self):
        sys.path.insert(0, str(cn.ROOT / "framework" / "scripts"))
        import repurposing_bridge as bridge
        self.assertTrue(cn.SCOPES - {"UNVERIFIED_HYPOTHESIS"} <= set(bridge.EVIDENCE_SCOPES))


class Defects(unittest.TestCase):
    def broken(self, fn):
        doc = copy.deepcopy(DOC)
        fn(doc)
        return cn.check(doc)[0]

    def test_wrong_anchor(self):
        self.assertTrue(any("anchor" in p for p in self.broken(lambda d: first_manifest(d).update(anchor="no entry contains this"))))

    def test_entry_out_of_range(self):
        self.assertTrue(any("out of range" in p for p in self.broken(lambda d: first_manifest(d).update(entry=99999))))

    def test_missing_document(self):
        def f(d):
            need(d, "NEED-WWOX-PTC-READTHROUGH")["observed"][0]["locators"].append({"kind": "document", "path": "no/such/file.md", "anchor": ""})
        self.assertTrue(any("document missing" in p for p in self.broken(f)))

    def test_track_goal_values(self):
        self.assertTrue(any("track must be" in p for p in self.broken(lambda d: need(d, "NEED-ISR-ATTENUATION").update(track="A"))))
        self.assertTrue(any("goal must be" in p for p in self.broken(lambda d: need(d, "NEED-ISR-ATTENUATION")["goal"].update(value="cure"))))

    def test_scope_vocabulary(self):
        self.assertTrue(any("evidence_scope" in p for p in self.broken(lambda d: need(d, "NEED-ISR-ATTENUATION")["observed"][0].update(evidence_scope="PROVEN"))))

    def test_need_scope_must_be_backed_by_an_observation(self):
        def f(d):
            n = need(d, "NEED-ISR-ATTENUATION")
            n["evidence_scope"] = n["evidence_scope"] + ["UNVERIFIED_HYPOTHESIS"]
        self.assertTrue(any("not carried by any observation" in p for p in self.broken(f)))

    def test_duplicate_id_and_missing_field(self):
        self.assertTrue(any("duplicate" in p for p in self.broken(lambda d: d["needs"][1].update(id=d["needs"][0]["id"]))))
        self.assertTrue(any("missing field" in p for p in self.broken(lambda d: need(d, "NEED-ISR-ATTENUATION").pop("targets"))))

    def test_unresolved_ids(self):
        def f(d):
            s = need(d, "NEED-LACTATE-LDH")["sources"]
            s["cards"].append("Z99_nothing"); s["hypotheses"].append("HYP-19990101-01"); s["registry_ids"].append("CLAIM 999")
        problems = self.broken(f)
        for word in ("card not found", "hypothesis not in the ledger", "registry id does not resolve"):
            self.assertTrue(any(word in p for p in problems), word)


class Cli(unittest.TestCase):
    def test_help_and_run(self):
        r = subprocess.run([sys.executable, "-B", str(HERE / "check_needs.py"), "--help"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)
        r = subprocess.run([sys.executable, "-B", str(HERE / "check_needs.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
