# A1: WWOX-DEE reports, intervention outcomes, denominators, and whether symptomatic and developmental outcomes move together

Scientist `sb-a1`, challenge `CH-SB-CONCORDANCE`, task `ORCH-SCIBATCH-DR-20261105` (part 1). Written 2026-11-05 from 22:35Z. Revised 2026-11-06 in the correction round after the blind quote audit (`verify/audit_A1/`) and the adversarial review (`verify/review_A/`). Every finding is answered in `RESPONSE.md`.
**Not medical advice.** This file gives no dose, schedule, route, preparation or clinical preference. Published cases appear only under the label their source prints, at genotype-class level. Children are counted once across reports.

## Answer first: the decision in 10 lines

1. **DATO.** Fourteen reports contribute rows:
   * 11 read here beyond the abstract at partial full-text depth (sections per source in the table below);
   * 2 read at abstract depth;
   * 1 assembled from an earlier reading's manifest.

   A twelfth partial full-text reading (PMID 30356099, a check of a supplementary table) contributes no row. Two more abstracts, read in the correction round, enter no count (PMIDs 42735667 and 42721537). The rows cover 36 to 38 distinct children who received at least one of the four classes. For 6 of them, both a symptomatic and a developmental outcome are recorded.
2. **DATO.** In 4 of those 6, development did not progress while seizures showed a partial, transient or clinically-only-defined improvement. Two of the four come from one report; the other two from one report each. In the other 2 of the 6, neither seizures nor development moved. No child achieved a sustained, instrumented response. One more vigabatrin-exposed child carries a printed status of "profound developmental delay and regression", not timed relative to the drug and coded `not_reported`. No child on any of the four classes is recorded with a developmental gain.
3. **INFERENZA.** Vigabatrin reaches the threshold of 5 children with both endpoints: 4 discordant, 1 concordant non-response. These are counts only, n is below 10. The five are not five independent vigabatrin observations:
   * three of them also supply the hormonal, ketogenic-diet and cannabidiol counts;
   * all five were on co-therapy;
   * in two, vigabatrin was given in sequence with another class.

   The assembly is not computable for hormonal therapy (3 of 11), the ketogenic diet (2 of 12) or cannabidiol (1 of 7 after de-duplication).
4. **DATO.** The five-patient series still does not state how many children went on the ketogenic diet. Table 1 records three responders (patients 1, 2 and 4) and no diet entry for patients 3 and 5. The narratives of patients 1 to 4 are on no surface an open route reaches.
5. **DATO.** Choi 2026 can be read only at abstract level. It reports 2 of 2 children on vigabatrin, both with the MRI change, in a report selected for the finding. It does not state age band, duration, genotype, or hormonal co-therapy at the time of the change, and the full text is not reachable by an open route. The same group's 64-child vigabatrin cohort (PMID 42735667, abstract level) gives the population figure the case report lacks: 18 of 64 imaged children developed the abnormality. In univariable analysis, concomitant prednisolone was associated with it (OR 4.07, 95% CI 1.22-17.3). The two children are probably inside that cohort (INFERENZA) and must not be added to it.
6. **INFERENZA.** C2 stays on both case series. BRIEF_A1 fixed this consequence in advance, and the H02 "human MRI denominators" line is now filled:
   * at abstract level: 2 of 2 exposed children with the change, in a report selected for the finding, so not a rate;
   * completed by the cohort: 18 of 64, with genetic aetiology in 9 of the 18.

   The denominator exists in the published record, not in the two-child report. Hormonal co-therapy at the MRI change is unknown in these two children but is measured as a risk factor in the cohort, so the H02 caveat names it as a confounder and gives its source. A brainstem or central-tegmental signal also appears in two children with no documented vigabatrin. It is not the globus-pallidus-and-thalamus pattern of the exposed pair, so it does not weaken that pair's within-child "new during treatment" comparison.
