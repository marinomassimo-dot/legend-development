#!/usr/bin/env python3
"""Regressions for reacquire.py, with a mutation battery.

The failure mode of a replay tool is not a crash: it is `RECOVERED` over bytes that do not
hash to the declared digest, `TAMPERED` over a publisher's re-typeset PDF, or a `FAILED`
that cannot say what wall it hit. Every one of those is mutated into the shipped source here
and at least one test goes red per mutation. Transport is exercised against a local HTTP
server that plays each wall the 2026-09-09/10 sweep measured — a Cloudflare 403 with its
`cf-ray`, a reCAPTCHA served as HTTP 200, a plain 404 — so the suite needs no network and
writes nothing outside its own temporary workspace. The one real-corpus case reads only.
"""

from __future__ import annotations

import hashlib
import http.server
import importlib.util
import io
import json
import os
import sys
import threading
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reacquire as ra  # noqa: E402

ROOT = HERE.parents[1]
MODULE_PATH = HERE / "reacquire.py"


def load_mutated(*substitutions):
    """Load reacquire.py with textual substitutions applied — the shipped file, mutated."""
    src = MODULE_PATH.read_text(encoding="utf-8")
    for old, new in substitutions:
        if old not in src:
            raise AssertionError(f"mutation target not present in source: {old!r}")
        src = src.replace(old, new, 1)
    spec = importlib.util.spec_from_loader("reacquire_mutant", loader=None)
    module = importlib.util.module_from_spec(spec)
    module.__dict__["__file__"] = str(MODULE_PATH)
    exec(compile(src, str(MODULE_PATH) + " [MUTANT]", "exec"), module.__dict__)
    return module


# --------------------------------------------------------------------------
# a local publisher that plays every wall the sweep measured

OK_XML = b'<?xml version="1.0"?><article><body><p>The declared bytes.</p></body></article>'
CHANGED_PDF = b"%PDF-1.4\n% re-typeset by the publisher\n%%EOF\n"
CAPTCHA_HTML = (b"<html><head><title>Verify</title></head><body>"
                b"<div class=\"g-recaptcha\" data-sitekey=\"x\"></div></body></html>")
CF_HTML = b"<html><body>Attention Required! | Cloudflare</body></html>"
REQUESTS: list[dict] = []


class Publisher(http.server.BaseHTTPRequestHandler):
    def log_message(self, *_args):  # silence
        return

    def do_GET(self):  # noqa: N802
        REQUESTS.append({"path": self.path, "headers": {k.lower(): v for k, v in self.headers.items()}})
        if self.path == "/ok.xml":
            self._send(200, OK_XML, "text/xml")
        elif self.path == "/changed.pdf":
            self._send(200, CHANGED_PDF, "application/pdf")
        elif self.path == "/cf.pdf":
            self._send(403, CF_HTML, "text/html", extra={"Server": "cloudflare", "CF-RAY": "a391d5dedee7d384-FRA"})
        elif self.path == "/captcha.jpg":
            self._send(200, CAPTCHA_HTML, "text/html")
        elif self.path == "/interstitial.pdf":
            self._send(200, b"<html><body>please wait</body></html>", "text/html")
        else:
            self._send(404, b"gone", "text/plain")

    def _send(self, status, body, ctype, extra=None):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)


