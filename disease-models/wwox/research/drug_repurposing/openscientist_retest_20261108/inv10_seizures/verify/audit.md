# Blind audit, INV-10 (seizures versus development, quality of life), verifier vf-10, 2026-11-08

Task record `ORCH-IT38OS-20261108`. Written only in `verify/`. README.md, phase1_note.md and chains.tsv were not opened at any point (parts A and B were written without them, and C and D did not need them). No gate, lint or test was run. Labels: DATO, INFERENZA, IPOTESI. No dose, schedule, route or clinical preference is stated or implied here.

## 0. Routes and depth actually used

All 16 PMIDs read were claimed with `paper_packet.py claim --actor vf-10` before opening. Every route below returned source text directly (structured full text or abstract), none through a page summariser. One route was blocked or empty and is listed.

| Source | Route | Depth |
|---|---|---|
| 34634460 | PubMed tool full text (PMC8609180), read end to end; second independent copy: NCBI PMC OAI record by plain `curl` (HTTP 200, about 155 kB, body, figure legends, tables, back matter); regex counts on that copy | full text of main body, legends and tables; supplementary files (Figs S1-S4, Table S1) NOT read |
| 39101447 | NCBI PMC OAI record (PMC11298992), Abstract, Case presentation, Results, Discussion | full text |
| 42949433 | PubMed tool full text (PMC13715567) incl. Table 1; abstract also via metadata | full text |
| 39933386 | PubMed metadata abstract only (no PMC copy) | abstract only |
| 42721537 | PubMed metadata abstract only | abstract only |
| 42520581 | PubMed metadata abstract only. Europe PMC search says not open access, not in PMC; doi.org led to a publisher landing redirect, not followed further (access wall expected, recorded as unreachable) | abstract only |
| 42237860 | NCBI PMC OAI record (PMC13394045), searched for the quoted sentence and for WWOX | full text, keyword-level |
| 41442931 | PubMed metadata abstract | abstract only |
| 42735667 | Europe PMC search record (abstract) | abstract only |
| 42953089 | NCBI PMC OAI record (PMC13714648), abstract plus keyword search | full text, keyword-level |
| 34747138, 42422765 | NCBI PMC OAI records, abstract plus targeted keyword search (34747138: seizure, PTZ, EEG, timing) | abstract plus targeted passages |
| 32000863 | NCBI PMC OAI record, Results, Discussion, Methods, Fig. 7 legend; Fig. 7 image viewed (PMC cdn jpg) | full text; figure viewed |
| 39039877, 36779245 | PubMed metadata abstract | abstract only |
| 12040897, 19362867, 15658788, 40088508 | PubMed metadata abstract | abstract only |

Europe PMC REST full-text endpoint returned HTTP 500 once; not retried (the NCBI route worked).

## 1. Part A, verdicts per proposition (summary)

| Id | Verdict | Depth | One-line reason |
|---|---|---|---|
| D01 | SUPPORTED | full text | Matches; see 2.1 for two refinements (order of events, "only case") |
| D02 | PARTLY | abstract and full text | Item describes the report accurately; the cited source 42949433 disclaims the causal reading and the report states it more strongly than its own limitation |
| D03 | PARTLY | abstract only | "All seven" is not stated per patient in the abstract; IESS sentence scope and WWOX count unresolved (2.4) |
| D04 | PARTLY | abstract only for Oliver 2023 | Genotype stratifies survival (mortality), not shown for seizure control or development; "Established" is not supported as worded |
| D05 | SUPPORTED | full text | Verified, with nuance on "gap junction dependent" (2.5) |
| D06 | SUPPORTED | full text, two routes | No AMPA antagonist experiment; one AMPA mention (2.2) |
| D07 | SUPPORTED | abstract only | Quote and finding verified; population cohort abstract verified (18 of 64) |
| D08 | SUPPORTED | abstract only (42520581), keyword full text (42237860) | Exclusion of LGS, DS, TSC verified at abstract level; limits in 2.6 |
| D09 | SUPPORTED | abstract plus passages | Mouse rescue verified; "development" is mouse phenotypes; same laboratory origin |
| D10 | PARTLY | full text (42949433), abstract (others) | KCNQ2 figure is cohort-level in the abstract; the full text and Table 1 give a mixed KCNQ2 picture (2.3) |
| D11 | SUPPORTED | full text and figure | Lithium in all three genotypes (figure viewed); ethosuximide in the same paper |
| D12 | SUPPORTED | abstract only | 2 of 12 seizure-free; "untested candidates" is the producer's inference |
| D13 | PARTLY | full text, keyword-level | Quote verified verbatim, but review covers LGS, DS and TSC only, WWOX not mentioned; module-level absence cannot be verified by me |

