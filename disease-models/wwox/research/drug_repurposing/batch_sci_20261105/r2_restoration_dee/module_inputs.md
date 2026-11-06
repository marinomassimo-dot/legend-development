Contributions only; the consolidated set for NEED-WWOX-GENE-ADDITION is owned by the Orchestrator (integration/ folder).

# Contributions from `sb-r2` to the consolidated observation set

Revised 2026-11-06 after a blind locator audit and an independent review. **Nothing outside this directory was
edited**: `needs/needs.json`, `cards/`, `view/work_order.json`, `ranking_it8_p9_20261029/ranking.json`, the registries
and the four scientific current files are untouched. Not medical advice; no dose, schedule or administration route
appears. Every statement below is an `OTHER_DISEASE_PRECEDENT` or a human clinical report: none of it is WWOX evidence,
and by the module's own rule **none of it changes or takes a `window_state`**.

**What changed in this file in the correction round.** The first issue proposed observation identifiers `O7` to `O12`.
Those collided with the sibling package's `O7`-`O10`, each pair carrying different content, and one pair read as a
contradiction. **The identifier proposals are withdrawn.** The Orchestrator owns one consolidated set
(`verify/review_R/review_R.md` section 4); what follows is the content this package contributes to it, as plain text,
with the row ids it rests on. Two vocabulary proposals are also withdrawn — see section 3.

---

## 1 · Contributions to the consolidated set

Each item gives a proposed statement and its limits. The Orchestrator assigns the identifier and merges with the
sibling package; where the review's section 4 already supplies merged wording, that wording governs and the item below
is the contributing half.

### C1 · Post-onset restoration of seizures, survival, behaviour and cognition in a conditional channel model

*Statement.* "Conditional Dravet knock-in mouse, restoration of the silenced allele after manifest seizures (P30; onset
stated P18-P24) in animals selected for seizing at handling: complete rescue of spontaneous seizures on two weeks of
video-EEG (0 of 9 treated against 7 of 8 control-virus-treated), of thermally induced seizures, of death from seizures,
of hyperactivity, working memory and spatial learning, and of reactive astrogliosis and inflammation transcripts; the
**cortical** transcriptome showed no differentially expressed gene against wild type. Restoration at P90, about ten
weeks after onset, abolished established seizures in 6 of 6 animals, each with its own two-week pre-treatment video-EEG
baseline. Within the same arm, sociability recovered chamber preference but its index only trended; fast-spiking
interneuron excitability recovered but **overshot** wild type and non-fast-spiking cells became more excitable than
both other groups, the authors themselves separating phenotype-level recovery from the cellular measure; and two of
nine treated animals died after the thermal challenge with protein incompletely re-established."

*Limits.* "Not WWOX evidence. The recovery is complete at the level of the phenotype and partial at the level of the
cellular and social measures — 'fully' is the authors' phenotype-level word and must not be carried as an
endpoint-by-endpoint grade. The adult arm carries a seizure endpoint only: no behaviour, cognition or survival endpoint
is reported for it. In that arm protein was restored in cortex and hippocampus but not cerebellum or striatum. The
hippocampal count of 163 differentially expressed genes is a treated-versus-control-treated contrast — genes the
treatment changed — and **not** a residual defect against wild type, which the source never reports. No myelin
endpoint. The model has no motor deficit, so motor recovery is unmeasurable in it. The lesion is viable into adulthood
and the gene is a channel; WWOX is neither."

*Rests on:* R01-R14. *Changed in this round:* R13 reworded and re-binned out of cognition; R12 section corrected and
its hedge restored; R04 noted as a multi-element row whose locator reaches one element.

### C2 · Post-onset correction in a second DEE model, with the intervention's own cost measured

*Statement.* "**Silencing of a mutant channel transcript, not replacement of a missing protein**, in a homozygous
gain-of-function DEE mouse with seizures from P18, treated while symptomatic at P40: survival recovered, and seizure
frequency, interictal acute spikes and nest building improved **partially**, against a non-hybridizing control in the
same genotype; re-treatment after relapse in neonatally treated animals worked again. The neonatal arm of the same
model gives the pre-onset comparison in the same laboratory, and growth stayed below wild type even there."

