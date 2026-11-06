Contributions only; the Orchestrator owns the consolidated consumer edits (integration/ folder).

# A1 module inputs (proposals only; nothing here edits a module file or a registry)

Scientist `sb-a1`, task `ORCH-SCIBATCH-DR-20261105`. Revised 2026-11-06 in the correction round (`RESPONSE.md`). Each proposal names the rows of `cases_a1.tsv` (`A1-nn`) or `denominators_a1.tsv` it rests on, and uses the field names and value sets of its target file. Not medical advice: no dose, schedule or preference is carried anywhere. Per-child detail stays at genotype class.

## 1. `ranking_it8_p9_20261029/ranking.json`, investigation `INV-10`

| Field | Proposed value | Rests on |
|---|---|---|
| `evidence_available` | "Clinical reports only. Children counted once across 14 reports: 36 to 38 exposed to at least one of vigabatrin, hormonal therapy, ketogenic diet or cannabidiol. Both a symptomatic and a developmental outcome are recorded for 6. In 4 of them, a partial or transient improvement came with development unchanged; in 2, neither moved. No sustained, instrumented response is recorded, and no developmental gain follows any of the four classes. Vigabatrin: 5 children with both endpoints in 4 reports (4 discordant, 1 concordant non-response). These are not independent of the other classes: three of the five also supply them, and all five were on co-therapy. Hormonal 3 of 11; ketogenic diet 2 of 12; cannabidiol 1 of 7. Counts only, no percentage (n below 10). Developmental statements are clinical narratives without a scale." | A1-01, A1-02, A1-03, A1-17, A1-18 to A1-21, A1-24, A1-25, A1-26; denominators `POOLED` rows |
| `evidence_depth` | "E4 - card reviewed, WWOX-side assertions read beyond abstract at partial full-text depth in 11 reports (the six children with both endpoints come from five of them); one source at abstract level" | receipts `FTR-2026110[56]-*-21` |
| `decisive_uncertainty` | add: "and whether a sustained response, which no published child achieved, is followed by gain; and whether the separation holds for residual-function alleles" | A1-32 |
| `next_test` | Record the existing next test as **EXECUTED 2026-11-05** with its result: "6 children with both endpoints; a discordance rate is not computable at n below 10; counts given instead". Then add the new next test: "Denominator request, without contact. For each WWOX-DEE series that reports an intervention: the number exposed, the response definition, and a dated developmental instrument before and after. The five-patient series and Choi 2026 come first, and the seven-child series (PMID 42721537) is read when an open route exists." Branches: vigabatrin fired the 5-or-more branch (counts with sources); hormonal therapy, diet and cannabidiol fired the fewer-than-5 branch ("not computable from the public record: k of N"). | denominators `POOLED` rows; BRIEF_A1 consequences rows 1 and 2 |
| `why_now` | replace "The module already holds a series in which symptomatic response and developmental outcome did not move together" with: "Four children in three reports show a partial or transient improvement without developmental gain. The five-patient series is not among them, because its developmental row is a single status label." | A1-04, A1-05, A1-07; A1-01 to A1-03, A1-17, A1-24 |

## 2. `needs/needs.json`, need `NEED-SEIZURE-CONTROL-SYMPTOMATIC`

* **`observed` O1, field `limits`.**
    * Current text: "At least one, probably two, of the three responders are previously published individuals (patient 4 explicitly; patient 2 by a Table 1 row), so pooled counts can double-count them."
    * Proposed text: "One of the three responders (patient 4) is stated to be published before. Patient 2's Table 1 credit to an earlier cohort is variant-level: no column of that report's Supplementary Table 1 carries patient 2's homozygous exon-level deletion. The series' other previously published child is most likely patient 3, a non-responder (INFERENZA). So pooled counts can double-count patient 4 among responders and patient 3 among exposed children."
    * Rests on A1-05, A1-06, A1-07 and receipt `FTR-20261105-30356099-21`.
