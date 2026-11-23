# ADV-199 result (SCI): can one non-tautological matched card be assembled from the KCC2 transposon mutant library paper? (feasibility only; no engine, no model call, no spend; hypothesis level; nothing WWOX-specific; not medical advice)

result_at: 2026-11-23T17:17Z
task: ORCH-SCI-ADV065-DEEPEN-20261118, step 90 (assignment ADV-199, Codex REPLY_35)
pre-registration: `PREREG_ADV199_SCI_20261123.md` (commit 46b09c8cd, before the body was read). Frozen card: `FROZEN_CARD_ADV199_SCI_20261123.md`, sha256 eed46a7c1b99a7bef1ac0a29efbfd41a901781798f8540e7df391d1844d5ae71, frozen before any scorer was applied (after the source was read: the question is the feasibility of a card from this source).

## 0. Disposition: REJECTED (the proposed card, C1 against WT, transport versus abundance)
Stopper, in one sentence: whichever label the card carries, a one-line scorer reaches it (the textbook pairing rule if the label is the paired readout; always-abstain if the label is ABSTAIN), and the source cannot supply the matched second member that would break the tie, because the abundance and the function of C1 were measured in different neuronal preparations, with a surface FRACTION as the abundance metric and about 3 points for C1 in the functional panel.
A narrow within-assay fallback exists (section 6); it is not frozen and not assessed beyond one paragraph.

## 1. What I read, and the facts that decide it (Frontiers HTML, CC BY; Europe PMC isOpenAccess Y; PMC page not requested)
Read: Methods 2.1 to 2.8, Results 3.1 to 3.6, Discussion, Tables 1 and 2, Figures 1 to 6 (3 to 6 viewed as images), erratum. Not read: Introduction, abstract, Supplementary Figures (hasSuppl Y; not opened). The erratum corrects only the Figure 4 legend (it had duplicated the Figure 3 legend); nothing in the values used here depends on it.
**ADV's quoted values: all four confirmed.** B8 surface 2.96 +/- 1.16 of WT (p 0.027, one-sample Wilcoxon, Fig 5C); C1 and C11 "no difference" in membrane abundance (Fig 5C); delta E_GABA WT 8.0 +/- 1.4, B8 17.9 +/- 1.5, C1 17.9 +/- 0.5 mV (Results 3.6, Fig 6E).
**Corrections to the two proposals.** Codex is right that Fig 5 is in cortical neurons (not HEK293): the HEK293 assays are Figs 3 and 4. ADV's "HEK293 versus cortical neurons" therefore describes Fig 3 against Figs 5 and 6, not the pair Fig 5 against Fig 6. The pair that matters is Fig 5 against Fig 6, and that pair is unmatched in other ways.

| Quantity | Fig 5C surface (abundance) | Fig 6E gradient (function) |
|---|---|---|
| Preparation | rat cortical neurons, transfected DIV 6, labelled "two weeks after plating" (Methods 2.4), about 8 days of expression | "immature" DIV 3 neurons, transient transfection 24 h (Methods 2.6, Results 3.6); culture type **Methods 2.6 says hippocampal, Results 3.6 says cortical** |
| Metric | **ratio** surface/total FLAG per cell, normalised to WT ("the ratio of the two signals serves as a measure of the KCC2 plasmalemmal abundance") | somatic minus dendritic E_GABA under a 29 mM chloride pipette load |
| C1 | box about 0.4 to 1.9 (log axis), whiskers about 0.25 to 4.5, 8 to 9 points (visual); "no difference", never tested for equivalence | 17.9 +/- 0.5 mV, **about 3 points** (visual), p < 0.0001 against WT |
| B8 | about 2 (median) / 2.96 mean, p 0.027 | 17.9 +/- 1.5 mV, about 8 points |
| Expression readout in the same cells | yes (total) | **none reported** for the recorded neurons |

Three different neuronal preparations carry the three C1 readouts that Table 1, Fig 5 and Fig 6 report (permeabilised FLAG-ir at DIV 10 plus 48 h in Methods 2.3, the surface ratio, the gradient). None is matched to another.

