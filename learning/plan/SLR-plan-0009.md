---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0009
actor_id: plan
role: Plan
date: 2026-08-19
task: P5DOMAIN-001 · directive v1 · generation 1 — post-XPORT pre-routing blocker resolution;
  P5 fixed-point integrity; Orchestrator work/batch/routing-surface semantics
scope: two false sentences in § P5 corrected; one fixed-point hazard measured and disclosed; the
  classification question left open and routed to its owner. The Orchestrator-surface debt was
  analysed to a conclusion and deliberately NOT bound into this candidate. Routing not opened.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-2 is adjacent to the instrument class Mirror has recorded
  four times and is offered as a distinct observation about *evidence of absence*, not as a
  re-claim of it — Mirror decides which it is.
derived_from: [SLR-plan-0008, SLR-plan-0007, SLR-mirror-0014, SLR-mirror-0015]
---

# SLR-plan-0009 — the interim ended in another file, and the sentence that authorized it never found out

## Context

Three parties independently observed that § P5 says something about `runtime/` that is not true.
The section defers the classification of `runtime/` to C-9 §7.2 and, to justify deferring it,
asserts that the interim is safe:

> *"While `runtime/` remains untracked it is invisible to `git ls-tree` and therefore absent from
> the domain, so no fixed point arises in the interim."*

`runtime/` has not been untracked since `325da04`. That commit gave the `ORCHESTRATOR_LEASE` a
tracked home, for reasons that are correct and argued at length in the deployment profile: Annex
I.3 specifies the lease's `DETECTION` as *"doppio record sulla stessa successione"*, and a file no
other checkout can read cannot produce one. **The change was right. The sentence it falsified was
in a different file, and nothing connected them.**

---

## WORK COMPLETED

```
IDENTITY          rehydrated fail-closed · pwd == git top-level == evidence-index ·
                  roles/plan.md read in full at main · governance 3.1.1
CANONICAL MAIN    f70878d1 verified from git, not from the prompt
XPORT             81f241f2… reproduced independently from a fresh clone with no checkout —
                  positive control for every later probe
PREMISE           CONFIRMED false: one tracked path under runtime/ at main, not git-ignored,
                  entry 495 of the 532 the XPORT binding hashed — and CHK-plan-0018 records
                  496, off by one, which I reproduced before catching my own 497
FIXED POINT       measured with three probes and one non-void negative control (below)
MECHANIZATION     lease_state.py derives lifecycle, not location; batch_commit.py is
                  snapshot/restore only; no script checks a candidate's write surface
ORCH SURFACE      roles/orchestrator.md frontmatter contradicts its own body and the deployment
                  profile; Annex D.1 verified CORRECT and untouched; --cwd divergence reproduced
E5                self-observation demonstrated with two independent instruments
REMEDIATION       two false sentences corrected; rule-parse regression PASS with negative control
NOT DONE          Orchestrator-surface candidate · runtime/ classification · the detector ·
                  Routing · Candidate B · BENCH-AB-001
```

---

## PROBLEMS

### 1 · The safety argument for a deferral had no expiry, and its premise was owned elsewhere

§ P5 does two separable things in one paragraph. It **declines** to classify `runtime/` — correctly,
because declaring a root for a container that holds four classes of artifact is the error C-9's B-1
corrected one level down. And it **argues that declining is free**, on a premise about the git
index.

The first is a judgement and it has aged well. The second is a fact about a file, and the file
moved. Two days later `325da04` made the premise false, and no reader of either commit was looking
at both. The deferral survived its own justification without anything registering that it had.

### 2 · Every prior binding succeeded, and that told me almost nothing

The tempting conclusion from seven clean candidates is that the domain is sound. It is not what the
record supports. What actually held is an **unwritten convention**: lease rows are written on the
`orchestrator` branch, so a candidate cut from `main` carries a frozen lease blob. I found no
statement of that rule anywhere in governance, and no script that enforces it —
`lease_state.py` derives `ACTIVE`/`STALE` and the singleton invariant, and never asks *where* a row
was written; `batch_commit.py` is a snapshot/restore helper for the four scientific current files
and implements no gate at all; `GATE 0` is asserted by hand.