7. **DATO + INFERENZA.** Two children homozygous for the Q230P allele class have a documented ketogenic-diet exposure: one with no outcome attributable to the diet, one a non-response. CLAIM 042's revival trigger, "any documented diet exposure in a Q230P carrier", has therefore fired. It fires on a different allele configuration from the claim's own carrier, which is compound heterozygous with an exon-level deletion. The claim's statement about that carrier is unchanged; the new evidence bounds the homozygous class only.
8. **INFERENZA.** The five-patient series has two previously published children:
   * Patient 4: stated by the source.
   * Patient 2: not one of them. Its Table 1 credit is variant-level, and no column of the cited report's supplementary table carries patient 2's genotype (checked cell-wise).
   * Patient 3: most likely the other one. Patient 3 was a non-responder. It matches the first child of PMID 30361190 on five features including genotype class, onset band and two imaging features, and the two reports share co-authors (INFERENZA). A variant credit alone would not carry it, which is why the same kind of credit counts for patient 3 and not for patient 2.

   Pooled counts can therefore double-count patient 4 among responders and patient 3 among exposed children. CLAIM 042's "two of the three responders" is wider than its sources.
9. **DATO → INFERENZA.** The same Discussion that carries CLAIM 031's qualifier attaches the improvement of epileptic activity to the first child as an example ("e.g. in the first child"), and both narratives record profound delay. The better of the two readings is therefore that "in some of these cases" scopes the achievement of better control, not the developmental failure. This is not a resolution. The referent of "these cases" is not shown to be limited to the report's two children. If it ranges over the cases the Discussion reviews, neither scoping concerns them.
10. **IPOTESI.** In null and splice WWOX-DEE, symptomatic response does not predict developmental gain. The published record cannot yet test this, because no child in it achieved a sustained, instrumented response. What it records is that partial and transient responses were not followed by a gain. Test: a series with a dated developmental instrument before and after a sustained response; one responder with a measured gain falsifies the hypothesis. The only recorded gains in the read set are a one-time status, not attributed to treatment, in a homozygous missense child on two other drugs, outside the four classes (row A1-32).

## Files in this directory

| File | What it is |
|---|---|
| `cases_a1.tsv` | 57 rows × 18 columns, one row per child per intervention class, columns as the brief orders them plus `same_patient_as` |
| `denominators_a1.tsv` | 33 rows × 14 columns: per class and source, then pooled per class and pooled per child |
| `queries.tsv` | 32 rows: every search, fetch and screen, with time and hits |
| `module_inputs.md` | contributions in the vocabulary of `needs.json`, `work_order.json`, `ranking.json` (INV-10), card H02, the early cards and `vigabatrin_sources_resolved.tsv`, plus `proposed_registry_changes` |
| `RESPONSE.md` | the author response to every audit triple and review statement |
| `receipts/` | 16 staged receipts (suffix 21) and `receipts/INDEX.tsv` |

## Sources and depth

`source_depth` in `cases_a1.tsv` uses only `partial_fulltext`, `abstract_only` and `reused_prior_reading FTR-...`. The sections read are listed here.