class Workspace:
    """A temp repository root with one manifest declaring artefacts served by the publisher."""

    def __init__(self, base_url: str):
        self.tmp = TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.base = base_url
        (self.root / "disease-models/wwox/research/deepdive_manifests").mkdir(parents=True)

    def cleanup(self):
        self.tmp.cleanup()

    def manifest(self, pmid: str, artifacts: list[dict]) -> dict:
        data = {"schema_version": 2, "pmid": pmid, "source_artifacts": artifacts}
        (self.root / f"disease-models/wwox/research/deepdive_manifests/PMID{pmid}.json").write_text(
            json.dumps(data), encoding="utf-8")
        data["_file"] = f"PMID{pmid}.json"
        return data

    def recipe(self, route: str, **overrides) -> dict:
        recipe = {"resolved_url": self.base + route, "http_method": "GET", "tier": "test_publisher",
                  "user_agent_policy": "none", "acquired_on": "2026-09-09", "derived": False}
        recipe.update(overrides)
        return recipe


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ReplayAgainstALocalPublisher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Publisher)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:%d" % cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        self.ws = Workspace(self.base)
        self.addCleanup(self.ws.cleanup)
        REQUESTS.clear()

    def _replay(self, artifact, module=ra, **kw):
        manifest = self.ws.manifest("1", [artifact])
        return module.replay_artifact(self.ws.root, manifest, artifact, [], **kw)

    def test_recovered_writes_the_bytes_and_says_what_it_did(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        record = self._replay(art)
        self.assertEqual(record["verdict"], ra.RECOVERED)
        self.assertEqual(record["observed_sha256"], digest(OK_XML))
        self.assertEqual(record["transport"]["status"], 200)
        self.assertEqual(record["transport"]["user_agent_policy_sent"], "none")
        self.assertEqual(record["written"], "written")
        self.assertEqual((self.ws.root / art["path"]).read_bytes(), OK_XML)

    def test_a_no_user_agent_policy_sends_no_user_agent_header(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        self._replay(art)
        self.assertEqual(REQUESTS[-1]["path"], "/ok.xml")
        self.assertNotIn("user-agent", REQUESTS[-1]["headers"])

    def test_an_identified_policy_sends_the_honest_agent(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml", user_agent_policy="identified")}
        self._replay(art)
        self.assertEqual(REQUESTS[-1]["headers"].get("user-agent"), ra.UA_IDENTIFIED)

    def test_a_different_binary_from_the_same_route_is_a_finding_not_tampering(self):
        art = {"path": "files/fulltext/paper.pdf", "sha256": "0" * 64, "kind": "article_binary",
               "acquisition_recipe": self.ws.recipe("/changed.pdf")}
        record = self._replay(art)
        self.assertEqual(record["verdict"], ra.DIGEST_DIFFERS_SAME_ROUTE)
        self.assertEqual(record["declared_sha256"], "0" * 64)
        self.assertEqual(record["observed_sha256"], digest(CHANGED_PDF))
        self.assertIn("not TAMPERED", record["finding"])
        self.assertFalse((self.ws.root / art["path"]).exists(), "mismatched bytes were written")

    def test_a_cloudflare_wall_is_named_as_such(self):
        art = {"path": "files/fulltext/paper.pdf", "sha256": "0" * 64, "kind": "article_binary",
               "acquisition_recipe": self.ws.recipe("/cf.pdf")}
        record = self._replay(art)
        self.assertEqual(record["verdict"], "FAILED_HTTP_403_CLOUDFLARE")
        self.assertEqual(record["transport"]["status"], 403)

    def test_a_recaptcha_served_as_200_is_a_named_failure_never_a_recovery(self):
        art = {"path": "files/figures/f1.jpg", "sha256": digest(CAPTCHA_HTML), "kind": "figure",
               "acquisition_recipe": self.ws.recipe("/captcha.jpg")}
        record = self._replay(art)
        self.assertEqual(record["verdict"], "FAILED_RECAPTCHA")
        self.assertEqual(record["transport"]["challenge"], "recaptcha")

    def test_a_200_that_is_not_the_artefact_is_named(self):
        art = {"path": "files/fulltext/paper.pdf", "sha256": "0" * 64, "kind": "article_binary",
               "acquisition_recipe": self.ws.recipe("/interstitial.pdf")}
        self.assertEqual(self._replay(art)["verdict"], "FAILED_NOT_THE_ARTEFACT")

    def test_a_404_is_named(self):
        art = {"path": "files/fulltext/paper.pdf", "sha256": "0" * 64, "kind": "article_binary",
               "acquisition_recipe": self.ws.recipe("/missing.pdf")}
        self.assertEqual(self._replay(art)["verdict"], "FAILED_HTTP_404")

    def test_no_recipe_is_a_verdict_carrying_the_stated_reason(self):
        art = {"path": "files/fulltext/paper.pdf", "sha256": "0" * 64, "kind": "article_binary"}
        record = self._replay(art)
        self.assertEqual(record["verdict"], ra.NO_RECIPE)
        self.assertIsNone(record["no_recipe_reason"])
        manifest = self.ws.manifest("1", [art])
        ledger = [{"record_kind": "backfill_no_recipe", "pmid": "1", "artifact_path": art["path"],
                   "no_recipe_reason": "pmcid_only_route_unstated", "recorded_at": "t"}]
        record = ra.replay_artifact(self.ws.root, manifest, art, ledger)
        self.assertEqual(record["verdict"], ra.NO_RECIPE)
        self.assertEqual(record["no_recipe_reason"], "pmcid_only_route_unstated")

    def test_a_backfilled_recipe_in_the_ledger_is_replayed(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text"}
        manifest = self.ws.manifest("1", [art])
        ledger = [{"record_kind": "backfill_recipe", "pmid": "1", "artifact_path": art["path"],
                   "recipe": self.ws.recipe("/ok.xml"), "recorded_at": "t"}]
        record = ra.replay_artifact(self.ws.root, manifest, art, ledger)
        self.assertEqual(record["verdict"], ra.RECOVERED)
        self.assertTrue(record["recipe_source"].startswith("retrieval_manifest:"))

    def test_offline_never_recovers_a_fetched_artefact(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        self.assertEqual(self._replay(art, offline=True)["verdict"], "FAILED_OFFLINE")
        self.assertEqual(REQUESTS, [])

    def test_a_recipe_url_carrying_an_address_is_refused_before_any_request(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml?mailto=a@b.c")}
        record = self._replay(art)
        self.assertEqual(record["verdict"], "FAILED_UNSUPPORTED")
        self.assertEqual(REQUESTS, [])

    def test_recovered_bytes_never_overwrite_a_file_with_another_digest(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        local = self.ws.root / art["path"]
        local.parent.mkdir(parents=True)
        local.write_bytes(b"someone else's bytes at this path")
        record = self._replay(art)
        self.assertEqual(record["verdict"], ra.RECOVERED)
        self.assertTrue(record["written"].startswith("refused"))
        self.assertEqual(local.read_bytes(), b"someone else's bytes at this path")

    def test_the_replay_entry_point_records_into_the_versioned_manifest(self):
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        self.ws.manifest("1", [art])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = ra.main(["--workspace", str(self.ws.root), "--actor", "test", "--task", "T",
                          "replay", "--pmid", "1"])
        self.assertEqual(rc, 0)
        self.assertIn("RECOVERED / FAILED / NO_RECIPE / DRIFT_OR_DIFFERS = 1 / 0 / 0 / 0", buf.getvalue())
        lines = ra.read_ledger(ra.retrieval_manifest_path(self.ws.root, "wwox"))
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]["record_kind"], "replay")
        self.assertEqual(lines[0]["verdict"], ra.RECOVERED)
        self.assertEqual(lines[0]["actor"], "test")
        self.assertIn("pymupdf", lines[0]["host_environment"])

    def test_ledger_only_targets_replay_artefacts_no_manifest_declares(self):
        """The 33914858 case: a recipe in the ledger, no deep-dive manifest at all."""
        self.ws.manifest("1", [])
        ra.append_ledger(ra.retrieval_manifest_path(self.ws.root, "wwox"), {
            "record_kind": "backfill_recipe", "pmid": "33914858", "kind": "article_binary",
            "artifact_path": "files/fulltext/PMID33914858.pdf", "declared_sha256": "0" * 64,
            "recipe": self.ws.recipe("/cf.pdf"), "recorded_at": "t"})
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = ra.main(["--workspace", str(self.ws.root), "replay", "--ledger-only", "--no-record"])
        self.assertEqual(rc, 0)
        self.assertIn("FAILED_HTTP_403_CLOUDFLARE", buf.getvalue())
        self.assertIn("PMID 33914858", buf.getvalue())


# --------------------------------------------------------------------------
# derived artefacts and extractor drift

def _fitz():
    try:
        import fitz
    except ImportError:
        return None
    return fitz


class DerivedReplayAndExtractorDrift(unittest.TestCase):
    def setUp(self):
        self.fitz = _fitz()
        if self.fitz is None:
            self.skipTest("PyMuPDF unavailable on this host — the drift verdicts cannot be exercised")
        self.ws = Workspace("http://127.0.0.1:9")
        self.addCleanup(self.ws.cleanup)
        pdf = self.ws.root / "files/fulltext/paper.pdf"
        pdf.parent.mkdir(parents=True)
        doc = self.fitz.open()
        page = doc.new_page()
        page.insert_text((72, 72), "A sentence the text layer will carry.")
        doc.save(str(pdf))
        self.pdf = pdf
        self.text = "".join(p.get_text() for p in self.fitz.open(str(pdf))).encode("utf-8")
        self.host_version = ra.pymupdf_version()

    def _manifest(self, txt_digest, version, join=""):
        arts = [
            {"path": "files/fulltext/paper.pdf", "sha256": ra.sha256_file(self.pdf), "kind": "article_binary"},
            {"path": "files/fulltext/paper.txt", "sha256": txt_digest, "kind": "article_text",
             "acquisition_recipe": {"derived": True, "derived_from": "files/fulltext/paper.pdf",
                                    "acquired_on": "2026-09-09",
                                    "extractor": {"name": "PyMuPDF", "version": version,
                                                  "call": "page.get_text() default mode", "join": join}}},
        ]
        return self.ws.manifest("1", arts), arts[1]

    def test_a_derived_artefact_regenerates_to_its_digest_under_the_same_version(self):
        manifest, art = self._manifest(digest(self.text), self.host_version)
        record = ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)
        self.assertEqual(record["verdict"], ra.RECOVERED)
        self.assertEqual(record["derivation"]["version_host"], self.host_version)

    def test_a_mismatch_under_another_version_is_drift_naming_both_versions(self):
        manifest, art = self._manifest("0" * 64, "1.26.5")
        record = ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)
        self.assertEqual(record["verdict"], ra.EXTRACTOR_DRIFT)
        self.assertEqual(record["drift"]["version_recipe"], "1.26.5")
        self.assertEqual(record["drift"]["version_host"], self.host_version)
        self.assertEqual(record["drift"]["receipt_era_pymupdf"], "1.26.5")
        self.assertNotIn("TAMPERED", json.dumps(record))

    def test_a_mismatch_under_the_same_version_is_not_drift(self):
        manifest, art = self._manifest("0" * 64, self.host_version)
        record = ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)
        self.assertEqual(record["verdict"], ra.DIGEST_DIFFERS_SAME_EXTRACTOR)

    def test_an_absent_source_is_a_named_failure(self):
        manifest, art = self._manifest(digest(self.text), self.host_version)
        self.pdf.unlink()
        record = ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)
        self.assertEqual(record["verdict"], "FAILED_SOURCE_ABSENT")

    def test_a_source_whose_digest_moved_is_a_named_failure(self):
        manifest, art = self._manifest(digest(self.text), self.host_version)
        manifest["source_artifacts"][0]["sha256"] = "f" * 64
        record = ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)
        self.assertEqual(record["verdict"], "FAILED_SOURCE_DIGEST_MISMATCH")

    def test_the_join_is_part_of_the_recipe(self):
        joined = "\n".join(p.get_text() for p in self.fitz.open(str(self.pdf))).encode("utf-8")
        manifest, art = self._manifest(digest(joined), self.host_version, join="\n")
        self.assertEqual(ra.replay_artifact(self.ws.root, manifest, art, [], offline=True)["verdict"],
                         ra.RECOVERED)


