# ADV-292 increment 2: blind second-reader report, copied verbatim from the delegate transcript

Delegate: legend-delegate, model sonnet, effort high stated in the dispatch. Sentences S6a to S10 (file `BLIND_SENTENCES_INC2_SCI_20261126.md`). The reader saw the sentence file and the source folders only, none of the first reader's notes. The delegate names the first author of 39923817 as Wood and of 31781019 as Gureviciene (the repository file name for 31781019 says Kam2019 and an earlier note of mine said Wiseman for 39923817; the article XML gives Wood and Gureviciene).

BLIND VERIFIER REPORT, ADV-292 increment 2 (sentences S6a to S10)
Each sentence was judged only against the folder it names. I did not use the network or write any repository file. The first reader's notes were not consulted.

Held files per folder:
- F: article XML only. The supplement (Figs S1 to S8, Tables S1 to S5) is not held. This leaves unjudged anything that rests only on the supplement, such as Fig S6A (the CSCS-alone Scn4b qPCR).
- G: article XML, Fig 1 to 3, Table 1 and 2 images, MOESM1 and MOESM2 docx, MOESM3 xlsx.
- H: article XML, Fig 1 to 6, MOESM1 pdf and MOESM2 xlsx.
- I: article XML, Fig 1 to 4, MOESM1 to MOESM18. I read Table S1 (MOESM1) and the text of MOESM2.
- J: article XML, Fig 1 to 13, Image_1, supplementary Table_1.docx (per-mouse counts), main PDF.

---

## S6a (folder F, Wood et al. 2025, PMID 39923817)

Verdict: STANDS. It is an accurate summary. One optional addition is listed at the end.

| Separable claim | Verdict | Source |
|---|---|---|
| The two-cysteine mutant (C696S/C698S, "CSCS") lost deacetylase activity in vitro | STANDS | Results: "The cysteine mutants exhibited almost no deacetylase activity (Figure 2A)." The assay used FLAG-HDAC5 immunoprecipitated from HEK293T cells with a class IIa HDAC kit. The paper says "almost no", not "none". The single mutants were only partly reduced. |
| It abolished the effect of nuclear (3SA) HDAC5 on one transcript | STANDS | "HDAC5-3SA, but not HDAC5-3SA-CSCS (Figure 6C) or HDAC5-CSCS (Figure S6A), significantly reduced Scn4b mRNA levels in the NAc." The transcript is Scn4b only. |
| It abolished the effect on a behaviour in rat NAc | STANDS | "HDAC5-3SA reduced cue-induced reinstatement of cocaine seeking, neither HDAC5-CSCS nor HDAC5-3SA-CSCS mutants affected cued seeking (Figure 3E)." The test was AAV expression in rat NAc, male and female Long Evans rats. |
| No SLC2A1 or glucose readout | STANDS | I searched the article XML for SLC2A1, Slc2, GLUT, glucose and the word "glucose". There were no hits. The only "Glut" hit is the reagent L-Glutamine. |
| Loss of binding to another factor is not excluded | STANDS | Discussion: "we cannot rule out the possibility that the CSCS mutation disrupts HDAC5 binding to some other factor that exhibits deacetylase activity ... or that it confers a gain-of-function recruitment of an inhibitory protein." The CSCS mutation did not alter HDAC3 or MEF2C binding. |
| The older "no neural catalytic arm" statement is out of date | STANDS | This is repository reasoning, not a source claim. It is consistent with the Conclusions: "provide an update regarding the role of intrinsic enzymatic activity in class IIa HDAC function." |

Optional addition: the same CSCS mutants also abolished the effect on NAc MSN firing rate (Fig 5B-D, rat slice electrophysiology). The cysteines coordinate a structural zinc ion. The catalytic-site mutant D870N also lacked activity (Fig 2C). Neither point makes the sentence wrong.

## S6b (folder F)

Verdict: STANDS for the part resting on this paper.
- "A catalytic-domain mutant of HDAC5 exists in rat neurons for other outputs." STANDS. It was expressed in rat NAc neurons in vivo and in cultured rat striatal neurons (MEF2 reporter). Outputs: Scn4b mRNA, excitability, cocaine seeking.
- "None reads SLC2A1 in a human neural cell." STANDS. The only human cells in the paper are HEK293T (deacetylase assay, co-immunoprecipitation). No SLC2A1 or glucose readout exists (search as in S6a). HEK293T cells are not neural.
- The "no ranked unit / not a depth of zero" remark is repository bookkeeping and was not judged against the source.

