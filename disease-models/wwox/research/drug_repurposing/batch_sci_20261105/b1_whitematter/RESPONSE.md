# Author response — package B1 (`sb-b1`), correction round 2026-11-06

Response to the blind quote audit in `verify/audit_B/` (38 triples: 25 SUPPORTED, 9 OVERSHOOT,
2 UNDERSHOOT, 2 UNVERIFIABLE_SURFACE) and to the adversarial review in `verify/review_B/`
(decision statements: 0 HOLDS, 9 NARROW, 1 REJECT; module proposals: 2 HOLDS, 5 NARROW,
2 REJECT). Every finding is answered. Where a finding is ACCEPTED the place of the change is
named; where it is DISPUTED the evidence is given.

Summary: **every audit finding ACCEPTED (13 of 13). Of the review's findings, 15 ACCEPTED, 2
ACCEPTED WITH A NARROWING OF THE REVIEW'S OWN WORDING, 0 DISPUTED outright.** Two statements
where I differ from the reviewer's framing rather than its substance are marked and argued.

---

## A · Blind quote audit

| triple | verdict | response | where changed |
|---|---|---|---|
| B1-B1-03 | OVERSHOOT, locator mismatch | ACCEPTED. The conclusion sentence does not carry an association test. | `evidence_b1.tsv` row B1-03: `locator_quote` re-anchored to the regression sentence naming rapamycin as the only associated factor, with Table 3 and Table 1 named as the surfaces; `finding` rewritten to state the univariate and multivariate non-significance per variable. |
| B1-B1-06 | UNDERSHOOT, seven is the alone-count | ACCEPTED. Ten of the thirteen symptomatic cases had a movement disorder. | Row B1-06 `finding`; and decision 2 and the clinical-correlates paragraph of `README.md`. |
| B1-B1-14 | OVERSHOOT, 43 is not 43 at three time points | ACCEPTED. | Row B1-14 `species_or_population` (13 before, 18 during, 12 after) and `finding` (region-by-region resolution rests on the 12, and was not complete in the thalami). |
| B1-B1-15 | OVERSHOOT, improvement is not resolution; the 2-of-8 denominator was transferred | ACCEPTED. | Row B1-15 `finding` ("two infants, denominator not stated") and `reversibility` ("one improved on withdrawal"). |
| B1-B1-17 | OVERSHOOT, hydrocephalus relabelled as white-matter injury | ACCEPTED, and it was load-bearing in a white-matter package. | Row B1-17 `cofactors`, `age_at_first_exposure` and `transfer_breakers`; decision 8 of `README.md` now says post-haemorrhagic hydrocephalus. |
| B1-B1-19 | OVERSHOOT, locator mismatch | ACCEPTED. | Row B1-19 `locator_quote` re-anchored to the Results sentence that names the deep-grey and brainstem endpoint; the baseline sentence is now cited in `baseline_condition` as what it is. |
| B1-B1-20 | OVERSHOOT, resolution confounded; exposure start wrong; abstract contradicts body | ACCEPTED in full, and verified independently in the body before accepting: the case section states the drug was discontinued, that steroid pulses and antimicrobial and antiviral treatment were introduced, and the Discussion states it is impossible to predict whether the changes would have resolved without the steroid. | Row B1-20 `age_at_first_exposure`, `exposure_pattern_qualitative`, `reversibility`, `cofactors`, `transfer_breakers`, and `locator_quote` re-anchored to the "impossible to predict" sentence. The reversal of this case is no longer offered as support in decision 2. |
| B1-B1-22 | OVERSHOOT, "not infants" is the reader's inference | ACCEPTED. | Row B1-22 `age_at_first_exposure`, `species_or_population`, `transfer_breakers`; the counter-evidence paragraph of `README.md` now says ages not stated. |
| B1-B1-23 | UNDERSHOOT, hypothalamic T2 omitted | ACCEPTED, and it is material: it is the one quantitative imaging measure that did not normalise. | Row B1-23 `reversibility`; decision 4 of `README.md`; the work-order `data` proposal now asks for a quantitative imaging measure for this reason. |
| B1-B1-25 | OVERSHOOT, "adult" not in the abstract | ACCEPTED. The convention I applied to two neighbouring rows was not applied here. | Row B1-25 `species_or_population`, `age_at_first_exposure`, `baseline_condition`. |
| B1-B1-29 | OVERSHOOT, day-3 timing belongs to the GABA arm; quote is a fragment | ACCEPTED. The sentence that carries the vigabatrin direction also carries an administered amount, which the Orchestrator's addendum forbids reproducing, so the row now carries `attestation_without_quote` with the passage described, per that addendum. | Row B1-29 `species_or_population`, `age_at_first_exposure`, `exposure_pattern_qualitative`, `duration_class`, `finding`, `locator_quote`. |
| B1-B1-37, B1-B1-38 | UNVERIFIABLE_SURFACE | ACCEPTED. Both are attestations, not quotes. | `locator_quote` is now `attestation_bounded_null`; `finding` carries the query ids and run dates; and `README.md` has a dedicated "Bounded-null attestations" section naming the query set, the routes and the dates. |