* **`observed` O1, field `statement`.** Replace "developmental status was recorded as identical across all five" with "developmental status is a single Table 1 label (profound developmental delay) in all five; no pre-diet status or course is on the delivered surface". Rests on A1-04, A1-05, A1-07.
* **`observed` O2, field `statement`.** Append: "Further: complete control for one month, then relapse (Tarta-Arsene 2017); seizures controlled in three of four treated children of one series, one with myoclonic seizures still on EEG (Al Baradie 2022); used in 7 of 10 children with spasms of one cohort, with no response reported (Oliver 2023). The 'resistant' case of the five-patient series is regimen-level poor control on three drugs." Rests on A1-24, A1-29, A1-30, A1-34, A1-36 to A1-43, A1-08.
* **`observed`, new O4** (all 16 fields of the existing observations):

```json
{"id": "O4",
 "statement": "Across published WWOX-DEE reports, children with both a symptomatic and a developmental outcome recorded: 6. In 4, a partial or transient seizure improvement came with development unchanged; in 2, neither moved. No sustained, instrumented response is recorded.",
 "model_type": "human_clinical_report",
 "species": "human",
 "genotype": "biallelic WWOX; null or splice class in 5, homozygous missense class in 1",
 "tissue_or_cells": "whole organism",
 "age_stage": "infancy to early childhood",
 "comparison": "responders against non-responders, between reports; no comparator arm",
 "readout": "clinician-reported seizure course and clinician-narrated development",
 "readout_level": "clinical",
 "direction_observed": "symptom and development apart in 4 of 6 (partial or transient improvement, development unchanged); together in 2 of 6 (both unchanged)",
 "evidence_scope": "WWOX_EXPERIMENT_IN_DEE_SYSTEM",
 "limits": "Six children from five reports, two of them from one report; developmental statements are clinical narratives without a scale; follow-up about 5 months to 2.5 years where dated, undated in 2; co-therapy in every case; counts only. The source receipts are staged, not recorded.",
 "pmid": "30361190, 39101447, 28721938, 35573960, 29808465",
 "locators": [{"kind": "document", "path": "disease-models/wwox/research/drug_repurposing/batch_sci_20261105/a1_wwox_reports/cases_a1.tsv", "anchor": "rows A1-01, A1-02, A1-03, A1-17, A1-18, A1-24, A1-25, A1-26"}],
 "locator_status": "DOCUMENT"}
```

* **`counter_evidence`, append:**
    * "A one-time status with recent developmental gains, not attributed to treatment, in a homozygous missense child on two other drugs (outside the four classes)" (A1-32).
    * "Brainstem or central-tegmental signal is recorded in two children with no vigabatrin in their drug column; neither shows the globus-pallidus-and-thalamus pattern of the exposed pair" (A1-32, A1-54).

## 3. `view/work_order.json`

* **Entry `NEED-SEIZURE-CONTROL-SYMPTOMATIC`, field `data`.** Append: "Status 2026-11-05/06 (A1): the diet denominator is still not stated. At least 3 children were exposed; patients 3 and 5 have no diet entry; the narratives of patients 1-4 are not reachable. Vigabatrin MRI exposure is 2 of 2 at abstract level in a report selected for the finding, so it is not a denominator of exposed children. The same group's 64-child cohort (PMID 42735667) gives 18 of 64 with the abnormality, 9 of the 18 of genetic aetiology." Rests on A1-04, A1-05, A1-07, A1-09, A1-10.
* **Entry `NEED-SEIZURE-CONTROL-SYMPTOMATIC`, field `would_change`.** No change: C2 stays for both series.
* **Entry `NEED-MYELINATION`, field `feasibility`.** Replace "Human MRI denominators are not available from the abstract" with: "Human MRI denominators at abstract level: 2 of 2 exposed children had the change, in a report selected for the finding. The full text is not reachable by an open route: no PMC record, and the publisher refuses automated access. The same group's 64-child vigabatrin cohort gives 18 of 64 with the abnormality and 9 of the 18 of genetic aetiology. Not available: age band at exposure, duration class, and hormonal co-therapy at the change in these two children." Rests on A1-09, A1-10, receipt `FTR-20261106-42735667-21`.

## 4. `cards/H02_gabaat_inactivator_myelin_exposure.packet.json`, caveats

