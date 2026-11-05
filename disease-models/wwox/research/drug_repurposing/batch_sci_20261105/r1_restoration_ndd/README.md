# R1: restoration after onset in syndromic neurodevelopmental disorder models

Non-canonical research material, Scientist label `sb-r1`, task `ORCH-SCIBATCH-DR-20261105`, challenge
`CH-SB-POSTONSET-RESTORATION`, written 2026-11-05. **Not medical advice.** No dose, schedule, route or
preparation appears here for any species; where a source stated one it was deliberately left out. Public
edition: the subject is the WWOX-DEE reference genotype class and nothing here is an individual-level record.
This file changes none of the four scientific current files, no registry and no ledger. A knockout is not an
inhibitor, an association is not modulation, and "rescue" below is always the authors' word for a measured
change in a stated endpoint of a stated model.

Evidence table: `evidence_r1.tsv` (76 rows, 18 sources). Queries: `queries.tsv` (30 entries).
Staged receipts: `receipts/` with `receipts/INDEX.tsv`. Nothing was recorded to the ledger.

---

## Decision (10 lines)

1. **DATO** — Across 18 external sources, **no study restored the deficient gene after a documented
   phenotype onset and then measured a myelin endpoint.** All eight myelin rows in the table are pre-onset
   restorations or arms whose onset was never located.
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
5. **DATO** — Spontaneous seizure endpoints behave the opposite way: epileptic spasms fell with early
   restoration and not with late (PMID 39855191), and the seizure phenotype was "refractory to postnatal
   Ube3a reactivation" (PMID 25866966). The one post-onset seizure success is a pathway drug whose benefit
   "reversed after stopping the drug" (PMID 18389497).
6. **DATO** — Behaviour splits by domain *inside single studies*: social and repetitive behaviours recovered
   in adulthood while anxiety and motor coordination did not (PMID 26886798), and working memory resisted
   restoration at every age and in both sexes across two independent alleles (PMID 39855191).
7. **DATO** — Restoring the gene too abruptly killed animals in two independent models (PMID 17289941,
   PMID 34651584); three rows in the table carry `outcome = worse`.
8. **INFERENZA** — What decides the difference is not the endpoint's tissue level but whether the endpoint is
   *maintained by ongoing gene function* or was *built once during development*. The Angelman pair is the
   clean case: same gene, same restoration ages, plasticity open and behaviour shut.
9. **INFERENZA** — For the reference genotype class the honest external expectation is that a post-onset arm
   could move network and cellular readouts, would probably not move the myelin endpoint, and is **untested**
   on myelin in every precedent found. "Probably not" here is an expectation from adjacent genes, not a result.
10. **IPOTESI** — The `INV-01` added arm should therefore be worded per endpoint class, and the quantified
    myelin endpoint should be treated as the *discriminating* measurement rather than the confirmatory one.
    The test that separates the two readings: whether quantified myelin moves while spike-wave rate does.

### How the status vocabulary was applied

The closed set (`PREVENTED`, `RECOVERED`, `EARLY-WINDOW`, `UNMEASURED`, `UNVERIFIED`) has no value for an arm
that *was* given after a manifested phenotype, *was* measured, and did *not* move. `UNMEASURED` would be
false, because it was measured. So in `evidence_r1.tsv` **`status_vocab` carries the timing class of the arm**
(`RECOVERED` = restoration followed a manifested phenotype) and **`outcome` alone carries the result**
(`full`, `partial`, `none`, `worse`). A `RECOVERED` row with `outcome = none` therefore means "tested after
onset and did not move", which is the single most informative row type for this challenge. This reading is
flagged rather than silent because it differs from the wording in
`rescue_window_it6_20261029.md`, where `RECOVERED` embeds the movement.

---

## Matrix: endpoint class by restoration timing

Counts are `studies | rows` from `evidence_r1.tsv`. **This is not a meta-analysis.** The models differ in gene,
lesion class, lifespan and assay; nothing here is pooled, averaged or weighted. Publication bias runs one way
throughout: a restoration study that moved nothing is much less likely to exist as a paper, so the `none` and
`worse` cells are almost certainly under-counted relative to the `full` cells, and the strongest `none` rows in
this table are the ones reported *inside* otherwise positive papers.

| Endpoint class | pre_onset | post_onset_early | post_onset_advanced | adult | not_stated |
|---|---|---|---|---|---|
| survival | 1 \| 2 | 1 \| 1 | 2 \| 3 | - | 2 \| 2 |
| seizure_or_network | - | 3 \| 3 | 3 \| 4 | 3 \| 5 | - |
| motor | 1 \| 1 | 2 \| 2 | 1 \| 1 | 2 \| 2 | - |
| cognition_behaviour | 4 \| 4 | 6 \| 11 | 2 \| 2 | 5 \| 7 | 3 \| 4 |
| neuronal_structure | - | 2 \| 3 | 2 \| 4 | 1 \| 1 | 3 \| 3 |
| myelin_glia | 2 \| 4 | - | 1 \| 1 | - | 2 \| 3 |
| systemic_metabolic | - | 1 \| 1 | 1 \| 1 | 1 \| 1 | - |

### The same rows restricted to post-onset arms, by outcome

| Endpoint class | full | partial | none | worse |
|---|---|---|---|---|
| survival | - | 2 \| 2 | - | 2 \| 2 |
| seizure_or_network | 5 \| 7 | 2 \| 2 | 2 \| 3 | - |
| motor | 1 \| 1 | 2 \| 2 | 2 \| 2 | - |
| cognition_behaviour | 6 \| 6 | 5 \| 6 | 6 \| 8 | - |
| neuronal_structure | 1 \| 1 | 3 \| 4 | 2 \| 2 | - |
| **myelin_glia** | **-** | **-** | **-** | **-** |
| systemic_metabolic | - | 3 \| 3 | - | - |

