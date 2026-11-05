# Module inputs proposed by R1 (`sb-r1`)

Proposals only. **Nothing in `needs/needs.json`, `cards/`, `view/work_order.json`,
`ranking_it8_p9_20261029/ranking.json`, the registries, the ledgers or the four scientific current files was
edited by me.** Every row below is written in the vocabulary of the file it would touch, with the evidence row
ids from `evidence_r1.tsv` it rests on. Not medical advice; no dose, schedule or route appears here.

All sources below are **`OTHER_DISEASE_PRECEDENT`** in the `evidence_scope` vocabulary of `needs/needs.json`:
none of them is WWOX evidence, and by the module's own rule none of them changes a `window_state` value.

---

## 1 · `needs/needs.json` — `NEED-WWOX-GENE-ADDITION`

### 1.1 Proposed new observations (`observed`, continuing the `O` series after `O6`)

| Proposed id | `statement` (proposed text) | `model_type` | `evidence_scope` | `readout_level` | `direction_observed` | Rests on |
|---|---|---|---|---|---|---|
| `O7` | "External precedent, endpoint-class split: across 18 studies in eight other single-gene neurodevelopmental disorders, restoration of the deficient gene after a manifested phenotype moved circuit and physiology endpoints in 5 of 5 models that measured them, cellular structural endpoints in 3 models, and left anxiety, working memory, motor coordination and tissue-level structure unmoved in 6 models. The failures are reported inside otherwise positive papers." | `other_disease_model` | `OTHER_DISEASE_PRECEDENT` | `functional` | `improved for circuit and cellular endpoints, unchanged for developmentally-built behaviour` | R07-R09, R13-R16, R18-R20, R29, R34-R38, R41-R43, R53-R56 |
| `O8` | "External precedent, seizure endpoints: in two independent models the spontaneous seizure endpoint was reduced by early restoration and not by late restoration of the same gene. One two-allele study states the occurrence 'appears to be preventable upon early re-expression of CDKL5 but becomes limited if expressed after seizure onset'. The only post-onset seizure success in the set is a downstream pathway drug whose benefit reversed on withdrawal." | `other_disease_model` | `OTHER_DISEASE_PRECEDENT` | `functional` | `prevented but not recovered` | R23, R24, R28, R37, R39, R44, R47 |
| `O9` | "External precedent, myelin: no study found restored the deficient gene after a documented phenotype onset and then measured a myelin endpoint. All eight myelin rows are pre-onset restorations or arms with an unlocated onset. Restoring the gene only in the oligodendrocyte lineage of a Rett model left one myelin protein at about 60 per cent of control and another aberrant, attributed to a non-cell-autonomous effect of other cell types." | `other_disease_model` | `OTHER_DISEASE_PRECEDENT` | `protein` | `undetermined after onset; not corrected by lineage-restricted restoration` | R49-R52, R57-R59, R74, R76 |
| `O10` | "External precedent, restoration toxicity: in two independent models abrupt restoration of the deficient gene caused death selectively in the restored genotype, and both groups switched to a graded induction because of it. A third study showed benefit from a pathway drug reversing when the drug was withdrawn." | `other_disease_model` | `OTHER_DISEASE_PRECEDENT` | `functional` | `worse` | R05, R31, R47 |

### 1.2 Proposed additions to `inferred`

Proposed text, to sit beside the existing line that `rescue_window_it6_20261029.md` already proposed:

> "That which endpoint classes could recover after onset is partly predictable from outside WWOX: circuit,
> physiology and cellular structural endpoints have recovered after onset in several other single-gene
> neurodevelopmental models, developmentally-built behaviours and tissue-level structure generally have not,
> spontaneous seizure endpoints have been preventable and not recoverable in the two cleanest cases, and the
> myelin endpoint has never been tested after onset in any of them. This is an expectation imported from other
> genes, not a WWOX result, and it changes no `window_state`."

Rests on: `O7`, `O8`, `O9`.

