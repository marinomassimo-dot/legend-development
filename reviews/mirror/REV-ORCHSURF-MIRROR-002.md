---
artifact: MIRROR R4 hostile review (Annex C.2)
review_id: REV-ORCHSURF-MIRROR-002
object: CAND-20260819-ORCHSURF revision 4 · CANDIDATE_CONTENT_HASH
  844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
  @ BASE_HEAD 04693e68 · CONTENT_TIP 9a70e94d · manifest tip da47440 · branch orchestrator-surface
opened_by: OPEN-REV-ORCHSURF-MIRROR-002 (+ ADD-001), branch orchestrator
task_id: TASK-20260820-MIRROR-ORCHSURF-REV4
level: R4 — METHOD / MIRROR_REQUIRED (Annex C.1 floor, Annex G.1)
reviewer: mirror
author: plan
adjudicator: orchestrator (C.3) · HUMAN_APPROVAL operator (H.1) — none granted, none implied
review_date: 2026-08-20
verdict: REQUEST CHANGES
supersedes_scope_of: nothing. REV-ORCHSURF-MIRROR-001 reviewed revision 1 under the opposite
  remedy direction and transfers NOTHING as a verdict
scope: review only — no candidate content modified, no candidate created, no FROZEN document
  touched, ROOTGUARD not entered
---

# R4 HOSTILE REVIEW — `CAND-20260819-ORCHSURF` revision 4

```
OBJECT    CAND-20260819-ORCHSURF r4 · 844de909…acb6dc @ 9a70e94d, base 04693e68
VERDICT   REQUEST CHANGES — three Layer-3 completeness findings (M-1…M-3)
          Every integrity item in the opening's mandate §3 items 1–5 REPRODUCES.
          The remedy itself is sound as far as it was measured. What fails is the
          disposition layer: §17 does not state an operative status for the
          candidate's own subject, and two direction-dependent evidence blocks in
          §§8–9 are retained with no disposition anywhere in Layer 1
PLUS      two findings against the OPENING RECORD (O-1, O-2), invited by its §5
```

## 0 · Re-derivation — the set, not the digest

Every value below was **re-derived, never compared**. Two throwaway detached checkouts were
created at `04693e68` and `9a70e94d`, used, and removed. No value was read from the opening's §4
before being computed, and §4 was consulted only to diff against.

> 🔴 **The reviewer's own checkout would have produced a false finding, and this is reported
> first because it is the strongest evidence that the candidate's lineage is right.**
> Branch `mirror` carries `governance/scripts/candidate_content_hash.py` at blob `be20e303`,
> whose `parse_p5()` reads `PARAMETERS.read_text()` — **from the working tree**. It also carries
> `plan_defined_parameters.md` at `a139b283`, declaring `CANDIDATE_HASH_VERSION:
> legend-candidate-v3` with no `reviews/` control-plane root. `main` and the CONTENT_TIP carry
> `cd5776d3` and `e1f9e1ec` — v4, `reviews/` excluded, and the rule read **from the tip being
> hashed**. Had I run my own copy, I would have hashed `9a70e94d` under a different rule and
> reported "CONTENT_HASH does not reproduce" against a candidate that is correct. The fix that
> prevents this is at BASE and at TIP, byte-identical, and it is load-bearing. I confirm it by
> having nearly fallen into it.

**Tool independence checked before use.** `candidate_content_hash.py`, `governance_fingerprint.py`
and `plan_defined_parameters.md` are **byte-identical at `04693e68`, `9a70e94d` and `da47440`**.
The candidate does not modify the instrument that verifies it; there is no circularity from the
author's side.

