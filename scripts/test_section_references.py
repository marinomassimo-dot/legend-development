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
`.claude/skills/`, all of `governance/`, `disease-models/wwox/analysis/` and the commit
candidates. Those are the references a reader must be able to follow, and they are the files
an actor may repair at T0.

Dated session evaluations, mirror consultations, full-text dossiers, learning records, ledger
checkpoints and the hostile-review corpus are **censused, not gated** (`--census`). A gate
that can only be satisfied by editing a file the protocol forbids editing outside a batch is a
gate that gets disabled; the census is there so the number stays visible instead of being
rounded to zero.

🔴 EVERY WIDENING IS A MEASUREMENT, AND EVERY EXCLUSION CARRIES ITS OWN
----------------------------------------------------------------------
The first run found 82 unresolvable references repository-wide against 3 on the normative
surface, and most of the 82 sat under `disease-models/`. A Scientist pass on 2026-09-28
repaired that backlog to 17 and handed back the per-prefix numbers; this pass re-measured them
after the grammar repairs below took the census to **11 of 1155**, and widened on the result:

  gated 2026-09-28    `disease-models/wwox/analysis/`               289 checked, 0 unresolvable
                      `disease-models/wwox/research/commit_candidates/`  110 checked, 0
                      `governance/` (all of it, replacing four named files)  92 checked, 0

The original exclusion of the commit candidates rested on a premise that turned out false —
that a candidate cannot be repaired without a `BATCH_COMMIT`. `prompt_batch_commit.md` §7.2
licenses exactly this in-place identifier correction under its three-part marker, and 17
candidates were repaired that way. The gated population goes 65 -> 552 of 1155, i.e. +487 (the
three prefixes hold 491 references, four of which — `governance/`'s own root files — were
already gated by name); 42 % of every checkable reference in the repository moved from being
counted to being enforced.

Still censused, with today's number, so the next widening is a **read of `--census`** and not a
re-derivation:

  `disease-models/wwox/registries/`   32 checked, 4 unresolvable — changeable only through
      `BATCH_COMMIT`. 🔴 **Gate it the moment `CC-20260928-SECTION-REFS-01` propagates**: that
      candidate carries the repair for these, and its residual is then 0. One of the five the
      Scientist measured was never a defect — `working_model_current.md:266`'s
      `` `therapy_levers.md` §B2 `` is a real section, invisible to a bold-label extractor that
      required column 0; the LIST-ITEM DEFINITIONS repair below resolved it without an edit.
  `learning/`   343 checked, 0 unresolvable — the three that blocked it were the `4bis` /
      `10bis` / `4ter` truncation repaired below. Gateable today at zero cost; left censused in
      this pass only because the hand-off scoped it out, not because anything argues against
      it. The next actor may widen it on this number.
  `reviews/`   112 checked, 5 unresolvable — **permanently censused**, see below.

🔴 WHY `reviews/` IS CENSUSED PERMANENTLY AND NOT UNTIL ITS BACKLOG CLEARS
-------------------------------------------------------------------------
Two reasons, and neither is a count, so no future clean census lifts them.

1. **A reviewer's record is not the reviewed party's to edit.** The corpus under `reviews/` is
   the adversarial record of what a reviewer said at a date. A gate that turns red until
   somebody edits it points the repair at whoever is running the suite, which is normally not
   the author. `test_documented_commands.py` already treats `reviews/` this way, in
   `ARCHIVAL_DIRECTORIES`, for the same reason.

2. **This checker cannot tell a reference a document *makes* from one it *quotes to refute*.**
   `REV-AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md:465` is Mirror's own finding `AR-5`,
   which quotes `` `GOVERNANCE_v3.1.1.md` §325 `` **in order to report it as wrong** — a line
   number cited as a section. The checker reports it as a defect; the document is the thing
   that found it. The documented escape (drop the backticks) is available only to the quoting
   author, and a review corpus is exactly the place where quoting a bad reference is the
   normal, correct act. Gating a surface whose correct content the instrument misreads is how
   an instrument gets disabled.

