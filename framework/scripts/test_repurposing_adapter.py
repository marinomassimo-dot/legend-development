#!/usr/bin/env python3
"""Regressions for the repurposing adapter seam (framework/adapters/ + repurposing_adapter.py).

Offline: every case runs through canned responses. The live measurement of each adapter is done
by hand with `selftest --live` and recorded with its date in the task record, because a
regression that needs six external services up is a regression that gets disabled.

Properties pinned:
  1. discovery is the directory listing — no registration anywhere;
  2. removing each adapter in turn leaves the CLI and every other adapter green (one-file removal);
  3. every shipped adapter's offline selftest is green and its output meets the convention;
  4. `add` writes a loadable module that passes the contract check; `remove` deletes only that file;
  5. a QUERY_ERROR, a NO_MATCH_FOUND and a MATCH_FOUND stay three different states, and
     NO_MATCH_FOUND carries the "never absence" note;
  6. no output hit carries a score/rank/probability/belief key.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_adapter as ra  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "framework" / "scripts" / "repurposing_adapter.py"
ADAPTERS = ROOT / "framework" / "adapters"


def cli(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(CLI), *args], capture_output=True, text=True, cwd=cwd)


class Discovery(unittest.TestCase):
    def test_population_is_the_directory_listing(self):
        names = ra.discover(ADAPTERS)
        on_disk = sorted(p.stem for p in ADAPTERS.glob("*.py") if not p.name.startswith("_"))
        self.assertEqual(names, on_disk)
        self.assertGreaterEqual(len(names), 1)
        self.assertNotIn("_http", names)

    def test_list_prints_every_adapter(self):
        done = cli("list")
        self.assertEqual(done.returncode, 0, done.stderr)
        for name in ra.discover(ADAPTERS):
            self.assertIn(name, done.stdout)


class ShippedAdapters(unittest.TestCase):
    def test_every_adapter_selftest_is_green_offline(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                report = ra.run_selftest(name, ADAPTERS, live=False)
                self.assertTrue(report.get("ok"), report)

    def test_every_adapter_output_meets_the_convention(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                self.assertEqual(ra.check_info(module), [], name)
                self.assertEqual(module.INFO["name"], name)
                self.assertRegex(module.INFO["licence_read_on"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertTrue(module.INFO["licence_url"].startswith("http"))
                result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: ra._sample_response(module))
                self.assertEqual(ra.check_output(result), [], name)
                self.assertEqual(result["licence"], module.INFO["licence"])
                self.assertEqual(result["citation"], module.INFO["citation"])

    def test_no_record_carries_an_email_address(self):
        for path in list(ADAPTERS.glob("*.py")) + [ra.DEFAULT_ACK]:
            self.assertNotRegex(path.read_text(encoding="utf-8"), r"[\w.+-]+@[\w-]+\.[\w.]+", path.name)


class Acknowledgements(unittest.TestCase):
    def test_committed_file_matches_the_adapters(self):
        self.assertTrue(ra.DEFAULT_ACK.exists(), ra.DEFAULT_ACK)
        self.assertEqual(ra.DEFAULT_ACK.read_text(encoding="utf-8"), ra.render_acknowledgements(ADAPTERS),
                         "ACKNOWLEDGEMENTS.md is stale: run repurposing_adapter.py acknowledgements --write")

    def test_every_adapter_has_a_section_with_licence_and_citation(self):
        text = ra.render_acknowledgements(ADAPTERS)
        for name in ra.discover(ADAPTERS):
            module = ra.load(name, ADAPTERS)
            self.assertIn(f"## {name}", text)
            self.assertIn(module.INFO["citation"], text)
            self.assertIn(module.INFO["licence_url"].split(" ")[0], text)
        self.assertIn("grateful", text)

    def test_remove_rerenders_the_list_without_the_removed_adapter(self):
        tmp = Path(tempfile.mkdtemp(prefix="ack_"))
        try:
            work = tmp / "adapters"
            shutil.copytree(ADAPTERS, work, ignore=shutil.ignore_patterns("__pycache__"))
            victim = ra.discover(work)[0]
            done = cli("--dir", str(work), "remove", victim)
            self.assertEqual(done.returncode, 0, done.stderr)
            rendered = (work / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8")
            self.assertNotIn(f"## {victim}", rendered)
            for other in ra.discover(work):
                self.assertIn(f"## {other}", rendered)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_transport_failure_is_query_error_with_text(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: (0, "URLError: name resolution"))
                self.assertEqual(result["status"], "QUERY_ERROR")
                self.assertIn("URLError", result["error"])
                self.assertEqual(ra.check_output(result), [])

    def test_empty_request_is_query_error_not_no_match(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                result = module.query({}, fetch=lambda *a, **k: (200, {}))
                self.assertEqual(result["status"], "QUERY_ERROR")
                self.assertTrue(result["error"])


class OneFileRemoval(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="adapters_"))
        self.dir = self.tmp / "adapters"
        shutil.copytree(ADAPTERS, self.dir, ignore=shutil.ignore_patterns("__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_removing_each_adapter_in_turn_leaves_the_rest_green(self):
        names = ra.discover(self.dir)
        self.assertGreaterEqual(len(names), 2)
        for victim in names:
            with self.subTest(removed=victim):
                work = self.tmp / f"minus_{victim}"
                shutil.copytree(self.dir, work)
                done = cli("--dir", str(work), "remove", victim)
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertFalse((work / f"{victim}.py").exists())
                remaining = sorted(set(names) - {victim})
                self.assertEqual(ra.discover(work), remaining)
                done = cli("--dir", str(work), "selftest")
                self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
                self.assertIn(f"{len(remaining)} adapter(s), 0 red", done.stdout)
                for other in remaining:  # the other adapter files are byte-identical: nothing else was edited by hand
                    self.assertEqual((work / f"{other}.py").read_bytes(), (self.dir / f"{other}.py").read_bytes())

    def test_add_writes_a_loadable_module_and_remove_deletes_only_it(self):
        before = {p.name: p.read_bytes() for p in self.dir.glob("*.py")}
        done = cli("--dir", str(self.dir), "add", "example_source")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("example_source", ra.discover(self.dir))
        report = ra.run_selftest("example_source", self.dir, live=False)
        # The template loads and runs, but is red until its licence fields are filled from the
        # source's own terms page: an unfilled adapter is never green.
        self.assertFalse(report.get("ok"), report)
        self.assertTrue(any("placeholder" in p for p in report.get("contract_problems", [])), report)
        self.assertIn("## example_source", (self.dir / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8"))
        done = cli("--dir", str(self.dir), "remove", "example_source")
        self.assertEqual(done.returncode, 0, done.stderr)
        after = {p.name: p.read_bytes() for p in self.dir.glob("*.py")}
        self.assertEqual(before, after)
        self.assertNotIn("## example_source", (self.dir / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8"))

    def test_add_refuses_a_private_or_existing_name(self):
        self.assertEqual(cli("--dir", str(self.dir), "add", "_private").returncode, 2)
        self.assertEqual(cli("--dir", str(self.dir), "add", ra.discover(self.dir)[0]).returncode, 2)


class ThreeStates(unittest.TestCase):
    def test_pubtator_empty_list_is_no_match_with_the_note(self):
        module = ra.load("pubtator3", ADAPTERS)
        result = module.query({"gene": "WWOX", "type": "treat"}, fetch=lambda *a, **k: (200, []))
        self.assertEqual(result["status"], "NO_MATCH_FOUND")
        self.assertIn("never absence", result["note"])
        self.assertEqual(result["hits"], [])

    def test_chembl_match_found_needs_the_named_substance(self):
        module = ra.load("chembl", ADAPTERS)

        def fetch(url, params=None, body=None, timeout=20):
            if "molecule/search" in url:
                return 200, {"molecules": [
                    {"molecule_chembl_id": "CHEMBL1", "pref_name": "CYANOCOBALAMIN CO 57", "molecule_synonyms": []},
                    {"molecule_chembl_id": "CHEMBL2", "pref_name": "VALPROATE",
                     "molecule_synonyms": [{"molecule_synonym": "Depakene"}]}]}
            if "mechanism.json" in url:
                return 200, {"mechanisms": [{"action_type": "MODULATOR", "mechanism_of_action": "x"}]}
            return 200, {"chembl_db_version": "ChEMBL_T"}
        # a class or sentence is not a molecule: the nearest hit must not become MATCH_FOUND
        near = module.query({"drug": "HSP70 co-inducers"}, fetch=fetch)
        self.assertEqual(near["status"], "NO_MATCH_FOUND")
        self.assertEqual(near["hits"], [])
        self.assertTrue(near["nearest"])
        self.assertIn("never absence", near["note"])
        # a synonym of the named substance is the substance, even when it is not the first hit
        named = module.query({"drug": "depakene"}, fetch=fetch)
        self.assertEqual(named["status"], "MATCH_FOUND")
        self.assertEqual({h["molecule_chembl_id"] for h in named["hits"]}, {"CHEMBL2"})

    def _chembl_fallback_fetch(self, parent_reply):
        """Mocked HTTP layer (no network): molecule-id lookup returns 0 rows; the parent lookup answers `parent_reply`."""
        def fetch(url, params=None, body=None, timeout=20):
            if "molecule/search" in url:
                return 200, {"molecules": [{"molecule_chembl_id": "CHEMBL192", "pref_name": "SILDENAFIL",
                                            "max_phase": 4, "molecule_synonyms": []}]}
            if "parent_molecule_chembl_id=" in url:
                return parent_reply
            if "mechanism.json" in url:
                return 200, {"mechanisms": []}
            return 200, {"chembl_db_version": "ChEMBL_T", "chembl_release_date": "2026-01-01"}
        return fetch

    def test_chembl_parent_fallback_keeps_identity_provenance_and_status(self):
        module = ra.load("chembl", ADAPTERS)
        reply = (200, {"mechanisms": [{"action_type": "INHIBITOR", "mechanism_of_action": "PDE5 inhibitor",
                                       "target_chembl_id": "CHEMBL1827",
                                       "mechanism_refs": [{"ref_type": "DailyMed", "ref_id": "setid=x"}]}]})
        out = module.query({"drug": "sildenafil"}, fetch=self._chembl_fallback_fetch(reply))
        self.assertEqual(out["status"], "MATCH_FOUND")
        self.assertEqual(out["error"], "")
        self.assertEqual([h["kind"] for h in out["hits"]], ["mechanism"])
        hit = out["hits"][0]
        self.assertEqual((hit["molecule_chembl_id"], hit["pref_name"], hit["max_phase"]), ("CHEMBL192", "SILDENAFIL", 4))
        self.assertEqual(hit["references"], ["DailyMed:setid=x"])
        self.assertEqual(out["source_version"], "ChEMBL_T 2026-01-01")
        self.assertTrue(any("mechanism.json?molecule_chembl_id=CHEMBL192" in u for u in out["requests_sent"]))
        self.assertTrue(any("parent_molecule_chembl_id=CHEMBL192" in u for u in out["requests_sent"]))
        self.assertEqual(out["evidence_label"], "NOT WWOX EVIDENCE")

    def test_chembl_parent_fallback_error_is_an_error_never_no_mechanism(self):
        module = ra.load("chembl", ADAPTERS)
        for reply in ((500, "server error"), (0, "timeout"), (200, "not a dict")):
            with self.subTest(reply=reply):
                out = module.query({"drug": "sildenafil"}, fetch=self._chembl_fallback_fetch(reply))
                self.assertEqual(out["status"], "QUERY_ERROR")
                self.assertTrue(out["error"])
                self.assertEqual(out["hits"], [])  # no molecule_without_mechanism hit is manufactured
        # a genuine empty parent answer is the only route to molecule_without_mechanism
        empty = module.query({"drug": "sildenafil"}, fetch=self._chembl_fallback_fetch((200, {"mechanisms": []})))
        self.assertEqual(empty["status"], "MATCH_FOUND")
        self.assertEqual([h["kind"] for h in empty["hits"]], ["molecule_without_mechanism"])

    def test_openfda_404_is_no_match_not_error(self):
        module = ra.load("openfda", ADAPTERS)
        result = module.query({"drug": "amlexanox"}, fetch=lambda *a, **k: (404, {"error": {"code": "NOT_FOUND"}}))
        self.assertEqual(result["status"], "NO_MATCH_FOUND")
        self.assertEqual(result["error"], "")

    def test_server_error_is_query_error(self):
        module = ra.load("opentargets", ADAPTERS)
        result = module.query({"ensembl_id": "ENSG00000186153"}, fetch=lambda *a, **k: (503, "down"))
        self.assertEqual(result["status"], "QUERY_ERROR")
        self.assertIn("503", result["error"])

    def test_opentargets_drops_the_association_score(self):
        module = ra.load("opentargets", ADAPTERS)
        result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: module.SAMPLE["response"])
        self.assertNotIn("score", json.dumps(result["hits"]).lower())

    def test_contract_check_flags_a_score_key(self):
        bad = {"adapter": "x", "retrieved_at": "t", "request": {}, "requests_sent": [], "status": "MATCH_FOUND",
               "hits": [{"score": 0.9}], "source_version": "UNKNOWN", "evidence_label": "NOT WWOX EVIDENCE",
               "licence": "CC0; key-less", "citation": "x", "note": "never absence", "error": ""}
        self.assertTrue(any("score" in p for p in ra.check_output(bad)))


class ChemblActivities(unittest.TestCase):
    """The iteration-6 activity mode: accession resolution, assay context, pagination, errors."""

    def _fetch(self, total=3, assay_status=200, activity_status=200):
        rows = [{"activity_id": i, "molecule_chembl_id": f"CHEMBL{i}", "assay_chembl_id": "CHEMBLA1", "standard_type": "IC50",
                 "standard_relation": "=", "standard_value": "150.0", "standard_units": "nM", "pchembl_value": "6.82",
                 "target_chembl_id": "CHEMBL1904", "target_organism": "Homo sapiens", "document_chembl_id": "CHEMBLD",
                 "data_validity_comment": None, "potential_duplicate": 0} for i in range(total)]
        def fetch(url, params=None, body=None, timeout=20):
            if "status.json" in url:
                return 200, {"chembl_db_version": "ChEMBL_T", "chembl_release_date": "2026-01-01"}
            if "target.json" in url and "target_chembl_id__in" in url:
                return 200, {"targets": [{"target_chembl_id": "CHEMBL1904", "target_type": "PROTEIN COMPLEX", "pref_name": "Glutamate NMDA receptor",
                                          "target_components": [{"target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "GRIN1"}]},
                                                                {"target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "GRIN2A"}]}]},
                                         {"target_chembl_id": "CHEMBL612545", "target_type": "UNCHECKED", "pref_name": "Unchecked", "target_components": []},
                                         {"target_chembl_id": "CHEMBL2093872", "target_type": "PROTEIN FAMILY", "pref_name": "GABA-A receptor", "target_components": []}]}
            if "target.json" in url:
                return 200, {"targets": [{"target_chembl_id": "CHEMBL1904", "target_type": "SINGLE PROTEIN", "organism": "Homo sapiens",
                                          "target_components": [{"accession": "Q13224"}]},
                                         {"target_chembl_id": "CHEMBL1907603", "target_type": "PROTEIN COMPLEX", "organism": "Homo sapiens",
                                          "target_components": [{"accession": "Q05586"}, {"accession": "Q13224"}]}]}
            if "activity.json" in url:
                if activity_status != 200:
                    return activity_status, "boom"
                off = int(url.split("offset=")[1].split("&")[0]) if "offset=" in url else 0
                lim = int(url.split("limit=")[1].split("&")[0])
                page = rows[off:off + lim]
                return 200, {"page_meta": {"total_count": len(rows), "next": "x" if off + lim < len(rows) else None}, "activities": page}
            if "assay.json" in url:
                if assay_status != 200:
                    return assay_status, "no"
                return 200, {"assays": [{"assay_chembl_id": "CHEMBLA1", "assay_organism": "frog", "assay_cell_type": "Oocyte"}]}
            return 404, {}
        return fetch

    def test_accession_resolves_single_protein_and_complexes_apart(self):
        out = ra.load("chembl", ADAPTERS).query({"uniprot": "Q13224"}, fetch=self._fetch())
        self.assertEqual([h["target_type"] for h in out["hits"]], ["SINGLE PROTEIN", "PROTEIN COMPLEX"])
        self.assertEqual(out["status"], "MATCH_FOUND")

    def test_activity_rows_carry_assay_organism_apart_from_target_organism(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch())
        h = out["hits"][0]
        self.assertEqual((h["target_organism"], h["assay_context"]["assay_organism"]), ("Homo sapiens", "frog"))
        self.assertEqual((out["total_count"], out["retrieved"], out["truncated"]), (3, 3, False))
        self.assertEqual(ra.check_output(out), [])

    def test_activity_rows_carry_component_gene_symbols_and_flag_placeholder_targets(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch())
        h = out["hits"][0]
        self.assertEqual((h["target_type"], h["target_gene_symbols"], h["non_gene_target"]), ("PROTEIN COMPLEX", ["GRIN1", "GRIN2A"], False))
        base = self._fetch()
        def fetch(url, params=None, body=None, timeout=20):
            status, payload = base(url, params, body, timeout)
            if "activity.json" in url and status == 200:
                payload = dict(payload, activities=[dict(a, target_chembl_id="CHEMBL612545") for a in payload["activities"]])
            return status, payload
        h = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=fetch)["hits"][0]
        self.assertEqual((h["target_gene_symbols"], h["non_gene_target"]), (None, True))      # a placeholder target is flagged, not read as 'no gene'
        def fetch_family(url, params=None, body=None, timeout=20):
            status, payload = base(url, params, body, timeout)
            if "activity.json" in url and status == 200:
                payload = dict(payload, activities=[dict(a, target_chembl_id="CHEMBL2093872") for a in payload["activities"]])
            return status, payload
        h = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=fetch_family)["hits"][0]
        self.assertEqual((h["target_type"], h["target_gene_symbols"], h["non_gene_target"]), ("PROTEIN FAMILY", None, None))      # a protein family without component symbols is unknown, not 'non-gene'


    def test_target_lookup_failure_is_declared_and_rows_keep_null_genes(self):
        base = self._fetch()
        def fetch(url, params=None, body=None, timeout=20):
            return (503, "no") if "target.json" in url else base(url, params, body, timeout)
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=fetch)
        self.assertIn("target genes incomplete", out["note"])
        self.assertIsNone(out["hits"][0]["target_gene_symbols"])
        self.assertEqual(out["status"], "MATCH_FOUND")

    def test_molecule_alone_reads_every_target_and_says_so(self):
        seen = []
        base = self._fetch()
        def fetch(url, params=None, body=None, timeout=20):
            seen.append(url)
            return base(url, params, body, timeout)
        out = ra.load("chembl", ADAPTERS).query({"molecule": "CHEMBL807"}, fetch=fetch)
        act = [u for u in seen if "activity.json" in u][0]
        self.assertIn("molecule_chembl_id=CHEMBL807", act)
        self.assertNotIn("target_chembl_id=", act)
        self.assertEqual((out["scope"]["target"], out["scope"]["molecule"]), (None, "CHEMBL807"))

    def test_a_hit_page_cap_is_reported_as_truncated(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904", "max_rows": 2}, fetch=self._fetch(total=5))
        self.assertEqual((out["retrieved"], out["total_count"], out["truncated"]), (2, 5, True))
        self.assertIn("TRUNCATED", out["note"])

    def test_activity_http_error_is_query_error_never_no_match(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(activity_status=500))
        self.assertEqual(out["status"], "QUERY_ERROR")
        self.assertIn("500", out["error"])

    def test_assay_context_failure_is_declared_and_rows_keep_null_context(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(assay_status=503))
        self.assertIn("assay context incomplete", out["note"])
        self.assertIsNone(out["hits"][0]["assay_context"])

    def test_no_row_under_the_filters_is_no_match_not_absence(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(total=0))
        self.assertEqual(out["status"], "NO_MATCH_FOUND")
        self.assertIn("never absence", out["note"])


def load_http():
    from importlib import util
    spec = util.spec_from_file_location("adapters_http", ADAPTERS / "_http.py")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class KeepingAFetchedDocument(unittest.TestCase):
    """IT15: third-party READMEs saved verbatim into a tracked package leaked contributor
    e-mail addresses to the release gate and left relative links that dangled in the copy."""

    ORIGIN = "https://example.invalid/tool/blob/v1.2/README.md"
    SOURCE = ("# Tool\nMaintainer: jane.roe" + "@lab.example.org\n"
              "See [install](docs/install.md) and [usage](#usage) and [site](https://example.invalid/x).\n"
              "Licensed under Apache-2.0; copyright the authors.\n")

    def test_address_bearing_text_is_refused_the_original_stays_and_a_reference_replaces_it(self):
        from importlib import util
        gate_path = ROOT / "scripts" / "public_release_gate.py"
        spec = util.spec_from_file_location("public_release_gate", gate_path)
        gate = util.module_from_spec(spec)
        sys.modules[spec.name] = gate
        spec.loader.exec_module(gate)
        http = load_http()
        with tempfile.TemporaryDirectory() as tmp:
            corpus, repo = Path(tmp) / "files", Path(tmp) / "repo"
            repo.mkdir()
            record = http.keep_original(corpus, "tool/README.md", self.SOURCE.encode(), self.ORIGIN, "v1.2")
            with self.assertRaises(http.NoticeContainsAddress) as caught:
                http.public_extract(self.SOURCE, self.ORIGIN)
            self.assertIn("lines [2]", str(caught.exception))
            self.assertNotIn("lab.example.org", str(caught.exception), "the refusal reports lines, never the address")
            (repo / "reference.md").write_text(http.reference_record(record, "Apache-2.0", "install steps read; no claim"), encoding="utf-8")
            findings: list = []
            gate.scan_privacy_and_secrets(repo, findings)
            self.assertNotIn("EMAIL_ADDRESS", {f.code for f in findings})
            ref = (repo / "reference.md").read_text(encoding="utf-8")
            for needle in (record["sha256"], self.ORIGIN, "v1.2", "Apache-2.0"):
                self.assertIn(needle, ref)
            # the original is byte-identical, addressed by digest, and refuses silent replacement
            self.assertEqual(self.SOURCE.encode(), (corpus / "tool/README.md").read_bytes())
            self.assertEqual(http.hashlib.sha256(self.SOURCE.encode()).hexdigest(), record["sha256"])
            with self.assertRaises(FileExistsError):
                http.keep_original(corpus, "tool/README.md", b"changed", self.ORIGIN, "v1.3")

    def test_a_text_without_address_keeps_every_licence_byte(self):
        http = load_http()
        clean = "# Tool\nCopyright 2026 The Tool Authors\nLicensed under Apache-2.0; see [LICENSE](LICENSE).\n"
        out = http.public_extract(clean, self.ORIGIN)
        self.assertEqual(clean.replace("(LICENSE)", "(https://example.invalid/tool/blob/v1.2/LICENSE)"), out)
        self.assertIn("Copyright 2026 The Tool Authors\nLicensed under Apache-2.0;", out)

    def test_relative_paths_and_anchors_resolve_against_the_source(self):
        http = load_http()
        out = http.public_extract(self.SOURCE.replace("Maintainer: jane.roe" + "@lab.example.org\n", ""), self.ORIGIN)
        self.assertIn("(https://example.invalid/tool/blob/v1.2/docs/install.md)", out)
        self.assertIn("(https://example.invalid/tool/blob/v1.2/README.md#usage)", out)
        self.assertIn("(https://example.invalid/x)", out)
        self.assertNotIn("(docs/install.md)", out)
        self.assertNotIn("(#usage)", out)


class ReusableToolsAnswerHelpOffline(unittest.TestCase):
    """IT16: `--help` of a reusable fetch tool must not touch the network or write a file. The
    shebang was never the safety: vfetch_activities.py made three network attempts on `--help`."""

    GUARD = ("import runpy, socket, sys\n"
             "def deny(*a, **k):\n"
             "    sys.stderr.write('NETWORK_ATTEMPT'); raise OSError('network denied')\n"
             "socket.socket.connect = deny; socket.create_connection = deny; socket.getaddrinfo = deny\n"
             "script = sys.argv[1]; sys.argv = [script, '--help']\n"
             "runpy.run_path(script, run_name='__main__')\n")
    TOOLS = (
        "framework/scripts/repurposing_adapter.py",
        "disease-models/wwox/research/drug_repurposing/verify_it15_qb_20261101/vfetch_activities.py",
    )

    def test_help_makes_no_network_attempt_and_writes_nothing(self):
        for tool in self.TOOLS:
            with self.subTest(tool=tool), tempfile.TemporaryDirectory() as scratch:
                done = subprocess.run([sys.executable, "-c", self.GUARD, str(ROOT / tool)],
                                      capture_output=True, text=True, cwd=scratch, timeout=60)
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertNotIn("NETWORK_ATTEMPT", done.stdout + done.stderr)
                self.assertEqual([], list(Path(scratch).iterdir()))


class ResilientTransport(ChemblActivities):
    """IT16 P3: a bounded retry and a cache of successful responses only; coverage states stay distinct; declared identity and salt/parent stay apart."""

    def setUp(self):
        sys.path.insert(0, str(ROOT))
        from framework.adapters import _http
        self.H = _http
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def _counting(self, inner, fail_if=None):
        calls = []
        def get(url, params=None, body=None, timeout=20):
            calls.append(url)
            if fail_if and fail_if(url, len(calls)):
                return 500, "boom"
            return inner(url, params, body, timeout)
        get.calls = calls
        return get

    def test_retry_is_bounded_logged_and_a_4xx_is_not_retried(self):
        seq = [500, 0, 200]
        def inner(url, params=None, body=None, timeout=20):
            st = seq.pop(0)
            return st, ({"ok": 1} if st == 200 else "x")
        f = self.H.make_fetch(None, retries=2, pause=0, get=inner, sleep=lambda s: None)
        self.assertEqual(f("u")[0], 200)
        self.assertEqual([x["http"] for x in f.failures], [500, 0])
        self.assertEqual(f.stats["requests_ended_in_error"], 0)
        g = self.H.make_fetch(None, retries=2, pause=0, get=lambda *a: (500, "b"), sleep=lambda s: None)
        self.assertEqual(g("u")[0], 500)
        self.assertEqual((len(g.failures), g.stats["requests_ended_in_error"]), (3, 1))
        h = self.H.make_fetch(None, retries=2, pause=0, get=lambda *a: (404, {}), sleep=lambda s: None)
        h("u"); self.assertEqual(h.stats["network_requests"], 1)

    def test_only_success_is_cached_and_nothing_is_written_without_a_directory(self):
        d = Path(self.tmp) / "cache"
        st = {"n": 0}
        def inner(url, params=None, body=None, timeout=20):
            st["n"] += 1
            return (500, "e") if st["n"] <= 3 else (200, {"v": 1})
        f = self.H.make_fetch(str(d), retries=0, pause=0, get=inner, sleep=lambda s: None)
        self.assertEqual(f("u")[0], 500)
        self.assertFalse(d.exists())
        self.assertEqual((f("u")[0], f("u")[0]), (500, 500))
        self.assertEqual(f("u")[0], 200)
        n = st["n"]
        self.assertEqual(f("u"), (200, {"v": 1}))
        self.assertEqual(st["n"], n)
        self.assertEqual(f.stats["cache_hits"], 1)
        (next(d.glob("*.json"))).write_text("{damaged")
        self.assertEqual(f("u")[0], 200)  # a damaged file is a miss
        before = sorted(Path(self.tmp).rglob("*"))
        self.H.make_fetch(None, get=lambda *a: (200, {"v": 2}))("u")
        self.assertEqual(sorted(Path(self.tmp).rglob("*")), before)

    def test_failed_page_is_partial_not_no_match_and_a_rerun_reads_only_the_missing_page(self):
        inner = self._fetch(total=450)
        bad = {"on": True}
        get = self._counting(inner, fail_if=lambda url, n: bad["on"] and "activity.json" in url and "offset=200" in url)
        f1 = self.H.make_fetch(self.tmp, retries=0, pause=0, get=get, sleep=lambda s: None)
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904", "max_rows": 450}, fetch=f1)
        self.assertEqual((out["status"], out["coverage"], out["retrieved"], out["total_count"], out["next_offset"]), ("QUERY_ERROR", "PARTIAL_ERROR", 200, 450, 200))
        self.assertEqual(len(out["hits"]), 200)
        bad["on"] = False
        before = len(get.calls)
        f2 = self.H.make_fetch(self.tmp, retries=0, pause=0, get=get, sleep=lambda s: None)
        out2 = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904", "max_rows": 450}, fetch=f2)
        self.assertEqual((out2["status"], out2["coverage"], out2["retrieved"]), ("MATCH_FOUND", "COMPLETE", 450))
        new_urls = get.calls[before:]
        self.assertFalse(any("offset=0" in u for u in new_urls), "page 1 must come from the cache")
        self.assertTrue(any("offset=200" in u for u in new_urls) and any("offset=400" in u for u in new_urls))
        self.assertGreaterEqual(out2["transport"]["cache_hits"], 1)

    def test_first_page_failure_is_not_read_and_cap_above_2000_is_honoured_and_reported(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(activity_status=500))
        self.assertEqual(out["coverage"], "NOT_READ")
        big = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904", "max_rows": 2300}, fetch=self._fetch(total=2300))
        self.assertEqual((big["retrieved"], big["coverage"], big["truncated"]), (2300, "COMPLETE", False))
        cut = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904", "max_rows": 2}, fetch=self._fetch(total=5))
        self.assertEqual(cut["coverage"], "TRUNCATED")
        self.assertEqual(ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(total=0))["status"], "NO_MATCH_FOUND")

    def test_missing_assay_context_is_a_coverage_state_of_a_complete_row_set(self):
        out = ra.load("chembl", ADAPTERS).query({"target": "CHEMBL1904"}, fetch=self._fetch(assay_status=503))
        self.assertEqual((out["coverage"], out["assay_batches_failed"], out["retrieved"]), ("COMPLETE_ASSAY_CONTEXT_MISSING", 1, 3))

    def _identity_fetch(self):
        salt = {"molecule_chembl_id": "CHEMBL2", "pref_name": "DRUG HYDROCHLORIDE", "max_phase": -1.0, "molecule_synonyms": [{"molecule_synonym": "Drug hcl"}],
                "molecule_hierarchy": {"parent_chembl_id": "CHEMBL1", "molecule_chembl_id": "CHEMBL2"}}
        noname = {"molecule_chembl_id": "CHEMBL9", "pref_name": None, "molecule_synonyms": [], "molecule_hierarchy": {"parent_chembl_id": "CHEMBL9"}}
        def fetch(url, params=None, body=None, timeout=20):
            if "status.json" in url:
                return 200, {"chembl_db_version": "ChEMBL_T"}
            if "molecule/search" in url:
                return 200, {"molecules": [noname]}
            if "molecule/CHEMBL2.json" in url:
                return 200, salt
            if "molecule/CHEMBL9.json" in url:
                return 200, noname
            if "molecule/CHEMBL404.json" in url:
                return 404, {}
            if "mechanism.json?molecule_chembl_id=CHEMBL2" in url:
                return 200, {"mechanisms": []}
            if "mechanism.json?parent_molecule_chembl_id=CHEMBL1" in url:
                return 200, {"mechanisms": [{"action_type": "ANTAGONIST", "mechanism_of_action": "x antagonist", "target_chembl_id": "CHEMBLT", "mechanism_refs": []}]}
            if "mechanism.json" in url:
                return 200, {"mechanisms": []}
            return 404, {}
        return fetch

    def test_a_name_ChEMBL_does_not_store_is_no_match_with_candidates_and_a_declared_id_resolves_it(self):
        mod = ra.load("chembl", ADAPTERS)
        byname = mod.query({"drug": "Ro 25-6981"}, fetch=self._identity_fetch())
        self.assertEqual(byname["status"], "NO_MATCH_FOUND")
        self.assertEqual(byname["nearest"][0]["parent_molecule_chembl_id"], "CHEMBL9")
        declared = mod.query({"drug": "Ro 25-6981", "molecule_id": "CHEMBL9"}, fetch=self._identity_fetch())
        self.assertEqual((declared["status"], declared["identity_basis"], declared["queried_name"]), ("MATCH_FOUND", "declared_chembl_id", "Ro 25-6981"))
        self.assertEqual(declared["hits"][0]["kind"], "molecule_without_mechanism")
        gone = mod.query({"drug": "x", "molecule_id": "CHEMBL404"}, fetch=self._identity_fetch())
        self.assertEqual(gone["status"], "NO_MATCH_FOUND")

    def test_salt_id_reads_the_mechanism_from_its_parent_and_says_so(self):
        out = ra.load("chembl", ADAPTERS).query({"drug": "delucemine", "molecule_id": "CHEMBL2"}, fetch=self._identity_fetch())
        h = out["hits"][0]
        self.assertEqual((h["molecule_chembl_id"], h["parent_molecule_chembl_id"], h["queried_is_salt_or_child"], h["mechanism_found_via"]), ("CHEMBL2", "CHEMBL1", True, "parent_filter"))
        self.assertTrue(any("parent_molecule_chembl_id=CHEMBL1" in u for u in out["requests_sent"]))
        self.assertFalse(any("activity.json" in u for u in out["requests_sent"]), "no activity row is borrowed from another molecule")


class CacheRefusesEmptyAnd200Errors(unittest.TestCase):
    def test_empty_or_error_envelope_200_is_not_cached(self):
        h = load_http()
        for payload in ({}, [], {"error": "rate limited"}, {"detail": "x", "message": "y"}):
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as d:
                calls = []
                def get(url, params=None, body=None, timeout=20, _p=payload):
                    calls.append(url); return 200, _p
                f = h.make_fetch(cache_dir=d, get=get)
                f("http://x/a"); f("http://x/a")
                self.assertEqual(2, len(calls), "must be re-fetched, not served from cache")
                self.assertEqual([], os.listdir(d))


class StandingMethodIsReachable(unittest.TestCase):
    """IT16 P5: the roles and the Scientist brief reach the repurposing standing method by link, and the target section exists."""
    def test_links_and_anchor(self):
        road = (ROOT / "disease-models/wwox/research/drug_repurposing/roadmap_current.md").read_text(encoding="utf-8")
        self.assertIn("\n## Standing method\n", road)
        for f in ("CLAUDE.md", "roles/orchestrator.md", "roles/scientist.md", "framework/protocols/scientist_standing_brief.md"):
            self.assertIn("roadmap_current.md#standing-method", (ROOT / f).read_text(encoding="utf-8"), f)
        conv = road.split("## Standing method")[1].split("\n## ")[0]
        self.assertIn("repurposing_adapter_convention.md", conv)


class KeepingAFetchedDocumentEdges(unittest.TestCase):
    ORIGIN = "https://example.invalid/tool/blob/v1.2/README.md"

    def test_keep_original_refuses_a_name_outside_the_corpus(self):
        http = load_http()
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp) / "files"
            for bad in ("../esc.txt", "/abs/esc.txt", "a/../../esc.txt", "."):
                with self.assertRaises(ValueError, msg=bad):
                    http.keep_original(corpus, bad, b"x", self.ORIGIN, "v1")
            self.assertFalse((Path(tmp) / "esc.txt").exists())

    def test_every_link_form_is_resolved(self):
        http = load_http()
        out = http.public_extract(
            "![logo](img/pic.png) [a](<docs/my file.md>) [ref]\n\n[ref]: guide.md\n"
            '<a href="x/y.html">h</a> <img src=\'z.png\'> [abs](https://e.invalid/q)\n'
            "Copyright 2026 The Authors, Apache-2.0\n", self.ORIGIN)
        base = "https://example.invalid/tool/blob/v1.2/"
        for expected in (f"({base}img/pic.png)", f"(<{base}docs/my file.md>)", f"[ref]: {base}guide.md",
                         f'href="{base}x/y.html"', f"src='{base}z.png'", "(https://e.invalid/q)",
                         "Copyright 2026 The Authors, Apache-2.0"):
            self.assertIn(expected, out)

    def test_an_address_is_refused_in_a_copyright_line_and_in_a_mailto_target_never_masked(self):
        http = load_http()
        for text in ("Copyright 2026 Jane <jane" + "@lab.org>, Apache-2.0\n", "[mail](mailto:a" + "@b.org)\n"):
            with self.subTest(text=text):
                with self.assertRaises(http.NoticeContainsAddress):
                    http.public_extract(text, self.ORIGIN)
        self.assertFalse(hasattr(http, "EMAIL_REPLACEMENT"), "no text is rewritten into a masked variant")


class CacheValidatesOnRead(unittest.TestCase):
    """IT17 P1.1: the write-side guard does not protect against entries written before it or damaged since; one test serves both sides."""
    URL = "http://x/molecule/search.json?q=a"

    def _seed(self, d, h, payload, raw=None):
        f = h.make_fetch(cache_dir=d, get=lambda *a: (200, {"molecules": [1]}))
        path = os.path.join(d, h.hashlib.sha256(json.dumps([self.URL, None, None], sort_keys=True, default=str).encode()).hexdigest() + ".json")
        os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(raw if raw is not None else json.dumps({"url": self.URL, "http": 200, "retrieved_at": "t", "payload": payload}))
        return path

    def _run(self, payload, expect="molecules", raw=None, retries=2, get_replies=None):
        h = load_http()
        calls, replies = [], list(get_replies or [(200, {"molecules": [{"id": 1}], "page_meta": {}})])
        def get(url, params=None, body=None, timeout=20):
            calls.append(url); return replies.pop(0) if len(replies) > 1 else replies[0]
        with tempfile.TemporaryDirectory() as d:
            path = self._seed(d, h, payload, raw)
            f = h.make_fetch(cache_dir=d, retries=retries, pause=0, get=get, sleep=lambda s: None)
            out = f(self.URL, expect=expect)
            return out, f, calls, sorted(os.listdir(d)), path

    def test_old_error_only_entry_is_a_miss_refetched_and_kept_aside(self):
        out, f, calls, files, path = self._run({"error": "rate limited"})
        self.assertEqual(200, out[0]); self.assertIn("molecules", out[1])
        self.assertEqual(1, len(calls))
        self.assertEqual(1, f.stats["cache_discarded"]); self.assertEqual(0, f.stats["cache_hits"])
        self.assertEqual("bare error envelope", f.discarded[0]["reason"])
        self.assertTrue(any(n.endswith(".json.discarded") for n in files), files)
        self.assertEqual(2, len(files), "the good answer replaced the entry; the bad one is kept")

    def test_legitimate_empty_page_is_a_hit(self):
        empty = {"molecules": [], "page_meta": {"total_count": 0, "next": None}}
        out, f, calls, files, _ = self._run(empty)
        self.assertEqual((200, empty), out)
        self.assertEqual([], calls); self.assertEqual(0, f.stats["cache_discarded"]); self.assertEqual(1, f.stats["cache_hits"])

    def test_entry_missing_the_expected_key_is_a_miss_but_without_expectation_it_is_a_hit(self):
        out, f, calls, _, _ = self._run({"page_meta": {}, "other": []})
        self.assertEqual(1, len(calls)); self.assertEqual(1, f.stats["cache_discarded"])
        self.assertIn("'molecules'", f.discarded[0]["reason"])
        out, f, calls, _, _ = self._run({"page_meta": {}, "other": []}, expect=None)
        self.assertEqual([], calls); self.assertEqual(1, f.stats["cache_hits"])

    def test_damaged_json_is_a_miss_and_counted(self):
        out, f, calls, files, _ = self._run(None, raw="{not json")
        self.assertEqual(1, len(calls)); self.assertEqual(1, f.stats["cache_discarded"])
        self.assertEqual("damaged JSON", f.discarded[0]["reason"])

    def test_retry_stays_bounded_after_a_discard(self):
        out, f, calls, files, _ = self._run({"error": "x"}, retries=2, get_replies=[(503, "down")])
        self.assertEqual(503, out[0]); self.assertEqual(3, len(calls))
        self.assertEqual(1, f.stats["cache_discarded"]); self.assertEqual(3, f.stats["failed_attempts"])

    def test_a_refetched_answer_still_lacking_the_key_is_not_cached(self):
        out, f, calls, files, _ = self._run({"error": "x"}, get_replies=[(200, {"unexpected": 1})])
        self.assertEqual(1, len(calls))
        self.assertEqual(files, [n for n in files if n.endswith(".discarded")], "only the kept-aside entry remains")

    def test_chembl_adapter_tells_a_caching_fetch_which_key_it_needs(self):
        h = load_http()
        seen = []
        def get(url, params=None, body=None, timeout=20):
            seen.append(url)
            if "status.json" in url:
                return 200, {"chembl_db_version": "ChEMBL_X", "chembl_release_date": "d"}
            return 200, {"molecules": [], "page_meta": {}}
        with tempfile.TemporaryDirectory() as d:
            f = h.make_fetch(cache_dir=d, get=get, retries=0)
            out = ra.load("chembl", ADAPTERS).query({"drug": "nothing"}, fetch=f)
            self.assertEqual("NO_MATCH_FOUND", out["status"])
            n = len(seen)
            out2 = ra.load("chembl", ADAPTERS).query({"drug": "nothing"}, fetch=f)
            self.assertEqual(n, len(seen), "the legitimate empty page was a cache hit")
            self.assertEqual("NO_MATCH_FOUND", out2["status"])
            self.assertEqual(0, out2["transport"]["cache_discarded"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
