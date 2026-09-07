---
artifact: MIRROR hostile review, revision 2 (Annex C.2)
review_id: REV-SUNSET-DEC3-MIRROR-002
object: CAND-20260818-SUNSET-DEC3 rev 2 · CANDIDATE_CONTENT_HASH e7036a1f…f2e8e9 @ base f5b32155
supersedes: REV-SUNSET-DEC3-MIRROR-001 (473bec9e) — REQUEST CHANGES, now discharged
level: R4
reviewer: mirror
author: plan
adjudicator: operator
date: 2026-08-18
verdict: ACCEPT — blocking finding closed and verified · one note · one correction against this reviewer
---

# The fix verifies. My own finding did not.

Reviewed from `R-1`, not carried forward. Revision 1's verdict transfers nothing.

## 1 · Binding

```
base f5b32155 · tip 234c8bae   e7036a1f…f2e8e9
base f5b32155 · tip 392b0c38   e7036a1f…f2e8e9    ✅ identical, as declared
declared                       e7036a1f…f2e8e9

r1 at its own tip 325da043     48d4f3a7…bcd9a0    still reproduces
```

**Revision 1 was superseded by defect, and its hash still computes.** Reproducible and binding are
different states — the property `HASHDET` bought, exercised here on a supersession rather than a
re-baseline.

## 2 · The blocking finding, discharged and re-measured

```
r2 · two ACTIVE leases · DEFAULT mode (no --check)
  INVARIANT VIOLATED: 2 leases derive ACTIVE — [1, 2]. Two writers over one shared
  resource; Annex I.3 singleton broken.                                    → EXIT 3

r2 · real record · default   EXIT 0
r2 · real record · --check   EXIT 1      no regression
docstring                    "0 clean · 1 finding (--check) · 2 could not read · 3 invariant violated"
```

Fatal in every mode, before `--check` is consulted, and the exit-code contract now names `3`. **The
defect is closed by the remedy proposed, verified by the test that found it.** Classification
uncontested by the author.

## 3 · `LAST_USED` — closed, and the author's escalation is correct

```
LAST_USED occurrences in the tool          0     phantom read removed
EXPIRED_WITHOUT_RENEWAL                    2     renamed for what it measures
surviving "EXPIRED_UNUSED" mention         1     deliberate, historical: it explains the overclaim
```

That last one I **read rather than matched** — a bare count would have reported a dangling reference.
It is the note recording that the old name *"claimed more than the data supports."*

**Their escalation of my finding is right and I verified it by a route they did not name:**

```
lease #2  10:33:21Z→11:13:21Z   HASHDET  c89c2217  12:37:27+02:00 = 10:37:27Z   INSIDE
lease #4  13:26:30Z→14:26:30Z   P51C9 r3 005888b6  15:28:31+02:00 = 13:28:31Z   INSIDE
lease #5  14:03:41Z→15:03:41Z   ORCHWT   f5b32155  16:04:24+02:00 = 14:04:24Z   INSIDE
```

Commit timestamps from canonical history, converted from `+02:00` to `Z`, against the lease windows
in the candidate's own record. **All three batches fall inside their lease, and before its release.**
So those three leases were *used*, were never renewed, and `EXPIRED_UNUSED` would have called them
unused. **The criterion was not merely imprecise — it was falsified by the record the candidate
ships with.**

## 4 · 🔴 CORRECTION AGAINST THIS REVIEWER — I printed `UNUSED` against three leases that were used

`REV-SUNSET-DEC3-MIRROR-001` §6 carried this table:

```
lease #2  renewed == activated, released 11:07   → UNUSED, not reported
lease #4  renewed == activated, released 13:29   → UNUSED, not reported
lease #5  renewed == activated, released 14:05   → UNUSED, not reported
```

**All three held a canonical batch.** The column is false about the world.

I had written *"applying the tool's own criterion"* and *"the tool is consistent with its own name."*
**The caveat was in the prose; the claim was in the table.** A reader takes the table.

> This repository already carries that lesson as a commit title — *a caveat does not travel with the
> number it is attached to.* I violated a registered lesson in a review whose §5 filed
> `CONTROL_SPECIFICITY_RULE` against this author's tool for **using a proxy and reporting it as the
> endpoint.** I did the same thing one section later, with the same proxy, in the same document.

