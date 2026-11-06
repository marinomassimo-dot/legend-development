# Review A: adversarial review of packages A1 and A2

Independent reviewer (not a producer), `ORCH-SCIBATCH-DR-20261105`, 2026-11-06. Bound by
`BRIEF_COMMON.md` exactly as the producers were. Not medical advice: no dose, schedule, route,
preparation, titration or clinical preference is given here for any species, and exposures are
described qualitatively. Public edition: published cases appear only under the label their source
prints, at genotype-class level. Nothing outside this directory was written and nothing was
committed. No contact address was sent to any service; no route was worked around.

Scope: the conclusions of both packages and their consistency. The verbatim quotes are being
audited blind by other actors and are not re-audited here; where a quote is used below it is used
as the producers transcribed it, except where an open source let me check the number inside it.

## Answer first

**The arithmetic is clean and the conclusions are not.** Every headline number in both packages
reproduces exactly from the delivered tables — in rows and, for A1, in children after
de-duplication (section 3 below). I found no counting error in either package. A2's derived
quantities recompute to the digit, including the mediation estimate and the power of about one in
four, and A2 correctly transcribed and flagged a published confidence interval whose sign is
opposite to the difference in means it accompanies. The defects are of five other kinds:

1. **Depth labels overstate what was read, in both packages.** A1's decision line 1 says
   "11 read in full text here"; all 14 of its receipts say `partial_fulltext_read` (12) or
   `abstract_only` (2), and not one of its 14 source-depth labels says `full_text`. A2's table
   labels seven sources `full_text` while the receipt for each of those seven says
   `partial_fulltext_read`. Neither package read a source to full-text depth.
2. **The load-bearing symptomatic responses are partial, transient or clinical-only.** A1's
   headline — 4 of 6 children discordant — is arithmetically right, but in all four the response
   is qualified inside the quoted sentence itself: the first child's "the spasms resolved"
   continues "however, he soon developed other seizure types" and that report's own Table 1 codes
   the overall response *Partial*; the second child's Table 1 codes it *Poor*; one child's
   response is "no visible seizures" while video-EEG still recorded attacks and spasms; the fourth
   had one month of control then relapse. **No child in the set achieved a sustained,
   instrumented symptomatic response.** The record therefore cannot test whether a response
   predicts development; it can report only that partial and transient responses were not
   followed by a gain.
3. **A pre-registered consequence was not applied as written, and the repair is better than
   either wording.** BRIEF_A1 fixed: "Choi 2026 states exposure counts → the H02 human MRI
   denominators line is filled". Choi does state counts, and A1 declares the line unfillable.
   A1 is right that 2 of 2 in a report selected for the finding is not a denominator — and the
   denominator exists anyway: the same first author and two of the same co-authors, at the same
   institution, published a 64-child vigabatrin cohort in which 18 (28.1%) developed the
   abnormality and 9 of those 18 had genetic epilepsy. A1 missed it.
4. **Two module files cannot accept the proposals as written.** A1's new `needs.json` observation
   omits four fields that all 98 existing observations carry and sets `locator_status` to a value
   outside the closed vocabulary; its proposed rows for the vigabatrin assertion table give 10 of
   that file's 12 columns and use two values outside the file's own value sets.
5. **One statement in each package reaches past its stratum.** A1 reads a brainstem finding as
   "compatible with" a deep-grey finding it does not match; A2 declares a pre-registered
   consequence fired although its own rows block the condition in the unknown-aetiology stratum.

Verdicts over 44 statements, one row each in `review_A.tsv`. **A1** (10 decision lines + 14
module_inputs proposals = 24): 5 HOLDS, 17 NARROW, 2 REJECT, 0 UNVERIFIABLE. **A2** (10 decision
lines + 4 module_inputs proposals = 14): 7 HOLDS, 7 NARROW, 0 REJECT, 0 UNVERIFIABLE.
**Cross-package and depth points (a) to (f)** (6): 0 HOLDS, 6 NARROW.
Totals: **12 HOLDS, 30 NARROW, 2 REJECT, 0 UNVERIFIABLE.** Nothing is UNVERIFIABLE because every
statement of both packages is either recomputable from a delivered table or checkable against a
consumer file or an open record; the two REJECTs are both vocabulary and schema failures in
`module_inputs.md`, not scientific errors.

