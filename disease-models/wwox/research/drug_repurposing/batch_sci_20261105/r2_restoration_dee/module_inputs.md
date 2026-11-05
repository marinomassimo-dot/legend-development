# Module inputs proposed by `sb-r2`

Proposals only. **Nothing outside this directory was edited**: `needs/needs.json`, `cards/`, `view/work_order.json`,
`ranking_it8_p9_20261029/ranking.json`, the registries and the four scientific current files are untouched. Each item
names the `evidence_r2.tsv` rows it rests on. Wording is written to drop straight into the named field by an
integrator. Not medical advice; no dose, schedule or administration route appears. Every statement below is an
`OTHER_DISEASE_PRECEDENT`: none of it is WWOX evidence, and by the module's own rule the WWOX window states are
unchanged by it.

---

## 1 · `NEED-WWOX-GENE-ADDITION` — proposed `observed` entries O7 to O12

Fields follow the existing O4-O6 shape (`id`, `pmid`, `statement`, `model_type`, `species`, `genotype`,
`tissue_or_cells`, `age_stage`, `comparison`, `readout`, `readout_level`, `direction_observed`, `evidence_scope`,
`limits`, `locators`, `locator_status`). All six take `evidence_scope: OTHER_DISEASE_PRECEDENT`,
`model_type: other_animal_model` (O11 and O12: `human_clinical_precedent`, a value the vocabulary does not yet carry —
see section 5), `readout_level: functional`, `locator_status: DOCUMENT`, and
`locators: [{kind: document, path: disease-models/wwox/research/drug_repurposing/batch_sci_20261105/r2_restoration_dee/README.md, anchor: <section named below>}]`.

**O7 — the first well-controlled post-onset restoration of seizures, behaviour and cognition.** PMID 35013317.
*Statement:* "Conditional Dravet knock-in mouse, restoration of the silenced allele after manifest seizures (P30;
onset stated P18-P24) in animals selected for seizing at handling: complete rescue of spontaneous seizures on two
weeks of video-EEG (0 of 9 treated against 7 of 8 control-virus-treated), of thermally induced seizures, of
seizure-related death, of hyperactivity, working memory and spatial learning, and of reactive astrogliosis and
inflammation transcripts; the cortical transcriptome showed no differentially expressed gene against wild type.
Restoration at P90, about ten weeks after onset, abolished established seizures in 6 of 6 animals, each with its own
two-week pre-treatment video-EEG baseline."
*Genotype:* Scn1a haploinsufficiency with a conditionally reactivatable silent allele (not WWOX).
*Age stage:* juvenile post-onset (P30) and adult (P90); the authors map these to roughly 4 and 20 human years.
*Comparison:* control-virus same-genotype littermates and wild type; the adult arm additionally within-animal.
*Limits:* "Not WWOX evidence. Interneuron excitability did not normalise — fast-spiking cells overshot and
non-fast-spiking cells became more excitable than both other groups — and the authors state the phenotype recovered
while the cellular measure did not, so the benefit rests on an alternative excitation-inhibition balance. Sociability
only trended. Two of nine treated animals died after thermal challenge with incompletely restored protein. In the
adult arm protein was restored in cortex and hippocampus but not cerebellum or striatum. No myelin endpoint. The model
has no motor deficit, so motor recovery is unmeasurable in it. Lesion is viable into adulthood."
*Rows:* R01-R14. *README anchor:* section 2.1.

**O8 — post-onset correction in a second DEE model, with the intervention's own cost measured.** PMID 36173683.
*Statement:* "Homozygous gain-of-function DEE mouse, seizures from P18, treated while symptomatic at P40: survival,
seizure frequency, interictal spikes and nest building all improved against a non-hybridizing control in the same
genotype; re-treatment after relapse in neonatally treated animals worked again. The neonatal arm of the same model
gives the pre-onset comparison in the same laboratory, and growth stayed below wild type even there."
*Limits:* "Not WWOX evidence. The mechanism is silencing of an excess transcript, not replacement of a missing protein.
The intervention reduced open-arm time in every treated group including treated wild type, and novel-arm time in
treated wild type: without that arm both would read as rescues. The authors state that seizures prevented a
within-animal before-and-after behavioural comparison. Homozygous-only phenotype, unlike the human heterozygous
disease."
*Rows:* R15-R23. *README anchor:* section 2.2.

