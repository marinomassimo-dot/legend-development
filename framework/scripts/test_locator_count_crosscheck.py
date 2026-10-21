#!/usr/bin/env python3
"""Regressions for `locator_count_crosscheck.py`.

The defect it was built for, pinned so it cannot come back quietly: on 2026-09-21,
**16 of 34** locator-count declarations in `paper_registry_current.md` disagreed with the
manifests they name, and **all sixteen understated** — deltas +2 to +27.

The tests below pin three things, in descending order of how badly they would hurt:

1. **The dict-versus-list trap.** `verbatim_locators` is an object whose `entries` key holds
   the locators. `len()` on the object returns 6 — its key count. Two independent actors hit
   this on the same day. A tool that inherited the same mistake would report every
   30-locator manifest as holding 6 and call the registry's wrong "6" correct.
2. **Anti-vacuity.** A scan that finds no declarations must FAIL, not pass. A guard whose
   population is empty agrees with nothing, and this one's entire value is that it looked.
3. **Direction.** Understating and overstating are different findings. Overstatement means
   the registry claims depth it does not have; understatement means it under-claims. The
   tool must not flatten them into one number.
"""
from __future__ import annotations

import io
import contextlib
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import locator_count_crosscheck as lcc  # noqa: E402

REPO = Path(__file__).resolve().parents[2]


class EntryCounting(unittest.TestCase):
    def test_dict_shape_counts_entries_not_keys(self):
        """The trap. Six keys, thirty locators — the answer is thirty."""
        manifest = {"verbatim_locators": {
            "waived": False,
            "source_fulltext_indexed": True,
            "source_fulltext_indexed_evidence": "x",
            "abstract_anchoring_waived": "y",
            "surface_note": "z",
            "entries": [{"proposition": str(i)} for i in range(30)],
        }}
        self.assertEqual(lcc.manifest_entry_count(manifest), 30,
                         "len() on the object returns 6; the locators are in `entries`")

    def test_legacy_list_shape_still_counts(self):
        self.assertEqual(lcc.manifest_entry_count({"verbatim_locators": [1, 2, 3]}), 3)

    def test_absent_or_malformed_yields_none_not_zero(self):
        """A zero from a parser is not evidence. Unknown must read as unknown."""
        self.assertIsNone(lcc.manifest_entry_count({}))
        self.assertIsNone(lcc.manifest_entry_count({"verbatim_locators": {"entries": "nope"}}))
        self.assertIsNone(lcc.manifest_entry_count({"verbatim_locators": 7}))


class DeclarationScanning(unittest.TestCase):
    MANIFESTS = {"11111111": (30, Path("PMID11111111.json")),
                 "22222222": (5, Path("PMID22222222.json"))}

    def test_mismatch_and_match_are_distinguished(self):
        text = ("a\n`deepdive_manifests/PMID11111111.json` (6 locators, schema v2)\n"
                "b\n`deepdive_manifests/PMID22222222.json` (5 locators, schema v2)\n")
        found = lcc.scan(text, self.MANIFESTS)
        self.assertEqual([f["state"] for f in found], ["mismatch", "match"])
        self.assertEqual(found[0]["actual"], 30)
        self.assertEqual(found[0]["line"], 2)

    def test_a_bare_locator_count_in_prose_is_not_a_declaration(self):
        """The regex is anchored on the manifest path on purpose: the defect is a broken
        link between two named artefacts, not a loose number in a sentence."""
        self.assertEqual(lcc.scan("the reading produced (7 locators) in total\n",
                                  self.MANIFESTS), [])

    def test_a_declaration_whose_manifest_is_absent_is_reported_not_silently_passed(self):
        found = lcc.scan("`deepdive_manifests/PMID99999999.json` (4 locators)\n", self.MANIFESTS)
        self.assertEqual(found[0]["state"], "no_manifest")