---

## S7a, S7b, S7c (folder G, Pagnamenta et al. 2023, PMID 37946251)

**Searches made**
- Article XML: WWOX, Piard, exon, RNA, protein, PVS1.
- MOESM1 and MOESM2 docx (parsed with zipfile, including comments and footnotes): WWOX, Sev001, chr16, 78291861, His236, mitochond, epilept.
- MOESM3 xlsx (shared strings plus the dump): WWOX, Sev001, Piard, 30356099.

**Findings**
- WWOX appears in only one patient, case 009Sev001.
- The main-text Methods describe RNA-seq for some cases (PAXgene blood). That passage names no WWOX case.
- The docx files have no WWOX or 009Sev001 content. MOESM2 narratives cover other cases (ARX, APP and others).

**S7a verdict: STANDS**
- Table 1 (image) row 009Sev001, WWOX, SV_DEL, 219 kb, "Reported as Patient 11 (Table S1) in case series in Piard et al [97]". The quote is verbatim, apart from the bracketed [97].
- Table S7, rows 19 and 20, both with M (ACMG criteria) = "PVS1, PM2, PM3":
  - Row 20 is the in-frame SV deletion chr16:g.78291861_78511176del.
  - Row 19 is the insertion giving p.His236fs.
  - So "null criterion (PVS1, PM2, PM3)" is correct for the exons 6-8 deletion.
- Text: "in-frame 219 kb deletion of exons 6-8 of WWOX ... in trans with a c.705dup p.(His236fs)".
- Validation for this case is DNA-level only. Table 1 lists "PCR and Sanger sequencing" and the text says "previously reported". I found no RNA or protein assay for this patient in any held file, by the searches above. Treat that negative as stated for the searched files.
- Not judgeable from folder G: "the genotype matches Piard's Supplementary Table 1", and the paper numbers (PAPER 117 and others).

**S7b verdict: STANDS**
- The in-frame deletion of exons 6-8 plus c.705dup p.(His236fs) is stated in the text and Table S7.
- Human, DNA only: supported by the same searches.
- Minor: Table S7 gives zygosity "hom" for the c.705dup row and "het" for the SV row, while Table 1 says "CH". This is a sheet quirk and does not contradict the sentence.

**S7c (PAPER 218 part only) verdict: STANDS**
- "In-frame exons 6-8 deletion coded PVS1 (null) with no RNA and no protein measured" is supported (Table S7 row 20; no RNA or protein assay found).
- Table 1 lists "Severe Epileptic Encephalopathy", WWOX, CH (compound heterozygous).

---

## S8a, S8b, S8c (folder H, Hamanaka et al. 2025, PMID 40858643)

**Relevant rows**
- Supplementary Data 1, row 25 (xlsx), case Pt2317:
  - WWOX NM_016373, c.517-1G>A, chr16:78386859G>A.
  - Consequence type "Exonic or near-exon variant". Protein column ".".
  - Compound heterozygous, Maternal, Novel. CADD 25.1. ACMG "Pathogenic".
  - Criteria: "PVS1, PM2, PM3, PP3".
- Supplementary Data 2, row 44 (xlsx), case Pt2317:
  - "1 exon CNV", Chr16:g.78140467_78313935delinsCA, "WWOX exon 5 (NM_016373)".
  - Compound heterozygous, Paternal, Novel. "Pathogenic".
  - Criteria: "PVS1, PM2, PM3". There is no PP3. WES resolvable = NO.
  - SV callers Manta, Smoove, Delly, Canvas and CNVnator: all YES. MELT: NA.
- Main Table 2 gives Pt2317 as "WWOX c.517-1G>A, Comp het, P, ES-detectable Yes" and a second row "Ex5 DEL, P, No". It prints no intron number.
- Supplement PDF (ACMG section): PVS1 was applied by the ClinGen decision tree for "canonical ±1 or 2 splice site variants, and exonic CNVs". PM3 was assigned when the two variants were "confirmed to be inherited in trans from each parent, based on Sanger sequencing and/or breakpoint PCR". PP3 for splicing variants was applied "when the SpliceAI delta score exceeded 0.2".

