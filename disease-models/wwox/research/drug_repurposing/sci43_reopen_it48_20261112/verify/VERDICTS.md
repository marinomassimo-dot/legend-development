# IT48 increment 1: second independent reading of eight SCI43 rows (D01, D02, D03, D04, D07, D08, D11, D13)

Not medical advice. Reference genotype class only. Verifier: separate context, plain requests only, no contact address sent to any service, no browser-header spoofing. Saved sources and SHA-256 values are in `READ_LOG.tsv` (files under `/home/desktop/legend-development/files/fulltext/reopen_it48/`). The earlier verifier's notes (`potassium_conductances_sci43_20261110/verify/verdicts.tsv`, `audit.md`) were read first; every row below was re-opened against its original source rather than against those notes.

How the sources were reached (details in READ_LOG.tsv). bioRxiv answered 429 (Cloudflare error 1015) on the first attempts and on the DOI redirect; after waiting about 90 s the full-text HTML returned 200, and the supplementary-tables PDF (media-1.pdf) was reached the same way. The main-text PDF and the JATS XML stayed at 429. Niday (PMC5242407) and Guan (PMC3191833) came through the plain PMC URL. Day (PMC6725503) returned a reCAPTCHA interstitial on the plain URL and the full text only through the `?report=classic` variant of the same PMC URL. Europe PMC full-text XML returned 500, europepmc.org and jneurosci.org returned 403.

Conventions. "Printed" = taken from the source as written. "Derived" = my arithmetic on printed numbers, inputs stated. The preprint's text says values are "mean ± 95% C.I." (Methods 2.4) but Supplementary Table 1 lists the same figures (for example Rin 172.7 and 34.7) in a column headed SD; I therefore call the ± values SD in this file and note that the preprint is internally inconsistent about it.

---

## D01 — Ba2+ and input resistance in wild-type mouse L2/3 auditory cortex

Verdict: **SUPPORTED** (all propositions), with four wording points below. Depth: full text (Methods, Results, legends), Fig 1 viewed, Supplementary Table 1 read (summary statistics, not per-cell raw data).

| Proposition in the statement | Source | Result |
|---|---|---|
| wild-type mouse, L2/3 primary auditory cortex pyramidal neurons, P28-P42 | Methods 2.2.1: "from wild-type (WT; C57BL/6J) and Fmr1-KO ... mice, between 28 and 42 days old"; Abstract: "juvenile mice (P28-P42)" | supported |
| 34 C | Methods 2.2.1: "continuously perfused with oxygenated ACSF (1-3 mL/min) at 34 ± 2 °C" | supported (the statement omits the ±2 °C) |
| K-gluconate pipette | Methods 2.2.2: "120 K-gluconate, 10 KCl, 8 NaCl, 10 HEPES, 0.5 EGTA, 4 Mg-ATP, 0.3 Na-GTP, and 10 phosphocreatine (pH 7.2, adjusted with KOH ...)" | supported; the internal has 10 mM KCl plus 120 mM K-gluconate |
| no synaptic blocker stated | Methods 2.2.2 (current clamp) lists none; synaptic blockers (10 µM CNQX, 100 µM DL-AP5, 50 µM picrotoxin, with TTX, TEA, 4-AP) appear only in 2.2.4 for voltage clamp. In addition the same neurons were recorded for sEPSPs in this condition (Methods 2.2.3 "Spontaneous EPSPs ... recorded in current-clamp mode at 0 pA holding current"; Results 3.2: WT 3.56 ± 0.89 Hz) | supported; the stronger statement "synaptic input was present" is also supported by the sEPSP data, so the earlier wording point is now closed in the safe direction |
| 60 µM Ba2+ raised Rin about 30 percent, 172.7 to about 224 MΩ | Results 3.1: "Rin; WT: 172.7 ± 34.7 MΩ" and "effects in WT were smaller (ΔRMP: 1.5 mV; ΔRin: 51.1 MΩ; Fig. 1A-C)"; Supplementary Table 1 (WT, n = 26, paired t test, p < 0.001): Rin 172.7 (SD 34.7) to 223.8 (SD 43.4) | supported; 223.8 is now printed, so "about 224" is a printed value, not a derived one |
| only a 1.5 mV depolarisation | Results 3.1 "ΔRMP: 1.5 mV"; Suppl Table 1: RMP -78.3 to -76.8, paired t test p = 0.285; Fig 1A trace labels "Vm = -78.3 mV" and "Vm = -76.8 mV" | supported; not significant |
| implied Ba2+-sensitive share about 23 percent of resting input conductance | Derived: 51.1/172.7 = 29.6 percent rise in Rin; share = 1 - 172.7/223.8 = 22.8 percent. Conductances: 1000/172.7 = 5.79 nS and 1000/223.8 = 4.47 nS, difference 1.32 nS | arithmetic correct; this is a ratio of group means of a paired design (per-cell shares are not available in the text; Fig 1C shows the paired lines all rising) |

