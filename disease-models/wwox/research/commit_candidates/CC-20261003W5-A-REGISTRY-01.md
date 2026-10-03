# CC-20261003W5-A-REGISTRY-01 — registry landing for the six PMIDs read in intake wave 5 (Scientist A)

- `context_policy: SOURCE_FIRST`
- Change class: **MINOR**. Six new `PAPER` records and six new `LIT` records; no existing record is
  edited, no claim is created, no `consolidated baseline` claim is touched.
- **Why this candidate exists:** each of the six PMIDs now has a receipt
  (`FTR-20261003-<pmid>-01`), a validating manifest and a dossier, and no registry presence at all —
  `paper_packet.py packet --pmid <N>` returned "no title recorded / manifest: none / prior read:
  depth=none" for all six before this wave. Without these records LINT blocks `BATCH_COMMIT` with
  `ORPHAN_COMPLETE_READ`.
- **Numbers are PROVISIONAL.** Measured with `registry_records.py catalog` in this worktree on
  2026-10-03 after merging `main` at `663970a`: highest `PAPER` = **150**, highest `LIT` = **0443**,
  highest `DIS` = **030**, highest `CORPUS-STUB` = **179**. Scientists B and C of this wave are
  landing their own registry candidates in parallel, so **the integrator re-measures and renumbers in
  event order**; the PMID and the record id must stay in the same section so the orphan check can
  see the pairing.
- All six papers are **about other genes**. None mentions WWOX. Each record says so in its `Role`
  field, so that a later reader cannot mistake a transferable method for WWOX evidence.
- **Nothing here is medical advice.**

## Per-PMID landing summary

| PMID | Provisional PAPER | Provisional LIT | Receipt | Depth |
|---|---|---|---|---|
| 41314141 | PAPER 151 | LIT-0444 | `FTR-20261003-41314141-01` | `partial_fulltext_read` |
| 40988338 | PAPER 152 | LIT-0445 | `FTR-20261003-40988338-01` | `partial_fulltext_read` |
| 39358605 | PAPER 153 | LIT-0446 | `FTR-20261003-39358605-01` | `partial_fulltext_read` |
| 41712282 | PAPER 154 | LIT-0447 | `FTR-20261003-41712282-01` | `partial_fulltext_read` |
| 40809677 | PAPER 155 | LIT-0448 | `FTR-20261003-40809677-01` | `partial_fulltext_read` |
| 41712149 | PAPER 156 | LIT-0449 | `FTR-20261003-41712149-01` | `partial_fulltext_read` |

Every depth is `partial_fulltext_read` and not `complete_fulltext_read`: figure panels were not
rendered for any of the six, and supplements were fetched for one only (PMID 40988338). That is
stated rather than rounded up.

## Ops — `disease-models/wwox/registries/paper_registry_current.md`, `append` (six new records)