* **Caveat 1:** "Hormonal co-therapy at the time of these two children's MRI change is unknown: the abstract is silent and the full text unreachable, so it cannot be named as present or excluded here. The same group's 64-child cohort reports concomitant prednisolone as associated with the abnormality (OR 4.07, 95% CI 1.22-17.3, univariable). It is therefore a named confounder, not a neutral unknown. The two children are probably inside that cohort and are not added to its 18 cases."
* **Caveat 2:** "In WWOX-DEE, brainstem and central-tegmental T2 or diffusion signal also occurs without documented vigabatrin (two children in two reports; absence from a drug column). Neither shows the globus pallidus and thalamus pattern reported in the exposed pair. Attributing a deep-grey change therefore needs a scan of the same structures before exposure. The exposed pair supplies this as a within-child comparison, at abstract level."
* **For the white-matter package (B1).** Oliver 2023 Table 2 records brainstem, central-tegmental, midbrain, globus-pallidus or dentate findings in six vigabatrin-exposed children, timing not stated (A1-36 to A1-41). Riva 2022 records pons and dentate signal while vigabatrin was continued (A1-18).

Rests on A1-09, A1-10, A1-18, A1-32, A1-36 to A1-41, A1-54.

## 5. `catalogue_funnel_it18_p2_20261101/vigabatrin_sources_resolved.tsv`

Proposed new and updated rows. All 12 columns are given, and every value comes from the file's own value sets.

| assertion_id | member_evidence_sign | source_as_carried | paper_record | pmid | receipt_on_ledger | held_locator | descriptive_code_it17_semantics | objective_match | origin_group | pub_year | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-VGB-1 (update) | benefit | Shaukat 2018, child 1, via CLAIM 001 | PAPER 045 | 30361190 | add staged FTR-20261105-30361190-21 | a1_wwox_reports/cases_a1.tsv A1-02 | favourable | yes | PMID:30361190 | 2018 | add: other seizure types followed; Table 1 codes the overall response of this case Partial (3 drugs); development remained profoundly delayed (discordant) |
| A-VGB-2 (update) | partial_benefit | Shaukat 2018, child 2, via CLAIM 001 | PAPER 045 | 30361190 | as A-VGB-1 | A1-03 | favourable (partial) | yes | PMID:30361190 | 2018 | add: Table 1 codes Poor (4 drugs); discordant |
| A-VGB-10 (update) | null | Chong 2023 case series, via CLAIM 001 | PAPER 017 | 36537114 | add staged FTR-20261105-36537114-21 | A1-08 | undeterminable | yes | PMID:36537114 | 2023 | regimen-level poor control with clobazam and zonisamide; a second likely pathogenic variant in another gene is a confounder |
| A-VGB-11 (update) | (not in member_evidence) | Chong 2023, improved only with ketogenic diet, via CLAIM 001 | PAPER 017 | 36537114 | as A-VGB-10 | not found: the delivered surface pairs vigabatrin with the diet in no patient | undeterminable | unknown | PMID:36537114 | 2023 | still unresolvable on open routes; the CLAIM 001 sentence is wider than the delivered text |
| A-VGB-12 (new) | partial_benefit | Tarta-Arsene 2017 | PAPER 151 | 28721938 | staged FTR-20261105-28721938-21 | A1-24 | favourable (partial) | yes | PMID:28721938 | 2017 | one month of control, then relapse; discordant with development; possibly Piard 2019 patient 8, whose report carries no treatment row |
| A-VGB-13 (new) | benefit | Al Baradie 2022, patients 2.1, 2.2 and 6 | PAPER 171 | 35792847 | staged FTR-20261105-35792847-21 | A1-29, A1-30, A1-34 | favourable | yes | PMID:35792847 | 2022 | controlled, not stated seizure-free; 2.1 still had myoclonic seizures on EEG; development status labels only; 2.1 and 2.2 possibly an earlier sibship |
| A-VGB-14 (new) | unresolved | Oliver 2023, 7 of 10 with spasms plus patient 6 | PAPER 018 | 36779245 | staged FTR-20261105-36779245-21 | A1-36 to A1-43 | undeterminable | yes | PMID:36779245 | 2023 | exposure only, no response reported by drug; 2 of 8 current at follow-up |
| A-VGB-7 (update) | (harm, other endpoint) | Choi 2026, via CLAIM 001 | PAPER 003 | 41442931 | staged FTR-20261105-41442931-21 (abstract) | A1-09, A1-10 | contrary on another endpoint (off_objective) | no | PMID:41442931 | 2025 | exposure 2 of 2 with the MRI change, abstract level, report selected for the finding; hormonal co-therapy unknown in these two; population figure in the same group's cohort PMID 42735667 (18 of 64; prednisolone associated, univariable) |