*Limits.* "Not WWOX evidence, and the modality is decisive: a loss-of-function gene cannot be corrected by knockdown of
anything, so this is a timing precedent and not a replacement one. Survival is graded partial, not full: the
highest-exposure median is stated as beyond 300 days, a censored figure, and the source claims no normalised lifespan.
The authors state that seizures prevented a within-animal before-and-after behavioural comparison. The intervention
reduced elevated-plus-maze open-arm time in every treated group **and equally in treated wild type**; the source reads
that as a normalised disease marker and this package read it as an intervention cost, so **the direction is contested
and is recorded as contested, not graded**. In treated wild-type animals a memory measure also fell. Homozygous-only
phenotype, unlike the human heterozygous disease."

*Rests on:* R15-R23. *Changed in this round:* R16's locator re-located (it had been mis-assigned to a survival
sentence); R15 regraded partial; R18 regraded partial with both readings stated; R19 section corrected; R21 follow-up
corrected to the age at which weight was measured.

### C3 · The age cliff, what it is evidence of, and what bounds it

*Statement.* "In a null of a DEE gene dying in the third postnatal week, a brain-directed vector supplying the missing
protein extended lifespan, reduced seizure severity **without changing the time to first seizure**, prevented
thermally induced seizures and fully restored parvalbumin interneuron and pyramidal excitability when given at P2;
given at P10, at twice the exposure, all eight treated null animals died in the usual window. Its authors attribute the
later failure to transgene level and distribution rather than to irreversibility, **citing other studies and their own
unpublished work** — not a finding of this paper — for sharply reduced rodent CNS expression after the first postnatal
days. The restoration achieved at the later age was never measured, so biology and vector kinetics are not separated.
The generalisation is specific to route, capsid and promoter: a single systemic administration as late as P20 rescued
lethality in another short-lived null, and a systemic vector at four to five weeks in a null already symptomatic
transduced only a few percent of neurons and still moved survival. Growth was not rescued at either age despite
rescued survival, and the vector reached forebrain only."

*Limits.* "Not WWOX evidence. The P10 arm is `UNVERIFIED`, not a recovery failure. No electrographic recording was
possible, so that model's seizure endpoint is behavioural. No myelin or glial endpoint exists in it. The two
late-delivery sources that bound the generalisation are abstract level, and one of them never locates onset."

*Rests on:* R37-R44, R66, R72, R77. *Changed in this round:* **R66 added** — the pre-onset survival row the review
found missing behind three decision lines; the expression statement re-attributed to its real source; the two
late-delivery precedents added.

### C4 · Myelin and white matter: what is recovered, what is arrested, and what is genuinely untested

*Statement.* "The two hypomyelination models reachable by this package's queries were both treated before onset and
the sheath moved least in both, reaching about a tenth of control with reduced compaction in one and remaining below
control in the other, while oligodendrocyte number (81-101 percent of control), apoptosis, glial markers, respiration,
locomotion and lifespan moved far more; conduction velocity reached about a sixth of control and correlated with the
myelin level. Even a **germline** correction of the same lesion increased myelination to only about half of wild type
with incomplete compaction, while conduction velocity, motor function and lifespan reached wild-type levels. Both
author groups state that treating later in disease was not done. Outside those gene families the class is **not
empty**: an astrocyte-directed vector given at 10 months of age, stated by its authors as seven months after
cerebellar white-matter vacuolation onset and called a post-symptomatic strategy, **fully rescued** vacuolation to
control levels against a null-vector arm in the same genotype and normalised raised water content in every affected
region, while diffusion metrics improved only partly and a progressive motor deficit documented two months before
treatment reverted within two to four months; a single systemic administration as late as P20 in a null that dies
within a month rescued lethality and globally improved myelination with residual lipid abnormalities; and enzyme
re-expression improved or normalised oligodendrocyte and neuronal lineage markers with the effect **blunted in old
animals**, the authors attributing the limit to neuronal rather than oligodendrocyte recovery. A second antisense
hypomyelination precedent extended lifespan and improved motor phenotypes and seizures and recovered visual evoked
potential latencies, but its authors' own verb is that it **prevents** myelin and oligodendrocyte loss, so it is an
early-window result."