Counts: SUPPORTED 8 (D01, D05, D06, D07, D08, D09, D11, D12), PARTLY 5 (D02, D03, D04, D10, D13), NOT SUPPORTED 0, UNVERIFIABLE 0.

## 2. Part A, detail

### 2.1 D01, PMID 39101447 (WWOX case, full text)
DATO. Case text: focal seizures from 19 days; the case was reported with levetiracetam plus a second agent controlling early seizures for about 3 months, then a third agent for about 3 months; spasm onset at 8 months; after vigabatrin was added "epileptic seizures gradually decreased"; at 11 months "no apparent seizures", while video-EEG "showed clinical seizures, but these were not noticed at home by her parents"; at last follow-up (13 months) no visible seizures. Abstract order: "Her developmental delay gradually worsened, and she suffered infantile spasms. After treatment with vigabatrin, seizures subsided." Developmental statement in Results: body skills "slightly developed" before 8 months, milestones not reached after 8 months (spasm onset 8 months, vigabatrin after that). So the item is right that the stall starts at spasm onset before vigabatrin.
Refinements for the producer (INFERENZA): (a) the report (L41, L76, L86) reads the abstract's "worsened" as worsening in spite of controlled seizures; the abstract places it before the drug, so the report's "contradicted by the one responsive case" is not supported. (b) The report's "only published WWOX-DEE case documenting a sustained antiseizure response to a specific drug" is not shown by the report: this same paper records earlier control by two other agents for about 3 months each, and the module's earlier INV-10 package counts other partial or transient responders; "sustained" here is 11 to 13 months of a single patient. (c) The case series from the same paper's Discussion cites WWOX reports where vigabatrin effect was poor, so one case cannot stand for a vigabatrin class signal.

### 2.2 D06 and the PMID 34634460 AMPA search (asked specially)
Route: PubMed tool full text of PMC8609180 read end to end; independent second copy (NCBI PMC OAI XML, body plus back matter, 75 kB of plain text after tag stripping); case-sensitive regular expressions. DATO results on the full text: "AMPA" 1 hit (Results 2.3: "indicating no overt change in the proportion of the NMDAR:AMPA response", about mEPSC decay time constant); AMPAR 0; NBQX 0; CNQX 0; DNQX 0; GYKI 0; kainate 0; kynurenic 0; CPP 0; MK-801 0; ifenprodil 0; felbamate 0; perampanel 0; topiramate 0; lithium, ethosuximide, vigabatrin, cannabidiol, fenfluramine all 0. Methods 5.4 (Pharmacology) lists only four compounds: tetrodotoxin, d-APV, carbenoxolone, brilliant blue FCF. Results 2.2 applies only d-APV, carbenoxolone and brilliant blue FCF to bursts. Conclusion: the item is SUPPORTED. Residual risk: supplementary files not read; but Methods list four compounds, so a hidden AMPA antagonist arm is very unlikely. (A first case-insensitive search gave 16 "AMPA" hits from words such as "sample"; this is a regex artefact, corrected by case-sensitive matching.)
Additional DATO the producer should carry: Results 2.2 calls d-APV a "glutamatergic blocker" and the paper's heading says "glutamatergic blockade abolishes spontaneous bursting", but only an NMDA-site antagonist was used, so non-NMDA ionotropic contribution to bursts is untested, not excluded. Felbamate and perampanel have different targets from d-APV (INFERENZA, pharmacology outside this paper, not checked in a source).
A report sentence to correct (L38): "no WWOX patient or model has been treated with an NMDAR- or gap-junction-directed agent against this readout" is false as worded for the model: d-APV and carbenoxolone were applied to the same bursts in this paper. What is untested is felbamate and perampanel specifically, and an AMPA arm.

