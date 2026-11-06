# A1 author response to the blind quote audit (`verify/audit_A1/`) and the adversarial review (`verify/review_A/`)

Scientist `sb-a1`, 2026-11-06. Each finding is ACCEPTED or DISPUTED below, with the evidence and the place it was changed. Nothing is disputed; one finding is accepted with a scoped addition. Not medical advice.

## Blind quote audit (triple ids)

| Triple | Verdict | Response | Changed where |
|---|---|---|---|
| A1-A1-03 | UNDERSHOOT | ACCEPTED. Shaukat 2018 Results and the Figure 3B caption print bilateral parietal (posterior) polymicrogyria, a dysplastic thin corpus callosum and reduced white matter volume for the second child. | `cases_a1.tsv` A1-03 `imaging_finding` |
| A1-A1-18 to A1-A1-21 | UNDERSHOOT | ACCEPTED. One correction for the same child: thinned corpus callosum, squared ventricles, mild pons and dentate signal at 2 years 4 months. Added to the imaging theme as a signal in a vigabatrin-continued child, timing unstated. | A1-18 to A1-21 `imaging_finding`; README section 9; `module_inputs.md` section 4 |
| A1-A1-19 (caveat) | — | ACCEPTED. "stopped" is inferred from the current-drug sentence; said so. | A1-19 `co_therapy_stated` |
| A1-A1-22 | OVERSHOOT | ACCEPTED. No EEG is tied to the vigabatrin step. | A1-22 `symptomatic_instrument` |
| A1-A1-32 | OVERSHOOT | ACCEPTED. "improved" rested on a one-time status not linked to the drugs. Recoded `not_reported` (status). Concordance becomes `not_assessable`; role becomes `context`. The second diagnosis and the chemotherapy admission are now stated. Effect: the other_context concordant row disappears, and README decision line 10 now says "one-time status, not attributed to treatment". | A1-32; `denominators_a1.tsv` other_context PMID 35792847; README lines 2 and 10, sections 9 and counter-evidence |
| A1-A1-33 | OVERSHOOT | ACCEPTED. "regressed" is a status printed about two months after vigabatrin was added, untimed relative to it. Recoded `not_reported` (status). Effect: vigabatrin children with a developmental outcome go from 6 to 5; any-class goes from 7 to 6. | A1-33; denominators vigabatrin PMID 35792847, vigabatrin POOLED, any_of_the_four_classes |
| A1-A1-35 | OVERSHOOT | ACCEPTED. Current vigabatrin is not restated at the last visit; weaning off the diet was under consideration. | A1-35 `co_therapy_stated`, `symptomatic_instrument` |
| A1-A1-55, A1-A1-56, A1-A1-57 | OVERSHOOT | ACCEPTED. Status is now `tried`, and adjunctive status is recorded as not stated for these patients. A1-57 is "none by criterion" (below a 50 percent reduction; no worsening listed), not a demonstrated zero. The earlier arithmetic inference about the third patient is withdrawn from the README. | A1-55 to A1-57; denominators cannabidiol PMID 40126049 |
| A1-A1-08 (caveat) | — | ACCEPTED. The narrative says progressive volume loss while Table 1 says stable; both are now stated. | A1-08 `imaging_finding` |
| A1-A1-09, A1-A1-10 (caveat) | — | ACCEPTED. The abstract describes the two children jointly. The cohort membership note is added. | A1-09, A1-10 `imaging_finding`, `same_patient_as` |
| A1-A1-14 (caveat) | — | ACCEPTED. The self-contradictory outcome cell is noted. | A1-14 `symptomatic_instrument` |
| A1-A1-17 (caveat) | — | ACCEPTED. The widened left ventricle and the widened frontotemporal extracerebral space are added. | A1-17 `imaging_finding` |
| A1-A1-27 (caveat) | — | ACCEPTED. `partial` is stated as the coding floor. | A1-27; README coding rules |
| A1-A1-30 (caveat) | — | ACCEPTED. "controlled" is coded `resolved` without implying seizure freedom; the same note goes on A1-34. | A1-30, A1-34; README coding rules |
| A1-A1-39 (caveat) | — | ACCEPTED. Cerebellum and peduncles are added. | A1-39 |
| A1-A1-45 (caveat) | — | ACCEPTED. Text and table differ (2 against 3); the row follows Table 2, as stated. | A1-45 `co_therapy_stated`; README section 2 |
| A1-A1-54 (caveat) | — | No change needed: consistent. The age at death is removed under the class-level redaction. | A1-54 |
| All other SUPPORTED triples | SUPPORTED | No change, except `source_depth`, which is normalised in all 57 rows (review XP-F). | `cases_a1.tsv` |

