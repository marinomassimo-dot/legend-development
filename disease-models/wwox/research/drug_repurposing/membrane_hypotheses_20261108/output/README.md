# Package A: membrane physiology to pharmacological hypotheses (producer mh-a, 2026-11-08; revised after the blind audit)

Not medical advice; no dose, schedule or route; reference genotype class only; ex vivo tool arms only, no exposure statement.

## Answer first

1. IPOTESI: no compound is nominated and the abstention stands after the audit and the figure reading. The question sharpens to an order of three steps: (a) compare cells at matched potential and deflection with capacitance, seal and access resistance reported; (b) does a blocker-sensitive current differ in voltage clamp; (c) does any blocker move bursts. MH1-MH3 (`hypotheses.tsv`) all survive, only as exploratory hypotheses, MH2 only as a conditional one.
2. DATO: the only WWOX datum is one table (34634460 Table 1, layer II/III pyramidal neurons, P13-P17): Rin 102.88 / 143.26 / 143.03 Mohm, rest -79.25 / -75.51 / -73.62 mV, sag 1.18 / 2.04 / 2.57 mV, rebound 0.96 / 1.24 / 1.86 mV (WT / HT / KO). No Ih, Kv7, K2P or Kir measurement exists.
3. INFERENZA: tau is nearly flat (18.55 / 18.79 / 21.25 ms) while Rin rises 39 percent; a pure leak loss at constant capacitance predicts about 25.8 ms (observed values about 3.9 and 2.9 SE below), so, under the single-compartment assumption, a pure leak loss does not fit (a hyperpolarisation-activated conductance in the 50-60 ms fit window could also shorten the apparent tau). The implied capacitance (about 180 / 131 / 149 pF) has about 14 percent propagated uncertainty (WT versus HT z about 1.6, WT versus KO about 1.1): a lower capacitance in mutants is a direction of means, not an established difference. Smaller cells plus a fixed seal leak (A10) would also give Rin up, rest depolarised and tau flat.
4. INFERENZA: E_K (about -97 to -98 mV) is a property of the solutions and needs no junction correction; the recorded potentials do (about -13 mV, borrowed from two companion papers, not measured here). On the corrected scale the estimated -200 pA peaks lie about 16-21 mV below E_K, so K+ current at the sag peak is inward and not small. "A K-leak difference current reverses near E_K" is a prediction for the voltage-clamp experiment E3 only.
5. INFERENZA: the HT-versus-KO differences in sag and rest are not distinguishable from the printed means (t about 0.9 and 0.8); "grading with gene dose" is a description of three means, and a residual non-passive sag excess is not established (sag fraction z about 1.6 WT versus KO; per-cell data are needed).
6. DATO (transfer): ivabradine reduces cortical layer 5/6 sag by about half (about 2.65 to 1.4 mV at -200 pA, n=6, Fig 5 viewed) and ZD7288 leaves 0.4-2.1 mV in thalamic neurons; this shows HCN contributes to sag in those cells, not that it differs in Wwox. A drug response is not proof of a defect in the target, and an increased current is not assumed harmful.
7. INFERENZA: the Methods drug list (TTX, d-APV, carbenoxolone, brilliant blue FCF) contains no AMPA or GABA-A antagonist, so the intrinsic recordings were probably unblocked, with spontaneous bursting in 36 of 42 KO slices; persistence under blockade would show the difference is intrinsic to the recorded membrane, not Wwox cell-autonomy (pan-neuronal Cre).
8. IPOTESI: first experiment E1 (matched potential, matched deflection, normalised sag, capacitance, seal and access resistance by genotype, with and without blockade), then E2 (Ih in voltage clamp, two chemotypes), then E4; E3 tests the K-leak difference current.
9. Abstention on drug choice: Kv7 openers and ZD7288 off-target actions were read at abstract level only; K2P and Kir tool papers exist (ML133, ML335/ML402; reported by the verifier, not read by me) but none is shown to work in layer II/III pyramidal neurons. The datum that would change this is a Wwox conductance (Ba2+-, XE991- or ZD7288-sensitive current).
10. Source count: 9 newly read sources against a cap of 8, one above the cap; the extras are abstract-only (14575712, 27464853).

## What changed relative to the IT38 qualified state