Points on what the statement does or does not say:

1. Wording "adult": the source labels P28-P42 mice "juvenile" (Abstract; Methods says "between 28 and 42 days old"). The statement says only "P28-P42", which is correct; the label "adult auditory-cortex figure" used in the brief and closing text is the Orchestrator's, not the source's. It matters for the age transfer to P13-P17.
2. The Methods never say how Rin was computed (the ±50 pA pulses are described only as a series-resistance monitor, Methods 2.2.2). The 23 percent is a conductance share of whatever the authors' Rin measure samples at the resting potential, on a cell at -78.3 mV before and -76.8 mV after Ba2+.
3. "Ba2+-sensitive" is pharmacological at 60 µM; the authors themselves write "we cannot fully exclude off-target effects of Ba2+ ... even relatively low concentrations of Ba2+ have been reported to inhibit A-type potassium currents" (Discussion 4.2) and that the Kir subtype is undetermined. The 23 percent is therefore a Ba2+ (60 µM) increment, not a measured Kir2 share.
4. The n is 26 neurons from 8 mice (Fig 1 legend). The figure legend gives KO n = 24 whereas Supplementary Table 1 gives 26 for KO, so the preprint is not consistent on n for the KO group; WT n = 26 agrees.

---

## D02 — Ba2+-sensitive current at -130 mV, reversal -89.6 mV, coherence with E_K

Verdict: **PARTLY**. All source numbers are supported; the statement says "of those neurons" and omits that the voltage-clamp data are a separate, smaller, pharmacologically isolated sample, and its "within about 1 mV" is 1.2 mV on my recomputation. Depth: full text, Fig 4 viewed, Supplementary Table 3 read.

| Proposition | Source | Result |
|---|---|---|
| Ba2+-sensitive current at -130 mV was -218 pA | Results 3.3: "(WT: -218.2 ± 70.2 pA ... p = 0.0302; Fig. 4B,C)"; Suppl Table 3 "Subtracted current (pA) -218.2 70.2" (WT n = 8). Also Table 3: Imax at -130 mV -365.9 (SD 82.5) before and -147.7 (SD 48.2) after Ba2+, and 365.9 - 147.7 = 218.2 | supported |
| 60 percent block | Results 3.3: "the percent Ba2+ block at -130 mV was ... (WT: 59.6 ± 12.0%" ; Table 3 "I, % of inhibition 59.6 12.0"; derived 218.2/365.9 = 59.6 percent | supported |
| reversed at -89.6 mV "on the recorded scale" | Results 3.3: "reversal potentials ... (WT: -89.6 ± 2.4 mV ..." ; Methods 2.2.4: "The liquid junction potential (LJP) was calculated as 16.2 mV using the stationary Nernst-Planck equation and LJPcalc ... and were not subtracted." Suppl Table 3 "Erev (mV) -89.6 2.4" | supported |
| E_K about -104 mV at 34 C on the stated concentrations | Pipette K+ = 120 + 10 = 130 mM (Methods 2.2.4; K+ added by the KOH titration not counted); bath K+ 2.5 mM (Methods 2.2.1). Derived: RT/F at 34 C = 26.47 mV, E_K = 26.47 x ln(2.5/130) = -104.6 mV (-103.9 at 32 C, -105.3 at 36 C, i.e. across the stated ±2 C; activity coefficients not applied) | statement's "about -104" is off by 0.6 mV; -104.6 is my value |
| within about 1 mV once the 16.2 mV offset is removed | Derived: -89.6 - 16.2 = -105.8 mV; -105.8 - (-104.6) = -1.2 mV (range -0.5 to -1.9 mV over 32-36 C) | "about 1 mV" holds only loosely: 1.2 mV at 34 C |
| a K+ current is a coherent reading; the offset is roughly 16 mV | the source states only the calculated LJP (16.2 mV); the sign convention for its removal is not printed, and the removal direction (subtract) and the inference are the producer's, as the statement itself says | coherence is an inference of the producer; the source does not claim it |