| Source | Depth | Sections read | Rows |
|---|---|---|---|
| PMID 30361190 (Shaukat 2018) | partial_fulltext | Results (both children), Discussion, Table 1 This-study columns (page render) | A1-01 to A1-03 |
| PMID 36537114 (Chong 2023) | partial_fulltext | delivered chunks 0, 1, 2, 18, 22 to 25: abstract, introduction, part of the methods including part of the patient 5 narrative, Table 1, part of the discussion | A1-04 to A1-08 |
| PMID 41442931 (Choi 2026) | abstract_only | abstract | A1-09, A1-10 |
| PMID 37583270 (Nagarajan 2023) | partial_fulltext | Tables 1 and 4, WWOX rows and abbreviations | A1-11 to A1-16 |
| PMID 39101447 (You 2024) | partial_fulltext | Results, clinical manifestations, with the Figure 1 caption | A1-17 |
| PMID 35573960 (Riva 2022) | partial_fulltext | Results, clinical features | A1-18 to A1-21 |
| PMID 42092735 (Serce Pehlevan 2026) | partial_fulltext | case presentation | A1-22, A1-23 |
| PMID 28721938 (Tarta-Arsene 2017) | partial_fulltext | case study | A1-24, A1-25 |
| PMID 29808465 (Johannsen 2018) | partial_fulltext | Results, patient data | A1-26 |
| PMID 30061856 (Ko 2018) | partial_fulltext | abstract, methods, results, Table 3, supplementary table | A1-27 |
| PMID 38407561 (Nishino 2024) | abstract_only | abstract | A1-28 |
| PMID 35792847 (Al Baradie 2022) | partial_fulltext | Results narratives, Tables 1 to 3, one Discussion paragraph | A1-29 to A1-35 |
| PMID 36779245 (Oliver 2023) | partial_fulltext | Tables 1 and 2, Results paragraphs on drugs and development | A1-36 to A1-54 |
| PMID 40126049 (Cerulli Irelli 2025) | reused_prior_reading FTR-20261003-40126049-01 | from that reading's manifest; not re-read | A1-55 to A1-57 |
| PMID 30356099 (Piard 2019) | partial_fulltext | Supplementary Table 1 | none |
| PMID 42735667 (64-child vigabatrin cohort) | abstract_only | abstract; builds on the staged abstract receipt of package B1 | none |
| PMID 42721537 (seven-child WOREE series) | abstract_only | abstract; for the full-text queue | none |

## Coding rules (read before the tables)

* **genotype_class**:
    * `missense`: at least one allele is missense as printed.
    * `splice`: at least one allele sits at a splice site or in a splice region, and none is missense.
    * `null/null`: both alleles are nonsense, frameshift, or an exon-level deletion or duplication.
    * `other`: no genotype printed.

    Oliver 2023 classes its patient 13 as null/null; this table codes it `splice`.
* **symptomatic_outcome**: `resolved` is used when the source says seizures stopped, were controlled, or were absent, with no contrary EEG statement. "Controlled" is coded `resolved` but is not a statement of seizure freedom. `partial` is the floor for a criterion response without stated seizure freedom. `none` is a non-response, including "below criterion".
* **developmental_outcome**: coded only from a statement about development across or after the intervention, such as "remained", "no milestones achieved" or "failed to develop". A single status label or a one-time status, with no timing relative to the intervention, is coded `not_reported`, and the status is quoted in `developmental_instrument`. This follows the brief's rule not to infer an outcome from a diagnosis label.
* **concordance**:
    * `discordant`: the symptom resolved or was partial, and development was unchanged or regressed.
    * `concordant`: both improved, or the symptom was none and development unchanged.
    * `not_assessable`: either endpoint is `not_reported`.
* **role**:
    * `support`: a recorded symptomatic benefit of the class.
    * `counter`: the null, or the adverse finding (VABAM, or a brainstem signal without documented exposure).
    * `context`: exposure only, co-therapy, a status, or an overlap row.
* **same_patient_as**: a row id means the same child in the same report (stated). `possible: <reason>` means an identity that no text states. In pooled figures a possible identity counts once, the lower count.
* **locator_quote**: section, a colon, then the verbatim quote, at most 25 words. `[...]` marks text omitted inside the same passage.

## Evidence by theme

### 1. Vigabatrin: 22 exposures in 10 reports, 21 after de-duplication