**O9 — the age cliff in the design closest to WWOX, and its stated cause.** PMID 39847501.
*Statement:* "Constitutive null mouse of a DEE gene, dying in the third postnatal week, treated with a brain-directed
AAV supplying the missing protein: at P2 survival was prolonged, seizure severity reduced (time to first seizure
unchanged), thermally induced seizures prevented and parvalbumin interneuron and pyramidal excitability fully
restored; at P10, at twice the exposure, all eight treated null animals died in the usual window. The authors
attribute the P10 failure to transgene level and distribution, note that single-stranded AAV needs one to two weeks to
reach therapeutic expression, and report that AAV CNS expression falls sharply with injection after P3-P4 in rodents.
Growth was not rescued at either age: treated null body weight never exceeded about half the wild-type value through
P80 despite rescued survival."
*Limits:* "Not WWOX evidence. The P10 arm is scored UNVERIFIED, not a recovery failure: the restoration achieved at the
lethal window was never measured, so biological irreversibility and vector kinetics are not separated. Vector reached
forebrain only — midbrain and brainstem undetected — so no cerebellar or brainstem endpoint was testable. No
electrographic recording was possible; the seizure endpoint is behavioural. No myelin or glial endpoint."
*Rows:* R37-R44. *README anchor:* section 2.4.

**O10 — both hypomyelination precedents are pre-onset, and the myelin endpoint moved least in both.**
PMIDs 32610343 and 28100454.
*Statement:* "In a Pelizaeus-Merzbacher model treated at birth, lifespan rose about eleven to twelve fold,
oligodendrocyte number was fully restored (81-101 percent of control), respiratory control normalised and open-field
locomotion reached wild-type levels, while myelinated axons reached only about 10 percent of control at three weeks and
persisted at eight months with less compaction, conduction velocity about 17 percent and rotarod at most 36 percent;
the germline arm of the same study, correcting earlier and completely, did restore myelination and conduction to
wild-type levels. In a hypomyelinating leukodystrophy model an oligodendrocyte-directed AAV given at P10 — an age
chosen to precede the stated onset of severe demyelination in the fourth postnatal week — improved myelin density
without reaching wild type, while oligodendrocyte apoptosis fell from about half of counted cells to about one in
twenty and glial and macrophage markers, motor measures and survival all improved. Both author groups state that
treating later in disease was not done and name it as the next step."
*Limits:* "Not WWOX evidence. Both lesions are intrinsic to the oligodendrocyte, one stated as cell-autonomous — the
opposite driver from the Wwox system, where neuronal deletion reproduces the phenotype and lineage deletion is
phenotypically silent. One corrects a toxic protein by suppression, which has no WWOX analogue. The second used a
focal brain-directed delivery, so distribution is partial by design, and was read through the open article page, not
structured full text."
*Rows:* R24-R31, R54-R59. *README anchor:* section 2.3.

**O11 — human timing precedent, SMA.** PMID 35715566.
*Statement:* "Single-administration AAV gene replacement given before symptom onset to 14 infants genetically at risk
of the severe form: all sat independently for at least 30 seconds, 11 inside the normal developmental window, and all
were alive and free of permanent ventilation at 14 months, against none of 23 and 6 of 23 respectively in a matched
untreated natural-history cohort. In the symptomatic trials of the same intervention, reported in this paper's
discussion, 64 percent and 44 percent reached the same sitting endpoint and did so months later, and one infant in
each cohort walked by 18 months."
*Limits:* "Human precedent, never a WWOX expectation. Single-arm against a matched natural-history cohort. The
symptomatic comparison is a secondary cross-trial statement inside this paper, which the authors themselves flag as
limited by differing design, endpoints and eligibility; the symptomatic primary reports were not read. A lower motor
neuron disease with a peripheral endpoint and no seizure, interneuron or myelin endpoint. Even pre-symptomatically,
five of 14 were below the normal gross motor range at 18 months. Pre-symptomatic treatment depends on newborn
screening that does not exist for WWOX."
*Rows:* R50-R53. *README anchor:* section 2.5.

**O12 — human timing precedent, metachromatic leukodystrophy, with a white-matter endpoint.** PMID 35065785.
*Statement:* "Lentiviral autologous haematopoietic stem-cell gene therapy in 29 children: pre-symptomatic and
early-symptomatic groups both exceeded a matched untreated natural-history cohort on gross motor function, and 20 of 25
assessed children showed normal acquisition of cognitive skills. The brain MRI white-matter and atrophy score
stabilised in every treated group but plateaued at a worse level in the early-symptomatic group than in the
pre-symptomatic group. Children entering the rapid progression phase at treatment could not benefit: two died of
progression and two deteriorated at the untreated rate, with engraftment and enzyme levels normal. The authors state
that most symptomatic cases would not be eligible at all, because progression outruns the months needed for enzyme
reconstitution."
*Limits:* "Human precedent, never a WWOX expectation. Benefit comes from cross-correction by a secreted enzyme supplied
by engrafted donor-type myeloid progeny, not from restoring the gene in the affected neural cell. No randomised
comparator; historical single-centre cohort; the conditioning regimen carries its own harms. An MRI severity score is
not a myelin measurement and cannot be set beside electron microscopy or a myelin marker. No seizure or interneuron
endpoint."
*Rows:* R45-R49. *README anchor:* section 2.5.