What the statement says less of than the source:

* The Fig 4 legend gives "n = 8 neurons, N = 4 mice per genotype"; Suppl Table 3 gives WT n = 8, Fmr1-KO n = 10. The 218 pA belongs to those 8 WT cells, not to the 26 current-clamp neurons of D01. "Those neurons" is wrong as a literal reading.
* Voltage-clamp conditions (Methods 2.2.4) are very different from the current-clamp conditions of D01: held at -80 mV, 1 mM QX-314 in the pipette, and bath "0.5 µM TTX, 5 mM TEA, 5 mM 4-AP, 10 µM CNQX, 100 µM DL-AP5, and 50 µM picrotoxin", "with 10 µM ZD7288 added" to isolate the Ba2+-sensitive current. The statement does not say so; the cocktail removes other K+ currents and Ih from the denominator of the "60 percent".
* The command voltage of -130 mV is nominal; with the 16.2 mV offset not subtracted the true potential is about -146 mV (same producer convention).
* Table 3 Erev p is printed "-0.126" (a typo for 0.126).

---

## D03 — XE-991 in adult rat L2/3 neurons (Guan)

Verdict: **PARTLY**. The printed numbers and the "little change in slope resistance near rest" are supported; the statement transfers the "-70 mV" activation threshold, and omits cortical area. Depth: full text (PMC3191833), Fig 6 viewed (464 x 158 raster).