### 2.3 D10, the KCNQ2 figure in PMID 42949433 (asked specially)
DATO, abstract: "KCNQ2 variants were the most frequent genetic cause (29.4%)"; "Seizure freedom was achieved in a subset of patients, particularly those with KCNQ2-related DEE"; "severe-to-profound intellectual disability affected 71.7% of evaluable patients and persisted even among those who became seizure-free". The 71.7% figure is whole-cohort (full text: 43 of 60 evaluable). The abstract does not give a KCNQ2-specific persistence figure.
DATO, full text (producer read the abstract only; the paper is open access): Discussion says persistence of severe-to-profound impairment "in most patients who achieved durable seizure freedom (including a substantial proportion of the" KCNQ2 subgroup (the gene name is stripped in the PMC rendering, so the subgroup identity is inferred from context). Table 1 (62 patients, 15 with KCNQ2): 9 KCNQ2 patients are controlled or resolved. By my tally of the ID column, 4 of the 9 have severe ID (by the GDD column, 5 of the 9 are severe), 4 have moderate and 1 mild. The extraction of a table from the PMC text is a risk for misalignment; the columns were checked row by row. Also the paper states that seizure burden, age at seizure control and cumulative treatment were not quantified, that a contribution of epileptic activity "cannot be excluded", and that the data preclude causal inference.
Verdict on the report's use (INFERENZA): the report (L10, L21, L72) attributes "severe-to-profound disability persists" to KCNQ2-related DEE. The source supports it for the cohort and only partly for the KCNQ2 subgroup (about 4 of 9 by my count, mixed picture). The report's "fixed substrate" reading and "WWOX behaves like KCNQ2" are a transfer by analogy stronger than the source. Producer correction in 4.
Other D10 citations: 12040897 is a 2002 review chapter on surgically treated symptomatic infantile spasms (abstract confirms the two quoted sentences); 19362867 is a narrative review (abstract confirms "an early response to treatment seems to be of predictive value for the cognitive outcome in children with cryptogenic spasms"; predictive, not causal; it lists an early and sustained response as favourable for infantile spasms generally, not only cryptogenic); 15658788 is a review of cognitive and behavioural correlates of tuberous sclerosis whose abstract does say "Seizure control is important for developmental outcome and quality of life" (so the report's "considered important" is accurate for that sentence, but it is an authors' statement in a review, not a measured effect).

### 2.4 D03, the IESS statement in PMID 39933386 (asked specially) and the Argentine WWOX series
DATO, abstract of 39933386 (24 infants with IESS and hypsarrhythmia, genomic study 2019 to 2022): "A genetic etiology was identified in 50 % of cases" (12 patients; 13 variants). Sentence in the report: "Developmental delay preceded seizure onset in all patients, persisting or worsening thereafter." The sentence follows the description of the 12 genetic cases; "all patients" could also be read as all 24; the abstract does not say which. WWOX is named twice: once in the list of single nucleotide variants ("7/13 ... in KCNQ2, STXBP1, SCN8A, CDKL5, UGDH, and WWOX") and once in the copy-number list ("5/13 ... UBE3A-GABRB3-GABRA5, SCN2A-SCN1A-SCN9A, and WWOX"). The number of WWOX patients is not stated: at least 1 patient, at most 2 variant entries; whether the two WWOX entries are one patient (a compound change) is unknown (IPOTESI; the abstract says two cases were recessive). The delay statement is therefore not WWOX-specific; the report's "IESS cohort data show" (L72) and the classification row "Consistent across cohorts" (L77) overstate. Full text not reachable (no open copy).
42721537 (Argentine series of seven): abstract says "Epilepsy was drug-resistant in all" and "Developmental delay was evident from birth with generalized hypotonia, acquired microcephaly, and impaired visual attention"; the delay sentence is series-level, not stated per patient; five of seven started with focal seizures, two with IESS at onset, median onset 3 months. "All seven" is the module's and the producer's reading of the abstract. Full text not reached. Verdict PARTLY at abstract level.

