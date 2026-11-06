Contributions only; the consolidated set for `NEED-WWOX-GENE-ADDITION` is owned by the Orchestrator (`integration/` folder).

# Module inputs contributed by R1 (`sb-r1`)

Revised 2026-11-06 after the blind locator audit (`verify/audit_R1/`) and the independent review
(`verify/review_R/`). **Nothing in `needs/needs.json`, `cards/`, `view/work_order.json`,
`ranking_it8_p9_20261029/ranking.json`, the registries, the ledgers or the four scientific current files was
edited by me.** Not medical advice; no dose, schedule, route or administered-dose number appears here.

**What changed in this round.** The earlier version proposed observation ids `O7` to `O10`. Those are
withdrawn: they collided with the sibling package's `O7`-`O12`, and one pair read as a contradiction. The
Orchestrator owns one consolidated set (`review_R.md` § 4). Below are **contributions** — the statement and
the limits for each of my row groups, as plain text, with no identifier claimed. The invalid `model_type`
value `other_disease_model` is removed throughout; the existing value in the file is `other_animal_model`.

All sources here are **`OTHER_DISEASE_PRECEDENT`** in the `evidence_scope` vocabulary: none is WWOX evidence,
and by the module's own rule none changes a `window_state`.

---

## 1 · Contributions to the consolidated set

`model_type` for every animal entry below is **`other_animal_model`**. `readout_level` is stated per
contribution and never promoted.

### C1 · Endpoint-class split after a manifested phenotype (`readout_level: functional`)

After a manifested phenotype, non-seizure electrophysiological endpoints recovered fully in every model that
measured them; learning, memory and social endpoints split by domain, recovering in some and failing in
others within single studies; cellular structural endpoints moved in several models while tissue-level
structure failed where it was measured. Failures are reported inside otherwise positive papers, so the
negative cells are under-counted.

*Limits.* The earlier headline "5 of 5 models that measured them" is withdrawn: it is not reproducible from
`evidence_r1.tsv`, because the endpoint class that holds those rows also holds models with outcome `none` and
`partial`. It is reproducible only if the class is redefined to exclude seizure endpoints, which it is not.
Three rows were re-binned out of `cognition_behaviour` in this round (two hippocampal long-term potentiation
rows and one phosphorylation-plus-receptor-current row), because they inflated the one cell a consumer is
most likely to read as "cognition recovers after onset". Rests on rows `R03`, `R07`-`R10`, `R13`-`R20`,
`R25`, `R29`, `R30`, `R34`-`R38`, `R41`-`R43`, `R53`-`R56`, `R90`, `R91`.

### C2 · Seizure endpoints after onset (`readout_level: functional`)

Conditional re-expression left two seizure endpoints unmoved after onset: epileptic spasms in a kinase model
(late arm, two alleles, two Cre drivers) and audiogenic susceptibility in a ligase model. In the same set,
adult conditional restoration of a synaptic regulator eliminated interictal spiking measured in the same
animals before and after, and a pathway drug begun after seizure onset suppressed seizures while it was
given. **Gene class correlates with this split and is not established as its cause**: it is confounded with
restoration mode, with endpoint identity and with the level of restoration achieved.

*Limits.* The earlier `direction_observed` "prevented but not recovered" is withdrawn as a summary of the
seizure class; it was true only of the two conditional arms. The clause claiming the only post-onset seizure
success was a pathway drug is withdrawn as contradicted by rows `R13`, `R14` and `R19` of my own table. The
threshold result of `R14` holds at the tonic-clonic stage only. Rests on `R13`, `R14`, `R19`, `R23`, `R24`,
`R37`, `R39`, `R44`, `R47`; `R44` and `R47` are producer-re-acquired and not independently verified.

### C3 · The same locus under a different restoration mode (`readout_level: functional`)

Antisense reactivation of the ligase locus whose conditional reactivation left seizures in place gave a full
rescue of audiogenic seizure susceptibility at the same postnatal age, and rescued the electroencephalographic
rhythm and sleep phenotype in juveniles and in adults, with the degree of improvement correlated to the
protein level reached. **The same study reports that cortical poly-spike frequency, its epileptiform
endpoint, was not reduced at either age.** So the mode change moves the rhythm and provoked-threshold
sub-classes and not the epileptiform one.