* Source: Guan et al. 2011 (PMID 21697446), J Neurophysiol, DOI 10.1152/jn.00211.2011 (the paper is not a J Neurosci paper).
* "5 uM XE-991 did not change resting potential (-83.4 to -82.4 mV)": Results, Function of Kv7-mediated currents: "On average, XE-991 had no significant effect on resting membrane potential (-83.4 ± 2 mV in control vs. -82.4 ± 1.8 mV in XE-991, n = 6 cells)." Supported; values are mean ± SE (Methods, Statistics: "Data are means ± SE"), n = 6.
* "slope resistance near rest": Results: "Near resting potential the slope resistance (the slope of the curve) showed little change, but near spike threshold the I-V relationships were relatively linear in control solution but curved upward in XE-991 (depolarized to approximately -70 mV)". Supported as text. Fig 6A (my read-off, a single example cell): the control and XE-991 ramps overlap from about -88 mV to about -78 mV and separate above about -75 mV. No number is printed for slope resistance, so "did not change" is "showed little change" without a value, in 6 cells.
* "adult rat L2/3 neurons (sharp electrode, 34 C)": Methods, Sharp electrode: "regular-spiking neurons in layers II/III of the motor cortex ... adult (8-16 wk old) rats ... sharp electrodes (40-50 MΩ) ... filled with 3 M KCl ... at 34 ± 1 °C". Supported, but the statement leaves out "motor cortex" (the dissociated-cell part used frontoparietal supragranular layers). Sharp electrode with KCl filling and cells at about -83 mV.
* "whose Kv7 current begins to activate near -70 mV": this comes from a different preparation. Results (Properties of linopirdine-sensitive current): steady-state activation from "a holding potential of -70 mV", acutely dissociated juvenile cells (Methods: P16-P36 mostly), room temperature (21-23 °C), V1/2 -16.7 ± 1.6 mV, slope 11.8 ± 1.3 mV (n = 12); "the holding current at -70 mV was shifted inward 2-22 pA by 3 µM linopirdine (7.5 ± 2.2 pA). When cells were held at -80 mV, there was no significant difference in holding current (n = 7 cells)." Discussion: "putative Kv7-mediated current was active at potentials depolarized to approximately -70 mV". Because the steps start from a -70 mV holding potential, the data cannot show activation below -70 mV; they show a small holding-current effect at -70 and none detectable at -80 (n = 7). So the sentence is supported for the dissociated cells, not for the adult sharp-electrode neurons.
* "at a rest near -80 mV the Kv7 share was therefore small in that preparation": consistent with the resting-potential and slope data, and with the authors' own reading: "Most layer II/III pyramidal neurons had resting membrane potentials of approximately -80 mV ... compared with activation of Kv7 currents at approximately -70 mV ... overall there was no significant effect of XE-991 on resting membrane potential." The authors also write that the current "made up a large fraction of the subthreshold outward current" (at potentials above about -70 mV) and that percent-block data "underestimate the contribution". The statement's "small share" is for rest only; the source says it is large nearer threshold.
* More than the source says: 5 µM XE-991 is above the ≤1 µM range the authors call "selective for Kv7 channels" for voltage clamp (Results: "we chose doses of linopirdine (≤3 μM) or XE-991 (≤1 μM) that are selective"); n = 6 with SE about 2 mV does not exclude a few-millivolt effect.

---

## D04 — Kcnq2 conditional knock-out, input resistance (Niday)

Verdict: **SUPPORTED**. Every proposition is printed in the source. Depth: full text (PMC5242407), Methods, Results, figure legends 1-2; figures not viewed (values are in the text and legend).

* "Genetic loss of KCNQ2 raised input resistance 25 percent (239 to 299 MΩ) in L2/3 somatosensory pyramidal neurons": Results, first section after mAHP: "The input resistance, measured at resting membrane potential followed by a small hyperpolarizing step (−25 pA), of Kcnq2-null neurons was also larger than in control pyramidal neurons (control, 239 ± 17 MΩ, n = 21; Kcnq2 cKO, 299 ± 18 MΩ, n = 18; p < 0.05, Student's t test)". Methods: "Pyramidal neurons from L2/3 somatosensory cortex"; cKO is Emx1Cre:Kcnq2f/f. Derived: 299/239 - 1 = +25.1 percent; share = 1 - 239/299 = 20.1 percent (conductance 4.18 to 3.34 nS, difference 0.84 nS).
* "P15-P20": Methods "Postnatal day 15 (P15) to P20 mice". Supported.
* "synaptic blockers": Methods "100 μm picrotoxin, 4 μm CNQX, and 25 μm d-APV". Supported.
* "room temperature": Methods "All recordings were performed at RT". Supported.
* "resting potential near -67 mV on the corrected scale": Methods "All reported potential values were corrected for the liquid junction potential, calculated to be −14.4 mV"; Fig 2 legend: "control: −67.3 ± 0.8 mV, n = 49; Kcnq2 cKO: −65.7 ± 1.1 mV, n = 39; p = 0.2, Student's t test". Supported; RMP not significant, as the statement says.
* Values are mean ± SEM (Methods "mean ± SEM"; derived SD about 78 and 76 MΩ).

