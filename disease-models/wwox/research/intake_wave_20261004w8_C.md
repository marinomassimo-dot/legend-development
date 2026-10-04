context_policy: SOURCE_FIRST

# Intake wave 8 (2026-10-04), Scientist C: primaries behind the AAV toxicity commentaries

**Not medical advice.** Public edition: no individual-level record. None of the six sources names WWOX (zero occurrences in each persisted artefact); they are read for one transferable question, with limits stated.

## Question

What does each source add to, or limit in, the claim that DRG and hepatic pathology of a high-dose AAV9 administration is immune-mediated and therefore modifiable rather than dose-intrinsic, and in which species is each component measured?

## Sources and receipts

| PMID | What it is | Species, route | Receipt | Depth |
|---|---|---|---|---|
| 42137263 | Liver RNA-seq reanalysis, AAV9-PHP.B-SMN1 | cynomolgus and rat, intravenous | `FTR-20261004-42137263-01` | partial |
| 30073179 | Toxicology, AAV9-IDUA, with a 3-animal immunosuppression arm | rhesus, ICM | `FTR-20261004-30073179-01` | partial |
| 30073178 | Toxicology, AAV9-IDS, 5-animal immunosuppression arm | rhesus, ICM | `FTR-20261004-30073178-01` | partial |
| 35229008 | Controlled DRG study with an expression-null arm, function and MRI | cynomolgus, ICM | `FTR-20261004-35229008-01` | partial |
| 41438872 | AAV-PHP.eB versus AAV9 transduction | pigtail macaque, ICV | `FTR-20261004-41438872-01` | partial |
| 42198847 | Fatal high-dose case, class level only | human, intravenous | `FTR-20261004-42198847-01` | partial |

All six are PARTIAL because supplements were not analysed and some figure panels were read by caption only (stated per dossier).

## First-pass answer (before any registry or candidate was opened)

1. **Expression, not DNA presence, is the best-supported driver of the primate ganglion lesion.** An AAV9 genome with no functional promoter reached DRG at equal or greater DNA levels with no neuronal degeneration (PMID 35229008). Single Null construct, n = 4, four weeks.
2. **Immunosuppression did not reliably lower the ganglion score** in the two small arms (n = 3, n = 5), and at the low dose in the second the immunosuppressed score was higher (panels inspected). Both papers had a single day-90 necropsy.
3. **Liver, systemic, day 4:** pathway signatures order by dose: p53/DNA damage and interferon at every dose; pro-apoptotic UPR and loss of hepatocyte identity only at and above 5e13 vg/kg, correlating with transgene level (PMID 42137263). Correlational, n = 2 per sex per dose.
4. **Human boundary:** one fatal case at 2.2e14 vg/kg intravenous under prednisolone plus sirolimus, innate and complement driven by the authors' reading, no counterfactual (PMID 42198847).
5. **Capsid:** PHP.eB is about five-fold more efficient than AAV9 for cortical neuron labelling after ICV, with no toxicity measurement (PMID 41438872); liver load after ICV is about 100 to 250 vg per diploid genome in both capsid groups.

## Statements carried from the wave-7 commentaries: which now have a primary

| Carried statement | Primary now read | Does the wording hold |
|---|---|---|
| Rebound after antimetabolite withdrawal at day 60 led to a delayed DRG phenotype | PMIDs 30073179 and 30073178 | **Not as a DRG observation.** Single day-90 necropsy, no DRG time course; the primaries tie MMF withdrawal only to later T-cell responses and one late CSF-cell peak, with "perhaps" and "likely" |
| Immunosuppression reduced DRG severity in some animals | same two | **Weak.** Panels overlap; low-dose immunosuppressed animals scored higher in the second paper |
| UPR is "strongly" tied to transgene synthesis (liver commentary) | PMID 42137263 | **Direction holds, strength overstated**: correlational, collinear with dose, lobe pseudoreplication |
| Dose-related DRG toxicity is lower with lower transcriptional activity | PMID 35229008 (not 42137263) | **Holds** for an expression-null genome; not for graded expression |
| "Immune suppression ablated T cell responses, but not DRG pathology" (wording in PMID 35229008 citing the two 2018 papers) | the two 2018 papers | **Overstated**: T-cell response present in one of three immunosuppressed animals; antibodies abolished |

## Registry statements and sources: findings

- Premise corrections to the selection note: PMID 30073179 does contain an immune-modulation arm; PMID 35229008 is single-species single-route and tests (Null arm), it does not only describe; PMID 42137263 is an intravenous PHP.B liver dataset, not a CSF-route one; PMID 41438872 never mentions DRG.
- Dates and day counts only; no identifiers or birth years carried from the case report.
- Day-14 animals in the IDUA study have no DRG data (DRG sampled only in the second study), so "lesions absent at day 14" holds for spinal axonopathy only.

## Increments over waves 3-7 (read after the first pass; identical findings merged)

Waves 3-7 already hold: empty-capsid and promoterless negatives (liver and DRG, another primate study), immunosuppression not bounding the ganglion infiltrate, DRG attribution by route, dose scalars, and a DRG imaging endpoint in a mouse. This wave adds only: (a) a second expression-null control with measured DRG DNA parity and a capsid-fullness gradient (`CC-20261004W8-C-EXPRESSION-NULL-01`); (b) the two primaries behind the rebound relay and the wording check (`CC-20261004W8-C-IMMUNOSUPPRESSION-PRIMARIES-01`); (c) the liver ordering by dose, the human case under sirolimus and the ICM liver load (`CC-20261004W8-C-SYSTEMIC-BOUNDARY-01`); registry landing in `CC-20261004w8-C-REGISTRY-01`.

## Transfer limit (exact)

Every datum is from a non-WWOX transgene, mostly secreted lysosomal enzymes (cross-correction possible), in macaque with mixed or single sex, CB7-type promoters, and four-week to 90-day windows. Nothing here bounds a WWOX dose, route, capsid or age, and nothing says whether WWOX expression would stress the endoplasmic reticulum. A constitutive null or any other genotype is not modelled.

## What would change the model

- A primate arm with graded expression (dose-matched weak promoter or miRNA detargeting) and ganglion histology: would turn "expression-dependent" from presence/absence into a function.
- An adequately sized immunosuppressed arm with several necropsy times: would settle the rebound question either way.
- Falsifier of expression dependence: ganglion lesion with a Null genome at larger n.

## Not read

Supplementary tables and figures (all six); Figure 3 of PMID 42137263; Figures 1, 2, 4 of PMID 30073178; Figures 1, 3, 5-7 of PMID 35229008 (MRI panels); Figures 1-3 of PMID 41438872; Figures 1-2 of PMID 42198847; reference lists (enumerated only). A halt by a safety classifier did not occur in this run.
