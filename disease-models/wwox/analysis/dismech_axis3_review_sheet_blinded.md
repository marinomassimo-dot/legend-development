# Axis 3 — blinded review sheet

> **Non-canonical. This is the measurement.** The comparator can say two propositions are
> not textually equal. It cannot say whether they mean the same thing, and axis 3 is
> entirely that judgement.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Status:** AWAITING REVIEW
**Sides:** `α` and `β`, **shuffled independently at every anchor** (seed `20260804`)
**Key:** `data/dismech_axis3_blinding_key.json` — **do not open it before reviewing**
**Scope:** 11 anchors · 37 propositions

---

## Why the sides are hidden

One side was authored by the reference derivation, the other by the independent run. Both
authors would tend to read their own wording as equivalent — the bias runs toward `SAME`,
which is exactly the direction that would let an inadequate atomization contract pass. The
labels are hidden so that reflex has nothing to attach to.

**The shuffle is per anchor.** Recognising a side at anchor 6 tells you nothing about
anchor 3: `α` does not mean the same author twice.

## What was normalised, and what still shows

Only transformations already declared non-semantic in canonicalisation v1 were applied:
Unicode NFC, whitespace, dash unification, the `GSK3beta → GSK3β` alias family, and a
trailing full stop. **Nothing else was touched** — normalising further would erase the
wording differences this sheet exists to judge.

So the blinding is partial, and pretending otherwise would be worse than declaring it:

| Residual tell | Where |
|---|---|
| `stabilises` vs `stabilizes` | anchor 6, both present |
| `uM` written out | anchor 6 |
| One side consistently names the experimental system and the mutant control — *"WT WWOX, but not L404A"*, *"in SH-SY5Y cells"*, *"During RA-induced…"* | anchors 8, 10, 11 |

If you notice which side is which, say so in the note rather than pretending you did not.
A verdict reached knowing the authorship is still worth having — it is just worth knowing
that you knew.

## How to fill this in

For each anchor, decide **per proposition on one side** what happened to it on the other.

| Verdict | Meaning |
|---|---|
| `SAME` | Both say the same fact. Wording differs; the assertion does not |
| `SUBSUMED` | One statement is contained in another that also says more |
| `SPLIT` | One statement corresponds to two or more on the other side, taken together |
| `DIFFERENT` | Not the same assertion, whatever the surface similarity |
| `ABSENT` | No counterpart at this anchor |

Also record whether the **split** agrees — same number of assertions from the same
sentence — independently of wording.

**Two traps, in opposite directions.** Near-identical wording is not agreement: *inhibits
Tau phosphorylation* and *inhibits GSK3β-dependent Tau phosphorylation* differ by an
attribution. And different wording is not disagreement: two sentences can carry the same
fact with different word order.

---

## 1 · CLAIM 016 | Meccanismo aggiunto | sent[0]

| | proposition | verdict |
|---|---|---|
| α1 | WWOX directly binds GSK3β through its ADH/SDR domain, using the 388-407 region with L404 required for binding | |
| α2 | WWOX binding inhibits GSK3β kinase activity toward Tau | |
| β1 | WWOX amino acids 388-407 are required for the interaction with GSK3β | |

split agrees: ☐ yes ☐ no · note:

## 2 · CLAIM 016 | Meccanismo aggiunto | sent[1]

| | proposition | verdict |
|---|---|---|
| α3 | Loss of WWOX can be interpreted as de-repressing GSK3β by removing a direct physical inhibitor | |
| β2 | Reducing WWOX raises GSK3β output on Tau, consistent with de-repression rather than a level change | |

split agrees: ☐ yes ☐ no · note:

## 3 · CLAIM 016 | Summary | sent[0]

| | proposition | verdict |
|---|---|---|
| α4 | In Wwox-null mice GSK3β is elevated in cortex, hippocampus and cerebellum | |
| α5 | Lithium suppresses PTZ-induced seizure susceptibility in the Wwox-null mouse | |
| β3 | GSK3β abundance is elevated in cortex, hippocampus, and cerebellum of Wwox-null mice | |
| β4 | Lithium significantly suppresses PTZ-induced seizure susceptibility in Wwox-null mice | |

split agrees: ☐ yes ☐ no · note:

## 4 · CLAIM 024 | Precisazione meccanicistica | sent[0]

| | proposition | verdict |
|---|---|---|
| α6 | WW2 pre-orders and stabilizes the otherwise unstable WW1 domain | |
| α7 | WW2 can directly engage a second PPxY motif when a dual-motif peptide presents a compatible sequence, spacing, linker, and orientation | |
| β5 | WW2 engages a second PPxY motif directly when sequence, spacing, linker and orientation create a compatible topology | |

split agrees: ☐ yes ☐ no · note:

## 5 · CLAIM 024 | Precisazione meccanicistica | sent[1]

| | proposition | verdict |
|---|---|---|
| α8 | The largest direct WW2 contribution was observed with engineered tandem peptides using a short polyglycine linker | |
| α9 | Native ErbB4 PY1PY2 gains tandem-domain affinity but binds predominantly through WW1, with only very weak apparent WW2 affinity | |
| β6 | The strongest direct WW2 engagement requires a short engineered linker; the native ErbB4 PY1PY2 linker gives a weaker interaction | |

