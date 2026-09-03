#!/usr/bin/env python3
"""The stop policy must live on the surface every actor loads, and stay reachable from the router.

A rule an actor never loads is not a rule. `CLAUDE.md` became a router on 2026-08-16 and the
operating law moved to `framework/instruction/LEGEND_CORE.md`; a stop policy is operating law,
so it belongs there. This suite fails on three distinct regressions, and each one has actually
cost a session: the text is paraphrased rather than carried (a paraphrase is a different rule);
the text is dropped; or the router stops naming its destination, which is the moment an actor
loads the chain and never reaches the rule at all.

Reachability is asserted PER SURFACE, over the surfaces every actor loads, rather than as "some
member of `ROUTER_CHAIN` mentions the file". The weaker form was satisfied by a single incidental
YAML field and would still have passed with `CLAUDE.md`'s own reference deleted — Mirror's F4
finding against the first version of this suite. The four suites this repository already trusts
for obligation reachability assert per named file, and this one now matches them. `ROUTER_CHAIN`
is still imported rather than restated, so the chain is checked against the router's own copy and
never against a second one that could agree while the real chain was broken.

Provenance of both ratified blocks below:
`governance/decisions/DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY.md`.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

from runtime_parity import ROUTER_CHAIN  # noqa: E402

SURFACE = Path("framework/instruction/LEGEND_CORE.md")

# Asserted individually, the way test_fulltext_trace_contract.py and its three siblings assert
# their obligations: a fixed tuple of named files, each checked on its own. Both are loaded every
# session — CLAUDE.md by the harness, the state manifest by CLAUDE.md §0's "first, every session"
# — so deleting either reference fails this suite, which "any member of the chain" did not.
ALWAYS_LOADED = ("CLAUDE.md", "framework/state/state_manifest_current.md")

# Verbatim, sha256 776e6556d5fbbac3d23fd99e15a3b1bce416d27d17f6701685bd93369030f941 over the 42
# lines below. Anchored to DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY rather than to a bare
# date: a date records when someone typed the text, a hash records which bytes were ratified. A
# paraphrase is a different rule, so this is compared as one block and never token by token.
STOP_POLICY = """STOP POLICY (HARD RULE, operator decision 2026-09-03)

An actor stops only for one of three reasons:
  1. a guard denial;
  2. an act reserved to the operator by H.1 with no sanctioned alternative;
  3. a condition with NO safe default.

Every other condition has a safe default. The actor takes the default, continues, and
records it in the report under the heading DEFAULTS_TAKEN (condition · default taken · why
it is safe · what would have been different). Idle peer sessions, stale counts, unverified
prior figures, missing operator presence are conditions with a safe default, never reasons
to stop.

When an actor stops, it says in four lines: what the act does; why it is reserved; what the
operator pastes in the terminal; what the operator pastes back. If the actor believes the
reserved act should pass to agents, it adds one yes/no question with one line on what
changes if the answer is yes.

Nothing waits on operator presence except a reason 1–3 stop. Mirror reviews DEFAULTS_TAKEN
after the fact; a wrong default is a finding, not a reason to have stopped.

STOP LOG. Every stop — taken or avoided — is recorded in the report under STOP_LOG:
reason class (1 guard · 2 reserved act · 3 no safe default) · what was asked · time
waited · outcome.
  Class 2 entries carry the yes/no question. An operator YES retires that stop permanently
  and is recorded as a decision.
  Class 3 entries carry the hindsight default: "the safe default would have been X".
  X is added to SAFE_DEFAULTS in this policy by the next dispatch that touches it.
A stop that recurs after its default or decision exists is a finding against the actor.
Target on any unattended deployment: STOP_LOG class 3 = 0; class 2 = 0 after the
operator's decisions; class 1 only.

SAFE_DEFAULTS is the one part of this policy agents may extend, by appending an entry
under Class 3 above; the rules stated before it, and all of §21d, are reserved to the
operator.

SAFE_DEFAULTS (seeded from 2026-09-02/03):
  - idle peer sessions on a shared checkout → proceed, note them
  - prior-report figures not re-derivable in minutes → treat as hypothesis, proceed
  - population counts that decay (refs, worktrees) → re-derive at start, never wait
  - a test that fails on a dead premise when enrolled → enroll, leave red, report
  - a report that exists only in a transcript → persist verbatim, note the source"""

# The companion rule: same day, same surface, same DEC. sha256
# a1eff7741ffe03f8349b49f4d38e23be5bed4cd1725dfaf58473fdaf631029ba over the 32 lines below. It
# names itself a fundamental guarantee, so drift in it is reserved to the operator by its own
# terms — which is exactly why it is asserted verbatim. SAFE_DEFAULTS is the one carve-out, and
# it is stated inside the RESERVED list so the exemption lives where the reservation does.
DECISION_AUTHORITY = """DECISION AUTHORITY (HARD RULE, operator decision 2026-09-03)

