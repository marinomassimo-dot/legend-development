# ADV-295 block 2, record 2 (PMID 33704440): first reader report, verbatim

Subagent hand-back saved verbatim by SCI on 2026-11-28 (legend-delegate, claude-sonnet-5-5, effort high read back from the transcript). Model output, hypothesis level, not medical advice; not edited.

---

**Record 7: PMID 33704440 (El Ghaleb 2021), consumer DL-MECH-170. First reading, hypothesis level, not medical advice.**

The main result is that the gain-of-function half of the bullet is WRONG as written on this paper. Two of the six carriers of a gain-of-function variant have no seizures. The loss-of-function half cannot be assessed from this paper, which studies no loss-of-function variant.

Locators: "S1/S3" are Supplementary Tables, "SFig" Supplementary Figures, "Fig" main figures.

## (1) Statements

| id | verbatim statement | verdict | grounds |
|---|---|---|---|
| R7-S01 | "**Symptomatic in every paper that looks.**" | NOT ASSESSABLE | The bullet does not say what is symptomatic or which papers "look". In this paper the only treatment datum is one patient and a seizure outcome (Discussion, last paragraph). It reports no developmental or disease-course outcome under treatment, so it can neither support nor refute a symptomatic-versus-modifying claim. A universal over unnamed papers cannot be tested from one. |
| R7-S02 | "Genotype decides whether a T-type block is mechanism-matched" | ADD | This is the consumer's inference. No blocker was applied to any variant channel (Methods read in full; searches below). Authors: Cav3.3 is "an attractive target for pharmacological treatment with licensed T-type channel blockers" and "Further studies are required to establish a target therapy". Direction was established by patch-clamp per variant, not by genotype alone. |
| R7-S03 | "gain-of-function T-type variants cause seizures" | **WRONG** | S1 row "Seizures", patients 1 to 6: Yes, Yes, **No, No**, Yes, Yes. Patients 3 and 4 carry p.(Ile860Met), classed gain-of-function, and were 28 y 11 m and 31 y (S1 "Age"). Discussion: "Together, our data add CACNA1I to the list of disease genes associated with motor and cognitive impairment **with or without epilepsy**." Cited Cav3.1 A961T: "cerebellar atrophy with or without epilepsy". Causation of seizures is also hedged: "could explain seizures" (Abstract), "plausible cause" and "At present it remains uncertain to what extent..." (Discussion). |
| R7-S04 | "loss-of-function variants cause neurodevelopmental disease" | NOT ASSESSABLE (not carried by this paper) | All four studied variants are classed gain-of-function. The only T-type loss-of-function material is cited, in the Introduction: CACNA1I p.(Arg1346His), a schizophrenia risk variant, and "CACNA1I loss-of-function variants disrupt neuronal excitability and network activity and **may contribute** to the development of schizophrenia, autism and/or other complex neuropsychiatric disorders". That is not a causal statement. It rests on PMID 40825030, which I did not open. |
| R7-S05 | "...without seizures" (of loss-of-function variants) | NOT ASSESSABLE (not carried by this paper) | The paper says nothing about seizure status for p.(Arg1346His) or any T-type loss-of-function variant (I read that paragraph; searches below). In its own data, the two individuals with neurodevelopmental disease and no seizures carry a **gain**-of-function variant, so absence of seizures cannot indicate loss. |
| R7-S06 | "T-type variants" (the class: the rule covers Cav3.1, 3.2 and 3.3) | ADD | Own data cover only CACNA1I (Cav3.3). Cav3.1 and Cav3.2 appear by citation only. Germline Cav3.2 gain-of-function is cited for primary aldosteronism and hypertension ("causing... primary aldosteronism"; M1549V/I "incomplete penetrance"), with no seizure phenotype stated for it. Introduction, on CACNA1G/H in inherited epilepsy: "none of the investigated variants have been undoubtable identified as causing seizure phenotypes... genetic risk factors". The paper states no general gain/loss seizure rule. |

**Citation attribution.** PMID 33704440 can be cited for CACNA1I gain-of-function being associated with a neurodevelopmental spectrum with or without epilepsy. It cannot be cited for the loss-of-function half.

**What PMID 40825030 would have to carry for the bullet to stand:**
- Functionally measured loss-of-function T-type variants in affected individuals with neurodevelopmental disease.
- None of those individuals with seizures, with ages and how seizures were ascertained.
- Support for causation.
- Coverage of more than one T-type gene, or the sentence must name the gene.

Even then it could not rescue "gain-of-function variants cause seizures" as a universal, or a two-way rule that separates gain from loss by seizure status.

## (2) Corrected sentences

- **S03 (WRONG):** "In PMID 33704440, four CACNA1I (Cav3.3) variants classed gain-of-function in transfected HEK293T cells were found in six individuals (four families) with neurodevelopmental phenotypes; four had seizures (one with onset at 58 years) and two, both p.(Ile860Met), had none reported at 28 and 31 years (no EEG data)."
- **S02 (ADD):** "A variant's measured channel direction bears on whether a T-type block is mechanism-matched (our inference): PMID 33704440 tested no blocker on any variant channel, and reports one patient (p.(Ile860Asn)) with improved seizure control on ethosuximide, dose not given."
- **S06 (ADD):** "These data are for CACNA1I only, and do not establish a seizure-based rule separating gain from loss across T-type genes."
- **S04/S05:** keep only if PMID 40825030 carries them for a named gene, and cite it alone for that half.