### 1.3 Proposed addition to `do_not_assume`

> "Do not read an external post-onset recovery as licence for a WWOX post-onset arm in the mouse: every
> external post-onset arm treats an animal that would otherwise reach adulthood (haploinsufficiency, a viable
> null, or symptoms at about six weeks with death at about eleven), while the null in this corpus is dead at
> about three weeks. No external precedent treats an animal on that timescale."

Rests on: R01-R06 (onset about 6 weeks, death about 11 weeks), R13-R17 (haploinsufficiency), R23-R28
(heterozygous female, seizures at adult ages), R44-R47 (seizure onset about 1 to 2 months).

### 1.4 Proposed addition to `notes`

> "The prevented-versus-recovered split now carries an external-precedent line (`O7` to `O10`). Its practical
> content is that the three endpoint classes most likely to move after onset (network, cellular structure,
> cognition in some domains) are not the ones this need's goal field names as `deep_recovery`, and the one
> class with no external precedent in either direction is myelin."

---

## 2 · `view/work_order.json` — entry for `NEED-WWOX-GENE-ADDITION`

### 2.1 Proposed append to `data`

> "Added by R1 (2026-11-05, external precedents): the added arm should be worded per endpoint class. External
> post-onset restoration arms in eight other disorders moved circuit, physiology and cellular structural
> endpoints, failed on anxiety, working memory, motor coordination and tissue-level structure, were preventive
> but not curative for spontaneous seizures in the two cleanest cases, and never measured myelin at all.
> Quantified myelin is therefore the discriminating measurement of the arm rather than a confirmatory one."

### 2.2 Proposed append to `would_change`

> "A post-onset arm that moved a circuit readout but not quantified myelin would match every external
> precedent and would support hypothesis R1 of IT8 P5; the reverse pattern would be the first result of its
> kind in this literature and would need the locator audit before it touched a card."

### 2.3 Proposed append to `feasibility`

> "External precedents do not relieve the feasibility problem; they sharpen it. No external post-onset arm
> treats an animal with the lifespan of this null, so the design options stay the three already named
> (organoids with a same-organoid baseline, a slower-onset allele, an inducible switch)."

### 2.4 `window_state` — no change proposed

By the module's own rule in `advance_it8_p5_20261029/loop2_broad_recovery/README.md` section 7, window states
change only on WWOX observations. All 76 rows here are `OTHER_DISEASE_PRECEDENT`. The three existing states
(`prevented_early_window`, `recovered_post_onset_model`, `unmeasured`) stand unchanged.

---

## 3 · `cards/` — proposed appends

| Card and field | Proposed append | Rests on |
|---|---|---|
| `C01_aav9_wwox` `temporal_or_model_limit` | "External precedent (R1, 2026-11-05): post-onset restoration of a deficient gene has recovered circuit, cellular structural and some cognitive endpoints in other single-gene neurodevelopmental models, so a post-onset arm is not a priori futile; but no such study measured a myelin endpoint after onset, and two caused death by restoring the gene abruptly. The precedents constrain which endpoint classes to measure, never a treatable age." | R07-R09, R41-R43, R53, R05, R31, R49-R52 |
| `C04_aav9_endpoint_families` `temporal_or_model_limit` | "External precedent (R1, 2026-11-05): endpoint families behave differently under post-onset restoration. Spike-wave discharge rate, the single endpoint this card carries, belongs to the class that was preventable and not recoverable in the two cleanest external cases; a post-onset null on that endpoint would be consistent with the precedents rather than a failure of the arm." | R23, R24, R37, R28 |
| `C04_aav9_endpoint_families` `next_measurement` | "Add, beside the post-onset organoid arm already named in IT8: a cellular-versus-tissue structural pair and a quantified myelin measure in the same animals, because one external study moved cellular structure and not cortical thickness in the same animals, and because myelin after onset has no external precedent in either direction." | R53-R55, R49-R52 |
| Any card or view text using "rescue" or "reverses" for AAV9 | No new change proposed. The two-state wording already proposed in `rescue_window_it6_20261029.md` section 5 is sufficient; this package adds no WWOX observation that would alter it. | - |

