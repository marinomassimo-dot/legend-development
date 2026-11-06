# RESPONSE — author response of package R1 (`sb-r1`) to the blind locator audit and the independent review

Written 2026-11-06. Non-canonical research material. **Not medical advice**; no dose, schedule, route or
administered-dose number appears here. Public edition, reference genotype class only.

Inputs answered: `verify/audit_R1/audit_R1.tsv` and `audit_R1_README.md` (62 triples) and
`verify/review_R/review_R.md` with `review_R.tsv` (the R1 statements). **Headline: 26 findings ACCEPTED in
full, 3 ACCEPTED with a correction to the correction, 2 DISPUTED in part, 0 disputed in whole.** Both checks
were good: the audit caught two errors I could not have caught myself (a locator pointing at the wrong
sentence, and a follow-up window belonging to a different experiment), and the review caught a false
sentence in my own decision list that my own table contradicted.

I also owe one plain admission up front: **my bounded myelin null was a search artefact.** My queries were
anchored on the nine gene names my brief assigned, so no string of mine could reach a leukodystrophy caused
by an enzyme, a connexin, a tubulin or an astrocyte transporter. The reviewer's four searches found three
post-onset white-matter arms in exactly those families. Decision line 1 was rewritten.

---

## 1 · Audit findings, by triple id

### OVERSHOOT (6)

| Triple | Verdict | What I changed |
|---|---|---|
| `R1-R14` | **ACCEPTED** | Wild-type-level latency holds for the tonic-clonic stage only. `R14` outcome `full` → `partial`; `endpoint_detail` now names all three stages separately (wild-type level at the second, improvement without equivalence at the first, no genotype effect at hind-limb extension). This also weakened my own rebuttal of decision line 5, and I said so there rather than leaning on it. |
| `R1-R20` | **ACCEPTED** | The quote was the specificity caveat, not the result. `R20`'s locator is re-located to the Discussion result sentence; outcome `full` → `partial`; both caveats recorded (proportional wild-type effect, locomotor correction only at the longer duration). The audited caveat quote is preserved as a new counter row **`R77`**, so nothing audited was discarded. |
| `R1-R57` | **ACCEPTED** | `follow_up` → "measured at postnatal day 16"; `endpoint_detail` → myelin basic protein and proteolipid protein levels plus corpus callosum **myelin basic protein immunostaining thickness**; "no electron microscopy in the source" added to `authors_stated_limit`; `transfer_breakers` now says marker-level, not sheath morphometry. |
| `R1-R58` | **ACCEPTED** | Same two fixes. Outcome `none` confirmed and kept. |
| `R1-R59` | **ACCEPTED** | `follow_up` → postnatal day 16. Interpretation kept; it is the authors' own. |
| `R1-R64` | **ACCEPTED, and this was the worst error in the package.** | A locator mismatch: my quote reported the overall observational symptom score, not respiration, while the row's endpoint and *both* follow-up figures matched a different sentence. Re-located to the auditor's suggested sentence ("two months after TAM-treatment, the respiratory pattern in 10 of 12 ... were within normal range"), with the five-month follow-up clause added to `endpoint_detail`. I could not have found this by re-reading my own notes, because the quote *was* verbatim; only a blind match of proposition against sentence catches it. |

### UNDERSHOOT (6)

| Triple | Verdict | What I changed |
|---|---|---|
| `R1-R04` | **ACCEPTED** | Body weight outcome `partial` → `full`; no partiality qualifier attaches to weight in the source. |
| `R1-R07` | **ACCEPTED with a correction to the correction** | The direction was wrong, as the audit says: it is over-correction, not incomplete correction. But `outcome` is a closed set of `full \| partial \| none \| worse \| not_measured` and has no value for "exceeded". I set `full` and put "restored and then exceeding wild-type level (over-correction)" in `endpoint_detail` with the authors' own flag in `authors_stated_limit`. If the integrator wants a sixth outcome value, this row and the sibling package's interneuron row are its two occupants. |
| `R1-R22` | **ACCEPTED** | Split by arm, as instructed: `R22` keeps the 6-week start (`post_onset_early`, `none`) so the matrix cell the audit checked is preserved, and the birth-start arm is the new row **`R78`** (`pre_onset`, `full`). Both now declare in `authors_stated_limit` that this is the audited source reporting a cited 2011 study and not its own data. |
| `R1-R25` | **ACCEPTED** | Outcome `partial` → `full` for the four named endpoints of the six-week arm; working memory is not among them and is excepted explicitly. The leaky-Cre note is carried into `authors_stated_limit`. This sharpens decision line 6 rather than softening it. |
| `R1-R53` | **ACCEPTED** | Outcome `partial` → `full` for soma size, dendritic length and hippocampal spine density, with the significant treatment effect named; residual deficits named as cortical thickness (own row `R55`) and dendritic complexity at 2 of 11 radii. Also fixed: the source says about 70 per cent of **neurons**, not of brain cells — corrected in `cells_restored` and `transfer_breakers` on both `R53` and `R54`. |
| `R1-R54` | **ACCEPTED** | Outcome `partial` → `full` against the normalisation sentence, with the two named exceptions in `endpoint_detail`. |

