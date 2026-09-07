---
artifact: MIRROR candidate readiness summary — handoff for HUMAN_APPROVAL review
handoff_id: HANDOFF-CANDIDATE-READINESS-001
reviewer: mirror
adjudicator: operator
date: 2026-08-17
scope: readiness summary only — no execution authorised, GATE 0 not evaluated, no merge, no batch
---

# CANDIDATE READINESS SUMMARY

Prepared for the operator's `HUMAN_APPROVAL` review. Every hash and tip below was recomputed here
with the HASHDET r3 tooling from disposable clones; none is taken from a candidate's own
declaration.

---

## 1 · Candidate status

| | **HASHDET r3** | **P51C9 rev 2** | **ORCHWT** | **GOV311** *(reference)* |
|---|---|---|---|---|
| **Identifier** | `CAND-20260817-HASHDET` | `CAND-20260817-P51C9` | `CAND-20260817-ORCHWT` | `CAND-20260816-GOV311` |
| **Branch** | `hash-determinism` | `evidence-index` | `orchestrator-worktree` | *(committed)* |
| **Tip** | `b9af54ebe2fd24d94ec0eee71fcb064797922082` | `b5eaf81ed50b3c994c6ee7cede47a2114cdcaa6c` | `ab4856b1d90c4361f63705f487d5285c54ecba0e` | `9720a0cd…` |
| **Hash** | `c85acdb2…ad05d8` | `f325bd9d…0651da` | `280dc497…65763d` | `c39ecae8…30c239` |
| **Hash version** | `v3` | `v4` | `v3` | `v3` |
| **BASE_HEAD** | `908197ba…` | `908197ba…` | `908197ba…` | `749a9a9b…` |
| **CHANGE_CLASS** | MAJOR | MAJOR | MAJOR | MAJOR |
| **Content radius** | script + suite + manifest | P5.1 amendment + 1 SLR | `deployment_profile.md` only | — |
| **Mirror review** | **ACCEPTED** — `REV-HASHDET-MIRROR-003` (`e0da42b0`) | **ACCEPTED** — `REV-P51C9-MIRROR-002` (`64177c08`) | 🔴 **NOT REVIEWED** | approved · committed at `908197b` |
| **Remaining blockers** | **none** | **none** | **unknown — no review performed** | none |
| **Non-blocking open** | 4 | 3 | not assessed | — |
| **Can HUMAN_APPROVAL evaluate intent?** | **YES** | **YES**, with §3.2 noted | **NO** — see §3.1 | n/a, historical |

**Non-blocking items, carried and not waived.**
*HASHDET r3:* duplicated serialization expression in `serialize_domain`/`compute`; `$(…)` strips
the last byte of the `--emit-domain` representation; `test_historical_replay` does not discriminate
in a v3 checkout; encoding implicit in P5.2.
*P51C9 rev 2:* `reviews/` is a third unbounded prefix root; `runtime/`'s interim safety is
conditional on staying untracked with nothing enforcing it; `legend_lint.py` has zero coverage of
`governance/`, so this class of defect is not machine-detectable.

**GOV311 is reference only.** It is already approved and in canonical history. It appears here
because it is the replay control: it recomputes to its recorded `c39ecae8…30c239` from every
checkout tested, which is the property HASHDET restored.

---

## 2 · Dependency ordering — established by measurement, not by argument

**HASHDET first. P51C9 second. ORCHWT separately.**

I tested what happens *without* the HASHDET fix, computing each pending candidate's hash with the
pre-fix script from two checkouts:

| Candidate | from a **v3** checkout | from a **v4** checkout | its manifest declares |
|---|---|---|---|
| P51C9 rev 2 | `db6cffac…` | **`f325bd9d…`** ✅ | `f325bd9d…` |
| ORCHWT | **`280dc497…`** ✅ | `b4e7c493…` | `280dc497…` |

**The two pending candidates require opposite checkouts to reproduce their own declared hashes.**
Without HASHDET there is **no single vantage point** from which an operator can verify both
bindings — verifying one necessarily falsifies the other. With HASHDET r3 both reproduce from
anywhere, which is what I verified in the two acceptance reviews.

That is the dependency, and it is about **verifiability, not value**: the numbers do not change,
but before HASHDET an approval bound to either hash could not be checked by a third party without
first knowing which governance the checkout happened to carry.

- **HASHDET first**, because it restores `HASH = f(BASE, TIP)` and therefore makes any subsequent
  approval binding checkable. Its own hash is `v3` and reproduces from anywhere already, so it does
  not depend on itself.
- **P51C9 after HASHDET**, because it is hashed under `v4` — the rule its own tip carries — and only
  the fix makes that value reproducible outside a v4 checkout.
- **ORCHWT separately**, because its subject is runtime and worktree governance rather than
  candidate identity. It shares no content file with either (its whole content radius is
  `deployment/deployment_profile.md`), so it is orderable independently — and it must be, because
  §3.1 may remove it from the queue entirely.

---

## 3 · Open decisions that technical review cannot resolve

