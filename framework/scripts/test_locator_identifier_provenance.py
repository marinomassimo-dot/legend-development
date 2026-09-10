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
ROOT = SCRIPT.parents[2]
MANIFESTS = ROOT / "disease-models" / "wwox" / "research" / "deepdive_manifests"


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


class TheVerdictSaysWhatWasScreened(unittest.TestCase):
    """Retrospective 9.2. Four zero counts read exactly like a clean result."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_a_manifest_with_no_identifier_is_insufficient_data(self):
        """🔴 Nothing measured is not the same as nothing wrong.

        Corpus-wide this is 11 of 81 manifests, and all 11 were previously inside the
        headline count of what the tool had measured.
        """
        path = build(self.tmp, "The paper reports a growth phenotype in mouse pups.")
        verdict = L.screen_manifest(path, self.tmp)
        self.assertTrue(verdict.is_insufficient, verdict)
        self.assertIn("identifier", verdict.missing)

    def test_an_absent_artefact_is_insufficient_data_naming_the_artefact(self):
        """With an empty haystack every identifier reads as absent. That is locality, not
        provenance, and the verdict must say which bytes are missing."""
        path = build(self.tmp, "PMID 29310447 is cited by the source.")
        (self.tmp / "files" / "src.xml").unlink()
        verdict = L.screen_manifest(path, self.tmp)
        self.assertTrue(verdict.is_insufficient, verdict)
        self.assertIn("declared artefacts", verdict.missing)
        self.assertIn("src.xml", verdict.missing)

    def test_an_unreadable_manifest_is_insufficient_data(self):
        broken = self.tmp / "broken.json"
        broken.write_text("{not json", encoding="utf-8")
        self.assertTrue(L.screen_manifest(broken, self.tmp).is_insufficient)
        self.assertTrue(L.screen_manifest(self.tmp / "absent.json", self.tmp).is_insufficient)

    def test_an_identifier_in_the_artefact_is_clean_with_a_digest(self):
        path = build(self.tmp, "PMID 29310447 is cited by the source.")
        verdict = L.screen_manifest(path, self.tmp)
        self.assertTrue(verdict.is_clean, verdict.render())
        self.assertTrue(verdict.digest.startswith("sha256:"))

    def test_an_undeclared_external_identifier_is_refused_naming_the_signature(self):
        path = build(self.tmp, "PMID 12345678 supports this.")
        verdict = L.screen_manifest(path, self.tmp)
        self.assertTrue(verdict.is_refused, verdict.render())
        self.assertIn("UNDECLARED_EXTERNAL", verdict.signature)

    def test_the_digest_moves_when_the_artefact_moves(self):
        """🔴 The haystack is half the comparison, so it is half the digest.

        A digest over the manifest alone would stay constant while the answer changed.
        """
        path = build(self.tmp, "PMID 29310447 is cited by the source.")
        before = L.screen_manifest(path, self.tmp)
        (self.tmp / "files" / "src.xml").write_text("a different reference list", encoding="utf-8")
        after = L.screen_manifest(path, self.tmp)
        self.assertNotEqual(before.digest, after.digest)
        self.assertNotEqual(before.verdict, after.verdict)


class TheCommandLine(unittest.TestCase):
    """main() was never entered by this suite before 2026-09-10."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def run_cli(self, *args):
        proc = subprocess.run([sys.executable, str(SCRIPT), *args],
                              capture_output=True, text=True)
        return proc.returncode, proc.stdout + proc.stderr

    def test_strict_exits_one_on_a_refusal_and_zero_on_absent_evidence(self):
        path = build(self.tmp, "PMID 12345678 supports this.")
        code, out = self.run_cli(str(path), "--root", str(self.tmp), "--strict")
        self.assertEqual(code, 1, out)
        (self.tmp / "files" / "src.xml").unlink()
        code, out = self.run_cli(str(path), "--root", str(self.tmp), "--strict")
        self.assertEqual(code, 0, "absent evidence is not a provenance failure of the reading")
        self.assertIn("[INSUFFICIENT_DATA]", out)

    def test_the_json_carries_a_verdict_per_manifest(self):
        path = build(self.tmp, "PMID 29310447 is cited by the source.")
        code, out = self.run_cli(str(path), "--root", str(self.tmp), "--json")
        record = json.loads(out)
        self.assertEqual(len(record["verdicts"]), 1)
        self.assertEqual(record["verdicts"][0]["verdict"], "CLEAN")
        self.assertTrue(record["verdicts"][0]["screened"]["digest"].startswith("sha256:"))
        self.assertEqual(code, 0)

    def test_a_manifest_that_could_not_be_measured_is_not_counted_as_measurable(self):
        path = build(self.tmp, "No identifier appears in this proposition at all.")
        code, out = self.run_cli(str(path), "--root", str(self.tmp))
        self.assertIn("measurable (all artefacts present): 0", out)
        self.assertIn("unmeasurable (evidence absent): 1", out)


class RealManifestsFromTheCorpus(unittest.TestCase):
    """Cases drawn from the tracked corpus, degrading to a declared skip when absent."""

    def test_every_verdict_over_the_real_corpus_is_self_consistent(self):
        if not MANIFESTS.is_dir():
            self.skipTest(f"real artefacts absent: {MANIFESTS}")
        paths = sorted(MANIFESTS.glob("PMID*.json"))[:8]
        if not paths:
            self.skipTest("no manifest in the corpus directory")
        for path in paths:
            with self.subTest(manifest=path.name):
                verdict = L.screen_manifest(path, ROOT)
                if verdict.is_insufficient and verdict.missing.startswith("declared artefacts"):
                    # files/ is gitignored: the named bytes must really be absent.
                    for name in verdict.missing.split(": ", 1)[1].split(", "):
                        self.assertFalse((ROOT / name).exists(),
                                         f"{name} exists but was reported missing")
                    continue
                self.assertIsNotNone(verdict.screened,
                                     "a verdict over a real manifest must name its bytes")
                if verdict.is_refused:
                    self.assertTrue(verdict.evidence["rows"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
