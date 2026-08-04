# Axis 3 — prompt for the blind reviewer

> Recorded so the measurement is auditable: a judgement whose question was not written down
> cannot be checked later. Copy the block below verbatim into a fresh session with no prior
> context from this project.
>
> **Deliberately absent:** who wrote which side, that two different systems were involved,
> the project's name, and the interpretive notes that mark three anchors as contract
> decisions in the operator's copy. Those notes steer, and steering is what this run is
> spending its independence to avoid.

---

```text
You are reviewing pairs of scientific assertions for semantic equivalence.

CONTEXT
Two independent readers were each given the same set of summary sentences about
WWOX (a human gene) from a curated research database. Each reader decomposed those
sentences into atomic assertions in their own words. I need to know, sentence by
sentence, whether the two readers ended up asserting the same things.

The two readers are labelled α and β. The labelling is randomised separately at
every anchor: α at anchor 3 is not the same reader as α at anchor 7. Do not try to
track a reader across anchors; judge each anchor on its own.

YOUR TASK
For each of the 11 anchors below, compare the α propositions with the β
propositions and assign every proposition one verdict:

  SAME       — the same fact, stated in different words
  SUBSUMED   — contained in a proposition on the other side that also says more
  SPLIT      — corresponds to two or more propositions on the other side, together
  DIFFERENT  — not the same assertion, whatever the surface similarity
  ABSENT     — no counterpart on the other side

Also record, per anchor, whether the SPLIT ITSELF agrees: did both readers cut the
sentence into the same number of assertions, regardless of wording?

TWO ERRORS TO AVOID, IN OPPOSITE DIRECTIONS
1. Near-identical wording is not agreement. "inhibits Tau phosphorylation" and
   "inhibits GSK3β-dependent Tau phosphorylation" differ by an attribution: the
   second says which kinase does it. Qualifiers, named controls, mutants, species,
   experimental systems and negations are part of the assertion.
2. Different wording is not disagreement. Two sentences may carry exactly the same
   fact with different word order, different verbs, or one naming a quantity the
   other omits without contradicting it.

When you are genuinely unsure, say UNSURE and state what would settle it. A wrong
confident verdict is worse than a marked uncertainty.

OUTPUT
A markdown table with columns: id | verdict | one-line justification.
Then a second table: anchor | split agrees (yes/no) | note.
Then the tally of each verdict.
No preamble.

═══════════════════════════════════════════════════════════════════════
ANCHOR 1
α1  WWOX directly binds GSK3β through its ADH/SDR domain, using the 388-407 region with L404 required for binding
α2  WWOX binding inhibits GSK3β kinase activity toward Tau
β1  WWOX amino acids 388-407 are required for the interaction with GSK3β

ANCHOR 2
α3  Loss of WWOX can be interpreted as de-repressing GSK3β by removing a direct physical inhibitor
β2  Reducing WWOX raises GSK3β output on Tau, consistent with de-repression rather than a level change

ANCHOR 3
α4  In Wwox-null mice GSK3β is elevated in cortex, hippocampus and cerebellum
α5  Lithium suppresses PTZ-induced seizure susceptibility in the Wwox-null mouse
β3  GSK3β abundance is elevated in cortex, hippocampus, and cerebellum of Wwox-null mice
β4  Lithium significantly suppresses PTZ-induced seizure susceptibility in Wwox-null mice

ANCHOR 4
α6  WW2 pre-orders and stabilizes the otherwise unstable WW1 domain
α7  WW2 can directly engage a second PPxY motif when a dual-motif peptide presents a compatible sequence, spacing, linker, and orientation
β5  WW2 engages a second PPxY motif directly when sequence, spacing, linker and orientation create a compatible topology

ANCHOR 5
α8  The largest direct WW2 contribution was observed with engineered tandem peptides using a short polyglycine linker
α9  Native ErbB4 PY1PY2 gains tandem-domain affinity but binds predominantly through WW1, with only very weak apparent WW2 affinity
β6  The strongest direct WW2 engagement requires a short engineered linker; the native ErbB4 PY1PY2 linker gives a weaker interaction

ANCHOR 6
α10 Isolated WWOX WW2 has no measurable binding to a single PPxY peptide
α11 WW2 stabilizes the otherwise unstable WW1 domain within the WWOX tandem WW1-WW2 construct
β7  WW2 lacks significant inherent affinity for the ErbB4 PY3 motif, yet the tandem domain binds PY3 more strongly than isolated WW1 (30 vs 78 uM)
β8  WW2 stabilises the otherwise unstable WW1 domain

ANCHOR 7
α12 WWOX amino acids 388-407 are required for the interaction with GSK3β
α13 WWOX 388-412 contains the FXXXLI/VXRLE motif conserved in GSKIP, Axin and FRAT
α14 L404 is strictly required for the WWOX-GSK3β interaction
β9  WWOX binds GSK3β through its ADH/SDR domain
β10 WWOX residues 388-407 are required for binding GSK3β and are similar to Axin/FRAT/GSKIP GSK3β-binding motifs
β11 WWOX L404 is required for GSK3β binding, whereas the nearby L311 control is not

ANCHOR 8
α15 WT WWOX, but not L404A, inhibits GSK3β-dependent Tau phosphorylation at S396 and S404 without affecting S422
α16 WT WWOX, but not GSK3β-binding-deficient L404A, restores Tau-dependent microtubule assembly impaired by GSK3β
α17 WT WWOX promotes RA-induced neurite outgrowth in SH-SY5Y cells, and the effect is abolished by L404A
β12 WWOX inhibits Tau phosphorylation at S396 and S404 but not at the MKK4 site S422

ANCHOR 9
α18 Endogenous WWOX and GSK3β reciprocally co-immunoprecipitate from mouse brain extract
β13 The WWOX-GSK3β interaction is detectable between endogenous proteins in mouse brain

ANCHOR 10
α19 During RA-induced SH-SY5Y differentiation, phospho-GSK3β S9 remains unchanged while WWOX rises and Tau S396/S404 phosphorylation falls
β14 Phospho-GSK3β-S9 is unchanged while GSK3β output falls

ANCHOR 11
α20 Tau knockdown abolishes the neurite-outgrowth increase caused by either WWOX overexpression or GSK3β knockdown
α21 WWOX overexpression and GSK3β knockdown are non-additive, supporting a linear WWOX-GSK3β-Tau pathway with Tau as effector
β15 Tau knockdown abolishes the WWOX effect, and WWOX with siRNA-GSK3β is non-additive
β16 WWOX, GSK3β and Tau lie on one linear pathway with Tau as the effector
═══════════════════════════════════════════════════════════════════════
```

---

## Notes for whoever runs it

- **Fresh session, no memory, no project files.** The block is self-contained by design:
  a reviewer with repository access could find the key.
- **Do not answer follow-up questions about the sides.** If it asks which reader is which,
  say the labelling is randomised per anchor and cannot be tracked — that is true.
- **Keep the raw reply.** Paste it back unedited; the tally can be recomputed, the
  justifications cannot be reconstructed.
- The reviewer is told it may answer `UNSURE`. Expect some, and treat them as findings:
  an anchor two readers cannot resolve is an anchor the contract under-determines.

## Related

[`dismech_axis3_review_sheet_blinded.md`](dismech_axis3_review_sheet_blinded.md) · [`dismech_axis3_review_sheet.md`](dismech_axis3_review_sheet.md) · [`dismech_independent_comparison_rev13.md`](dismech_independent_comparison_rev13.md)