class AgainstTheLiveRepository(unittest.TestCase):
    """A fixture test would have passed throughout the months this was wrong."""

    def test_the_scan_finds_declarations_at_all(self):
        manifests = lcc.load_manifests(REPO, "wwox")
        self.assertGreater(len(manifests), 40, "the manifest directory must be readable")
        registry = REPO / lcc.REGISTRY.format(disease="wwox")
        found = lcc.scan(registry.read_text(encoding="utf-8"), manifests)
        self.assertGreater(len(found), 20,
                           "if this collapses to ~0 the declaration format drifted and the "
                           "tool has gone blind — that is a FAILURE, not a clean registry")

    def test_no_declaration_overstates_its_manifest(self):
        """The direction that would be serious. Understatement is the known debt and is
        tracked in a commit candidate; an OVERSTATEMENT would mean the canonical registry
        claims evidence depth that does not exist, and must fail loudly the day it appears."""
        manifests = lcc.load_manifests(REPO, "wwox")
        registry = REPO / lcc.REGISTRY.format(disease="wwox")
        found = lcc.scan(registry.read_text(encoding="utf-8"), manifests)
        over = [f for f in found
                if f["state"] == "mismatch" and f["actual"] < f["declared"]]
        self.assertEqual(over, [], f"registry overstates its manifests: {over}")


class ExitCodes(unittest.TestCase):
    def test_vacuous_scan_returns_usage_error_not_success(self):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = lcc.main([str(REPO), "--disease", "no-such-disease"])
        self.assertEqual(code, 2, "a missing registry is an error, never a pass")

    def test_json_mode_emits_parsable_findings(self):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            lcc.main([str(REPO), "--json"])
        rows = json.loads(buf.getvalue())
        self.assertTrue(all({"line", "pmid", "declared", "actual", "state"} <= set(r)
                            for r in rows))



class DepthLineDrift(unittest.TestCase):
    """N10 (2026-10-20): depth lines that name a receipt the manifest was not produced by."""

    def test_producer_unknown_and_depth_drift_are_each_named(self) -> None:
        import tempfile
        from unittest import mock
        import fulltext_receipts as fr
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifests = root / lcc.MANIFEST_DIR.format(disease="wwox")
            manifests.mkdir(parents=True)
            (manifests / "PMID11111111.json").write_text(
                json.dumps({"pmid": "11111111", "receipt": "FTR-20260101-11111111-01"}))
            (manifests / "PMID22222222.json").write_text(
                json.dumps({"pmid": "22222222", "receipt": "FTR-20260101-22222222-01"}))
            ledger = fr.default_ledger_path(root, "wwox")
            ledger.parent.mkdir(parents=True)
            ledger.write_text("")
            events = [
                {"event_id": "FTR-20260101-11111111-01", "study_id": {"pmid": "11111111"},
                 "evidence_depth": "partial_fulltext_read"},
                {"event_id": "FTR-20260102-11111111-02", "study_id": {"pmid": "11111111"},
                 "evidence_depth": "complete_fulltext_read"},
                {"event_id": "FTR-20260101-22222222-01", "study_id": {"pmid": "22222222"},
                 "evidence_depth": "complete_fulltext_read"},
            ]
            text = (
                "**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20260102-11111111-02`, "
                "`deepdive_manifests/PMID11111111.json`\n"
                "**Evidence depth:** `complete_fulltext_read` — receipts `FTR-20260101-22222222-01` "
                "(producer) and `FTR-20260109-22222222-02`, `deepdive_manifests/PMID22222222.json`\n")
            with mock.patch.object(fr, "load_ledger", return_value=events), \
                    mock.patch.object(fr, "active_receipts", side_effect=lambda e: e):
                rows = lcc.scan_depth(text, root, "wwox")
        first, second = rows
        self.assertEqual(2, len(first["problems"]))
        self.assertTrue(first["problems"][0].startswith("receipt_differs"))
        self.assertTrue(first["problems"][1].startswith("depth_differs"))
        self.assertEqual(["unknown_receipt: FTR-20260109-22222222-02"], second["problems"])

