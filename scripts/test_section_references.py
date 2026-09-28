#!/usr/bin/env python3
"""A `§NN` cross-reference into a named file must resolve to a section that file has.

🔴 WHY THIS EXISTS
------------------
Two checks already guard deep links: `test_link_targets.py` resolves Markdown fragments and
LEGEND wikilinks, and `test_fresh_clone_reader_journey.py` resolves inline repository paths.
Neither reads the *section number* that a sentence cites, so a reference of the form

    `LEGEND_CORE` §26 forbids answering a scientific mistake with a new gate ...

was unchecked in both directions: the file resolved, the path resolved, and the section did
not exist. `LEGEND_CORE.md` ends at `## 22. FINAL MAXIMS`; the rule meant is the operator's
**task directive** §26, which is how every commit candidate in the repository cites it and
which `governance/candidates/CAND-20260819-ORCHSURF.md:444` had already disambiguated in
writing (*"directive §26, not body §26"*). That defect sat live on `main` from 2026-09-22 to
2026-09-28 in two files — the V0 proposal and the shipped skill — on the one sentence the
proposal itself calls *"the one design constraint that outranks everything below."* It was
caught once, on 2026-09-22, by a session whose branch never merged, and nothing noticed for
six days. An unresolvable `§NN` is the same defect class as an unresolvable path, so it gets
the same kind of instrument.

🔴 WHAT THE GATE COVERS, AND WHY IT IS NOT THE WHOLE REPOSITORY
--------------------------------------------------------------
The failing assertion covers the **normative surface** — the files a reader is told to obey:
the root documents, `framework/instruction|master|protocols|manuals|state`, `roles/`,
`.claude/skills/` and the governance body and annexes. Those are the references a reader must
be able to follow, and they are the files an actor may repair at T0.

Dated analysis records, hostile reviews, session evaluations, commit candidates and ledger
checkpoints are **censused, not gated** (`--census`). Two reasons, both measured rather than
assumed: the first run found 82 unresolvable references repository-wide against 3 on the
normative surface, and most of the 82 sit under `disease-models/`, which changes only through
`BATCH_COMMIT`. A gate that can only be satisfied by editing a file the protocol forbids
editing outside a batch is a gate that gets disabled. The census is there so the number stays
visible instead of being rounded to zero.

🔴 WHAT COUNTS AS A SECTION OF THE TARGET
-----------------------------------------
Headings (`## 21c. STOP POLICY`, `## S.6 · Preservation`, `## §0 · ...`) **and** line-initial
bold definitions (`**S.6.3 — Held as HAZARD, not authority:**`). The second form is not a
nicety: `legend_operating_convention_v1.md` defines S.6.1–S.6.7 that way, so a heading-only
extractor reported `LEGEND_CORE.md:508` — a provenance callout inside §21e, which is reserved
to the operator — as a defect it is not. A checker whose first false positive points at
reserved text is a checker nobody will be allowed to fix.

An ancestor resolves: `§4` is satisfied by a file that defines `4.0` but no bare `4`, because
a reader looking for §4 finds it. A label must contain a digit, so `§A` / `§Phase` and prose
capitals are out of the population rather than guessed at.

🔴 THERE IS DELIBERATELY NO "THIS ONE IS AN EXAMPLE" LIST
--------------------------------------------------------
`test_link_targets.EXAMPLE_FRAGMENT` is an allow-list of placeholder spellings, and an
allow-list is a place to put the next real defect. Here the escape is in the citation instead:
a document that must *quote* a wrong reference writes it without backticks, which is what the
repair callout in `LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md` does. The checker found
that on its own first run against the repaired file, which is the cheapest possible proof that
it reads what a reader reads.

Run: `python3 scripts/test_section_references.py`
     `python3 scripts/test_section_references.py --census`   # repository-wide, prints, exits 0
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# One definition of "this directory is another checkout", shared with the publication gate and
# with `test_link_targets.py`: a worktree mounted inside this one is not part of this audit.
_GATE_PATH = Path(__file__).with_name("public_release_gate.py")
_SPEC = importlib.util.spec_from_file_location("public_release_gate", _GATE_PATH)
assert _SPEC and _SPEC.loader
GATE = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = GATE
_SPEC.loader.exec_module(GATE)

# `backup/` holds the byte-identical snapshots Phase 3 of the BATCH_COMMIT protocol requires;
# scanning them makes every file resolve twice. Excluded by name, as in `test_link_targets`.
SKIP_PARTS = {".git", "__pycache__", ".venv", "venv", "node_modules", "backup"}

#: A section label carries at least one digit, may carry a short uppercase prefix (`H.1`,
#: `P2.2`, `S.6.3`, `J.0`), a trailing lower-case letter (`21c`, `5e`) and dotted parts.
LABEL = r"(?:[A-Z]{1,3}\.?)?\d+[a-z]?(?:\.[0-9A-Za-z]+)*"

HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
HEADING_LABEL = re.compile(r"^(?:§\s*)?\**\s*(" + LABEL + r")[.)·:\s]")
BOLD_LABEL = re.compile(
    r"^\s{0,3}\*\*(?:§\s*)?(" + LABEL + r")\s*[—–·:.\-]"
)
IN_HEADING = re.compile(r"§\s*(" + LABEL + r")")
FENCE = re.compile(r"^\s*```")

#: `` `<file>` §<label> `` — the one form tight enough to check without guessing. The optional
#: `body` matches the repository's own disambiguating idiom ("`LEGEND_CORE.md` body §35").
REFERENCE = re.compile(
    r"`([A-Za-z_][A-Za-z0-9_./-]*)`\s+(?:body\s+)?\**§\s*(" + LABEL + r")"
)

#: The surface whose cross-references a reader must be able to follow, and which an actor may
#: repair at T0 (§21e GATES). Prefix match on the repository-relative POSIX path.
NORMATIVE_PREFIXES = (
    "AGENTS.md",
    "ARCHITECTURE.md",
    "BOOTSTRAP.md",
    "CAPABILITIES.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "FAQ.md",
    "README.md",
    "SKILLS.md",
    ".claude/skills/",
    "framework/instruction/",
    "framework/manuals/",
    "framework/master/",
    "framework/protocols/",
    "framework/scripts/README.md",
    "framework/state/",
    "governance/ANNEX_INDEX.md",
    "governance/GOVERNANCE_v3.1.1.md",
    "governance/annex_",
    "governance/plan_defined_parameters.md",
    "roles/",
)


def markdown_files(root: Path = ROOT) -> list[Path]:
    """Markdown of *this* checkout only, pruning caches, snapshots and nested checkouts."""
    tracked = GATE.tracked_paths(root)
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        dirnames[:] = [
            name
            for name in dirnames
            if name not in SKIP_PARTS
            and not GATE.is_nested_checkout(here / name, root, tracked)
        ]
        found.extend(here / name for name in filenames if name.endswith(".md"))
    return sorted(found)


def section_labels(path: Path) -> set[str]:
    """Every section label the file defines, plus the ancestors those labels imply."""
    defined: set[str] = set()
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        bold = BOLD_LABEL.match(line)
        if bold:
            defined.add(bold.group(1))
        heading = HEADING.match(line)
        if not heading:
            continue
        title = heading.group(1)
        leading = HEADING_LABEL.match(title + " ")
        if leading:
            defined.add(leading.group(1))
        defined.update(match.group(1) for match in IN_HEADING.finditer(title))
    resolvable = set(defined)
    for label in defined:
        parts = label.split(".")
        for cut in range(1, len(parts)):
            resolvable.add(".".join(parts[:cut]))
    return resolvable


def is_normative(path: Path, root: Path = ROOT) -> bool:
    return path.relative_to(root).as_posix().startswith(NORMATIVE_PREFIXES)


def unresolved_references(
    root: Path = ROOT, normative_only: bool = True
) -> tuple[list[str], int]:
    """Return (one line per unresolvable reference, how many references were checked)."""
    files = markdown_files(root)
    by_name: dict[str, list[Path]] = {}
    for path in files:
        for key in {path.name.casefold(), path.stem.casefold()}:
            by_name.setdefault(key, []).append(path)
    labels = {path: section_labels(path) for path in files}

    problems: list[str] = []
    checked = 0
    for source in files:
        if normative_only and not is_normative(source, root):
            continue
        in_fence = False
        for number, line in enumerate(
            source.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in REFERENCE.finditer(line):
                name, label = match.group(1), match.group(2)
                candidates = list(
                    dict.fromkeys(
                        by_name.get(Path(name).name.casefold(), [])
                        + by_name.get(Path(name).stem.casefold(), [])
                    )
                )
                # 0 candidates: the name is not a file of this checkout (the public edition
                # drops private-overlay documents on purpose) — a path question, not ours.
                # >1: ambiguous by basename, and guessing which one was meant is how a
                # checker starts reporting the wrong file.
                if len(candidates) != 1:
                    continue
                target = candidates[0]
                checked += 1
                if label not in labels[target]:
                    problems.append(
                        f"{source.relative_to(root)}:{number}: `{name}` §{label} "
                        f"-> {target.relative_to(root)} defines no §{label}"
                    )
    return problems, checked


class SectionReferenceTests(unittest.TestCase):
    def test_normative_section_references_resolve(self) -> None:
        problems, checked = unresolved_references(normative_only=True)
        self.assertGreater(checked, 40, "the population collapsed; the pattern stopped matching")
        self.assertFalse(
            problems,
            f"Section references with no such section ({len(problems)} of {checked} "
            "checked on the normative surface):\n" + "\n".join(problems),
        )


class TheCheckCanActuallyFail(unittest.TestCase):
    """The fixture is built, not hoped for.

    🔴 The defect this suite exists for was green under every other check for six days. A
    suite that only ever reports zero on the tree it ships with has not demonstrated that it
    can report anything else.
    """

    def build(self) -> tuple[Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "CLAUDE.md").write_text(
            "# Router\n\n"
            "See `target_law` §1 and `target_law` §S.6.3 and `target_law` §4 "
            "and `target_law` §26.\n",
            encoding="utf-8",
        )
        (root / "target_law.md").write_text(
            "# Target law\n\n"
            "## 1. FIRST\n\n"
            "#### 4.0 A subsection whose parent has no heading of its own\n\n"
            "## S.6 · Preservation\n\n"
            "**S.6.3 — defined in bold, not as a heading**\n",
            encoding="utf-8",
        )
        return root, root / "CLAUDE.md"

    def test_only_the_missing_section_is_reported(self) -> None:
        root, _ = self.build()
        problems, checked = unresolved_references(root=root, normative_only=True)
        self.assertEqual(checked, 4)
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("§26", problems[0])

    def test_a_bold_definition_counts_as_a_section(self) -> None:
        root, _ = self.build()
        self.assertIn("S.6.3", section_labels(root / "target_law.md"))

    def test_an_ancestor_of_a_defined_subsection_resolves(self) -> None:
        root, _ = self.build()
        self.assertIn("4", section_labels(root / "target_law.md"))

    def test_a_non_normative_source_is_censused_not_gated(self) -> None:
        root, _ = self.build()
        stray = root / "reviews" / "REV-EXAMPLE-001.md"
        stray.parent.mkdir(parents=True)
        stray.write_text("`target_law` §999\n", encoding="utf-8")
        gated, _ = unresolved_references(root=root, normative_only=True)
        everything, _ = unresolved_references(root=root, normative_only=False)
        self.assertEqual(len(gated), 1)
        self.assertEqual(len(everything), 2)


def census() -> int:
    problems, checked = unresolved_references(normative_only=False)
    print(f"SECTION REFERENCE CENSUS: {len(problems)} unresolvable of {checked} checked, "
          "repository-wide (the normative surface is the gated subset)")
    for line in problems:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    if "--census" in sys.argv:
        raise SystemExit(census())
    unittest.main(verbosity=2)
