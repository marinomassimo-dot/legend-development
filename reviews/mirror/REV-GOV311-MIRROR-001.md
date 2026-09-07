---
artifact: MIRROR hostile review record (Annex C.2)
review_id: REV-GOV311-MIRROR-001
task_id: GOV311-MIRROR-REVIEW-001
directive_version: 1
generation: 1
reviewer: mirror
author: plan
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED (Annex G.1); MAJOR governance review
review_date: 2026-08-16
review_date_precision: date only — the runtime exposed no wall-clock time
disposition: REVISION_REQUESTED
---

# MIRROR HOSTILE REVIEW — CAND-20260816-GOV311 revision 4

## 0 · Binding of this review

```
CANDIDATE_ID:            CAND-20260816-GOV311 — revisione 4
CANDIDATE_CONTENT_HASH:  2e7da13ff3bfff4554a28300d01b6e23b62ead3b787c3de78f92a2cd5b9256d7
                         (as assigned and as recorded in the manifest — NOT REPRODUCIBLE, see R-1)
BASE_HEAD:               749a9a9b8f29c855f803a43b979c591532557561   (VERIFIED)
BRANCH / TREE REVIEWED:  evidence-index @ 154aef5b6257cd16e602447e881946091933ea23
MANIFEST:                governance/candidates/CAND-20260816-GOV311.md
REVIEW_DATE:             2026-08-16
REVIEWER:                mirror
DISPOSITION:             REVISION_REQUESTED
```

> 🔴 **This is not a content clearance.** Only **R-1** was performed. **R-2 through R-7 were not
> reviewed** — they are PARKED under the task's own `RETRY_POLICY`, which classifies a
> `CANDIDATE_CONTENT_HASH mismatch` as **non_retryable → PARK + report BLOCKER**. No verdict in
> this document may be read as approval of the candidate's content, and none of it may be
> transferred to a future hash.

---

## 1 · M1 — CANDIDATE_BINDING: **FAILED**

| Element | Expected (assignment + manifest agree) | Verified state | Result |
|---|---|---|---|
| `CANDIDATE_ID` | `CAND-20260816-GOV311` | manifest §1 identical | ✅ |
| `REVISION` | 4 | manifest `REVISION: 4` | ✅ |
| `BASE_HEAD` | `749a9a9b…557561` | manifest identical; `git rev-parse main` identical; ancestor of tip | ✅ |
| `EXPECTED_MANIFEST` path | `governance/candidates/CAND-20260816-GOV311.md` | exists, blob `ecf61f12` | ✅ |
| Superseded hashes | rev.1/2/3 declared | declared in manifest with reasons | ✅ |
| `CANDIDATE_CONTENT_HASH` | `2e7da13f…9256d7` | **does not reproduce from any committed tree** | ❌ |

**There is no disagreement between the assignment and the manifest.** Both state the same hash.
What fails is that the hash does not reproduce from the repository by the manifest's own
published recipe.

### 1.1 · The manifest's own command, run verbatim

The manifest publishes a copy-pasteable reproduction command. Executed unmodified:

```bash
git ls-tree -r --full-tree 3c6c6e15 | grep -v $'\tgovernance/candidates/' \
  | { printf 'legend-candidate-v2\n749a9a9b8f29c855f803a43b979c591532557561\n'; cat; } \
  | shasum -a 256
```

```
computed : e3ca1983f6f09bc613fa1b108efc805f28c0a43782978eba2586cc1e04e79e76
recorded : 2e7da13ff3bfff4554a28300d01b6e23b62ead3b787c3de78f92a2cd5b9256d7
```

The same command at the actual branch head `154aef5` yields the **identical** `e3ca1983…`,
confirming the filter behaves as PID-06 designs it (the manifest's own commit does not perturb
the value).

### 1.2 · The failure is not in the reviewer's method — proof

144 combinations were tested: 9 candidate-related commits × 16 serialization variants (v1/v2
prefixes; base-head before/after the listing; trailing-newline present/absent; full vs filtered
listing; names-only listing; tree-oid instead of listing).

**Exactly one recorded hash reproduced — revision 1:**

```
04cbd3bd, recipe P5 v1 = SHA-256("legend-candidate-v1\n" + <tree-oid> + "\n" + <base-head>)
  → f869a5237a70634ada535343b7484ddc45f36111e9c79664179086a81f8b8909
  = the superseded rev.1 hash recorded in the manifest, exactly.
```

Reproducing a known-good value with the same tooling establishes that the method is sound.
Revisions **2, 3 and 4** reproduce under **no** tested variant. The defect therefore begins
precisely where PID-06 amended the recipe, and has been carried forward through three revisions.

The mechanism that produced `2e7da13f…` is **UNKNOWN**. Only Plan can state it; the reviewer will
not infer it (R-1 forbids choosing a version by inference).