Notes recorded on SUPPORTED rows: all adopted. B1-01 now says "per imaged child" and names the
143 excluded; B1-08 carries the exposed denominator; B1-27's "across species" is read as the
abstract permits (the species in which vacuolation was seen is not stated there, and the
companion abstract reports rodents and dogs but not primates); B1-30 states that the
gamma-hydroxybutyrate correlation is almost as strong and that inseparability is my inference;
B1-34 now states that the supplement was not retrieved. The B1-18 and B1-35 wording notes are
reflected in decision 2 and in the reversibility paragraph.

---

## B · Adversarial review of the decision statements

| id | verdict | response | where changed |
|---|---|---|---|
| S1 | NARROW | ACCEPTED on all three defects. Two of the four cohorts are one department with eight shared authors — my own row B1-13 said so and the decision line contradicted it; the rates are per imaged child; the unexposed comparators were missing. | Decision 1 rewritten: three independent centres, rates per imaged child, about 26 percent per exposed child where the denominator is given, and both unexposed comparators. Rows B1-01 and B1-08 carry the denominators. |
| S2 | NARROW | ACCEPTED. Resolution under continued exposure is reported in two of the newly read sources, so my exposure-window logic rested on a contingency the literature does not show. | Decision 2 rewritten ("not shown to be conditional on stopping"); the reversibility paragraph and transfer condition 4 updated; row B1-14's transfer condition no longer asserts that reversal is contingent on stopping. |
| S3 | REJECT | ACCEPTED. This was the largest defect in the package and I accept the rejection in full: the full-text cohort's exposure was almost entirely under 12 months and so could not test a within-infancy window; the diffusion study tested no risk factor; and the "pooled review" I leaned on had no row, no receipt and no identifier. Four sources with a positive age signal, three of them in my own Q3 output, were not read. | Decision 3 rewritten to say the human age band is supported, not contested, naming the controlled cross-age design and three further cohorts, with the restricted-range null and the untested diffusion study stated as what they are; the animal half kept with its species limits as `BRIEF_B1.md` pre-registered. Four new rows B1-39 to B1-42 with receipts. The uncited "pooled review" sentence is removed, not sourced. `module_inputs.md` §5.3 rewritten. |
| S4 | NARROW | ACCEPTED (same as audit B1-B1-23). | Decision 4; row B1-23. |
| S5 | NARROW | ACCEPTED on all three narrowings. "Negative" was stronger than a non-significant univariate comparison supports, my own B1-19 is a case in the opposite direction, and the under-recognition argument belongs in the statement that uses the null. | Decision 5 rewritten ("the only cohort-level human test ... did not demonstrate an excess", with the 14-of-34 under-recognition and the opposite-direction case). |
| S6 | NARROW | ACCEPTED. My own row B1-11 records a positive univariable association of prednisolone with the imaging finding, and the two symptomatic-form cohorts are one centre twice. | Decision 6 rewritten: absent in two cohorts, present for oral prednisolone in univariable analysis in a third with a wide interval, and the symptomatic-form signal from one group and centre twice. |
| S7 | NARROW | ACCEPTED. My Q8 was conjunctive and title-abstract only, which cannot see a histopathology endpoint inside a toxicology package. I read the open progress report and confirmed its sentence placing the standard toxicology of OV329 in an earlier, subscription-only report. | Decision 7 rewritten to "open by blockage, not demonstrated absent"; new row B1-43 and receipt `FTR-20261106-42470358-23`; rows B1-32 and B1-34 `transfer_breakers`; `README.md` unreachable section lists the two blocked reports; queries Q19 and Q20 added. |
| S8 | NARROW | ACCEPTED, with one narrowing of the reviewer's own wording (below). The axis is two-sided by receptor class and a molecule-specific taurine rival exists; I had not searched that literature. | Decision 8 rewritten and relabelled IPOTESI, naming both signs, the taurine rival and the autoimmune-model dissociation; new rows B1-44 to B1-48 with receipts; `module_inputs.md` §2 mechanism paragraph now leaves the direction unsigned. |
| S9 | NARROW | ACCEPTED. No `harm tag` field exists in any packet card, `undetermined` is in no closed vocabulary, and the work order had already registered that demonstrated added injury in a Wwox-deficient model is what would make a card-level C3. Asserting it from outside-WWOX cohorts pre-empted that. | Decision 9 rewritten: add the counter-evidence rows and let the position be computed; siblings UNKNOWN; C3 stays conditional. The harm-tag request is withdrawn from `module_inputs.md` §2 and the "retina-sparing" phrasing is gone. |
| S10 | NARROW | ACCEPTED. "The human literature shows those three do not recover together" was contradicted two sections later in my own README. | Decision 10 rewritten to attribute the separation of readouts to the two rat studies and to say the human record covers imaging alone; the receptor-subtype arm added; `module_inputs.md` §4 `data` proposal corrected in the same way. |

