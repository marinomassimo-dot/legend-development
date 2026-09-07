---
artifact: HUMAN DECISION RECORD — resolution request
record_id: DEC-20260817-001
prepared_by: plan
prepared_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT, so preparing
  this record moves no candidate's content hash
state: RESOLVED — all four decisions taken by the operator on 2026-08-17
authority: H.1 — governance and strategic choices are the operator's
---

# Decision record — four open choices

**Nothing here is decided.** The instruction asks for a record of the operator's decisions between
stated options, and no choice was supplied with it. Filling one in would be the silent
reinterpretation the same instruction forbids, so each decision below carries its options, the
evidence for each, a clearly separated Plan recommendation, and an empty `CHOSEN` field.

Verified for this record: `REV-P51C9-MIRROR-002` reads `verdict: ACCEPT`, and
`REV-HASHDET-MIRROR-003` reads `verdict: ACCEPT` with `REMAINING BLOCKERS · None.` Both accepted
candidates were confirmed unmodified at their recorded hashes.

---

## DEC-1 · `SLR-plan-0001.md` inclusion in P51C9 rev 2

```
DECISION_ID       DEC-20260817-001-A
CHOSEN            A — KEEP INCLUDED
DECIDED_BY        operator, 2026-08-17
AFFECTED          CAND-20260817-P51C9 rev 2
CONTENT CHANGE    none · HASH UNCHANGED f325bd9d…0651da · no new review cycle
```

**Decision.** `SLR-plan-0001.md` remains inside the candidate.

**Rationale, as given.** Decision 4 is not read as an absolute prohibition on every SLR in a
candidate, but as a prohibition on introducing **uncured learning material belonging to other
actors** without an owner and a curation path. This record is different: it is Plan's artifact
about Plan's own work, included as Plan's own `WORK_COMMIT`, it declares
`curation: PENDING` explicitly, it was inside the candidate that went to review, and Mirror
assessed that candidate and called the inclusion sound without raising it as a blocker.

### Durable interpretive note — binding on future readings of decision 4

> **Decision 4 excludes the uncurated transcription of learning records belonging to other actors;
> it does not exclude the inclusion of one's own learning records, declared and submitted through
> the normal review path.**

The distinction the note draws is between *transcribing someone else's record* — which supplies
durability without curation, the half E.2 assigns elsewhere — and *including one's own*, where the
author is the owner, the class is declared as proposed, and a reviewer sees it in place.

**Option A — decision 4 was specific.** It excluded the two SLR records that existed at the time,
both the Orchestrator's. `SLR-plan-0001.md` is a later Plan artifact, produced as a deliverable of
the F-1/F-3 remediation, and §18 makes candidate inclusion the durability path — *what is not in
durable state has not happened*. **No candidate change required; hash unchanged.**

**Option B — decision 4 stated a principle.** Uncured learning artifacts do not belong in a MAJOR
candidate, whoever wrote them, because E.2 assigns epistemic curation to Mirror and the record's
confirmation class is proposed by its own author. `SLR-plan-0001.md` violates that principle.
**Requires removal, a new content hash, and a new review cycle** — the candidate is currently
`MIRROR_ACCEPTED`, so Option B discards an acceptance.

| | Option A | Option B |
|---|---|---|
| Content change | none | remove one content file |
| Hash | `f325bd9d…` unchanged | new hash required |
| Mirror ACCEPT | preserved | **discarded**, re-review needed |
| Risk carried | an uncurated class inside a MAJOR candidate, disclosed in §5 item 7 | the F-3 lesson leaves the candidate that performs the F-3 repair, and needs another home |

**Plan recommends A**, on the narrow ground that the record is disclosed rather than smuggled: the
manifest states its class is proposed and awaits E.2, so a reviewer is not misled about its
status. Plan notes against itself that A is the option that costs Plan nothing, which is a reason
to weigh it more sceptically rather than less.

### Evidence incorporated 2026-08-17 — `REV-P51C9-MIRROR-002`

Verified in the durable record:

- **`verdict: ACCEPT`**, and *"No blockers remain."*
- The SLR **is** inside the candidate's content domain — the review's own diff lists
  `learning/plan/SLR-plan-0001.md` as the one content file, blob `c8fa6833…` `MATCH`, with
  everything else control plane.
- The review holds the inclusion **sound** on §18 grounds, reads decision 4 as having excluded
  *the Orchestrator's two SLRs* pending curation, and records it as **not a blocker**.