Sources the producers missed, found in 5 logged searches (section 8): a seven-child WWOX-DEE
series published 2026-08-30; the 64-child vigabatrin cohort from the same group as the two WWOX
children; a 110-child early-infantile DEE cohort reporting profound impairment irrespective of
genotype.

---

## 1. What I checked, in the order the task fixed

(1) every headline recomputed from the TSV in children and in rows → section 3; (2) overreach →
sections 2 and 4; (3) double counting and the identity inferences → section 5; (4) selection →
section 8; (5) transfer conditions and breakers → section 6; (6) the briefs' consequences tables →
section 7; (7) the module_inputs against the consumer files → section 9; (8) provenance of the
quotes used in a conclusion → noted inline; (9) answer-first sentences that read as advice and
counts that disagree → section 10; (10) a headline inviting a stronger reading than its
denominator supports → sections 2 and 4.

## 2. A1: the strongest reason each decision line could be wrong

**Line 1 — NARROW.** Counts confirmed: 14 sources; 41 children at row level; 38 children with at
least one of the four classes before the two possible-identity collapses and 36 after, matching
"36 to 38"; 6 children with both endpoints inside the four classes and 7 including the one
outside. The defect is the depth word. All 14 staged receipts read `partial_fulltext_read` (12) or
`abstract_only` (2); every `source_depth` cell in `cases_a1.tsv` begins `partial_fulltext` or
`abstract_only`. "Read in full text" is contradicted by the package's own two depth records. The
unnamed twelfth source is PMID 30356099, whose receipt exists and which contributes no row.

**Line 2 — NARROW.** The 4-and-2 split reproduces exactly. The reading does not. In every one of
the four, the response is qualified in the same passage the row quotes (detail in the answer-first
section above and in the table of section 3). Two of the four children come from one report. And
the sentence "no child on any of the four classes is recorded with a developmental gain" leaves
out that one vigabatrin-exposed child is recorded as *regressed* with timing relative to the
exposure not stated (row A1-33) — an outcome the phrase "development did not progress" does not
cover.

**Line 3 — NARROW.** All four per-class counts reproduce (vigabatrin 5, hormonal 3, diet 2,
cannabidiol 1). The threshold of 5 is met in *children*, not in independent exposures: three of
the five vigabatrin children are the same children that supply the hormonal, diet and cannabidiol
counts (one child supplies all four classes), every one was on co-therapy, and in two the class
was given in sequence with another class, so no developmental endpoint is assignable to
vigabatrin. The per-class columns are not independent samples and must not be read as four
separate assemblies.

**Line 4 — HOLDS.** The diet denominator is still unstated, 3 is a minimum, and the three
responder columns plus two columns with no diet entry are as the source prints them. Consistent
with CLAIM 042's own evidence boundary.

**Line 5 — NARROW.** True as printed, incomplete as evidence. See section 4(e): the same group's
64-child cohort supplies the population denominator and identifies concomitant hormonal therapy
as a risk factor, which converts A1's "unknown" into "unknown in these two, measured as a risk
factor in the same department's cohort".

**Line 6 — NARROW.** C2 staying is correct and well-reasoned. The H02 sentence departs from the
pre-registered consequence (section 7) and from A1's own `module_inputs.md`, which states the
2-of-2 figure in the very field the decision line calls unfillable.