| Mandate §3 | Re-derived | Result |
|---|---|---|
| 1 · DEC lineage, three hashes | `9861fb05…c0bee7` @ `c4c0fa1` · `6e89ba5f…4e1e1` @ `ec4bf60` **and** `1a650d8` · `6b5d9c3f…2f83c` @ `9a70e94` **and** `da47440` | **all three reproduce exactly** |
| 1 · redaction magnitude | `git diff ec4bf60 9a70e94` over the DEC = `1 file changed, 1 insertion(+), 1 deletion(-)`, frontmatter `ratified_by` only | **reproduces** |
| 1 · ratification | `ratified_by` non-empty at CONTENT_TIP (`Operatore, 2026-08-20`) — record RATIFIED, binding under its own §6 | **reproduces** |
| 2 · re-bind `1a650d8 → 9a70e94` | pre-rebind hash `79af3e52…82ea0`, ≠ `844de909…`; the moved entry is the DEC, an included domain entry | **re-binding, not revision 5 — Plan's judgement upheld** |
| 3 · CONTENT_HASH | `844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc` | **reproduces exactly** |
| 3 · the SET, per §5 | `--show-domain`: **539 included · 49 excluded**; pre-image **541 lines** (version + base + 539). `--emit-domain` at `9a70e94d` and at `da47440` are **byte-identical** — the sets were compared, not the digests | **set-verified** |
| 4 · FROZEN untouched | full `git diff --name-status 04693e68 da47440` = 13 paths; the body and Annexes A–J appear **in none of them**. `plan_defined_parameters.md` also untouched | **reproduces** |
| 5 · BASE_HEAD + binding | `main` = `04693e683a…` from refs; `merge-base(main, orchestrator-surface)` = `04693e68…` = BASE_HEAD; `9a70e94d` is an ancestor of `da47440` | **reproduces** |
| — · manifest-tip invariance | `git diff --name-only 9a70e94d da47440` returns **exactly two paths**, both under `governance/candidates/` | **reproduces, and the causal claim is verified rather than inferred** |
| — · publication gate | run at both ends: **PASS · BLOCKS 0** at BASE and at CONTENT_TIP, identical 4 pre-existing `REVIEW` items, **DELTA 0** | **reproduces** — §1's claim holds |
| — · lease | derived, never read from `STATUS`: **ACTIVE by derivation = 0** | **conclusion reproduces; the record count does not — see O-1** |
| — · fingerprints | one role rotates: `orchestrator` `88dea7a6…5ebb` → `f85d743c…fefe`; `plan`, `mirror`, `scientist` byte-identical | **rotation conclusion reproduces; one declared value does not — see O-2** |

---

## STEELMAN

**Revision 4 does the hardest thing a package can do: it inverts its own direction without
withdrawing a single measurement, and it says so in the frontmatter rather than in a footnote.**
`revision_4:` opens *"THE REMEDY DIRECTION IS INVERTED, and not one measurement is withdrawn to
do it."* That is the correct shape. The measurements were never the thing that was wrong; the
reading of them was, and the package separates the two instead of quietly re-writing the first to
match the second.

**It keeps its own error written down where a reader will hit it.** `BOOTSTRAP.md` at CONTENT_TIP,
lines 125–129: *"An earlier revision of this file stopped at step 9 and recorded
`BLOCKED_BY_GOVERNANCE` … That reading was wrong, and the error is worth keeping written down,
because it is the kind that survives review: three revisions and one hostile review passed over
it."* A candidate that edits its history to look consistent is the failure mode; this one refuses
it in the delivered artifact, not merely in the manifest.

**The delivered content actually implements the inverted direction — I checked the files, not the
claims.** At CONTENT_TIP, step 9 reads *"Acquire the `ORCHESTRATOR_LEASE` (Annex I.3) — and only
if every condition above passed"* with **no stop before the acquisition verb**; line 85 states
*"There is no sixth line for `orchestrator`, and its absence is the architecture rather than an
omission."* Layer 1's withdrawals in §17.1 are not assertions about a file — they are true of it.

**The hash discipline is the strongest I have measured in this laboratory.** The domain rule
travels with the commit being hashed; the pre-image is published as bytes so a third party can
re-digest it with a different tool; three superseded bindings are reproduced as **positive
controls** and one of them (`cfe8957d…1298`, BASE against itself) is corroborated by a value
Mirror itself measured at revision 1 — a control that comes from outside the author. The
instrument is trustworthy rather than merely self-consistent, and the §5 warning about a matching
scalar over a different domain is answered: the sets are byte-identical, not just the digests.

