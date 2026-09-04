#!/usr/bin/env python3
"""§21c and §21d must be reachable BY NAME from the surface every actor opens with.

`test_stop_policy.py` already pins the two sections verbatim and checks that `CLAUDE.md`
links to the file that carries them. That is not the same guarantee, and the gap is not
theoretical: on 2026-09-04 a session opened, loaded `CLAUDE.md` in full, followed the §1
table — whose only description of `LEGEND_CORE.md` is "gates, blocking strings, commit
rules, recovery order" — and reached neither section. Every existing check was green. The
operator found it by asking.

So the property here is narrower and stronger than "the file is linked": **each surface an
actor is guaranteed to open must link to the two SECTIONS, by their anchors, in the part of
the surface that is read before acting.** A link to `LEGEND_CORE.md` satisfies the old
check and not this one, which is the whole point of adding it.

Three deliberate choices, each of them a repair to a way an earlier reachability check went
green while the rule was unreachable:

* **Per surface, never "some surface in the chain".** Mirror's F4 finding against the first
  version of `test_stop_policy.py` was that an existential quantifier over `ROUTER_CHAIN`
  stayed green with `CLAUDE.md`'s own reference deleted. The four obligation suites this
  repository already trusts — `test_locator_obligation_reaches_every_route.py` and its
  siblings — assert over a fixed tuple of named files with `subTest(file=...)`. This one is
  the same shape, over the same two files those suites use.
* **A markdown link with a fragment, not a mention of "§21c".** A mention cannot tell a
  route from an anti-route: "§21c is DEPRECATED, do not read it" contains the string.
* **Position, not merely presence.** A link in `CLAUDE.md` §4's read-order list is not
  "before your first act". The `CLAUDE.md` assertion is scoped to §0, the section whose own
  heading is "Before anything else", so moving the line down the file fails this suite.

What this suite does NOT claim: that an actor which loads the surface reads the link. No
test in this repository can establish that, and asserting it would be the same overreach
that made the earlier version green. It establishes that the route exists, resolves, and
sits where the actor is looking — and that is the part a file can carry.
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
sys.path.insert(0, str(ROOT / "scripts"))

from runtime_parity import ROUTER_CHAIN  # noqa: E402
# `heading_slug` is imported from the suite that already owns fragment resolution rather
# than reimplemented. A second copy of the slug rule could agree with this file while
# disagreeing with the checker that actually validates the repository's links — which is
# how a test ends up certifying an anchor that resolves nowhere.
from test_link_targets import heading_slug  # noqa: E402

SURFACE = "framework/instruction/LEGEND_CORE.md"

# Both are opened by an actor before it acts, in the two runtimes this repository declares:
# `CLAUDE.md` by the Claude harness, `AGENTS.md` as the Codex adapter whose own §1 chain is
# what a Codex session follows. This is the tuple the four obligation suites already use.
ALWAYS_LOADED = ("CLAUDE.md", "AGENTS.md")

SECTIONS = (
    ("## 21c. STOP POLICY", "21c-stop-policy"),
    ("## 21d. DECISION AUTHORITY", "21d-decision-authority"),
)

# `CLAUDE.md` §0 runs from its heading to the next `## `. Scoping the assertion to it is
# what turns "the link is somewhere in the router" into "the link is where §0 says it
# binds"; `AGENTS.md` has no §0, so its own scope is its chain section.
SCOPES = {
    "CLAUDE.md": "## 0 · Before anything else",
    "AGENTS.md": "## 1 · The chain, in this order",
}


def section_of(text: str, heading: str) -> str:
    start = text.index(heading)
    rest = text[start + len(heading):]
    end = rest.find("\n## ")
    return rest if end == -1 else rest[:end]


def anchors_in(text: str) -> set[str]:
    """Every `#fragment` that a markdown link in `text` aims at LEGEND_CORE.md."""
    pattern = re.compile(r"\]\(" + re.escape(SURFACE) + r"#([^)\s]+)\)")
    return set(pattern.findall(text))


def legend_core_slugs() -> set[str]:
    return {heading_slug(line.lstrip("#").strip())
            for line in (ROOT / SURFACE).read_text(encoding="utf-8").splitlines()
            if line.startswith("#")}


class TheTwoSectionsAreReachableByName(unittest.TestCase):
    def test_every_always_loaded_surface_links_to_both_sections(self) -> None:
        for name in ALWAYS_LOADED:
            text = (ROOT / name).read_text(encoding="utf-8")
            found = anchors_in(text)
            for heading, anchor in SECTIONS:
                with self.subTest(file=name, section=heading):
                    self.assertIn(
                        anchor, found,
                        f"{name} does not link to {SURFACE}#{anchor}. An actor that opens "
                        f"{name} is routed to the FILE and never to `{heading}`, which is "
                        "the exact failure of 2026-09-04. Add the link; do not copy the "
                        "rule — CLAUDE.md's first line forbids a second home for it.")

    def test_the_link_sits_where_the_surface_says_it_binds(self) -> None:
        """A route the actor reaches after acting is not a route it acted under."""
        for name, heading in SCOPES.items():
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(heading, text, f"{name} no longer has `{heading}`")
            scoped = anchors_in(section_of(text, heading))
            for _, anchor in SECTIONS:
                with self.subTest(file=name, anchor=anchor):
                    self.assertIn(
                        anchor, scoped,
                        f"`{heading}` in {name} contains no link to #{anchor}. Either the "
                        "link was never added or it moved out of the part an actor reads "
                        "before its first act; the sibling test above says which.")

    def test_both_anchors_resolve_to_real_headings(self) -> None:
        """A route naming a destination it cannot reach is not a route.

        Checked against `LEGEND_CORE.md`'s own headings, so renaming §21c fails here even
        though the link text would still read correctly.
        """
        slugs = legend_core_slugs()
        for heading, anchor in SECTIONS:
            with self.subTest(anchor=anchor):
                self.assertEqual(
                    anchor, heading_slug(heading.lstrip("#").strip()),
                    f"`{heading}` no longer slugs to `{anchor}`")
                self.assertIn(anchor, slugs, f"{SURFACE} has no heading anchored at #{anchor}")

    def test_the_detector_fires_on_a_surface_that_only_names_the_file(self) -> None:
        """The negative control, and it is the case this suite exists to catch.

        `CLAUDE.md` as it stood at 57c0f25 — the commit at which the failure happened —
        linked to `LEGEND_CORE.md` five times and to neither section. Stripping the
        fragments from the live text reconstructs that surface, and every assertion above
        must go red on it. Without this, a bug in `anchors_in` would make the whole suite
        pass by finding nothing to complain about.
        """
        text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        as_it_was = re.sub(r"\]\((" + re.escape(SURFACE) + r")#[^)\s]+\)", r"](\1)", text)
        self.assertIn(f"]({SURFACE})", as_it_was, "the file link itself must survive")
        self.assertEqual(set(), anchors_in(as_it_was))
        self.assertEqual(set(), anchors_in(section_of(as_it_was, SCOPES["CLAUDE.md"])))

    def test_the_asserted_surfaces_are_ones_the_router_actually_routes_through(self) -> None:
        """Guards the tuple against drifting onto a file nobody opens.

        `AGENTS.md` is not a `ROUTER_CHAIN` member — the chain is what a session reads, and
        `AGENTS.md` is the Codex *adapter* that puts a session on it. So it is asserted
        through its own declared contract instead: it must name `CLAUDE.md` as the shared
        entry, which is what makes it an always-loaded surface for that runtime.
        """
        chain = {str(member) for member in ROUTER_CHAIN}
        self.assertIn("CLAUDE.md", chain)
        for member in ROUTER_CHAIN:
            self.assertTrue((ROOT / member).exists(), f"ROUTER_CHAIN member absent: {member}")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("](CLAUDE.md)", agents,
                      "AGENTS.md no longer routes to the shared entry, so asserting on it "
                      "asserts on a surface the Codex runtime may never reach")


if __name__ == "__main__":
    unittest.main(verbosity=2)
