---
record: PHASE III — REVISED SCIENTIFIC SYNTHESIS
id: PHASE3_REVISED_SYNTHESIS_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Mutates nothing. **NOT hostile-reviewed** — §10 requires a Scientist who did
  not author this, so A or C must perform Phase IV. I cannot, and I do not pretend the review
  happened.
producer_designation: 🔴 **NOT designated by any canonical mechanism.** §9 says designate a producer
  "according to the canonical task/routing mechanism". `ledger/tasks/` holds only `plan/` on every
  ref — there is no Scientist task surface and no routing mechanism to invoke, and §15 puts actor
  designation with Orchestrator. I therefore produce this **only for the position I personally held
  and revised**, plus the composition of three first-passes that no one of us held alone. It is a
  proposal to the team, not an assumption of the producer role.
---

# Phase III — the revised thesis, and the account that only exists when three readings are put together

> **Nothing here is medical advice.** Lithium has a narrow therapeutic index. Nothing below supports
> its use in any patient, and the strongest conclusion here is about what a mouse experiment does
> *not* show.

---

## 0 · Which relations actually reached Phase III

§9 triggers on *substantive disagreement*. Measured against Phase II:

| Disagreement | Kind | Resolution |
|---|---|---|
| Wang 2012 locator match, 2/9 vs 9/9 | **my measurement error** | **Retracted.** No thesis to revise — a finding withdrawn |
| Edge type for `016 ↔ 035`: `INDIRECT_UNKNOWN_INTERMEDIATES` vs `ASSOCIATED` | **interpretation, same evidence** | **Resolved in A's favour → §1 below** |
| Does the Pathograph workset exist | **different evidence** (worktree scope) | Resolved against C; a measurement question, not a scientific one |
| "Disproven" vs "unsupported" for the *elevated* wording | **wording, agreed substance** | Resolved against me, twice over |
| Whether the Ser9 fall is WWOX-proximal or systemic | **nobody disagreed — three partial accounts** | **Composes → §2 below.** Unresolved as science, not as dispute |

🔴 **There is no surviving substantive scientific disagreement between the three scientists on the
eight §12 questions.** That is itself a result and it should not be dressed up as one: the three
readings converged on nine propositions (Phase II §5), and every disagreement that arose was either
an error, a token choice, or a scope artefact. **A pilot designed to surface dissent surfaced
almost none, and the interesting output was complementarity instead.**

---

## 1 · Revised thesis — the relation `CLAIM 016 ↔ CLAIM 035`

### INITIAL POSITION

`INDIRECT_UNKNOWN_INTERMEDIATES`, direction `035 → 016` only. My reasoning: the residue-mapped WWOX ⊣
GSK-3β brake (Wang 2012) is real and direct at the molecular scale; the murine seizure phenotype is
real; between them sits at least one intermediate nobody has measured — and the one bridging
measurement offered, Ser9 dephosphorylation, is on an axis the mechanism paper declares
S9-independent. I read that as *the path exists and its intermediates are unmapped*.

### CHALLENGE

Scientist A, artifact 02:

> *"`INDIRECT_UNKNOWN_INTERMEDIATES` … asserts a causal path with unspecified intermediates. Here
> the intermediates are not merely unknown — the one bridging measurement offered (Ser9) is the one
> the mechanism paper shows is not the operative channel. Typing it this way would encode as
> unknown-but-real something that is untested."*

### NEW EVIDENCE

**A's observation 7, which I did not have.** Wang 2012, body-exact:

> *"Transfection with GFP–GSK3β WT and S9A notably decreased SH-SY5Y cell differentiation, whereas
> KD and R96A did not affect SH-SY5Y cell differentiation"*

A GSK-3β mutant that **cannot be inhibited by Ser9 phosphorylation** suppresses differentiation
**exactly like wild type**, while kinase-dead and R96A do not. I had only the weaker observation —
pS9 unchanged while output falls — which shows the Ser9 axis is *not engaged* in that experiment.
Obs. 7 shows it is *dispensable by design*, with internal controls, in the assay the mechanism rests
on.

**A's count, verified in kind by me:** the shared evidential paper contains `seizure` 0, `epilep` 0,
`convuls` 0, `lithium` 0, `LiCl` 0 across 49,334 non-abstract characters. The "shared evidence" is
bibliographic, not evidential — it measures one endpoint and never the other.

### WHAT CHANGED

