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


if __name__ == "__main__":
    unittest.main(verbosity=2)