## (3) Strict candidates (WRONG as written)

- **R7-S03 only.** Its sentence is the whole second sentence of the bullet ("Genotype decides ... without seizures (PMID 33704440, PMID 40825030)."). The blind reader should get that sentence verbatim.
- S04 and S05 are not counted: unsupported by this paper, but possibly carried by the unopened one.

## The checks requested

**Gene, variants, individuals.** CACNA1I only; heterozygous missense; six individuals in four families (S1, S2). All four variants are absent from gnomAD (S2).

| Patient | Variant, origin | Sex, age at last exam | Development | Seizures (S1) |
|---|---|---|---|---|
| 1 | I860N, de novo | F, 8 y 1 m | severe global delay, no motor milestones, nonverbal | yes, onset 4 m, difficult to treat |
| 2 | I860M, origin not determined | F, 58 y | IQ 70-85 | yes, onset 58 y, controlled on "Diphantoine" |
| 3 | I860M, maternal | M, 28 y 11 m | IQ 50-70 | no (EEG: no data) |
| 4 | I860M, maternal | F, 31 y | IQ 36-51 | no (EEG: no data) |
| 5 | I1306T, de novo | F, 21 m | severe delay, hypotonia | yes, onset 2 wk, controlled (Keppra; earlier response to phenobarbital) |
| 6 | M1425I, absent in mother, father untested | M, 8 y 3 m | developmental impairment, nonverbal | yes, onset 2 y, controlled |

By variant, seizures were present in I860N 1/1, I860M 1/3, I1306T 1/1 and M1425I 1/1.

**Function.**
- System: human Cav3.3 (AF393329, a shorter I-II linker splice variant), GFP-tagged, transient transfection of HEK293T, whole-cell voltage clamp, 2 mM Ca2+.
- Replicate unit is the cell, from 4 to 6 passages.
- Values are mean ± SEM, variant vs matched WT (S3). V½ is in mV; times are in ms; "r500" is percent inactivated at 500 ms.

| measure (S3) | I860N | I860M | I1306T | M1425I |
|---|---|---|---|---|
| n variant / WT (cells) | 6 / 7 | 7 / 6 | 9 / 9 | 9 / 9 |
| V½ activation | -58.7 vs -42.2 | -49.1 vs -40.9 | -53.2 vs -38.7 | -52.4 vs -38.7 |
| V½ inactivation | -76.2 vs -69.6 | -75.5 vs -69.6 | -71.0 vs -72.5 (ns) | -79.3 vs -72.5 |
| time to peak | 84.8 vs 23.6 | 45.7 vs 22.8 | 78.6 vs 19.8 | 53.0 vs 19.8 |
| r500 | 51.9 vs 98.3 | 87.5 vs 97.1 | 50.2 vs 95.1 | 63.3 vs 95.1 |
| tau inactivation | 564 vs 138 | 214 vs 138 (ns) | 690 vs 79 | 419 vs 79 |
| tau deactivation | 4.8 vs 0.5 | 0.8 vs 0.5 (ns) | 2.0 vs 0.6 | 2.2 vs 0.6 |
| peak current, pA/pF | -45.0 vs -72.9 (ns) | -105.3 vs -118.2 (ns) | -54.7 vs -39.5 (ns) | -109.1 vs -39.5 (P=0.03) |
| window current (Fig 5) | enlarged, left-shifted | left-shifted, not enlarged | enlarged, left-shifted | left-shifted, not enlarged |

- The tau and V½ inactivation rows use n = 6 cells per group (8 WT for I860N-set deactivation).
- **Mixed?** The authors class none as mixed. They note that slowed activation "would represent a loss-of-function", significant only at -50 mV (all four) and also -40 mV (I860N) (SFig 4). My inference, not theirs: the hyperpolarised inactivation in three variants would also reduce resting availability.
- Mutants were expressed without co-expressed WT as far as the Methods state, so heterozygosity is not modelled.
- Action-potential clamp (SFig 3): cells WT 18, I860N 9, I860M 8, I1306T 10, M1425I 9.
- NEURON model (Fig 6): all four lower the firing threshold. This is simulation only.
- Mouse chromaffin cells (Fig 7; only I860N and I860M; 3 culture preparations; unit is the cell):
  - At rest, WT n=4 and I860M n=4 fired; I860N n=11 showed no spontaneous activity.
  - At -70 mV (WT 6, I860N 5, I860M 6), I860N gave only slow oscillations, and "spike-firing ceased completely".
- Seal loss (SFig 6): I860N 15/19, I860M 1/11, WT 0/12 cells.

