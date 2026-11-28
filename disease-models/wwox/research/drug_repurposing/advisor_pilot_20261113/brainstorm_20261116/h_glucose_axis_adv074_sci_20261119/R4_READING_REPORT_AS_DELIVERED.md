# R4 report: glucose and metabolic findings in Wwox-loss animals, from the held originals

Producer, SCI ADV-074, 2026-11-19. Hypothesis level. No dose, no lever, no recommendation. Not medical advice. No file was written (no folder was named in the dispatch), so this message is the deliverable. Tool calls used: about 52 by my own count (budget 90). Values marked "~" are read from plotted points, not from text. All glucose values are mg/dl.

## 0. Depth reached per original

- **32000863 Cheng 2020:** full PMC text read completely. Figures 2 and 7 viewed. Supplement PDF text-searched (24 pp). Figures 1 and 3-6 not viewed as images.
- **34747138 Repudi 2021 EMBO Mol Med:** PMC XML text only. No figure images held. The Appendix, which carries the glucose panels S1C and S1D, is NOT held. Glucose data are therefore text statements only.
- **42422765 Obeid 2026:** full text read, main Figures 1, 2, 3, 7 viewed, and supplement mmc1 pages 2 and 10 viewed (Fig S1 and S8). Fig S2 is legend only. mmc2 is the publisher article PDF (text extracted).
- **33914858 Repudi 2021 Brain:** operator-supplied PDF and text, Figures 1 and 2 viewed. Supplement read: the legend PDF (File009) and two RNA-seq xlsx files (File012, File013), which I only identified by sheet name (differential-expression gene lists) and did not analyse. Videos not opened. No glucose anywhere.
- **30755385 Abu-Remaileh 2019:** PMC XML text only. No images and no supplement. Values live in plots, so only directions are available.
- **25012504 Abu-Remaileh 2014:** PMC HTML text only. No images. Supplementary figures not held.
- **19500159 Suzuki 2009 (lde rat): ORIGINAL NOT HELD.**
  - Held: abstract only (`files/fulltext/origin_it_20261117/abstract_19500159.txt`). The receipt FTR-20260806-19500159-01 cites `files/fulltext/PMID19500159_Suzuki2009.html`, which is absent from the folder (Suzuki-named search of `files/` found nothing).
  - Rat statements below come from the repository dossier (`fulltext_dossiers/PMID19500159.md`), which quotes the paper. That is secondary: not primary evidence, and not figures viewed by me.
- **30290271 Hussain 2019:** PMC XML text only. It reports no glucose, survival or seizure measurement.
- **36828035 Hussain 2023 (P47T):** PMC text, Figure 1 viewed (survival, weight, EEG). Supplementary Tables 2-3 (blood chemistry) not held.
- **24871327 Iatan 2014:** PMC text only. Glucose was measured but not reported in the text.
- **Also found and read:** PMID 19936220 Ludes-Meyers 2009 (EIIA-Cre null, `files/fulltext/multihop/...EuropePMC.xml`), text only, Table 3 read.
- **Held reviews not used as evidence:** several reviews repeat "hypoglycaemia" without data (for example 24520212, 33916893, 38161429, 29724996 intro, 33195192 intro). Aqeilan 2008 (18487609) is not held as a file.

## 1. Per-datum table

Columns: paper | preparation | measure | value, n, test | locator and depth | rescue.

### Germline null: glucose, growth, survival