class TheWideSweep(unittest.TestCase):
    """D-40 (2026-10-21). The defect the narrow pattern could not see, and the four states.

    `DECLARATION_RE` requires the count as the first token inside the parenthesis. The two
    records D-40 was written into say `(schema v2, **11** persisted verbatim locators`, so
    they were never in its population at all: the check was green on a defect it was built
    for. Every wording below is copied from a live `paper_registry_current.md` sentence.
    """

    MANIFESTS = {"11111111": (11, Path("PMID11111111.json")),
                 "22222222": (28, Path("PMID22222222.json")),
                 "33333333": (29, Path("PMID33333333.json"))}

    def states(self, text, manifests=None, key_counts=None):
        return [(f.get("state"), f.get("excluded"), f["declared"])
                for f in lcc.sweep(text, manifests or self.MANIFESTS, key_counts)]

    def test_a_correct_count_passes_in_the_d40_wording(self):
        """The exact shape of PAPER 427 after its repair: count not first in the parenthesis."""
        text = ("**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261020-11111111-01`; "
                "manifest `deepdive_manifests/PMID11111111.json` (schema v2, **11** persisted "
                "verbatim locators, all 11 on the body surface)\n")
        self.assertEqual([("agrees", None, 11)], self.states(text))

    def test_the_len_mapping_trap_is_a_fixture_and_cannot_be_repeated(self):
        """🔴 THE DEFECT ITSELF. A manifest whose `verbatim_locators` mapping has SIX keys and
        ELEVEN entries, and a registry sentence asserting the key count. The checker must name
        both numbers, call it a disagreement, and recognise the mis-measurement by name — if it
        ever agreed here it would have repeated D-40 instead of catching it."""
        manifest = {"pmid": "11111111", "verbatim_locators": {
            "waived": False, "source_fulltext_indexed": True,
            "source_fulltext_indexed_evidence": "x", "note": "y",
            "artifact_locality_note": "z",
            "entries": [{"proposition": str(i)} for i in range(11)]}}
        self.assertEqual(6, lcc.manifest_key_count(manifest),
                         "len() on the mapping is 6 — the wrong answer, derived on purpose")
        self.assertEqual(11, lcc.manifest_entry_count(manifest))
        text = ("manifest `deepdive_manifests/PMID11111111.json` (schema v2, **6** persisted "
                "verbatim locators, exact text match verified)\n")
        found = lcc.sweep(text, self.MANIFESTS, {"11111111": 6})
        self.assertEqual("disagrees", found[0]["state"])
        self.assertEqual(6, found[0]["declared"])
        self.assertEqual(11, found[0]["actual"])
        self.assertTrue(found[0]["d40_signature"],
                        "6 asserted against a 6-key mapping holding 11 entries is not a stale "
                        "total, it is the mis-measurement, and the report must say so")

    def test_a_wrong_count_is_named_with_both_numbers_in_the_report(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / lcc.MANIFEST_DIR.format(disease="wwox")).mkdir(parents=True)
            (root / lcc.MANIFEST_DIR.format(disease="wwox") / "PMID11111111.json").write_text(
                json.dumps({"pmid": "11111111", "verbatim_locators": {
                    "waived": False, "entries": [{"p": i} for i in range(11)]}}))
            registry = root / lcc.REGISTRY.format(disease="wwox")
            registry.parent.mkdir(parents=True)
            registry.write_text("manifest `deepdive_manifests/PMID11111111.json` "
                                "(schema v2, **4** persisted verbatim locators)\n")
            with contextlib.redirect_stdout(io.StringIO()) as buf:
                code = lcc.main([str(root), "--sweep", "--max-disagreements", "0"])
        out = buf.getvalue()
        self.assertEqual(1, code, "a disagreement above the ceiling must exit non-zero")
        self.assertIn("asserts 4", out)
        self.assertIn("holds 11", out)

    def test_an_absent_manifest_is_reported_absent_and_never_counted_clean(self):
        text = "manifest `deepdive_manifests/PMID99999999.json` (9 verbatim locators)\n"
        self.assertEqual([("manifest_absent", None, 9)], self.states(text))

    def test_an_unparsable_sentence_is_reported_not_silently_clean(self):
        """Live wording, lines 6856/6880/6905: a count and no manifest path anywhere in the
        clause. Guessing a file for it would invent the link the tool exists to check."""
        text = ("**Evidence depth:** receipt `FTR-20260806-19500159-01`; manifest schema-v2 "
                "con **30 locator** verificati (24 corpo, 2 tabella, 4 figura)\n")
        rows = lcc.sweep(text, self.MANIFESTS)
        self.assertEqual("unparsed", rows[0]["state"])
        self.assertEqual(30, rows[0]["declared"])
        self.assertIsNone(rows[0]["actual"])
        self.assertEqual({"agrees": 0, "disagrees": 0, "manifest_absent": 0, "unparsed": 1},
                         lcc.tally(rows))

    def test_the_measured_wordings_are_all_reached(self):
        """Each line is a live registry wording the narrow pattern missed."""
        wordings = [
            ("manifest `deepdive_manifests/PMID11111111.json` (11 locators, schema v2)", "agrees"),
            ("manifest `deepdive_manifests/PMID11111111.json` (11 verbatim locators, PASS)", "agrees"),
            ("manifest `deepdive_manifests/PMID11111111.json` (11 locator, validatore PASS)", "agrees"),
            ("manifest `deepdive_manifests/PMID11111111.json`, **11** verbatim locators — 5 "
             "persisted", "agrees"),
            ("11 locator verificati in `deepdive_manifests/PMID11111111.json` (validatore PASS)",
             "agrees"),
            ("manifest `deepdive_manifests/PMID22222222.json` (schema v2, **28** persisted "
             "verbatim locators)", "agrees"),
        ]
        for line, expected in wordings:
            with self.subTest(line=line):
                rows = lcc.sweep(line + "\n", self.MANIFESTS)
                self.assertEqual(1, len(rows), "exactly one assertion on this line")
                self.assertEqual(expected, rows[0]["state"])

    def test_a_retired_quotation_is_excluded_rather_than_counted_wrong(self):
        """Both D-40 repairs keep the superseded figure on the line, inside «…». Verifying it
        would report a disagreement the registry has already resolved in writing."""
        text = ("manifest `deepdive_manifests/PMID11111111.json` (schema v2, **11** persisted "
                "verbatim locators) [corrected 2026-10-21 from «6 persisted verbatim locators» "
                "by `BATCH_20261019_009`]\n")
        self.assertEqual([("agrees", None, 11), (None, "retired_quotation", 6)],
                         self.states(text))

    def test_a_subset_mention_is_not_the_total(self):
        text = ("manifest `deepdive_manifests/PMID33333333.json` (29 locators, 3 declared gaps; "
                "the first 20 locators quote an absent artefact)\n")
        self.assertEqual([("agrees", None, 29), (None, "subset_mention", 20)],
                         self.states(text))

    def test_a_number_that_names_a_figure_is_not_a_count(self):
        """Live, line 7333: *"the only Figure 3 locator"*. A bare `\\d+ locator` reads three."""
        self.assertEqual([], self.states("the only Figure 3 locator, `entries[7]`, reads panel F\n"))

    def test_a_clause_barrier_blocks_a_false_attribution(self):
        """Also line 7333: a count about THIS paper sitting after an ERRATUM's manifest path.
        Attributing across the closing parenthesis would manufacture a disagreement."""
        text = ("read as its own source (`FTR-1`, manifest `deepdive_manifests/PMID11111111.json` "
                "PASS 0 gaps), and checked against this paper's 38 locators\n")
        self.assertEqual([("unparsed", None, 38)], self.states(text))


