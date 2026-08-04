#!/usr/bin/env python3
"""The verbatim-locator obligation must reach every route that can claim a complete read.

A rule that lives in one manual is bypassed by every route that does not mention it. That
is the same shape as the failure it exists to fix: on 2026-08-04 an export found that no
verbatim locator existed anywhere in the canonical state, across every complete read in the
ledger, because reading routes recorded conclusions and not quotations.

So this is not a documentation check. It fails when a new skill, agent, protocol or manual
starts instructing a `complete_fulltext_read` without carrying the obligation — which is the
moment the gap reopens, and the only moment at which it is cheap to close.

Adding a route means adding the rule to it, or declaring here why it is exempt. Both are
visible; neither is silence.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Detection is on the reading contract's vocabulary, not on one token. A route that stops
# writing `complete_fulltext_read` while still instructing a full-text reading would
# otherwise leave scope silently — found by falsifying this test against itself, where
# stripping the obligation also stripped the only occurrence of the token.
MARKERS = ("complete_fulltext_read", "FULLTEXT_READ_RECEIPT", "coverage map")
MARKER = MARKERS[0]          # the one an exemption must still name
OBLIGATION = "verbatim_locators"

# Files that name the depth without instructing anyone to produce one. Each needs a reason
# a reviewer can disagree with; "not a reading route" on its own is not one.
EXEMPT = {
    "framework/state/state_manifest_current.md":
        "state file: records counts and gates, instructs no reading",
    "framework/eval/learned_gates_registry.md":
        "registry of gates already learned; describes the depth, does not ask for one",
    "framework/protocols/session_self_evaluation.md":
        "post-hoc self-diagnosis: reads receipts that already exist, produces none",
    ".claude/skills/find-fulltext/SKILL.md":
        "retrieval only — it obtains the document and explicitly does not read it, so it has "
        "no statement to locate",
    ".claude/skills/legend-proband-priority-matrix/SKILL.md":
        "ranking aid over already-classified records; names the depth as an input attribute",
    ".claude/skills/legend-batch-inferential-sweep/SKILL.md":
        "emits queried_not_full_read or retrieved_not_read by design and says so; it states "
        "that neither removes reading debt nor permits a complete receipt",
    ".claude/skills/legend-hypothesis-forge/SKILL.md":
        "consumes an existing receipt and its dossier; it queries the ledger first and "
        "produces no reading of its own",
    ".claude/skills/legend-paperqa/SKILL.md":
        "RAG over the corpus; its own text states a query does not emit a complete receipt "
        "and does not remove a paper from reading debt",
}

# Only instruction surfaces are in scope: places where an agent is told what to do. A
# registry, a generated report, an analysis write-up or a script names the depth as data and
# instructs nobody, so requiring the rule there would be noise — and noise is how a guard
# gets switched off.
INSTRUCTION_SURFACES = (
    "CLAUDE.md", "AGENTS.md",
    ".claude/skills/*/SKILL.md",
    ".claude/agents/*.md",
    "framework/manuals/*.md",
    "framework/protocols/*.md",
    "framework/instruction/*.md",
)


def candidate_files() -> list[Path]:
    found: list[Path] = []
    for pattern in INSTRUCTION_SURFACES:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file() or path.name.startswith("test_"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if any(marker in text for marker in MARKERS):
                found.append(path)
    return found


class ObligationReachesEveryRoute(unittest.TestCase):
    def test_every_route_carries_the_obligation_or_declares_an_exemption(self) -> None:
        missing = []
        for path in candidate_files():
            relative = str(path.relative_to(ROOT))
            text = path.read_text(encoding="utf-8", errors="replace")
            if OBLIGATION in text or relative in EXEMPT:
                continue
            missing.append(relative)
        self.assertFalse(
            missing,
            "these instruct or describe a complete full-text read without the verbatim-locator "
            "obligation, and without a declared exemption:\n  " + "\n  ".join(sorted(missing)) +
            "\n\nAdd the rule, or add the path to EXEMPT with a reason.")

    def test_exemptions_still_exist_and_still_name_the_depth(self) -> None:
        """An exemption for a file that moved or stopped mentioning the depth is stale."""
        for relative, reason in sorted(EXEMPT.items()):
            with self.subTest(path=relative):
                path = ROOT / relative
                self.assertTrue(path.exists(), f"exempted path is gone: {relative}")
                text = path.read_text(encoding="utf-8", errors="replace")
                self.assertTrue(any(marker in text for marker in MARKERS),
                                f"exemption no longer needed, remove it: {relative}")
                self.assertGreater(len(reason), 40,
                                   "an exemption needs an argument, not a label")

    def test_the_normative_home_states_the_rule(self) -> None:
        """The receipt protocol is where the depth contract lives; the rule belongs there."""
        protocol = (ROOT / "framework/protocols/fulltext_read_receipt.md").read_text(
            encoding="utf-8")
        self.assertIn(OBLIGATION, protocol)
        self.assertIn("does not attest", protocol,
                      "the protocol must say what a receipt does NOT attest")

    def test_the_bootstrap_states_the_rule(self) -> None:
        """CLAUDE.md is read at the start of every session; a rule absent there is optional."""
        for name in ("CLAUDE.md", "AGENTS.md"):
            with self.subTest(file=name):
                self.assertIn(OBLIGATION, (ROOT / name).read_text(encoding="utf-8"))

    def test_the_gate_actually_enforces_it(self) -> None:
        """Prose without a gate is advice. The manifest validator must require the section."""
        gate = (ROOT / "framework/scripts/deepdive_manifest.py").read_text(encoding="utf-8")
        self.assertIn(OBLIGATION, gate)
        self.assertIn("SECTIONS", gate)
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "deepdive_manifest", ROOT / "framework/scripts/deepdive_manifest.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertIn(OBLIGATION, module.SECTIONS)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