### Where I narrow the reviewer's wording rather than dispute it

1. **S8, on the strength of the GABA-A source.** The reviewer calls PMID 27796063 "a far better
   source than its 1989 explant culture" and places it in my direction. ACCEPTED as better
   evidence, with one limit stated in the row and in decision 8: it is a slice preparation with
   no drug, so it supports a receptor-level mechanism and not the exposure, and its own abstract
   reports that the GABA effect required a permissive axonal factor. That matters for a brain in
   which the axonal signal may be reduced — the repository's own counter-argument on the vacuole
   bridge — and I have not let the new source close that question.
2. **S7, on the sibling accumulation datum.** The reviewer reports the retina-to-plasma ratio and
   the below-quantitation result as the report's "one new sibling safety datum". ACCEPTED as the
   datum, with the addition that the sibling was below quantitation **in brain as well**, so the
   study supports no brain-exposure inference in either direction at the amount used. Row B1-43
   and decision 7 both say so.

### The review's open question, settled as instructed

The Orchestrator settles whether the two children of the WWOX imaging report are inside the
64-child aetiology cohort. As instructed, this package does **not** use the genetic-aetiology
signal of row B1-11 as independent corroboration of the WWOX report: `README.md` says so under
"What is not established", and `module_inputs.md` §1 attaches the caveat to DR-H02-016 and §5
item 1 repeats it.

---

## C · Adversarial review of `module_inputs.md`

| id | verdict | response | where changed |
|---|---|---|---|
| MI-1 | NARROW | ACCEPTED in full. `UNDETERMINED` and `NOT_MEASURED` were not in the consumer's vocabulary; six rows carried compound strings; DR-H02-025 would have inverted a sign; DR-H02-015 and -016 overclaimed; DR-H02-019 filed a diffusion metric as myelination; DR-H02-028 and -029 were not drug assertions. | §1 rebuilt: every `direction` is now INCREASE, DECREASE, UNKNOWN or NO_CHANGE with no compound strings; -015 and -016 are UNKNOWN; -025 is split into -025a and -025b, one per agent, with the endpoint named as the model's clinical severity score and no myelination target; -019 is retargeted to the diffusion metric with a note that it is not a myelin measure; -028 and -029 are gone from `drug_assertions` and the two genetic conditions now appear only in the §2 mechanism text; the DR-H02-005 note no longer says "four independent cohorts". |
| MI-2 | NARROW | ACCEPTED. | §2: harm-tag paragraph replaced by the counter-evidence-row wording; mechanism paragraph leaves the direction unsigned and names the receptor-subtype conflict and the taurine rival; `evidence_against` adds only what the card does not hold and cites the card for the rest; `not_known` uses "did not demonstrate". |
| MI-3 | NARROW | ACCEPTED. | §3: `counter_evidence` text now says "did not demonstrate an excess" with its limits; `do_not_assume` states the sign as unresolved and names both receptor classes. |
| MI-4 | NARROW | ACCEPTED, including the procedural point: describing an edit to a pre-registered sentence as "unchanged in substance" was wrong. | §4: the `data` proposal attributes the separation of readouts to the two rat studies and adds a quantitative imaging measure and a receptor-subtype arm; the `would_change` change is now flagged as an explicit amendment for the file owner to accept or refuse; the `feasibility` addition is kept as written and now also names the unexposed comparators. |
| MI-5.1 | REJECT | ACCEPTED. PCDH19 is not a GABA-pathway gene; the GABA-receptor subunit remark belongs to a different source. This was a factual error of mine. | §5 item 1 rewritten: the second case is described as one with a concurrent systemic metabolic deficiency, and the GABA-receptor subunit observation is attributed to its own cohort with the non-independence caveat. |
| MI-5.2 | NARROW | ACCEPTED. | §5 item 2 rewritten with three centres, the per-exposed rate and both unexposed comparators. |
| MI-5.3 | REJECT | ACCEPTED. It rested on S3, and the brief's consequences table had pre-registered that without full-text confirmation the sentence is kept with its species limits. | §5 item 3 rewritten: both halves supported, neither confirmed at full text here, status `premise_supported_species_split`. |
| MI-5.4, MI-5.5 | HOLDS | No change needed; both kept as written. | — |