# --------------------------------------------------------------------------
# the back-fill: a route the note does not show is not invented

class TheBackfillIsDeclaredlyIncomplete(unittest.TestCase):
    def _art(self, note="", path="files/fulltext/PMID1_PMC.xml", kind="article_text", **extra):
        art = {"path": path, "sha256": "0" * 64, "kind": kind, "note": note}
        art.update(extra)
        return art

    def test_an_efetch_note_with_a_pmcid_yields_the_determined_url(self):
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                            self._art("Structured JATS XML from NCBI E-utilities efetch (db=pmc, id=PMC3037996), retrieved 2026-09-09."))
        self.assertEqual(reason, "route_shown")
        self.assertEqual(recipe["tier"], ra.TIER_EFETCH)
        self.assertTrue(recipe["resolved_url"].endswith("db=pmc&id=3037996"))
        self.assertEqual(recipe["acquired_on"], "2026-09-09")
        self.assertEqual(recipe["user_agent_policy"], "none")

    def test_a_europe_pmc_404_narration_is_not_a_europe_pmc_route(self):
        note = ("Europe PMC's fullTextXML endpoint returns HTTP 404 for PMC2832309 — but NCBI efetch "
                "db=pmc returns the COMPLETE deposit.")
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []}, self._art(note))
        self.assertEqual(reason, "route_shown")
        self.assertEqual(recipe["tier"], ra.TIER_EFETCH)

    def test_a_pmcid_alone_is_not_a_route(self):
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                            self._art("PMC deposit PMC1266103, 6 pages.", path="files/fulltext/x.pdf", kind="article_binary"))
        self.assertIsNone(recipe)
        self.assertEqual(reason, "pmcid_only_route_unstated")

    def test_pow_fetch_without_a_url_on_a_supplement_is_not_invented(self):
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                            self._art("Supplement, 24 pages, retrieved 2026-09-09 through framework/scripts/pmc_pow_fetch.py from the PMC instance binary route.",
                                                      path="files/fulltext/PMID1_supplement1.pdf", kind="article_binary"))
        self.assertIsNone(recipe)
        self.assertEqual(reason, "pow_route_named_url_not_recorded")

    def test_pow_fetch_of_the_article_pdf_from_pmc_is_labelled_url_form_inferred(self):
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                            self._art("7-page publisher PDF obtained from PMC (PMC11159152) on 2026-09-09 via framework/scripts/pmc_pow_fetch.py.",
                                                      path="files/fulltext/PMID1_PMC.pdf", kind="article_binary"))
        self.assertEqual(reason, "route_shown")
        self.assertEqual(recipe["tier"], ra.TIER_PMC_POW)
        self.assertEqual(recipe["recipe_confidence"], "route_named_url_form_inferred")

    def test_a_quoted_cdn_route_is_taken_verbatim(self):
        recipe, reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                            self._art("", path="files/figures/PMID1/f1.jpg", kind="figure",
                                                      route="cdn.ncbi.nlm.nih.gov/pmc/blobs/aec4/3412936/85a4/f1.jpg — URL embedded in the article HTML already held"))
        self.assertEqual(recipe["tier"], ra.TIER_PMC_BLOB)
        self.assertEqual(recipe["resolved_url"], "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aec4/3412936/85a4/f1.jpg")

    def test_a_derived_text_needs_its_join_stated(self):
        manifest = {"pmid": "1", "source_artifacts": [{"path": "files/fulltext/PMID1_Aqeilan2026.pdf", "kind": "article_binary", "sha256": "1" * 64}]}
        art = self._art("Deterministic extraction with PyMuPDF get_text() over all 7 pages, no layout mode.",
                        path="files/fulltext/PMID1_Aqeilan2026_fitz.txt")
        recipe, reason, _ = ra.infer_recipe(manifest, art)
        self.assertIsNone(recipe)
        self.assertEqual(reason, "derived_join_unstated")
        art = self._art("PyMuPDF 1.26.5, page.get_text() default mode, ''.join(pages), no separator.",
                        path="files/fulltext/PMID1_Aqeilan2026_fitz.txt")
        recipe, reason, _ = ra.infer_recipe(manifest, art)
        self.assertEqual(reason, "route_shown")
        self.assertEqual(recipe["extractor"]["version"], "1.26.5")
        self.assertEqual(recipe["extractor"]["join"], "")

    def test_a_note_carrying_an_address_never_becomes_a_url(self):
        recipe, _reason, _ = ra.infer_recipe({"pmid": "1", "source_artifacts": []},
                                             self._art("fetched from https://api.unpaywall.org/v2/x?email=a@b.c today"))
        self.assertIsNone(recipe)

    def test_the_real_corpus_backfill_shows_a_route_for_a_minority_and_invents_none(self):
        """Read-only over the real manifests: the ratio is reported, never padded."""
        manifests = ra.load_manifests(ROOT, "wwox")
        if not manifests:
            self.skipTest("no deep-dive manifests in this checkout")
        shown = total = 0
        for manifest in manifests:
            for artifact in ra.artifacts_of(manifest):
                total += 1
                recipe, reason, _ = ra.infer_recipe(manifest, artifact)
                if recipe:
                    shown += 1
                    self.assertTrue(recipe.get("derived") or ra.RECIPE_URL_RE.fullmatch(recipe["resolved_url"]),
                                    recipe)
                else:
                    self.assertTrue(reason)
        self.assertGreater(total, 0)
        self.assertLess(shown, total // 2, "a majority of notes cannot show a route; check the inference")
        self.assertGreater(shown, 0)


class TheVersionedLedgerAndTheRealCorpus(unittest.TestCase):
    def test_append_only(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "retrieval_manifest.jsonl"
            ra.append_ledger(path, {"a": 1})
            first = path.read_text(encoding="utf-8")
            ra.append_ledger(path, {"b": 2})
            self.assertTrue(path.read_text(encoding="utf-8").startswith(first))
            self.assertEqual(len(ra.read_ledger(path)), 2)

    def test_the_versioned_home_is_tracked_and_not_under_files(self):
        rel = ra.RETRIEVAL_MANIFEST.format(disease="wwox")
        self.assertFalse(rel.startswith("files/"))
        self.assertTrue(rel.startswith("disease-models/"))

    def test_record_refuses_an_address_in_the_url(self):
        with TemporaryDirectory() as tmp:
            payload = Path(tmp) / "p.json"
            payload.write_text(json.dumps({"pmid": "1", "artifact_path": "files/x.pdf",
                                           "recipe": {"resolved_url": "https://x/?email=a@b.c"}}))
            err = io.StringIO()
            from contextlib import redirect_stderr
            with redirect_stderr(err):
                rc = ra.main(["--workspace", tmp, "record", "--json", str(payload)])
            self.assertEqual(rc, 2)
            self.assertFalse((Path(tmp) / ra.RETRIEVAL_MANIFEST.format(disease="wwox")).exists())

    def test_status_runs_over_the_real_corpus_and_reads_only(self):
        """Calls main() on the real root. The ratchet line is asserted, nothing is written."""
        ledger = ra.retrieval_manifest_path(ROOT, "wwox")
        before = ledger.read_bytes() if ledger.is_file() else None
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = ra.main(["--workspace", str(ROOT), "status"])
        self.assertEqual(rc, 0)
        self.assertIn("replayable", buf.getvalue())
        self.assertIn("declared artefacts", buf.getvalue())
        after = ledger.read_bytes() if ledger.is_file() else None
        self.assertEqual(before, after, "status wrote the retrieval manifest")

    def test_the_selftest_entry_point_passes_on_the_real_corpus(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = ra.main(["--workspace", str(ROOT), "selftest"])
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn("SELFTEST: PASS", buf.getvalue())

    def test_the_docstring_declares_the_verdicts_and_the_determinism_risk(self):
        doc = ra.__doc__
        for word in ("RECOVERED", "EXTRACTOR_DRIFT", "DIGEST_DIFFERS_SAME_ROUTE", "NO_RECIPE",
                     "1.26.5", "1.28.2", "NOT `TAMPERED`", "NO EMAIL ADDRESS"):
            self.assertIn(word, doc)


# --------------------------------------------------------------------------
# the mutation battery

class MutationBattery(unittest.TestCase):
    """Each mutation breaks one named invariant; each must be caught here."""

    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Publisher)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = "http://127.0.0.1:%d" % cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        self.ws = Workspace(self.base)
        self.addCleanup(self.ws.cleanup)
        REQUESTS.clear()

    def _both(self, mut, artifact, **kw):
        manifest = self.ws.manifest("1", [artifact])
        live = ra.replay_artifact(self.ws.root, manifest, artifact, [], write=False, **kw)
        mutant = mut.replay_artifact(self.ws.root, manifest, artifact, [], write=False, **kw)
        return live, mutant

    # --- M1
    def test_mutation_recovering_on_a_digest_mismatch_is_caught(self):
        mut = load_mutated(("    elif observed == declared:\n        record[\"verdict\"] = RECOVERED\n    else:\n        record[\"verdict\"] = DIGEST_DIFFERS_SAME_ROUTE",
                            "    elif True:\n        record[\"verdict\"] = RECOVERED\n    else:\n        record[\"verdict\"] = DIGEST_DIFFERS_SAME_ROUTE"))
        live, mutant = self._both(mut, {"path": "files/fulltext/p.pdf", "sha256": "0" * 64, "kind": "article_binary",
                                        "acquisition_recipe": self.ws.recipe("/changed.pdf")})
        self.assertEqual(mutant["verdict"], ra.RECOVERED)
        self.assertEqual(live["verdict"], ra.DIGEST_DIFFERS_SAME_ROUTE)

    # --- M2
    def test_mutation_dropping_the_cloudflare_cause_is_caught(self):
        mut = load_mutated(('    return "cf-ray" in headers or headers.get("server", "").lower().startswith("cloudflare")',
                            '    return False'))
        live, mutant = self._both(mut, {"path": "files/fulltext/p.pdf", "sha256": "0" * 64, "kind": "article_binary",
                                        "acquisition_recipe": self.ws.recipe("/cf.pdf")})
        self.assertEqual(mutant["verdict"], "FAILED_HTTP_403")
        self.assertEqual(live["verdict"], "FAILED_HTTP_403_CLOUDFLARE")

    # --- M3
    def test_mutation_blind_to_a_recaptcha_is_caught(self):
        mut = load_mutated(('    return b"recaptcha" in head or b"g-recaptcha" in head', '    return False'))
        live, mutant = self._both(mut, {"path": "files/figures/f.jpg", "sha256": "0" * 64, "kind": "figure",
                                        "acquisition_recipe": self.ws.recipe("/captcha.jpg")})
        self.assertNotEqual(mutant["verdict"], "FAILED_RECAPTCHA")
        self.assertEqual(live["verdict"], "FAILED_RECAPTCHA")

    # --- M4
    def test_mutation_labelling_a_publisher_change_tampered_is_caught(self):
        mut = load_mutated(('        record["verdict"] = DIGEST_DIFFERS_SAME_ROUTE\n        record["finding"]',
                            '        record["verdict"] = "TAMPERED"\n        record["finding"]'))
        live, mutant = self._both(mut, {"path": "files/fulltext/p.pdf", "sha256": "0" * 64, "kind": "article_binary",
                                        "acquisition_recipe": self.ws.recipe("/changed.pdf")})
        self.assertEqual(mutant["verdict"], "TAMPERED")
        self.assertEqual(live["verdict"], ra.DIGEST_DIFFERS_SAME_ROUTE)

    # --- M5
    def test_mutation_sending_a_user_agent_under_the_none_policy_is_caught(self):
        mut = load_mutated(('        opener.addheaders = []            # urllib would otherwise send Python-urllib/x.y',
                            '        opener.addheaders = [("User-Agent", UA_BROWSER_LIKE)]'))
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        manifest = self.ws.manifest("1", [art])
        mut.replay_artifact(self.ws.root, manifest, art, [], write=False)
        self.assertIn("user-agent", REQUESTS[-1]["headers"])
        ra.replay_artifact(self.ws.root, manifest, art, [], write=False)
        self.assertNotIn("user-agent", REQUESTS[-1]["headers"])

    # --- M6
    def test_mutation_turning_no_recipe_into_a_failure_is_caught(self):
        mut = load_mutated(('        record.update(verdict=NO_RECIPE, no_recipe_reason=no_reason)',
                            '        record.update(verdict=failed("UNSUPPORTED"), no_recipe_reason=no_reason)'))
        live, mutant = self._both(mut, {"path": "files/fulltext/p.pdf", "sha256": "0" * 64, "kind": "article_binary"})
        self.assertNotEqual(mutant["verdict"], ra.NO_RECIPE)
        self.assertEqual(live["verdict"], ra.NO_RECIPE)

    # --- M7
    def test_mutation_overwriting_a_foreign_file_is_caught(self):
        mut = load_mutated(('        record["written"] = "refused: a file with a different digest already sits at the path"\n        return',
                            '        local.write_bytes(data)\n        record["written"] = "written"\n        return'))
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml")}
        manifest = self.ws.manifest("1", [art])
        local = self.ws.root / art["path"]
        local.parent.mkdir(parents=True)
        local.write_bytes(b"foreign")
        ra.replay_artifact(self.ws.root, manifest, art, [])
        self.assertEqual(local.read_bytes(), b"foreign")
        mut.replay_artifact(self.ws.root, manifest, art, [])
        self.assertEqual(local.read_bytes(), OK_XML)

    # --- M8
    def test_mutation_admitting_an_address_in_the_url_is_caught(self):
        mut = load_mutated(('RECIPE_URL_RE = re.compile(r"^https?://[^\\s@]+$")',
                            'RECIPE_URL_RE = re.compile(r"^https?://\\S+$")'))
        art = {"path": "files/fulltext/ok.xml", "sha256": digest(OK_XML), "kind": "article_text",
               "acquisition_recipe": self.ws.recipe("/ok.xml?mailto=a@b.c")}
        manifest = self.ws.manifest("1", [art])
        live = ra.replay_artifact(self.ws.root, manifest, art, [], write=False)
        self.assertEqual(live["verdict"], "FAILED_UNSUPPORTED")
        self.assertEqual(REQUESTS, [], "the live tool put an address on the wire")
        mut.replay_artifact(self.ws.root, manifest, art, [], write=False)
        self.assertEqual(len(REQUESTS), 1)                      # the mutant sent it
        self.assertIn("mailto=a@b.c", REQUESTS[-1]["path"])

    # --- M9
    def test_mutation_collapsing_drift_into_same_extractor_is_caught(self):
        if _fitz() is None:
            self.skipTest("PyMuPDF unavailable")
        mut = load_mutated(("            if v_recipe != v_host:\n                record[\"verdict\"] = EXTRACTOR_DRIFT",
                            "            if False:\n                record[\"verdict\"] = EXTRACTOR_DRIFT"))
        case = DerivedReplayAndExtractorDrift("test_a_mismatch_under_another_version_is_drift_naming_both_versions")
        case.setUp()
        manifest, art = case._manifest("0" * 64, "1.26.5")
        self.assertEqual(ra.replay_artifact(case.ws.root, manifest, art, [], offline=True)["verdict"], ra.EXTRACTOR_DRIFT)
        self.assertEqual(mut.replay_artifact(case.ws.root, manifest, art, [], offline=True)["verdict"], ra.DIGEST_DIFFERS_SAME_EXTRACTOR)
        case.ws.cleanup()

    # --- M10
    def test_mutation_dropping_the_host_version_from_the_drift_record_is_caught(self):
        if _fitz() is None:
            self.skipTest("PyMuPDF unavailable")
        mut = load_mutated(('                                   "version_recipe": v_recipe, "version_host": v_host,',
                            '                                   "version_recipe": v_recipe, "version_host": None,'))
        case = DerivedReplayAndExtractorDrift("test_a_mismatch_under_another_version_is_drift_naming_both_versions")
        case.setUp()
        manifest, art = case._manifest("0" * 64, "1.26.5")
        self.assertIsNone(mut.replay_artifact(case.ws.root, manifest, art, [], offline=True)["drift"]["version_host"])
        self.assertEqual(ra.replay_artifact(case.ws.root, manifest, art, [], offline=True)["drift"]["version_host"], ra.pymupdf_version())
        case.ws.cleanup()

    # --- M11
    def test_mutation_inventing_a_route_from_a_bare_pmcid_is_caught(self):
        mut = load_mutated(('    if pmc_num:\n        return None, "pmcid_only_route_unstated", blob[:200]',
                            '    if pmc_num:\n        return fetch(TIER_PMC_POW, "https://pmc.ncbi.nlm.nih.gov/articles/PMC%s/pdf/" % pmc_num, "identified", "invented", blob[:200])'))
        art = {"path": "files/fulltext/x.pdf", "sha256": "0" * 64, "kind": "article_binary",
               "note": "PMC deposit PMC1266103, 6 pages."}
        self.assertIsNotNone(mut.infer_recipe({"pmid": "1", "source_artifacts": []}, art)[0])
        self.assertIsNone(ra.infer_recipe({"pmid": "1", "source_artifacts": []}, art)[0])

    # --- M12
    def test_mutation_truncating_the_ledger_is_caught(self):
        mut = load_mutated(('    with path.open("a", encoding="utf-8") as fh:', '    with path.open("w", encoding="utf-8") as fh:'))
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            mut.append_ledger(path, {"a": 1})
            mut.append_ledger(path, {"b": 2})
            self.assertEqual(len(mut.read_ledger(path)), 1)
            ra.append_ledger(path, {"c": 3})
            self.assertEqual(len(ra.read_ledger(path)), 2)

    def test_the_battery_is_exhaustive_over_the_named_invariants(self):
        invariants = {
            "mismatch_is_never_recovered", "cloudflare_is_named", "recaptcha_is_named",
            "publisher_change_is_not_tampered", "none_policy_sends_no_agent",
            "no_recipe_is_a_verdict", "never_overwrite_foreign_bytes", "no_address_on_the_wire",
            "drift_is_named_by_version", "drift_names_the_host_version",
            "no_route_is_invented", "ledger_is_append_only",
        }
        mutation_tests = {n for n in dir(self) if n.startswith("test_mutation_")}
        self.assertEqual(len(mutation_tests), len(invariants),
                         "%d mutations for %d named invariants" % (len(mutation_tests), len(invariants)))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