*Limits.* Read at full text here (the review had these two at abstract level, which is why the poly-spike
result is added rather than adopted). Both are one gene; the restoration level reached was partial and
regionally uneven, which the authors themselves offer as a candidate explanation of the poly-spike failure.
Rests on `R79`, `R82`-`R89`.

### C4 · Myelin and white matter (`readout_level: protein for the lineage rows, functional for the external arms`)

No study in this bounded search restored the deficient gene after a documented onset of a myelin phenotype
and then measured **myelin sheath structure**. Seven of eight myelin rows are pre-onset or unlocated-onset
arms; the eighth is a post-onset arm in which myelination was not measured in any section. Restoring the gene
only in the oligodendrocyte lineage left one myelin protein at about 60 per cent of control and another
aberrant, attributed by the authors to a non-cell-autonomous effect of other cell types.

*Limits.* The earlier generalisation — that the myelin endpoint has never been tested after onset anywhere —
is withdrawn; it failed four independent searches by the reviewer, whose three external arms sit in gene
families my queries could not reach. The readout level must travel with the conclusion: the structural
readout in the lineage rows is the thickness of **myelin basic protein immunostaining measured at postnatal
day 16**, not myelin thickness beyond 12 weeks, and that source contains no electron microscopy. The one
myelin endpoint recorded as having moved under treatment is in an arm begun between postnatal days 7 and 9
with no stated onset, its Results word is "effectively restored" while its abstract says "improved", and it
is producer-re-acquired and not independently verified. Rests on `R49`-`R52`, `R57`-`R59`, `R74`, `R76`.

### C5 · Interneuron endpoints (`readout_level: functional`)

Interneuron **number** after post-onset restoration was not found in a bounded search, independently
corroborated by the reviewer's own search. Interneuron **structure** is not unmeasured: a brief pathway
inhibition confined to the third postnatal week rescued parvalbumin perisomatic innervation and adult social
behaviour in a cell-type-restricted lesion, with the period anchored to that innervation's maturation
plateauing at the end of the first postnatal month.

*Limits.* The earlier claim that interneuron endpoints are unmeasured in every source is withdrawn as too
broad. The arm is a pathway drug, not restoration of the deficient gene, and it precedes the adult endpoint,
so it is prevention inside a stated sensitive period. The endpoint is innervation density, not cell number.
Rests on `R90`-`R92`.

### C6 · The cost of restoring (`readout_level: functional`)

Abrupt widespread reactivation of the deficient gene killed animals selectively in the restored genotype in
two independent models, and both groups moved to a graded induction because of it. A third instance is
compound-specific rather than restoration-specific: two of three candidate antisense compounds caused overt
toxicity at a higher exposure, and lowering it left the restoration insufficient.

*Limits.* The third element of the earlier version — a pathway drug's benefit reversing on withdrawal — rests
on a producer-re-acquired row that the blind audit could not reach, and must be marked as such. The hazard is
specific to abrupt conditional reactivation and to a compound, not to gene addition as such: the review
records that modest vector-mediated overexpression in wild-type brain was tolerated in two external sources.
Rests on `R05`, `R31`, `R47`, `R84`.

### C7 · Level and distribution achieved, not only timing (`readout_level: functional`)

Three sources tie the result to how much restoration was achieved rather than to the treatment age alone:
improvement tracked the protein level across compounds, ages and timepoints; the weaker adult arm is
attributed by its own authors to the smaller protein increase rather than to lost reversibility; and a
post-onset behavioural gain occurred at coverage described as sporadic at the cellular level and regionally
uneven.

*Limits.* Correlation across pooled arms, not a dose-controlled design, and it holds for the endpoints that
moved and not for the one that did not. The third source is abstract only. Level, distribution and timing are
confounded in every study in this set. Rests on `R83`, `R87`, `R88`, `R94`, `R95`.

---

## 2 · `needs/needs.json` — text contributions, no identifiers claimed

**For the `inferred` line.** Proposed text, replacing what I proposed earlier:

> "That which endpoint classes could recover after onset is partly predictable from outside WWOX: circuit,
> physiology and cellular structural endpoints have recovered after onset in several other single-gene
> neurodevelopmental models, developmentally-built behaviours and tissue-level structure generally have not,
> spontaneous seizure endpoints have been preventable and not recoverable in two conditional non-channel
> models and recoverable in two channel models and under antisense reactivation of one of the same
> non-channel loci, and **the myelin sheath has not been measured after onset in any of them**. This is an
> expectation imported from other genes, not a WWOX result, and it changes no `window_state`."

