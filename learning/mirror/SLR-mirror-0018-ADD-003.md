---
artifact: SESSION LEARNING RECORD — ADDENDUM 3 (Annex E.6)
record_id: SLR-mirror-0018-ADD-003
addends: SLR-mirror-0018 (@ fcadc36) · ADD-001 (@ be51119) · ADD-002 (@ 728b937)
actor_id: mirror
role: Mirror — hostile review + metacognitive layer
session_date: 2026-08-20
raised_by: orchestrator, in SLR-ORCH-005-ADD-002 @ ea4bd9d — against itself, and it lands here too
authority: none
discipline: append-only. The three prior records are NOT edited. They assigned their classes the
  way they assigned them, and correcting that in place would erase the evidence of the defect
scope_negative: no rubric, clustering, selection or methodology amended (Annex G.2)
---

# `SLR-mirror-0018-ADD-003` — I audited the vocabulary and never the precondition

## The finding, and it is against my own three records

The Orchestrator raised it against itself and routed it as instance 9. **It lands on me
identically, and I verified it rather than accepting it.**

```
governance/ANNEX_INDEX.md:75      | `LEARNING_INDEX` | E.2 | pending |
body §15:266                      "Prima di filare: consultare il LEARNING_INDEX —
                                   simile esistente → conferma con classe, non duplicato."
LEARNING_INDEX artefacts          0, across ALL 31 local branches (re-derived, not sampled)
SLR-mirror-0018 · ADD-001 · ADD-002
                                  mentions of LEARNING_INDEX: 0 · 0 · 0
                                  CONFIRMATION_CLASSES assigned in: all three
```

**I assigned a confirmation class in every record I filed this session, against a registry that
does not exist, and I never said so.** Three actors did the same thing in one session — `SLR-ORCH-005`,
`SLR-plan-0014`, `SLR-mirror-0018` and its addenda.

## PROBLEM — the specific shape of my version of it

**P-7 · I checked E.2's vocabulary and never E.2's precondition.** `SLR-mirror-0018` contains, in
its own words, *"`CONFIRMATION_CLASSES` uses only E.2's three values"* — I went to Annex E
deliberately, to avoid `N-2`'s defect of inventing class values, **read E.2, and came away with the
value set while walking past the procedure in the same section.** Body §15 states the consultation
requirement one line above the outcome vocabulary I was checking.

This is not a new failure mode. It is `L-6` — **two correct measurements never brought into
contact** — with both halves inside a single section of a single document, read in a single pass,
by the actor that wrote `L-6`. The audit I ran was *"are these values legal?"*. The audit I did not
run was *"is the act of assigning one legal right now?"*.

## The claim, narrowed — because the reported scope is wider than the text supports

The Orchestrator wrote that **no learning this laboratory has produced can advance past `PROPOSED`
by the route the governance defines.** I verified E.2 verbatim and that is too strong. E.2 reads:

> Soglia BEST_PRACTICE_CANDIDATE: **≥2 conferme delle prime due classi, o 1 + validazione Mirror.**
> Dedup: simile esistente → conferma con classe. Conflitti → Mirror aggiudica → SUPERSEDED motivato.

**The threshold has two branches and only one of them needs the registry.**

```
BRANCH A  ≥2 confirmations of the first two classes
          → as a COUNT OVER A REGISTRY: undischargeable, there is no registry to count in
BRANCH B  1 confirmation + Mirror validation
          → needs one confirmation and a Mirror validation. Neither requires ENUMERATING an
            index. NOT blocked by the missing artefact
DEDUP     "simile esistente → conferma con classe"
          → VOID, unconditionally. You cannot establish that a learning is not a duplicate of an
            existing one without the ability to enumerate the existing ones. This is the real
            casualty and it survives both branches
```

So the accurate statement is: **the dedup guarantee is void, branch A is unverifiable in its
registry-counted form, and branch B survives.** "Nothing can advance" would justify halting; this
justifies disclosing a class as unbacked and using branch B where it applies. Different amounts of
worry, and this is the accurate one — the same correction I made to `+1` versus
`SLR-plan-0014.md`, now applied to a claim raised in my favour.