### 1.3 · Corroborating arithmetic

The manifest states *"507 tree entries are hashed"*. The filtered listing contains **508** at
both `3c6c6e15` and `154aef5`; 507 is the count at revision **3** (`d371eed`). The 508th entry is
`ledger/checkpoints/plan/CHK-plan-0005.json`, added at `3c6c6e1`. So §1's prose was carried
forward from revision 3 without recomputation, notwithstanding the revision-4 commit subject
*"hash recomputed"*.

---

## 2 · R-1 · CANDIDATE IDENTITY, BINDING AND PROVENANCE — Annex C.2

```
REVIEW_ID:   REV-GOV311-MIRROR-001 / R-1
OBJECT:      CANDIDATE_CONTENT_HASH 2e7da13f…9256d7 + BASE_HEAD 749a9a9b…557561
             (identity and binding of CAND-20260816-GOV311 rev. 4)
LEVEL:       R4 — METHOD / MIRROR_REQUIRED, MAJOR
REVIEWER:    mirror
AUTHOR:      plan
ADJUDICATOR: operator
```

### STEELMAN (mandatory, before the objections)

The candidate's approach to identity is better than what it replaces, and better than most of
what it could have been. PID-06 identifies a genuine fixed point — a manifest that records the
hash of a tree containing that manifest can never be stable — and resolves it by **rule** rather
than by judgement, replacing revision 1's hand-picked commit with a deterministic path filter.
That is the repository's own stated discipline (*"a recipe recorded only in prose decays
silently; one a command runs cannot"*) applied correctly and unprompted. The version prefix moves
`v1 → v2` specifically so the two definitions cannot collide — an anti-collision measure most
authors would have omitted. `BASE_HEAD` is folded into the hash so an approval cannot be
transplanted onto another base, which is exactly gate 5's concern. The manifest declares its own
supersessions, records **why** each earlier revision died rather than erasing them, and publishes
the reproduction command in full.

That last choice deserves emphasis: **the defect below is detectable only because the author
published the command that convicts the number beside it.** A less disciplined manifest would
have asserted a hash and been impossible to check. The binding failure is a bookkeeping failure
inside an unusually rigorous artifact, not evidence of a careless one.

### EVIDENCE_FOR (the binding as recorded)

- `BASE_HEAD` is exactly right: matches the assignment, matches `git rev-parse main`, is an
  ancestor of the tip; branch is 0 behind / 13 ahead. GATE 0's base condition genuinely holds.
- The filter design provably works: `3c6c6e15` and `154aef5` yield the same value, which is the
  invariance PID-06 claims for it.
- All three superseded hashes are declared, with reasons, and are not silently overwritten.
- The candidate does not claim `SNAPSHOT_ID`, and correctly marks it `n/a until canonical
  execution — GATE 4 belongs to Orchestrator`. No authority is usurped.

### EVIDENCE_AGAINST

1. The recorded `CANDIDATE_CONTENT_HASH` does not reproduce from any committed tree under any of
   16 serialization variants (§1.2). The manifest's own command yields `e3ca1983…`.
2. `plan_defined_parameters.md` § P5 — the governance artifact to which Annex D.2 delegates this
   very definition — **still defines `legend-candidate-v1` over a tree-oid**. The string
   `legend-candidate-v2` occurs nowhere in the candidate except inside the manifest itself
   (verified by scanning every file under `governance/` and `roles/`). PID-06 nonetheless records
   *"Implemented in: § P5 + §1 of this manifest"*. The pointer is false: P5 carries no amendment.
3. The entry count in §1 (507) belongs to revision 3; the reviewed trees carry 508 (§1.3).
4. `TIP: 3c6c6e15` is not the tip of the candidate under review — revision 4 is commit `154aef5`.
   Harmless to the value (both hash identically), but it means the manifest names a tip that a
   reviewer must correct by inference, which R-1 explicitly forbids.
5. **The filter excludes one fixed point and leaves an equivalent one standing.** PID-13 places
   checkpoints at `ledger/checkpoints/<ACTOR_ID>/`, inside the hashed tree. `CHK-plan-0005.json`
   — whose own `_note` reads *"the checkpoint lives inside the hashed tree"* — is the file that
   moved the count from 507 to 508. So **writing a checkpoint that describes the candidate
   changes the candidate's content hash.** The self-reference PID-06 was created to break exists
   a second time, at a path PID-06 does not exclude.

### ALTERNATIVES_CONSIDERED

- *Accept the tree's recomputed identity `e3ca1983…` and review against that.* Rejected: gate 5
  binds approval to a specific hash, and the operator's instruction forbids transferring a
  verdict between hashes. Substituting an identity is Plan's act to propose and the operator's to
  approve, never the reviewer's to perform silently.