That is why `PERMANENTLY_CENSUSED` exists below, and why a test asserts no prefix reaches into
it: the argument has to survive the next reader who sees a clean census and reaches for it.

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

Three false-positive classes were found by the 2026-09-28 hand-off and repaired here. Each was
a **correct citation reported as a defect**, which is the only kind of bug that discredits a
checker, and each was three or more real references:

  **MULTI-LETTER SUFFIXES.** `LABEL` admitted one trailing lower-case letter, so
  `deep_dive_manual.md`'s genuine `§4bis`, `§10bis` and `§4ter` truncated to `4b` / `10b` /
  `4t` **on both sides**: the heading was not recorded as a definition and the citation was not
  recognised, so three correct citations reported as unresolvable. Widened to `[a-z]*`. This
  was the whole of `learning/`'s residual.

  **LIST-ITEM DEFINITIONS.** `BOLD_LABEL` required column 0, and `therapy_levers.md` defines
  its lever ladder as `- **B2. Neuroinflammation control.**` — a bold definition carried by an
  unordered list marker. Three citations of `§B2` reported, one of them from
  `working_model_current.md`, where it looked like a defect repairable only by `BATCH_COMMIT`.

  **COMPOSED SUB-HEADINGS.** A heading whose own label is letters only (`### B.
  READ_STATUS_REPAIR` under `## 3. The three failures`) carries no digit and so is no label at
  all; the reference a reader writes is `§3.B`. A letters-only sub-heading is now composed with
  its nearest numeric ancestor. Composition only ever *adds* definitions, so it can turn a red
  green and never the reverse.

Not repaired, deliberately: `§4.1` used for **item 1 of the ordered list under §4** (four
references, all from the registries into dossiers). Teaching the checker to compose heading
labels with list-item numbers would make every `§N.M` below a list's length resolve, and
`controlled_benchmark_ab.md` §4.5 — a real defect, `4.1`–`4.4` exist — is exactly that shape.
That would trade a false positive for a false negative, which is the wrong direction.

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

import argparse
import contextlib
import importlib.util
import io
import os
import re
import subprocess
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
LABEL = r"(?:[A-Z]{1,3}\.?)?\d+[a-z]*(?:\.[0-9A-Za-z]+)*"

HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*)$")
HEADING_LABEL = re.compile(r"^(?:§\s*)?\**\s*(" + LABEL + r")[.)·:\s]")
#: A sub-heading whose own label is letters only (`### B. READ_STATUS_REPAIR`). It carries no
#: digit, so it is not a label on its own; composed with the nearest numeric ancestor it is the
#: `3.B` a reader cites. See COMPOSED SUB-HEADINGS in the module docstring.
LETTER_SUBHEADING = re.compile(r"^(?:§\s*)?\**\s*([A-Z]{1,3})[.)·:]")
#: Line-initial bold definitions, optionally carried by an unordered list marker: the
#: `- **B2. Neuroinflammation control.**` form `therapy_levers.md` uses for its lever ladder.
BOLD_LABEL = re.compile(
    r"^\s{0,3}(?:[-*+]\s+)?\*\*(?:§\s*)?(" + LABEL + r")\s*[—–·:.\-]"
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
    # 🔴 Widened 2026-09-28, each entry with the measurement that justified it (see WHAT THE
    # GATE COVERS). `governance/` replaces the four hand-listed governance files it used to
    # name: the body, the annexes, the candidates, the decisions and the design records
    # together carry 92 references at 0 unresolvable, and correcting a cross-reference inside
    # a decided record is not re-deciding it.
    "governance/",
    "disease-models/wwox/analysis/",
    "disease-models/wwox/research/commit_candidates/",
    "roles/",
)

