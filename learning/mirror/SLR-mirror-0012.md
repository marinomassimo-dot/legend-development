---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0012
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC revision 4 — the census was made complete and
  the sentence describing it is printed in a mode where it is not produced
review: reviews/mirror/REV-SCIAB-MIRROR-004.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×1, third sighting on one seam) · MICRO_UPGRADE (×1, fourth and fifth
  instance of a defect already on file) · BEST_PRACTICE_CONFIRMATION (×1) ·
  CURATION (Annex E.2, over SLR-plan-0004)
derived_from: [SLR-mirror-0010, SLR-mirror-0011, SLR-plan-0003, SLR-plan-0004]
---

# A remediation is scoped to the mode the finding was measured in

## 1 · FAILURE_PATTERN — the finding names a population; the code has a second axis

`SLR-mirror-0011` §1 said *the artifact most likely to carry the next false claim is the one
written to correct the last one*, and `SLR-plan-0004` L-1 said the same thing from the author's
side — *the finding is a lower bound; the code is the denominator*. Both were written before
revision 4 was reviewed. Revision 4 is the third consecutive instance, and neither rule caught it.

The reason is that both rules are stated over the **population** axis and the recurrence happened
on a **mode** axis:

```
M-2  scoped to one spec key          → the exemption lived in two
M-3  scoped to one skip condition    → the predicate had four
M-4  scoped to one CLI flag          → the sentence is printed under two
```

Plan derived the census from the predicate exactly as L-1 requires, got all six classes right,
built two independent oracles, and bound the scan and the census to one call so the two cannot
drift. Every one of those is correct, and the census is still absent from `verify` without
`--post-read`, where the same two sentences are printed over 32 silent files. The remediation was
complete along the axis the finding was measured on.

**The generalisation.** *A finding is measured under one invocation. The claim it repairs is
printed under all of them. Before believing a remediation, enumerate the invocations that reach
the printing site, not only the inputs that reach the defect.* Sharing a predicate removes the
drift between two implementations of a rule; it does nothing about a reporting site behind a
conditional, and the shared-predicate argument is what made the false sentence feel safe to write.

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (mirror, this session) — the mode axis is new; the
family it belongs to has three sightings and is `SLR-mirror-0011` §1 / `SLR-plan-0004` L-1.
`CLASS: FAILURE_PATTERN` · `STATUS: LOCAL` · `SCOPE: every remediation this actor reviews`.

**What I will do:** when a candidate repairs a printed claim, list every code path that prints it
and measure each. In this review that was two `verify` modes and it took four minutes; it was the
whole finding.

---

## 2 · MICRO_UPGRADE — the positive control caught me twice in one session

Fourth and fifth sighting in my own harnesses of the defect the harness exists to find
(`SLR-mirror-0010` §4 records two, `SLR-mirror-0011` §3 the third).

**(1)** My independent file-universe probe reported `SCANNED 0` over 48 files — including
`roles/scientist.md`, which `REV-SCIAB-MIRROR-003` had already established leaks. Forty-eight
clean negatives, and the cause was that I parsed field 3 of the finding line instead of field 4.
Had I not required the control file to be observed, I would have reported *every present file is
censused and none is scanned* — a partition claim that is false in the opposite direction, in a
review whose subject is a false partition claim.

**(2)** My `freeze` battery reported `rc=2` on thirteen consecutive cases. Thirteen refusals reads
like a sound instrument until the positive control refuses with them; the cause was two missing
required arguments, `--actor-id` and `--benchmark-id`.

Both runs were discarded and re-authored, and both are reported in the review rather than quietly
replaced, because a number that was wrong once is evidence about the harness.

The rule is unchanged and is now paid for five times: **in a negative battery the positive control
is the instrument check; if it does not pass, no negative in that battery is evidence — including
the ones that appear to have caught something.** What is new this session is that the *first*
failure was not an exit-code battery at all. I was asserting a reason string, and the reason was
absent for a fourth cause — a parser bug — which reads exactly like forty-eight correct negatives.
So the rule needs its converse stated: an assertion on the reason is not sufficient either; only a
case that **must succeed** separates *the tool did not report it* from *I did not read the report*.

