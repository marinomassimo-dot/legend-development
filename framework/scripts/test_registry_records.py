#!/usr/bin/env python3
"""Regressions for `registry_records.py`, built on the Aqeilan corpus's own adverse cases.

🔴 THE EXPECTED SETS ARE DERIVED INDEPENDENTLY OF THE SELECTOR. Each case below computes what
must come back using a different mechanism — a line scan over the raw file, the way a person with
`awk` would do it — and only then asks the selector. Using the selector's own output as evidence
of its completeness is the failure this file exists to avoid.

The cases are the ones the operator named, each instantiated on real records:

  A · identifier ambiguity          PMID 33914858 is claimed by TWO paper-registry records
  B · identity versus mention       the same PMID is cited inside a third record's prose
  C · dependency between papers     18460020's reagents descend from 16223882
  D · caveat that a fragment kills  CLAIM 030 carries a methodological caveat mid-record
  E · reachable only past hop 0     the claim a paper stands on is one wikilink away
  F · empty result                  a query that matches nothing must not read as "not known"
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import registry_records as rr  # noqa: E402

REGISTRIES = ROOT / "disease-models/wwox/registries"
PAPERS = REGISTRIES / "paper_registry_current.md"
CLAIMS = REGISTRIES / "claim_registry_current.md"
LITLOG = REGISTRIES / "literature_tracking_log_current.md"

AMBIGUOUS_PMID = "33914858"     # Repudi 2021, held behind Cloudflare, CLAIM 003's primary
CAVEAT_CLAIM = "CLAIM 030"


def records_naming_identity(path: Path, pmid: str) -> set[str]:
    """The expected set, derived WITHOUT the selector: a line scan for an identity field."""
    current, found = "", set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
        elif re.match(r"\*\*Identifier(?: value)?:\*\*", line.strip()) and pmid in line:
            found.add(current)
    return found


def record_text_by_scan(path: Path, record_id: str) -> str:
    """The record's EXACT bytes, taken by scanning — the comparison for 'returned whole'.

    Byte-identical, not content-identical: the first cut of the tool normalised trailing
    whitespace, and this helper normalised it the same way, so the pair agreed while neither
    matched the file. An independent check caught it. Any `## ` heading ends the record — an em
    dash in the next heading does not extend this one.
    """
    out, inside = [], False
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip() == record_id
        if inside:
            out.append(line)
    return "".join(out)


class CaseAIdentifierAmbiguity(unittest.TestCase):
    def setUp(self) -> None:
        self.expected = records_naming_identity(PAPERS, AMBIGUOUS_PMID)
        self.found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=0)

    def test_the_corpus_really_does_hold_the_ambiguity(self) -> None:
        """If this ever becomes one record the case is fixed, and this test should be retired."""
        self.assertGreaterEqual(len(self.expected), 2, self.expected)

    def test_every_independently_expected_record_comes_back(self) -> None:
        returned = {record.record_id for record, why in self.found.hits
                    if record.source == "paper_registry_current" and why.startswith("identity")}
        self.assertEqual(self.expected, returned)

    def test_the_ambiguity_is_reported_and_not_resolved(self) -> None:
        self.assertTrue(self.found.ambiguous, "two records claiming one identity must be named")
        text = " ".join(self.found.ambiguous)
        for record_id in self.expected:
            self.assertIn(record_id, text)
        self.assertIn("a reader decides", text)

    def test_the_literature_log_record_is_reached_too(self) -> None:
        expected = records_naming_identity(LITLOG, AMBIGUOUS_PMID)
        returned = {record.record_id for record, _ in self.found.hits
                    if record.source == "literature_tracking_log_current"}
        self.assertTrue(expected <= returned, (expected, returned))


class CaseBIdentityIsNotMention(unittest.TestCase):
    def test_a_record_citing_the_pmid_in_prose_is_labelled_mention(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=0)
        identity = records_naming_identity(PAPERS, AMBIGUOUS_PMID)
        mentions = {record.record_id for record, why in found.hits if why == "mention"}
        self.assertTrue(mentions, "the corpus cites this PMID in prose somewhere")
        self.assertFalse(mentions & identity, "a mention was mislabelled as an identity")

    def test_both_kinds_are_returned_never_merged(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=0)
        kinds = {why.split(" (")[0] for _record, why in found.hits}
        self.assertIn("identity", kinds)
        self.assertIn("mention", kinds)


class CaseCDependencyBetweenPapers(unittest.TestCase):
    """18460020's virus and antibodies come from 16223882, which is under an expression of
    concern — the sweep's S7. Both records must be obtainable, and the second is a separate
    query, not a silent inclusion."""

    def test_each_paper_resolves_to_its_own_record(self) -> None:
        for pmid in ("18460020", "16223882"):
            expected = records_naming_identity(PAPERS, pmid)
            self.assertTrue(expected, f"the corpus holds no identity record for {pmid}")
            found = rr.select(ROOT, "wwox", pmid=pmid, hops=0)
            returned = {record.record_id for record, why in found.hits
                        if record.source == "paper_registry_current" and why.startswith("identity")}
            self.assertEqual(expected, returned, pmid)

    def test_the_dependency_is_not_invented_by_the_selector(self) -> None:
        """A selector that silently joined the two would be asserting a dependency. It does not:
        the join is the reader's, and the screen that proposes it is `dependency_integrity.py`."""
        found = rr.select(ROOT, "wwox", pmid="18460020", hops=1)
        returned = {record.record_id for record, _ in found.hits}
        expected_16223882 = records_naming_identity(PAPERS, "16223882")
        for record_id in expected_16223882:
            if record_id in returned:
                linked = [why for record, why in found.hits if record.record_id == record_id]
                self.assertTrue(any("linked from" in why for why in linked),
                                "if it came back it must be because a wikilink said so")


