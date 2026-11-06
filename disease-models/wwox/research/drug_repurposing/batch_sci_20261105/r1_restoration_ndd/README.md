# R1: restoration after onset in syndromic neurodevelopmental disorder models

Non-canonical research material, Scientist label `sb-r1`, task `ORCH-SCIBATCH-DR-20261105`, challenge
`CH-SB-POSTONSET-RESTORATION`, written 2026-11-05. **Not medical advice.** No dose, schedule, route or
preparation appears here for any species; where a source stated one it was deliberately left out. Public
edition: the subject is the WWOX-DEE reference genotype class and nothing here is an individual-level record.
This file changes none of the four scientific current files, no registry and no ledger. A knockout is not an
inhibitor, an association is not modulation, and "rescue" below is always the authors' word for a measured
change in a stated endpoint of a stated model.

Evidence table: `evidence_r1.tsv` (95 rows, 22 sources). Queries: `queries.tsv` (34 entries).
Staged receipts: `receipts/` with `receipts/INDEX.tsv`. Nothing was recorded to the ledger.

**Revised 2026-11-06 after a blind locator audit (`verify/audit_R1/`) and an independent review
(`verify/review_R/`).** Row-level responses to every finding are in `RESPONSE.md`. Four sources were added
on instruction, two blocked sources were re-acquired, 12 rows were corrected, three rows were re-binned out
of `cognition_behaviour`, and decision lines 1, 5, 9 and 10 were rewritten. Two sources
(PMID 18389497, PMID 18495876) carry `source_depth` = "partial_fulltext re-acquired by producer via article
page; not independently verified"; every headline count below is given both with and without them.

---

## Decision (10 lines)

1. **DATO** — Within the 22 sources read here, **no study restored the deficient gene after a documented
   onset of a myelin phenotype and then measured myelin sheath structure.** Seven of the eight myelin rows
   are pre-onset or unlocated-onset arms; the eighth (`R49`) is a post-onset arm in which myelination was
   not measured at all. **Outside this gene set the class is not empty** — the reviewer found an
   astrocyte-directed vector given seven months after a stated onset of white-matter vacuolation that
   reversed white-matter water accumulation and a motor deficit against an untreated same-genotype
   comparator (PMID 40051162), a systemic administration as late as postnatal day 20 in a short-lived
   leukodystrophy null that improved myelination (PMID 23817205), and enzyme re-expression reported to
   reverse dysmyelination with the effect blunted in old animals (PMID 37149081). None measured sheath
   morphometry and all three correct a glial or metabolic lesion, so what is empty is **sheath structure
   after onset in a neuron-driven lesion**, not the myelin class.
2. **DATO** — Cellular neuronal structure *does* move after onset: soma size, dendritic length and
   hippocampal spine density became statistically indistinguishable from wild type in symptomatic Mecp2
   animals (PMID 22525157); striatal spine density rose after adult Shank3 restoration, overshooting wild
   type (PMID 26886798); cortical spine density was corrected by a post-onset drug in Fmr1 (PMID 22500629).
3. **DATO** — The tissue-level structural measure in that same Mecp2 study did not move: cortical thickness
   "was not reversed to a statistically significant extent" (PMID 22525157).
4. **DATO** — Circuit and physiology endpoints recover most reliably. Adult restoration fully corrected every
   identified prefrontal physiological deficit in an Angelman model, with the authors stating "there is no
   critical developmental window" for them (PMID 30082419); hippocampal plasticity recovered at every age
   tested in the same disorder (PMID 25866966).
5. **DATO** — Seizure endpoints split, and the split is not between prevention and recovery. Two
   conditional-reactivation arms failed after onset: epileptic spasms fell with early restoration and not
   with late (PMID 39855191), and the seizure phenotype was "refractory to postnatal Ube3a reactivation"
   (PMID 25866966). But post-onset successes in this same set are genetic, not only pharmacological: adult
   conditional restoration eliminated interictal spiking in the same animals before and after
   (PMID 31025938), and **antisense reactivation of the very locus behind one of the two failures gave a
   full rescue of audiogenic seizure susceptibility at the same postnatal age** (PMID 34369389). The
   earlier wording of this line — that the one post-onset seizure success was a pathway drug — was
   contradicted by rows `R13`, `R14` and `R19` of this table and is withdrawn.
6. **DATO** — Behaviour splits by domain *inside single studies*: social and repetitive behaviours recovered
   in adulthood while anxiety and motor coordination did not (PMID 26886798), and working memory resisted
   restoration at every age and in both sexes across two independent alleles (PMID 39855191).
7. **DATO** — Restoring the gene too abruptly killed animals in two independent models (PMID 17289941,
   PMID 34651584); three rows in the table carry `outcome = worse`.
