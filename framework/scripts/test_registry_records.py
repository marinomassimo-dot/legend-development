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

import derived_inputs  # noqa: E402
import registry_records as rr  # noqa: E402

REGISTRIES = ROOT / "disease-models/wwox/registries"
PAPERS = REGISTRIES / "paper_registry_current.md"
CLAIMS = REGISTRIES / "claim_registry_current.md"
LITLOG = REGISTRIES / "literature_tracking_log_current.md"
LEDGER = ROOT / "disease-models/wwox/research/discovery_ledger_current.md"

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


def ledger_leads_by_scan() -> dict[str, str]:
    """Each `DL-*` lead of the discovery ledger and its body, by a plain line scan: a lead
    starts at a `###`/`####` heading whose text, past any emoji, begins `DL-`, and runs to the
    next heading at its own level or above. Fenced lines are not headings."""
    leads: dict[str, list[str]] = {}
    open_lead, open_level, fenced = "", 0, False
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        match = None if fenced else re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if match:
            level, title = len(match.group(1)), match.group(2)
            if open_lead and level <= open_level:
                open_lead = ""
            if level in (3, 4) and re.match(r"^[^0-9A-Za-z]*DL-[A-Z]+-\d+", title):
                open_lead, open_level = title, level
                leads[title] = []
        if open_lead:
            leads[open_lead].append(line)
    return {head: "\n".join(body) for head, body in leads.items()}


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
        named = [n for n in found.notes if "discovery_ledger_current" in n]
        self.assertTrue(named, found.notes)
        self.assertIn("--id", " ".join(named))
        # D0 (2026-09-24): the ledger's leads are `###` records, so a mention inside one is a
        # RECORD hit carried whole — it used to be buried in a 100 KB+ `##` block and only
        # named. The expected set is a line scan, not the selector.
        expected = {head for head, body in ledger_leads_by_scan().items()
                    if "29724996" in re.findall(r"\b\d{7,8}\b", body)}
        got = {r.record_id for r, _ in found.hits if r.source == "discovery_ledger_current"}
        self.assertTrue(expected, "the fixture needs a ledger lead citing the PMID")
        self.assertEqual(expected, got)

    def test_a_section_is_still_reachable_when_it_is_asked_for_by_name(self) -> None:
        found = rr.select(ROOT, "wwox", record_id="Change-log", hops=0, open_sections=True)
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


class TheAnswerNamesTheTreeItWasReadFrom(unittest.TestCase):
    """🔴 A DIGEST SAYS THE BYTES MOVED; ONLY A COMMIT SAYS WHICH TREE THEY CAME FROM.

    Until 2026-09-18 an answer carried the record digest and the source-file digests and
    nothing else. A reader holding a quoted record whose digest no longer matches could not
    tell whether the registry had moved forward, whether they were on a different branch, or
    whether the quotation had been taken from an uncommitted edit that exists in no clone at
    all. The first two are answered by the commit; the third only by `DIRTY`.

    The tests below pin the property in all three of `derived_inputs`' states, and pin that
    adding the state changed no record — the failure a "harmless" envelope change makes is to
    re-normalise the bytes it is wrapping.
    """

    def _git(self, root: Path, *args: str) -> None:
        subprocess.run(["git", "-C", str(root), *args], check=True,
                       capture_output=True, text=True)

    def _workspace(self, tmp: str) -> Path:
        """A real git repository holding two registries, committed."""
        root = Path(tmp)
        registries = root / "disease-models/wwox/registries"
        registries.mkdir(parents=True)
        (registries / "paper_registry_current.md").write_text(
            "## PAPER 001\n**Identifier:** PMID 11111111 / DOI 10.1/x\n"
            "**Wikilinks:** [[claim_registry_current#CLAIM 001]]\n", encoding="utf-8")
        (registries / "claim_registry_current.md").write_text(
            "## CLAIM 001\n**Title:** the claim that exists\n", encoding="utf-8")
        self._git(root, "init", "--quiet")
        self._git(root, "config", "user.email", "t@example.invalid")
        self._git(root, "config", "user.name", "t")
        self._git(root, "add", "-A")
        self._git(root, "commit", "--quiet", "-m", "registries")
        return root

    def test_a_live_answer_carries_the_commit_it_was_read_at(self) -> None:
        found = rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1)
        block = found.repository
        self.assertIn(block["verdict"],
                      (derived_inputs.BOUND, derived_inputs.DIRTY, derived_inputs.UNBOUND))
        self.assertRegex(block["commit"], r"^[0-9a-f]{40}$")
        self.assertIn("disease-models/wwox/registries/paper_registry_current.md",
                      block["inputs"])

    def test_the_commit_reaches_the_json_envelope_and_the_rendered_form(self) -> None:
        done = subprocess.run(
            [sys.executable, str(ROOT / "framework/scripts/registry_records.py"),
             "get", "--pmid", AMBIGUOUS_PMID, "--json"],
            capture_output=True, text=True, cwd=str(ROOT))
        payload = json.loads(done.stdout)
        self.assertRegex(payload["repository"]["commit"], r"^[0-9a-f]{40}$")
        rendered = rr.render(rr.select(ROOT, "wwox", pmid=AMBIGUOUS_PMID, hops=1),
                             query="x")
        self.assertIn("read at commit", rendered)

    def test_an_uncommitted_registry_is_named_and_the_answer_is_still_given(self) -> None:
        """🔴 REPORTED, NEVER REFUSED. `derived_inputs.refuse_if_dirty` exists and is
        deliberately not called: this command is read-only, and refusing on a dirty tree would
        make the selective path fail during a BATCH_COMMIT — exactly when a reader most needs
        to look at the registries. The record still comes back; the answer says it is not in
        any clone."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = self._workspace(tmp)
            registry = root / "disease-models/wwox/registries/paper_registry_current.md"
            registry.write_text(registry.read_text(encoding="utf-8") +
                                "**Caveat:** added and not committed\n", encoding="utf-8")
            found = rr.select(root, "wwox", pmid="11111111", hops=1)
            self.assertEqual(derived_inputs.DIRTY, found.repository["verdict"])
            self.assertIn("disease-models/wwox/registries/paper_registry_current.md",
                          [row["path"] for row in found.repository["dirty_inputs"]])
            self.assertTrue(found.hits, "a dirty tree must not suppress the answer")
            line = rr.repository_line(found.repository)
            self.assertIn("WORKING TREE DIRTY", line)
            self.assertIn("not in any clone", line)

    def test_a_clean_tree_is_not_reported_dirty(self) -> None:
        """The anti-vacuity half: a detector that reports DIRTY always proves nothing."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = self._workspace(tmp)
            found = rr.select(root, "wwox", pmid="11111111", hops=1)
            self.assertEqual(derived_inputs.BOUND, found.repository["verdict"])
            self.assertEqual([], found.repository["dirty_inputs"])

    def test_outside_a_repository_the_state_is_unbound_and_says_so(self) -> None:
        """UNBOUND is a named state, never a pass — `derived_inputs`' own rule. The fixtures
        of this suite build plain temporary directories, so a guard that threw here would be
        removed the same day."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registries = root / "disease-models/wwox/registries"
            registries.mkdir(parents=True)
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 001\n**Identifier:** PMID 11111111\n", encoding="utf-8")
            found = rr.select(root, "wwox", pmid="11111111", hops=1)
            self.assertEqual(derived_inputs.UNBOUND, found.repository["verdict"])
            self.assertTrue(found.hits, "an unbound workspace must still answer")
            self.assertIn("UNBOUND", rr.repository_line(found.repository))

    def test_an_empty_result_also_names_the_tree_it_searched(self) -> None:
        """The refusal is a statement about a query over files; without the commit it is a
        statement about files nobody can identify."""
        found = rr.select(ROOT, "wwox", pmid="99999999", hops=1)
        self.assertEqual([], found.hits)
        self.assertRegex(found.repository["commit"], r"^[0-9a-f]{40}$")
        self.assertIn("read at commit", rr.render(found, query="pmid=99999999"))

    def test_naming_the_tree_changed_no_record(self) -> None:
        """🔴 THE ONLY WAY THIS CHANGE CAN DO HARM. The record bytes are the product; the
        envelope is packaging. Compared against an INDEPENDENT scan of the file, not against
        the selector's own earlier output."""
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0)
        record, _why = found.hits[0]
        self.assertEqual(record_text_by_scan(CLAIMS, CAVEAT_CLAIM), record.text)

    def test_the_block_names_only_files_this_call_opened(self) -> None:
        """Binding the answer to a file the call never read would claim a tree state it never
        observed. `--source` narrows the read; the block must narrow with it."""
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual(["disease-models/wwox/registries/claim_registry_current.md"],
                         found.repository["inputs"])

    def test_the_derived_index_names_its_tree_too(self) -> None:
        index = rr.build_index(ROOT, "wwox")
        self.assertRegex(index["repository"]["commit"], r"^[0-9a-f]{40}$")