- *Treat it as a typo and proceed to R-2…R-7.* Rejected: a typo and a hash computed over content
  that is not the reviewed content are indistinguishable from outside, and the difference is
  exactly what gate 5 exists to detect. Diagnosing which one it is requires Plan.
- *Fail the candidate outright.* Rejected as disproportionate: every finding is local, mechanical
  and repairable, and the underlying design is sound. `FAIL` is reserved for structural defects
  that a revision cannot fix.

### KEY_OBJECTIONS

- **KO-1 (blocking).** The binding object of a MAJOR candidate is unverifiable. A `HUMAN_APPROVAL`
  granted now would cite a hash that no committed tree produces, making gate 5 unenforceable at
  the exact moment it matters.
- **KO-2 (blocking).** Governance and manifest disagree on the definition of the hash. P5 is
  normative-on-approval and sits in `CORE`; the manifest is a per-candidate artifact. Approving
  this candidate would canonicalise a parameter file that contradicts the operative practice —
  the second-source-of-truth condition Plan itself argues against in PID-03 and PID-10, not
  carried to the site where it bites.
- **KO-3 (design).** The checkpoint fixed point (EVIDENCE_AGAINST 5) means the candidate's
  identity mutates whenever Plan records its own progress on that candidate.

### VERDICT: **REFUTED**

The proposition under review — *"`2e7da13f…9256d7` is the content hash binding this candidate"* —
is not supported: it is contradicted by the manifest's own executable recipe. Refuted as a
statement about identity; **no judgement is made on the candidate's content**, which was not
reviewed.

```
REVIEWER_CONFIDENCE:  HIGH on the mismatch (deterministic, reproduced twice, method validated
                      against a known-good value). NONE on the cause, which is UNKNOWN.
RESIDUAL_UNCERTAINTY: Why the recorded value exists at all. It matches no tree state in this
                      repository. Whether the same is true of the rev.2 and rev.3 numbers is
                      established (it is), but the mechanism is not.
EVIDENCE_NEEDED:      From Plan — the exact command and the exact tree state that produced
                      2e7da13f…, or the acknowledgement that it cannot be reproduced.
WHAT_WOULD_CHANGE_MY_MIND:
                      A single executable command, run against a committed object in this
                      repository, that outputs 2e7da13ff3bfff4554a28300d01b6e23b62ead3b787c3de
                      78f92a2cd5b9256d7. One such command reverses this verdict entirely.
AUTHOR_RESPONSE:      PENDING_OPERATOR_ROUTING
```

---

## 3 · REQUIRED_CHANGES (numbered, for routing to Plan by the operator)

Each is material; each produces a new `CANDIDATE_CONTENT_HASH` and mandates a new Mirror review.

| # | Change | Severity | Evidence |
|---|---|---|---|
| **RC-1** | Recompute `CANDIDATE_CONTENT_HASH` with the published command and record the value it actually returns; or state the derivation of `2e7da13f…` if one exists. The value must be verifiable by a third party running one command. | **BLOCKER** | §1.1, §1.2 |
| **RC-2** | Amend `plan_defined_parameters.md` § P5 to the `v2` definition actually in force, so the governance parameter and the operative recipe agree. Today `legend-candidate-v2` exists nowhere outside the manifest, while PID-06 claims P5 implements it. | **BLOCKER** | §2 EVIDENCE_AGAINST 2 |
| **RC-3** | Correct the entry count in §1 (508, not 507) — or, better, stop stating a count that must be re-derived by hand at each revision. | material | §1.3 |
| **RC-4** | Record `TIP` as the candidate's actual tip (`154aef5`), or state explicitly why the parent commit is named. | material | §2 EVIDENCE_AGAINST 4 |
| **RC-5** | Resolve the checkpoint fixed point: either exclude `ledger/checkpoints/` from the filtered listing on the same rationale that excludes `governance/candidates/`, or state deliberately that a checkpoint write is a content change and accept the re-hash it forces. Either is defensible; silence is not. | material (design) | §2 EVIDENCE_AGAINST 5 |

---

## 4 · ESCALATE_TO_OPERATOR

**ESC-1 — RC-2 has a cascade, and its sequencing is the operator's decision, not Plan's.**

`plan_defined_parameters.md` is in `CORE` for every role, so **any** edit to it changes **all
four** role fingerprints. Demonstrated on a scratchpad copy (the repository was not touched):

| Role | Fingerprint now | After a one-line edit to the parameters file |
|---|---|---|
| mirror | `fddbe5a5…7532bd` | `f34eb25d…92c733` |
| orchestrator | `0f7acdee…00ea704` | `38ca77d7…0686a47` |
| plan | `c1d1a9cf…7ccc81da` | `32460f6b…5e721f74` |
| scientist | `1369930d…348adbfdd` | `f0fdde2c…e01e8f23` |

