# RESPONSE — author's answer to the blind audit and the review of package R2

Author `sb-r2`, 2026-11-06. Answers every finding of `verify/audit_R2/audit_R2.tsv` by triple id and every finding of
`verify/review_R/review_R.tsv` for this package by statement id. Not medical advice; no dose, schedule or
administration route appears.

**Summary.** 9 audit findings: **9 ACCEPTED, 0 disputed.** 23 review findings for this package:
**21 ACCEPTED, 2 ACCEPTED WITH A NARROWER CHANGE THAN PROPOSED** (R2-MI-CE2 and R2-D09, both explained below), 0
disputed. Both checks were right about everything that mattered, and one of them caught an error I would not have
caught myself: my myelin null was a search artefact, not a finding. I am recording one error of my own that I made
*while* fixing an audit finding, because it is the most instructive thing in this round — see the note at the end.

---

## 1 · Blind audit findings (9 non-SUPPORTED rows)

| Triple | Verdict | My answer | Where changed |
|---|---|---|---|
| **R2-R16** NOT_IN_SOURCE | ACCEPTED | Correct, and this was the worst defect in the package. My quote was the sentence on survival of the control-treated arm and carried nothing about seizure frequency or interictal spikes. I re-located to the sentence the audit names and verified it word for word against the source before using it. | `evidence_r2.tsv` R16 locator; the re-location is noted in the row's `transfer_breakers` |
| **R2-R13** OVERSHOOT | ACCEPTED | Correct and important: I converted a treatment-effect count into a residual-defect count, which reverses its meaning. The source never reports a residual hippocampal count against wild type. Reworded to the audit's suggestion. I also accepted the secondary point and moved this row out of `cognition and behaviour` into a new class, `molecular state (bulk transcriptome)` — a bulk transcriptome is not a behavioural endpoint. | R13 `endpoint_class`, `endpoint_detail`, `transfer_breakers`; decision line 9 now says **cortical** transcriptome |
| **R2-R18** OVERSHOOT | ACCEPTED | Correct. The facts were exact but the grade `worse` and the inference "a property of the intervention and not a rescue" were mine, and the source's own next sentence reads the same result as normalised disease markers. Regraded `partial` and both readings are now stated in the row. I kept the methodological point — that a treated wild-type arm is indispensable — because it holds either way, and in fact holds *more* strongly now: the same datum reads as rescue or as cost depending on the prior, and only that arm separates them. | R18 `outcome`, `endpoint_detail`, `transfer_conditions`, `transfer_breakers`; README section 3 |
| **R2-R28** OVERSHOOT | ACCEPTED | Correct. "Tracked the myelin level rather than the functional benefit" asserts a dissociation the source does not make; it introduces the measurement to ask whether myelin contributes to the gains and concludes the treatment increases functional myelin. Reworded to the audit's suggestion. | R28 `endpoint_detail`, `transfer_breakers`; README section 2.3 |
| **R2-R31** OVERSHOOT | ACCEPTED | Correct, and it changes a conclusion rather than a sentence. The quoted sentence places myelination **outside** the restored-to-wild-type list, and the body gives about half of wild type with incomplete compaction. My wording moved it inside. Reworded and regraded `partial`. The inference I drew from it — that complete early correction normalises the sheath — is withdrawn; what survives is that earlier and more complete correction moved the sheath *further*, not to normal. | R31 `endpoint_detail`, `outcome`, `transfer_conditions`, `transfer_breakers`; README section 2.3 |
| **R2-R48** OVERSHOOT | ACCEPTED | Correct. 20 of 25 is the assessed treated cohort, which included early-symptomatic children; the source never reports that denominator for the pre-symptomatic subset, and the coincidence of the number 20 in the baseline table makes this an easy misread — I made it. Reworded, regraded `partial` (5 of 25 did not show normal acquisition), and the age field changed to `not_stated`, because a mixed cohort cannot sit in a timing cell. | R48 all affected fields |
| **R2-R55** OVERSHOOT | ACCEPTED | Correct. The sixfold macrophage reduction is a panel reading, not a reported quantity: the caption says only that the counts confirm a significant reduction. Reworded to declare the magnitude as an attestation, and the row regraded `partial`. | R55 `endpoint_detail`, `outcome` |
| **R2-R58** UNVERIFIABLE_SURFACE | ACCEPTED | Correct, and avoidable as the audit says. I re-acquired the open article page in a fourth pass and the row now carries a verified verbatim span of the Results sentence that reports the survival comparison. **No row in this package carries an attestation in place of a quote any longer.** | R58 `locator_quote`, `transfer_breakers`; README section 7 |
| **R2-R62** OVERSHOOT | ACCEPTED | Correct, and the error weakened my own negative, as the audit notes. Dosing began at P10 while this model's single lethal seizure is at P14, so the compound arm started **before** onset. Age corrected to `pre_onset`, status to `PREVENTED`, and the row now carries the stronger statement the source supports: the compound failed even when started ahead of onset. | R62 `age_at_restoration_vs_onset`, `status_vocab`, `endpoint_detail` |