The empty myelin row is the finding, not a gap in my search: it survived three targeted searches (`Q12`, `Q16`,
`Q18` in `queries.tsv`). The one myelin endpoint that moved under treatment (PMID 18495876) sits in an arm
begun between postnatal days 7 and 9, inside primary myelination, with no stated onset — `EARLY-WINDOW`, not
recovery. **Interneuron number is `UNMEASURED` in every source found** (`Q16`, 20 titles reviewed, no study
restoring a single gene after onset and counting interneurons).

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

**Myelin and glia.** Every myelin row is a prevention or an unlocated-onset row. The nearest analogue to the
module's own question is the inverse experiment: restoring Mecp2 *only* in the oligodendrocyte lineage left
one myelin protein at about 60 per cent of control and another "remained aberrant", with the authors
attributing the residue to a non-cell-autonomous effect of other cell types (PMID 24285883). At abstract level,
raising a different protein in a Tcf4 model rescued a learning endpoint while "OL gene expression and molecular
phenotypes ... are unchanged" (PMID 41997465) — behaviour moving while myelin does not, in the same animals.
Astrogliosis was *prevented* by early pathway inhibition and only partly reduced by the same drug given after
seizure onset (PMID 18389497).

**Seizures.** The seizure endpoint is where prevention and recovery separate most sharply. Early restoration
reduced epileptic spasms and late restoration did not, in two independent alleles with two Cre drivers
(PMID 39855191); the authors' own summary is that the seizure occurrence "appears to be preventable upon early
re-expression ... but becomes limited if expressed after seizure onset". Postnatal Ube3a restoration left
seizures in place (PMID 25866966). The successes are of two weaker kinds: provoked thresholds and interictal
measures after genetic restoration (PMID 31025938, PMID 22500629), and a pathway drug started after onset whose
effect did not outlast it (PMID 18389497).

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
(PMID 34651584) while the two-allele study narrows that to specific domains (PMID 39855191).

---

## Counter-evidence (30 rows, `role = counter`)

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
- **Contradicts a seizure expectation:** the two cleanest seizure endpoints in the set were preventable and
  not recoverable. Since the module's single carried WWOX endpoint is spike-wave discharge rate, this is the
  prediction most at risk.
- **Does not address myelin at all.** The expected return in the brief's consequence table — "structural or
  myelin endpoints rarely recover after onset while circuit or behaviour endpoints partly do" — is **half
  right and half unsupported**. Circuit and behaviour endpoints do partly recover. Structural endpoints at the
  *cellular* level recover better than the brief anticipated; at the *tissue* level they do not. Myelin is not
  rarely recovered after onset: it has **never been tested** after onset in this literature.

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
| Persistence | benefit outlasts the intervention | benefit requires continued treatment and reverses on withdrawal |
| Dose behaviour | restoration level is near physiological and its toxicity was checked | restoration is supraphysiological or abrupt, where two models show lethality |

---

## What the added arm of `INV-01` must measure, given these precedents (IPOTESI)

1. **IPOTESI** — A pre-treatment measurement of every endpoint in the same animals, or in an age-matched
   cohort sacrificed at the injection day; without it the arm produces another `EARLY-WINDOW` row, not a
   recovery row, exactly as all nine existing WWOX rows do.
2. **IPOTESI** — An untreated same-genotype comparator measured at the *same age* as the treated animals;
   three precedent studies lose interpretability precisely here, and one says so itself.
3. **IPOTESI** — Quantified myelin (g-ratio or densitometry, not marker intensity) as the **discriminating**
   endpoint: it is the one class with no external precedent in either direction, so it is the only measurement
   whose result is not partly predictable before the run.
4. **IPOTESI** — Spike-wave discharge rate recorded *before* restoration in the same animals, because the two
   cleanest external seizure endpoints were preventable and not recoverable; a post-onset null here would be
   consistent with the precedents rather than a failure of the arm.
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

- Whether any myelin endpoint recovers after onset in any single-gene neurodevelopmental disorder model. Not
  established in either direction; the class is empty after three targeted searches.
- Whether interneuron number recovers after onset anywhere. Not found (`Q16`, bounded search, 20 titles).
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

- **Full text of five records**, by any route allowed for this task. PMID 19211884 (Pten, pathway inhibition)
  is `abstract_only`: its abstract separates "prevent and reverse" for a structural endpoint, which is exactly
  on question, but the treatment ages, the comparator and the stated onset are unread, so it carries a
  conditional lead and nothing more. PMID 41997465 has no PMC identifier at all and is `abstract_only`.
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
- **Two rows are `cited_in_source_not_read`** (`R17`, `R22`): a working-memory null and a contradicting
  spine-density result, both read through the citing paper only. Their primary sources were not opened.
- Methods and supplementary material were not read for most records; figures were not viewed for any. Every
  receipt's `coverage` states this per section, understated rather than overstated.

## Queries

All 30 are in `queries.tsv` with database, exact string, timestamp, hit count and what was done with each.
Routes used: the PubMed MCP tools, NCBI E-utilities (esearch, esummary, efetch), Europe PMC REST, and PMC
article pages. Zero spend, no registration, no account, no author contact, no contact address sent anywhere.
No third-party bytes were saved inside the repository; downloads stayed in the session scratch directory.