**For `intervention_direction.do_not_assume`.** The target is named correctly this time: it is a single
string inside `intervention_direction`, not a list field of the need, so this is offered as an extension of
that string and not as a list append.

> "Do not read an external post-onset recovery as licence for a WWOX post-onset arm in the mouse: every
> external post-onset arm treats an animal that would otherwise reach adulthood, while the null in this
> corpus is dead at about three weeks. One external systemic arm given at an age when a comparable null is
> already symptomatic produced only a few percent neuronal transduction with a partial survival benefit, so
> the constraint is as much vector kinetics as biology."

**For `notes`.** Proposed text, with the closing clause corrected:

> "The prevented-versus-recovered split now carries an external-precedent line. Its practical content is that
> the three endpoint classes most likely to move after onset (network, cellular structure, cognition in some
> domains) are not the ones this need's goal field names as `deep_recovery`, and the one class with no
> external precedent in either direction is **myelin sheath structure after onset in a neuron-driven
> lesion**."

---

## 3 · `view/work_order.json` — entry for `NEED-WWOX-GENE-ADDITION`

**Append to `data`** (field exists on the entry):

> "Added by R1 (revised 2026-11-06, external precedents): the added arm should be worded per endpoint class.
> External post-onset restoration arms in other disorders moved circuit, physiology and cellular structural
> endpoints, failed on anxiety, working memory, motor coordination and tissue-level structure, split on
> spontaneous seizure endpoints by restoration mode and by endpoint identity rather than cleanly by gene, and
> **never measured myelin sheath structure after onset**. Quantified sheath structure is therefore the
> discriminating measurement of the arm rather than a confirmatory one. The restoration level and its
> regional distribution should be measured alongside every endpoint, because three external sources tie the
> result to the level reached and one reports a post-onset gain at sporadic coverage."

**Append to `would_change`** (earlier wording withdrawn as overstated):

> "A post-onset arm that moved a circuit readout but not quantified myelin would match the precedents in the
> syndromic gene set. The reverse pattern would be the first of its kind **for a neuron-driven lesion
> measured as sheath structure** — not the first of its kind outright, since white-matter abnormality has
> been reversed after a documented onset in a glial-gene leukodystrophy. Either pattern would need the
> locator audit before it touched a card."