| Paper | Preparation | Measure | Value | Locator, depth | Rescue |
|---|---|---|---|---|---|
| 42422765 | Wwox-null, FVB, sex not split, P14 | glucose | KO+RI ~58 vs WT ~137; n=6 vs 6; Student t | Fig 1C/F/I/L, viewed | see CMV, EF1a, MBP, Syn rows |
| 42422765 | null, P10 / P11 / P17 / P19 | glucose | P10 KO+RI ~95 vs WT ~130 (* , Fig 3E). Fig 2D: KO ~98 (P11), ~73 (P17), ~57 (P19) vs WT ~122-143; KO n=4, WT n=5 | Fig 3E, Fig 2D, viewed | HD Syn normal by P20 |
| 42422765 | null, P14 (S8D) | glucose | KO ~40 vs WT ~160 (** ); n=6 vs 6 | Fig S8D, viewed | P1-P5 Syn: all normal |
| 42422765 | null | weight | KO plateaus ~6 g from ~P13, declines to ~4 g by P19, WT ~12 g at P21 | Fig 1B/E/H/K, viewed | Syn restores to WT line |
| 42422765 | null, KO+RI | survival | all dead by ~P8-19 (Fig 1, n=6); Fig 3B n=10, all dead by ~P20; log-rank | viewed | see below |
| 34747138 | null, P0 AAV9-hSynI-mWwox or -hWWOX | glucose | text only: "hypoglycemic from the second week until they succumbed"; rescued mice "normal vs WT" | Results text; Appendix S1C/D NOT held | Syn rescued growth, glucose, seizures, ataxia, survival |
| 34747138 | same | weight, survival | rescued indistinguishable from WT by 6 wk (n=4 and n=3 per group). KM (mWwox): total 18, 6 spontaneously dead, 12 taken out. KM (hWWOX): 16, 6 alive, 6 dead, 4 taken out. Uninjected KO n=8, EGFP n=6. Log-rank p<0.0001 | Figs 1B/C, 2B/C, text only | |
| 19936220 | EIIA-Cre null, P18 survivors | glucose | KO 143.5±8.8 (n=4) vs HET 227.0±11.7 (n=3) vs WT 250.6±5.0 (n=3); p=0.000131 (test not named); BUN 37.25 vs 17.67 (p=0.01); CO2 14.5 vs 21.7 (p=0.006); Ca lower (p=0.0004) | Table 3, text only | none |
| 19936220 | same | survival | 43% (15/35) dead by 72 h; 77% by P17; none past weaning | Results text | |
| 25012504 | null (age not given in text) | serum glucose / insulin / lactate | glucose low (n=5 per genotype); insulin LOWER in KO (WT n=9, KO n=13); serum lactate higher (Suppl S2A); islets histologically normal. Values not in text | Fig 1a-b, text only | |
| 25012504 | digoxin at P21, KO=3, WT=3 | glucose 40 min after i.p. | KO glucose rose; PBS control. Datum only; no seizure or survival read-out | Fig 5c legend, text only | |

### Promoter series (42422765), 4E10 vg, P0 ICV, WPRE vectors

| Vector | Glucose P14 | Weight | Survival | Locator |
|---|---|---|---|---|
| EF1a (n=5) | ~103 vs KO ~58 vs WT ~137; *** vs KO and *** below WT: partial | no rescue | no rescue, all dead ~P17-20 | Fig 1A-C, viewed |
| CMV (n=5) | ~131, ns vs WT (*** vs KO) | rises toward WT to ~P21 | ~80% alive to ~P30, then 40% by ~P32-35 | Fig 1D-F, viewed |
| MBP (n=5) | ~50, same as KO | flat ~5 g | all dead ~P15 | Fig 1G-I, viewed |
| hSynI (n=6) | ~131, ns vs WT | WT line | 100% to P21+ | Fig 1J-L, viewed |
| CBA (n=4, 5E10) | normalised, p<0.001 vs KO | not stated in legend | "prolonged", p<0.05 | Fig S2A-C, legend only |

Glucose was measured only at P14 in this series, so glucose at the time of CMV deaths is not known. Legend p-values are as printed. Seizures were not assessed in any promoter-series animal.

### Dose and WPRE series (42422765), hSynI, no WPRE unless stated

| Group | Glucose | Survival | Locator |
|---|---|---|---|
| 4E10 without WPRE (n=3) | P11 ~137, P17 ~128, P19 ~98 (WT 122-143) | 1 of 3 alive to ~P26; deaths from ~P17-18 | Fig 2B/D, viewed |
| 8E10 without WPRE (n=5) | WT-like at P11-19 | rescued | Fig 2B/D |
| 4E10 with WPRE (n=3) | WT-like | WT-like | Fig 2B/D |
| LD 1.23E11 (n=20) | P10 ~105 (ns vs WT), P20 ~128 vs WT ~145 (*), P30 ~162, ns | all dead by ~P75, median ~P55 | Fig 3B/E-G, viewed; n per point ~7-12 plotted, not stated |
| HD 2.63E11 (n=30) | P10 ~113 (ns vs WT), P20 ~147 (ns), P30 ~170 (ns), P180 ~188 vs WT ~197 (ns) | ~77% alive at P300; WT-RI ~72% (n=20) | Fig 3, viewed |
| P1-P5 injection, 2.63E11 (n=3-7 per day) | P14 normal | ~100% to P300 (P3 group n=3: one of three dead ~P25-30) | Fig S8, viewed |

### EEG, ECoG and firing