#: 🔴 DIRECTORIES THAT STAY CENSUSED ON PRINCIPLE, not on a count. `is_normative` never
#: consults this tuple — the gate is the prefix list above — but a test asserts no prefix
#: above reaches into these, so a later actor cannot widen them by reading a clean census.
PERMANENTLY_CENSUSED = ("reviews/",)


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
    #: depth -> the numeric label that heading level is currently under, so a letters-only
    #: sub-heading can be composed with the section it sits in.
    numeric_ancestors: dict[int, str] = {}
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
        depth, title = len(heading.group(1)), heading.group(2)
        for deeper in [level for level in numeric_ancestors if level >= depth]:
            del numeric_ancestors[deeper]
        leading = HEADING_LABEL.match(title + " ")
        if leading:
            defined.add(leading.group(1))
            numeric_ancestors[depth] = leading.group(1)
        else:
            letters = LETTER_SUBHEADING.match(title + " ")
            parent = max(
                (level for level in numeric_ancestors if level < depth), default=None
            )
            if letters and parent is not None:
                defined.add(f"{numeric_ancestors[parent]}.{letters.group(1)}")
        defined.update(match.group(1) for match in IN_HEADING.finditer(title))
    resolvable = set(defined)
    for label in defined:
        parts = label.split(".")
        for cut in range(1, len(parts)):
            resolvable.add(".".join(parts[:cut]))
    return resolvable


def is_normative(path: Path, root: Path = ROOT) -> bool:
    return path.relative_to(root).as_posix().startswith(NORMATIVE_PREFIXES)


def scan(root: Path = ROOT) -> list[tuple[Path, str | None]]:
    """Every checkable reference in the checkout, as (source, complaint-or-None).

    One pass, two consumers: the gate filters it to the normative surface, and `--census`
    groups it by directory. Deriving both from the same scan is what makes the per-directory
    table a *read* of the gate's own population rather than a second measurement of it — the
    per-prefix numbers a widening decision needs used to be produced by hand.
    """
    files = markdown_files(root)
    by_name: dict[str, list[Path]] = {}
    for path in files:
        for key in {path.name.casefold(), path.stem.casefold()}:
            by_name.setdefault(key, []).append(path)
    labels = {path: section_labels(path) for path in files}

    found: list[tuple[Path, str | None]] = []
    for source in files:
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
                complaint = None
                if label not in labels[target]:
                    complaint = (
                        f"{source.relative_to(root)}:{number}: `{name}` §{label} "
                        f"-> {target.relative_to(root)} defines no §{label}"
                    )
                found.append((source, complaint))
    return found


def unresolved_references(
    root: Path = ROOT, normative_only: bool = True
) -> tuple[list[str], int]:
    """Return (one line per unresolvable reference, how many references were checked)."""
    selected = [
        (source, complaint)
        for source, complaint in scan(root)
        if not normative_only or is_normative(source, root)
    ]
    return [complaint for _, complaint in selected if complaint], len(selected)


class SectionReferenceTests(unittest.TestCase):
    def test_normative_section_references_resolve(self) -> None:
        problems, checked = unresolved_references(normative_only=True)
        # Anti-vacuity floor, raised with the surface: 552 references are gated at the
        # 2026-09-28 widening, against 65 before it. A floor of 40 would have gone on passing
        # after the widened prefixes silently stopped matching — which is the failure a floor
        # exists to catch. A floor, never an exact count (`growth_anchors.py`: the quiet
        # birthday).
        self.assertGreater(checked, 400, "the population collapsed; the pattern stopped matching")
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
            "and `target_law` §26.\n"
            # The three false-positive classes repaired on 2026-09-28, each cited CORRECTLY:
            # a correct citation that reports as a defect is the failure mode that discredits
            # the instrument, so each one is a case and not a comment.
            "Also `target_law` §4bis and `target_law` §B2 and `target_law` §7.C.\n",
            encoding="utf-8",
        )
        (root / "target_law.md").write_text(
            "# Target law\n\n"
            "## 1. FIRST\n\n"
            "#### 4.0 A subsection whose parent has no heading of its own\n\n"
            "## 4bis. A HEADING WHOSE LABEL CARRIES A MULTI-LETTER SUFFIX\n\n"
            "## S.6 · Preservation\n\n"
            "**S.6.3 — defined in bold, not as a heading**\n\n"
            "- **B2. Defined in bold behind a list marker**, as a lever ladder does\n\n"
            "## 7. A NUMBERED SECTION WITH LETTER-LABELLED CHILDREN\n\n"
            "### C. The child carries no digit of its own\n",
            encoding="utf-8",
        )
        return root, root / "CLAUDE.md"

    def test_only_the_missing_section_is_reported(self) -> None:
        root, _ = self.build()
        problems, checked = unresolved_references(root=root, normative_only=True)
        self.assertEqual(checked, 7)
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("§26", problems[0])

    def test_a_multi_letter_suffix_is_one_label_on_both_sides(self) -> None:
        """`§4bis` must not truncate to `4b` in the heading or in the citation."""
        root, _ = self.build()
        labels = section_labels(root / "target_law.md")
        self.assertIn("4bis", labels)
        self.assertNotIn("4b", labels)
        self.assertEqual(
            ["4bis"], [match[1] for match in REFERENCE.findall("see `target_law` §4bis here")]
        )

    def test_a_bold_definition_behind_a_list_marker_counts(self) -> None:
        root, _ = self.build()
        self.assertIn("B2", section_labels(root / "target_law.md"))

    def test_a_letter_subheading_composes_with_its_numeric_ancestor(self) -> None:
        root, _ = self.build()
        labels = section_labels(root / "target_law.md")
        self.assertIn("7.C", labels)
        # The composition is scoped to the section the child sits in, not to the whole file.
        self.assertNotIn("1.C", labels)

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


