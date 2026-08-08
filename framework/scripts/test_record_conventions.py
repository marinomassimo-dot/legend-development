#!/usr/bin/env python3
"""One definition of "a canonical record", and proof that every consumer uses it.

The paper registry has three heading conventions — `PAPER n`, `CORPUS Pn`, `CORPUS-STUB-n` —
and the literature log has two, `LIT-n` and `LIT-EX-n`. On 2026-08-08 five modules each held
a private list of which ones exist, and the shortest list was wrong: `coverage_report.py`
knew `PAPER n` and `CORPUS Pn` only.

The visible cost was a denominator 168 records short. The cost that mattered was different
in kind. **A heading a splitter does not recognise does not merely go uncounted — it does not
end the previous record.** The 168 stub bodies were absorbed into `PAPER 032`, the last
recognised heading before them, and every repeated `**Key:**` line overwrote that record's
own field. `PAPER 032` is the sole primary source of `CLAIM 026`; `coverage_report.py` and
the LINT registry-declaration ratchet both read its `Identifier` as `PMID 23446842`, a
different and *retracted* paper, and its `Status` as `not_processed` rather than
`claim_linked`. Receipt matching keys off that identifier.

So this suite guards three things, in increasing order of what they would have caught:

1. the consumers agree with the shared definition (catches a reverted or forked copy);
2. no module restates the definition (catches a *sixth* copy before it can drift);
3. no parsed record body contains a second record's fields (catches an unlisted convention
   that nobody has thought of yet — the general form of the 2026-08-08 defect).

Test 3 is the one that does not depend on knowing what went wrong.
"""

from __future__ import annotations

import ast
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[2] / ".claude" / "skills"
        / "legend-study-intake-triage" / "scripts"),
)

import batch_queue  # noqa: E402
import coverage_report as cov  # noqa: E402
import growth_anchors as ga  # noqa: E402
import legend_lint  # noqa: E402
import study_dedup_triage as triage  # noqa: E402
import unread_gold  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REGISTRIES = ROOT / "disease-models" / "wwox" / "registries"
PAPERS = REGISTRIES / "paper_registry_current.md"
LITERATURE = REGISTRIES / "literature_tracking_log_current.md"

# The field that decides a record's identity, and the one the defect overwrote.
IDENTIFIER_LINE = re.compile(r"(?m)^\*\*Identifier:\*\*")

# A string constant that both looks like a `## ` heading matcher and names a canonical record
# convention is a private copy of the shared definition. `^##\s+` alone is a generic fragment
# (`split_blocks` builds on it), and the commit-candidate heading `CC-yyyy-mm-dd-nnn` is not a
# canonical registry record — neither is an offender.
RECORD_KEYWORD = re.compile(r"PAPER|CORPUS|CLAIM|LIT-")

# Every module that names a canonical registry file is a candidate splitter and is scanned.
# Derived from disk, never hand-listed: the first version of this constant named three modules
# and a blind review found two *unscanned* modules carrying live, wrong copies. A list someone
# must remember to extend is the very defect this suite exists to prevent, one level up.
#
# `study_dedup_triage.py` is exempt from the AST scan and covered by a behavioural test
# instead: it is deliberately standard-library-only so the skill runs in a fresh clone, so it
# must restate the conventions rather than import them.
REGISTRY_FILENAMES = (
    "paper_registry_current.md",
    "literature_tracking_log_current.md",
    "claim_registry_current.md",
)
AST_SCAN_EXEMPT = {"study_dedup_triage.py", "growth_anchors.py"}


def splitter_modules() -> list[Path]:
    roots = [ROOT / "framework" / "scripts", ROOT / "scripts"]
    roots += sorted((ROOT / ".claude" / "skills").glob("*/scripts"))
    roots += sorted((ROOT / "disease-models").glob("*/analysis/scripts"))
    found = []
    for root in roots:
        for path in sorted(root.glob("*.py")) if root.is_dir() else []:
            # Test modules are exempt: a suite must be able to *construct* the wrong pattern
            # to prove the guard fails on it, and this file does exactly that below. The risk
            # being guarded is a production splitter drifting, not a fixture.
            if path.name in AST_SCAN_EXEMPT or path.name.startswith("test_"):
                continue
            source = path.read_text(encoding="utf-8")
            if any(name in source for name in REGISTRY_FILENAMES):
                found.append(path)
    return found