```
## PAPER 151
**Short title:** Greenberg 2026 EBioMedicine - the first-in-human high-dose intrathecal AAV9 trial, and the CRIM rule that makes transgene immunity a recessive-null problem
**Full title:** First-in-human high dose AAV9 intrathecal gene therapy for paediatric CLN7 disease: a phase 1, open-label, single ascending dose, non-randomised clinical trial
**Authors:** Greenberg BM, Minassian B, Messahel S, et al.; Gray SJ, Kayani SN
**Year:** 2026
**Source type:** primary clinical study - phase 1, open label, non-randomised, single ascending intrathecal dose, n = 4
**Journal/source:** *EBioMedicine* 2026;123:106044
**Identifier:** PMID 41314141 / PMCID PMC12703863 / DOI 10.1016/j.ebiom.2025.106044
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number; highest `PAPER` measured 150 on `main` 663970a. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41314141-01`; manifest `deepdive_manifests/PMID41314141.json`; dossier `research/fulltext_dossiers/PMID41314141.md`
**Primary pathway:** none for WWOX - AAV9 CNS gene replacement, dose and immunosuppression
**Model/species:** human, four children aged 4-5 years at dosing
**Genotype/model:** biallelic *MFSD8* (CLN7); NOT a WWOX genotype
**Transferability:** T2 for the immunosuppression protocol and the empty-capsid arithmetic; T4 for efficacy
**clinical relevance:** HIGH strategic - the only human high-dose intrathecal AAV9 source in this repository
**Claim links:** none
**Role:** 🔵 **Transferable protocol, not WWOX evidence. The paper does not mention WWOX.** It is the repository's source for the cross-reactive-immunological-material (CRIM) rule: patients predicted to make no protein were classified CRIM-negative and given a THIRD immunosuppressant against a response to the gene product, which makes transgene immunity a problem for a biallelic null rather than a non-problem for a "self" protein. Also the source for a clinical lot at 42% genome-containing particles (so a 1 x 10^15 vg dose carried 2.38 x 10^15 capsids) and for attributing dorsal-root-ganglion toxicity to transgene overexpression. ⚠️ Efficacy is not established: declines on every instrument, no matched natural-history comparator, no dose-response, no transgene-expression measurement in any patient, and no formal statistics. ⚠️ Table 2 does not reconcile with itself: counts sum to 58 against a stated 57, and two rows disagree with their own percentages.
**LIT link:** [[literature_tracking_log_current#LIT-0444]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.

## PAPER 152
**Short title:** Quinlan 2025 Mol Ther - an oversized full-length cassette packages, with a measured yield and heterogeneity penalty, in a heterozygous model
**Full title:** AAV delivery of full-length SYNGAP1 rescues epileptic and behavioral phenotypes in a mouse model of SYNGAP1-related disorders
**Authors:** Quinlan MA, Guo R, Clark AG, et al.; Levi BP
**Year:** 2025
**Source type:** primary preclinical study - vector engineering, AAV-PHP.eB delivery, EEG/EMG, two behavioural assays
**Journal/source:** *Mol Ther* 2025
**Identifier:** PMID 40988338 / PMCID PMC12703155 / DOI 10.1016/j.ymthe.2025.09.040
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-40988338-01`; manifest `deepdive_manifests/PMID40988338.json`; dossier `research/fulltext_dossiers/PMID40988338.md`; supplementary document S1 persisted and read (PDF plus derived text layer)
**Primary pathway:** none for WWOX - AAV cargo size, dose-response, expression ceiling
**Model/species:** mouse, conditional *Syngap1* heterozygote (~55% of wild-type protein)
**Genotype/model:** dominant haploinsufficiency; NOT a null and NOT a WWOX genotype
**Transferability:** T2 for the packaging arithmetic; T4 for rescue, which is measured against a 55%-of-wild-type baseline
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Transferable cargo lesson, not WWOX evidence. The paper does not mention WWOX.** A 5.136 kb ITR-to-ITR cassette above the ~4.7 kb limit packages with a measured two-fold yield loss against a 4.617 kb same-day control and a 94.60:5.40 full-to-empty ratio. ⚠️ Read in the supplement rather than the body, the headline "75.81% full-length" is a 4-6 kb SIZE BIN with a further 15.22% above 6 kb. ⚠️ Table S3 shows 5 of 10 high-dose mice had poor surgical outcomes and only 5 were recorded, against 0 of 8 and 0 of 4 in the lower-dose arms - a dose-confined attrition the Discussion never mentions, which means the high-dose electrophysiology is the surviving half of that group. The authors report a protein ceiling: a 2.5-fold rise in transgene signal produced no further total protein.
**LIT link:** [[literature_tracking_log_current#LIT-0445]]
**Note:** class-level record; no individual-level detail. Not medical advice.

## PAPER 153
**Short title:** Wiseman 2024 EMBO Mol Med - the closest architectural analogue: a complete IND package for a recessive loss-of-function CNS disease, whose immunogenicity arm used wild-type animals
**Full title:** Pre-clinical development of AP4B1 gene replacement therapy for hereditary spastic paraplegia type 47
**Authors:** Wiseman JP, Scarrott JM, Alves-Cruzeiro J, et al.; Ebrahimi-Fakhari D, Azzouz M
**Year:** 2024
**Source type:** primary preclinical study - four cell models, neonatal and adult mouse efficacy, potency assay, two mouse safety studies, GLP non-human-primate toxicology
**Journal/source:** *EMBO Mol Med* 2024;16(11)
**Identifier:** PMID 39358605 / PMCID PMC11554807 / DOI 10.1038/s44321-024-00148-5
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-39358605-01`; manifest `deepdive_manifests/PMID39358605.json`; dossier `research/fulltext_dossiers/PMID39358605.md`
**Primary pathway:** none for WWOX - recessive loss-of-function gene replacement, route, dose translation, window
**Model/species:** *Ap4b1* knockout mouse; wild-type mouse safety studies; wild-type cynomolgus macaque GLP toxicology
**Genotype/model:** biallelic loss of function (AP-4 deficiency); NOT a WWOX genotype
**Transferability:** T2 as a programme template - it is the nearest architectural analogue in the corpus for a recessive null CNS disease
**clinical relevance:** HIGH strategic
**Claim links:** none
**Role:** 🔵 **Transferable programme template, not WWOX evidence. The paper does not mention WWOX.** Intracisterna magna beat intravenous; partial restoration of the complex sufficed; the human dose was derived by scaling to CSF volume on FDA advice (primate high dose equating to 4 x 10^14 genome copies in a four-year-old). 🔴 **The named gap:** transgene immunogenicity was tested only in WILD-TYPE mice dosed at P1-3, with an interferon-gamma ELISpot and no antibody assay anywhere - so the protein-naive host a recessive-null patient models was never tested; the primates were wild type too. ⚠️ The window is endpoint-specific: adult treatment left brain structure unrescued while still rescuing motor function. ⚠️ The abstract's "no significant adverse events" covers dose- and time-dependent nerve and spinal-cord degeneration, a treatment-associated leucocytosis at 28 days and one unexplained death at 80 days in a treated animal. ⚠️ The adult mid dose is stated as 3 x 10^12 vg/kg in Results and 4 x 10^12 vg/kg in the Discussion, and the declared n = 12 per dose is not the analysed n for any endpoint.
**LIT link:** [[literature_tracking_log_current#LIT-0446]]
**Note:** class-level record; no individual-level detail. Not medical advice.

## PAPER 154
**Short title:** Bailey 2026 J Clin Invest - the metabolic and the seizure endpoint do not share a dose, and age costs an order of magnitude of delivery at matched dose and route
**Full title:** AAV-mediated gene therapy in a model of SLC13A5 citrate transporter disorder rescues epileptic and metabolic phenotypes
**Authors:** Bailey LE, Adams RM, Schackmuth MK, et al.; Bailey RM
**Year:** 2026
**Source type:** primary preclinical study - vector design, neonatal dose comparison, adult route comparison, electrophysiology, sleep staging, chemoconvulsant challenge, biodistribution
**Journal/source:** *J Clin Invest* 2026;136(8)
**Identifier:** PMID 41712282 / PMCID PMC13078891 / DOI 10.1172/JCI197503
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41712282-01`; manifest `deepdive_manifests/PMID41712282.json`; dossier `research/fulltext_dossiers/PMID41712282.md`
**Primary pathway:** none for WWOX - two-sided dose, self-complementary cargo, route versus age
**Model/species:** *Slc13a5* knockout mouse
**Genotype/model:** biallelic loss of function (DEE25); NOT a WWOX genotype
**Transferability:** T2 for the two-axis dose design and the age-versus-route arithmetic; T4 for any dose
**clinical relevance:** HIGH strategic
**Claim links:** none
**Role:** 🔵 **Transferable dosing lesson, not WWOX evidence. The paper does not mention WWOX.** 🔴 **The two endpoints have different dose-response curves:** plasma citrate fell dose-dependently to 65 +/- 8.0% of wild type at the high dose - an overshoot past normal from a baseline about 20% above wild type - while the chemoconvulsant endpoint saturated, the low dose matching the high. The authors themselves name a published developmental harm from overexpressing the same gene. ⚠️ Age cost an order of magnitude of delivery at matched dose and route (cerebellar vector 15.7 x 10^3 at P10 against 1.2 x 10^3 at 3 months, vg per genome), partly recovered by switching the adult route - which is why its apparent window result resolves to delivery. ⚠️ A short synthetic promoter is what permits self-complementary packaging of a 1.7 kb coding sequence. ⚠️ No immune endpoint of any kind is reported, although a human transgene in a knockout host is the closest thing here to a protein-naive recipient. ⚠️ The antibody does not recognise the endogenous mouse protein, so expression has no wild-type reference. ⚠️ The vehicle control arms of the P10 sleep and power-spectrum analysis were already published by the same group.
**LIT link:** [[literature_tracking_log_current#LIT-0447]]
**Note:** class-level record; no individual-level detail. Not medical advice.

## PAPER 155
**Short title:** Duba-Kiss 2025 Mol Ther Methods Clin Dev - early expression buys cellular but not humoral tolerance, does not transfer to a redose, and is antigen-specific
**Full title:** Early postnatal expression mitigates immune responses to Cas9 in the murine central nervous system
**Authors:** Duba-Kiss R, Hampson DR
**Year:** 2025
**Source type:** primary preclinical immunology study - neonatal versus adult CNS delivery, glial and adaptive-immune readouts, EGFP comparator, prime-and-redose arm
**Journal/source:** *Mol Ther Methods Clin Dev* 2025;33(3):101536
**Identifier:** PMID 40809677 / PMCID PMC12347139 / DOI 10.1016/j.omtm.2025.101536
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-40809677-01`; manifest `deepdive_manifests/PMID40809677.json`; dossier `research/fulltext_dossiers/PMID40809677.md`
**Primary pathway:** none for WWOX - window x immunity interaction, promoter choice and tolerance
**Model/species:** wild-type C57BL/6J mouse
**Genotype/model:** none - the antigen is a bacterial nuclease; NOT a WWOX genotype
**Transferability:** T3 - mechanism transfers, magnitude does not
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Transferable mechanism, not WWOX evidence. The paper does not mention WWOX.** Early postnatal expression preserved the transgene and raised no MHC II or T-cell response, while adult delivery destroyed the transgene and cost about a third of cortical neurons. 🔴 **Three limits that bound the "early delivery buys tolerance" idea:** antibodies were raised at BOTH ages, so the tolerance is cellular and not humoral; a neonatal prime did not abolish the harm of an adult redose (still -25.3% neuronal density); and the effect is antigen-specific - EGFP in the same compartment at the same age was inert, so "foreign protein" is not one category. ⚠️ A neuron-restricted promoter may itself impede MHC II-dependent regulatory T-cell tolerance, which sets promoter choice against the overexpression-safety argument. ⚠️ The adult arm received four times the vector of the neonatal arm, so age and antigen load are not separated, and the adult quantification used a parenchymal route where the neonatal used intraventricular.
**LIT link:** [[literature_tracking_log_current#LIT-0448]]
**Note:** class-level record; no individual-level detail. Not medical advice.

## PAPER 156
**Short title:** Balestrini 2026 CNS Drugs - landscape review; half its most advanced modalities are structurally unavailable to a biallelic null
**Full title:** Ameliorating Seizures in Dravet Syndrome: A Review of Newly Approved and Investigational Drugs, RNA and Gene-Based Therapies
**Authors:** Balestrini S, Scheffer IE
**Year:** 2026
**Source type:** narrative review - NOT a systematic review and NOT a primary study
**Journal/source:** *CNS Drugs* 2026;40(4):535-548
**Identifier:** PMID 41712149 / PMCID PMC12989007 / DOI 10.1007/s40263-026-01276-x
**Status:** processed
**Record provenance:** created by `CC-20261003W5-A-REGISTRY-01` (intake wave 5 2026-10-03, Scientist A). Provisional number. The integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41712149-01`; manifest `deepdive_manifests/PMID41712149.json`; dossier `research/fulltext_dossiers/PMID41712149.md`. The gene- and RNA-based sections were read in full; the small-molecule sections in outline only, as stated in the dossier.
**Primary pathway:** none for WWOX - modality landscape, cargo limit, window counter-datum
**Model/species:** not applicable - review
**Genotype/model:** *SCN1A* haploinsufficiency (dominant, de novo in over 95%); NOT a WWOX genotype
**Transferability:** T4 as evidence - every datum must be traced to a primary before it counts; T2 as a map of which modalities reached patients
**clinical relevance:** MODERATE strategic
**Claim links:** none
**Role:** 🔵 **Positioning map, not evidence. The review does not mention WWOX.** 🔴 **The sharpest transfer limit in the wave:** because this disease leaves one intact allele, almost every modality the review treats as most advanced - antisense upregulation, dCas9 transcriptional activation, an engineered transcription factor, conditional reactivation, paralogue rebalancing - requires an endogenous locus to act on and is therefore STRUCTURALLY UNAVAILABLE to a biallelic null. The one route that does transfer, split-intein dual-vector replacement for an over-6 kb open reading frame, is the one with no human data. ⚠️ It carries the corpus's only expression-matched age comparison - conditional reactivation at P90 in adulthood still rescued seizures after months of seizures - which points the window later rather than earlier, but is review-level and its primary was not retrieved. ⚠️ It quantifies the paediatric CSF cost of repeated intrathecal dosing: transient protein elevations above 50 mg/dL in about three-quarters of children in the extension studies. ⚠️ Its stated search window closes 31 March 2025, before the clinical results it reports; both flagship programmes are sponsored by companies with which the authors declare relationships.
**LIT link:** [[literature_tracking_log_current#LIT-0449]]
**Note:** class-level record; no individual-level detail. Not medical advice.
```

## Ops — `disease-models/wwox/registries/literature_tracking_log_current.md`, `append` (six new records)

```
## LIT-0444
**Short title:** Greenberg 2026 first-in-human high-dose intrathecal AAV9, CLN7
**Authors:** Greenberg BM, et al.; Gray SJ, Kayani SN
**Year:** 2026
**Source type:** primary clinical study - phase 1, n = 4
**Identifier:** PMID 41314141 / DOI 10.1016/j.ebiom.2025.106044
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41314141-01`
**Relevance:** transferable protocol only - CRIM-based immunosuppression and empty-capsid arithmetic; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 151]]
**Note:** not medical advice.

## LIT-0445
**Short title:** Quinlan 2025 oversized full-length SYNGAP1 AAV cassette
**Authors:** Quinlan MA, Guo R, et al.; Levi BP
**Year:** 2025
**Source type:** primary preclinical study
**Identifier:** PMID 40988338 / DOI 10.1016/j.ymthe.2025.09.040
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-40988338-01`
**Relevance:** transferable cargo-size arithmetic in a heterozygous, dose-sensitive model; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 152]]
**Note:** not medical advice.

## LIT-0446
**Short title:** Wiseman 2024 AP4B1 gene replacement IND package
**Authors:** Wiseman JP, Scarrott JM, et al.; Azzouz M
**Year:** 2024
**Source type:** primary preclinical study with GLP primate toxicology
**Identifier:** PMID 39358605 / DOI 10.1038/s44321-024-00148-5
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-39358605-01`
**Relevance:** nearest architectural analogue for a recessive loss-of-function CNS disease; immunogenicity tested only in wild-type animals; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 153]]
**Note:** not medical advice.

## LIT-0447
**Short title:** Bailey 2026 SLC13A5 gene replacement, metabolic and seizure endpoints
**Authors:** Bailey LE, Adams RM, et al.; Bailey RM
**Year:** 2026
**Source type:** primary preclinical study
**Identifier:** PMID 41712282 / DOI 10.1172/JCI197503
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41712282-01`
**Relevance:** the two phenotypes do not share a dose; age costs an order of magnitude of delivery at matched dose and route; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 154]]
**Note:** not medical advice.

## LIT-0448
**Short title:** Duba-Kiss 2025 early postnatal expression and CNS immunity to a foreign protein
**Authors:** Duba-Kiss R, Hampson DR
**Year:** 2025
**Source type:** primary preclinical immunology study
**Identifier:** PMID 40809677 / DOI 10.1016/j.omtm.2025.101536
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-40809677-01`
**Relevance:** the window x immunity interaction, with three limits - humoral response at both ages, no transfer to a redose, antigen specificity; the paper does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 155]]
**Note:** not medical advice.