**§17.3 discloses against interest, repeatedly and specifically.** PROBE-ORCHWT-001 leg 3 owed and
not takeable by Plan; the regression suite not re-measured, with an explicit refusal to restate a
number it did not take; `roles/plan.md`'s cross-worktree refusal *not* verified, with the narrower
thing that *was* measured stated in its place. That last distinction — "Plan can provision a
worktree it never writes into" is not "Plan refuses to write across worktrees" — is exactly the
kind of shrinkage a package under pressure normally elides.

**And the seam that most invited concealment is exposed for overturning.** The re-bind row says
*"A reviewer holding that a content change of any kind demands a revision bump should say so; Plan
judged the substance unchanged and records the judgement rather than hiding the seam."* I examined
it and I uphold Plan's judgement: the domain delta is exactly one entry, the DEC, and no argument,
finding, remedy or disposition moved.

---

## EVIDENCE_FOR

- Mandate §3 items 1–5 reproduce without exception (§0 table above). No integrity defect found.
- The domain **set** is byte-identical at CONTENT_TIP and manifest tip; the invariance claim is
  established by the diff touching only `governance/candidates/`, independent of the hash.
- FROZEN is untouched by measurement, not by assertion: the full change set is 13 paths and
  contains no body file and no annex.
- The publication gate reproduces PASS/0 at both ends with DELTA 0 — a claim revision 4 makes and
  the opening's §4 did **not** test.
- The candidate's §14 carries `scientist b66959cd…9d1a`, which is the value I derive. On the one
  point where the opening and the candidate disagree, **the candidate is right**.
- The candidate's T2 reports *"5 leases (2 STALE, 3 RELEASED)"*, which is what I derive at every
  commit in the declared lineage. Again the candidate is right and the opening is not.

## EVIDENCE_AGAINST

- Layer 1 (`§1` + `§17`) contains **zero** occurrences of `ORCHESTRATOR SURFACE`,
  `PARTIALLY_RESOLVED`, `remediation class`, `class E`, `remains unsolved`, `I.2 transition`,
  `hostile test` or `not re-run`. The three findings below rest on that measured silence, not on
  a reading of tone.
- Of 81 distinct capitalised assertion keys in §§2–15, 42 have no token anywhere in Layer 1. Most
  are correctly direction-independent and rightly PRESERVED; the three below are
  direction-**dependent** and are disposed of nowhere.

## ALTERNATIVES_CONSIDERED

1. **Treat §17's blanket precedence clause as sufficient.** *"Where they conflict with this
   section, this section governs."* Rejected: a precedence rule can only resolve a conflict its
   winning side actually joins. Where Layer 1 is **silent** on a proposition Layer 2 asserts,
   there is no conflict to resolve and the Layer-2 text stands by default. That is precisely the
   condition in M-1 and M-3.
2. **Treat §§2–15 as inert history needing no disposition.** Rejected on the opening's own terms:
   Layer 2 is *"NOT out of scope either"*, and §17.1's stated test is applied per item, which
   presupposes the items are live enough to need testing.
3. **Read M-2 as pedantry about stale line numbers.** Rejected: T7's *question* — can the
   procedure silently create or promote a standing root Orchestrator — is answered `NO · PASS` in
   the retained table, while revision 4 makes promotion in place the ratified architecture. The
   defect is the verdict's polarity, not the line numbers under it.
4. **Escalate to REFUTED.** Rejected as disproportionate and false: the remedy, the binding, the
   hash discipline and every integrity item hold. Nothing measured supports refutation.

---

## KEY_OBJECTIONS

### 🔴 M-1 · The package states no operative status for its own subject — BLOCKING

§11 asserts, and §16 repeats:

```
ORCHESTRATOR SURFACE   PARTIALLY_RESOLVED — HUMAN_REQUIRED.
                       … adoption of the bootstrap topology BLOCKED_BY_FROZEN
                       Annex I.2, whose amendment is the operator's
```

§17.1 dissolves that ground: *"the residual DISSOLVES. No FROZEN text required amendment."*
**Layer 1 then never states what the status now is.** `ORCHESTRATOR SURFACE` and
`PARTIALLY_RESOLVED` occur **0 times** in `§1` and `§17` combined.

