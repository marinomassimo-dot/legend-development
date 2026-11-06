# Independent verification of the 14 orchestrator narrowing edits (package b1_whitematter)

Non-canonical verifier note. Not medical advice. Nothing in the repository was edited. Sources read through Europe PMC REST only (no contact address sent).
Depth: FULLTEXT = Europe PMC fullTextXML read for the passages cited; ABSTRACT = Europe PMC abstract only.
Sources: PMID36601084 / PMC9806385 FULLTEXT; PMID42033488 / PMC13357445 FULLTEXT (whole case report); PMID42470358 / PMC13675778 FULLTEXT (OV329 section 5.1-5.4); PMID27796063 / PMC5214060 FULLTEXT (abstract and discussion passage); PMIDs 37690269, 35183975, 18783433, 20384718, 19258289, 31349008 ABSTRACT.
Supplements (Table S1-S3 of 36601084) not retrieved; the main text states their content, which is what was relied on.

## Per-edit findings (CONSUMER-BOUND edits first)

### Edit 2 and 3 (B1-03 finding; cofactors) -- CONSUMER-BOUND (DR-H02-013, U20 hormonal caveat)
Source Table 3 / Results: univariate significant = TSC (OR 0.23), rapamycin (OR 0.116), topiramate (p=0.003), hormonal therapy (p=0.002); days of exposure p=0.198, peak p=0.243, cumulative p=0.217 on univariate. LASSO-selected multivariate model contained TSC, TPM, hormonal, age at first exposure, infant-period exposure, cumulative dose, peak dose, rapamycin; rapamycin the only significant term (p=0.019); hormonal p=0.080, TPM p=0.171. Days of exposure is not in the LASSO list. Both edits are SUPPORTED. Residual inconsistency: the unedited field exposure_pattern_qualitative of B1-03 still reads "peak amount, cumulative amount and days of exposure all entered the models", which now contradicts the edited finding (days did not enter the multivariate model).

### Edit 4 (B1-06 cofactors) -- CONSUMER-BOUND (U20, DR-H02-005 context)
First clause (within the 38 with the abnormality, no factor associated with the symptomatic form, Table S2): SUPPORTED verbatim ("no risk/protective factor associated with symptomatic VABAM ... n = 38, Table S2").
Second clause ("the hormonal and topiramate univariate associations belong to the whole 172-child cohort (row B1-03)"): OVERSHOOT / MISATTRIBUTION. B1-03 records topiramate and hormonal therapy as univariate risk factors for the presence of the abnormality. The source's separate statement is about the symptomatic form in the whole cohort: hormonal therapy p=0.012 (OR 4.457) and topiramate p=0.037 (OR 8.967), Table S3, "but not confirmed by further final multivariate logistic regression analysis". Pointing to B1-03 merges two different outcomes (abnormality present versus symptomatic). The original pre-edit wording was also imprecise (scope), but the new pointer is wrong. Note also that the multivariate non-confirmation is the decisive qualifier and is absent.

### Edit 12 (B1-44 cofactors) -- CONSUMER-BOUND (NEED-MYELINATION do_not_assume, card H02 mechanism, DR-H02-035)
Abstract: "suggesting that control of myelination by endogenous GABA may require a permissive factor to be released from axons". "May require" is exact. SUPPORTED. (Receptor-subtype specificity and no-drug/no-disease qualifiers in the row are intact.)

### Edit 14 (B1-46 locator_quote) -- CONSUMER-BOUND (NEED-MYELINATION do_not_assume, DR-H02-036)
Abstract text: "chronic treatment with GABA and baclofen, specific GABA<sub>B</sub>R agonist, accelerates OPC differentiation". GABA-B-R is the correct subtype; the old record dropped the letter. SUPPORTED. Caveat: the quote is no longer character-verbatim (it is a rendering of subscript markup); the bracketed explanation covers it.

### Edit 5 (B1-17 finding) -- CONSUMER-BOUND (DR-H02-018 INCREASE, card mechanism)
Abstract: GABA/Cr 0.48 +/- 0.10 in VABAM vs 0.31 +/- 0.15 in non-VABAM "tended to be higher ... (P = 0.31)"; CSF GABA p=0.03; GABA/Cr higher under vigabatrin than controls p=0.02. The added clause is SUPPORTED. Consequence not carried through: module_inputs DR-H02-018 reads "cerebrospinal and spectroscopic GABA concentration in children with and without the abnormality ... INCREASE", but the spectroscopic comparison was not significant (n=2 versus 11), so the row should carry that in its note.