## Adversarial review (statement ids)

| Statement | Verdict | Response | Changed where |
|---|---|---|---|
| A1-D01 | NARROW | ACCEPTED. The receipts say 12 partial_fulltext_read and 2 abstract_only (now 4 abstract_only, with the 2 correction-round abstracts). "Read in full text" becomes "beyond the abstract at partial full-text depth". The twelfth source is named (PMID 30356099). A per-source depth table is added. | README line 1 and "Sources and depth" |
| A1-D02 | NARROW | ACCEPTED, using the reviewer's wording. The regression mention is now a status (after audit A1-A1-33). | README line 2, section 5 table |
| A1-D03 | NARROW | ACCEPTED. The five are not independent: three also supply the other classes, all five were on co-therapy, and two had vigabatrin in sequence with hormonal therapy. | README line 3; denominators vigabatrin POOLED note |
| A1-D04 | HOLDS | No change. | — |
| A1-D05 | NARROW | ACCEPTED. The 64-child cohort was read at abstract level (`FTR-20261106-42735667-21`, built on sb-b1's `FTR-20261105-42735667-23`). It gives 18 of 64 and prednisolone OR 4.07 (univariable); probable membership of the pair is marked INFERENZA. | README line 5, section 6; A1-09, A1-10; denominators Choi row |
| A1-D06 | NARROW | ACCEPTED. The pre-registered consequence is applied: the H02 line is filled at abstract level with the selection caveat and the cohort figure, and hormonal co-therapy is named as a confounder with its source. | README line 6; `module_inputs.md` sections 3 and 4 |
| A1-D07 | NARROW | ACCEPTED. The trigger fires on the homozygous configuration; the claim's compound-heterozygous carrier is untouched. Per-child allele, age and cause of death are removed from the denominators notes (genotype class only). | README line 7; denominators ketogenic_diet rows; `module_inputs.md` item 3 |
| A1-D08 | NARROW | ACCEPTED. The asymmetry is now stated: a variant credit alone is no identity, and patient 3 is carried by the extra matched features. The double-counting clause is restored and re-scoped. Feature lists are reduced to class-level counts. | README line 8, section 8; A1-01, A1-06; `module_inputs.md` O1 |
| A1-D09 | NARROW | ACCEPTED. This is the better of two readings, not a resolution; the residual ambiguity (the referent of "these cases") is named. | README line 9, section 7; `module_inputs.md` item 2 |
| A1-D10 | NARROW | ACCEPTED. The hypothesis is untestable on the present record; no sustained, instrumented responder exists in it. | README line 10 |
| A1-MI-INV10 | NARROW | ACCEPTED. The E4 wording now says partial. The existing next test is recorded as EXECUTED with its result, and each class is assigned to the branch it fired. | `module_inputs.md` section 1 |
| A1-MI-NEEDS-O1 | NARROW | ACCEPTED. The double-counting clause is kept and re-scoped; the genotype is at class level. | section 2 |
| A1-MI-NEEDS-O2 | HOLDS | No change beyond one EEG qualifier. | section 2 |
| A1-MI-NEEDS-O4 | REJECT | ACCEPTED. Re-emitted with all 16 fields, including `tissue_or_cells`, `age_stage`, `evidence_scope` WWOX_EXPERIMENT_IN_DEE_SYSTEM and `locators`. `locator_status` is now DOCUMENT, pointing at `cases_a1.tsv`; the staged state is noted in `limits`. | section 2, new O4 |
| A1-MI-NEEDS-COUNTER | HOLDS | Reworded for audit A1-A1-32 (status) and review XP-D (location). | section 2 |
| A1-MI-WO-SEIZURE | NARROW | ACCEPTED, with the reviewer's wording. | section 3 |
| A1-MI-WO-MYELIN | NARROW | ACCEPTED. The replacement no longer contradicts the pre-registered consequence. | section 3 |
| A1-MI-H02 | NARROW | ACCEPTED. Both caveats now carry the reviewer's wording. | section 4 |
| A1-MI-VGBTSV | REJECT | ACCEPTED. All rows are re-emitted with 12 columns including `origin_group` and `pub_year`. A-VGB-14 is `unresolved`, A-VGB-12 is `favourable (partial)`, and A-VGB-7 keeps "(off_objective)". | section 5 |
| A1-MI-CARDS | HOLDS | Kept. The ages at death in the EB-KD-01 wording are removed. | section 6 |
| A1-MI-REG-001 | HOLDS | Kept, plus the imaging location boundary. | registry item 1 |
| A1-MI-REG-031 | NARROW | ACCEPTED. | registry item 2 |
| A1-MI-REG-042 | NARROW | ACCEPTED: the configuration clause is added. | registry item 3 |
| A1-MI-REG-PAPERS | NARROW | ACCEPTED. Item 9 adds the cohort. Items 3, 4, 6 and 7 are reduced to class level and matched-feature counts. Item 13 adds the seven-child series to FT-110. | registry items 3 to 13 |
| XP-A | NARROW | ACCEPTED as the Orchestrator's consolidated sentence. A1 states the WWOX side and the binary-only comparison, and does not import A2's numbers. | README section 5 |
| XP-B | NARROW | ACCEPTED (as A1-D07 and A1-D08). | README lines 7 and 8 |
| XP-C | NARROW | ACCEPTED (as A1-D09). | README line 9 |
| XP-D | NARROW | ACCEPTED. "Compatible" is withdrawn: the unexposed children's dorsal pons and central-tegmental signal is not the exposed pair's globus pallidus and thalamus pattern, and "no vigabatrin" means absence from a drug column. The within-child comparison is not weakened. Added: Riva's vigabatrin-continued child also shows pons and dentate signal, timing unstated (audit A1-A1-18). | README line 6, section 9; A1-32, A1-54 role and imaging; `module_inputs.md` section 4 |
| XP-E | NARROW | ACCEPTED. A row is added to the identity table: the pair is probably inside the cohort and is not added to it. | README sections 6 and 8; A1-09, A1-10 |
| XP-F | NARROW | ACCEPTED. `source_depth` now uses only `partial_fulltext`, `abstract_only` and `reused_prior_reading FTR-20261003-40126049-01`; sections moved to the README table. | `cases_a1.tsv` all rows; README |
| Selection (review section 8) | — | ACCEPTED. The drug-name strings could not see reports whose abstracts name no drug. The seven-child series was read at abstract level (`FTR-20261106-42721537-21`), enters no count, and goes to FT-110. Possible overlaps with rows of this table are named. | README counter-evidence and section 8; `module_inputs.md` item 13 |
| Breakers (review section 6) | — | ACCEPTED: response quality and ascertainment are added. | README transfer section |
| Class-level redaction (review section 5) | — | ACCEPTED. Death ages and ages at last report are removed from `cases_a1.tsv`. Identity reasons now give matched-feature counts. The denominators notes carry genotype class only. | `cases_a1.tsv` A1-01, A1-04 to A1-07, A1-31, A1-54; denominators notes; README section 8 |

## Brief deviation, recorded

On 2026-11-05 the `paper_packet.py claim` markers for the re-opened held artefacts were written at 22:58Z, after several of those re-reads had begun. The brief requires a claim before opening. No other actor held a live claim on any of them. In the correction round both PMIDs were claimed before reading.

For PMID 42735667 the claim showed sb-b1 already on the paper. The Orchestrator's round message asked for this reading. It was done at abstract level only, and the receipt names sb-b1's staged receipt as `prior_receipt` (`new_question_outside_prior_coverage`), so the two must be recorded in event-id order, sb-b1's first.

## Counts re-derived (children)

* 41 children at row level; 38 with at least one of the four classes; 36 after the two possible-identity collapses.
* With both endpoints: 6. Of these, 4 discordant and 2 concordant non-responses.
* Per class (children with both endpoints):
    * vigabatrin 5 (4 discordant, 1 concordant);
    * hormonal 3 (2, 1);
    * ketogenic diet 2 (0, 2);
    * cannabidiol 1 (0, 1).
* Developmental outcome recorded: 6 in the four classes (was 7) and 5 for vigabatrin (was 6).
* other_context: 0 children with both endpoints (was 1).
* Row level: support 18, counter 16, context 23; concordance discordant 6, concordant 5, not_assessable 46.