## 6. Early cards (`cards_early/`)

* **`EB-KD-01`, `p4_fields.temporal_or_model_limit`.**
    * Replace "two of the three responders had died within roughly two years and the developmental row is identical in all five columns" with "two of the three responders were deceased at the last report; the developmental row is a single status label in all five columns, so no developmental course is recorded".
    * Add: "Across reports: 12 exposed (a minimum count), 5 responders, none with a developmental outcome; two children of the homozygous missense class exposed, one non-responder (A1-26), one with no outcome attributable to the diet (A1-35)."
* **`EB-HORM-AX-01`, `p4_fields.functional_evidence_available`.** Add: "Primary reports read: 11 exposed in 6 reports; 3 responses (one partial, one with relapse, one complete clinical control with sleep EEG still abnormal), 5 non-responses, 3 not stated."
* **`EB-CBD-AX-01`, `p4_fields.functional_evidence_available`.** Add: "27-centre series: WWOX 3 treated, 2 at least 50 percent responders, the third below criterion, adjunctive status not stated, no developmental measure (CGI-I only); one single case ineffective (CBD oil); one cohort 4 of 4 continued."
* **`EB-DEV-AX-01`, `p4_fields.functional_evidence_available`.** Replace "the case-series bodies were not searched" with "the bodies of 11 case reports and series were read at partial full-text depth for this question: the developmental course is a clinical narrative in every one, without a scale; 6 children have both endpoints and none a sustained response".

## proposed_registry_changes (plain statements; nothing is changed here)

1. **CLAIM 001.**
    * Replace "Chong 2023: un caso resistente al vigabatrin, uno migliora in combinazione con KD" with "Chong 2023: one patient (patient 5) poorly controlled on a three-drug regimen that included vigabatrin; the delivered text pairs vigabatrin with the diet in no patient" (A1-08).
    * Add to the Shaukat sentence: "other seizure types followed; Table 1 codes the overall response Partial (child 1) and Poor (child 2)" (A1-02, A1-03).
    * Narrow the Riva wording to the printed "three cycles of ACTH had very poor results" and "did not significantly improve seizures and was suspended" (A1-20, A1-21).
    * Add efficacy observations: Tarta-Arsene 2017 (A1-24), Al Baradie 2022 (A1-29, A1-30, A1-34), Oliver 2023 exposure (A1-36 to A1-43).
    * Add one imaging boundary: brainstem or central-tegmental signal occurs without documented vigabatrin in two WWOX children, not in the exposed pair's deep-grey pattern (A1-32, A1-54).
    * Status `conflicting evidence` unchanged.
2. **CLAIM 031.**
    * Replace "The qualifier's scope is ambiguous in the source and this record does not resolve it" with the better-supported of two readings, with the residual ambiguity named: "the same Discussion attaches the improvement of epileptic activity to the first child as an example, and both narratives record profound delay, so the qualifier most likely scopes the achievement of better control; the referent of 'these cases' is not shown to be limited to the report's two children".
    * Narrow the Title's universal to the record: "in the published WWOX-DEE reports read, partial or transient seizure improvement was not followed by developmental gain in any of 4 children with both endpoints (null or splice classes; clinical narratives; short or undated follow-up); no sustained response is recorded".
    * Add the allele-class context row (A1-32).
    * Add the premise support at abstract level: "developmental delay was evident from birth" in the seven-child series (PMID 42721537).
    * Status `in observation` unchanged.
