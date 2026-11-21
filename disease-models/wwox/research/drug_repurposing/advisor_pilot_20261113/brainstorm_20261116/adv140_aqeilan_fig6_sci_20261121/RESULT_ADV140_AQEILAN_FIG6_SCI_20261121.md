# ADV-140 result: Fig. 6 of the Brain 2026 WWOX organoid paper, metric by metric (SCI window X, 2026-11-21; hypothesis level; no dose; reference genotype class only; not medical advice)

Pre-registration: `PREREGISTRATION_ADV140_AQEILAN_FIG6_SCI_20261121.md` (committed before any figure was opened for this assignment). Rules for MADE / VISUAL / NOT PRINTED / UNREADABLE are the ones fixed there. Source: Brain 2026, PMID 42397075, doi 10.1093/brain/awag239. Held bytes (root checkout `files/fulltext/`): the OUP accepted manuscript (text layout file, figure pages 32 to 36 and their image crops) and the bioRxiv v2 preprint (`PPR960425_..._bioRxiv-v2.full_layout.txt` and its Expanded View figures PDF). Every number below carries its version: **AM** = accepted manuscript, **PP2** = preprint v2 (posted 2025-09-25), **COM** = Bedrosian commentary (orients questions only).

## Answer first
1. **For hyperexcitability, the printed tests compare each genotype with WT and each genotype before and after treatment. They never compare WOREE with SCAR12, and never compare treated WOREE or treated SCAR12 with WT.** The two headline sentences ("approximately 3-fold higher" WOREE over SCAR12; restoration brought activity to "a level similar to the WT organoids") are therefore **NOT PRINTED** as comparisons in Fig. 6 (the 3-fold ratio is readable from bar heights, 0.257 against 0.075 Hz, but no test is shown on the figure; "similar to WT" is the absence of a bracket, with 3 WT organoids and 20 WT regions of interest).
2. **Two of the three activity metrics do not support "similar to WT" at face value.** Mean amplitude of treated WOREE is about 0.044 against WT 0.023 (about 1.9 times) and the share of active regions is about 70 percent against 45 percent, both unbracketed. Only event rate is indistinguishable from WT on the printed scale (both near zero). Treated SCAR12 amplitude (about 0.013) falls **below** WT (about 0.023); that is unbracketed too.
3. **The "active regions" metric is at ceiling in both untreated mutant groups (100 percent, no error bar).** It cannot separate WOREE from SCAR12 at baseline.
4. **The five metrics are not equally supported:** cortical markers (CTIP2, SATB2) are the only metric where a WOREE-specific restoration is MADE with named tests (WOREE untreated against WT, and WOREE treated against untreated). Radial glia state is **not in Fig. 6 at all** in either version; the AM puts it in Supplementary Fig. 10C-F (not obtainable) and PP2 in Fig. EV13 (held; scRNA, one batch, no test on cell fractions).
5. **A text-against-figure mismatch on the untreated week-16 radial glia (AM Fig. 2).** The Results say WOREE organoids show a "prominent increase" of total radial glia. The AM Fig. 2F bars give a WOREE radial-glia log2 fold change of about +0.07 and neurons about -0.05 (my bar measurement of Fig. 2E gives about +0.1 to +0.2 on the same quantity; blind reader about +0.07). The large effect (about +1.0) belongs to WWOX-KO, which the text then calls "more pronounced". The commentary also says the large expansion was "not consistently observed" in the patient-derived lines, which agrees with the figure and not with the first Results sentence. PP2 carries the same sentence.
6. **Rejecting observation (all five metrics MADE for both genotypes): not met.** Pre-registered predictions P1 to P3 held; P4 half held (see below).

## What Fig. 6 is (a correction of my own pre-reading assumption)
Fig. 6 is the AAV9-SynapsinI-WWOX experiment, not a baseline comparison. Week-10 organoids are infected with AAV9-EGFP (control) or AAV9-WWOX and read at week 16 (AM legend; PP2 Methods say week 11, an internal inconsistency in PP2). The WT arm is untreated (no WT plus AAV9-EGFP, no WT plus AAV9-WWOX): **the comparator for "similar to WT" is not vector-matched**. Baseline frequency, amplitude and active-region statements are read from the AAV9-EGFP groups of the same panel. The earlier week-7 comparison (cell-attached, spikes per neuron, AM Fig. 1D) is a different preparation and age.