- 🔴 And it declines to settle the question: *"Decision 4 was the operator's, so its scope remains
  the [operator's]."*

**What this changes, and what it does not.** It removes the possibility that DEC-1 is a defect
question — no reviewer finds a defect here. It leaves DEC-1 exactly what it was: an interpretation
of the operator's own earlier decision, which only the operator can give. Mirror's ACCEPT is
therefore evidence *for* option A's soundness and is **not** a resolution of DEC-1; option B
remains fully available and would discard that ACCEPT.

---

## DEC-2 · ORCHWT — should the object exist

```
DECISION_ID       DEC-20260817-001-B
CHOSEN            B — KEEP CANDIDATE WITH DECLARED DIVERGENCE
DECIDED_BY        operator, 2026-08-17
AFFECTED          CAND-20260817-ORCHWT
CONTENT CHANGE    none · HASH UNCHANGED 280dc497…65763d
```

**Decision.** `ORCHWT` stays in the candidate queue and must go to Mirror review.

### The STOP CONDITION is a bifurcation, not a termination

Settled, and this reading is now the record:

> Option A is compatibility with the existing rule; Option B is declared formal divergence.
> **The failure of Option A does not imply withdrawal of the candidate — it activates Option B.**

That resolves the ambiguity Plan flagged when it took Option B and said it might be reading `STOP`
wrongly. It was not.

**Rationale, as given.** The problem `ORCHWT` addresses is structural: the Orchestrator must have
an operational location consistent with its `WORK_COMMIT` obligations and with branch governance.
**Withdrawing the candidate would remove the candidate without removing the problem that generated
it.** The divergence must therefore stay visible, documented and reviewable.

**No execution authorisation follows from this decision.** `ORCHWT` becomes reviewable, not
executable.

The prior instruction's `STOP CONDITION` admits two readings, and this decision settles which.

**Option A — withdraw.** The compatibility path failed: §8 places the Orchestrator's chat in the
root, and §0.2 and §47 steps 9/14 describe that same chat promoted *in place*, *"non servono due
chat root"*. If `STOP` meant stop the candidate, ORCHWT should not proceed, and the underlying
problem — the Orchestrator has no branch on which a `WORK_COMMIT` is possible — needs a different
route.

**Option B — keep.** The declared divergence proceeds to Mirror review as an explicit governance
object requiring later ratification. Option B does not adopt the divergence; it lets it be
reviewed as what it is.

**What is true either way, and is not a reason to choose:** the underlying defect is real and
verified. `Annex D.1` gives `WORK_COMMIT` to an actor's own branch, the root's branch is `main`,
and a commit to `main` is canonical by definition — so the Orchestrator's output cannot become
durable, and the root cannot reach clean, which blocks `GATE 0` for **every** candidate including
the two already accepted. Withdrawing ORCHWT does not dissolve that; it changes who must propose
the remedy and by what route.

**Plan recommends B**, because Option B keeps the divergence visible and reviewable while
deciding nothing, and because withdrawal leaves a verified blocker with no owner. Plan does not
decide, and notes that B is also the option that preserves Plan's own work — again a reason for
the operator to discount the recommendation, not to weight it.

**Evidence incorporated 2026-08-17 (i): `ORCHWT` had never received a Mirror review** when DEC-2
was posed. That is why the existence question came first: reviewing an object whose existence is
undecided would have spent Mirror on a candidate the operator might withdraw.

### Evidence incorporated 2026-08-17 (ii) — `REV-ORCHWT-MIRROR-001`, after DEC-2 chose B

Verified in the durable record:

```
verdict         ACCEPT — no blockers
CHANGE_CLASS    MAJOR CONFIRMED
reviewed hash   280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
scope           "candidate review only — no execution authorised, no gate assessed, no batch,
                 no merge, no adoption"
identity        reproducible under HASHDET r3
```

The review confirms that the §8 divergence is **explicitly declared**; that the textual conflict is
reported without reinterpretation; that it is **limited to the Orchestrator's residence clause**;
that authority, the canonical commit, the lease and the gates are all unchanged; and that the
candidate **does not self-adopt** the divergence.

> **La divergenza è stata giudicata tecnicamente coerente e revisionabile, ma la sua adozione
> resta una decisione separata dell'operatore.**

🔴 **What this ACCEPT is, exactly.** It concerns **the technical correctness of the candidate under
Option B** and nothing else. It records **no** adoption of the divergence, **no** operational
authorisation, **no** `GATE 0` clearance, **no** batch authorisation, and **no** change to the
governance in force. The review's own scope line says as much, and it is quoted above so the
distinction travels with the record rather than depending on anyone remembering it.

---

## DEC-2b · Adoption of the declared §8 divergence — **OPEN**

```
DECISION_ID       DEC-20260817-001-B2
CHOSEN            ______________________
STATUS            OPEN — created by DEC-2's outcome, not answered by it
AFFECTED          §8 of the FROZEN text; ORCHWT's operational effect
```

DEC-2 settled that the object should exist and be reviewed. It did not settle whether the
divergence it declares becomes operative. Three routes, none selected here:

1. **Adopt the declared divergence** — the operational rule stands as declared, with §8 unamended
   and the divergence carried as an explicit, recorded departure.
2. **Amend §8 in a future governance change** — practice and frozen text are reconciled by moving
   the text, which unfreezes v3.1.1 and is the heaviest route.
3. **Keep the declared state without adoption** until a further decision — the divergence stays
   documented and reviewable and does not take effect.

**Not chosen automatically.** A Mirror ACCEPT on technical correctness is not an adoption trigger,
and treating it as one would be exactly the collapse this record keeps taking apart: review,
approval, adoption and execution are four different acts.

---

## DEC-3 · C-9 adoption status

```
DECISION_ID       DEC-20260817-001-C
CHOSEN            DEFERRED WITH TRIGGER
DECIDED_BY        operator, 2026-08-17
acceptance_is_not_adoption: true          ← preserved
```

**Decision.** C-9 remains `ACCEPTED as a document` and `NOT ADOPTED as operative governance`.

### The trigger, verbatim

> **L'adozione di C-9 sarà riesaminata dopo il completamento della sequenza:
> HASHDET → P51C9 → ORCHWT
> e dopo il raggiungimento dello stato ACTIVE_ORCHESTRATOR.**

**Rationale, as given.** Adopting now, while MAJOR candidates are still in transition, would
introduce a new governance while the previous one is still being validated.

### The sequence is a technical prerequisite, not only prudence — measured

The Orchestrator raised this and measured it from the root; Plan measured it from
`evidence-index` and got **the opposite pairing**, which is the finding rather than a
disagreement. With the **canonical, pre-HASHDET** tool:

| Verifier stands in | P51C9 (`b5eaf81e`) | ORCHWT (`ab4856b1`) |
|---|---|---|
| root / `main` — working tree carries v3, 2 roots | `db6cffac…` ✗ mismatch | `280dc497…` ✓ matches |
| `evidence-index` — working tree carries v4, 3 roots | `f325bd9d…` ✓ matches | `b4e7c493…` ✗ mismatch |

**With the canonical tool exactly one of the two candidates verifies, and which one depends on the
verifier's checkout.** Neither measurement is wrong; both are artifacts of the rule being read from
the working tree. Until `HASHDET` is in `main`, any third party checking either binding gets an
answer determined by where they happen to be standing — which is precisely what gate 5 cannot
tolerate.

**Both rows are independently reproduced by two actors.** Plan measured from `evidence-index` and
the orchestrator from the root; each then reproduced the other's row in the other's directory. For
a measurement that sits in a durable governance record and is the stated reason a sequence is a
prerequisite, that is a different quality of evidence than a single actor's pair of numbers, and it
is recorded as such rather than left implicit.

The first report of this — *"P51C9 is not canonically verifiable until HASHDET lands"* — was true
and narrower than the evidence carried: stated alone it implies P51C9 is the defective candidate,
which the second row refutes. **Neither candidate is defective; the verification procedure is.**
Withdrawn and corrected by its author. Recorded because a governance record that keeps only the
corrected claim loses the reason the correction was needed, and this table exists precisely to stop
one half of a measurement standing in for the whole.

That makes `HASHDET → …` a **prerequisite of verifiability**, not an ordering preference. It does
not authorise executing anything; it establishes that the other two cannot be soundly verified
before it.

### The cure, measured against the same two standpoints

The table above is the disease. Running **HASHDET r3's** hasher against the same two candidates
from the same two standpoints:

| Verifier stands in | P51C9 (`b5eaf81e`) | ORCHWT (`ab4856b1`) |
|---|---|---|
| root / `main` — working tree v3, 2 roots | `f325bd9d…` ✓ | `280dc497…` ✓ |
| `evidence-index` — working tree v4, 3 roots | `f325bd9d…` ✓ | `280dc497…` ✓ |

**Both recorded hashes verify, from both standpoints.** So the property HASHDET restores is not
merely that ORCHWT's identity becomes reproducible — it is that **the answer stops depending on
where the verifier stands**, and both candidates then verify. Measured by the orchestrator from the
root and by Plan from `evidence-index`, each extracting the r3 hasher into a gitignored path and
removing it afterwards rather than leaving a copy of a script that is about to be superseded.

Reproduce it: `git show hash-determinism:governance/scripts/candidate_content_hash.py` into a path
whose `parent.parent.parent` is inside the repository, then run with
`--base 908197ba --tip <candidate tip>`.

**Which sharpens what DEC-3's sequence is for.** It is a prerequisite of **gate 5 meaning anything
at all**: gate 5 binds an approval to a content hash, and until HASHDET is in `main` that hash has
no single answer for a third party to check. Not convenience — the condition under which the gate
is a gate.

**Current state, corrected 2026-08-17.** The previous entry described today's state as
`deferred`, which was wrong in a way worth naming: `deferred` is **one of the three choices**, and
using it for the current state pre-answered the decision it was supposed to leave open.

The state is two facts, neither of them a choice:

```
ACCEPTED     as a document — C-9 closed at revision 4 on the operator's closure directive
NOT ADOPTED  as operational governance — no clause of it is in force
acceptance_is_not_adoption: true
```

Every remedy in C-9 §8 is unapplied: the four-field transitional form, the ANNEX_INDEX derivation,
the `held`-row revival treatment and the Agent Card split. The status/C-8 batch remains frozen
behind it.

The three choices — `adopted`, `rejected`, `deferred` — all remain open, and `deferred` among them
means *deliberately not now*, which is not what the repository currently is. Today the clauses are
unadopted because nothing has decided anything.

**If adopted**, the consequences are not small and belong in front of the choice: adoption touches
every governed artifact carrying a status, two of which are in `CORE`, so it rotates all four role
fingerprints and invalidates every checkpoint. It should be sequenced with the frozen status/C-8
batch as one change, per the do-it-once reasoning already accepted.

**Plan takes no position.** This is the one of the four where a recommendation from the author of
the proposal would be worth least.

---

## DEC-4 · Capability rollback authority

```
DECISION_ID       DEC-20260817-001-D
CHOSEN            INTERIM OPERATOR RULING WITH SUNSET
DECIDED_BY        operator, 2026-08-17
C-9 §10           NOT adopted, not even in part
```

**Decision.** C-9 §10 is **not** adopted partially. In its place stands a standalone operator
ruling:

- **Mirror** keeps identification of the evidence events that require review;
- **Orchestrator** holds the authority to apply the capability state transition.

### Sunset clause, verbatim

> **Questa decisione non costituisce adozione di C-9. Il presente ruling decade automaticamente al
> momento dell'adozione di C-9, quando la relativa norma sarà assorbita nel documento governance
> adottato.**

**Rationale, as given.** It avoids the ambiguous state *"C-9 not adopted, but one of its clauses is
already in force"*, and keeps three things apart that are easy to collapse: acceptance of the
document, adoption of the governance, and a temporary operating rule.

**Why the distinction is not merely formal.** The ruling and C-9 §10 assign the same two roles, so
the difference is entirely one of provenance — and provenance is what decides what happens next.
Under the ruling, the rule's authority is the operator's and it **expires by its own terms**; under
partial adoption it would be C-9's, and C-9 would then be partly in force with no record of which
part. The second state cannot be audited.

### The authority exists and cannot yet be exercised

Recorded because it will otherwise read as a change that took effect today. **L2 remains
suspended** by a separate directive that this decision does not lift, and the authority to *apply*
a capability transition is not the authority to *run the smoke that produces one*. No capability is
`VERIFIED`, so none can be demoted. The ruling becomes load-bearing at the first L2 promotion and
not before.

*(Raised by the orchestrator when the decision was relayed; verified here — L2's suspension is
untouched by every artifact in this pass.)*

Answerable from durable state, and answered here rather than deferred:

**Current authority owner: none is named.** `Annex I.4` reads:

```
DETECTION:  fallimenti ripetuti sullo stesso tipo di task → Mirror coordination review
RECOVERY:   retrocessione a UNVERIFIED → nuovo smoke → riabilitazione
```

Mirror is named as the **detector**. The writer of the demotion is named by nobody — not I.4, not
H.1, not G.2. The Orchestrator asserted at one point that demotion runs through Mirror coordination
review and withdrew it on inspection: that clause names detection, not write authority.

**C-9 §10 is a derivation, explicitly not a ratification.** It separates two questions and assigns
each from existing text — the **evidence event** to Mirror under `Annex C.4` (`SYSTEM → Mirror`),
and the **state transition** `VERIFIED → UNVERIFIED` to Orchestrator by symmetry with promotion at
L2. §10 states in terms that this *follows from* C.4 and symmetry and **is not stated anywhere**,
so it remains a proposal for the operator under H.1 and is not adopted by having been derived.

**Required next step if unresolved:** it blocks nothing today — no capability has been verified, so
none can be demoted, because L2 is suspended and all six of Plan's remain `UNVERIFIED`. It becomes
load-bearing the first time L2 promotes anything. Ratifying §10's split, or naming a different
writer, is the operator's act; leaving it open is legitimate provided the record says so, which is
what this entry does.

---

## Summary

| # | Decision | Chosen | Affected | Hash / content change | Next review step |
|---|---|---|---|---|---|
| DEC-1 | SLR inclusion | **A — KEEP INCLUDED** | P51C9 rev 2 keeps its `MIRROR_ACCEPTED` | **none** — hash `f325bd9d…` unchanged | none; P51C9 needs no further review on this account |
| DEC-2 | ORCHWT exists | **B — KEEP, divergence declared** | ORCHWT stays queued | **none** — hash `280dc497…` unchanged | **first Mirror review of ORCHWT** |
| DEC-3 | C-9 adoption | **DEFERRED WITH TRIGGER** | C-9 stays accepted-not-adopted; status/C-8 batch stays frozen | none | re-examine after `HASHDET → P51C9 → ORCHWT` **and** `ACTIVE_ORCHESTRATOR` |
| DEC-4 | Rollback authority | **INTERIM RULING WITH SUNSET** | Mirror identifies evidence · Orchestrator applies the transition | none | expires automatically on C-9 adoption; dormant until the first L2 promotion |

---

## Sequence constraint — recorded as a constraint, not an authorisation

```
HASHDET  →  P51C9  →  ORCHWT
```

Two independent reasons now hold it in place, and neither is a preference:

1. **Verifiability** (DEC-3). Until `HASHDET` is in `main`, canonical verification of the other two
   has no fixed answer — the two-actor table above shows the verdict flipping with the verifier's
   directory.
2. **Base movement** (this review). `ORCHWT` introduces a dependency on the sequence:
   - it **must not** be executed automatically ahead of the sequence's resolution;
   - any future execution requires assessing the effect on `BASE_HEAD`;
   - if `ORCHWT` moves the common base, **`P51C9` may require a rebase and a re-hash under
     HASHDET r3** before its approval can bind under gate 5.

**This is a constraint on ordering, not a licence to proceed in that order.** Nothing here
authorises the first step any more than the last.

---

## Candidate states after this update

| Candidate | Hash | State |
|---|---|---|
| `CAND-20260817-HASHDET` r3 | `c85acdb2…ad05d8` | **READY FOR HUMAN APPROVAL** |
| `CAND-20260817-P51C9` rev 2 | `f325bd9d…0651da` | **READY FOR HUMAN APPROVAL** |
| `CAND-20260817-ORCHWT` | `280dc497…65763d` | **MIRROR ACCEPTED — AWAITING HUMAN DECISION ON ADOPTION OF DIVERGENCE** (DEC-2b) |

`READY FOR HUMAN APPROVAL` means a review is complete and an approval may now be sought. It does
not mean an approval exists, and it does not touch `GATE 0`, which still cannot pass for any of the
three: the root is not clean, no `ORCHESTRATOR_LEASE` exists, and L2 remains suspended.

---

# HUMAN APPROVAL PACKAGE — four decisions, all `CHOSEN` empty

## The three states, and why the record keeps repeating them

```
MIRROR_ACCEPTED   ≠   HUMAN_APPROVED   ≠   EXECUTION_AUTHORIZED
```

All three candidates have reached only the **first**. The technical reviews established exactly
three things and no more: **no blocker requiring modification**, **identity reproducible**, and
**content consistent with the manifest**.

They do **not** constitute approval of the intent, adoption of governance, `GATE 0` clearance,
batch authorisation, or a merge. The separation is written out here because the collapse is easy
and one-directional: nobody ever mistakes an approval for a review, and this sequence has already
had to take the reverse apart three times.

## Technical state, verified

| Candidate | Review | Class | Hash | State |
|---|---|---|---|---|
| `HASHDET` r3 | ACCEPT · `REV-HASHDET-MIRROR-003` | MAJOR | `c85acdb2…ad05d8` | READY FOR HUMAN APPROVAL |
| `P51C9` rev 2 | ACCEPT · `REV-P51C9-MIRROR-002` | MAJOR | `f325bd9d…0651da` | READY FOR HUMAN APPROVAL |
| `ORCHWT` | ACCEPT · `REV-ORCHWT-MIRROR-001` | MAJOR | `280dc497…65763d` | MIRROR ACCEPTED — DEC-2b open |

---

## HA-1 · `HASHDET r3` — **APPROVED**

```
CHOSEN      APPROVED
DECIDED_BY  operator, 2026-08-17
APPROVAL_ID APR-20260817-HA-1 · bound to c85acdb2…ad05d8 + 908197ba…557561
```

**Rationale, as given.** HASHDET r3 is approved as intent because it restores the fundamental
property of gate 5: `CANDIDATE_CONTENT_HASH` must be a reproducible function of
`BASE_HEAD + TIP`, independent of the verifier's standpoint.

**This approval does not:** authorise execution · pass `GATE 0` · authorise a batch · modify
`main` · adopt any additional governance.

## HA-2 · `P51C9 rev 2` — **DEFERRED**

```
CHOSEN      DEFERRED
DECIDED_BY  operator, 2026-08-17
```

**Rationale, as given.** The candidate is technically `ACCEPTED` by Mirror, but its approval binds
to `CANDIDATE_CONTENT_HASH + BASE_HEAD`. Since HASHDET is first in the sequence and its execution
would move `BASE_HEAD`, a simultaneous approval of P51C9 would lose validity at the first movement
of the base.

Recorded: **technical review valid · no blocker · deferred for re-baseline, re-hash and a new
`HUMAN_APPROVAL` after HASHDET.**

This is the *one approval live at a time* consequence being acted on rather than absorbed — the
deferral is not a doubt about the candidate.

## HA-3 · `DEC-2b` — adoption of the §8 divergence · **B — NOT NOW**

```
CHOSEN      B — NOT NOW
DECIDED_BY  operator, 2026-08-17
```

**Rationale, as given.** The divergence remains documented and not adopted. The decision **does
not** amend §8, does not modify the governance in force, does not constitute partial adoption of
C-9, and preserves the possibility of future adoption or amendment.

Routes A and C remain available; choosing B closes nothing except the question of what happens
today.

| | Route | Consequence |
|---|---|---|
| **A** | **Adopt** the declared divergence | the Orchestrator residence clause becomes an explicit operating rule; authority, canonical commit, lease and gates stay unchanged; **requires tracking as a governance decision** |
| **B** | **Do not adopt now** | candidate stays technically accepted, divergence stays documented, governance in force unchanged |
| **C** | **Amend §8** in a future governance change | a new governance modification and a new review cycle; the heaviest route, and the only one that removes the divergence rather than declaring it |

## HA-4 · `ORCHWT` — **DEFERRED** · separate from HA-3

```
CHOSEN      DEFERRED
DECIDED_BY  operator, 2026-08-17
```

**Rationale, as given.** The candidate is technically `ACCEPTED` by Mirror, but the same binding
rule requires a fresh assessment after `BASE_HEAD` changes.

Recorded: **technical review valid · no blocker · no automatic adoption of the divergence · a new
approval after re-baseline.**

🔴 Approving the candidate **does not adopt the divergence** — that is HA-3, and the two are
deliberately separable. Approval also authorises **none** of: creating the worktree, cleaning the
root, or running a batch.

The two can be answered independently in any combination. Approving HA-4 while choosing B on HA-3
is coherent: it says *this candidate is well-formed and I accept its intent*, while leaving the
divergence declared and inoperative.

---

## 🔴 How this package can be used — only one approval can be live at a time

This is arithmetic, not a risk assessment, and it should shape the choice rather than be discovered
after it.

**All three candidates declare the same base, and it is where `main` is now.** Verified, each read
from its own branch:

```
HASHDET   BASE_HEAD 908197ba62a064546f17c9c277ff497ffc753656
P51C9     BASE_HEAD 908197ba62a064546f17c9c277ff497ffc753656
ORCHWT    BASE_HEAD 908197ba62a064546f17c9c277ff497ffc753656
main                908197ba62a064546f17c9c277ff497ffc753656
```

`GATE 5`, verbatim: *"ogni approvazione si lega a `CANDIDATE_CONTENT_HASH + BASE_HEAD`; qualsiasi
modifica materiale le invalida."*

**So the moment the first canonical batch executes, `main` moves past `908197ba` and the other two
hold a stale `BASE_HEAD`.** Their content hash must be recomputed against the new base, and their
approvals — bound to hash **and** base — no longer apply. Approving all four today would leave two
approvals void by construction the instant the first executes.

**The shape that follows.** In a serial sequence where each execution moves the base, only one
approval can be live at a time. `HASHDET` is the one whose approval cannot be invalidated by a
predecessor, because it has none; `P51C9` and `ORCHWT` would each be re-based, re-hashed and
re-approved in turn.

**And it is a second, independent reason `HASHDET` goes first.** Under HASHDET r3 the re-hash is
deterministic and standpoint-independent, so re-basing the other two is a mechanical recomputation
rather than a fresh argument about which value is correct — which is exactly what it would be
today, given the two-row table above.

**The choice this leaves the operator**, and it is a real one: approve **one at a time**, or approve
all four now accepting that two approvals will need re-issuing after the first execution. Neither
is wrong. It is recorded here so the decision is made *with* the consequence rather than into it.

*(Raised by the orchestrator; the three BASE_HEADs, `main` and the gate-5 text verified here
independently.)*

## 🔴 What the approval moves, and the circularity it lands in

```
GATE 3 for HASHDET   SATISFIED — Mirror ACCEPT + HUMAN_APPROVAL
GATE 0               BASE_HEAD ✓ 908197ba · root clean ✗ nine untracked ·
                     lease ✗ absent, exemption spent · ONE_WRITER ~ cf79f1 CLOSED_UNIDENTIFIED
```

**HASHDET is approved and not executable.** Nothing about L2, the lease or the root changed today.

`GATE 0` needs a clean root. The nine untracked files belong to the Orchestrator, and the route
that relocates them is `ORCHWT` — now deferred behind `HASHDET`, which is itself waiting on the
clean root. **Circular, unless the files are disposed of by a route that needs no candidate.**

It is not a hard deadlock. Routes exist that require nothing approved — but one of them is a trap,
and it is recorded here because this is where the approval will be read:

| Route | Moves `main`? | Status |
|---|---|---|
| create the ORCHWT worktree, then relocate | no | blocked — ORCHWT deferred |
| operator moves or removes them | no | ✅ **TAKEN — `EVAC-20260817-001`, 2026-08-17** |
| commit them canonically | **YES** | 🔴 avoided — would have invalidated HASHDET's approval |
| delete them | no | not taken; would have lost the work |

### Resolved 2026-08-17 — the root is clean, and `main` did not move

The operator authorised evacuating the nine files out of the repository. Verified independently by
Plan, and the negative verified too, because *"`git status` reports clean"* and *"the root is
clean"* are different claims and two routes exploit the difference:

```
root, --untracked-files=all      0 entries
main                             908197ba62a064546f17c9c277ff497ffc753656 — unmoved
.git/info/exclude                0 non-comment lines — not used to conceal
.gitignore                       identical to main — unmodified
git stash list                   1 entry, and it is Plan's pre-existing base-alignment stash
runtime/ and learning/           absent from the root filesystem
HASHDET · P51C9 · ORCHWT         c85acdb2… · f325bd9d… · 280dc497… all unchanged
```

**HASHDET's approval survives**, which was the point of choosing this route: it binds to
`c85acdb2… + 908197ba…`, and a canonical commit of those files would have moved the base and voided
it hours after it was granted.

**A clean root is a preparatory condition, not an operational authorisation.** No `GATE 0`
assessment follows automatically, no execution, no batch.

**Return plan**, recorded in the evacuation manifest: triggered by ORCHWT's execution, returned as
a `WORK_COMMIT` into the Orchestrator's new worktree — never canonical — with SHA-256 re-checked on
arrival, and the Agent Card registry and runtime inventory first, being the only durable record of
who exists.

**The cost, accepted under a stated condition.** Evacuating those two removes the roster while the
laboratory is stopped: lease absent, L2 suspended, zero task contracts, no batch pending, so no
actor is rehydrating and no assignment depends on a capability status. The manifest states the
condition explicitly so a future evacuation is argued rather than copied — **the condition is *the
laboratory is stopped*, not *evacuation is a normal tool*.**

Unchanged by any of this: the two Orchestrator SLRs still carry no Mirror-verified confirmation
class and must not enter canonical state as learning content until E.2 curation supplies one.

### GATE 0 now

```
BASE_HEAD    ✓ 908197ba
root clean   ✓ was the blocker, now cleared
lease        ✗ ABSENT — exemption spent
ONE_WRITER   ~ cf79f1 CLOSED_UNIDENTIFIED
```

**The remaining blocker is the lease, and the lease is behind L2, which is suspended by operator
directive.** One blocker moved; the sequence did not.

**The third is the trap.** HA-1's approval binds to `c85acdb2…` **plus** `BASE_HEAD 908197ba…`.
Committing the nine files to `main` moves the base and destroys the approval granted in this same
record — by the identical rule that caused HA-2 and HA-4 to be deferred. **Anything that cleans the
root must do so without moving `main`.**

Neither Plan nor the Orchestrator proposes a route. The files are the Orchestrator's, their
disposal has governance consequences that are the operator's, and one option would void an
approval issued minutes earlier.

*(Raised by the orchestrator; the binding rule and the base are verified above.)*

## Invariants — recorded as unchanged

```
main                       908197ba62a064546f17c9c277ff497ffc753656
CANONICAL_BATCH_COMMIT     none
merge                      none
execution                  none
GATE 0                     not assessed, not passed
ORCHESTRATOR_LEASE         absent
L2                         suspended
root                       not clean — nine untracked files
```

**Dependency sequence:** `HASHDET → P51C9 → ORCHWT` — **a sequence of validation and hash
dependency, not an automatic authorisation of execution.** Recorded in those terms at the
operator's instruction: HA-1's approval covers intent only, and the two deferrals exist precisely
because the sequence moves the base rather than because it licenses movement.

Recorded motivation: before `HASHDET`, verification of a content hash depended on the verifier's
standpoint; after it, both candidates reproduce from both standpoints — measured, two actors, two
directories. **This is a condition of gate 5 having meaning, not an execution authorisation.**

### Update log

| Date | Change |
|---|---|
| 2026-08-17 | Record created; DEC-4 answered from durable state |
| 2026-08-17 | `REV-ORCHWT-MIRROR-001` ACCEPT, no blockers, MAJOR confirmed, identity reproducible under HASHDET r3. Recorded as technical correctness under Option B only. **DEC-2b opened** — adoption of the divergence, three routes, none chosen. Sequence constraint recorded with its second, independent reason. Candidate states updated. |
| 2026-08-17 | DEC-3 evidence became two-actor; the withdrawn narrower claim kept beside its correction |
| 2026-08-17 | All four operator choices recorded: DEC-1 A · DEC-2 B · DEC-3 deferred-with-trigger · DEC-4 interim ruling with sunset |
| 2026-08-17 | Evidence incorporated: `REV-P51C9-MIRROR-002` ACCEPT with no blockers and decision-4 scope left to the operator; `ORCHWT` confirmed never reviewed; **DEC-3 corrected** — the prior entry called the current state `deferred`, which pre-answered the decision by using one of its own options as a description. No `CHOSEN` field filled. |

**No execution authorisation. No batch authorisation.** Both accepted candidates remain
unexecutable regardless of these decisions: `GATE 0` cannot pass — the root is not clean, no
`ORCHESTRATOR_LEASE` exists, the one-commit exemption is spent, and L2 is suspended.

> **COR-20260817-GATE0-001** — the clause *"the root is not clean"* above was true when written and
> is false from `EVAC-20260817-001` onward. Left standing rather than edited, per the append-only
> discipline: superseded by the assessment below. The paragraph's conclusion is unaffected — `GATE
> 0` still cannot pass, now for the lease alone.

---

# L2 → LEASE → GATE 0 · readiness assessment, 2026-08-17

Prepared by Plan on operator instruction. **Nothing here is executed**: no lease created, no
capability promoted, no candidate or `main` touched. This is the next decision package for the sole
residual block.

## GATE 0 as it now stands

| Condition | Verdict | Evidence |
|---|---|---|
| `BASE_HEAD` | **PASS** | `908197ba…`, unmoved |
| root clean | **PASS** | 0 entries with `--untracked-files=all`; concealment excluded as a negative |
| `GOVERNANCE_VERSION` | **PASS** | 3.1.1 FROZEN, materialised and fingerprinted |
| lease `ACTIVE` singleton | 🔴 **FAIL — absent** | never acquired; the one-commit exemption is spent |
| `ONE_WRITER` | recorded unchanged | `cf79f1` `CLOSED_UNIDENTIFIED`, residual accepted |

`HASHDET`: `HUMAN_APPROVED` + `MIRROR_ACCEPTED`, `c85acdb2…` bound to `908197ba…`, **no execution
authorisation granted.** `MIRROR_ACCEPTED ≠ HUMAN_APPROVED ≠ EXECUTION_AUTHORIZED`, unchanged.

## The five questions

The answers were relayed by the Orchestrator and are recorded **only after Plan re-read the frozen
text**. A peer's derivation is not evidence. Three claims confirmed at source, one not — and the
failure was in my own check.

**1 · What reactivates L2?** Only the operator lifting their own suspension. No governance
condition blocks it.

**2 · Which capabilities must flip to `VERIFIED`?** For *this* batch, three, all the
Orchestrator's: batch dry-run, snapshot restore, lease acquisition/renewal. Plan's six, Mirror's
four and Scientist's six are not load-bearing, and the evidence is behavioural: neither Plan
preparing three candidates nor Mirror reviewing them was blocked by their being `UNVERIFIED`.

🔴 **This is a deviation and must be ratified, not assumed.** Verified verbatim at
`annex_i_bootstrap_deployment.md:38` — *"9. condizioni PASS → acquisizione ORCHESTRATOR_LEASE
(I.3)"*. The conditions are steps 3–8 **entire**. A three-capability L2 is a narrower reading than
the text licenses. Available, but not free.

**3 · Who promotes a capability?** **The frozen text names no owner.** I.4 gives the Orchestrator
*assignment on* `VERIFIED` capabilities, not the transition itself. What governs today is `DEC-4`'s
interim operator ruling — Orchestrator applies the transition — with automatic sunset at C-9
adoption. **Known property, recorded now rather than discovered at first use:** under it the
Orchestrator promotes its own three capabilities. That is self-attestation, the shape E.2 and G.2
route elsewhere precisely to avoid.

**4 · Does L2 reactivation need an explicit human decision?** Two answers that must not be merged.
**By governance: no** — §4's `HUMAN_REQUIRED` taxonomy has no bootstrap-qualification or
capability-smoke row. **By the present state: yes** — L2 is suspended by a standing operator
directive, twice reaffirmed, and only its author can lift it. The requirement is a fact about now,
not a property of the text.
*Plan's own check of §4 was defective and is not offered as confirmation: the range `/^## 4/,/^## 5/`
also matches §47, so the count it returned describes the wrong section. The claim's shape is
recorded; its arithmetic is `UNVERIFIED` by me.*

> **COR-20260817-GATE0-002 — §4 resolved, and the answer changed twice**
>
> Re-run by Plan, bounded by the enumerated heading list rather than a regex range. Heading
> `## 4 · TASSONOMIA HUMAN_REQUIRED`, next heading `## 5 · GERARCHIA DI PRECEDENZA`:
>
> ```
> pipe lines in §4      13
> body rows             12   ← one of the 13 is the header
> ```
>
> **The relayed "thirteen" and the corrected "twelve" are both true of different objects** — pipe
> lines versus body rows. That is the same failure family as my own regex range: an instrument
> returning something accurate about a span other than the one asked about. Two independent
> instruments failed that way in one exchange, which is why the count is recorded here with its
> bound stated rather than as a bare number.
>
> **The substantive claim survives, with one qualifier that "none" did not carry.** No row is
> capability qualification or bootstrap smoke, so L2 is not intrinsically `HUMAN_REQUIRED`. But one
> row is adjacent and must be quoted rather than summarised away:
>
> `| Chat/window chiusa | gli altri continuano | sì, per rebootstrap se necessario |`
>
> Its trigger is a closed chat, not a capability check — so it does not make L2 qualification
> human-required. Its *consequence*, however, names rebootstrap, and a rebootstrap contains the
> qualification levels. The row does not reach L2; it borders it. Recorded at that width and no
> wider.
>
> Answer 4 therefore stands as written — **by governance no, by the present state yes** — and its
> arithmetic is now `VERIFIED BY PLAN` at 12 body rows.

**5 · Minimum path to an `ACTIVE` lease without touching candidates or `main`**

The obstacle is real: writing the lease anywhere tracked dirties the root just cleaned; committing
it moves `main` and voids `HASHDET`'s approval.

The proposal is `deployment/local_instance.md`, derived from I.5's class assignment. **Plan verified
both load-bearing facts:** I.5 assigns `REPO_ROOT · WORKTREE_ROOT · INTERACTION_PROFILE ·
RUNTIME_INSTANCE_ID · SESSION_REFS correnti` to the LOCAL RUNTIME INSTANCE and states *"Nessun path
assoluto nella governance"*; and `git check-ignore -v` confirms `.gitignore:49 →
deployment/local_instance.md`. The path satisfies all three constraints and discharges G3, never
created.

🔴 **Plan's finding, which the derivation does not survive intact.** I.3's lease carries eight
fields — `ACTOR_ID / SESSION_REF / GOVERNANCE_VERSION / ROOT_HEAD / ACTIVATED_AT / LAST_RENEWED /
EXPIRES_AT / STATUS`. Only `SESSION_REF` appears in I.5's list. **`GOVERNANCE_VERSION` and
`ROOT_HEAD` are repository facts, and `ACTOR_ID` is a lab-wide identity** — none is machine-local.
The class assignment is *partial*, so I.5 does not carry the placement on its own.

And the two criteria differ: **I.5's split exists for portability; a lease exists for exclusion.**
Belonging to the local runtime instance for the first reason does not make a location adequate for
the second. I.3's stated `FAILURE` is two sessions reacquiring a `STALE` lease with **no CAS**, and
its `DETECTION` is *"doppio record sulla stessa successione"* — which a file no other checkout can
read cannot deliver. Per-machine visibility addresses the race; cross-actor verification it does
not. This is `C-5b` in a third place.

**Plan's recommendation: the placement is the best available and should be ratified before use, as
an explicit deviation carrying its own detection gap** — not adopted silently because it is the
only door that opens.

## Two findings on the frozen learning record — the cost is wider than the manifest states

The Orchestrator reported that `SLR-ORCH-002` is frozen: it sits in the evacuation directory with
its SHA-256 pinned in `EVAC-20260817-001`, so editing it breaks the digest that makes the return
verifiable. Plan checked the analogous question for its own records, which the manifest did not
cover, and the answer is worse in one case and better in the other.

**`SLR-plan-0001` is safe** — tracked in `evidence-index`, present in the working tree, unaffected.

🔴 **`SLR-plan-0002` is frozen by a stronger mechanism than the manifest's digest.** Verified:

```
in the tree at b9af54eb                    learning/plan/SLR-plan-0002.md      present
learning/ in the excluded control-plane list of that hash    0 mentions → CONTENT
learning/ files inside the hashed tree                       1
present at any branch tip                                    none
hash-determinism now points to                               6422e223 — not b9af54eb
```

`learning/` is content domain, so **`SLR-plan-0002` is part of `HASHDET`'s hashed content**, and
that content hash is `c85acdb2…`, which is `HUMAN_APPROVED` and bound to `908197ba…`. **Revising
that learning record changes the hash and voids the approval.** The Orchestrator's freeze is a
manifest digest; this one is a human approval. They are not the same strength, and only the second
can invalidate a decision the operator already made.

**Consequence for Mirror.** E.2 curation of `SLR-plan-0002` cannot amend the file before `HASHDET`
executes. Curation must either wait, or be recorded *about* the file from the control plane without
touching it. Recorded now rather than discovered when Mirror opens the curation.

**Second-order note.** No branch tip carries `SLR-plan-0002`; it is reachable only through the
candidate commit, and `hash-determinism` has moved to `6422e223`. The object is intact and the
approval binds to the commit, not the branch — but this is the F-3 lesson in its mirror image.
There, a full oid proved identity and not reachability; here the oid still resolves while **the
branch name no longer names the approved object.** Anyone verifying `HASHDET` by branch rather than
by commit would measure the wrong tree — the same measured-correctly-labelled-wrong signature as
§4's row count, at object scale.

> **COR-20260817-GATE0-003 — the clause above is overstated, and Plan measured its own error**
>
> Challenged by the Orchestrator, re-measured by Plan rather than accepted on report:
>
> ```
> --tip b9af54eb           c85acdb2…
> --tip hash-determinism   c85acdb2…      identical
> whole diff between them  governance/candidates/CAND-20260817-HASHDET.md, 1 file
> that root, declared AT b9af54eb   governance/candidates/ — present
> ```
>
> **Verifying `HASHDET` by branch does not currently measure the wrong tree.** The only file that
> moved is the candidate's own manifest, under a declared `CONTROL_PLANE_ROOT`, therefore outside
> the domain by construction. P5.1's fixed-point rule — a manifest describing a candidate cannot
> change the identity of what it describes — is exactly what absorbed the hazard.
>
> **The generalisation survives; the instance does not.** A branch name is a moving reference and
> an approval binds to a commit, so branch-name verification is unsafe *in general*. Here it is
> safe.
>
> One sharpening on why, because the Orchestrator's phrasing — *"the accident is a rule doing its
> job rather than luck"* — merges two things. The rule guarantees the **implication**: if the diff
> is confined to control-plane roots, the hash is unchanged. What is contingent is the
> **antecedent**: that only a control-plane file happened to move. The rule did its job; whether it
> was ever asked to is a fact about what has been committed to that branch, not about the rule.
> Had one content file moved, the two standpoints would diverge and the original warning would have
> been exact.
>
> So the fourth row of the signature table stands, and it is mine: measured correctly — the branch
> did move, the approved tip is only an ancestor, both true — and **labelled "wrong tree" when the
> trees are equivalent in the only domain that decides identity.** The label was wrong, not the
> measurement. Which is the signature itself, committed by the party who had just named it.
>
> Durable answer unchanged, and it is what the register already does: **verify by full oid.**

## A gate this exchange earns, and why Plan is not writing it

Three defects today shared one shape: **the measurement was right and the noun was wrong.**
834/829 bytes vs characters · 469/470 zero- vs one-based · 13/12 pipe lines vs body rows. In each,
both numbers were true of different objects and one was labelled wrong. Re-running the command
reproduces the number forever, so the defect is invisible to repetition — it is only visible when
two instruments disagree. The defence is to **record the bound with the number**: *"12 body rows,
§4 bounded by the next enumerated heading"* cannot be misread; *"13"* can.

That belongs in `framework/eval/learned_gates_registry.md`, alongside `LOCATOR_OVERSHOOT_GATE`,
which it is the small-scale case of. **Plan is not writing it there.** `framework/` is content
domain under P5 — everything outside `governance/candidates/`, `ledger/` and `reviews/` — so
registering a gate there is a content change requiring a candidate and a review, not a unilateral
write. Proposed here in the control plane, where recording it moves no hash; the content path stays
owed, alongside `MAT-012…015`.

## What a clean root still does not authorise

The lease · L2 · a batch · `HASHDET`'s execution. It is a preparatory condition. One blocker moved;
the sequence did not.
