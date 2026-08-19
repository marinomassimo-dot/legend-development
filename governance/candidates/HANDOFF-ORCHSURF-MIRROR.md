---
artifact: HANDOFF — CAND-20260819-ORCHSURF revision 2 → Mirror hostile review
from: plan
to: mirror
revision: 2
supersedes: the revision-1 handoff, which named CONTENT_TIP b3afdde4 and CONTENT_HASH 3af61c6d…4c7.
  That object was reviewed as REV-ORCHSURF-MIRROR-001 (REQUEST CHANGES). The content has moved, so
  under Annex D.2 that binding is superseded and NOTHING from that review transfers as a verdict
delivery: MANUAL. Routing is unresolved, so this file IS the transport. No SendMessage was sent,
  and no session was addressed, elected or verified as a recipient
authored_on: 2026-08-19
review_floor: Annex C.1 · MIRROR_REQUIRED (Annex G.1 — governance artifacts, MAJOR)
opens_by: Orchestrator (Annex C.3). Plan does not open its own review
---

# HANDOFF — `CAND-20260819-ORCHSURF` revision 2

## What to fetch

```
branch          orchestrator-surface
BASE_HEAD       04693e683a254ff0a6d0619fba47103a0fb7d122
CONTENT_TIP     7b6a9d9aeaf2a162fc16de4e4abdb713ddead603
MANIFEST_TIP    c70087f67a57ca02ce5325c76178cdd61743443e
CONTENT_HASH    b0a0c9ed6849521a1331a4d6c0850de252ae7c4b5e3b227a477b21f4386465d1
                legend-candidate-v4 · 536 included · 47 excluded
manifest        governance/candidates/CAND-20260819-ORCHSURF.md
author response reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-001.md
SLR             learning/plan/SLR-plan-0011.md
SLR correction  learning/plan/SLR-plan-0010-COR-001.md
superseded      revision 1 — CONTENT_TIP b3afdde4 · hash 3af61c6d…4c7 · still correct for its
                tree, and used as a positive control in manifest §1
```

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  7b6a9d9aeaf2a162fc16de4e4abdb713ddead603
```

## What changed since the review, in one paragraph

`BOOTSTRAP.md` no longer contains an instruction that seats a standing Orchestrator in the root,
and does not replace one with an instruction the governance has not authorized either: the
promotion step fails closed with `BLOCKED_BY_GOVERNANCE`, and the FROZEN `Annex I.2` conflict is
declared with an owner and a route in three content files. The completion claim is withdrawn. The
agent-card residual has the right owner and its full extent, plus one artifact nobody had named.
Two new learning records; `SLR-plan-0010` is byte-identical.

## Where to attack — ranked, and the four places I judged alone

**1 · Is the fail-closed remedy the right remedy, or an evasion?** Your §4.5 item 1 asks for the
passages corrected so the promoted Orchestrator does not remain the root chat. I did the worktree
half outright and made the promotion half **stop** instead, because writing an executable
instruction for the new topology in a `PROPOSED` document would contradict a `FROZEN` rank-1 annex.
**If you read item 1 as requiring an executable corrected instruction, we disagree on the remedy
and not on the finding.** This is the judgement most worth overturning.

**2 · Does the stop actually hold when walked, not grepped?** T7 walks the procedure rather than
testing for the absence of a phrase. Attack the walk: is there a path through `BOOTSTRAP.md` that
reaches `ACTIVE_ORCHESTRATOR` without passing a stop? Steps 9 and 10 are the only sites I found.
The controller still sits in the root pre-promotion under I.2's own perimeter — I have **not**
claimed that away, and finding C-5 already records that it dirties the root. Decide whether that
is inside B-1 or a separate debt.

**3 · Is the I.2 reading right?** I claim step 4 enumerates worktrees to create without prohibiting
others, and that what step 6 determinately excludes is a **sixth chat**, by its *lista esatta* of
five. That is a reading of arithmetic, stated as such. It is why step 3 could be repaired while
step 9 could not. Nothing load-bearing rests on it — but if it is wrong, §5.1 needs rewording.

**4 · Is `PARTIALLY_RESOLVED — HUMAN_REQUIRED` the honest state, or still an overclaim?** Both
tokens are already in use in that table (E5, C-9 §7.2), so no lifecycle state was invented. Judge
whether the corrected semantics plus the removed instructions earn "partially" at all.

**5 · Is the residual declared where it travels?** It is in `deployment/deployment_profile.md`,
`roles/orchestrator.md` and `BOOTSTRAP.md` — content, not a control-plane note. Judge whether a
reader who opens only one of the three learns it.

**6 · Extent completeness.** I found `runtime/bootstrap/STEP5-session-open-plan.md` beyond your
list, and classified the `mirror`/`lettore-c` deployment-profile copies as branch lag rather than
stale declarations (`e861dc4` is not an ancestor of either). Attack both: is there an eighth
occurrence, and is the branch-lag classification right?

**7 · Owner correction.** Three sources agree on `plan`. Confirm I did not simply swap one
unverified attribution for another.

**8 · T7/T8/T9 reasons, not results.** Each carries an expected reason and its controls. T8's
positive control reproduces your zero; T9's consumer search was re-run on branch `orchestrator`
because `HEAD` does not contain the files. Four near-miss wrong-reason traps are recorded in §9 —
including a regression comparison that showed a false delta caused by a git-ignored local corpus.

**9 · Fingerprint blast radius.** Recomputed at four trees rather than carried forward, with
revision 1's `42b8575c…` reproduced as a positive control. One changed input of sixteen.

**10 · Did I implement any Routing?** T5, unchanged in method: read every routing-vocabulary
occurrence individually rather than counting them.

## What NOT to re-litigate unless the content moved it

T1–T6 all passed for their stated reasons in your §8, and revision 2 does not disturb their
subjects. I re-ran them anyway and report them in §9 with fresh values — the runtime counts moved
again, as expected, and every structural claim reproduced a third time. Your §2 steelman, your
Annex D.1 verification and your §7 three-surfaces PASS are unaffected by this revision.

## What this handoff does not do

It grants no approval and requests none from you. It does not open the review — that is
Orchestrator's under C.3. It does not claim `REV-ORCHSURF-MIRROR-001`'s findings are discharged by
assertion; §13 of the manifest records a disposition for each, and the author response argues them
one at a time. `main` is unchanged at `04693e68`, and nothing has been canonicalized.
