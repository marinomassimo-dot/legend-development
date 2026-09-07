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
  route from an anti-route, and 🔴 **neither can a link — this rationale was overstated and
  is corrected here.** Blind review built two surfaces that carry the real fragments and
  route nobody: the links wrapped in `<!-- retired route, do not use: … -->`, and the links
  present but immediately labelled "**DEPRECATED — do not read them**". The suite passed
  both. The first is now closed, because a link inside an HTML comment is not markup an
  actor follows and `anchors_in` strips comments before matching. The second is NOT closed
  and cannot be by this method: no string test distinguishes a live route from a live route
  standing next to a sentence that disowns it. What a fragment link buys over a mention is
  narrower than first claimed — it pins WHICH section and it is checkable against the
  destination's real headings — and that narrower claim is the one this suite makes.
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

ROUTER_CHAIN = ("CLAUDE.md", "BOOTSTRAP.md", "governance/ANNEX_INDEX.md",
                "roles/plan.md", "framework/protocols/index.md")
# 🔴 BOTH are imported from the suite that owns fragment resolution. Importing only
# `heading_slug` and reimplementing the file walk was not the same guarantee, and the
# docstring claimed it was: `heading_slugs` owns fence-skipping and duplicate
# disambiguation, so a local reimplementation happily produced `21c-stop-policy` for a
# heading sitting inside a ``` fence, where the repository's own checker produces nothing.
# The suite would then have certified an anchor `test_link_targets.py` rejects — the exact
# failure the import was supposed to prevent.
from test_link_targets import heading_slug, heading_slugs  # noqa: E402

SURFACE = "framework/instruction/LEGEND_CORE.md"

# Both are opened by an actor before it acts, in the two runtimes this repository declares:
# `CLAUDE.md` by the Claude harness, `AGENTS.md` as the Codex adapter whose own §1 chain is
# what a Codex session follows. This is the tuple the four obligation suites already use.
ALWAYS_LOADED = ("CLAUDE.md", "AGENTS.md")

