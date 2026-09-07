---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-ORCHWT-MIRROR-001
candidate: CAND-20260817-ORCHWT
content_hash: 280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
base_head: 908197ba62a064546f17c9c277ff497ffc753656
branch_tip: ab4856b1d90c4361f63705f487d5285c54ecba0e
reviewer: mirror
adjudicator: operator
level: R4 / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: ACCEPT
scope: candidate review only — no execution authorised, no gate assessed, no batch, no merge, no adoption
---

# MIRROR HOSTILE REVIEW — CAND-20260817-ORCHWT

```
candidate  CAND-20260817-ORCHWT
tip        ab4856b1d90c4361f63705f487d5285c54ecba0e
hash       280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
reviewer   mirror     level R4 / MIRROR_REQUIRED
verdict    ACCEPT — no blockers
```

The operator has settled the STOP CONDITION as **Option B**, so I review whether Option B is
formally coherent and reviewable, not whether the candidate should be withdrawn.

---

## 1 · Identity and hash — **VERIFIED**

Recomputed with HASHDET r3 tooling, from **two different checkouts**, twice each:

```
ow1 (hash-determinism, v3 working tree)  run1 · run2   280dc497…65763d
ow2 (evidence-index,   v4 working tree)  run1 · run2   280dc497…65763d
declared                                               280dc497…65763d
```

Checkout-independent, as HASHDET r3 guarantees. **Content is exactly what is declared**: the
change set `908197b → ab4856b1` is a single file. The hash at the branch head `4f4ffad` — which
adds the manifest — is **identical**, confirming the manifest is control plane and does not
perturb the object.

## 2 · Scope — **CLEAN, and the tightest of the three candidates**

```
M  deployment/deployment_profile.md          ← the only content file, +24 −1
```

No undeclared change to governance, runtime, capability or authority. **Fingerprints verified
unchanged**, recomputed at `main` and at the tip:

```
mirror 84d2b841… · orchestrator 6b55605d… · plan 37c3b863… · scientist ce3c0d94…   identical at both
```

No other candidate is touched: HASHDET r3 and P51C9 recompute to their recorded values (§6).

## 3 · The §8 divergence — **CORRECTLY DECLARED, and not a bypass**

**Explicitly declared:** yes, and in the strongest available form. §3.1 quotes the **resisting**
text first — §8, §0.2, §47 steps 9 and 14 — before the supporting text. That inverts the ordering
of revision 1, which is exactly what F-2 asked for: the clauses that resist a change are quoted
before the clauses that support it.

**Option A honestly abandoned rather than argued around.** §3.2 states what a compatibility
argument would require — that §8's *"chat grafica associata a `<REPO_ROOT>`"* names a session
location distinct from a filesystem boundary — and concedes *"in this deployment they are the same
concept."* It then notes that §0.2 and §47 do not merely permit the Orchestrator to be the root
chat but describe it being **promoted in place**. Concluding *"Option A is not available"* rather
than manufacturing an interpretation is the correct outcome.

**Limited to the residence clause:** yes, and the narrowing is earned rather than asserted. §0.2's
*"la posizione nella root NON conferisce autorità"* does real work — authority derives from role and
ACTIVE lease, so moving where the actor works cannot move what it may do. §8's sentence is split
and only the first half diverges:

| §8 clause | Status |
|---|---|
| *"vive nella chat grafica associata a `<REPO_ROOT>`"* | **DIVERGES** |
| *"l'unico ruolo che esegue CANONICAL_BATCH_COMMIT"* | **UNCHANGED** |

**Authority, canonical commit, lease and gates unchanged:** confirmed, and enumerated by the
candidate itself under `WHAT IS NOT CHANGED` — root authority (§0.2 already denies location confers
it), `CANONICAL_BATCH_COMMIT` root-only and Orchestrator-only, the `ORCHESTRATOR_LEASE` requirement
intact and still the source of authority, gates 0–5 untouched, §47's promotion still occurring with
only the promoted chat's subsequent residence differing. I verified the mechanical half: the
fingerprints do not move and no governance artifact is edited.

**Not a bypass.** Three properties distinguish a declared divergence from a patch, and all three
hold: the conflicting text is quoted rather than paraphrased; the divergence is stated in C-9
§9.3's own form with `EXISTING RULE / PROPOSED RULE / CONFLICT / REASON / WHAT IS NOT CHANGED`; and
the candidate states `ADOPTION DECISION REQUIRED — Operator, under H.1. This candidate does not
adopt the divergence by declaring it.` A bypass would do the opposite of each.

## 4 · The Orchestrator worktree — **the problem is real and correctly solved**

I verified the diagnosis independently rather than accepting it. Annex D.1: `WORK_COMMIT (ogni
attore, proprio branch — obbligatorio, non canonico)`. The root's branch is `main`. A commit to
`main` is a `CANONICAL_BATCH_COMMIT` by definition. **Therefore an Orchestrator resident in the
root has no branch on which the obligatory WORK_COMMIT is possible — uniquely among six actors.**

The consequence is not theoretical: body §8 obliges that actor to maintain the `DAILY_BRIEF` and
record every adjudication rationale, so the frozen text requires an artefact it gives the actor no
lawful way to persist. The nine untracked files in the root are that defect made visible.

**New problems introduced — none found.** Authority: unchanged, verified. Ownership: the new
worktree is the Orchestrator's own, so no actor writes in another's tree. Security: nothing is
granted; if anything the root's exposure narrows, since it carries a writer only inside a batch
window rather than continuously — which is what §14 calls critical.

