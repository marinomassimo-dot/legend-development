# Minimum comparison that would make a KEAP1/NRF2 reagent interpretable in a neural class (SCI48, 2026-11-12)

Non-canonical research material. Not medical advice; no dose, schedule or clinical use; no claim about WWOX or about any reagent as a treatment. Labels: DATO read in a source, INFERENZA mine, IPOTESI proposal.

**Status.** The matrix justifies a design, not a recommendation. INFERENZA: no available reagent is a good comparator in a neural class today. The only neural-class entries with an adequate loss are KI-696 in primary rat microglia (reused SCI46 row, glia, one source) and none for RA839 or sulforaphane (germline KO only, loss unverified in print, or abstract depth).

**Question.** Does a reagent's effect on a stated endpoint need NRF2, separately from other actions, and is a non-covalent binder a usable partner for an electrophile?

**Preparation.** Human-derived or mouse neural cells in which NRF2 activity can be measured: primary mouse cortical neuron-astrocyte cultures kept as separate arms (neuron-enriched, astrocyte-enriched, mixed), or human iPSC-derived neurons and astrocytes. A WWOX-deficient and a matched control version of the same preparation, only after INV-08 X0 shows nuclear NRF2 and NQO1 activity in it (IPOTESI; this comparison does not itself test WWOX).

**Indispensable arms (IPOTESI).**
1. Non-covalent KEAP1 binder versus its inactive scaffold analogue (Winkel RA889/RA912 are the only such controls read; neither was run under loss).
2. An electrophile comparator already in use (sulforaphane or bardoxolone methyl) in the same cells, at a matched on-target response rather than a matched concentration (Winkel: 50 nM versus 20 uM; DATO).
3. A genetic Keap1 loss arm (siRNA, two independent sequences), the Winkel design, which gives the expected on-target response without any reagent.
4. The same four conditions under NRF2 loss. Include the loss-alone arm under the same challenge and the reagent-alone arm: Mao 2019 (neurons) showed OGD+Sfn+sh-Nrf2 but no OGD+sh-Nrf2 arm and no Sfn-alone arm, so a harm from the loss itself cannot be separated from loss of the Sfn effect.

**Control on the target.** Loss adequacy criterion (written before the experiment): NRF2 protein and mRNA reduced at the endpoint time, and loss of the matched target-gene induction by the Keap1-loss arm. Occlusion: Keap1 loss must not add to a reagent effect that is NRF2-dependent, and NRF2 loss must remove the Keap1-loss effect. Prefer acute loss (siRNA or inducible) over germline loss, which is compensated; a germline arm only as an additional arm.

**Discriminating endpoint.** One endpoint per class with the same readout for all reagents: molecular (NQO1 and a second target gene, mRNA and protein), then one functional readout with an exposure that is not cytotoxic (network firing or sEPSC/sIPSC frequency, with the reagent applied in the dish, not by dosing animals). Viability only as a toxicity control, never as the main endpoint.

**Expected results under competing explanations.**
- H1 or H3 (NRF2-dependent): reagent effect lost under adequate loss; binder, electrophile and Keap1-loss arm agree.
- H5 (independent action): reagent effect unchanged under adequate loss; Keap1-loss arm gives nothing at that endpoint.
- H5 for the electrophile only: the binder matches the Keap1-loss arm and the electrophile retains an effect under loss (the contrast Winkel proposed but did not run).
- H6: viability or network worse under activation; the axis becomes a risk arm.

**Inconclusive if:** loss is below the criterion at the endpoint time; reagent exposure is cytotoxic or far above the on-target range (Winkel's 10-20 uM is 1.7-3.3 times its ITC Kd, 71-143 times its FP IC50); the Keap1-loss arm is absent; or only NQO1 is read (SCI46 weak-readout rule).

**Decision that changes.** Which role INV-08 gives each reagent (probe, comparator, conditional hypothesis, not interpretable). It leaves claim 2 (useful in WWOX loss) and claim 3 (therapeutic transfer) untouched.
