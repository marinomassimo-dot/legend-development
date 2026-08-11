#!/usr/bin/env python3
"""Mutation battery: put known defects back and require every guard to refuse them.

A guard nobody has seen fail is a guard nobody knows works. Each entry below is a defect that
really shipped in this repository — most of them within a single session — and the battery
reintroduces it, then asserts the corresponding test refuses it.

Two passes, and the second is the one that matters:

* **one at a time** — does each guard fire on its own defect?
* **all at once** — does any guard MASK another? A suite where breaking many things fails
  three tests has blind spots that per-defect testing cannot reveal, because each defect was
  measured while everything else was healthy.

Two lessons are baked into the design, both learned the hard way here:

* **A mutation must actually remove the property under test.** The first run replaced a bullet's
  heading in `AGENTS.md` and left the rule itself in place, then reported a guard gap that did
  not exist. `drop_line` removes the whole line for that reason.
* **A stale anchor proves nothing and must not read as a pass.** If a mutation's anchor no
  longer matches, the defect was never reintroduced, so the guard was never tested. That is
  reported as `ANCORA STANTIA` and counted separately from a catch.

It MUTATES its target, so it takes an explicit path and must never be pointed at the working
tree:

    git archive HEAD | tar -x -C /tmp/clone
    python3 scripts/guard_mutation_battery.py /tmp/clone
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

TOUCHED = [
    ".claude/agents/legend-deepdive.md",
    "framework/scripts/deepdive_manifest.py",
    "framework/scripts/fulltext_receipts.py",
    "disease-models/wwox/analysis/scripts/export_dismech_dryrun.py",
    "disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py",
    "AGENTS.md",
    "framework/scripts/pubmed_corpus_harvest.py",
    "scripts/public_release_gate.py",
]
SNAPSHOT: dict[str, bytes] = {}
MODES: dict[str, int] = {}


def snapshot() -> None:
    for rel in TOUCHED:
        SNAPSHOT[rel] = (ROOT / rel).read_bytes()
        MODES[rel] = (ROOT / rel).stat().st_mode


def restore() -> None:
    """Restore from an in-memory copy — no git in the throwaway checkout, because blanket
    staging is blocked repository-wide and rightly so."""
    for rel, blob in SNAPSHOT.items():
        (ROOT / rel).write_bytes(blob)
        (ROOT / rel).chmod(MODES[rel])


def sub(rel: str, old: str, new: str):
    def apply() -> str | None:
        path = ROOT / rel
        text = path.read_text()
        if old not in text:
            return f"anchor not found in {rel}"
        path.write_text(text.replace(old, new, 1))
        return None
    return apply


def drop_line(rel: str, marker: str):
    def apply() -> str | None:
        path = ROOT / rel
        lines = path.read_text().splitlines(keepends=True)
        kept = [line for line in lines if marker not in line]
        if len(kept) == len(lines):
            return f"marker not found in {rel}"
        path.write_text("".join(kept))
        return None
    return apply


def chmod_off(rel: str):
    def apply() -> str | None:
        path = ROOT / rel
        path.chmod(path.stat().st_mode & ~0o111)
        return None
    return apply


DEFECTS = {
    "locator rule removed from an agent": (
        "scripts/test_locator_obligation_reaches_every_route.py",
        sub(".claude/agents/legend-deepdive.md", "verbatim_locators", "VERBATIM-REMOVED")),
    "waived:false read as a waiver": (
        "framework/scripts/test_deepdive_manifest.py",
        sub("framework/scripts/deepdive_manifest.py",
            "if waiver is None or waiver is False:", "if waiver is None:")),
    "elision check removed": (
        "framework/scripts/test_deepdive_manifest.py",
        sub("framework/scripts/deepdive_manifest.py",
            "if ELISION_RE.search(snippet):", "if False:")),
    "abstract-anchor requirement removed": (
        "framework/scripts/test_deepdive_manifest.py",
        sub("framework/scripts/deepdive_manifest.py",
            "        if indexed is False:", "        if False:")),
    "PubMed abstract accepted as complete source": (
        "framework.scripts.test_fulltext_receipts.FulltextReceiptTests.test_new_complete_receipt_refuses_pubmed_abstract_url",
        sub("framework/scripts/fulltext_receipts.py",
            "if ABSTRACT_ONLY_LOCATOR.search(str(receipt.get(\"source_locator\") or \"\")):",
            "if False and ABSTRACT_ONLY_LOCATOR.search(str(receipt.get(\"source_locator\") or \"\")):")),
    "remote source accepted for authoritative complete read": (
        "framework.scripts.test_fulltext_receipts.FulltextReceiptTests.test_authoritative_complete_read_requires_local_snapshot",
        sub("framework/scripts/fulltext_receipts.py",
            'if receipt.get("source_kind") != "fulltext_local":', "if False:")),
    "authoritative append skips the work manifest": (
        "framework.scripts.test_fulltext_receipts.FulltextReceiptTests.test_direct_append_to_authoritative_sink_cannot_skip_work_manifest",
        # 🔴 Re-anchored 2026-08-11, and the first attempt was too weak to mean anything:
        # flipping `strict=True` to `False` was ESCAPED, because `load_and_validate` still
        # runs and a missing manifest still errors. `strict` governs how hard the manifest is
        # checked, not whether it is required — so the defect this entry names is the call not
        # happening at all. A mutation that the guard survives is not evidence the guard
        # works; it is evidence the mutation was not the defect.
        sub("framework/scripts/fulltext_receipts.py",
            "        require_work_manifest(",
            "        (lambda *a, **k: None)(")),
    "declared manifest gaps accepted before append": (
        "framework.scripts.test_fulltext_receipts.FulltextReceiptTests.test_declared_manifest_gap_blocks_a_new_complete_read",
        sub("framework/scripts/fulltext_receipts.py",
            "    if strict and incomplete:", "    if False:")),
    "schema-v2 locator surface made optional": (
        "framework.scripts.test_deepdive_manifest.EntriesMustBeUsable.test_schema_v2_requires_surface_on_every_locator",
        sub("framework/scripts/deepdive_manifest.py",
            "                if schema_version >= 2 and surface is None:",
            "                if False:")),
    "one abstract locator accepted as evidence": (
        "framework.scripts.test_deepdive_manifest.EntriesMustBeUsable.test_schema_v2_refuses_even_one_abstract_evidence_locator",
        sub("framework/scripts/deepdive_manifest.py",
            '                if schema_version >= 2 and surface == "abstract":',
            "                if False:")),
    "text locator no longer checked against artifact": (
        "framework.scripts.test_deepdive_manifest.EntriesMustBeUsable.test_strict_verification_distinguishes_abstract_from_body",
        sub("framework/scripts/deepdive_manifest.py",
            "                        matched, mode = _quote_matches(snippet, body_text)",
            "                        matched, mode = _quote_matches(\n"
            "                            snippet, body_text + abstract_text)")),
    "routing basis hardcoded again": (
        "disease-models/wwox/analysis/scripts/test_export_dismech_dryrun.py",
        sub("disease-models/wwox/analysis/scripts/export_dismech_dryrun.py",
            "    exportable = bool(backed)", "    exportable = False")),
    "stale-sidecar refusal disabled": (
        "disease-models/wwox/analysis/scripts/test_export_dismech_dryrun.py",
        sub("disease-models/wwox/analysis/scripts/export_dismech_dryrun.py",
            "    target = path or SIDECAR", "    return None\n    target = path or SIDECAR")),
    "closed-world assertion reintroduced": (
        "scripts/test_no_closed_world_assertions_on_live_state.py",
        sub("disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py",
            "self.assertEqual(set(by_paper), expected,",
            'self.assertEqual(set(by_paper), {"055", "056"},')),
    "corpus rule removed from AGENTS.md": (
        "scripts/test_abstract_corpus_is_not_evidence.py",
        drop_line("AGENTS.md", "A local abstract corpus is not full-text evidence")),
    "corpus declared evidential": (
        "scripts/test_abstract_corpus_is_not_evidence.py",
        sub("framework/scripts/pubmed_corpus_harvest.py",
            '"evidential_status": "NOT_EVIDENCE",', '"evidential_status": "EVIDENCE",')),
    "book records dropped again": (
        "framework/scripts/test_pubmed_corpus_harvest.py",
        sub("framework/scripts/pubmed_corpus_harvest.py",
            'PARSERS = {"PubmedArticle": _parse_article, "PubmedBookArticle": _parse_book}',
            'PARSERS = {"PubmedArticle": _parse_article}')),
    "completeness invariant removed": (
        "framework/scripts/test_pubmed_corpus_harvest.py",
        sub("framework/scripts/pubmed_corpus_harvest.py",
            "    if len(seen) + len(deleted) != count:", "    if False:")),
    # 🔴 This entry reported ESCAPED for as long as it has existed, and it was never a guard
    # gap. Its target derives its population from `git ls-files`, and the throwaway export
    # this docstring prescribes — `git archive HEAD | tar -x` — has no index, so the check ran
    # over nothing and passed. The target now refuses an empty index, which turns this into an
    # honest BASELINE RED here and a real check in a checkout. Testing it inside the battery
    # would mean making the throwaway a git repository, which is a change to the battery's
    # contract and not something to smuggle in beside a mutation.
    "executable bit stripped": (
        "scripts/test_release_surface.py",
        chmod_off("framework/scripts/pubmed_corpus_harvest.py")),
    # 🔴 The publication gate had no entry here at all until 2026-08-11 — the one guard whose
    # failure ships something irreversible was the one whose tests were never mutated.
    "parental vocabulary narrowed back to the possessive": (
        "scripts.test_public_release_gate.GateTests"
        ".test_the_bare_parental_nouns_are_detected",
        sub("scripts/public_release_gate.py",
            'MATERNAL_WORDS = r"maternal(?:ly)?|mothers?(?:\'s?)?|materno|materna|madre"',
            'MATERNAL_WORDS = r"maternal(?:ly)?|mother\'?s|materno|materna|madre"')),
    # The regression this one pins is not a typo, it is a habit: editing one of two lists that
    # say the same thing. That is how the escape hatch came to recognise more parental
    # language than the net it suppresses.
    "escape hatch given its own vocabulary again": (
        "scripts.test_public_release_gate.GateTests"
        ".test_the_escape_hatch_is_never_wider_than_the_net",
        sub("scripts/public_release_gate.py",
            'subject = rf"(?:{PARENT_OF_ORIGIN_WORDS}|{MATERNAL_WORDS}|{PATERNAL_WORDS})"',
            'subject = r"(?:parent[- ]of[- ]origin|maternal|paternal)"')),
}


def run(target: str) -> int:
    command = ([sys.executable, target] if target.endswith(".py")
               else [sys.executable, "-m", "unittest", target])
    return subprocess.run(command, cwd=ROOT,
                          capture_output=True, text=True).returncode


def main() -> int:
    snapshot()
    print("=== ONE AT A TIME — each defect against its guard\n")
    # 🔴 A target that is ALREADY red proves nothing when it goes red again. The battery
    # reported 19/19 while one of them — test_release_surface, red in any working tree that
    # still has files/ or staging/ — would have counted as CAUGHT with the guard deleted.
    # That is the battery committing, inside itself, the exact defect it exists to detect.
    baseline = {}
    for target in sorted({t for t, _a in DEFECTS.values()}):
        baseline[target] = run(target) == 0

    caught = stale = unusable = 0
    for name, (target, apply) in DEFECTS.items():
        restore()
        if not baseline[target]:
            unusable += 1
            print(f"  [BASELINE RED ]  {name}: {Path(target).name} already fails unmutated, "
                  "so its result carries no information here")
            continue
        problem = apply()
        if problem:
            stale += 1
            print(f"  [STALE ANCHOR ]  {name}: {problem}")
            continue
        failed = run(target) != 0
        caught += failed
        print(f"  [{'CAUGHT' if failed else 'ESCAPED':<13}]  {name}")
    testable = len(DEFECTS) - unusable
    print(f"\n  {caught}/{testable} caught · {stale} stale anchor(s) · "
          f"{unusable} untestable in this environment")
    if stale:
        print("  A stale anchor is not a pass: the defect was never reintroduced, so the "
              "guard was never tested. Update it.")
    if unusable:
        print("  A red baseline is not a pass either. Run against a clean export "
              "(git archive HEAD) where those targets are green.")

    print("\n=== ALL AT ONCE — does any guard mask another?\n")
    restore()
    applied = sum(1 for _name, (_target, apply) in DEFECTS.items() if apply() is None)
    targets = sorted({target for target, _apply in DEFECTS.values()})
    results = {target: run(target) for target in targets}
    for target in targets:
        state = "FAILS" if results[target] else "PASSES — MASKED"
        print(f"  [{state:<16}]  {Path(target).name}")
    failing = sum(1 for code in results.values() if code)
    print(f"\n  {applied} simultaneous defects · {failing}/{len(targets)} targets fail")
    restore()

    ok = caught == testable and not stale and not unusable and failing == len(targets)
    print(f"\nVERDICT: {'PASS' if ok else 'FAIL'} — target restored")
    if not ok and unusable and caught == testable and not stale:
        print("  (every testable defect was caught; the run is incomplete, not failing)")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        print("usage: guard_mutation_battery.py <path-to-a-throwaway-checkout>")
        raise SystemExit(2)
    raise SystemExit(main())
