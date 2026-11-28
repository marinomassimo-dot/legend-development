# ADV-317 result (SCI bb, 2026-11-28): Crawford 2010 recruitment test, PMID 20858739

Hypothesis level; reference genotype class only; not medical advice. Status: FINAL for SCI's own reading (SCI bc added the Fig 9 and Fig 5C image check, section 3); the cell-by-cell comparison with HE's independent blind table (ADV-318) is still pending, so no value goes to IT before it. Frozen note: `PREREG_CRAWFORD2010_RECRUITMENT_ADV317_SCI_20261128.md` (sha256 fcef81d145212bf3bb66f3f9abbbcc11a84c9f94d40c784e12a0570c83faa0d6, written 2026-11-28T11:34:39Z, before any figure of this paper was opened). Delegate: legend-delegate, sonnet 5.5, effort high, blind brief without values or hypothesis; report verbatim in `BLIND_FIGURES_CRAWFORD2010_ADV317_DELEGATE.md` (figures and supplement from the PMC open-data bucket PMC2947430.1, held under `files/figures/PMID20858739/`). SCI check on the original: Fig 8 opened by SCI as an image at about 11:42Z (see section 3).

## Disclosures
* **Caption seen after the freeze.** At about 11:35Z, after the freeze and before any figure was opened, I printed the Fig 8 and Fig 9 CAPTIONS from the held XML. From the Fig 8 caption ("evoked at a stimulus of 4 mA") I guessed that amplitude is given at one stimulus only and that rule 3 (NONE) would apply. That guess was WRONG: Fig 8C and 8D plot full stimulus-response curves per group (delegate and SCI image check). The rule was applied to the figures, not to the guess.
* The delegate's per-group values are by eye (about 5 percent of axis range, curves on 572 x 800 and 686 x 800 pixel JPEGs). Ratios below are mine, computed from those eye values.

## 1. What the figures print (frozen rule 1: plotted or printed values only)
| Readout | Normal | EAE + vehicle | EAE + ER-beta ligand | Source |
|---|---|---|---|---|
| N1 CAP at 4 mA (mV, eye) | about 1.07 | about 0.55 (D36), 0.59 (D20) | about 0.90 (D36), 0.80 (D20) | Fig 8C |
| N2 CAP at 4 mA (mV, eye) | about 0.84 | about 0.33 (D36), 0.35 (D20) | about 0.60 (D36), 0.45 (D20) | Fig 8D |
| N1 vehicle / normal at 4 mA | | 0.51 to 0.55 | ligand D36 / normal 0.85 | computed |
| N2 vehicle / normal at 4 mA | | 0.39 to 0.42 | ligand D36 / normal 0.71 | computed |
| Shape (eye) | | N1 and N2 curves coincide from 0 to about 0.7 to 1 mA, then diverge; vehicle curves flatten from about 3 to 3.3 mA while normal rises to 4 mA | | Fig 8C, D |
| Paired-pulse 50 percent interval N1, ms (printed, mean ± SD, n = 4 animals) | 2.2 ± 0.21 | 3.9 ± 0.15 | 3.0 ± 0.11 | Fig 9 table |
| Paired-pulse 50 percent interval N2, ms (printed) | 3.1 ± 0.12 | 3.5 ± 0.20 | 3.1 ± 0.22 | Fig 9 table (the text prints SDs 0.10, 0.05, 0.16: mismatch) |
| N1 upper plateau of C2/C1 (eye) | about 90 percent in all three groups | | | Fig 9B |
| EM at day 36 (bar, eye; text agrees) | myelin 0.060 um, g-ratio 0.865 | 0.027 um, 0.947 | 0.065 um, 0.853 | Fig 5C (i, ii) |
n: Fig 8 legend "4 mice per group, 3 sections per mouse, 12 sections"; Statistics "n = number of animals"; error-bar type and unit UNSTATED in Fig 8. EM: "at least four mice" in the legend against "three animals perfused for electron microscopy" in Methods, ">500 axons" per mouse or per group (statements disagree); the EM animals are NOT the recorded animals (Methods list four animals for electrophysiology and three for EM). Fig 9 paired-pulse stimulus: "a defined strength", not stated.

## 2. Frozen rule applied
* **N1:** plateau down by about 45 to 49 percent (eye ratio 0.51 to 0.55) AND the paired-pulse 50 percent interval moves from 2.2 to 3.9 ms (printed; +1.7 ms, about +77 percent, with SDs 0.21 and 0.15). Pattern **both change** for vehicle EAE against normal. The ligand arm shows a partial return in both readouts (N1 0.85 of normal; 3.0 ms).
* **N2:** plateau down by about 58 to 61 percent (ratio 0.39 to 0.42) while the 50 percent interval moves 3.1 to 3.5 ms (+0.4 ms, about +13 percent, SDs 0.12 and 0.20). The N2 C2/C1 curves are close but not identical: by eye the vehicle curve lies below normal at 1.5 to 3 ms, they cross near 4 ms and vehicle lies above normal by about 7 to 10 points at 5 to 8 ms (upper plateau about 78 percent against about 73). An earlier wording here ("overlap closely between 3 and 6 ms") was too strong and is withdrawn. Reading: **plateau change with little paired-pulse change**, the E-RECRUIT pattern for N2 (the slower component, not a myelin-thickness readout).
* **Prediction (written before any figure):** "N1 plateau lower by a clearly readable fraction (met); C2/C1 shifted by little or not at all (NOT met for N1: a shift of 1.7 ms was printed; met for N2)". My lean (recruitment) is therefore **half supported**: supported for N2, refuted for the N1 paired-pulse clause.
* **Strong counterexample** (a C2/C1 shift of the printed size with NO plateau change): **not observed**; the plateau changed in every comparison, so it neither confirms E-FAIL as the sole cause nor removes it.
* **Frozen table row:** N1 = "Both change": the two readings cannot be separated by this source; N2 = recruitment-like.

