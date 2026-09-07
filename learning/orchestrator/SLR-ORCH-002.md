---
artifact: Session Learning Record (Annex E.6)
record_id: SLR-ORCH-002
learning_id: LEARN-ORCH-002
session_ref: legend-public-cf
session_id: d46e5f47-0295-4071-b807-26b2873cd1d0
date: 2026-08-17
actor_id: orchestrator
role: orchestrator (BOOTSTRAP_CONTROLLER — no lease held)
task: none
classification: FAILURE_PATTERN — durable records that state the false
confirmation_class: ORIGINAL_OBSERVATION
contributors: mirror (instances 4, 5 and the two-branch split) · plan (self-diagnosis on uneven application)
scope: what may be written into durable state, and what must re-anchor it
status: PROPOSED — NON NORMATIVE
slr_outcome: MACRO_UPGRADE_CANDIDATE
governance_defect_candidate: GDC-C2-002
supersedes: none
---

# DURABLE RECORDS THAT STATE THE FALSE — two branches, two different fixes

I filed this as one lesson with three instances. Mirror swept canonical state, found two more, and
showed they are a **different sub-shape with a different remedy**. That correction is the substance
of this record, and it did not come from me.

## The five instances

| # | Instance | Branch |
|---|---|---|
| 1 | `TIMESTAMP_PRECISION: date only — the runtime exposed no wall-clock time`, in nine records including three approval-queue lines. `date -u` returns a full timestamp. | **(a)** |
| 2 | `index mtime and reflog both unmoved since 2026-08-15`, cited as evidence for `ONE_WRITER` — and written into the commit message of `908197b`, the act that overwrote the index. | **(a)** |
| 3 | P5.2: a hash recorded from a computation nobody re-ran; `$(…)` stripped a trailing newline and the published command could not reproduce the published value. | **(a)** |
| 4 | Seven governed artifacts declare `status: PROPOSED — binding once Mirror hostile review passes and the operator approves`. Both conditions are satisfied and recorded. | **(b)** |
| 5 | `ANNEX_INDEX.md` lists as `pending` six of ten downstream artifacts that exist, several of them reviewed, approved and committed. | **(b)** |

Verified here rather than accepted. On instance 4 my exact-string sweep returned **six**, not
seven: `plan_defined_parameters.md` reads *"normative once…"* where the other six read *"binding
once…"*. Mirror's count of seven is right and my grep was narrower than the claim — which is a
small instance of the same disease, since a search string is also an assertion about the world.

## The split, and why it changes the fix

**Branch (a) — never verified, written as fact.** The wall-clock claim was never tested. The index
mtime was cited without asking whether it survives. The hash was recorded from a computation
nobody re-ran. Common mechanism: an assumption dressed as an observation.

> **Fix: test before asserting.** One command each, in all three cases.

### (a) splits again — and the second half is worse

Mirror found the split by going to verify a claim it was about to make, and found the defect in its
own `REV-GOV311-MIRROR-002` §4 — the review that passed the candidate now in canonical history.

```
(a1)  assertion never tested                       → C-6, C-7, P5.2
      fix: test before asserting
(a2)  a test that ran, passed, and does not discriminate
      fix: show the test can fail. A check nobody has seen fail is not evidence when it passes.
```

**(a2) is worse than (a1) for the same reason (b) is worse than both: it leaves a green result
behind.** An untested assertion is bare and anyone may challenge it. A mis-scoped test wears the
badge of having been checked — and the badge is what stops the next reader looking.

Two instances, both live in this session:

- **My `ONE_WRITER` argument.** The reflog gap was a real measurement that could not fail for the
  thing it was offered to prove: ref writes and file writes are different events, and the reflog
  cannot see the latter. It would have returned the same value if the tree had been rewritten all
  night.
- **Mirror's literal-presence check.** *"19 load-bearing literals … all survive outside the
  router"*, tested as *does this string appear in any tracked file other than `CLAUDE.md`*. For
  `publish the derivation, not the derived` the hits were a paper-specific README and a deepdive
  manifest — incidental occurrences in artifacts that predate the migration and are not
  destinations of it. The test would have passed with rule 5e deleted.

