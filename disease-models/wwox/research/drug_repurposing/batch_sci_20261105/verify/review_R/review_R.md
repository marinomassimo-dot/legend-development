# Review R — independent review of the conclusions of `r1_restoration_ndd` and `r2_restoration_dee`

Reviewer, not producer. Written 2026-11-05. Non-canonical research material. **Not medical advice**: no dose,
schedule, administration route, preparation or clinical preference appears here for any species; exposure is
described qualitatively only. Public edition — the subject is the WWOX-DEE reference genotype class and no
individual-level record is used. Nothing outside `verify/review_R/` was written; nothing was committed; no
receipt was recorded.

Scope: the conclusions and their consistency. The verbatim quotes of R2 were audited blind by another actor
(`verify/audit_R2/`) and of R1 by another (`verify/audit_R1/`); both are read here and used where a row-level
finding moves a conclusion (§ 1.4). I re-matched no quote to an artefact myself, in either package. Verdicts per statement are in `review_R.tsv`.

---

## 0 · Answer first

1. **Verdict counts over 67 statements: HOLDS 21, NARROW 39, REJECT 7, UNVERIFIABLE 0.** One decision
   statement is rejected outright (R1 decision line 5); six proposals or vocabulary additions are rejected.
   Both blind quote audits had finished by the time this review closed and both are folded in (§ 1.4).
2. **The single largest defect is shared and is a search artefact, not a reasoning error.** Both packages
   conclude that no study has ever restored a gene after onset and measured a myelin endpoint, and both build
   their most consequential recommendation on that emptiness. The emptiness does not survive four independent
   searches. A leukodystrophy model treated **7 months after the stated onset of white-matter vacuolation**
   with a brain-directed gene-addition vector reversed white-matter water accumulation and a progressive motor
   deficit, with an untreated same-genotype comparator and a phenotype documented 2 months before treatment
   (PMID 40051162). A single systemic vector administration **as late as P20** in a leukodystrophy null whose
   lifespan is under one month globally improved CNS myelination (PMID 23817205). Re-expression of the same
   enzyme is reported to reverse dysmyelination, with the effect **blunted in old animals** (PMID 37149081).
   None of the three measures myelin sheath morphometry in a neuron-driven lesion, so the narrow claim
   survives; the headline does not.
3. **The two packages do not actually disagree about seizures; they read two halves of one split.** Post-onset
   recovery of a *spontaneous convulsive* seizure endpoint exists in 2 studies, both ion-channel or
   channel-transcript lesions (1 full, 1 partial). Non-recovery after conditional re-expression exists in 2
   studies, both non-channel (a kinase, a ligase). But the same ligase gene recovers a *spontaneous network*
   endpoint after onset under a different restoration mode in 2 studies neither producer read
   (PMID 34369389, PMID 36594817), and a non-channel synaptic regulator recovers interictal spiking in adults
   (PMID 31025938, in R1's own table). Gene class **correlates** with the split in the four studies the
   packages read and is **not established** as the discriminating factor; it is confounded with restoration
   mode, with endpoint identity and with the level of restoration achieved. See § 2 (a).
4. **R1's decision line 5 is contradicted by R1's own table.** "The one post-onset seizure success is a
   pathway drug" is false against rows R13 and R14 (adult genetic restoration eliminated interictal spiking and
   normalised seizure-induction latency) and against R19; R1's own body paragraph says so. REJECT.
5. **R2's "full" recovery of behaviour and cognition is not what its own rows say.** Sociability only trended
   (R05, graded `partial`, and the blind audit confirms both clauses are in the source), the cellular
   interneuron measure overshot rather than normalised (R07), 2 of 9 treated animals died after the thermal
   challenge with incompletely restored protein (R11), and the adult arm (R09) carries a seizure endpoint only.
   See § 2 (e).
6. **Three headline numbers do not recompute.** R1's two matrices recompute exactly, and its row, source,
   `role` and `worse` counts are all exact. R2's matrix has four membership errors, the largest being a
   survival cell counted as 3 studies where the table supports 2 (the third source's only post-onset survival
   row is `not_measured`). R2's "at P2 survival was prolonged" — in decision line 5, line 7, § 2.4 and
   proposed observation O9 — **has no row in `evidence_r2.tsv`**.
7. **Both packages mis-bin endpoints into `cognition and behaviour`.** In R1, 3 of the 6 rows in the
   post-onset `full` cell are not behaviour (two are hippocampal long-term potentiation, one is substrate
   phosphorylation and receptor currents); in R2 a bulk transcriptome sits there, as the blind audit also
   noted. Both inflate the one cell a consumer is most likely to read as "cognition recovers after onset".
8. **A combined post-onset matrix can be built, and it should be built from `age_at_restoration_vs_onset` and
   `outcome` alone** — not from `status_vocab`, on which the two producers diverge. It is in § 3. The two
   packages share no source, so no study is double counted across them; 30 distinct sources, 141 rows.
9. **The identifier collision is real and blocking**: both packages propose new `observed` entries starting at
   `O7` for the same need, with four ids (`O7`-`O10`) carrying different content, including one pair whose
   headline directions read as a contradiction. A consolidated, non-contradictory set of 8 is in § 4.
10. **Both of R2's vocabulary additions are unnecessary.** `needs/needs.json` already carries
    `human_clinical_report` as a `model_type` (9 observations use it, and the `evidence_scope` note defines
    it), and the four `window_states` in `view/work_order.json` attach to the WWOX entry and the WWOX cards
    only, so a non-WWOX precedent never takes one. See § 2 (d).

---

## 1 · Recomputation of every headline number

### 1.1 R1 — all counts exact

| Claim in `r1_restoration_ndd/README.md` | Recomputed from `evidence_r1.tsv` | Verdict |
|---|---|---|
| 76 rows, 18 sources | 76 rows, 18 distinct `source_id` | exact |
| 30 entries in `queries.tsv` | Q01-Q30 | exact |
| "Counter-evidence (30 rows, `role = counter`)" | support 34, counter 30, context 12 | exact |
| "three rows in the table carry `outcome = worse`" | 3 (R05, R31, R47) | exact |
| Matrix 1, every cell (`studies \| rows` by endpoint class and timing) | reproduced cell for cell | exact |
| Matrix 2, every cell (post-onset arms by outcome) | reproduced cell for cell, taking post-onset as `post_onset_early` + `post_onset_advanced` + `adult` | exact |
| "All eight myelin rows are pre-onset restorations or arms whose onset was never located" | 8 myelin rows: 4 `pre_onset`, 3 `not_stated`, **1 `post_onset_advanced`** (R49) | not exact |
| "Full text of five records" not reachable | exactly 2 sources carry `abstract_only` (5 rows) | wording disagrees with the table |

