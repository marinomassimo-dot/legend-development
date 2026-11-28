# ADV-316 step 2, first reader, PMID 42395553: delegate report, verbatim (2026-11-28)

Delegate: legend-delegate, sonnet 5.5, effort HIGH stated in the dispatch. Unread parts opened: Figure 1 (PDF page 26), Figure 2 (page 27), Supplementary Figure 1 (page 37), as 110 dpi renders of the held PDF (files/figures/PMID42395553_r2/); also fig4.png and figS2.png (held). Sentences: SENTENCES_CURATED_STEP2_42395553.txt (C01 to C03). Not edited by SCI.

FIRST READ, PMID 42395553 (Petrozziello 2026, bioRxiv, NOT peer reviewed). Hypothesis level, not medical advice.
Read: the whole text file (lines 1-1735, including Methods, legends and Table 1), the three unopened pages (Fig 1 p26, Fig 2 p27, Supp Fig 1 p37), and fig4.png and figS2.png. All values marked "eye" below were read from bar tops against the axis and are about +/-0.005 in OD units. They are not source numbers.

**Sentence checks**

| Item | Verdict | Locator and basis |
|---|---|---|
| C01: rWWOX reduced viability of ESC-derived cortical neurons at 100 ng/mL in both 65Q and 27Q | SUPPORTED | Text: "significant decrease in cell viability in both rWWOX-treated HD cortical neurons (65Q) and their isogenic controls (27Q) compared to the respective vehicle-treated cells". Fig 4B legend: Tukey p<0.0001 for each against its own vehicle. Text and figure. |
| C01 / C03: 24 h exposure | SUPPORTED (text only) | Results: "treated with 100ng/mL rWWOX for 24h". The Fig 4B legend gives no time. |
| C01: genotype main effect F(1,28)=6.181, p=0.0192 | SUPPORTED | Fig 4B legend, verbatim. |
| C01: no treatment x genotype interaction F(1,28)=0.3129, p=0.5804 | SUPPORTED | Fig 4B legend, verbatim. |
| C01: treatment main effect F(1,28)=78.44, p<0.0001 "dominates both" | SUPPORTED | Fig 4B legend. F is 78.44 vs 6.18 vs 0.31. |
| C01 / C02: viability about 0.71 (27Q) and 0.64 (65Q) of vehicle, by hand | SUPPORTED within reading error | Fig 4B, axis 0-0.15. My eye readings on mean bar tops: 27Q vehicle 0.112, rWWOX 0.078, ratio 0.70. 65Q vehicle 0.104, rWWOX 0.066, ratio 0.64. The source prints no ratio. The ratios are my computation from raw MTT optical density (OD). |
| C01: "toxicity is quantified and is not disease-specific on these data" | SUPPORTED, with caveat | Both genotypes fall significantly, and the interaction is not significant. A non-significant interaction is not proof of equal effects. n per cell is not given. The absolute drops are 0.034 (27Q) and 0.038 (65Q), by eye. |
| C02: "three sources now say..." and "outside the vector setting" | NOT ADDRESSED | Only this paper was provided. The other two sources cannot be checked here. |
| C02: the same neuron facts as C01 | SUPPORTED | As above. |
| C02: "applied protein rather than a transgene" | SUPPORTED for the viability result | Viability was tested only with rWWOX protein. WWOX overexpression (SH-SY5Y, RPE-1) was measured for gamma-H2AX only (Figs 5C-E, 7), not viability. |
| C02: "no heat-denatured or endotoxin control reported" | SUPPORTED as absence | Methods: "Recombinant full-length human WWOX protein (rWWOX) was purchased from Pepmic Co (Suzhou, China)". Nowhere are heat-denatured protein, endotoxin, purity, tag or vehicle composition mentioned. |
| C02: "no in vivo arm" | SUPPORTED as absence | The paper has post-mortem tissue, ESC neurons, SH-SY5Y and RPE-1 only. |
| C03: SH-SY5Y doses 1, 10, 100, 500 ng/mL | SUPPORTED | Results and Supp Fig 2 legend. |
| C03: significant loss at 100 and 500 at 24 h | SUPPORTED | Supp Fig 2 legend: 100 ng/mL p=0.0086, 500 ng/mL p=0.0004. 1 and 10 not significant (p=0.9558, p>0.9999). |
| C03: significant loss at 10, 100, 500 at 48 h | SUPPORTED | Supp Fig 2 legend: 10 ng/mL p=0.0460, 100 ng/mL p=0.0030, 500 ng/mL p=0.0081. 1 ng/mL not significant (p>0.9999). Legend and text. |
| C03: neuron arm is 100 ng/mL, 24 h, the lowest dose with a significant 24 h loss in SH-SY5Y | SUPPORTED | Follows from the two rows above. "In that line" has to mean SH-SY5Y. |
| C03: neuron arm is one dose and one time | SUPPORTED | Text: "HD and control ESC-derived cortical neurons were treated with 100ng/mL rWWOX for 24h". No neuron dose-response is shown. |
| C03: F(1,28) in Fig 4B, four cells, 32 observations, eight per cell "implied" | SUPPORTED, with a limit | All three terms carry df 28, and 28+4=32. Eight per cell holds only if the design is balanced, and the source does not say so. |
| C03: replication unit not stated in the Fig 4B legend | SUPPORTED as absence | Fig 4B legend states no n. Fig 4A legend says "n=4 biological replicates". The Methods give no n for neuron MTT. |