* **DATO.** A symptomatic outcome is stated for 11 exposures: 8 responses and 3 non-responses.
    * Responses: Shaukat 2018, both children (A1-02, A1-03); Nagarajan 2023 row 37, after failed hormonal therapy (A1-12); You 2024, partial (A1-17); Al Baradie 2022 patients 2.1, 2.2 and 6 (A1-29, A1-30, A1-34); Tarta-Arsene 2017, one month of control, then relapse (A1-24).
    * Non-responses: patient 5 of the five-patient series, at regimen level (A1-08); Riva 2022 (A1-18); Serce Pehlevan 2026 (A1-22, clinical report, with no EEG tied to the vigabatrin step).
    * Not stated: Choi 2026 (2 children), Oliver 2023 (8), and Al Baradie patient 5, whose printed status of profound delay and regression is not timed relative to the drug (A1-33).
* **DATO.** Every response is qualified:
    * Shaukat 2018's own Table 1 codes case 1 *Partial* (3 drugs) and case 2 *Poor* (4 drugs). The first child's "the spasms resolved" continues "however, he soon developed other seizure types".
    * You 2024: "no visible seizures", while video-EEG at 11 months still recorded attacks and spasms.
    * Al Baradie 2.1: the follow-up EEG captured myoclonic seizures.
    * Tarta-Arsene: one month of control, then relapse.
* **DATO.** The five-patient series mentions vigabatrin once, for patient 5, and only as part of a three-drug regimen. CLAIM 001's pairing of vigabatrin with the diet has no support in the delivered text.

### 2. Hormonal therapy: 11 exposures in 6 reports

* **DATO.** 3 responses:
    * Shaukat first child, partial on prednisolone (A1-01).
    * Nagarajan row 38, responded then relapsed (A1-13).
    * Tarta-Arsene, complete clinical control with fragmented sleep hypsarrhythmia persisting; seizures returned later (A1-25).