### Surface defects inside SUPPORTED rows — all ACCEPTED

| Row | Defect | Fix |
|---|---|---|
| R2-R12 | Section given as "Supplementary results"; quote is in the main Results; the proposition dropped the source's hedge | Section corrected to `Results`; the "slightly inferior latency to fall" hedge restored in `endpoint_detail` |
| R2-R19 | Same section error | Corrected to `Results (tolerability in wild type)`, the subsection the authors title that way; the row already said the source reports the reduction without a statistic |
| R2-R50 | Unmarked elision — the source interposes a confidence interval inside the parenthesis | Quote re-cut to a genuinely contiguous span beginning after the parenthesis; the re-cut is recorded in the row |
| R2-R41 | Comparator is treated wild type, and the treatment itself shifted wild-type firing | `comparator_and_controls` now states this explicitly in capitals, so a downstream reader cannot miss it |
| R2-R15, R2-R24 | Survival graded `full` on censored endpoints | Both regraded `partial`, each with the censoring reason in `transfer_breakers` (a median stated as beyond 300 days; a predetermined eight-month endpoint) |
| R2-R43 | Whole-document absence claim that no single quote can carry | The section field now says so: "whole-document absence, no single quote can carry it; verified by inspection of the full prose" |
| R2-R21 | Follow-up to P150 belongs to the survival endpoint, not to weight | `follow_up` corrected to "measured at P40" with the reason recorded |
| R2-R65 | The cognition-and-behaviour binning is the reader's; the abstract says "disease-associated phenotypes" | `endpoint_detail` now states that the binning is this record's and quotes the abstract's own wording |
| R2-R04, R2-R33, R2-R45 | Quote reaches one element of a multi-element row | Each row's `endpoint_detail` now names which element the locator carries; R45 also had its status corrected (below) |

---

## 2 · Review findings for this package (23)

### Decision lines

| Id | Verdict | My answer |
|---|---|---|
| **R2-D01** NARROW | **ACCEPTED.** "Fully" was the authors' phenotype-level word and I carried it as an endpoint-by-endpoint grade. Line 1 now separates what is full (seizures, death from seizures, working memory, spatial learning) from what is not (sociability trending, interneuron excitability overshooting, 2 of 9 deaths after thermal challenge) and states that the adult arm carries a seizure endpoint only. |
| **R2-D02** HOLDS | Noted, no change. |
| **R2-D03** NARROW | **ACCEPTED.** Line 3 now opens with the modality — silencing a mutant transcript, not replacing a missing protein — and grades seizure frequency and nest building `partial`. |
| **R2-D04** NARROW | **ACCEPTED, and this is the finding that most changes the package.** My myelin queries were anchored on six gene symbols, so no string could reach an enzyme-deficiency, connexin, tubulin or astrocyte-transporter leukodystrophy. The broad null is withdrawn as a search artefact. Line 4 now states the two reachable models, the five new sources, and the narrower null that survives: no sheath morphometry after onset, in any family. |
| **R2-D05** NARROW | **ACCEPTED.** "Worked at P2" rested on a survival benefit with no row behind it. Row **R66** added with a verified locator, and "completely ineffective" now carries the unmeasured-restoration qualifier in the same sentence rather than one line later. |
| **R2-D06** NARROW | **ACCEPTED.** The expression statement is the authors citing others and their own unpublished work, which line 6 now says, and the generalisation is route-, capsid- and promoter-specific, which the two new late-delivery rows now bound. |
| **R2-D07** NARROW | **ACCEPTED.** Line 7 now cites R66 for survival rather than R40/R41, and "rescued" is dropped for seizure severity. |
| **R2-D08** NARROW | **ACCEPTED.** "Dominates" is withdrawn. Line 8 says "associated with", states that stage is not separated from the eligibility rules that follow from it, and marks the SMA contrast as a cross-trial secondary statement in the answer-first line rather than only in section 7. |
| **R2-D09** NARROW | **ACCEPTED, with one narrower change than proposed.** I took the whole correction: the recover-list is now qualified as two channel or channel-transcript models, interneuron excitability is "moving but overshooting", the transcriptome is cortical only, and the accumulated-structure clause no longer asserts arrest-never-reversal. The one thing I did **not** do is drop the accumulated-structure category: I kept it as a named class whose post-onset sheath cell is empty, because deleting the category would lose the distinction the challenge exists to draw. The claim attached to it is now an absence of measurement, not a direction. |
| **R2-D10** HOLDS | Noted. The review asks only that the imperative phrasing be softened; line 10 now reads as requirements of an interpretable design rather than as instructions, and names the three independent sources supporting the measure-the-restoration requirement. |