### UNVERIFIABLE_SURFACE (8)

| Triple | Verdict | What I changed |
|---|---|---|
| `R1-R33` | **ACCEPTED** | Kept as a declared attestation, with the basis now stated in the row: spine morphology was measured in the adult-deletion arm only, not in any restoration arm. The audit independently confirmed that against the source. |
| `R1-R49` | **ACCEPTED, now resolved** | Kept as a declared attestation and **confirmed** on re-acquisition: the source reports myelination in no section, figure or supplement. The row says so and marks that it was unverifiable to the audit. |
| `R1-R44` … `R1-R48`, `R1-R50` | **ACCEPTED** | Both sources were re-acquired on 2026-11-06 through the PMC article-page route this package had already declared as `Q26`; the auditor received a bot-check interstitial, I received the body, and I worked nothing around. Every quote re-confirmed. Because re-confirmation by the producer is not independent verification, all nine rows of those two sources now carry `source_depth` = "partial_fulltext re-acquired by producer via article page; not independently verified", and the README carries a **second post-onset matrix with those two sources removed**. `R45` also gained a better, abstract-surface-verifiable locator ("Late treatment with rapamycin suppressed seizures and prolonged survival in Tsc1GFAPCKO mice that had already developed epilepsy"). |
| `R1-R50`, outcome grading | **DISPUTED in part** | The audit reads `partial` on the abstract surface ("improved"). The Results sentence, which I read and have now re-confirmed, says "effectively restored myelination". I keep `full` on the Results word and record both wordings in `authors_stated_limit` so the integrator can see the discrepancy. The row is in any case `EARLY-WINDOW` with an unlocated onset, excluded from the headline matrix, and not load-bearing for any conclusion. |

### Carry-forward notes on SUPPORTED rows (6)

| Triple | Verdict | What I changed |
|---|---|---|
| `R1-R16` | **ACCEPTED** | Locator extended to the sentence that actually carries the failure to improve ("we did not observe an effect of phase, or an interaction between phase and genotype in this analysis"). |
| `R1-R24` | **ACCEPTED** | `authors_stated_limit` now records that the authors' word is "becomes limited", weaker than `none`, and that the `none` grade rests on the separate statistical statement in `R23`. |
| `R1-R09` | **ACCEPTED** | Recorded that grooming lacks an explicit wild-type-level statement, so `full` is strong for that component. |
| `R1-R41` | **ACCEPTED** | Recorded that the induction age and recording window were absent from the only surface the auditor could reach and are unverified there. |
| `R1-R05` | **ACCEPTED** | "over 15 months" → the source's "survived for 15 months", in `follow_up` and `authors_stated_limit`. |
| `R1-R74` | **ACCEPTED** | Recorded that the source hedges ("molecular experiments suggest that") although its title asserts the negative outright. |

---

## 2 · Review findings, by statement id