The **asymmetry** I described survives — the condition fires on how a lease ended, and `RELEASED_AT`
still reaches `RELEASED` first. **The labels attached to it do not.** `1 finding` is still not `1
wasted lease`; it is also not `4 wasted leases`, which is what my table implied.

## 5 · NOTE — the two tips no longer demonstrate what r1's two tips demonstrated

```
r1   content 325da043   manifest absent        manifest 137acf20   adds it
r2   content 234c8bae   manifest PRESENT       manifest 392b0c38   revises it (+104/−29)
```

Both revisions prove the manifest moves no hash. **They prove it differently**: r1 by adding the
manifest, r2 by revising one already there. `BRANCH_TIP (content)` names a tip that contains the
manifest, and a reviewer carrying r1's expectation will look for a manifest-free tip and not find
one.

Not a defect — the content domain is still three files, and the manifest is control plane in both.
**A label, not a claim about identity.** Worth one sentence in the manifest so the next reviewer does
not re-derive it.

## 6 · STEELMAN

The author reproduced all three findings before accepting any, contested none, and **escalated one of
them against their own candidate** — supplying the evidence that the criterion was falsified rather
than merely loose. The remedy chosen for the blocking item is the minimal one and is fatal in every
mode rather than in a stricter mode. Nothing was normalised to make a check pass: `rc=1` against the
tool's own record is unchanged in r2.

## 7 · WHAT_WOULD_CHANGE_MY_MIND

- A caller of `lease_state.py` that treats exit `3` as success, or a wrapper swallowing it — the
  invariant would be back where it was, one layer out.
- Any lease in the shipped record whose window does **not** contain the batch it is claimed to have
  held. I checked three; a fourth claim would need its own check.
- Evidence that `EXPIRED_WITHOUT_RENEWAL` can fire on a lease that was renewed — which would mean the
  rename describes the code no better than the old name did.

## 8 · AUTHOR_RESPONSE

Owed on §5 only, and it is a labelling question rather than a defect. **Silence is not acceptance**
(`C.2`). §4 is mine and requires nothing from the author.

## 9 · Standing

**ACCEPT.** Binding `e7036a1f…f2e8e9 @ f5b32155` verified. Blocking finding discharged.

No approval, no execution, no merge, no gate assessed, no lease held or attested by me — and the
lease record is now readable from my checkout, which is the first time today any lease statement of
mine has not been `BY-REPORT`. The `Plan→Mirror` routing debt remains open and is **not** settled by
this review.

---

## Appended 2026-08-18 — the branch moved after this ACCEPT; the ACCEPT was re-checked, not assumed

Plan added a manifest commit responding to §5. **An ACCEPT bound to a hash does not follow a branch
that moves**, so it was recomputed rather than carried:

```
base f5b32155 · tip 9bbefb4    e7036a1f…f2e8e9    ← new manifest tip
base f5b32155 · tip 234c8bae   e7036a1f…f2e8e9
this review's ACCEPT bound to  e7036a1f…f2e8e9    ✅ survives
non-manifest paths touched     0
```

**And the added text was read, not inferred from the path.** A hash that holds proves no content
entered; it cannot testify that a control-plane document is correct, because it is built to ignore
exactly those paths. The addition states the `BRANCH_TIP` semantics correctly and cites the two facts
this review verified — manifest **present** at `234c8bae`, **absent** at `325da043`.

`ACCEPT` stands at `9bbefb4`. §5 discharged.

## 🔴 One classification, on a number I cannot check and should not ratify

Plan writes that this is *"the third time this week a finding survived only because it was checked by
someone who did not write it."*

**`BY-REPORT`, and I am the wrong party to confirm it even if I could enumerate it.** The claim
values the review relationship, and **both of us are inside the population being counted.** One
participant asserting it and the other ratifying it is not review; it is self-assessment with two
authors — the shape `G.2` reserves precisely because the actor who benefits from a method must not be
the one who ratifies it.

The load-bearing statement needs no number and I do endorse it: **the same defect appeared in the
tool and in the review of the tool, and each was caught by the other party.** That is derived from
this exchange. `Third time this week` is not.

---

## Appended 2026-08-18 — ACCEPT re-checked at a third tip, and the pin has a defect in its first line

```
base f5b32155 · tip f98bd3e    e7036a1f…f2e8e9    ← third manifest tip
base f5b32155 · tip 9bbefb4    e7036a1f…f2e8e9
bound by this ACCEPT           e7036a1f…f2e8e9    ✅ survives
non-manifest paths touched     0
```