**The type.** `INDIRECT_UNKNOWN_INTERMEDIATES` presupposes the causal path and reports its interior
as unmapped. With obs. 7, the bridging measurement is not merely uninformative about the path — it is
an event the mechanism predicts would *not* occur if the path were the operative one. That is not an
unmapped interior; it is **an untested exterior.**

**REVISED: `ASSOCIATED`, direction `035 → 016` only.**

### WHAT DID NOT CHANGE

- Every figure reading, re-verified against artifacts whose fingerprints match the manifest exactly.
- Directionality: no direction is licensed for the `016` half. A reaches this independently.
- The per-half disposition: WWOX ⊣ GSK-3β is `DIRECT` **within Wang's system**, with the
  no-WWOX-DEE-allele boundary attached; GSK-3β state → seizure remains hypothesis.
- The reciprocity the assembler reports is a `Wikilinks` list entry, not evidence.
- The four canonical defects. None applied. §16 observed.

### REMAINING UNCERTAINTY

`ASSOCIATED` is the best available token and all three of us report the vocabulary as insufficient.
Four causal values cannot express what the paper registry already writes in seventeen free-text
qualifiers — `supplies the functional assay`, `refutes its imported premise for the mouse`,
`bounds its imported premises`, `tensions`. **The agreement A and I reached is a local optimum inside
an instrument we both say is the wrong shape.**

### FALSIFIER / DECISIVE NEXT EVIDENCE

Demonstrate the Wang mechanism operating in `Wwox−/−` brain: a GSK-3β pull-down from null brain, an
L404-dependent manipulation *in vivo*, or a substrate-specific GSK-3β activity readout (Tau S396/S404
rather than pS9). Any of the three would move this edge from `ASSOCIATED` toward a causal type. **None
exists**, and the field is narrow: `WWOX AND GSK3` returns five records in all of PubMed.

---

## 2 · The composed account — three readings, one explanation

This is the substantive scientific output of the pilot, and **no single first-pass contains it.**

### The observation everyone agrees on

In `Wwox−/−` mouse brain at postnatal day 20, GSK-3β Ser9 phosphorylation is reduced by 36–52% across
cerebellum, hippocampus and cortex, while total GSK-3β is flat (all nine lanes 2.2–2.6). One
representative blot, no error bars, no per-lane n, no statistical test. The heterozygote is **not**
intermediate — it sits at or above wild-type on the phospho row in every region.

### The reading the canonical model carries

*Loss of WWOX de-represses GSK-3β; de-repressed GSK-3β contributes to seizure susceptibility;
lithium, a GSK-3β inhibitor, suppresses the seizures.*

### Three independent objections that compose into one account

| Source | Objection | What it establishes |
|---|---|---|
| **B** (readout mismatch) | CLAIM 035 declares WWOX's inhibition **S9-independent** and warns that pS9 will produce a **false negative** in a WWOX-deficient setting. CLAIM 016's principal molecular evidence *is* a pS9 western in exactly that setting | The two claims are wikilinked while one contains the argument that the other's key measurement does not mean what it is taken to mean |
| **A** (S9A mutant) | A GSK-3β immune to Ser9 inhibition behaves like wild type in Wang's own assay, with kinase-dead and R96A as internal controls | The Ser9 axis is **dispensable by design**, not merely unengaged. B's mismatch stops being an inference and becomes a designed result |
| **C** (metabolic route) | Ser9 phosphorylation is the canonical output of insulin/IGF-1 → PI3K → AKT. CLAIM 036 documents the systemic constitutive null at P18 as hypoglycaemic (143.5 vs 250.6 mg/dL), acidotic (bicarbonate 14.50 vs 21.67 mEq/L) and uraemic (BUN 37.25 vs 17.67 mg/dL). A hypoglycaemic, catabolic, acidotic animal has reduced AKT activity and therefore reduced Ser9 phosphorylation | Supplies a **complete alternative cause** — the right direction, the right readout, no WWOX–GSK-3β mechanism required |

**Composed:** losing the WWOX brake predicts raised GSK-3β activity **with Ser9 unchanged** (A).
Cheng observed Ser9 **changed** (the datum). Therefore the observed event is not the signature of the
lost brake (B) — and there is a standing, quantified, same-window, same-model-class explanation that
predicts exactly it (C).

