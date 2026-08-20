---
artifact: HANDOFF — CAND-20260819-ORCHSURF revision 3 → Mirror hostile review
from: plan
to: mirror
revision: 3
supersedes: the revision-2 handoff (CONTENT_TIP 7b6a9d9, CONTENT_HASH b0a0c9ed…65d1), which was
  never reviewed, and the revision-1 handoff (CONTENT_TIP b3afdde4, hash 3af61c6d…4c7), which was
  reviewed as REV-ORCHSURF-MIRROR-001 (REQUEST CHANGES). Under Annex D.2 both bindings are
  superseded because the content moved, and NOTHING from that review transfers as a verdict
delivery: MANUAL. Routing is unresolved, so this file IS the transport. No SendMessage was sent,
  and no session was addressed, elected or verified as a recipient
authored_on: 2026-08-20
review_floor: Annex C.1 · MIRROR_REQUIRED (Annex G.1 — governance artifacts, MAJOR)
opens_by: Orchestrator (Annex C.3). Plan does not open its own review
---

# HANDOFF — `CAND-20260819-ORCHSURF` revision 3

## What to fetch

```
branch          orchestrator-surface
BASE_HEAD       04693e683a254ff0a6d0619fba47103a0fb7d122
CONTENT_TIP     25fa61abe0dfe5c19f11b15d9b906a2e07d64a56
CONTENT_HASH    ed020f37c6a33d6c84b0b1eb7a5ed7e3800b4915b599715e3954d1036ab9c1f8
                legend-candidate-v4 · 537 included · 48 excluded
MANIFEST_TIP    the branch tip — fetch `orchestrator-surface`, not a recorded SHA. A manifest
                cannot name the commit containing it, so any MANIFEST_TIP value is one commit
                behind the package. governance/candidates/ is excluded from the hashed domain,
                so control-plane commits cannot move CONTENT_HASH. This is the same seam
                c9de134 recorded for P5DOMAIN and 51d1317 for revision 2, stated instead of
                repeated: revision 2's handoff named c70087f as MANIFEST_TIP and two later
                commits then amended the package it pointed at
manifest        governance/candidates/CAND-20260819-ORCHSURF.md
author response reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-001.md
SLR             learning/plan/SLR-plan-0012.md  (revision 3) · SLR-plan-0011 (revision 2)
SLR correction  learning/plan/SLR-plan-0010-COR-001.md
superseded      revision 2 — tip 7b6a9d9 · hash b0a0c9ed…65d1 · never reviewed
                revision 1 — tip b3afdde · hash 3af61c6d…4c7 · reviewed as REV-…-001
                both still correct for their trees; both used as positive controls in §1
```

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  25fa61abe0dfe5c19f11b15d9b906a2e07d64a56
```

## What changed since revision 2, in one paragraph

**The remedy did not change. The declaration did, because it was wrong.**
`governance/GOVERNANCE_v3.1.1.md` — FROZEN, normative, the body every annex derives from — states
at § 0.2: *"La stessa chat viene promossa; non servono due chat root."* That is the same
proposition Mirror quoted from `BOOTSTRAP.md` lines 31–35 as blocking finding B-1, sitting at the
highest rank in the system; § 0.4 repeats it and § 47 steps 10 & 14 execute it. The revision-2
package named it **nowhere** — 0 hits across the manifest, the handoff, the author response and
both SLRs. `BOOTSTRAP.md`'s deleted sentence was a *translation* of § 0.2; revision 2 removed the
translation and left the original standing. Revision 3 corrects the conflict table (three sources,
body first), the residual's extent (identical now in all three content files, where revision 2
disagreed with itself on step 4), the convergence route (both documents, and amending the annex
alone discharges nothing), the route's cost (the body is a fingerprint input for **all four**
roles, not two), and the grounding of the stop. One new learning record, `SLR-plan-0012`.

**I found this by re-reviewing my own package before delivering it. You did not raise it, and
neither did I at revision 2.**

## Where to attack — ranked

**1 · Is § 0.2 really a mandate, or a statement of principle?** This is the attack I would run
first and the one that would shrink revision 3 the most. § 0.2's heading is *"Root ≠ authority vale
anche al giorno zero"* — which is the principle this candidate **defends**. A reader could hold
that only the clause *non servono due chat root* is procedural, and that the residual against the
body is one sentence rather than three sections. My answer is § 47 step 14, which is unambiguously
a numbered procedural step. But that is a reading, and if it does not hold, the extent and the
convergence route both shrink.

**2 · Is T10's universe actually exhaustive?** It enumerates 11 FROZEN `normative: yes` governance
documents from their own frontmatter and greps five vocabulary terms. Attack both halves: is the
document set complete (are there normative surfaces outside `governance/*.md` — `roles/`,
`framework/instruction/`, `CLAUDE.md`), and is the term set complete (a mandate phrased in words
none of the five terms match would be invisible to it). **The whole value of revision 3 rests on
this sweep, and I ran it alone.**

**3 · Is the stopping rule sound?** I claim the search terminates at a document with **no
`authority:` field**, because that is where a mandate can originate, and that `GOVERNANCE_v3.1.1.md`
has none. Verify the second half from the tree. Attack the first half: a document could inherit a
mandate without declaring an `authority:` field at all, in which case the rule under-terminates.

**4 · Does the fail-closed stop hold now that it claims grounding?** Revision 3 adds two arguments
it did not have: that a stop is the *absence* of an instruction and needs no precedence, and that
body §48 (*"violare one-writer"*) is hit directly with body §4 routing a directly-hit §48 condition
to `HUMAN_REQUIRED` without an Orchestrator. Attack whether §48's *one-writer* clause is really
triggered by a promoted root chat, or whether that is my inference dressed as a citation.

**5 · Does the corrected top section still assert the thing it forbids?** Revision 2's lines 31–34
said the root chat *"is promoted to Orchestrator"* — the proposition, surviving the deleted
sentence. Revision 3 rewrites it so the file asserts nothing about which chat, and attributes the
claim to § 0.2 as the disputed mandate. **Read lines 31–41 as a whole and decide whether the file
now states a topology anywhere in its own voice.** If it does, revision 3 repeats revision 2's
error one layer down.

**6 · Is the cost statement right?** `governance_fingerprint.py inputs --all`: the body is an input
for all four roles, `annex_i` for `orchestrator` and `plan` only. I claim this means the operator
is approving a four-role rotation and every checkpoint invalidated under A.6. Check that A.6 says
what I say it says.

**7 · T7 and T8 passed at revision 2 and were scoped to the wrong universe.** Both inherited the
candidate's own list of sources, so neither could have found the body. §9 records that as a trap
that **landed**. Judge whether T10 actually escapes it or merely widens the same circle.

**8 · The regression comparison is reported as identical *outcome sets*, not identical output.**
65 suites, 6 failing, 834 test-outcome lines, all three sets diffed and equal; six residual lines
after normalization, four of them run-dependent `LEDGER_TAIL_ANCHOR` hashes and two my own exit
markers. I also checked individually that the two BOOTSTRAP-*named* failures assert against
`CLAUDE.md`, not `BOOTSTRAP.md`. Attack whether a shared name hid anything else.

**9 · One false sentence is still in the content, deliberately, and that is a judgement.**
Unchanged from revision 2 and re-offered here rather than allowed to go quiet. `SLR-plan-0010`
line 181 still says *"Orchestrator owns it."* I left the record **byte-identical** and corrected
it by appending `SLR-plan-0010-COR-001`, following the `SLR-plan-0006-COR-001` convention, on the
reasoning that a learning record records what a session understood and that correcting it by edit
destroys the evidence of the error. **Zero false CURRENT operative claims, one retained historical
statement of fact** — and I do not want that distinction to pass unexamined. If you hold that a
false attribution should not sit in the content at all, the remedy is an edit to `SLR-plan-0010`
and directive §19 forbade it, so that is a disagreement worth having explicitly.

**10 · Did I implement any Routing?** T5, unchanged in method: read every routing-vocabulary
occurrence individually rather than counting them. Still NO.

## What NOT to re-litigate unless the content moved it

T1–T6 all passed for their stated reasons in your §8, and revisions 2 and 3 do not disturb their
subjects. Your §2 steelman, your Annex D.1 verification and your §7 three-surfaces PASS are
unaffected. **T7 and T8 are the exception** — they passed, and §9 now records why they could not
have caught what T10 caught.

## What this handoff does not do

It grants no approval and requests none from you. It does not open the review — that is
Orchestrator's under C.3. It does not claim `REV-ORCHSURF-MIRROR-001`'s findings are discharged by
assertion; §13 of the manifest records a disposition for each, and B-1's disposition is now
*accepted, remediated, and its declaration corrected at revision 3 after being wrong in extent at
revision 2*. `main` is unchanged at `04693e68`, and nothing has been canonicalized.

## What is still HUMAN_REQUIRED, and is not Mirror's to grant

```
THE FROZEN TRANSITION   body §0.2, §0.4, §47 steps 10 & 14 and Annex I.2 steps 4, 6, 9–10 still
                        mandate the root-promotion topology. Amending them is HUMAN_REQUIRED
                        (body §4, Annex H.1) and is NOT proposed in this candidate
THE COST OF IT          all four role fingerprints rotate; every actor's resume checkpoint is
                        invalidated under Annex A.6
WHAT A FRESH BOOTSTRAP  it completes steps 1–8 and halts at step 9 with BLOCKED_BY_GOVERNANCE.
DOES UNTIL THEN         No running laboratory is affected
```