### The instance that closes the loop, and it is mine

Verifying Mirror's self-criticism, I grepped the destination for that literal and got **zero
hits**. For about a minute I believed the migration had lost rule 5e, and was preparing to report a
content loss in canonical history.

It had not. The phrase is at `gold_is_in_the_details.md:45`, as **`Publish` the derivation, not the
derived** — capital P, because it opens a sentence. My grep was case-sensitive. So was Mirror's,
which is why its test found the two incidental hits and **missed the true destination entirely**
while returning PASS: the check passed for a reason unrelated to the thing it was checking.

Two actors, the same defect, on the same phrase, minutes apart, while examining that very class of
defect. And it is the third time in this session a **search string functioned as an unexamined
assertion about the world** — the first was my sweep returning six artifacts where seven exist,
because six say *"binding once"* and one says *"normative once"*.

Rule 4 of the parity principle already says `grep` is forbidden as a method of analysis and
permitted only for technical search and post-reading audit. What none of us extracted from it is
the operational corollary: **a grep used as evidence is a test, and an untested test is not
evidence.** A negative result needs a positive control — search for something you know is there,
with the same command — before it may be reported as absence.

### Fourth instance — and here the failing instrument was not the search

Mirror ran a **case-insensitive** grep, which found the phrase, then printed the line through
`cut -c1-400` to check it. The output looked like a line not containing the phrase, and it drafted
the message declaring my correction unfounded. What stopped it was noticing the arithmetic did not
add up: a case-insensitive grep had *matched* a line it was about to describe as not containing the
string.

Reproduced here exactly:

```
line 45 length                              829 characters / 834 bytes
"Publish the derivation" begins at          character 469 / byte 473
grep -ci on the full line                   1
grep -ci on the same line after cut -c1-400 0
```

> **Seventh instance, and it is in this paragraph.** I first wrote *"character 473 of an
> 834-character line"*. Both numbers are byte counts: `awk`'s `length()` and `index()` count bytes
> on this build. Plan measured 829/469 with Python; the blob is byte-identical at both HEADs
> (`757cf15c…`), so one of us had to be measuring something other than what we said.
> **The instrument silently changed the unit and I read the output as characters.**
>
> **Eighth and ninth — inside the sentence that resolved the seventh.** Plan re-measured and found
> two more, both mine to own in part:
>
> - I wrote *"five multi-byte characters"*. There are **three** — `·` (U+00B7, 2 bytes) and `—`
>   (U+2014, 3 bytes) twice — contributing **5 extra bytes**. I read the byte delta as a character
>   count. The two figures coincide only by arithmetic accident.
> - I published `469` beside `473` as though they were the same convention. `469` is 0-based
>   characters (Python `.index()`); `473` is 1-based bytes (`awk`). The 1-based character index is
>   **470**. Plan supplied the 0-based figure without stating its convention, so that half is its.
>
> Corrected above. **Plan's guess at the original discrepancy — "a table-prefix or newline
> accounting difference" — was also wrong**, while its conclusion was right.
>
> **What this chain actually demonstrates**, in Plan's words rather than mine: *"each correction
> has been right about the thing it corrected and has carried a smaller instance of the same
> family… That is not carelessness compounding; it is what the class looks like when it is
> actually being hunted, because each pass measures at finer resolution than the last and the
> instrument gets no more careful on its own."*
>
> 🔴 **And it is the first test the proposed model passes.** Every instance in this chain is a
> **static assertion** — a measurement, true or false about a fixed object — and every one was
> remediated by **re-measuring**, never by anyone remembering better. That is branch (A) exactly,
> and requirement 1 already names its remedy. A model that classified these as transitional state,
> or prescribed re-anchoring for them, would be wrong. It does neither.

**Grep found it and said so; a filter between the evidence and the reader removed it.** So the
corollary needs one more clause, and it is Mirror's:

> A grep used as evidence is a test — **and so is every pipe you read it through.** `cut`, `head`,
> `sed -n`, a column limit: each is an unlogged filter between the evidence and the reader, and
> none announces that it dropped something.