The Orchestrator decides every question not on the RESERVED list, consulting Plan
(measurement) and Mirror (hostile review) when it judges necessary. Consultation is
mandatory only where a guarantee requires it: Mirror on any non-zero scientific delta;
producer ≠ verifier on scientific claims. §21d reassigns to the Orchestrator only the
decisions H.1 assigns to the Operator. It moves no authority H.1 assigns to Scientist,
Plan or Mirror.

RESERVED to the operator (exceptions, by nature not by habit):
  - publication to origin or any public surface
  - history rewrite
  - irreversible deletion of unique material
  - a change to a fundamental guarantee — including this list, all of §21d, and the STOP
    POLICY body. SAFE_DEFAULTS is the sole exception: §21c authorises agents to append a
    hindsight default there, and an append is not a change to the STOP POLICY body it
    sits inside.
  - external spend above the declared default
  - exposure of private or patient data outside the declared perimeter

Everything else: decide, act, record. Each decision goes in the report under
DECISIONS_TAKEN: what · alternatives rejected · who was consulted · reversibility ·
how to revert. Mirror reviews DECISIONS_TAKEN after the fact. The operator reads it when
present; a wrong decision is a finding and a revert, never a reason to have waited.

Operator decisions already taken (2026-09-03), retiring class-2 stops:
  - branch switch inside a single-owner worktree: agents. Root: reserved.
  - worktree provisioning: agents, once the guard false refusal is fixed (0B).
  - birth of bound sessions: BOOTSTRAP automates it; not an operator act per dispatch.
  - push of an actor's own branch to `development`: agents, PROVIDED development is
    credential-gated. Orchestrator verifies and records the verification. origin stays
    reserved."""


class TheStopPolicyIsCarriedWhereActorsLoadIt(unittest.TestCase):
    def surface_text(self) -> str:
        return (ROOT / SURFACE).read_text(encoding="utf-8")

    def test_the_stop_policy_is_present_verbatim(self) -> None:
        self.assertIn(
            STOP_POLICY, self.surface_text(),
            f"{SURFACE} no longer carries the ratified stop policy verbatim. Restore the "
            "text, or have the operator ratify a replacement — editing it here instead "
            "would let the rule and its test drift together.")

    def test_the_decision_authority_is_present_verbatim(self) -> None:
        self.assertIn(
            DECISION_AUTHORITY, self.surface_text(),
            f"{SURFACE} no longer carries the ratified decision authority verbatim. Its "
            "RESERVED list is a fundamental guarantee by its own text, so a change to it "
            "is an operator act — restore it rather than editing this constant.")

    def test_every_always_loaded_surface_names_the_destination(self) -> None:
        """Per surface, not "any member of the chain" — one deleted reference must fail this.

        The predicate is the router's own (name or path appears in the text), but the quantifier
        is universal over ALWAYS_LOADED rather than existential over ROUTER_CHAIN. Under the old
        form the state manifest's `framework_file:` YAML field alone kept this green, so removing
        the router's actual instruction to read LEGEND_CORE.md changed nothing here.
        """
        missing = []
        for surface in ALWAYS_LOADED:
            text = (ROOT / surface).read_text(encoding="utf-8", errors="replace")
            if str(SURFACE) not in text and SURFACE.name not in text:
                missing.append(surface)
        self.assertFalse(
            missing,
            f"these always-loaded surfaces no longer name {SURFACE}, so an actor that loads "
            f"them is never routed to the stop policy: {missing}")

    def test_the_chain_resolves_and_still_covers_the_asserted_surfaces(self) -> None:
        """A chain that names a destination it cannot resolve is not a route."""
        unresolvable = [str(m) for m in ROUTER_CHAIN if not (ROOT / m).exists()]
        self.assertFalse(unresolvable, f"ROUTER_CHAIN members absent from the tree: {unresolvable}")
        outside = [s for s in ALWAYS_LOADED if s not in {str(m) for m in ROUTER_CHAIN}]
        self.assertFalse(
            outside,
            f"asserted surfaces that are no longer ROUTER_CHAIN members: {outside}. Either the "
            "chain changed or this tuple drifted — reconcile them, rather than asserting on a "
            "surface the router no longer routes through.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