## 3. SCI checks on the original
Fig 8 opened as an image by SCI (about 11:42Z): C and D show five series (Normal, EAE + vehicle D20 and D36, EAE + ligand D20 and D36) with fitted curves; N1 normal about 1.07 at 4 mA and vehicle about 0.55 to 0.58; N2 normal about 0.83 and vehicle about 0.35; the curves coincide below about 0.7 to 1 mA. CONFIRMED against the delegate. The delegate's remarks that the "*" bracket in N1 ends near the ligand D20 marker and that the legend assigns marks to "compared with normal" while the text assigns "*" to ligand against vehicle (late) are not mine; not re-checked. Fig 9 table values and Fig 5 were not re-opened by SCI (delegate report only).

**Second SCI check (SCI bc, 2026-11-28, about 11:53Z): Fig 9 and Fig 5C opened as images** (`awq237f9.jpg`, sha256 ba2f1400faa56f0ddfce4d67eacb7e25a012cd25f68c92e92f274b07dbccbaba; `awq237f5.jpg`, sha256 a91a10a7ec0978a455ba4804c4d870aa6cd5abec2cd06566f76eb6ed3e410093).
* Fig 9 printed table CONFIRMED, all six cells (columns "N1 (ms)" and "N2 (ms)"): Normal 2.2 ± 0.21 and 3.1 ± 0.12; EAE + vehicle 3.9 ± 0.15 and 3.5 ± 0.20; EAE + ligand 3.0 ± 0.11 and 3.1 ± 0.22.
* Fig 9B CONFIRMED by eye: N1 vehicle curve shifted to longer intervals, ligand between, all three near 90 percent at 6 to 8 ms. N2: see the corrected wording in section 2. The figure prints no test or significance mark.
* Fig 5C(i, ii) CONFIRMED by eye: myelin thickness about 0.060, 0.027, 0.065 um and g-ratio about 0.865, 0.947, 0.854 (Normal, EAE + vehicle, EAE + ligand); both panels mark ** for vehicle against normal and against ligand.
* Fig 5C(iii, iv) by eye: unmyelinated axons sit at g = 1.0 and myelin = 0 in the scatters, and normal myelinated axons lie mostly above 0.06 um, so the bar means appear to include unmyelinated axons (not printed on the figure; this was already recorded by HE in ADV-315 and in item 9 of the ADV-313 addendum, so it is confirmation, not a new point). If so, the fall from 0.060 to 0.027 um mixes loss of myelinated fraction with thinner sheaths, and the scatters (overplotted) do not separate the two (hypothesis).

## 4. Limits that stop a stronger reading
* "Plateau" here means the amplitude at the highest plotted stimulus (4 mA): the normal curves are still rising there, so no upper plateau is demonstrated for the normal group.
* The paired-pulse stimulus intensity is unstated. C2/C1 is a ratio to each group's own C1, and C1 is about halved in vehicle EAE, so a shifted C2/C1 can partly reflect a different place on the stimulus-response curve; this source cannot say how much (hypothesis).
* Group level only: EM and CAP come from different animals (Methods); the CAP unit of the error bars is UNSTATED; EM n is stated three ways; the EM bar means appear to include unmyelinated axons (delegate's inference from the scatter, not printed).
* No threshold, slope, half-maximal stimulus or plateau parameter is printed; the values above are eye reads; conduction velocity is text-only (no regression panel exists).
* One model (chronic EAE, adult), one tract (callosal slices), eight to sixteen recordings from four animals per group; no test is printed for Fig 9.

## 5. What this changes
| Item | Change |
|---|---|
| Clemastine and dalfampridine caveat (a fitted peak slope can shift when the responding proportion changes) | Gains a measured precedent in a held source: in demyelinating EAE the N1 and N2 plateau falls by about half or more while curves coincide at low stimulus, i.e. the responding population at high stimulus changes. A slope or latency taken at one stimulus in such a slice mixes both effects. |
| INV-06 / RP-049 next experiment | Specify, in the same slices, (1) N1 and N2 amplitude against stimulus strength per animal, (2) latency at each distance, and (3) the paired-pulse protocol at a stimulus giving matched C1 amplitude (for example half-maximal) in each group, so that the C2/C1 shift is not confounded with the position on the curve. |
| Priority of the question "conditional distal failure vs changed recruitment" from held data | Stays open for N1 (both change, frozen row "both change"); it drops for held-source analysis (no other held source prints stimulus-response curves with EM; Palma 2022 text has no amplitude by distance) until an animal-linked recording with identifiable components appears. |
| Compound roles | Unchanged (clemastine and dalfampridine conditional comparators); no new compound. |

## 6. Open for the successor
(a) DONE: the SCI image check of Fig 9B, the printed table and Fig 5C (section 3); (b) deliver to ADV, then compare with the HE ADV-318 table cell by cell; (c) sentences for IT only if ADV-317 names a consumer sentence; (d) the PMID 31140740 cross-check is NOT done (text-level only, frozen rule 5).