IT38 state: Table 1 read; sag not matched or normalised for Rin; review says open HCN lowers Rin; sag not shown HCN-exclusive; GAERS and ivabradine facts. This package adds (labels as in Phase 1, corrected after the audit):
1. INFERENZA, partly known: flat tau and implied capacitance were in hcn_20261107 Y03 and IT38 D02; new here: its consequence for the leak reading, with the uncertainty (not an established smaller-cell difference).
2. DATO: Rin and tau are identity criteria and outcomes. New.
3. DATO and INFERENZA: access resistance up to 40 Mohm accepted against Rin 100-143 Mohm, not reported by genotype; junction potential uncorrected here, corrected in the two companion papers. New.
4. INFERENZA: E_K versus peak potentials; corrected as in line 4 above. New.
5. DATO then INFERENZA: F-I slope unchanged when aligned to rheobase (Supp S4 viewed). New.
6. DATO and INFERENZA: bursting 36/42, 4/23, 0/11 and probably unblocked intrinsic recordings (drug list). New.
7. DATO (transfer): GAERS: more Ih with lower peak-based Rin, unchanged rest and sag; ZD7288 about 15-18 mV hyperpolarisation, Rin lower by about 9-32 percent at the more negative potential (Fig 6 viewed). Partly in IT38 D04.
8. DATO (transfer): ivabradine 3 versus 30 umol/L, 25-35 d, layer 5/6, in-vivo free level 184 nmol/L (n=4) with an efflux inhibitor and 4.7 (n=2) without; partial sag reduction. New in detail.
9. DATO: one review sentence says HCN blockade depolarises; contradicts the review and primary data; not used.
10. DATO: Ih reversal about -20 to -30 mV remains a review statement. Unchanged.
11. DATO within perimeter: no Ih, Kv7, K2P, Kir, HCN protein or blocker datum in 34634460 or its supplement; capacitance is never reported; the cited neocortical ZD7288 study stays secondhand.
12. New after the audit: smaller cells plus a fixed seal leak as an alternative (A10); the HT-versus-KO argument withdrawn; "removes sag" corrected to "reduces".

## Figures read after the audit (`figure_notes.tsv`)

All five figures of 34018186 (Figs 1-4 are in vivo; Fig 5 carries the sag and resting-potential data) and Figs 2, 4, 5, 6 of 24953239 were viewed through the public PMC open-data bucket (queries Q17), plus Figs 1 and 3 earlier. Figs 1-5 of 34634460 were not viewed by design (bursting and synaptic-current figures; no membrane or blockade statement per caption). Numbers read off figures are INFERENZA with the stated precision. Nothing in the figures changed a hypothesis; Fig 6 of 24953239 and Fig 5 of 34018186 sharpened wording (partial sag reduction; ZD7288 Rin measured at a 15-18 mV more negative potential; Rin not shown for ivabradine). Fig 2 (oral, in vivo) disagrees with the text in bar heights and stars (details in `figure_notes.tsv` F03); left unresolved, the oral percentages are not to be quoted as certain, and Fig 2 carries no hypothesis. Injection AUC bars (Figs 3 and 4) are relative to vehicle.

## Evidence

`observations.tsv` (O01-O12 WWOX; T01-T05 transfer), `evidence.tsv` (49 rows), `alternatives.tsv` (A01-A10), `probes.tsv`, `figure_notes.tsv`. Depth: 34634460 partial_fulltext_read (receipt depth; membrane parts read in full; Figs 1-5 not viewed); 34018186 and 24953239 partial_fulltext_read (text and all figures; references not read); 37982354 partial_fulltext_read; abstract_only for 11466425, 31063701, 18534748, 14575712, 27464853; 22989944 abstract re-read, earlier partial receipt reused. Receipts `receipts/INDEX.tsv` (suffix -51 and, for the two figure completions, -52, whose prior_receipt is the staged -51 receipt).

## Counter-evidence

HT and KO not distinguishable (no dose effect established); the sag fraction is within about 1.6 SE; F-I slope unchanged; GAERS shows more Ih with lower Rin; ZD7288 lowered Rin in thalamic neurons but is reported to raise it in a neocortical study (secondhand); the review says open HCN lowers Rin.

## Not reached

Figs 1-5 of 34634460 and Supp S1 and S3 (not needed); full text of 22989944 and 11466425 (PDF-only, not in the open-data bucket); primary papers for XE991, any K2P or Kir tool, ZD7288 sodium-block numbers (unverified); the Methods of the Kv7 papers; an explicit statement whether the intrinsic recordings were blocked. Open needs (not opened): Methods and concentrations of a neuronal Kv7 opener recording; the cited Wang 2016 full text for ZD7288 sag and Rin numbers; the Sanchez-Alonso 2008 and Wu 2012 concentration-response for a ZD7288 window.

## Queries

`queries.tsv` Q01-Q18 (Q09: the unclaimed batch metadata call; Q14: unreachable routes before the bucket was used; Q17: the bucket route).