**Searches for RNA or protein work on Pt2317**
- "2317" and "WWOX" in the article XML, the supplement PDF text and the xlsx shared strings, plus RNA, protein, western, trio and phas in the XML.
- The RNA-seq in this paper is lymphoblastoid cell line (LCL) RNA-seq, named only for Pt2190, Pt2074 and Pt2286, plus RT-PCR for some splice variants. I found nothing for Pt2317. Treat the negative as limited to these files.

**S8a verdict: MUST CHANGE (one parenthetical)**
- "Both consequences are predicted by rule (PVS1, PM2, PM3, PP3)".
- Only c.517-1G>A carries PP3. The exon-5 deletion is coded PVS1, PM2, PM3.
- Corrected wording: "Both alleles are coded PVS1 (c.517-1G>A: PVS1, PM2, PM3, PP3; exon-5 deletion: PVS1, PM2, PM3), by the ClinGen PVS1 decision tree, with no RNA and no protein assay reported for this patient."
- The claim "no RNA and no protein assay; a classification, not a measurement" STANDS. The paper itself says the criteria were applied by decision tree. Sanger/PCR was DNA confirmation of parental phase only.

**S8b**
- Genotype/model line (c.517-1G>A plus single-exon deletion spanning exon 5; trio-phased): STANDS.
  - The source gives "1 exon CNV, WWOX exon 5" and parental origin of each allele (maternal SNV, paternal CNV). PM3 is defined as trans-confirmed by Sanger/breakpoint PCR in the parents.
  - The CNV coordinates span about 173 kb. The paper still labels it a "1 exon CNV" (Ex5 DEL).
- "Human, DNA only, trio-phased": STANDS. The family is not stated to be a trio; both parental alleles are assigned.
- "T3, an intron-5 acceptor allele": ADD. This is unsupported as a source statement.
  - The source never gives an intron number. It types the allele "Exonic or near-exon variant". The word "acceptor" and "intron 5" occur nowhere for this allele.
  - Searched: intron, acceptor, Int5, "intron 5" in the XML, supplement and xlsx.
  - The only "acceptor" hits are generic SpliceAI text and a different variant (c.265-2104G>A).
  - Add: "(intron number and acceptor class derived by this repository from the HGVS position and the WWOX exon map; the source gives only 'Exonic or near-exon variant', c.517-1G>A)".
- The distinction from c.517-2A>G of PAPER 039 rests on other papers and was not judged here.

**S8c (PAPER 219 part only) verdict: STANDS for what rests on H**
- "Exon-5 deletion coded PVS1 (null) with no RNA/protein measured": supported (Data 2 row 44, M44 = "PVS1, PM2, PM3").
- "The supplementary row types it «Exonic or near-exon variant» and prints no intron number": verified. Supplementary Data 1 row 25 col F reads "Exonic or near-exon variant". Table 2 and the Data 1 and 2 rows print no intron number.
- So the repository's own statement that "intron-5 acceptor" is its derivation is correct. This matches the S8b ADD.
- "One blot and one PCR, both qualitative": no blot appears for these alleles in folder H. If that premise label is meant to cover PAPER 219, it does not rest on H. Only DNA-level PCR/Sanger confirmation exists in H.

---

## S9 (folder I, Chen et al. 2015, Mol Neurodegener, PMID 26419537; clause about the primary paper only)

Verdict: ADD. Both numbered factual claims hold, but two limits are missing.

**Claim 1: "a wild-type arm with no effect"**
- Supported for the main wild-type arms:
  - Text: "none of the concentrations used had any significant effect on the lifespan of wild-type N2" (Table S1: N2 on PBS control: 1 mg/ml +3.56% p=0.40; 2 mg/ml +1.29% p=0.51; 4 mg/ml -7.71% p=0.50; N2 on empty-vector RNAi (L4440) -2.05% p=0.92).
  - No effect on N2 food-race and thrashing; none on the Tau-model wild-type control worms (CZ1200 thrashing and lifespan). Replicate unit: worms (n about 50 to 130 per arm).