---

## 2 · `NEED-WWOX-GENE-ADDITION` — proposed additions to `inferred` and `counter_evidence`

**Proposed new `inferred` line (replaces nothing; the existing endpoint-class line stays and is narrowed by it):**

> "That the prevented-versus-recovered split runs by endpoint class alone. The external precedents support a different
> split: endpoints sustained by ongoing dysfunction (seizures, network firing, astrogliosis, the transcriptome,
> interneuron excitability) have recovered after onset in two DEE models; endpoints that are accumulated structure
> (myelin sheath, atrophy) have at best been arrested, never reversed, and only when treatment preceded onset; and
> endpoints with a peripheral or growth component recovered least, failing even with pre-onset treatment in the
> precedent whose design most resembles this one. This is a hypothesis built on non-WWOX models and it is not
> established for WWOX." (Rows R01-R09, R25, R42, R47, R54.)

**Proposed second new `inferred` line:**

> "That the perinatal efficacious window in the mouse is a biological boundary. A brain-directed AAV replacing a
> missing protein in a comparably short-lived null worked at P2 and failed completely at P10 at twice the exposure, and
> its authors attribute the failure to transgene level and distribution rather than to irreversibility, reporting that
> rodent AAV CNS expression falls sharply with injection after P3-P4. In a separate model a blood-brain-barrier-crossing
> capsid restored protein and abolished established seizures in adults. An observed perinatal-only window in a rodent
> is therefore a candidate artefact of the modality in the rodent until the restoration achieved at the later age is
> measured. This cuts both ways: it weakens 'WWOX restoration after onset cannot work' and equally forbids concluding
> that it can." (Rows R09, R37-R39.)

**Proposed additions to `counter_evidence`:**

* "In the one external post-onset success with a cellular endpoint, interneuron excitability did not normalise but
  overshot wild type, and the authors state the phenotype recovered while the cellular measure did not. A firing or
  excitability endpoint used as a success criterion for WWOX needs its acceptable direction fixed in advance." (R06, R07.)
* "Two of the external interventions produced measurable behavioural change in treated wild-type animals, so an
  intervention effect would be scored as a rescue without a treated wild-type or heterozygote arm." (R18, R19.)
* "External benefit has decayed (four of 14 treated animals dying between two and six months, with the authors allowing
  that the effect may be confined to a three-to-four-week interval) and has required re-treatment after relapse. A short
  follow-up would miss both." (R23, R61.)
* "Human post-symptomatic treatment of a leukodystrophy failed outright in rapidly progressing cases whose molecular
  correction was successful, and the structural white-matter endpoint was arrested at a stage-dependent plateau rather
  than reversed." (R46, R47.)
* "Two external DEE models could not be asked the post-onset question at all, because death follows the first seizure
  within minutes to days; their authors say so in the limitations. The absence of a post-onset arm in the WWOX
  literature is the field's normal condition for a lethal null, not a gap peculiar to WWOX." (R32, R37.)

**Proposed addition to `notes`:**

> "External precedents (O7-O12) place post-onset recovery on record for seizure, network, behavioural, cognitive and
> glial endpoints, and nowhere for the myelin sheath. No source in any model, in either direction, has measured whether
> an established hypomyelination re-myelinates under gene restoration, and no source has measured interneuron number."

---

## 3 · Cards `C01_aav9_wwox` and `C04_aav9_endpoint_families`

Both cards' `p4_fields.temporal_or_model_limit` currently ends with the IT6 P7 sentence that no treated-after-onset arm
exists and that the authors call this a model and technical constraint rather than a definitive boundary. Proposed
append, identical in both:

> "External precedent now bears on that sentence in both directions. A brain-directed AAV replacing a missing protein
> in a comparably short-lived null was effective at P2 and completely ineffective at P10 at twice the exposure, and its
> authors attribute the failure to transgene level and distribution, not to irreversibility; in a different model a
> blood-brain-barrier-crossing capsid abolished established seizures in adults with a within-animal baseline. The
> perinatal window recorded here is therefore not established as biological, and no conclusion about later
> responsiveness follows from it either way. Until the restoration achieved at a later age is measured, a null later
> arm would be uninterpretable." (Rows R09, R37-R39.)

Proposed append to `C01.p4_fields.endpoint_pursued`:

> "Among external precedents the seizure and network class is the only one with clean post-onset recovery, so the
> spike-wave discharge endpoint is the one this card should expect to move if a later arm is ever run; it is also the
> endpoint on which severity and onset latency have dissociated in a precedent, so a rate alone is not sufficient."
> (Rows R02, R03, R09, R16, R40.)

Proposed append to `C04.p4_fields.functional_evidence_available`:

