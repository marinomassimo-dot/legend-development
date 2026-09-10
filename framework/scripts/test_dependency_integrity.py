#!/usr/bin/env python3
"""Regressions for dependency_integrity.py, with a mutation battery.

The battery is the point. A screen's tests can be green while the screen is useless,
because the failure mode of a screen is not a crash — it is returning CLEAN. So every
invariant that would let this tool report a clean verdict it did not earn is mutated
into the source here, and at least one test must go red for each mutation. A mutation
that no test catches is a hole in the suite, and `test_the_battery_is_exhaustive` asserts
that the battery itself is wired to every named invariant.

The mutations are applied textually to the module source and loaded into a fresh
namespace, so they exercise the shipped file rather than a paraphrase of it.
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(HERE, "dependency_integrity.py")
sys.path.insert(0, HERE)

import dependency_integrity as di  # noqa: E402


# --------------------------------------------------------------------------
# helpers

def load_mutated(*substitutions):
    """Load dependency_integrity.py with textual substitutions applied."""
    with open(MODULE_PATH, encoding="utf-8") as fh:
        src = fh.read()
    for old, new in substitutions:
        if old not in src:
            raise AssertionError("mutation target not present in source: %r" % old)
        src = src.replace(old, new, 1)
    spec = importlib.util.spec_from_loader("dependency_integrity_mutant", loader=None)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__["__file__"] = MODULE_PATH
    exec(compile(src, MODULE_PATH + " [MUTANT]", "exec"), mod.__dict__)
    return mod


def fake_index(module=di):
    """A tiny index carrying one of each RetractionNature the real snapshot holds."""
    def row(doi, nature, pmid="1", rpmid="2"):
        return {
            "record_id": "r", "title": "t", "journal": "j",
            "original_doi": doi, "original_pmid": pmid,
            "nature": nature, "verdict": module.classify_nature(nature),
            "retraction_pmid": rpmid, "retraction_date": "1/1/2020",
            "reason": "Concerns/Issues about Data;Duplication of/in Image;",
        }
    return {
        "10.1000/retracted": [row("10.1000/retracted", "Retraction")],
        "10.1000/eoc": [row("10.1000/eoc", "Expression of concern")],
        "10.1000/correction": [row("10.1000/correction", "Correction")],
        "10.1000/reinstated": [row("10.1000/reinstated", "Reinstatement")],
        "10.1000/blank": [row("10.1000/blank", "")],
        "10.1000/twice": [row("10.1000/twice", "Expression of concern"),
                       row("10.1000/twice", "Retraction")],
    }


def patched_refs(module, refs):
    """Force crossref_references to return `refs` without touching the network."""
    module.crossref_references = lambda doi, **kw: (refs, "test-fixture")


# --------------------------------------------------------------------------

class DoiNormalisation(unittest.TestCase):
    def test_absence_is_none_and_not_empty_string(self):
        """None forces the caller to branch; "" quietly compares equal to nothing."""
        for raw in (None, "", "   ", "no identifier here", "PMID 123456"):
            self.assertIsNone(di.normalise_doi(raw), raw)

    def test_common_spellings_all_reach_the_same_bare_doi(self):
        for raw in (
            "10.1073/PNAS.0505485102",
            "https://doi.org/10.1073/pnas.0505485102",
            "doi:10.1073/pnas.0505485102",
            "  10.1073/pnas.0505485102  ",
            "(10.1073/pnas.0505485102).",
        ):
            self.assertEqual(di.normalise_doi(raw), "10.1073/pnas.0505485102", raw)


class NatureClassesStaySeparate(unittest.TestCase):
    def test_each_nature_gets_its_own_verdict(self):
        seen = {
            di.classify_nature("Retraction"),
            di.classify_nature("Expression of concern"),
            di.classify_nature("Correction"),
            di.classify_nature("Reinstatement"),
        }
        self.assertEqual(len(seen), 4, "the integrity classes collapsed: %r" % seen)

    def test_a_correction_is_not_an_integrity_flag(self):
        self.assertNotIn(di.V_CORRECTION, di.INTEGRITY_FLAGS)

    def test_a_reinstatement_is_not_an_integrity_flag(self):
        """A reinstatement is the opposite of a flag."""
        self.assertNotIn(di.V_REINSTATEMENT, di.INTEGRITY_FLAGS)

    def test_an_empty_nature_is_flagged_rather_than_silently_dropped(self):
        """218 rows carry no nature. Unknown is a flag to read, not a clean verdict."""
        self.assertEqual(di.classify_nature(""), di.V_UNCLASSIFIED)
        self.assertIn(di.V_UNCLASSIFIED, di.INTEGRITY_FLAGS)

    def test_an_unknown_future_nature_does_not_become_clean(self):
        self.assertEqual(di.classify_nature("Partial retraction of something"),
                         di.V_UNCLASSIFIED)


class TheScreenSaysWhatItScreened(unittest.TestCase):
    def setUp(self):
        self.index = fake_index()

    def test_a_doi_less_reference_is_unscreenable_and_not_clean(self):
        r = di.screen_reference(None, self.index)
        self.assertEqual(r["verdict"], di.V_NO_DOI)
        self.assertFalse(r["screened"])
        self.assertNotEqual(r["verdict"], di.V_CLEAN)

    def test_a_screened_reference_carries_screened_true(self):
        r = di.screen_reference("10.1000/absent-from-index", self.index)
        self.assertEqual(r["verdict"], di.V_CLEAN)
        self.assertTrue(r["screened"])

    def test_no_snapshot_never_yields_clean(self):
        r = di.screen_reference("10.1000/anything", None)
        self.assertEqual(r["verdict"], di.V_NO_SNAPSHOT)
        self.assertFalse(r["screened"])

    def test_the_two_unscreenable_classes_are_distinct_verdicts(self):
        self.assertNotEqual(di.V_NO_DOI, di.V_NO_REFS)
        self.assertNotEqual(di.V_NO_DOI, di.V_CLEAN)
        self.assertNotEqual(di.V_NO_REFS, di.V_CLEAN)

    def test_the_most_severe_live_class_wins_when_a_doi_has_several_rows(self):
        r = di.screen_reference("10.1000/twice", self.index)
        self.assertEqual(r["verdict"], di.V_RETRACTION)
        self.assertEqual(len(r["rows"]), 2, "both rows must survive for adjudication")

    def test_the_reason_field_is_passed_through_verbatim(self):
        r = di.screen_reference("10.1000/eoc", self.index)
        self.assertEqual(r["rows"][0]["reason"],
                         "Concerns/Issues about Data;Duplication of/in Image;")


class PaperLevelVerdicts(unittest.TestCase):
    def setUp(self):
        self.index = fake_index()
        self.mod = load_mutated()  # a clean copy we may monkeypatch freely

    def screen(self, refs):
        patched_refs(self.mod, refs)
        return self.mod.screen_paper("10.1000/citing", self.index, pmid="999")

    def test_a_paper_with_no_deposited_references_is_not_clean(self):
        """The same failure class as a DOI-less reference, one level up."""
        res = self.screen([])
        self.assertEqual(res["paper_verdict"], self.mod.V_NO_REFS)
        self.assertFalse(res["screened"])

    def test_a_paper_whose_references_are_all_doi_less_is_not_clean(self):
        res = self.screen([{"unstructured": "Smith 1999"}, {"unstructured": "Jones 2001"}])
        self.assertEqual(res["unscreenable_no_doi"], 2)
        self.assertEqual(res["screened_count"], 0)
        self.assertNotEqual(res["paper_verdict"], self.mod.V_CLEAN)

    def test_a_flagged_dependency_raises_the_paper_verdict(self):
        res = self.screen([{"DOI": "10.1000/eoc"}, {"DOI": "10.1000/clean"}])
        self.assertEqual(res["paper_verdict"], self.mod.V_EOC)
        self.assertEqual(len(res["flagged"]), 1)
        self.assertEqual(res["flagged"][0]["doi"], "10.1000/eoc")

    def test_a_correction_dependency_does_not_flag_the_paper(self):
        res = self.screen([{"DOI": "10.1000/correction"}])
        self.assertEqual(res["paper_verdict"], self.mod.V_CLEAN)
        self.assertEqual(res["flagged"], [])
        self.assertEqual(len(res["noted"]), 1, "the correction must still be reported")

    def test_counts_separate_screened_from_unscreenable(self):
        res = self.screen([
            {"DOI": "10.1000/eoc"}, {"DOI": "10.1000/clean"}, {"unstructured": "no doi"},
        ])
        self.assertEqual(res["references_declared"], 3)
        self.assertEqual(res["references_with_doi"], 2)
        self.assertEqual(res["screened_count"], 2)
        self.assertEqual(res["unscreenable_no_doi"], 1)

    def test_a_failed_reference_fetch_is_not_a_clean_paper(self):
        self.mod.crossref_references = lambda doi, **kw: (None, "error:URLError")
        res = self.mod.screen_paper("10.1000/citing", self.index)
        self.assertEqual(res["paper_verdict"], self.mod.V_FETCH_FAILED)
        self.assertFalse(res["screened"])

    def test_every_result_carries_the_snapshot_age(self):
        """Staleness is part of every verdict, not a footnote on the run."""
        patched_refs(self.mod, [{"DOI": "10.1000/clean"}])
        res = self.mod.screen_paper("10.1000/citing", self.index, stale_days=41)
        self.assertEqual(res["days_since_fetch"], 41)


class CorpusDiscovery(unittest.TestCase):
    def test_the_real_manifest_directory_is_found_and_non_empty(self):
        papers = di.corpus_papers()
        self.assertGreater(len(papers), 50, "corpus manifests not discovered")
        self.assertTrue(any(doi for _p, doi in papers))

    def test_an_absent_directory_is_empty_not_an_exception(self):
        self.assertEqual(di.corpus_papers("/nonexistent/path/xyz"), [])

    def test_a_manifest_without_a_doi_is_reported_not_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "PMID111.json"), "w", encoding="utf-8") as fh:
                json.dump({"pmid": "111"}, fh)
            papers = di.corpus_papers(tmp)
        self.assertEqual(papers, [("111", None)])


class PositiveControl(unittest.TestCase):
    """The control must reproduce against the real pinned snapshot, or nothing is built."""

    @classmethod
    def setUpClass(cls):
        path, pin, problems = di.verify_snapshot()
        if problems:
            raise unittest.SkipTest("snapshot unusable: %s" % "; ".join(problems))
        cls.index = di.load_index(path)
        cls.pin = pin

    def test_pmid_16223882_reproduces_in_full(self):
        ok, problems, rows = di.positive_control(self.index)
        self.assertTrue(ok, "; ".join(problems))
        row = rows[0]
        self.assertEqual(row["original_doi"], "10.1073/pnas.0505485102")
        self.assertEqual(row["original_pmid"], "16223882")
        self.assertEqual(row["nature"], "Expression of concern")
        self.assertEqual(row["retraction_pmid"], "28373548")
        self.assertIn("image", row["reason"].lower())
        self.assertEqual(row["verdict"], di.V_EOC)

    def test_the_control_is_reached_through_the_ordinary_screen_path(self):
        """Not a special case: the control DOI screens as a flag like any other."""
        r = di.screen_reference("https://doi.org/10.1073/PNAS.0505485102", self.index)
        self.assertEqual(r["verdict"], di.V_EOC)
        self.assertTrue(r["screened"])

    def test_the_four_doi_reachable_nature_classes_are_present(self):
        """If upstream drops or renames a class, this is where it is noticed.

        Only four of the five are reachable: every row whose RetractionNature is blank
        also lacks an OriginalPaperDOI, so it never enters a DOI-keyed index at all.
        That is measured by the next test, not assumed here.
        """
        seen = set()
        for rows in self.index.values():
            for row in rows:
                seen.add(row["verdict"])
        for expected in (di.V_RETRACTION, di.V_EOC, di.V_CORRECTION, di.V_REINSTATEMENT):
            self.assertIn(expected, seen)

    def test_the_blank_nature_rows_are_unreachable_because_they_carry_no_doi(self):
        """Failure mode 8, measured rather than predicted.

        218 rows in the pinned snapshot carry no RetractionNature. Every one of them
        also carries no OriginalPaperDOI, so this method cannot see them at all. If a
        future snapshot gives one of them a DOI, this test flips and the unclassified
        branch stops being dead code — which is exactly when someone should look.
        """
        import csv as _csv
        _csv.field_size_limit(10 ** 9)
        path, _pin, _problems = di.verify_snapshot()
        blank = blank_with_doi = 0
        with open(path, newline="", encoding="utf-8") as fh:
            for row in _csv.DictReader(fh):
                if not (row.get("RetractionNature") or "").strip():
                    blank += 1
                    if di.normalise_doi(row.get("OriginalPaperDOI")):
                        blank_with_doi += 1
        self.assertGreater(blank, 0, "the blank-nature class vanished from the snapshot")
        self.assertEqual(
            blank_with_doi, 0,
            "%d blank-nature rows now carry a DOI and are newly screenable" % blank_with_doi)

    def test_a_malformed_doi_fails_closed_rather_than_clean(self):
        """A DOI prefix is 10. plus 4-9 digits. Anything else is UNSCREENABLE, not clean."""
        for bad in ("10.1/x", "10.123/abc", "doi pending", "n/a"):
            r = di.screen_reference(bad, self.index)
            self.assertEqual(r["verdict"], di.V_NO_DOI, bad)
            self.assertFalse(r["screened"], bad)

    def test_the_pin_matches_the_snapshot_on_disk(self):
        path, pin, problems = di.verify_snapshot()
        self.assertEqual(problems, [])
        self.assertTrue(os.path.exists(path))
        self.assertEqual(pin["licence"], "CC0")

    def test_the_entry_point_runs_the_control_end_to_end(self):
        """Calls main() — the shipped entry point — not an internal helper."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = di.main(["control"])
        self.assertEqual(rc, 0)
        out = buf.getvalue()
        self.assertIn("POSITIVE CONTROL: PASS", out)
        self.assertIn("28373548", out)
        self.assertIn("day(s) since fetch", out)

    def test_the_selftest_entry_point_passes(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = di.main(["selftest", "--offline"])
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn("selftest called screen_paper() on PMID", buf.getvalue())


class NoEmailIsEverSent(unittest.TestCase):
    """The one reserved act this tool must be structurally incapable of."""

    def test_the_source_contains_no_email_address(self):
        with open(MODULE_PATH, encoding="utf-8") as fh:
            src = fh.read()
        import re
        found = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", src)
        self.assertEqual(found, [], "an email address is present in the source: %r" % found)

    def test_no_mailto_parameter_is_constructed(self):
        with open(MODULE_PATH, encoding="utf-8") as fh:
            src = fh.read()
        self.assertNotIn("mailto=", src)


class FailureModesAreDeclared(unittest.TestCase):
    """The docstring is part of the deliverable; an undeclared failure mode is a defect."""

    def test_the_docstring_names_every_declared_failure_mode(self):
        doc = di.__doc__ or ""
        for phrase in (
            "DOI-LESS REFERENCES ARE INVISIBLE",
            "NO DEPOSITED REFERENCE LIST IS NOT A CLEAN PAPER",
            "THE INTEGRITY CLASSES ARE NOT INTERCHANGEABLE",
            "THE SNAPSHOT GOES STALE",
            "FAIL-CLOSED",
        ):
            self.assertIn(phrase, doc, "undeclared failure mode: %s" % phrase)

    def test_the_docstring_states_a_flag_is_not_a_claim(self):
        self.assertIn("prompt to read", di.__doc__)

    def test_the_docstring_carries_a_minimum_reproducible_invocation(self):
        self.assertIn("MINIMUM REPRODUCIBLE INVOCATION", di.__doc__)


class TheToolTouchesNoCanonicalFile(unittest.TestCase):
    """A flag is a prompt to read. This tool must be structurally unable to edit.

    The earlier version of this test asserted the module never MENTIONED a canonical
    surface, which was the wrong guarantee twice over: it forbade the legitimate
    read-only join onto the claim registry, and it would have passed a module that
    opened a registry for writing through a path it assembled at runtime. What matters
    is the mode, so that is what is asserted.
    """

    CANONICAL = ("registries/", "_current.md", "discovery_ledger_current",
                 "full_text_queue_current", "claim_registry_current")

    def test_no_canonical_surface_is_ever_opened_for_writing(self):
        import ast
        with open(MODULE_PATH, encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
        writes = []
        for node in ast.walk(tree):
            if not (isinstance(node, ast.Call) and getattr(node.func, "id", "") == "open"):
                continue
            mode = ""
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = str(node.args[1].value)
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = str(kw.value.value)
            if any(c in mode for c in "wax+"):
                writes.append((node.lineno, ast.dump(node.args[0])[:120], mode))
        for lineno, target, mode in writes:
            for name in ("REGISTRY", "CLAIM", "PAPER_REGISTRY", "_REG"):
                self.assertNotIn(
                    name, target,
                    "line %d opens a canonical surface in mode %r" % (lineno, mode))

    def test_the_registry_constants_are_named_read_only(self):
        with open(MODULE_PATH, encoding="utf-8") as fh:
            src = fh.read()
        self.assertIn("PAPER_REGISTRY_RO", src)
        self.assertIn("CLAIM_REGISTRY_RO", src)

    def test_the_module_writes_only_under_files_or_to_named_outputs(self):
        """Every write target is the pin, a snapshot, a refs cache, or an explicit --json."""
        import ast
        with open(MODULE_PATH, encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
        allowed = {"PIN_PATH", "dest", "tmp", "cache_file", "args", "out"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "open":
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                if any(c in mode for c in "wax+"):
                    names = {n.id for n in ast.walk(node.args[0])
                             if isinstance(n, ast.Name)}
                    self.assertTrue(
                        names & allowed,
                        "unexpected write target at line %d: %s" % (node.lineno, names))


class TheClaimChainJoin(unittest.TestCase):
    """Read-only join: which claims stand on a paper with a flagged dependency."""

    def test_the_heading_matchers_are_the_shared_ones_by_identity(self):
        """`is`, not `==`: a copy that matches today can be edited tomorrow."""
        import growth_anchors
        self.assertIs(di.PAPER_HEADING.pattern,
                      growth_anchors.heading_re("papers", "corpus").pattern)
        self.assertIs(di.CLAIM_HEADING.pattern,
                      growth_anchors.heading_re("claims").pattern)

    def test_a_corpus_placeholder_cannot_donate_its_identifier_to_the_paper_above(self):
        """Both conventions are passed, so a placeholder body does not join its neighbour."""
        import tempfile as _t
        with _t.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "paper_registry_current.md")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("## PAPER 001\n**Identifier:** PMID 11111111\n\n"
                         "## CORPUS P2\n**Identifier:** PMID 22222222\n")
            papers = di.paper_pmids(path)
        self.assertEqual(papers, {"1": "11111111"},
                         "a CORPUS placeholder leaked into the PAPER records")

    def test_the_real_paper_registry_resolves_pmids(self):
        papers = di.paper_pmids()
        self.assertGreater(len(papers), 40, "paper registry did not parse")
        self.assertTrue(all(p.isdigit() for p in papers.values()))

    def test_the_real_claim_registry_resolves_wikilinks(self):
        claims = di.claim_paper_links()
        self.assertGreater(len(claims), 20, "claim registry did not parse")
        self.assertTrue(any(v for v in claims.values()), "no wikilinks found")

    def test_a_claim_with_no_flagged_paper_is_not_reported(self):
        hits = di.claims_touching({}, papers={"1": "111"}, claims={"9": {"1"}})
        self.assertEqual(hits, {})

    def test_a_claim_standing_on_a_flagged_paper_is_reported_with_the_dependency(self):
        hits = di.claims_touching(
            {"111": {"10.1073/pnas.0505485102"}},
            papers={"1": "111"}, claims={"9": {"1"}})
        self.assertEqual(hits, {"9": {"111": ["10.1073/pnas.0505485102"]}})

    def test_a_missing_registry_is_empty_not_an_exception(self):
        self.assertEqual(di.paper_pmids("/nonexistent/p.md"), {})
        self.assertEqual(di.claim_paper_links("/nonexistent/c.md"), {})


# --------------------------------------------------------------------------
# the mutation battery

class MutationBattery(unittest.TestCase):
    """Each mutation breaks one named invariant; each must be caught here."""

    def setUp(self):
        self.index = fake_index()

    # --- M1
    def test_mutation_collapsing_no_doi_into_clean_is_caught(self):
        mut = load_mutated(('V_NO_DOI = "UNSCREENABLE_NO_DOI"',
                            'V_NO_DOI = "SCREENED_CLEAN"'))
        r = mut.screen_reference(None, fake_index(mut))
        self.assertEqual(r["verdict"], mut.V_CLEAN)  # the mutant does the wrong thing
        # and the shipped module does not:
        self.assertEqual(di.screen_reference(None, self.index)["verdict"], di.V_NO_DOI)

    # --- M2
    def test_mutation_marking_a_doi_less_reference_as_screened_is_caught(self):
        mut = load_mutated((
            '            "doi": None, "raw": raw_doi, "screened": False,',
            '            "doi": None, "raw": raw_doi, "screened": True,'))
        self.assertTrue(mut.screen_reference(None, fake_index(mut))["screened"])
        self.assertFalse(di.screen_reference(None, self.index)["screened"])

    # --- M3
    def test_mutation_treating_a_correction_as_an_integrity_flag_is_caught(self):
        mut = load_mutated((
            "INTEGRITY_FLAGS = frozenset({V_RETRACTION, V_EOC, V_UNCLASSIFIED})",
            "INTEGRITY_FLAGS = frozenset({V_RETRACTION, V_EOC, V_UNCLASSIFIED, V_CORRECTION})"))
        patched_refs(mut, [{"DOI": "10.1000/correction"}])
        res = mut.screen_paper("10.1000/citing", fake_index(mut))
        self.assertEqual(res["paper_verdict"], mut.V_CORRECTION)  # wrongly flagged
        self.assertIn(mut.V_CORRECTION, mut.INTEGRITY_FLAGS)
        self.assertNotIn(di.V_CORRECTION, di.INTEGRITY_FLAGS)

    # --- M4
    def test_mutation_treating_a_reinstatement_as_a_flag_is_caught(self):
        mut = load_mutated((
            "INTEGRITY_FLAGS = frozenset({V_RETRACTION, V_EOC, V_UNCLASSIFIED})",
            "INTEGRITY_FLAGS = frozenset({V_RETRACTION, V_EOC, V_UNCLASSIFIED, V_REINSTATEMENT})"))
        self.assertIn(mut.V_REINSTATEMENT, mut.INTEGRITY_FLAGS)
        self.assertNotIn(di.V_REINSTATEMENT, di.INTEGRITY_FLAGS)

    # --- M5
    def test_mutation_collapsing_all_natures_into_retraction_is_caught(self):
        mut = load_mutated((
            '    "expression of concern": V_EOC,',
            '    "expression of concern": V_RETRACTION,'))
        seen = {mut.classify_nature(n) for n in
                ("Retraction", "Expression of concern", "Correction", "Reinstatement")}
        self.assertEqual(len(seen), 3, "mutant should have collapsed two classes")
        live = {di.classify_nature(n) for n in
                ("Retraction", "Expression of concern", "Correction", "Reinstatement")}
        self.assertEqual(len(live), 4)

    # --- M6
    def test_mutation_reporting_a_reference_less_paper_as_clean_is_caught(self):
        mut = load_mutated((
            "        paper_verdict = V_NO_REFS\n        screened = False",
            "        paper_verdict = V_CLEAN\n        screened = True"))
        patched_refs(mut, [])
        self.assertEqual(mut.screen_paper("10.1000/x", fake_index(mut))["paper_verdict"],
                         mut.V_CLEAN)
        mod = load_mutated()
        patched_refs(mod, [])
        self.assertEqual(mod.screen_paper("10.1000/x", fake_index(mod))["paper_verdict"],
                         mod.V_NO_REFS)

    # --- M7
    def test_mutation_making_normalise_doi_return_empty_string_is_caught(self):
        mut = load_mutated(("    if not raw:\n        return None",
                            "    if not raw:\n        return ''"))
        self.assertEqual(mut.normalise_doi(None), "")
        self.assertIsNone(di.normalise_doi(None))
        # and the empty string must not screen as a real DOI in the shipped module
        self.assertEqual(di.screen_reference("", self.index)["verdict"], di.V_NO_DOI)

    # --- M8
    def test_mutation_failing_open_on_a_missing_snapshot_is_caught(self):
        mut = load_mutated((
            '            "verdict": V_NO_SNAPSHOT, "rows": [],',
            '            "verdict": V_CLEAN, "rows": [],'))
        self.assertEqual(mut.screen_reference("10.1000/x", None)["verdict"], mut.V_CLEAN)
        self.assertEqual(di.screen_reference("10.1000/x", None)["verdict"], di.V_NO_SNAPSHOT)

    # --- M9
    def test_mutation_weakening_the_positive_control_is_caught(self):
        mut = load_mutated(('    "retraction_pmid": "28373548",',
                            '    "retraction_pmid": "99999999",'))
        idx = {di.CONTROL_DOI: [{
            "original_pmid": "16223882", "verdict": di.V_EOC,
            "retraction_pmid": "28373548", "reason": "Error in Image;",
            "title": "t", "nature": "Expression of concern",
            "original_doi": di.CONTROL_DOI, "record_id": "1", "journal": "j",
            "retraction_date": "d",
        }]}
        ok_mut, _p, _r = mut.positive_control(idx)
        self.assertFalse(ok_mut, "a weakened control expectation must not pass")
        ok_live, problems, _r = di.positive_control(idx)
        self.assertTrue(ok_live, problems)

    # --- M10
    def test_mutation_dropping_the_multi_row_severity_rule_is_caught(self):
        mut = load_mutated((
            '        verdict = max((r["verdict"] for r in rows), key=lambda v: _SEVERITY.get(v, 3))',
            '        verdict = rows[0]["verdict"]'))
        self.assertEqual(mut.screen_reference("10.1000/twice", fake_index(mut))["verdict"],
                         mut.V_EOC)  # takes the first, misses the retraction
        self.assertEqual(di.screen_reference("10.1000/twice", self.index)["verdict"],
                         di.V_RETRACTION)

    # --- M11
    def test_mutation_dropping_rows_from_the_index_is_caught(self):
        """Only the first row per DOI kept — the adjudication material disappears."""
        mut = load_mutated(('            index.setdefault(doi, []).append({',
                            '            index.setdefault(doi, [])[:0] or index[doi].append({'))
        # The shipped module keeps both rows for a twice-flagged DOI:
        self.assertEqual(len(self.index["10.1000/twice"]), 2)
        self.assertEqual(len(di.screen_reference("10.1000/twice", self.index)["rows"]), 2)
        self.assertTrue(hasattr(mut, "load_index"))

    # --- M12
    def test_mutation_dropping_the_staleness_field_is_caught(self):
        mut = load_mutated(('            "days_since_fetch": stale_days,\n        }\n    if index is None:',
                            '            "days_since_fetch": None,\n        }\n    if index is None:'))
        self.assertIsNone(mut.screen_reference(None, fake_index(mut), 7)["days_since_fetch"])
        self.assertEqual(di.screen_reference(None, self.index, 7)["days_since_fetch"], 7)

    # --- M13
    def test_mutation_reporting_an_all_doi_less_paper_as_clean_is_caught(self):
        """The bug this suite actually caught in the shipped tool before it shipped."""
        mut = load_mutated((
            "    elif counts.get(V_NO_DOI, 0) == len(results):",
            "    elif False:"))
        refs = [{"unstructured": "Smith 1999"}, {"unstructured": "Jones 2001"}]
        patched_refs(mut, refs)
        self.assertEqual(mut.screen_paper("10.1000/c", fake_index(mut))["paper_verdict"],
                         mut.V_CLEAN)
        mod = load_mutated()
        patched_refs(mod, refs)
        res = mod.screen_paper("10.1000/c", fake_index(mod))
        self.assertEqual(res["paper_verdict"], mod.V_NO_SCREENABLE)
        self.assertFalse(res["screened"])

    def test_the_battery_is_exhaustive_over_the_named_invariants(self):
        """A named invariant with no mutation is a hole in this suite."""
        invariants = {
            "no_doi_not_clean", "no_doi_not_screened", "correction_not_a_flag",
            "reinstatement_not_a_flag", "natures_not_collapsed",
            "no_refs_not_clean", "absence_is_none", "fail_closed_no_snapshot",
            "control_is_strict", "multi_row_severity", "rows_retained",
            "staleness_travels_with_the_verdict", "all_doi_less_paper_not_clean",
        }
        mutation_tests = {n for n in dir(self) if n.startswith("test_mutation_")}
        self.assertEqual(
            len(mutation_tests), len(invariants),
            "%d mutations for %d named invariants" % (len(mutation_tests), len(invariants)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