### 3.1 · ORCHWT — which reading of the STOP CONDITION was meant 🔴

The instruction that produced ORCHWT offered **Option B (formal divergence)** for the case where a
compatibility argument fails, and also instructed a **STOP** on conflict. Plan reads these as
"stop the compatibility route and declare the divergence" and states in the manifest that under the
other reading — "stop the candidate" — **the candidate should be withdrawn rather than reviewed.**

**Only you can settle this, because it is a question about what your own instruction meant.** No
amount of review resolves it, and the order matters: reviewing ORCHWT before the reading is settled
risks producing a verdict on a candidate that should not exist. **I have therefore not reviewed
it**, and I recommend the reading be settled first.

This is also the answer to *"should any candidate be withdrawn instead of revised"*: **ORCHWT is the
only candidate for which withdrawal is on the table**, and not because of any defect found — none
was looked for.

### 3.2 · P51C9 — the scope of operator decision 4

Decision 4 excluded SLRs from the P51C9 candidate pending Mirror's E.2 curation. `SLR-plan-0001.md`
is now inside it. Plan reads decision 4 as having named *the Orchestrator's two SLRs*, this record
being Plan's own and later. **I confirmed that reading is textually supported** — §18 names
inclusion in a candidate as a route to durability, and the record declares its class proposed
rather than self-certified — **but the scope of your decision is yours to state**, not mine to
infer. It is not a blocker; it is a confirmation I cannot give on your behalf.

### 3.3 · Authority questions still open from earlier reviews

| Question | Status |
|---|---|
| PID-09 / PID-10 — the two declared deviations from frozen text | `APPROVAL-GOV311-DEVIATIONS.md` is `AWAITING_HUMAN_APPROVAL`. I recommended ACCEPT for both and declined to ratify: a deviation from frozen text is governance, and H.1 assigns governance to you |
| `MIRROR_RETROSPECTIVE` interval `N` | still unassigned. G.2 forbids me setting it alone; three actors have now declined it |
| Capability demotion — who writes the state transition | C-9 §10 derives Mirror-writes-evidence / Orchestrator-writes-transition from C.4 and promotion symmetry. Derived is not ratified |
| C-9's own clauses | the document is `ACCEPTED` and carries `acceptance_is_not_adoption: true`. Nothing in it binds until adopted through a governed change |
| `HUMAN_APPROVAL_QUEUE` | `APR-20260816-GOV311-001` (MAJOR) and `APR-20260816-GOV311-002` (GOVERNANCE) both read `PENDING` |

---

## 4 · Gate separation — four distinct things, none of which implies the next

```
1  REVIEW ACCEPTANCE          Mirror.  "No defect found requiring change, given the evidence
                              bundle." Annex C.2: CONFIRMED never means "true". It is not
                              permission for anything.  ← the only thing I have granted

2  HUMAN_APPROVAL             Operator. Authorises the INTENT, bound to a specific
                              CANDIDATE_CONTENT_HASH + BASE_HEAD, recorded as a durable object in
                              the queue (J.3).  ← not granted; both entries read PENDING

3  EXECUTION AUTHORIZATION    Body §12, E4: "APPROVAL ≠ AUTHORIZATION — l'approvazione autorizza
                              l'intento, non bypassa i gate." An approved MAJOR with a dirty root
                              is still NO BATCH. GATES 0–5 apply at execution time regardless of
                              approval.  ← not evaluated in this handoff, by instruction

4  BATCH PERMISSION           Orchestrator alone, under an ACTIVE singleton lease, with
                              batch_commit_gate open and GATE 0 satisfied.  ← no lease exists
```

**Nothing in this document collapses these.** My acceptance of two candidates is (1) and only (1).

---

## 5 · Final recommendation

```
CAND-20260817-HASHDET r3    READY FOR HUMAN APPROVAL
CAND-20260817-P51C9 rev 2   READY FOR HUMAN APPROVAL   (§3.2 to be confirmed by you)
CAND-20260817-ORCHWT        NOT READY — §3.1 must be settled before review, not after
```

**Overall: READY FOR HUMAN APPROVAL, for the two accepted candidates only.**

I give a per-candidate verdict rather than one because a single answer would hide the distinction
that matters: two candidates have been reviewed and carry no blockers, and the third has not been
reviewed at all and may not need to be.

**What "ready" means here**, precisely: the two accepted candidates are internally consistent,
their identities reproduce from any checkout under HASHDET r3, their provenance resolves, and I
found no defect requiring change before you look at them. It means their **intent is evaluable**.
It does not mean they should be executed, that any gate has been assessed, or that the sequence
beyond your decision has been prepared.

🔴 **This handoff authorises nothing.** It recommends no execution, evaluates no gate, performs no
merge, and creates no batch. `HUMAN_APPROVAL` remains ungranted for every candidate listed; GATE 0
remains unevaluated by instruction and, on the evidence in the candidates themselves, remains
unpassable; no lease exists. The decision is yours alone.

No file of any candidate was modified. All recomputation ran in disposable clones outside the
repository.