8. **INFERENZA** — What may decide the difference is whether the endpoint is *maintained by ongoing gene
   function* or was *built once during development*. The Angelman case is consistent with it for slice
   plasticity against behaviour, but it is no longer a clean case: the same gene's rhythm and provoked-seizure
   endpoints recover after onset under antisense reactivation, with improvement correlated to the protein
   level reached (PMID 36594817, PMID 34369389). **Restoration mode and level achieved are not separated
   from the temporal requirement in any of the genes that fit**, so this stays INFERENZA and not DATO.
9. **INFERENZA** — For the reference genotype class the honest external expectation is that a post-onset arm
   could move network and cellular readouts. Within the syndromic single-gene models searched here, myelin is
   untested after onset; outside them a white-matter abnormality **has** been reversed after a documented
   onset in a glial-gene leukodystrophy. The expectation therefore rests on the sheath-morphometry and
   neuron-driven-lesion parts of the question, not on an empty class.
10. **IPOTESI** — The `INV-01` added arm should be worded per endpoint class, and **quantified myelin sheath
    structure in a neuron-driven lesion** should be the discriminating measurement: that sub-class has no
    external precedent, while white-matter abnormality after onset now has one in the positive direction. The
    test that separates the two readings is whether quantified sheath structure moves while spike-wave rate
    does — with the caveat of line 5 that the external precedent for the spike-wave class is **split**, not
    negative, so a null there is neither expected nor surprising.

### How the status vocabulary was applied

The closed set (`PREVENTED`, `RECOVERED`, `EARLY-WINDOW`, `UNMEASURED`, `UNVERIFIED`) has no value for an arm
that *was* given after a manifested phenotype, *was* measured, and did *not* move. `UNMEASURED` would be
false, because it was measured. So in `evidence_r1.tsv` **`status_vocab` carries the timing class of the arm**
(`RECOVERED` = restoration followed a manifested phenotype) and **`outcome` alone carries the result**
(`full`, `partial`, `none`, `worse`). A `RECOVERED` row with `outcome = none` therefore means "tested after
onset and did not move", which is the single most informative row type for this challenge.

**Corrected attribution of this deviation (2026-11-06).** The earlier note said the deviation was from
`rescue_window_it6_20261029.md`. That is wrong and the review is right: that file defines the vocabulary as
timing-only ("RECOVERED (intervention follows a manifested phenotype)"), which is the same reading used here.
What embeds movement is (i) that file's own summary-table column and its usage lines ("Nothing RECOVERED"),
and (ii) `BRIEF_R1.md`, which restates RECOVERED as "restoration follows a manifested phenotype **and the
endpoint moves toward control**". The deviation is therefore from **the brief**, not from the IT6 record.

Four rows apply the convention imperfectly and the review is right to name them: `R67`, `R68`, `R74` and
`R75` carry `RECOVERED` with `age_at_restoration_vs_onset` = `not_stated` (two a transgene bypass, two an
abstract-only pathway drug). They are left as they are rather than silently re-labelled, because the
honest value for them is "timing unknown", which the closed set does not carry either; they are excluded
from every post-onset count in this file by the age filter.

---

## Matrix: endpoint class by restoration timing

Counts are `studies | rows` from `evidence_r1.tsv`. **This is not a meta-analysis.** The models differ in gene,
lesion class, lifespan and assay; nothing here is pooled, averaged or weighted. Publication bias runs one way
throughout: a restoration study that moved nothing is much less likely to exist as a paper, so the `none` and
`worse` cells are almost certainly under-counted relative to the `full` cells, and the strongest `none` rows in
this table are the ones reported *inside* otherwise positive papers.

All 95 rows, 22 sources.

| Endpoint class | pre_onset | post_onset_early | post_onset_advanced | adult | not_stated |
|---|---|---|---|---|---|
| survival | 2 \| 3 | 1 \| 1 | 2 \| 3 | - | 2 \| 2 |
| seizure_or_network | 1 \| 1 | 6 \| 9 | 3 \| 4 | 6 \| 9 | - |
| motor | 1 \| 1 | 2 \| 2 | 1 \| 1 | 2 \| 2 | - |
| cognition_behaviour | 6 \| 7 | 7 \| 13 | 2 \| 2 | 3 \| 5 | 3 \| 4 |
| neuronal_structure | 2 \| 3 | 3 \| 4 | 2 \| 4 | 1 \| 1 | 3 \| 3 |
| myelin_glia | 2 \| 4 | - | 1 \| 1 | - | 2 \| 3 |
| systemic_metabolic | - | 1 \| 1 | 1 \| 1 | 1 \| 1 | - |

### The same rows restricted to post-onset arms, by outcome

A `not_measured` column is added, because the review was right that its absence was what made the myelin row
print as empty when it is not: `R49` is a post-onset arm in which myelination was not measured, and that
is stronger stated than hidden.