All five existing checkpoints `CHK-plan-0001…0005` record `c1d1a9cf…`. Under Annex A.6's refusal
rule, once P5 is amended **Plan may not resume on any of them** — including `CHK-plan-0005`, the
checkpoint holding this candidate's state. This is not a defect: P2.3 states that broad
invalidation on a `CORE` change is the intended behaviour, and this is a genuine governance
change. But it means the repair of RC-2 requires a fresh directive/generation for Plan rather
than a resume, and that sequencing belongs to the operator (H.1: governance → operator).

This is also the **first live exercise of the invalidation-rate signal** that A.6 and G.3 assign
to Mirror to monitor. Recorded as the first data point.

---

## 5 · NON_BLOCKING_NOTES

**NBN-1 — manifest UNRESOLVED #8 is now partially discharged, positively.** The manifest states:
*"no fingerprint is load-bearing until an actor other than Plan has run the composer. The script
has been exercised only by its author."* Mirror has now run it as a second, independent actor and
reproduced Plan's own recorded value **exactly** (`c1d1a9cf3054bfdfaee8c2db45129f8049e652f2bebbb
56b3f6740a07ccc81da`, identical in all five checkpoints). The composer is deterministic across
actors, and PID-03's parse-the-prose design demonstrably works. This is a real positive result
and should not be lost in a REVISION_REQUESTED disposition.

**NBN-2 — the reviewer's worktree is 189 commits behind `main`** and contains no `governance/`
tree at its HEAD. All verification in this document was therefore run against the candidate's own
objects (`evidence-index@154aef5`), never against the reviewer's working directory — per the
repository's own rule that a branch carries the manifest but not necessarily the evidence.

---

## 6 · GOVERNANCE_DEFECT_CANDIDATES (against the FROZEN text — recorded, not acted on)

**None identified.** Every finding above lies in `PLAN IMPLEMENTATION DECISION — PROPOSED`
material (PID-06, PID-13) or in manifest bookkeeping. Annex D.2 and body §12 gate 5 behaved
exactly as designed: they are what made this defect visible before approval rather than after.
No modification to the frozen text is proposed or implied.

---

## 7 · What was NOT reviewed — PARKED

| Object | State | Reason |
|---|---|---|
| R-2 · fidelity of the FROZEN materialization | **NOT REVIEWED** | parked at M1 |
| R-3 · the 18 PLAN IMPLEMENTATION DECISIONS individually | **NOT REVIEWED** | parked at M1 |
| R-4 · `CLAUDE.md` migration and router | **NOT REVIEWED** | parked at M1 |
| R-5 · prior-art design record and byte identity | **NOT REVIEWED** | parked at M1 |
| R-6 · PENDING_IMPLEMENTATION and UNRESOLVED census | **NOT REVIEWED** | parked at M1 |
| R-7 · gate-3 readiness | **NOT REVIEWED** | parked at M1 |

*(The count of 18 PIDs is a census of the manifest's table, taken during R-1; it is not a review
of them.)*

**Why parked rather than continued.** The task's `RETRY_POLICY` lists `CANDIDATE_CONTENT_HASH
mismatch` as **non_retryable**, with `on_exhaust: PARK + report BLOCKER`. The R-1 instruction
orders a STOP on a binding failure. And every REQUIRED_CHANGE above is material, so each produces
a new hash and compels a new review under gate 5 — content verdicts issued now could not be
carried forward without performing exactly the transfer the instruction prohibits.

---

## 8 · DISPOSITION

```
MIRROR_REVIEW: REVISION_REQUESTED

CANDIDATE_ID:           CAND-20260816-GOV311 — revisione 4
CANDIDATE_CONTENT_HASH: 2e7da13ff3bfff4554a28300d01b6e23b62ead3b787c3de78f92a2cd5b9256d7
BASE_HEAD:              749a9a9b8f29c855f803a43b979c591532557561
REVIEW_DATE:            2026-08-16
REVIEWER:               mirror

REQUIRED_CHANGES:            RC-1, RC-2 (blocking); RC-3, RC-4, RC-5 (material)
ESCALATE_TO_OPERATOR:        ESC-1 (fingerprint cascade / resume sequencing)
NON_BLOCKING_NOTES:          NBN-1, NBN-2
GOVERNANCE_DEFECT_CANDIDATES: none
```

The candidate must not proceed to `HUMAN_APPROVAL` in its current form. The defects are local and
repairable; the design they sit in is sound. Return to Plan via the operator; a corrected
revision 5 requires a new `CANDIDATE_CONTENT_HASH` and a new Mirror review.

**No file of the candidate was modified. No canonical commit was executed. No actor was
directed.**