> "External precedents that quantified myelin after restoration reached about 10 percent of wild type with reduced
> compaction, and conduction velocity about 17 percent, with both obtained before onset; the human white-matter
> endpoint was arrested, not reversed, and at a worse plateau when treatment followed symptoms. The unquantified
> myelin panels in the treated arms of this card's source should not be read as a stronger result than those." (Rows
> R25, R28, R47, R54.)

---

## 4 · `view/work_order.json` entry for `NEED-WWOX-GENE-ADDITION`, and `INV-01`

The work-order entry's `question` already asks whether benefit is "only prevented inside the first days of life or also
recovered when treatment follows onset", and its `data` field lists a pre-treatment baseline and treated-after-onset
arms. Proposed append to `data`:

> "Added in this batch, from external precedent: the arm must also measure the restoration actually achieved at the age
> of treatment and its regional coverage, because the one published later-age failure in a comparable null is
> attributed by its own authors to transgene level and distribution rather than to irreversibility; a treated
> wild-type or heterozygote arm, because two external interventions changed behaviour in normal animals; growth and
> glycaemia as primary rather than supportive endpoints, because growth failed to recover even with pre-onset treatment
> in that precedent; a myelin endpoint scored as arrest versus reversal rather than as recovery, because no source in
> any model has shown post-onset re-myelination; interneuron number as well as excitability, because no source has
> measured number; and a follow-up long enough to detect decay, with a pre-specified re-treatment arm."

Proposed append to the `INV-01` row's `feasibility` or `next_test` field (`next_test` currently reads: one added arm of
the published design with injection after the first recorded spike-wave discharge, same endpoints, untreated
same-genotype comparator kept):

> "Per-endpoint wording from external precedent: expect the seizure and network endpoints to carry the arm's power;
> expect the myelin endpoint to show arrest at best and score it as such; treat a negative result as uninterpretable
> unless the restoration achieved at the treatment age was measured."

---

## 5 · `proposed_registry_changes` (plain statements; nothing was changed)

1. **No change to any of the four scientific current files is proposed.** Every row in `evidence_r2.tsv` is an
   `OTHER_DISEASE_PRECEDENT`; by the module's own rule the WWOX window states are unchanged by non-WWOX observations.
2. **`NEED-WWOX-GENE-ADDITION` (`needs/needs.json`)** would gain observations O7-O12, two `inferred` lines, five
   `counter_evidence` lines and one `notes` sentence, as in sections 1 and 2. Its `sources.papers` would gain PMIDs
   35013317, 36173683, 32610343, 31943325, 39847501, 35065785, 35715566, 28100454, 37901435, each with an empty
   `paper_registry_ids` list (none is in the paper registry).
3. **Vocabulary gap.** `model_type` has no value for a human clinical precedent; O11 and O12 need one
   (`human_clinical_precedent` is proposed). Without it the two human rows cannot be entered without mislabelling them
   as animal models. This is a schema decision for the Orchestrator, not a scientific one.
4. **`window state` column** proposed in IT6 P7 (`prevented_early_window`, `recovered_post_onset_model`,
   `symptom_suppression_reversible`, `unmeasured`) would need a fifth value to hold R37 and R62: a later-age arm that
   was run and produced no benefit but whose restoration level was not measured. `attempted_post_onset_uninterpretable`
   is proposed. Scoring R37 as `unmeasured` loses the fact that the arm was run; scoring it as a recovery failure
   asserts more than the source supports.
5. **Cards `C01_aav9_wwox` and `C04_aav9_endpoint_families`** would gain the appends in section 3. No assertion row,
   score or comparison in either card changes; the appends touch `temporal_or_model_limit`,
   `C01.endpoint_pursued` and `C04.functional_evidence_available` only.
6. **`view/work_order.json`** and the `INV-01` row of `ranking_it8_p9_20261029/ranking.json` would gain the appends in
   section 4. `INV-01` keeps rank 1 and its question is unchanged: nothing here answers it, and the batch strengthens
   rather than weakens the case for running it, because the one comparable later-age experiment on record was left
   uninterpretable by a missing measurement that the WWOX arm can cheaply include.
7. **No claim, paper or working-model record is proposed for creation, edit or revival.** No CLAIM id is touched. The
   three `abstract_only` sources (PMIDs 31607539, 32848094, 41883162) are not proposed as inputs to any card or need:
   they are table rows and nothing more.
8. **Two nulls are proposed for the record as bounded searches, not as absences**: no post-onset restoration study for
   Stxbp1, Scn2a or Kcnq2 (queries Q10, Q11, Q13, Q14, Q24, Q25; 93 records screened by title, 2026-11-05), and no
   post-onset myelin-correction arm in any hypomyelination model (queries Q16, Q23; 13 records, 2026-11-05, plus the
   explicit statements of both myelin papers). If the module keeps a dismissal or negative-premise ledger entry for
   either, these are the search bounds to record with it.
