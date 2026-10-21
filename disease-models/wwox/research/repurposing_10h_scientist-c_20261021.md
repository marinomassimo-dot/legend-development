# Repurposing ten-hour batch, group R3 — downstream pathways and the safety record of their drug classes

- **Actor:** `scientist-c` · **Task:** `REPURP-10H-R3-C-20261021` · **Date:** 2026-10-21
- **context_policy:** `QUESTION_DRIVEN`. The dispatch had the reader open the known-roads note (section 2.4)
  and the rescue-reference scaffold before the first paper, so no reading here is `SOURCE_FIRST`; the
  manifests and the staged receipts say so.
- **Every paper below is NOT WWOX EVIDENCE.** Each is a precedent at class level, measured in tumour cells,
  adult or genetically unrelated mouse models, or clinical series of other diseases. No dose, route,
  schedule, duration or paediatric suitability is recommended or presumed anywhere in this note. Doses are
  recorded only as what a paper did, so that a claim about dose can be tested against it. **Not medical advice.**
- **The four scientific current files, `disease_model.md`, `drug_repurposing/` and
  `repurposing_bridge.py` were not touched.** Receipts are staged, never recorded. One commit candidate
  is written (section 7).
- **Blind locator audit: DONE on six readings (40665325, 38147624, 42310739, 40156289, 35945201, 41980417); OWED on the other eleven and on the candidate.** The six manifests were repaired by the producer on 2026-10-22 and **the repairs are unaudited**. A producer does not verify their own.

> **CORRECTED 2026-10-22 after the blind locator audit of six of these readings** (`page_adjudications/locator_audit_R3_20261022.md`: 129 triples, 78 supported, 46 overshoot, 4 undershoot, 1 unverifiable). The manifests were repaired at source by the producer; **the repairs are unaudited**. Changes in this note: the A51 pharmacokinetic statement and its row in section 5 (the table reproduces neither proportionality nor the earlier sub-proportional correction), the hepatic dose-limiting statement (one hepatic DLT at 42 mg, the other DLT was alkaline phosphatase at 21 mg), the Myc-under-A51 statement and the withdrawn schedule conflict (38147624), the family-to-variant conflict and the variant count (40156289), three statistics and the age range of 42310739, the Rictor and p-Akt statements of 35945201, and the gliosis, normal-brain and safety statements of 41980417. Papers not audited (the other ten readings) are unchanged and remain unaudited.

## 0 · What was read, and how deeply

All 16 selected rows of group R3 were read, in tier order, to the depth stated. Identity (`pubmed_identity_check.py`):
MATCH on all 16. Manifest column: `deepdive_manifest.py --verify-artifacts --require-current-schema`
returned PASS with 0 gaps on all 16. Locator counts are `len(manifest['verbatim_locators']['entries'])`.
Figures were opened as images: embedded 300 ppi rasters where the packet ranker named them, vector pages
rendered at 130 to 300 dpi where it named a vector page, publisher JPEGs only where nothing better existed
(stated per paper in its manifest).

| PMID | Study (class) | Depth | Receipt (staged) | Locators | Figures/supplement debt |
|---|---|---|---|---|---|
| 40665325 | BTX A51 phase 1, adult AML/MDS | complete | FTR-20261021-40665325-01 | 22 | none |
| 38147624 | Csnk1a1 haploinsufficiency + Trp53 mouse leukaemia, A51 | complete | FTR-20261021-38147624-01 | 25 | none |
| 40156289 | CSNK1A1 variants, infantile spasms, HEK-293T | complete | FTR-20261021-40156289-01 | 21 | none |
| 42154236 | Cdk7 loss in cortical glutamatergic neurons | complete | FTR-20261021-42154236-01 | 23 | none |
| 35945201 | Raptor reduction in Tsc1 forebrain knockout | partial | FTR-20261021-35945201-01 | 26 | supplementary figures captions only |
| 41980417 | Clemastine in Pdk1 OPC-lineage knockout | partial | FTR-20261021-41980417-01 | 20 | supplementary figures captions only |
| 35372341 | Clemastine in wild-type neonatal mouse | complete | FTR-20261021-35372341-01 | 20 | supplementary figures not retrieved (declared unavailable) |
| 42401046 | SB415286 (GSK3 inhibitor) in kainate TLE | partial | FTR-20261021-42401046-01 | 20 | ESM Figs 2-4 not opened |
| 36615165 | Sirolimus under age 2, tuberous sclerosis | complete | FTR-20261021-36615165-01 | 19 | no supplement exists |
| 42217144 | Sirolimus dyslipidaemia, neonates and infants | complete | FTR-20261021-42217144-01 | 18 | none |
| 40871085 | Tideglusib population PK, myotonic dystrophy | partial | FTR-20261021-40871085-01 | 16 | Figs 1-3 captions only |
| 42310739 | J4 (ENT1 inhibitor) in Tsc2+/- mouse | partial | FTR-20261021-42310739-01 | 15 | Figs 3, 5, 6, 8 captions only |
| 40911604 | Rapamycin in Npc1 mouse, microglia and myelin | partial | FTR-20261021-40911604-01 | 13 | Figs 1-4 and S1-S2 captions only |
| 38942888 | Clemastine minimum effective dose, neonatal hypoxia | partial | FTR-20261021-38942888-01 | 16 | Figs 3, 4, 6 captions only; supplement not read |
| 39762658 | Microglia-free mouse (Csf1r FIRE) | partial | FTR-20261021-39762658-01 | 15 | Figs 1-6, other ED captions only |
| 37296418 | CSF1R inhibitor in neonatal hydrocephalus mouse | partial | FTR-20261021-37296418-01 | 14 | other figures captions only; pptx not read |