More or less than the source: (a) the RMP figures come from larger cell counts (49 and 39) than the Rin figures (21 and 18), so the resting potential of the Rin cells is not printed; (b) the 20 percent "implied lost share" assumes no compensatory change of other conductances in a constitutive Emx1-Cre knock-out recorded at P15-P20 (the source does not claim a share; its own statement is "partly due to changes in the input resistance"); (c) the Rin step is taken at rest, about -67 mV on the corrected scale, which is about 13 mV more depolarised than a cell resting at -80 mV, where Kv7 is expected to be less open (D03); the source gives no Rin at -80 mV; (d) Fig 2A firing was at "−84 mV by injecting a small direct current", a different condition from the Rin measurement.

---

## D07 — ZD7288 (10 µM) in wild-type mouse L2/3 auditory cortex

Verdict: **SUPPORTED**. The earlier "panel read-off baseline" is now replaced by a printed value. Depth: full text, Fig 5 viewed and Fig 5C zoomed, Supplementary Table 4 read.

* "ZD7288 changed wild-type L2/3 auditory-cortex Rin by about +6 percent (+8 MΩ)": Results 3.4: "Blocking Ih with ZD7288 (10 μM) hyperpolarized RMP in both genotypes (ΔWT: -4.7 mV; ΔFmr1-KO: -3.3 mV; all p < 0.05; Fig. 5A,B) and increased Rin (ΔWT: 8.0 MΩ, p = 0.0349 ...". Supplementary Table 4 (WT, paired t test): Rin 132.0 (SD 34.5) to 140.0 (SD 31.0), p = 0.0349; RMP -78.4 to -83.1, p < 0.001. Derived: 8.0/132.0 = +6.1 percent; share = 1 - 132.0/140.0 = 5.7 percent (conductance 7.58 to 7.14 nS, difference 0.43 nS). My read-off of Fig 5C (filled markers, y-axis 0-250): WT control about 131 and WT ZD7288 about 139 MΩ, consistent with the table. Using the other cohort's 172.7 MΩ as denominator would give 4.6 percent; the table value 132.0 is the correct denominator for these cells.
* "hyperpolarised the cell 4.7 mV": printed (-78.4 to -83.1; Fig 5A trace labels "Vm=-78.4 mV" and "Vm=-83.1 mV").
* "not 28 percent": that 28 percent is the producer's earlier figure, not a source statement (see D13: the Fmr1-KO Rin reduction relative to WT is 27.9 percent, a different quantity).

More or less than the source: (a) Rin after ZD7288 is measured 4.7 mV more hyperpolarised than before, where Kir conductance is larger, so the +8 MΩ is a net of the Ih loss and the voltage change (direction of the bias is not determined by the source); (b) 10 µM is the concentration the preprint used; the Day paper (D08) calls 50 µM "nominally saturating", and the preprint's sag falls from 1.83 to 1.04 mV (Suppl Table 4, p = 0.0257), not to zero, although Results say "abolishing sag"; so an incomplete block cannot be excluded; (c) the ZD7288 cohort is not the Ba2+ cohort: n is 17 in Suppl Table 4 and 20 in the Fig 5 legend (WT), and the baseline Rin differs (132.0 versus 172.7 MΩ), so 5.7 percent and 22.8 percent are shares of different cells' conductances; in nS the blocked increments are 0.43 (ZD7288) and 1.32 (Ba2+); (d) the authors' own reading is "modest changes in passive properties" and "Ih is not the primary determinant".

---

## D08 — ZD7288 in deep-layer mouse prefrontal neurons (Day), and the layer-3 no-sag clause

Verdict: **SUPPORTED** for both clauses; the central datum is "data not shown" in the source, so it can be confirmed only as a printed sentence, not against a figure or table. Depth: full text (PMC6725503 classic view), Fig 1 legend read, Fig 1 not viewed; the layer-3 clause was checked in Kroon (PMC6433913) Fig 3 legend, Table 2 and Methods.

