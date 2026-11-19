# G audit: measured results in held WWOX neural and pharmacology papers that the project does not carry

SCI, 2026-11-19. Hypothesis level, no dose, not medical advice. Method: results were taken from the deep-dive dossiers and manifests (held originals named per row). Consumers searched: needs.json (N), cards/*.card.json (K, 30 cards), open_questions_map.tsv (M), EXPERIMENT_BRIEF V1 and V1.1 plus the frozen priors file (B), arm-table notes V5 to V7 and the V9 arm table (A). Search was by regex over concatenated copies of these files in /tmp (case-insensitive), and every hit I relied on was read in context. Labels: C carried, P partly, N not carried, U unclear. Every N has two routes (R1 and R2, two different concept-word sets), plus a PMID and author-name route for a whole paper and a read of the closest need or card; where I ran only one set the row is U.

Caveat on method: the dossiers were the source for the result list, not a fresh page-by-page reading of every held file. Figure and table locators are those the dossiers give. I did not open the held PDFs and XMLs row by row (see section d).

## (a) Table

Abbreviations: Fig = figure, ST = supplementary table, n as printed. "Decision" = the decision the result could change.

| Paper | Result (locator) | Label | Where | Routes (N and P rows) | Decision it could change |
|---|---|---|---|---|---|
| 33914858 Repudi 2021 Brain | S-KO myelinated axons/field CC 55+-35 vs 180+-40, g-ratio up, P17 n=3 (Fig 2 EM) | C | N: "about 3.3 times fewer myelinated axons" | | none |
| 33914858 | Axonal conduction delayed in S-KO (conduction panel, main text) | P | N: only "a callosal conduction-latency proxy" in a readout list (IT14 P4 statement); no measured direction or size | R1 conduction/CAP/conductivity: cards 3 hits all peroneal CV in a DCA card; M 0, B 0. R2 latency: no genotype hit | adds a functional endpoint to the myelin cards (F02, H02). Already handled today in r1_conduction_endpoint_sci_20261119 (not one of the five consumers) |
| 33914858 | CC1+ mature OL 2-fold down, PDGFRa+ OPC up (CC1 n=3, 0.5 mm2) | C | N: "CC1+ and PDGFRa+ counts move toward wild type" | | none |
| 33914858 | Cleaved caspase-3 and CC1: "no significant OL death", an image with no count, n or test (Suppl Fig 1) | N | | R1 caspase/cleaved caspase/OL death: only IL-1 and caspase-1 hits in unrelated cards. R2 cell death/OL survival: 0 genotype hits. Read the myelin need (anchor "THE AUTHORS STATE THE LIMIT OF THEIR OWN NEGATIVE"): it is about O-KO, not this | adds a limit to the maturation-block premise on myelin cards F02/H02 |
| 33914858 | S-HT slice bursting 4/23 vs 0/11 vs 36/42 (Fig 2B) | C | N 34634460 entry; M "S-HT phasic deficit"; B | | none |
| 33914858 | S-HT: no S-HT vs control test on any measure; in vivo S-HT spectrum at or above S-KO below 5 Hz but in vitro below control; evoked-response brackets omit S-HT vs control (Fig 2D, 2F; Suppl Fig 3B); "indistinguishable" behaviour asserted, no data | N | | R1 spectral/12-20 Hz/0-4.9 Hz/power in S-: 0 in all five. R2 "indistinguishable from control/did not show any abnormal": one card hit, a Breton hippocampal sentence. Read B S-HT paragraph: carries bursting incidence only | bounds the heterozygote premise (B: S-HT phasic-deficit prediction) |
| 33914858 | O-KO and G-KO no phenotype (survival n=11/10 and 8/9; MBP unquantified) | C | N genotype comparison need; anchor "flat negative" | | none |
| 33914858 | Residual Wwox normalised counts in S-KO cortex 173/187/331 vs hippocampus about 19 (ST1) | N | | R1 residual Wwox/incomplete deletion/normalised counts: hits belong to an organoid card and to map NP3A5 (a different deposit, glial UMI). R2 cortex residual/172.7/331: 0. Read the cortical-burst cards: no deletion-depth statement | deletion efficiency by region bears on reading cortical slice bursting and cortex vs hippocampus transcript disagreements (A notes) |
| 33914858 | WT OPC on null DRG neurons differentiate less (n=4) | C | M "reproduce the OPC differentiation delay (DRG-OPC co-culture)" | | none |
| 33914858 | N-KO EM: myelinated 45+-26 vs 148+-45; unmyelinated 440+-210 vs 195+-35 (Suppl Fig 5G) | P | N, K carry nestin-Cre phenotype (survival, seizures); the EM counts are not carried | R1 "N-KO": 0. R2 Nestin: 5 hits, read: survival/seizure only | none (confirms S-KO numbers) |
| 34747138 neonatal gene therapy | Hypoglycaemia rescued: KO about 85 falling to 45 by d20-24 vs WT 120, n=5 (App Fig S1C-D); one tail-prick reading, state unknown | P | N NEED-SYSTEMIC-GLYCAEMIA-GROWTH carries 42422765 values only | R1 tail-prick/glucometer/fed-fasted: 0. R2 insulin/ketone: need hits unrelated | adds the measurement-state limit to the glycaemia need and cards I01/E03 |
| 34747138 | Adult EM unmyelinated axons about 2x WT (Fig 5E) | C | N counter_evidence "about 52 versus about 26" | | none |
| 34747138 | Transduction stated 60-70% but panels 52-71%, cerebellum below range (Fig 1E, 2G) | N | | R1 "50 to 70 percent/60 to 70 percent": one hit, other paper. R2 transduction: unrelated. Read C01: carries 42422765 dose arms | low: bounds C01 dose comparisons |
| 34747138 | Treated survival reaches 0% at about 330-350 d (Fig 1C, 2C): "extended life span" bounded | N | | R1 330/350 d, extended lifespan: other models. R2 late deaths/bounded: unrelated. Read C01 and C04: carry P180 durability of 42422765, not these curves | adds a durability ceiling to C01 |
| 42422765 AAV9 series | Glucose P10 about 95 vs 130, P20-P30 treated WT-like (Fig 3E-H) | C | N glycaemia need O1 | | none |
| 42422765 | Fig 1: CMV vector normalises glucose with 3/5 dead by d32; EF1a partial, death by P20; MBP vector none; synapsin normalises and survives | P | glucose from Fig 3 carried; vector dissociation (glucose not predicting survival) not found | R1 CMV/EF1/MBP vector: unrelated hits. R2 "glucose normalises ... do not reach": 0 | weakens hypoglycaemia as lethal driver (I01, E03 premise) |
| 42422765 | Dose-dependent durable survival, seizure rescue | C | C01, C04 (94 card hits) | | none |
| 30290271 Hussain 2019 | PV+ down 44% whole hippocampus, DG p<.005, CA1 p<.05 (Fig 1) | C | N anchor "reduced ... by 44 percent"; B | | none |
| 30290271 | NPY+ down 30% DG only (Fig 2) | C | N anchor "30% reduction" | | none |
| 30290271 | IBA1 and GFAP area up CA1, CA3, whole (Fig 3-4) | C | N anchors | | none |
| 30290271 | GAD65/67 lower, n=5 | C | N "not gaba concentration or flux" | | none |
| 30290271 | Il6 up significant, Tnf-a not | C | N anchor "il6 but not tnf-a" | | none |
| 30290271 | Neurosphere RNA-seq 283 DEGs (184 up, 99 down; KO n=2, WT n=3): Kcna2, Grm3, Grin2b, Arx down; Gabbr2, Gabra2, Calb2, Htr3a up (Fig 6, ST2) | N | | R1 neurosphere/283 DEG/Kcna2/Grin2c: hits are other datasets (A notes cortex vs hippocampus). R2 Gabra2/Gabbr2/Calb2/Htr3a: 0. Read N for this paper: 7 anchors, none transcriptomic | adds channel/receptor transcript premises (Kv, GABA-A) for E/I and Kv7 arms |
| 36828035 Hussain 2023 P47T | Video-EEG: 11-22 GTC seizures/43-53 h, spikes 0-3098/h vs 0-68/h, n=3 (Fig 1) | C | N readout "video-EEG seizures, provoked threshold" | | none |
| 36828035 | Survival hom 393+-32 d vs het 495+-23, WT 542+-8, log-rank p=0.001; weight 29.2 vs 41.2 g | N | | R1 393/495/542 and P47T survival: 0 in all five. R2 P47T lifespan/median survival: 0. Read the P47T needs: RNA-seq and EEG only | adds a natural-history ceiling for any P47T-class durability or rescue arm |
| 36828035 | Astrogliosis progresses 80 to 250 d; microglial abundance untested | C | N anchors | | none |
| 36828035 | Purkinje number about 4-fold down at 80 d, basket unchanged; ML/GL thinning (Fig 5d-h) | P | K: "cerebellum atrophic with Purkinje loss" as a composition caveat; no measured size | R1 Purkinje/cerebellar degeneration: one need hit on another model. R2 basket: 0 | adds a cell-composition bound to cerebellar cytokine readouts |
| 36828035 | Olig2+ cells down (about 122 vs 205 at 80 d; 117 vs 237 at 250 d) while Mbp area ns (Fig 4e, Suppl S6c-d, n=3) | N | | R1 Olig2 count/oligodendrocyte number: only jimpy. R2 Mbp area: 0. Read F02/H02 myelin cards: no P47T row | a case where OL count falls without myelin change: limits OL count as a myelin proxy on F02/H02 |
| 36828035 | Cholestasis 43/22/0% (hom/het/WT), nephropathy 52/72/14%, kidney and liver weight up (ST4) | N | | R1 cholestasis/nephropath/kidney weight/liver weight: 0. R2 P47T within 200 chars of kidney/liver: 0. Read NEED-SYSTEMIC: mouse null glucose only | adds an organ-pathology limit to the systemic need and to hepatically or renally loaded arms |
| 36828035 | Blood chemistry and haematology ns, terminal samples, K and creatinine off-scale (ST2-3) | N | | R1 blood chemistry/haematolog: one unrelated hit. R2 as above | none (negative is uninformative) |
| 36828035 | PPxY pull-down near-lost (n=2), transcript ns (S2a n=6, FPKM n=5), protein present but lighter | N | | R1 P47T near pull-down/PPPY/binding: 0. R2 protein present/FPKM/transcript unchanged: Q230P only. Read P47T needs: allele-blind notes, no binding datum | none to low; frames P47T as protein-present function-lost |
| 34268881 Steinberg 2021 | WOREE organoid firing about 4x, normalised by WWOX (24/41/40 cells) | C | N "organoid hyperexcitability ... add-back" | | none |
| 34268881 | Depolarising GABA is interpretation; no E_GABA, NKCC1/KCC2 | C | N anchors; M NP3A4 | | none |
| 34268881 | RNA-seq 2 WT vs 4 KO, raw p<0.01; glycolysis/OXPHOS | C | K "ratio of normalised counts, 4 KO over 2 WT" | | none |
| 34268881 | Rescue supraphysiological, partial | C | N counter-evidence; K | | none |
| 34268881 | Wnt targets up; nuclear beta-catenin 2 WT vs 4 KO | C | K "2 WT versus 4 KO; activation step unmeasured" | | none |
| 32000863 Cheng 2020 | Lithium suppresses PTZ seizures in all three genotypes (Fig 7d) | C | N "lithium suppressed in all three genotypes" | | none |
| 32000863 | Ethosuximide significant only in null; same PTZ dose; no interaction term (Fig 7b) | C | N, K, M | | none |
| 32000863 | GSK3b Ser9 down, total unchanged, het not intermediate | C | N O1, K | | none |
| 32000863 | Het Tc-MEP latency equals null with normal amplitude (candidate carrier readout) | N | | R1 Tc-MEP/motor evoked/MEP latency: 0 (the "MEP" hits are mEPSC). R2 latency near heterozygote/null: none. Read B and heterozygote cards: bursting only | adds a functional conduction-class endpoint and a carrier readout to the heterozygote question and myelin cards |
| 32000863 | Peripheral nerve: Schwann apoptosis, onion-bulb degeneration | N | | R1 Schwann/onion/peripheral nerve: other drugs only (BLOCK-1 neuropathy is a drug flag). R2 neuropath: same. Read the safety/hazard lines | adds a PNS phenotype to the myelin endpoint and the peripheral-neuropathy hazard logic |
| 32000863 | Cortical thinning at E16.5 before any seizure; DCX stays high (delayed maturation); apoptosis about 5x brain-wide; cerebellar vermis fusion; holoprosencephaly-range; brain water unchanged | N | | R1 E16.5/cortical thinning/DCX: 0 (one unrelated in utero card). R2 vermis/Joubert/holoprosencephal/brain water: 0. Read acute-seizure cards (H01, F04): no malformation limit | structure precedes seizure: timing limit for every acute seizure-drug card |
| 34634460 Breton 2021 | Bursting 36/42 vs 4/23 vs 0/11; d-APV abolishes; pannexin blocker does not reduce | C | N 33 hits, B, K | | none |
| 34634460 | Supplement contradicts text: median 2.29 vs 0.84 /min; carbenoxolone -87% vs -96% | C | N anchors "2.29 [1.1", ".84 [.57" | | none |
| 34634460 | Slices cut in sucrose, recorded in 10 mM glucose ACSF: bursting in glucose-replete bath | P | M asks "bath glucose of the Wwox recordings"; the answer (10 mM) is not recorded | R1 10 mM/glucose-replete/bath glucose: only the question. R2 low-glucose/ketone bath: 0 | closes that map question; lowers a metabolic-bath confound on E-cards |
| 34634460 | PAC controls: low-frequency power vs coupling uncorrelated, animal-level in 8/9 (Suppl S1) | P | K proposes PAC as a future readout only | R1 phase-amplitude/oscillat: cards 3, brief 3 proposals. R2 PAC: 0 | none |
| 19500159 Suzuki rat | Audiogenic seizures 19/20 (95%), female cohort only, latency 56 to 36 to 25 s (kindling-like), controls 0/14 (Fig 6) | N | | R1 audiogenic/lde: hits are other models. R2 kindling/latency across trials: none. Read H01 audiogenic endpoint row: no rat | adds a rodent audiogenic endpoint with trial kinetics to H01 |
| 19500159 | Rat lde/lde serum constituents normal at 28 d (cited to unread FT-041; renal markers raised in its abstract), vs mouse metabolic crisis | N | | R1 28-day-old/normal levels of serum: 0. R2 systemic metabolic/renal: only the mouse need. Read NEED-SYSTEMIC: mouse only | decides whether hypoglycaemia is a confounder or driver of excitability (high) |
| 19500159 | Hippocampal vacuoles 9/9 vs 0/10; amygdala 6; interictal spikes about 10 Hz in all 5 mutants | P | K: rat glial rows and a "vacuole" caveat; no counts | R1 vacuol: 48 card hits, rat only as a caveat. R2 amygdala: kindling rows only | none |
| 19500159 | mRNA normal, protein absent (Fig 4-5): functional null | C | K "no normal Wwox protein" | | none |
| 24369382 Mallaret 2014 | P47T WW1 fusions lose WBP1 PPPY peptide pull-down | N | | R1 P47T near pull-down/PPPY: 0; Mallaret/PMID 0 in all five. R2 first WW domain pull-down: need hits are HIF1A/DVL2 | none to low (same class as the P47T binding row above) |
| 24369382 | Null mouse audiogenic 3/8 at 16 d, 4/4 survivors at 20 d, WT 0/8 | N | | R1 3 of 8/11-14 kHz/audiogenic: other strains. R2 Mallaret/24369382: 0. Read H01: audiogenic row is generic | age-window anchor for the audiogenic endpoint (H01) |
| 24369382 | 189 ataxia patients no further WWOX mutation; no tumour in 6 homozygotes aged 5-26 | N | | R1 189/ataxic patients/182 families: unrelated. R2 no tumour: gene-therapy card says "no tumour surveillance". Read C01 | tumour-risk limit on C01 (human observation) |
| 24369382 | G372R: no protein measured, not modellable | P | K carries G372R siblings; M R9 asks band identity | R1 G372R: 2 card hits. R2 dehydrogenase domain: 0 | none |
| 35792847 Al Baradie 2022 | 70-patient table: spasms 50%, 78.6% onset under 3 months; 9 patients (Tables 1-3) | P | M D5B asks about AED response in Table 3 | R1 PMID/Elsaadany: 0. R2 78.6/spasms 50%: 0 | prior for AED-class response |
| 35792847 | Q230P case seizure-free about 9 mo on vigabatrin plus ketogenic diet; R54* spasms controlled on vigabatrin | P | N carries "three of four treated children" (Al Baradie) | R1 Q230P near ketogenic/vigabatrin: 0. R2 suppression-burst: 0 | vigabatrin and diet class priors |
| 27495153 Elsaadany 2016 W44X | Older sister four AEDs failed, alive at 7 y ventilated; younger partial; MRI progressive demyelination; metabolic and CSF normal | P | N lists Trp44 only in a read-through census; drug failures not carried | R1 Elsaadany/Trp44/7 years: 1 hit census. R2 phenobarbit/clonazepam/levetiracetam: other roles | adds an AED-failure and survival bound for a null/null genotype |
| 30361190 Shaukat 2018 | Child 1 spasms resolved on vigabatrin after partial prednisolone | C | N anchors | | none |
| 30361190 | Table 1: spastic quadriplegia 14/23, delay 23/23; single MRI at 2 months | N | | R1 microcephal/spastic quadripleg/polymicrogyria: MYCN only. R2 optic atrophy: M one ketamine question | none |
| 30755385 Abu-Remaileh 2019 | Muscle cKO: glucose intolerance (peak about 400 vs 250 mg/dL), insulin about 2.4 vs 0.5 ng/mL n=4, weight 44 vs 34 g (Fig 1) | N | | R1 PMID/skeletal muscle/muscle-specific/insulin resist/glucose intoleran: 0 in N, M, B, A; one card hit is the 2014 paper. R2 opposite sign/two tissues: "opposite sign" hits unrelated. Read NEED-SYSTEMIC: null mouse only | tissue-of-origin of glycaemia (opposite sign to the null) for the systemic need and I01/E03 |
| 30755385 | Fasting glucose 78 vs 67 (18 h, n=8); FDG uptake down in two muscles; AMPK phosphorylation loss | N | | R1 FDG/AMPK: AMPK hits are activity papers. R2 as above | peripheral arm of the HIF/glycolysis question (K01) |
| 30755385 | Human metabolic variants nominal only (best p 3.78E-06; ST1) | N | | R1/R2 as above | none |
| 24871327 Iatan 2014 | Liver-specific KO does not lower HDL-C in either sex | N | | R1 PMID/Iatan 0. R2 HDL/ApoA-I/ABCA1: 0 in N, M, B, A; cards 2 unrelated. Read M OQ4 (cholesterol into myelin): no HDL | low: lipid supply limit for the myelin-lipid question |
| 24871327 | Whole-body KO (P2 pups) lower ApoA-I; Abca1 mRNA marked; ApoA-I mRNA not (Fig 5) | N | | as above | low |
| 24871327 | ANGPTL4 up in males p=0.0229, not females p=0.0877 (Fig 4F); IPA pathway ranking reverses by sex | N | | R1 Angptl4/triglycerid: other topics. R2 female: other | none |
| 25491415 review | Narrative review: no measured results | | | | none; the held text is not under that PMID name in files/fulltext (dossier only) |
| 27551439 Chang 2015 | WWOX suppresses TPC6A-delta aggregation about 50% (COS7, about 300 cells, Fig 5b) | N | | R1 TRAPPC6/TPC6A/TIAF1: 5 hits in other-protein cards. R2 Chang/PMID: 0 | none to low (transfected, non-neural) |
| 27551439 | MEF shuttling 40-60 vs 20 min; WT TPC6A equally apoptotic; no WT comparator in vivo (Fig 2a-b, 4a, 7) | N | | as above | none |
| 15064722 Ludes-Meyers 2004 | WW1 binds only PPPY among four ligands; no statistics | P | N carries WW1 for HIF1A, and DVL2 scaffold, not this peptide specificity | R1 PPxY/PPPY/WW1/pull-down: 4 N hits read. R2 Wbp1/Dvl2: 2 hits | none (see SCI's WW1-PPxY branch)|
| 15064722 | SIMPLE needs WW1 and the first PPSY (Fig 3a-b), MCF-7 | N | | R1 SIMPLE/PIG7/COTE1/LITAF: 0 relevant. R2 NF-kB activating: 0 | none |
| 15064722 | Endogenous WWOX perinuclear/Golgi, not mitochondrial (MCF-7, Fig 4) | U | | one set only (perinuclear/Golgi/mitochondrial localisation): 0 | possibly the LDH/PDH localisation premise; not tested further |
| 30619736 Hussain 2018 TAP-MS | HEK293T TAP-MS: 216 prey after filters, n=2 purifications | P | N: only the unvalidated GCN1 prey (score 0.133, no empty-vector control) | R1 TAP-MS/MUSE/tandem affinity: 1 hit. R2 HEK293T: cards are other proteins | none |
| 30619736 | Validated prey SEC23IP, SCAMP3, VOPP1 (co-IP, over-expressed); PPxY-motif enrichment IS>0.3 in 14/32 | N | | R1 SEC23IP/SCAMP3/VOPP1: 0. R2 Hussain 2018/PMID: 0 | none to low |
| 42397075 Steinberg 2026 | MYC top upregulated in WWOX-deficient RG; MYC raised in all three mutant lines | C | N anchors | | none |
| 42397075 | RG shift to S/G2M, M down (about +0.77, +0.52, -0.39) | C | N "S and G2M" | | none |
| 42397075 | A51 normalises SOX2+, not layer markers | C | K "partial and selective" | | none |
| 42397075 | AAV9: SATB2 up to about 11x; WWOX protein 0.4-7x WT by line (SCAR12 0.1 to 7) | P | N carries SATB2 overshoot; protein range not found | R1 SATB2/overshoot: carried. R2 "0.4 to 7"/protein relative to WT: 0 | adds the uncontrolled-expression range to the dose limit on C01 |
| 42397075 | WOREE vs SCAR12 near-indistinguishable in neurons | U | | one set only (WOREE versus SCAR12/ribosomal genes): 0 | would bear on whether patient lines separate by allele |
| 42397075 | Oligodendrocyte/myelin enrichment term and lipid-synthesis terms moving opposite (Fig 6E) | P | N "no annotated oligodendrocyte"; the 6E term is not | R1 lipid synthesis/oligodendrocyte myelin term: 0. R2 GSEA/enrich: other datasets | low: no myelin inference from the term |

## (b) Ten NOT_CARRIED results with the highest decision value

1. Het Tc-MEP latency equals null, amplitude normal (32000863). Source: files/fulltext/PMID32000863_Cheng2020_PMC.xml and Cheng2020_assets; manifest PMID32000863.json verbatim_locators entry "heterozygotes have a Tc-MEP latency" (figure number not re-opened by me). Could change: heterozygote premise and a carrier readout.
2. Rat lde/lde normal serum at 28 d vs mouse metabolic crisis (19500159). No held file under that PMID name in files/fulltext; dossier fulltext_dossiers/PMID19500159.md quotes the Discussion; the claim is cited to unread FT-041. Could change: whether hypoglycaemia drives excitability.
3. Muscle cKO glucose intolerance, insulin, weight (30755385). files/fulltext/PMID30755385_AbuRemaileh2019_PMC_r2.xml, Fig 1E, 1H. Could change: tissue-of-origin of glycaemia.
4. Structure precedes seizure: cortical thinning E16.5, DCX high, apoptosis about 5x, vermis fusion (32000863). Same XML; supplement PMID32000863_Cheng2020_supplementary.pdf. Could change: timing limit on acute seizure-drug cards.
5. Peripheral nerve Schwann apoptosis and onion-bulb degeneration (32000863). Same XML. Could change: PNS endpoint and hazard logic.
6. S-HT spectrum, evoked brackets, untested S-HT vs control (33914858). files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf, Fig 2D and 2F, Suppl Fig 3B (supplement folder alongside). Could change: heterozygote premise in the brief.
7. P47T cholestasis, nephropathy, organ weights (36828035). Supplementary Table 4 (NIHMS1957654 supplementary tables, named in manifest PMID36828035.json; I did not locate the docx on disk); files/fulltext/PMID36828035_Hussain2023_PMC.xml. Could change: systemic organ limit.
8. Olig2+ cells fall while Mbp area is unchanged (36828035). PMC.xml Fig 4e; Suppl S6c-d. Could change: OL count as myelin proxy.
9. Residual Wwox transcript by region in S-KO (33914858). Supplement Suppl Table 1 (spreadsheet in PMID33914858_Repudi2021_Brain_operator_supplied_supplement). Could change: reading of cortical slice bursting.
10. Caspase-3 "no OL death" is an image only (33914858). Same PDF, Fig 2 and Suppl Fig 1 panels. Could change: myelin maturation-block premise.

Near misses: Hussain 2019 neurosphere DEGs (channel and receptor transcripts); P47T survival 393 vs 542 d; Mallaret null-mouse audiogenic 3/8 and 4/4; vector glucose dissociation (42422765 Fig 1).

## (c) Counts (results listed: 78)

Carried 30; partly 16; not carried 30; unclear 2. The review (25491415) lists no measured results.

## (d) What I could not check

- I did not open the held PDFs and XMLs page by page for every row. Results come from the dossiers and manifests; two dossier numbers are marked by their authors as chart readings (for example glucose values), not text.
- The brief file path in the dispatch (advisor_pilot_20261113/brainstorm_20261116/experiment_brief_presidio013_sci_20261116/) does not exist; the brief is at drug_repurposing/experiment_brief_presidio013_sci_20261116/ and I used it. The newer work folders under brainstorm_20261116 (r1_conduction_endpoint, premise_checks, source_base_c, r3_erbb4) and files outside the five named consumers were not searched, so a row marked N may be carried there.
- Held text missing by PMID name: 19500159 (Suzuki) and 25491415 (review) in files/fulltext; the Hussain 2023 supplementary tables docx was not located on disk.
- Searches used regex over concatenated files; a result carried in different wording (for example a figure described by effect, not by concept word) could be missed. Rows marked U had one concept-word set only.
- No network use; no agents started.
