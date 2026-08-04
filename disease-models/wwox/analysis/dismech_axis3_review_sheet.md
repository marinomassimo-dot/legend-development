# Axis 3 — human review sheet

> **Non-canonical. This is the measurement.** The comparator can tell you that two
> propositions are not textually equal. It cannot tell you whether they say the same
> thing. That judgement is the whole of axis 3, and no tool in this repository is allowed
> to make it.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Status:** AWAITING REVIEW
**Inputs:** reference sidecar (`A`) vs realigned independent derivation (`B`)
**Scope:** 11 shared anchors · 16 `A` propositions · 21 `B` propositions

---

## How to fill this in

For each anchor, decide **per `A` proposition** what happened to it on the `B` side, and
write the verdict in the `verdict` column.

| Verdict | Meaning |
|---|---|
| `SAME` | Both say the same fact. Wording differs; the assertion does not |
| `SUBSUMED` | The `A` statement is contained in a `B` statement that also says more |
| `SPLIT` | `A` corresponds to two or more `B` statements taken together |
| `DIFFERENT` | Not the same assertion, whatever the surface similarity |
| `ABSENT` | No `B` counterpart at this anchor |

And note, per anchor, whether the **split** itself agrees — same number of assertions from
the same sentence — independently of wording.

**Two things to resist.** Do not count near-identical wording as agreement without reading
both: *inhibits Tau phosphorylation* and *inhibits GSK3β-dependent Tau phosphorylation*
differ by an attribution. And do not count different wording as disagreement: `A6` and `B6`
below are the same fact in different words, and calling that a divergence would be as wrong
as the comparator calling it one.

**What the answer is for.** If most pairs are `SAME`, the atomization contract is adequate
and only the *form* of a proposition is unspecified — a phrasing rule would close it. If
most are `DIFFERENT` or `SPLIT`, the contract genuinely under-determines what an assertion
is, and that is a much larger repair.

---

## 1 · CLAIM 016 | Meccanismo aggiunto (BATCH_20260726_001) | sent[0] — 1 vs 2

| | proposition | verdict |
|---|---|---|
| A1 | WWOX amino acids 388-407 are required for the interaction with GSK3beta | |
| B1 | WWOX directly binds GSK3β through its ADH/SDR domain, using the 388–407 region with L404 required for binding. | |
| B2 | WWOX binding inhibits GSK3β kinase activity toward Tau. | |

split agrees: ☐ yes ☐ no · note:

## 2 · CLAIM 016 | Meccanismo aggiunto | sent[1] — 1 vs 1

| | proposition | verdict |
|---|---|---|
| A2 | Reducing WWOX raises GSK3beta output on Tau, consistent with de-repression rather than a level change | |
| B3 | Loss of WWOX can be interpreted as de-repressing GSK3β by removing a direct physical inhibitor. | |

split agrees: ☐ yes ☐ no · note:

## 3 · CLAIM 016 | Summary | sent[0] — 2 vs 2

| | proposition | verdict |
|---|---|---|
| A3 | In Wwox-null mice GSK3beta is elevated in cortex, hippocampus and cerebellum | |
| A4 | Lithium suppresses PTZ-induced seizure susceptibility in the Wwox-null mouse | |
| B4 | GSK3β abundance is elevated in cortex, hippocampus, and cerebellum of Wwox-null mice. | |
| B5 | Lithium significantly suppresses PTZ-induced seizure susceptibility in Wwox-null mice. | |

split agrees: ☐ yes ☐ no · note:

## 4 · CLAIM 024 | Precisazione meccanicistica | sent[0] — 1 vs 2

| | proposition | verdict |
|---|---|---|
| A5 | WW2 engages a second PPxY motif directly when sequence, spacing, linker and orientation create a compatible topology | |
| B6 | WW2 pre-orders and stabilizes the otherwise unstable WW1 domain. | |
| B7 | WW2 can directly engage a second PPxY motif when a dual-motif peptide presents a compatible sequence, spacing, linker, and orientation. | |

split agrees: ☐ yes ☐ no · note:

## 5 · CLAIM 024 | Precisazione meccanicistica | sent[1] — 1 vs 2

| | proposition | verdict |
|---|---|---|
| A6 | The strongest direct WW2 engagement requires a short engineered linker; the native ErbB4 PY1PY2 linker gives a weaker interaction | |
| B8 | The largest direct WW2 contribution was observed with engineered tandem peptides using a short polyglycine linker. | |
| B9 | Native ErbB4 PY1PY2 gains tandem-domain affinity but binds predominantly through WW1, with only very weak apparent WW2 affinity. | |