R1's matrix 2 has no `not_measured` column, which is why the myelin row prints empty: the one post-onset
myelin row, R49, is `outcome = not_measured`. The finding ("myelin was not measured in the one post-onset
seizure arm") is real and is stronger stated than hidden.

### 1.2 R2 — four membership errors in the matrix, and one headline with no row

| Matrix cell in `r2_restoration_dee/README.md` | Recomputed from `evidence_r2.tsv` | Defect |
|---|---|---|
| Survival, RECOVERED: "3 (35013317 full, 36173683 full, 35065785 partial in human early-symptomatic)" | 2 sources (35013317 R01/R11; 36173683 R15/R23). 35065785's only post-onset survival row is R49, `UNMEASURED` / `not_measured` | count inflated by one; the third source contributes no survival result in either direction |
| Seizure or network, pre-onset: "4 (31943325, 39847501, 32848094, 31607539)" | 3 sources. 31607539's single row R63 is `neuronal structure`, `UNVERIFIED`, age `not_stated` | count inflated by one; the same source is also listed in the neuronal-structure cell |
| Cognition and behaviour, pre-onset: "1 (36173683 neonatal) + 1 human" | 1 source (35065785 R48). 36173683 has no pre-onset cognition row; its neonatal rows are growth (R21) and survival (R22) | count inflated by one |
| Motor, RECOVERED: "1 human, partial (35065785)" | 2 sources: 35065785 R46 `none`, and 35715566 R52 `partial` | the outcome label belongs to the source that is missing from the cell; the source named has outcome `none` |
| Neuronal structure, pre-onset: "2 (39847501 PV excitability, 31607539)" | 2 sources but a different pair: 39847501 R41 and 32610343 R28 | membership wrong, count coincidentally right |
| Survival, UNMEASURED/UNVERIFIED after onset | also contains 35065785 (R49) and 37901435 (R62), omitted from the cell | two omissions |
| "Table: 65 rows over 12 sources", "29 entries", "24 of the 65 rows are `role = counter`", "nine sources read beyond the abstract and three at abstract level" | 65 rows, 12 sources, Q01-Q29, counter 24, 9 `partial_fulltext` sources + 3 `abstract_only` | all exact |

**The headline with no row.** Decision line 5 ("worked at P2"), decision line 7 ("pre-onset treatment rescued
survival ... (R40, R41)"), § 2.4 ("At P2 it prolonged survival") and proposed observation O9 ("at P2 survival
was prolonged") all assert a pre-onset survival benefit in PMID 39847501. `evidence_r2.tsv` holds no survival
row for that source at `pre_onset`: its three survival rows are R37, R38, R39, all `at_onset` and all
`UNVERIFIED`. The claim is very likely true of the paper; it is not traceable in the deliverable, and R40/R41,
the rows cited for it, are a seizure-severity row (`partial`, with time to first seizure explicitly unchanged)
and an interneuron-excitability row.

### 1.3 Receipts and internal consistency

* R1 stages 18 receipts for 18 sources, including 2 `abstract_only` receipts, all `validated_ok = yes`.
* R2 stages 9 receipts for its 9 read sources and states in § 8 that the 3 `abstract_only` sources carry no
  receipt. `BRIEF_COMMON.md` § Receipts contemplates an abstract receipt (`source_kind: abstract` "says
  'PubMed record', not PMC"), so the batch is internally inconsistent between the two packages; this is for the
  integrator, not a scientific defect.
* `r2_restoration_dee/receipts/INDEX.tsv` carries `validated_ok = pending` on all nine rows while the README
  asserts "all nine pass `staged_receipt_check.py`". One of the two is wrong.
* `prior_receipt` for PMID 39847501 is correct in both the INDEX and the receipt JSON.

### 1.4 What the two blind quote audits change in these conclusions

Both audits are row-level and mine is conclusion-level; I use them only where a row-level finding moves a
conclusion. `verify/audit_R1/audit_R1.tsv`: 62 triples, SUPPORTED 42, OVERSHOOT 6, UNDERSHOOT 6,
UNVERIFIABLE_SURFACE 8. `verify/audit_R2/audit_R2.tsv`: 64 triples, SUPPORTED 55, OVERSHOOT 7,
NOT_IN_SOURCE 1, UNVERIFIABLE_SURFACE 1.

**Seven R1 rows across two sources are unaudited, not refuted.** R44-R49 (PMID 18389497) and R50
(PMID 18495876) carry full-text sentences the auditor could not reach by any open route, so there was no
surface to match; the audit's own route field records "abstract only; full text unreachable". R1 obtained them
through the PMC article-page page-to-text route it declares in `queries.tsv` Q26, which the audit did not
reproduce. By the module's own rule an all-UNVERIFIABLE result means the artefact is missing, not that the
reading is unsupported: the repair is re-acquisition and a re-audit, and until then these rows should not carry
a conclusion alone. That matters in four places, because those seven rows populate five cells of the matrix:

* R1 decision line 5's third sentence rests on R44 and R47 (the pathway drug and its withdrawal). It was
  already rejected here on other grounds; it is now also the only support for a claim whose rows are unaudited.
* The `worse` count of decision line 7 is arithmetically exact, but one of its three rows (R47) is unaudited.
* Three of the eight myelin rows (R48, R49, R50) are unaudited, and the auditor adds that on the reachable
  abstract surface the one myelin endpoint R1 records as having *moved* under treatment (R50) reads
  **"improved"**, which would be `partial`, not `full`.
* R49, the one post-onset myelin row, carries no quote and could not be checked against a body text at all.

**Three R1 overshoots narrow a conclusion.** R14: wild-type-level seizure-induction latency is reported for
the tonic-clonic stage only, with a large residual effect at the first stage and no genotype effect at the
third — so the genetic post-onset seizure success that refutes decision line 5 rests on R13 (SUPPORTED, interictal
spiking eliminated in the same animals) plus a stage-limited threshold result. R20: the quoted sentence is the
authors' specificity caveat rather than the rescue result, and locomotor correction was present at the longer
treatment duration and absent at the shorter — one more reason the `cognition and behaviour` post-onset `full`
cell is softer than it reads. R57-R59: the follow-up field should be postnatal day 16, not beyond 12 weeks, and
the "myelin thickness" readout is the thickness of myelin basic protein immunostaining — a marker measure,
which is exactly the readout level R1's own transfer table excludes.

**Four R1 undershoots strengthen conclusions R1 graded conservatively**, and none of them rescues a statement
this review narrows: R53 and R54 (the Mecp2 morphology result is `full` for soma size, dendritic length and
spine density, with a significant treatment effect and the exceptions being cortical thickness and dendritic
complexity at 2 of 11 radii), R07 (the Shank3 spine result is over-correction above wild type, not incomplete
correction), R25 (all four named behavioural endpoints of the six-week Cdkl5 arm were rescued; `partial` applies
only to a bundle containing working memory, which sharpens decision line 6), R04 (body weight `full`).

**One R1 row is confirmed as a second-hand account.** R22's audit says in terms that it is the audited source
reporting a cited study and that `outcome = none` erases the positive arm, since rescue did occur when
treatment began at birth and failed only from the six-week start. R17 and R43 were audited SUPPORTED, which
answers the quote question and not the provenance question: both sentences are the citing paper reporting
earlier work, R1 declares R17 as `cited_in_source_not_read` and does not declare R43.

**The R2 audit's findings are folded into § 2 and § 3** where they change a reading: R62 is a pre-onset arm
(the model's single lethal seizure follows the dosing age), R13's "163" is a treatment-effect count and not a
residual-defect count, R18's `worse` grade is contested by the source's own next sentence, R31's germline arm
increased myelination to about half of wild type rather than restoring it, R28's dissociation is asserted and
not in the source, R48's "20 of 25" is the whole assessed treated cohort, R55's sixfold magnitude is a figure
reading, R58 carries no quote, and R16's seizure-frequency locator is mis-assigned to a survival sentence.

---

## 2 · The cross-package points, settled

### (a) Seizure endpoints: what the combined, defensible statement is

**The disagreement is partly real and partly an artefact of pooling different endpoints into one class.**
Decomposing the combined `seizure_or_network` post-onset rows of both tables by what was actually measured:

| Endpoint actually measured, after onset | Studies | Outcome | Gene class |
|---|---|---|---|
| Spontaneous convulsive seizures on continuous video-EEG | 1 (PMID 35013317) | full, in a P30 arm on animals selected for seizing and in a P90 arm with a within-animal 2-week baseline | channel (silenced Scn1a allele restored) |
| Spontaneous seizure frequency and interictal spikes | 1 (PMID 36173683) | partial | channel transcript (gain-of-function silenced) |
| Epileptic spasms, late arm | 1 (PMID 39855191) | none, against a reduction in the early arm, 2 alleles and 2 Cre drivers | kinase (Cdkl5) |
| Audiogenic seizure susceptibility after Cre-reactivation | 1 (PMID 25866966) | none | ligase (Ube3a) |
| Interictal spiking and provoked seizure threshold, adult restoration, same animals before and after | 1 (PMID 31025938) | full | synaptic GAP/scaffold (Syngap1) |
| Audiogenic seizure susceptibility under a pathway drug or an antiseizure drug | 2 (PMID 22500629, PMID 25866966 R39) | full but intervention-dependent; returns on withdrawal | not restoration |
| **Not read by either producer:** audiogenic seizure susceptibility after antisense reactivation of the same locus at P21 | 1 (PMID 34369389, abstract) | "a full rescue of sensitivity to audiogenic seizures" at P1 and at P21 | ligase (Ube3a) |
| **Not read by either producer:** electroencephalographic rhythm and sleep architecture after antisense reactivation in juveniles and adults | 1 (PMID 36594817, abstract) | rescued; "the degree of phenotypic improvement correlates with the increase of Ube3a protein levels"; authors state the window is "broader than previously thought" | ligase (Ube3a) |

**Combined statement, defensible as written.** *Post-onset restoration has recovered a spontaneous convulsive
seizure endpoint in two models, both channel or channel-transcript lesions, one of them fully and with a
within-animal pre-treatment recording. In non-channel genes the post-onset result splits by endpoint identity
and by restoration mode rather than by gene class: conditional re-expression left epileptic spasms and
audiogenic susceptibility unmoved in two models, while adult conditional re-expression abolished interictal
spiking in one, and antisense reactivation of the same locus as one of the two negatives rescued audiogenic
susceptibility at P21 and the electroencephalographic rhythm phenotype in juveniles and adults. Two studies
support each side as the producers framed it; adding the two antisense studies puts the same gene on both
sides. The factor that tracks the outcome across all of them is the level and distribution of restoration
achieved — measured and correlated with improvement in one study, named by its own authors as the explanation
of a later-age failure in another, and present as a stated transduction threshold in two more — together with
whether the endpoint is continuously generated excitability or a developmentally established seizure
phenotype. Gene class is correlated with the split and is not established as its cause.*

**Where WWOX falls.** WWOX is a WW-domain, oxidoreductase-domain adaptor with no channel function; its
neuronal deletion reproduces the phenotype and the carried endpoint is spike-wave discharge rate. It falls on
the **non-channel** side, with Cdkl5, Ube3a and Syngap1 — so R2's two post-onset seizure successes are the
least transferable part of its package, and R2's own § 6 says this. But spike-wave discharge rate is an
interictal, spontaneous *network* measure, which is precisely the sub-class in which a non-channel gene **has**
recovered after onset (Syngap1 interictal spiking; the Ube3a antisense rhythm result). R1's "the prediction
most at risk" should therefore read **"the prediction whose external precedent is split"**: it is not
contradicted by the precedents, it is unresolved by them.

### (b) The status vocabulary, and whether a combined matrix can be built

**R1 misattributes its own deviation.** `rescue_window_it6_20261029.md` defines the vocabulary at its lines
26-29 as **"PREVENTED (intervention precedes the phenotype), RECOVERED (intervention follows a manifested
phenotype), EARLY-WINDOW ..., UNMEASURED, UNVERIFIED"**. That definition is timing-only and does not embed
movement — it is the same reading R1 adopted. What embeds movement is (i) that file's *summary-table column*
("RECOVERED after manifestation") and its usage lines ("Nothing RECOVERED", "no RECOVERED endpoint"), and
(ii) `BRIEF_R1.md`, which restates RECOVERED as "restoration follows a manifested phenotype **and the endpoint
moves toward control**". R1's flagged deviation is therefore from **the brief**, not from
`rescue_window_it6_20261029.md`, and R1's note names the wrong document as the one it differs from.

**Both producers apply their own convention imperfectly.** 5 rows have a `status_vocab` that contradicts their
own `age_at_restoration_vs_onset`: R1 R67, R68, R74, R75 are `RECOVERED` with age `not_stated` (two of them a
transgene bypass, two an abstract-only pathway drug), and R2 R45 is `RECOVERED` with age `pre_onset`.

**Answer: yes — and the combined matrix must be built from `age_at_restoration_vs_onset` and `outcome`
alone.** Those two columns use the same closed value sets in both files (`outcome`: full, partial, none, worse,
not_measured; `age`: the brief's six values, R2 additionally using `at_onset`), they are populated independently
of the `status_vocab` disagreement, and they carry exactly the two facts the challenge needs. Three conditions:
(i) `endpoint_class` must be normalised, because R1 writes `seizure_or_network`, `cognition_behaviour`,
`myelin_glia`, `systemic_metabolic`, `neuronal_structure` and R2 writes the same classes in prose; (ii) rows
whose age is `not_stated` leave the matrix, which drops 12 R1 rows and 3 R2 rows and with them 2 whole R1
sources; (iii) `at_onset` must be shown separately, because the blind audit of R2 found that its only
non-null-model `at_onset` row (R62) is in fact a pre-onset arm — the model's single lethal seizure occurs at
P14 and dosing began at P10.

### (c) The `O7`-`O10` identifier collision

`needs/needs.json` has `NEED-WWOX-GENE-ADDITION` with observations `O1`-`O6`. R1 proposes `O7`-`O10`; R2
proposes `O7`-`O12`. **Four identifiers collide, each carrying different content**, and one pair reads as a
contradiction if both are applied as written: R1's `O8` records `direction_observed` "prevented but not
recovered" for seizures, R2's `O7` records complete post-onset rescue of spontaneous seizures. Content
duplication: R1's `O9` and R2's `O10` are the same myelin conclusion from different sources; R1's `O7` and
R2's `O7`/`O8` overlap on the endpoint-class split. Vocabulary defects on both sides: R1 proposes
`model_type: other_disease_model`, a value the file does not use (it uses `other_animal_model`, as in O4 and
O5); R2 proposes a new value for the human rows when `human_clinical_report` already exists. The consolidated
set of 8 is in § 4.

### (d) R2's two vocabulary additions: both unnecessary

**`model_type` for a human clinical precedent — REJECT.** `needs/needs.json` already carries
`human_clinical_report` on 9 observations, and its `vocabularies.evidence_scope` text defines it ("model_type
`human_clinical_report` marks an uncontrolled case or series"). Both human sources here are uncontrolled in
the randomisation sense — one single-arm against a matched natural-history cohort, one single-centre with a
historical comparator — so the existing value fits. `model_type` is not declared as a closed vocabulary in
`vocabularies`, so adding a near-synonym would fragment it for no gain. Whether a cohort came from a
registered trial or a case series is a `limits` sentence.

**A fifth `window_state` — REJECT.** The four states live in `view/work_order.json` as `window_states` and are
attached to the WWOX need entry's `window_state` list and to `card_windows` for `C01_aav9_wwox` and
`C04_aav9_endpoint_families`. By the module's own rule — which R2 itself states twice — a non-WWOX observation
never changes or takes a window state, so the proposed `attempted_post_onset_uninterpretable` would have no row
to hold: both of its intended occupants are external precedents, and one of them (R62) turns out to be a
pre-onset arm. The fact R2 wants to preserve is already carried twice over, by `status_vocab = UNVERIFIED` on
the row and by the observation's `limits`. If a WWOX arm is ever run after onset without measuring the
restoration achieved, add the state then and gloss it as applying to WWOX arms only.

### (e) R2's "full" recovery of behaviour and cognition

Against R2's own rows, and with the blind audit confirming each quote: **cognition** (radial-maze working
memory, water-maze spatial learning and reversal) is `full` (R04); **behaviour** is not. Sociability recovered
chamber preference but the index "show[ed] a trend toward the recovery" (R05, graded `partial`, audit
SUPPORTED, "both clauses present in the quote"). The cellular interneuron measure did not normalise: fast-
spiking cells overshot and non-fast-spiking cells became more excitable than both other groups, and the authors
themselves separate phenotype-level recovery from the cellular measure (R06, R07). Survival is `full` for
sudden death over four months (R01) but 2 of 9 treated animals died after the thermal challenge with protein
incompletely re-established (R11, `partial`). The adult arm (R09) carries the seizure endpoint only; no
behaviour, cognition or survival endpoint is reported for it. The transcriptome element is cortical only — the
audit found that the hippocampal "163" R2 carried is a treatment-effect count, not a residual-defect count.
**"Fully" is the authors' phenotype-level word and must not be carried as an endpoint-by-endpoint grade.**

---

## 3 · The combined post-onset matrix

Both tables, rows with `age_at_restoration_vs_onset` in {`at_onset`, `post_onset_early`,
`post_onset_advanced`, `adult`}, `endpoint_class` normalised, **studies counted once per source per cell**
(`studies | rows`). The two packages share no source, so nothing is double counted across them. Not a
meta-analysis: the models differ in gene, lesion class, species and lifespan, and the literature selects for
success, so the `none` and `worse` cells are under-counted.

| Endpoint class | full | partial | none | worse | not_measured |
|---|---|---|---|---|---|
| survival | 2 \| 2 | 4 \| 4 | 2 \| 3 | 2 \| 2 | 2 \| 2 |
| seizure_or_network | 6 \| 10 | 4 \| 5 | 2 \| 3 | - | - |
| motor | 1 \| 1 | 3 \| 3 | 3 \| 3 | - | 1 \| 1 |
| cognition_behaviour | 7 \| 7 | 7 \| 10 | 6 \| 8 | 1 \| 1 | - |
| neuronal_structure | 2 \| 2 | 4 \| 5 | 2 \| 2 | - | 1 \| 1 |
| **myelin_glia** | **1 \| 1** | **1 \| 1** | **-** | **-** | **1 \| 1** |
| systemic_metabolic | - | 3 \| 3 | - | - | - |

Sources per cell, so the matrix can be audited:

* survival — full: 35013317 (R01), 36173683 (R15); partial: 17289941 (R01), 18389497 (R45), 35013317 (R11),
  36173683 (R23); none: 39847501 (R37, R38), 37901435 (R62); worse: 18389497 (R47), 34651584 (R31);
  not_measured: 35065785 (R49), 39847501 (R39).
* seizure_or_network — full: 22500629 (R19), 25866966 (R39), 26886798 (R08), 30082419 (R41, R42),
  31025938 (R13, R14), 35013317 (R02, R03, R09); partial: 18389497 (R44), 35013317 (R10, R14),
  36173683 (R16), 39855191 (R28); none: 25866966 (R37), 39855191 (R23, R24).
* motor — full: 25866966 (R34); partial: 22525157 (R56), 26886798 (R12), 35715566 (R52); none: 25866966 (R35),
  26886798 (R10), 35065785 (R46); not_measured: 35013317 (R12).
* cognition_behaviour — full: 17289941 (R03), 22500629 (R20), 25866966 (R38), 26886798 (R09), 31025938 (R15),
  34651584 (R30), 35013317 (R04); none: 25866966 (R36), 30082419 (R43), 31025938 (R16, R17), 34651584 (R32),
  39855191 (R26, R27), 41509287 (R71); worse: 36173683 (R18).
* neuronal_structure — full: 22500629 (R18), 35013317 (R06); partial: 18389497 (R46), 22525157 (R53, R54),
  26886798 (R07), 35013317 (R07); none: 22500629 (R22), 22525157 (R55); not_measured: 34651584 (R33).
* myelin_glia — full: 35013317 (R08, astrogliosis, a glial not a myelin endpoint); partial: 35065785 (R47, a
  composite magnetic-resonance white-matter and atrophy severity score in humans); not_measured:
  18389497 (R49).

**Six readings of the matrix that neither README states.**

1. **`at_onset` carries three of the four survival non-successes.** Excluding `at_onset`, the survival `none`
   cell empties and `not_measured` falls to one study. The blind audit moves R62 to pre-onset, so the `none`
   cell rests on one source (39847501) treated at onset in a null that dies in the third week.
2. **The myelin row has no sheath measurement after onset in either package** — one glial endpoint, one human
   composite imaging score, one explicit non-measurement. That part of both packages' conclusion holds; what
   does not hold is the generalisation to the literature (§ 0.2).
3. **The `seizure_or_network` `full` cell is heterogeneous** and must be decomposed before use (§ 2 (a)): of
   its 6 studies, one measured spontaneous convulsive seizures, two measured slice or in-vivo physiology
   without a seizure endpoint, two used drugs, one measured interictal spiking.
4. **The `cognition_behaviour` `full` cell is inflated by mis-binning** in both packages: R03 and R38 are
   hippocampal long-term potentiation, R30 is substrate phosphorylation plus receptor currents, R13 is a bulk
   transcriptome. Removing them leaves 4 studies with a genuine learning, memory or social endpoint recovered
   after onset.
5. **Two of R1's rows are another study's finding carried under the citing paper's `source_id`** — R17 and
   R22, both declared `cited_in_source_not_read`. R22 is the only occupant of the `neuronal_structure` `none`
   cell for its source, so that cell attributes a third party's result to PMID 22500629. R43 has the same
   provenance problem (its own `endpoint_detail` says "from the same group's earlier work") but is labelled
   `partial_fulltext`, not `cited_in_source_not_read`, and it is one of the two rows behind R1's "clean case"
   reading of the Angelman dissociation.
6. **`worse` after onset is one row in 141** (R18) and the blind audit found its grade contested by the
   source's own next sentence, which reads the same change as a normalised disease marker. The methodological
   lesson R2 draws from it — that a treated wild-type arm is indispensable — is strengthened, not weakened, by
   the dispute.
7. **Seven rows in five cells are unaudited for want of an artefact** (§ 1.4): PMID 18389497 contributes the
   `seizure_or_network` `partial` cell, one `survival` `partial` row, the `neuronal_structure` `partial` cell
   and the only `myelin_glia` `not_measured` row, and one of the two `survival` `worse` rows; PMID 18495876
   contributes the one myelin row R1 records as having moved under treatment, which reads `partial` rather than
   `full` on the surface the auditor could reach. No cell of the matrix should be quoted without that caveat,
   and three of them have no other occupant.
8. **Two grades in the matrix are now known to be too low** and they both run in the direction R1 argued
   against: the Mecp2 cellular-structure rows belong in `full` rather than `partial`, and the Shank3 spine row
   is an over-correction above wild type. Moving them makes `neuronal_structure` after onset the second
   best-supported class in the table, behind `seizure_or_network`, which strengthens the case for measuring a
   cellular structural endpoint in the added arm and weakens nothing in this review.

---

## 4 · One consolidated observation set, 8 entries

For `needs/needs.json`, `NEED-WWOX-GENE-ADDITION`, continuing after `O6`. All eight take
`evidence_scope: OTHER_DISEASE_PRECEDENT`; `model_type: other_animal_model` for the animal entries and the
existing `human_clinical_report` for O13 and O14; `readout_level` stated per entry and never promoted. None of
them changes a `window_state`, by the module's own rule. Replaces both producers' proposals; the row ids after
each entry are the evidence rows it rests on.

| Id | Proposed statement, corrected | `readout_level` | Rests on |
|---|---|---|---|
| `O7` | "External precedent, endpoint-class split across 30 single-gene models in two bounded searches: after a manifested phenotype, non-seizure electrophysiological endpoints recovered fully in 5 of 5 models that measured them; learning, memory or social endpoints recovered fully in 4 models and failed in 6; cellular structural endpoints moved in 6 models and failed in 2; tissue-level structure failed where it was measured. Failures are reported inside otherwise positive papers, so the negative cells are under-counted." | `functional` | R1 R03, R07-R09, R13-R16, R18-R20, R29, R34-R38, R41-R43, R53-R56; R2 R04-R07 |
| `O8` | "External precedent, spontaneous seizure endpoints after onset: complete rescue in one conditional channel model treated after manifest seizures and again in adults with a within-animal two-week baseline, partial in one channel-transcript model treated while symptomatic; no recovery in a kinase model (epileptic spasms, late arm, two alleles) or in a ligase model (Cre-reactivated allele). In the same set an adult conditional restoration of a synaptic regulator eliminated interictal spiking, measured in the same animals before and after." | `functional` | R2 R01-R03, R09, R16; R1 R13, R14, R23, R24, R37 |
| `O9` | "External precedent, the same question under a different restoration mode: antisense reactivation of the ligase locus whose Cre-reactivation left seizures in place gave a full rescue of audiogenic seizure susceptibility at P21, and rescued the electroencephalographic rhythm and sleep phenotype in juveniles and adults, with the degree of improvement correlated to the protein level reached. Abstract level only; methods, comparators and ages beyond those stated were not read." | `functional` | new: PMID 34369389, PMID 36594817 (abstract only, this review) |
| `O10` | "External precedent, myelin and white matter: no study in either bounded search restored or corrected the gene after a documented onset of a myelin phenotype and then measured myelin sheath structure; the two reachable hypomyelination models were both treated before onset and the sheath moved least in both, reaching about a tenth of control with reduced compaction in one and remaining below control in the other, while oligodendrocyte number, apoptosis, glial markers, respiration and lifespan moved far more. Outside those gene families the class is not empty: an astrocyte-directed vector given seven months after the stated onset of white-matter vacuolation reversed white-matter water accumulation and a progressive motor deficit against an untreated same-genotype comparator; a single systemic administration as late as P20 in a leukodystrophy null with a lifespan under one month globally improved CNS myelination with residual lipid abnormalities; and re-expression of the same enzyme is reported to reverse dysmyelination with the effect blunted in old animals. None of the three measured sheath morphometry, all three correct a glial or metabolic lesion rather than a neuronal one, and two are abstract level." | `functional` | R1 R49-R52, R57-R59, R74, R76; R2 R24-R31, R47, R54-R59; new: PMID 40051162, PMID 23817205, PMID 37149081 |
| `O11` | "External precedent, the age cliff and what it is evidence of: in a null of a DEE gene dying in the third postnatal week, a brain-directed vector reduced seizure severity without changing time to first seizure and fully restored parvalbumin interneuron and pyramidal excitability at P2, while at P10, at twice the exposure, all eight treated null animals died in the usual window. Its authors attribute the later failure to transgene level and distribution, not to irreversibility, citing other studies and their own unpublished work for sharply reduced rodent CNS expression after the first postnatal days; the restoration achieved at the later age was never measured, so biology and vector kinetics are not separated. The generalisation is route- and capsid-specific: a single systemic administration at P20 rescued lethality in another short-lived null, and a systemic vector given at four to five weeks in a null that is symptomatic by then produced low transduction, about one neuron in twenty-five to fifty, and still a measurable survival benefit." | `functional` | R2 R37-R41; new: PMID 23817205, PMID 23011033 (abstract only, this review) |
| `O12` | "External precedent, the cost of restoring and the cost of the modality: abrupt widespread reactivation of the deficient gene killed animals selectively in the restored genotype in two independent models, and both groups moved to a graded induction because of it; a pathway drug's benefit reversed when it was withdrawn. The hazard is specific to abrupt conditional reactivation, not to gene addition as such: modest vector-mediated overexpression in wild-type brain was tolerated in two sources. Separately, two interventions changed behaviour in treated wild-type animals, so without a treated wild-type arm an intervention effect is scored as a rescue; in one of them the source's own reading of that change is benefit rather than harm, so its direction is contested." | `functional` | R1 R05, R31, R47; R2 R18, R19, R44; new: PMID 23011033 |
| `O13` | "Human timing precedent, spinal muscular atrophy, single-administration vector replacement: treated before symptom onset, 14 of 14 infants sat independently for at least 30 seconds and 11 within the normal developmental window, and all were alive and free of permanent ventilation at 14 months, against none of 23 and 6 of 23 in a matched untreated natural-history cohort; even pre-symptomatically 5 of 14 were below the normal gross-motor range at 18 months. The symptomatic comparison, 64 and 44 percent reaching the same endpoint and months later, is a cross-trial secondary statement inside this report whose authors flag differing design, endpoints and eligibility; the symptomatic primary reports were not read. Never a WWOX expectation: a lower motor neuron disease with a peripheral endpoint, no seizure, interneuron or myelin endpoint, and a pre-symptomatic route that depends on newborn screening that does not exist here." | `clinical` | R2 R50-R53 |
| `O14` | "Human timing precedent, metachromatic leukodystrophy, ex-vivo lentiviral haematopoietic gene therapy: across the assessed treated cohort, which included early-symptomatic children, 20 of 25 showed normal acquisition of cognitive skills at ages at which the untreated cohort was severely impaired, and treated groups exceeded a matched untreated cohort on gross motor function; the magnetic-resonance white-matter and atrophy score stabilised in every treated group but plateaued at a worse level when treatment followed symptoms, and children entering the rapid progression phase did not benefit at all, two dying of progression with engraftment and enzyme levels normal. Never a WWOX expectation: benefit arrives by cross-correction from engrafted donor-type myeloid progeny rather than restoration in the affected neural cell, with a months-long latency; no randomised comparator; a composite imaging severity score is not a myelin measurement." | `clinical` | R2 R45-R49 |

Three further corrections the integrator must carry with the set: the `inferred` line proposed by both
producers must say "myelin sheath structure after onset" and not "myelin", because of `O10`; the
`do_not_assume` text proposed by R1 belongs inside `intervention_direction.do_not_assume`, which is a single
string and not a list; and R1's proposed append to a `next_measurement` field of `C04_aav9_endpoint_families`
has no target, because the card's `p4_fields` are `endpoint_pursued`, `functional_evidence_available`,
`temporal_or_model_limit` and `cellular_context` — the same content already sits in R1's own proposed append
to the work-order `data` field.

Four corrections inside the set follow from the two blind audits and must travel with it. In `O10`, the
lineage-restriction clause must say that the structural readout is the thickness of myelin basic protein
immunostaining measured at postnatal day 16, not myelin thickness beyond 12 weeks, and the clause about the
one myelin endpoint that moved under treatment must be graded `partial` and marked unaudited pending
re-acquisition of that full text. In `O12`, the third element — a pathway drug's benefit reversing on
withdrawal — rests on an unaudited row and must be marked as such. In `O7`, the two Mecp2 cellular-structure
rows count as `full` rather than `partial` and the Shank3 spine row as an over-correction, while the Fmr1
behavioural row must be re-located to its result sentence and carry the duration dependence. In `O8`, the
provoked-threshold element reached wild-type level at the tonic-clonic stage only.

---

## 5 · Overreach, selection, transfer conditions, consequences

### 5.1 Overreach found (beyond § 1 and § 2)

* **Marker read as function, both packages.** R1's transfer-condition table forbids "marker intensity or
  transcript share only" as a readout level and then carries a myelin row whose readouts are two myelin protein
  levels (R57, R58) and an abstract-level molecular myelin phenotype (R74) as the evidence that lineage-
  restricted restoration leaves myelin wrong. The conclusion is right; the readout level must travel with it.
  The blind audit of R1 settles the point: the third readout in those rows, carried as "myelin thickness", is
  the thickness of myelin basic protein immunostaining in the corpus callosum, measured at postnatal day 16,
  with no electron microscopy in that source.
* **"Statistically indistinguishable" read as equivalence — half conceded.** R1's decision line 2 reports that
  soma size, dendritic length and spine density "became statistically indistinguishable from wild type", sourced
  to a row whose quote is "all parameters were not significantly different from their respective age-matched,
  wild-type controls", which R1's own IPOTESI 9 forbids reading as equivalence. The blind audit of R1 answers
  half of the objection: the source also reports a *significant treatment effect* for those three parameters,
  so there is a treatment-effect claim behind the sentence and the row's `partial` grade understates it. What
  survives is the comparator caveat in R1's own counter-evidence section — the study had no untreated
  same-genotype arm surviving to the measurement, which its authors say hinders a treatment-effect
  interpretation — and the two named exceptions, cortical thickness and dendritic complexity at 2 of 11 radii.
* **A pathway drug carried in a restoration sentence.** R1's decision line 2 lists a mGlu5-inhibitor spine
  result beside two genetic restorations without marking it; the same study's drug "also had a proportional
  effect on WT mice" (R20) and a result cited inside it reports spine rescue only when treatment began at
  birth (R22).
* **Species and age mapping.** R2 § 5 states that the P30 and P90 mouse ages are mapped by the source's authors
  to roughly 4 and 20 human years "with citations", and immediately says no human age follows for WWOX. The
  hedge is present and correct; the mapping should not appear in a card field without it.
* **Provenance, three places.** R2's decision line 6 attributes to the authors a general statement about
  rodent vector expression that the row itself describes as "other studies and the authors' unpublished work";
  R2's decision line 8 presents a cross-trial secondary statement as "the same intervention and endpoint"; R1's
  R43 carries a cited dissociation at full-text depth.

### 5.2 Selection: what the bounded queries could not see

* **R2's myelin queries are anchored on gene and syndrome names** — `hypomyelination`, `Pelizaeus`, `jimpy`,
  `shiverer`, `Plp1`, `Mbp` (Q16, Q20, Q23). No string could reach a leukodystrophy caused by an enzyme
  deficiency (Canavan, metachromatic), by a connexin, by a tubulin or by an astrocyte transporter. All three
  post-onset white-matter arms I found sit in exactly those families, and so does the second antisense
  hypomyelination precedent the brief asked for by name (PMID 41566774, a tubulin leukodystrophy: lifespan,
  motor and seizure improvement, with myelin and oligodendrocyte loss **prevented** — which supports R2's
  direction while adding a model it did not have).
* **R1's interneuron query required `adult[tiab]` and an autism, Rett or neurodevelopmental term** (Q16), so
  it could not see interneuron measurements in DEE models, in non-adult arms, or under `Pvalb`, `GABAergic`,
  `cell density` or `cell number` wording. Its "interneuron number is UNMEASURED in every source found" stands
  as a bounded null, but with a narrower net than the sentence implies. My own search found no post-onset
  interneuron **count** either, which corroborates it; it did find an author-stated **sensitive period** for an
  interneuron **structural** endpoint in one of R1's own assigned gene families (PMID 34135323: treatment
  confined to the third postnatal week rescued parvalbumin cell perisomatic innervation and social behaviour
  measured in adults), which is a missing critical-period row.
* **R1's gene list excluded the DEE and leukodystrophy space by design and R2's excluded the syndromic space**,
  which is the batch's design and not a defect — but it means neither producer could see that Cdkl5, the kinase
  behind R1's strongest "preventable not recoverable" claim, also has a vector gene-replacement study with a
  post-neonatal arm (PMID 32125365: intrajugular delivery at 28 to 30 days, significant behavioural
  improvement, with a cerebellar structural abnormality corrected in high-expression regions).

### 5.3 Transfer conditions and breakers

R1's nine-row table is the stronger of the two and is pertinent as written; its "Timing anchor" and
"Comparator" rows are exactly the two conditions that the post-onset white-matter precedent I found satisfies
(onset located 7 months before treatment; untreated same-genotype comparator; phenotype documented 2 months
before treatment) and that most of R1's own post-onset rows do not. Three gaps:

* **No readout-granularity row.** The table forbids marker-only readouts but has no row separating a
  *composite imaging severity score* from *sheath morphometry* from *myelinated-axon counts*. Without it, R2's
  human white-matter row (R47) and the module's own electron-microscopy counts sit at the same level, and the
  post-onset white-matter reversal I found cannot be graded against either.
* **No lesion-compartment row on the glial side.** Both packages state the breaker in prose (the WWOX driver
  is neuronal, lineage deletion is phenotypically silent) but neither makes it a table row, and it is the
  single condition that disqualifies all three of the post-onset white-matter precedents.
* **R2 has no transfer table**, only a prose § 5. Its seven conditions are sound and two of them are sharper
  than R1's (modality: loss cannot be corrected by knockdown of anything; direction of a window cuts both
  ways), but they are not joined per row, so a consumer cannot filter rows by them as `transfer_conditions` and
  `transfer_breakers` in the TSV allow.

### 5.4 The consequences tables: applied as pre-registered?

| Brief row | Applied? |
|---|---|
| R1 row 1, endpoint-class split returns | **Yes**, and honestly labelled "half right and half unsupported". |
| R1 row 2, "at least one well-controlled model shows myelin or interneuron structure recovering after onset" → record "recovery of structural endpoints after onset is not excluded" with that source and its conditions | **Not applied, and now triggered.** R1 found none and recorded the class as empty. PMID 40051162 meets the row's condition at the white-matter level with a located onset and an untreated comparator, though not at sheath level and not in a neuron-driven lesion. This is the one pre-registered consequence the batch owes. |
| R1 row 3, an author-stated critical period becomes a transfer condition with its anchor | **Partly.** The periods are listed in prose (3 to 6 weeks; P14; P20 to P21) but none entered the transfer-condition table as a timing condition with its anchor, and PMID 34135323's third-postnatal-week period is missing. |
| R1 row 4, nothing reachable → UNMEASURED with the queries | **Yes** (myelin, interneuron number, with query ids). |
| R2 row 1, seizure and interneuron endpoints recover → an external-precedent line on the **window states** | **Declined with a stated reason**, correctly: non-WWOX observations do not change window states, so the content went to `inferred` and `notes` instead. The brief's pre-registered action conflicted with the module rule; the substitution is the right call and is disclosed. |
| R2 row 2, myelin only before the myelination peak → the peak and its anchor become a transfer condition | **Yes**, with the anchor imported from the IT29 P3-C row set rather than sourced here, and R2 says so. |
| R2 row 3, human stage dominance stated with limits, never as a WWOX expectation | **Yes**, and the limits are the most careful part of the package. |
| R2 row 4, UNMEASURED with queries | **Yes**, with bounds and record counts. |

### 5.5 Answer-first sentences that read as advice or as a ranking

Both § 4 lists are labelled IPOTESI and are addressed to an internal investigation's design, which the briefs
asked for, so neither crosses into clinical advice; no dose, schedule or route appears in either package, and
exposure is described qualitatively throughout ("twice the exposure", "high-dose arm"). Two sentences should
still lose their imperative: R2's "the added arm should be **powered on** seizure and network endpoints"
(decision line 10) and "**expect** the myelin endpoint to show arrest at best and score it as such" (the
proposed ranking append) read as a ranking of endpoints to pursue; with `O10` the second is also no longer
supported, and both should be written as conditionals with their precedent attached.

---

## 6 · Sources the producers missed, with their routes

All found through NCBI E-utilities `esearch`/`esummary`/`efetch` and, for one, the Europe PMC REST
`fullTextXML`. No contact address was sent to any service, no account, no registration, zero spend. Four
searches are logged below with their exact strings and timestamps; two further confirmatory searches are
listed. Depth is stated per source: five are `abstract_only` to me, one was read as open full text in two
question-directed passes and no figure was viewed.

| PMID | What it is | Depth here | Which conclusion it changes |
|---|---|---|---|
| 40051162 | Astrocyte-directed vector given to 10-month-old nulls of an astrocyte-specific leukodystrophy gene, stated by the authors as "7 months after CWM vacuolation onset" and a "post-symptomatic strategy"; white-matter water accumulation normalised on in-vivo imaging, locomotor deficits reverted, both motor tests already discriminating treated from untreated animals "at 8 months of age, 2 months before treatment"; no electron microscopy and no g-ratio in the paper | open full text, two passes, no figure viewed | R1 D01, D09, D10; R2 D04, D09 and the matrix cell "myelin sheath after onset: 0 sources"; R1 brief consequence row 2 |
| 23817205 | Single systemic vector administration "as late as P20" in a leukodystrophy null with a lifespan under one month: "completely rescued their early lethality", "globally improved CNS myelination, although some abnormalities persisted in the content and distribution of myelin-specific and -enriched lipids" | abstract only (the body is not open at PMC for this record) | R1 D01/D09; R2 D06 (the post-P3-P4 generalisation); R1 transfer-breaker 1 (lifespan forbids the design) |
| 37149081 | Re-expression of the same enzyme; oligodendrocyte and neuronal lineage markers "either improved or normalized"; "this effect of ASPA re-expression is blunted in old mice" | abstract only | R1 D01/D09/D10; R2 D04/D09; supplies an author-stated age dependence for a myelin-lineage endpoint |
| 34369389 | Antisense reactivation of the ligase locus at P1 or P21: "a full rescue of sensitivity to audiogenic seizures" at both ages; no rescue of marble burying or nest building | abstract only | R1 D05/D08 and the "preventable not recoverable" pillar; cross-package point (a) |
| 36594817 | Antisense reactivation in juvenile or adult animals rescues the electroencephalographic and sleep phenotype; "the degree of phenotypic improvement correlates with the increase of Ube3a protein levels"; authors state the therapeutic window is "broader than previously thought" | abstract only | R1 D05/D08/D09; R2 D10 (it is the direct evidence for "measure the restoration achieved"); cross-package point (a) |
| 23011033 | Vector gene transfer to neonatal **and juvenile** nulls of a short-lived model: at four to five weeks, "brain transduction efficiency in juvenile mice was low (~2-4% of neurons)" yet "modest improvements in survival were still observed"; neonatal injection of the same vector into wild-type animals produced no significant deficit | abstract only | R2 D06; R1 D07 and transfer-breaker 6 (the lethality is specific to abrupt conditional reactivation, not to gene addition); R1 transfer-breaker 1 |
| 41566774 | The second antisense hypomyelination precedent `BRIEF_R2.md` asked for by name, in a tubulin leukodystrophy: lifespan extended, motor phenotypes improved, seizures reduced, and treatment "**prevents** myelin and oligodendrocyte loss" and recovers visual evoked potential latencies | abstract only | supports R2 D04's direction with a model it did not have; adds a non-channel gene whose seizure endpoint improved |
| 34135323 | An author-stated sensitive period "during the third postnatal week" during which pathway inhibition rescues parvalbumin cell innervation and social behaviour measured in adults, in one of R1's own assigned gene families | abstract only | R1's critical-period section and brief consequence row 3; the interneuron-structure half of R1's "UNMEASURED" claim |
| 32125365 | Vector gene replacement for the kinase behind R1's strongest negative, delivered at 28 to 30 days: significant behavioural improvement, with a cerebellar structural abnormality corrected in high-expression regions | abstract only | R1 D05/D08 and `O8`; cross-package point (a) |

### Queries run for this review

| Id | Route | String | Run (UTC) | Hits | What was done |
|---|---|---|---|---|---|
| V01 | NCBI E-utilities esearch + esummary + efetch, db=pubmed | `Aspa AND (gene therapy OR AAV) AND Canavan AND (myelin OR myelination) AND mice` | 2026-11-05T23:14:27Z | 19 | all 19 titles reviewed; two records retrieved as abstracts (23817205, 37149081), one further named (28194442, no late arm in its abstract) |
| V02 | NCBI E-utilities esearch, db=pubmed | `Stxbp1 AND (restoration OR reinstat* OR re-expression OR reversal) AND (adult OR postnatal OR juvenile) AND mice` | 2026-11-05T23:14:59Z | 1 | corroborates R2's bounded null for that gene: nothing on post-onset restoration |
| V03 | NCBI E-utilities esearch + esummary, db=pubmed | `Tubb4a AND (antisense OR oligonucleotide OR gene therapy) AND (myelin OR leukodystrophy)` | 2026-11-05T23:14:59Z | 9 | 9 titles reviewed; 41566774 retrieved as abstract |
| V04 | NCBI E-utilities esearch + esummary, db=pubmed | `(parvalbumin OR somatostatin OR GABAergic) AND (number OR density OR count*) AND (gene restoration OR re-expression OR reinstatement OR reactivation OR conditional rescue) AND (mouse OR mice) AND brain` | 2026-11-05T23:16:04Z | 57 | top 25 titles reviewed; no post-onset interneuron count found, which corroborates both packages; 34135323 retrieved as abstract |
| V05 | NCBI E-utilities esearch + esummary + efetch, db=pubmed | `(Stxbp1 OR Syngap1 OR Cdkl5 OR Ube3a OR Shank3) AND (AAV OR gene therapy OR antisense) AND (symptomatic OR after onset OR post-onset OR adult) AND (seizure* OR EEG OR spike)` | 2026-11-05T23:16:29Z | 60 | top 25 titles reviewed; 34369389 and 36594817 retrieved as abstracts |
| V06 | NCBI E-utilities esearch + esummary + efetch, db=pubmed | `(leukodystrophy OR hypomyelination OR dysmyelination) AND (gene therapy OR AAV OR antisense OR re-expression OR gene replacement) AND (symptomatic OR after onset OR delayed OR juvenile OR adult) AND (remyelination OR myelin) AND (mice OR mouse OR rat)` | 2026-11-05T23:17:06Z | 51 | top 25 titles reviewed; 40051162 and 31143934 retrieved as abstracts; the module's own WWOX gene-therapy source appeared in the same list, which is the control that the search space was the right one |
| V07 | NCBI E-utilities esearch + esummary + efetch, db=pubmed | `(interneuron number OR interneuron density OR parvalbumin cell number OR interneuron survival) AND (rescue OR restoration OR gene therapy OR re-expression) AND (epileptic encephalopathy OR neurodevelopmental OR epilepsy) AND mice` | 2026-11-05T23:18:15Z | 65 | top 25 titles reviewed; 32125365 and 40106582 retrieved as abstracts |
| V08 | NCBI E-utilities esearch + esummary, db=pubmed | `AAV AND (neonatal versus juvenile OR age at injection OR injection age) AND (lethal OR short-lived OR null mice) AND brain AND (transduction OR expression) AND gene therapy` | 2026-11-05T23:18:15Z | 2 | both reviewed; 23011033 retrieved as abstract |
| V09 | NCBI E-utilities efetch db=pmc | PMC record of 23817205 | 2026-11-05T23:15Z | 1 | front matter only; the body is not open for that record, so it stays `abstract_only` |
| V10 | Europe PMC REST `fullTextXML` | PMC record of 40051162 | 2026-11-05T23:17Z | 1 | open full text read in two question-directed passes for the onset, comparator and readout statements; no figure viewed; bytes kept in the session scratch directory, outside the repository |

### What was not reachable or not done

* The bodies of 23817205, 37149081, 34369389, 36594817, 23011033, 41566774, 34135323, 32125365 and 40106582
  were not opened; each is `abstract_only` here and none of their methods, figures, comparators or exact
  treatment ages were read beyond what the abstract states. Every conclusion above that rests on them is
  phrased as a bounded contest to a null, not as a result.
* No route was worked around. No service requiring a contact address was called.
* I re-matched no quote to any artefact myself, in either package: that is the two blind audits' question and
  the task forbade duplicating it. Both audits had finished when this review closed and both are folded in at
  § 1.4 and cited wherever a row-level finding moves a conclusion — `verify/audit_R1/audit_R1.tsv` for R1 rows
  R04, R07, R14, R20, R22, R25, R33, R44-R50, R53, R54, R57-R59 and R64, and
  `verify/audit_R2/audit_R2.tsv` for R2 rows R13, R16, R18, R28, R31, R48, R55, R58 and R62. Fourteen R1 rows
  were not sent to that audit at all, among them the five `abstract_only` rows and both `cited_in_source_not_read`
  rows' companions, so a SUPPORTED verdict is absent rather than withheld for them.
* The seven R1 rows the auditor could not reach (PMID 18389497, PMID 18495876) are unaudited and not refuted.
  I did not attempt to re-acquire either full text: the reading route R1 used is declared in its own
  `queries.tsv` and re-running it would duplicate the audit's repair step rather than this review's question.