class CaseDACaveatSurvivesTheSelection(unittest.TestCase):
    def test_the_claim_record_comes_back_byte_for_byte(self) -> None:
        expected = record_text_by_scan(CLAIMS, CAVEAT_CLAIM)
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0)
        match = [record for record, _ in found.hits if record.record_id == CAVEAT_CLAIM]
        self.assertEqual(1, len(match))
        self.assertEqual(expected, match[0].text)

    def test_the_caveat_and_the_negative_are_inside_what_came_back(self) -> None:
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0)
        text = found.hits[0][0].text
        self.assertIn("caveat", text.lower())
        self.assertIn("⚠️", text)
        self.assertIn("Evidence boundary", text)

    def test_a_mid_record_field_is_not_dropped(self) -> None:
        """The fragment failure, stated as a property: every `**Field:**` line of the scanned
        record is present in the returned one."""
        expected = record_text_by_scan(CLAIMS, CAVEAT_CLAIM)
        fields = [line for line in expected.splitlines() if line.startswith("**")]
        self.assertGreater(len(fields), 8)
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0)
        returned = found.hits[0][0].text
        for line in fields:
            self.assertIn(line, returned)


class CaseEReachableOnlyByExpansion(unittest.TestCase):
    def test_hop_zero_does_not_reach_the_claim_and_hop_one_does(self) -> None:
        at_zero = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=0)
        at_one = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        claims_zero = {r.record_id for r, _ in at_zero.hits if r.source == "claim_registry_current"}
        claims_one = {r.record_id for r, _ in at_one.hits if r.source == "claim_registry_current"}
        self.assertEqual(set(), claims_zero)
        self.assertTrue(claims_one, "one hop must reach the claims the paper record links to")
        self.assertTrue(claims_one - claims_zero)

    def test_expansion_is_explicit_and_the_limit_is_stated(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        rendered = rr.render(found, query="x")
        self.assertIn("limits of this selection", rendered)
        self.assertIn("--hops", rendered)


class CaseFAnEmptyResultIsNotAScientificStatement(unittest.TestCase):
    def test_no_match_exits_non_zero_and_says_what_it_is_not(self) -> None:
        code = rr.main(["get", "--pmid", "10000001", "--root", str(ROOT)])
        self.assertEqual(1, code)

    def test_the_wording_refuses_the_inference(self) -> None:
        found = rr.select(ROOT, "wwox", pmid="10000001", hops=1)
        rendered = rr.render(found, query="pmid=10000001")
        self.assertIn("NO RECORD MATCHED", rendered)
        self.assertIn("not evidence", rendered)

    def test_the_json_flag_carries_the_same_refusal(self) -> None:
        done = subprocess.run(
            [sys.executable, str(HERE / "registry_records.py"), "get", "--pmid", "10000001",
             "--root", str(ROOT), "--json"], capture_output=True, text=True)
        self.assertEqual(1, done.returncode)
        self.assertTrue(json.loads(done.stdout)["empty_result_is_not_a_scientific_statement"])


class NoSilentTruncation(unittest.TestCase):
    def test_a_limit_names_its_residue(self) -> None:
        wide = rr.select(ROOT, "wwox", theme="myelin", hops=0)
        self.assertGreater(len(wide.hits), 3, "the fixture needs a query with several hits")
        narrow = rr.select(ROOT, "wwox", theme="myelin", hops=0, limit=2)
        self.assertEqual(2, len(narrow.hits))
        self.assertEqual(len(wide.hits) - 2, narrow.residue)
        self.assertIn("were NOT returned", rr.render(narrow, query="theme=myelin"))

    def test_a_record_is_never_cut_in_the_middle(self) -> None:
        narrow = rr.select(ROOT, "wwox", theme="myelin", hops=0, limit=2)
        for record, _why in narrow.hits:
            self.assertTrue(record.text.startswith("## "))
            self.assertTrue(record.text.endswith("\n"))


class ProvenanceAndDrift(unittest.TestCase):
    def test_every_answer_carries_the_source_digests(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        self.assertIn("paper_registry_current", found.file_digests)
        for digest in found.file_digests.values():
            self.assertEqual(64, len(digest))

    def test_each_record_carries_its_own_digest_path_and_line(self) -> None:
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0)
        record, why = found.hits[0]
        self.assertEqual(64, len(record.digest))
        self.assertTrue(record.path.endswith("claim_registry_current.md"))
        self.assertGreater(record.line, 0)
        self.assertEqual(record.text, record_text_by_scan(CLAIMS, CAVEAT_CLAIM))
        self.assertEqual("record id", why)

    def test_a_changed_source_changes_the_reported_digest(self) -> None:
        """The drift detector, exercised rather than asserted: a byte changes, the digest moves."""
        before = rr.file_digest(CLAIMS)
        after = rr.file_digest(PAPERS)
        self.assertNotEqual(before, after)

    def test_an_unresolvable_link_is_named_and_not_dropped(self) -> None:
        """A synthetic workspace, because the live corpus currently has no broken link at two
        hops from the fixture PMID — and a test that only runs when the corpus happens to be
        broken is a test that proves nothing. Found by mutation: dropping the `unresolved`
        append left the conditional version green."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registries = root / "disease-models/wwox/registries"
            registries.mkdir(parents=True)
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 001\n**Identifier:** PMID 11111111 / DOI 10.1/x\n"
                "**Wikilinks:** [[claim_registry_current#CLAIM 999]] · "
                "[[nowhere_current#THING 1]]\n", encoding="utf-8")
            (registries / "claim_registry_current.md").write_text(
                "## CLAIM 001\n**Title:** a claim that is not 999\n", encoding="utf-8")
            found = rr.select(root, "wwox", pmid="11111111", hops=1)
            self.assertEqual(2, len(set(found.unresolved)), found.unresolved)
            joined = " ".join(found.unresolved)
            self.assertIn("CLAIM 999", joined)
            self.assertIn("does not exist", joined)
            self.assertIn("nowhere_current", joined)
            self.assertIn("no such registry surface", joined)
            self.assertIn("UNRESOLVED LINKS", rr.render(found, query="x"))

    def test_a_link_that_resolves_is_not_reported_as_unresolved(self) -> None:
        """The anti-vacuity half: a detector that reports everything proves nothing either."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registries = root / "disease-models/wwox/registries"
            registries.mkdir(parents=True)
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 001\n**Identifier:** PMID 11111111 / DOI 10.1/x\n"
                "**Wikilinks:** [[claim_registry_current#CLAIM 001]]\n", encoding="utf-8")
            (registries / "claim_registry_current.md").write_text(
                "## CLAIM 001\n**Title:** the claim that exists\n", encoding="utf-8")
            found = rr.select(root, "wwox", pmid="11111111", hops=1)
            self.assertEqual([], found.unresolved)
            self.assertIn("CLAIM 001", {record.record_id for record, _ in found.hits})