split agrees: ☐ yes ☐ no · note:

## 6 · CLAIM 024 | Summary | sent[0]

| | proposition | verdict |
|---|---|---|
| α10 | Isolated WWOX WW2 has no measurable binding to a single PPxY peptide | |
| α11 | WW2 stabilizes the otherwise unstable WW1 domain within the WWOX tandem WW1-WW2 construct | |
| β7 | WW2 lacks significant inherent affinity for the ErbB4 PY3 motif, yet the tandem domain binds PY3 more strongly than isolated WW1 (30 vs 78 uM) | |
| β8 | WW2 stabilises the otherwise unstable WW1 domain | |

split agrees: ☐ yes ☐ no · note:

## 7 · CLAIM 035 | Summary | sent[0]

> ⚠️ **This one is a contract decision, not only a reading.** One side separates the
> experimentally required segment from the sequence-homologous one; the other merges them.
> That distinction was recovered from the source because the registry had blurred it.
> Judging it `SUBSUMED` says the merge is acceptable.

| | proposition | verdict |
|---|---|---|
| α12 | WWOX amino acids 388-407 are required for the interaction with GSK3β | |
| α13 | WWOX 388-412 contains the FXXXLI/VXRLE motif conserved in GSKIP, Axin and FRAT | |
| α14 | L404 is strictly required for the WWOX-GSK3β interaction | |
| β9 | WWOX binds GSK3β through its ADH/SDR domain | |
| β10 | WWOX residues 388-407 are required for binding GSK3β and are similar to Axin/FRAT/GSKIP GSK3β-binding motifs | |
| β11 | WWOX L404 is required for GSK3β binding, whereas the nearby L311 control is not | |

split agrees: ☐ yes ☐ no · note:

## 8 · CLAIM 035 | Summary | sent[1]

> ⚠️ Watch the attribution: one side says *Tau phosphorylation*, the other *GSK3β-dependent
> Tau phosphorylation*, and conditions the effect on a mutant.

| | proposition | verdict |
|---|---|---|
| α15 | WT WWOX, but not L404A, inhibits GSK3β-dependent Tau phosphorylation at S396 and S404 without affecting S422 | |
| α16 | WT WWOX, but not GSK3β-binding-deficient L404A, restores Tau-dependent microtubule assembly impaired by GSK3β | |
| α17 | WT WWOX promotes RA-induced neurite outgrowth in SH-SY5Y cells, and the effect is abolished by L404A | |
| β12 | WWOX inhibits Tau phosphorylation at S396 and S404 but not at the MKK4 site S422 | |

split agrees: ☐ yes ☐ no · note:

## 9 · CLAIM 035 | Summary | sent[2]

| | proposition | verdict |
|---|---|---|
| α18 | Endogenous WWOX and GSK3β reciprocally co-immunoprecipitate from mouse brain extract | |
| β13 | The WWOX-GSK3β interaction is detectable between endogenous proteins in mouse brain | |

split agrees: ☐ yes ☐ no · note:

## 10 · CLAIM 035 | Summary | sent[3]

> ⚠️ One side names the experimental setting; the other does not. Decide whether that
> changes what is asserted.

| | proposition | verdict |
|---|---|---|
| α19 | During RA-induced SH-SY5Y differentiation, phospho-GSK3β S9 remains unchanged while WWOX rises and Tau S396/S404 phosphorylation falls | |
| β14 | Phospho-GSK3β-S9 is unchanged while GSK3β output falls | |

split agrees: ☐ yes ☐ no · note:

## 11 · CLAIM 035 | Summary | sent[4]

| | proposition | verdict |
|---|---|---|
| α20 | Tau knockdown abolishes the neurite-outgrowth increase caused by either WWOX overexpression or GSK3β knockdown | |
| α21 | WWOX overexpression and GSK3β knockdown are non-additive, supporting a linear WWOX-GSK3β-Tau pathway with Tau as effector | |
| β15 | Tau knockdown abolishes the WWOX effect, and WWOX with siRNA-GSK3β is non-additive | |
| β16 | WWOX, GSK3β and Tau lie on one linear pathway with Tau as the effector | |

split agrees: ☐ yes ☐ no · note:

---

## Tally, when done

| | count |
|---|---:|
| `SAME` | |
| `SUBSUMED` | |
| `SPLIT` | |
| `DIFFERENT` | |
| `ABSENT` | |
| anchors where the split agrees | / 11 |

## What the answer decides

- **Mostly `SAME`** → the atomization contract holds; only the *form* of a proposition is
  unspecified, and a phrasing rule closes it.
- **Mostly `DIFFERENT` or `SPLIT`** → the contract genuinely under-determines what an
  assertion is. A much larger repair.

Disagreement between two independent reviewers of this sheet is itself the result: it
localises where the contract is ambiguous by construction.

## Related

[`dismech_axis3_review_sheet.md`](dismech_axis3_review_sheet.md) (unblinded) · [`dismech_independent_comparison_rev13.md`](dismech_independent_comparison_rev13.md) · [`dismech_blind_derivation_contract.md`](dismech_blind_derivation_contract.md)
