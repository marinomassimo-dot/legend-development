# Blind audit, Package A (membrane physiology), 2026-11-08

Verifier label `vf-mh`. Task `ORCH-IT39OS-20261108`. Written before opening `output/README.md`, `output/engine_consumption.md` and `output/consumer_delta.md` (an addendum after them is at the end and is marked as such). Nothing outside `verify/` was written. Plain `curl` with the default user agent only. Labels DATO / INFERENZA / IPOTESI are mine unless I say I am quoting the producer.

Verdict vocabulary: SUPPORTED / PARTLY / NOT SUPPORTED / UNVERIFIABLE.

## 0. What I read, at which depth, by which route

| Source | Route | Depth I can claim |
|---|---|---|
| 34634460 (Breton 2021, PMC8609180) | NCBI efetch XML (all of Abstract, Introduction, Results, Discussion, Methods, Table 1, every legend), PMC open-data bucket for figures and the supplement; Fig 6 viewed (A, B, C), crops of Fig 6A enlarged; supplement `mmc1.docx` converted to text (Table S1, legends S1-S4); Supp Fig S4 image viewed. Supp S1-S3 images not viewed (captions read; they concern LFP, PAC, field NMDA responses, not intrinsic properties) | full_text_read for everything the three hypotheses use; Fig 1-5 not viewed |
| 34018186 (Iacone 2021, PMC9543052) | efetch XML (all text, legends), bucket images; Fig 1 (brain levels), Fig 5 (neuron sag and RMP) and Fig 2 and 4 viewed | full_text_read for Methods, Results, Discussion; Figs 1, 2, 4, 5 viewed; Fig 3 not viewed |
| 24953239 (Cain 2015, PMC4435665) | efetch XML (all text, Table 1), bucket images; Figs 1, 3, 6 viewed | full_text_read for text and Table 1; Figs 1, 3, 6 viewed; Fig 2, 4, 5 not viewed |
| 37982354 (review, PMC7616572) | efetch XML | only the sentences needed to check the six quotes, via text search; not a section-level read |
| 11466425, 31063701, 18534748, 14575712, 22989944, 27464853 | PubMed metadata (abstract) | abstract_only |
| 21615117 (ML133), 28693035 (ML335/TREK-1), 33127683, 42190144, 21767287, 18365142 | PubMed search and metadata | abstract_only, used only for the absence re-run in section 6 |

Route notes (honest record). The Europe PMC `supplementaryFiles` endpoint at the ebi.ac.uk host returned a connection-refused error body for PMC8609180 on four tries and a truncated archive for the other two papers (same as the producer). Two paths on the europepmc.org host returned a bot-check page (HTTP 403, "Just a moment"); I did not retry them by another trick. The figures and the supplement came instead from the public PMC open-data bucket (`pmc-oa-opendata.s3.amazonaws.com`) with plain `curl`, which needs no account and no header. PMC3536728 and PMC6762632 (the PDF-only deposits for 22989944 and 11466425) are not in that bucket and stay unreachable. Claims: placed before opening for 34634460, 34018186, 24953239, 37982354, 11466425, 31063701, 18534748, 14575712, 22989944, 27464853. Late claims, placed after the abstract had already appeared in a batch metadata call or a search result: 21615117, 28693035, 33127683, 42190144, 21767287, 18365142 (only used as absence-re-run context).

---

## A. Numbers from the primary sources

### A1. 34634460 (Breton 2021)