| Paper | Preparation | Finding | Locator |
|---|---|---|---|
| 42422765 | null pups, ECoG from ~P14, 7 days | spikes/h: KO ~9 vs WT ~2. Spike-wave discharges/h: KO ~0.64, WT ~0.03, HD ~0.13 (****; n=5 per group). Fig 7C shows 3 KO and 2 WT points with printed p=0.2000, whereas the legend and text say * / significant. Discrepancy flagged | Fig 7, viewed |
| 34747138 | P18-21 cell-attached, 30-45 neurons per group, n=3 animals | firing ~6-fold higher in KO; KO+AAV not different from WT; adult rescued (6 mo) equal to WT | Fig 3, text only |
| 33914858 | S-KO, P13-17, anaesthetised in vivo LFP; slices | slice bursting: 36/42 S-KO (86%; 24 animals) vs 4/23 S-HT vs 0/11 S-Control. ACSF contains 10 mM glucose | Fig 2, viewed |

### Conditional lines (33914858)

| Line | Seizures and EEG | Growth and survival | Glucose | Locator |
|---|---|---|---|---|
| Synapsin-Cre (S-KO) | tonic-clonic seizures from P9, 68.5±13.4 s (n=6, P14-18) | weight diverges by ~P4-7; all dead by ~P19-27 (S-KO n=15, S-Control n=13; p=0.0001) | none reported | Fig 1G-I, viewed |
| Nestin-Cre (N-KO) | tremors / seizures noted | dead by 4 weeks (n=14 vs 12) | none reported | Fig 1D-F |
| Olig2-Cre and GFAP-Cre | no phenotype | normal growth and survival (n=10-11, 8-9) | none reported | Fig 1J-O |
| Germline null | n/a | KO n=11, WT n=10 | none reported | Fig 1A-C |

Glucose, insulin, lactate and ketones appear in no panel of this paper or its supplement. The only glucose mentions are the 10 mM glucose in the slice and sucrose solutions.

### Other germline-null lines and hypomorphs

| Paper | Preparation | Measure | Value | Locator, depth |
|---|---|---|---|---|
| 32000863 | two germline nulls (exon 1 and exons 2/3/4), mouse | seizures | spontaneous seizures "commonly observed after P12", provoked by noise, strobe and a new cage (video, no counts). Pilocarpine and PTZ susceptibility in preweaning mice (age not stated): KO n=4 and 6 vs WT n=6 and 20; half of KO reached status epilepticus | text and Fig 7, viewed |
| 32000863 | same | survival | "survived for less than a month" (Fig S1d, text only; supplement legend contains no values) | text |
| 32000863 | same | glucose | not measured; the word glucose occurs only as a cited HIF-1 reference | full text and supplement |
| 36828035 | P47T/P47T knock-in, adult, both sexes | survival | mean 393 ± 32 days vs 495 (P47T/WT) vs 542 ± 8 (WT); n=25/30/14; log-rank p=0.001 | Fig 1b, viewed |
| 36828035 | same | weight | 29.2 ± 4.3 g vs 41.2 ± 9.5 g WT; n=16 vs 9 | Fig 1c, viewed |
| 36828035 | same | EEG and seizures | n=3 per group, 21-53 h recordings: 11-22 generalised seizures in 43-53 h; interictal spikes 0-3098/h vs WT 0-68/h. Seizures up to 1 min, "not lethal" | Fig 1d, viewed |
| 36828035 | same | blood chemistry | "comparable, no significant differences" (glucose not itemised in text; Supp Tables 2-3 not held) | text only |
| 30290271 | null, 2 weeks old | seizure, glucose, survival | none reported (interneuron counts, cytokines, transcriptome) | text only |
| 19500159 | lde/lde rat (13-bp exon-9 deletion; protein undetectable per dossier) | seizures and EEG | audiogenic seizures 19/20 (95%) in 21-33-day-old FEMALES (3 died, excluded); spontaneous 30/50 (60%); interictal ~10 Hz spikes in all 5 mutants; 0/14 controls (dossier; abstract confirms 95% and EEG) | secondary via dossier |
| 19500159 | rat, 28 days | serum constituents | dossier quotes the paper: "28-day-old lde/lde rats had normal levels" and "Normal levels of serum constituents clearly excluded the possibility that these abnormal excitabilities are resulted from a systemic metabolic disorder". Per the dossier, this is cited to the unread Suzuki 2007 (17803050), whose abstract reports raised BUN, creatinine and phosphate and lowered growth hormone | secondary via dossier. Not verified against the original |
| 19500159 | rat | viability | 3-12 weeks (Table 2, via dossier); Table S1 growth data not available | secondary |

### Peripheral conditional lines