Staged receipts were checked with `staged_receipt_check.py --check-doi` (OK on all 70 files in the directory,
mine included). Peer directories were checked before each paper (`paper_packet.py claim` exit 0 every time).

## 1 · The first-pass observations, paper by paper (each ends with its negative)

### 1.1 The compound class behind the only intervention applied to a WWOX-deficient human neural model

**40665325 (BTX A51, phase 1, adults).** 31 adults, median age 75 (22-84), eight dose levels 1-42 mg; the
42 mg level was stopped after a grade 3 hepatic failure meeting Hy's law with encephalopathy that resolved
within two weeks (the only hepatic DLT; the second cycle-1 DLT was a grade 3 alkaline phosphatase rise at 21 mg); the level of 21 mg three days a week for 28 days was set as recommended phase 2 dose. The
text calls transaminase toxicity "dose-dependent" because it was commoner at 21 and 42 mg, and in the same
paragraph reports 1 of 15 events at 21 mg; the paper tabulates no event count per dose. The supplementary
pharmacokinetic table (read from the docx; N = 1, 1, 3, 3, 3, 8, 5 at 1, 3, 5, 8, 11, 21, 42 mg) does **not** reproduce the text's "dose-proportional
between 1 and 42 mg": per-mg Day 5 AUC runs 43, 200, 140, 117, 166, 180, 114; the log-log slope from 1 to 21 mg is about 1.38 (Day 5 AUC) and 1.36 (Day 1 AUC), so
exposure rises faster than dose; from 21 to 42 mg the Day 5 AUC rises 1.27-fold (3773 to 4773) for a 2-fold dose, Day 5 Cmax 1.19-fold, Day 1 Cmax falls
0.83-fold, and the 42 mg Day 1 AUC cell is blank. With CVs of 22 to 79 percent and N = 1 at two levels the table supports neither proportionality nor a
sub-proportionality claim (an earlier version of this note called the top step sub-proportional; that single 21-versus-42 comparison is withdrawn as a general statement).
The Abstract states that no treatment-related death occurred; six of eleven on-study deaths happened without overt progression. The p53 and MCL1 pharmacodynamics are from CD34-positive marrow
cells of **three** patients, one cell per condition shown, no quantification. In Figure 4 (vector page rendered at 300 dpi) the
RUNX1-mutant line OCI-AML-5 shows MYC faint in **both** lanes, so MYC suppression is not demonstrated in the one mutant line
the paper centres on; pSer5 in HL-60 is not visibly reduced; each line is a single blot without quantification.
Fig. 5C's bracket sits over the 10 nM bars, not an IC50 comparison.
**Negative:** nothing here is neural, paediatric or Wnt; no CNS exposure, no brain penetration, no CNS adverse-event
analysis beyond one encephalopathy attributed to the hepatic event. It supports organ toxicity (liver, GI,
haematological, hypokalaemia) as the class record in adults and says nothing about a developing brain.