The clean history was evidence that the convention had been followed, not that the domain excluded
the hazard.

### 3 · One consequence is structural, and I nearly wrote the candidate without noticing it

`GATE 0` requires an `ACTIVE` lease, and a lease's terminal row is written after the batch it
authorized. **The row recording a lease can therefore never sit inside the batch that lease
authorized.** `main` carries rows #1–#5; the `orchestrator` branch carries #1–#8. So the tracked
home restored less of Annex I.3's `DETECTION` than the deployment profile claims for it: the rows an
actor must compare to see a double succession are on a branch it has to know to read.

That is not a defect of `325da04`, which improved on an untracked seat in every respect. It is a
property of putting a record that mutates *during* canonical execution inside the domain that
canonical execution binds.

### 4 · I published the wrong index for the very entry this candidate is about

I located `runtime/orchestrator_lease.md` in the emitted domain with `grep -n` and wrote the line
number — 497 — into § P5, into this record and into a commit message. **The emitted domain carries
two header lines before the first entry**, so the entry index is 495. `--emit-domain` exists
precisely so a third party can rebuild and re-digest those bytes, and its first two lines are the
version prefix and `BASE_HEAD`.

`CHK-plan-0018` records 496 for the same entry at the same tip. So the number has now been got
wrong twice, in two directions, by two sessions — and § P5.2 already documents an off-by-one of
this exact shape in the revision-4 count. I caught mine only because I re-derived the index with
`awk` to reconcile against that checkpoint rather than quoting it.

The historical record is **not** repaired here: `XPORT` is canonical and closed, and the value is
control plane. It is reported so the discrepancy is checkable rather than inherited.

---

## SOLUTION

**The false sentences are corrected; the classification is not made.** Excluding
`runtime/orchestrator_lease.md` from the domain is very probably the right eventual answer — the
lease is control plane by § P5's own definition, *"artifacts whose function is to describe or manage
… an actor's runtime state"* — and it is **not mine to make in this candidate**. § P5 routes the
question to C-9 §7.2; C-9 is `ACCEPTED` with `acceptance_is_not_adoption: true`,
`status_transition_owner: operator`, and a `hold` forbidding governance modification until an
operator-owned review closes. Re-deriving the exclusion here under a different name is exactly the
self-authorization the hold exists to prevent — the failure `SLR-plan-0007` L-4 already recorded
about Routing, arriving a second time by a different door.

So the amendment states what is true, measures the hazard, names the mitigation as `PROCEDURAL` and
not `MECHANIZED`, and records the debt with its owner.

**The hazard was measured, not argued.** Three probes on synthetic trees in a throw-away clone,
with the published `XPORT` value as the oracle:

```
T0  unmodified XPORT tip                  →  81f241f2…   reproduces the published hash
T1  lease blob swapped (IN domain)        →  ddc0b08d…   HASH MOVES        tree verified changed
T2  reviews/ blob swapped (EXCLUDED)      →  81f241f2…   HASH HOLDS        tree verified changed
T3  BASE_HEAD advanced, same tree         →  06095c0c…   HASH MOVES
```

`T2` is the control that matters and it is the one most easily faked. A negative control that
leaves the hash unchanged proves nothing unless the tree *did* change — otherwise it reports the
instrument's indifference to an edit that never happened. Both `T1` and `T2` assert the tree SHA
moved before reading the hash, and `T2` substitutes the **same** 18 837-byte blob as `T1`, so the
two differ in domain membership and in nothing else.

The prose edit carries its own regression: § P5's parsed rule — version prefix and control-plane
roots — is identical before and after, checked with a mutation that adds `- runtime/` to prove the
checker can see a rule change at all.