*Limits.* "Not WWOX evidence. **None of the post-onset white-matter sources measured myelin sheath morphometry** —
no electron microscopy, no g-ratio — and that remains the genuine null after five bounded searches by this package and
three by the reviewer. All three correct a glial or metabolic lesion in the cell that carries it; the Wwox myelin
deficit follows a **neuronal** defect and the oligodendrocyte-lineage deletion is phenotypically silent, so the target
cell differs. Vacuolation and water content are not myelin; a composite human imaging severity score is not a myelin
measurement. Two of the three late sources are abstract level and one never locates onset. One source's major stated
limitation is that the oligonucleotide failed to reach cerebellar granule neurons by any route tried — the structure
that carries the ataxia phenotype. One source was read through an open article page rather than structured text."

*Rests on:* R24-R31, R47, R54-R59, R67-R76. *Changed in this round:* **the generalised null withdrawn** as a search
artefact; R31 regraded partial with myelination outside the restored-to-wild-type list; R28's asserted dissociation
removed; R24 regraded partial for censoring; R55's fold value declared a figure reading; R58's attestation replaced by
a verified verbatim span; R67-R76 added.

### C5 · The cost of restoring, and the indispensability of a treated wild-type arm

*Statement.* "Two interventions changed behaviour in treated wild-type animals, so without a treated wild-type arm an
intervention effect is scored as a rescue; in one of them the source's own reading of that change is benefit rather
than harm, so its direction is contested. Against that, modest vector-mediated overexpression in wild-type brain was
tolerated in three independent sources, one of which also reports that overexpression of its gene is separately
deleterious — producing a phenotype worse than the null — while the exposure used produced no detectable harm. The
hazard is therefore specific to the exposure and to abrupt conditional reactivation, not to gene addition as such."

*Limits.* "Not WWOX evidence. No powered toxicity or tumour-surveillance endpoint in any of them; single exposures;
hazards are gene-specific and do not transfer numerically, and WWOX overexpression has its own recorded signals
(ectopic protein moved organoid readouts beyond wild type; applied recombinant protein lowered viability)."

*Rests on:* R18, R19, R44, R71, R78.

### C6 · Human timing precedent, spinal muscular atrophy

*Statement and limits.* As in the review's section 4 entry for this source, with `model_type: human_clinical_report`
and the cross-trial provenance **inside the statement**: the symptomatic comparison (64 and 44 percent reaching the
same endpoint, months later) is a secondary statement inside the pre-symptomatic report, flagged by its own authors as
limited by differing design, endpoints and eligibility, and the symptomatic primary reports were not read here. Even
pre-symptomatically, 5 of 14 were below the normal gross-motor range at 18 months.

*Rests on:* R50-R53. *Changed in this round:* R50's quote re-cut to a contiguous span (the previous version silently
elided a confidence interval).

### C7 · Human timing precedent, metachromatic leukodystrophy

*Statement and limits.* As in the review's section 4 entry, with `model_type: human_clinical_report` and the cognitive
denominator attributed to **the assessed treated cohort as a whole, which included early-symptomatic children**: 20 of
25 showed normal acquisition at ages at which the untreated cohort was severely impaired, and 5 of 25 did not. The
composite white-matter and atrophy score stabilised in every treated group but plateaued at a worse level when
treatment followed symptoms; children entering rapid progression did not benefit, two dying of progression with
engraftment and enzyme levels normal. Benefit arrives by cross-correction from engrafted donor-type myeloid progeny,
not by restoration in the affected neural cell, with a months-long latency.

*Rests on:* R45-R49. *Changed in this round:* R48's denominator corrected and its age field set to `not_stated`
because the cohort is mixed, so it cannot sit in a timing cell; R45's status corrected from `RECOVERED` to `PREVENTED`,
since a `RECOVERED` status with a `pre_onset` age contradicts the timing-only vocabulary.

---

## 2 · Contributions to `inferred` and `counter_evidence`