The asymmetry that makes this the nastiest of the four: **a mis-scoped pattern leaves a suspicious
silence; a truncated display returns content**, and content reads as a complete answer. Fix, and it
costs nothing: when a negative matters, print the whole thing, or count rather than look.

### What actually worked, recorded because condemning the instrument would be the wrong lesson

I wrote that none of the three greps was the reason we agree 5e is preserved. Mirror corrected me:
one of them was. Its session check on the destination was
`grep -n -iE '5e|adjudicat|crop|recipe|derivation'` — case-insensitive, pattern-based, and **aimed
at the file the migration map declared as the destination**. It returned line 45. That is how 5e
was correctly established.

| Instrument | Outcome |
|---|---|
| case-sensitive literal, swept across the whole corpus | ❌ passed on incidental hits, missed the destination |
| case-sensitive confirmation of a phrase believed known | ❌ reported absence that was not there |
| correct search read through a truncating display | ❌ near-miss, caught by arithmetic |
| **case-insensitive pattern, aimed at the declared destination** | ✅ **established the fact** |

The lesson is not that grep is untrustworthy. It is that a grep used as evidence needs **a declared
target, a tolerant pattern, and an unfiltered view of its own output** — which is nearer to parity
rule 4's *permitted* use, technical search and post-reading audit, than to grep-as-analysis. The
map said where to look; looking there tolerantly is the thing that held.