**38147624 (Csnk1a1+/- with Trp53 edited, mouse leukaemia).** The transformation rests on **one animal**
(one leukaemic mouse of the Csnk1a1+/- Trp53 group). A51 at 5 mg/kg/day (supplement: five days a week for three
weeks from day 8; the Figure 5 legend says until four weeks after transplant: the two are compatible, day 8 plus three weeks ending about four weeks after transplant; a schedule conflict flagged in an earlier version is withdrawn) reduced blood counts and spleen weight
in a tertiary transplant model but marrow blasts only to P = 0.1352 (blood blasts 0.0709, marrow cellularity 0.0002; WBC, platelet and spleen
panels print no P). The selective effect on the double-hit blasts appears at **one** concentration
(316 nM: about 25 versus about 50 percent viability), and the CK1 inhibitor D4476 was not significantly more efficient in the Csnk1a1+/- cells and blasts than in wild type; the source draws no attribution
from that comparison and none is drawn here. The Myc protein "reduction" under A51
(Fig. 6I) is one unquantified blot (6 untreated and 10 A51 lanes) with no statistic in the figure, legend or Methods: the reduction is stated in the text, not demonstrated. The bands follow the printed
bone-marrow blast percentage only partly (A51 lanes show bands at about 62, 70, 93 and 94 percent and none at 99 percent), so the Myc effect is confounded with blast burden but not simply explained by it. Fig 1A and 1B also show that white cell counts and CD11b+ output are not similar across the genotypes. Figure 1F (400 dpi crop of the vector page) does **not** show the
Hallmark Wnt/beta-catenin set up in the Csnk1a1-haploinsufficient LSKs: it is negative or blank in that column
while the Myc set is positive; the Wnt-up statement for blasts rests on a pathway-footprint tool whose Wnt score is
pale and small (about 0.7 against MAPK about 3), and the Lrp6/GSK3B/Lef1 chain is a CARNIVAL prediction.
**Answer to the attribution question:** this paper does not disentangle Wnt, MYC and CDK for A51. It gives one
concentration at which a p53-mutant leukaemic line is more sensitive, one in-vivo dose level in leukaemia, and a Myc readout that is one unquantified blot. A co-author is a consultant to the company advancing A51.

**40156289 (CSNK1A1 variants, infantile spasms).** Two families; patient 1 had multiple congenital anomalies
and died at one year, patient 2 is a nine-year-old with controlled seizures every 3-6 months. Both are
exome-trio de novo; the supplement lists thirteen other variants "not directly linked", including a de novo
ACTN1 frameshift and a TSC1 variant, admitted as possibly related to the phenotype. The mechanism is entirely
**HEK-293T overexpression** of GFP-tagged CSNK1A1: the missense lowered mRNA and protein, the deletion did not;
beta-catenin co-IP lower and cellular beta-catenin higher for both; MYC and CCND1 mRNA about 1.25-1.5-fold
higher; EdU about 20 percent versus 36 and 30. Fig. 3E's pulled-down band is faint in all lanes (one blot, no
quantification), and a deletion that does not lower CSNK1A1 protein still "reduces" binding. The sentence
that "vinyl chloride" slightly controlled the spasms is a translation artefact, so the treatment history is
unreadable. The Figure 1B sequencing traces fit Family_1 = the six-base deletion and Family_2 = the missense, the opposite of the Results text (missense in patient 1, deletion in patient 2), on which the Discussion builds its genotype-phenotype statement; the panel has no variant labels and no position axis. This is an **unresolved conflict inside the source**; neither assignment is adopted. The HEK-293T arm has no empty-vector control in the text and the source does not state endogenous CK1-alpha status.
**Answer:** CK1-alpha loss of function is **proposed** as epileptogenic through excess beta-catenin, in two families and in a non-neural cell
line. It is not a measured seizure signal in any neural system.

**42154236 (Cdk7 in postmitotic cortical neurons).** Nex-Cre removal of Cdk7 at E11.5: thinner cortex and corpus callosum
at P21 (n = 3 animals, one-sided Mann-Whitney, P = 0.05 is the smallest value the test can return), unchanged neuron
number and layer markers, fewer dendrites (30 neurons from 3 animals), shorter callosal axons in utero-electroporated
P7 brains, normal open field, novel-object and T-maze, but fewer social contacts (about 25 versus 45; interaction time about
52 versus 125 s; n = 11-12) and lower sniffing of two of four urine groups. RNA-seq at P3: 976 genes at FDR below 0.1,
862 down. Four of seven Wnt5a-pathway genes reached P below 0.05 by RT-qPCR with one-sided tests, **Wnt5a itself P = 0.0601**;
Wnt5a protein at 100 ng/mL raised neurite length 52.4 percent and 50 ng/mL had no effect (Dunn P above 0.9999): two doses, one effective, no threshold located.
The pharmacological check with the CDK7 inhibitor YKL-5-124 is a one-to-two well, two-dam panel with **no test**; the vehicle itself
swings from 1.0 to about 1.46 to about 0.56 over 24 h, so "a rapid and important decrease" is not readable from it.
**Negative and answer:** a neurodevelopmental cost of losing **Cdk7 in neurons** is measured (morphology, thinning,
social behaviour) and no seizure or EEG endpoint exists. A CDK7 inhibitor given systemically is a different experiment from a conditional neuronal
knockout; the paper itself warns that THZ1 also blocks CDK12/13.

### 1.2 Direction of Wnt modulation