**Numbers by figure**
- **Fig 4B** (human ESC-derived cortical neurons, MTT OD, 24 h, replicate unit not stated). The labelled significance is **** for both pairs. Vehicle baselines differ by about 7% (65Q/27Q = 0.104/0.112, eye). This is not labelled significant, but it probably feeds the genotype main effect. The 65Q cells are also lower after rWWOX (0.066 vs 0.078, eye).
- **Fig 4A** (same neurons, WWOX western blot, n=4 biological replicates): 27Q about 79, 65Q about 147 %GAPDH, ratio about 1.9 (eye). Legend: Mann-Whitney U=0, p=0.0266. By my calculation an exact two-sided U=0 with n=4 vs 4 gives 0.0286, which is the value Supp Fig 3A prints. I cannot explain the 0.0266.
- **Supp Fig 2** (SH-SY5Y, MTT OD, replicate unit and n not stated). The df of 20 imply 30 observations across 10 cells, so about 3 per cell if balanced. Means by eye, with ratio to the same-time vehicle:

| Dose (ng/mL) | 24 h OD | 24 h ratio | 48 h OD | 48 h ratio |
|---|---|---|---|---|
| 0 | 0.076 | 1.00 | 0.061 | 1.00 |
| 1 | 0.067 | 0.88 | 0.061 | 1.01 |
| 10 | 0.070 | 0.93 | 0.019 | 0.30 |
| 100 | 0.024 | 0.32 | 0.004 | 0.06 |
| 500 | 0.008 | 0.10 | 0.009 | 0.15 |

  - At 48 h the 10 ng/mL SEM bar is very wide (top about 0.040), and 500 is above 100, so the dose-response is non-monotonic there.
  - Two-way ANOVA: dose F(4,20)=21.15, time F(1,20)=10.67 (p=0.0037), interaction F(4,20)=3.280 (p=0.0320).
  - The figure's asterisk brackets are ambiguous. For example, "**" sits over a bracket whose legend p is 0.0004. I relied on the legend p values.
- **Cross-line comparison, not in C01-C03.** At the same 100 ng/mL and 24 h, SH-SY5Y viability is about 0.32 of vehicle against about 0.64-0.70 in the neurons (eye). The cell lines differ, and the OD scales and plating are not comparable.

**What the three newly opened pages show**
- **Fig 1 (p26)**: post-mortem PFC western blots, controls n=13 and HD n=21. ATM (U=130, p=0.8337), pATM-S1981 (U=105, p=0.6944) and ITCH (U=118, p=0.5288) are all unchanged. Many control ATM points sit near 0. It does not bear on C01-C03.
- **Fig 2 (p27)**: SH-SY5Y treated with HD PFC lysate 25 ng/mL for 24 h, CPT 10 uM for 2 h as positive control.
  - Panels A-C: pATM-S1981 unchanged (F(2,6)=0.1127). gamma-H2AX F(2,6)=10.87, p=0.0101. CPT p=0.0080 and HD p=0.0347 against vehicle, n=3 biological replicates. By eye, gamma-H2AX is about 1.3x vehicle for HD (about 1.4x for CPT). Only the direction is firm.
  - Panels D-G: gamma-H2AX/pATM co-localization is unchanged (Pearson U=2.5, p=0.5; Manders M1 U=4, p>0.9999; Manders M2 U=3, p=0.7).
  - This concerns lysate, not rWWOX, so it does not bear on the sentences.
- **Supp Fig 1 (p37)**: SH-SY5Y, gamma-H2AX intensity, F(4,34)=11.81.
  - By eye: vehicle about 30,000, CPT about 36,500 (1.22x), 10 ng/mL HD about 31,300, 25 ng/mL HD about 33,300 (1.11x), 25 ng/mL control about 31,800. Legend: CPT p<0.0001, 25 ng/mL HD p=0.0211, the other two not significant.
  - Unit of analysis: df 34 means 39 observations, far more than 3 biological replicates (Fig 2 uses df 6 for the same kind of experiment). The unit is probably images or fields, so that panel is possibly pseudo-replicated. This shows that the paper's df can exceed the biological n, which is relevant to C03's "units not stated". It does not bear on the viability numbers.
  - The lysate is tested at two concentrations. It is not an rWWOX experiment.

**Notes on the sentences**
- **Scope of the toxicity claim.** All rWWOX viability data rest on extracellular recombinant protein at 100 ng/mL. The paper's own heading "Increases in WWOX induce neuronal toxicity" goes beyond what was tested. Viability under WWOX overexpression or in the HD context was never measured.
- **MTT in neurons.** The only MTT method written is for SH-SY5Y ("SH-SY5Y cells were incubated with MTT for 1h"). The neuron protocol, plating and timing are not described. The Fig 4B axis does say "Cell viability (MTT Assay)".
- **Preprint status.** The Supp Fig 2 legend carries a stray "Scale bar 50um" with no images.

**What I could not read or establish**
- Individual data points for Fig 4B and Supp Fig 2. They are bars with SEM only, so replicate counts and spread are unreadable.
- The n per cell and the replicate unit for Fig 4B and Supp Fig 2.
- The vehicle composition and rWWOX purity or tag.
- The neuron differentiation day at treatment.
- All other-source claims in C02.
- I did not open the Fig 3, 5, 6, 7 or Supp Fig 3 images, and did not need to.