class TheCensusedSurfacesAreDeliberate(unittest.TestCase):
    """A widening decision is a read of `--census`; a *permanent* exclusion is an argument.

    🔴 `reviews/` is not censused because its residual is 5. It is censused because this
    checker cannot distinguish a reference a document MAKES from one it QUOTES IN ORDER TO
    REFUTE — `REV-AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md:465` is Mirror's finding
    `AR-5` doing exactly that — and because a reviewer's record is not the reviewed party's to
    edit. Both reasons are independent of any count, so a future clean census must not be
    enough to widen it. This case is what makes that argument load-bearing instead of prose.
    """

    def test_no_gated_prefix_reaches_into_a_permanently_censused_directory(self) -> None:
        for censused in PERMANENTLY_CENSUSED:
            for prefix in NORMATIVE_PREFIXES:
                self.assertFalse(
                    prefix.startswith(censused) or censused.startswith(prefix),
                    f"{prefix!r} gates {censused!r}, which is censused on principle and not "
                    "on a backlog count — read WHY `reviews/` IS CENSUSED PERMANENTLY in the "
                    "module docstring before changing this",
                )

    def test_the_permanently_censused_directories_are_really_in_the_census(self) -> None:
        """Excluded from the gate is not excluded from the measurement."""
        rows = {row[0]: row for row in by_directory()}
        covered = [
            row for name, row in rows.items()
            if name.startswith(PERMANENTLY_CENSUSED)
        ]
        self.assertTrue(covered, "the census stopped reaching the reviews corpus")
        self.assertTrue(all(row[3] == "no" for row in covered), covered)


class TheOneFlagIsDocumentable(unittest.TestCase):
    """🔴 `--census` was unreachable from `--help`, so the repository could not document it.

    `scripts/test_documented_commands.py` asks a documented command's `--help` whether the
    flag exists. With `--census` read off `sys.argv` and everything else falling through to
    `unittest.main`, `--help` printed unittest's options: exit 0, no mention of `--census`. Any
    document writing the guarded form `python3 scripts/test_section_references.py --census`
    therefore turned that suite red, and with it four cases of
    `test_repository_surface_determinism.py`. The eleven documents that already cited the flag
    escaped only by omitting `python3`.
    """

    def test_help_declares_the_census_flag(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--help"],
            cwd=ROOT, capture_output=True, text=True, timeout=60, check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("--census", completed.stdout + completed.stderr)

    def test_unittest_arguments_still_pass_through(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()),
             "-k", "test_a_bold_definition_behind_a_list_marker_counts"],
            cwd=ROOT, capture_output=True, text=True, timeout=120, check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("Ran 1 test", completed.stdout + completed.stderr)

    def test_a_failing_run_still_exits_non_zero(self) -> None:
        """`unittest.main(exit=False)` returns instead of exiting, so `main` carries the code.

        Without this, an `argparse` front would have turned a gate into a reporter: the suite
        would print FAILED and exit 0, and `run_release_regressions.py` keys on the exit code.
        An unresolvable test name is loaded by unittest as a failing test, which is the
        cheapest real failure to provoke.
        """
        buffer = io.StringIO()
        with contextlib.redirect_stderr(buffer), contextlib.redirect_stdout(buffer):
            code = main(["scripts.test_section_references.NoSuchCase.no_such_test"])
        self.assertEqual(1, code, buffer.getvalue())