- Not all wild-type rows are null. Table S1, N2 on hsp-1 RNAi: +17.72% (p=2.2e-08, n=118 treated vs 116 control). In wild-type N2 on daf-16 RNAi: +1.08% (p=0.89, no effect).
- The paper's transcriptomic analysis used N2 and CZ1200 wild-type controls. Genes common to all four strains were induced by ethosuximide, so the wild-type arm shows no phenotypic effect but does show a transcriptional response.
- The Discussion also notes older work reporting wild-type lifespan extension by ethosuximide (refs 39, 41).
- Add "on lifespan, food race and thrashing, in untreated N2 and CZ1200 worms on vector RNAi; N2 on hsp-1 RNAi was extended +17.7%".

**Claim 2: "direct test that loss of the worm T-type channel does not remove the benefit"**
- Supported. The test used cca-1(ad1650), a deletion or loss-of-function allele.
  - Fig 2a: thrashing in Tau V337M and Tau V337M;cca-1 worms rose to similar extents (day 1 and day 3; * to **).
  - Fig 2b / Table S1 lifespan: Tau V337M +29.26% (p=6.5e-09, n=116 per arm); CK10; cca-1(ad1650) +26.62% (p=2.2e-09, n=112 vs 114).
  - The cca-1 single mutant itself: +1.83% (not significant).
- Gaps in the sentence:
  1. This test was done in the Tau V337M frontotemporal dementia (FTDP-17) model, not in the dnj-14 model. The authors say crossing cca-1 with dnj-14 is technically hard because both genes are on the X chromosome.
  2. The daf-16 dependence was tested only in the dnj-14 model (RNAi: +26.29% on vector vs +5.60% on daf-16 RNAi, p=0.15). The two tests were therefore in different models. The paper does not show DAF-16 dependence of the Tau benefit, or the cca-1 independence of the dnj-14 benefit.
  3. The authors caveat: "we cannot rule out redundancy with other channel subunit homologs that share a putative ethosuximide binding site."
- The main text reports "25% and 16%" for the Tau and Tau;cca-1 lifespan gains. Table S1 gives 29.26% and 26.62%. The text and the table do not match, and I could not tell which experiment the text refers to. Either way, the benefit persists and is significant.
- Suggested wording: "FOXO-pathway rescue in worms: ethosuximide extends lifespan of the dnj-14 mutant in a daf-16 RNAi-dependent way (wild-type N2 lifespan unchanged); in the separate Tau V337M model, loss of the worm T-type channel cca-1 did not remove the thrashing or lifespan benefit (PMID 26419537)".

---

## S10 (folder J, Gureviciene et al. 2019, Front Neurol, PMID 31781019; APP/PS1 clause only)

Verdict: MUST CHANGE. The sentence does not say which effect is meant. I read it as the ethosuximide (200 mg/kg i.p.) response per spike class, the only drug effect the paper compares across genotypes. "Same-direction effects in both genotypes for the spike classes present in both" is not supported as written.

**What I computed**
- Source: Supplemental Table 1 (docx and dump), per mouse and per session.
- Mice: 8 APP/PS1 male mice (IDs 30, 31, 76, 82, 96, 97, 103, 124) and 6 wild-type littermates (IDs 32, 77, 78, 83, 87, 108). All mice included.
- Saline baseline: mean of the saline sessions per mouse (mouse 96 has C1 only). Ethosuximide: the single D session per mouse.
- I computed the ethosuximide/saline ratio of group means, on raw counts and on counts per hour of immobility, plus the number of mice going down, up or unchanged.
- Replicate unit: mouse (each session is 3 h).

**Ethosuximide/saline ratio of group means (per-immobility-hour rate; raw counts agree in direction unless stated)**

| Spike class | APP/PS1 (n=8) | Wild-type (n=6) |
|---|---|---|
| C (cortical) | 0.73 | 0.61 including mouse 78; about 1.7 (14.3 to 24.6 per hour) excluding it, up |
| M (muscle twitch) | 0.60 (down) | 0.65 (down) |
| CH | 0.30 (down) | 0.13 (down) |
| SPL | 1.86 (up) | 2.48 (up) |
| FSPL | 0.02 (down) | 0.00 (down) |
| SWD | 1.03 on rate; 0.39 on raw counts | 1.35 (up) |
| CHhp | 0.65 | not present in any WT session |
| GS | 0.92 | 0.79, from near-zero counts (about 0.2 to 0.4 per session) |

