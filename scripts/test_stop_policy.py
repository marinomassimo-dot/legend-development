#!/usr/bin/env python3
"""The stop policy must live on the surface every actor loads, and stay reachable from the router.

A rule an actor never loads is not a rule. `CLAUDE.md` became a router on 2026-08-16 and the
operating law moved to `framework/instruction/LEGEND_CORE.md`; a stop policy is operating law,
so it belongs there. This suite fails on three distinct regressions, and each one has actually
cost a session: the text is paraphrased rather than carried (a paraphrase is a different rule);
the text is dropped; or the router stops naming its destination, which is the moment an actor
loads the chain and never reaches the rule at all.

Reachability is asserted with the router's own predicate — `ROUTER_CHAIN` is imported rather
than restated, because a second copy of the chain would pass this test while the real chain
was broken.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

from runtime_parity import ROUTER_CHAIN  # noqa: E402

SURFACE = Path("framework/instruction/LEGEND_CORE.md")

# Verbatim. The operator ratified this text on 2026-09-03; a paraphrase is a different rule,
# so this is compared as one block and not probed token by token.
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

SAFE_DEFAULTS (seeded from 2026-09-02/03):
  - idle peer sessions on a shared checkout → proceed, note them
  - prior-report figures not re-derivable in minutes → treat as hypothesis, proceed
  - population counts that decay (refs, worktrees) → re-derive at start, never wait
  - a test that fails on a dead premise when enrolled → enroll, leave red, report
  - a report that exists only in a transcript → persist verbatim, note the source"""

# The companion rule, ratified the same day and carried on the same surface. It names itself
# a fundamental guarantee ("including this list and the STOP POLICY"), so drift in it is
# reserved to the operator by its own terms — which is exactly why it is asserted verbatim.
DECISION_AUTHORITY = """DECISION AUTHORITY (HARD RULE, operator decision 2026-09-03)

The Orchestrator decides every question not on the RESERVED list, consulting Plan
(measurement) and Mirror (hostile review) when it judges necessary. Consultation is
mandatory only where a guarantee requires it: Mirror on any non-zero scientific delta;
producer ≠ verifier on scientific claims.

RESERVED to the operator (exceptions, by nature not by habit):
  - publication to origin or any public surface
  - history rewrite
  - irreversible deletion of unique material
  - a change to a fundamental guarantee — including this list and the STOP POLICY
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

    def test_the_surface_is_reachable_from_the_router_chain(self) -> None:
        """Same predicate `runtime_parity` uses: a chain member must NAME the destination."""
        naming = []
        for member in ROUTER_CHAIN:
            path = ROOT / member
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if str(SURFACE) in text or SURFACE.name in text:
                naming.append(str(member))
        self.assertTrue(
            naming,
            f"no member of ROUTER_CHAIN names {SURFACE}, so an actor traversing the chain "
            "never reaches the stop policy. Name it from a chain member.")

    def test_the_chain_member_that_names_it_is_itself_present(self) -> None:
        """A chain that names a destination it cannot resolve is not a route."""
        unresolvable = [str(m) for m in ROUTER_CHAIN if not (ROOT / m).exists()]
        self.assertFalse(unresolvable, f"ROUTER_CHAIN members absent from the tree: {unresolvable}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