**Other published T-type variants** (all citation, none the paper's own data):
- CACNA1G de novo gain-of-function: severe motor and cognitive impairment with cerebellar atrophy. M1531V is cited with severe epileptic encephalopathy; A961T with or without epilepsy.
- CACNA1H: germline gain-of-function with aldosteronism and hypertension; somatic I1430T in adenomas.
- CACNA1I p.(Arg1346His): loss of expression and current density; schizophrenia risk; mouse knock-in with sleep-spindle deficit. No seizure status is given.
- The Cav2.1 and Cav1.4 "likely... loss-" remark is not about T-type channels.

**Drugs.**
- None tested in cells.
- Ethosuximide (called "non-selective T-type channel blocker"): Patient 1 only, "improved control of seizures, in particular in a reduction of myoclonic seizures". No dose, age at treatment, duration, co-medication or quantification.
- It appears only in the Discussion. S1 says "controlled to some extent by medication" and names no drug.
- Results say she had daily myoclonic seizures and rare grand mal seizures "that did not respond to treatment". The text does not date this against the ethosuximide course.
- Phenytoin ("Diphantoine"), levetiracetam and phenobarbital are antiseizure treatments in other patients or earlier courses, not tests of T-type block.

**General rule.** Not stated. The authors claim an association/causal link for CACNA1I gain-of-function with a spectrum "ranging from borderline intellectual functioning to a severe neurodevelopmental disorder with epilepsy", and call further therapy studies necessary.

**Dated searches behind the negatives.**
- Date 2026-11-28. Case-insensitive fixed string, one per search.
- Files: the text I converted from the XML (`PMID33704440_ElGhaleb2021_PMC_r2.xml`), the held `awab101_Supplementary_Data.txt`, and `pdftotext -layout` of `PMC8422349.1.pdf`.
- Hit counts are given as XML / supplement / PMC PDF.

| query | hits | note |
|---|---|---|
| "ethosuximide" | 1/0/1 | the Discussion sentence |
| "blocker" | 4/1/4 | discussion and reference titles only |
| "without seizures" | 0/0/0 | |
| "seizure-free" | 0/0/0 | |
| "loss-of-function" | 2/1/3 | the supplement hit is a reference title |
| "loss of function" | 0/0/0 | |
| "Arg1346His" | 2/0/0 in XML and supplement; 2 in PMC PDF | Introduction only |
| "zonisamide", "valpro", "mibefradil", "Z944", "TTA-" | 0/0/0 each | |
| "dose" | 0/0/0 | |
| "co-express", "coexpress", "co-transfect", "cotransfect" | 0/0/0 each | |

## (4) ADDs not in the bullet that matter

I did not check whether any other record holds these.
- Gain-of-function with no seizures at 28 and 31 years, and one onset at 58 years: severity tracks the variant, even at the same residue.
- The I860N chromaffin phenotype is loss of sodium spiking with persistent slow oscillation, so "gain" at the channel is not simply more spikes.
- The ethosuximide report is n=1, uncontrolled and undosed.
- The paper's proposed route to harm includes early developmental calcium toxicity. A seizure response says nothing about that.
- Internal errors, to avoid copying numbers:
  - The Fig 3 legend gives activation shifts of 6.6 and 5.9 mV for I1306T and M1425I. Text and S3 give 14.5 and 13.7 mV; 6.6 and 5.9 match Fig 5 inactivation shifts of other variants.
  - The I860N activation shift is 15.5 mV in the text, but the S3 values differ by 16.5 mV.
  - The SFig 5 legend says tau inactivation is significant "throughout the tested voltage range". Its own table gives ns at -50 mV for I860N and M1425I, and at -40 mV for M1425I.
  - M1425I peak current is "almost 3-fold" in the text and "doubled" in the Fig 3 legend.
  - Methods name a thalamic relay neuron model, while Results call it a TRN model.

## (5) What I opened, could not read, and failures

**Opened:**
- The "Record 7" section and the "Matching rule" section.
- The full XML text, including the reference list (each entry truncated).
- All 7 main figures, viewed as images.
- Supplement: text layer for all 19 pages (held `.txt`); pages 8-17 also viewed as images at 80 dpi (Tables S1-S3, SFigs 1-6).
- PMC PDF: searched by text only, not read page by page.
- Values said to be seen on figures are by eye. Table numbers are from S3.

**Not opened:** PMID 40825030. Nothing touching PMID 42422765. No repository search, no network.

**Failure:** my first command, which combined reading `framework/protocols/delegation_budget.md` §2/§7 with `df -h`, was refused by the auto-mode classifier ("[Unauthorized Access]"). I did not retry the protocol read, so **those sections were not read**. Your "open no other repository file" limit and the standing delegate instruction to read them conflict. I then ran `df` alone.

**Disk:** free space was 1.6 to 2.1 GB, never below 1.0 GB. I wrote about 1.67 MB (1,664,008 bytes of extracts and renders, 2,314 bytes of script) under `/home/desktop/.claude/jobs/fc428159/tmp/b2r2` and `b2r2_scripts`, and **deleted both**. I wrote nothing in the repository and made no commit.

A final `git status` showed one untracked file that is not mine and that I did not open: `BLIND_PACKET_B2R3_35079122_ADV295_SCI_20261128.md` in the batch folder.

Source: PubMed Central copy of PMID 33704440, held locally. I used no PubMed tool and did not retrieve or verify a DOI.