**Cortical spikes (C), wild-type**
- The paper removes one wild-type mouse from the cortical analysis as an outlier (single unilateral spikes about once every 20 s). By the table, that is mouse 78, with 548 and 526 saline spikes in 3 h.
- Without mouse 78, the wild-type direction for cortical spikes is up (per-hour 14.3 to 24.6; raw 33.2 to 62.8; Fig 11A shows the WT black dots rising on ethosuximide). APP/PS1 goes down. The direction therefore differs between genotypes, under the paper's own exclusion.

**Spike-wave discharges**
- SWDs are present in both genotypes (WT counts are low but present in 5 of 6 mice). Direction: APP/PS1 down on raw counts (0.39), flat on rate; WT up. The paper reports no significant ethosuximide effect in either genotype (WT p=0.70, TG p=0.22).
- Giant spikes in wild-type are rare. The paper reports only the APP/PS1 effect for giant spikes (ESM p=0.88, "mixed").

**Paper's own statements**
- Drug effects were tested as one-way repeated-measures ANOVA, including levetiracetam, within genotype.
  - CH: WT p=0.12, TG p=0.04.
  - SPL: WT p=0.04, TG p=0.30.
  - FSPL: both significant.
  - C and M: neither genotype significant.
  - SWD: neither significant.
- Text: "In as much as spikes were present in wild-type mice, their response to AEDs seemed to follow the pattern of APP/PS1 mice."
- Per-mouse direction is mixed (for example SPL, 2 of 8 APP/PS1 mice go down; C wild-type, 2 of 6 down).
- The paper stresses "large individual variability" and could not run a two-way genotype-by-drug model.

**Corrected wording**
"In APP/PS1 and wild-type littermates (8 and 6 male mice, 5 to 6 months), ethosuximide 200 mg/kg i.p. 30 min before a 3 h recording changed cortico-hippocampal spikes (down), fast-spindle spikes (down) and spindle-associated spikes (up) in the same direction in both genotypes (group means). Significance differed by genotype, and cortical spikes, muscle-twitch spikes and spike-wave discharges showed no significant effect in either. The authors describe the wild-type response as 'seemed to follow' the APP/PS1 pattern, with no formal genotype-by-drug test (PMID 31781019)."

---

## Summary table

| sentence id | verdict | one-phrase reason |
|---|---|---|
| S6a | STANDS | CSCS mutant: almost no deacetylase activity, no Scn4b repression, no cue-seeking effect; no SLC2A1 or glucose; binding caveat stated |
| S6b | STANDS | rat NAc/striatal neurons only; HEK293T not neural; no SLC2A1 anywhere |
| S7a | STANDS | Table 1 verbatim Patient 11 quote; Table S7 PVS1, PM2, PM3; DNA-only validation |
| S7b | STANDS | exons 6-8 deletion plus c.705dup, human, DNA only |
| S7c | STANDS | PVS1-coded exons 6-8 deletion, no RNA or protein found in held files |
| S8a | MUST CHANGE | PP3 only on c.517-1G>A; exon-5 CNV is PVS1, PM2, PM3 |
| S8b | ADD | genotype and trio-phasing fine; "intron-5 acceptor" is not in source (derivation) |
| S8c | STANDS | verified "Exonic or near-exon variant" and no intron number; exon-5 CNV PVS1, no RNA or protein; "blot/PCR" not from H |
| S9 | ADD | wild-type and cca-1 claims hold, but cca-1 test was in the Tau model while daf-16 was in dnj-14; N2 on hsp-1 RNAi was +17.7% |
| S10 | MUST CHANGE | cortical spikes (WT up if the paper's outlier is excluded, TG down) and SWD not same direction; only CH, SPL, FSPL clearly agree; significance differs by genotype |

Not done or not reachable: the F supplement (Figs S1 to S8, Tables S1 to S5) is not held, so the CSCS-only Scn4b qPCR (Fig S6A) is unjudged. Nothing from Piard 2019 and no repository paper-registry or claim entries were available, so the cross-paper statements in S7a and S7c (PAPER 117, "genotype matches Piard") are unjudged. I did not open S9's MOESM3 to MOESM18 beyond Table S1 and the text of MOESM2.
