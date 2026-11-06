# A1: WWOX-DEE reports, intervention outcomes, denominators, and whether symptomatic and developmental outcomes move together

Scientist `sb-a1`, challenge `CH-SB-CONCORDANCE`, task `ORCH-SCIBATCH-DR-20261105` (part 1). Written 2026-11-05 from 22:35Z; last edited 23:32Z.
**Not medical advice.** This file gives no dose, schedule, route, preparation or clinical preference. Published cases appear only under the label their source prints, at genotype-class level. Children are counted once across reports.

## Answer first: the decision in 10 lines

1. **DATO.** Fourteen reports contribute rows: 11 read in full text here (question-directed re-reads of held artefacts, and one first read), 2 at abstract depth, 1 assembled from an earlier reading's manifest. A twelfth full text was read and contributes no row. Between them, 36 to 38 distinct children received at least one of the four classes. A symptomatic outcome and a developmental outcome are both recorded for 6 of them.
2. **DATO.** In 4 of those 6, seizures resolved or improved while development did not progress (Shaukat 2018 both children, You 2024, Tarta-Arsene 2017). In the other 2, neither moved (Riva 2022; Johannsen 2018 patient 2). No child on any of the four classes is recorded with a developmental gain.
3. **INFERENZA.** Vigabatrin meets the threshold of 5: 5 children have both endpoints, 4 discordant and 1 a concordant non-response (counts only, n below 10). The assembly is not computable for hormonal therapy (3 of 11), the ketogenic diet (2 of 12) or cannabidiol (1 of 7 after de-duplication).
4. **DATO.** The five-patient series still does not state how many children went on the ketogenic diet. Table 1 records three responders (patients 1, 2 and 4) and no diet entry for patients 3 and 5. The narratives of patients 1 to 4 are on no surface an open route reaches.
5. **DATO.** Choi 2026 states exposure only at abstract level: 2 of 2 children on vigabatrin, both with the MRI change. Age band, duration and hormonal co-therapy at the time of the change are not stated. The full text is not reachable (publisher HTTP 403, no PMC record, Europe PMC marks it subscription only).
6. **INFERENZA.** C2 therefore stays on both case series. The H02 "human MRI denominators" line cannot be filled. Hormonal co-therapy at the MRI change stays *unknown*, not absent.
7. **DATO + INFERENZA.** Two homozygous Q230P children have a documented ketogenic-diet exposure: Al Baradie 2022 patient 6 (no outcome attributable to the diet) and Johannsen 2018 patient 2 (no response). CLAIM 042's revival trigger, "any documented diet exposure in a Q230P carrier", has fired.
8. **INFERENZA.** In the five-patient series, the two previously published children are most likely patient 4 (the source says so) and patient 3, who matches Shaukat 2018's first child on genotype, sex, onset, MRI and optic atrophy, and whose report shares co-authors with it. Patient 2's "Piard et al. (2019)" credit matches no child in that cohort's Supplementary Table 1. CLAIM 042's "two of the three responders" is therefore wider than its sources.
9. **DATO → INFERENZA.** The same Discussion that carries CLAIM 031's qualifier attaches the seizure improvement to the first child ("e.g. in the first child"). Both narratives record profound delay. Read together, "in some of these cases" scopes the achievement of better control, not the developmental failure.
10. **IPOTESI.** In null and splice WWOX-DEE, symptomatic response does not predict developmental gain. Test: a series with a dated developmental instrument before and after each intervention; one responder with a measured gain falsifies it. The only gain in the read set is a homozygous P47T child on levetiracetam and topiramate, outside the four classes (row A1-32).

## Files in this directory

| File | What it is |
|---|---|
| `cases_a1.tsv` | 57 rows, 18 columns, one row per child per intervention class, in the column order of the brief plus `same_patient_as` |
| `denominators_a1.tsv` | 33 rows, 14 columns: per class and source, then pooled per class and pooled per child |
| `queries.tsv` | 29 rows: every search, fetch and screen, with time and hits |
| `module_inputs.md` | proposals in the vocabulary of `needs.json`, `work_order.json`, `ranking.json` (INV-10), the early cards and `vigabatrin_sources_resolved.tsv`, plus `proposed_registry_changes` |
| `receipts/` | 14 staged receipts (suffix 21) and `receipts/INDEX.tsv` |

## Coding rules (read these before reading the tables)