🔴 **The heterozygote closes the loop, and it is the lane nobody was looking at.** C read the panel's
own `Wwox` row: WWOX protein is absent in `−/−` and **visibly reduced in `+/−`**. So gene dosage is
plainly visible at the level of WWOX protein and **entirely absent at the level of pSer9** — half the
WWOX yields full Ser9 phosphorylation. **A dosage control internal to the panel, showing that the
readout does not track the gene.** That is what a systemically-driven readout looks like, and it is
what a WWOX-proximal one does not.

### Held at its proper strength

**This does not refute the observation and does not refute CLAIM 016.** Ser9 dephosphorylation and
loss of docking inhibition are not mutually exclusive: a WWOX-null brain could carry both, and both
push GSK-3β activity up. A states that counter-argument at its strongest and does not defeat it —
**what it lacks is a measurement**, and the heterozygote weighs against its simple dose-dependent
form.

C's confound is likewise **untested, of high prior plausibility, not demonstrated**: CLAIM 036's
window is P14–P18 in a different line (EIIA-Cre `Wwox^ΔCre/ΔCre`), Cheng's is P20 in his own strains.

**What the composition removes is not the observation. It is the observation's right to be read as a
WWOX-specific mechanistic signal until a metabolically-controlled measurement exists.**

### FALSIFIER — one experiment settles it

Measure brain pGSK-3β(Ser9) in `Wwox`-null mice against littermate controls that are **pair-fed or
glucose-clamped**, or in a **brain-restricted conditional null that is not systemically ill** — the
`Wwox^flox` allele CLAIM 036 records as built and never used in this direction.

- pSer9 drop **survives** metabolic normalisation → the mechanistic reading stands, and the
  S9-independence of CLAIM 035 becomes the open question instead.
- pSer9 drop **disappears** → CLAIM 016's core molecular datum is a readout of terminal illness, and
  the edge to CLAIM 035 loses its only in-vivo bridge.

Either outcome is informative, which is what makes it the right experiment. **Secondary falsifier for
the pharmacology:** a PTZ + lithium arm with an explicit, tested genotype × treatment interaction, a
structurally unrelated GSK-3β inhibitor at matched exposure, and a post-treatment pSer9 western
demonstrating target engagement — a measurement the paper never made in any lithium-treated animal
(C, verified across 71,916 characters of XML and a 24-page supplement).

---

## 3 · The dissent trail, not erased

Preserved because §9 requires it and because two of these were mine:

1. **B reported the Wang 2012 manifest as 2/9 strict and confirmed a defect class. Withdrawn** — the
   figure was an artefact of B's own tag-stripping. A got 9/9. The Phase I record carries the
   retraction in place.
2. **B typed `016 ↔ 035` as `INDIRECT_UNKNOWN_INTERMEDIATES`. Revised to `ASSOCIATED`** on A's
   argument. The original verdict stands in the Phase I record with a forward pointer, not overwritten.
3. **B wrote "disproven" for the *elevated* wording. Revised to "unsupported and misdescribed"** —
   the abundance direction really is upward by 9–18%. A and C objected independently.
4. **B wrote that the working-model mirror "is already corrected". Revised to "half-corrected"** —
   C is right that *"not merely elevated abundance"* still presupposes abundance is elevated.
5. **C concluded the Pathograph does not exist. It does**, untracked in the shared checkout; C's
   sweep was worktree-confined. **C's ref denominator (57) is better than B's (50).** Not conceded by
   C — C has not read this.
6. **A declared the Phase II gate closed on C.** It opened 6 min 23 s before A wrote that. Not
   conceded by A — A has not read this.
7. **B's Q1/Q2 formulation was stronger than the panels license.** C's is weaker and harder to
   overturn; adopted.

🔴 **Items 5 and 6 are one-sided.** I have read A and C; neither has read me. **This is not agreement
and must not be recorded as such.** Phase II as specified is symmetric — *A reads B and C, B reads A
and C, C reads A and B* — and only one third of it has happened.

---

## 4 · What this synthesis is not

- **Not hostile-reviewed.** §10 requires a Scientist who did not author it. **A or C must perform
  Phase IV**, and the two findings that most need adversarial attention are the two I depend on and
  did not derive: A's obs. 7 and C's AKT route.
- **Not a Phase V final synthesis.** §11's producer is designated by a mechanism that does not exist
  here; §15 puts that with Orchestrator.
- **Not canonical, and not a commit candidate.** The four canonical defects (Phase I §12) still
  require `BATCH_COMMIT` and the operator.
- **Not a claim that the science is settled.** The decisive experiment in §2 has not been done by
  anyone, and the field is five papers wide.