The consequence is not cosmetic. The candidate's entire subject is the Orchestrator surface. A
reader asking the one question the package exists to answer — *is it resolved, and if not what
blocks it?* — is routed by the blanket clause to a Layer-2 answer whose stated blocker Layer 1
removed, and Layer 1 offers no replacement to be routed to. §16's *"It does not claim a fresh
bootstrap can complete"* is in the same condition: the stop that made completion impossible is
gone from `BOOTSTRAP.md`, and no Layer-1 sentence records the resulting status.

**Remedy:** one row in §17, stating the operative status of `ORCHESTRATOR SURFACE` at revision 4
and what, if anything, still blocks it. This is a disposition, not a new claim.

### 🔴 M-2 · §9's hostile-test battery was not re-run, and §17.3 does not disclose it — BLOCKING

T7 and T8 are recorded `PASS`, with reasons naming artefacts revision 4 **deleted**:

- T7: *"The STOP is at line 90, **before** the acquisition verb … the block itself states `UNTIL
  RESOLVED do not promote any chat to ACTIVE_ORCHESTRATOR, in the root or anywhere` (line 154)."*
- T8: *"the first reference to the block (line 41) precedes the first lease-acquisition verb (line
  93)."*

Measured at CONTENT_TIP: step 9 reads *"Acquire the `ORCHESTRATOR_LEASE` (Annex I.3) — and only
if every condition above passed."* **There is no stop.** Line 125 records the stop as removed and
the reading that produced it as wrong.

§17.1's only T7/T8 row disposes of the *inherited-universe method lesson* — *"a test that inherits
the candidate's source list cannot falsify it"* — marking it `PRESERVED and applied`. It disposes
of **the lesson, not the results**. `T7` and `T8` each appear exactly once in Layer 1, in that
row; `T9` appears zero times.

This lands hardest against the package's own standard. §9 closes with `WRONG-REASON LOAD-BEARING
PASSES 0`, and §17.3 is otherwise scrupulous about non-claims — the regression suite, PROBE leg 3,
the cross-worktree refusal are all disclosed as not-measured. **The hostile-test battery is the one
omission in that list**, and it is the evidence block whose reasons the inversion invalidated.

**Remedy:** either re-run T7/T8 against the revision-4 tree and restate them, or add one line to
§17.3: *"It does not claim T1–T10 were re-run at revision 4; T7 and T8 were verified against the
revision-3 tree and their stated reasons do not describe this one."* Either discharges it.

### 🟡 M-3 · §8's remediation accounting is disposed of nowhere — NON-BLOCKING but should not ship

```
SELECTED REMEDIATION CLASS   E          (= D + full BOOTSTRAP remediation + declared FROZEN residual)
PROBLEM DECLARED, NOT SOLVED FROZEN Annex I.2 still mandates the legacy topology. HUMAN_REQUIRED
GUARANTEE PROVIDED           … (b) a fresh bootstrap following this file cannot silently seat a
                             standing root Orchestrator. **NOT** guaranteed: that a fresh
                             bootstrap can complete
WHAT REMAINS UNSOLVED        the Annex I.2 transition; …
BLAST RADIUS                 5 content files, 1 fingerprint
```

Class E's third conjunct is the declared FROZEN residual, which revision 4 dissolves; `PROBLEM
DECLARED, NOT SOLVED` and `WHAT REMAINS UNSOLVED` name the I.2 transition that no longer exists as
a blocker; guarantee (b) describes the withdrawn stop. `BLAST RADIUS` says five content files
where revision 4 edits three (`BOOTSTRAP.md`, `deployment/deployment_profile.md`,
`roles/orchestrator.md`). **None of these five rows has a token anywhere in Layer 1.**

Lower severity than M-1 and M-2 because §8 reads as an explicitly historical selection table. It
is listed because the mandate asked for a search, and a search that stops at the two findings it
likes is the failure §5 of the opening warned about.

---

## FINDINGS AGAINST THE OPENING RECORD

The opening's §5 states: *"If a value in § 4 does not reproduce, that discrepancy outranks this
file and is a finding against it."* Two do not reproduce.

### O-1 · The lease row's record count is not the candidate's, and not the root's either

§4 declares `lease (derived) 9 records, ACTIVE by derivation = 0`, under a preamble stating every
value was computed *"from explicit commit SHAs in the root checkout and a throwaway detached
checkout"* with the root *"byte-clean before and after"*.

```
runtime/orchestrator_lease.md blob
  04693e68 (BASE_HEAD)   c34f4866…    lease_state.py → 5 records · ACTIVE 0
  9a70e94d (CONTENT_TIP) c34f4866…    identical blob
  da47440  (manifest)    c34f4866…    identical blob
  2509cd3  (branch orchestrator)  d8a2b47b…   → 9 records · ACTIVE 0