## Five-metric table (WOREE and SCAR12 separately; version AM unless marked)
Preparation for rows 1 to 3: Ca2+ imaging of whole organoids, week 16, one experiment; legend n: **organoids** WT 3, SCAR12 EGFP 6, SCAR12 WWOX 8, WOREE EGFP 6, WOREE WWOX 6; event rate additionally **regions of interest** WT 20, SCAR12 EGFP 30, SCAR12 WWOX 30, WOREE EGFP 40, WOREE WWOX 40 (so about 5 to 7 regions per organoid). Test named: multiple t-tests with Benjamini-Hochberg false-discovery-rate control. Values are bar readings with my own measurement against the axis (reading error about 2 axis units; the blind reader's numbers agree within it). Marks are those printed on the figure.

| # | Metric | Statement (locator) | Genotype | Printed comparison and mark | Class |
|---|---|---|---|---|---|
| 1 | Event rate (Hz) | "firing rate of WOREE ... approximately 3-fold higher than that of SCAR12" (AM Results, layout file lines 1136 to 1139) | WOREE vs SCAR12 | Bars 0.257 and 0.075 (ratio 3.4); **no bracket between them**; the AM text cites Supplementary Fig. 9C (not obtainable), PP2 cites Fig. 6B and EV11 (EV11 is representative traces only) | **NOT PRINTED** (ratio readable; test absent) |
| 1 | Event rate | "significantly higher compared to the WT" (lines 1125 to 1127) | SCAR12 vs WT | WT about 0.001; SCAR12 EGFP 0.075; *** | MADE |
| 1 | Event rate | same | WOREE vs WT | WOREE EGFP 0.257; **** | MADE |
| 1 | Event rate | treatment effect | SCAR12 EGFP vs WWOX | 0.075 to about 0.003; **** | MADE |
| 1 | Event rate | treatment effect | WOREE EGFP vs WWOX | 0.257 to about 0.001; **** | MADE |
| 1 | Event rate | "a level similar to the WT organoids" (line 1129) | treated WOREE or SCAR12 vs WT | all three near zero on a 0 to 0.3 axis; no bracket | **VISUAL** (absence of a mark; 3 WT organoids; not an equivalence test) |
| 2 | Mean amplitude (dF/F0) | same sentences | SCAR12 vs WT | 0.023 vs 0.061; *** | MADE |
| 2 | Mean amplitude | same | WOREE vs WT | 0.023 vs 0.069; **** | MADE |
| 2 | Mean amplitude | treatment effect | SCAR12 | 0.061 to 0.013; *** | MADE |
| 2 | Mean amplitude | treatment effect | WOREE | 0.069 to 0.044; * | MADE |
| 2 | Mean amplitude | "similar to WT" | treated WOREE vs WT | 0.044 vs 0.023 (about 1.9 times); no bracket | **NOT PRINTED** (and the numbers do not look similar) |
| 2 | Mean amplitude | "similar to WT" | treated SCAR12 vs WT | 0.013 vs 0.023 (below WT); no bracket | **NOT PRINTED** (possible overshoot; no WT plus AAV9-WWOX arm to read it against) |
| 2 | Mean amplitude | WOREE vs SCAR12 | untreated | 0.069 vs 0.061; no bracket | NOT PRINTED (not claimed) |
| 3 | Active regions (percent) | text names "proportion of active regions of interest" higher than WT | SCAR12, WOREE vs WT | WT about 45; both EGFP groups 100, no error bar; ** and ** | MADE (ceiling: 100 percent in both, so the genotypes cannot be told apart) |
| 3 | Active regions | treatment effect | SCAR12 | 100 to about 60; * | MADE |
| 3 | Active regions | treatment effect | WOREE | 100 to about 70; * | MADE |
| 3 | Active regions | "similar to WT" | treated WOREE vs WT | 70 vs 45 (25 points); no bracket | **NOT PRINTED** |
| 4 | CTIP2 (fraction of nuclei, week 16) | text: lower in WOREE than WT, restored in WOREE; SCAR12 "similar to WT" (lines 1142 to 1147) | WOREE vs WT | medians about 6 vs 28; * | MADE |
| 4 | CTIP2 | restoration | WOREE EGFP vs WWOX | 6 to about 28; * | MADE |
| 4 | CTIP2 | SCAR12 | SCAR12 vs WT | medians about 34 and 28, no bracket | MADE only as a non-significant result; "already WT-like" is the absence of a mark (VISUAL as an equivalence claim) |
| 5 | SATB2 (fraction of nuclei, week 16) | same sentences | WOREE vs WT | medians about 12 vs 23; * | MADE |
| 5 | SATB2 | restoration | WOREE EGFP vs WWOX | 12 to about 35; * | MADE |
| 5 | SATB2 | SCAR12 | SCAR12 vs WT | medians about 25 and 23; no bracket | as CTIP2 |
| 6 | Radial glia state | "did not affect" radial glia after treatment (lines 1172 to 1176; Supplementary Fig. 10C-F) | WOREE only (scRNA); SCAR12 not stated | not in Fig. 6 or any held AM page; **PP2 Fig. EV13** (held): no differentially expressed genes between treated and untreated radial glia, cell-cycle overlap, no test on cell fractions, scRNA from one batch | **NOT PRINTED in AM Fig. 6; UNREADABLE for the AM supplement; PP2 only, WOREE only** |

Units and sample structure that bound every row (AM legend; PP2 Fig. EV10 and EV12 name the lines):
* Marker n is stated as organoids (WT 4, SCAR12 8, WOREE 7) and tests use a one-way analysis of variance; the dots drawn in some boxes outnumber the stated organoids, which suggests the field of view is a plotted unit (VISUAL from the image; I did not count dots).
* **Lines (PP2 EV10 and EV12):** each genotype is two lines pooled: SCAR12 = WPM S and WPM D, WOREE = WSM S and LM-iPS, n about 4 organoids per line. The AM legend does not say which lines enter Fig. 6; the AM mentions "one experiment" (replicates are biological and technical from one experiment). Independent differentiations are not stated for either version. **n is organoids (and regions of interest), not lines or differentiations, for every Fig. 6 metric.**
* **How much of the neuronal population carries the transgene is not in Fig. 6:** the AM panel A(i) is images only (a subset of NeuN-positive cells carry WWOX, sparse by eye); the quantification is in Supplementary Fig. 9A-B (AM, not obtainable) or PP2 Fig. EV10B (legend and n held; the bar page is a legend-only page in the held PDF). "Sufficient" is therefore tested at an unquantified, visibly partial transduction.
* **PP2 mRNA markers (Fig. EV12B and C, my reading of one 100 dpi page, not blind-checked):** SATB2 mRNA in SCAR12 EGFP reads about 3.8 against WT 1.1 (a bracketed difference whose endpoints I cannot resolve) and WOREE WWOX about 4.8 with an error bar of about 2.4 either way. The AM sentence "SCAR12 ... similar to WT" is a protein-by-immunofluorescence statement; the PP2 mRNA bar does not look similar to WT. Recorded as a version difference to re-read at full resolution, not as a finding.

## Version differences found (AM against PP2)
| Item | PP2 (preprint v2) | AM |
|---|---|---|
| Panel names | Fig. 6B activity; EV10 infection quantification; EV11 traces; EV12 markers per line; EV13 radial glia | 6A(ii) activity; Supplementary 9 and 10 |
| 3-fold statement | cites Fig. 6B and EV11 (traces) | cites Fig. 6A(ii) and Supplementary 9C |
| Infection timing | text week 10, Methods week 11 | text and legend week 10 |
| Lines per genotype | named (EV10, EV12) | not named in the legend |
| Methods for Ca2+ imaging | held (Fluo-5 AM loaded organoids, 10 Hz acquisition, amplitude defined as maximum dF over baseline) | in the Supplementary Methods (not obtainable) |
| Radial glia after treatment | Fig. EV13, no differentially expressed genes | Supplementary 10C-F (not obtainable) |

## Route results (dated 2026-11-21; none bypassed)
| Route | Result |
|---|---|
| OUP landing page for the Brain paper (doi redirect) | HTTP 403, Cloudflare "Just a moment" challenge at 14:03Z; no supplementary link reachable; recorded as a stop |
| Europe PMC record for the Brain paper | 200; not open access, not in Europe PMC, no supplementary files flagged (`hasSuppl` N) |
| E-MTAB-14792 (re-check, one probe each) | BioStudies API 403 "Study not accessible"; BioStudies page 200 but only the generic site shell (the accession string is not in it); files path 404. The scRNA data in it would not answer Fig. 6 activity metrics in any case |
| Preprint on bioRxiv | Europe PMC lists the preprint without full text; held PP2 bytes used |
| Bedrosian commentary | Europe PMC full text read once (open access, CC BY-NC; digest of the XML `b23e2b082e6d28e8`); used to orient only |
| S540E bioRxiv attempt 2 (parked item, this window) | HTTP 429, Cloudflare 1015 at about 14:05Z; second and last planned attempt; see the S540E route result |

## Commentary (orientation only; no value taken from it)
It says hyperexcitability was "substantially normalized in both WOREE and SCAR12" and "more severe" in WOREE, and that WOREE and SCAR12 showed few transcriptional differences. It places the radial glia and SATB2 findings at "7 weeks" for both immunofluorescence and single-cell sequencing, whereas the single-cell data in the AM and PP2 are week 16 (week 7 is immunofluorescence and cell-attached recording): a commentary-level slip. No claim of mine rests on it. GSE156243 bulk data do not answer the PV question and are not used.

## Blind check (statement-carrying rows)
A delegate (legend-delegate, effort stated in the brief as medium; the Agent tool cannot set it) read five figure crops with no paper context and no class labels and returned axis readings and every bracket with its two groups. Its report is a hand-back message in the session transcript; the crop images are in the job scratch (not committed; third-party figures). Agreement with my producer readings, within the stated reading error:
* Fig. 6A(ii): same bar values for all three panels (active regions about 45, 100, 60, 100, 70; amplitude 0.023, 0.061, 0.013, 0.069, 0.044; rate 0.001, 0.075, 0.003, 0.257, 0.001); **same bracket set (4 per panel) and same six unbracketed pairs, including WOREE against SCAR12 and treated groups against WT in every panel**. Its one unresolved item: the right end of the long top bracket in the active-regions panel (WT to WOREE EGFP, **).
* Fig. 6B(ii) and (iii): same two brackets (WT to WOREE EGFP, WOREE EGFP to WOREE WWOX) in each, no other.
* Fig. 2E and F: same cumulative boundaries (neurons WT 0.46, KO 0.09, SCAR12 0.57, WOREE 0.48 against my 0.45, 0.075, 0.56, 0.47) and same log2 changes (WOREE about +0.07 and -0.05).
* Fig. 1D: five brackets, all from WT to a mutant group, all ****, **no bracket among the mutant groups** (WOREE and SCAR12 lines all about 330 to 370 spikes per neuron at week 7 against WT about 105).
* Procedure limits: the reader could not read the fifth legend label (cropped at the edge; the legend text is in the AM) and one stacked-bar row label; its identification of the salmon group as treated WOREE came from a legend fragment. No inference depends on those.
* The reader did not see the PP2 EV pages; the EV12 mRNA reading above is mine alone and flagged as such.

## Predictions scored (fixed before reading)
* P1 (65 percent: several statements VISUAL or NOT PRINTED): **held** (two headline sentences and the treated-against-WT claims).
* P2 (60 percent: genotypes not separated for at least one metric): **held and stronger than predicted**: no WOREE against SCAR12 comparison is printed for any Fig. 6 metric; the week-7 Fig. 1D mutant groups are also not compared among themselves.
* P3 (55 percent: n as organoids or recordings, not lines or differentiations): **held**; PP2 shows two lines per genotype pooled.
* P4 (80 percent: E-MTAB-14792 inaccessible and S9 and S10 not retrievable): **half held**: the accession and the AM supplement are not retrievable, but the preprint's Expanded View figures (held) carry the counterparts of S9 and S10 (EV10 to EV13), which I had not counted on.

## Competing explanations for the Fig. 6 pattern (one table; prediction rows are labelled; mouse and human are separate preparations)
| # | Explanation | What it predicts | What Fig. 6 and held PP2 say | Observation that separates it from the others |
|---|---|---|---|---|
| A | Loss of WWOX in excitatory cortical-plate neurons directly raises network activity (cell-autonomous), and neuronal restoration is sufficient | Neuronal re-expression lowers rate and amplitude with no change in progenitors | Rate falls to near zero in both genotypes (MADE); radial glia unchanged by treatment (PP2 EV13, WOREE only); transduction fraction unquantified in Fig. 6 | Dose-response: activity against the per-organoid fraction of NeuN-positive cells that carry WWOX; a WT plus AAV9-WWOX and a WT plus AAV9-EGFP arm |
| B | Immature neuronal state (fewer CTIP2 and SATB2 cells, ion-channel and synaptic gene sets low or high) drives hyperactivity; restoration works through maturation | Activity tracks marker maturation per organoid | WOREE markers restored together with activity; SCAR12 has WT-like markers but still hyperactive and also rescued (a split that B alone does not explain) | Per-organoid association between marker fraction and rate, within genotype; a marker-restored but still-active group |
| C | Network composition: more active regions and larger events reflect neuron number or density, not intrinsic excitability | Amplitude (legend says it reflects the number of spiking neurons) and active share move together | Active regions at ceiling (100 percent) in both untreated groups; amplitude and share fall together after treatment | Cell-attached or patch recordings at matched week 16 (the held cell-attached data are week 7 only) |
| D | Inhibitory deficit or interneuron development (the INV-15 question) | Interneuron markers reduced, hyperactivity not cell-autonomous | **Not testable here**: these organoids are unguided and predominantly dorsal, no interneuron or inhibitory marker is measured in Fig. 6 | An inhibitory readout in a ventralised or assembloid preparation; in vivo the INV-15 levels are unanchored (ADV-139 result) |
| E | Vector or batch effect (EGFP control against WWOX-2A-EGFP; one experiment; WT not vector-matched; treated SCAR12 amplitude below WT) | Differences remain with a matched vector or a second batch | Cannot be excluded; one batch stated for the transcriptome panels | Replicate in an independent differentiation with a vector-matched WT arm |
| F (ADV's sufficiency row; a **prediction**, not a result) | Restoring WWOX only in Synapsin-driven neurons is sufficient to remove the network phenotype (mouse and human tested separately) | In mouse: seizures and lethality rescued without non-neuronal restoration (already reported by the same programme, not independent); in the organoid: as row A | Organoid evidence is in row A; the mouse row is a separate preparation. **At risk** only if hyperactivity persists with intact inhibitory markers; Fig. 6 carries no inhibitory marker, so **the row is neither supported nor at risk by this figure** | An inhibitory-marker readout together with the activity readout in the same preparation, or a non-neuronal restoration arm |

Compound ranking changes only if its supporting evidence changes; nothing here changes a compound's evidence, so no ranking changes. The one portfolio consequence is wording: any consumer that carries "restoration normalised hyperexcitability to WT" should carry "reduced event rate to near zero in both genotypes (tests against untreated MADE); amplitude and active-region share at or above WT with no test printed; WT arm not vector-matched".

## CHOICE (ADV-140 closing)
* **Next most informative verifiable question:** does the AM supplement (Supplementary Figs. 9 and 10 and Methods) show the NeuN-positive WWOX-positive fraction per line and the activity values per line (the PP2 EV10 and EV11 counterparts)? That settles row A against row E (transduction fraction against effect) and whether the two lines per genotype agree.
* **Rejecting observation:** a per-line breakdown in which one line per genotype does not fall to near zero, or in which activity does not track the transduced fraction, would reject "restoration is sufficient and uniform" and promote rows B, C or E.
* **Comparison for the next batch (pharmacological lever):** none opens from this figure. The one interpretable contrast is the **WOREE and SCAR12 split that no test prints**: if a future source prints it, the genotype-specific activity gap (3.4 times) against an identical week-7 level is the question to look at (what changes between week 7 and week 16).
* **Document that would unblock (access-limited):** the Brain supplement PDF (OUP is behind a Cloudflare challenge; Europe PMC has no supplement) or a request to the authors through the operator's own channel (not drafted here; peer messages are not the operator's authority). **Best in-silico step meanwhile:** re-read PP2 Fig. EV10 to EV12 at full resolution from the held Expanded View PDF (this window read EV12 at 100 dpi only) and extract Table EV1 (organoid numbers, sections, batches) if present in the held files (not searched this window).

## Limits
Values are pixel readings of low-resolution crops (reading error about 2 axis units; the blind reader agreed). The AM supplement and E-MTAB-14792 were not obtained. PP2 EV12 mRNA bars and EV10 bar page were not read at full resolution. The statement "dots outnumber organoids" is by eye. "Similar to WT" is judged from absent marks, not from an equivalence test, and the authors may have an equivalence analysis in the unseen supplement. The week-16 Ca2+ and week-7 cell-attached readings are different preparations and ages.