**42401046 (SB415286, kainate TLE, adult mice).** Adult 8-10 week mice; daily i.p. 14 days from 24 h after kainate; dose 10 mg/kg/day, one level; n = 6 per group.
Wnt activity (Axin2) fell in the ipsilateral dentate after unilateral kainate (bar about -7 against about 15 in saline; points -28 to +23) and in the bilateral model (about 5 against about 17.5); the drug restored both to baseline.
The epilepsy endpoint is **histological**: in the unilateral model dispersion, migration and contralateral cell
count improved; in the bilateral model dispersion, migration and cell count did **not** change and only dendrite
angle did (Figure 4). No EEG, no seizure counting after induction, no behaviour. In saline controls the drug raised Axin2 above baseline
(30 against 15), and the authors cite their own earlier finding that a related GSK3 inhibitor impaired cognitive testing in non-epileptic controls.
The paper's frame calls GSK3 inhibition "releasing the handbrake".
**Answer to question 2:** Wnt **activation** reduced two of four histological remodelling markers in one model and one of four in the
other, in adult mice, during a latent period; that is the opposite direction to Wnt suppression, but it is a different
disease, brain age and endpoint. **No measured window exists in any selected paper in which Wnt suppression in a developing
brain is shown safe or unsafe**; the organoid experiment, the Cdk7 knockout (a non-canonical Wnt5a arm) and the CSNK1A1 variants
(excess beta-catenin) pull in different directions and none is a dose-window study.

### 1.3 mTOR and the myelin / gliosis / hyperexcitability endpoints

**35945201 (Raptor, Tsc1 forebrain knockout).** The only paper in the group that measures myelin, gliosis and
network hyperactivity **in the same genetic neurodevelopmental model**, all with genetic Raptor reduction, not with a drug:
heterozygous Rptor loss moved survival (median 18.5 to 24.5 days; males 5 percent and females 40 percent alive at P40, so
sex-dependent), cortical MBP (KO about 7.3, KO;Het about 10, WT about 13.3; still significantly below WT, P = 0.0002), CA1 GFAP to near WT, and culture calcium
transient frequency (about 11.5 to 9.3 against 7 per minute) while network-event frequency and duration were **not** significantly reduced. Hyperexcitability is calcium imaging in cultured
hippocampal neurons; in vivo EEG was not done. Homozygous Raptor loss gave a severely underdeveloped forebrain. The
postnatal AAV9-shRptor arm raised cortical MBP to a value not distinguishable from WT but **also not distinguishable from untreated KO** (P = 0.4833 on both),
and the treated mice still had spontaneous seizures. "Gene-dose-dependent" survival rests on three genotypes (0, 1, 2 copies) with each step a different phenotype; no
graded function.
**Negative:** no drug in this paper; rapamycin appears only as a culture benchmark that suppresses p-Akt below the Tsc1-loss level.

**41980417 (clemastine, Pdk1 OPC-lineage knockout, induced at P10-12).** Clemastine 10 mg/kg/day from P21 to P58
(single dose; the knockout was induced at P10-12): hippocampal MBP area 0.64 to 1.0, TrueGold 0.69 to 0.99, Olig2, ASPA, VGlut1/Homer1 puncta and c-Fos counts and
Y-maze/NOR performance all return to control level (three to six animals per group). Clemastine in controls did not alter VGlut1 puncta. GFAP is not significantly different between genotypes (one marker, n = 6), which does not show that gliosis is not a phenotype or a treatment target; no EEG,
seizure, body-weight, exposure, histamine or sedation-labelled measure (arm entries and speed are unchanged by clemastine); control plus clemastine arms are plotted in Figs 4 to 7 and are not different from control; mEPSC rests on three animals (about 15 neurons plotted).
**Negative:** the model removes an oligodendrocyte kinase and the drug is given after weaning, outside the infant window; the constitutive version of the model
(seizures, death before P21) is not treated in this paper.

**42310739 (J4, Tsc2+/- adult male mice).** 0.06 mg/mL in drinking water for 10 weeks from 6 weeks of age (Fig 1A runs to 16 weeks, while the Methods give the animal age as 6 to 12 weeks: inconsistent inside the source; an estimated 10.2 mg/kg/day assuming water intake): open-field
centre time, NOR discrimination index (-0.02 to 0.37), diffusion MRI of fornix and callosal body, cortical and hippocampal MBP/PLP, onion-bulb count (2.3 to 0.6 per 100 square micrometres), OPC and APC counts, pS6 and **cFos counts
(a proxy for hyperactivity)**. Histology is three animals per group in most panels (onion bulbs: 3, 3 and 4 animals); the EM g-ratio regression uses individual axons. In the retrosplenial cortex the treated cFos falls **below** the wild-type level (layer V about 7 against 12).
In wild-type mice the text prints F(1,974) = 1.986 with p = 0.0158 for a myelin-thickness comparison and the same F with p = 0.1591 for the slope comparison in the next sentence; that F corresponds to p of about 0.159, so p = 0.0158 is a defect in the source and no finding about J4 on wild-type myelin thickness is drawn. Males only; adenosine itself was not measured.
**Negative:** no seizure phenotype exists in this model; a single drinking-water concentration.