| Statement | Verdict | Response |
|---|---|---|
| `R1-D01` | **ACCEPTED** | Both halves. The count error is real: `R49` is `post_onset_advanced`, so "all eight myelin rows are pre-onset or unlocated" was false — it is seven of eight, the eighth being a post-onset arm with no myelin measurement. And the generalisation to the literature does not survive the reviewer's four searches. Decision line 1 rewritten to scope the null to **sheath structure after onset in a neuron-driven lesion**, naming all three external arms with their breakers. |
| `R1-D02` | **ACCEPTED** | The three results were pooled at one epistemic level. Line 2 now separates them: a study without a surviving untreated same-genotype arm and therefore not an equivalence result; an over-correction above wild type; and a **pathway drug**, marked as such, whose spine rescue a study cited in the same paper reports only from a birth start. The audit's half-concession (a significant treatment effect does stand behind the sentence) is reflected by `R53`/`R54` moving to `full`. |
| `R1-D03` | HOLDS | No change. |
| `R1-D04` | HOLDS | No change, except that line 5 no longer leans on `R14` as a general threshold recovery. |
| `R1-D05` | **ACCEPTED — REJECT accepted in full** | This was a false sentence contradicted by my own table and my own body paragraph. Line 5 is rewritten: the two conditional failures are kept, and the post-onset successes are named for what they are, including **genetic** ones (`R13`, `R14`) and the new antisense rescue at the same postnatal age as one of the failures. The claim that the only post-onset seizure success was a pathway drug is withdrawn in the README, in `module_inputs.md` and in the card append. |
| `R1-D06` | HOLDS | No change; `R1-R25` sharpens it, and I say so. |
| `R1-D07` | HOLDS | Count kept at three `worse` rows and the mark added that one of them (`R47`) was unaudited. A fourth `worse` row (`R84`) is added from the new reading, and the hazard is now explicitly scoped: abrupt conditional reactivation and a specific compound, not gene addition as such. |
| `R1-D08` | **ACCEPTED** | "The Angelman pair is the clean case" is withdrawn. Line 8 now states that restoration mode and level achieved are not separated from the temporal requirement in any gene that fits, and stays INFERENZA. |
| `R1-D09` | **ACCEPTED** | Rewritten per `R1-D01`. |
| `R1-D10` | **ACCEPTED** | Rewritten: the discriminating endpoint is sheath structure in a neuron-driven lesion, and "the prediction most at risk" is replaced by "the external precedent for the spike-wave class is split, not negative". |
| `R1-MI-O7` … `R1-MI-O10` | **ACCEPTED** | All four proposed identifiers withdrawn. `module_inputs.md` now opens with the line stating that the consolidated set is the Orchestrator's, and the content is carried as unnumbered **contributions** `C1`-`C7`. "5 of 5 models" is withdrawn as not reproducible from my table. `model_type` is `other_animal_model` throughout. |
| `R1-MI-INF`, `R1-MI-NOTES` | **ACCEPTED** | Both closing clauses replaced with the sheath-structure scoping; the `inferred` line now carries the split seizure statement. |
| `R1-MI-DNA` | **ACCEPTED** | The target is named as `intervention_direction.do_not_assume`, a single string, and offered as an extension of it rather than a list append; the few-percent juvenile transduction precedent is added. |
| `R1-MI-WO-DATA` | **ACCEPTED** | Both clauses replaced. |
| `R1-MI-WO-WC` | **ACCEPTED — REJECT accepted** | "would be the first result of its kind in this literature" is false. Replaced with "the first of its kind for a neuron-driven lesion measured as sheath structure", with the glial-gene precedent named. |
| `R1-MI-WO-FEAS`, `R1-MI-WINDOW`, `R1-MI-C-NOCHANGE` | HOLDS | Kept, with the review's additions: the two later-than-perinatal external arms, and the fourth window state `symptom_suppression_reversible` named so a proposed fifth can be assessed against the full set. |
| `R1-MI-C01-TML` | **ACCEPTED** | Clause replaced as suggested. |
| `R1-MI-C04-TML` | **ACCEPTED** | Replaced with the split statement, and the card append now says explicitly that a post-onset null must **not** be pre-registered as expected. |
| `R1-MI-C04-NEXTMEAS` | **ACCEPTED — REJECT accepted** | Withdrawn; the card has no such field. The content stays in the work-order `data` append, where it already was. |
| `R1-MI-RANK-NEXTTEST`, `R1-MI-RANK-NOVELTY` | **ACCEPTED** | Myelin clause replaced with sheath structure; the novelty perimeter now states the gene-name anchoring of my queries as the reason three external arms were invisible to them. |
| Review § 1.1, "full text of five records" wording disagrees with the table | **ACCEPTED** | Corrected to four records, and the three `abstract_only` sources are now named (PMID 19211884, PMID 41997465, PMID 32125365). |
| Review § 2 (b), misattributed deviation | **ACCEPTED** | The status-vocabulary note now says the deviation is from `BRIEF_R1.md`, not from `rescue_window_it6_20261029.md`, which defines the vocabulary as timing-only. The four rows that apply my own convention imperfectly (`R67`, `R68`, `R74`, `R75`) are named in the README rather than silently re-labelled. |
| Review § 3 point 4, mis-binning | **ACCEPTED** | `R03` and `R38` (hippocampal long-term potentiation) and `R30` (phosphorylation plus receptor currents) moved from `cognition_behaviour` to `seizure_or_network`, with `endpoint_detail` stating in each that it is not a behavioural endpoint. Both matrices recomputed; `cognition_behaviour` post-onset `full` falls from 6 studies to 3. |
| Review § 3 point 8, two grades too low | **ACCEPTED** | `R53`, `R54` to `full` and `R07` to over-correction. The reviewer is right that this strengthens the case for a cellular structural endpoint in the added arm, which is the direction I had argued against; it is now IPOTESI 5 and 6 unchanged in content but better supported. |
| Review § 5.1, marker read as function | **ACCEPTED** | The readout level now travels with the myelin conclusion in the README, in `C4` of `module_inputs.md`, and in three new rows of the transfer table (readout granularity, glial lesion compartment, biological timing anchor). |
| Review § 5.1, provenance of `R43` | **ACCEPTED as a disclosure, not re-labelled** | `R43` is left at `partial_fulltext` because the sentence quoted is in the audited source, but the README now states that it should not be read as a measurement made there, and `R1-D04` no longer uses it. |
| Review § 5.4, brief consequence row 2 | **ACCEPTED** | Recorded as fired, with its two conditions attached (white-matter level not sheath level; glial lesion not neuron-driven), and credited to the reviewer. |
| Review § 5.4, consequence row 3 | **ACCEPTED** | The author-stated periods now enter the transfer table as a timing-anchor row, and PMID 34135323's third-postnatal-week period is added with its biological anchor. |
| Review § 6, nine missed sources | **ACCEPTED for the four I was instructed to read** (PMID 34369389, 36594817, 34135323, 32125365), all now rows and receipts. The other five are the reviewer's own and are cited in my decision line 1 and in `module_inputs.md` as the reviewer's findings, not re-read by me. |