def by_directory(root: Path = ROOT) -> list[tuple[str, int, int, str]]:
    """(directory, checked, unresolvable, gated?) — the table a widening decision reads.

    The row key is the source file's own directory, not a curated prefix list: a curated list
    is a thing that decays, and the question *"what would gating this cost today"* is asked of
    a directory. `gated` is `yes` / `no` / `part` because a prefix tuple can cover some files
    of a directory and not others (`framework/scripts/README.md` is gated, its siblings are
    not).
    """
    checked: dict[str, int] = {}
    red: dict[str, int] = {}
    gated: dict[str, set[bool]] = {}
    for source, complaint in scan(root):
        key = source.relative_to(root).parent.as_posix()
        checked[key] = checked.get(key, 0) + 1
        red[key] = red.get(key, 0) + (1 if complaint else 0)
        gated.setdefault(key, set()).add(is_normative(source, root))
    rows = []
    for key in checked:
        flags = gated[key]
        rows.append((
            key,
            checked[key],
            red[key],
            "yes" if flags == {True} else "no" if flags == {False} else "part",
        ))
    return sorted(rows, key=lambda row: (-row[2], row[0]))


def census(root: Path = ROOT) -> int:
    problems, checked = unresolved_references(root=root, normative_only=False)
    print(f"SECTION REFERENCE CENSUS: {len(problems)} unresolvable of {checked} checked, "
          "repository-wide (the normative surface is the gated subset)")
    for line in problems:
        print(f"  {line}")
    rows = by_directory(root)
    width = max([len(row[0]) for row in rows] + [len("DIRECTORY")])
    print()
    print(f"  {'DIRECTORY'.ljust(width)}  CHECKED  UNRESOLVABLE  GATED")
    for directory, count, red, gate in rows:
        print(f"  {directory.ljust(width)}  {count:>7}  {red:>12}  {gate}")
    print(f"  {'TOTAL'.ljust(width)}  {checked:>7}  {len(problems):>12}")
    return 0


def main(argv: list[str] | None = None) -> int:
    """An `argparse` front, so the one flag this script has is documentable.

    🔴 `--census` used to be read straight off `sys.argv` with everything else falling through
    to `unittest`, which meant `--help` printed *unittest's* help and did not mention
    `--census`. `scripts/test_documented_commands.py` asks `--help` whether a documented flag
    exists, so the repository could not document its own newest flag in the guarded
    `python3 scripts/... --census` form: doing so turned that suite red, and with it four cases
    of `test_repository_surface_determinism.py`. The eleven documents that already cited the
    flag escaped only by omitting the `python3` prefix — an accidental convention holding up a
    documented contract. Unrecognised arguments still go to `unittest`, so
    `-k`, `-v`, `--failfast` and a dotted test name keep working.
    """
    parser = argparse.ArgumentParser(
        description="Check that every `<file>` §<label> reference resolves to a section that "
                    "file defines. With no arguments, runs the unittest suite that gates the "
                    "normative surface.",
        epilog="Any other argument is passed through to unittest (e.g. -v, -k NAME).",
    )
    parser.add_argument(
        "--census",
        action="store_true",
        help="print the repository-wide census and the per-directory table, then exit 0 "
             "(reports, never fails)",
    )
    known, rest = parser.parse_known_args(argv if argv is not None else sys.argv[1:])
    if known.census:
        return census()
    result = unittest.main(argv=[sys.argv[0], *rest], verbosity=2, exit=False)
    return 0 if result.result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