### 2.5 D05, PMID 34634460 (full text)
DATO verified: neuron-specific (Synapsin-Cre, flox) Wwox knockout, slices from mice 13 to 17 days old; bursts present in 36 of 42 knockout slices, 0 of 11 wild type, 4 of 23 heterozygous slices (heterozygotes without behavioural seizures; hippocampal slices without spontaneous bursts). d-APV eliminated bursts; carbenoxolone decreased frequency by 87 percent and duration by 18 percent, with no recovery after washout; the pannexin blocker had no effect. The paper itself lists off-target limits of carbenoxolone (NMDA receptors, pannexin channels). So "gap-junction dependent" rests on a partial effect of a non-selective agent; the paper's abstract nonetheless says "These bursts were NMDAR and gap junction dependent". INFERENZA (producer): carry "carbenoxolone, partial, irreversible" with the item. The report's "increased excitatory postsynaptic current amplitude" is a shift in the amplitude distribution (mean amplitudes 23.3 versus 24.7 pA); the paper reports no change in the current-frequency slope, hyperexcitability being attributed to subthreshold properties. The report's "intrinsic hyperexcitability" is therefore a narrower claim than it sounds. The report also calls the slice bursts "the network substrate of seizures" (L36); the paper calls them "a marker of the underlying network hyperexcitability".

### 2.6 D08, PMIDs 42520581 and 42237860 (asked specially for LGS, DS, TSC)
DATO, abstract of 42520581: "...patients with developmental and epileptic encephalopathies (DEEs) and complex treatment-resistant epilepsies (TREs) other than LGS, DS, and TSC", systematic search of Embase, Medline and Cochrane in March 2024, 32 studies, 1343 patients; 31 of 32 studies reported improvement in a non-seizure outcome "in ≥ 1 patient"; "mainly identified observational studies with moderate to high bias risk"; narrative summary. So the exclusion of Lennox-Gastaut, Dravet and TSC is stated in the objective, at abstract level. Not determinable: whether an individual included study enrolled mixed populations that contained some patients with those syndromes (full text not open access, not reached). The report (L31) says "across DEEs and treatment-resistant epilepsies" and does not state the exclusion; the report's later "baseline" use of CBD data for genetic DEEs therefore omits that the two best-known DEE syndromes were excluded by design. Two of four authors list the CBD manufacturer as affiliation (abstract affiliations); the report does not mention it. The report's descriptors "largely open-label" and "caregiver-reported" (L31, L117) are not in the abstract (the abstract says observational, moderate to high bias, narrative); unverified at abstract level.
42237860: sentence located verbatim: "Early data suggest fenfluramine and cannabidiol may benefit alertness, behavior, sleep, and communication beyond seizure reduction, while acknowledging that LGS-specific evidence remains preliminary." The paper is an expert-panel framework for assessing non-seizure impact in LGS, not a drug-benefit analysis; the report drops the "preliminary" clause and turns "beyond seizure reduction" into "direct CNS effects" (INFERENZA of the report). WWOX does not occur in the full text. Verdict SUPPORTED for the item as stated.

### 2.7 D04 (no PMID in the report)
DATO (abstract of Oliver 2023, PMID 36779245, a module source): 13 patients, genotype classes null/null, null/missense, missense/missense; biallelic null has lower survival (log-rank p about 0.009). No stratification of seizure control or development is reported in that abstract. The two abstracts I read (39039877: 12 children, 2 seizure-free, 9 still with seizures; 42721537: drug resistant in all) report no genotype comparison of seizure control or development. The report's "stratified by genotype ... rather than by seizure control" is an unsourced contrast; "Established" is not supported for development. Mortality stratification is supported. Two PubMed searches I ran returned only 36779245.