split agrees: ☐ yes ☐ no · note:

## 6 · CLAIM 024 | Summary | sent[0] — 2 vs 2

| | proposition | verdict |
|---|---|---|
| A7 | WW2 lacks significant inherent affinity for the ErbB4 PY3 motif, yet the tandem domain binds PY3 more strongly than isolated WW1 (30 vs 78 uM) | |
| A8 | WW2 stabilises the otherwise unstable WW1 domain | |
| B10 | Isolated WWOX WW2 has no measurable binding to a single PPxY peptide. | |
| B11 | WW2 stabilizes the otherwise unstable WW1 domain within the WWOX tandem WW1–WW2 construct. | |

split agrees: ☐ yes ☐ no · note:

## 7 · CLAIM 035 | Summary | sent[0] — 3 vs 3

| | proposition | verdict |
|---|---|---|
| A9 | WWOX amino acids 388-407 are required for the interaction with GSK3beta | |
| A10 | WWOX 388-412 contains the FXXXLI/VXRLE motif conserved in GSKIP, Axin and FRAT | |
| A11 | L404 is strictly required for the WWOX-GSK3beta interaction | |
| B12 | WWOX binds GSK3β through its ADH/SDR domain. | |
| B13 | WWOX residues 388–407 are required for binding GSK3β and are similar to Axin/FRAT/GSKIP GSK3β-binding motifs. | |
| B14 | WWOX L404 is required for GSK3β binding, whereas the nearby L311 control is not. | |

split agrees: ☐ yes ☐ no · note: *(A distinguishes 388–407 required from 388–412 homologous; B merges them into B13 — the distinction rev. 3 recovered from the source)*

## 8 · CLAIM 035 | Summary | sent[1] — 1 vs 3

| | proposition | verdict |
|---|---|---|
| A12 | WWOX inhibits Tau phosphorylation at S396 and S404 but not at the MKK4 site S422 | |
| B15 | WT WWOX, but not L404A, inhibits GSK3β-dependent Tau phosphorylation at S396 and S404 without affecting S422. | |
| B16 | WT WWOX, but not GSK3β-binding-deficient L404A, restores Tau-dependent microtubule assembly impaired by GSK3β. | |
| B17 | WT WWOX promotes RA-induced neurite outgrowth in SH-SY5Y cells, and the effect is abolished by L404A. | |

split agrees: ☐ yes ☐ no · note:

## 9 · CLAIM 035 | Summary | sent[2] — 1 vs 1

| | proposition | verdict |
|---|---|---|
| A13 | The WWOX-GSK3beta interaction is detectable between endogenous proteins in mouse brain | |
| B18 | Endogenous WWOX and GSK3β reciprocally co-immunoprecipitate from mouse brain extract. | |

split agrees: ☐ yes ☐ no · note:

## 10 · CLAIM 035 | Summary | sent[3] — 1 vs 1

| | proposition | verdict |
|---|---|---|
| A14 | Phospho-GSK3beta-S9 is unchanged while GSK3beta output falls | |
| B19 | During RA-induced SH-SY5Y differentiation, phospho-GSK3β S9 remains unchanged while WWOX rises and Tau S396/S404 phosphorylation falls. | |

split agrees: ☐ yes ☐ no · note: *(B names the experimental setting; A does not — see whether that changes what is asserted)*

## 11 · CLAIM 035 | Summary | sent[4] — 2 vs 2

| | proposition | verdict |
|---|---|---|
| A15 | Tau knockdown abolishes the WWOX effect, and WWOX with siRNA-GSK3beta is non-additive | |
| A16 | WWOX, GSK3beta and Tau lie on one linear pathway with Tau as the effector | |
| B20 | Tau knockdown abolishes the neurite-outgrowth increase caused by either WWOX overexpression or GSK3β knockdown. | |
| B21 | WWOX overexpression and GSK3β knockdown are non-additive, supporting a linear WWOX–GSK3β–Tau pathway with Tau as effector. | |

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

## Related

[`dismech_independent_comparison_rev13.md`](dismech_independent_comparison_rev13.md) · [`dismech_independent_derivation_design.md`](dismech_independent_derivation_design.md) · [`dismech_blind_derivation_contract.md`](dismech_blind_derivation_contract.md)