**Line 7 — NARROW.** The revival trigger is quoted correctly from CLAIM 042 and does fire on
exposure alone. Two narrowings. CLAIM 042's own carrier is *compound heterozygous* Q230P with an
exon-5 deletion; both new exposures are *homozygous* Q230P, a different configuration, so the
claim's sentence about its own carrier is untouched and what fires is evidence about the
homozygous class. And the allele that the decision rests on appears nowhere in `cases_a1.tsv`
(which carries `missense` at class level, correctly) — only in two `denominators_a1.tsv` notes,
which name the allele per child together with an age and a cause of death. That exceeds the
brief's "genotype at class level" for per-child data.

**Line 8 — NARROW.** The conclusion is right and the work behind it is good: the cell-wise check
that refutes the patient-2 credit is the strongest single piece of verification in either package.
Two defects. The package applies two standards to the same kind of evidence — a Table 1 variant
credit is "no identity" for patient 2 and part of a probable identity for patient 3 — and the
asymmetry, although justified by the extra matched features, is never stated as such. And the
proposed replacement text drops the operative clause of the field it replaces ("so pooled counts
can double-count them"), which must be kept and re-scoped.

**Line 9 — NARROW.** The two quotes are as printed and the chosen reading is the better of the two
syntactic options. But "these cases" sits in a Discussion and is not shown to refer only to the
report's two children; if it ranges over the cases that Discussion reviews, neither scoping
concerns them and the resolution does not follow. "e.g." marks an example, not the only instance.
Keep the reading as the preferred of two, and name the residual ambiguity — the referent of "these
cases" — rather than reporting the qualifier as resolved.

**Line 10 — NARROW.** The hypothesis is well formed and the falsifier is the right one. As the set
stands it is untestable rather than supported: no child in it achieved a sustained instrumented
response, so no qualifying responder exists to expose the hypothesis to its own test.

## 3. Child-level table, recomputed from `cases_a1.tsv`

Children, not rows. Rows are per child per intervention class; `same_patient_as` was used to
merge, treating a bare row id as a stated identity and leaving "possible" identities separate,
then applying the two cross-report collapses the README declares. Script:
`children.py` in the reviewer's scratch directory (not in the repository).

Row-level totals confirmed: 57 rows, 18 columns, 58 lines all of equal field count; classes
vigabatrin 22, ketogenic diet 12, hormonal 11, cannabidiol 8, other context 4; concordance
discordant 6, concordant 6, not assessable 45; roles support 18, counter 17, context 22.
Children: 41 at row level; 38 with at least one of the four classes; 36 after the two collapses.

| Child (as printed) | Genotype class | Classes recorded | Symptomatic, per class | Development | Concordance | In the four classes | What qualifies the response |
|---|---|---|---|---|---|---|---|
| PMID 30361190, first child | null/null | hormonal, vigabatrin | hormonal partial; vigabatrin resolved | severe impairment unchanged | discordant | yes | the quoted sentence continues "however, he soon developed other seizure types"; that report's Table 1 codes the overall response *Partial* on three drugs |
| PMID 30361190, second child | splice | vigabatrin | partial | severe impairment unchanged | discordant | yes | Table 1 codes the overall response *Poor* on four drugs; residual cluster spasms at 11 months |
| PMID 39101447, single case | splice | vigabatrin | partial | severe impairment unchanged | discordant | yes | "no visible seizures" only; video-EEG still recorded electrical attacks and spasms |
| PMID 28721938, single case | splice | hormonal, vigabatrin | vigabatrin partial; hormonal resolved | severe impairment unchanged | discordant | yes | vigabatrin: one month of control then relapse; hormonal: complete clinical control with fragmented hypsarrhythmia persisting in sleep, seizures later returned |
| PMID 35573960, single case | null/null | vigabatrin, hormonal, ketogenic diet, cannabidiol | none in all four | severe impairment unchanged | concordant | yes | a true non-response; the only child supplying all four classes |
| PMID 29808465, patient 2 | missense | ketogenic diet | none | severe impairment unchanged | concordant | yes | non-response at 10 years |
| PMID 35792847, patient 4 | missense | other context | resolved | **improved** | concordant | **no** | the only recorded developmental gain; outside the four classes; the allele class the module associates with the milder phenotype |

Per class, children with both endpoints: vigabatrin 5 (4 discordant, 1 concordant), hormonal 3
(2 discordant, 1 concordant), ketogenic diet 2 (0 discordant, 2 concordant), cannabidiol 1
(0 discordant, 1 concordant). The 4 discordant children come from 3 reports, 2 of them from one
report. Every pooled row of `denominators_a1.tsv` matches this recomputation cell for cell.

Not in the table but relevant: one further vigabatrin-exposed child (row A1-33) has a
developmental outcome recorded as *regressed* with no symptomatic outcome, so it does not enter
the "both endpoints" set while being the only recorded worsening.

## 4. A2: the strongest reason each decision line could be wrong

**Line 1 — NARROW.** I checked the ICISS 18-month numbers against the open record (search S1):
mean VABS 73.9 (SE 1.3) versus 72.7 (1.4), difference -1.2, 95% CI -4.9 to 2.6, p 0.55; epilepsy
present 30.0% versus 29.2%. All as A2 prints them. A2 noticed that the printed difference carries
the opposite sign to the difference in means and wrote "(sign as printed)" — that is correct
handling of a real feature of the source, and I record it as verified rather than as a defect.
Two narrowings. "Did not develop better overall" states a null that is an undemonstrated
difference: A2's own line 6 computes the power at about 0.24, so the sentence should say no arm
difference was demonstrated and name the power. And EPISTOP and PREVeNT test *prevention before
onset*, which A2's own breaker list says, so they cannot carry a sentence about *response*;
PREVeNT's spasm comparison was neither prespecified nor tested, which A2 also says in section 1.1
but not in the decision line.

**Line 2 — HOLDS.** Verified against the open record: responders 229 versus non-responders 129,
VABS 79.1 (SE 1.2) versus 63.2 (1.1), difference 15.9, 95% CI 12.4 to 19.5, p < 0.001. 175 + 61 =
236. Aramanadka's cells give an odds ratio of 5.17, printed as 5.2. 18 of 22 versus 13 of 38 is
82% versus 34%, and A2 is right that the ratio in that direction is 2.4 from the cells while
Table 2 prints 4.2 on both rows — contesting a printed statistic from the cells is the correct
move and it checks out.

**Line 3 — NARROW.** 126 of 175 is 72.0%, 40 of 62 is 64.5%, 13 of 38 is 34.2%: all as printed.
The only narrowing is the one A2 itself flags — Aramanadka's responder denominator is 61 in its
Table 2 and 62 in its Tables 3-4 — so the figure is 65% only on the larger denominator and the
discrepancy belongs in the sentence, not only in section 1.2.

**Line 4 — HOLDS.** With one condition to carry forward: 0 of 49 is over *all* children of genetic
aetiology, and A2's own table says the responder count among them is not in the text read, so it
is not a responder rate and must not be quoted as one.

**Line 5 — HOLDS.** The stratum dependence is supported and the inference about CLAIM 031 is the
right one. The instrument condition in section 4(a) must travel with it.

**Line 6 — HOLDS.** Recomputed independently and it is exact. 0.150 x 15.9 = 2.385, printed 2.4.
Standard error of the difference from the reported standard errors: the square root of
(1.3 squared + 1.4 squared) = 1.911; the published interval's half-width of 3.75 implies 1.913, so
those are the right standard errors. Power at two-sided 0.05 for a true effect of 2.385 = 0.239,
printed "about one chance in four". And 2.4 lies inside the printed interval under either sign
convention. This is the best-verified derived quantity in either package.

**Line 7 — NARROW.** Correct as to the sources, but it mixes depths without saying so: the UKISS
and ICISS lead-time associations are abstract-level rows, while the one full-text test found lead
time not independent of aetiology and absent within unknown aetiology. The sentence should name
which side is abstract and which is full text.

**Line 8 — NARROW.** Two of the three sources are abstract-only. "Even after adjustment for
seizure control by 1 month" describes an adjustment model that cannot be read from an abstract; it
should be carried as the abstract's own assertion, not as a property of the analysis.

**Line 9 — HOLDS.**

**Line 10 — NARROW.** See section 7: the brief's row-1 condition requires the arm-level null in
the genetic, structural *and* unknown strata, and A2's own rows A03 and A05 record a randomised
developmental arm difference in the unknown stratum. A2 partly repairs this by writing "generic
*genetic*-DEE feature", but the departure from the pre-registered condition should be declared
rather than absorbed into an adjective.

## 5. Double counting and the identity inferences

Judged one by one against the evidence cited. Those that should be worded INFERENZA and are:
patient 3 of the five-patient series = the first child of PMID 30361190 (a rare homozygous
exon-level deletion credited to that report, same sex, same onset week, same two MRI features,
optic atrophy, shared co-authors — strong, and correctly marked); the three homozygous
p.Arg264* children across two reports (sex and age at last follow-up exclude both candidate
identities — sound). Correctly refused: the patient-2 credit to the 2019 cohort, refuted cell-wise
against that report's supplementary table. Correctly marked "possible" and collapsed to the lower
count: the Choi pair against patient 5 of the five-patient series; the single case against one of
the three children of the 27-centre series. Correctly marked "possible" with no effect on any
count, because the earlier report carries no treatment row: the 2017 case against patient 8 of the
2019 cohort; patients 2.1 and 2.2 against the earlier sibship report; patient 3.1 against the
earlier report. I found no double count anywhere in the pooled figures.

**On the public-edition rule.** Linking "patient 3" to "child 1" across two papers is not
individual-level linkage in the sense the brief prohibits — the brief prohibits coordinates,
pedigree, parent-of-origin allele linkage, dates of birth, photographs — and de-duplication across
reports is required by the coordinator's own addendum, so a per-child table that carries
`same_patient_as` respects the rule. What exceeds it is the *evidence* column of the identity
table and two notes of the denominators table: together they assemble, for single children, a
specific allele, sex, onset week, named MRI features, optic atrophy, an age at death and an age at
last visit. That is a clinical vignette reconstructed across two papers, and it is more than the
judgement needs. Recommendation: keep every identity verdict, and replace the feature lists with
the count of matched features plus class-level descriptors ("five matched features including
genotype class, onset band and two imaging features; shared co-authors").

## 6. Transfer conditions and breakers

**A1.** Four breakers (allele class, instrument, timing, co-therapy) and one condition. They are
the right five and they are honestly stated — the instrument breaker in particular ("an absence of
recorded gain is not a measured absence of change") is the sentence that should govern the whole
package. Two are missing. **Response quality** is a breaker and the most important one: a set in
which no response is sustained or instrumented cannot speak to what a response predicts (section
2, line 2). **Ascertainment** is a breaker: every report is selected for being publishable, and
the one cohort that is population-like is named only as unreachable.

**A2.** Four conditions and five breakers, all supported, and the fourth condition (a cut at 70
hides change below it) is what makes A2's own IPOTESI testable. Missing: the **arm-level nulls are
underpowered**, which A2 computes in line 6 but does not carry into the condition list, so a
consumer reading only section 3 would take the trial nulls as evidence of decoupling — which A2's
own line 6 denies.

## 7. The briefs' consequences tables: applied as pre-registered?

| Pre-registered | Applied? |
|---|---|
| A1, 5 or more children with both endpoints for a class → INV-10 gets counts with sources, no percentage under n = 10 | **Yes.** Vigabatrin fired it; `module_inputs.md` gives counts and no percentage. |
| A1, fewer than 5 → "not computable from the public record: k of N"; C2 stays; next test reworded as a denominator request, no contact | **Yes for the three classes below threshold**, and no contact was made. But the next-test rewording was applied to the whole investigation although the headline class fired the other branch; say which branch fired for which class. |
| A1, Choi states exposure counts → the H02 human MRI denominators line is filled; if hormonal co-therapy was present at the MRI change, the H02 caveat names it as a confounder | **No, on both clauses.** Counts are stated (2 and 2) and the line is declared unfillable; the co-therapy clause is answered "unknown" when the same group's 64-child cohort measures it as a risk factor. A1's scientific point — that 2 of 2 in a report selected for the finding is not a denominator — is correct and better than the brief's wording; the repair is to fill the line with the abstract-level figure, the selection caveat and the sibling cohort's population denominator. |
| A1, any claim wording wider than its source → a proposed narrowing with the quote, nothing edited | **Yes**, for CLAIM 001, 031 and 042; nothing was edited. |
| A2, row 1: an early spasm-control arm difference that does not carry to development in genetic/structural/**unknown** strata → base rate stated; INV-10 reworded as a generic DEE feature | **Partly.** The condition fails in the unknown stratum by A2's own rows; declared fired. Narrow to genetic and structural. |
| A2, row 2: development tracks lead time or aetiology more than arm → INV-10 gets a transfer condition | **Yes.** |
| A2, row 3: association never reported → stated as such | **Correctly did not fire**; the association is reported in five sources and as a null in three. |

## 8. Selection: what the bounded queries could not see, and what they missed

**A1's blind spot is structural.** All six PubMed strings and all six Europe PMC strings are
`WWOX AND (epilep* OR encephalopath* OR WOREE OR SCAR12)` combined with a *drug name*. A report
whose abstract names no drug is unreachable by every one of them, however much therapy its tables
carry. An independent string without a drug term returns 24 records on the cohort axis and 113 on
a therapy-and-outcome axis; A1 ran neither.

The miss this produced, found in search S2: **a seven-child WWOX-DEE series published 2026-08-30**
(PMID 42721537, *Seizure* 142:204-211,
[DOI](https://doi.org/10.1016/j.seizure.2026.08.027)). Seven children, median seizure onset
3 months, five with focal seizures evolving to infantile epileptic spasms syndrome and two with
that syndrome at onset, hypsarrhythmia in six, **"Epilepsy was drug-resistant in all"**,
**"Developmental delay was evident from birth"**, a recurrent splice-site variant in five
suggesting a regional founder effect. Its abstract names no drug, which is exactly why A1's
strings could not see it. Consequences: it is a candidate source of up to seven further children
with a symptomatic outcome (non-response) and a developmental outcome, which would *dilute* the
4-of-6 discordance headline toward concordant non-response; and its "developmental delay was
evident from birth" is independent support, in seven children, for the premise of CLAIM 031 that
A1 found "not cleanly shown" in the two children of its own source. No PMC record, so the full
text is not reachable by an open route and I did not attempt a workaround; it belongs in the
full-text queue, not in a count.

**A2's selection is sound on its main axis.** An independent stratified-by-aetiology string
(search S4) returns 13 records and its top hit is the one A2 read at text level, so the thin
literature A2 describes is really thin. On its second axis it missed one large source (search S3):
**a 110-child early-infantile DEE cohort with burst-suppression EEG** (PMID 42190144, *Neurology*
106(12):e218013, [DOI](https://doi.org/10.1212/WNL.0000000000218013)), reporting that most
children (72.5%) had persistent seizures at a mean of 6.5 years "as well as profound intellectual
disabilities, **irrespective of genotype**", with mortality of 25%. It points the same way as A2's
line 4 and would strengthen it; it is gene-cohort shaped, so A2's gene-specific strings could not
retrieve it.

**Searches run for this review** (route, string, UTC date, hits):

| Id | Route | String or identifiers | Date | Hits | What it settled |
|---|---|---|---|---|---|
| S1 | PubMed metadata | PMIDs 42735667, 41442931, 30236380 | 2026-11-06 | 3 | point (e); the ICISS numbers and interval behind A2's lines 1, 2 and 6 |
| S2 | PubMed search | `WWOX AND (encephalopathy OR WOREE OR epilepsy) AND (cohort OR series OR "natural history")`, by date | 2026-11-06 | 24 (20 returned) | found PMID 42721537 |
| S3 | PubMed metadata | PMIDs 42721537, 42397075, 42266427, 42190144, 41561974, 41510857, 41153369 | 2026-11-06 | 7 | confirmed 42721537; found 42190144 |
| S4 | PubMed search | `("infantile epileptic spasms syndrome" OR "infantile spasms" OR "West syndrome") AND (etiology OR aetiology OR genetic OR structural) AND ("developmental outcome" OR "neurodevelopmental outcome") AND (responder OR "spasm cessation" OR "treatment response") AND (stratified OR subgroup OR "by etiology")`, by date | 2026-11-06 | 13 | A2's main axis confirmed complete |
| S5 | PubMed search | `WWOX AND (treatment OR therapy OR antiseizure OR "ketogenic diet" OR vigabatrin OR management) AND (outcome OR development OR follow-up)`, by date | 2026-11-06 | 113 (20 returned) | quantified A1's selection hole |

All five are open PubMed routes. No contact address was sent anywhere. Not found, after S2 and S5:
any later report, correspondence or erratum stating how many children of the five-patient series
were placed on the ketogenic diet — A1's "not stated, minimum 3" stands. Not found: any open
report of the two WWOX children beyond the case report itself; their likely cohort membership
(point (e)) is an inference from author, institution, design and window, not a stated fact.

## 9. The module_inputs files against the consumer files

**A1 section 1, INV-10.** Right file and right field names: `evidence_depth` does exist in
`ranking.json` (current value "E3 - card reviewed with assertions; no WWOX-side result read beyond
abstract"). Three defects. The E4 wording claims reads the receipts record as partial. The
`next_test` replacement silently abandons the existing next test ("Assemble the published
same-genotype cases with both a symptomatic and a developmental endpoint recorded, and state the
discordance rate"), which this package has now *executed* and found not computable as a rate —
that execution and its result are the finding, and replacing the field hides it. And the
branch-2 consequence is applied investigation-wide (section 7).

**A1 section 2, `needs.json`.** The O1 and O2 edits are well targeted and quote-anchored, but the
O1 `limits` replacement drops that field's operative clause. **The new observation O4 is REJECT as
written**: every one of the 98 observations in `needs.json` carries `tissue_or_cells`, `age_stage`,
`evidence_scope` and `locators`, and O4 omits all four; and `locator_status` is set to "STAGED",
which is not one of the four permitted values (MANIFEST, DOCUMENT, REGISTRY_ONLY, GAP). The rest
of O4 is in vocabulary: `model_type` human_clinical_report and `readout_level` clinical are both
used by the existing observations.

**A1 section 3, `work_order.json`.** Right entries and right fields. The NEED-MYELINATION
`feasibility` rewrite keeps "not available" while stating the figure, so it contradicts itself and
the pre-registered consequence; the NEED-SEIZURE `data` append needs the selection caveat. The
`would_change` judgement (C2 stays) is correct and matches that field's own wording.

**A1 section 4, card H02.** Both caveat sentences are the right ones to add. The first must name
the sibling cohort's measured hormonal-co-therapy association rather than leaving the confounder
as unknown; the second needs the location caveat of point (d).

**A1 section 5, the vigabatrin assertion table. REJECT as written.** The target file has 12
columns; the proposal gives 10, omitting `origin_group` and `pub_year`. Two proposed values sit
outside the file's own value sets: `member_evidence_sign` "(exposure only)" (the file uses
benefit, partial_benefit, null, unresolved, "(not in member_evidence)", "(harm, other endpoint)")
and `descriptive_code_it17_semantics` "favourable (transient)" (the file uses favourable,
"favourable (partial)", null, undeterminable, "contrary on another endpoint (off_objective)"); the
A-VGB-7 row also drops that last value's "(off_objective)" suffix. The new ids A-VGB-12 to -14 do
not collide with the file's ids.

**A1 section 6, early cards — HOLDS.** All four edits follow from the denominators rows.

**A1 `proposed_registry_changes` — NARROW.** The CLAIM 001, 031 and 042 narrowings follow from the
rows and are quote-anchored; item 9 must add the sibling cohort; items 3 and 7 carry per-child
allele and age detail that should be class-level.

**A2 section 1, INV-10 — NARROW.** Right file and fields. The proposed `evidence_available`
sentence imports the undemonstrated-null problem of line 1 and should carry the power figure, and
its TSC clause must say prevention rather than response. Everything else is in the entry's own
vocabulary, and the note that the entry has no dedicated transfer-condition field is correct.

**A2 section 2, work order — HOLDS.** Correct fields, and the wording correctly leaves the C2
judgement to package A1.

**A2 section 3, CLAIM 031 — HOLDS.** This is the strongest single proposal in either package. The
claim's `Genotype/model relevance` line does assert a genotype-independent principle, and the
randomised unknown-aetiology subgroup is the right counter to it. One narrowing only: the quote
offered is from an abstract and must be labelled so.

**A2 section 4, `proposed_registry_changes` — HOLDS.** Item 4 deserves recording: A2 corrected its
own brief, whose statement that nothing on this baseline had been read at full-text level by the
module is false, the three TSC trials being module-held complete reads. Items 1 and 2 must
describe the eight text-level sources as partial, per their receipts.

## 10. Answer-first sentences, advice, and counts that disagree

No sentence in either README reads as clinical advice or a preference between interventions. Both
carry the not-medical-advice line, both describe exposures qualitatively, and I found no dose,
schedule, route or titration anywhere in either package. A1's "C2 therefore stays" and A2's
"a responder with poor development is what the genetic-DEE baseline predicts" are statements about
the record, not recommendations.

Counts that disagree between sentences: A1's "11 read in full text" against its own 14 depth
labels and 14 receipts (section 2, line 1); A1's "2 of 2" stated in `module_inputs.md` against
"cannot be filled" in decision line 6; A2's table labels `full_text` against its own eight
`partial_fulltext_read` receipts. Between the two READMEs there is no numerical disagreement: A1
reports no base rate and A2 reports no WWOX count, and each says so.

A headline inviting a stronger reading than its denominator supports: A1's "vigabatrin meets the
threshold of 5" (five overlapping children, every one on co-therapy, no sustained response) and
A1's "2 of 2 children on vigabatrin, both with the MRI change" (a report selected for the
finding). Both are flagged above with corrected wording.

## 11. Cross-package points (a) to (f)

See the final report for the settled sentences; the evidence for each is in sections 2, 4, 5, 8
and 9 above. (a) is settled in favour of a combined sentence that raises A1's n and denies
specificity, with the instruments named. (b) the trigger fires, on a different allele
configuration from the claim's own carrier. (c) the reading is the better of two, not a
resolution. (d) the two unexposed children show a brainstem pattern, not the deep-grey pattern
reported in the exposed pair, so they do not qualify that pair's within-child comparison; what
they qualify is any attribution without a pre-exposure scan. (e) overlap is probable on five
converging features. (f) both packages normalise to `partial_fulltext` almost everywhere.

## 12. What this review did not do

It did not re-audit the verbatim quotes, which other actors are auditing blind. It did not read
any full text: its five searches were PubMed metadata and search routes only, and the one new
WWOX series it found has no open full text. It recorded no receipt, committed nothing, and wrote
only inside this directory, with its one script in the reviewer's scratch directory outside the
repository.