### 2.8 D07, D09, D11, D12, D13 (short)
- D07 DATO: abstract of 41442931 confirms two children, new symmetrical signal change in globus pallidi and thalami "consistent with VABAM", and the generic question about GABAergic pathway or delayed myelination. Population cohort 42735667 (abstract): 18 of 64 (28.1%) with VABAM; association with exposure measures attenuated by model specification; genetic epilepsy 9 of 18; GABA-A subunit variants in both groups; WWOX not mentioned; authors call it hypothesis-generating. The report's "WWOX-relevant" safety signal is an inference.
- D09 DATO: abstract of 34747138 quote verified verbatim ("specific neuronal restoration of WWOX expression rescued brain hyperexcitability and seizures, hypoglycemia, myelination deficits, and the premature lethality and behavioral deficits"); in the body, no spontaneous seizures were observed in rescued mice and hyperexcitability was assessed by cell-attached recordings (no EEG found in the text); neonatal delivery. 42422765 abstract: survival, growth, metabolic function, behavior and fertility restored; "Early neuronal hyperexcitability was suppressed"; early postnatal window. Same laboratory: 42422765 lists the senior author of the laboratory whose earlier paper the first paper cites as "we recently demonstrated" (reference to Repudi 2021); I did not retrieve the 34747138 author list from the record; so same origin is DATO for the second paper and strongly implied for the first. "Development" in the report is mouse growth, behaviour, myelination, survival: INFERENZA boundary correctly flagged by the item.
- D11 DATO: Fig. 7d viewed. PTZ versus PTZ plus lithium is significant (four asterisks) in wild type, heterozygous and knockout mice, so lithium is not WWOX-specific; the effect is a reduction in stage score (knockout peak about 3.5 down to about 1.5), the abstract says "abolishes the onset". Ethosuximide (Fig. 7b) is significant in the knockout only, not in wild type or heterozygote, in the same paper; Discussion says lithium is "better than" it. The report names neither the paper nor ethosuximide, and "the only pharmacological node with an existing drug" (L26) is wrong as worded.
- D12 DATO (abstract of 39039877, 12 children, Peking): 1 death, 2 seizure-free, 9 with seizures at follow-up of 11 months to 5 years 3 months; developmental data in the abstract are narrative ("global developmental delay in all 12"). No information on duration of freedom or on development of the two seizure-free children. The report's premise "there is no population of seizure-controlled WWOX children" (L109) is contradicted by this series (2 of 12). Perimeter of the report: 41 papers, no search string (L140).
- D13: abstract of 42953089 contains the quoted sentence verbatim ("growing evidence indicates that non-seizure manifestations often represent the main determinants of long-term disability, quality of life, and caregiver burden"). The review concerns Lennox-Gastaut, Dravet and tuberous sclerosis; the word WWOX does not occur in the full text. The report presents it as DEE-wide. The module-level absence claim (no QoL measure in the WWOX reports read) cannot be tested by me beyond the three WWOX sources I read (39101447 full text, 42721537 and 39039877 abstracts), where none appears.

## 3. Part B, coverage audit (12 points from the complete original report)

Read: all 140 lines of `INV-10_seizures_development.txt`. Points chosen to include list ends, compounds in passing, hedges and each class of caveat.

| # | Report content (anchor) | In extraction.tsv | Result |
|---|---|---|---|
| 1 | dismech knowledge base entry declines to claim efficacy, drug resistance as class property (L16) | E07 | PRESENT |
| 2 | spontaneous bursting called "the network substrate of seizures" (L36) | E24 (no such phrase) | PRESENT_NARROWED |
| 3 | no WWOX patient or model treated with NMDAR- or gap-junction-directed agent (L38) | E26 note | PRESENT (repeated without flag) |
| 4 | diagram labels: "NOT reversed by seizure control (observed clinically)", lithium and felbamate/perampanel boxes (L48-71) | E47 (arrows), E48 (statement) | PRESENT_NARROWED (labels in E21, E26, E45, E48) |
| 5 | "exactly what the single vigabatrin-responsive case and IESS data show" (L72) | E48 | PRESENT |
| 6 | TSC example given as "e.g." with PMID 15658788 (L106) | E17 | PRESENT |
| 7 | n = 1 hedge, milder SCAR12 or hypomorphic genotypes not excluded (L111) | E50 | PRESENT |
| 8 | developmental outcomes narrative, small seizure effects could be missed (L113) | E51 | PRESENT |
| 9 | mice die within weeks, cannot test chronic control (L115) | E38 | PRESENT |
| 10 | "Uncouple remyelination from WWOX restoration" (L132, terse list end) | E58 | PRESENT |
| 11 | footer: 5 iterations, 6 findings, 41 papers, quotes from abstracts (L140) | E65 | PRESENT |
| 12 | interface text "View full report" (L2) | E67 | PRESENT |

Result: 12 of 12 present (10 PRESENT, 2 PRESENT_NARROWED), 0 MISSING, so the extension scan was not triggered by a miss. I still scanned all remaining lines for hedges, side remarks and compounds in passing and found only marginal narrowings: (a) L23 explanation that the link "appears where there is no fixed structural or genetic lesion" is only implied in E16 and E18; (b) E39 omits "neuropsychiatric function 9/9" and the other categories before the ellipsis (counts quoted partially, harmless); (c) L12 and L28 "drug avoidance" framing for vigabatrin is in E32 as "caution". Every named compound (lithium, felbamate, perampanel, vigabatrin, cannabidiol, fenfluramine, AAV9-WWOX, "selective GSK-3 inhibitor") has a row. Coverage of the report is complete at row level. Two annotation errors in notes are listed in section 6 (E12 note).

