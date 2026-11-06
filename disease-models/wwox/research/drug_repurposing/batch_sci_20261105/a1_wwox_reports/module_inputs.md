# A1 module inputs (proposals only; nothing here edits a module file or a registry)

Scientist `sb-a1`, task `ORCH-SCIBATCH-DR-20261105`, 2026-11-05. Every proposal names the rows of `cases_a1.tsv` (`A1-nn`) or `denominators_a1.tsv` it rests on. The field names below are those of the files each proposal targets. Not medical advice: no dose, schedule or preference is carried anywhere.

## 1. `ranking_it8_p9_20261029/ranking.json`, investigation `INV-10`

| Field | Proposed value | Rests on |
|---|---|---|
| `evidence_available` | "Clinical reports only. Children counted once across 14 reports: 36 to 38 exposed to at least one of vigabatrin, hormonal therapy, ketogenic diet or cannabidiol. Both a symptomatic and a developmental outcome recorded for 6: 4 discordant (symptom improved, development did not), 2 concordant non-responses; no developmental gain recorded after any of the four classes. Vigabatrin: 5 children with both endpoints in 4 reports (4 discordant, 1 concordant non-response); hormonal 3 of 11; ketogenic diet 2 of 12; cannabidiol 1 of 7. Counts only, no percentage (n below 10). Developmental instruments are clinical narratives without a scale." | A1-01, A1-02, A1-03, A1-17, A1-18 to A1-21, A1-24, A1-25, A1-26; denominators rows `POOLED` |
| `evidence_depth` | "E4 - card reviewed, WWOX-side assertions read beyond abstract in 11 reports (the six children with both endpoints come from five of them); one source at abstract level (Choi 2026)" (the scale's own wording: E3 = no WWOX-side result read beyond abstract, E4 = WWOX-side assertions read beyond abstract) | receipts `FTR-20261105-*-21` |
| `decisive_uncertainty` | unchanged in substance; add: "and whether the separation holds for residual-function alleles: the only developmental gain in the read set is in a homozygous P47T child outside the four classes" | A1-32 |
| `next_test` | reword as a denominator request, without contact: "Name, for each WWOX-DEE series that reports an intervention, the number exposed, the response definition, and a dated developmental instrument before and after; the five-patient series and Choi 2026 are the first two." | denominators rows for PMID 36537114 and 41442931 |
| `why_now` | replace "The module already holds a series in which symptomatic response and developmental outcome did not move together" with "Four children in three reports show symptomatic response without developmental gain; the five-patient series is not one of them (its developmental row is a single status label)" | A1-04, A1-05, A1-07 (status labels), A1-01 to A1-03, A1-17, A1-24 |

## 2. `needs/needs.json`, need `NEED-SEIZURE-CONTROL-SYMPTOMATIC`

* **`observed` O1, field `limits`.** Replace "At least one, probably two, of the three responders are previously published individuals (patient 4 explicitly; patient 2 by a Table 1 row)" with: "One of the three responders (patient 4) is stated to be published before. Patient 2's Table 1 credit to Piard 2019 is variant-level: no column of that report's Supplementary Table 1 carries patient 2's homozygous genotype. The series' other previously published child is most likely patient 3, a non-responder, who matches Shaukat 2018's first child (INFERENZA)." Rests on A1-05, A1-06, A1-07, receipt `FTR-20261105-30356099-21`.
* **`observed` O1, field `statement`.** Replace "developmental status was recorded as identical across all five" with "developmental status is a single Table 1 label (profound developmental delay) in all five; no pre-diet status or course is on the delivered surface". Rests on A1-04, A1-05, A1-07.
* **`observed` O2, field `statement`.** Append: "Further: complete control for one month then relapse (Tarta-Arsene 2017); seizures controlled in three of four treated children of one series (Al Baradie 2022); used in 7 of 10 children with spasms of one cohort with no response reported (Oliver 2023). The 'resistant' case of the five-patient series is regimen-level poor control on three drugs." Rests on A1-24, A1-29, A1-30, A1-34, A1-36 to A1-43, A1-08.
* **`observed`, new O4.** Fields: `statement` "Across reports, children with both a symptomatic and a developmental outcome: 6; symptom improved without developmental gain in 4, neither moved in 2"; `model_type` human_clinical_report; `species` human; `genotype` "predicted null or splice in 5, homozygous Q230P in 1"; `comparison` "responders against non-responders, between reports"; `readout` "clinician-reported seizure course and clinician-narrated development"; `readout_level` clinical; `direction_observed` "symptom and development apart in 4 of 6, together (both unchanged) in 2 of 6"; `limits` "six children, clinical narratives without a developmental scale, follow-up after the intervention about 5 months to about 2.5 years where dated (4 children), undated in 2, co-therapy in every case, counts only"; `pmid` "30361190, 39101447, 28721938, 35573960, 29808465"; `locator_status` "STAGED (this package; receipts not recorded)". Rests on A1-01, A1-02, A1-03, A1-17, A1-18, A1-24, A1-25, A1-26.
* **`counter_evidence`, append:**
    * "One developmental gain under seizure control in the read set, in a homozygous P47T child on levetiracetam and topiramate (outside the four classes)" (A1-32).
    * "VABAM-compatible deep grey or brainstem signal is recorded in WWOX children without documented vigabatrin" (A1-32, A1-54).

## 3. `view/work_order.json`

* **Entry `NEED-SEIZURE-CONTROL-SYMPTOMATIC`, field `data`.** Append: "Status 2026-11-05 (A1): the diet denominator is still not stated (minimum 3 exposed; patients 3 and 5 without a diet entry; narratives of patients 1-4 not reachable); vigabatrin MRI exposure is 2 of 2 at abstract level, with age band, duration and hormonal co-therapy at the MRI change not stated." Rests on A1-04, A1-05, A1-07, A1-09, A1-10.
* **Entry `NEED-SEIZURE-CONTROL-SYMPTOMATIC`, field `would_change`.** No change: C2 stays for both series.
* **Entry `NEED-MYELINATION`, field `feasibility`.** Replace "Human MRI denominators are not available from the abstract" with: "Human MRI denominators are not available. The abstract states 2 of 2 exposed with the change; the full text is not reachable by an open route (publisher HTTP 403, no PMC record). A VABAM-compatible signal is recorded in WWOX children without vigabatrin (Oliver 2023 patient 5; Al Baradie 2022 patient 4)." Rests on A1-09, A1-10, A1-32, A1-54.

## 4. `cards/H02_gabaat_inactivator_myelin_exposure.packet.json`

* **Caveat, proposed wording:**
    * "Hormonal co-therapy at the time of the WWOX children's MRI change: unknown (abstract silent; full text unreachable). It cannot be named as present or excluded."
    * "In WWOX-DEE, deep grey and brainstem T2 or diffusion signal also occurs without vigabatrin (two children in two reports), so attribution needs a pre-exposure scan of the same structures; Choi 2026 supplies a within-child 'new during treatment' comparison at abstract level."
  Rests on A1-09, A1-10, A1-32, A1-54.
* **For the white-matter package (B1).** Oliver 2023 Table 2 places VABAM-compatible findings in six vigabatrin-exposed children, with timing not stated (patients 1, 3, 6, 7, 8, 10). Rows A1-36 to A1-41.

## 5. `catalogue_funnel_it18_p2_20261101/vigabatrin_sources_resolved.tsv` (proposed new and updated rows, in its columns)

| assertion_id | member_evidence_sign | source_as_carried | paper_record | pmid | receipt_on_ledger | held_locator | descriptive_code_it17_semantics | objective_match | note |
|---|---|---|---|---|---|---|---|---|---|
| A-VGB-1 (update) | benefit | Shaukat 2018, child 1 | PAPER 045 | 30361190 | add staged FTR-20261105-30361190-21 | cases_a1.tsv A1-02 | favourable | yes | add: Table 1 codes the overall response of this case Partial (3 drugs); development remained profoundly delayed (discordant) |
| A-VGB-2 (update) | partial_benefit | Shaukat 2018, child 2 | PAPER 045 | 30361190 | as above | A1-03 | favourable (partial) | yes | add: Table 1 codes Poor (4 drugs); discordant |
| A-VGB-10 (update) | null | Chong 2023 patient 5 | PAPER 017 | 36537114 | add staged FTR-20261105-36537114-21 | A1-08 | undeterminable | yes | regimen-level poor control with clobazam and zonisamide; a de novo GRIA4 variant is a confounder |
| A-VGB-11 (resolve) | (not in member_evidence) | Chong 2023, "improved only with KD" | PAPER 017 | 36537114 | as above | none: the delivered surface pairs vigabatrin with the diet in no patient | undeterminable | unknown | stays unresolvable on open routes; the CLAIM 001 sentence is wider than the delivered text |
| A-VGB-12 (new) | partial_benefit | Tarta-Arsene 2017 | PAPER 151 | 28721938 | staged FTR-20261105-28721938-21 | A1-24 | favourable (transient) | yes | complete control for one month, then relapse; discordant with development; possibly Piard 2019 patient 8 |
| A-VGB-13 (new) | benefit | Al Baradie 2022 patients 2.1, 2.2 and 6 | PAPER 171 | 35792847 | staged FTR-20261105-35792847-21 | A1-29, A1-30, A1-34 | favourable | yes | 2.1 still had myoclonic seizures on EEG; development status labels only; 2.1 and 2.2 possibly an earlier sibship |
| A-VGB-14 (new) | (exposure only) | Oliver 2023, 7 of 10 with spasms plus patient 6 | PAPER 018 | 36779245 | staged FTR-20261105-36779245-21 | A1-36 to A1-43 | undeterminable | yes | no response by drug; 2 of 8 current at follow-up |
| A-VGB-7 (update) | (harm, other endpoint) | Choi 2026 | PAPER 003 | 41442931 | staged FTR-20261105-41442931-21 (abstract) | A1-09, A1-10 | contrary on another endpoint | no | exposure 2 of 2 with the MRI change (abstract); hormonal co-therapy unknown |

## 6. Early cards (`cards_early/`)

* **`EB-KD-01`, `p4_fields.temporal_or_model_limit`.** Replace "two of the three responders had died within roughly two years and the developmental row is identical in all five columns" with "two of the three responders had died within roughly two years; the developmental row is a single status label in all five columns, so no developmental course is recorded". Add: "Across reports, 12 exposed (minimum), 5 responders, none with a developmental outcome; two homozygous Q230P children exposed, one non-responder (A1-26), one with no outcome attributable to the diet (A1-35)." Rests on denominators `ketogenic_diet` rows.
* **`EB-HORM-AX-01`, `p4_fields.functional_evidence_available`.** Add: "Primary reports read: 11 exposed in 6 reports; 3 responses (one partial, one with relapse, one complete clinical control with persisting sleep EEG abnormality), 5 non-responses, 3 not stated." Rests on denominators `hormonal` rows.
* **`EB-CBD-AX-01`, `p4_fields.functional_evidence_available`.** Add: "27-centre series: WWOX 3 treated, 2 at least 50 percent responders, no developmental measure (CGI-I only); one single case ineffective (CBD oil); one cohort 4 of 4 continued." Rests on A1-19, A1-50 to A1-53, A1-55 to A1-57.
* **`EB-DEV-AX-01`, `p4_fields.functional_evidence_available`.** Replace "the case-series bodies were not searched" with "the case-report bodies of 11 full texts were read for this question: developmental course is a clinical narrative in every one, without a scale; 6 children have both endpoints". Rests on denominators `any_of_the_four_classes` row.

## proposed_registry_changes (plain statements; nothing is changed here)

1. **CLAIM 001** (`claim_registry_current.md`):
    * Replace "Chong 2023: un caso resistente al vigabatrin, uno migliora in combinazione con KD" with "Chong 2023: one patient (patient 5) poorly controlled on a three-drug regimen that included vigabatrin; the delivered text pairs vigabatrin with the diet in no patient" (A1-08).
    * Add to the Shaukat sentence: "Table 1 codes the overall response Partial (child 1) and Poor (child 2)" (A1-02, A1-03).
    * Narrow the Riva wording "ACTH e dieta chetogenica senza effetto" to the printed "three cycles of ACTH had very poor results" and "did not significantly improve seizures and was suspended" (A1-20, A1-21).
    * Add efficacy observations: Tarta-Arsene 2017 (A1-24), Al Baradie 2022 (A1-29, A1-30, A1-33, A1-34), Oliver 2023 exposure (A1-36 to A1-43).
    * Add one imaging boundary: VABAM-compatible signal occurs without vigabatrin in two WWOX children (A1-32, A1-54).
    * Status `conflicting evidence` unchanged.
2. **CLAIM 031:**
    * Replace the sentence "The qualifier's scope is ambiguous in the source and this record does not resolve it" with the source-resolved reading: the same Discussion assigns the improvement of epileptic activity to the first child ("e.g. in the first child") and the narratives record profound delay in both, so "in some of these cases" scopes the achievement of better control (INFERENZA from DATO; quotes in README section 7).
    * Narrow the Title's universal ("seizure control does not rescue development") to the record: "in the published WWOX-DEE reports read, seizure control was not followed by developmental gain in any of 4 children with both endpoints (null or splice genotypes, clinical narratives, follow-up under 3 years)".
    * Add the counter (A1-32) as an allele-class boundary.
    * Status `in observation` unchanged.
3. **CLAIM 042:**
    * In the blockquote, replace "two of the three diet responders are previously published individuals, named by the source" with "one of the three responders (patient 4) is stated to be published before; patient 2's Piard credit is variant-level (no individual of that Supplementary Table 1 carries its genotype); the second previously published child is most likely patient 3, a non-responder, matching Shaukat 2018's first child" (A1-05, A1-06, A1-07).
    * Replace "the developmental endpoint did not move in any column" with "the developmental row is a single status label in every column; no course is recorded" (A1-04, A1-05, A1-07).
    * Record that the `REVIVAL_TRIGGER` "any documented diet exposure in a Q230P carrier" is met by two reports (A1-26 no response; A1-35 no attributable outcome). The Q230P boundary becomes "two homozygous exposures, no attributable response".
    * Denominator: still not stated, minimum 3.
4. **PAPER 017** (Chong 2023): add a patient-overlap field, "patient 3 probably = PAPER 045 child 1 (INFERENZA: genotype, sex, onset, MRI, optic atrophy, shared co-authors); patients 2 and 4 credited to Piard 2019 at variant level only".
5. **PAPER 045** (Shaukat 2018): add the same overlap field, the Table 1 response codes, and the resolved reading of the qualifier.
6. **PAPER 143** (Nagarajan 2023): refine the overlap note of `CC-20261004W7-B-PATIENT-OVERLAP-01` to "row 40 is female (not Piard 14) and 30 months at last follow-up in a 2018-2022 testing window (not Piard 13): three distinct homozygous p.Arg264* children across the two reports" (A1-15).
7. **PAPER 171** (Al Baradie 2022): add the per-patient treatment of Table 3 and the homozygous Q230P child's diet exposure (A1-29 to A1-35). Add that the Discussion's "nine patients ... treated with vigabatrin" counts its 70-patient table, not its own series.
8. **PAPER 018** (Oliver 2023): add "hormonal therapy: 2 patients in the text, 3 in Table 2 (adds patient 7); current drugs are underlined in Table 2 (ketogenic diet continued by patient 12; cannabidiol by patients 6, 9, 10, 11); VABAM-compatible MRI findings in patients 1, 3, 5, 6, 7, 8, 10, with patient 5 never on vigabatrin" (A1-36 to A1-54).
9. **PAPER 003** (Choi 2026) and `full_text_queue_current.md` **FT-114**: add "re-checked 2026-11-05: still no open route (no PMCID; Europe PMC subscription only; publisher pages HTTP 403 to automated fetch); abstract receipt staged `FTR-20261105-41442931-21`".
10. **New paper record** for PMID 30061856 (Ko 2018, DOI 10.3389/fneur.2018.00530): WWOX n = 1 among 155 diet-treated DEE patients, a responder (at least 90 percent seizure reduction) at 3, 6 and 12 months; no genotype or development. Staged receipt `FTR-20261105-30061856-21`.
11. **CORPUS P225** (Nishino 2024, PMID 38407561): depth becomes abstract-only with a staged receipt; the ACTH non-response is an abstract-level datum. Its title wording stays as the record already handles it.
12. **PAPER 189** (Cerulli Irelli 2025): note the possible identity of one of its three WWOX patients with the single case of PAPER 133 (shared authors; preparation differs), counted once.