**Inferred, A — the endpoint-class split, corrected.** "That the prevented-versus-recovered split runs by endpoint class
alone. Endpoints sustained by ongoing dysfunction — seizures, network firing, astrogliosis, the cortical transcriptome
— recovered after onset in two channel or channel-transcript models, with interneuron excitability moving but
overshooting. Endpoints that are accumulated structure **have not been measured after onset at the level of the myelin
sheath in any model**; the only post-onset structural readouts on record are a composite human imaging score that
stabilised at a stage-dependent plateau and a rodent white-matter vacuolation and water-content endpoint that was fully
reversed in a glial-gene lesion. Endpoints with a peripheral or growth component recovered least, failing even
pre-onset. This is a hypothesis built on non-WWOX models and is not established for WWOX." (R01-R09, R25, R42, R47,
R54, R67, R68.)

**Inferred, B — the window as a candidate modality artefact.** Unchanged in substance from the first issue, which the
review called the best single proposal in either package, with two additions: the expression generalisation is the
authors citing others and their own unpublished work, and two late-delivery precedents show it is route-, capsid- and
promoter-specific rather than age-specific. (R09, R37-R39, R72, R77.)

**Counter-evidence lines.** (i) The cellular interneuron measure overshot rather than normalised, so a firing or
excitability success criterion needs its acceptable direction fixed in advance (R06, R07). (ii) Two interventions
changed behaviour in treated wild-type animals, and for one the direction of that change is contested between the
source and this record (R18, R19). (iii) Benefit has decayed and has required re-treatment (R23, R61). (iv) Human
post-symptomatic treatment failed outright in rapidly progressing cases whose molecular correction was successful, and
the **composite imaging** white-matter and atrophy score was arrested at a stage-dependent plateau rather than
reversed; that score is not a myelin measurement (R46, R47). (v) Two external models could not be asked the question at
all because death follows the first seizure; the WWOX null is a third — though a short lifespan does not by itself
forbid a later-delivery design, since a systemic arm at P20 worked in a null that dies within a month (R32, R37, R72).

**Contribution to `notes`.** "External precedents place post-onset recovery on record for seizure, network,
behavioural, cognitive and glial endpoints, and for a white-matter vacuolation and water-content endpoint in a
glial-gene lesion. No source reached by these searches has measured whether an established hypomyelination
re-myelinates under gene restoration in a neuron-driven lesion, and none has measured myelin sheath morphometry after
onset in any lesion. No source has measured interneuron number."

---

## 3 · Withdrawn proposals

1. **Observation identifiers `O7`-`O12`: withdrawn.** They collide with the sibling package, and the Orchestrator owns
   one consolidated set. The content is above as C1-C7.
2. **A new `model_type` for human clinical precedents: withdrawn.** `needs/needs.json` already carries
   `human_clinical_report` on nine observations and its `vocabularies.evidence_scope` text defines it as marking an
   uncontrolled case or series. Both human sources here are uncontrolled in that sense, so the existing value fits;
   the trial-versus-series distinction belongs in `limits`. I had not checked the file's existing values before
   proposing, which is the error.
3. **A fifth `window_state` (`attempted_post_onset_uninterpretable`): withdrawn.** The four states attach to the WWOX
   need entry and to `card_windows` for the two WWOX cards, and by the module rule this package states twice, a
   non-WWOX observation never takes a window state — so the proposed value would have had no row to hold. One of its
   two intended occupants (R62) also turns out to be a pre-onset arm. The fact is already carried twice, by
   `status_vocab` on the row and by the observation's `limits`. If a WWOX arm is ever run after onset without
   measuring the restoration achieved, add the state then and gloss it as applying to WWOX arms only.

---

## 4 · Card and work-order contributions (corrected wording)

Nothing was edited. All four target fields were verified to exist.

**`C01_aav9_wwox` and `C04_aav9_endpoint_families`, `p4_fields.temporal_or_model_limit`** — append as proposed in the
first issue, which the review upheld unchanged, plus: "Two late-delivery precedents outside this gene family show the
rodent expression generalisation behind that cliff is specific to route, capsid and promoter rather than to age."