**40911604 (rapamycin, Npc1 mouse, pups through the milk P10-P21).** Rapamycin 40 ug/mL in the dam's water: cerebellar white-matter MBP volume rose about 8,700 to 11,900 cubic micrometres (n = 3 per group), VGLUT2 terminals preserved, microglial
proliferation and CD68 volume down. The same drug **further shortened microglial processes and reduced terminal points** in the molecular layer (total length 197 to 128 micrometres,
against wild type 247). The white-matter microglia were unchanged, so the myelin effect is **not** a microglial effect, and mTORC1 was not hyperactive in the mutant microglia at P7 (pS6 was lower) and rose only by P10.
There is no wild-type rapamycin arm; gliosis is microglial morphology, not GFAP.
**Negative:** the authors themselves read the process shortening as impaired postnatal microglial growth.

**Answer to question 3 (which approved or class-adjacent drugs have measured myelin effects in a genetic neurodevelopmental model, and which also measured hyperexcitability).**
Measured myelin effect in a genetic model: **clemastine** (Pdk1 OPC knockout), **rapamycin** (Npc1), **J4** (Tsc2+/-), and genetic **Raptor** reduction (Tsc1). Hyperexcitability measured **in the same animals or culture**: Raptor (calcium transients in culture; in vivo seizures persisted) and J4 (cFos counts). Not measured with the same drug: clemastine (c-Fos only as activation, no seizure
measure) and rapamycin (no excitability measure). **No selected paper measures EEG or electrographic seizure burden together with myelin after a drug in a genetic neurodevelopmental
model.** That is the missing measurement, not a negative.

### 1.4 Documented harm in developing myelin or microglia (counter-indications to record)

**35372341 (clemastine in healthy neonatal mice).** 50 mg/kg/day i.p. P5 to P20/21 (the Fig. 1 legend prints "50 ug/kg", the text mg/kg, the end day P20 versus P21: three descriptions of one schedule).
Differentiation went up (mature fraction about 67 to 77 percent of Olig2 in callosum) while callosal compound-action-potential velocity fell (about 0.507 to 0.428 mm/s), nodes of Ranvier fell (about 580 to 385 per mm2), myelinated axons
fell (about 288 to 250 per 1000 square micrometres, three animals) and the g-ratio rose in axons under 0.5 micrometre (0.769 to 0.788, three animals: the "***" stands on individual axons). CD11c-positive microglia and IGF
fell. **No behaviour, EEG or seizure measure.**
**Class-level counter-indication to record:** a pro-myelinating drug can reduce functional myelin in a normally developing brain. The reverse case (clemastine in the model of 41980417, in 38942888) is rescue of an injured or deficient state.

**38942888 (clemastine, neonatal hypoxia, four doses).** Doses 0.5, 2, 7.5, 10 mg/kg/day P3-P10. The "minimum effective dose" of 7.5 is a **conjunction rule** (lowest dose above vehicle "by all measures tested") on **four dose points** and two or three outcomes: striatal MBP is already significant at 2 mg/kg (P = 0.003),
corpus callosum area and the oligodendrocyte-fraction measures first at 7.5. The authors concede the true minimum may lie between 2 and 7.5. The step from "ns" at 2 to "significant" at 7.5 on the OPC fraction (0.67 to 0.52) has no point between. Normoxia is never reached (striatal MBP about 290 against 410 in normoxia),
and at 10 weeks the benefit is partial (optic-nerve MBP and callosal area not different from vehicle). PK at 7.5 mg/kg (Cmax 44 ng/mL, t1/2 4.6 h) came from a separate normoxic group; no toxicity study, no maximal tolerated dose, no behaviour; muscarinic-antagonist sedation is named by the authors as a limit.

**39762658 (microglia-free mouse, Csf1r FIRE deletion).** Synapse numbers, intrinsic properties, LGN segregation, PTZ seizure latency and duration (n = 9 and 11) and PFC-hippocampal coherence were **normal** with lifelong
microglial absence. Not null everywhere: a cortical boundary cavity persists to P7, layer-4 NMDAR decay is shorter at P14, and astrocytic GFAP is higher (ED Fig. 8 genotype effect P = 0.0054 neocortex; hippocampus unchanged).
**Reading:** microglia are not required for the tested synaptic milestones; a **genetic lifelong** absence permits compensation and is not a pharmacological ablation in an infant; no myelin endpoint.