---

## 4 · `ranking_it8_p9_20261029/ranking.json` — `INV-01`

### 4.1 Proposed append to `next_test`

> "Per endpoint class, with a pre-treatment measurement in the same animals or an age-matched cohort
> sacrificed at the injection day, and an untreated same-genotype comparator at the same age. Quantified myelin
> (g-ratio or densitometry, not marker intensity) is the discriminating endpoint; spike-wave rate recorded
> before restoration is the confirmatory one. Graded rather than abrupt restoration, with mortality declared as
> an endpoint."

### 4.2 Proposed append to `novelty_perimeter`

> "Extended on 2026-11-05 beyond this module's own sources to a bounded external search (30 queries,
> `queries.tsv` of `batch_sci_20261105/r1_restoration_ndd`): PubMed through two routes, Europe PMC REST and PMC
> article pages, for conditional, pharmacological and switch-based restoration after onset in Mecp2, Ube3a,
> Fmr1, Tsc1, Pten, Syngap1, Cdkl5, Shank3 and Tcf4 models. 18 sources read, 16 at partial full text. No
> post-onset myelin arm exists in that search, and no post-onset interneuron count. This is a bounded search,
> not a statement that none exists."

### 4.3 No rank change proposed

`INV-01` stays at rank 1. Nothing here weakens the reason given in its `why_now` field; the external
precedents make the per-endpoint wording of the arm more specific, which is a sharpening of the same
investigation rather than a reason to move it.

---

## 5 · `proposed_registry_changes` (plain statements; I changed nothing)

1. **No new PAPER record is proposed as a completed reading.** All 18 sources are
   `OTHER_DISEASE_PRECEDENT` and none is a WWOX study; by the convention recorded in the operator memory on
   declaration versus attestation, listing them as registry readings would inflate the coverage and self-eval
   counters without a WWOX claim behind any of them. They live as rows in `evidence_r1.tsv` and as 18 staged
   receipts in `receipts/`, which is where a non-WWOX precedent belongs.
2. **18 staged receipts await the integrator**, event ids `FTR-20261105-<PMID>-24` for PMIDs 17289941,
   18389497, 18495876, 19211884, 21716289, 22500629, 22525157, 24285883, 25866966, 26886798, 30082419,
   31025938, 31143434, 34651584, 35535852, 39855191, 41509287, 41997465. Each has `prior_receipt` null and
   `reread_reason` `first_read`; each passed `staged_receipt_check.py --check-doi`. I recorded none of them.
3. **No claim id is proposed for creation, revision or retirement.** No row here narrows, reverses,
   corroborates or removes a `consolidated baseline` claim, because no row is a WWOX observation. Therefore no
   `legend-locator-audit` trigger is proposed either.
4. **One existing record's wording is worth the integrator's attention, and no edit is proposed by me.** The
   `goal` field of `NEED-WWOX-GENE-ADDITION` is `deep_recovery`. The external precedents show that the endpoint
   classes most likely to answer a post-onset restoration are not the deep ones (myelin, progenitor state) but
   the network and cellular ones. `rescue_window_it6_20261029.md` already proposed a `notes` line on this; this
   package adds the external half of the same observation and no new field.
5. **No change to `non_molecule_modalities.tsv`.** Conditional re-expression, an inducible switch and a
   pathway drug used as a reversal probe are all modalities the module already represents; three of the
   external sources are pathway drugs rather than gene restoration, and they are labelled as such per row in
   the `restoration_mode` column rather than entering any catalogue.
6. **Two rows in `evidence_r1.tsv` are `cited_in_source_not_read`** (`R17`, `R22`). If the integrator wants
   either as a module input, the primary source must be opened first; neither should be promoted on the citing
   paper's word.
