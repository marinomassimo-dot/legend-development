---
artifact: HANDOFF — CAND-20260819-ORCHSURF → Mirror hostile review
from: plan
to: mirror
delivery: MANUAL. Routing is unresolved, so this file IS the transport. No SendMessage was sent,
  and no session was addressed, elected or verified as a recipient
authored_on: 2026-08-19
review_floor: Annex C.1 · MIRROR_REQUIRED (Annex G.1 — governance artifacts)
opens_by: Orchestrator (Annex C.3). Plan does not open its own review
---

# HANDOFF — `CAND-20260819-ORCHSURF`

## What to fetch

```
branch          orchestrator-surface
BASE_HEAD       04693e683a254ff0a6d0619fba47103a0fb7d122
CONTENT_TIP     b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2
MANIFEST_TIP    c930889cc0bc000550976a57b3b961846ca282d1
CONTENT_HASH    3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
                legend-candidate-v4 · 534 included · 45 excluded
manifest        governance/candidates/CAND-20260819-ORCHSURF.md
SLR             learning/plan/SLR-plan-0010.md
```

Three content files changed, plus one SLR:
`roles/orchestrator.md` · `deployment/deployment_profile.md` · `BOOTSTRAP.md`

---

## The claim, stated so it can be attacked

Execution was never ambiguous; **labelling** was. Annex D.1 is `FROZEN`, correct, and untouched.
`roles/orchestrator.md` carried a line that was true on 2026-08-16 and false from 2026-08-17, and
`BOOTSTRAP.md` carried the same claim in a table that instructs a human. One untyped word,
`worktree`, was naming two different surfaces for one actor. Working directory is now prohibited
as an actor-identity discriminator, for every actor. No routing is implemented.

---

## Attack these, in this order

**1 · Was execution actually ambiguous?** I say NO and left Annex D.1 alone. If you find any
executing path whose behaviour depended on the stale frontmatter line, the whole framing is wrong
and the candidate should be reclassified, not amended. I searched and found only D.1-governed
execution — but §4.1 below is the place where I came closest to being wrong.

**2 · Is Annex D.1 unnecessarily modified?** It is not modified at all. Verify:
`git diff 04693e68..c930889 -- governance/` should show **only** the new candidate file. If a
single normative byte moved, block it.

**3 · Is `BOOTSTRAP.md` really the stronger finding, or am I inflating it?** I claim a fresh
bootstrap against the old table would have re-created the standing-writer-in-root condition that
`e861dc4` removed and `GATE 0` forbids. That is a counterfactual about an operation nobody has run
recently. Attack it: is the bootstrap path actually reachable, and does anything else downstream
correct the operator before damage? If the counterfactual fails, MAJOR may be too strong.

**4 · Is the stale text truly contradictory, or merely terse?** The body says *"Position in the
root confers nothing"* and *"must not treat the root as free working space"*, while the frontmatter
said the root was its worktree. I read that as self-contradiction. A defensible alternative is
that `worktree:` meant *"where this actor is opened"* and the body meant *"authority"* — two
compatible statements. If that reading holds, my correction is still right but my justification
is overstated, and the change class may drop.

**5 · Is cwd being promoted beyond the evidence?** I claim the runtime exposes no identity field
and that `name` is a function of `cwd` (17/17). Re-run it. If any session anywhere exposes an
actor or role attribute, requirement 5 and the whole "prohibited" verdict weaken to "corroborating".

**6 · Is root discovery merely broad, or genuinely non-actor-specific?** I explicitly retreated
from the inherited universal claim — see §6.1 of the manifest, and note that this **corrects a
canonical candidate's published reasoning while leaving its conclusion intact.** Decide whether
P5DOMAIN §8.3 needs its own remedy; I did not edit it, and I may be under-reacting.

**7 · Are ordinary actors and Orchestrator being forced into one model?** I deliberately did NOT
rename `worktree:` in the other three contracts, to hold the blast radius to one fingerprint. The
counter-argument is real: the schema is now non-uniform, and a future parser must handle a field
that exists in one contract only. If you judge uniformity worth three extra fingerprint rotations,
say so — that is a design call, and I made it alone.

**8 · Does the candidate accidentally implement Routing?** T5 says no. Note that grepping the diff
for routing vocabulary *does* return hits — they are the prohibitions themselves. Check that every
one is a denial and none is a mechanism.

**9 · Fingerprint blast radius.** orchestrator `88dea7a6…` → `42b8575c…`; the other three
byte-identical. Verify independently:
`python3 governance/scripts/governance_fingerprint.py compose --all` at `c930889`.
Confirm I changed no fingerprint *composition* — P2.2 is untouched.

**10 · Multi-runtime neutrality.** The measurement names `claude agents --json` and CLI 2.1.232.
Confirm the ontology does not depend on it — requirement 5 says the identity model must survive
that tool's replacement. If any normative sentence needs the tool to be meaningful, it is a leak.

**11 · Wrong-reason tests.** Four probes would have passed for the wrong reason and were caught
(manifest §9). Look for a fifth. The likeliest place is §6.1, where I corrected an inherited
reason while keeping its conclusion — agreement on a verdict is exactly the condition under which
nobody re-checks the premise.

---

## What I did not do, and will not do without you

```
no Mirror review self-performed        no CURRENT session elected
no HUMAN_APPROVAL requested/prefilled  no lease state written
no canonicalization                    no P5 reopened, no C-9 §7.2 touched
main UNCHANGED at 04693e68             Scientist A/B not activated, C untouched
                                       BENCH-AB-001 not started
```

**Residual, reported not fixed:** `runtime/agent_card_registry.md` on branch `orchestrator` still
says `WORKTREE: the root checkout # branch main`. Not canonical, not Plan's to touch.
Orchestrator owns it. The correction is incomplete without it, and I am saying so rather than
reaching across.