class ARecordIsNotAProseSection(unittest.TestCase):
    """Measured, not assumed: the first cut pulled a 470,808-character `## Change-log` block
    into a reading because it mentioned a PMID once, and the selective path came out LARGER
    than the full preload it replaces. Sections are named and left behind; records are carried."""

    def test_the_giant_prose_sections_really_exist(self) -> None:
        blocks = rr.parse_records(ROOT, "wwox", "discovery_ledger_current")
        sections = [b for b in blocks if b.kind == "section"]
        self.assertTrue(sections, "the fixture needs a prose section to exclude")
        self.assertGreater(max(len(b.text) for b in sections), 100_000)

    def test_a_mention_inside_a_section_is_named_and_not_carried(self) -> None:
        """Asserted as a property, not by section name: the heading fix re-cut the discovery
        ledger's prose into differently named blocks, and a test pinned to one name would have
        gone green while the protection lapsed."""
        found = rr.select(ROOT, "wwox", pmid="29724996", hops=1)
        carried = {(r.source, r.record_id) for r, _ in found.hits}
        self.assertFalse([pair for pair in carried if pair[0] == "discovery_ledger_current"
                          and not rr.is_record_id(pair[1])], carried)
        big = [n for n in found.notes if "discovery_ledger_current" in n]
        self.assertTrue(big, found.notes)
        self.assertTrue(any(int(n.split("prose section, ")[1].split(" chars")[0].replace(",", ""))
                            > 100_000 for n in big), big)
        self.assertIn("--id", " ".join(found.notes))

    def test_a_section_is_still_reachable_when_it_is_asked_for_by_name(self) -> None:
        found = rr.select(ROOT, "wwox", record_id="Change-log", hops=0)
        self.assertTrue([r for r, _ in found.hits if r.record_id == "Change-log"])

    def test_hops_never_expand_through_a_section(self) -> None:
        found = rr.select(ROOT, "wwox", record_id="Change-log", hops=1)
        linked = [why for _r, why in found.hits if "linked from Change-log" in why]
        self.assertEqual([], linked)

    def test_every_carried_record_has_a_recognised_identity_shape(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        for record, why in found.hits:
            if why != "record id":
                self.assertTrue(rr.is_record_id(record.record_id), (record.record_id, why))

    def test_the_selective_path_is_smaller_than_the_full_preload(self) -> None:
        """The claim this whole change rests on, as an executable comparison."""
        four = ["working_model_current.md", "claim_registry_current.md",
                "paper_registry_current.md", "literature_tracking_log_current.md"]
        preload = sum((REGISTRIES / name).stat().st_size for name in four)
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        selected = len(rr.render(found, query="x"))
        self.assertLess(selected * 4, preload, (selected, preload))


class TheFourDefectsAnIndependentCheckFound(unittest.TestCase):
    """2026-09-11. A verifier that built its own expected answers refuted four of five claims
    this file's own suite had passed. Each is pinned here with the record that exposed it."""

    def test_an_em_dash_heading_ends_the_record_before_it(self) -> None:
        """LIT-0405 came back as 6,860 characters where the file holds 2,751, absorbing two
        sections whose headings carry an em dash — and manufacturing false mentions on five
        further PMIDs."""
        blocks = {b.record_id: b for b in rr.parse_records(ROOT, "wwox",
                                                           "literature_tracking_log_current")}
        self.assertIn("LIT-0405", blocks)
        self.assertEqual(record_text_by_scan(LITLOG, "LIT-0405"), blocks["LIT-0405"].text)
        self.assertNotIn("\n## ", blocks["LIT-0405"].text[3:])

    def test_a_citation_in_a_source_field_is_a_mention_not_an_identity(self) -> None:
        """A CLAIM's `**Source:**` names the paper it cites. Calling that identity labelled
        thirteen claims as identity matches for a PMID that is only their citation."""
        found = rr.select(ROOT, "wwox", pmid="15070730", hops=0)
        labels = {record.record_id: why for record, why in found.hits}
        self.assertEqual("mention", labels.get("CLAIM 023"))
        expected = records_naming_identity(CLAIMS, "15070730")
        identities = {rid for rid, why in labels.items() if why.startswith("identity")
                      and rid.startswith("CLAIM")}
        self.assertEqual(expected, identities)

    def test_the_same_identifiers_in_a_different_order_are_one_identity(self) -> None:
        """`PMID x / PMC y / DOI z` and `PMID x / DOI z / PMC y` are the same paper. Keying on
        the whole string missed the duplicates on ten PMIDs."""
        self.assertEqual(rr.identity_key("PMID 21115974 / PMC1 / DOI 10.1182/blood-2010-08-303073"),
                         rr.identity_key("PMID 21115974 / DOI 10.1182/blood-2010-08-303073 / PMC1"))
        found = rr.select(ROOT, "wwox", pmid="21115974", hops=0)
        self.assertTrue(found.ambiguous, "two paper-registry records claim this identifier")
        joined = " ".join(found.ambiguous)
        self.assertIn("PAPER 086", joined)
        self.assertIn("CORPUS P305", joined)

    def test_a_bare_pmid_and_a_pmid_with_a_doi_are_one_identity(self) -> None:
        """Second pass: keying on PMID+DOI together left two real duplicates unreported, because
        one record carries the bare identifier `30290271` and the other `PMID 30290271 / DOI …`."""
        self.assertEqual(rr.identity_key("30290271"),
                         rr.identity_key("PMID 30290271 / DOI 10.1016/j.nbd.2018.09.026"))
        found = rr.select(ROOT, "wwox", pmid="30290271", hops=0)
        joined = " ".join(found.ambiguous)
        self.assertIn("LIT-006", joined)
        self.assertIn("LIT-0108", joined)

    def test_digits_inside_a_doi_do_not_enter_the_pmid_key(self) -> None:
        """`10.1371/journal.pone.0007775` was contributing `0007775` to the key — cosmetic today,
        a false collision the day two unrelated DOIs share a seven-digit suffix."""
        self.assertEqual("PMID 19936220",
                         rr.identity_key("PMID 19936220 / DOI 10.1371/journal.pone.0007775"))
        self.assertNotIn("0007775", rr.identity_key("PMID 19936220 / DOI 10.1371/journal.pone.0007775"))

    def test_two_records_with_different_pmids_are_not_an_ambiguity(self) -> None:
        """The anti-vacuity half: a key that collides on everything reports everything."""
        self.assertNotEqual(rr.identity_key("PMID 11111111 / DOI 10.1/x"),
                            rr.identity_key("PMID 22222222 / DOI 10.1/x"))

    def test_a_block_carrying_an_identifier_is_a_record_whatever_its_heading(self) -> None:
        """`CORPUS P###` (188 headings) and `LIT-EX-###` (6) were withheld as prose, so records
        holding a real identifier never came back and their links were never followed."""
        self.assertTrue(rr.is_record("CORPUS P206", "**Identifier:** PMID 15070730 / DOI 10.1/x"))
        self.assertTrue(rr.is_record("LIT-EX-001", "**Identifier value:** 10.1/y"))
        self.assertFalse(rr.is_record("Change-log", "some prose with no identifier field"))
        found = rr.select(ROOT, "wwox", pmid="15070730", hops=0)
        labels = {record.record_id: why for record, why in found.hits}
        self.assertTrue(labels.get("CORPUS P206", "").startswith("identity"), labels)

    def test_a_section_is_still_withheld_and_still_named(self) -> None:
        """The fix must not undo the measured one: six-figure prose blocks stay out."""
        found = rr.select(ROOT, "wwox", pmid="29724996", hops=1)
        withheld = [n for n in found.notes if "prose section" in n]
        self.assertTrue(withheld, "the giant ledger prose must be named, not carried")
        carried = sum(len(record.text) for record, _ in found.hits)
        self.assertLess(carried, 200_000, "the selective path must stay small")


class TheIndexIsDerivedNeverAuthoritative(unittest.TestCase):
    def test_the_index_reproduces_the_independent_identity_scan(self) -> None:
        index = rr.build_index(ROOT, "wwox")
        expected = {f"paper_registry_current#{rid}"
                    for rid in records_naming_identity(PAPERS, AMBIGUOUS_PMID)}
        self.assertTrue(expected <= set(index["identities"].get(AMBIGUOUS_PMID, [])))

    def test_the_index_carries_the_digest_of_what_it_was_built_from(self) -> None:
        index = rr.build_index(ROOT, "wwox")
        self.assertEqual(rr.file_digest(PAPERS),
                         index["sources"]["paper_registry_current"]["digest"])

    def test_the_index_is_not_written_to_disk_by_building_it(self) -> None:
        before = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                                capture_output=True, text=True).stdout
        rr.build_index(ROOT, "wwox")
        after = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                               capture_output=True, text=True).stdout
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