| Endpoint class | full | partial | none | worse | not_measured |
|---|---|---|---|---|---|
| survival | - | 2 \| 2 | - | 2 \| 2 | - |
| seizure_or_network | 8 \| 10 | 5 \| 8 | 3 \| 4 | - | - |
| motor | 1 \| 1 | 2 \| 2 | 2 \| 2 | - | - |
| cognition_behaviour | 3 \| 3 | 6 \| 9 | 6 \| 8 | - | - |
| neuronal_structure | 3 \| 4 | 2 \| 2 | 2 \| 2 | - | 1 \| 1 |
| **myelin_glia** | **-** | **-** | **-** | **-** | **1 \| 1** |
| systemic_metabolic | 1 \| 1 | 2 \| 2 | - | - | - |

### The same post-onset matrix without the two sources that are not independently verified

PMID 18389497 and PMID 18495876 were unreachable to the blind auditor and were re-acquired by me on
2026-11-06 through the route this file already declared. That is re-confirmation by the producer, not
independent verification, so the headline version of the matrix excludes them (86 rows, 20 sources).

| Endpoint class | full | partial | none | worse | not_measured |
|---|---|---|---|---|---|
| survival | - | 1 \| 1 | - | 1 \| 1 | - |
| seizure_or_network | 8 \| 10 | 4 \| 7 | 3 \| 4 | - | - |
| motor | 1 \| 1 | 2 \| 2 | 2 \| 2 | - | - |
| cognition_behaviour | 3 \| 3 | 6 \| 9 | 6 \| 8 | - | - |
| neuronal_structure | 3 \| 4 | 1 \| 1 | 2 \| 2 | - | 1 \| 1 |
| **myelin_glia** | **-** | **-** | **-** | **-** | **-** |
| systemic_metabolic | 1 \| 1 | 2 \| 2 | - | - | - |

**Reading the myelin row correctly.** It is not that myelin was measured after onset and failed; it is that
in the headline set it was never measured after onset at all, and in the full set the single post-onset arm
reports no myelination in any section (`R49`, re-confirmed 2026-11-06). The one myelin endpoint that moved
under treatment (PMID 18495876, `R50`) sits in an arm begun between postnatal days 7 and 9 with no stated
onset for that endpoint — `EARLY-WINDOW`, not recovery — and its Results word is "effectively restored"
while its abstract says "improved". Three targeted searches found no post-onset myelin arm in this gene
space (`Q12`, `Q16`, `Q18`); the reviewer's four searches found three outside it (decision line 1), so the
null is scoped to sheath morphometry in a neuron-driven lesion.

**Interneuron endpoints, corrected.** The earlier claim that interneuron endpoints are `UNMEASURED` in every
source was too broad. Interneuron **number** after post-onset restoration remains a bounded null, now
corroborated by the reviewer's own independent search. Interneuron **structure** is no longer unmeasured:
a brief pathway inhibition confined to the third postnatal week rescued parvalbumin perisomatic innervation
and adult social behaviour in a cell-type-restricted Tsc1 lesion (PMID 34135323, rows `R90`-`R92`). It is a
drug and a prevention arm, not post-onset gene restoration, but it is an author-stated sensitive period with
a biological anchor and it belongs in the transfer table, which is where it now is.

---

## Evidence by theme

**The gene is needed now versus the damage was done then.** Two mirror experiments bound the question from
both sides. Deleting Ube3a at 3 or 12 weeks "did not have a significant effect on most behavioral tasks"
(PMID 31143434), so the behavioural damage is built early; and restoring it at those ages does not undo it
(PMID 25866966). Against that, deleting Cdkl5 post-developmentally *does* disrupt behaviour, and restoring it
post-developmentally recovers much of it (PMID 34651584) — a gene with a real adult job. Syngap1 is explicitly
read by its own authors as having both kinds of function at the same synapses (PMID 31025938). This is the
mechanism behind line 8 of the decision, and it is gene-specific rather than general.

**Circuit and physiology.** The strongest recoveries in the set are electrophysiological: interictal spiking
eliminated by adult restoration, measured in the *same animals* before and after (PMID 31025938); every
identified prefrontal current and interneuron excitability measure fully corrected at 14 weeks of age
(PMID 30082419); striatal field responses and miniature current frequency restored to wild type in adults
(PMID 26886798); hippocampal plasticity recovered at juvenile and adult ages alike (PMID 25866966,
PMID 17289941). Two of these carry an explicit no-window statement.

**Structure.** Post-onset restoration normalised soma size, dendritic length and spine density in symptomatic
Mecp2 animals (PMID 22525157) and raised striatal spine density in adults (PMID 26886798) — but in the second
case *above* wild type, which the authors read as spines escaping developmental pruning. Restoring the gene in
astrocytes alone restored neuronal dendritic morphology non-cell-autonomously (PMID 21716289). Against this:
cortical thickness did not reverse (PMID 22525157), and neuronal dysplasia and migration were unchanged even
in an early-treated arm (PMID 18495876).