| Paper | Preparation | Measure | Value | Locator, depth |
|---|---|---|---|---|
| 30755385 | skeletal-muscle KO (ACTA1-rtTA-Cre), adult | fasting glucose (18 h, n=8) | raised; hepatocyte KO and adipocyte KO unchanged. No numbers in text | Fig 1E, text only |
| 30755385 | same | GTT, 6 months, n=8 | impaired | Fig 1F-H |
| 30755385 | same | ITT, 10 months | insulin resistance | Fig 2E-G |
| 30755385 | same | serum insulin (4 vs 4) | higher | Fig 2H |
| 30755385 | same | weight, from 6-8 weeks (n=8) | heavier | Fig 1K |
| 30755385 | same | FDG-PET (control 8, KO 9) | uptake lower in gastrocnemius and hamstring; brain and liver uptake unchanged | Fig 2I/J, S2A/B |
| 30755385 | same | serum lactate (n=6) | higher | Fig 3L |
| 30755385 | same | food intake (n=8) | lower in the dark phase | Fig 3G/H |
| 30755385 | same | seizures and survival | not reported | |
| 24871327 | hepatocyte KO (Alb-Cre), young and old | health, weight | "healthy, normal body weight"; glucose measured but not reported in text | text only |

## 2. Age-resolved timeline (by preparation)

**Germline null (several labs and lines)**

| Event | Age and source |
|---|---|
| Growth divergence | from ~P4 (33914858 Fig 1B, n=3 per group) |
| Seizure onset (conditional S-KO, behavioural) | P9 (33914858) |
| Seizure onset (germline null) | "after P12" (32000863) |
| First quantitative glucose in these originals | P10 (42422765 Fig 3E; ~95 vs ~130) and P11 (Fig 2D; ~98) |
| Hypoglycaemia stated | "from the second week" (34747138 text; Appendix not held) |
| Later glucose | P14 ~58 / ~40; P17 ~73; P18 143.5 vs 227-251 (19936220); P19 ~57 |
| First EEG / ECoG | ECoG started at ~P14, so earlier onset is unobservable (42422765). In vivo LFP bursting P13-17 (S-KO). Cell-attached firing P18-21 |
| Death | 43% by 72 h and 77% by P17 (19936220); ~P8-19 (42422765); ~P19-27 (33914858); <1 month (32000863) |

**Rat lde:** audiogenic seizures tested at 21-33 days; serum constituents at 28 days; viability 3-12 weeks (secondary).

**P47T:** seizures and EEG in adults; deaths up to ~600 days.

**Muscle KO:** glucose at adulthood, GTT 6 months, ITT 10 months.

**Gaps**

1. No glucose before P10 in any held original.
2. Seizure onset (P9) precedes the first quantitative glucose (P10).
3. No glucose at the time of a seizure or an ECoG epoch.
4. In 19936220, 43% of KO pups died by 72 h and before the only glucose sample (P18, n=4 survivors), so that sample is from survivors.
5. Glucose in the dose and promoter series is taken in animals alive at that age, so survivorship applies.

## 3. Dissociation list

**A. Glucose normal or near-normal, seizures or death present**

- **A1. LD vector** (42422765 Fig 3): glucose at P30 ns vs WT (~162 vs ~170). Per Fig 3B all LD mice (n=20) were dead by ~P75, median ~P55. The text says "modestly, though significantly, extended lifespan".
- **A2. CMV vector** (Fig 1D-F): glucose at P14 ns vs WT; survival ~80% to ~P30 and ~40% by ~P32-35. Brief's framing "glucose normalises while animals die" is only half-supported. Glucose after P14 was not measured, so it is unknown whether glucose was normal when they died. The authors say protection "was not sustained at later stages".
- **A3. 4E10 no-WPRE** (Fig 2B/D, n=3): glucose ~137 (P11) and ~128 (P17), near WT, while deaths began ~P17-18. Glucose fell to ~98 at P19. n=3.
- **A4. P47T** (36828035): spontaneous generalised seizures and early death with blood chemistry "comparable" (glucose not itemised). Text: seizures "not lethal".
- **A5. Rat lde** (secondary): seizures 95% audiogenic, normal 28-day serum constituents as quoted by the dossier. This is a species and allele difference as well as an age difference (28-day rat vs P18 mouse).
- **A6. S-KO slice bursting** (33914858 Fig 2B): 36/42 slices burst in 10 mM glucose ACSF, 0/11 control slices. Glucose was not measured in S-KO animals, so a prior in vivo metabolic imprint is not excluded. Flagged as my inference.

**B. Glucose partly or fully corrected, death not prevented**