### Module-input findings

| Id | Verdict | My answer |
|---|---|---|
| **R2-MI-O7** NARROW | ACCEPTED. The sociability trend and the cellular overshoot are now in the statement (C1), not only in `limits`. |
| **R2-MI-O8** NARROW | ACCEPTED. C2 opens with the modality and carries the partial grades. |
| **R2-MI-O9** NARROW | ACCEPTED. C3 drops the unsourced survival clause (now R66), attributes the expression statement correctly, and adds the two late-delivery precedents. |
| **R2-MI-O10** NARROW | ACCEPTED. C4 states the germline arm as increased myelination to about half of wild type with incomplete compaction, drops the asserted dissociation, and carries the search-bounds qualifier. |
| **R2-MI-O11** NARROW | ACCEPTED. C6 uses `human_clinical_report` and puts the cross-trial provenance in the statement. |
| **R2-MI-O12** NARROW | ACCEPTED. C7 uses `human_clinical_report` and attributes the cognitive denominator to the whole assessed cohort. |
| **R2-MI-INF1** NARROW | ACCEPTED. The structure clause is replaced with the review's wording. |
| **R2-MI-INF2** HOLDS | Noted; the two late-delivery precedents are added as suggested. |
| **R2-MI-CE1** HOLDS | Noted, unchanged. |
| **R2-MI-CE2** HOLDS | **ACCEPTED, with a note.** The review upholds the methodological point and says the grade `worse` should not travel with it. I have done exactly that for R18. I have **kept** `worse` on R19, which is the only `worse` left in the table, because R19 is measured in treated **wild-type** animals, where no normalised-disease-marker reading is available — there is no disease to normalise. If the Orchestrator reads that as the same overreach, it is a one-field change to `partial` and I will not argue it further. |
| **R2-MI-CE3** HOLDS | Noted, unchanged. |
| **R2-MI-CE4** NARROW | ACCEPTED. The clause now names the readout as a composite imaging severity score and is not generalised to the sheath. |
| **R2-MI-CE5** HOLDS | Noted. I added one qualifier the new sources force: a short lifespan does not by itself forbid a later-delivery design, since a systemic arm at P20 worked in a null that dies within a month. |
| **R2-MI-NOTES** NARROW | ACCEPTED, reworded as proposed. |
| **R2-MI-CARDS-TML** HOLDS | Noted; one sentence added about the route-specificity of the expression generalisation. |
| **R2-MI-C01-EP** NARROW | ACCEPTED. The channel-gene qualifier is in. |
| **R2-MI-C04-FEA** NARROW | ACCEPTED, with the audit's two corrected numbers and the germline comparison, plus the one post-onset structural reversal. |
| **R2-MI-WO-DATA** HOLDS | Noted; the myelin clause now reads "sheath structure". |
| **R2-MI-RANK** NARROW | ACCEPTED. The pre-commitment is removed and replaced with the review's conditional wording. |
| **R2-MI-VOCAB-MODELTYPE** REJECT | **ACCEPTED, withdrawn.** `human_clinical_report` already exists on nine observations and its definition fits both human sources. My error was not checking the file's existing values before proposing a new one. |
| **R2-MI-VOCAB-WINDOWSTATE** REJECT | **ACCEPTED, withdrawn.** The reasoning is decisive: by the rule I myself stated twice, a non-WWOX observation never takes a window state, so the proposed value had no row to hold — and one of its two intended occupants (R62) turns out to be a pre-onset arm anyway. The fact is already carried by `status_vocab` and by `limits`. |
| **R2-MI-PRC-NULLS** HOLDS | Noted. The myelin null's bounds are now stated as narrowly as they actually are. |
| **R2-MI-PRC** HOLDS | Noted, unchanged. |

### Cross-package points