class SharedDefinitionTests(unittest.TestCase):
    def test_consumers_use_the_shared_paper_registry_pattern(self) -> None:
        """`is`, not `==`: a copy that happens to match today can be edited tomorrow."""
        self.assertIs(cov.ENTRY, ga.PAPER_REGISTRY_RECORD)
        self.assertIs(batch_queue.ENTRY, ga.PAPER_REGISTRY_RECORD)
        self.assertIs(cov.TRACKING_ENTRY, ga.HEADINGS["literature"])
        # legend_lint's was a function-local until a blind review swapped it for a *subset*
        # and this suite went 8/8 green. Nothing local can be pinned, so it is bound at module
        # level and pinned here.
        self.assertIs(legend_lint.PAPER_REGISTRY_RECORD, ga.PAPER_REGISTRY_RECORD)
        self.assertIs(unread_gold.BLOCK_RE, ga.HEADINGS["corpus"])

    def test_the_intake_skill_splitter_agrees_on_every_canonical_registry(self) -> None:
        """The one legitimate restatement, held to behavioural equivalence.

        `study_dedup_triage.py` ships inside a skill package and is standard-library-only by
        design, so it cannot import the shared definition. It may restate it; it may not
        disagree with it. Its looser INBOX/FT/CC conventions are out of scope here.
        """
        canonical = {
            REGISTRIES / "paper_registry_current.md": ga.PAPER_REGISTRY_RECORD,
            REGISTRIES / "literature_tracking_log_current.md": ga.HEADINGS["literature"],
        }
        for path, pattern in canonical.items():
            text = path.read_text(encoding="utf-8")
            mine = [" ".join(identifier.split()) for identifier in pattern.findall(text)]
            theirs = [
                identifier for identifier, _ in triage.split_blocks(text)
                if not identifier.startswith(("INBOX", "FT", "CC"))
            ]
            self.assertEqual(
                theirs,
                mine,
                f"{path.name}: the intake gate and growth_anchors disagree about which "
                f"headings are records. The intake gate is the authoritative classifier, so "
                f"a disagreement here misclassifies real studies",
            )

    def test_shared_pattern_covers_every_convention_actually_present(self) -> None:
        """Derived from the file, not from a list someone remembered to update.

        `**Identifier:**` is the probe because it is the field that decides identity — receipt
        matching keys off it, and it is what was overwritten in 2026-08-08. Prose sections
        (`## Registry rules`, the tier legends, the appendix preamble, the file header) carry
        bolded labels but no identifier, so they are excluded by the data rather than by a
        hand-kept skip list.

        A heading convention introduced by a future batch appears here as an identifier the
        shared pattern cannot account for, and fails, whatever it is called.
        """
        text = PAPERS.read_text(encoding="utf-8")
        # A bijection, not a count. Equal totals are satisfied by a pattern that loses one
        # real record and gains one prose heading — which is exactly the shape of the two
        # defects a blind review found in the unconsolidated splitters.
        entries = cov.parse_entries(text)
        self.assertEqual(
            len(IDENTIFIER_LINE.findall(text)),
            len(entries),
            "every '**Identifier:**' field must belong to its own recognised record",
        )
        without = [entry["_id"] for entry in entries if "identifier" not in entry]
        self.assertEqual(
            without,
            [],
            f"recognised records carrying no identifier: {without}. Either a prose heading is "
            f"being split as a record, or a real record lost its identifier to a neighbour",
        )

    def test_literature_pattern_sees_the_lit_ex_records(self) -> None:
        found = ga.HEADINGS["literature"].findall(LITERATURE.read_text(encoding="utf-8"))
        self.assertTrue(
            any(identifier.startswith("LIT-EX-") for identifier in found),
            "the six LIT-EX-nnn records are real records and must be counted",
        )

    def test_heading_re_refuses_an_unknown_convention(self) -> None:
        with self.assertRaises(KeyError):
            ga.heading_re("papers", "not_a_convention")


