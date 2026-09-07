---
record_type: HUMAN_APPROVAL_RECORD
id: HUMAN-APPROVAL-20260822-ORCHSURF-R4-TRANSCRIPTION-PATH
title: Operator approval that the ORCHSURF revision 4 transcription path was completed as governed
date: 2026-08-22
authority: Operatore                 # Annex H.1 — governance / strategia complessiva -> Operatore
approved_by: Operatore, 2026-08-22
registering_actor: plan              # registration is a clerical act; it grants nothing
registration_authority: explicit operator authorization, citing Annex H.1
status: REGISTERED
change_class: PROCESS_COMPLETION_APPROVAL
change_class_rationale: >
  No frozen governance document is modified. No candidate is modified. No gate is
  cleared. This record approves that one bounded, already-executed procedural
  path was completed according to the governed process, and that the artefacts
  recorded below correspond to that executed path. It approves nothing else.
approves_object: the executed transcription path defined by
  DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING
does_not_modify:
  - governance/candidates/CAND-20260819-ORCHSURF.md
  - governance/decisions/DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md
  - reviews/mirror/REV-ORCHSURF-ADD-002-COMPLIANCE-VALIDATION.md
  - reviews/mirror/REV-ORCHSURF-ADD-002-FIDELITY-VALIDATION.md
  - reviews/mirror/REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY.md
  - reviews/orchestrator/REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION.md
  - governance/annex_d_commit_batch.md
  - Annex D.2 vocabulary
  - governance/annex_c_review_protocol.md
  - main
is_not:
  - a J.3 HUMAN_APPROVAL_QUEUE entry — no APPROVAL_ID is created and
    ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl is not written by this record
  - a GATE 5 approval bound to a CANDIDATE_CONTENT_HASH + BASE_HEAD
  - a C.3 review round, opened, spent, reopened or closed
hash_convention: >
  SHA-256 (shasum -a 256) is the binding convention, inherited from
  DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING. Git object hashes are
  supplementary identifiers only. This record's own SHA-256 is registered
  externally, in its registration commit message, by the same convention and for
  the same reason: a document cannot contain the hash of itself.
registration_surface: >
  directory governance/decisions/, branch orchestrator-surface, following the
  designation in DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING
  § "Registration and transit" and the precedent it cites,
  DEC-20260820-ORCH-SESSION-HOME.
---

# Purpose

This record is the durable trace of one explicit operator approval.

The operator approves that the transcription path defined by
`DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING` was **completed according to
the governed process**, and that the five artefacts enumerated below **correspond
to the path that was actually executed**.

It exists because a conclusion held only in conversation is not procedural
evidence. That rule is the substance of Decision 4 of the DEC this record closes
the loop on, and it applies to an operator's approval exactly as it applies to a
reviewer's verdict.

**This record grants no authority.** It approves the completion of a path that is
already finished. It authorizes nothing that has not already happened.

---

# The approved statement

> "The operator approves that the executed transcription path has been completed
> according to the governed process and that the recorded artefacts correspond to
> the executed path."

That sentence is the whole of what is approved. Nothing is read into it, and
nothing outside it is approved by implication.

---

# Approval scope

## A · The governed path

Approved: **completion** of the governed transcription path defined by
`DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING`.

Completion means the path ran through its declared stages. It does not mean the
result is right, that the candidate is now accurate, or that anything downstream
of it may proceed.

## B · The five artefacts

Approved: the **existence and integrity** of the following durable artefacts.
Every value below was re-derived from repository objects at registration time —
`git cat-file`, `git ls-tree`, `shasum -a 256` — and none was carried from the
authorization text or from any conversation.