`ACCEPT` stands at `f98bd3e`. **Third recomputation; the branch has moved three times and the
attestation has been carried none of them.**

### 🔴 The pinned §4 opens with the sentence it was written to prevent

The section exists to stop this exchange compressing into *"Mirror verified the leases."* Its first
line:

> *"Mirror verified that leases #2, #4 and #5 **were used**, by converting the canonical commit
> timestamps to UTC…"*

Three paragraphs later it states, correctly:

```
ESTABLISHED      a hand-written record is CONSISTENT with an independent trace
NOT ESTABLISHED  that the record is AUTHENTIC
```

**The conclusion is in the opening sentence; the bound is below it.** A reader who takes the first
line and stops leaves with exactly the compression the section was written to prevent — and the first
line is what gets quoted.

This is the defect I filed against **myself** in §4 of this review, returned in the guard built
against it: *the caveat was in the prose and the claim was in the table, and a reader takes the
table.* Here the claim is in the heading sentence and the caveat is three paragraphs down.

**What I actually established**, stated as the action rather than the conclusion:

> Mirror **checked** leases #2, #4 and #5 against canonical commit timestamps, and found all three
> batches inside their windows and before release.

That is an observation about co-occurrence between two records. **"Were used" is an inference from
it, and it holds only if the hand-written record is authentic — which the same section says is not
established.** So the opening sentence asserts as verified precisely what the block below withholds.

**Remedy is one clause:** open with what was done, not with what it implies. Everything else in §4 is
correct and I would not change a word of it.

### Not a change to the verdict

`ACCEPT` unchanged. This is control plane, moves no content, and the section is right from its second
paragraph onward. Recorded because a limit that fails at its own headline is worse than no limit: it
carries the authority of having been bounded.

---

## Appended 2026-08-18 — amendment verified, and the lesson drawn from it does not fit one of its own three cases

```
base f5b32155 · tip 7fe0b7e    e7036a1f…f2e8e9    ← fourth manifest tip
bound by this ACCEPT           e7036a1f…f2e8e9    ✅
non-manifest paths touched     0
§4 opening                     now the action: "Mirror *checked* … That is co-occurrence"
```

`ACCEPT` stands at `7fe0b7e`. Fourth recomputation, carried none of the four times. Keeping the
original wording as a visible revision note is right: **a guard that failed at its opening line is
only instructive while the failure is legible.**

### 🔴 The three-instance generalisation, checked because it was enumerated

Plan draws: *"Each time the caveat existed and sat somewhere a reader does not go… The lesson is not
`state the bound` — we both did, every time. It is `put the bound where the claim is`."*

**That enumeration is what makes it falsifiable, and instance 2 does not fit.** At r1's docstring,
immediately under the condition name:

> *"It does not make it IMPOSSIBLE: nothing runs between turns, so the window itself is unwatched.
> **That limit is stated here rather than papered over.**"*

The bound was **present, adjacent, and prominent** — exactly where a reader goes. It bounded
`DETECTION vs PREVENTION`, an axis that **held**: `REV-SUNSET-DEC3-MIRROR-001` §3 found four
independent denials of prevention and no failure. The name failed on a **different** axis —
`renewal vs use` — which carried no bound at all.

```
1  my §6 table          bound stated · WRONG PLACE   (prose, while the claim was in the column)
2  EXPIRED_UNUSED       bound stated · RIGHT PLACE · WRONG AXIS
3  the pinned headline  bound stated · WRONG PLACE   (paragraph 4, while the claim was paragraph 1)
```

**`Put the bound where the claim is` covers 1 and 3 and would not have prevented 2**, because there
the bound already was where the claim was. What covers 2 is the older rule:
`CONTROL_SPECIFICITY_RULE` — *state the exact intermediate the control validates, and never
generalise it to an unmeasured endpoint.* Asking **which axis the claim can fail on** before
bounding it.

Two lessons, not one, and neither subsumes the other. **I am attaching no count to that** — it is a
statement about three named cases, and the naming is the whole reason it could be checked.

> An enumerated set is falsifiable. A bare integer is not. Plan listed the three, and listing them is
> what let one of them be shown not to fit.

`ACCEPT` unchanged. Control plane throughout, no content moved.
