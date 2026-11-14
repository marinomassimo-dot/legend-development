#!/usr/bin/env python3
"""IT44 P2 regressions, offline: a fake ChEMBL transport stands in for the endpoint and goes through the real shared adapter and its cache (HE45).
A measured activity is not an action; a truncated read is not absence; the catalogue join is by id; a screening flood never hides dose-response rows; the cache never answers another query."""
import csv, gzip, json, os, re, sys, tempfile, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "framework")); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import activity_search as A  # noqa: E402
from adapters import _http  # noqa: E402

def act(mid, name, typ, val, atype="F", doc="CHEMBL_DOC1", aid=None, target="CHEMBLT1"):
    return {"activity_id": aid or f"{mid}-{typ}-{val}", "molecule_chembl_id": mid, "parent_molecule_chembl_id": mid, "molecule_pref_name": name, "standard_type": typ, "standard_relation": "=", "standard_value": val,
            "standard_units": "nM", "assay_chembl_id": f"A_{atype}", "target_chembl_id": target, "target_organism": "Homo sapiens", "data_validity_comment": None, "assay_description": "fixture", "document_chembl_id": doc}

class Transport:
    """Serves status, activity (filtered by type, paged), assay and target endpoints from a list of activity rows; counts the activity requests."""
    def __init__(self, rows, release="ChEMBL_T1"):
        self.rows, self.release, self.activity_calls = rows, release, 0
    def __call__(self, url, params=None, body=None, timeout=20):
        if "status.json" in url: return 200, {"chembl_db_version": self.release, "chembl_release_date": "2026-01-01"}
        if "assay.json" in url:
            ids = re.search(r"assay_chembl_id__in=([^&]+)", url).group(1).split("%2C")
            return 200, {"assays": [{"assay_chembl_id": i, "assay_type": i[-1], "assay_organism": "Homo sapiens"} for i in ids]}
        if "target.json" in url:
            return 200, {"targets": [{"target_chembl_id": "CHEMBLT1", "target_type": "SINGLE PROTEIN", "target_components": [{"target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "FAKE1"}]}]}]}
        if "activity.json" in url:
            self.activity_calls += 1
            types = re.search(r"standard_type__in=([^&]+)", url).group(1).replace("%2C", ",").split(",")
            sel = [r for r in self.rows if r["standard_type"] in types]
            off, lim = int(re.search(r"offset=(\d+)", url).group(1)), int(re.search(r"limit=(\d+)", url).group(1))
            return 200, {"page_meta": {"total_count": len(sel), "next": "x" if off + lim < len(sel) else None}, "activities": sel[off:off + lim]}
        return 404, {}

class Offline(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); (self.tmp / "cc/chembl").mkdir(parents=True)
        with gzip.open(self.tmp / "cc/chembl/targets.jsonl.gz", "wt") as f:
            f.write(json.dumps({"organism": "Homo sapiens", "pref_name": "t", "target_chembl_id": "CHEMBLT1", "target_type": "SINGLE PROTEIN",
                                "target_components": [{"target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "FAKE1"}]}]}) + "\n")
        (self.tmp / "rel.tsv").write_text("relation_id\ttarget_symbols\nSX\tFAKE1\n")
        os.environ.update(LEGEND_CATALOG_CACHE=str(self.tmp / "cc"), LEGEND_ACTIVITY_CACHE=str(self.tmp / "act"), LEGEND_ACTIVITY_RESOLVER="0")
        self.addCleanup(lambda: [os.environ.pop(k, None) for k in ("LEGEND_CATALOG_CACHE", "LEGEND_ACTIVITY_CACHE", "LEGEND_ACTIVITY_RESOLVER")])
    def run_path(self, rows, extra=(), cached=False, release="ChEMBL_T1"):
        tr = Transport(rows, release); out = self.tmp / f"out{len(list(self.tmp.glob('out*')))}"
        fetch = _http.make_fetch(str(self.tmp / "act" / release), get=tr) if cached else _http.make_fetch(get=tr)
        rc = A.main(["--relations", str(self.tmp / "rel.tsv"), "--out", str(out), *extra], fetch=fetch)
        self.assertEqual(rc, 0)
        self.calls = tr.activity_calls
        with open(out / "activity_molecules.tsv") as f: return {x["parent_chembl_id"]: x for x in csv.DictReader(f, delimiter="\t")}
    def test_activity_is_never_an_action(self):
        m = self.run_path([act("CHEMBL_A", "alpha", "EC50", "40"), act("CHEMBL_B", "", "IC50", "9")])
        self.assertTrue(all(x["verdict"] == "ACTIVITY_ONLY" and "direction" in x["unknown_fields"] for x in m.values())); self.assertEqual(set(m), {"CHEMBL_A", "CHEMBL_B"})
    def test_truncated_read_is_named(self):
        m = self.run_path([act(f"CHEMBL_{i}", "", "EC50", "40") for i in range(5)], ["--max-rows", "2"])
        self.assertTrue(all("dose_response:TRUNCATED" in x["coverage"] and x["read_state"] == "TRUNCATED" for x in m.values()))
    def test_complete_read_is_named(self):
        m = self.run_path([act("CHEMBL_A", "alpha", "EC50", "40")]); self.assertEqual(m["CHEMBL_A"]["coverage"], "dose_response:COMPLETE")
    def test_screening_deposit_is_flagged_and_a_small_document_is_not(self):
        big = [act(f"CHEMBL_S{i}", "", "IC50", "9", doc="BIGSCREEN") for i in range(250)] + [act("CHEMBL_KEEP", "keep", "EC50", "40", doc="SMALLDOC")]
        m = self.run_path(big)
        self.assertEqual(m["CHEMBL_S1"]["read_state"], "SCREEN_DEPOSIT"); self.assertEqual(m["CHEMBL_KEEP"]["read_state"], "OK")
    def test_a_potency_flood_does_not_hide_the_dose_response_rows(self):
        rows = [act(f"CHEMBL_P{i}", "", "Potency", "900", doc="QHTS") for i in range(300)] + [act("CHEMBL_KEEP", "keep", "EC50", "40", doc="SMALLDOC")]
        m = self.run_path(rows, ["--max-potency-rows", "50"])
        self.assertEqual((m["CHEMBL_KEEP"]["read_state"], m["CHEMBL_KEEP"]["coverage"]), ("OK", "dose_response:COMPLETE"))
        self.assertEqual(m["CHEMBL_P1"]["read_state"], "SCREEN_PARTIAL")              # a sampled screening row is counted, not listed, never read as absence of other rows
        self.assertEqual(len([x for x in m.values() if x["read_state"] == "SCREEN_PARTIAL"]), 50)
    def test_a_molecule_in_both_classes_keeps_complete_dose_response_state(self):
        rows = [act(f"CHEMBL_P{i}", "", "Potency", "900", doc="QHTS") for i in range(100)] + [act("CHEMBL_P1", "both", "EC50", "40", doc="SMALLDOC")]
        self.assertEqual(self.run_path(rows, ["--max-potency-rows", "10"])["CHEMBL_P1"]["read_state"], "OK")
    def test_best_potency_is_not_pooled_across_types_targets_or_assays(self):
        m = self.run_path([act("CHEMBL_A", "alpha", "EC50", "5000", atype="F", aid="a1"), act("CHEMBL_A", "alpha", "Ki", "2", atype="B", aid="a2"), act("CHEMBL_A", "alpha", "IC50", "90", atype="B", aid="a3")])["CHEMBL_A"]
        self.assertEqual(m["n_measure_groups"], "3"); self.assertNotIn("best_nM", m)
        self.assertIn("EC50", m["measure_summary"]); self.assertIn("activity_id=a1", m["measure_summary"]); self.assertIn("activity_id=a2", m["measure_summary"])
    def test_activity_rows_keep_the_original_row_id(self):
        self.run_path([act("CHEMBL_A", "alpha", "EC50", "40", aid="777")])
        rows = list(csv.DictReader(open(next(self.tmp.glob("out*/activity_rows.tsv"))), delimiter="\t"))
        self.assertEqual((rows[0]["activity_id"], rows[0]["read_class"]), ("777", "dose_response"))
    def test_cache_does_not_answer_another_query(self):
        rows = [act("CHEMBL_A", "alpha", "IC50", "40"), act("CHEMBL_B", "beta", "EC50", "30")]
        first = self.run_path(rows, ["--types", "IC50"], cached=True)
        second = self.run_path(rows, ["--types", "IC50,EC50"], cached=True)            # the earlier cache entry is for IC50 only
        self.assertEqual(set(first), {"CHEMBL_A"}); self.assertEqual(set(second), {"CHEMBL_A", "CHEMBL_B"})
    def test_one_cache_directory_per_release(self):
        d, basis = A.release_dir(self.tmp / "act", lambda url: (200, {"chembl_db_version": "ChEMBL_77"}))
        self.assertEqual((d.name, basis), ("ChEMBL_77", "status_endpoint")); self.assertTrue(d.is_dir())
        d2, basis2 = A.release_dir(self.tmp / "act", lambda url: (0, "down"))                  # offline: the newest cached release, declared
        self.assertEqual(d2.name, "ChEMBL_77"); self.assertIn("NETWORK_UNREACHABLE", basis2)
        d3, basis3 = A.release_dir(self.tmp / "nothing", lambda url: (0, "down"))
        self.assertEqual((d3, basis3), (None, "UNKNOWN"))
    def test_symbol_without_target_is_unread_not_empty(self):
        with gzip.open(self.tmp / "cc/chembl/targets.jsonl.gz", "wt") as f: f.write("")
        (self.tmp / "rel.tsv").write_text("relation_id\ttarget_symbols\nSX\tNOSUCHGENE\n")
        A.main(["--relations", str(self.tmp / "rel.tsv"), "--out", str(self.tmp / "outx")], fetch=_http.make_fetch(get=Transport([])))
        self.assertEqual(json.load(open(self.tmp / "outx/activity_manifest.json"))["_symbols"], {"SX:NOSUCHGENE": "UNRESOLVED_IN_CACHED_INDEX"})
    def test_unnamed_molecule_without_catalogue_row_is_status_none(self):
        m = self.run_path([act("CHEMBL_ZZ_NOT_IN_CATALOGUE", "", "Ki", "5", atype="B")])["CHEMBL_ZZ_NOT_IN_CATALOGUE"]; self.assertEqual((m["catalogue_status"], m["n_functional"]), ("none", "0"))
    def test_a_checkout_without_the_cached_target_file_says_what_to_set_instead_of_a_traceback(self):
        (self.tmp / "rel.tsv").write_text("relation_id\ttarget_symbols\nSX\tKCNQ2\n")
        saved = os.environ.get("LEGEND_CATALOG_CACHE"); os.environ["LEGEND_CATALOG_CACHE"] = str(self.tmp / "no_cache_here")
        try:
            import io, contextlib
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                code = A.main(["--relations", str(self.tmp / "rel.tsv"), "--out", str(self.tmp / "outy")], fetch=_http.make_fetch(get=Transport([])))
        finally:
            if saved is None: os.environ.pop("LEGEND_CATALOG_CACHE", None)
            else: os.environ["LEGEND_CATALOG_CACHE"] = saved
        self.assertEqual(code, 2); self.assertIn("LEGEND_CATALOG_CACHE", err.getvalue()); self.assertIn("nothing was read", err.getvalue())

if __name__ == "__main__": unittest.main(verbosity=2)