### Edit 6 and 7 (B1-19 age_at_first_exposure; cofactors) -- CONSUMER-BOUND (card H02 not_known, module_inputs section 5 item 1, README item 5)
Case report: "clinical history ... began at 22 days of life ... Treatment with vigabatrin ... titrated up to 125 mg/kg/day and carbamazepine ... was initiated" with no date; admission at 9 months. Age at first exposure "not stated" SUPPORTED. Co-medication edit SUPPORTED (carbamazepine, 30 mg/kg/day), though it is redundant because exposure_pattern already says "with carbamazepine" and the phrase "not listed here" is then untrue.
Unedited fields of the same row that carry the same class of error (important, consumer-bound):
 (a) duration_class "about nine months to the finding": 9 months is the patient's age at admission, not time on drug (start undated). OVERSHOOT.
 (b) transfer_conditions "a non-WWOX genetic encephalopathy whose baseline MRI carries delayed myelination and callosal hypoplasia", and the consumer sentences built on it (module_inputs section 2 not_known: "one case report describes the pattern arising on such a baseline"; section 5 item 1: "one whose baseline MRI carries delayed myelination"; README item 5: "arising on a baseline of delayed myelination"): OVERSHOOT. The source says "Initial brain MRI was normal"; delayed myelination and mild callosal hypoplasia appear in the same MRI as the toxic-pattern abnormality, as "additional findings" (the row's own baseline_condition field says this correctly). It is therefore not shown that the pattern arose on a pre-existing delayed-myelination baseline; it co-occurred with it at 9 months. This weakens the one case offered against B1-09 and enters card H02 not_known.

### Edit 8 (B1-40 age_at_first_exposure) -- not directly consumer-bound (DR-H02-031 uses the age/duration/peak association, and README age-window text cites it; the edit moves wording away from an overshoot)
Abstract: "Patients were assessed for age at time of MRI ... median age of 11 months versus 5 years". SUPPORTED. Note the downstream reading "younger initiation" in README (age and window paragraph, "younger age at examination" is used there correctly).

### Edit 9 (B1-41 reversibility) -- CONSUMER-BOUND at README/DR-H02-032 level (reversal-conditional-on-stopping statement)
Abstract: "Analysis of patients undergoing scans before, during, and after VGB treatment (n = 14) revealed that four patients had abnormal MRI signal during treatment ... two reversed with cessation, one reversed without cessation, and another had persistent abnormal signal while being weaned". SUPPORTED. Note the 14 and the 15-of-25 follow-up subset are different subsets; the row's transfer_breakers sentence ("reversal was assessed in 15 of 25, and one child reversed without stopping") conflates them slightly (the without-cessation child belongs to the 14).

### Edit 1 of B1-14 (finding) -- CONSUMER-BOUND (README reversibility paragraph, work-order window series wording)
Abstract: complete T2/FLAIR resolution in all patients for midbrain, dentate nuclei, subthalamic nuclei, hypothalami; complete DWI resolution for globus pallidi, midbrain, dentate, hippocampi, anterior commissure, hypothalami. Thalami appear in neither list; globus pallidi appear only in the DWI list. The new wording is SUPPORTED and appropriately flags non-resolution as an inference. Mild omission: it does not say the globus pallidi are in the complete-DWI-resolution list, so a reader could take pallidal non-resolution as broader than the source shows (UNDERSHOOT, minor).

### Edit 10 (B1-42 age_at_first_exposure) -- indirect (DR-H02-033, age-and-window paragraph)
Abstract: "22 epileptic infants (age: 9 +/- 1 months)". The abstract does not say this age is at imaging; "age of the reviewed infants at imaging" is OVERSHOOT (minor) and "implies earlier starts" is an inference from an assumed time point.

### Edits 11 and 13 (B1-43) -- indirect (DR-H02-034 / DR-H02-009 note)
EILAT XVIII 5.3: "male C57BL/6J mice received a two-day subcutaneous infusion ... osmotic pump"; no age given; OV329 below LLOQ 3 ng/mL in brain, eyeball, retina; vigabatrin retina-to-plasma 4.30. Both edits SUPPORTED. No conclusion changes.

## Summary table

| edit | row / field | verdict | consumer-bound | depth read | one-line reason |
|---|---|---|---|---|---|
| 1 | B1-03 finding | SUPPORTED | CONSUMER-BOUND (DR-H02-013, U20) | FULLTEXT | Table 3 and LASSO list match every clause; days of exposure not in the multivariate model |
| 2 | B1-03 cofactors | SUPPORTED | CONSUMER-BOUND (U20) | FULLTEXT | TPM p=0.003 and hormonal p=0.002 univariate only; multivariate p=0.171 / 0.080 |
| 3 | B1-06 cofactors | OVERSHOOT (second clause) | CONSUMER-BOUND (U20) | FULLTEXT | first clause exact; the whole-cohort hormonal/TPM associations are with the symptomatic form (Table S3, not confirmed multivariately), not the B1-03 association |
| 4 | B1-14 finding | SUPPORTED (minor UNDERSHOOT) | CONSUMER-BOUND (reversibility text) | ABSTRACT | lists match; pallidal DWI resolution not mentioned |
| 5 | B1-17 finding | SUPPORTED | CONSUMER-BOUND (DR-H02-018) | ABSTRACT | 0.48 vs 0.31 p=0.31 stated; DR-H02-018 note must reflect it |
| 6 | B1-19 age_at_first_exposure | SUPPORTED | CONSUMER-BOUND (H02 not_known) | FULLTEXT | start of drug undated; but duration_class and transfer_conditions of same row still overshoot (see corrections) |
| 7 | B1-19 cofactors | SUPPORTED (redundant) | CONSUMER-BOUND | FULLTEXT | carbamazepine named in the source and already in exposure_pattern |
| 8 | B1-40 age_at_first_exposure | SUPPORTED | indirect | ABSTRACT | median age is at the time of MRI |
| 9 | B1-41 reversibility | SUPPORTED | CONSUMER-BOUND (reversal conditional on stopping) | ABSTRACT | n=14, four abnormal, 2/1/1 outcomes exact |
| 10 | B1-42 age_at_first_exposure | OVERSHOOT (minor) | indirect | ABSTRACT | abstract gives 9 +/- 1 months without a time point |
| 11 | B1-43 species_or_population | SUPPORTED | indirect | FULLTEXT | male mice, no age given |
| 12 | B1-43 age_at_first_exposure | SUPPORTED | indirect | FULLTEXT | C57BL/6J male, no age |
| 13 | B1-44 cofactors | SUPPORTED | CONSUMER-BOUND (NEED-MYELINATION, H02) | FULLTEXT (abstract passage) | "may require" is the source modality |
| 14 | B1-46 locator_quote | SUPPORTED | CONSUMER-BOUND (NEED-MYELINATION, H02) | ABSTRACT | subtype is GABA-B-R; quote is a rendering, not character-verbatim |

(The ORCHESTRATOR_EDITS.md table has 14 rows; the numbering above follows its row order.)

## Proposed wording corrections (exact replacement text)

1. B1-06 cofactors, replace with:
   "within the 38 children with the abnormality no factor was associated with the symptomatic form (the source's Table S2); in the whole 172-child cohort hormonal therapy (p = 0.012) and topiramate (p = 0.037) were univariate risk factors for the symptomatic form, not confirmed on the final multivariate model (the source's Table S3); these are separate from the associations with the presence of the abnormality in row B1-03"

2. B1-03 exposure_pattern_qualitative, replace "peak amount, cumulative amount and days of exposure all entered the models" with:
   "peak amount, cumulative amount and days of exposure were each tested on univariate regression; peak and cumulative amount entered the multivariate model, days of exposure did not"

3. B1-19 duration_class, replace "about nine months to the finding" with:
   "not stated (the patient was nine months old at the finding; the start of exposure is not dated)"

4. B1-19 transfer_conditions, replace with:
   "the finding occurs in a non-WWOX genetic encephalopathy in which delayed myelination and mild callosal hypoplasia were reported in the same examination as the finding; the initial MRI was normal, so the pattern is not shown to have arisen on a pre-existing delayed-myelination baseline"
   and correct the three consumer sentences accordingly: module_inputs section 2 not_known ("while one case report describes the pattern arising on such a baseline" -> "while one case report describes delayed myelination reported in the same examination as the pattern, on a normal initial MRI"); section 5 item 1 ("one whose baseline MRI carries delayed myelination and callosal hypoplasia" -> "one in which delayed myelination and callosal hypoplasia were reported in the same examination"); README item 5 ("arising on a baseline of delayed myelination and callosal hypoplasia" -> "with delayed myelination and callosal hypoplasia reported in the same examination, after a normal initial MRI").

5. B1-19 cofactors, replace the tail with: "carbamazepine is the named co-medication (already in the exposure pattern)".

6. B1-42 age_at_first_exposure, replace with:
   "not stated (the abstract gives the infants' age as 9 +/- 1 months without naming the time point; the peak at 3 to 6 months after the start of exposure does not fix the start age)"

7. B1-14 finding, replace the parenthetical tail with:
   "complete T2/FLAIR resolution is listed for midbrain, dentate nuclei, subthalamic nuclei and hypothalami, and complete restricted-diffusion resolution for globus pallidi, midbrain, dentate nuclei, hippocampi, anterior commissure and hypothalami; the thalami are in neither list and the globus pallidi are not in the T2/FLAIR list (non-resolution there is inferred from absence from the lists, not stated)"

8. DR-H02-018 note (module_inputs): add "the spectroscopic ratio did not differ significantly between children with and without the abnormality (p = 0.31, two against eleven children); only the cerebrospinal free GABA difference (p = 0.03) and the higher ratio under the drug than in controls (p = 0.02) were significant".

9. B1-41 transfer_breakers, replace "reversal was assessed in 15 of 25, and one child reversed without stopping" with: "follow-up scans were done in 15 of 25 (reversible on withdrawal); in the separate before-during-after subset of 14, four had the abnormality and one of them reversed without stopping".