class NoPrivateCopyTests(unittest.TestCase):
    """No consumer may restate a heading pattern.

    Scanned through the AST, so an explanatory comment quoting the old regex — this file and
    three others carry one — is not mistaken for a live second definition. Only real string
    constants count.

    🔴 **The honest limit.** This detector requires one string constant holding both `^##\\s+`
    and a record keyword, so it is defeated by assembling the pattern from fragments — a blind
    review did exactly that and reintroduced the 2026-08-08 bug past this check. It is a
    lint against the *careless* second copy, not a proof of uniqueness. The guarantees that do
    not depend on how the pattern is spelled are `test_consumers_use_the_shared_paper_registry_pattern`
    (identity, not equality) and the contamination tests below. Overstating this one would be
    the same unearned assurance the receipt protocol refuses elsewhere.
    """

    def test_the_scan_actually_reaches_the_modules_that_matter(self) -> None:
        """A scan over an empty or accidentally-narrowed set passes vacuously."""
        names = {path.name for path in splitter_modules()}
        for required in ("coverage_report.py", "batch_queue.py", "legend_lint.py",
                         "unread_gold.py"):
            self.assertIn(required, names, "the AST scan no longer reaches this module")

    def test_no_consumer_declares_its_own_record_heading_regex(self) -> None:
        for path in splitter_modules():
            name = path.name
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            offenders = [
                node.value
                for node in ast.walk(tree)
                if isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and r"^##\s+" in node.value
                and RECORD_KEYWORD.search(node.value)
            ]
            self.assertEqual(
                offenders,
                [],
                f"{name} declares a record-heading pattern of its own: {offenders}. "
                f"Import it from growth_anchors.RECORD_PATTERNS instead",
            )


class NoContaminationTests(unittest.TestCase):
    """The general invariant: one record's body holds one record's fields.

    This does not know what `CORPUS-STUB` is, and that is the point. Whatever convention a
    future batch introduces, if a splitter cannot see it, the field it repeats will land in a
    neighbour's body and this fails.
    """

    def test_no_parsed_record_absorbs_a_neighbour(self) -> None:
        text = PAPERS.read_text(encoding="utf-8")
        for entry in cov.parse_entries(text):
            for key in ("Identifier", "Status", "Full title"):
                count = len(re.findall(rf"(?m)^\*\*{key}:\*\*", entry["_body"]))
                self.assertLessEqual(
                    count,
                    1,
                    f"{entry['_id']} contains {count} '{key}' fields: it has absorbed "
                    f"records the splitter cannot see, and its own field values have been "
                    f"overwritten by the last one absorbed",
                )

    def test_the_2026_08_08_defect_reproduces_without_the_shared_pattern(self) -> None:
        """The failing case, pinned. A guard that cannot fail proves nothing.

        Parsed with a splitter blind to `CORPUS-STUB`, `PAPER 001` reports the *stub's*
        identifier as its own. Parsed with the shared pattern, it reports its own.
        """
        fixture = (
            "## PAPER 001\n"
            "**Identifier:** PMID 30619736\n"
            "**Status:** claim_linked\n"
            "\n"
            "## CORPUS-STUB-001\n"
            "**Identifier:** PMID 23446842\n"
            "**Status:** not_processed\n"
        )
        blind = re.compile(r"(?m)^##\s+(PAPER\s+\d+|CORPUS\s+P\d+)\s*$")
        original = cov.ENTRY
        try:
            cov.ENTRY = blind
            contaminated = {e["_id"]: e for e in cov.parse_entries(fixture)}
            self.assertEqual(len(contaminated), 1)
            self.assertEqual(
                contaminated["PAPER 001"]["identifier"],
                "PMID 23446842",
                "the defect no longer reproduces; this test has stopped proving anything",
            )
            self.assertEqual(contaminated["PAPER 001"]["status"], "not_processed")
        finally:
            cov.ENTRY = original

        repaired = {e["_id"]: e for e in cov.parse_entries(fixture)}
        self.assertEqual(len(repaired), 2)
        self.assertEqual(repaired["PAPER 001"]["identifier"], "PMID 30619736")
        self.assertEqual(repaired["PAPER 001"]["status"], "claim_linked")
        self.assertEqual(repaired["CORPUS-STUB-001"]["identifier"], "PMID 23446842")

    def test_paper_032_resolves_to_its_own_study(self) -> None:
        """The live record the defect actually corrupted, named so a regression is legible.

        `PAPER 032` anchors `CLAIM 026`. Under the blind splitter its identifier resolved to
        PMID 23446842 — a retracted record under `PUBLICATION_INTEGRITY_HOLD`.
        """
        entries = {e["_id"]: e for e in cov.parse_entries(PAPERS.read_text(encoding="utf-8"))}
        self.assertIn("PAPER 032", entries)
        self.assertIn("30619736", entries["PAPER 032"].get("identifier", ""))
        self.assertNotIn("23446842", entries["PAPER 032"].get("identifier", ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