3. **CLAIM 042.**
    * Blockquote: replace "two of the three diet responders are previously published individuals, named by the source" with "one of the three responders (patient 4) is stated to be published before; patient 2's credit to an earlier cohort is variant-level (no individual of its Supplementary Table 1 carries that genotype); the second previously published child is most likely patient 3, a non-responder (INFERENZA); pooled counts can double-count patient 4 among responders and patient 3 among exposed children" (A1-05, A1-06, A1-07).
    * Replace "the developmental endpoint did not move in any column" with "the developmental row is a single status label in every column; no course is recorded" (A1-04, A1-05, A1-07).
    * `REVIVAL_TRIGGER`: met by two reports (A1-26 no response; A1-35 no attributable outcome). Both new exposures are homozygous for the allele, whereas this claim's carrier is compound heterozygous with an exon-level deletion. The statement about that carrier is unchanged, and the boundary now reads: "two homozygous exposures, no attributable response; nothing is yet recorded for the compound-heterozygous configuration".
    * Denominator: still not stated, minimum 3.
4. **PAPER 017** (Chong 2023): add a patient-overlap field: "patient 3 probably = PAPER 045 child 1 (INFERENZA: five matched features including genotype class, onset band and two imaging features; shared co-authors); patients 2 and 4 credited to Piard 2019 at variant level only".
5. **PAPER 045** (Shaukat 2018): add the same overlap field, the Table 1 response codes, and the better-supported reading of the qualifier with its residual ambiguity.
6. **PAPER 143** (Nagarajan 2023): refine the overlap note of `CC-20261004W7-B-PATIENT-OVERLAP-01` to "sex and age at last follow-up exclude both candidate identities: three distinct children of this genotype class across the two reports" (A1-15).
7. **PAPER 171** (Al Baradie 2022):
    * Add the per-patient class of treatment from Table 3 (vigabatrin in four, the diet in two; A1-29 to A1-35) and the diet exposure in one child of the homozygous missense class.
    * Add that the Discussion's "nine patients ... treated with vigabatrin" counts its 70-patient table, not its own series.
8. **PAPER 018** (Oliver 2023): add "hormonal therapy: 2 patients in the text, 3 in Table 2; Table 2 underlines current drugs (the diet continued by 1 of 3, cannabidiol by 4 of 4); brainstem, central-tegmental, globus-pallidus or dentate MRI findings in six vigabatrin-exposed patients with timing not stated, and a dorsal-pons finding in one patient never on vigabatrin" (A1-36 to A1-54).
9. **PAPER 003** (Choi 2026) and `full_text_queue_current.md` **FT-114**:
    * Add "re-checked 2026-11-05: still no open route (no PMCID; Europe PMC subscription only; publisher pages HTTP 403 to automated fetch); abstract receipt staged `FTR-20261105-41442931-21`".
    * Add "the same group published a 64-child vigabatrin cohort (PMID 42735667, *Seizure* 2026) reporting 18 of 64 with the abnormality, 9 of the 18 of genetic aetiology, and an association with concomitant hormonal therapy. The two children of this report are probably inside it (INFERENZA from shared first author, two shared co-authors, one institution, an inclusion criterion of two scans before and during exposure, and an intake window that precedes this report)".
    * New paper record for PMID 42735667, abstract-level (receipts `FTR-20261105-42735667-23` of B1 and `FTR-20261106-42735667-21`).
10. **New paper record** for PMID 30061856 (Ko 2018, DOI 10.3389/fneur.2018.00530): WWOX n = 1 among 155 diet-treated DEE patients, a responder (at least 90 percent seizure reduction) at 3, 6 and 12 months; no genotype or development. Staged receipt `FTR-20261105-30061856-21`.
11. **CORPUS P225** (Nishino 2024, PMID 38407561): depth becomes abstract-only with a staged receipt. The ACTH non-response is an abstract-level datum.
12. **PAPER 189** (Cerulli Irelli 2025): note the possible identity of one of its three WWOX patients with the single case of PAPER 133 (shared authors; preparation differs), counted once. Note also that adjunctive status is not stated for its WWOX patients.
13. **`full_text_queue_current.md` FT-110** (PMID 42721537, seven-child series):
    * Add this package's question: per-child treatment, response definition and developmental course. The abstract names no drug, reports drug resistance in all seven and delay from birth, and enters no count (receipt `FTR-20261106-42721537-21`).
    * Add de-duplication targets for when it is read: PMID 36537114 patients 1 and 2, and the three WWOX patients of PMID 40126049.
    * Narrow FT-110's "cinque pazienti omozigoti": the abstract says the recurrent splice-site variant was "identified in five patients" and does not state zygosity.