---

## LEARNING

### L-1 — *A deferral is justified by a premise with a lifetime, and nothing in this system watches that premise expire.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · offered for wider scope`

The paragraph deferring `runtime/` bundled a durable judgement with a perishable fact. The
judgement — *do not treat a container as a class* — is still right. The fact — *`runtime/` is
untracked* — was true for two days.

```
DEFERRAL          "not decided here, and here is who decides"        durable
SAFETY ARGUMENT   "and deferring costs nothing, because <fact>"      perishable, owned elsewhere
```

Nothing bound the two. The commit that falsified the fact was in `deployment/`, argued its own case
well, and had no reason to grep for sentences that depended on it.

> **When a deferral is justified by a fact about another file, the deferral has acquired a
> dependency it does not declare. State the premise as a condition that can be checked — *this is
> safe while `git ls-tree main -- runtime/` is empty* — so the claim is falsifiable by the command
> that falsifies it, rather than by three parties noticing it years-equivalent later.**

The reusable half: an interim arrangement should name the observation that ends it, not the state
it assumes. The first is checkable; the second goes stale silently, which is the failure mode
`designed_for_growth.md` names for status sections and this is the same shape one level down.

### L-2 — *A run of successes is evidence about the convention that was followed, not about the rule that was written.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · adjacent to the instrument class in
SLR-mirror-0014 but about a different object — that class is an instrument measuring nothing;
this is a measurement that is real and answers a question nobody asked · Mirror decides`

Seven candidates bound cleanly under a domain containing a mutable runtime record. The inference
*therefore the domain is safe* is unsound, and I had to be explicitly instructed not to make it —
the directive said **"Do not select A merely because previous candidates successfully bound"**, and
without that sentence I judge it more likely than not that I would have.

What held was a convention no document states and no script enforces. The successes measured
compliance with it.

> **Before reading a clean history as evidence about a rule, find the mechanism that produced it.
> If the mechanism is a convention, the history is evidence about the people who followed it, and
> it transfers to the next actor only as far as their knowledge of the convention does.**

The diagnostic is cheap: ask what would have to go wrong for the record to look different, then ask
whether anything would have stopped it. Here the answer was *a lease row on a candidate branch*, and
*nothing*.

### L-3 — *A resolver attribute that names a superset returns a confident non-empty answer and is not thereby working.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · offered for wider scope`

`roles/orchestrator.md` says `worktree: the repository root checkout`. The deployment profile
assigns the `orchestrator` worktree. Asked through the runtime at 2.1.232:

```
--cwd <root>                  24 sessions   10 evidence-index · 9 mirror · 4 root · 1 lettore-c
--cwd <orchestrator worktree>  0 sessions
--cwd <evidence-index>        10 sessions   positive control: the query CAN return non-zero
```

The two readings do not disagree about which session is Orchestrator's. **One of them returns every
other actor's sessions**, because `--cwd` matches a subtree and every worktree lives under the root
at `.claude/worktrees/`. The root is not a discriminator that is hard to evaluate; it is the
universal set wearing the shape of an answer.

> **An identity attribute that over-matches fails in the direction that looks like success. A
> resolver returning 24 rows looks healthier than one returning 0, and here the 24 contains no
> Orchestrator at all while the 0 is the honest answer.**

The narrow scope worth keeping: when a location is used as an identity discriminator, check
containment before checking equality. The general form is older than this laboratory; what is
recorded here is that the repository's own layout — worktrees nested inside the root — is what turns
one normative sentence into a superset query.

---

## MICRO-UPGRADE

1. **The hazard travels in the normative section, not in the manifest.** § P5 now carries the three
   measured values and the sentence that the mitigation is `PROCEDURAL`. `SLR-mirror-0015` L-2 and
   `SLR-plan-0008` L-1 both say a correction on the wrong side of the content seam dies there; this
   is that applied a third time, without being told.
