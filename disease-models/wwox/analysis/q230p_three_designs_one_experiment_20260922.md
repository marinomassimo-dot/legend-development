# Three independent designs converged on one experiment that has already been run once

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Class:** `DISCOVERY` — non-canonical, not
proposed for `BATCH_COMMIT`. Nothing here is medical advice.

---

## §1 · The convergence

Three files written today, by three actors who did not read each other, arrive at the same bench
step from three directions:

| Origin | What it asks for | Why |
|---|---|---|
| `q230p_direct_discriminator_20260922.md` (Scientist I) | a mechanism matrix over **`A`** attainable abundance, **`S`** insoluble fraction, **`dS/dA`**, engagement per molecule, under a lever panel | to separate `M1` degradation · `M1′` synthesis/co-translational triage · `M2` insolubility · `M3a` folded-and-inert · `M3b` soluble-unfolded-and-inert |
| `q230p_pharmacological_precedents_20260922.md` (Scientist K) | *"one blot, two lanes, one SDS-soluble / pellet split"* on `Q230P` fibroblasts | to decide whether the chaperone precedent set applies at all |
| **`DL-MECH-029`**, in the discovery ledger since 2026-07 | *"Western/qRT-PCR allele-specific + nascent-synthesis pulse-labelling + soluble/insoluble fractionation + pulse-chase"* | because Johannsen 2018 left `cause ∈ {impaired_translation, insolubility, premature_degradation}` **undiscriminated** |

🔴 **The convergence is not the finding. This is:**

> **The experiment has already been performed once, and its result is the reason all three designs
> exist.** Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, Schirmer MA, Denecke J, Santer R,
> *Neurogenetics* 2018;19(3):151–156 (PMID 29808465,
> [DOI](https://doi.org/10.1007/s10048-018-0549-5)) measured, in donor-derived fibroblasts from two
> sisters homozygous at Gln230: **normal WWOX transcript by qRT-PCR, and no detectable WWOX protein
> by Western blot.** The authors wrote *"impaired translation or premature degradation."*

Neither Scientist I's nor Scientist K's file names that paper. Both were proposing a **first**
measurement of something that has a **published prior measurement** — and the prior measurement is
the one whose ambiguity they are trying to resolve. That changes the framing of both designs from
*"measure whether Q230P protein exists"* to **"re-run a published negative under conditions that can
tell three mechanisms apart."** The second is a much easier experiment to justify and a much harder
one to get wrong.

## §2 · 🔴 Why the published negative cannot settle it — and the one line of Methods that decides

The ledger already records, correctly, that *"«absence» at Western blot is a sensitivity limit, not
an absolute zero"*, and that protein stability may be tissue-specific. **There is a second, sharper
reason that the ledger does not state:**

> A Western blot reading "absent" is a statement about the **lysate that was loaded**, not about
> the cell. An aggregation-prone variant partitions into the insoluble pellet. A mild
> non-denaturing lysis buffer discards that pellet **before** the gel is loaded. Under those
> conditions "absent" means *absent from the soluble fraction*, and the protein may be entirely
> present.

So `M2` (insolubility) and `M1` (degradation) are **distinguishable only by the lysis buffer**, and
the authors' own disjunction — *"impaired translation or premature degradation"* — **omits
insolubility from the list of candidates**, which is precisely the mechanism a mild buffer would
hide. The ledger's `cause ∈ {…}` set is the more careful statement and should be preferred to the
authors' pair.

## §3 · Retrieval attempted and failed, with the boundary recorded

The paper's Methods are the single line that would resolve §2. Two routes tried today:

1. **PMC / PubMed full text** — Springer-closed, no PMCID. Already recorded as parked.
2. **`Scholar_Gateway semanticSearch`** — the publisher-side route that has twice in this session
   recovered text PMC could not serve (superscripts preserved as `^…^`, figure legends retained).
   A well-formed natural-language query naming the sisters, the homozygous Gln230 missense, the
   normal qRT-PCR and the absent Western returned **eight on-topic WWOX-DEE records and not this
   one**.

⚠️ **What that licenses, and what it does not.** It licenses: *this record is not in that corpus,
although WWOX-DEE literature is.* It does **not** license *"the gateway does not carry Springer"* —
that is a hypothesis about the corpus boundary from a single probe, and the returned set was mixed
(Wiley, John Libbey, Elsevier DOIs), so the boundary is not a clean publisher split. Recorded as
`IPOTESI`, not as a routing rule.

**The Methods of PMID 29808465 stay `PREMISE: METHODS_INVISIBLE`.** `REVIVAL_TRIGGER`: any Springer
route, an author-hosted copy, or a later paper quoting Johannsen's buffer.

## §4 · What this changes about the three designs — and what it does not

**Changes:**
- Both new designs should be written as **re-runs with discriminating readouts**, citing Johannsen
  2018 as the prior, not as first measurements.
- The **minimum** addition to the published protocol is small and fully specified: load a
  **denaturing whole-cell lysate** and keep the **pellet**, rather than a cleared soluble lysate
  alone. If the original used a denaturing buffer, that step is free and the result already
  excludes `M2` — which is why the buffer line is worth chasing before designing anything.
- The **permissive-temperature arm (26–30 °C)** proposed in the orchestrator verification of
  Scientist K's file gains a second justification: it is the arm Atanasov 2007 actually used on
  11β-HSD2 `Y338H`, and it separates foldable-but-unstable from fold-incompetent, which the
  soluble/pellet split alone does not.

**Does not change:**
- 🔴 The assumption flagged in `DL-MECH-029` is untouched and remains the binding one: **that
  `Q230P` protein, once restabilised, would be catalytically and functionally active.** Johannsen
  does not test it and neither would any of the three designs. Stability or solubility rescue is
  **not** a surrogate for functional rescue. Lou 2018 supplies an adverse prior for the SDR fold;
  Atanasov 2007 supplies a favourable one for a stability-class lesion. `Q230P`'s class is
  unmeasured, which is the whole point.
- 🔴 A fibroblast is not a neuron. Every statement above is about donor-derived fibroblasts.
- 🔴 `Q230G` remains excluded as a discriminator: glycine removes the side chain **and** adds
  backbone flexibility, perturbing two variables at once.
- The `null/missense` versus *functionally* `null/null` inference for the reference genotype is
  **not** re-opened or strengthened here. It rests on the same published negative, and if that
  negative cannot exclude insolubility the inference is weaker, not stronger. Adjudicating by how
  much is a separate census and is not attempted in this file.

## §5 · Method note

This file exists because of a check that cost one `grep`: **before endorsing a delegate's "first
measurement", ask the repository whether a measurement already exists.** Two independent delegates,
both careful, both grading themselves conservatively, both proposed as novel an experiment whose
prior sits in the discovery ledger under a heading that names the allele. Neither was wrong about
the science. Both were wrong about the baseline — the same defect class recorded this morning in
`recursive_reread_repudi2021_20260922.md` §5.4, now observed a second time, in a different actor
and a different file.

`enumerate_baseline_before_scoring` has now been **observed to fail twice and to succeed zero
times**, which is the strongest evidence on the scorecard for adding it — and the reason its
candidate status stays 🟠 until it has been run deliberately rather than reconstructed from its
own absence.
