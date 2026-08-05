#!/usr/bin/env python3
"""Mutation battery: put known defects back and require every guard to refuse them.

A guard nobody has seen fail is a guard nobody knows works. Each entry below is a defect that
really shipped in this repository — most of them within a single session — and the battery
reintroduces it, then asserts the corresponding test refuses it.

Two passes, and the second is the one that matters:

* **one at a time** — does each guard fire on its own defect?
* **all at once** — does any guard MASK another? A suite where breaking twelve things fails
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
    "disease-models/wwox/analysis/scripts/export_dismech_dryrun.py",
    "disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py",
    "AGENTS.md",
    "framework/scripts/pubmed_corpus_harvest.py",
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
            "        elif indexed is False:", "        elif False:")),
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
        drop_line("AGENTS.md", "A local abstract corpus is not evidence")),
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
            "    if len(seen) != count:", "    if False:")),
    "executable bit stripped": (
        "scripts/test_release_surface.py",
        chmod_off("framework/scripts/pubmed_corpus_harvest.py")),
}


def run(target: str) -> int:
    return subprocess.run([sys.executable, target], cwd=ROOT,
                          capture_output=True, text=True).returncode


def main() -> int:
    snapshot()
    print("=== ONE AT A TIME — each defect against its guard\n")
    caught = stale = 0
    for name, (target, apply) in DEFECTS.items():
        restore()
        problem = apply()
        if problem:
            stale += 1
            print(f"  [STALE ANCHOR ]  {name}: {problem}")
            continue
        failed = run(target) != 0
        caught += failed
        print(f"  [{'CAUGHT' if failed else 'ESCAPED':<13}]  {name}")
    print(f"\n  {caught}/{len(DEFECTS)} caught · {stale} stale anchor(s)")
    if stale:
        print("  A stale anchor is not a pass: the defect was never reintroduced, so the "
              "guard was never tested. Update it.")

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

    ok = caught == len(DEFECTS) and not stale and failing == len(targets)
    print(f"\nVERDICT: {'PASS' if ok else 'FAIL'} — target restored")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        print("usage: guard_mutation_battery.py <path-to-a-throwaway-checkout>")
        raise SystemExit(2)
    raise SystemExit(main())