### The two partial disputes

**D1 · The combined seizure statement of review § 2 (a) needs one clause added, not removed.**
The review places the Ube3a antisense rhythm result in the column where a non-channel gene recovers a
spontaneous **network** endpoint after onset, and then reads my spike-wave prediction as merely "split". I
accept "split" and have rewritten line 5 and the card append accordingly. But I read PMID 36594817 at full
text where the review had the abstract, and the full text reports that **cortical poly-spike frequency — the
study's own epileptiform endpoint — was not reduced at either age** (new row `R86`; the authors' words: "we
were not able to reduce the frequency of poly-spikes ... at either age", with two section headings saying the
same). Spike-wave discharge rate is an interictal **epileptiform** measure, nearer to poly-spikes than to a
power-spectrum ratio. So within that one source the rhythm sub-class recovered after onset and the
epileptiform sub-class did not. The defensible combined statement is therefore split **by sub-class as well
as by mode**: rhythm and provoked-threshold endpoints have recovered after onset in non-channel genes;
the epileptiform sub-class has recovered in one gene (interictal spiking, PMID 31025938) and failed in
another at two ages. This strengthens the review's conclusion that gene class is not the discriminator while
removing a reading in which the WWOX endpoint sits on the recovered side by default.

**D2 · `R1-R50`'s grade.** Stated above: I keep `full` on the Results sentence, record the abstract's weaker
"improved", and note that the row is `EARLY-WINDOW` and excluded from the headline matrix either way.

---

## 3 · What changed, in numbers

| | Before | After |
|---|---|---|
| Rows | 76 | 95 (19 added: 17 from the four new sources, 2 from splitting `R20` and `R22`) |
| Sources | 18 | 22 |
| `role` | support 34, counter 30, context 12 | support 39, counter 38, context 18 |
| `outcome` | full 23, partial 25, none 19, worse 3, not_measured 6 | full 31, partial 33, none 21, worse 4, not_measured 6 |
| Rows corrected in place | - | 24 (the 12 the Orchestrator named, plus the 6 carry-forward notes, plus the 3 re-binned and the 9 of the two re-acquired sources) |
| Queries | 30 | 34 |
| Receipts | 18 | 22, all `validated_ok` with the date in `receipts/INDEX.tsv` |
| Decision lines rewritten | - | 1, 5, 8, 9, 10, plus the status-vocabulary note |

## 4 · What I did not do

- I did not re-read the five sources the reviewer found that were outside my instructed four; they are cited
  as the reviewer's findings with that provenance stated.
- I did not open the primary sources behind `R17`, `R22` and `R78`; all three stay
  `cited_in_source_not_read`.
- I did not view a figure in any source, in either round.
- I did not work around any bot check. One publisher route was tried once for PMID 18495876 and returned
  HTTP 403; it was not retried (`Q34`).
- I did not change `R43`'s depth label, for the reason given above, and I did not change the four rows whose
  `status_vocab` and `age_at_restoration_vs_onset` are in tension; both are disclosed instead.