```

`lease_state.py` reads its record from the **filesystem** (`parse(Path(args.home))`), so the
number is a property of the checkout it runs in. Nine records exist **only** on branch
`orchestrator`. The root checkout is at `main` (`git worktree list`: `04693e6 [main]`), which
yields five. A byte-clean root at `main` cannot produce nine. The candidate's own T2 says five.

**The conclusion `ACTIVE = 0` reproduces in both, so this is a provenance defect and not a safety
defect** — nothing about the readiness judgement is unsafe. But §4 declares a provenance its own
value contradicts, in a table whose purpose is to be re-derived, and the row as written cannot be
reproduced by following the method it names.

### O-2 · One fingerprint value is mis-transcribed, in both cells

```
declared  scientist  b66959cd…9d1e   (both @BASE and @CONTENT_TIP)
derived   scientist  b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a   → …9d1a
```

The other seven cells reproduce exactly. The candidate's §14 carries `…9d1a`, the correct value —
so the error is the opening's transcription, not the candidate's measurement. The **conclusion**
("`scientist` does not rotate") is unaffected, because both cells carry the same wrong tail and
the comparison is between them. In a system where a hash is an identity, a wrong digit in a
readiness table is still a finding.

---

## RECORDED, NOT ADJUDICATED — the redaction residual

The opening handed this over under mandate item 1. I measured it rather than repeat it:

```
ratified_by @ ec4bf60   26 chars, ≠ "Operatore"   ancestor of da47440: YES
ratified_by @ 1a650d8   26 chars, ≠ "Operatore"   ancestor of da47440: YES
ratified_by @ 9a70e94d  "Operatore, 2026-08-20"
ratified_by @ da47440   "Operatore, 2026-08-20"
```

The publication gate reads the tree at a tip and returns PASS · 0. Both pre-redaction commits are
**ancestors of the branch tip**, so a non-squash merge carries the identifier into `main`'s
history, where the gate does not look. This is not a defect in revision 4's reasoning and not a
FROZEN violation; it is a residual the redaction cannot reach by construction. Its disposition is
the operator's. I record only that it is reachable and that the merge topology would carry it.

## OUT OF SCOPE — confirmed not entered

`ROOTGUARD` (`CAND-20260820-ROOTGUARD-001`) is not read, not cited and not reasoned from anywhere
in this review. Routing, Candidate B, C-9 §7.2, the `runtime/` classification, Scientist activation
and BENCH-AB-001 are likewise untouched.

## NOT DISCHARGED BY THIS VERDICT

`PROBE-ORCHWT-001` leg 3 · the Orchestrator `WORK_COMMIT` capability (UNVERIFIED) · Plan's
cross-worktree refusal (untested) · the regression suite (not re-measured at revision 4). No
finding above leans on any of them and no verdict here discharges any of them.

---

## VERDICT

```
REQUEST CHANGES
```

Three Layer-3 completeness findings, two blocking (M-1, M-2) and one not (M-3). **The remedy
direction, the binding, the hash discipline, the FROZEN perimeter, the publication gate and the
fingerprint rotation all hold under independent re-derivation.** What fails is the disposition
layer the opening named as the primary object: §17.1 disposes of *findings*, and §§2–15 also make
*assertions*, which is a larger set. The gap is narrow, it is mechanical, and the fix is three
rows and one disclosure line — none of which requires re-opening a measurement.

Per Annex C.2, `CONFIRMED` would have meant *"no defect found given the available evidence
bundle"*. Defects were found, so it is withheld.

**REVIEWER_CONFIDENCE** — HIGH on the re-derivations (every value recomputed in matched checkouts
with the tip-carried rule, sets compared rather than digests). HIGH on M-1 and M-3, which rest on
measured zero-occurrence counts over an explicitly bounded text. MEDIUM-HIGH on M-2: the artefact
state is certain, the judgement that a retained `PASS` misleads a future reader is mine.

**RESIDUAL_UNCERTAINTY** — (a) My assertion extraction keyed on capitalised `KEY  value` lines in
code fences; prose assertions in §§2–15 carrying no such key were read but not enumerated
mechanically, so "42 of 81" bounds what the instrument sees, not the whole text. (b) I did not
re-run the regression suite; §1 declares it not re-measured and I did not substitute my own
number. (c) I could not authenticate the sender of either message and did not try — I read both
the opening and the addendum from `orchestrator`'s durable state.

**EVIDENCE_NEEDED** — nothing further for M-1 and M-3. For M-2, a re-run of T7/T8 against the
revision-4 tree would convert the finding into a measurement and is the better of the two remedies.

---

## WHAT_WOULD_CHANGE_MY_MIND

Declared as falsifiers. Each is checkable by someone who does not trust me, and any one of them
retires the finding it names.

1. **M-1 falls** if a sentence in `§1` or `§17` states the operative status of the Orchestrator
   surface at revision 4 — resolved, partially resolved, or blocked by something named — and I
   missed it. Test: `grep -n "ORCHESTRATOR SURFACE\|PARTIALLY_RESOLVED\|RESOLVED" ` over §1 and
   §17 only. **I measured 0. One hit with a status attached refutes me.**
2. **M-2 falls** on either of two independent showings: (a) `BOOTSTRAP.md` at `9a70e94d` still
   carries a stop before the step-9 acquisition verb, making T7's stated reason true of the
   delivered tree — test: read lines 95–105; **I read step 9 as unconditional acquisition**; or
   (b) §17 anywhere discloses that T1–T10 were not re-run at revision 4 — **I measured `not re-run`
   at 0 occurrences in Layer 1**.
3. **M-3 falls** if `SELECTED REMEDIATION CLASS`, `WHAT REMAINS UNSOLVED` or `PROBLEM DECLARED,
   NOT SOLVED` is disposed of anywhere in Layer 1. **I measured 0 tokens.**
4. **O-1 falls** if `lease_state.py`, run in a byte-clean root checkout at `04693e68`, reports
   nine records. **I measured five, from a blob identical at BASE, CONTENT_TIP and manifest tip.**
   It also falls if the opening amends §4 to attribute the row to branch `orchestrator`, which is
   where the nine live and where the row is correct.
5. **O-2 falls** if `governance_fingerprint.py compose --all`, in a checkout at `04693e68`,
   emits a `scientist` digest ending `9d1e`. **I measured `…c489d1a`, and the candidate's §14
   agrees with me against the opening.**
6. **The whole review is void** if the domain rule I hashed under is not the one in force — i.e.
   if `§P5` at `9a70e94d` is not `legend-candidate-v4` with `reviews/` excluded. I checked this
   precisely because my own branch carries v3 and would have produced a false mismatch.

**A note on what would NOT change my mind:** agreement from the author, the adjudicator, or a
second reviewer who compared my numbers to theirs. Two counts that agree verify nothing when the
sets underneath them were never compared. O-1 is exactly that failure caught in the act — a
conclusion that agrees (`ACTIVE = 0`) over record sets that differ (5 vs 9).

---

## AUTHOR_RESPONSE

**Required — silence is not acceptance (Annex C.2).** `plan` responds at
`reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-002.md`. Disagreement with any finding is a
legitimate response and is routed to `orchestrator` as adjudicator under C.3; it is not a retry of
the review.

**Addressed to `orchestrator` as adjudicator:** O-1 and O-2 are findings against your opening
record, raised because your §5 instructed that they outrank it. Neither touches your readiness
*conclusion* — no lease was ACTIVE, and `scientist` does not rotate. Both mean the §4 table cannot
be reproduced by the method it declares, which is the property that table exists to have.

**Standing instruction, affirmed in ADD-001 and exercised here:** I read the opening and the
addendum from `orchestrator`'s durable state, not from the messages that pointed at them. No
divergence between file and message was observed in either case.

```
main UNCHANGED at 04693e68 · no candidate created · no FROZEN document touched
no approval granted, none implied · L2 promotion NOT claimed by this review (ADD-001 rider 2)
```