* Day et al. 2005 (PMID 16177047). "In deep-layer (V-VI) mouse prefrontal neurons at P19-P25": Methods "Coronal slices containing the PrL/IL cortex ... from 19- to 25-d-old C57BL/6 mice"; "Deep-layer (V-IV) PPNs" (the source's own typo, for V-VI; Abstract "layer V-VI pyramidal neurons in slices of mouse prelimbic and infralimbic cortex"). Supported.
* "at 50 uM": Results: "The application of ZD-7288 at nominally saturating concentrations (50 μm) for at least 10 min". Supported.
* "raised the slope resistance at -80 mV from a median 55 to 244 MΩ ('data not shown')": Results, whole-cell recordings: "The loss of the HCN conductance at hyperpolarized membrane potentials led to a significant increase in the slope resistance at –80 mV; the median resistance was 55 MΩ before HCN channel block and 244 MΩ after block (n = 8; p < 0.01, Wilcoxon's matched-pairs test; data not shown)." Supported verbatim; n = 8. Derived: 1 - 55/244 = 77 percent of the slope conductance at -80 mV (ratio of medians; 18.2 to 4.1 nS).
* "hyperpolarised the cell 5 mV": Results: "HCN channel block resulted in a modest, but consistent, hyperpolarization of the somatic membrane (–5 ± 3 mV; n = 15)"; Fig 1 legend example "hyperpolarized 4 mV". Supported (the ± is SE or SD per the source's "means ± SE or box plots").
* Temperature "32-33 C": Methods "maintained at 32–33°C". Not in the statement but consistent.
* "so Ih can carry most of the conductance at -80 mV in deep neurons": my 77 percent derivation agrees; but the resting potential in this paper is "typically approximately –65 mV" and "Records were not corrected for the liquid junction potential, which was estimated to be 6–7 mV", so -80 mV is about 15 mV below rest; the half-activation of the HCN current is about -86 to -90 mV (Results; Abstract "near –90 mV"). The statement keeps "at -80 mV" and so does not say it is the share at rest. The source gives no share at rest.
* "this is not shown for L2/3 neurons": true; the source is layer V-VI only.
* "layer-3 neurons showed no prominent sag at P7-P28 in another dataset": Kroon et al. 2019 (PMID 30911152), Fig 3 legend: "(e) There is no prominent voltage sag in layer 3 neurons. Layer 5 neurons do exhibit a voltage sag"; Results: "Layer 5 neurons showed a characteristic voltage sag ... which is absent in layer 3 neurons (Fig. 3a)". Table 2 sag (L3) 8.08 ± 1.78, 5.27 ± 0.91, 5.05 ± 0.59 percent (weeks 1, 2, 4; ANOVA p = 0.307). Mouse medial prefrontal (prelimbic) layer 3, not somatosensory. The age groups are "week 1 (P6-8), week 2 (P13-16) and week 4 (P26-30)", so "P7-P28" is the group means; and a sag of about 5 percent is not zero, the authors' wording is "no prominent". Supported with those labels.

---

## D11 — Kv7-mediated current density by age (Guan)

Verdict: **PARTLY**. The four printed means and the ANOVA statement are supported; the inference to a smaller Kv7 share at P13-P17 is not supported statistically and is measured in another quantity. Depth: full text (PMC3191833).

* Results, Ontogeny of Kv7-mediated current: "Current density (at −10 mV from a holding potential of −70 mV) increased from 6.9 ± 1.6 pS at P6–P8 (n = 13), to 8.7 ± 2.3 pS at P11–P14, 17.9 ± 3.1 pS at P20–P24, and 17.6 ± 4.9 pS at P26–P30. There was a significant difference in putative Kv7-mediated density with age (P < 0.003: ANOVA), but only the 1-wk data (P6–P8) differed from the other groups, so in subsequent experiments, the data were combined for cells from animals from P16 to P36." The units "pS" are as printed for a "peak current divided by whole cell capacitance" density. Supported verbatim. Derived: 17.9/8.7 = 2.06. Methods give n = 18 for P11-P14 ("P11–P14, n = 18"), n = 13 for P6-P8; n for P20-P24 and P26-P30 are not itemised (P21-P26: 43 cells, P27-P36: 56 cells).
* The statement's own caveat (P11-P14 versus P20-P24 not significant by post hoc test) is confirmed: the sentence says only the P6-P8 group differed. The sentence is odd on its face (P6-P8 at 6.9 and P11-P14 at 8.7 are close, yet are said to differ), so which pairs differed cannot be read from the text; the safe reading is that the P11-P14 versus P20-P24 pair is not reported as significant.
* Why not SUPPORTED: (a) "so a Kv7 share is expected to be smaller at P13-P17 than at P20 and later" rests on a difference of means that the source does not call significant; (b) the quantity is a current density at -10 mV from -70 mV in acutely dissociated cells at room temperature (Methods, 21-23 °C), not a conductance share at rest or in slices; (c) the source assumes "that sensitivity to these blockers does not change with age"; (d) the source's blocker doses are sub-saturating ("an underestimate of the Kv7 contribution"); (e) P13-P17 falls between the P11-P14 and P20-P24 groups and the P16-P20 cells (n = 11) are not reported separately.
* "no developmental source for Kir2 or HCN contributions in the same neurons was reached": an absence statement about the producer's search; not something this source can confirm or refute (the source reports none).

---

## D13 — Fmr1 knock-out as a K+ gain calibration

Verdict: **SUPPORTED** for the three numbers and their direction; "known sign" is the preprint's inference from Ba2+ pharmacology, not an independent measurement. Depth: full text, Fig 1 and Fig 4 viewed, Supplementary Tables 1 and 3.

* "Rin 172.7 to 124.5 MΩ": Results 3.1 "(Rin; WT: 172.7 ± 34.7 MΩ; Fmr1-KO: 124.5 ± 33.2 MΩ, p < 0.001; Fig. 1C)". Derived: (124.5-172.7)/172.7 = -27.9 percent; conductance 5.79 to 8.03 nS (+2.24 nS).
* "rest -78.3 to -82.0 mV": Results 3.1 "(RMP; WT: -78.3 ± 6.4 mV; Fmr1-KO: -82.0 ± 6.8 mV; p = 0.0457". Supported (Suppl Table 1: 6.3 and 6.8 as SD for the same means).
* "Ba2+-sensitive current -218 to -307 pA at -130 mV": Results 3.3 "(WT: -218.2 ± 70.2 pA; Fmr1-KO: -307.3 ± 89.2 pA; p = 0.0302". Suppl Table 3: Fmr1-KO -307.5; n = 8 WT and 10 KO (Fig 4 legend says 8 per genotype); Erev KO -82.9 ± 16.3, p = 0.126 (not different).
* Direction ("K+ gain"): the authors conclude "enhanced Ba2+-sensitive potassium conductance as a primary determinant of the Fmr1-KO subthreshold conductance state"; Ba2+ moved KO Rin 124.5 to 191.1 MΩ (ΔRin 66.6 MΩ, KO share 1 - 124.5/191.1 = 34.9 percent, versus 22.8 percent in WT; Ba2+-sensitive conductance 2.80 versus 1.32 nS, ratio 2.1), and KO RMP 4.8 mV depolarised (Suppl Table 1: -82.0 to -77.2).
* More than the source: the preprint does not manipulate the conductance; it compares two genotypes and uses 60 µM Ba2+, and says in the Discussion that Kir2.x versus Kir3.x, expression, and "additional contributions from other K+ conductances (including A-type currents)" are untested. "Opposite pattern to Wwox" is the producer's comparison and not in the source.

---

## Final table

| Row | Verdict | Depth reached | Main reason for the verdict |
|---|---|---|---|
| D01 | SUPPORTED | full text, Fig 1 viewed, Suppl Table 1 | every number printed (223.8 now printed); 22.8 percent recomputed; source calls P28-P42 "juvenile"; Rin method not described |
| D02 | PARTLY | full text, Fig 4 viewed, Suppl Table 3 | numbers printed; "those neurons" is a separate n = 8 pharmacologically isolated set; E_K -104.6 not -104 and the gap is 1.2 mV |
| D03 | PARTLY | full text, Fig 6 viewed | numbers printed; motor cortex omitted; "begins to activate near -70 mV" comes from dissociated juvenile cells at RT (holding potential -70) |
| D04 | SUPPORTED | full text (no figures) | all values, ages, blockers, RT, LJP-corrected rest printed; share 20.1 percent recomputed |
| D07 | SUPPORTED | full text, Fig 5 viewed, Suppl Table 4 | baseline now printed (132.0 to 140.0); 6.1 percent and 5.7 percent; ZD7288 sag not abolished (1.04 mV) |
| D08 | SUPPORTED | full text (Day, Kroon); Day Fig 1 not viewed | 55 to 244 MΩ printed but "data not shown"; slope at -80 mV is 15 mV below rest; layer-3 clause verified in Kroon |
| D11 | PARTLY | full text | four means and ANOVA printed; doubling not significant post hoc; density at -10 mV in dissociated cells at RT; inference not supported |
| D13 | SUPPORTED | full text, Fig 1 and 4 viewed, Suppl Tables 1 and 3 | three numbers printed; "known sign" is the preprint's pharmacological inference |

Counts: SUPPORTED 4 (D01, D04, D07, D08), PARTLY 3 (D02, D03, D11), NOT_SUPPORTED 0, STILL_UNVERIFIABLE 0. The earlier verdict was UNVERIFIABLE on all eight.

---

## Closing paragraph

The 23 percent figure survives as printed arithmetic: Supplementary Table 1 gives WT Rin 172.7 to 223.8 MΩ with 60 µM Ba2+ in 26 neurons (paired, p < 0.001), a share of 22.8 percent of the resting input conductance (1.32 of 5.79 nS), at 34 ± 2 °C, K-gluconate internal, no synaptic blocker, RMP -78.3 mV. It is a Ba2+ (60 µM) increment, not a measured Kir2 share; the voltage-clamp reversal (-89.6 mV, 1.2 mV from a recomputed E_K once the 16.2 mV offset is removed) supports a K+ current but comes from a separate set of 8 cells in a pharmacological cocktail; and the source calls these P28-P42 mice "juvenile" rather than adult. None of the other rows measures a Ba2+-sensitive resting conductance in juvenile layer II/III neurons at about P13-P17, so none can confirm or contradict the magnitude there: the juvenile L2/3 evidence is for Kv7 only (D04: input resistance +25.1 percent, implied share 20.1 percent, but at P15-P20, room temperature, with synaptic blockers and at a rest of -67 mV; D11: Kv7 density about doubles from P11-P14 to P20-P24 in dissociated cells, a difference the source does not call significant), the adult Kv7 data point to a small share at -80 mV (D03, motor cortex), and the Ih data give about 6 percent in the same P28-P42 auditory cortex (D07, 0.43 nS) and a large share only at -80 mV in deep prefrontal neurons (D08). KH1's magnitude for juvenile L2/3 therefore remains a transfer from P28-P42 auditory cortex; these shares are of different cells, ages, areas, temperatures and potentials and must not be added. What I did not read: the preprint main-text PDF and JATS XML (429), per-cell raw data and source data files (none found; the supplementary file holds summary tables only), Fig 2, 3, 6 and 7 of the preprint and Fig 2 to 7 of Guan other than Fig 6, any figure of Niday and of Day (Day Fig 1 legend only), the Guan and Kroon references beyond the clauses cited, and the Wwox data themselves; I did not assess druggability and changed no row, ranking or other file.