| # | Item the producer relies on | What I found | Verdict |
|---|---|---|---|
| A1.1 | Rin 102.88 / 143.26 / 143.03 Mohm | Table 1, PY row: 102.88 +/- 11.74, 143.26 +/- 15.49*, 143.03 +/- 8.88* (WT, HT, KO). Method: "Input resistance was measured by the slope of the computed I-V plot." Current range not stated. | SUPPORTED |
| A1.2 | tau 18.55 / 18.79 / 21.25 ms | Table 1: 18.55 +/- 1.52, 18.79 +/- 1.77, 21.25 +/- 1.53, no asterisk. Method: first 50-60 ms of a "small hyperpolarizing stimulus" fitted to a standard exponential. | SUPPORTED |
| A1.3 | RMP -79.25 / -75.51 / -73.62 mV | Table 1: -79.25 +/- 1.99, -75.51 +/- 1.81*, -73.62 +/- 1.36*. RMP = mean of 50 ms before the first intracellular stimulus. | SUPPORTED |
| A1.4 | sag 1.18 / 2.04 / 2.57 mV | Table 1: 1.18 +/- 0.24, 2.04 +/- 0.44*, 2.57 +/- 0.42*. Fig 6B printed p 0.04761 and 0.00322. | SUPPORTED |
| A1.5 | rebound 0.96 / 1.24 / 1.86 mV | Table 1: 0.96 +/- 0.19, 1.24 +/- 0.58, 1.86 +/- 0.44*. Fig 6C: p 0.24947 (WT vs HT), 0.00393 (WT vs KO, bracket drawn WT to KO). | SUPPORTED |
| A1.6 | "-200 pA protocol", 500 ms | Methods: "hyperpolarizing pulse of -200pA" inside a series of 500 ms current pulses; Fig 6A/B time axis puts the step at roughly 0.08 to 0.56 s. The duration of the -200 pA step itself is therefore read from the general 500 ms statement plus the figure, not stated for that step alone. | SUPPORTED (500 ms is inferred from the general statement and the figure) |
| A1.7 | cells/animals 13/5, 15/6, 40/15 (PY); IN 5/4, 6/5 | Table 1 last row "N's (# cells/# animals)". Fig 6B/C legend: "average +/- SEM for all animals tested". The analysis unit (cell or animal) is not declared. | SUPPORTED |
| A1.8 | bursting 36/42 (24 mice), 4/23 (14), 0/11 (7) | Results first section, verbatim: "0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice". Median inter-burst interval 26.2 s, "2.29 [1.1-4.2] bursts/minute" in the text. | SUPPORTED |
| A1.9 | Supplement Table S1 baseline frequency 0.84 bursts/min vs 2.29 in the text | Supplement docx Table S1: baseline "Frequency (bursts/min) .84 [.57-.1.53]; min 0.36, max 3.89"; N 119 bursts/18 slices/9 animals. Text: 2.29 [1.1-4.2]. Both as printed; the producer's flag is right. | SUPPORTED |
| A1.10 | How pyramidal identity was confirmed | Methods: "Putative pyramidal neurons were identified based on their appearance under the infrared filter and their electrophysiological features. They were later confirmed based on comparison of the spike-half width, input resistance, and membrane time constant." Rin and tau are criteria and outcomes. No morphology, biocytin or marker. | SUPPORTED |
| A1.11 | Access-resistance tolerance | "Cells were not used if the access resistance was >40 MOhm and if they had an unstable membrane potential." Access resistance "monitored throughout"; no value, no distribution by genotype, no bridge-balance or series-resistance compensation statement. | SUPPORTED |
| A1.12 | Junction-potential statement | "We did not correct for liquid junction potential since all results central to the hypothesis were measured against a change from wildtype littermate controls." (24 words). | SUPPORTED |
| A1.13 | F-I slope (Supp S4) | Results: slope WT 0.184 +/- 0.044, HT 0.162 +/- 0.037, KO 0.204 +/- 0.070 Hz/pA; p 0.1902 (WT-HT), 0.3669 (WT-KO). Supp S4 image viewed: four asterisks at about 80, 100, 120, 140 pA in a1 (raw current), none in a2 (aligned to 20 pA below rheobase). Supplement legend lists p 0.0124, 0.0237, 0.0348, 0.0436. | SUPPORTED |
| A1.14 | Intrinsic properties recorded under synaptic blockade? | Not stated, and the section "Pharmacology" lists the only drugs used: TTX 1 uM, d-APV 50 uM, CBX 100 uM, BB-FCF 10 uM. TTX is tied to mEPSC recordings; none of the four is an AMPA or GABA-A antagonist; no picrotoxin, bicuculline, gabazine, CNQX, DNQX, NBQX or kynurenic acid appears anywhere in the main text or supplement (text search). I conclude (INFERENZA) that the intrinsic-property recordings were most probably made without a synaptic blocker. The producer's "not stated" is true but understates what the Methods let one conclude. | PARTLY (true, but the exhaustive drug list is not used) |
| A1.15 | Internal and external solutions, temperature | Internal (pipette 3-5 MOhm): 135 K-gluconate, 1 MgCl2, 10 NaCl, 2 Na2ATP, 0.3 NaGTP-Tris, 10 NaHEPES, 0.5 EGTA, 0.0001 CaCl2, pH 7.2-7.3, 270-290 mOsm (no titrating base stated, so K+ could exceed 135). External: the ACSF given is the incubation ACSF (123 NaCl, 25 NaHCO3, 10 glucose, 3.5 KCl, 1.3 MgSO4, 1.2 NaH2PO4, 1.5 CaCl2); "kept at 35 for 30 min ... experimentation at 35". A separate recording ACSF is not described, so "3.5 mM K+ in the bath" is the natural reading, not a declared bath value. Cutting solution 2 mM KCl. | SUPPORTED (with the caveat that the recording bath is inferred from the incubation ACSF) |
| A1.16 | Supplement content on Ih, HCN, Kv7, K2P, Kir, Ba2+, Cs+, capacitance | Text search of main text and supplement docx text: no HCN, Kv7, KCNQ, K2P, Kir, TASK, TREK, XE991, Ba2+, Cs+; "capacitance" does not occur at all (so capacitance is never reported; the producer's C is derived). "Ih" and "ZD7288" occur only in the Discussion, as cited literature. | SUPPORTED |
| A1.17 | O04 caveat "p values ... not labelled by comparison" | The legend does not label them, but the Fig 6B bracket graphic does: "*" spans S-WT to S-HT and "**" spans S-WT to S-KO; Fig 6C has one "*" from S-WT to S-KO. | PARTLY (labelled in the figure, not in the legend) |
| A1.18 | O04 "graded with gene dose" | Means are monotone (1.18, 2.04, 2.57). HT vs KO from the printed summary, assuming "+/-" is SEM (Fig 6B legend says SEM and the bar whiskers match Table 1): sag difference 0.53 mV, SE 0.61, t of about 0.9; RMP difference 1.9 mV, SE 2.3, t of about 0.8. HT and KO are not distinguishable. A "gradient" is a description of three means, not a tested dose effect. | PARTLY (INFERENZA, not DATO) |
| A1.19 | O10 "a few example KO traces in Fig 6A show small rebound spikes at step offset" | Enlarged Fig 6A (KO pyramidal): after the -200 pA step the trace shows a slow depolarising bump of a few mV from about -65 to about -61 mV, nothing near spike threshold (about -41 mV). No rebound spikes are visible in any of the three pyramidal examples. | NOT SUPPORTED |
| A1.20 | O05 "example traces in Fig 6A reach a similar plateau near -100 mV in all three genotypes" | Enlarged: WT rest about -77, plateau about -99; HT rest about -72, plateau about -101; KO rest about -65/-66, plateau about -97/-98 with an early peak near -100/-103. The KO example is much more depolarised at rest than the KO group mean (-73.6). Single cells, so the producer's own caveat stands. | SUPPORTED |
| A1.21 | O06 "peaks lie at or below E_K in HT and KO" | WT's estimated peak (-101) is also below E_K (-97/-98) by about 3 mV on the recorded scale; the statement singles out HT and KO as if WT were above. | PARTLY |

Other Table 1 values quoted by the producer (AP threshold -43.77/-40.3/-41.32; AP amplitude 76.30/68.77*/68.67*; interneuron entries) match the table.

### A2. 34018186 (Iacone 2021)

| # | Item | What I found | Verdict |
|---|---|---|---|
| A2.1 | Rat age, layer | Methods: "Male Wistar rats and GAERSs (both 25-35 days old)", 320 um coronal slices, 35 C. Cortical cells: "cortical initiation network" layer 5/6 pyramidal neurons of Wistar rats (Fig 5 legend: "Layer 5 pyramidal neuron"); n = 6 given for the spike counts, per-cell lines in the RMP panel show 6. | SUPPORTED |
| A2.2 | Concentration in text vs legend | Results: "IVA (3 umol/L) blocked the characteristic depolarizing sag". Fig 5 legend: "before (control) and during application of 30 umol/L IVA" (both neuron examples). Unresolved in the paper. | SUPPORTED (discrepancy confirmed) |
| A2.3 | Free brain concentration with and without elacridar | Results: 184 +/- 67.8 nmol/L (ELA + IVA 30), 4.7 +/- 0.1 nmol/L (VEH1 + IVA 30), 2 h after oral dosing in GAERS. Fig 1C/D (viewed): n = 4 and n = 2 animals; the four elacridar brain points run from about 40 to about 360 nmol/L. The producer does not give n or the spread. Wistar 1 h: 307 +/- 53.0 (5 mg/kg ELA) vs 128 +/- 28.4 nmol/L (2.5 mg/kg). | SUPPORTED (n and range missing from the producer's rows) |
| A2.4 | Injection design | Oral IVA after intravenous elacridar (or vehicle) pretreatment under brief isoflurane, 20 min earlier; crossover design with at least 5 days between treatments; microinjection 6 nmol per side over 2 min into CIN or VB. | SUPPORTED |
| A2.5 | "96 percent in CIN against 40 percent in VB" | Results: AUC time in seizure 96% smaller after CIN injection (p < .0001, n = 5 v 5); VB 40% reduction (p = .05, n = 7 v 5). | SUPPORTED |
| A2.6 | Slice concentration 16-160 times in-vivo free level | 3 umol/L / 0.184 = 16; 30 umol/L / 0.184 = 163. | SUPPORTED (arithmetic) |
| A2.7 | "Ivabradine blocked/removed the sag" (T01; MH2 step 3 "removes") | Fig 5 (viewed; panel letters in the image differ from the legend letters): cortical sag at -200 pA about 2.65 mV in control and about 1.4 mV with ivabradine, significant from -200 to -120 pA only; thalamic about 2.8 to about 1.45 mV, significant at -200 and -180 pA only. A reduction of about half, with a residual sag of about 1.4 mV. The text verb "blocked" is the authors'; the figure shows a partial reduction. The legend says "decreased". | PARTLY (the producer's wording repeats the verb, the figure shows a partial effect) |
| A2.8 | RMP effect (producer: "magnitude only in Fig 5D, not viewed") | Fig 5 RMP panels: cortical about -61.8 to about -65.7 mV (n = 6, five of six cells hyperpolarised, one slightly depolarised); thalamic about -65.3 to about -67.5 mV (n = 10). Rin is not shown in Fig 5. | SUPPORTED (now measurable; producer's note is stale) |
| A2.9 | What was measured for sag and RMP | Sag amplitude versus injected current from -200 to -20 pA (steps of 20 pA); RMP in control and during drug in each cell. Example traces: -200 pA and +80 or +100 pA steps. Example-cell holding potentials -58 and -61 mV (legend). Liquid junction potential -13 mV corrected offline (so these potentials are on a corrected scale; 34634460 is not). | SUPPORTED |
| A2.10 | Other effects omitted by the producer | Ivabradine reduced the number of spikes evoked by a low-threshold spike: cortical 2.5 +/- 0.28 to 1.0 +/- 0.4 (n = 6), thalamic 5.3 to 4.5 (n = 10) (both p < .05); spikes from depolarising steps, AP amplitude and threshold unchanged. T01 reports only the unchanged ones. | PARTLY (omission; relevant to rebound) |
| A2.11 | Recording bath K+ | Recording aCSF: 130 NaCl, 3.5 KCl, 1 KH2PO4 (so 4.5 mM K+), internal 126 K-gluconate + 4 KCl (130 mM K+). Not used by the producer. | context |

### A3. 24953239 (Cain 2015)

| # | Item | What I found | Verdict |
|---|---|---|---|
| A3.1 | Rin | Fig 1d (viewed): P15-P20 NEC about 305, GAERS about 265 Mohm; adult NEC about 230, GAERS about 175 Mohm; both starred. Definition (Results): "maximum change in membrane potential upon hyperpolarization during a 1,000-ms current injection divided by the current injected", i.e. a peak-based Rin that includes the sag and is not the steady-state slope used in 34634460. | SUPPORTED (values); definitional difference confirmed |
| A3.2 | RMP | Fig 1e: about -73 mV in all four groups, text: "measurements of resting membrane potential were not significantly different". | SUPPORTED |
| A3.3 | Ih density | Fig 3b (viewed), P15-P20 at -110 mV: NEC about -3.3, GAERS about -5.9 pA/pF; Fig 3c adult: about -6.2 vs about -8.8. Tail currents of the ZD7288-sensitive component, 20 uM. V50 -86.2 vs -86.5 mV, slope 4.2 vs 5.1 (text). Fig 3d: a small but significant leftward difference in the normalised current at -80 to -65 mV in P15-P20 GAERS, not mentioned by the producer (A3.7). | SUPPORTED |
| A3.4 | Sag unchanged | Table 1: pre-epileptic NEC 4.99 +/- 0.43, GAERS 5.81 +/- 0.52 mV; adult NEC -4.22, GAERS -3.93 (sign as printed). | SUPPORTED |
| A3.5 | ZD7288 effects | 20 uM: sag falls to 0.39 / 1.02 (P15-P20 NEC / GAERS) and 0.99 / 2.13 (adult) mV; Rin falls (Fig 6d: about 305 to about 278 and 265 to 218 at P15-P20; about 230 to about 156 and 175 to 138 adult); resting potential falls by about 17 mV (Fig 6e: about -73 to about -91; about -74 to about -90). The producer's rows give sag and Rin but not the size of the hyperpolarisation, and quote the pre-burst potential (-78 to -95) in its place. | SUPPORTED (producer omits the roughly 17 mV hyperpolarisation, which matters for any Rin comparison before and after) |
| A3.6 | "Authors read the Ih rise as non-restraining at most" (MH2 step 5) | Discussion: "suppressed burst-firing in these neurons would be expected to reduce absence seizures"; they raise the possibility of a compensatory response, then say "any apparent compensation is unlikely to be directly related to the development of SWDs". They do not call the rise harmful. The statement "do not read their increased Ih as restraining seizures" is not accurate as written: they read it as expected to be restraining via burst suppression and then say the pattern does not explain SWD development. | PARTLY |
| A3.7 | Selection and contamination caveats not carried | Current-clamp neurons "that did not exhibit burst-firing ... in response to depolarizing current steps were discarded" (a selection on burst-firing). The authors state that the ZD7288-subtracted current may be contaminated by T-type window current (they cite one report of partial T-type block). Both are direct, independent support for the producer's E2 design (second chemotype, no single-drug subtraction) and are not used. | held, not used |

---

## B. Calculations (recomputed, no tool but arithmetic)

### B1. Implied capacitance, tau / Rin

Ratio of group means (the only thing the table allows):

| Genotype | tau / Rin | Propagated relative uncertainty if "+/-" is SEM and tau, Rin are independent | C (pF) |
|---|---|---|---|
| WT | 18.55 ms / 102.88 Mohm | sqrt(0.114^2 + 0.082^2) = 0.14 | 180.3 +/- 25 |
| HT | 18.79 / 143.26 | 0.14 | 131.2 +/- 19 |
| KO | 21.25 / 143.03 | 0.095 | 148.6 +/- 14 |

The producer's 180 / 131 / 149 pF reproduce. Assumption and limit: this is a ratio of means; a mean of per-cell ratios would be larger by roughly 1 + CV(Rin)^2 (CV(Rin) about 0.4 if "+/-" is SEM, so about +15-18 percent), nearly the same in the three groups, so it would shift all three values together and leave the ordering unchanged; the covariance of tau and Rin within cells is unknown and cannot be recovered from the table. With the propagated uncertainty above, WT minus HT is 49 pF with SE 32 (z about 1.6) and WT minus KO is 32 pF with SE 29 (z about 1.1). The direction "capacitance lower in the mutants" follows from the means; it is not established as a difference. HT (131) is also below KO (149), so the implied C does not follow the dose order, unlike Rin, RMP and sag.

Does "tau nearly flat while Rin +39 percent" argue against a pure leak loss at constant capacitance? At constant C, tau should scale with Rin: predicted 25.8 ms in HT and KO against 18.8 (1.77 SEM, about 3.9 SE below) and 21.3 (1.53 SEM, about 2.9 SE below). It follows, under the single-compartment assumption, that a pure leak loss at constant C does not fit by itself. It follows with a caveat the producer states only in part: tau comes from a 50-60 ms exponential of a small step and Rin from an I-V slope of unstated range, in a non-uniform neuron; a voltage-dependent conductance active in the fit window (Ih activating, shortening the apparent tau) would also lower tau relative to Rin. So flat tau supports "something besides a pure leak loss", not specifically "smaller cells". Verdict on the inference: SUPPORTED as "against pure leak loss at constant C", PARTLY as "smaller cells".

### B2. E_K and the -200 pA peaks

Nernst, 35 C, K+ out 3.5 mM: internal 135 mM gives -97.0 mV; 140 mM gives -98.0 mV; at 34 or 36 C the figures move by 0.3 mV; 130 mM gives -96.0 mV. The producer's "about -98 mV" is within 1 mV of the declared solutions and within about 2 mV if internal K+ is somewhat below 135. Activity coefficients of the same order inside and out cancel to first order.

GHK: E_K is by definition the Nernst value; a GHK correction matters only if one asks where the membrane would rest or where a mixed-cation current reverses. With 3.5 mM K+ outside, a 1 percent Na+ permeability moves a GHK potential from -97.0 to about -89 mV (2 percent: about -83 mV), so a "leak" difference current with small Na+/cation permeability would reverse several mV positive of E_K. The producer's "should vanish near E_K" is therefore a prediction good to a few mV for a K-selective conductance, not to 10 mV. Cl- with 12 mM inside and 130 mM outside moves it by a further 1-2 mV for P_Cl/P_K of 0.05-0.1.

Estimated peaks (recomputed): deflection Rin x 0.2 nA = 20.6 / 28.7 / 28.6 mV; peak = RMP - deflection - sag = -101.0 / -106.2 / -104.8 mV; sag over (deflection + sag) = 5.4 / 6.6 / 8.2 percent. All reproduce. Fig 6A examples are consistent (HT deflection about 28.5 mV; WT about 22-23; KO about 31).

Junction potential. The correction direction matters and the producer's step 5 does not carry it: E_K needs no junction correction (it is a property of the solutions); the recorded potentials do. For a K-gluconate pipette the recorded potentials are too positive by the liquid junction potential: the two companion papers corrected -13 mV (34018186, "-13 mV ... corrected offline") and +13.3 mV (24953239, K-gluconate-based internal, corrected off-line), and a Henderson estimate with the declared 34634460 solutions (approximate mobilities from memory, so a rough figure only) gives about 14 mV. Taking about 13 mV (INFERENZA; not measured in this paper):

| | recorded | corrected (-13) |
|---|---|---|
| rest WT / HT / KO | -79.3 / -75.5 / -73.6 | about -92 / -88 / -87 |
| -200 pA peak WT / HT / KO | -101 / -106 / -105 | about -114 / -119 / -118 |
| distance of peak below E_K (-98) | 3 / 8 / 7 | about 16 / 21 / 20 |
| K+ driving force at rest | | about +6 / +10 / +11 mV (outward) |

The genotype contrasts (differences in rest, deflection, sag) are untouched by a common offset, as the authors say. What changes is the absolute position. On the recorded scale the peaks are 3-8 mV below E_K ("near E_K"); on the corrected scale they are 16-21 mV below it, where a K+ conductance carries inward current with a driving force larger than at rest. So MH1 step 5 ("at those potentials ... the K+ leak current is small or reversed, so a K-leak difference ... should vanish near E_K") does not follow: reversed yes, small no, and a K+ conductance difference would still contribute to the deflection at the sag peak (the conductance difference implied by Rin, about 2.7 nS, times 16-21 mV is of the order of 40-55 pA, a fifth of the injected current, an order-of-magnitude statement that is already inside the measured Rin). The prediction "difference current vanishes near E_K" stays valid for the voltage-clamp experiment E3 (zero crossing at the corrected E_K), not for the sag peak. Verdict: calculation SUPPORTED; inference at step 5 NOT SUPPORTED as worded.

Also unaddressed: a seal (pipette-membrane) leak that is constant across cells depolarises a high-Rin small cell more than a low-Rin large one (roughly rest shift = -V x G_seal / (G_cell + G_seal): with a 1 GOhm seal about 7 mV for Rin 103 Mohm and about 10 mV for 143 Mohm, so a 2-3 mV genotype difference from size alone; with 2 GOhm about half of that). This is INFERENZA with an invented seal value, offered only to show that MH1 step 3 ("a smaller cell does not by itself depolarise rest") and alternative A05 ("a seal leak does not fit Rin up") are both too strong in combination: smaller cell plus a fixed seal leak predicts Rin up, rest depolarised, tau flat.

### B3. Sag fraction and the crude "residual" (MH2 step 2)

Propagating the table SEMs (independence assumed, no per-cell covariance) the sag fraction 5.4 / 6.6 / 8.2 percent carries uncertainties of about 1.2 / 1.6 / 1.3 points; WT versus KO z about 1.6, WT versus HT z about 0.7. The "fraction still rises" premise is not established from the printed summaries; per-cell sag, Rin and deflection are needed (covariance of sag and Rin within cells would shrink the error, and cannot be known). Separately, Ih activation is steeply voltage dependent, so a sag fraction can rise with unchanged HCN density when the step reaches 4-5 mV deeper; a crude fraction is not a matched comparison. The producer already says "crude group means"; I add the uncertainty and the nonlinearity. Printed p values: under SEM and cells as units WT versus KO sag gives t of about 2.9 (printed 0.0032, same order) but WT versus HT t of about 1.7 (printed 0.0476, not reproduced), as earlier packages found.

---

## C. Logic of the three hypotheses

### MH1 (passive size / leak reading of Rin, sag and rebound)

* Labels. Step 1 DATO correct. Step 2 INFERENZA correct, but it needs the uncertainty of B1 (C lower is not a tested difference). Step 3 INFERENZA correct and follows (B1); the sentence "a smaller cell does not by itself depolarise rest" is true only without seal leak (B2). Step 4 INFERENZA correct; "with no change in HCN" is the hypothesis, not what the arithmetic shows (the arithmetic shows that a larger deflection can raise sag and rebound in mV). Step 5 INFERENZA mislabelled as a safe consequence: see B2, it does not follow once the junction offset is applied to the measured potentials. Step 6 correctly "none".
* Competing explanation. MH2, A04, A05, A06 each predict something different at matched potential and deflection, so they are really competing. A03 + seal leak (above) is a competitor the table lacks.
* Counter-evidence and weakening. The HT-versus-KO "same deflection, different sag and rest" point is cited as counter-evidence against MH1; it rests on differences with t of about 0.9 and 0.8 and does not weaken MH1 (A1.18). The weakening result in the column is partly written as a confirming outcome ("removes the genotype difference ... AND capacitance lower"); the failing outcomes are in the second sentence and are right (sag remains at matched conditions; C unchanged with Rin higher; no reversal near E_K).
* Discriminating experiment. E1 plus E3 separates passive size/leak from a non-passive sag remainder if capacitance is measured in the same cells. It cannot separate: an HCN density difference from an HCN gating or modulation difference (needs E2), HCN from other time-dependent hyperpolarisation-activated or deactivating components (M-current deactivation, T-type de-inactivation for rebound), or leak loss from a Kir or K2P difference (Ba2+ is not selective). Neither a harmful reading of an increased current nor a drug-response-as-defect step appears.
* Verdict: PARTLY. The qualitative logic (flat tau, Rin up) is sound; the quantitative support (C lower, step 5, HT-KO gradient) is weaker than written.

### MH2 (HCN contribution after matching, tool arm only)

* Labels. Step 1 DATO correct. Step 2 INFERENZA correct, premise not yet established (B3). Step 3 labelled DATO (transfer) correct as a transfer; "removes the sag" is stronger than Fig 5 (about half) and than the thalamic ZD7288 sag (residual 0.4-2.1 mV, from 4-6) (A2.7, A3.5), so "contributes to" is the supported verb. The off-target items are labelled abstract level, which is right. Step 4 INFERENZA correct. Step 5: "an increased Ih is not assumed harmful" is right; the GAERS sentence is inexact (A3.6); the A09 comparison (more Ih with lower Rin, unchanged rest) uses Rin defined at the peak (A3.1) and a thalamic cell, so it is a weak breaker of the cortical pattern, as the producer labels it ("transfer").
* Competing explanation. MH1 predicts no residual at matched conditions and no genotype difference in ZD7288 or ivabradine-sensitive current per pF; MH2 predicts both; they differ. The T-type, Na+ and isoform/compartment competitors listed are real and predict different things to the second chemotype and voltage-clamp subtraction.
* Weakening result. Right and sufficient: no excess at matched potential and deflection, or identical blocker-sensitive current density and V1/2.
* Discriminating experiment. E1 then E2 then E4 can separate HCN difference from passive size. It would fail to separate: Ih density from cAMP-dependent gating shift without a gating protocol, dendritic from somatic Ih (space clamp is named in the producer's cost note), and HCN from ZD7288's Na+ and T-type actions unless a second chemotype and a Na+ check are run (named). The thalamic paper's own caution that a ZD7288-subtracted current can be contaminated by T-type window current (A3.7) is a further reason for the second chemotype.
* Increased current treated as harmful? No. Drug response as proof of defect? No; step 3 explicitly limits itself to "HCN contributes to sag in those cells".
* Verdict: PARTLY (sound design; premise and two wordings need correction).

### MH3 (design control: state, selection, maturation)

* Labels. Step 1 DATO correct. Step 2 INFERENZA: "should LOWER Rin" for synaptic drive or raised extracellular K+ is not sourced; synaptic shunting plausibly lowers Rin, raised [K+]o has opposite effects through Kir (conductance rises with [K+]o) and through rectification, so the premise is IPOTESI for [K+]o and INFERENZA for synaptic shunt. Step 3 INFERENZA: the HT argument assumes the recorded HT cells came from the 83 percent non-bursting HT slices, which the paper does not link cell by cell; and HT slices do differ from WT in the synaptic recordings (Fig 4 legend: mEPSC amplitude and frequency S-WT versus S-HT, KS p 1.98e-04 and 0.0018, pooled events), so a synaptic state without bursts is not excluded. Step 4 DATO correct. Step 5 INFERENZA correct; "cell-autonomous" is over-read: with a pan-neuronal Synapsin-Cre deletion, persistence under synaptic blockade shows the difference is intrinsic to the recorded neuron's membrane, not that Wwox acts cell-autonomously; that needs sparse or mosaic deletion.
* Competing explanation. Real: MH1/MH2 as genuine intrinsic differences predict persistence under blockade; A05/A06 predict shrinkage; A04 predicts a smaller sag; they differ.
* Weakening result. Written as the two outcomes of the experiment; adequate.
* Discriminating experiment. E1 variants plus E5 separate state from intrinsic and maturation from genotype. They cannot separate selection by Rin and tau from a true difference unless identity is by morphology or marker (named), and cannot test the Wwox cell-autonomy of the change.
* Producer's open datum. "The answer to the blockade question is not in the paper": the Methods "Pharmacology" list (A1.14) is an indirect answer (no AMPA or GABA blocker listed), which the producer should state; it lowers the weight of "any report from the original authors" as the decision-changing item without removing it.
* Verdict: SUPPORTED as a design control with two wording corrections; its premise is stronger than the producer says (probable absence of blockers).

---

## D. Probes

| Probe | Mechanism claim and limit against source | Depth I can confirm | Verdict |
|---|---|---|---|
| Ivabradine | HCN blocker, "a nonselective inhibitor of HCN channel isoforms" (Discussion) confirmed. The class label "open-channel" does not occur in 34018186, 24953239 or 34634460 (text search); it comes from outside the cited sources. Limits (elacridar dependence, 96 v 40 percent, concentration discrepancy, 16-160 fold) confirmed. "Fig 5 image unreachable" is stale: sag reduced about half, RMP about -61.8 to -65.7 mV (cortical). Missing: n = 4 and 2 for the free-brain figures; effect on LTS-evoked spikes. | full_text_read, Figs 1, 2, 4, 5 viewed | PARTLY (delete "open-channel" or source it) |
| ZD7288 | Sag and Rin and hyperpolarisation from 24953239 confirmed (the roughly 17 mV hyperpolarisation absent). Off-target statements match the abstracts: Na+ in DRG and Nav1.4 (22989944, "ZD7288 inhibits not only HCN channel currents"), extracellular T-type block in CA1 (18534748, "ZD 7288 blocked T-type currents when applied extracellularly, but not when included in the recording pipette"), IC50 about 100 uM in spermatogenic cells and all cloned T-type channels (14575712). The IC50 values for Na+ "carried from hcn_20261107" cannot be confirmed from the abstract. The 20 uM used in VB neurons is a fifth of the spermatogenic-cell IC50, which is not a statement about CA1 or layer II/III (the CA1 concentration-response is in the full text only). | abstract_only (three), full_text (24953239) | PARTLY (Na+ IC50: UNVERIFIABLE) |
| Second chemotype / HCN4-preferential blocker | "Recent development of a preferential HCN4 blocker" is in the Discussion of 34018186, no primary source. | text | SUPPORTED |
| Retigabine | Abstract confirms hyperpolarising shift for KCNQ2/3, KCNQ2, KCNQ3, KCNQ4, not KCNQ1, native M channels in rat sympathetic neurons, hyperpolarisation and fewer spikes in unclamped neurons. The class label "Kv7 (KCNQ2-5)" and the hypothesis wording "KCNQ2-5" go beyond the abstract: KCNQ5 is not in it. The lower Rin after an opener is a physical inference, not in the abstract. | abstract_only | PARTLY |
| SCR2682 | EC50 9.8 +/- 0.4 nM, about 100-fold more potent than retigabine, native M-current in rat hippocampal or cortical neurons, W236 confirmed. "cultured, per the abstract": the abstract does not say cultured (the term is a MeSH heading only). The hypothesis text groups both openers as "non-cortical or cultured neurons"; SCR2682's abstract names cortical neurons. | abstract_only | PARTLY |
| XE991 | Not read, no claim made. | none | SUPPORTED (honest) |
| Z944 | "1 uM abolished burst-firing and T-type current (EC50 3.8 +/- 1.5 nM in P7-P9 VB neurons) without significantly altering HVA current; Rin and RMP unchanged (not shown)" matches the Results and Fig 5 legend as printed (an EC50 next to a single-concentration statement is odd and is the authors'). | text of 24953239 | SUPPORTED |
| Elacridar | 5 mg/kg intravenous: brain 259 +/- 57.6 to 622 +/- 107 ng/g; elacridar plus vehicle changed no seizure measure. | text | SUPPORTED |
| K2P / Kir tool class | "No primary paper establishing a mechanism usable in cortical layer II/III pyramidal neurons was located" is a narrow, defensible wording. The brief's wider formulation "no K2P or Kir tool paper" is false as stated: tool papers exist (ML133, Kir2 inhibitor, 21615117, with little selectivity within Kir2.x; ML335 and ML402, TREK-1/TREK-2 activators, 28693035), characterised in heterologous systems per the abstracts; none was shown by me to work in layer II/III pyramidal neurons. | abstract_only (mine) | see F |

Is the producer's abstention on a compound warranted by what was read? Yes for every candidate, with one qualification each:

1. HCN tools (ZD7288, ivabradine) are named as tools only, which is right. The one more primary read that would change what a tool arm can look like is the full text of Sanchez-Alonso 2008 (18534748) and Wu 2012 (22989944): concentration-response of Na+ and T-type block to set a ZD7288 concentration window. Both are unreachable here (PDF-only or not in the open-access bucket). It would change the design of E2/E4, not the abstention.
2. Kv7 openers: no Wwox M-current datum, no readout that discriminates; one more read (Methods of 31063701 for slice concentrations) would help design an arm and would not change the abstention.
3. K2P/Kir: abstention is right, because no Wwox datum gives a subtype; the thing that changes it is a Ba2+- or XE991-sensitive difference current in Wwox neurons, as the producer says, not another paper.

---

## E. Evidence rows

All 49 rows (V01-V49) checked, each quote against the text I read (efetch XML for V01-V41, PubMed abstracts for V42-V49; the reviewing text search for V36-V41).

* Verbatim at stated locator and at most 25 words: 49 of 49 (longest are V17 at 22 words, V08 at 24, V40 at 22; table-row quotes are reformatted for spacing and for the unicode minus, which I accept).
* Carrying the proposition they are attached to: 47 of 49.
* Defective, 2: **V49** is attached to O11 and A06 but its quote ("Blocking the Ih current ... modulated the elevated [K+]o ...") does not carry A06's claim that elevated [K+]o depolarises RMP (that is in the preceding abstract sentence and not quoted); **V22**'s note ("Magnitude only in Fig 5D, not viewed") is wrong in its panel letter (the legend letters and the image letters differ) and is now readable (A2.8).
* Three role labels are ambiguous, not wrong: V30, V31, V32 are labelled `counter` and each *supports* its observation T03/T04 (it counters only the transfer to Wwox).
* Counts: checked 49, correct 47, defective 2.

---

## F. Absence claims

| Claim | Perimeter stated | My assessment | Re-run |
|---|---|---|---|
| No Ih, Kv7, K2P, Kir, HCN protein or blocker datum in 34634460 or its supplement | main text and supplement docx | Adequate. I read the full text, every legend and the docx text, and searched both for HCN, Ih, ZD, Kv7, KCNQ, K2P, Kir, TASK, TREK, XE991, M-current, Ba2+, Cs+, ivabradine: only "Ih" and "ZD7288" in the Discussion as cited literature. Not covered: Supp images S1-S3 (captions concern LFP, PAC, NMDA field responses) and Fig 1-5. Also absent: capacitance, any synaptic-blocker statement for intrinsic recordings. | full re-run done, same result |
| No Wwox-HCN literature | PubMed strings in `queries.tsv` | Adequate for PubMed title/abstract/MeSH. | `WWOX AND (HCN OR "hyperpolarization-activated" OR "Ih current" OR "sag")` on 2026-11-08: 1 hit, 34634460 itself. |
| No Wwox-Kv7/K2P/Kir/potassium channel literature | same | Adequate. | `WWOX AND (Kv7 OR KCNQ OR "potassium channel" OR "M-current" OR "K2P" OR "Kir")`: 3 hits, none about Wwox neuronal physiology (an EEG cohort, a type 2 diabetes GWAS, a meningioma array study). |
| No K2P or Kir tool paper | Q04-Q07 strings (including one 0-hit long string and a 2-hit ML335 string) | Not adequate as a general statement: the long conjunctions in Q06 and Q07 are the kind that return 0 for syntactic reasons. Simple strings find tool papers: `ML133 Kir2 inward rectifier potassium channel inhibitor selective small molecule` gave 2 hits including 21615117; `TREK-1 activator ML335 K2P` gave 8 hits including 28693035 and 33127683. Adequate only in the narrower form "no tool paper shown to work in layer II/III pyramidal neurons" (not tested by me). | done, above |

---

## Corrections the producer must make

| File | Row / location | Correction |
|---|---|---|
| observations.tsv | O10 readout caveat text "a few example KO traces in Fig 6A show small rebound spikes at step offset" | Replace with "the KO example in Fig 6A shows a slow rebound depolarisation of a few mV after the step; no spikes are visible in any of the three pyramidal examples." |
| observations.tsv | O04 caveat "(not labelled by comparison)" and observation text "graded with gene dose" | The Fig 6B brackets label WT-HT (*) and WT-KO (**); state "HT and KO are not distinguishable from the printed means and SEM (t about 0.9)". Label the gradient INFERENZA. |
| observations.tsv | O06 | Add that E_K needs no junction correction, the recorded potentials do (about -13 mV: companion papers -13 and +13.3 mV; my Henderson estimate about 14 mV); corrected peaks lie about 16-21 mV below E_K; WT's recorded peak (-101) is also below E_K. |
| observations.tsv | O07 / O11 / hypotheses MH3 step 2 | State that Methods "Pharmacology" lists only TTX, d-APV, CBX and BB-FCF and no AMPA or GABA antagonist, so intrinsic recordings were probably unblocked (INFERENZA), instead of "not stated". |
| observations.tsv | O03 | Add the propagated uncertainty of C (about 14 percent; WT-HT z 1.6, WT-KO z 1.1) and that capacitance is never reported in the paper. |
| hypotheses.tsv | MH1 chain step 5 and counter-evidence | Reword: the K+ current at the sag peak is inward on the corrected scale and not small; the "vanishes near E_K" prediction belongs to E3, not to the sag peak. Drop or relabel as non-informative the HT-versus-KO "same deflection, different sag and rest" item (t about 0.9 and 0.8). |
| hypotheses.tsv | MH1 step 3 and alternatives A05 | Add smaller cell plus constant seal leak as a combination that predicts Rin up, rest depolarised and tau flat. |
| hypotheses.tsv | MH2 step 3 ("removes the sag") | Replace "removes" by "reduces" and give the size: ivabradine about 2.65 to 1.4 mV at -200 pA in cortical layer 5/6 (Fig 5, n = 6); ZD7288 to 0.4-2.1 mV in VB neurons. |
| hypotheses.tsv | MH2 step 5 GAERS sentence | Replace by: the GAERS authors expect the Ih-driven burst suppression to be seizure-reducing, discuss a compensatory origin and then state it is unlikely to be directly related to SWD development; they do not call the Ih rise harmful. |
| hypotheses.tsv | MH2 step 2 | Add that the sag fraction 5.4/6.6/8.2 percent is within about 1.6 propagated SE and that Ih activation is nonlinear in voltage, so a crude fraction is not a matched-condition residual. |
| hypotheses.tsv | MH3 steps 3 and 5 and discriminating experiment | HT slices differ from WT in mEPSC statistics, so a synaptic state without bursts is not excluded; persistence under blockade means "intrinsic to the recorded membrane", not "Wwox cell-autonomous" (pan-neuronal Cre). |
| probes.tsv | Ivabradine class | Delete "open-channel" or source it; update depth statement (Fig 5 viewed) and add n = 4 and n = 2 for the free-brain values and the LTS-spike effect. |
| probes.tsv | ZD7288 measured_in | Add the roughly 17 mV hyperpolarisation (Fig 6e) and that Rin in 24953239 is peak-based. |
| probes.tsv | Retigabine class; SCR2682 measured_in; hypotheses MH1 counter-evidence text | Remove "KCNQ2-5" (KCNQ5 not in 11466425's abstract); remove "cultured, per the abstract" and "non-cortical" for SCR2682 (abstract names hippocampal or cortical neurons). |
| probes.tsv | K2P/Kir row | State that tool papers exist (ML133 21615117, ML335/ML402 28693035) and narrow the absence claim to "none shown to work in layer II/III pyramidal neurons"; simple query strings return them. |
| evidence.tsv | V49 | Re-attach to O11 only, or add the abstract sentence that carries A06. |
| evidence.tsv | V22 | Update the note (magnitude now read from Fig 5; legend and image panel letters differ). |
| alternatives.tsv | A09 | State the peak-based Rin definition when using the GAERS Rin fall. |
| held_not_used.tsv | new rows | (a) Methods "Pharmacology" list of 34634460 answers part of the blockade question; (b) 24953239's own T-type window-current caveat on ZD7288-subtracted Ih. |

## Verdict per hypothesis

* MH1: PARTLY. Flat tau against Rin +39 percent argues against a pure leak loss at constant C (SUPPORTED); implied C, step 5 and the HT-KO gradient are weaker than written, and step 5 does not follow once the junction offset is applied.
* MH2: PARTLY. The design (matched conditions, two chemotypes, voltage-clamp subtraction, no compound ranked) is sound; the premise (a residual sag excess) is not established, "removes" overstates both drug effects, the GAERS sentence is inexact.
* MH3: SUPPORTED as a design control; wording corrections needed; its premise is stronger than the producer says.

## Count of checked items by verdict

Numbers and statements in A (A1.1-A1.21, A2.1-A2.11, A3.1-A3.7) plus the six separate verdicts in B (C arithmetic, "against a pure leak loss", "smaller cells", E_K, estimated peaks, step-5 inference) and the sag-fraction premise (B3), each counted once: SUPPORTED 33; PARTLY 8; NOT SUPPORTED 2 (A1.19 rebound spikes; B2 step-5 inference); UNVERIFIABLE 2 (the Na+ IC50 values for ZD7288 carried from 22989944; the sag-fraction premise of MH2 step 2, which needs per-cell data); rows with no verdict (A2.11 context, A3.7 held-not-used): 2. Evidence rows: 49 checked, 47 correct, 2 defective. Probes (the nine data rows of `probes.tsv`): SUPPORTED 4 (second chemotype, XE991 honesty, Z944, elacridar), PARTLY 5 (ivabradine, ZD7288, retigabine, SCR2682, K2P/Kir narrowed). Hypotheses: MH1 PARTLY, MH2 PARTLY, MH3 SUPPORTED (with wording corrections).

## What I could not reach or do

* The europepmc.org supplement and image paths (bot check) and the ebi.ac.uk supplement endpoint for PMC8609180 (connection refused on every try); the open-data bucket substituted for figures and the docx.
* Fig 1-5 of 34634460, Fig 3 of 34018186 and Figs 2, 4, 5 of 24953239 not viewed; Supp S1-S3 images of 34634460 not viewed.
* 22989944 and 11466425 full text (PDF-only), 31063701 full text (not open access), so Na+ IC50 values, ZD7288 and retigabine concentrations in neurons are unconfirmed.
* The junction potential for the 34634460 solutions was not measured; about 13 mV is a borrowed and estimated figure.
* Per-cell data (capacitance, access resistance, sag/Rin covariance) do not exist in the sources.

---

## Addendum, written after the verdicts above (README, engine_consumption and consumer_delta opened only now)

The three files carry the same statements as the TSVs, so the corrections above apply to them. Specific carry-overs:

| File | Location | Carry-over |
|---|---|---|
| README.md | Answer first 4 | "E_K about -98 mV ... (before junction correction) ... sag peaks at or below E_K ... K-leak difference should ... vanish near E_K": same defect as MH1 step 5 (B2). E_K needs no correction; the recorded peaks do, which puts them about 16-21 mV below E_K. |
| README.md | Answer first 5 | "HT and KO still differ in sag and rest; this is a non-passive component": the HT-KO difference is about 0.9 SE (A1.18); it does not support a non-passive component. |
| README.md | Answer first 6 and consumer_delta row 5 | "ivabradine and ZD7288 remove sag": ivabradine reduced cortical sag by about half at -200 pA (Fig 5), ZD7288 left 0.4-2.1 mV in VB neurons. "reduce" is supported, "remove" is not. |
| README.md | Answer first 3 | "smaller cells explain Rin but not the depolarised rest": add that a constant seal leak in smaller cells would depolarise them (B2). The capacitance figures carry about 14 percent propagated uncertainty (B1). |
| README.md | Answer first 7 | "an activity-driven state would lower Rin, not raise it": unsourced for raised [K+]o; HT slices also differ from WT in mEPSC statistics (MH3 section). |
| README.md | Not reached | "Figure images of 34018186; Figs 4 and 6 of 24953239 ...; Figs 1-5 of 34634460 and Supp S1 and S3": reachable. The PMC open-data bucket lists and serves figures and supplements of open-access deposits by plain `curl` (listing `https://pmc-oa-opendata.s3.amazonaws.com/?prefix=<PMCID>.1/&list-type=2`); I read Fig 5 of 34018186, Figs 1, 3, 6 of 24953239, Figs 1-6 of 34634460 (Fig 6 viewed) and the docx there. The producer's own list of what the three papers still do not offer (Rin in Fig 5, per-cell data) remains true. |
| README.md | Evidence line | "34634460 (partial_fulltext_read ...)" while observations and evidence rows say full_text_read for the membrane parts; use one depth word per source (receipts index decides). |
| consumer_delta.md | row 4 | "E_K (about -98 mV from the declared solutions before junction correction)": reword to "E_K about -97 to -98 mV from the declared solutions; recorded potentials need a junction correction of about -13 mV (not measured in 34634460)". |
| consumer_delta.md | row 2 | Add that Methods "Pharmacology" lists only TTX, d-APV, CBX and BB-FCF, so intrinsic recordings were probably unblocked (INFERENZA). |
| consumer_delta.md | row 7 | "no K2P or Kir tool qualified (PubMed strings in queries.tsv)": simple strings return tool papers (ML133 21615117; ML335/ML402 28693035); say "none shown to work in layer II/III pyramidal neurons". |
| engine_consumption.md | Format limits | Not verified by me (no validator run, no read of `repurposing_search.py`); the statements are plausible as descriptions and I make no claim on them. |

---

## Recheck (second look after the producer's corrections; narrow scope)

Scope: (1) whether each of the nine substantive errors plus the MH3 wording was corrected as meant and no new overstatement entered, in `hypotheses.tsv`, `observations.tsv`, `alternatives.tsv`, `probes.tsv` (and where I met them, `held_not_used.tsv`, `evidence.tsv`, `README.md`); (2) five figure-level numbers from `figure_notes.tsv`, looked at again in enlarged crops of the bucket images (same plain-curl route as before) and the Fig 2 mismatch; (3) the two new receipts (-52). All TSVs have equal column counts (hypotheses 11, alternatives 6, probes 7, observations 10, experiments 7, held_not_used 4, figure_notes 7, queries 6, evidence 9).

### 1. Were the corrections made as meant

| # | Error | Where now | Verdict |
|---|---|---|---|
| 1 | E_K / junction potential, MH1 step 5 | MH1 step 5, O06, O05, README line 4: E_K -97 to -98 mV needs no correction; recorded potentials need about -13 mV (borrowed, flagged as not measured, Henderson about 14 mV rough); corrected peaks about 16-21 mV below E_K; inward current not small; "reversal near E_K" moved to E3. | SUPPORTED. One stale copy remains: `held_not_used.tsv` row 4 (`how_it_enters_the_hypothesis`) still says "E_K about -98 mV ... puts the HT and KO sag peak at or below E_K" in the old uncorrected wording. Replace by the MH1 step 5 sentence. |
| 2 | O10 rebound spikes | O10: slow rebound depolarisation of a few mV, about -65 to -61 mV, no spikes in any of the three examples. | SUPPORTED |
| 3 | "removes" to "reduces", with sizes | MH2 step 3, T01, T04, README line 6, context column: about 2.65 to 1.4 mV (cortical), 0.4-2.1 mV residual (VB). | PARTLY. Three leftovers: `probes.tsv` Ivabradine, `selectivity_known_and_unknown`: "Known: sag blocked" (use "reduced"); `alternatives.tsv` A01 prediction "remove sag" and A08 "a blocker removes only the HCN part of sag" (both are predictions of those explanations, so tolerable, but "reduce" is safer and consistent). The verbatim quote V20 and receipt -51 keep the authors' "blocked", which is correct for a quote. |
| 4 | Implied-capacitance uncertainty | O03, MH1 step 3, A03, README line 3: about 14 percent (10 percent KO), WT-HT z about 1.6, WT-KO about 1.1, HT below KO, "a direction of means". | SUPPORTED. README line 3 ends "a pure leak loss does not fit" without the single-compartment caveat that MH1 step 2 and O03 carry; add "under the single-compartment assumption". |
| 5 | HT-versus-KO argument withdrawn | MH1 `counter_evidence` ("NOT used against MH1"), O04, MH2 step 2, README line 5, `held_not_used.tsv` row 3. | SUPPORTED |
| 6 | New alternative A10 | A10 present; cross-referenced from A05, MH1, E1. | PARTLY, with a new overstatement: A10 says it "Reproduces the whole triad plus flat tau with no change in any channel" and that the HT and KO shifts "are of that order". My own arithmetic (invented seal value, stated in A10) gives a 2-3 mV rest difference between genotypes at a 1 GOhm seal against 3.7 and 5.6 mV observed, and size has not been shown to differ (B1). Replace with: "can reproduce the direction of Rin up, rest depolarised and tau flat; at a 1 GOhm seal the size-driven rest difference is about half of the observed shift (illustrative, invented seal value)". A10's credit line "inference by the verifier and me" is accurate. |
| 7 | Probe wording | Ivabradine: "open-channel" removed and said so; retigabine: KCNQ2, KCNQ3, KCNQ2/3, KCNQ4, KCNQ5 not in abstract; SCR2682: "the abstract does not say whether cultured or in slices"; MH1 counter-evidence names "rat hippocampal or cortical neurons". | SUPPORTED |
| 8 | K2P/Kir absence | Probe row and MH1 `counter_evidence`: tool papers exist (ML133 21615117, ML335/ML402 28693035, "reported by the verifier, not read by me"), absence narrowed to "none shown to work in layer II/III pyramidal neurons". | SUPPORTED, with one unverified assertion: "my long conjunction strings returned 0 for syntactic reasons" is my inference, not a tested fact; say "probably". |
| 9 | GAERS sentence | MH2 step 5 and T03: authors expect Ih-driven burst suppression to be seizure-reducing, discuss a compensatory origin, say it is unlikely to be directly related to SWD development, do not call the rise harmful. | SUPPORTED |
| 10 | MH3 wording | Methods drug list as indirect evidence; shunting INFERENZA, raised [K+]o IPOTESI; HT mEPSC differences; "intrinsic to the recorded membrane", not Wwox cell-autonomy; sparse or mosaic deletion named. | SUPPORTED |

Other new content checked: MH2 `status` ("conditional, exploratory"), the V22 and V49 evidence repairs (V49 now says A06 does not rest on it) and the two new `held_not_used.tsv` rows are correct. No step treats an increased current as harmful or a drug response as proof of a defect.

### 2. Figure-level spot checks (enlarged crops; what I see)

| Producer number | What I see | Verdict |
|---|---|---|
| 34018186 Fig 5 cortical sag, about 2.65 to 1.4 mV at -200 pA, stars -200 to -120 pA | Control point at -200 pA is at about 2.65 (whisker to about 2.95), ivabradine about 1.40; stars under the five points from -200 to -120 pA; at -20 pA the two points coincide near 0.3. The figure does not print n. | SUPPORTED |
| Cortical RMP about -61.8 to -65.7 mV, n=6, five down and one up | Six paired lines; mean markers about -61.8 and about -65.7 (star); five lines fall (steepest from about -55.5 to -70), one rises from about -59.5 to about -57.5. | SUPPORTED |
| Thalamic sag about 2.8 to 1.45 mV; RMP about -65.3 to -67.5, n=10 | Control about 2.78 (whisker about 2.0-3.5) to ivabradine about 1.43; stars only at -200 and -180 pA; RMP panel: ten lines, all fall, means about -65.3 and about -67.5. | SUPPORTED. The thalamic control whiskers are wide (about +/-0.75 mV); the producer's "about +/-0.1 mV" precision applies to reading the dots, not to the data. |
| Fig 1 free brain about 5 nM without and about 184 nM with elacridar | Panel D: vehicle brain points at about 4 nM (two, n=2); elacridar brain points about 42, 120, 215 and 358 nM with mean about 184 and whisker to about 320; plasma points shown for comparison. Panel A: total brain about 260 vs about 620 ng/g (n=5 each). | SUPPORTED |
| CIN versus VB injection residual, about 0.03 versus about 0.6 | Fig 4 (file g001): ivabradine AUC bar about 0.03 against vehicle 1.0 (n=5 v 5); Fig 3 (file g003): about 0.6 against 1.0 (n=5 v 7), seizure number about 0.7, duration about 0.95. These bars are normalised to the vehicle group (the text says "96% smaller than VEH"), not to each animal's baseline; per-baseline time courses show CIN near 0 to 0.1 and VB about 0.3 to 0.8 with vehicle about 0.75 to 1.0. Say "relative to vehicle". Figure-internal oddities in Fig 3: the number time course carries "ns" while its AUC bar carries a star, and the duration time course carries "**" while its AUC bars are equal. | SUPPORTED as numbers; wording "of baseline" would be wrong |
| 24953239 Fig 6: ZD7288 hyperpolarisation about 17 mV | Vrest bars: P15-P20 about -73.5 (NEC) and -73 (GAERS) to about -91.5 and -91; adult about -74 and -72.5 to about -89.5 and -88.5. Shift about 17-18 mV at P15-P20 and about 15-16 mV in adults. | PARTLY: "about 15-18 mV" |
| Fig 6 Rin drop "about 10-35 percent" | Rin bars: P15-P20 NEC about 305 to 278 (-9 percent), GAERS about 266 to 218 (-18); adult NEC about 230 to 156 (-32), GAERS about 175 to 137 (-22). No star on any ZD7288 drop; the control NEC-GAERS stars are intact. | PARTLY: the range is about 9-32 percent; "35" is not read from the bars (T04, probes ZD7288, MH2 text if repeated) |
| Fig 4 HCN1/HCN3 protein | HCN1 about 0.96 (NEC) vs about 1.53 (GAERS, star); HCN3 about 0.31 vs about 0.60 (star); HCN2 about 0.80 vs 0.77; HCN4 about 0.04 vs 0.04 (axis to 0.10, bands faint). Four lanes per group shown; the text and legend say 12 samples from six animals. Within-isoform comparisons only, as the authors state. | SUPPORTED |
| Fig 2 oral dose-response: asterisk on ELA+IVA20 against p = .07 in the text | Confirmed and wider than the producer's note. B1 (time in seizure): ELA+IVA20 bar about 0.64 with a red single star, ELA+IVA30 about 0.50 with two stars; the text gives IVA20 .53 +/- .09, p = .07 and IVA30 .38 +/- .09, p = .0044 (62 percent). B2 (duration): IVA20 about 0.72, no star (text .66, p = .09 consistent); IVA30 about 0.53 with two stars (text .59, p = .008). B3 (number): IVA20 about 0.58 with a star (text .71, p = .24, no star expected), IVA30 about 0.32 with four stars (text .55, p = .01). The B3 panel legend lists VEH1+VEH2 n=8 against n=9 in the text legend. So bar heights as well as stars disagree with the text in B1 and B3 and in opposite directions (bars higher than text in B1, lower in B3); a uniform renormalisation does not explain it. Unresolved; Fig 2 is in vivo oral absence-model data and carries no hypothesis, so the oral percentages (62, 45, 41) should not be quoted as certain anywhere. | Mismatch CONFIRMED and extended; add the B1 and B3 value differences to the note in `figure_notes.tsv` F03 and T02's caveat |

### 3. Receipts -52

`FTR-20261108-34018186-52` and `FTR-20261108-24953239-52`: `source_fingerprint` values equal the SHA-256 of the efetch XML I fetched independently (ed1de0c5...772a4d for PMC9543052, e7407099...953f5e for PMC4435665), so the text read is the same document; DOIs correspond (10.1111/epi.16926; 10.1007/s00424-014-1549-4); `analysis_at` 22:50Z precedes `event_at` 22:57:07Z; `prior_receipt` chains to the -51 receipts and `reread_reason` `inadequate_prior_coverage` fits (figures captions-only before, all viewed after). The quoted loci are verbatim in my text ("Note the decreased depolarizing sag in the presence of IVA."; "IVA hyperpolarized the membrane potential of both neuronal types"; "decreased the input resistance (Fig. 6d) which is unexpected ..."). Coverage statements match what I could check: no tables in 34018186, no supplement in the bucket listings, Table 1 present in 24953239, references not read. One mismatch: the -52 receipt for 24953239 says all six figures were viewed; the observations (T03, T04) and figure_notes F10 say Figs 1 and 3 were viewed in Phase 1 and F07-F09 in this round, which is consistent with "all six" over the two rounds. SUPPORTED. I did not run `staged_receipt_check.py` (the brief forbids gates and tests of this kind for me).

### Further corrections requested

1. `held_not_used.tsv` row 4, `how_it_enters_the_hypothesis`: replace the old "at or below E_K" sentence with the corrected MH1 step 5 wording.
2. `probes.tsv` Ivabradine, `selectivity_known_and_unknown`: "sag blocked" to "sag reduced". Optionally A01 and A08 "remove(s)" to "reduce(s)".
3. `alternatives.tsv` A10: soften "Reproduces the whole triad ... with no change in any channel" as above and compare the 2-3 mV illustrative difference with the observed 3.7 and 5.6 mV.
4. README line 3: add the single-compartment caveat to "a pure leak loss does not fit".
5. `probes.tsv` ZD7288 and T04: "Rin lowered by about 9-32 percent" and "resting potential hyperpolarised by about 15-18 mV".
6. `figure_notes.tsv` F03 and `observations.tsv` T02: record that the Fig 2 bars also differ from the text values in B1 and B3 (list above) and that the oral reductions are not to be quoted; F04 and F05: state that the AUC bars are relative to vehicle.
7. `probes.tsv` K2P/Kir row: "returned 0 for syntactic reasons" to "probably returned 0 for syntactic reasons".

Verdict of the recheck: eight of the ten corrections are fully in place (items 1, 2, 4, 5, 7, 8, 9, 10; item 1 with one stale copy in `held_not_used.tsv`, item 4 and 8 with one-phrase edits); item 3 ("removes" to "reduces") has leftovers and item 6 (A10) introduced a mild new overstatement. Figure numbers: eight of ten rows SUPPORTED, two PARTLY (ZD7288 shift and Rin range), the Fig 2 mismatch confirmed and larger than noted. Receipts -52: SUPPORTED.
