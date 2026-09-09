#!/usr/bin/env python3
"""Tests for locator_identifier_provenance.py.

The first test is the one that matters: the tool, as first written, MISSED the error it was
built for, because the offending proposition contained an unrelated external-provenance
phrase. That regression is test 1 and it must never go green by accident.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import locator_identifier_provenance as L  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "locator_identifier_provenance.py"


def build(tmp: Path, proposition: str, artefact_text: str = "reference list pmid 29310447") -> Path:
    (tmp / "files").mkdir(parents=True, exist_ok=True)
    art = tmp / "files" / "src.xml"
    art.write_text(artefact_text)
    manifest = {
        "schema_version": 2, "pmid": "31428585",
        "source_artifacts": [{"path": "files/src.xml", "sha256": "x", "kind": "article_text"}],
        "verbatim_locators": {"entries": [
            {"proposition": proposition, "snippet": "s", "surface": "body",
             "artifact": "files/src.xml", "anchor": "a"}]},
    }
    path = tmp / "PMID31428585.json"
    path.write_text(json.dumps(manifest))
    return path


class TestProvenance(unittest.TestCase):
    def _audit(self, proposition, artefact_text="reference list pmid 29310447"):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            rep = L.audit_manifest(build(tmp, proposition, artefact_text), tmp)
            return {r["identifier"]: r["verdict"] for r in rep["rows"]}

    def test_1_the_real_error_is_caught_despite_a_declaring_phrase(self):
        """THE REGRESSION. 'no receipt here' is a true statement about the ledger and must not
        silence the separate, false claim that this PMID is reference 1 of the source."""
        v = self._audit("attributed to ref 1 (Huang and Chang 2018, PMID 29581896, no receipt here)")
        self.assertEqual(v["29581896"], "SOURCE_IDENTITY_UNVERIFIED")

    def test_2_the_corrected_value_passes(self):
        v = self._audit("attributed to ref 1 = Huang and Chang 2018, pmid 29310447")
        self.assertEqual(v["29310447"], "IN_ARTEFACT")

    def test_3_a_declared_external_identifier_is_not_flagged(self):
        v = self._audit("PMID 24550385 is already read here at complete_fulltext_read in this corpus")
        self.assertEqual(v["24550385"], "DECLARED_EXTERNAL")

    def test_4_an_undeclared_external_identifier_is_flagged(self):
        v = self._audit("This bears on the findings of PMID 26499798 about the same protein")
        self.assertEqual(v["26499798"], "UNDECLARED_EXTERNAL")

    def test_5_identity_claim_outranks_declaration(self):
        """Both signals present; the artefact wins because it is the authority on citation identity."""
        v = self._audit("cited to PMID 11111111, no receipt in this corpus")
        self.assertEqual(v["11111111"], "SOURCE_IDENTITY_UNVERIFIED")

    def test_6_doi_and_pmcid_are_recognised(self):
        v = self._audit("the deposit is PMC6688159 with doi 10.3389/fonc.2019.00719",
                        artefact_text="PMC6688159 10.3389/fonc.2019.00719")
        self.assertEqual(v["PMC6688159"], "IN_ARTEFACT")
        self.assertEqual(v["10.3389/fonc.2019.00719"], "IN_ARTEFACT")

    def test_7_a_pmid_substring_does_not_count_as_present(self):
        """29310447 must not be found inside 293104470 — a boundary bug would make the check
        report provenance it does not have."""
        v = self._audit("attributed to ref 1, PMID 29310447", artefact_text="value 293104470 here")
        self.assertEqual(v["29310447"], "SOURCE_IDENTITY_UNVERIFIED")

    def test_8_snippet_identifiers_are_out_of_scope(self):
        """The snippet is verified verbatim by the manifest validator; identifiers there are the
        source's own words and must not be re-judged as the reader's assertion."""
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            path = build(tmp, "no identifier in this proposition")
            m = json.loads(path.read_text())
            m["verbatim_locators"]["entries"][0]["snippet"] = "as reported in PMID 99999999"
            path.write_text(json.dumps(m))
            rep = L.audit_manifest(path, tmp)
            self.assertEqual(rep["rows"], [])

    def test_9_a_missing_artefact_is_named_not_silently_passed(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            path = build(tmp, "attributed to ref 1, PMID 29310447")
            (tmp / "files" / "src.xml").unlink()
            rep = L.audit_manifest(path, tmp)
            self.assertEqual(rep["artefacts_missing"], ["files/src.xml"])
            self.assertEqual(rep["rows"][0]["verdict"], "SOURCE_IDENTITY_UNVERIFIED")

    def test_10_strict_exit_code(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            path = build(tmp, "attributed to ref 1, PMID 29581896")
            r = subprocess.run([sys.executable, str(SCRIPT), str(path), "--root", str(tmp), "--strict"],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 1)
            r2 = subprocess.run([sys.executable, str(SCRIPT), str(path), "--root", str(tmp)],
                                capture_output=True, text=True)
            self.assertEqual(r2.returncode, 0, "default must be advisory, not a gate")

    def test_11_json_output_is_parseable(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            path = build(tmp, "attributed to ref 1, PMID 29310447")
            r = subprocess.run([sys.executable, str(SCRIPT), str(path), "--root", str(tmp), "--json"],
                               capture_output=True, text=True)
            out = json.loads(r.stdout)
            self.assertEqual(out["measurable"][0]["counts"]["IN_ARTEFACT"], 1)
            self.assertEqual(out["unmeasurable"], [])

    def test_12_a_manifest_with_absent_evidence_is_unmeasurable_not_flagged(self):
        """THE SECOND SELF-INFLICTED DEFECT, KEPT AS A TEST. `files/` is gitignored, so most
        manifests in most checkouts point at bytes that are not present. With an empty haystack
        every identifier is 'not in the artefact', and the first run of this tool duly reported a
        corpus-wide provenance crisis that was really an evidence-locality fact. An unmeasurable
        manifest must be separated, must not enter the totals, and must not trip --strict."""
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            path = build(tmp, "attributed to ref 1, PMID 29581896")
            (tmp / "files" / "src.xml").unlink()
            r = subprocess.run([sys.executable, str(SCRIPT), str(path), "--root", str(tmp),
                                "--json", "--strict"], capture_output=True, text=True)
            out = json.loads(r.stdout)
            self.assertEqual(out["measurable"], [])
            self.assertEqual(len(out["unmeasurable"]), 1)
            self.assertEqual(r.returncode, 0,
                             "absent evidence is not a provenance failure of the reading")


if __name__ == "__main__":
    unittest.main(verbosity=2)