2. **The prose edit ships with a rule-parse regression and a mutation control.** A prose-only change
   to § P5 is exactly the change that could silently move the domain, because
   `candidate_content_hash.py` parses this section. Asserting *"prose only"* is not checking it.
3. 🔴 **The detector was NOT built, and this is a trade, not an oversight.** A check that a
   candidate's tip mutates no tracked `runtime/` path would mechanize the convention in §2 above.
   It is not in this candidate because the candidate's remit is two false sentences, and because a
   detector that enforces a classification is one short step from making it — which the C-9 hold
   forbids. **Carried as a declared debt, owner named: it belongs with the C-9 §7.2 closure, not
   before it.**
4. **The Orchestrator-surface analysis is complete and unbound.** Section 8–13 of the directive were
   executed to a conclusion — Annex D.1 verified correct, the contradiction localised to one
   frontmatter line, the divergence reproduced. It is not in this candidate, and the partition
   rationale is in the manifest rather than here.

---

## IMPACT

Two false sentences leave the authoritative definition of `CANDIDATE_CONTENT_HASH`. The domain rule
is byte-identical, verified by parse and by mutation control, so **no published hash moves and none
was recomputed** — `81f241f2…` still reproduces from a clean clone under the prefix it was computed
with.

What the laboratory gains is smaller than the analysis: it now knows, in the file that governs
binding, that a mutable runtime record sits inside the domain, that only a convention keeps it
still, and that one lease row per batch is structurally unrepresentable in the batch it authorized.
None of that was hidden by anyone; it was distributed across three files and one branch, and no
reader had reason to hold all four at once.

What it does not gain: the classification, the detector, the Orchestrator-surface fix, or any
movement on Routing.

---

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1 ORIGINAL_OBSERVATION · L-2 ORIGINAL_OBSERVATION · L-3 ORIGINAL_OBSERVATION
                 ALL PROPOSED — E.2 curation is Mirror's; Plan does not self-ratify

SCOPE            L-1  offered for wider scope — deferrals with perishable premises occur in any
                      governed system that defers
                 L-2  offered for wider scope — the inference from clean history is general
                 L-3  offered for wider scope in its general form; the nesting observation
                      (worktrees inside the root) is laboratory-internal

EVIDENCE         §4   `--emit-domain | awk 'NR>2 {n++; ...}'` returns 495 of 532 at the XPORT
                      tip and 496 of 533 at this candidate's content tip; `grep -n` returns 497
                      for the same line because two header lines precede the entries
                 L-1  § P5 at f70878d1 against `git ls-tree -r main -- runtime/` (one path) and
                      `git log main -- runtime/orchestrator_lease.md` (325da04, 234c8ba);
                      `git check-ignore` returns rc=1
                 L-2  `git log --all -- runtime/orchestrator_lease.md`: rows #6–#8 on branch
                      `orchestrator`, absent from main; lease blob c34f4866 identical at main and
                      xport, 2795dfe0 at orchestrator; lease_state.py has no location predicate;
                      batch_commit.py exposes only snapshot/restore
                 L-3  `claude agents --json --cwd <path>` at CLI 2.1.232, 2026-08-19T17:35:40Z,
                      three queries above, with the evidence-index query as positive control;
                      session `name` is derived from the cwd leaf, so name and cwd are one
                      attribute, not two

REVIEW           L-2 is the entry most worth attacking, and the attack is specific: I claim an
                 unwritten convention exists and that nothing enforces it. A reviewer who finds
                 the convention written down anywhere in governance, or finds any check that
                 constrains a lease row's write surface, falsifies the learning and weakens the
                 candidate's central claim. I searched roles/, governance/, framework/scripts/
                 and the lease record's own frontmatter; the frontmatter's `writer: orchestrator
                 ONLY — one writer, from the orchestrator worktree` is the closest thing to a
                 statement and it is a declaration in the artifact, not a rule in governance and
                 not a check.
```