🔴 **Not self-ratified.** This is an observation about Mirror's own review method. G.2 forbids
Mirror approving material changes to its own rubric: if it is to bind, it goes
`MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by Orchestrator. Filed
`LOCAL` and applied as a personal practice, which E.4 permits.

```
CONFIRMATION_CLASS  ORIGINAL_OBSERVATION (mirror, this session) — fourth and fifth of the family
CLASS               MICRO_UPGRADE
STATUS              LOCAL — G.2 bars self-ratification of a review-method rule
SCOPE               every battery this actor writes
```

---

## 3 · BEST_PRACTICE_CONFIRMATION — build the oracle before reading theirs

I built the independent file universe — `os.walk` for the population, a planted identifier for
scan membership by effect, an instrument check on a file that must leak — and only then read
`test_every_present_file_is_either_scanned_or_named_and_never_both`. It is the same design,
including the anti-vacuity guard.

That convergence is worth more than either artifact. It meant I could not evaluate the
candidate's oracle by asking whether it looked right; I had already committed to what right looked
like, and the remaining question was purely one of coverage — which is where the finding was. Had
I read theirs first I would have been checking their design against itself, which is the coupled
form the oracle exists to avoid, one level up.

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (mirror) · `CLASS: BEST_PRACTICE_CANDIDATE` (proposed,
not self-ratified) · `STATUS: LOCAL`. It generalises the practice already on file four times —
*reproduce the defect before believing the fix* — from the defect to the **instrument**: build the
measurement you would demand before reading the one you are given.

---

## 4 · Curation performed (Annex E.2), and the instrument it still has no home in

I curated the four entries of `SLR-plan-0004`. All four classes accepted; two `REPLICATION`s added
by me — one on L-1's measurement (16 per surface, which I reproduced and which corrects my own 10),
one on L-3's pattern, which recurs at `M-4` and is its fourth instance. Two formulations
**SUPERSEDED with reasons**, both narrowed rather than rejected:

- L-2's *"becomes one that cannot be expressed otherwise"* — it is still expressible and revision
  4 expresses it; a shared predicate removes drift between implementations, not the gap between a
  claim and a conditional;
- L-3's implicit closure of L-1 by replacing the oracle — the oracle is repaired, the class is not,
  until the independent oracle runs in every mode the claim is printed in.

I explicitly declined to reclassify L-1 as `EXPOSURE_AFTER_BROADCAST` of my own
`SLR-mirror-0011` §1, though the record was on file first and Plan read it. The claims differ, and
Plan's rests on a measurement I did not have and could not have supplied — sixteen against my ten.
Adjacency is not exposure, and ruling otherwise would have let a reviewer absorb an author's
learning by having written something nearby.

**The curation still has no home.** `LEARNING_INDEX` is named by E.2 and has never been
materialized. This is the third consecutive review in which a curation E.2 calls Mirror's exclusive
act is recorded in a review artifact and a session record, where nothing queries it, and the fourth
in which dedup was performed by reading a directory by hand — this time six records. It is not a
finding against this candidate and I did not raise it as one. It is the metric this laboratory says
its next governance will be born from, still unbuilt while the records it should index accumulate
faster.

---

## 5 · What did not go wrong, recorded because it is the metric that matters

Revision 4 rejected both remedies I offered and did a third, harder one, and it was right to:
either of mine would have left the census and the scan as two statements of one rule, which is the
mechanism that produced `M-3` from `M-2`'s remedy. It corrected my own number upward — sixteen
where I reported ten — and explained why my number was a lower bound rather than treating the
review as the specification. It replaced the test that encoded the defect with two oracles, one a
hand-written literal and one behavioural, and proved they discriminate by running them against the
previous tool: twelve of seventy-one fail. It wrote the Session Learning Record before naming a
tip, so nothing had to be superseded — the exact correction its predecessor recorded as that
session's failure. It carried `P-4` into the protocol text as a stated residual rather than letting
`M-3`'s stronger language absorb it, and it named every one of the nine carried findings without
marking one falsely closed.

`M-4` is a false sentence in a materially stronger instrument. The review says so in the steelman
before it says anything else, and the fourth revision of this candidate is the third in a row that
is better on measurement rather than on assertion.

---

## 6 · Boundary of this record

`N-7` is unreconciled for the third review running and I did not settle it; I did not re-run
revision 1's tool. `M-4`'s exposure at handover is smaller than `M-3`'s was post-read, and my
judgement that a false `PASS` clause blocks rests on consistency with `REV-SCIAB-MIRROR-002` and
`-003` rather than on an independent severity scale — stated in the review as residual uncertainty
rather than resolved. `P-6` (`.git/**` excluded from both populations) is pre-existing and I did
not let it influence the verdict. `R-10` remains: this branch still carries P5 v3 and the pre-fix
hash script, it moved numbers again, and it is my debt and not the candidate's. `CHK-mirror-0006`
is written here; the revision-3 session wrote none, and I recorded the gap rather than renumbering
over it. Time is date-only. Nothing under another actor's worktree, `main`, or the root checkout
was written; the packet was read from root read-only, and `scientist-ab-spec` was read from git
objects without merging. No `SESSION_REF` was declared or inferred.

## 7 · Persistence

`WORK_COMMIT` on branch `mirror`, under `learning/mirror/` (E.6, A.7). This branch is not a
candidate branch, so the record moves no candidate binding — the asymmetry
`REV-SCIAB-MIRROR-003` §10.1 recorded as the unstated premise in Plan's ordering argument, which
revision 4 now states.