class AFieldFilterReportsItsDenominator(unittest.TestCase):
    """🔴 THE FIELD VALUES IN THIS CORPUS ARE FREE PROSE, AND THAT IS THE WHOLE DESIGN PROBLEM.

    The roadmap that proposed this filter asked for `--status INFERENZA`. Two things are wrong
    with that sentence and both were found by measuring the corpus rather than by reading the
    proposal:

      - the epistemic level is declared in `Type`, not in `Status` — `Status` is the claim's
        lifecycle (`consolidated baseline`, `in observation`, `flagged for review`);
      - `Type` is compound prose. Of the 39 claim records, only a handful declare a bare level;
        the rest read `DATO + INFERENZA prudente`, `DATO (le misure) + IPOTESI (entrambe le
        spiegazioni)`, and so on.

    So exact matching would return 2 records and call them "the inferential claims"; substring
    matching returns 14 and would call the same thing by the same name. Neither is the answer.
    The filter therefore reports **the denominator and every distinct value it matched**, and
    lets the reader decide — the `identity` / `mention` rule, one field along.
    """

    def _independent_claim_scan(self, needle_field: str, needle_value: str) -> set[str]:
        """The expected set, derived WITHOUT the selector: a line scan over the raw file."""
        text = CLAIMS.read_text(encoding="utf-8")
        heads = list(re.finditer(r"^##[ \t]+(?P<id>\S.*?)[ \t]*$", text, re.M))
        found = set()
        for index, head in enumerate(heads):
            end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
            body = text[head.start():end]
            match = re.search(rf"^\*\*{needle_field}:\*\*\s*(.*)$", body, re.M)
            if match and needle_value.lower() in match.group(1).strip().lower():
                found.add(head.group("id").strip())
        return found

    def test_the_compound_values_really_are_in_the_corpus(self) -> None:
        """The fixture this class rests on. If claim `Type` ever becomes a closed vocabulary,
        this fails and the substring rule can be revisited — rather than silently outliving
        the corpus that justified it."""
        records = [item for item in rr.parse_records(ROOT, "wwox", "claim_registry_current")
                   if item.kind == "record"]
        types = [value for item in records for name, value in item.fields() if name == "Type"]
        compound = [value for value in types if "+" in value]
        self.assertTrue(compound, "no compound Type value: the substring rule needs revisiting")
        self.assertGreater(len(set(types)), 10, "Type is not the free prose this design assumes")

    def test_the_count_arrives_with_its_denominator_and_its_values(self) -> None:
        found = rr.select(ROOT, "wwox", constraints=[("Type", "INFERENZA")], hops=0,
                          sources=["claim_registry_current"])
        entry = found.field_report[0]
        self.assertEqual(len(self._independent_claim_scan("Type", "INFERENZA")),
                         entry["records_matching"])
        self.assertGreater(entry["records_declaring_the_field"], entry["records_matching"])
        bare = entry["distinct_values_matched"].get("INFERENZA", 0)
        self.assertLess(bare, entry["records_matching"],
                        "the point of the report is that the count is not the bare value")

    def test_the_selection_itself_matches_compound_values_not_only_bare_ones(self) -> None:
        """🔴 ADDED AFTER A SURVIVING MUTATION. Swapping the match to `==` left the whole class
        green: every case used `Status`, whose values happen to be exact, and the only case
        touching compound `Type` asserted on the REPORT rather than on the hits. The report and
        the selection are two code paths and they must be pinned separately."""
        expected = self._independent_claim_scan("Type", "INFERENZA")
        found = rr.select(ROOT, "wwox", constraints=[("Type", "INFERENZA")], hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual(expected, {record.record_id for record, _ in found.hits})
        compound = {record.record_id for record, _ in found.hits
                    if any(name == "Type" and value.strip() != "INFERENZA"
                           for name, value in record.fields())}
        self.assertTrue(compound, "no compound-valued record was selected; the fixture moved")

    def test_the_selection_agrees_with_an_independent_scan(self) -> None:
        expected = self._independent_claim_scan("Status", "consolidated baseline")
        found = rr.select(ROOT, "wwox", constraints=[("Status", "consolidated baseline")],
                          hops=0, sources=["claim_registry_current"])
        self.assertEqual(expected, {record.record_id for record, _ in found.hits})

    def test_a_filter_composes_with_another_selector_rather_than_replacing_it(self) -> None:
        both = rr.select(ROOT, "wwox", theme="myelin",
                         constraints=[("Status", "consolidated baseline")], hops=0,
                         sources=["claim_registry_current"])
        theme_only = rr.select(ROOT, "wwox", theme="myelin", hops=0,
                               sources=["claim_registry_current"])
        selected = {record.record_id for record, _ in both.hits}
        self.assertTrue(selected < {record.record_id for record, _ in theme_only.hits},
                        "the filter must narrow the theme selection, strictly")
        self.assertEqual(selected,
                         {record.record_id for record, _ in theme_only.hits}
                         & self._independent_claim_scan("Status", "consolidated baseline"))

    def test_an_unsatisfiable_filter_returns_nothing_rather_than_ignoring_itself(self) -> None:
        """Anti-vacuity: a filter that never removes anything is not a filter."""
        found = rr.select(ROOT, "wwox", theme="myelin",
                          constraints=[("Status", "in observation")], hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual(set(), self._independent_claim_scan("Status", "in observation")
                         & {"CLAIM 003", "CLAIM 004", "CLAIM 011", "CLAIM 014", "CLAIM 015"},
                         "the corpus changed; this case needs a new pair")
        self.assertEqual([], found.hits)

    def test_a_record_asked_for_by_name_is_not_withheld_by_a_filter(self) -> None:
        """`--id X --field Y=z` returning nothing would be indistinguishable from 'X does not
        exist', and this command's contract is that an empty result is never a silent one."""
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM,
                          constraints=[("Status", "a value no record carries")], hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual([CAVEAT_CLAIM], [record.record_id for record, _ in found.hits])
        self.assertEqual(0, found.field_report[0]["records_matching"])

    def test_an_unknown_field_is_a_named_refusal_with_a_suggestion(self) -> None:
        found = rr.select(ROOT, "wwox", constraints=[("Stato", "x")], hops=0,
                          sources=["claim_registry_current"])
        entry = found.field_report[0]
        self.assertTrue(entry["no_surface_declares_this_field"])
        self.assertIn("Status", entry["similar_field_names"])
        rendered = "\n".join(rr.field_report_lines(found.field_report))
        self.assertIn("NO SEARCHED SURFACE DECLARES A FIELD NAMED", rendered)
        self.assertIn("not about the corpus", rendered)

    def test_the_denominator_does_not_move_when_hops_widen_the_corpus(self) -> None:
        """🔴 The denominator is over the SEARCHED surfaces. A hop pulls other registries into
        the working corpus; a denominator that grew with it would answer a different question
        than the one asked. Found while wiring this, not after.

        🔴 THE FIELD MUST EXIST IN MORE THAN ONE SURFACE or this case is vacuous. The first cut
        used `Type`, which only the claim registry declares, so widening the corpus added zero
        and the mutation survived. `Status` is declared by both registries, and a wikilink from
        a claim reaches the paper registry at hop 1."""
        field = "Status"
        claims_only = len([item for item in rr.parse_records(ROOT, "wwox",
                                                             "claim_registry_current")
                           if item.kind == "record"
                           and any(name == field for name, _ in item.fields())])
        papers = len([item for item in rr.parse_records(ROOT, "wwox", "paper_registry_current")
                      if item.kind == "record"
                      and any(name == field for name, _ in item.fields())])
        self.assertGreater(papers, 0, f"{field} must exist in a second surface, or this is vacuous")
        counts = []
        for hops in (0, 2):
            found = rr.select(ROOT, "wwox", constraints=[(field, "baseline")], hops=hops,
                              sources=["claim_registry_current"])
            counts.append(found.field_report[0]["records_declaring_the_field"])
        self.assertEqual([claims_only, claims_only], counts,
                         "the denominator followed the hop expansion instead of the search")

    def test_the_filter_reads_declared_fields_and_not_the_prose(self) -> None:
        """A record whose Summary discusses an inference is not a record whose Type declares
        one. Asserted on a synthetic workspace so it cannot pass by corpus accident."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registries = root / "disease-models/wwox/registries"
            registries.mkdir(parents=True)
            (registries / "claim_registry_current.md").write_text(
                "## CLAIM 001\n**Identifier:** C1\n**Type:** DATO\n"
                "**Summary:** this paragraph discusses an INFERENZA at length\n\n"
                "## CLAIM 002\n**Identifier:** C2\n**Type:** INFERENZA\n"
                "**Summary:** plain\n", encoding="utf-8")
            found = rr.select(root, "wwox", constraints=[("Type", "INFERENZA")], hops=0,
                              sources=["claim_registry_current"])
            self.assertEqual(["CLAIM 002"], [record.record_id for record, _ in found.hits])

    def test_the_census_is_derived_and_writes_nothing(self) -> None:
        before = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                                capture_output=True, text=True).stdout
        census = rr.field_census(ROOT, "wwox", ["claim_registry_current"])
        after = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                               capture_output=True, text=True).stdout
        self.assertEqual(before, after)
        surface = census["surfaces"]["claim_registry_current"]
        self.assertEqual(len(self._independent_claim_scan("Status", "")),
                         surface["fields"]["Status"]["records"])

    def test_a_malformed_constraint_is_refused_rather_than_guessed(self) -> None:
        with self.assertRaises(ValueError):
            rr.parse_constraint("Status")
        with self.assertRaises(ValueError):
            rr.parse_constraint("=value")
        self.assertEqual(("Status", "in observation"),
                         rr.parse_constraint("Status=in observation"))
        self.assertEqual(("Note", "a=b"), rr.parse_constraint("Note=a=b"),
                         "only the first '=' separates; a value may contain one")


class TheSurfacePreambleTravelsWithTheAnswer(unittest.TestCase):
    """🔴 The bytes before the first `##` belong to no record, so selective retrieval dropped them.

    Measured on 2026-09-20: `parse_records` covers every byte of all seven surfaces contiguously
    EXCEPT 25 to 1,737 characters of header per file — and that header is where each registry
    says it is the de-identified public edition, that it is not medical advice, and (in the
    discovery ledger) what `DATO / INFERENZA / IPOTESI / ESPANSIONE` mean. A command that returns
    records whole and drops the file that defines their vocabulary loses the caveat one level
    above the one `CaseD` pins.
    """

    @staticmethod
    def _header_by_scan(stem: str) -> str:
        """Independent of the subject: re-read the file and cut at the first `##` by hand."""
        text = (ROOT / f"disease-models/wwox/{rr.SOURCES[stem]}").read_text(encoding="utf-8")
        return text.split("\n## ", 1)[0].strip()

    def test_the_preamble_is_carried_verbatim_for_a_consulted_surface(self) -> None:
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual(self._header_by_scan("claim_registry_current"),
                         found.preambles["claim_registry_current"])
        self.assertIn("Not medical advice", found.preambles["claim_registry_current"])

    def test_it_is_emitted_once_per_surface_in_the_rendered_answer(self) -> None:
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=0,
                          sources=["claim_registry_current"])
        rendered = rr.render(found, query="test")
        self.assertEqual(1, rendered.count("SURFACE PREAMBLE — claim_registry_current"),
                         "once per surface: a caveat repeated per hit is a caveat skimmed past")
        self.assertIn("Not medical advice", rendered)

    def test_the_epistemic_vocabulary_reaches_a_reader_of_the_discovery_ledger(self) -> None:
        """The concrete loss: `--field Type=...` filters on a vocabulary defined only in a header."""
        found = rr.select(ROOT, "wwox", theme="wwox", hops=0,
                          sources=["discovery_ledger_current"], limit=1)
        preamble = found.preambles["discovery_ledger_current"]
        for token in ("DATO", "INFERENZA", "IPOTESI", "ESPANSIONE"):
            self.assertIn(token, preamble)
        self.assertIn("Append-only", preamble)

    def test_a_surface_reached_only_by_a_hop_brings_its_preamble_too(self) -> None:
        """The two call sites must stay in step: a digest without a preamble is a file quoted
        without its own caveat."""
        found = rr.select(ROOT, "wwox", record_id=CAVEAT_CLAIM, hops=2,
                          sources=["claim_registry_current"])
        self.assertGreater(len(found.file_digests), 1, "the hop must have widened the surfaces")
        self.assertEqual(sorted(found.file_digests), sorted(found.preambles),
                         "every consulted surface carries a preamble entry")

    def test_the_json_envelope_carries_it_too(self) -> None:
        result = subprocess.run(
            [sys.executable, str(HERE / "registry_records.py"), "get", "--id", CAVEAT_CLAIM,
             "--hops", "0", "--source", "claim_registry_current", "--json", "--root", str(ROOT)],
            capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn("Not medical advice",
                      payload["surface_preambles"]["claim_registry_current"])

    def test_an_empty_result_still_states_the_frame_it_searched_under(self) -> None:
        found = rr.select(ROOT, "wwox", pmid="00000000", hops=0,
                          sources=["claim_registry_current"])
        self.assertEqual([], found.hits)
        self.assertIn("Not medical advice", rr.render(found, query="test"))


class WholeRecordsAtTheirMeasuredLevels(unittest.TestCase):
    """D1, on fixtures shaped like the seven surfaces as D0 measured them
    (governance/design_records/d0_registry_record_shapes_20260924.md). Each test fails on the
    `##`-only splitter it replaces; none adds a shape the census did not find."""

    FILES = {
        "registries/working_model_current.md":
            "# Working Model Current\n\nintro\n\n## Disease identity\nprose\n\n"
            "# BLOCK 1 — one-pager\n## 0) DATA vs INFERENCE\n### DATA\nd1\n## 1) ACTIVE\na1\n"
            "# BLOCK 2 — mirror\nm2\n",
        "research/dismissal_ledger_current.md":
            "# Dismissal Ledger\n\n## Why it exists\nw\n### The asymmetry\nx\n\n"
            "## Active rejections\n\n### DIS-001 — «first» → REOPENED\n- **Verdict:** v1\n\n"
            "### DIS-002 — «second» → FALSE\n- **Verdict:** v2\n\n## Closing\nc\n",
        "research/discovery_ledger_current.md":
            "# Discovery Ledger\n\n## MECH — indizi\n\n"
            "### DL-MECH-001 — plain lead\n- **Status**: open · **Tag**: IPOTESI\nPMID 12345678\n\n"
            "### 🔴 DL-MECH-029 — decorated lead\n- **Status**: maturing\n"
            "#### 🔴 AGGIUNTA 2026-08-10 — appended to 029\nkept with its record\n"
            "#### DL-MECH-029b — a lead nested in 029\nnested body\n\n"
            "### DL-MECH-030 — the next lead\nbody 30\n\n"
            "## Run 2026-07-09\nrun prose PMID 12345678\n\n"
            "### Update DL-MECH-001 — later news\nupdate body\n\n"
            "### Change-log\nfirst\n\n## Change-log\nsecond\n",
        "research/full_text_queue_current.md":
            "# FULL TEXT QUEUE\n\n## FT-157\n**Paper:** PMID 22222222\n### La domanda, risposta\n"
            "appended\n\n# FT-158 … FT-169 — twelve debts\ngroup intro\n\n## FT-158\n**Paper:** x\n",
        "registries/literature_tracking_log_current.md":
            "# Literature Tracking Log\n\n## Record template\n```\n## LIT-[NNN]\n"
            "**Identifier:** PMID [n]\n```\n\n## LIT-0001\n**Identifier:** PMID 33333333\n",
    }

    def setUp(self) -> None:
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for rel, text in self.FILES.items():
            path = self.root / "disease-models/wwox" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def get(self, record_id: str, **kw):
        return rr.select(self.root, "wwox", record_id=record_id, hops=0, **kw)

    def only(self, record_id: str) -> rr.Record:
        hits = [r for r, _ in self.get(record_id).hits]
        self.assertEqual(1, len(hits), [h.record_id for h in hits])
        return hits[0]

    def test_an_h1_block_is_a_record_holding_its_subsections(self) -> None:
        block = self.only("BLOCK 1")
        self.assertEqual(1, block.level)
        self.assertIn("### DATA\nd1\n## 1) ACTIVE\na1\n", block.text)
        self.assertNotIn("BLOCK 2", block.text, "a record ends at the next heading of its level")

    def test_a_record_ends_at_a_higher_heading_and_never_swallows_it(self) -> None:
        """`FT-157` used to carry `# FT-158 … FT-169` and its introduction."""
        ft157 = self.only("FT-157")
        self.assertIn("### La domanda, risposta\nappended", ft157.text, "nested blocks stay in")
        self.assertNotIn("twelve debts", ft157.text)
        self.assertNotIn("group intro", ft157.text)
        [mech] = [r for r, _ in self.get("Disease identity", open_sections=True).hits]
        self.assertNotIn("BLOCK 1", mech.text)

    def test_an_h3_ledger_record_is_addressable_between_its_neighbours(self) -> None:
        first = self.only("DIS-001")
        self.assertEqual(("Dismissal Ledger", "Active rejections"), first.heading_path)
        self.assertNotIn("DIS-002", first.text)
        second = self.only("DIS-002")
        self.assertNotIn("## Closing", second.text, "a higher heading ends the record")

    def test_decoration_is_not_identity_but_a_leading_word_is(self) -> None:
        decorated = self.only("DL-MECH-029")
        self.assertTrue(decorated.record_id.startswith("🔴 DL-MECH-029"))
        self.assertIn("appended to 029", decorated.text)
        definition = self.only("DL-MECH-001")
        self.assertTrue(definition.record_id.startswith("DL-MECH-001"),
                        "the update heading after it is not its identity")
        self.assertNotIn("later news", definition.text)

    def test_a_nested_record_is_addressable_and_named_by_its_parent(self) -> None:
        nested = self.only("DL-MECH-029b")
        self.assertEqual(4, nested.level)
        parent = self.only("DL-MECH-029")
        self.assertIn("nested body", parent.text, "the parent stays whole")
        self.assertEqual(("DL-MECH-029b",), parent.contains)

    def test_adjacent_records_do_not_bleed(self) -> None:
        self.assertNotIn("DL-MECH-030", self.only("DL-MECH-029").text)
        self.assertEqual("### DL-MECH-030 — the next lead\nbody 30\n\n", self.only("DL-MECH-030").text)

    def test_a_range_heading_is_not_the_first_occurrence_identity(self) -> None:
        record = self.only("FT-158")
        self.assertEqual(2, record.level)
        self.assertEqual("FT-158", record.record_id)
        self.assertEqual(("FT-158 … FT-169 — twelve debts",), record.heading_path)

    def test_a_heading_inside_a_fence_is_not_a_record(self) -> None:
        records = rr.parse_records(self.root, "wwox", "literature_tracking_log_current")
        self.assertEqual(["LIT-0001"], [r.record_id for r in records if r.kind == "record"])

    def test_a_bare_id_and_the_full_heading_reach_the_same_record(self) -> None:
        by_id, by_heading = self.only("DL-MECH-029"), self.only("🔴 DL-MECH-029 — decorated lead")
        self.assertEqual(by_id.line, by_heading.line)

    def test_a_mention_in_a_record_is_carried_and_one_in_a_section_is_named(self) -> None:
        found = rr.select(self.root, "wwox", pmid="12345678", hops=0)
        self.assertEqual(["DL-MECH-001 — plain lead"], [r.record_id for r, _ in found.hits])
        self.assertTrue(any("Run 2026-07-09" in note for note in found.notes), found.notes)

    def test_two_blocks_with_one_name_are_both_returned(self) -> None:
        """Keyed on the heading text, the second `Change-log` was silently dropped."""
        hits = [r for r, _ in self.get("Change-log", open_sections=True).hits]
        self.assertEqual([3, 2], [r.level for r in hits])

    def test_two_definitions_of_one_id_are_both_returned_and_named(self) -> None:
        path = self.root / "disease-models/wwox/research/dismissal_ledger_current.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n### DIS-001 — again\nx\n",
                        encoding="utf-8")
        found = self.get("DIS-001")
        self.assertEqual(2, len(found.hits))
        self.assertTrue(any("DEFINED as DIS-001" in item for item in found.ambiguous), found.ambiguous)

    def test_no_match_is_still_empty(self) -> None:
        self.assertEqual([], self.get("DL-MECH-999").hits)


class ThinDeterministicQueries(unittest.TestCase):
    """D2. Literal terms with an explicit `any`/`all`, and fields read in the declaration shapes
    D0 measured — bulleted only on the two ledgers that declare fields that way."""

    FILES = {
        "research/discovery_ledger_current.md":
            "# L\n\n## MECH\n\n"
            "### DL-MECH-001 — a\n- **Status**: maturing · **Tag**: DATO · **Fonte**: x · y\nGSK3 tau\n\n"
            "### DL-MECH-002 — b\n- **Status**: open · **Tag**: IPOTESI\nGSK3 only\n\n"
            "### DL-MECH-003 — c\n- **Status**: parked\ntau only\n",
        "research/dismissal_ledger_current.md":
            "# D\n\n## Active rejections\n\n### DIS-001 — r\n- **Verdict:** holds\n",
        "registries/claim_registry_current.md":
            "# C\n\n## CLAIM 001\n**Status:** in observation\n- **Status:** a bullet in prose\n",
    }

    def setUp(self) -> None:
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for rel, text in self.FILES.items():
            path = self.root / "disease-models/wwox" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def ids(self, found) -> list[str]:
        return [r.identity_id for r, _ in found.hits]

    def test_all_needs_every_term_and_any_needs_one(self) -> None:
        both = rr.select(self.root, "wwox", theme=["gsk3", "TAU"], match="all", hops=0)
        either = rr.select(self.root, "wwox", theme=["gsk3", "TAU"], match="any", hops=0)
        self.assertEqual(["DL-MECH-001"], self.ids(both))
        self.assertEqual(["DL-MECH-001", "DL-MECH-002", "DL-MECH-003"], self.ids(either))

    def test_each_term_reports_its_own_count(self) -> None:
        found = rr.select(self.root, "wwox", theme=["gsk3", "absent-term"], hops=0)
        self.assertEqual([], found.hits)
        counts = {e["term"]: e["records_containing"] for e in found.term_report}
        self.assertEqual({"gsk3": 2, "absent-term": 0}, counts)

    def test_the_order_is_the_files_order_every_time(self) -> None:
        runs = [self.ids(rr.select(self.root, "wwox", theme=["o"], match="any", hops=0))
                for _ in range(3)]
        self.assertEqual(runs[0], runs[1])
        self.assertEqual(runs[0], runs[2])

    def test_a_term_is_literal(self) -> None:
        self.assertEqual([], rr.select(self.root, "wwox", theme="GSK-3", hops=0).hits)

    def test_an_unknown_match_mode_is_refused(self) -> None:
        with self.assertRaises(ValueError):
            rr.select(self.root, "wwox", theme="x", match="some", hops=0)

    def test_ledger_fields_are_read_in_their_bulleted_shapes(self) -> None:
        found = rr.select(self.root, "wwox", constraints=[("Status", "maturing")], hops=0,
                          sources=["discovery_ledger_current"])
        self.assertEqual(["DL-MECH-001"], self.ids(found))
        report = found.field_report[0]
        self.assertEqual((3, 1), (report["records_declaring_the_field"], report["records_matching"]))
        dis = rr.select(self.root, "wwox", constraints=[("Verdict", "holds")], hops=0,
                        sources=["dismissal_ledger_current"])
        self.assertEqual(["DIS-001"], self.ids(dis))

    def test_several_fields_on_one_line_split_only_before_a_field_name(self) -> None:
        record = [r for r in rr.parse_records(self.root, "wwox", "discovery_ledger_current")
                  if r.identity_id == "DL-MECH-001"][0]
        self.assertEqual([("Status", "maturing"), ("Tag", "DATO"), ("Fonte", "x · y")],
                         record.fields())

    def test_a_bulleted_bold_lead_in_is_prose_on_other_surfaces(self) -> None:
        record = rr.parse_records(self.root, "wwox", "claim_registry_current")[-1]
        self.assertEqual([("Status", "in observation")], record.fields())


class LedgerFieldsOnTheRealCorpus(unittest.TestCase):
    def test_the_ledger_status_denominator_agrees_with_a_line_scan(self) -> None:
        expected = sum(1 for body in ledger_leads_by_scan().values()
                       if re.search(r"^\s*(?:[-*]\s+)?\*\*Status(?::\*\*|\*\*:)"
                                    r"|\s·\s\*\*Status(?::\*\*|\*\*:)", body, re.M))
        found = rr.select(ROOT, "wwox", constraints=[("Status", "")], hops=0,
                          sources=["discovery_ledger_current"])
        self.assertGreater(expected, 100)
        self.assertEqual(expected, found.field_report[0]["records_declaring_the_field"])


class NoMatchIsNotAToolError(unittest.TestCase):
    """D3. The exit status is how a caller tells an honest empty answer from a broken tool."""

    SCRIPT = HERE / "registry_records.py"

    def run_cli(self, root: Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(self.SCRIPT), "get", "--root", str(root), *args],
                              capture_output=True, text=True)

    def test_an_unreadable_registry_is_a_tool_error_not_a_no_match(self) -> None:
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            registries = Path(tmp) / "disease-models/wwox/registries"
            registries.mkdir(parents=True)
            (registries / "claim_registry_current.md").write_bytes(b"## CLAIM 001\n\xff\xfe\n")
            broken = self.run_cli(Path(tmp), "--id", "CLAIM 001")
            self.assertEqual(2, broken.returncode, broken.stderr)
            self.assertIn("TOOL ERROR", broken.stderr)
            (registries / "claim_registry_current.md").write_text("## CLAIM 001\nok\n",
                                                                  encoding="utf-8")
            self.assertEqual(0, self.run_cli(Path(tmp), "--id", "CLAIM 001").returncode)
            empty = self.run_cli(Path(tmp), "--id", "CLAIM 999")
            self.assertEqual(1, empty.returncode)
            self.assertIn("NO RECORD MATCHED", empty.stdout)

    def test_a_newly_addressable_ledger_record_carries_its_provenance(self) -> None:
        answer = json.loads(subprocess.run(
            [sys.executable, str(self.SCRIPT), "get", "--id", "DL-MECH-029", "--hops", "0",
             "--json"], capture_output=True, text=True, check=True).stdout)
        record = answer["records"][0]
        self.assertEqual("DL-MECH-029", record["identity_id"])
        self.assertEqual("disease-models/wwox/research/discovery_ledger_current.md", record["path"])
        self.assertTrue(record["heading_path"])
        self.assertEqual(64, len(record["record_digest"]))
        self.assertIn(answer["repository"]["verdict"], (derived_inputs.BOUND, derived_inputs.DIRTY))
        self.assertTrue(answer["repository"]["commit"])
        self.assertIn("discovery_ledger_current", answer["source_digests"])


class CatalogAndNavigation(unittest.TestCase):
    """D4. A catalog projected at call time and never stored; a named section answered with
    where it is and what it holds, loaded only when asked."""

    SCRIPT = HERE / "registry_records.py"

    def setUp(self) -> None:
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        ledger = self.root / "disease-models/wwox/research/discovery_ledger_current.md"
        ledger.parent.mkdir(parents=True)
        ledger.write_text(
            "# Ledger title\n\n## Run 2026-07-09 — a run\nrun prose\n\n"
            "### DL-MECH-001 — first\n- **Status**: open · **Tag**: IPOTESI\n\n"
            "### 🔴 DL-MECH-002 — second\n- **Tag**: DATO\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_naming_a_section_answers_with_navigation_not_its_text(self) -> None:
        found = rr.select(self.root, "wwox", record_id="Run 2026-07-09 — a run", hops=0)
        self.assertEqual([], found.hits)
        [nav] = found.navigation
        self.assertEqual(["DL-MECH-001", "DL-MECH-002"], nav["contains_records"])
        self.assertEqual(2, nav["level"])
        self.assertNotIn("run prose", json.dumps(nav))

    def test_a_section_opens_whole_only_when_asked(self) -> None:
        found = rr.select(self.root, "wwox", record_id="Run 2026-07-09 — a run", hops=0,
                          open_sections=True)
        [record] = [r for r, _ in found.hits]
        self.assertIn("run prose", record.text)
        self.assertIn("DL-MECH-002", record.text)

    def test_the_title_section_is_not_a_back_door_to_the_whole_file(self) -> None:
        found = rr.select(self.root, "wwox", record_id="Ledger title", hops=0)
        self.assertEqual([], found.hits)
        self.assertEqual(1, len(found.navigation))

    def test_navigation_alone_is_an_answer_not_an_empty_result(self) -> None:
        run = subprocess.run([sys.executable, str(self.SCRIPT), "get", "--root", str(self.root),
                              "--id", "Ledger title"], capture_output=True, text=True)
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        self.assertIn("HEADINGS NAMED BY THE QUERY", run.stdout)
        self.assertNotIn("NO RECORD MATCHED", run.stdout)

    def test_the_catalog_projects_records_and_declared_columns(self) -> None:
        table = rr.catalog(self.root, "wwox", ["discovery_ledger_current"], ["Status", "Tag"])
        self.assertEqual([("DL-MECH-001", "first", ["open"], ["IPOTESI"]),
                          ("DL-MECH-002", "second", [], ["DATO"])],
                         [(r["id"], r["title"], r["Status"], r["Tag"]) for r in table["rows"]])
        self.assertEqual(1, table["columns"]["Status"]["records_declaring_the_field"])
        self.assertEqual(2, table["columns"]["Status"]["records_catalogued"])

    def test_an_undeclared_column_is_a_named_refusal(self) -> None:
        table = rr.catalog(self.root, "wwox", ["discovery_ledger_current"], ["Stato"])
        self.assertTrue(table["columns"]["Stato"]["no_surface_declares_this_field"])
        self.assertIn("Status", table["columns"]["Stato"]["similar_field_names"])

    def test_the_catalog_writes_nothing(self) -> None:
        before = sorted(p.relative_to(self.root) for p in self.root.rglob("*"))
        subprocess.run([sys.executable, str(self.SCRIPT), "catalog", "--root", str(self.root),
                        "--column", "Status"], capture_output=True, text=True, check=True)
        self.assertEqual(before, sorted(p.relative_to(self.root) for p in self.root.rglob("*")))

    def test_the_real_dismissal_catalog_agrees_with_a_heading_scan(self) -> None:
        text = (ROOT / "disease-models/wwox/research/dismissal_ledger_current.md").read_text(
            encoding="utf-8")
        expected = re.findall(r"^### (DIS-\d+)", text, re.M)
        table = rr.catalog(ROOT, "wwox", ["dismissal_ledger_current"])
        self.assertEqual(expected, [row["id"] for row in table["rows"]])


class LedgerIdentityUpdatesAndHops(unittest.TestCase):
    """D6. A ledger id returns its definition; the later headings that name it stay findable
    beside it; hops follow declared wikilinks, to a caller's depth, without looping."""

    def setUp(self) -> None:
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        ledger = self.root / "disease-models/wwox/research/discovery_ledger_current.md"
        ledger.parent.mkdir(parents=True)
        ledger.write_text(
            "# L\n\n## MECH\n\n"
            "### DL-MECH-001 — a\nsee [[discovery_ledger_current#DL-MECH-002 — b]]\n\n"
            "### DL-MECH-002 — b\nsee [[discovery_ledger_current#DL-MECH-001 — a]] and "
            "[[discovery_ledger_current#DL-MECH-003 — c]] and [[discovery_ledger_current#^fm-1]]\n\n"
            "### DL-MECH-003 — c\nend of chain\n\n"
            "## Run 2026-07-26\n\n### STATUS UPDATE — DL-MECH-001 — later\nnews\n\n"
            "### DL-MECH-0010 — a different id\nx\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_the_definition_is_returned_and_the_update_heading_listed_beside_it(self) -> None:
        found = rr.select(self.root, "wwox", record_id="DL-MECH-001", hops=0)
        self.assertEqual(["DL-MECH-001"], [r.identity_id for r, _ in found.hits])
        related = [n["heading"] for n in found.navigation]
        self.assertEqual(["STATUS UPDATE — DL-MECH-001 — later"], related)
        self.assertNotIn("news", found.hits[0][0].text)

    def test_hops_are_caller_controlled_and_cycle_safe(self) -> None:
        one = rr.select(self.root, "wwox", record_id="DL-MECH-001", hops=1)
        self.assertEqual(["DL-MECH-001", "DL-MECH-002"], [r.identity_id for r, _ in one.hits])
        many = rr.select(self.root, "wwox", record_id="DL-MECH-001", hops=50)
        self.assertEqual(["DL-MECH-001", "DL-MECH-002", "DL-MECH-003"],
                         [r.identity_id for r, _ in many.hits])
        self.assertEqual("linked from DL-MECH-002 — b (hop 2)", many.hits[2][1])

    def test_a_block_reference_is_named_for_what_it_is(self) -> None:
        found = rr.select(self.root, "wwox", record_id="DL-MECH-002", hops=1)
        self.assertTrue(any("block reference" in item for item in found.unresolved), found.unresolved)

    def test_the_real_ledger_update_is_listed_beside_its_definition(self) -> None:
        found = rr.select(ROOT, "wwox", record_id="DL-MECH-017", hops=0)
        [definition] = [r for r, _ in found.hits]
        self.assertTrue(definition.record_id.startswith("DL-MECH-017"))
        self.assertTrue(any(n["heading"].startswith("STATUS UPDATE — DL-MECH-017")
                            for n in found.navigation), found.navigation)


class RetrievalAcceptanceBench(unittest.TestCase):
    """Representative real records on all seven surfaces, including every edge D0 found: the
    expected record is cut by an independent line scanner, never by the selector, and the
    selector must return exactly it — same line, same id, same bytes, one record. On the tool
    before D1 this bench scored 11 of 25; every miss was a retrieval-rule defect."""

    CASES = (
        ("registries/paper_registry_current.md", "PAPER 044", 2),
        ("registries/paper_registry_current.md", "CORPUS P206", 2),
        ("registries/paper_registry_current.md", "CORPUS-STUB-073", 2),
        ("registries/literature_tracking_log_current.md", "LIT-0405", 2),
        ("registries/literature_tracking_log_current.md", "LIT-EX-001", 2),
        ("registries/claim_registry_current.md", "CLAIM 030", 2),
        ("registries/working_model_current.md", "BLOCK 1", 1),
        ("registries/working_model_current.md", "BLOCK 3", 1),
        ("research/dismissal_ledger_current.md", "DIS-001", 3),
        ("research/dismissal_ledger_current.md", "DIS-012", 3),
        ("research/discovery_ledger_current.md", "DL-BIO-001", 3),
        ("research/discovery_ledger_current.md", "DL-MECH-029", 3),
        ("research/discovery_ledger_current.md", "DL-MECH-017", 3),
        ("research/discovery_ledger_current.md", "DL-MECH-069", 3),
        ("research/discovery_ledger_current.md", "DL-MECH-069b", 4),
        ("research/discovery_ledger_current.md", "DL-METH-107", 4),
        ("research/full_text_queue_current.md", "FT-022", 2),
        ("research/full_text_queue_current.md", "FT-062", 2),
        ("research/full_text_queue_current.md", "FT-069", 2),
        ("research/full_text_queue_current.md", "FT-157", 2),
        ("research/full_text_queue_current.md", "FT-158", 2),
    )

    @staticmethod
    def scan(path: Path, record_id: str, level: int) -> tuple[int | None, str]:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        fenced, start, out = False, None, []
        for index, line in enumerate(lines):
            if re.match(r"^[ \t]{0,3}(```|~~~)", line):
                fenced = not fenced
            match = None if fenced else re.match(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$",
                                                  line.rstrip("\r\n"))
            if start is None and match and len(match.group(1)) == level:
                title = re.sub(r"^[^0-9A-Za-z]+", "", match.group(2))
                if re.match(re.escape(record_id) + r"($|[\s—–:\-])", title, re.I):
                    start = index
                    out.append(line)
                    continue
            if start is not None:
                if match and len(match.group(1)) <= level:
                    break
                out.append(line)
        return (start + 1 if start is not None else None), "".join(out)

    def test_every_representative_record_comes_back_exactly(self) -> None:
        for rel, record_id, level in self.CASES:
            with self.subTest(record_id=record_id):
                path = ROOT / "disease-models/wwox" / rel
                line, text = self.scan(path, record_id, level)
                self.assertIsNotNone(line, "bad fixture: the scanner found no such record")
                found = rr.select(ROOT, "wwox", record_id=record_id, hops=0)
                records = [r for r, _ in found.hits]
                self.assertEqual(1, len(records), [r.record_id for r in records])
                self.assertEqual((line, record_id.lower(), level),
                                 (records[0].line, records[0].identity_id.lower(), records[0].level))
                self.assertEqual(text, records[0].text)
                self.assertEqual(f"disease-models/wwox/{rel}", records[0].path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