class TheRatchet(unittest.TestCase):
    def test_the_ceiling_is_a_ceiling_and_not_an_equality(self):
        """Repairing a registry count is a `BATCH_COMMIT` act by the integrator. A suite that
        went red the day one was repaired would be a gate on scientific work
        (`harness_development_principles.md` principle 3), so the live assertion is `<=` — and
        the tool prints its own instruction to come down whenever there is headroom."""
        manifests = lcc.load_manifests(REPO, "wwox")
        registry = REPO / lcc.REGISTRY.format(disease="wwox")
        found = lcc.sweep(registry.read_text(encoding="utf-8"), manifests,
                          lcc.load_key_counts(REPO, "wwox"))
        counts = lcc.tally(found)
        self.assertLessEqual(
            counts["disagrees"], lcc.BASELINE_DISAGREEMENTS,
            "a NEW locator-count disagreement: re-derive from the manifest, and remember the "
            "repair is a BATCH_COMMIT act. Disagreeing now: " + ", ".join(
                f"PMID {f['pmid']} line {f['line']} ({f['declared']} vs {f['actual']})"
                for f in found if f.get("state") == "disagrees"))
        self.assertLessEqual(
            counts["unparsed"], lcc.BASELINE_UNPARSED,
            "a NEW unparsed count assertion: the registry's wordings moved and the pattern did "
            "not follow. An unparsed sentence is a distinct state, never a clean one.")
        self.assertLessEqual(counts["manifest_absent"], lcc.BASELINE_MANIFEST_ABSENT,
                             "a declaration whose manifest is gone is never clean")

    def test_headroom_prints_the_instruction_to_lower_the_ceiling(self):
        """How it tightens by itself: a ceiling with headroom says so, in the output, on every
        run — so a baseline can only ever move down.

        🔴 THE CEILING IS PASSED EXPLICITLY, and that is the point of this test rather than an
        detail of it. Until 2026-10-21 this fixture asserted the headroom message while
        leaving the ceiling to `BASELINE_DISAGREEMENTS`, so it was really asserting that the
        live baseline is greater than zero — and it went red the moment
        `BATCH_20261019_011` repaired all fourteen disagreements and lowered that baseline to
        0, which is the one event the ratchet exists to reward. A test of the
        tightening MECHANISM must not fail when the mechanism is used, so the ceiling is now
        this fixture's own.
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / lcc.MANIFEST_DIR.format(disease="wwox")).mkdir(parents=True)
            (root / lcc.MANIFEST_DIR.format(disease="wwox") / "PMID11111111.json").write_text(
                json.dumps({"pmid": "11111111",
                            "verbatim_locators": {"entries": [{"p": 1}]}}))
            registry = root / lcc.REGISTRY.format(disease="wwox")
            registry.parent.mkdir(parents=True)
            registry.write_text("manifest `deepdive_manifests/PMID11111111.json` (1 locator)\n")
            with contextlib.redirect_stdout(io.StringIO()) as buf:
                code = lcc.main([str(root), "--sweep", "--max-disagreements", "3"])
        self.assertEqual(0, code)
        self.assertIn("RATCHET HAS HEADROOM", buf.getvalue())
        self.assertIn("lower BASELINE_DISAGREEMENTS to 0", buf.getvalue())

    def test_a_sweep_that_parses_nothing_is_an_error_not_a_pass(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root / lcc.REGISTRY.format(disease="wwox")
            registry.parent.mkdir(parents=True)
            registry.write_text("## PAPER 001\nno counts here at all\n")
            with contextlib.redirect_stdout(io.StringIO()) as buf:
                code = lcc.main([str(root), "--sweep"])
        self.assertEqual(2, code)
        self.assertIn("NO ASSERTIONS PARSED", buf.getvalue())

    def test_the_sweep_reaches_more_than_the_narrow_pattern(self):
        """The whole reason `--sweep` exists: the narrow population did not contain D-40."""
        manifests = lcc.load_manifests(REPO, "wwox")
        text = (REPO / lcc.REGISTRY.format(disease="wwox")).read_text(encoding="utf-8")
        narrow = lcc.scan(text, manifests)
        wide = [f for f in lcc.sweep(text, manifests) if not f.get("excluded")]
        self.assertGreater(len(wide), len(narrow),
                           "if the wide parse stops reaching further than the narrow one, the "
                           "wordings have collapsed or the pattern has broken")

    def test_json_mode_carries_the_ceiling_and_the_four_counts(self):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            lcc.main([str(REPO), "--sweep", "--json"])
        payload = json.loads(buf.getvalue())
        self.assertEqual(lcc.BASELINE_DISAGREEMENTS, payload["ceiling"])
        self.assertEqual(set(lcc.STATES), set(payload["counts"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