## 5 · Provenance — **CLEAN**

Two oids appear in the manifest; both are commits, both exist, both are ancestors of the declared
tip, and both are reachable from a live ref. **No orphans**, and none of the rebase-orphaning that
appeared in the C-9 lineage: the branch was cut directly from `BASE_HEAD` as a single commit, with
no rebase, amend or force-push.

## 6 · Regressions — **NONE**

```
HASHDET r3  b9af54eb → c85acdb2…ad05d8   unchanged
P51C9       b5eaf81e → f325bd9d…0651da   unchanged
GOV311      9720a0cd → c39ecae8…30c239   unchanged
main                 → 908197ba…          unchanged
```

## 7 · Control plane vs content — **CORRECT**

The manifest sits in `governance/candidates/`, a declared control-plane root, and the hash is
provably unaffected by it: identical at `ab4856b1` and at the branch head that adds it. The
verification record's claims match what I measured, including *"fingerprints unchanged — this
candidate touches no CORE artifact"*, which I confirmed by recomputing all four at both commits.

---

## BLOCKING FINDINGS

**None.**

---

## NON-BLOCKING OBSERVATIONS

**N-1 · the divergence is cured in the manifest and not in the artifact that becomes canonical.**
`deployment/deployment_profile.md` mentions §8 exactly **once**, at line 49 — *"§8 obliges it to
produce durable output"* — the clause that **supports** the change. It never mentions the residence
clause it diverges from, nor the divergence, nor the candidate that declares it. So F-2's original
shape — citing the half that helps and omitting the half that resists — survives in the file that
will live in canonical history, while being fully cured in the manifest beside it.

**I considered this blocking and decided against**, for three reasons I record so the judgement can
be checked: the manifest is tracked and persists in canonical history, so the record is not lost;
the body is unamended, so the conflict is visible to anyone reading both; and forcing a content
edit costs a new hash and a new review for what is a documentation improvement rather than a
correctness defect. **Recommendation, not a requirement:** when a future governed change next
touches the profile, give that section one sentence pointing at the divergence record.

**N-2 · §5's recommended ordering makes the practice precede its ratification.** The candidate
recommends establishing the worktree and moving the nine files as *"an operational act, not a
commit"*, before the canonical commit that records it — and says so openly, *"stated openly rather
than discovered"*. That disclosure is the right handling and it is not a bypass: Plan recommends
and does not decide, and no gate is touched. But the operator should weigh what it means — under
that ordering the divergence becomes operational fact **before** it is ratified, and a subsequent
refusal would require undoing an arrangement already in place. That is a choice, not a defect.

**N-3 · no instrument error to report this round.** I record this because I have reported one in
every previous review of this sequence; identity, scope, provenance and regression all ran clean
on first execution, and the one count I could have misread — the single §8 mention in the content
file — I opened rather than assumed.

---

## CHANGE_CLASS — **MAJOR CONFIRMED**

The candidate's §2 argues that the smaller cascade does not downgrade the class, and that is
right. Fingerprints are provably unchanged, so this candidate's blast radius is the smallest of
the three — **and blast radius is not the test.** §12's strict definition names *governance,
authority* and *epistemic policy*; this changes where an actor with unique commit authority
resides, and does so in acknowledged divergence from the frozen body. A zero-cascade change to the
authority model is MAJOR on the definition, and treating cascade size as the criterion would be the
error.

---

## DECISIONS REMAINING EXCLUSIVELY WITH THE OPERATOR

1. **Adoption of the divergence.** The candidate declares it and explicitly does not adopt it.
   H.1 assigns governance to you. The stated alternative — amending §8 in the frozen text — is
   named as *"a larger act and not proposed here"*, and remains open.
2. **The execution ordering of §5**, including whether the operational move precedes the commit
   that legitimises it (N-2).
3. **The consequence the candidate states and I confirm:** whichever of ORCHWT and P51C9 executes
   first moves the other's `BASE_HEAD`. If ORCHWT goes first, P51C9 must be re-based and re-hashed
   **under v4** before its approval binds — its current binding would no longer describe it.

---

## DISPOSITION

```
MIRROR_REVIEW: ACCEPT

CANDIDATE  CAND-20260817-ORCHWT
HASH       280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
BASE       908197ba62a064546f17c9c277ff497ffc753656
TIP        ab4856b1d90c4361f63705f487d5285c54ecba0e
DATE       2026-08-17     REVIEWER  mirror

Identity · Scope · Divergence form · Provenance · Regression · Control plane   all verified
Blockers                                                                       none
Non-blocking                                                                   N-1, N-2, N-3
CHANGE_CLASS                                                                   MAJOR, confirmed
```

🔴 **`ACCEPT` means only: no defect found that requires change before the human decision.** It is
not operational approval, not batch authorization, not a `GATE 0` assessment, not a merge, and not
adoption of the governance divergence — which the candidate itself refuses to self-adopt and which
only you can grant.

No file of this or any other candidate was modified. HASHDET r3 and P51C9 were not reopened. All
verification ran in disposable clones outside the repository; this worktree is clean.

---

## Appended 2026-08-18 — where this record's C.2 elements live

All three obligatory elements were missing and are supplied in `OWED-C2-FORMAT-001-REPAIR` **§ B.3**, written on 2026-08-18 and marked there as after-the-fact.

Appended, not edited. The original text above is unchanged.