* **genotype_class**: `missense` if at least one allele is missense as printed. `splice` if at least one allele sits at a splice site or in a splice region and none is missense. `null/null` if both alleles are nonsense, frameshift or exon-level deletion or duplication. `other` if no genotype is printed. Oliver 2023 classes its patient 13 (a homozygous deletion that removes the +2 donor base) as null/null; this table codes it `splice`.
* **developmental_outcome** is coded from a statement about development across or after the intervention: a gain, a loss, "remained", "no milestones achieved", "failed to develop". A single status label with no timing relative to the intervention is coded `not_reported`, and the label is quoted in `developmental_instrument` as "status label only". Example: Table 1 of the five-patient series prints "Profound developmental delay" once per child. This follows the brief's rule not to infer an outcome from a diagnosis label. Because of it, the five-patient series contributes no developmental outcome.
* **concordance**: `discordant` = symptom resolved or partial, and development unchanged or regressed. `concordant` = both improved, or symptom none and development unchanged. `not_assessable` = either endpoint `not_reported`.
* **role**: `support` = the row records a symptomatic benefit of the class (including discordant pairs). `counter` = the null (no response), the adverse (VABAM), or developmental gain alongside seizure control. `context` = exposure only, co-therapy, or an overlap row.
* **same_patient_as**: a row id for the same child in the same report (stated); `possible: <reason>` for an identity that neither text states, including identities with reports that have no row here; `none_known` otherwise. In pooled figures, a possible identity counts once, the lower count (coordinator's rule).
* **locator_quote**: the section, a colon, then the verbatim quote in double quotes, at most 25 words. `[...]` marks text omitted inside the same passage. Every quote was string-checked against the artefact it names (scratch check, NFKC and hyphen-normalised). The field never starts with a quote character, so CSV readers keep the quote marks.

## Evidence by theme

### 1. Vigabatrin: 22 exposures in 10 reports, 21 after de-duplication

* **DATO.** A symptomatic outcome is stated for 11 exposures: 8 responses, 3 non-responses.
    * Responses: Shaukat 2018 both children (A1-02, A1-03); Nagarajan 2023 row 37 after failed hormonal therapy (A1-12); You 2024, partial (A1-17); Al Baradie 2022 patients 2.1, 2.2 and 6 (A1-29, A1-30, A1-34); Tarta-Arsene 2017, one month, then relapse (A1-24).
    * Non-responses: the five-patient series patient 5, at regimen level (A1-08); Riva 2022 (A1-18); Serce Pehlevan 2026 (A1-22).
    * Not stated for 11: Choi 2026 (2), Oliver 2023 (8: 7 of 10 children with spasms plus patient 6), Al Baradie patient 5.
* **DATO.** Shaukat 2018's own Table 1 codes the overall antiseizure-drug response of case 1 as *Partial* (3 drugs) and of case 2 as *Poor* (4 drugs). This was read on a page render of the rotated table, page 9. So "the spasms resolved" (CLAIM 001) is the narrative's spasm-specific statement, and the table is less favourable.
* **DATO.** You 2024: "no visible seizures" at 13 months, while video-EEG at 11 months still recorded electrical attacks and spasms. Al Baradie patient 2.1: "effectively controlled", while the follow-up EEG captured myoclonic seizures. Both are coded `partial`.
* **DATO.** In the five-patient series the delivered text mentions vigabatrin once: patient 5, "poorly controlled with clobazam, vigabatrin, and zonisamide". CLAIM 001's "un caso resistente al vigabatrin, uno migliora in combinazione con KD" is wider than this. No delivered sentence pairs vigabatrin with the diet.

### 2. Hormonal therapy (ACTH, prednisolone, unnamed "hormonal therapy"): 11 exposures in 6 reports

* **DATO.** 3 responses:
    * Shaukat first child, partial on prednisolone (A1-01).
    * Nagarajan row 38, responded then relapsed (A1-13).
    * Tarta-Arsene, complete clinical control on ACTH added to two drugs, with fragmented hypsarrhythmia persisting in sleep (A1-25).
* **DATO.** 5 non-responses: Nagarajan rows 37, 39 and 40 (initial hormonal therapy failed); Riva 2022 ("three cycles of ACTH had very poor results"); Nishino 2024 (abstract only).
* **DATO.** Outcome not stated for 3: Oliver 2023. Oliver's text names two hormonally treated patients (2 and 11), while its Table 2 lists three (it adds prednisolone and ACTH for patient 7).

### 3. Ketogenic diet: 12 exposures in 7 reports (3 of them a minimum count)

* **DATO.** 5 responses:
    * Five-patient series patients 1, 2 and 4: clinician-reported, no count (A1-04, A1-05, A1-07).
    * Al Baradie 3.1, "responded well", later non-convulsive status during sepsis (A1-31).
    * Ko 2018, WWOX n = 1, a responder (at least 90 percent reduction) at 3, 6 and 12 months (A1-27). This is a source the module did not hold.
* **DATO.** 3 non-responses: Nagarajan row 40 (A1-16); Riva 2022, "did not significantly improve seizures and was suspended" (A1-21); Johannsen 2018 patient 2 (A1-26).
* **DATO.** Not stated for 4:
    * Oliver 2023: 3 started, only patient 12 continued.
    * Al Baradie patient 6: the diet was started at 11 months, after vigabatrin had controlled the seizures. He was still on it, seizure-free for about nine months, with breakthrough seizures during febrile illness. No outcome is attributable to the diet.
* **DATO.** The five-patient series denominator stays unstated, and 3 is a minimum. Table 1 records "Responded to ketogenic diet" in three columns and nothing about the diet in the columns of patients 3 and 5. The delivered narrative of patient 5 does not mention the diet. Patients 1 to 4 have no delivered narrative.
* **DATO.** No diet responder in any report has a developmental outcome recorded. Both children with both endpoints are concordant non-responses.

### 4. Cannabidiol: 8 exposures in 3 reports, 7 after de-duplication

* **DATO.**
    * Riva 2022: "CBD oil" ineffective and not among the current drugs (A1-19).
    * Oliver 2023: "all four patients who had cannabidiol continued that ASM". Continuation is not an efficacy measure.
    * Cerulli Irelli 2025, a 27-centre series, Table 2, from the earlier manifest: 2 of 3 WWOX patients were at least 50 percent responders; mean reduction 41.7 (SD 38.2); CGI-I improved 2 of 3. CGI-I is a global impression, not a developmental measure.
* **INFERENZA.** The printed mean and SD are reproduced exactly by reductions of 50, 75 and 0 percent. The mean alone bounds the non-responder's reduction at about 25 percent or less. The supplement's worsening list excludes WWOX, so the non-responder is coded `none` (A1-57).

### 5. The INV-10 assembly: do symptomatic and developmental outcomes move together?

| Child (row) | Class | Symptom | Development (as printed) | Result |
|---|---|---|---|---|
| Shaukat 2018, first child (A1-01, A1-02) | prednisolone, then vigabatrin | partial, then spasms resolved | severe delay at 6 months; "remained profoundly delayed" at 2 years | discordant |
| Shaukat 2018, second child (A1-03) | vigabatrin | partial | no milestones at 4 months; profound delay at 11 months | discordant |
| You 2024 (A1-17) | vigabatrin | visible seizures gone, electrographic persisting | expected milestones not reached after 8 months | discordant |
| Tarta-Arsene 2017 (A1-24, A1-25) | vigabatrin, then ACTH | one month of control, then complete clinical control | "no motor or cognitive development was identified" | discordant |
| Riva 2022 (A1-18 to A1-21) | vigabatrin, cannabidiol, ACTH, diet | none | "No developmental milestones were achieved." | concordant (neither moved) |
| Johannsen 2018 patient 2 (A1-26) | ketogenic diet | none | "failed to develop any motor or language skills" | concordant (neither moved) |

* **DATO.** Development is described as severely impaired at the last report in all six, and in none is a gain recorded after the intervention. For You 2024 the narrative records slight motor progress before 8 months and none after. Every developmental instrument is a clinical narrative: no developmental scale, no score, no age-equivalent.
* **INFERENZA.** In this record a symptomatic response is not followed by developmental gain. A non-response is not followed by gain either. So response status carries no information about development in these six. Note: 6 children, 5 reports, null and splice genotypes except one homozygous Q230P child. Where the timing is printed (4 children), follow-up after the intervention runs from about 5 months to about 2.5 years. This is not a rate.
* **DATO (counter).** The only developmental gain in the read set: Al Baradie 2022 patient 4, homozygous P47T, seizures controlled on levetiracetam and topiramate, "recently started sitting alone, saying up to 10 single words" (A1-32). P47T is the allele the module associates with the ataxia phenotype. An earlier reading (manifest of PMID 39507621, not re-read) records a homozygous missense child who sat, crawled and walked with support while seven drugs gave no sustained effect.

### 6. Choi 2026: what is and is not stated (the H02 line)

* **DATO.** Abstract only. Two children with WWOX-related epileptic encephalopathy were on vigabatrin; brain MRI *during* treatment showed *new* symmetrical signal changes in the globus pallidi and thalami. Initial imaging showed periventricular white-matter volume loss and callosal atrophy. Presentation: microcephaly, hypertonia, dysphagia, profound global developmental delay, early infantile onset drug-resistant epilepsy.
* **Not stated:** age band at exposure, duration class, genotype, sex, any reversal, and whether hormonal therapy was co-administered when the MRI changed.
* **INFERENZA.** "New ... during vigabatrin treatment" is a within-child before-and-after comparison, so the change is anchored in time. The abstract gives no denominator of exposed WWOX children, so no rate can be read from it. That matches CLAIM 001's existing wave note.

### 7. CLAIM 031's qualifier, resolved from the source text

* **DATO.** Shaukat 2018, Discussion: "In support of this hypothesis is the fact that the cognitive and psychomotor impairment preceded the onset of epileptic encephalopathy and did not improve with achievement of better control of epileptic activity in some of these cases."
* **DATO.** In the same Discussion: "The developmental outcome was unfavourable with profound impairment despite improvement of epileptic activity (e.g. in the first child)."
* **DATO.** In the narratives, both children are profoundly delayed at the last description.
* **INFERENZA.** Read alone, the first sentence is syntactically ambiguous. The second sentence assigns the *improvement* to the first child as the example, and the narratives give the developmental failure for *both*. So "in some of these cases" restricts where better control was achieved; it does not restrict where development failed. Whether impairment "preceded the onset" is not cleanly shown for either child. The first child had neurological concerns soon after birth and severe global delay at six months, but also body jerks from five weeks and arm-stiffening episodes the parents had noticed months before the EEG at seven months. For the second child it is not shown, as CLAIM 031 already says.

### 8. Patient identity across reports (coordinator's addendum)

| Pair | Evidence | Status |
|---|---|---|
| Five-patient series patient 3 (A1-06) = Shaukat 2018 first child (A1-01) | same homozygous exon 3-4 deletion, and Table 1 credits the variant to Shaukat 2018; male; myoclonic onset at five weeks; periventricular cysts and thin corpus callosum; bilateral optic atrophy; three of the five 2018 authors are co-authors of the 2023 series | INFERENZA, strong; counted once |
| Five-patient series patient 4 (A1-07) = an earlier CNV report | the source states "published in figure S2; Dharmadhikari et al., 2019" | DATO; that report is not in this table |
| Five-patient series patient 2 (A1-05) vs Piard 2019 | no column of Piard Supplementary Table 1 carries a homozygous exon-7 deletion (read cell-wise; the exon-7 deletion occurs only compound heterozygous, in its patients 2 and 4) | the "Piard et al. (2019)" cell is a variant-level credit; no identity |
| Five-patient series patient 4 vs Piard 2019 | no Piard column carries the overlapping exon-6 and exons 6-8 deletion pair | variant-level credit only |
| Choi 2026 children (A1-09, A1-10) vs five-patient series patient 5 (A1-08) | both are vigabatrin-exposed children and both reports come from the same national setting; the abstract prints no genotype, sex or age; patient 5 has no microcephaly, while the Choi abstract lists microcephaly in its joint description | possible; the three counted as 2 |
| Riva 2022 (A1-18) vs the 27-centre cannabidiol series (A1-57) | the multicentre author list includes the 2022 report's group; the series admitted only highly purified CBD, while the 2022 report names "CBD oil" | possible; counted once |
| Tarta-Arsene 2017 (A1-24) = Piard 2019 patient 8 | module record `CC-20261003W4-A-PATIENT-OVERLAP-01` (blind audit 7 of 7 SUPPORTED) | possible; Piard has no treatment row, so nothing is double counted |
| Al Baradie 2022 patients 2.1 and 2.2 = an earlier sibship report (Ehaideb 2018) | module record `CC-20261003W5-B-PATIENT-OVERLAP-01` | possible; that report gives no treatment, so nothing is double counted |
| Nagarajan 2023 row 40 vs Piard 2019 patients 13 and 14 (all homozygous p.Arg264*) | row 40 is female, so it is not Piard 14 (male). Row 40 was 30 months old at last follow-up in a cohort tested January 2018 to June 2022, so it is not Piard 13, who was 8 years old at that report's last examination | INFERENZA: three distinct children, refining `CC-20261004W7-B-PATIENT-OVERLAP-01`'s "at most three, possibly two" |
| You 2024 child; Riva 2022 child | no other row carries their genotypes (homozygous c.172+1G>C; p.Arg264* with an exon-6 deletion) | none_known |
| Oliver 2023 cannabidiol patients 6, 9, 10, 11 vs the 27-centre series | Oliver's Table 1 places them in recruiting countries that are not among the series' centres | none_known |

### 9. Imaging context for H02 and the white-matter package

* **DATO.** VABAM-compatible locations are recorded in WWOX children with no documented vigabatrin:
    * Oliver 2023 patient 5, on valproate and levetiracetam only: increased T2 in the dorsal pons at 17 months (A1-54).
    * Al Baradie 2022 patient 4, no vigabatrin listed: bilateral central tegmental tract T2/FLAIR/DWI hyperintensity (A1-32).
* **DATO.** The same locations appear in vigabatrin-exposed children, with timing relative to exposure not stated: Oliver patients 1, 3, 6, 7, 8 and 10 (restricted diffusion in the dorsal pons, central tegmental tracts or posterior midbrain; increased T2 in the globus pallidus, brainstem or dentate nuclei).
* **INFERENZA.** In WWOX-DEE a deep grey or brainstem signal is not attributable to vigabatrin without a scan of the same structures before exposure. Choi 2026's "new ... during vigabatrin treatment" is that kind of comparison, at abstract level only. This mirrors the non-WWOX finding the module already holds (VABAM-like abnormalities in 7 of 52 unexposed children with tuberous sclerosis).

## Counter-evidence searched on purpose

For every benefit row, the same queries were used to look for the null, the adverse finding and the context where the reading fails.

* **Null.** 13 non-response rows across the four classes: A1-08, A1-11, A1-14, A1-15, A1-16, A1-18 to A1-22, A1-26, A1-28, A1-57.
* **Adverse.** The two Choi children with VABAM (A1-09, A1-10).
* **Context where the separation fails.** One developmental gain with seizure control, in a P47T homozygote outside the four classes (A1-32).
* **Not found.** No report with a developmental gain after any of the four classes. Bounded statement: not found after PubMed and Europe PMC queries Q01 to Q12 on 2026-11-05, the screening of 48 open-access texts (Q14), and the manifests of 25 already-read hit papers plus 56 treatment-bearing manifests repository-wide. Absence from this search is not absence from the literature: 13 open-access records and 12 abstract books could not be screened (Q14, Q15, Q17).

## Transfer conditions and transfer breakers

* **Condition.** Every child with both endpoints has a predicted null or splice genotype (Shaukat: homozygous exon deletion and homozygous canonical acceptor; You: homozygous donor; Tarta-Arsene: acceptor plus frameshift; Riva: nonsense plus exon deletion), except Johannsen patient 2 (homozygous Q230P, non-responder). The discordance therefore holds for the null and splice classes. For the Q230P-bearing class there is one concordant non-response and no responder with a developmental outcome.
* **Breaker.** Allele class. The one developmental gain is in a homozygous P47T child (A1-32), and the 2025 registry cohort (from its earlier manifest, not re-read) reports a registry biased toward living, possibly milder individuals. A residual-function allele may break the separation.
* **Breaker.** Instrument. Every developmental statement is a clinician narrative with no scale. A gain below the resolution of "profoundly delayed" would be invisible. An absence of recorded gain is not a measured absence of change.
* **Breaker.** Timing. Where the timing is printed (4 children), follow-up after the intervention runs from about 5 months to about 2.5 years. It is undated for Riva 2022 and Johannsen 2018. Nothing here speaks to later development.
* **Breaker.** Co-therapy. No intervention was given alone: every responder was on other drugs, and two had two classes in sequence (Shaukat first child, Tarta-Arsene). The concordance is about seizure control, not about one agent.

## What is not established

* A response rate for any class in WWOX-DEE. Every denominator is a case-level count from selected reports, and the five-patient series and Choi 2026 do not state theirs.
* Whether any symptomatic response changes development. No report pairs a dated developmental instrument with an intervention.
* Whether hormonal therapy was co-administered when the WWOX children's MRI changed (Choi 2026): unknown.
* Whether the diet does anything in a Q230P carrier. One exposure has no attributable outcome; one did not respond.
* Whether Choi 2026's children appear in other reports from the same national setting. Possible for one; not decidable from an abstract.

## What was not reachable (zero spend, open routes only)

* Choi 2026 full text: no PMCID, Europe PMC subscription only, publisher pages HTTP 403 (Q20 to Q22).
* Chong 2023 per-patient narratives of patients 1 to 4 (chunks 3 to 17): no PMC record, publisher HTTP 403. Only the delivered chunks held under `files/fulltext/` were read.
* Gao 2025 registry cohort (PMID 40875931): no PMCID and no held artefact. CLAIM 001's sentence about it rests on the 2026-08-04 reading and was not re-checked.
* Nishino 2024 full text: paywalled; abstract only.
* Unscreened records: 13 open-access full texts that Europe PMC refused (HTTP 500), 12 conference abstract books, and 5 PMC records that refuse XML download, among them PMID 29100083 (a de novo DEE cohort) and PMID 38605122. The PMC page of PMID 40811633 was screened through a model-summarised fetch only.
* Primary reports reachable only through secondary tables, not read (cap of 12 full texts): Ben-Salem 2015 (steroids with valproate, response "yes" in two curations) and Ehaideb 2018.

## Queries run

The full list, with times and hits, is in `queries.tsv`. Summary:

| Route | Strings | Date (UTC) | Hits |
|---|---|---|---|
| PubMed (E-utilities) | `WWOX AND (epilep* OR encephalopath* OR WOREE OR SCAR12)` AND each of vigabatrin, ketogenic, ACTH, (corticosteroid OR prednisolone), cannabidiol, hormonal | 2026-11-05T22:39Z | 2, 1, 1, 0, 0, 2 |
| Europe PMC REST (abstracts and open-access full text) | same six strings | 2026-11-05T22:39Z | 41, 52, 38, 29, 28, 44 (110 records; 88 PMIDs with PubMed) |
| Europe PMC fullTextXML screen | 63 open-access records and 14 abstract books | 2026-11-05T22:45Z to 22:47Z | 48 and 2 retrieved; 2 patient-level WWOX treatment hits |
| Full-text routes for Choi 2026 and Chong 2023 | PubMed idconv, Europe PMC core, three publisher pages | 2026-11-05T22:38Z | no open copy |

## Against the sentences the brief quotes

* **INV-10, "what the published symptomatic response predicts about development".** *Supports* a narrowly worded answer: in 6 children with both endpoints, a response did not predict a gain and a non-response did not predict a loss. *Narrows* it to null and splice genotypes, clinical narrative instruments, and short or undated follow-up. No report *contradicts* it within the four classes.
* **CLAIM 031, "seizure control does not rescue development", with the qualifier "in some of these cases".** *Supported* by 4 discordant children in 3 reports, not 2 children in 1 report. *Narrowed*: the qualifier scopes the seizure control, the evidence is clinical narrative, and genotype is a breaker. *Contradicted* only outside the four classes and in a milder allele class (A1-32).
* **CLAIM 042, "the number of patients exposed is not stated".** *Supported*: still not stated, minimum 3. Its patient-overlap sentence and its "no Q230P carrier ... nothing transfers" boundary are *narrowed and updated* (decision lines 7 and 8; `module_inputs.md`).

## What this package did not do

* It recorded no receipt and committed nothing. It edited no file outside this directory, except the reading-claim markers that `paper_packet.py claim` writes in the shared git directory as the brief instructs. It contacted no author and no service requiring a contact address.
* Claims through `paper_packet.py claim` for the re-opened held artefacts were made at 22:58Z, after several of those re-reads had started, rather than before opening. No other actor held a live claim on any of them.
* Cerulli Irelli 2025 (PMID 40126049) was used from its manifest only and was not re-read. It has no new receipt.
* The 2025 registry cohort, Ben-Salem 2015 and Ehaideb 2018 were not read.