**`C01_aav9_wwox`, `p4_fields.endpoint_pursued`** — corrected: "Among external precedents the seizure and network class
is the only one with clean post-onset recovery, and **both clean cases are channel or channel-transcript lesions**; for
a non-channel gene the class is split, so spike-wave discharge rate is the endpoint this card should expect to move
only if the WWOX deficit is sustained rather than developmentally built. Severity and onset latency dissociated in a
precedent, so a rate alone is not sufficient."

**`C04_aav9_endpoint_families`, `p4_fields.functional_evidence_available`** — corrected: "External precedents that
quantified myelin after restoration reached about ten percent of wild type with reduced compaction and conduction
velocity about seventeen percent, both before onset; even a germline correction of the same lesion reached only about
half of wild-type myelination with incomplete compaction while conduction velocity, motor function and lifespan reached
wild-type levels; the human composite white-matter score was arrested, not reversed, and at a worse plateau when
treatment followed symptoms; and the one post-onset structural reversal on record is a white-matter vacuolation and
water endpoint in a glial-gene lesion, with no sheath morphometry measured anywhere. The unquantified myelin panels in
the treated arms of this card's source should not be read as a stronger result than those."

**`view/work_order.json`, the `NEED-WWOX-GENE-ADDITION` entry's `data`** — append as proposed in the first issue, which
the review upheld, with one word changed: the myelin clause reads **sheath structure**, not "myelin".

**`ranking_it8_p9_20261029`, the `INV-01` row** — corrected, and no longer phrased as a pre-commitment: "Per-endpoint
wording from external precedent: the seizure and network endpoints carry the arm's power in the two clean channel-gene
precedents; score the myelin endpoint as arrest versus reversal rather than as recovery, noting that sheath structure
after onset has no precedent in either direction while white-matter abnormality has one reversal on record in a
glial-gene lesion; treat a negative result as uninterpretable unless the restoration achieved at the treatment age was
measured." `INV-01` keeps rank 1: nothing here answers it, and the correction round strengthens the case for running
it, because the one comparable later-age experiment on record was left uninterpretable by a missing measurement the
WWOX arm can cheaply include.

---

## 5 · Statements about the registries (nothing changed)

1. **No change to any of the four scientific current files is proposed.** Every row is an external precedent or a human
   clinical report, and none changes a `window_state`.
2. **No claim, paper or working-model record is proposed for creation, edit or revival.** No CLAIM id is touched. The
   seven `abstract_only` sources are not proposed as inputs to any card or need: they are table rows and nothing more.
3. **`sources.papers` for the need** would gain PMIDs 35013317, 36173683, 32610343, 31943325, 39847501, 35065785,
   35715566, 28100454, 37901435 and 40051162, each with an empty `paper_registry_ids` list (none is in the paper
   registry). The six abstract-only PMIDs are deliberately excluded.
4. **Nulls, as bounded searches rather than absences.** (a) No post-onset restoration study for Stxbp1, Scn2a or Kcnq2:
   queries Q10, Q11, Q13, Q14, Q24, Q25, 93 records title-screened, 2026-11-05; the reviewer's V02 corroborates the
   Stxbp1 half. (b) **No source measuring myelin sheath morphometry after a documented onset, in any gene family**:
   queries Q16, Q23, Q30, Q31 (2026-11-05 and 2026-11-06) plus the reviewer's V01, V03 and V06; Q30 returned one hit
   that proved to be an unrelated ocular-surface review and Q31 returned none. (c) No source measuring interneuron
   number at any timing: my own searches plus the reviewer's V04 and V07 independently. **The first issue's broader
   myelin null — that no post-onset myelin arm exists at all — is withdrawn: it was an artefact of queries anchored on
   six gene symbols, and is replaced by (b).**
5. **One boundary crossing to record.** PMID 23011033 lies in the gene family assigned to the sibling package. It was
   read at abstract level on the Orchestrator's explicit instruction in the correction round; the claim was taken with
   `paper_packet.py claim` and returned no competing claim. Flagged in the row and here so the integrator knows why the
   boundary moved and can de-duplicate if the sibling package also carries it.