- **B1. EF1a vector:** glucose partly raised (~103 vs ~58), no survival gain.
- **B2. CMV (P14 only):** glucose normal, survival partial (see A2).
- **B3. CBA:** glucose normal (p<0.001 vs KO), survival "prolonged" (p<0.05), legend only.

**C. Glucose low, seizures absent**

- No held original contains a documented case. Glucose low at P10-11 (~95-98, modest) precedes the only quantitative seizure and ECoG measures.
- MBP vector: glucose ~50, all dead ~P15, seizures not assessed.
- Muscle KO: the reverse sign (hyperglycaemia); no seizure or survival data.

**D. Measures that moved together (not a dissociation)**

- Syn vectors (HD, P1-P5): glucose normal, SWD ~0.13/h, firing normal, survival ~77-100%.
- KO: glucose low, spikes ~9/h, SWD ~0.64/h, death. These are co-variation at group level in separate cohorts, not same-animal pairs.

## 4. What each original says about cause, and whether the data support it

- **34747138:** neuronal WWOX "reversibility of hypoglycemia" shows a "central role of WWOX in the CNS regulation of metabolism of glucose". Supported only as: a neuron-targeted vector normalised glucose. The Appendix panels are not held, and no peripheral expression was found in the rescued mice (Appendix S2, text).
- **25012504:** low glucose and raised lactate are linked to HIF1α-driven glycolysis; lower insulin is read as a response to low glucose. Whole-animal timing and brain data are absent.
- **42422765:** near-normal glycaemia accompanies rescue; the discussion treats neuronal WWOX as necessary and sufficient for survival and glycaemic control. Promoter results (CMV and CBA normalise glucose transiently) are read as a transient benefit. The paper itself states expression was not normalised across promoters.
- **33914858:** neuronal WWOX loss is sufficient for epilepsy and death; no metabolic claim and no glucose data.
- **32000863:** neuronal migration and GSK3β activation drive seizures. No metabolic claim.
- **19500159 (secondary):** normal serum "clearly excluded" a systemic metabolic cause for the excitability. The dossier flags this as stronger than the cited support.
- **30755385:** muscle-autonomous WWOX loss gives hyperglycaemia. This does not address the null's hypoglycaemia.

Net for the question, hypothesis level:

- **No held original shows glucose driving excitability, seizure or death.** The directly manipulated variable in every rescue is neuronal WWOX, not glucose.
- **The data do not exclude it either.** Glucose is never measured at seizure time.
- **A1 and A3** are the strongest "death without low glucose" cases; both are small, and both rely on survivors.
- **The rat** supports "seizures without a metabolic crisis", but only through a secondary source.

## 5. Not measured anywhere in the held originals

- Ketones and beta-hydroxybutyrate.
- Lactate by age (one adult serum lactate comparison in the muscle KO and one unspecified-age null comparison).
- Insulin by age (a single unspecified-age null comparison).
- Feeding or milk intake and stomach filling in pups (food intake only in adult muscle KO).
- Glucose at seizure time or during ECoG.
- Glucose before P10.
- Glucose in S-KO and N-KO.
- Seizure read-out for CMV, EF1a, MBP, LD and the no-WPRE 4E10 group (only survival, weight and glucose).
- Brain glucose, uptake or CSF lactate in null pups (FDG only in adult muscle KO).
- Corticosterone, GH or other counter-regulatory hormones in nulls (the rat 2007 abstract mentions GH via the dossier).
- Same-animal glucose and ECoG or behaviour pairs.

## 6. Limits of this reading

- Several values are read from plots, so only direction and magnitude are reliable.
- Appendix and Supplementary Tables for 34747138 and 36828035 are not held.
- The rat original is not held.
- Ludes-Meyers 2009, Aqeilan 2008 and Suzuki 2007 are outside the requested set. Only 19936220 was read, as text.
## Correction (ADV-330, 2026-11-28, IT36): two items called "not held" are held
The Appendix of PMID 34747138 (glucose panels S1C and S1D) has been held since 2026-10-19 (`files/supplement/PMID34747138_r2/EMMM-13-e14599-s001.pdf`; read for ADV-328, values in line 23 of [[meta_gaba_paradox_current]]), and Supplementary Tables 2 and 3 of PMID 36828035 (blood chemistry and haematology, `files/supplement/PMID36828035/NIHMS1957654-supplement-Supplementary_tables.docx`) are held and read in `research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv330_p47t_blood_chemistry_it_20261128/RESULT_ADV330_IT_20261128.md` under the ADV-330 folder. The delivered text above stays as the record of what the reader had at the time; the sentences "Appendix ... not held" and "supplementary tables ... not held" do not apply to the current repository.