*(Rule 5e is preserved. The candidate, `REV-002`'s verdict and commit `908197b` are unaffected.)*

**Branch (b) — true when written, invalidated by the system's own success.** Nothing was assumed
and nothing went unchecked. The seven `status: PROPOSED` lines were accurate the moment they were
authored; the review then passed, the operator approved, and the artifacts were built. They were
made false *by progress*.

> **Fix: make the transition write the status, or stop stating it.** Verifying harder cannot
> help — they were verified, and then the world moved.

## Branch (b) is a rule this repository already wrote, applied at one site and not the second

`designed_for_growth.md` consequence 1:

> *"Never pin a number a human must remember to update. The change must be re-anchored by the tool
> that causes it, as `fulltext_receipts.py record` re-anchors the ledger… updating a constraint
> must cost at least as much as complying with it."*

A `status: PROPOSED` field that only an act of memory can flip **is** a pinned value. So is a
ten-row `pending` table. The repository owns the mechanism — `append_only_prefix`, the growth
anchors, `FREEZE_SCOPE_GATE` — and none of it was carried to the artifacts that describe the
governance's own readiness.

`PATTERN_ALREADY_SOLVED_GATE` applies exactly: *"Before building a guard, look for it — it is
probably already here… The failure mode of a system that grows by accretion is not ignorance, it
is uneven application."* Written in this repository, about this repository, and then reproduced by
three actors in two days.

## 🔴 The refinement that makes branch (b) usable: a true positive that must not be corrected

Plan swept the same ground and the grep returns **nine** files, not seven. The two extra split
into different classes, and the second one changes what the test for (b) actually is.

| Hit | What it is | Verdict |
|---|---|---|
| `design_records/claude_md_migration_map.md` | front-matter `status: PROPOSED`, `normative: no` | **stale — correct it.** Eighth item, non-normative class |
| `design_records/materialization_log.md:238` | *not a status field.* A sentence inside `MAT-003`: *"All are marked `status: PROPOSED`. They become binding when Mirror's hostile review passes and the operator approves"* | **true, and must not be touched** |

Verified here: line 238 sits inside a dated `MAT-003` record in an append-only log. It **was true
on 2026-08-16 when written**. It does not describe the present; it records what was true at
materialization. Correcting it would be the erasure the append-only rule exists to prevent — the
same reason `COR-20260816-GOV311-001` was appended rather than applied to line 2 of the approval
queue, and the same reason five superseded checkpoints were never rewritten. If the log must
reflect the change, it needs a **new record**, not an edit.

**So the branch-(b) test I had implied is wrong.** I wrote it as *"is this statement currently
false"*. That test flags line 238 and would licence destroying dated testimony. The correct test
is one question earlier:

> **Does this artifact claim to describe the present?**
>
> If yes and it is now false → branch (b), re-anchor it or stop stating it.
> If it is dated testimony → the same words are not a defect, and editing them is the defect.

An append-only record is *supposed* to contain statements that were true once and are false now.
That is what it is for. A sweep that cannot tell the two apart converts a lesson about stale state
into a licence to rewrite history — which is the more expensive of the two failures by a wide
margin, and the one this repository has already paid for twice.

Eight to correct, one to leave alone deliberately. The ninth hit is the sweep working correctly.

## The instance that cannot be repaired, and is therefore the one to keep

Instance 2 is in the commit message of `908197b`. Canonical history, immutable. An auditor who
checks it will find the index half contradicted by an attribute my own commit destroyed.

That is the sharpest statement of the lesson available: **I put a volatile filesystem attribute
into the most durable record the system has, and the act of recording it is what falsified it.**
The conclusion it supported still holds, on evidence Mirror supplied and I re-ran — a 46.6 h reflog
gap and zero root file writes in the window. What failed was the citation, permanently.

## Why (b) is the more dangerous branch in a system that accumulates

An (a) defect is wrong from birth and can be caught by anyone who checks. A (b) defect is **correct
when written, and decays silently** — no diff, no event, no failing test marks the moment it stops
being true. Nobody re-reads a `status:` line they authored, because it was right when they wrote
it. Instances 4 and 5 went unnoticed through a hostile review, an operator approval and a canonical
commit, by three actors all reading those files for other reasons.

This is the same asymmetry `epistemic_discipline` names for negatives: *a false positive gets
tested and dies; a false negative is silent, permanent and self-reinforcing.* A stale status line
is a false negative about the system's own state.

## Third branch — (C) OVERSHOOT, self-named by Plan and already solved here

Plan named a pattern of its own after three instances: *"a claim promoted past its evidence…
worth naming as a pattern of mine rather than three separate slips, since three is where a
coincidence stops being one."*

It is neither (A) nor (B). The evidence was gathered and is correct; the **statement** exceeds it.
Nothing was untested and nothing decayed — the sentence simply says more than what was measured.

```
(C) OVERSHOOT   evidence correct, statement stronger than the evidence carries
    fix: ask of a claim what LOCATOR_OVERSHOOT_GATE asks of a proposition —
         does the source say MORE or LESS than the claim?
```

**And the gate already exists**, verified at `learned_gates_registry.md`:

> *"A reading can be careful, honest and complete, and still say more than its source — and no
> structural check sees it: the receipt is valid, the manifest passes, every locator resolves, and
> the proposition still overshoots the sentence beneath it… require two answers per triple: does
> this quote support this proposition, and **does the source say MORE or LESS than the proposition
> claims**. Verdicts: `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`."*

Built for **readings of papers**. Never carried to **claims about the system's own state**, which
is where all six of this session's instances live:

| Claim | What the evidence carried | Whose |
|---|---|---|
| *"GATE 0 fails always"* | fails from the first Orchestrator output onward | plan |
| *"costs nothing new"* | costs nothing not already agreed to | plan |
| *"editing either rotates all four"* | only `plan_defined_parameters.md` does | plan |
| *"demotion runs through Mirror coordination review"* | I.4 names Mirror as **detector**; the writer is unnamed | mine |
| *"none of the three greps was the reason"* | one of them was | mine |
| *"the amendment makes `runtime/` move the hash"* | amendment **plus** tracking does; untracked is invisible to `ls-tree` | mine |

**Fourth site for `PATTERN_ALREADY_SOLVED_GATE`**, and the most pointed of the four: the gate's
whole apparatus — blind triples, the MORE/LESS question, five verdicts — was built to stop a
proposition overshooting a paper, and never turned on the system's propositions about itself.

Two of its own clauses transfer with it and would have to:

- *"Blindness is the active ingredient, not the tooling. Two reviewers with full context passed the
  same work back and forth twice, each finding real defects in the other's; a reviewer who did not
  know the authorship then found eight more in an hour."* That is a description of this session.
  Plan and I corrected each other across nine exchanges. It worked, and it was expensive, and the
  gate already says why.
- *"Deliberately NOT applied to every reading: a gate that fires on everything gets switched off."*
  So extending it to system-state claims needs a trigger, not a blanket — and choosing that
  trigger is the work, not the extension.

## 🔴 The capstone: every remedy but one was already written down, and we found none of them by looking

Plan checked the gate registry and found `(a2)` there already. Verified at
`framework/eval/learned_gates_registry.md:77`, inside `PATTERN_ALREADY_SOLVED_GATE`, as its **third
variant, dated 2026-08-10** — seven days before Mirror and I each reproduced it:

> *"Third variant, 2026-08-10, and it is not about the code at all: **the verification ran where
> the defect could not occur**… The rule: **a green suite is evidence only if the environment it
> ran in is capable of exhibiting the defect.** Before trusting a fix, either reproduce the trigger
> where you are testing, or state plainly that you did not… the durable form is the one the two
> repaired suites now carry: **the test mounts the condition itself**, plus a companion assertion
> that the fixture would have failed without the fix, so the next reader cannot verify in a place
> where failure is impossible."*

It even summarises the family: *"a defence not carried to the second site; a defence with no test
of its own; a test with no environment that can break it."* The third is (a2), stated with its
remedy and its durable form, before any of this session happened.

**The tally, once all four remedies are checked against what already exists:**

| Branch | Remedy | Where it already lives |
|---|---|---|
| (a1) untested assertion | test before asserting; a negative needs a positive control | the same gate's third variant, in substance |
| (a2) non-discriminating test | show the test can fail; mount the condition | `PATTERN_ALREADY_SOLVED_GATE`, variant 3, **2026-08-10** |
| (B) stale transitional state | re-anchored by the tool that causes the change | `designed_for_growth` consequence 1 |
| (B) rejection with expired premise | `REVIVAL_TRIGGER` + the re-audit rule | `epistemic_discipline` §2 — live, 11 entries, never carried to a governance rejection |

Three sites. All four remedies already present. **What is missing is not a mechanism — it is the
classifier that routes a defect to the remedy that already exists.**

### And the recursion is the finding

The entry that contains (a2)'s remedy is `PATTERN_ALREADY_SOLVED_GATE` — the gate whose whole
content is *"search this repository for the same concept before writing it."* Three actors spent a
day rediscovering, from first principles, a rule filed one week earlier inside the gate that tells
you to go and look. Its own prescribed habit is the cheapest one available: *"when a mechanism
feels novel, grep for its vocabulary before writing it. Twice out of three, the word was already
there."*

Nobody grepped. Including me, while writing a record about assertions made without checking.

That gate also names precisely why this half is hard: *"Only part of this is mechanizable, and
pretending otherwise is the same error one level up. What a test can catch: a definition duplicated
across guards. **What no test catches: the same concept implemented twice with different rigour**…
That half is caught by an adversarial reader who does not know who wrote what."* Here it was caught
by three readers who did know, over four exchanges — which worked, and is more expensive than one
grep.

## MICRO-UPGRADE

Applied in-session: C-7's evidence citation replaced with two instruments any actor can reproduce
from any worktree, with the destroyed one retained and marked rather than deleted; C-6 recorded as
observed-and-not-repaired, since rewriting nine durable records — three in an append-only queue —
would be the very act that queue's discipline exists to prevent.

**Nothing in branch (b) was repaired**, deliberately: the seven status fields are governance and
the operator's to ratify, `ANNEX_INDEX` is Plan's under §30, and an actor flipping its own
contract's binding status is the shape the composition rules exclude.

## What a fix would have to look like, if promoted

Not proposed as a design — recorded so the shape is not re-derived:

- a `status:` field that is **computed from the durable record of its own conditions** rather than
  typed, or absent from the artifact and held only where those conditions live;
- an `ANNEX_INDEX` readiness table **derived by a script** from the filesystem, the way
  `growth_anchors.py check` derives cardinality, rather than maintained by hand;
- either way, the criterion from consequence 1: **updating must cost at least as much as
  complying**, or the field will be bumped to look right.

## CLASSIFICATION

```
SLR_OUTCOME:                 MACRO_UPGRADE_CANDIDATE
GOVERNANCE_DEFECT_CANDIDATE: GDC-C2-002
LEARNING_STATE (E.1):        OBSERVED
CONFIRMATION_CLASS (E.2):    CONFIRMATION of PATTERN_ALREADY_SOLVED_GATE variant 3 (2026-08-10)
                             — NOT an original observation
derived_from:                learned_gates_registry.md § PATTERN_ALREADY_SOLVED_GATE, variant 3
STATUS:                      PROPOSED — NON NORMATIVE
```

> 🔴 **This field was `ORIGINAL_OBSERVATION` when first written, and that was wrong.** Branch (a2)
> is variant 3, rediscovered — remedy and durable form included. Under E.2 this record is a
> *confirmation* of an existing learning, and the distinction is not bookkeeping: `EVIDENCE_COUNT`
> and the `BEST_PRACTICE_CANDIDATE` threshold are computed from these classes, so misclassifying a
> rediscovery as a discovery inflates the evidence for a lesson by counting it twice.
>
> Mirror found the identical defect in `SLR-mirror-0002`, against itself, and its diagnosis applies
> here unchanged: the dedup was deferred to a `LEARNING_INDEX` that does not exist, instead of
> grepping a registry that does — **while filing a lesson about not checking.** I then repeated it
> in this file. The corrected classes are what the sweep below actually supports.

Five instances across three actors in two days clears E.2's `BEST_PRACTICE_CANDIDATE` threshold on
count. It is **not** promoted here: `LEARNING_INDEX` does not exist, epistemic curation is Mirror's
under E.2, and Mirror explicitly declined to cluster its own observations into a lesson —
*"contributing observations to a lesson someone else filed is inside my perimeter; deciding what
the lesson becomes is not."* Deciding is mine; promoting is not.

## ATTRIBUTION

Instances 4 and 5, and the (a)/(b) split that is the point of this record, are **Mirror's**. It
raised instance 4 at registration, connected it to the shape only after I filed the lesson, and
delivered the correction against a record it had no part in writing. Plan's contribution is the
same shape from the other side: on a separate defect it named its own error as
*"recognising the pattern and stopping there"* — consequence 5, uneven application, self-diagnosed.

Recording who found what matters here specifically: the lesson is that authors do not re-read their
own true statements. Both corrections came from readers who were not the author.

## EVIDENCE

```bash
date -u                                                    # 2026-08-17T11:31:44Z
stat -f "%Sm" .git/index                                   # 2026-08-16T22:49:20+0200 — overwritten
git reflog --date=iso -3                                   # 46.6 h gap, reproducible
grep -rl "status: PROPOSED" --include="*.md" .             # roles ×4, BOOTSTRAP, deployment, parameters
sed -n '/Downstream artifacts/,$p' governance/ANNEX_INDEX.md   # 10 rows, 6 describing a past state
grep -n "Never pin a number" framework/master/designed_for_growth.md   # consequence 1
```

## LEARNING_ID

```
LEARNING_ID:        LEARN-ORCH-002
ORIGIN_ACTOR:       orchestrator
CONTRIBUTORS:       mirror (REPLICATION ×2 + taxonomy), plan (REPLICATION ×1)
FIRST_OBSERVED:     2026-08-17
EVIDENCE_COUNT:     5
OWNER:              durability — plan (E.2) · epistemic curation — mirror (E.2)
STATUS:             OBSERVED
AFFECTED_WORKFLOW:  anything that writes a status, a readiness table or an observation into
                    durable state
EXPIRY_OR_REVIEW:   at the first MIRROR_RETROSPECTIVE — cadence N remains UNRESOLVED (ESC-3)
```

> **Not indexed.** `LEARNING_INDEX` does not exist. Index fields are declared so that indexing is
> mechanical when it is built, and this record does not claim to be indexed.
> This paragraph is itself branch (b): the day the index exists, this line becomes false.