## LIT-0449
**Short title:** Balestrini 2026 Dravet therapy landscape review
**Authors:** Balestrini S, Scheffer IE
**Year:** 2026
**Source type:** narrative review - not peer-reviewed primary evidence for any datum it reports
**Identifier:** PMID 41712149 / DOI 10.1007/s40263-026-01276-x
**Disposition:** analysed - intake wave 5 2026-10-03 (Scientist A), `partial_fulltext_read`, receipt `FTR-20261003-41712149-01`
**Relevance:** positioning map; most of its advanced modalities require an intact allele and so cannot transfer to a biallelic null; the review does not mention WWOX
**Paper link:** [[paper_registry_current#PAPER 156]]
**Note:** not medical advice.
```

## Integrator checklist

1. Re-run `registry_records.py catalog` and renumber `PAPER 151`-`156` and `LIT-0444`-`0449` from the
   measured maxima, in event order against Scientists B and C of this wave.
2. Keep each PMID and its record id in the same section (the orphan check pairs them positionally).
3. Record the six receipts from `scratchpad/receipts_pending_w5/sciA_<pmid>_1.json` in event-id order
   **before** running the generated surfaces, then regenerate `reading_state`, `coverage_report`,
   `batch_queue` and the pathograph from committed inputs.
4. No `CORPUS-STUB` is consumed by this candidate: none of the six PMIDs had a stub.

### LOCATOR TRIPLES FOR BLIND AUDIT

This candidate creates bibliographic records only; every scientific statement inside the `Role`
fields is sourced by a triple in one of the four companion candidates
(`CC-20261003W5-A-CARGO-CASSETTE-01`, `CC-20261003W5-A-TRANSGENE-IMMUNITY-01`,
`CC-20261003W5-A-WINDOW-STATUS-01`, `CC-20261003W5-A-DOSE-TWO-SIDED-01`), and the two arithmetic
findings not covered there are reproducible from the artefacts on disk by the commands printed in
`research/fulltext_dossiers/PMID41314141.md` and `research/fulltext_dossiers/PMID39358605.md`. No
triple is duplicated here.