## 4. Part C, reconciliation sample (8 rows of `reconcile.tsv`)

Classes: new_to_legend 3 of 4 existing rows sampled (E10, E39, E33); already_present_and_used 2 (E21, E24/E25); present_not_used 2 (E26, E27); superseded_or_contradicted 1 (E23). All four required class minima were available.

| Row | Pointer check | prior_brief_fate check (previous package `seizure_function_inv10_20261107/BRIEF.md`) | Finding |
|---|---|---|---|
| E10 (new) | `fulltext_receipts.py status --pmid 39933386` returns an empty list; git grep over `drug_repurposing` finds the PMID only inside this package; abstract content matches note (WWOX one gene among many, count unstated) | "omitted": the brief contains no mention of the PMID | PASS |
| E39 (new) | status for 42520581 empty; abstract confirms "other than LGS, DS, and TSC" and moderate to high bias | "omitted": brief names cannabidiol only as a studied class and in item 3C; the review is not named | PASS |
| E33 (new) | pointer "none" correct | "omitted": nearest text is brief item 3D ("produce no autonomous indication to exclude or change a therapy"), which narrows rather than omits the same area | MINOR: fate arguably "narrowed (3D)" |
| E21 | `needs/needs.json` contains `NEED-GSK3B-DEREPRESSION` with counter-evidence "Lithium suppressed PTZ-induced seizures in all three genotypes, wild type included" (confirmed by Fig. 7d, viewed) | "modified: brief 3C corrects 'only lithium'": brief 3C says "correct 'only lithium'" | PASS for pointer and fate; the note claims `audit_p8` states the wild-type effect, but `aed_compare_it31_20261107/verify/audit_p8.md` row 24 says the wild-type effect was UNVERIFIABLE from text; the figure now resolves it |
| E24, E25 | `research/deepdive_manifests/PMID34634460.json` exists; `nmda_inv05_20261107/output/README.md` exists; carbenoxolone caveats match the paper | "modified": brief 3C says "The d-APV block was done in the Wwox model: it does not validate felbamate or perampanel" | PASS |
| E26 | `cards/F04_nmdar_intervention_class.card.json` mentions felbamate | "narrowed" matches 3C | PASS |
| E27 | `aed_compare_it31_20261107/output/comparison.tsv` perampanel rows exist (rows 7, 8, 16, 17, 18); row 16 lists patients 6 and 13 of 36779245 with perampanel and the adult case of 39507621 | "modified: brief 3C splits exposure, attributable outcome, designed study" matches 3C | PASS |
| E23 (superseded) | `NEED-T-TYPE-CALCIUM` exists; its observation matches Fig. 7b (ethosuximide significant in knockout only) | "modified: brief 3C" matches ("correct 'only lithium' by considering the ethosuximide experiment") | PASS |

Prior-brief fate was checked against the previous BRIEF.md on all 8 sampled rows (at least 4 required). One adjustment suggested (E33). Also E19 ("superseded"): brief item 2 says "Do not classify WOREE as a 'fixed substrate'", which matches the classification.

## 5. Part D, evidence sample (`evidence.tsv`, all 10 rows checked)

| Row | Verbatim? | Carries the proposition? |
|---|---|---|
| EV01 | Yes (abstract) | Yes with the producer's own scope caveat; ambiguity 12 versus 24 patients also open (2.4) |
| EV02 | Yes (abstract) | Yes: WWOX named in SNV list and again in the CNV list |
| EV03 | Yes (abstract) | Yes; KCNQ2 29.4 percent of the diagnosed cohort (15 of 51) |
| EV04 | Yes (abstract) | Yes; 71.7 percent is 43 of 60 evaluable. Whole-cohort in the abstract; full text adds the KCNQ2 subgroup nuance (2.3) |
| EV05 | Yes (abstract) | Yes, a counter row |
| EV06 | Yes (abstract Background) | Yes at abstract level |
| EV07 | Yes (abstract) | Yes |
| EV08 | Yes (Results 2.3) | Yes; "only AMPA mention" confirmed by my independent search; no NBQX, CNQX, felbamate or perampanel hit confirmed |
| EV09 | Yes (abstract) | Yes |
| EV10 | Yes (Methods 5.1; the gene name is italicised and shows up in one rendering only) | Yes |

