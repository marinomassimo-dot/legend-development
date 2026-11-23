# ADV-199 frozen card (SCI): the one card assembled from Codex's proposal, frozen BEFORE any hand scoring (feasibility only; no engine has seen it; not medical advice; nothing WWOX-specific)

frozen_at: 2026-11-23T17:17Z. Honest order: the source (Methods, Results, Discussion, Tables 1 and 2, Figures 3 to 6, erratum) was read BEFORE this file, because the assignment asks whether a card can be built from it; what is frozen here is the card, its reference label and the scorers, before any scorer was applied. The pre-registration (commit 46b09c8cd) preceded the body.

## Visible card (what an engine would see; identifiers, values and units masked)
Question: "A variant of a chloride-extruding membrane transporter shows faster chloride extrusion than the wild type when chloride is loaded into the cell. Which evidence, from the same study, would best show whether the faster extrusion reflects more transporter at the plasma membrane or faster transport per transporter?"
* K1: the direct functional readout alone (the somatodendritic reversal-potential gradient under imposed chloride load, variant versus wild type, in cultured neurons).
* K2: a surface-labelling ratio alone (surface signal divided by total signal, variant versus wild type, in cultured neurons).
* K3: the functional readout of K1 paired with the surface ratio of K2, variant versus wild type.
* K4: the heterologous-cell fluorescent flux assay (blocker-sensitive), variant versus wild type.
* K5: abstain: the study measures neither the absolute amount at the membrane nor transport per molecule.

## Analyst-side reference (kept out of the card)
Reported: variant C1 versus WT. Surface ratio (Fig 5C, cortical neurons): "no difference" (box spans about 0.4 to 1.9 on a log axis, whiskers about 0.25 to 4.5, about 8 to 9 points). Gradient (Fig 6E): 17.9 +/- 0.5 mV against WT 8.0 +/- 1.4 mV (about 3 points for C1, visual). The paper's own inference (Results 3.6): "suggests that the C1 mutation induces a CTD conformation that promotes enhanced kinetics of Cl- extrusion".
Reference label under the source: **K5 (abstain)**, for the reasons in the result file; the alternative label proposed by Codex is **K3**. Both are scored below.

## Scorers (fixed)
* R1: always pick the direct functional readout (K1).
* R2: the textbook rule "to separate abundance from activity pair a surface measure with an activity measure" (K3).
* G: IT's endpoint-fidelity gate (does the chosen option state a comparator, population and endpoint checkable against the card).
* N1: always the first listed option (K1). N2: always abstain (K5).

## Masking budget (what can go and what cannot)
Can be removed without changing the evidence: gene and variant names, species, culture ages, millivolt and fold values, p values, the blocker name. Cannot be removed: that the functional readout is measured in neurons under imposed chloride load, that the surface assay is a ratio (surface over total) in neurons, and that a heterologous-cell flux assay exists; these ARE the options. Also cannot be removed if K5 is to be answerable: that the surface measure is a fraction, that the two neuronal readouts were taken in different culture preparations, and the point counts.