| Id | My answer |
|---|---|
| **XP-(a)** seizure endpoints | **ACCEPTED.** The decomposition is better science than my framing. My two post-onset seizure successes are both channel or channel-transcript lesions and are therefore the **least** transferable part of my package — which my own section 6 said, but my decision lines did not. I have added the channel-gene qualifier to decision line 4's reading, to the matrix reading and to the C01 card proposal. I also accept the sharper point: for a non-channel gene the external record is **split, not negative**, and spike-wave discharge rate is an interictal network measure, which is the sub-class in which a non-channel gene *has* recovered after onset. |
| **XP-(b)** status vocabulary | **ACCEPTED.** My R45 was `RECOVERED` with age `pre_onset`, a self-contradiction under the timing-only definition; corrected to `PREVENTED`. I agree the combined matrix must be built from `age_at_restoration_vs_onset` and `outcome` alone, and my section 1 now says so and is computed that way, with `at_onset` shown separately. |
| **XP-(c)** identifier collision | **ACCEPTED.** `O7`-`O12` withdrawn; `module_inputs.md` is now contributions only, with the first line the Orchestrator specified. |
| **XP-(d)** two vocabulary additions | **ACCEPTED, both withdrawn.** See the two rows above. |
| **XP-(e)** "full" behaviour and cognition | **ACCEPTED.** See R2-D01. |

---

## 3 · An error I made while fixing an audit finding

Worth recording because it is the sharpest lesson of the round. Fixing **R2-R58** meant replacing
`attestation_without_quote` with a real quote. I wrote a plausible-sounding sentence — "treated mice showed a
significant increase in survival compared with mock-treated mice" — from memory of what the paper reported. Before
committing it I re-acquired the page and checked: **it was not verbatim.** The actual sentence begins "Finally,
analysis of survival rates in additional groups of mock (n = 7) and fully treated mice (n = 5)". The row now carries
that verified span, and the means and p value are explicitly marked as a paraphrase of the sentence's continuation
rather than as quoted text.

Had I not checked, I would have replaced an honest declared absence with a fabricated quotation — a strictly worse
defect than the one I was repairing, and one that a verbatim audit would have caught as NOT_IN_SOURCE. The general
rule I am carrying forward: **a quote repaired from memory is not a quote.** Every locator written or re-cut in this
round was matched against its source text before use (normalising whitespace, case and dashes), and the 14 new or
re-located quotes were verified in one batch; two could not be matched on the first attempt and were re-cut.

---

## 4 · What changed, in numbers

| | First issue | After correction |
|---|---|---|
| Rows | 65 | 78 (13 added: R66-R78) |
| Sources | 12 | 17 (5 added) |
| Sources read beyond the abstract | 9 | 10 |
| Queries | 29 | 32 |
| Receipts | 9 | 10, all passing `--check-doi`, all recorded as validated in `INDEX.tsv` |
| Rows carrying an attestation instead of a quote | 1 | 0 |
| Rows graded `worse` | 2 | 1 (R19, in wild-type animals; justification above) |
| Matrix | hand-written, 4 membership errors | computed from the table |
| Observation identifiers proposed | O7-O12 | none; contributions only |
| Vocabulary additions proposed | 2 | 0 |

Rows changed by the audit or review: R04, R12, R13, R15, R16, R18, R19, R21, R24, R28, R31, R33, R41, R43, R45, R48,
R50, R55, R58, R62, R65 (21 rows). Rows added: R66 (the missing pre-onset survival row), R67-R71 (PMID 40051162),
R72-R73 (PMID 23817205), R74 (PMID 37149081), R75-R76 (PMID 41566774), R77-R78 (PMID 23011033).

---

## 5 · Re-validation

Run on the corrected deliverable, 2026-11-06:

* `evidence_r2.tsv`: 78 rows, 21 columns, equal column count on every row, no tab or newline inside a field. Every
  `locator_quote` is 25 words or fewer and every one was matched against its source. No `status_vocab` now contradicts
  its own `age_at_restoration_vs_onset`.
* Forbidden phrases: all eleven listed in the Orchestrator's addendum were checked by script against every file in
  this directory and none occurs. No country name occurs. The forbidden weight-normalised dose unit does not occur. No
  administered-dose number and no administration route occurs in any quote or any field. The two conditionally allowed
  terms covered by the proximity rule do not occur at all, so that rule is moot.
  *Note on this check:* the first draft of this section listed the forbidden phrases verbatim in order to report that
  they were absent, which made this file the only one in the package that contained them. The list is therefore
  referred to here rather than reproduced — a reminder that a compliance report is itself inside the compliance
  perimeter.
* No e-mail-like string, no markdown link to a file, no symlink, no executable bit, no shebang; the two helper scripts
  stay in the session scratch directory, outside the repository.
* All ten receipts: `staged_receipt_check.py --artifact-root ... --check-doi` returns `OK`.
* No file outside `r2_restoration_dee/` was created or modified; nothing was committed; no receipt was recorded.
