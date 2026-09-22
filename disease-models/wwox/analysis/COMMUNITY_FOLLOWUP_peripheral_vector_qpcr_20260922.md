# COMMUNITY_FOLLOWUP — peripheral vector-genome qPCR on already-harvested tissue

> **Non-canonical analysis.** Touches no `*_current.md`, no registry, no ledger, no receipt chain,
> no state manifest. No `BATCH_COMMIT`. `HYPOTHESIS ≠ CLAIM`.
> **Not medical advice.** No molecule, dose or route. Reference WWOX-DEE genotype class, never an
> individual. Alleles and models are never pooled.
> 🔴 **Nobody has been contacted and nobody will be by an agent. All outreach is `HUMAN_REQUIRED`.**
> **Actor:** Orchestrator · **Date:** 2026-09-22

---

## 0 · Why this one is different from a suggestion

Most follow-ups a reading programme generates are *designs*: someone must still work out the assay.
This one is not. **The assay is already defined, by the same laboratory, in the same paper, for the
same vector.** What is proposed is applying an existing, published, internally-validated
measurement to tissue that the same experiments necessarily produced — to answer a question that
was never asked of it.

```
EXISTING ASSAY  +  EXISTING MATERIAL  +  NEW QUESTION  →  no new animals
```

---

## 1 · The packet

| Field | Content |
|---|---|
| **Group** | The Aqeilan-associated WWOX gene-replacement programme (2021 and 2026 studies) |
| **Existing assay** | 🟢 **The vector-genome qPCR primer pair is published verbatim** in the 2026 Methods, transcribed first-hand into this repository at `cerebellum_layer_localisation_20260922.md:212–215`: forward `5′ GCTCTCTTAAGGTAGCCCCG 3′`, reverse `5′ CGCCTCATCCTGGTCCTAAA 3′`; **50 ng DNA template per reaction**; tissue lysed in **ATL buffer, up to 25 mg**; DNA quantified on DeNovix DS-11FX+. **No sequence is invented here.** |
| **Existing material** | Tissues a reported measurement *entails* were dissected — 2026 **liver** (WB + IHC, both LD and HD arms), **sciatic nerve** (HD), **spinal cord** (HD); 2021 **liver, pancreas, kidney, testis, ovary** at P17 and 9 months |
| **Open question** | **Did the vector arrive in the periphery and fail to express, or did it never arrive?** |
| **Minimal follow-up** | Run the programme's own qPCR on DNA from those already-harvested peripheral tissues, same plate design, with the `KO+RI` and `WT+RI` (vehicle) arms as **matrix-matched vector-free blanks** |
| **New animals?** | 🟢 **Potentially none** — conditional on material retention (§3) |
| **Ladder level** | **L1** — new analysis on stored material |
| **Decision value** | Directly tests whether *"CNS-restricted rescue"* is a **delivery** fact or an **expression** fact |

---

## 2 · The scientific gap it closes

The peripheral negative on record is a **protein** negative. Vector genomes were **never quantified
outside four brain regions** in either study. So the inference —

> *the vector is not in the periphery, therefore anything that changes there changes through the
> brain*

— is drawn from an **expression assay**, and it sits beside a measured fact that **WWOX protein IS
present in sciatic nerve and spinal cord**.

🔴 **And that positive is itself not evidence of local transduction.** WWOX protein in sciatic nerve
is **fully explicable by axonal transport from a transduced central or DRG neuron**, with no local
transduction at all. That is precisely why a *genome* measurement is informative rather than
confirmatory: it is the only measurement that separates arrival from output.

---

## 3 · 🔴 The one unknown that gates the whole thing

**Whether DNA-bearing material was retained.** This repository cannot establish it and **does not
guess**. It is `HUMAN_REQUIRED`, and only the holding laboratory can answer it.

Two bounds that are established:
- the 2026 set is the right archive — a DNA-extraction + qPCR workflow **demonstrably existed in
  that lab for that paper**, and the ATL-lysis protocol is tissue-generic (25 mg is a mass limit,
  not a tissue restriction);
- 🔴 the **2021 archive is image-only** — its Methods heading list contains no immunoblot and no
  tissue-extraction section at all. That route is parked, not proposed.

---

## 4 · What the assay needs before it can carry a negative

The published assay is reusable as a **relative** measure. It has **no host reference amplicon, no
standard curve, no absolute-copy units**. To answer this question it needs three additions, and
they are what make this `L1` rather than `L0`:

1. a **single-copy nuclear** normaliser — 🔴 **not `Gapdh` or `Actb`** (mouse processed pseudogenes
   inflate a DNA-template reading), and never rRNA or mitochondrial targets;
2. a **standard curve**, without which there is no LOD and **a negative is uninterpretable**;
3. a **spiked-matrix recovery control per tissue**, because extraction efficiency differs by matrix.

⚠️ Also unrecorded and worth resolving before the plate is run: **what the amplicon targets.** The
titration assay's bGH primers are a *different experiment* and must not be assumed to be the tissue
target. Cycling conditions, chemistry, replicates and `n` are `METHODS_INVISIBLE` here.

---

## 5 · The four outcomes, and what each does NOT license

| Outcome | What it licenses | What it does **not** |
|---|---|---|
| **Genomes ABSENT** | strengthens CNS-restricted delivery; the central-control reading of the glucose rescue stands on firmer ground | 🔴 "absent at P30" ≠ "never arrived" — **episomal genomes dilute with cell division**, the same argument this programme already applies to cerebellar granule precursors |
| **Genomes PRESENT + protein ABSENT** | reclassifies the peripheral negative as an **expression/output** phenomenon; CNS-exclusivity must be re-derived | does not say **which cells** hold them — genome presence assigns nothing to a cell type |
| **Genomes PRESENT + protein PRESENT** | forces re-evaluation of the CNS-only rescue interpretation | does not establish that peripheral expression is *doing* anything |
| **MATERIAL NOT AVAILABLE** | park with revival triggers | is not a negative result |

🔴 **The asymmetry that decides how to read the plate:** residual blood or plasma vector in a tissue
biases **only toward a false positive**. Therefore **ABSENT is robust and PRESENT is not** — a
positive needs the perfusion status resolved (stated in the source only for RNA: non-perfused).

---

## 6 · Three free things to do first, and the honest note about them

`L0`, zero cost, and they should precede any bench work:
- recover the 2026 supplementary **S6 at panel level** — the one residual way the answer may
  already be in print;
- read the **Fig. 5 caption** — settles whether *"normalized to WT levels"* scopes to vDNA;
- open **2021 Appendix S2B–C**.

🔴 **Stated plainly: none of these can answer the genome question.** They bound it. Only the qPCR
answers it.

---

## 7 · Where the cheaper option is genuinely not comparable

An `L2` alternative exists — vector-specific ISH / DNA-FISH on archived peripheral sections, where
a human transgene in a mouse host gives **zero endogenous background**. It is more expensive and it
should still be kept in view, because **it is the only route that assigns arrival to a cell type**.
The ladder says prefer the lower level *when information gain is comparable*. Here it is not.

---

## 8 · Framing

This extends the programme's own work using the programme's own assay. **Nothing here asserts that
the vector is or is not in the periphery** — the claim is that the measurement which would settle
it was never run, and that it is unusually cheap to run because the laboratory already built the
tool. If the material is gone, the finding is simply that the question needs one tube at a future
terminal bleed, not a new cohort.