### The consequences table of `BRIEF_B1.md`, re-answered

* Row 1 (risk in the first two years, mostly reversible): the review is right that the
  pre-registered action was a transfer condition on card H02 and that the first pass put it in
  prose. It is now proposed as card text in `module_inputs.md` §2 (`not_known` and the mechanism
  paragraph) and as the four transfer conditions in `README.md`, which is the nearest the card's
  own schema allows without a transfer-condition field.
* Row 2 (rodent or dog start-age series confirmed at full text): antecedent still not met — the
  full texts are blocked. The pre-registered default is applied: the sentence is **kept** with its
  sources and its species limits, and the first pass's downgrade of the human half is withdrawn.
* Row 3 (hormonal therapy not separable): applied, and now stated as split two to one rather than
  clean.
* Row 4 (nothing on a myelin-deficient baseline): applied, with the bounded null declared as an
  attestation; the sibling null is now stated as blocked rather than absent.

---

## D · Reading added in this round, and what the cap excluded

Ten sources, the Orchestrator's cap, all claimed with `paper_packet.py claim` and all with a
staged receipt (`FTR-20261106-<PMID>-23`), validated with `staged_receipt_check.py --check-doi`:

| PMID | depth | what it added |
|---|---|---|
| 19054414 | abstract_only | the controlled, blinded, ten-site cross-age design; resolution under continued exposure |
| 18783433 | abstract_only | age and duration contrast; an unexposed comparison group with the same indication |
| 20384718 | abstract_only | a fourth rate, an unexposed comparator, an age and an aetiology signal, reversal without cessation |
| 19258289 | abstract_only | the time course after the start of exposure and the age-dependence argument |
| 42470358 | partial_fulltext_read | the sibling toxicology pointer (blocked, not absent) and the ocular and brain accumulation comparison |
| 27796063 | abstract_only | GABA-A engagement reduces oligodendrocyte lineage number and myelination |
| 35980256 | abstract_only | a GABA-B agonist promotes remyelination in vivo |
| 31349008 | abstract_only | GABA and a GABA-B agonist accelerate precursor differentiation; a GABA-A agonist does not |
| 19194884 | abstract_only | taurine depletion as the reported cause of the drug's retinal lesion |
| 25062867 | abstract_only | inhibition of taurine transport by the drug |

Not read, because the cap bound at ten: PMID 39682762 (GABA-B removal from precursors protects
against demyelination) and PMID 20132888 (taurine deficiency damaging photoreceptors). Neither
direction is carried in any row. PMID 38092645 was treated as the brief requires — a pointer to
primary units, not a unit — and is not read and not rowed. The two conference reports holding the
OV329 toxicology (PMIDs 35946083, 39008349) are subscription-only and were not read.

## E · Re-validation after the corrections

* `evidence_b1.tsv`: 48 rows, 18 columns on every row, no tab or newline inside a field.
  Role counts support 19, counter 21, context 8; direction counts harm 24, undetermined 11,
  context_dependent 6, no_harm 7.
* `receipts/`: 37 staged receipts, all `OK` under
  `staged_receipt_check.py --artifact-root <shared checkout> --check-doi`; `INDEX.tsv` rebuilt
  with `validated_ok = yes_with_doi_check` on every row.
* Mechanical scan over every file in this directory against each of the eleven phrases the
  Orchestrator's addendum forbids, against country names and against the mass-per-weight unit:
  zero occurrences. One first-pass wording in the evidence table matched the second phrase of
  that list and was rewritten to "the first-detected case excluded post hoc". The phrases
  themselves are not reproduced here, since the release gate matches the literal wherever it
  appears, including in a compliance note.
* No administered-dose number in any field; two sources whose abstracts state amounts are
  recorded with an attestation in place of the quote.
* Nothing outside `b1_whitematter/` was written, nothing was committed, and no receipt was
  recorded to the ledger.