**Myelin and glia — corrected 2026-11-06.** Seven of the eight myelin rows are prevention or unlocated-onset
rows and the eighth is a post-onset arm in which myelination was not measured (`R49`). The readout level now
travels with the conclusion, as the review required: the lineage-restriction rows (`R57`-`R59`) rest on two
myelin protein levels and on the thickness of **myelin basic protein immunostaining** in the corpus callosum
measured at **postnatal day 16**, with no electron microscopy in that source — a marker measure, which this
file's own transfer table excludes from functional weight. The nearest analogue to the
module's own question is the inverse experiment: restoring Mecp2 *only* in the oligodendrocyte lineage left
one myelin protein at about 60 per cent of control and another "remained aberrant", with the authors
attributing the residue to a non-cell-autonomous effect of other cell types (PMID 24285883). At abstract level,
raising a different protein in a Tcf4 model rescued a learning endpoint while "OL gene expression and molecular
phenotypes ... are unchanged" (PMID 41997465) — behaviour moving while myelin does not, in the same animals.
Astrogliosis was *prevented* by early pathway inhibition and only partly reduced by the same drug given after
seizure onset (PMID 18389497).

**Seizures — rewritten 2026-11-06.** This is where the correction round changed the most. Two
conditional-reactivation arms failed: early restoration reduced epileptic spasms and late restoration did
not, in two independent alleles with two Cre drivers (PMID 39855191, the authors' summary being that the
occurrence "appears to be preventable upon early re-expression ... but becomes limited if expressed after
seizure onset"), and postnatal Ube3a reactivation left seizures in place (PMID 25866966). Against that, four
post-onset successes: interictal spiking eliminated and provoked threshold raised after adult conditional
restoration, within animals (PMID 31025938, the threshold result holding at the tonic-clonic stage only
after the audit's correction); a provoked threshold suppressed by a pathway drug that also moves wild-type
animals (PMID 22500629); seizures suppressed by a pathway drug begun after onset whose effect did not
outlast it (PMID 18389497); and **a full rescue of audiogenic seizure susceptibility by antisense
reactivation of the same Ube3a locus at the same postnatal age that the conditional switch failed at**
(PMID 34369389). Gene class correlates with the split across these studies but is not established as its
cause: the same gene sits on both sides once restoration mode changes.

**The sub-class that matters most here is the one that still failed.** The antisense study that rescued
electroencephalographic rhythm and sleep in juveniles *and* adults (PMID 36594817) reports that it did
**not** reduce cortical poly-spike frequency at either age — its own epileptiform endpoint
(`R86`). Spike-wave discharge rate, the module's carried endpoint, is an interictal epileptiform measure and
is nearer to poly-spikes than to a power-spectrum ratio. So the external precedent for a rhythm or biomarker
endpoint after onset is positive, and for an epileptiform endpoint after onset it is genuinely split:
recovered in one gene (interictal spiking, PMID 31025938), not recovered in another at two ages
(PMID 36594817), not recovered in a third late arm (PMID 39855191). Both of the sources that make this
precise were read at full text here and at abstract level by the reviewer, which is why this paragraph
qualifies the reviewer's combined statement rather than simply adopting it.

**What the authors say decides it.** Two of the new sources measure the restoration level and tie it to the
result: improvement "tracks the increase in Ube3a protein levels across different ASOs" (PMID 36594817), and
the weaker adult arm is attributed by its own authors to the smaller protein increase rather than to lost
reversibility (`R87`, `R88`). A third reports a post-onset behavioural gain at low and uneven coverage, with
expression "sporadic at the cellular level" (PMID 32125365, `R95`), which stops level achieved from being a
sufficient explanation of every negative. Level, distribution and timing are confounded in every study in
this set.

**Survival and systemic endpoints.** Survival moved after onset in two models (PMID 17289941, PMID 18389497)
and partially in a glia-restricted arm (PMID 21716289). Systemic endpoints moved only partially everywhere
they were measured: macroorchidism "partially corrected" (PMID 22500629), respiratory pattern normalised in
most but not all animals (PMID 21716289), obesity reversed in a single illustrated animal (PMID 17289941).

**Critical periods the authors named.** Motor coordination in Angelman mice has a window that "closes between
3 and 6 weeks postnatally" (PMID 25866966). Pitt-Hopkins restoration at postnatal day 14 "largely fails to
correct most phenotypes, except for a measure of cognitive function", which its authors call "a narrow, early
critical window" (PMID 41509287), against neonatal restoration in the same model that improved several
endpoints (PMID 35535852). Shank3 restoration at postnatal day 20 to 21 improved what adult restoration could
not (PMID 26886798). Cdkl5 is the counter-case: its authors claim "a broad therapeutic time window"
(PMID 34651584) while the two-allele study narrows that to specific domains (PMID 39855191) — and a vector
gene replacement in the same gene delivered at 28 to 30 days gave significant behavioural improvement with a
cerebellar structural correction confined to high-expression regions (PMID 32125365, abstract only), which is
a third reading of the same gene's window. Added in this round, and the only one with a biological anchor
rather than a day range: a sensitive period "during the third postnatal week" in which a brief pathway
inhibition rescued parvalbumin perisomatic innervation and adult social behaviour, anchored to the
maturation of that innervation plateauing at the end of the first postnatal month (PMID 34135323). Against
all of these, two antisense studies state the window is wider than the conditional-reactivation literature
implies (PMID 34369389, PMID 36594817) — for the endpoints they measured, and not for the epileptiform one.

---

## Counter-evidence (38 rows, `role = counter`)

Each support row in the table was paired with a deliberate search for the opposite. What the counter rows say:

- **Restoration after onset fails outright for named endpoints.** Anxiety, locomotion and motor coordination
  after adult Shank3 restoration (PMID 26886798); working memory at every age and both sexes (PMID 39855191);
  four behavioural endpoints at every postnatal age in Angelman mice (PMID 25866966); hyperactivity and
  elevated-plus-maze behaviour after juvenile Tcf4 reinstatement (PMID 41509287); hyperactivity tracked in the
  same animals before and after Syngap1 restoration (PMID 31025938).
- **Restoration can make things worse.** Abrupt reactivation killed 9 of 17 animals in one model
  (PMID 17289941) and caused "significant lethality ... selectively in Res mice" in another (PMID 34651584);
  withdrawing a pathway drug after months of benefit returned the phenotype and the deaths (PMID 18389497).
- **A positive structural result is contested.** The spine-density correction after onset (PMID 22500629) is
  directly opposed by a study cited in that same paper reporting rescue "when treatment started at birth, but
  not when treatment started in 6-week-old animals". I read this through the citing paper only; compound,
  duration and receptor occupancy all differ, so the disagreement is not clean.
- **A drug that moves wild type is not repairing the lesion.** For several endpoints the mGlu5 inhibitor "also
  had a proportional effect on WT mice" (PMID 22500629). This is the same caution the module already records
  for the Meis2 lead in `advance_it8_p5_20261029/loop2_broad_recovery/README.md`.
- **Cell-type ceilings.** Restoring the gene in one lineage only partially rescues, and leaves myelin proteins
  wrong (PMID 24285883); cell-type-restricted embryonic restoration rescued only a subset even under
  prevention conditions (PMID 35535852).
- **A missing comparator can manufacture a recovery.** The study with the best post-onset structural result had
  no untreated same-genotype arm surviving to the measurement point, which its authors say "somewhat hinders a
  straightforward 'treatment–effect' interpretation" (PMID 22525157). This is exactly the gap
  `rescue_window_it6_20261029.md` already records inside the module's own corpus.

---

## What supports, narrows or contradicts the sentence the brief quotes

The brief's `INV-01` question is: *does neuronal WWOX restoration started after symptom onset recover any
endpoint, or only prevent one when given in the neonatal window?* The external precedents **narrow** it rather
than answer it, and they narrow it unevenly:

- **Supports "recovery is possible in principle":** post-onset restoration recovered circuit physiology,
  cellular structure, cognition and survival in at least six independent models, and two sets of authors state
  there is no critical window for their physiological endpoints.
- **Narrows it to endpoint classes:** the same studies that recovered those endpoints failed on others, and
  the failures cluster in developmentally-built behaviours (anxiety, working memory, motor coordination) and
  tissue-level structure (cortical thickness, dysplasia).
- **Splits a seizure expectation rather than contradicting one.** Two conditional arms failed after onset and
  four arms succeeded, one of them on the same locus as a failure under a different restoration mode. Since
  the module's single carried WWOX endpoint is spike-wave discharge rate — an interictal epileptiform
  measure — the right statement is that **its external precedent is split, not negative**: the nearest
  analogue failed at two ages in one gene (PMID 36594817) and recovered in another (PMID 31025938). The
  earlier claim that this was "the prediction most at risk" is withdrawn; it is the prediction the external
  evidence leaves unresolved.
- **Narrows, rather than empties, the myelin question.** The expected return in the brief's consequence
  table — "structural or myelin endpoints rarely recover after onset while circuit or behaviour endpoints
  partly do" — is **partly right and partly wrong in both directions**. Circuit and behaviour endpoints do
  partly recover. Structural endpoints at the *cellular* level recover better than the brief anticipated
  (and better than this package first graded them, after the audit moved two rows from partial to full); at
  the *tissue* level they do not. Myelin is not "rarely recovered after onset" in this gene set: it was
  never measured after onset there. Outside the gene set it has been moved after a documented onset, in
  glial-gene lesions and without sheath morphometry.
- **Brief consequence row 2 now fires, through the reviewer.** That row pre-registered that if at least one
  well-controlled model showed myelin or interneuron structure recovering after onset, "recovery of
  structural endpoints after onset is not excluded" would be recorded with that source and its conditions.
  PMID 40051162 meets it at the white-matter level with a located onset and an untreated same-genotype
  comparator, though not at sheath level and not in a neuron-driven lesion. **Recorded here as fired, with
  those two conditions attached.** It was found by the reviewer, not by me; my own queries could not reach
  it, for the reason given under "What was not reachable".

---

## Transfer conditions and transfer breakers

Joined per row in `evidence_r1.tsv`. The template follows the IT29 P3-C shape (on branch `task/it29`,
`disease-models/wwox/research/drug_repurposing/phenotype_first_it29_20261105/p3_C/README.md`), adapted from a
compound-transfer question to a restoration-timing question.

| Item | Pertinent to the reference genotype class if | Breaks the comparison if |
|---|---|---|
| Timing anchor | the restoration age is stated *relative to a measured onset of that endpoint* | the age is stated only in postnatal days with no onset located (then it is `EARLY-WINDOW`, whatever the authors call it) |
| Comparator | an untreated same-genotype arm measured at the same age exists | the only comparator is wild type, or the untreated arm did not survive to the measurement |
| Pre-treatment state | the phenotype was measured in the same animals, or in an age-matched cohort, before restoration | the first measurement of that endpoint is after restoration |
| Lesion viability | the lesion permits survival to the restoration age without rescue | the untreated animal is dead or moribund at the age the precedent treats |
| Mode | restoration of the deficient gene itself | a downstream pathway drug or a different gene (bypass); then the result bounds symptom control, not restoration |
| Compartment | restoration reaches the compartment that drives the endpoint | restoration is restricted to a compartment downstream of the driver |
| Readout level | function, conduction, electroencephalography, or a quantified structural measure | marker intensity or transcript share only |
| Readout granularity (added 2026-11-06) | sheath morphometry (g-ratio, electron microscopy) or myelinated-axon counts | a composite imaging severity score, or immunostaining thickness, read as a sheath measurement — the lineage-restriction rows here are immunostaining at postnatal day 16, not morphometry |
| Lesion compartment, glial side (added 2026-11-06) | the myelin deficit follows the neuronal lesion, as it does in this disease model | the lesion is intrinsic to an astrocyte, oligodendrocyte or metabolic compartment — which disqualifies all three external post-onset white-matter precedents of decision line 1 |
| Timing anchor, biological (added 2026-11-06) | the author-stated period has a stated developmental anchor, e.g. parvalbumin innervation maturation plateauing at the end of the first postnatal month (PMID 34135323) or the myelination peak | a period stated only as a postnatal day range with no process it is anchored to |
| Persistence | benefit outlasts the intervention | benefit requires continued treatment and reverses on withdrawal |
| Dose behaviour | restoration level is near physiological and its toxicity was checked | restoration is supraphysiological or abrupt, where two models show lethality |

---

## What the added arm of `INV-01` must measure, given these precedents (IPOTESI)

1. **IPOTESI** — A pre-treatment measurement of every endpoint in the same animals, or in an age-matched
   cohort sacrificed at the injection day; without it the arm produces another `EARLY-WINDOW` row, not a
   recovery row, exactly as all nine existing WWOX rows do.
2. **IPOTESI** — An untreated same-genotype comparator measured at the *same age* as the treated animals;
   three precedent studies lose interpretability precisely here, and one says so itself.
3. **IPOTESI** — Quantified myelin **sheath structure** (g-ratio or electron microscopy, not marker intensity
   and not immunostaining thickness) as the **discriminating** endpoint: sheath structure after onset in a
   neuron-driven lesion is the sub-class with no external precedent, whereas white-matter abnormality after
   onset now has one in the positive direction in glial-gene lesions.
4. **IPOTESI** — Spike-wave discharge rate recorded *before* restoration in the same animals, and read
   against a split precedent: the nearest external analogue to this endpoint failed at two ages in one gene
   and recovered in another, so neither a null nor a recovery would settle the question on its own. Pair it
   with a power-spectrum or rhythm measure, which is the sub-class that **did** recover after onset at two
   ages (PMID 36594817). Measure and report the restoration level and its regional distribution alongside
   every endpoint: two of the new sources tie improvement to the level reached and one reports a post-onset
   gain at low, uneven coverage, so without that measurement a null cannot be separated from
   under-restoration — the ambiguity that makes this whole external literature hard to read.
5. **IPOTESI** — At least one circuit or cellular readout besides the seizure measure (firing, spine density,
   interneuron count), since those are the classes most likely to move and would otherwise be missed.
6. **IPOTESI** — A cellular-versus-tissue structural pair (spine or soma measure alongside a thickness or
   volume measure), because one precedent moved the first and not the second in the same animals.
7. **IPOTESI** — Graded rather than abrupt restoration, with mortality as a declared endpoint: two models
   killed animals by restoring the gene too fast, and neither effect was anticipated by its authors.
8. **IPOTESI** — Persistence past the first measurement, because the one post-onset seizure success in the set
   reversed when the intervention stopped.
9. **IPOTESI** — The unit of replication stated per figure (animal or differentiation batch, never pooled
   cells), and an equivalence margin fixed before the run; "not significant versus wild type" is not
   equivalence, a point `rescue_window_it6_20261029.md` already makes about the module's own source.
10. **IPOTESI** — A declared discriminating criterion before data: R1 of the module's loop-2 hypothesis is
    supported if a circuit readout enters the wild-type margin while quantified myelin does not, and refuted if
    myelin moves and the circuit readout does not.

---

## Conditions under which these precedents do not transfer to the neuron-restricted, short-lived, hypomyelinated Wwox null

1. **Lifespan forbids the design.** Every post-onset arm in this set treats an animal that would otherwise live
   to adulthood: symptoms at about 6 weeks with death at about 11 weeks (PMID 17289941), haploinsufficiency
   (PMID 31025938, PMID 39855191), viable nulls, or seizure onset at about 1 to 2 months (PMID 18389497). The
   null in the module's corpus is dead at about three weeks. **No precedent in this set treats an animal on
   that timescale**, so none of them licenses a post-onset mouse arm here; the question has to move to a
   slower-onset allele, to organoids, or to an inducible switch, which is what
   `advance_it8_p5_20261029/loop2_broad_recovery/README.md` already concluded for different reasons.
2. **Hypomyelination is not in the precedent set.** None of these models has a hypomyelination phenotype whose
   recovery after onset was tested. The two myelin-adjacent results are a lineage-restricted prevention
   (PMID 24285883) and an early-treated pathway drug (PMID 18495876). A primary developmental myelination
   deficit driven from the neuron is not represented.
3. **The compartment logic is inverted in the nearest analogue.** In the Rett lineage experiment the
   oligodendrocyte itself carries the mutation; in the WWOX corpus the lineage deletion gives no overt
   phenotype and the neuron is the driver. The non-cell-autonomy conclusion is the same in direction but rests
   on a different arrangement, so it transfers as a caution and not as a prediction.
4. **Most precedents are haploinsufficiency or hypomorphs, not complete nulls.** Residual protein changes what
   restoration means. Where a precedent is a true null (PMID 17289941, PMID 22500629) the lesion is still
   compatible with weeks of adult life.
5. **Three of the clearest results are pathway drugs, not gene restoration.** PMID 18389497, PMID 18495876 and
   PMID 22500629 bound what symptom control and downstream correction can do; they are not restoration
   results, and two of them move wild-type animals as well.
6. **Dosage sensitivity is demonstrated for the precedent genes and unknown for this one.** Two models died
   from rapid restoration. Whether neuronal WWOX is dosage-sensitive in that way is not established anywhere
   in the module, so the risk transfers as a design requirement rather than as an expected effect.
7. **Progenitor and radial-glia state is absent from every precedent.** No study here restored the gene after
   onset and measured progenitor composition. The one WWOX post-onset result that exists, the organoid arm,
   did not correct radial-glia abnormalities, and nothing external speaks to that endpoint class at all.
8. **Organoid culture age is not animal age and neither is a human age.** None of these windows, stated in
   mouse postnatal days or weeks, can be mapped onto a treatable age; the precedents constrain *which endpoint
   classes* to measure, never *when* to treat.

---

## What is not established

- Whether myelin **sheath structure** recovers after onset in a neuron-driven lesion. Not established in
  either direction. White-matter abnormality after onset has been reversed in glial-gene lesions
  (decision line 1), and no study in either search measured sheath morphometry after onset anywhere.
- Whether interneuron number recovers after onset anywhere. Not found (`Q16`, bounded search, 20 titles),
  and independently corroborated by the reviewer's own search. Interneuron *structure* is no longer
  unmeasured (PMID 34135323), but that arm is a pathway drug given before the adult endpoint existed.
- Why the same Ube3a locus and the same postnatal age give opposite seizure results under a conditional
  switch and under antisense reactivation (`R37` against `R79`). Restoration mode, restoration level and
  distribution all differ; none of the three is isolated by any design in this set.
- Whether the epileptiform sub-class (poly-spikes, spike-wave discharges) is genuinely less recoverable than
  the rhythm sub-class, or whether the one negative in it reflects the partial restoration its own authors
  name as a candidate explanation.
- Whether the cellular-versus-tissue structural split (PMID 22525157) generalises; it is one study, one model,
  and its own comparator is missing.
- Whether the "ongoing function versus built once" reading of line 8 is more than a restatement of the data. It
  predicts that a gene with a demonstrated adult requirement recovers more after onset; Cdkl5 and Syngap1 fit,
  Ube3a fits inversely, and that is three genes, not a test.
- Whether the seizure nulls are about onset or about age. In PMID 39855191 the variable is the animal's age,
  not the onset of that animal's seizures, which were not individually located.
- Whether the Angelman behaviour-versus-physiology dissociation is a property of the disorder or of the assays;
  the physiological measures are slice measures and the behavioural ones are whole-animal.
- The treatment age of the main glia-restricted arm (PMID 21716289): not stated in the passages read, so those
  rows are `EARLY-WINDOW` and cannot be counted as post-onset.
- Whether the Meikle myelin improvement (PMID 18495876) is prevention or recovery: the onset of the myelin
  deficit is not stated and treatment begins inside primary myelination.

## What was not reachable

- **The two blocked sources were re-acquired on 2026-11-06** (PMID 18389497, PMID 18495876), by the same PMC
  article-page route this file declared as `Q26`, which the blind auditor found serving a bot-check
  interstitial. I did not work around anything: the route simply answered. Every quote in rows `R44`-`R52`
  was re-confirmed, `R49`'s attestation was confirmed (the source reports myelination in no section, figure
  or supplement), and `R51` was confirmed to contain no statement that the phenotype had appeared by the
  treatment start age, which is why its timing stays `not_stated`. These are still producer readings, so
  their `source_depth` says so and the headline matrix excludes them.
- **My own search space could not reach the three post-onset white-matter arms the reviewer found.** My
  queries were anchored on the nine syndromic gene names my brief assigned and on `myelin`/`oligodendrocyte`
  wording (`Q12`, `Q16`, `Q18`). No string in that set could reach a leukodystrophy caused by an enzyme, a
  connexin, a tubulin or an astrocyte transporter. This is a real selection defect in the bounded null, it is
  the reviewer's finding and not mine, and it is the reason decision line 1 was rewritten.
- **PMID 32125365 is `abstract_only`**: Europe PMC reports no open full text and no PMC record for it, so
  rows `R93`-`R95` carry only what the abstract states and none of its methods, comparators or per-endpoint
  results were read.
- **Full text of four records**, by any route allowed for this task. PMID 19211884 (Pten, pathway inhibition)
  is `abstract_only`: its abstract separates "prevent and reverse" for a structural endpoint, which is exactly
  on question, but the treatment ages, the comparator and the stated onset are unread, so it carries a
  conditional lead and nothing more. PMID 41997465 has no PMC identifier at all and is `abstract_only`, as is
  PMID 32125365.
- **Europe PMC REST `fullTextXML` returned HTTP 500** for eight of the eighteen records, meaning no open body
  is held there. `efetch db=pmc` recovered three of those. The PubMed/PMC full-text tool returned empty
  `full_text` for all six it was asked for. The Europe PMC rendered-pdf and article-page routes returned
  HTTP 403 to an automated read.
- **Six records were read through the PMC article page via an automated page-to-text fetch**, which returns
  section-labelled verbatim excerpts and caps each excerpt's length. Those quotes are spans, not always whole
  sentences, and the six receipts say so. I did not view figures in any of them.
- **One route was refused and not worked around.** A direct repeat fetch of a PMC article page hit a bot check;
  I did not attempt to circumvent it and switched to the page-to-text route instead. No service requiring a
  contact address was used, so Unpaywall was not called even where Europe PMC named it as a route for
  PMID 34651584; the Europe PMC route was used instead.
- **Three rows are `cited_in_source_not_read`** (`R17`, `R22`, `R78`): a working-memory null and the two arms
  of a contradicting spine-density result, all read through the citing paper only. Their primary sources were
  not opened. `R43` has the same provenance problem — its `endpoint_detail` says "from the same group's
  earlier work" — and the review is right that it is labelled `partial_fulltext`; it is left as it is because
  the sentence quoted *is* in the audited source, but it should not be read as a measurement made there.
- Methods and supplementary material were not read for most records; figures were not viewed for any. Every
  receipt's `coverage` states this per section, understated rather than overstated.

## Queries

All 34 are in `queries.tsv` with database, exact string, timestamp, hit count and what was done with each
(`Q31`-`Q34` are the correction round of 2026-11-06).
Routes used: the PubMed MCP tools, NCBI E-utilities (esearch, esummary, efetch), Europe PMC REST, and PMC
article pages. Zero spend, no registration, no account, no author contact, no contact address sent anywhere.
No third-party bytes were saved inside the repository; downloads stayed in the session scratch directory.