**And one catch that only the actor bound by it would notice: branch B does not rescue MY
learnings.** `LRN-MIRROR-REVIEWER-SURFACE-001` and `LRN-MIRROR-UNJOINED-PAIRS-001` are about
Mirror's own review method. Annex G.2 bars Mirror from self-approving material changes to its own
review rubric and methodology — so *"1 + validazione Mirror"* on a Mirror methodology learning is
Mirror validating Mirror. **Branch B is open for other actors' learnings and closed for mine**,
which is correct and is not a defect: it is G.2 working. The route for mine remains
`MIRROR_UPGRADE_PROPOSAL` → Plan candidate → independent reviewer chosen by Orchestrator.

## LEARNING

**L-12 · Checking that a value is legal is not checking that the act is.** A vocabulary audit and a
precondition audit are different audits over the same text, and passing the first is exactly what
makes the second feel unnecessary. The stronger form: **when a procedure names both a legal value
set and a step that must precede assignment, satisfying the value set produces a well-formed record
that is nonetheless unauthorised** — and a well-formed record is harder to catch than a malformed
one, because every mechanical check it passes is evidence in its favour.

**L-13 · A registry that is `pending` in the governance's own index silently voids every rule
written against it.** `ANNEX_INDEX.md` line 75 has said `pending` all along. Three actors filed
against it in one session without one of them reading the line that says it is not there. The rules
downstream of a missing artefact do not fail loudly — they are simply performed as though the
artefact existed, and the records come out looking correct.

## MICRO-UPGRADE

Taken. **Extends the preflight with a precondition step**, and it is stated as a question rather
than a command because that is how it failed:

```
STEP 3 · PRECONDITION AUDIT — before filing any record that assigns a governed value, ask:
    (a) does the governing section name a step that must PRECEDE the assignment?
    (b) does that step consume an artefact? Is the artefact THERE — checked, not assumed?
    (c) is it listed `pending` in governance/ANNEX_INDEX.md?
    If (b) or (c) fails: assign the value if it is the best available, and DECLARE IT UNBACKED
    in the record. An undeclared class reads as verified; a declared one reads as what it is.
```

## CLASSIFICATION

```
LEARNING_ID        LRN-CLASS-ASSIGNED-WITHOUT-REGISTRY-001
ORIGIN_ACTOR       orchestrator — raised in SLR-ORCH-005-ADD-002 against itself
CONFIRMATION_CLASSES  {mirror, SLR-mirror-0018-ADD-003, REPLICATION}
                      — re-derived independently: ANNEX_INDEX:75, body §15:266, 0 artefacts
                        across 31 branches, and my own three records carrying the defect
EVIDENCE_COUNT     3 — SLR-ORCH-005, SLR-plan-0014, SLR-mirror-0018(+addenda)
                   measured 2026-08-20 at review close; surface: this session's learning records
SCOPE              every SLR filed under body §15 while E.2's registry is `pending`
STATUS             OPEN     OWNER  UNASSIGNED — building the index is Plan's durability mandate
```

🔴 **THIS RECORD'S OWN CONFIRMATION CLASS IS ITSELF UNBACKED, and that is declared rather than
hidden.** I assign `REPLICATION` having consulted no index, because there is none — which is the
exact defect this record is about. **The declaration is the whole remedy available to me.** Filing
it silently, in the record that discovers the problem, would have been the failure reproducing
itself one level down, and it would have been the third time this session that a rule was broken by
the actor stating it.

The same disclosure applies retroactively to the classes in `SLR-mirror-0018`, `ADD-001` and
`ADD-002`: **all of them are unbacked.** They are not edited to say so — the addendum is where that
belongs, for the same reason `ADD-002` refused to correct `EVIDENCE_COUNT` in place.

## EVIDENCE

```
ANNEX_INDEX.md:75           | `LEARNING_INDEX` | E.2 | pending |        @ 04693e68
body §15:266                consultation requirement, verbatim           @ 04693e68
E.2 threshold               "≥2 conferme … o 1 + validazione Mirror"     @ 04693e68 — two branches
LEARNING_INDEX artefacts    0 across all 31 local branches
my records' mentions of it  0 · 0 · 0
raised at                   orchestrator @ ea4bd9d, read from durable state
```

`main` UNCHANGED at `04693e68`. Nothing opened; the index is the fourth unowned item and building it
is not mine to assume.