* **DATO.** 5 non-responses: Nagarajan rows 37, 39 and 40 (row 39's outcome cell is self-contradictory); Riva 2022; Nishino 2024 (abstract level).
* **DATO.** 3 not stated: Oliver 2023. Its running text names two treated patients; its Table 2 lists three. The rows follow the table.

### 3. Ketogenic diet: 12 exposures in 7 reports, 3 of them a minimum count

* **DATO.** 5 responses:
    * five-patient series patients 1, 2 and 4, clinician-reported (A1-04, A1-05, A1-07);
    * Al Baradie 3.1, "responded well" (A1-31);
    * Ko 2018, WWOX n = 1, at least a 90 percent reduction at 3, 6 and 12 months, a source the module did not hold (A1-27).
* **DATO.** 3 non-responses: Nagarajan row 40 (A1-16), Riva 2022 (A1-21), Johannsen 2018 patient 2 (A1-26).
* **DATO.** 4 not stated:
    * Oliver 2023: 3 started; only patient 12 continued.
    * Al Baradie patient 6: the diet started after vigabatrin had controlled the seizures. At the last visit he was seizure-free for about nine months; the regimen was not restated, and weaning off the diet was under consideration (A1-35).
* **DATO.** No diet responder in any report has a developmental outcome recorded.

### 4. Cannabidiol: 8 exposures in 3 reports, 7 after de-duplication

* **DATO.**
    * Riva 2022: "CBD oil" ineffective and absent from the current regimen (A1-19).
    * Oliver 2023: four of four continued it; continuation is not efficacy.
    * Cerulli Irelli 2025 (from the earlier manifest): 2 of 3 WWOX patients were at least 50 percent responders, and the third was below criterion. Adjunctive status is not stated for these patients. CGI-I is a global impression, not a developmental measure.

### 5. The INV-10 assembly

| Child (row) | Class | Symptom, with its qualifier | Development, as printed | Result |
|---|---|---|---|---|
| Shaukat 2018, first child (A1-01, A1-02) | prednisolone, then vigabatrin | partial, then spasms resolved; other seizure types followed; overall Table 1 code Partial | severe delay before treatment; "remained profoundly delayed" at 2 years | discordant |
| Shaukat 2018, second child (A1-03) | vigabatrin | partial; overall Table 1 code Poor | no milestones before vigabatrin; profound delay at 11 months | discordant |
| You 2024 (A1-17) | vigabatrin | no visible seizures; electrographic attacks persisting | expected milestones not reached after 8 months | discordant |
| Tarta-Arsene 2017 (A1-24, A1-25) | vigabatrin, then ACTH | one month of control, then complete clinical control; seizures later returned | "no motor or cognitive development was identified" | discordant |
| Riva 2022 (A1-18 to A1-21) | four classes | none | "No developmental milestones were achieved." | concordant |
| Johannsen 2018 patient 2 (A1-26) | ketogenic diet | none | "failed to develop any motor or language skills" | concordant |

* **DATO.** Every developmental statement is a clinician narrative without a scale. Where timing is printed (4 children), follow-up after the intervention runs from about 5 months to about 2.5 years.
* **INFERENZA.** The record contains no sustained, instrumented responder. It can therefore show only that partial and transient responses were not followed by a gain. It cannot show what a sustained response predicts.
* **Cross-package note (review point XP-A).** The pattern matches the genetic and structural DEE baseline that package A2 assembles. The comparison holds only as a binary, because no WWOX developmental statement uses a scale and no WWOX rate is computable. The consolidated sentence belongs to the Orchestrator.

### 6. Choi 2026 and the 64-child cohort (PMID 42735667): what the cohort does to the two-child report

* **DATO (cohort abstract).** A retrospective single-institution cohort of children treated with vigabatrin. Inclusion required at least two brain MRI examinations before and during treatment. 18 of 64 (28.1%) developed the abnormality. Concomitant prednisolone was associated with it in univariable analysis (OR 4.07, 95% CI 1.22-17.3). Genetic epilepsy accounted for 9 of the 18 positives. The authors call the aetiology findings hypothesis-generating.
* **INFERENZA (strong; not stated in either abstract).** The two WWOX children of Choi 2026 are probably among the cohort's 18. Five features point the same way: the same first author, two shared co-authors, one institution, the same two-scan design, and an intake window that ends before the case report.
* **Consequences.**
    * The two children must not be added to the 18.
    * 18 of 64 is the population rate of the abnormality in imaged, vigabatrin-treated children of mixed aetiology at that centre. It is not a WWOX rate.
    * The hormonal association is measured in the cohort, not in the two children. For them, co-therapy remains unknown and is named as a confounder.
    * Neither abstract places the two WWOX children above or below 18 of 64.
* **Overlap with package B1.** Package B1 holds a staged abstract receipt for the same cohort, `FTR-20261105-42735667-23`. This package's receipt builds on it.

### 7. CLAIM 031's qualifier: the better-supported reading, not a resolution

* **DATO.** The Discussion has two sentences on this. The qualifier sentence: "...did not improve with achievement of better control of epileptic activity in some of these cases". The example sentence: "...despite improvement of epileptic activity (e.g. in the first child)". Both narratives record profound delay.
* **INFERENZA.** The better reading scopes the qualifier to the achievement of better control. The residual ambiguity is the referent of "these cases", which may range over the cases the Discussion reviews.
* **DATO.** Whether impairment "preceded the onset" is not cleanly shown for either child. The first child had early neurological concerns, and also early jerks and stiffening episodes before the EEG.
* **DATO (abstract level, not counted).** The seven-child series reports "Developmental delay was evident from birth" in all seven. This supports that premise of CLAIM 031 independently.

### 8. Patient identity across reports (identity verdicts kept; descriptors at class level)

| Pair | Evidence | Status |
|---|---|---|
| five-patient series patient 3 (A1-06) = Shaukat 2018 first child (A1-01) | five matched features including genotype class, onset band and two imaging features; shared co-authors; the Table 1 credit of the variant to that report | INFERENZA, strong; counted once |
| five-patient series patient 4 (A1-07) = an earlier CNV report | stated by the source | DATO; that report has no row here |
| five-patient series patient 2 (A1-05) vs Piard 2019 | no column of that report's Supplementary Table 1 carries patient 2's homozygous exon-level deletion | variant-level credit; no identity |
| Choi 2026 pair (A1-09, A1-10) vs five-patient series patient 5 (A1-08) | both vigabatrin-exposed; both reports come from the same national setting; the abstract prints no genotype, sex or age | possible; the three counted as 2 |
| Choi 2026 pair vs the 64-child cohort (PMID 42735667) | five converging features (section 6) | INFERENZA, strong; the pair is not added to the cohort |
| Riva 2022 (A1-18) vs the 27-centre series (A1-57) | shared authors; preparations differ | possible; counted once |
| seven-child series (PMID 42721537) vs five-patient series patients 1 and 2, and vs the 27-centre series | patient 1 carries the series' recurrent allele as one of two alleles; a co-author of the five-patient series works in the same national setting; shared authors with the 27-centre series | possible; to be resolved when it is read; it enters no count |
| Tarta-Arsene 2017 (A1-24) = Piard 2019 patient 8 | module record `CC-20261003W4-A-PATIENT-OVERLAP-01` | possible; no double count, because Piard has no treatment row |
| Al Baradie 2.1 and 2.2 = an earlier sibship report | module record `CC-20261003W5-B-PATIENT-OVERLAP-01` | possible; no double count |
| Nagarajan 2023 row 40 vs Piard 2019 patients 13 and 14 | sex and age at last follow-up exclude both candidates | INFERENZA: three distinct children |

### 9. Imaging context for H02 and the white-matter package (location matters)

* **DATO.** In the two children with no vigabatrin in their drug column (absence of report, not demonstrated absence of exposure):
    * Oliver 2023 patient 5: increased T2 in the dorsal pons (A1-54).
    * Al Baradie 2022 patient 4: bilateral central tegmental tract T2/FLAIR/DWI signal (A1-32).

    Neither shows the globus-pallidus-and-thalamus pattern reported in the exposed pair.
* **DATO.** In vigabatrin-exposed children, with timing relative to exposure not stated:
    * Oliver patients 1, 3, 6, 7, 8 and 10: brainstem, central-tegmental, midbrain, globus-pallidus or dentate signal.
    * Riva 2022's child: pons and dentate signal at 2 years 4 months, while vigabatrin was continued. The authors do not discuss it as drug-related.
* **INFERENZA.** This background rules out any cross-sectional attribution of a brainstem finding to vigabatrin, and rules out reading a rate from the exposed pair. It does not weaken that pair's within-child "new during treatment" comparison. "Compatible" (the first wording) overstated the match.

## Counter-evidence searched on purpose

* **Null.** 13 non-response rows: A1-08, A1-11, A1-14, A1-15, A1-16, A1-18 to A1-22, A1-26, A1-28, A1-57.
* **Adverse.** The Choi pair (A1-09, A1-10) and the brainstem signal without documented exposure (A1-54).
* **Context where the separation may fail.** A one-time status with recent gains in a missense-class child outside the four classes (A1-32).
* **Not found.** A report with a developmental gain after any of the four classes. Bounded statement: not found after queries Q01 to Q12 (2026-11-05), the screening in Q14, the repository manifests, and the correction-round abstracts.
* **Selection hole (review section 8).** Every one of the twelve strings carries a drug name, so a report whose abstract names no drug is invisible to them. The seven-child series is such a report. It is held at abstract level and is not counted. If read, it could add up to seven children, which would move the pattern toward concordant non-response.

## Transfer conditions and transfer breakers

* **Condition.** Every child with both endpoints has a null or splice genotype class, except one homozygous missense child, who is a non-responder.
* **Breaker, response quality.** No response in the set is sustained or instrumented.
* **Breaker, ascertainment.** Every report was selected for publication. The population-like cohort reads at abstract level only.
* **Breaker, allele class.** The only recorded gains are in a missense-class child, and only as a status.
* **Breaker, instrument.** Every developmental statement is a clinician narrative. An absence of recorded gain is not a measured absence of change.
* **Breaker, timing.** Follow-up is short where it is dated (4 children) and undated in two.
* **Breaker, co-therapy.** No class was given alone, and two children received two classes in sequence.

## What is not established

* A response rate for any class.
* What a sustained response predicts.
* Hormonal co-therapy in the Choi pair.
* Any diet effect in the compound-heterozygous configuration that CLAIM 042 names.
* Whether the seven-child series overlaps rows of this table.

## What was not reachable (zero spend, open routes only)

* Choi 2026 full text: no PMCID, publisher HTTP 403.
* Chong 2023 narratives of patients 1 to 4.
* Gao 2025: no open route, no held artefact.
* Nishino 2024 full text.
* Full texts of PMID 42735667 and PMID 42721537: Europe PMC subscription only, no PMCID (checked 2026-11-06).
* Unscreened records: 13 open-access texts (HTTP 500), 12 abstract books, and 5 PMC records that refuse XML download.
* Ben-Salem 2015 and Ehaideb 2018: not read (cap of 12 full texts).

## Queries run

The full list is in `queries.tsv`.

| Route | Strings | Date (UTC) | Hits |
|---|---|---|---|
| PubMed (E-utilities) | `WWOX AND (epilep* OR encephalopath* OR WOREE OR SCAR12)` AND each of vigabatrin, ketogenic, ACTH, (corticosteroid OR prednisolone), cannabidiol, hormonal | 2026-11-05T22:39Z | 2, 1, 1, 0, 0, 2 |
| Europe PMC REST | same six strings | 2026-11-05T22:39Z | 41, 52, 38, 29, 28, 44 |
| Europe PMC fullTextXML screen | 63 open-access records and 14 abstract books | 2026-11-05T22:45Z to 22:47Z | 48 and 2 retrieved |
| Full-text routes for Choi 2026 and Chong 2023 | PubMed idconv, Europe PMC core, publisher pages | 2026-11-05T22:38Z | no open copy |
| Correction round | PubMed metadata and Europe PMC core for PMIDs 42735667 and 42721537 | 2026-11-06T07:10Z | 2 abstracts; no open full text |

## Against the sentences the brief quotes

* **INV-10, "what the published symptomatic response predicts about development".**
    * *Supports* only this: partial and transient responses were not followed by a gain in 4 children (3 reports), and non-response in 2 was not followed by a loss.
    * *Narrows* the question: it cannot be answered for a sustained response, which no child achieved.
    * No report *contradicts* it.
* **CLAIM 031.**
    * *Supported* by 4 discordant children in 3 reports.
    * *Narrowed*: the qualifier reading is the better of two, not resolved; the title's universal reaches past the record.
    * *Context*: a missense-class status outside the four classes.
* **CLAIM 042.**
    * *Supported*: the denominator is not stated (minimum 3).
    * *Narrowed and updated*: the overlap sentence, and the revival trigger on the homozygous configuration (decision lines 7 and 8).

## What this package did not do

* It recorded no receipt and committed nothing.
* It wrote only inside this directory, apart from the reading-claim markers that `paper_packet.py claim` writes in the shared git directory.
* It contacted no author and no service that requires a contact address.
* **Brief deviation, recorded honestly.** On 2026-11-05 the `paper_packet.py claim` calls for the re-opened held artefacts were made at 22:58Z, after several of those re-reads had begun, rather than before opening. No other actor held a live claim on any of them. In the correction round both PMIDs were claimed before reading. The claim on 42735667 showed a claim by sb-b1, and this package's receipt builds on sb-b1's staged receipt.
* Cerulli Irelli 2025 was used from its manifest only. Gao 2025, Ben-Salem 2015 and Ehaideb 2018 were not read.