**37296418 (CSF1R inhibitor PLX5622, neonatal hydrocephalus and wild-type).** 50 mg/kg subcutaneously P3-P7. At P8 white-matter CNPase myelination in **wild-type** pups fell from about 30 to about 3 percent and OLIG2 density fell (P = 0.011); ventricles in the mutant were larger (P = 0.0323);
no benefit to edema or grey-matter thinning; wild-type myelination recovered by P20 (P = 0.9275, mean about 78 against 90) but treated mutants reached 13.5 percent against 55 (post-hoc P = 0.0167, n = 6 and 5, survivors only: the line has a median survival of 10 days).
**Class-level counter-indication to record:** early postnatal CSF1R inhibition removes microglia efficiently and is **detrimental to early myelin maturation in the healthy brain**, with delayed or absent recovery in a diseased one. One of 24 wild-type pups died during treatment.

**Answer to question 4:** documented harm in developing myelin or microglia exists for **clemastine given to a normally developing brain** (35372341), **CSF1R inhibition** (37296418) and **rapamycin on microglial process growth** (40911604); a lifelong genetic microglial absence (39762658) is not harmful in the tested synaptic domains but is not comparable. All are mouse studies with one dose level except 38942888.

### 1.5 The infant and paediatric safety record of the drug classes (literature observation, never a recommendation)

**mTOR inhibitor, sirolimus — 36615165.** 21 infants with tuberous sclerosis, median start 104 days (3-656); start dose 0.5 mg/m2/day, target trough 3-4 ng/mL, median achieved 4.34 (0.79-13.89). **All 21 had at least one adverse effect;**
anaemia 51-92 percent by age band, thrombocytosis 36-79, hyperlipidaemia 63-100, infections 17-50, neutropenia 10-42, mouth ulcers 3 cases; no grade 4 or 5 and no discontinuation for an adverse effect; one child hospitalised twice for infection (varicella and a bacterial infection). Baseline abnormality was already
present at month 0 (anaemia 10 of 21, hyperlipidaemia 7 of 18), and the denominators change from 7 to 21 per band. The text says median follow-up 12 months, Table 1 says 22 (3-24).
**42217144 (sirolimus dyslipidaemia, ten NICU infants plus a spontaneous-report database).** In the ten infants (median age 44.5 days, six preterm, start 0.02 mg/kg, trough 5-15 ng/mL) all ten had triglycerides in the "high" range after starting; nine total cholesterol; grade 2 triglycerides in four, grade 3 in one; no pancreatitis. Thresholds were pragmatic and sampling non-fasting.
The signal is a **reporting** ratio: adjusted reporting odds ratio 147 (79.7-271.5) for 28 days to 23 months from 19 dyslipidaemia reports out of 248 infant sirolimus reports, against 2.3 in adults; the comparator is all other drugs, there is no denominator and no dose or duration, and the authors call it hypothesis-generating. By this reader's arithmetic from the paper's own counts the share of sirolimus reports that are dyslipidaemia is 7.7 percent in infants, 4.8 percent in 2-11 year olds, 2.7 percent in 12-17 year olds and 6.3 percent in neonates: a smaller spread than the ratio of ratios.
**GSK3 inhibitor, tideglusib — 40871085.** No child was measured: the 16 patients were 13.8 to 34.9 years (the healthy volunteers 60-74). The paediatric content is a **weight-based simulation** (5-75 kg, no maturation function): exposure at 1000 mg falls with weight (a slope visible only at the higher dose; flat at 400 mg), bioavailability is
dose-dependent in a two-level step (400 mg versus higher), not a continuous curve. Earlier-formulation transaminase elevations with food and twice-daily dosing are mentioned; three authors are sponsor employees. There is no safety dataset in children in this paper.
**CDK-adjacent class — 40665325.** Adults only (section 1.1). Liver (one grade 3 failure at the highest level), gastro-intestinal, haematological, hypokalaemia, no tumour-lysis event with prophylaxis; no paediatric exposure.
**Answer to question 5:** the only infant series is for sirolimus, in **tuberous sclerosis, an mTOR-driven disease**, with a near-universal adverse-effect rate that is mostly haematological and metabolic; the infant dyslipidaemia signal is a
spontaneous-report ratio. For the GSK3 class there is **no paediatric safety record in the selected papers** (a simulation), and for the CDK7/9 plus CK1-alpha class **no paediatric record at all**. Monitoring items the authors themselves name: baseline lipids and early repeat after the first weeks (42217144); blood counts, lipids, infections (36615165); liver enzymes with dose escalation (40665325). These are the authors' statements, recorded here as theirs.

## 2 · FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON

Admitted after the readings: `repurposing_known_roads_20261020_scientist-a.md` section 2.4, `drug_repurposing/woree_rescue_reference_scaffold.md`
(sections 2 and 3.1), the group's five questions in the selection file. `registry_records.py get --pmid <PMID> --hops 0` for 15 PMIDs: **NO RECORD MATCHED** for each (a statement about that query, not about the laboratory; 40665325 has the record text quoted
in the selection file). 

## 3 · The five questions of group R3

**Q1. Organ toxicity, exposure and PD of the class behind the organoid intervention; does Csnk1a1 or Cdk7 loss reveal a neurodevelopmental or seizure cost?**
Answered at the level the papers allow. Adults: liver (dose-limiting), GI, haematology, electrolytes; exposure rising faster than dose from 1 to 21 mg and about 1.27-fold for a 2-fold dose from 21 to 42 mg (neither the text's proportionality nor an earlier sub-proportional correction is reproduced by the table; one hepatic DLT at 42 mg); PD shown in three patients. Csnk1a1: a **proposed** seizure/beta-catenin link in two infantile-spasms families and HEK cells, no neural model; Cdk7 loss in postmitotic cortical neurons costs morphology, cortical thickness and social behaviour with no seizure endpoint; Csnk1a1 haploinsufficiency
alone produced no malignancy in the leukaemia model but its attribution of A51 effects is unresolved. **Unanswerable from the selection:** brain exposure of A51, any CNS adverse-event series, and any neural measurement after a CK1-alpha/CDK7/9 inhibitor. The missing measurement is a brain-region
PK or CSF level plus a neurodevelopmental readout in a young animal at more than one dose.

**Q2. Direction of Wnt modulation and a safe suppression window.** Answered above (1.2): activation reduced remodelling markers in adult TLE in the unilateral model, hardly in the bilateral one, with a signal that over-activation in normal brain may impair cognition (author-cited). **No window exists**; declared unanswerable with the missing measurement: a dose-by-timing series of Wnt/GSK3/CK1 modulation in a developing cortex with progenitor and layer-neuron endpoints and an electrographic endpoint.

**Q3.** Answered in 1.3 (which drugs; who measured excitability).

**Q4.** Answered in 1.4.

**Q5.** Answered in 1.5.

## 4 · Where the readings land on the five endpoint families of the rescue-reference scaffold

| Family | What group R3 supplies (all NOT WWOX EVIDENCE) | What it does not |
|---|---|---|
| Excitability / EEG | none with EEG; culture calcium (Raptor), cFos counts (J4, clemastine), PTZ threshold (microglia-free mouse), histological remodelling (SB415286) | no electrographic seizure burden after a drug in any genetic neurodevelopmental model |
| Myelination | clemastine (rescue in a kinase knockout and in hypoxia; harm in healthy pups), rapamycin (Npc1), J4 (Tsc2+/-), Raptor, CSF1R inhibition (harm in healthy pups) | no WWOX-relevant myelin deficit model; the scaffold's M1 baseline (MBP 30-70 percent of WT) has no treated counterpart here |
| Neuroinflammation / gliosis | microglial morphology and CD68 (rapamycin), microglia absence (GFAP higher in cortex, not hippocampus), CA1 GFAP (Raptor) | none separates a glial direct target from a neuronal one |
| Growth / metabolism | sirolimus dyslipidaemia and anaemia in infants | no growth outcome |
| Survival / function | Raptor (survival), Tsc1 model | confounded by sex and genotype-dose |

## 5 · The dose standard applied to every dose claim in the group

CLAIM 011 was narrowed because two dose points cannot locate a threshold and an equality between unequal denominators is not grading. Applied here:

| Claim as printed | Dose points / denominators | Verdict |
|---|---|---|
| A51 hepatic toxicity "dose-dependent" (40665325) | levels not tabulated per event; 1 of 15 at the recommended level | **not graded** by the paper's own data; PK not proportional at the top |
| A51 PK "dose-proportional 1-42 mg" | Supplemental Table 3: seven dose levels, N = 1, 1, 3, 3, 3, 8, 5; Day 5 AUC per mg 43 to 200; 21 to 42 mg Day 5 AUC 1.27-fold for 2-fold dose; Day 1 AUC blank at 42 mg | **not reproduced**: supralinear 1 to 21 mg (slope about 1.38), 1.27-fold at the top step; CV 22-79 percent and N = 1 at two levels support neither proportionality nor sub-proportionality (audit recomputation; repair unaudited) |
| A51 selective for double-hit blasts (38147624) | one separating concentration of five | **threshold claimed, not located**; the other four overlap |
| Wnt5a rescue of neurites (42154236) | 0, 50, 100 ng/mL; 50 is ns | **two effective points of three**; no threshold |
| Raptor "gene-dose-dependent" survival (35945201) | 0, 1, 2 gene copies | **three genotypes**, each a different phenotype and with a sex split; not a graded function |
| Clemastine MED 7.5 (38942888) | 0.5, 2, 7.5, 10; conjunction rule | **a label on a rule, not a threshold**; MBP already significant at 2 |
| Clemastine 10 mg/kg (41980417); J4 0.06 mg/mL (42310739); SB415286 10 mg/kg (42401046); rapamycin via milk (40911604); PLX5622 50 mg/kg (37296418) | one dose each | **dose-dependence not tested** |
| Tideglusib "dose-dependent bioavailability" (40871085) | two levels, 400 and 1000 mg in patients; six groups in healthy adults | **two-level step**, authors concede no continuous quantification |
| Sirolimus hyperlipidaemia "dose-dependent" (36615165) | cited from literature; no dose analysis in the cohort, troughs held in a narrow band | **literature claim, not shown in this cohort** |
| Infant dyslipidaemia signal (42217144) | reporting ratio with no dose or duration | **not a dose claim** |

## 6 · Defaults taken, limits, owed work

- `DEFAULTS_TAKEN`, also in the task JSON: (1) manifests declare `QUESTION_DRIVEN`; (2) figures with only a publisher JPEG as surface were read at that resolution and declared (36615165; Fig. 7-8 of 39762658; ESM Fig. 1 of 42401046);
  (3) papers whose supplement is a docx or xlsx were read as text and supplementary figure images were declared `captions_only` where not opened; (4) receipts for partial readings state `partial_fulltext_read`
  with the unread surface named; (5) the registry comparison used `registry_records.py get --hops 0` only (a PMID-only query).
- **OWED:** a blind audit of the repairs to the six audited manifests, and a first blind audit of the other ten readings of the group and of the 42654068 reading. The audit's findings on the six are summarised in the banner above; the earlier owed items (the Figure 1B trace assignment in 40156289 and the Figure 5 schedule in 38147624) are now settled as, respectively, an unresolved source-internal conflict and a withdrawn conflict.
- **Not done:** no PubMed-wide census was run for these classes; a zero from a title/abstract query would licence only "no paper is indexed", never "never measured" (dismissal ledger D-37).

## 7 · Commit candidate

`research/commit_candidates/CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01.md` (MINOR, additive to `DL-THER-089` BLOCK-1 wording; no consolidated-baseline record touched).

## 8 · Adjacent search and the reading it produced

Question written before opening: *is there a measurement of a Wnt-lowering (tankyrase) drug class in a developing-brain model that reports a peripheral toxicity or a dose-versus-formulation separation?* PubMed queries (title/abstract, 2026-10-21, shared throttle): CSNK1A1 with neurodevelopment/epilepsy returned 2 records (one already read); a CK1-alpha neuronal conditional-knockout query returned 0 (a zero licenses only "no paper is indexed"); CDK7 inhibitor with neuron/brain returned 12, one neuronal (29163040, open access, acquired, not yet read); tankyrase inhibitor with neuro and development returned 2.

**42654068 (esterified XAV939 prodrug and a membrane-coated liposome, Shank3b-/- mouse; NOT WWOX EVIDENCE).** Read to partial depth (figures 3-6 as 330-820 ppi rasters; figures 1-2 and the supplement not read), manifest PASS with 14 locators, receipt staged `FTR-20261021-42654068-01`. 5 mg/kg intravenously for five days in 6-week-old mice improved sociability scores but left contact frequency and interaction time far below wild type and raised AST, ALT, ALP and bile acids (n = 3 per group) with Wnt inhibition in small intestine; at 2.5 mg/kg the uncoated prodrug did **not** help behaviour but still destroyed intestinal villi and raised liver enzymes in wild-type mice (ALT about 35 to 185 U/L), whereas the coated particle did both better. So **toxicity and benefit are separated by formulation, not by dose**, from one dose pair; brain delivery is a label fluorescence, not a drug level. The authors rely on Wnt being low in mature neurons to call the approach safe for the brain and name no developing-brain test. Relevance: a Wnt-lowering class with a measured peripheral (liver, gut) toxicity in a juvenile mouse, counted beside the organoid compound's hepatic signal in adults. **Not** an infant or developing-cortex test.

Reserve for a later pass (acquired or identified, not read): 29163040 (Cdk7 and activity-dependent neuronal gene expression, open access), 27852007 and 36717229 (APC conditional knockout infantile-spasms model; bodies restricted or no PMC XML), 29603837 (tideglusib in juvenile Cdkl5 knockout mice; no lawful body found: no PMCID, Unpaywall closed; park with that cascade).