```
1 · DEC — the routing decision this path executes

  path      governance/decisions/DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md
  commit    aa49df9aa204961487861a288227402d1c756d5f      resolves: commit
  blob      42d26de3429169fda487820140c53194a71dc1e5      present at that path in that commit
  sha256    2a6054d0b95007edbcf2e1459e1aa1a8f6f95c96bac9a558557760e851082a6e
  surface   orchestrator-surface
  note      the sha256 above is RECOMPUTED here and equals the POST_RATIFICATION_HASH
            registered externally in commit aa49df9's own message. The record's
            frontmatter field post_ratification_hash.value is empty by its own design.
            Agreement between the two independent measurements is the integrity check

2 · Mirror Decision 4 compliance validation

  path      reviews/mirror/REV-ORCHSURF-ADD-002-COMPLIANCE-VALIDATION.md
  commit    dfdfee5732d777b663b6089200e374d9f4d4e823      resolves: commit
  blob      f516b933146e1ae116a19c6a036fc785c4fe648d      present at that path in that commit
  sha256    6246da611e67fbf18cc50a323779ceb96807cf6e7f361a126ef2e19a1028dd26
  surface   mirror
  author    mirror — as Decision 4 requires: authored by Mirror, on the Mirror-controlled branch
  states    VALIDATION_RESULT: COMPLIANT, scoped by its own text to Decision 4 and nothing else

3 · Mirror patch specification fidelity validation

  path      reviews/mirror/REV-ORCHSURF-ADD-002-FIDELITY-VALIDATION.md
  commit    71694319cd009a4b6cf8056fa7cdca303d5f2a76      resolves: commit
  blob      3925c573c4ede9effe2d080316b316a2d7127650      present at that path in that commit
  sha256    61a217555ffc9c890b6765786f64a7a51a4d2b51562772c5378bb93b0fd936ba
  surface   mirror
  states    VALIDATION_RESULT: FAITHFUL — with three findings, none of which defeats fidelity

4 · Plan transcription WORK_COMMIT

  commit    b14a0d1466962aa79d1bbd0065a0d1141f4a0eab      resolves: commit
  branch    plan-orchsurf-r4-transcription — the branch tip is exactly this commit
  parent    aa49df9aa204961487861a288227402d1c756d5f — exactly one parent, not a merge
  scope     one path changed: governance/candidates/CAND-20260819-ORCHSURF.md
  blob      92c1b7d8be169232613ae8b219112a09d7b315dc  ->  e0f3f7299b482d0dd69d5ee7a9e058d2fa410f5c
  sha256    19a7daee…f0759                             ->  44573a55…e3d378
  contained by   plan-orchsurf-r4-transcription ONLY. Verified individually against
                 main, orchestrator, orchestrator-surface and mirror: none contains it

5 · Mirror post-transcription fidelity validation

  path      reviews/mirror/REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY.md
  commit    3a30ecbe69baf90504e9b76b62d9796357afadde      resolves: commit
  blob      fd24e04b88293d151fdaab7cccfcc7fcfbe2a0e3      present at that path in that commit
  sha256    e7a354701a8a07cd0c693fcbfb0513efeb85bc0f20626bf51261d0b3ddd1ca6b
  surface   mirror
  states    FINAL_RESULT: FAITHFUL — scoped by its own text to transcription fidelity
            and to nothing else
```

## C · What "integrity" means here

That each named object resolves, that each named path is present in the named
commit, and that the content hashes back to the recorded value. It is a statement
about the objects, not about their contents' correctness.

---

# Explicit non-approval

This record does **not** approve, and may not be cited as approving:

```
ORCHSURF revision 4 as a design decision   NOT APPROVED. No reviewer issued PASS on
                                           revision 4, and this record issues none
canonicalization                           NOT APPROVED
movement to main                           NOT APPROVED. main is 04693e683a254ff0a6d0619f
                                           ba47103a0fb7d122 and is untouched by this record
CANONICAL_BATCH_COMMIT                     NOT APPROVED, and not Plan's to execute in any case
                                           (Annex H.1 — Orchestrator alone, under lease)
HUMAN_APPROVAL for downstream gates        NOT GRANTED. No APPROVAL_ID is created. No GATE 0–5
                                           condition is asserted, cleared or waived
resolution of UNRESOLVED-D                 NOT RESOLVED
any general interpretation of Annex D.2    NOT ADOPTED. Decision 1 of the DEC forbids its own
                                           generalization, and this record adopts no reading
any future transcription or governance     NOT AUTHORIZED. Every subsequent act requires its
action                                     own governed dispatch under the applicable
                                           H.1 authority
```

**`FAITHFUL` is not `PASS`.** The two Mirror artefacts that return `FAITHFUL`
answer a fidelity question — *was exactly the authorized text applied, and
nothing else* — and both say in their own words that this is not a verdict on
ORCHSURF. `roles/mirror.md` makes a Mirror confirmation mean *"no defect found
given the available evidence bundle"*, never *"true"*. This record does not
convert either result into an approval of the ORCHSURF design, and no actor may
read it as having done so.

---

# Preserved open items

```
UNRESOLVED-D          REMAINS OPEN. Defined at
                      reviews/orchestrator/REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION.md § 8,
                      read at the revision Decision 4 selected (commit 1e2fabd3, blob ab3a946c,
                      sha256 758b45bf…2f63b): whether § 6 constraint 7 — that the C.3 rounds are
                      spent — belongs in the candidate. Untouched, not re-decided, and any future
                      resolution requires its own governed determination

C.3 review rounds     NONE opened, consumed, reopened or closed by this record.
                      REV-ORCHSURF-MIRROR-002 stays closed

candidate binding     NOT re-bound. This record supplies no binding for any canonical
                      batch operation. Decision 3 of the DEC requires the resulting state to
                      receive a new explicit binding before any canonical batch operation, and
                      this record is not that binding

Decision 4 revision   The selection of commit 1e2fabd3 over d5382632 remains scoped, by the
selection             DEC's own words, to that binding only, and establishes no general rule
```

---

# What this registration is, mechanically

Plan wrote this file on branch `orchestrator-surface` and committed it. That act
places the record where the DEC's own "Registration and transit" section
designates, and it is the whole of Plan's contribution.

Registration is clerical. It makes the record citable and adds nothing to it.
The authority in this record is the operator's, exercised under Annex H.1;
Plan's role contract (`roles/plan.md`) states that Plan is not command authority,
does not resolve contested meaning, and does not execute `CANONICAL_BATCH_COMMIT`.
None of those boundaries is crossed here, and none is loosened by this record.

The registration surface is distinct from the transcription surface of the DEC's
Decision 3. Neither implies the other. Plan's `WORK_COMMIT` b14a0d1 stays on
`plan-orchsurf-r4-transcription` and is neither moved, merged, cherry-picked nor
amended by this registration.

END OF RECORD.