**Append to `feasibility`** (held as written, with the review's addition):

> "External precedents do not relieve the feasibility problem; they sharpen it. No external post-onset arm
> treats an animal with the lifespan of this null, so the design options stay the three already named. Two
> external sources treated nulls with short lives later with a modest survival benefit (abstract level), so a
> vector contribution to the perinatal-only window is possible and unmeasured."

**`window_state` — no change proposed.** All rows are `OTHER_DISEASE_PRECEDENT`. The closed vocabulary in
`view/work_order.json` has four values, the fourth being `symptom_suppression_reversible`, which is named
here so that any proposed fifth state is assessed against the full set.

---

## 4 · `cards/` — proposed appends

| Card and field | Proposed append | Rests on |
|---|---|---|
| `C01_aav9_wwox` `p4_fields.temporal_or_model_limit` | "External precedent (R1, revised 2026-11-06): post-onset restoration has recovered circuit, cellular structural and some cognitive endpoints in other single-gene neurodevelopmental models, so a post-onset arm is not a priori futile; but **no such study measured myelin sheath structure after onset**, and the one external arm that corrected a white-matter abnormality after a documented onset did so in an astrocyte-specific lesion in a long-lived model. Two models caused death by restoring the gene abruptly. The precedents constrain which endpoint classes to measure, never a treatable age." | `R07`-`R09`, `R41`-`R43`, `R53`, `R05`, `R31`, `R49`-`R52` |
| `C04_aav9_endpoint_families` `p4_fields.temporal_or_model_limit` | "Spike-wave discharge rate is an interictal network measure. Among external precedents the class is **split**: preventable and not recoverable in two conditional non-channel models, fully recovered after adult conditional restoration of a synaptic regulator and after antisense reactivation of one of the same non-channel loci, and not reduced at either of two ages in the one external study whose epileptiform endpoint was measured alongside a rhythm endpoint that did recover. A post-onset null on this endpoint would be consistent with part of the precedent set and inconsistent with another part, so it must not be pre-registered as expected." | `R13`, `R14`, `R23`, `R24`, `R37`, `R79`, `R85`, `R86` |
| ~~`C04` `next_measurement`~~ | **Withdrawn.** The card has no `next_measurement` field; its `p4_fields` are `endpoint_pursued`, `functional_evidence_available`, `temporal_or_model_limit` and `cellular_context`. The same content is already contributed to the work-order `data` field above. | - |
| Any card or view text using "rescue" or "reverses" for AAV9 | No new change proposed; the two-state wording already proposed in `rescue_window_it6_20261029.md` § 5 is sufficient, since this package adds no WWOX observation. | - |

---

## 5 · `ranking_it8_p9_20261029/ranking.json` — `INV-01`

**Append to `next_test`:**

> "Per endpoint class, with a pre-treatment measurement in the same animals or an age-matched cohort
> sacrificed at the injection day, and an untreated same-genotype comparator at the same age. **Quantified
> myelin sheath structure (g-ratio or electron microscopy, not marker intensity and not immunostaining
> thickness) is the discriminating endpoint for a neuron-driven lesion**, since white-matter abnormality
> after onset now has one external precedent in the positive direction and sheath structure none. Spike-wave
> rate recorded before restoration is the confirmatory endpoint and its external precedent is split, so it
> should be paired with a rhythm or power-spectrum measure, the sub-class that did recover after onset.
> Restoration level and regional distribution measured alongside every endpoint. Graded rather than abrupt
> restoration, with mortality declared as an endpoint."

**Append to `novelty_perimeter`:**

> "Extended on 2026-11-05 and corrected on 2026-11-06 beyond this module's own sources to a bounded external
> search (34 queries, `queries.tsv` of `batch_sci_20261105/r1_restoration_ndd`) over conditional,
> pharmacological, antisense and vector restoration after onset in Mecp2, Ube3a, Fmr1, Tsc1, Pten, Syngap1,
> Cdkl5, Shank3 and Tcf4 models. 22 sources read, 17 at partial full text. **The search was anchored on
> those gene names and on myelin and oligodendrocyte wording, so it could not reach leukodystrophies caused
> by an enzyme, a connexin, a tubulin or an astrocyte transporter; an independent review found three
> post-onset white-matter arms in exactly those families.** No post-onset myelin sheath morphometry and no
> post-onset interneuron count exists in either search. This is a bounded search, not a statement that none
> exists."

**No rank change proposed.** `INV-01` stays at rank 1.

---

## 6 · `proposed_registry_changes` (plain statements; I changed nothing)

1. **No new PAPER record is proposed as a completed reading.** All 22 sources are
   `OTHER_DISEASE_PRECEDENT` and none is a WWOX study; listing them as registry readings would inflate the
   coverage and self-eval counters without a WWOX claim behind any of them. They live as rows in
   `evidence_r1.tsv` and as 22 staged receipts.
2. **22 staged receipts await the integrator**, event ids `FTR-20261105-<PMID>-24` for the 18 of the first
   round and `FTR-20261106-<PMID>-24` for PMIDs 34369389, 36594817, 34135323 and 32125365. Each has
   `prior_receipt` null and `reread_reason` `first_read`; each passed
   `staged_receipt_check.py --check-doi` on 2026-11-06, as `receipts/INDEX.tsv` now records per row. I
   recorded none of them.
3. **No claim id is proposed for creation, revision or retirement**, and therefore no
   `legend-locator-audit` trigger: no row here is a WWOX observation.
4. **Two sources are flagged for the integrator as not independently verified.** PMID 18389497 and
   PMID 18495876 were unreachable to the blind auditor and were re-acquired by me through the route this
   package had declared. Their rows carry that in `source_depth` and are excluded from the headline matrix.
   They populate cells that have no other occupant, so no cell resting on them should be quoted without the
   mark.
5. **No change to `non_molecule_modalities.tsv`.** Antisense reactivation, conditional re-expression, an
   inducible switch, vector gene replacement and a pathway drug used as a reversal probe are labelled per row
   in the `restoration_mode` column rather than entering any catalogue.
6. **Three rows are `cited_in_source_not_read`** (`R17`, `R22`, `R78`). If the integrator wants any of them
   as a module input, the primary source must be opened first. `R43` carries the same provenance problem at
   `partial_fulltext` depth and should not be read as a measurement made in the citing source.
