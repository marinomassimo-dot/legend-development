#!/usr/bin/env python3
"""A provenance freeze may not pin a living file by whole-file hash.

`FREEZE_SCOPE_GATE` was written into `framework/eval/learned_gates_registry.md` on
2026-08-06 as prose, and prose is what already failed. The `append_only_prefix` pattern that
solves this problem lived *inside the very ledger* the DisMech baseline pinned by whole file,
one directory away, and was not adopted — because nothing made the two meet. A rule that
depends on the next author having read a registry is the same mechanism, restated more
eloquently.

So this is the rule as a check.

**What it refuses.** A freeze artefact that names, among its whole-file SHA-256 inputs, a file
the repository has declared to be *living*: one of the four canonical current files, which
change on every `BATCH_COMMIT`, or the append-only receipt ledger, which changes on every
single full-text read. Those sets are derived from `legend_lint.CURRENTS` and from
`fulltext_ledger_path` in the state manifest, never hardcoded here — a check that keeps its own
private copy of what "living" means drifts away from the thing it is checking.

**What it permits.** Pinning the same files by *scope*: an `append_only_prefix` (length +
digest of the prefix that existed at freeze), or an extracted set of blocks plus a revision.
Growth is legal; rewriting what you actually consumed is not. The distinction is the whole
point — a whole-file hash over living state does not report "my dependency changed", it
reports "the file moved", and it therefore fires constantly on irrelevant edits while being
unable to fire harder on the one edit that matters.

**The grandfathered instance** is the ratchet this repository already uses elsewhere
(`unread_premise_baseline`, `registry_only_fulltext_declarations_baseline`): the known
offender is pinned by identity so that resolving it is the only way the list shrinks, and any
*new* freeze with the same defect is a visible regression from the first commit that
introduces it.
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import legend_lint  # noqa: E402

STATE_MANIFEST = ROOT / "framework/state/state_manifest_current.md"

# Ways a freeze may legitimately pin a living file. Presence of any of these keys beside the
# path means the author chose a scope rather than the whole file.
SCOPED_PIN_KEYS = ("append_only_prefix", "prefix_sha256", "prefix_length", "scope",
                   "blocks", "revision", "extracted")

# 🔴 Known offender, 2026-08-06: `dismech_phase2_baseline.json` pins the two canonical
# registries by whole file. It broke on `BATCH_20260806_001` — over CLAIM 005, which is not
# even in its export scope of CLAIM 016/024/035.
#
# The receipt ledger is deliberately NOT listed, and the reason matters more than the entry.
# The same baseline pins it with `verification_policy: append_only_prefix`, `prefix_event_count`
# and `prefix_sha256` — correctly, three lines above the two that are wrong. The prose version
# of this gate, written minutes before this check existed, asserted the opposite: that the
# ledger was whole-file pinned and that the append-only pattern "was not adopted". This test
# refuted it on first run. That is the entire argument for executable gates over registry
# prose, demonstrated on the author of the prose.
#
# Grandfathered by exact identity, not by count, so the list cannot shrink by swapping one
# offender for another.
GRANDFATHERED = {
    "disease-models/wwox/analysis/data/dismech_phase2_baseline.json": {
        "claim_registry", "paper_registry"},
}


def living_files() -> set[str]:
    """Repository-relative paths of files declared to keep changing.

    Derived, never restated: the four canonical currents come from the LINT's own list, the
    receipt ledger from the state manifest that anchors it.
    """
    living = set(legend_lint.CURRENTS)
    match = re.search(r"^fulltext_ledger_path:\s*(\S+)\s*$",
                      STATE_MANIFEST.read_text(encoding="utf-8"), re.M)
    if match:
        living.add(match.group(1))
    return living


def freeze_artefacts() -> list[Path]:
    """Every freeze/baseline artefact carrying an `inputs` map of pinned paths."""
    found = []
    for path in sorted(ROOT.glob("disease-models/*/analysis/data/*baseline*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(payload, dict) and isinstance(payload.get("inputs"), dict):
            found.append(path)
    return found


def whole_file_pins_of_living_state(path: Path, living: set[str]) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    offending = set()
    for name, entry in (payload.get("inputs") or {}).items():
        if not isinstance(entry, dict):
            continue
        if str(entry.get("path", "")) not in living:
            continue
        if any(key in entry for key in SCOPED_PIN_KEYS):
            continue                      # pinned by scope, which is the permitted form
        if entry.get("sha256"):
            offending.add(name)
    return offending


class FreezeScope(unittest.TestCase):
    def test_at_least_one_freeze_artefact_is_checked(self) -> None:
        """A check that silently matches nothing is indistinguishable from a passing one."""
        self.assertTrue(freeze_artefacts(), "no freeze artefact found to check")

    def test_no_new_freeze_pins_living_state_by_whole_file(self) -> None:
        living = living_files()
        self.assertTrue(living, "could not derive the set of living files")
        new_offenders = {}
        for path in freeze_artefacts():
            relative = path.relative_to(ROOT).as_posix()
            offending = whole_file_pins_of_living_state(path, living)
            unexpected = offending - GRANDFATHERED.get(relative, set())
            if unexpected:
                new_offenders[relative] = sorted(unexpected)
        self.assertEqual(
            new_offenders, {},
            "these freezes pin a file the repository declares living, by whole-file hash:\n"
            + json.dumps(new_offenders, indent=2)
            + "\n\nFREEZE_SCOPE_GATE: freeze what you consumed, not the container it arrived "
              "in. An append-only ledger is pinned by prefix length and prefix digest; a "
              "canonical registry by the blocks actually consumed plus a revision. Growth is "
              "legal; rewriting what you consumed is not.")

    def test_the_grandfathered_defect_has_not_silently_resolved(self) -> None:
        """A ratchet that never falls is a wall; one that falls unnoticed is a lie.

        If the DisMech re-seal lands, this fails and the entry must be removed — which is the
        only way the list is allowed to shrink.
        """
        living = living_files()
        for relative, expected in GRANDFATHERED.items():
            path = ROOT / relative
            if not path.is_file():
                continue
            with self.subTest(freeze=relative):
                self.assertEqual(
                    whole_file_pins_of_living_state(path, living), expected,
                    f"{relative} no longer matches its grandfathered defect. If it was "
                    "re-sealed, delete its entry from GRANDFATHERED; if it grew a new "
                    "whole-file pin, that is a regression.")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
