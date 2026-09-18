#!/usr/bin/env python3
"""Every tool this repository ships is routed, exactly once, to the question it answers.

🔴 WHY THIS EXISTS
------------------
The residual retrieval defect measured on 2026-09-18 is not size — selective registry access
already cut a MINIMAL session's load by 82 % — it is **routing**. The non-test Python tools
are spread across `framework/scripts/`, `scripts/` and `governance/scripts/`, and `CLAUDE.md`
deliberately does not legislate a list of them. A session that does not know a tool exists does
the thing this repository has twice named as its characteristic failure: it greps, and a fragment
is how a caveat dies.

`framework/scripts/README.md` is the routing table. This suite is what stops it decaying into
prose: it **discovers the population** rather than listing it, so the next tool added to the
repository turns this red until the table names it too — the same discipline
`test_generated_surfaces_are_regenerated.py` applies to generated surfaces, and the criterion
`growth_anchors.py` states in words: *updating a constraint must cost at least as much as
complying with it*. A routing table nobody is obliged to extend is a routing table that is wrong
by the third tool.

🔴 THE POPULATION COMES FROM THE GIT INDEX, NOT FROM THE DISK
-------------------------------------------------------------
`git ls-files`, for two reasons this repository has already paid for:

  - `artifact_index.py` rule 3 — the population is enumerated **before** any pattern runs, by an
    instrument that cannot express the property being hunted. A count whose denominator is
    "whatever my pattern matched" is not a measurement.
  - `test_repository_surface_determinism.py` — one clean checkout of `main` gave three verdicts
    from a disk-walking guard, because an untracked file and a nested checkout both changed the
    population. What is promised to a reader is carried by the INDEX.

So an untracked scratch script in `framework/scripts/` does not turn this suite red, and a tool
that is committed does.

Run: `python3 scripts/test_tool_routing.py`
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "framework" / "scripts" / "README.md"
ROOTS = ("framework/scripts/", "scripts/", "governance/scripts/")
# A path that starts at one of the three roots. Anchored on a non-path character so a longer
# path ending in one of these does not match its tail.
NAMED = re.compile(r"(?<![A-Za-z0-9_./-])((?:framework/scripts|governance/scripts|scripts)/"
                   r"[A-Za-z0-9_./-]+\.py)")


def is_tool(relative: str) -> bool:
    """A shipped tool: a tracked `.py` under one of the three roots, not a test."""
    return (relative.endswith(".py")
            and relative.startswith(ROOTS)
            and not Path(relative).name.startswith("test_"))


def population() -> set[str]:
    """Every tool, from the git index."""
    listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--", *ROOTS],
                            capture_output=True, text=True, check=True).stdout.split()
    return {item for item in listed if is_tool(item)}


def routed() -> list[str]:
    """Every tool path the table names, in order, duplicates kept so they can be reported."""
    text = TABLE.read_text(encoding="utf-8")
    return [item for item in NAMED.findall(text) if is_tool(item)]


def routed_by_section() -> dict[str, set[str]]:
    """Tool -> the set of `##` sections that route it.

    🔴 THE RULE IS ONE SECTION, NOT ONE ROW, and the difference was found by this suite on its
    first run. `paper_packet.py` legitimately earns two rows in § 1 — `packet` and `check` are
    two questions — while the same tool appearing under § 1 AND § 7 would leave a reader unable
    to tell which place is current. Rows are presentation; sections are the routing.
    """
    found: dict[str, set[str]] = {}
    section = "(before the first section)"
    for line in TABLE.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        for item in NAMED.findall(line):
            if is_tool(item):
                found.setdefault(item, set()).add(section)
    return found


class TheRoutingTableCoversEveryTool(unittest.TestCase):
    def setUp(self) -> None:
        self.assertTrue(TABLE.is_file(), f"the routing table is missing: {TABLE}")
        self.population = population()
        self.routed = routed()

    def test_the_population_is_not_empty(self) -> None:
        """Anti-vacuity: a guard whose population is empty passes by agreeing with nothing.
        The number is asserted as a floor, never as an exact count — an exact count is the
        quiet birthday `growth_anchors.py` was written about."""
        self.assertGreater(len(self.population), 50,
                           "the git index returned too few tools; the enumeration is broken, "
                           "not the table")

    def test_every_shipped_tool_is_routed(self) -> None:
        missing = sorted(self.population - set(self.routed))
        self.assertFalse(missing, "these tools are shipped and named nowhere in "
                                  f"framework/scripts/README.md — a tool nobody can find is a "
                                  f"tool that gets reimplemented or grepped around:\n  " +
                                  "\n  ".join(missing))

    def test_the_table_names_no_tool_that_does_not_exist(self) -> None:
        """The failure `test_documented_commands.py` exists for, applied to this table: prose
        survives a rename, the executable does not."""
        stale = sorted(item for item in set(self.routed) if not (ROOT / item).is_file())
        self.assertFalse(stale, "named in the routing table, absent from the tree:\n  " +
                         "\n  ".join(stale))

    def test_no_tool_is_routed_from_two_different_sections(self) -> None:
        """Two sections offering one tool are two answers to 'where do I look for this', and the
        reader cannot tell which is current. Two ROWS inside one section are fine — see
        `routed_by_section`."""
        split = sorted(f"{item}: {', '.join(sorted(sections))}"
                       for item, sections in routed_by_section().items() if len(sections) > 1)
        self.assertFalse(split, "routed from more than one section:\n  " + "\n  ".join(split))

    def test_the_section_rule_is_not_vacuous(self) -> None:
        """A rule that no arrangement could violate proves nothing. This pins that the parser
        really does attribute a tool to the section it sits under."""
        by_section = routed_by_section()
        self.assertIn("framework/scripts/public_release_gate.py".replace(
            "framework/scripts/", "scripts/"), by_section)
        self.assertEqual({"8 · Before publishing"},
                         by_section["scripts/public_release_gate.py"])
        self.assertEqual({"1 · I need a record, a paper or a claim — without loading a registry"},
                         by_section["framework/scripts/paper_packet.py"])

    def test_the_table_does_not_reroute_the_two_large_registries_to_grep(self) -> None:
        """The one rule the table exists to carry. Asserted on the table's own text, because a
        routing table that omitted it would be worse than none: it would look complete."""
        text = TABLE.read_text(encoding="utf-8")
        self.assertIn("registry_records.py", text)
        self.assertIn("Never grep the two large registries", text)

    def test_a_library_without_a_main_is_named_as_one(self) -> None:
        """Completeness is not tidiness. A reader who finds a module here and cannot run it must
        learn why from the table, not from running it. Derived from the files, so a library that
        grows a CLI — or a command that loses one — fails this rather than drifting."""
        text = TABLE.read_text(encoding="utf-8")
        libraries = sorted(item for item in self.population
                           if "__main__" not in (ROOT / item).read_text(encoding="utf-8"))
        self.assertTrue(libraries, "the fixture needs at least one importable-only module")
        section = text.split("Libraries, not commands", 1)
        self.assertEqual(2, len(section), "the table has no libraries section")
        for item in libraries:
            self.assertIn(item, section[1],
                          f"{item} has no __main__ and is routed as if it were runnable")
        for item in self.population - set(libraries):
            self.assertNotIn(item, section[1],
                             f"{item} has a __main__ and is listed as a library")


if __name__ == "__main__":
    unittest.main(verbosity=2)