SECTIONS = (
    ("## 21c. STOP POLICY", "21c-stop-policy"),
    ("## 21d. DECISION AUTHORITY", "21d-decision-authority"),
    # DEC-20260905-AGILE-HARNESS-MODE: the agile mode binds before the first act too — an
    # actor that has not loaded it falls back to waiting for an integrator that no longer exists.
    ("## 21e. AGILE OPERATING MODE", "21e-agile-operating-mode"),
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


HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
FENCE = re.compile(r"(?ms)^[ \t]*```.*?^[ \t]*```[ \t]*$")
#: An INLINE code span. Same class as the fence, and it was missed twice: a link wrapped in
#: single backticks renders as literal text, routes nobody, and kept the whole suite green.
#: Blind review found it by trying the third spelling after the first two were closed —
#: which is the lesson, not the regex: "the two ways I thought of" is not a class.
CODE_SPAN = re.compile(r"(`+)(?:(?!\1).)*?\1", re.S)


def anchors_in(text: str) -> set[str]:
    """Every `#fragment` a LIVE markdown link in `text` aims at LEGEND_CORE.md.

    Two kinds of non-route are removed first, and both were found by blind review after
    the suite passed surfaces that routed nobody.

    * HTML comments. A link inside `<!-- retired route, do not use: … -->` is not markup an
      actor follows, and the suite was green on a surface whose only references were
      commented out.
    * Fenced code blocks. A link shown as an EXAMPLE is not a route either, and
      `test_link_targets.heading_slugs` already skips fences on the destination side — this
      is the same rule applied on the source side, so the two agree about what markdown is
      live.

    Residual, stated because it is real: an UNBALANCED `<!--` earlier in a file swallows
    everything after it, so a live link can be missed. That direction is a false RED, which
    is the safe way for a reachability check to be wrong, and it is why the stripper is not
    made cleverer than this.
    """
    pattern = re.compile(r"\]\(" + re.escape(SURFACE) + r"#([^)\s]+)\)")
    live = CODE_SPAN.sub("", FENCE.sub("", HTML_COMMENT.sub("", text)))
    return set(pattern.findall(live))


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
        slugs = heading_slugs(ROOT / SURFACE)
        for heading, anchor in SECTIONS:
            with self.subTest(anchor=anchor):
                self.assertEqual(
                    anchor, heading_slug(heading.lstrip("#").strip()),
                    f"`{heading}` no longer slugs to `{anchor}`")
                self.assertIn(anchor, slugs, f"{SURFACE} has no heading anchored at #{anchor}")

    def test_a_heading_inside_a_code_fence_does_not_count_as_a_destination(self) -> None:
        """The check that `heading_slugs` is doing the work, and not a local lookalike.

        A local reimplementation scanned every line starting with `#` and accepted a
        heading inside a ``` fence; `test_link_targets.heading_slugs` does not. If this
        suite ever drifts back to its own walk, this case goes green when it should be red.
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            fenced = Path(tmp) / "fenced.md"
            fenced.write_text("# Real Title\n\n```\n## 21c. STOP POLICY\n```\n",
                              encoding="utf-8")
            slugs = heading_slugs(fenced)
            self.assertIn("real-title", slugs, "the positive control must be found")
            self.assertNotIn("21c-stop-policy", slugs)

    def test_the_detector_fires_on_a_surface_that_only_names_the_file(self) -> None:
        """The negative control, and it is the case this suite exists to catch.

        `CLAUDE.md` as it stood at 57c0f25 — the commit at which the failure happened —
        named `LEGEND_CORE.md` 4 times, linked to it twice, and pointed at neither
        section; `AGENTS.md` named it 0 times either way, so across the two asserted
        surfaces there were 2 links and 0 anchors. ("Five times" stood here and in the
        commit message until blind review re-derived it; no reading of either file yields
        five, and it was a checkable number stated without being checked.) Stripping the
        fragments from the live text reconstructs that surface, and every assertion above
        must go red on it. Without this, a bug in `anchors_in` would make the whole suite
        pass by finding nothing to complain about.
        """
        text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        as_it_was = re.sub(r"\]\((" + re.escape(SURFACE) + r")#[^)\s]+\)", r"](\1)", text)
        self.assertIn(f"]({SURFACE})", as_it_was, "the file link itself must survive")
        self.assertEqual(set(), anchors_in(as_it_was))
        self.assertEqual(set(), anchors_in(section_of(as_it_was, SCOPES["CLAUDE.md"])))

    def test_a_route_inside_an_html_comment_does_not_count(self) -> None:
        """Blind review's counter-example (A), closed. A commented link routes nobody."""
        live = "See [§21c](" + SURFACE + "#21c-stop-policy) before acting."
        self.assertEqual({"21c-stop-policy"}, anchors_in(live))
        commented = "<!-- retired route, do not use: " + live + " -->"
        self.assertEqual(set(), anchors_in(commented))
        self.assertEqual({"21c-stop-policy"}, anchors_in(commented + "\n" + live),
                         "a commented copy must not suppress a real one beside it")

    def test_the_three_non_route_spellings_are_all_dead(self) -> None:
        """Comment, fence, inline span — asserted together so the next one is noticed.

        🔴 The first two were closed one at a time, each time with a docstring implying the
        class was handled. Blind review then supplied the third: a link in single backticks
        renders as literal text and kept the suite green. Three spellings do not prove the
        class is closed either; what this case buys is that they fail together, so a repair
        to one that quietly drops another goes red here.
        """
        live = "[§21c](" + SURFACE + "#21c-stop-policy)"
        self.assertEqual({"21c-stop-policy"}, anchors_in(live), "the control must route")
        for label, dead in (("html comment", "<!-- retired: " + live + " -->"),
                            ("fenced block", "```\n" + live + "\n```"),
                            ("inline span", "`" + live + "`")):
            with self.subTest(spelling=label):
                self.assertEqual(set(), anchors_in(dead))
                self.assertEqual({"21c-stop-policy"}, anchors_in(dead + "\n\n" + live),
                                 "a dead copy must not suppress a live one beside it")

    def test_a_route_shown_as_a_fenced_example_does_not_count(self) -> None:
        """The destination side already skips fences; the source side now agrees.

        A link inside ``` is documentation of a link, not a link. Both non-routes are
        checked here together so the two strippers cannot drift apart silently.
        """
        live = "[§21c](" + SURFACE + "#21c-stop-policy)"
        self.assertEqual({"21c-stop-policy"}, anchors_in(live))
        self.assertEqual(set(), anchors_in("```\n" + live + "\n```"))
        self.assertEqual({"21c-stop-policy"}, anchors_in("```\n" + live + "\n```\n" + live),
                         "a fenced copy must not suppress a real one beside it")

    def test_an_unbalanced_comment_fails_CLOSED_and_that_is_the_safe_direction(self) -> None:
        """The residual the stripper keeps, asserted rather than left to be rediscovered.

        An unterminated `<!--` swallows a live link, so the suite goes RED on a surface
        that is in fact routed. A reachability check that errs toward "unreachable" sends
        someone to look; one that errs the other way certifies a rule nobody loads.
        """
        live = "[§21c](" + SURFACE + "#21c-stop-policy)"
        self.assertEqual(set(), anchors_in("<!-- unterminated\n" + live + "\n--> tail"))

    def test_the_limit_this_suite_does_not_close_is_stated_and_true(self) -> None:
        """Blind review's counter-example (B), NOT closed — recorded rather than hidden.

        A live link standing next to a sentence that disowns it still passes, and no string
        test separates those two. This asserts the weakness so it stays visible: if someone
        later believes the suite excludes anti-routes, this case says otherwise in the one
        place they will run.
        """
        disowned = ("[§21c](" + SURFACE + "#21c-stop-policy) and "
                    "[§21d](" + SURFACE + "#21d-decision-authority) "
                    "are **DEPRECATED — do not read them**.")
        self.assertEqual({"21c-stop-policy", "21d-decision-authority"}, anchors_in(disowned))
        self.assertIn("cannot be by this method", __doc__ or "",
                      "the docstring must keep stating the limit this case demonstrates")

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