Gaps in evidence.tsv (no row for the decisive propositions D01, D04, D07, D09, D11, D12, D13): these rest on earlier receipts or on module records; I re-read D01, D07, D09, D11, D12 and D13 sources above and they hold; D04 holds for mortality only.

## 6. Corrections the producer must make

1. `reconcile.tsv` row E12 and `extraction.tsv` E12 note: "WWOX not stated to be included" / "WWOX inclusion unknown" is wrong; the abstract of 40088508 lists WWOX among commonly implicated genes (147 children, yield 61.9 percent). Replace with: WWOX named among commonly implicated genes; count not stated; seizure outcome assessed at six months only.
2. `reconcile.tsv` row E14 and `evidence.tsv` EV04 note: add that the full text (open access) contains a KCNQ2 subgroup statement and Table 1; by my tally 4 of 9 KCNQ2 patients with controlled or resolved epilepsy have severe ID, 4 moderate, 1 mild (table extraction risk). "Whole cohort, not KCNQ2-specific" is right for the abstract only.
3. `extraction.tsv` E26 note and `reconcile.tsv` rows E26/E27: replace the repeated report sentence by: d-APV and carbenoxolone were applied to the Wwox-knockout bursts in the same paper; felbamate, perampanel and any non-NMDA ionotropic antagonist were not tested; the paper's AMPA mention concerns mEPSC decay only.
4. `reconcile.tsv` row E40 and `decisive.tsv` D08/D13 "not read": PMIDs 42237860 and 42953089 are open access; sentences verified, WWOX not mentioned in either; 42237860 is an assessment-framework paper and says LGS-specific evidence "remains preliminary"; 42953089 covers LGS, DS and TSC only.
5. `reconcile.tsv` row E39 and `extraction.tsv` E39 note: the descriptors "largely open-label, caregiver-reported" belong to the report, not the abstract (abstract: observational, moderate to high bias, narrative); add that two of four authors list the CBD manufacturer.
6. `reconcile.tsv` row E21 note: replace "aed_compare audit p8 ... state lithium also suppressed in wild type" by: audit p8 row 24 marked it UNVERIFIABLE from text; Fig. 7d (viewed here) shows it significant in all three genotypes; `needs/needs.json` already states it.
7. `reconcile.tsv` row E33: fate "narrowed (brief 3D)" rather than "omitted".
8. `reconcile.tsv` rows E08/E09: add that the report's "only published case with sustained control" is unverified and that the paper itself records earlier control by two other agents; state the response window (11 to 13 months).
9. `decisive.tsv` D03: state "all seven" is a series-level abstract sentence, not per patient; state the IESS sentence scope is 12 genetic or 24 total, unresolved at abstract level, and the WWOX count is at least 1 (two named entries).
10. `decisive.tsv` D04: change status to "mortality only (36779245); stratification of seizure control or development not found in the two WWOX series abstracts read; the report's 'Established' unsupported for those endpoints".
11. `decisive.tsv` D06/D05: add that the paper's heading and text call d-APV a "glutamatergic blocker" while only NMDAR was blocked; carbenoxolone decreased frequency by 87 percent (not abolished) and was irreversible.

## 7. Open uncertainties

- Full text of 39933386, 42721537 and 42520581 not reached (no open copy; publisher page not followed). The scope of the IESS sentence, the per-patient delay statement and the composition of the CBD review's included studies stay at abstract level.
- Supplementary material of 34634460 not read (Methods list four compounds, so an AMPA antagonist arm is very unlikely).
- Table 1 of 42949433 was parsed from text; the 4 of 9 count is mine and should be re-read from the rendered table before it is quoted.
- 34747138 author list not retrieved by me; same-laboratory origin of the two gene-therapy papers is DATO for the second and inferred for the first.
- Whether Fig. 7d, panel d, lithium effect in wild type reflects a different PTZ protocol from the knockout arm is not stated in the text; n per group is small (6 to 12).
- Module-level absence claims (no QoL measure in WWOX reports read; no other sustained response) are not testable from the three WWOX sources I read.