## 2. Why the proposed question is not a measured contrast
1. **The abundance metric is a fraction, not an amount.** C1 total and dendritic FLAG-ir are graded +++ (Table 1), "highest for B8 and C1" (Results 3.2), and the C1 monomer band in the HEK blot (Fig 4A, not quantified, single blot) is visibly the strongest of the lanes. An unchanged surface fraction with a higher total could still mean more transporter at the membrane per cell. The paper never reports absolute surface density.
2. **The gradient does not scale with the surface metric.** B8 has about three times the WT surface fraction and the same gradient as C1 (17.9 mV each). With one readout flat across a threefold change of the other, the pairing cannot separate abundance from kinetics; a ceiling, or construct level at 24 h, is as consistent as per-molecule speed. The HEK slope also differs: C1 232 +/- 7 and B8 137 +/- 20 percent of WT (Table 2), yet equal gradients.
3. **A null is not equivalence** (Fig 5C spread above; the legend gives one-sample Wilcoxon only against 1).
4. **The authors' sentence is the label.** "WT KCC2 and the C1 mutant exhibit similar membrane expression levels but different Cl- extrusion capacities suggests that the C1 mutation induces a CTD conformation that promotes enhanced kinetics" (Results 3.6): an inference from the pairing above, not a measurement of transport per molecule.
5. **Internal inconsistencies a card would inherit:** hippocampal versus cortical (Methods 2.6 against Results 3.6); C11 is "highly mature" in Results 3.4 and "intermediate" in 3.5, and the Endo H panel (Fig 4C) shows only A7, A8, B1, B8, C1 and WT, so C11's maturity rests on the band position in Fig 4A.

## 3. The hand test (paper only; scorers fixed in the frozen file)
Labels scored both ways: K5 (abstain, my reading) and K3 (Codex's informative pairing).
| Scorer | Picks | against K5 | against K3 |
|---|---|---|---|
| R1 always the direct functional readout | K1 | MISMATCH | MISMATCH |
| R2 textbook rule, pair surface with function | K3 | MISMATCH | **MATCH, card saturated** |
| G endpoint-fidelity gate | passes K1 to K4 (each states comparator, population, endpoint) | cannot see the label | cannot see the label |
| N1 first listed option | K1 | MISMATCH | MISMATCH |
| N2 always abstain | K5 | **MATCH, card saturated** | MISMATCH |
So R1 and N1 do not saturate (the first named reject rule does not fire), but R2 or N2 does, whichever label is chosen. G is a conformance check and, as in ADV-197, discriminates nothing here.
**Visible prompt gives the answer away:** under K3 it is the textbook design for separating abundance from activity, answerable without the paper. Under K5 the card must show the fraction-versus-amount point, the unmatched preparations and the point counts for K5 to be answerable, i.e. the masking cannot hide what the label rests on. Method detail that can be masked is listed in the frozen file; none of it is the part that decides the label.

## 4. Reject rules against the evidence
* Prompt gives away the informative arm: **yes** (K3, textbook), or K5 needs the reasons visible.
* Simple rule always picks it: R1 **no**; R2 **yes** (label K3); N2 **yes** (label K5).
* Assays distinguished only through unmatched preparations: **yes** (Fig 5 against Fig 6: DIV 14 against DIV 3, expression 8 days against 24 h, hippocampal or cortical, no expression readout in the recorded cells; Fig 3 is a third, heterologous preparation with no surface measure).
Any one of the three rejects; two hold.

## 5. What would change the answer (named, not requested)
A paper that reports, in one preparation, the absolute surface density (or surface-over-total together with total) AND a functional readout in the same cells, with at least a handful of cells per arm and a tested equivalence margin for the null arm. The present paper has no such measure; the raw data are "available from the authors" and nothing was requested.

## 6. A narrow fallback, not frozen (for ADV to weigh, no assignment proposed)
Within the HEK assay (one preparation, same traces): initial slope against end plateau as the readout of weak transport. A8 is slope-not-significant but plateau-significant (Fig 3D and E; Table 2: slope 56 +/- 15, plateau 105 +/- 15 percent of WT) and the authors' explanation (low transport is enough for a low steady state) assumes low leak, untested. It is one variant, n not stated in the text, the plateau is not systematically the more sensitive readout (B1, C10, F7 show 50 to 64 percent of WT by plateau and neither metric reaches significance), and the plateau-versus-slope distinction is assay-design knowledge, not a held scientific result. I would not freeze it without a separate read of the Supplementary Figure 3 and the n per arm.

## 7. Limits
Visual point counts and box ranges are read from reduced figure images; the HEK band intensity is a single unquantified blot; Supplementary Figures not opened; the Introduction and abstract not read; no author contact; raw data not requested. Nothing concerns a compound, a dose, a rank or WWOX. Route: Frontiers HTML and its figure files by plain requests (200); the PMC page was not requested (ADV: reCAPTCHA).
