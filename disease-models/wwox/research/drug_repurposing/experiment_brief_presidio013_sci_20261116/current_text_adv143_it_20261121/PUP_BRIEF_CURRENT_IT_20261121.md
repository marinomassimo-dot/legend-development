# Pup brief, current text: a first provoked-seizure experiment in the Wwox-null pup, to separate the readings of ethosuximide (E1 to E3; E4 no effect and E5 not interpretable are the other outcomes) and of lithium (L1 general, L2 GSK-3-specific)

<!-- STATUS-BOX -->
**STATUS: THIS TEXT GOVERNS. Version and date: 2026-11-21.**

- This is the one current text of this experiment brief. It replaces, for reading, the two older texts: the consolidated brief dated 2026-11-19 and the original brief dated 2026-11-18 with the dated lines appended to it (the last dated 2026-11-21).
- Where this text and an older text differ, this text is the one to follow. Where two older statements disagreed and one was later or more specific, this text follows that one, and the other is kept in the History.
- The older texts are kept unchanged in the repository. Every statement that this text supersedes is kept, word for word, in the section "History (old text kept)" at the end, with its date and the statement that replaced it. The History also names apart the two different things that the older texts both called "9.12": the dated correction of line 9.11, and the calcium add-on line of 2026-11-21. The body of this text does not use that number.
- Markers in the text. **OPEN-GAP** marks a question that cannot be answered by text work: a value or a decision is missing, no value has been invented, and the owner is named (SCI is the design team that wrote this brief; operator is the coordinator of this collaboration; laboratory is the collaborating laboratory). **CONFLICT-OPEN** marks a sentence where two statements of the older texts disagree and the design team has not decided between them; both statements stay in place. **[Clarification by text work, for SCI to confirm: ...]** marks a reading that this text supplies and the design team must confirm.
- Design-team notes. The bracketed notes "[Design-team answer ...; status: ...]" are the design team's answers of 2026-11-21 to the open questions of the earlier readings. The status after the semicolon says what a note is: computed from stated inputs; stated in a source text; confirmed or corrected; INFERENCE (a rule proposed by the design team, not a source value); or partly closed (the rest is a marked open item). A note is later and more specific than the sentence beside it: where they differ, follow the note; the sentence stays, and where both cannot hold a CONFLICT-OPEN marker says so.
- Apart from the design-team notes (each figure in a note carries the status that its note states), no number of the older texts was changed. Figures computed by the design team after the cold read (for example the doubled-vehicle total, the litter counts for wild-type supply, the inflation of the SD by one relative standard error, the pilot arithmetic) are labelled computed or inference where they stand; their derivations are in the design team's register of numeric tokens. Each number appears as in the older texts; where the older texts gave different figures for the same thing, both stay, each with its basis. Sections are named, not numbered, so that a reference cannot be confused with the numbering of the older texts.
- The contact route for questions to the design team and the terms of the collaboration are not named in this text: see "Logistics, terms and contact".
<!-- STATUS-BOX -->

Sections, in order: Scope and limits; The question; What this experiment cannot show; What is fixed here and what the laboratory decides; Animals; Stimulus, seizure grades and observation; Ages; Groups to run (stages and the assay-validation panel); Regimens and dose checks; Analysis plan; Sample size and animals needed; Welfare and stopping; What each outcome would favour; Optional add-ons; Optional, conditional cohort; Logistics, terms and contact; Sources and their levels; History (old text kept); Out of scope for this laboratory.

In this text "grade" always means a step of the 0 to 6 seizure scale, and "stage" always means a step of the experimental plan (stages 0 to 4). The design-team notes quote source papers that also say "stage" for a step of the seizure scale ("stage 6 is death"); in a note, a "stage" with a seizure meaning is a grade, and "stage units" are grade units. A reference in the body to a numbered line of an older text (for example "line 9.14") or to a set of the predictions file points to a text kept in the repository, not to a section of this one.

## Scope and limits

**Hypothesis level.** Written for a collaborating laboratory that reads this cold. Class labels; no agent is named as a use except as an illustrative reference; no dose; no schedule of our own (the only regimen mentioned is the one stated in Cheng 2020, as the replication condition); no recommendation for or against any use of any agent in any person. Reference genotype class only (a WWOX-related developmental and epileptic encephalopathy genotype class); no individual-level record was used or sought. Not medical advice. NOT a WWOX result: every statement about what an outcome would mean is a hypothesis to be tested. The laboratory chooses its doses, exposure times and stimulus within its own published standard assay and states them before data.

Ethosuximide and lithium are the two agents under test (they are the agents of the one published experiment that this design follows up). Every other agent name in this text is an example from the rodent literature and is not proposed for any use. (See also the second lithium regimen, under "Regimens and dose checks".)

Each statement is no stronger than its evidence level, which is given beside it or under "Sources and their levels" (full text read; abstract only; second-hand; read by eye from a figure; hypothesis).

Predictions for the outcome classes were fixed in a predictions file before the original brief was written. Its checksum is sha256 `326846fb5180a9355d4d462217bc83a97bf653054d24ae5dcd6344bde497122e`, and the file was not edited afterwards. Where this text is more specific than the predictions file (the definitions under "Stimulus, seizure grades and observation"), this text adds detail and the predictions file governs any conflict. The weights in it are subjective, not validated probabilities, and are scored literally when data exist. A different predictions file (sha256 `3c567acddf10244602c4536d3153f134cab4eba0690321290edd23772b7d8be0`) belongs to a different experiment (a brain-slice experiment) and is not used here.

**OPEN-GAP R2Q82 (owner operator): Does the laboratory receive the older texts, the operator note and the predictions file, and where are they kept?**

[Design-team answer Q06, 2026-11-21; status: partly closed. (a) Which definitions govern: the hashed priors file governs any conflict, the brief only adds detail. (b) Whether the laboratory receives the priors file at all is a send decision the brief leaves to the operator; no value is proposed.]

**OPEN-GAP Q06 (owner operator): send the hashed priors file with the brief, or keep it back until data exist? Note for the choice: the file holds our predictions written before data; it is meant to be scored literally afterwards.**

## The question

In Wwox-null pups, are the seizure-suppressing effects reported for ethosuximide and for lithium specific to the knockout, or are they the same proportional effect any anticonvulsant of that kind would have in a pup of that age, and does lithium act through GSK-3 (glycogen synthase kinase 3)?

**Why this question.** The only in vivo drug data in a Wwox-null animal that the design team holds are one experiment (Cheng 2020, PMID 32000863, global knockout, "preweaning" pups, pentylenetetrazol (PTZ)-provoked seizures scored 0 to 6, one laboratory): lithium lowered the seizure grade in all three genotypes; ethosuximide lowered it in the knockout and was not significant in wild-type and heterozygous pups. **No genotype-by-treatment test was reported or can be computed from the figures** (mean ± SEM curves, one-way ANOVA; no per-animal values; the test age is not stated; the knockout PTZ-alone curves of the two drug panels differ in height by eye, so different cohorts appear to have been used; wild-type grade is about 1 on 0 to 6, close to the floor, that is, so low that a reduction cannot be seen; "about 1" is an eye reading of the published curves, and the older texts do not say whether it is a peak value or a mean; it is not the 60-minute mean grade of the floor bracket used below (mean S 0.27 to 0.41 in grade units), which is a different quantity and is not to be compared with it). A claim of knockout selectivity rests on a difference in significance. By eye the proportional reduction by lithium looks similar in the three genotypes (an eye reading of the published image), which fits a general or regimen effect better than a knockout-enhanced one.



**Readings to separate for ethosuximide.**
- (E1) knockout-selective.
- (E2) age-limited: a small wild-type drug effect at the assay age while wild-type vehicle S is above the pilot-fixed floor, not a floor-bound arm (rat pups lose the PTZ effect of ethosuximide below about 25 days in abstracts from one Prague laboratory family; the mouse ontogeny was not found by two routes; one mouse pup datum exists for a different seizure type, Cortez 2004, PMID 15582027, abstract only).
- (E3) a general anticonvulsant effect, proportional in every genotype.
- (E4) no effect; (E5) not interpretable. These are the two other outcomes.

**OPEN-GAP Q81 (owner SCI): What exactly is outcome E5 ("not interpretable") and how does it differ from E4 ("no effect"), since E5 is named only in the title?**

**Readings to separate for lithium.** (L1) general, against (L2) specific to GSK-3 in the knockout. The inhibitory phosphorylation of GSK-3beta at serine 9 (p-Ser9) is lower in untreated knockout brain (Cheng 2020 Fig. 7c, one representative blot per region); lithium engagement was not measured; lithium has other targets.

**Sizing flag, read this first.** An eye reading of the knockout PTZ-alone curve of Cheng 2020 Fig. 7b, and a later quantification of Fig. 7b and 7d, show a between-animal variability of the full-hour summary that is large. At that variability a simple effect needs many animals per arm, and the genotype-by-treatment interaction is out of reach with that summary. The figures are in one table under "Sample size and animals needed". The brief plans a pilot first and promises no interaction test.

## What this experiment cannot show

**Cannot show:** whether any drug would help spontaneous seizures (spontaneous-seizure burden: there is no video-EEG in the basic design); whether a drug works after seizures start (acute rescue after seizure onset: all arms are pretreatment before a provoked seizure); how a drug works (any mechanism readout); development or survival effects; any statement about people. A provoked-seizure result in a pup says what a drug does to a PTZ seizure at that age, not what it would do to the null phenotype.

**Not attemptable as designed:** a test of "different between genotypes" on the full-hour area summary is **not attemptable** at the published variability, unless the pilot finds a far less variable stimulus or summary (for example the incidence of generalised seizures).

**What may not be ready:** whether any laboratory has the line and the capacity is unknown. Knockout pups are scarce and fragile: the held counts give 5.1 and 6.5 percent knockouts among pups genotyped at postnatal day 5 to 12 from heterozygote intercrosses (Cheng 2020, supplementary Methods; DERIVED about 0.4 to 0.5 per litter of 7) and 19.5 percent at day 3 in another null line (Ludes-Meyers 2009; Mendelian-compatible), not the one in four (25 percent) of Mendelian expectation that an earlier sizing assumed (see "Sample size and animals needed").

## What is fixed here and what the laboratory decides

**Fixed in this text (before the first animal):** all three genotypes in the same session at the same postnatal age; a vehicle group per genotype in every session; the allocation and blinding scheme; the outcomes per animal; the analysis plan and the order of hypotheses; the dose check per age; a written stopping rule for status; the order of stages.

**Decided by the laboratory and stated before data:**
- the assay age (the age at which knockout vehicle pups reliably show provoked seizures and can still be tested), and the ages of the wild-type series, spaced by the laboratory;
- the stimulus, within the laboratory's own published standard assay, and the observation window if it is not the 60-minute window;
- the doses and exposure times, the route, and any regimen other than the main lithium contrast;
- which agents serve as panel agents and as the comparator drug, and the laboratory's criterion for "selective" T-type and "different class" GSK-3 agents;
- the motor pre-test standard and the exclusion criterion;
- the humane endpoints, the rescue procedure and the ethics approvals, including whether stage 2 is possible at all;
- the permutation test or mixed model, where fewer than 10 litters are in a cell;
- whether it has or can obtain the global knockout line, and which optional arms and add-ons it takes.

Anything not in this list and not in the section concerned is either an OPEN-GAP (a value or decision nobody has made yet) or a CONFLICT-OPEN (two older statements disagree).

## Animals

- **Genotypes and crosses.** All three genotypes (+/+, +/-, -/-) are tested in the same session, at the same postnatal age. Pups come from heterozygote crosses (expected 1:2:1). Knockouts die by about 4 weeks and are fragile (the ages at which they die are in the table under "Ages").
- **Session and cells.** A session is one assay day at one assay age. A cell is one genotype-by-treatment (by age) combination. An arm is one treatment group: an agent, the vehicle, or a comparator. Cells are filled across litters, with litter as a block for the vehicle groups where numbers allow; a litter yields only about 7 pups, so all nine genotype-by-arm cells cannot come from the same litters.
- **Vehicle.** A vehicle group per genotype in every session (same-day control). Within a session the ethosuximide, T-type, lithium, second GSK-3 and comparator arms share one vehicle group per genotype (cheaper, and the interaction contrast is cleaner). The assay-validation panel shares the vehicle of its age.
- **Allocation.** Block randomisation of arm within genotype and litter is the general rule, scarcest genotype first (knockouts are allocated across arms in rotation before the others), with unequal cell sizes accepted and reported; n per cell is reported in cells, animals and litters. The sentence "litter as a block for the vehicle groups where numbers allow" is the vehicle-specific case of this rule, stated with its reason (cells are filled across litters because a litter yields few pups).
- **Blinding.** Drug syringes are coded by a person who does not score. Genotype is read before the test by a person who does not score (needed for the allocation above), and the scorer stays blind to genotype and arm. Every trial is video recorded and scored from the coded video by a scorer who was not present. Complete blinding to genotype may be impossible where knockout pups are visibly smaller; the brief then asks for blinding to arm, and the limit is stated in the report.

**OPEN-GAP R2Q81 (owner laboratory): Is scorer training or inter-scorer agreement required, and how many scorers are assumed?**
- **Cluster and sex.** Litter is recorded as a cluster. Sex is recorded; neither older text specifies balancing or stratifying by sex.

**OPEN-GAP R2Q16 (owner laboratory): Is sex balanced or stratified across arms, and are both sexes used?**
- **Heterozygotes.** Heterozygotes are in the vehicle and ethosuximide cells at the assay age and in "all genotypes" for lithium; they are not in the interaction ratio, which is knockout over wild type only (see "Analysis plan").

[Design-team answer Q42, 2026-11-21; status: source statements only; the value is the laboratory's or the operator's. Source statement: Cheng 2020 describes two knockout lines (exon 1 deleted; exons 2 to 4 deleted) and does not state in the seizure Methods or Fig. 7 legend which line the PTZ pups were. The brief does not require Cheng's line.]

**OPEN-GAP Q42 (owner laboratory): which Wwox-null allele and background strain do you hold, how is it maintained, and is it a global knockout (Cheng 2020 used global lines)?**

[Design-team answer Q43, 2026-11-21; status: source statements only; the value is the laboratory's or the operator's. Source statement: nothing on genotyping in Cheng 2020; the brief requires genotype read before the test by a person who does not score. Rule (INFERENCE): genotype must be known before allocation, since allocation is blocked within genotype; so tissue must be taken at least one turnaround time before the assay age.]

**OPEN-GAP Q43 (owner laboratory): at what age is tissue taken, what is the turnaround, and can the person who genotypes be separate from the scorer?**

**OPEN-GAP Q44 (owner laboratory): Who holds which code (genotype reader, syringe coder, injector), and may one person hold more than one?**

(see the design-team answer C25/Q45 above)

**OPEN-GAP Q46 (owner SCI): How are knockouts allocated within genotype and litter when a litter yields on average about 0.4 to 0.5 knockouts (Cheng 2020 frequency, DERIVED; 1.75 only if Mendelian)?**

**OPEN-GAP Q26 (owner SCI): Which nine genotype-by-arm cells are meant by "all nine genotype-by-arm cells"?**

**OPEN-GAP Q41 (owner laboratory): Which postnatal-day counting convention and which tolerance define "the same postnatal age" in a session, given that cells are filled across litters born on different days?**

**OPEN-GAP Q48 (owner SCI): Is each pup used once only, and are litters standardised or cross-fostered?**

## Stimulus, seizure grades and observation

**Stimulus.** A stimulus that gives wild-type pups a measurable non-floor response, fixed in a pilot (otherwise a wild-type null cannot be told from a floor). The stimulus is the laboratory's own published standard assay; no number is proposed. In the one published experiment the provoking agent was PTZ.

[Design-team answer Q12, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value; one input is the laboratory's. Rule (INFERENCE): the replication arms (ethosuximide and lithium) use PTZ given i.p. in one injection, because the replication condition is Cheng 2020. All other arms may use the laboratory's own published PTZ protocol provided the SAME stimulus is given to every genotype and arm of a session and gives wild-type pups a non-floor response. A different provoked-seizure assay is a different experiment, not a variant.]

**OPEN-GAP Q12 (owner laboratory): do you run PTZ-provoked seizures in pups as a published standard assay, by which route and schedule, and could you give the single i.p. injection used in Cheng 2020 for the replication arms?**

[Design-team answer QA3, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule (INFERENCE): the laboratory's own validated scale is allowed only with a written mapping to the Cheng 0 to 6 scale for stages 1 to 2, 3, 4 to 5 and 6, fixed before data, so S and the seizure-type categories can be computed and compared with Cheng 2020; otherwise S is not comparable with the replication.]

[Design-team answer QA2, 2026-11-21; status: source statements only; the value is the laboratory's or the operator's. Not in the brief or Cheng 2020. Reason it may matter: null pups show falling glucose by P14 and the brief offers a glucose series as an optional add-on. Rule (INFERENCE): record, do not set: time since last feeding or dam separation, body temperature and ambient temperature at the test, identically across arms within a session.]

**OPEN-GAP QA2 (owner laboratory): what is your standard for dam separation, feeding and warming of pups before and during the assay?**

**Seizure grades.**

| Grade or class | What the older texts say |
|---|---|
| 1 to 2 | minimal seizures; the behaviour of grades 0, 1 and 2 is not defined |
| 3 | unilateral forelimb clonus with myoclonic jerk: intermediate, its own category, reported and included in S |
| 4 without a tonic phase | bilateral clonus, reported on its own line |
| 5 | loss of righting, tonic-clonic; reported separately inside the generalised count |
| 4 to 5 with a tonic phase | generalised seizures, as the in vivo priors file defines "generalised" for its prediction P8 |
| 6 | a pup that dies keeps grade 6 for the rest of the window; whether grade 6 is death is not stated |
| status | three or more tonic-clonic seizures within the window (the Cheng 2020 definition) |

[Design-team answer Q18, 2026-11-21; status: stated in a source text. Source statement: the modified Racine scale of Cheng 2020 is printed in the Methods: stage 0 no response; 1 behavioural arrest then vibrissae twitching; 2 head nodding; 3 unilateral forelimb clonus with a myoclonic jerk; 4 bilateral forelimb clonus with rearing; 5 generalised tonic-clonic seizure with loss of righting; 6 dead. The brief's definitions are consistent with it; grade 6 IS death.]

[Design-team answer C011/Q84, 2026-11-21; status: stated in a source text. 'P5' and 'P8' are labels of predictions in the in vivo priors file (P5: the lithium interaction ratio lies between 0.7 and 1.43; P8: at least one test or panel agent raises minimal-seizure incidence by at least 1.3 times vehicle while lowering generalised-seizure incidence); they are not postnatal days. A separate earlier priors file has its own P5 (a different prediction, the d-APV class), so every use in this text says 'of the in vivo priors file'. Where the text named a numbered line of an older text or 'set P5', it now names the section or the prediction's own words.]

**OPEN-GAP Q52 (owner SCI): How are "three or more tonic-clonic seizures within the window" counted (what separates events, and is grade 5 the same as tonic-clonic), given that the status rule also triggers the rescue rule?**

**Outcomes per animal, not only a mean grade.**
- (a) **S** = area under the grade against time over a **60-minute window (as in Cheng 2020; any other window is stated before data)**, the grade assigned per 1-minute bin as the maximum grade in that bin; **a pup that dies keeps grade 6 for the rest of the window, and a pup rescued under the status stopping rule keeps its last grade carried forward to the end of the window; both are flagged, and the results are reported with and without them** (primary).
- (b) **Seizure type:** incidence and latency of minimal seizures (grades 1 to 2), **intermediate seizures (grade 3, its own category, reported and included in S)**, generalised seizures (**grades 4 to 5 with a tonic phase; grade 4 without a tonic phase is reported on its own line, and grade 5 is reported separately inside the generalised count**) and **status** (three or more tonic-clonic seizures within the window).

[Text repair 2026-11-21 conflict R2C05: a grade 4 counts as generalised only if a tonic phase is seen; a grade 4 without one does not count as generalised and has its own line; a grade 5 is a generalised tonic-clonic seizure in the printed scale of Cheng 2020 (see the note on the scale) and counts.]
- Reason: in rat pups several agents suppress generalised seizures while **raising minimal seizures** (MK-801 at P12, memantine, phenobarbital at P7 and P12, carbamazepine at P7 and P12), and wild-type pups sit at minimal-seizure level, so a mean grade can cancel two opposite effects.

[Design-team answer CLAR-S, 2026-11-21; status: confirmed by the design team. S is the area under the grade against time over the 60-minute window; the mean grade over 60 minutes is S divided by 60 for the same per-minute series. The floor bracket mean S 0.27 to 0.41 is in mean-grade units. The division cancels in every ratio R and in the CV, so no sizing figure changes; state the unit with every S value.]

**OPEN-GAP Q49 (owner SCI): In what units is S, and is the area, the sum or the mean grade the primary summary?**

**OPEN-GAP Q50 (owner SCI): In item (a) above, what is primary: S, or the reporting with and without deaths and rescued pups?**

[Design-team answer Q51, 2026-11-21; status: stated in a source text; the latency rule is an INFERENCE, to be fixed before data. Window start = the PTZ injection (time 0), not the pretreatment injections: Cheng 2020 scored seizure severity for 60 minutes following the PTZ injection (as in this text: 60-minute window, grade per 1-minute bin as the maximum in the bin). Latency rule (INFERENCE, to be fixed before data): the latency of a seizure type is the start of the first 1-minute bin, counted from the PTZ injection, whose grade reaches the lower bound of that type: minimal 1 to 2, intermediate 3, generalised 4 to 5 with a tonic phase, status = the bin of the third tonic-clonic seizure within the window, death = the bin in which grade 6 is first recorded. A pup that never reaches the type has no latency (censored at 60 minutes, analysed as a time-to-event with censoring).]

**OPEN-GAP S09 (owner laboratory): do you score per minute as the maximum grade in the bin, from the PTZ injection?**

[Design-team answer Q22, 2026-11-21; status: partly closed. Rule (INFERENCE): decide on pilot VEHICLE animals only, before any treated-arm data, in a dated note signed before stage 2. Switch the primary outcome from S to generalised-seizure incidence if the pilot SD of log S in the knockout vehicle group gives n per arm for ratio 0.7 above the number of knockouts the laboratory can supply: n per arm = 2 x 7.85 x sigma^2 / 0.1272 (two-sided 0.05, power 0.80). At the brief's binary example (fall from 50 to 10 percent) about 20 per arm. Who decides: the design team with the laboratory, in writing, before stage 2; the brief already says S is primary unless the pilot finds a far less variable summary.]

**OPEN-GAP Q22 (owner laboratory): how many knockout pups per genotype-by-arm cell can you realistically supply in one session and in total?**

**Motor and ataxia pre-test.** A motor and ataxia control (the laboratory's own standard: righting, gait or equivalent) is applied to every arm as a pre-test before the provoked seizure and reported per animal as a covariate; **it is mandatory for ketamine-class and other NMDA-receptor and sedating agents** (ketamine causes ataxia at the lowest exposure in rat pups, more in younger ones, abstract level, which would confound a grade score). A pup is excluded only if it fails the laboratory's own pre-specified criterion before the stimulus (stated before data), and exclusions are listed.

**OPEN-GAP Q53 (owner laboratory): When is the pre-test done relative to the drug and the stimulus, what cut-off excludes a pup, and are excluded pups replaced?**

**OPEN-GAP Q64 (owner laboratory): Which pups, apart from the motor pre-test, are excluded for illness or failure to thrive before the test?**

## Ages

**Documented ages in the sources read** (the laboratory confirms from its own colony):

| Age | What | Line and source |
|---|---|---|
| not stated | the age at which Cheng 2020 tested; only "preweaning" is given (spontaneous seizures were commonly seen after P12; the null dies by about four weeks) | germline null; Cheng 2020 |
| commonly after P12 | behavioural spontaneous seizures; no EEG | germline null; Cheng 2020 |
| from about P14 | cortical ECoG (electrocorticography) interictal-like spikes and generalised spike-wave discharges in null pups; n = 5 per group; nothing was recorded earlier, so onset may be earlier | germline null; a 2026 report |
| P13 to P17 | slice bursting (a brain-slice finding, not an in vivo seizure) | Breton 2021 |
| from P9 | the neuron-targeted line (called S-KO in the sources) seizes; a different line from the germline null, whose onset is after P12 to about P14; the source of this age is the dated add-on line of 2026-11-21 | neuron-targeted line |
| at about three to four weeks | death | knockouts in general ("knockouts die by about 4 weeks") |
| by about day 17 | death of untreated knockouts, stated "in the comparator's panel" (the AAV9 comparator's panel) | knockouts in that panel |

No EEG before P14 exists in the sources read. Any assay age beyond those documented is the laboratory's to decide.

**OPEN-GAP T55 (owner SCI): The full citations for the 2026 report, the report called "P47T" and the Prague abstracts are not given in the older texts; Breton 2021 and Kasahara 2019 also have no PMID there.**

**Assay age.** Defined by the laboratory (Cheng 2020 does not state it) as the age at which knockout vehicle pups reliably show provoked seizures and can still be tested.

[Design-team answer Q37, 2026-11-21; status: partly closed. The two death statements do not conflict: 'by about 4 weeks' is Cheng 2020 (two knockout lines survived less than a month; Results); 'about day 17' is the AAV9 comparator panel's untreated knockouts. Documented ages: spontaneous seizures after P12 (Cheng 2020), ECoG spikes from about P14, slice bursting P13 to P17, death at 3 to 4 weeks. Working window (INFERENCE from those documented ages): provoked-seizure testing at P12 to P17; P11 only as the chloride-window probe. The brief leaves the assay age to the laboratory.]

**Wild-type age series** (no null animal needed): wild-type pups, same stimulus and scale, at the assay age and at **at least two older ages up to about P28**, spaced by the laboratory, vehicle against each test agent; knockouts are tested at the assay age only (they cannot be matched at older ages). Purpose: to see whether a wild-type non-response is age. Which ages the series contains is fixed by this rule (the assay age and at least two older ages). A series that also straddles P11 and P14 is required only if the chloride-window read is wanted; when the assay age is P14 or later that read needs P11 as one further age (seven more wild-type cells); otherwise the series is as defined and no further age is added.

[Design-team answer C002/CLAR-SERIES, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. The wild-type series is the assay age plus at least two older ages inside the window to about P28. A series that also straddles P11 and P14 is required only if the chloride-window read is wanted; when the assay age is P14 or later that read needs P11 as one further age (seven more wild-type cells); otherwise the series is as defined and no further age is added. This note replaces the earlier note on the series: it describes the optional straddle, not a further requirement for the primary contrast.]

**OPEN-GAP S01 (owner laboratory): is the P11 versus P14 chloride-window read wanted, which sets whether a fourth age is needed?**

**OPEN-GAP CLAR-SERIES (owner laboratory): assay age**

[Design-team answer Q39, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule (INFERENCE): the series is the assay age plus at least two older ages up to about P28; when the assay age is P11, P14 is one of the older ages, which covers 'straddling P11 and P14' with a third age at P17 or later; when the assay age is P14, P11 is NOT an older age and is added as a fourth age (7 more cells). The brief's 21 wild-type cells assume 3 ages.]

[Design-team answer Q21, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value; one input is the laboratory's. Rule (INFERENCE): the same stimulus at every age of the wild-type series, because the series is meant to show whether a wild-type non-response is age; the pilot therefore must include wild-type vehicle pups at the older ages too (cheap: no knockout needed) so that the stimulus is fixed knowing the older-age response. Re-fixing the stimulus per age would turn age and stimulus into one variable; if an older age is at the floor or ceiling the series records it and a second stimulus level is an extra cell, not a replacement.]

**OPEN-GAP Q21 (owner laboratory): does the same stimulus remain tolerable and informative at the older ages of the series?**

**Timing limit: state the age and the structural state beside every effect.** In the germline null report, of the structural findings those at E12.5 (smaller embryo, elongated roof plate), E16.5 (fewer Ki-67-positive cells in the subventricular zone, thinner cortex) and birth (more BrdU-positive cells throughout the neocortex, more Ki-67-positive cells in the proliferative zones) **precede the seizures** the paper describes as "commonly observed after postnatal day 12" (no onset age is given; the gross brain abnormalities reported "from live births" have no stated age and are not placed in this order).  The doublecortin increase is at P14 (n = 5), brain-size and weight reduction at P20, and the apoptosis ratio (about five times control) and the cerebellar vermis fusion are at about P19 to P20 (one reading of the source, not re-checked), so these are concurrent with or after seizure onset. The paper proposes, without testing it, a chain from aberrant neuronal migration through reorganised networks to hyperexcitability (Discussion: the aberrant positioning of neurons "may cause reorganization of neuronal networks and alteration of cellular physiology that create hyperexcitable tissue"), and tests neither its order in time nor the link; "brain-wide" is not its word. A preventive or early arm cannot be read as a reversal in respect of the findings that precede seizure onset (E12.5, E16.5 and birth).

**State the chosen age against the chloride-gradient window** (the developmental period over which the neuronal chloride gradient matures; E_GABA is the GABA reversal potential). No Wwox system has a measured E_GABA. The one mouse study that suggested a P11 to P14 window (Kasahara 2019, full text read, groups of 4 to 5) is confounded: clonic incidence at P11 was not raised (5 of 5 in saline); the worsening is in latency, threshold temperature and LFP (local field potential) events; bumetanide (a blocker of the chloride importer NKCC1) did not block the latency effect and alone lowered incidence; there were 5 of 5 deaths on high-dose diazepam at both ages; and body temperature was near normal in the co-treatment arms. No other source supports a P11 to P14 chloride window (slice and in vivo data put the switch earlier, with region caveats). An NKCC1-blocker arm is **not** proposed (no brain-engagement control, narrow pup age effect, ototoxicity and diuresis signals in neonatal trials).

**The one mouse datum, febrile-seizure induction worsened at P11 and not at P14, does not show a direction change**, because its source is the confounded study above. A direction change between P11 and P14 is a rat-level possibility, not a mouse finding, and the age series is the more needed for that reason. An earlier line that an agent can change direction between P11 and P14 in the mouse is withdrawn here; whether the withdrawal follows from the later chloride-window line is an inference of the design team, not a statement of the original line. The panel names no benzodiazepine. Diazepam is age-dependent in rat pups (status epilepticus not stopped at P9, stopped at P15 and P21; abstract level).

**For any chloride-transport arm added** (none is proposed): a wild-type-on-agent group (a bumetanide effect on seizure latency was the same in wild type and mutant in one model); assignment by animal within litter, or analysis by litter (litter-level randomisation analysed per animal was a confound in the one genetic-DEE pup dataset); benzodiazepine tests timed from the onset of status, not from the convulsant; a sedation measure; and developmental endpoints kept separate from timing endpoints (a shift of a self-resolving phenotype is not a change in development).

**OPEN-GAP T72 (owner SCI): Which dataset is "the one genetic-DEE pup dataset"?**

## Groups to run (stages and the assay-validation panel)

**Stages (each has a stop rule).**

| Stage | What | Why this order | Stop or branch |
|---|---|---|---|
| 0 (not in vivo) | the brain-slice experiment (a separate experiment and a separate package, with its own predictions and no shared animals) | needs no animal harm assessment; independent of this assay | runs first or in parallel for stages 1 to 3; **stage 4 does not start before it has run**; otherwise this text does not depend on its result |
| 1 pilot | knockout and wild-type vehicle pups and wild-type pups given the flat-profile panel agent at one exposure, at candidate assay ages; stimulus and window fixed; within-genotype variability of S estimated **on the scale of the primary analysis (ratio of means with a bootstrap over litters; report the CV of S (coefficient of variation) and the SD of log S among animals with S above zero, since log S is undefined at S = 0)** (6 to 8 per cell for the pilot is of the order of the Cheng knockout groups (6 to 7)) | fixes the assay age, the non-floor stimulus and the sample size | stop if knockout vehicle pups cannot be tested at a wild-type response that is not at the floor, or if the panel agent has no effect at any age |
| 2 ethosuximide (the arm whose outcome decides between the three readings of ethosuximide: selective, age-limited or general) | ethosuximide against vehicle in all genotypes **with the wild-type age series and the panel** | the only arm whose outcome decides between selective, age-limited and general | if the panel is not valid at the assay age, move the assay age, do not read the null |
| 2, optional | a selective Cav3 (T-type calcium channel) blocker arm beside ethosuximide (class label; it asks whether a T-type route is the reason; "selective" = the laboratory states its criterion, at least published selectivity for Cav3 over other voltage-gated calcium, sodium and potassium channels at the exposure used and published rodent brain exposure; illustrative examples from the abstract-level literature: TTA-A2, Z944; no evidence that the drug reaches and acts on its target in the pup brain (an engagement control) exists in pups and no rodent pup datum for the selective blockers was found, so a null is not interpretable unless the laboratory adds one) | the only way to ask whether a T-type route is the reason | none |
| 3 lithium (optional) | lithium against vehicle in all genotypes **in the same session**, with the lithium-alone arm (see "Regimens and dose checks"), **one second GSK-3 inhibitor of a different class** (chemically unrelated to lithium, published selective GSK-3 inhibition at the exposure used and published rodent brain exposure; illustrative examples: SB216763, CHIR99021, TCS2002) and **one general non-GSK-3 anticonvulsant comparator drug** effective across ages (valproate in the rat literature) | separates "GSK-3 route" from "general property"; lithium alone cannot (it also acts on other targets); **the second GSK-3 inhibitor of another class becomes more necessary, not less** | none |
| 4 last (optional) | the NMDA-receptor pore-blocker arm (class label; channel-blocking antagonists such as ketamine and MK-801), **only with harms and stopping rules written first** (provoked-seizure aggravation, ataxia, status) and its predictions written then | aggravation is the class's best-documented harm; the slice arm should come first | predictions not fixed here |

**OPEN-GAP R2Q43 (owner SCI): For stage 3, in the same session as what, and at the assay age only or across the whole age series?**

[Design-team answer C09, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. The pilot carries, at each of its two ages, knockout vehicle, wild-type vehicle and the wild-type flat-profile panel agent at ONE exposure (n 6 to 8 per cell; 36 to 48 animals, as already counted). The stage 1 row lists the panel cell, so its stop rule ("the panel agent has no effect at any age") can be read in stage 1. The dose check ("if the lower exposure is effective in the panel agent at an age") belongs to stage 2, where the panel agents are already run at two exposures; an age left unresolved in stage 1 is handled by the rule for an unresolved panel age (re-read at the second exposure in stage 2). Not adopted: vehicle pups only (it would move the pilot's stop rule out of stage 1) and the panel agent at two exposures in the pilot (it adds wild-type cells beyond the pilot note's count).]

[Design-team answer Q19, 2026-11-21; status: partly closed. Inconsistency in the brief: the pilot row lists vehicle pups only, while its stop rule refers to the panel agent. Rule (INFERENCE): the pilot includes the flat-profile panel agent in wild-type pups at each candidate age (otherwise the stop rule cannot fire) and the pilot's candidate assay ages are two ages chosen by the laboratory inside the working window P12 to P17 (one near each end, from its colony's survival and the age at which knockout vehicle pups reliably seize); P11 and P14 are named in the brief only as chloride-window ages and enter the wild-type series only if that read is wanted; they are not the pilot assay ages. The pilot arithmetic (2 ages, 6 to 8 per cell) is unchanged. The window itself is an inference from documented ages: spontaneous seizures after P12 (Cheng 2020), ECoG spikes from about P14, slice bursting P13 to P17, death at about three to four weeks; the laboratory confirms from its colony. (This corrects the earlier answer, which took the pilot ages to be P11 and P14.)]

**OPEN-GAP S03 (owner laboratory): which two ages inside P12 to P17 can your knockout pups reach with at least a stated fraction alive and seizing under your standard stimulus?**

**OPEN-GAP Q19 (owner laboratory): up to what postnatal day can knockout pups in your colony be tested with a provoked-seizure assay without losing more than a stated fraction before the test?**

[Design-team answer Q20, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule (INFERENCE): 'wild-type response that is not at the floor' = under ONE stimulus given identically to both genotypes, wild-type vehicle pups are not at the floor by the floor rule (Q68) and the wild-type and knockout vehicle S distributions overlap at the stage level. The stimulus may NOT differ by genotype for a comparison that feeds the interaction ratio (two stimuli would confound the ratio). If no single stimulus meets both conditions, that is the pilot's stop rule firing.]

[Design-team answer Q34, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule (INFERENCE): pilot = 2 ages x [knockout vehicle; wild-type vehicle; wild-type flat-profile agent at one exposure], n 6 to 8 per cell. That is 36 to 48 animals; knockouts 12 to 16 (7 to 9 litters at the assumed 1.75 per litter, rounded to the nearest litter; 27 to 45 litters at the Cheng 2020 knockout frequency of 5.1 to 6.5 percent, DERIVED at 7 pups per litter, rounded up: 34 to 45 at 5.1 and 27 to 36 at 6.5); wild-type 24 to 32 taken from the same heterozygote crosses would need 14 to 18 litters at 1.75 per litter, nearest (the wild-type frequency is not reported), so, if wild types are at least about 13 percent of the pups (the pilot needs twice as many wild types as knockouts, so twice the 6.5 percent knockout frequency; 10.2 percent suffices at 5.1 percent), the pilot size in litters at the Cheng frequency is set by the knockout need and the same litters would supply the wild types; at the Mendelian 25 percent the 27 to 45 knockout litters would give about 47 to 79 wild types against the 24 to 32 needed, and below those thresholds the wild-type need would set the litter count (Q45). Adding older ages for the wild-type series (Q21) adds wild-type vehicle cells only.]

[Design-team answer Q23, 2026-11-21; status: stated in a source text. Restated from the brief's own arithmetic, no new value: 27 cells = wild-type age series 3 ages x [vehicle; ethosuximide at 2 exposures; flat-profile panel agent at 2 exposures; rising-profile panel agent at 2 exposures] = 3 x 7 = 21 cells, plus knockout and heterozygote at the assay age x [vehicle; ethosuximide at 2 exposures] = 2 x 3 = 6 cells. NOT in the 27: lithium and lithium-alone, the second GSK-3 inhibitor, the general comparator, the T-type blocker (optional or stage 3), the falling-profile agent, any older-age knockout or heterozygote cell. Wild-type cells at the assay age sit inside the 21.]

**OPEN-GAP Q25 (owner SCI): Does the lithium-alone arm receive PTZ, in which genotypes, and is it counted among the arms that share a vehicle group?**

**OPEN-GAP Q27 (owner operator): Is the brain-slice experiment of stage 0 to be run by this laboratory, by another laboratory or by nobody, given that stage 4 is gated on it?**

**OPEN-GAP Q30 (owner SCI): Is "vehicle" vehicle plus PTZ only, or is a no-PTZ control (vehicle only, no provocation) also needed?**

**Order if resources are limited.** If resources allow only one step: the pilot (stage 1), then the ethosuximide arm with the age series and panel (stage 2). **Required:** stages 1 and 2 with the panel and the age series. **Optional:** the T-type arm (it needs an engagement control to be readable), stage 3, stage 4, and the add-ons. The laboratory costs the number of arms, agents and ages from these lists; the animal counts are illustrative until the pilot gives the SD. [Design-team answer CLAR-ORDER, 2026-11-21; status: confirmed by the design team. The stage order (pilot, then ethosuximide with age series and panel; required: stages 1 and 2) is the order for the provoked-seizure design; the one-slot order of the optional measurements (add-on (i)) applies to the add-ons only.]

**OPEN-GAP Q35 (owner SCI): If the laboratory can obtain only a fixed number of knockouts, what is the smallest stage 2 that remains informative?**

**Assay-validation panel** (called "the panel"). Separate wild-type pups at every age, sharing that age's vehicle group, so that a null is read only at an age where the assay can show a drug effect. The valproate effect in mouse pups is unknown, so the panel's validity is established empirically at each age, and **a failed panel is reported as an assay failure, not as a negative**. The panel has: a **flat-profile** agent (an agent whose efficacy does not change with age in the cited literature: valproate protects against PTZ at every rat age tested; mouse unknown, so it is itself a check); one **rising-profile** agent (efficacy rising with age in rat PTZ abstracts: carbamazepine, or cannabidiol); and, if an NMDA-receptor arm is included, one **falling-profile** agent (efficacy falling with age: ifenprodil or Ro 25-6981; ifenprodil effective in mouse at P7 and P10 and not at P14 or P21, in rat up to P18 on one assay and proconvulsant on afterdischarges at P18 and P25; Ro 25-6981 effective at P12 and failing at P25 in rat). **All agent names are examples from the rodent literature only, not proposed for any use; the laboratory chooses** (abstract level; one laboratory family is the origin of many rat rows).

[Design-team answer Q67, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule: the panel is valid at an age if (i) vehicle S in that age's wild-type group is not at the floor (Q68) and (ii) the flat-profile agent gives R at most 0.7 with a bootstrap interval over litters excluding 1; a panel that fails is an assay failure, not a negative. The sample size at which the interval can exclude 1 depends on sigma (Q31); with n of 6 to 8 only a large effect is detectable. Null and unresolved bands are the brief's own: a null = interval inside 0.85 to 1.15; otherwise unresolved; an age is declared invalid when the flat-profile agent gives a null, unresolved otherwise.]

[Design-team answer R3C10, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. An unresolved panel age (the flat-profile agent gives neither a null band, 0.85 to 1.15, nor an effect, R at most 0.7 with an interval excluding 1) is 'validity-indeterminate', not an assay failure: the priors make only the reading of a NULL conditional on panel validity ('a null for any test arm is read only when the panel is valid at that age'), so at such an age an observed test-arm effect is reported and every test-arm null is reported as unresolved. One extension is declared before any treated arm is unblinded: the age is re-read at the second exposure of the dose check that the design already carries (or the panel's wild-type cell is enlarged once). If it is still indeterminate, the age is dropped from the null-bearing part of the design and the assay age is moved for any null reading (do not read the null). The stage 1 stop rule fires only on a demonstrated no-effect (an interval inside 0.85 to 1.15) at every age, not on indeterminacy. A failed panel (demonstrated no effect) keeps its own rule.]

**OPEN-GAP S13 (owner laboratory): can you enlarge the panel cell once at an age within the same session?**

## Regimens and dose checks

- **Main lithium contrast.** One regimen is the main lithium contrast: the Cheng 2020 repeated pretreatment (three injections within one hour before a low-dose PTZ challenge), as the replication condition. The laboratory states any other regimen before data.
- **Source evidence on regimen.** No regimen in the sources shows a clear sign flip against PTZ (the one acute pro-convulsant abstract is from one laboratory family, with interval and method unreadable and the full text closed). The pro-convulsant abstract is the same one: in that report (PMID 29102713, abstract level, male mice by its record) the acute arm was pro-convulsive and the chronic arm raised the threshold; the interval and the PTZ method of the acute arm are not stated and the full text is closed, which is why it is not counted as a clear sign flip.



- **Optional second regimen.** A second regimen is an optional comparator arm (a single injection, PTZ about 30 minutes later: the schedule of one published mouse report, PMID 31238129, read at abstract level, not a schedule of our own), not a design variable of the main contrast.



- **Lithium-alone arm.** A lithium-alone arm is added, with a sedation, righting-reflex and weight readout at the PTZ time and the recorded interval from the last injection to PTZ (Cheng's panel has no lithium-alone arm and states no sedation, weight or interval; a low grade cannot tell protection from reduced behavioural output).
- **Second GSK-3 inhibitor.** The second GSK-3 inhibitor of another class becomes more necessary, not less.
- **Dose check per age.** Because potency shifts with age and **no pup exposure measurement was found for any agent**, "an effect of the drug" is defined only together with a **dose check per age: two exposures per agent (or a published pup exposure) at each age of the series, or a measured exposure if the laboratory has the means (not required)**. A non-effect at an exposure that was not checked at that age is a **dose null, reported as unresolved**, not as no effect.

[Design-team answer Q13, 2026-11-21; status: partly closed. Dose and route of PTZ used by Cheng 2020 are printed in the full text (Methods paragraph on seizure induction; repeated in the Fig. 7b legend). It is one single PTZ dose given to all three genotypes (the Results call it 'a low dose of PTZ'). The injected volume is NOT printed (only 'dissolved in 0.9% sodium chloride'). The brief deliberately does not copy numbers (no-dose perimeter); the text should point to the Cheng 2020 Methods instead of copying them.]

**OPEN-GAP Q13 (owner laboratory): what volume per body weight and what vehicle do you use for the PTZ injection?**

[Design-team answer QA1, 2026-11-21; status: partly closed. Lithium salt, vehicle and route: stated in Cheng 2020 (lithium chloride i.p. in 0.9% sodium chloride, three injections within one hour before PTZ). Spacing within the hour is not printed. Rule (INFERENCE): equal spacing, recorded interval from the last injection to PTZ.]

**OPEN-GAP QA1 (owner laboratory): what spacing do you use for the three injections within the hour?**

[Design-team answer Q14, 2026-11-21; status: partly closed. Source fact: Cheng 2020 printed the ethosuximide dose, route (i.p.), a single injection and the interval before PTZ (Methods). Rule: the Cheng regimen is the replication condition and the main ethosuximide contrast; the brief's dose check then adds ONE further exposure per agent per age; that second value is not derivable from documented numbers.]

**OPEN-GAP Q14 (owner laboratory): what second exposure of ethosuximide would you add per age, and do you have a published or measured pup exposure for either?**

[Design-team answer Q15, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value; one input is the laboratory's. Rule (INFERENCE, double-dummy): every pup in a session gets the same number, volume and timing of injections, with the agent present or replaced by saline. The replication condition is the regimen printed in the Methods of Cheng 2020 (agent, route, interval and number of injections are read there; this text copies none of its doses); only its differing schedules matter here: the two agents are given on different schedules, so a single vehicle group is valid only if it receives the SAME schedule as the arm with the most injections and every other arm receives saline for the injections it does not need. Without that, an earlier statement ('one vehicle group per genotype shared by all arms') cannot hold for arms with different schedules.]

**OPEN-GAP Q15 (owner laboratory): can every pup receive the same number of injections (drug or saline) so that one vehicle group serves all arms?**

**OPEN-GAP Q16 (owner SCI): What does "two exposures per agent" mean (two doses, two pretreatment intervals or two measured levels), and how are the two chosen when no pup exposure measurement exists?**

**OPEN-GAP Q17 (owner SCI): Is the interval from the last pretreatment injection to PTZ recorded for all arms, or for the lithium-alone arm only?**

## Analysis plan

Fixed before data.
- **Effect ratio.** R(genotype) = mean S of the treated group over mean S of the same-genotype, same-session vehicle group, on the log scale. The **interaction ratio = R(-/-) over R(+/+)**. The animal is the unit; litter is the cluster (bootstrap over litters).
- **Thresholds** (one table):

| Quantity | Rule |
|---|---|
| an effect | R at most 0.7 with an interval excluding 1 |
| a null | an interval inside 0.85 to 1.15 |
| unresolved | otherwise; an interval that contains 1 and excludes 0.7 is reported as "an effect of 0.7 or larger is excluded" |
| genotype specificity (interaction ratio) | at most 0.7 or at least 1.43 |
| no genotype specificity (interaction ratio) | above 0.7 and below 1.43 (the open band of prediction P5 of the in vivo priors file) |

[Design-team answer R2C01, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. The endpoints belong to the genotype-specific class, as the frozen priors file already has them (an effect is a ratio at most 0.7; E1 "at most 0.7"; E3 is rejected if the interaction ratio is "at most 0.7 or at least 1.43"). The no-specificity band of prediction P5 is therefore the open interval: an interaction ratio above 0.7 and below 1.43. Wherever this text restated the complement of that band as "outside 0.7 to 1.43", it now says "at most 0.7 or at least 1.43". No number changes; only the classification of a ratio of exactly 0.7 or 1.43 is fixed.]

**OPEN-GAP D05a (owner SCI): Is 1.43 kept as the upper edge of the no-specificity band although it is the rounded reciprocal of 0.7 (1/0.7 = 1.4286), so that a ratio between 1.4286 and 1.43 sits in the band while its reciprocal is below 0.7? Owner: the design team with the laboratory, before data, as a pre-registration amendment. Options: (1) keep the frozen band as it is; (2) amend before data to the exact reciprocal. The frozen priors file is not edited.**

**OPEN-GAP D05b (owner SCI): Are the interaction thresholds (P5 and the classes E1 and E3) scored on the point ratio or on its interval? The frozen priors file is silent. Owner: the design team with the laboratory, before data, as a pre-registration amendment. Options: (1) class by the point ratio, with the point ratio and its interval both reported; (2) class by the interval (the class holds only if the whole interval lies in it). No deviation from the frozen file is adopted here.**

- **Floor rule.** If vehicle S in a genotype is zero or at the floor, R is not computed and the arm is not interpretable.
- **A null is hard to reach.** A "null" interval is hard to reach at these sample sizes, which is why "unresolved" and "an effect of 0.7 or larger is excluded" exist.
- **Interval method.** With few knockouts per litter (1.75 if Mendelian; about 0.4 to 0.5 at the Cheng 2020 frequency, DERIVED, so that most litters give no knockout and about 15 to 19 percent of the litters that give one give two or more) the bootstrap over litters is the primary interval; with fewer than 10 litters in a cell the laboratory uses a permutation test or a mixed model with a litter random effect and says so before data. The absolute-scale interaction is a secondary report.
- **Shared vehicle and multiplicity.** The family is the set of comparisons that share one vehicle group within one session and one genotype, counted from the final arm list and fixed, with the divisor, before data. In the required ethosuximide session the count is the one the sample-size section already uses: wild type at each age 6 test arms (ethosuximide at two exposures, the flat-profile and the rising-profile panel agent at two exposures each), knockout and heterozygote at the assay age 2 test arms (ethosuximide at two exposures). The vehicle is sized n x sqrt(k) (about 26.9 for k = 6 and 15.6 for k = 2 at n = 11) and the intervals are reported at 95% and at the Bonferroni-adjusted level 1 minus 0.05/k (about 99.17% for k = 6 and 97.5% for k = 2). The ethosuximide comparison at the assay age in the knockout is the pre-specified primary and is judged at 95% (see the primary comparison below); every other effect counts as confirmed only if it holds at the adjusted level of its family. An arm added to a session and not labelled exploratory before data enters that session's family (k rises, the adjusted level moves with it); an arm run in its own session carries its own vehicle group and its own family; an arm labelled exploratory before data is reported at 95% only and is outside the family. The lithium session (lithium, the second GSK-3 inhibitor, the comparator drug, any optional second regimen) is such a session: its k is read off its final arm list.
- **Why a ratio.** A bounded scale (0 to 6, floor at 0) makes a proportional effect look smaller in absolute grade where the baseline is low; that is why the ratio scale is primary and the floor rule exists.
- **Order of hypotheses (fixed before data).** (i) panel validity at each age; (ii) the ethosuximide effect ratios in the knockout and in the wild type at the assay age and at the older ages, as descriptive ratios with their intervals (the primary, the knockout ratio at the assay age, is judged at 95%; every other ratio is descriptive); (iii) the interaction ratio with its interval, **exploratory unless the pilot SD makes it sized**. Where the interaction cannot be sized, the answer comes through (i) and (ii).

[Design-team answer R2C09, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. The single pre-specified primary is the knockout ethosuximide ratio R(-/-) at the assay age, at the exposure the laboratory fixes before the first animal, judged at 95%. It is the comparison the sample-size section is computed for (knockout vehicle against ethosuximide, three knockout cells at the credible scale). Every other ratio (the other exposure, the wild-type ratio, the older ages, the panel agents, the interaction) is descriptive with its interval; the interaction is exploratory unless sized. The text that lists the ethosuximide effects as descriptive ratios keeps that wording for the ratios other than the primary; a reader who finds the same ratio named primary and descriptive should read the primary as this one only.]

**OPEN-GAP D06 (owner laboratory): which ethosuximide exposure is the primary in the knockout at the assay age, fixed before the first animal?**

[Design-team answer C35, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. The earlier statement of five comparisons (99%) is replaced; the planning total (about 354 animals) is unchanged, because it already counted 6 and 2. The count takes each exposure as a test arm, as the cell total of the sample-size section does (6 cells in wild type per age, 2 in knockout and heterozygote); counting per agent instead would give 3 and 1 and is not adopted.]

(see the design-team answer D04 above)

[Design-team answer Q68, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Rule (INFERENCE from documented numbers): vehicle S in a genotype is 'at the floor' when its mean S is at most 0.41 (grade units, the highest of the documented wild-type and heterozygote means that the addendum calls floor-bound, 0.27 to 0.41) or its CV is at least 1.4 (the addendum's floor-bound CV); either condition makes a ratio of 0.7 need about 140 to 210 per arm. To be replaced by the pilot's own distribution. Unit caveat: S in the earlier text is an area over 60 minutes while 0.27 to 0.41 are mean stage values, so the threshold must be restated in the units the pilot reports; an additional criterion is more than half of the animals with S = 0.]

**OPEN-GAP Q69 (owner SCI): How is an increase of seizure burden (aggravation, R above 1) classified, since "effect" is defined only as R at most 0.7?**

**OPEN-GAP Q71 (owner SCI): To whom and in what form is the analysis plan "stated before data" delivered (registry, collaborator, time stamp)?**

[Design-team answer Q73/C37, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Descriptive pattern when the interaction cannot be sized (INFERENCE, a rule the design team defines; no new number): classify from the two simple-effect ratios of the same session with their litter-bootstrap intervals, panel valid and wild type above the floor. E1: knockout R at most 0.7 with the interval excluding 1, wild-type interval inside 0.85 to 1.15. E3: both genotypes show an effect (R at most 0.7, interval excluding 1) and the point estimate of the interaction ratio lies above 0.7 and below 1.43. Anything else (wild type at the floor, wide intervals, only one genotype with an effect and the wild-type interval not inside 0.85 to 1.15): not separable, report both simple ratios and the interaction ratio as exploratory. The interaction interval is reported but not used to separate E1 from E3 unless the pilot makes it sized.]

**OPEN-GAP Q73 (owner laboratory): pilot data**

## Sample size and animals needed

All figures here are ASSUMED values, hypothesis level, not a forecast, and illustrative until the pilot gives the SD. In Cheng 2020 Fig. 7 the group sizes are printed in the figure legends as N: PTZ-alone knockout 6, knockout with ethosuximide 6, knockout with lithium 7 (6 to 7 knockouts per group); wild type and heterozygous groups 8 to 20 (7b: +/+ 20 and 16, +/- 18 and 12; 7d: +/+ 12 and 8, +/- 12 and 12); they are read from the figure legend, not stated in the Methods text. These group sizes rest on a single origin (the Cheng 2020 Fig. 7 legend): the supplement (24 pages) is held and gives no seizure methods and no seizure-group N (the group sizes it prints belong to the genotyping, with 177 and 785 genotyped pups, and to the brain weight, brain water content and histology panels), and no second source was found by three routes (2026-11-21); only the authors could add one (source statement, not an inference). Knockout yield per litter: the sizing first assumed the Mendelian 25 percent of about 7 pups per litter, that is 1.75 knockouts (ASSUMED), but the observed frequency is lower. Cheng 2020 reports Wwox-/- at 5.1 percent of N = 177 (WD1 line; about 9 knockouts) and 6.5 percent of N = 785 (WD234 line; about 51 knockouts) of pups genotyped at postnatal day 5 to 12 from Wwox+/- intercrosses (supplementary Methods, page 3), which at 7 pups per litter is 0.36 and 0.46 knockouts per litter (DERIVED from that frequency; the litter size of 7 is this brief's own figure and the knockout counts are the percentages times N). Another null line (exon 1 deleted by Cre) gave 30 knockouts among 154 pups genotyped at day 3 from heterozygote crosses (19.5 percent; 38.5 expected; p = 0.257, Mendelian-compatible; Ludes-Meyers 2009, Table 1); a different line and age, and the two are not reconciled here. Limits: the Cheng frequency pools pups of postnatal day 5 to 12; the frequency at the assay age is not reported and, if knockouts are lost no more slowly than their littermates, is at most that frequency; the paper states that some very severely affected embryos died embryonically but gives no count, so losses before genotyping are not quantified and would lower the yield further; the colony frequency of the laboratory governs the litter count. Litter figures below that depend on the yield are given at the assumed 1.75 and at the Cheng frequency (litters = knockouts over 7 times the frequency, rounded up; DERIVED); the 1.75 figures are a Mendelian case, not the expected yield. Where two older statements gave different figures for the same quantity, the later statement is used and the earlier one is in the History.

| Quantity | Value as stated | Basis |
|---|---|---|
| simple effect of ratio 0.7 (ln = -0.357), animals per arm | about 11, 31 or 79 for a within-genotype SD of 0.3, 0.5 or 0.8 | two-sided 0.05, power 0.80; the SD of 0.3 is the optimistic case |
| simple effect, from an eye reading of Cheng 2020 Fig. 7b (knockout PTZ-alone curve, N = 6; SEM bars of about a third to a half of the mean) | an SD of S of 0.7 to 1 times the mean, about 0.6 to 0.8 on the log scale; roughly 44 to 79 animals per arm | the number 44 here is a simple-effect number per arm; see the note below the table |
| simple effect, from a quantification of the means and upward SEM bars of Fig. 7b and 7d (per-minute SD = SEM times the square root of N; S = mean grade over 60 minutes; bounds from independent to fully correlated minutes; N assumed constant) | knockout PTZ-alone groups: a CV of S of 0.58 to 1.19 at a within-animal correlation of 0.6 to 1.0 (log SD about 0.54 to 0.94; the rigorous upper bound is 0.67 for 7b and 0.94 for 7d); about 36 to 109 animals per arm for a ratio of 0.7 | hypothesis level; the "log SD 0.6 to 0.8" of the eye reading is inside this bracket; the optimistic SD of 0.3 is not credible (it needs a within-animal correlation of 0.05 to 0.15) |
| wild-type and heterozygous pups at that published stimulus | at the floor: mean S 0.27 to 0.41, CV above 1.4; a ratio of 0.7 would need about 140 to 210 per arm, so a stimulus with a non-floor wild-type response is a requirement, not an option | same quantification; the floor bracket is a 60-minute mean grade (see the wild-type grade in the question section) |
| a binary outcome such as generalised seizure (assume 50% in vehicle knockouts) | a fall to 10% needs about 20 per arm; a fall to 20% about 38 | assumed values |
| interaction contrast (genotype by treatment), per cell | **twice** (not four times) the simple-effect number per cell; with the bracket above, about **180 to 320 animals per cell**; four cells; about 700 to 1,300 animals and 350 to 630 knockouts (200 to 360 litters at the assumed 1.75 per litter; 770 to 1,765 litters at the Cheng 2020 knockout frequency, DERIVED) for one drug against vehicle | the later statement; the older statement of four times is in the History |
| the same interaction contrast at the optimistic SD of 0.3 | 22 per cell, 88 animals, 25 litters at the assumed 1.75 per litter (rounded to the nearest litter; 44 knockouts / 1.75 = 25.1) (97 to 124 at the Cheng 2020 knockout frequency, DERIVED, rounded up) for one drug against vehicle | optimistic scale |
| three knockout arms, simple effect only | at 11 per arm about 19 litters; at 31 per arm about 53; at 36 to 109 per arm, 108 to 327 knockouts, about 62 to 187 litters (all at the assumed 1.75 per litter; at the Cheng 2020 knockout frequency, DERIVED, 73 to 93 litters at 11 per arm, 205 to 261 at 31 and 238 to 916 at 36 to 109, the lower figure of each pair at 6.5 percent and the higher at 5.1) | the figures at 11 and 31 are the optimistic scale; the figures at 36 to 109 follow the bracket |
| planning total for the required stages with the dose check (two exposures per agent per age, panel included; for planning, not a promise) | about 27 cells (the wild-type age series: 3 ages times vehicle, ethosuximide at two exposures, one flat-profile and one rising-profile panel agent at two exposures each = 21 cells; knockout and heterozygote at the assay age: vehicle and ethosuximide at two exposures = 6 cells), i.e. about 300 animals at 11 per cell or about 1,350 at 50 per cell, of which 33 to 150 knockouts (19 to 86 litters at the assumed 1.75 per litter; 73 to 421 litters at the Cheng 2020 knockout frequency, DERIVED: 93 to 421 at 5.1 percent and 73 to 330 at 6.5) | optimistic scale (the basis of the per-cell figure of 50 is not stated); the pilot decides the dose check first: if the lower exposure is effective in the panel agent at an age, one exposure per agent at that age is enough and the totals fall accordingly |

[Design-team answer C003, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Both totals: 3 ages = 21 wild-type cells and 27 cells in all (about 300 animals at 11 per cell, about 350 with the doubled vehicle); 4 ages (straddle wanted, assay age at P12 or later) = 28 wild-type cells and 34 cells in all, +77 animals at 11 per cell (34 x 11 = 374 against 297). The three-age totals stand for the primary contrast whatever the working window P12 to P17, because the straddle is optional (see the note on the age series).]

[Design-team answer R3Q37, 2026-11-21; status: INFERENCE: an illustrative range with its basis, not a source value; the figure itself is the laboratory's. No single figure can be fixed before the pilot gives the SD and the laboratory states its capacity. If one must be written, it is a range with its basis, not one number: (a) pilot: 36 to 48 animals (12 to 16 knockouts = 7 to 9 litters at the assumed 1.75 per litter (rounded to the nearest litter), 27 to 45 at the Cheng 2020 knockout frequency (DERIVED, rounded up); wild types from heterozygote crosses 14 to 18 litters at 1.75 (nearest), which at the Cheng frequency the knockout litters would already supply if wild types are about 25 percent of the pups (their frequency is not reported), or from wild-type pairs fewer); (b) required stage 2 at the credible scale: knockouts 108 to 327 for three knockout cells (vehicle plus ethosuximide at two exposures) = 62 to 187 litters of heterozygote crosses at the assumed 1.75 knockouts per litter, 238 to 916 at the Cheng 2020 knockout frequency of 6.5 to 5.1 percent (DERIVED); wild-type age series and panel 21 cells at 11 per cell = 231 animals, about 132 litters from heterozygote crosses at 1.75 per litter (at the Cheng frequency the knockout litters of this stage already exceed that number and would supply the wild types if these are about 25 percent of the pups; their frequency is not reported) or about 33 from wild-type pairs; the genotype-by-treatment interaction is not in the application figure (180 to 320 per cell at floor-bound wild-type variability, 72 to 218 at equal variability). All of it is illustrative until the pilot gives the SD.]

**OPEN-GAP S14 (owner laboratory): how many knockout and wild-type pups per month can you supply, and from which breeding scheme?**

[Design-team answer R3C01, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Which stimulus governs which cell: (a) the replication cells (ethosuximide and lithium in knockouts, with their vehicle, in a session of their own) use the published stimulus of Cheng 2020, because their purpose is to repeat that condition; (b) every cell that enters a genotype contrast, the panel or the age series uses the stimulus fixed in the pilot at which wild-type vehicle pups are not at the floor. If the pilot finds that the published stimulus is the one at which wild-type vehicle pups are not at the floor, the two coincide. If it is not, the contrast is read at the pilot stimulus and the replication at the published one; a stage that runs with a different stimulus carries its own vehicle group per genotype (the shared vehicle holds only within a session), which adds one vehicle cell per genotype to the totals. If only one of the two can be run, the contrast stimulus is kept and the replication is reported as not attempted. If a non-floor wild-type stimulus pushes knockout pups past the laboratory's approved stopping rule, the design becomes replication-only and the genotype contrast is abandoned, not weakened.]

**OPEN-GAP S10 (owner laboratory): at the published stimulus, do wild-type vehicle pups at your assay age show a non-floor response?**

Note on the number 44. The older texts used it for two different quantities: (i) a simple-effect number of 44 to 79 animals per arm at log SD 0.6 to 0.8 (the eye reading above); (ii) an interaction number of 44 per cell at SD 0.3 in the original arithmetic, which is superseded (see the History). Only the first is current.

**Planning scale.** The 36 to 109 animals per arm for the knockout is the scale for planning. The litter and animal totals of the sections above (19 and 53 litters; 25 litters for one drug-by-genotype interaction; the dose-check totals) are the optimistic scale and, being counted at the assumed 1.75 knockouts per litter, also the Mendelian case; they should be read with the 36 to 109 bracket, at which three knockout arms need 62 to 187 litters at 1.75 per litter and 238 to 916 at the Cheng 2020 knockout frequency (DERIVED; see the sentence on the knockout yield per litter above).

[Design-team answer R3C09, 2026-11-21; status: corrected by the design team. The text's references to '75 litters' as a figure of the sections above are replaced by the current figures of the planning table: at the optimistic log SD 0.3 (not credible) three knockout arms need 19 litters (11 per arm) and one drug-by-genotype interaction 25 litters; at the credible scale three knockout arms need 62 to 187 litters (36 to 109 per arm); all at the assumed 1.75 knockouts per litter, against 73 to 93, 97 to 124 and 238 to 916 litters at the Cheng 2020 knockout frequency (DERIVED). '75 litters' (3 x 44) is a superseded figure and stays in the History only.]

**An independent reading** of the same curves agrees within about 20 percent (per-minute means within 0.05 and 0.15 grade; SD of the summed grade 9.5 to 62 and 10.9 to 69 against 11.4 to 71.5 and 9.2 to 56.9 for the first reading, whose values are given only here) and concludes that the sizing flag stands.

**Limit on direction.** The bracket assumes the legend N over the whole hour; whether animals that die keep grade 6 or leave the mean is not stated, and the two possibilities bias the SD in opposite directions (fewer contributing animals than the legend N makes the bracket overstate the per-minute SD; survivor-only curves make it understate the full-cohort SD); the net direction needs the authors' per-animal data and does not change the order of magnitude of the sizing.

**The genotype-by-treatment contrast is therefore not attemptable with the full-hour area summary at the variability these curves show;** it is attemptable only if the pilot finds a stimulus or a summary (for example an incidence of generalised seizures) with far lower variability. The order of hypotheses under "Analysis plan" stands: panel validity and the effect ratios by genotype and age come first, and the interaction is an exploratory interval. The brief says so rather than promising an interaction test.

**A stage that runs in a different session carries its own vehicle group per genotype** (the shared vehicle holds only within a session).

Wild-type and heterozygous animals are not limiting.

[Design-team answer C25/Q45, 2026-11-21; status: computed from stated inputs; one input is the laboratory's. 'Wild-type and heterozygous animals are not limiting' holds only if wild types come from wild-type breeding pairs. From heterozygote crosses wild types are 1.75 per litter like knockouts: 21 wild-type cells at 11 are 231 animals = about 132 litters, against about 33 litters from wild-type pairs at 7 pups, and 33 knockouts need about 19 litters at 1.75 per litter (73 to 93 at the Cheng 2020 knockout frequency, DERIVED; the wild-type frequency is not reported, so 1.75 for wild types stays a Mendelian assumption).]

**OPEN-GAP C25 (owner laboratory): wild-type source**

[Design-team answer Q45, 2026-11-21; status: partly closed. The brief's 'wild-type and heterozygous animals are not limiting' holds only if wild types come from wild-type breeders. From heterozygote crosses wild types yield 1.75 per litter like knockouts. Computed (INFERENCE): 21 wild-type cells at 11 = 231 animals = 132 heterozygote-cross litters, against 33 litters from wild-type pairs at 7 pups; 33 knockouts need 19 litters at 1.75 per litter (73 to 93 at the Cheng 2020 knockout frequency, DERIVED; the wild-type frequency is not reported).]

**OPEN-GAP Q45 (owner laboratory): can wild-type pups for the age series and the panel come from wild-type pairs of the same background, and is littermate control needed for the knockout contrast?**

[Design-team answer C06, 2026-11-21; status: computed from stated inputs. Both brackets are right and answer different contrasts. 36 to 109 animals per arm is the simple effect in the knockout (knockout variability only). 180 to 320 animals per cell is the interaction contrast, whose variance holds the knockout and the wild-type variability; the per-cell number is the SUM of the two simple-effect numbers (knockout plus wild type), not twice the knockout number. 'Twice' holds only when the variability is equal in the two genotypes. Inputs of the per-cell figure: ratio 0.7, two-sided alpha 0.05, power 0.80, log SD 0.54 to 0.94 in the knockout and 1.06 to 1.30 in wild type and heterozygous pups (floor-bound arms, mean S 0.27 to 0.41, CV above 1.4).]

[Design-team answer C04, 2026-11-21; status: computed from stated inputs. The addendum is current. The standing figures from the superseded four-times rule (176 animals, 88 knockouts, 75 litters, 132 knockouts) are replaced as below and kept in History only. At the optimistic scale (log SD 0.3, which the addendum calls not credible): interaction 22 per cell, 4 cells 88 animals, 44 knockouts, 25 litters at the assumed 1.75 per litter (rounded to the nearest litter; 44 / 1.75 = 25.1) (97 to 124 at the Cheng 2020 knockout frequency, DERIVED, rounded up), for one drug against vehicle. The credible planning scale is the two-scale table in the planning table (C07). C04 resolves with C06: 'later wins' holds because the later statement corrects the per-cell factor; its own range (180 to 320) is right for floor-bound wild-type variability.]

[Design-team answer C07, 2026-11-21; status: computed from stated inputs. Planning table at three variability scales, animals per cell, litters at 1.75 knockouts per litter (all ASSUMED values; ratio 0.7; alpha 0.05 two-sided; power 0.80): (a) log SD 0.3, optimistic and not credible: simple effect 11 per arm, three knockout arms 33 knockouts = 19 litters; interaction 22 per cell, 88 animals, 44 knockouts, 25 litters. (b) log SD 0.5: simple effect 31 per arm, three knockout arms 93 knockouts = 53 litters; interaction 62 per cell, about 250 animals, 124 knockouts, 71 litters. (c) credible scale from the published curves: simple effect 36 to 109 per arm, three knockout arms 108 to 327 knockouts = 62 to 187 litters; interaction 72 to 218 per cell at equal variability (about 290 to 870 animals, 145 to 435 knockouts, 82 to 249 litters) and 180 to 320 per cell with floor-bound wild-type variability (about 700 to 1,300 animals, 350 to 630 knockouts, 200 to 360 litters). The planning scale is (c); 11 per cell is a lower bound only. Correction 2026-11-28: the litter figures of (a) to (c) are at the assumed Mendelian 1.75 knockouts per litter; at the Cheng 2020 knockout frequency (5.1 to 6.5 percent; DERIVED; litters rounded up) they are (a) three knockout arms 73 to 93 litters, interaction 97 to 124; (b) three knockout arms 205 to 261, interaction 273 to 348; (c) three knockout arms 238 to 916, interaction 319 to 1,219 at equal variability and 770 to 1,765 at floor-bound wild-type variability.]

**OPEN-GAP C07 (owner laboratory): pilot SD**

[Design-team answer C08/Q32, 2026-11-21; status: computed from stated inputs. The 27-cell total of about 300 animals gives every cell the same n (27 x 11 = 297). With the shared vehicle at about twice a test arm (square-root rule, n x sqrt(k)) and 11 per test arm, the total is about 354: wild type per age 6 test arms 66 plus vehicle 26.9 = 92.9, times 3 ages; knockout and heterozygote at the assay age 2 test arms 22 plus vehicle 15.6 = 37.6, times 2 genotypes. The vehicle of an age is also shared by the panel agents, which the square-root rule counts as test arms. State 'about 300 at equal cells, about 350 with the doubled vehicle'.]

[Design-team answer Q32, 2026-11-21; status: partly closed. Statements disagree: an earlier statement says one shared vehicle group per genotype of about twice a test arm (square-root rule); an earlier statement totals 27 cells at 11 per cell = 297 animals, i.e. vehicle cells at 11 (not doubled). Computed (INFERENCE, square-root rule n_vehicle = n x sqrt(k) per age and genotype): at 11 per arm the total is about 354, not about 300 (WT per age 6 arms: 66 + 26.9 = 92.9; knockout and heterozygote 2 arms each: 22 + 15.6 = 37.6). The 'about 300' does not count the doubled vehicle.]

[Design-team answer Q31, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Mapping of the figures in the briefs (INFERENCE where noted, from the inputs of the addendum): 11 and 31 and 79 per arm = simple effect at sigma_log 0.3, 0.5, 0.8; 22 = interaction at sigma 0.3 with equal sigma (twice 11); 44 = the superseded 'four times' error; 50 = an illustration; 36 to 109 = simple effect in knockouts at sigma 0.54 to 0.94 (addendum); 180 to 320 = interaction per cell with wild-type sigma 1.07 to 1.30 (see C06). For the first run (pilot) the brief already states 6 to 8 per cell. For stage 2, rule: n per arm = n_simple(sigma-hat from the pilot) with sigma-hat inflated by one relative standard error of an SD (1/sqrt(2(n-1)): 0.29 at n = 7), which at the addendum's range moves 36 to 60 and 109 to 181 per arm.]

(see the design-team answer C08/Q32 above)

[Design-team answer Q33, 2026-11-21; status: stated in a source text. All four litter figures are reproducible from stated inputs at 1.75 knockouts per litter: 19 = 3 knockout arms x 11 (sigma 0.3, simple); 53 = 3 x 31 (sigma 0.5, simple); 25 = interaction 22 per cell, 2 knockout cells = 44 knockouts (sigma 0.3; one drug against vehicle; the CURRENT optimistic figure after the correction in the addendum); 75 = 3 x 44. The addendum's credible range: 62 to 187 litters for three knockout arms at 36 to 109 (simple); 200 to 360 for one drug interaction at 175 to 315 per cell; both at the assumed 1.75 per litter (rounded to the nearest litter; 238 to 916 and 770 to 1,765 at the Cheng 2020 knockout frequency, DERIVED, rounded up). Note that the addendum itself calls sigma 0.3 not credible.]

## Welfare and stopping

**Humane endpoints and approvals are the laboratory's.** About half of PTZ-injected knockouts reached status epilepticus in Cheng 2020. A stopping rule for status (when to rescue, by the laboratory's own approved procedure; the pup then stays in the analysis with its last grade carried forward, flagged), written before the first animal, is a design requirement, not an option. The laboratory's own ethics approval for PTZ-provoked status epilepticus in fragile knockout pups is needed, and the laboratory decides whether stage 2 is possible at all. Stage stop rules are in the stage table.

[Design-team answer Q61, 2026-11-21; status: partly closed. Source statement: the definition of status = three or more tonic-clonic seizures within the hour (Cheng 2020), reached by about half of PTZ-injected knockouts; the brief requires a status stopping rule, written before the first animal, using the laboratory's approved rescue procedure, with the pup kept in the analysis at its last stage, flagged, and results reported with and without. The trigger, the rescue procedure and whether the rescue agent is given identically to all arms are not in any source read; no value is proposed (welfare).]

**OPEN-GAP Q61 (owner laboratory): what trigger and procedure does your approved protocol use for status, who decides blind to arm, and does the rescue agent confound the arm contrast (given identically to all arms or not)?**

[Design-team answer Q62, 2026-11-21; status: partly closed. Source statement: death is a scored outcome and about half of PTZ-injected knockouts reached status. Not stated: the death or status rate per arm, or whether the laboratory's approval accepts death as an outcome rather than a humane endpoint.]

**OPEN-GAP Q62 (owner laboratory): does your approval accept death as an outcome or require a humane endpoint, and what death and status rates have you seen in vehicle and treated knockouts at your stimulus?**

**OPEN-GAP Q63 (owner laboratory): What are the conditions of the 60-minute observation of fragile pups (dam present or isolated, heat support, handling)?**

**OPEN-GAP Q65 (owner laboratory): What experiment-level stopping rules exist (for example cumulative knockout deaths) beyond the pilot and stage stop rules?**

**OPEN-GAP Q66 (owner laboratory): What is the total procedural burden on one pup in the lithium arm (three injections, pre-test, PTZ, observation, possible tissue)?**

[Design-team answer QA5, 2026-11-21; status: partly closed. Source statement: stage 1 stop = knockout vehicle pups cannot be tested at a wild-type response that is not at the floor, or the panel agent has no effect at any age; stage 2 'if the panel is not valid at the assay age, move the assay age, do not read the null'; stage 4 waits for the slice arm. Rule (INFERENCE from the stage dependencies): a stage-1 stop ends stages 2 to 4 (they take the assay age, stimulus and sample size from it); the stage-2 branch ends only that reading (move age, repeat), not stage 3.]

[Design-team answer QA4, 2026-11-21; status: source statements only; the value is the laboratory's or the operator's. Each pup is tested once; pilot pups are therefore not reused in treated arms. Pilot data may enter the main analysis only if the pilot arm is identical to a main arm and declared so in writing before it is run. The sign-off (who accepts the pilot and releases stage 2) is not stated in the brief.]

**OPEN-GAP QA4 (owner laboratory): who signs off the pilot and releases stage 2?**

## What each outcome would favour

Hypothesis; each row is one stated reading.

| Arm | Pattern (panel valid at the age, wild type above floor) | Favours | Does not show |
|---|---|---|---|
| Ethosuximide | R(-/-) effect; R(+/+) null; interaction at most 0.7 (E1) | a knockout-selective effect | a T-type route; spontaneous-seizure benefit |
| Ethosuximide | R(+/+) a null at the assay age and an effect at the older age, with the panel valid and wild-type vehicle S above the floor (E2); if wild-type vehicle S is at or below the floor, R(+/+) is not computed and the reading is E5 | an age-limited wild-type non-response, not a floor-bound arm; the Cheng 2020 pattern is not knockout selectivity | that the knockout effect is absent |
| Ethosuximide | similar effects in all genotypes (E3) | a general anticonvulsant effect | selectivity or its absence at other ages |
| Ethosuximide | no effect anywhere (E4) | the Cheng 2020 knockout effect did not replicate at this age and stimulus | any statement about other ages or exposures |
| Selective T-type blocker beside ethosuximide | same pattern as ethosuximide in the knockout (C1) | a T-type route is plausible (not proven without engagement or genetics) | Cav3 expression in the knockout |
| Selective T-type blocker | no effect where ethosuximide has one (C2); applies only if the laboratory has added an engagement control, since without one a T-type null is not interpretable | ethosuximide's effect is not carried by selective T-type block at this exposure and age, or the exposure was inadequate | which |
| Lithium, second GSK-3 inhibitor, general comparator drug | lithium effect in all genotypes (interaction above 0.7 and below 1.43); second GSK-3 inhibitor effect; comparator effect | a general anticonvulsant effect of GSK-3 inhibition and of the comparator | GSK-3 specificity in the knockout |
| Lithium | knockout-larger effect, **reproduced by the second GSK-3 inhibitor and not by the comparator** | GSK-3 route, knockout-enhanced | p-Ser9 change or kinase activity (needs the add-on) |
| Any arm | minimal-seizure incidence up while generalised incidence down | seizure-type-specific action | benefit or harm in the null phenotype |

[Design-team answer R3C05, 2026-11-21; status: stated in a source text; the wording of the earlier row is corrected. The frozen in vivo priors settle it: the whole set E is conditioned on 'panel valid, wild type above floor' (set header), the floor is wild-type vehicle S below the stage-1 equivalent of the laboratory's detection limit, and an arm at the floor is class E5 'not interpretable'. The word 'floor' in E2's name ('age-limited with a wild-type floor') therefore does NOT mean a floor-bound arm; it means a small wild-type drug effect at the assay age while the wild-type vehicle S is above the pilot-fixed floor. Corrected E2 row: 'R(+/+) a null at the assay age and an effect at the older age, with the panel valid and wild-type vehicle S above the floor (an age-limited wild-type non-response, not a floor-bound arm); knockout effect present or not. If wild-type vehicle S is at or below the floor, R(+/+) is not computed and the reading is E5.']

The weights for these classes are in the predictions file; they are scored literally when data exist and are not calibrated probabilities.

C1 and C2 are labels of the two T-type rows (the blocker matches ethosuximide, or does not).

[Clarification by text work, for SCI to confirm: the first lithium row appears to correspond to reading L1 and the second to reading L2; the older table carries no L1 or L2 labels.]

[Design-team answer Q82, 2026-11-21; status: confirmed by the design team. Reading L1 (general) = the row 'lithium effect in all genotypes (interaction above 0.7 and below 1.43); second GSK-3 inhibitor effect; comparator effect'. Reading L2 (GSK-3-specific) = the row 'knockout-larger effect, reproduced by the second GSK-3 inhibitor and not by the comparator'. The title names L1 as general and L2 as GSK-3-specific.]

## Optional add-ons

All are optional; none changes an arm, a size or the order of stages. The one animal cohort of the calcium, glucose, glia and inhibitory-current lines below can carry them together, as stated in the line on inhibitory currents.

- **(a) Video-EEG** on a subset of knockout pups (the only route to spontaneous-seizure burden).
- **(b) p-Ser9 and total GSK-3beta** in tissue from the same lithium-treated and vehicle animals (Cheng 2020 measured p-Ser9 only in untreated animals, and its Methods and legend disagree on the age, day 14 against day 20).
- **(c) A Cav3 transcript or protein readout** from the same animals' tissue (no Cav3 measurement in Wwox-null tissue was found by two routes).

**OPEN-GAP R2Q80 (owner SCI): Which Cav3 transcript or protein readout, region and age is meant by add-on (c)?**
- **(d) Deletion completeness.** Record it per animal and per region at the protein level (immunostaining or a per-slice check) and report each effect against it; **residual bulk transcript is not deletion completeness** (control cortex about five times the hippocampal Wwox TPM; non-neuronal Wwox in bulk tissue; one of three knockout cortices inside the control range at P17; stage and deletion depth not separable at n = 3). The note on which this rests states it for the slice pilot and the pup brief in the words "a Synapsin-Cre deletion"; how it applies to a germline null is the laboratory's.
- **(e) A glucose series tied to seizure timing: optional, not a diet or glucose arm.** The original papers read do not show whether hypoglycaemia drives seizures and death or only accompanies them (no original paper read manipulates glucose; the rescues normalise glucose, growth, seizures and survival together). Gaps: no glucose before P10 (null about 95 against 130 mg/dl at P10 to P11, about 58 at P14, about 57 at P19, read from plots); none at the time of any seizure; none ever reported for the neuron-targeted or progenitor-targeted seizure-and-death lines (mouse lines in which pups seize and die early). Measurements: **blood glucose in the seizure-and-death lines (P7 to P14), glucose at seizure time (same-animal pairs with video-EEG or ECoG, the sampling burden stated), ketone and lactate by age, milk intake or stomach filling.** **The ketogenic-diet comparison is unchanged** (its rationale neither gains nor loses decisively).
- **(e2) Calcium, glucose, weight and milk-spot add-on** (dated 2026-11-21; hypothesis level; no dose; one optional add-on measurement line, not an arm and not a change to the design). Alongside any GFAP (glial fibrillary acidic protein) and Iba1 (microglial marker) scoring at P5 to P9, add serum total calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot (stomach-content visibility) score at P7, P9, P11 and P14, genotype-blind, in the germline null against the neuron-targeted line (S-KO). Reason: no source read has any of these values in a null pup between P7 and P14 (calcium only at P18 in one germline null line, 8.5 percent below wild type, n 3, 3 and 4 and weaker than printed once recomputed; glucose and glia have the same missing window), and the S-KO line, which seizes from P9, has never had a serum value. A change present in both lines is downstream of the central nervous system state or of feeding; a change present only in the germline null points to a systemic or endocrine origin; the milk-spot score is there because feeding is not separated from the P18 changes in any source read. The add-on is the cheapest form of the missing measure and carries no dose or schedule. This add-on needs, besides the germline null, the neuron-targeted line (a conditional neuron-specific knockout); the line, allele and cross are not stated in the older texts.
- **(e3) Inhibitory currents and phospho-ErbB4** (dated 2026-11-21; hypothesis level; no dose; one optional add-on measurement line next to (e2), not an arm and not a change to the design). The bridging observation for the NRG1-ErbB4 question is the inhibitory synaptic response (sIPSC, spontaneous inhibitory postsynaptic current, frequency and amplitude) in the neuron-targeted and germline-null pups against controls, read together with phospho-ErbB4 in PV (parvalbumin) interneurons, in the same pup window as (e2). A single animal cohort can carry all of it: serum calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot score, GFAP and Iba1 scoring, and sIPSC with phospho-ErbB4 in PV cells, taken from one group of pups. The GFAP and Iba1 part stays because the pre-onset glial sign in other early-onset epilepsy models came back mixed (stain-level GFAP and Iba1 mostly not different from wild type before the first seizure, one rise; cytokine and pathway-level rises in three models; no energy readout at all), not flat or lower across models; it is a readout scored beside the others, not an arm. Reason for the sIPSC and phospho-ErbB4 pair: the sign premise that Wwox loss lowers ErbB4 signalling in PV cells is untested, and everything said in favour of the NRG1-ErbB4 class depends on it.

- **(e3), dated line 2026-11-22 (ADV-167, from Sun 2016 in an adjacent wild-type juvenile mouse visual cortex; the text above is unchanged; not an arm and not a gate):** where the preparation and age allow PV identification (PV-reporter identification starts from about two weeks after birth, so a neonatal window may not allow it), an optional state descriptor: record baseline excitatory input onto identified PV cells beside baseline phospho-ErbB4 and the sIPSC read in (e3). Sun's input measure was photostimulation-EVOKED synaptic input, whereas the earlier draft clause named SPONTANEOUS excitatory currents: they are different quantities; keep them distinct and leave the choice of measure to the preparation. In Sun the two state variables co-vary; a paired reading shows whether they co-vary or separate in Wwox tissue, but neither a paired reading nor a null shows causal moderation, an absent response, absence of engagement or a WWOX result.

**OPEN-GAP R2Q79 (owner SCI): How are the inhibitory currents and phospho-ErbB4 to be measured (region, age, method, tissue plan) in animals of the same cohort as the calcium and serum add-on?**
- **(e4) The human side** (dated 2026-11-21; class level, no dose). The human side is empty too: calcium and parathyroid hormone are named in no human WWOX-DEE or SCAR12 (a human WWOX-related disorder) report read (20 reports and 4 reviews read at full-text depth; 15 further reports not obtained and unread at full text, a named access gap), and no lipid statement exists at an infant age (the single human lipid statement is "low" in one case at 21 months, not infant, at the edge of the spectrum). This strengthens the add-on measurement of (e2); it settles nothing in either direction.

[Design-team answer C31/Q57, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Default: ONE combined add-on, taken at P7, P9, P11 and P14, with the union of the lists of (e) and (e2) (glucose, ketone, lactate; milk intake or stomach filling; serum total calcium with albumin or ionised calcium; body weight; milk-spot score), glucose and feeding read taken once. This is the arrangement with the fewest pups and the least handling. If the laboratory's blood volume does not allow the union in the same pups at one age, split into two add-ons with their own lists and ages, still reading glucose and feeding once; the split is stated before data. This also settles the open question on one or two add-ons and on serial or separate cohorts: serial in the same pups is the default, separate cohorts only if the blood volume forces it.]

**OPEN-GAP D03 (owner laboratory): can the union be taken serially in the same pups at P7, P9, P11 and P14, or must the cohorts be separate?**

[Text repair 2026-11-21 conflict C32: no GFAP or Iba1 scoring is planned in the provoked assay; GFAP scoring appears only in the optional development cohort. The words "alongside any GFAP and Iba1 scoring at P5 to P9" in the add-on (e2) therefore apply only if the laboratory adds such scoring or runs that cohort; the measures of the add-on and the ages P7, P9, P11 and P14 are as listed there.]

[Design-team answer C30, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Keep the list of the calcium add-on (e2) as written (serum total calcium with albumin or ionised calcium, glucose, body weight, milk-spot score) and read the human-side line (e4) as context: parathyroid hormone and a lipid measure are NOT part of (e2) by default. If the laboratory can supply the pup blood volume for them, they are an optional extension of (e2) stated before data; they are never added without that answer.]

**OPEN-GAP D02 (owner laboratory): how much blood or serum can you take from a P7 pup and from a P14 pup, per sample and in total across P7, P9, P11, P14, and does that cover calcium with albumin, glucose, and optionally parathyroid hormone and a lipid measure?**

**OPEN-GAP T44 (owner SCI): Name the neuron-targeted line (S-KO), its allele, its cross and its source, and define "S-HT", used in (g).**

(see the design-team answer D03 above)

**OPEN-GAP Q54 (owner SCI): For add-on (b), when is tissue taken relative to the last injection and to PTZ, at which age and in which regions?**

**OPEN-GAP Q56 (owner laboratory): How does add-on (d), deletion completeness, apply to a germline null, and what is the laboratory to measure?**

**OPEN-GAP Q60 (owner SCI): For video-EEG on "a subset of knockout pups", which subset size, age and electrode plan?**

- **(f) A heterozygote carrier readout (candidate, one source).** In the germline-null report (3-week-old mice; chloral hydrate; legend SEM; one laboratory) transcranial motor-evoked-potential (Tc-MEP) **onset latency was 1.39 +/- 0.13 ms in wild type (n = 10), 2.13 +/- 0.22 ms in heterozygotes (n = 5; P < 0.05 against wild type) and 2.44 +/- 0.37 ms in nulls (n = 4; P < 0.01), amplitude 59.2 +/- 9.0, 59.6 +/- 17.2 and 11.8 +/- 5.4 microvolts**: a **latency prolongation in heterozygotes against wild type, with amplitude not different from wild type (59.6 against 59.2 microvolts, n.s.; n = 5, large spread)**; the authors write "a partial Tc-MEP deteriorative change"; **Fig 2c prints a bracket between heterozygotes and nulls on latency marked n.s., and Fig 2b one on amplitude marked * (heterozygote against null), although the Methods name only a one-way ANOVA with no post hoc test, so the test behind the brackets is unnamed and heterozygotes are not shown to differ from nulls on latency**. The Results call the measure "onset latency" while the Methods define latency as shock-artefact onset to the major positive peak, and the knockout line used for the recordings is not stated. This text carries no heterozygote bursting incidence: an earlier sentence said it carried only that value, and no such value is stated in either of the older texts.



**OPEN-GAP Q55 (owner SCI): What is the heterozygote bursting incidence that this brief is said to carry, and from which source?**

- **(g) Myelin or conduction endpoints.** The endpoints with demonstrated neuronal-rescue evidence are structural (electron microscopy myelinated-axon counts per animal, g-ratio, MBP (myelin basic protein) and CC1 (an oligodendrocyte marker) immunostaining). **Callosal conduction latency was measured once**: n = 8 slices from 5 animals (controls) and 8 from 6 (knockout), the control n identical to another experiment's S-HT n (possibly copied), effects read from graphs (first-peak latency about 2.5 against 3.2 ms), neuron-targeted line only, acute slices P13 to P17, no rescue, no velocity: **a candidate needing re-measurement with a rescue arm and animal-level statistics, not yet an endpoint.** In the germline null a different in vivo conduction measure exists (Tc-MEP at 3 weeks, n = 10, 5 and 4 for wild type, heterozygote and null; latency 1.39 against 2.44 ms, amplitude 59.2 against 11.8 microvolts; Cheng 2020 Fig. 2; values in add-on (f)): it has no rescue arm, and the paper does not state that its animals were those of the histology (sciatic nerve electron microscopy at postnatal day 20, N = 3). The held latency is a single-distance first-peak latency (no velocity), the unit is the slice, recorded in neocortical layer V after stimulation of the corpus callosum; the N2 (second-peak) latency, whose identity is not defined in Repudi 2021 (the unmyelinated or partially myelinated label is Palma's) and which is not significantly different (P = 0.5737; wide spread, 8 slices per group), is a candidate within-slice control that the brief does not yet carry; no held source gives a conduction readout with a drug arm in a Wwox-deficient model, and no WWOX patient report with an evoked-potential or conduction result was found by a title-and-abstract search on two routes (2026-11-25). **Candidate arm set for a drug test of conduction (ADV-288; hypothesis; no compound, dose or schedule is chosen):** four cells in the same litters (wild type and knockout, vehicle and drug), because in healthy developing wild-type mice the pro-myelinating drug clemastine (one compound, Palma 2022; daily from P5, slices at P21; one mouse as the unit, n = 10 to 12) slowed callosal N1 conduction velocity (ratio about 0.84 read from Fig 2B; one asterisk, P < 0.05 by its legend, while the text states P < 0.01 and the Methods name a paired t-test for two independent groups), so a wild-type drug-only arm is needed before a knockout effect can be read as rescue; callosal N1 velocity from the distance-latency slope over at least three electrode distances with N2 as the control, one value per animal, the same animals' g-ratio, seizure status recorded, recording at P17 to P21; **24 animals per arm planned** (from the held spread, by graph reads, a slowing of the size seen by Palma needs 9 to 24 animals per arm, and at 12 per arm only a ratio of 1.29 or more, or 0.78 or less, is detectable at the upper spread) with a pilot of at least 8 vehicle animals per genotype to replace the graph-read spread; the comparison stops for a compound if wild-type N1 velocity falls by at least 10 percent with the interval excluding zero. A published contrast of Olig2 (corpus callosum) against Mbp (parietal cortex) in the report called P47T in the sources compares different regions (the Mbp panels are Supplementary Figure S6 of the same paper, held by the design team; caption read, panels not opened: parietal cortex above the corpus callosum, 80 and 250 days, n = 3 per genotype, unpaired t-test not significant) and supports only a composition caveat.
- **(h) Sex, litter and cage** are recorded; the public per-animal deposits record none, so results drawn from them are uncontrolled for sex and litter.
- **(i) If a laboratory can take only ONE of the optional measurements** (here add-ons (a), (e), (f) and (g); the PV measurement is in the slice package; no laboratory is named; hypothesis level): glucose tied to seizure timing, add-on (e), first, then the PV count and signal measurement. This order comes from one comparison with unequal originals, is not validated, and the reasoning, not the comparison, carries it.

Add-ons (f) and (g) are optional; conduction is "not yet an endpoint".

**OPEN-GAP Q36 (owner SCI): What is the total animal burden if the add-ons (a) to (i) are included?**

## Optional, conditional cohort

A development-endpoint cohort for lithium on the endpoints of the AAV9 comparator study (hypothesis level; no dose).

- **Not an arm of this design, and not an arm of the slice experiment** (a slice cannot read development endpoints; in this design the provoking injection confounds survival, GFAP and myelination, since about half of PTZ-injected knockouts reached status epilepticus in Cheng 2020). It would be a **separate in vivo cohort**, litter-blocked, with its own vehicle-only knockout group; the treatment start age is the laboratory's.
- **Only lithium qualifies** (with a second GSK-3 inhibitor of another class beside it if it is run): it has the only in vivo Wwox-null drug effect (general-property reading); the sign of GSK-3 inhibition for myelination is divided across studies, so the arm decides nothing in advance. **Ethosuximide, the NMDA-receptor pore blockers and d-APV, and vigabatrin do not qualify** (no development rationale, or a harm experiment first); valproate belongs to the provoked-assay comparator list only.
- **Endpoints (the comparator study's own, age fixed beforehand):** survival to a fixed end age beyond day 17 with a stated censoring day (the primary comparable; untreated knockouts die by about day 17 in the comparator's panel); body-weight series from birth; one composite motor score per animal at a fixed age (the comparator's panel does not state its age: ask the source laboratory or fix our own); GFAP-positive cells; myelination (electron microscopy is the heavy item; a staining readout can precede it); brain size and weight at about day 20. Per-animal summaries and the genotype-by-treatment term are fixed before the first animal; no power calculation is offered (no variance is held for a drug arm).
- **What a comparison with AAV9 would not allow:** prevention against rescue; equivalence of mechanism; durability and dose; a safety comparison (a drug needs its own harm endpoints, for lithium renal and thyroid readouts as the label lists); pup pharmacokinetics are unknown for every agent here.
- **Condition for running it:** only after the provoked assay shows a lithium effect that is **selective, with the genotype-by-treatment term** (prediction P5 of the in vivo priors file rejected on the side of an interaction ratio at most 0.7, and the second GSK-3 inhibitor reproducing it while the non-GSK-3 comparator drug does not). **Fallback if the interaction cannot be sized (it usually cannot):** the interaction term is then exploratory and does not by itself decide; the condition becomes GSK-3 pharmacology in the knockout (lithium effect with R at most 0.7 reproduced by the second GSK-3 inhibitor of another class and not by the non-GSK-3 comparator drug), with the interaction interval reported as exploratory. **"General" is defined once, for the condition, the fallback and the drop rule: the lithium effect is also reproduced by the non-GSK-3 comparator drug** (with an interaction that cannot be sized, genotype specificity cannot be used to tell general from specific). If the provoked assay shows lithium to be general in that sense, the development arm has no rationale beyond a general anticonvulsant and should be dropped. The prior is thin (a divided GSK-3 sign for myelination, no pup exposure data) and an early floor is likely because untreated knockouts die by about day 17.

[Design-team answer R2C10, 2026-11-21; status: INFERENCE: a rule proposed by the design team, not a source value. Prediction P5 is kept as written (two-sided; the priors file is frozen). What a smaller knockout effect means for the optional development cohort: an interaction ratio at least 1.43 (the lithium effect in the knockout smaller than in wild type) rejects P5 but is knockout-attenuated, not knockout-enhanced; it does not by itself qualify the development cohort, whose rationale is a lithium effect in the knockout that the wild type lacks. The cohort condition is therefore: P5 rejected on the side 'ratio at most 0.7' with the second GSK-3 inhibitor reproducing it and the non-GSK-3 comparator not (the fallback, R at most 0.7 reproduced by the second inhibitor, applies when the interaction cannot be sized). A ratio at least 1.43 is reported and the cohort is run only if the laboratory decides so on other grounds, stated before data. This is a separate labelled statement; P5 itself is not edited.]

**OPEN-GAP T45 (owner SCI): Cite the AAV9 comparator study and the gene-addition benchmark paper, and state what is taken from each.**

## Logistics, terms and contact

This text promises no funding, no data ownership, no credit and no authorship, and none is offered until the coordinator of this collaboration says so. A laboratory will ask first: who funds it, who owns the data and what credit or authorship is offered; the lithium regimen and dose questions (see "Regimens and dose checks"); who supplies tool compounds (the T-type and second GSK-3 compounds are not trivial to source, and the laboratory may drop those arms, which are optional); and its own ethics approval for PTZ-provoked status epilepticus in fragile knockout pups (the laboratory's, and it decides whether stage 2 is possible at all). The mouse line, and whether the laboratory has the global knockout or can obtain it, is open. No laboratory is named for this experiment.

**OPEN-GAP Q74 (owner operator): Who funds the work, who owns the data, what credit or authorship is offered, and is there any agreement?**

**OPEN-GAP Q75 (owner operator): Whom does the laboratory ask questions, and by what route, since this text names no laboratory and no contact?**

**OPEN-GAP Q76 (owner operator): What deliverables are expected (per-animal data, litter and sex, coded videos, analysis code) and who runs the analysis?**

**OPEN-GAP Q77 (owner operator): What is the timeline, and does the laboratory wait for the slice experiment before stages 1 to 3?**

**OPEN-GAP Q79 (owner operator): Who supplies the T-type blocker, the second GSK-3 inhibitor and the panel agents?**

**OPEN-GAP Q78 (owner laboratory): How many people, cameras and test sessions does the plan assume (60-minute trials of fragile pups with a blinded scorer not present)?**

**OPEN-GAP Q80 (owner laboratory): How must breeding be scheduled to give same-age pups across litters of one session?**

## Sources and their levels

Cheng 2020 (PMID 32000863; full text, Fig. 7 read by eye); abstracts on ethosuximide ontogeny from one Prague laboratory family and a second-hand relay of them (abstract, relayed); Cortez 2004 (PMID 15582027, abstract, relayed); the rodent age-window table for the panel (abstract level; Tsuda 1997 PMID 9466723, mouse ifenprodil and dizocilpine; Kang 2015 PMID 26029047, mouse phenobarbital; rat PTZ rows of the Prague family; Witherspoon 2022 PMID 36220975, cannabidiol; Kubova 1991, 1993, Mares 2009 and Velisek 1991 for minimal-seizure potentiation); Breton 2021; Kasahara 2019 (full text read); the design team's notes on lithium, onset age, chloride, glucose, conduction and deletion completeness. No statement above is stronger than its level.

**Abstract-level evidence.** The age-window table behind the panel is abstract level, mostly rat, about half from one laboratory family. Three "not found" results (lithium and GSK-3 inhibitors; systemic ketamine in mouse pups; mouse valproate) were confirmed by a second search route. Diazepam ontogeny was found on a blind re-search (a search repeated without sight of the earlier result; see "Ages"). The other "not found" items (Z944, TTA-A2, mibefradil, ICA-069673, XE991 in vivo, eliprodil, fenfluramine) were confirmed as not found with a stated age.

**Second-hand statements.** The statements on the timing limit, the carrier latency, conduction and Olig2 against Mbp come from secondary checks of the source papers; the corrected forms in this text are the ones to use, and none is to be quoted as a source fact before the sentence is read in the source.

## History (old text kept)

This section keeps, word for word, every statement of the two older texts that this text supersedes. Each entry has the date, a plain sentence on what replaced the statement, and the old wording as quoted lines. The older texts themselves are also kept unchanged in the repository. Some quoted lines stop in the middle of a sentence on purpose: each is one verbatim passage of an older text, cut where the superseded statement ends. Names such as ADV, IT, HE and SCI in the quoted lines are roles of the design team and its coordinators in the older texts, kept as written. Repair of 2026-11-21 after the second cold read: two sentences of the Sample size section were restored to the wording of the older texts (the litter totals and the first reading's SD values), and four conflicts and six gaps that the second reader found unmarked received markers, all labelled R2 (the other two of its unmarked questions are answered by the two notes in this paragraph).

### The text itself: which text governs, and for whom it is written
- 2026-11-21: the status box at the top of this text replaces the following statements of the consolidated text (dated 2026-11-19), which said that nothing but folding had changed and that the brief was also written for the operator and the design team. The operator-facing content is kept in a separate operator note and is not in this text.

> This version folds the operator cover and the dated addenda 9.1 to 9.12 of the original into the body; nothing new was read; no tier, size, number, arm, stage or stop rule was changed.
> Written for: a collaborating laboratory that reads this cold, the operator who decides whether and to whom to send it, and (through ADV) IT for the arm table.
> Written for: a collaborating laboratory that reads this cold (and, through ADV, IT for the arm table).

**CONFLICT-OPEN C18 (owner SCI): The consolidated text said that no tier, size, number, arm, stage or stop rule was changed, while its own history lists removed claims and restored clauses and its line on the regimen added the lithium-alone arm; what changed between the original and the consolidated text is not stated in either.**

- 2026-11-21: the two different texts that the older texts both called "9.12" are named apart here: (i) the dated correction of line 9.11 (2026-11-19), counted 9.12 in the consolidated text; (ii) the calcium add-on line of 2026-11-21 in the original brief with dated lines, folded into the add-on called (e2) above. The body of this text does not use the number 9.12.

> 9.11 (2026-11-19, audit and conduction extraction) and its dated correction (counted 9.12; binding)
> Dated line 9.12 (2026-11-21, IT, after ADV-133 strand 1 by SCI

**CONFLICT-OPEN C17 (owner SCI): The older texts give the number 9.12 to two different texts; this text names them apart and does not use the number in its body, and whether the design team wants one numbering of dated lines is open.**

### The lithium regimen as a design variable (superseded 2026-11-19)
- 2026-11-19: the dated line 9.9 of the original replaced the earlier statement that the regimen is a design variable by "One regimen is the main contrast ... a second regimen is an optional comparator arm"; this text follows the later line (see "Regimens and dose checks").

> The lithium regimen (a single acute pretreatment against repeated pretreatment) is a design variable, because the rodent literature the repository holds has acute lithium pro-convulsive and chronic lithium threshold-raising in one mouse PTZ paper family (IT's ADV-051 rows L05 to L09); Cheng 2020's repeated pretreatment within an hour before PTZ is the replication condition and the laboratory states any other regimen before data.
> lithium regimen as a design variable with Cheng's repeated pretreatment as the replication condition;
> section 2.9 treated the lithium regimen as a design variable; read it as follows.

### The interaction arithmetic by "four times" (superseded 2026-11-18, kept beside the correction in the consolidated text)
- 2026-11-18: the dated addendum of the original corrected the interaction rule from four times to twice the simple-effect number per cell; this text uses the corrected figures in one table (see "Sample size and animals needed") and keeps the superseded statements here.

> The interaction contrast needs four equal cells (the arithmetic of this flag is corrected by the dated addendum in section 3) (treated and vehicle, in knockout and wild type): at 44 per cell that is about 176 animals for one drug against vehicle, of which 88 are knockouts; 75 litters is about 525 pups (plus the panel and the age series) and about 132 fragile knockouts.
> The interaction contrast needs four equal cells (treated and vehicle, in knockout and wild type): at 44 per cell about 176 animals for one drug against vehicle, 88 of them knockouts; 75 litters is about 525 pups (plus the panel and the age series) and about 132 fragile knockouts.
> A genotype-by-treatment interaction contrast of the same size needs about four times as many per cell (the contrast is a difference of two differences).
> For the interaction the same arithmetic gives about 44 per cell at SD 0.3, i.e. about 132 knockouts in three arms, about 75 litters, and it is out of reach at SD 0.5 or more. The knockout interaction is therefore realistic only if the pilot SD is about 0.3 or less, and even then needs about 75 litters across the three knockout arms;
> and it is out of reach at SD 0.5 or more.

### A direction change between P11 and P14 in the mouse (superseded 2026-11-19)
- 2026-11-19: after a blind check of the consolidated text, the clause that diazepam shows a mouse direction change between P11 and P14 was removed, because its only source is the confounded Kasahara 2019 study; this text states the conclusion at its evidence level (see "Ages").

> mouse febrile seizures with a high dose exacerbating the induction phase at P11 and not at P14).
> the wild-type age series is more needed, since an agent can change direction between P11 and P14 in the mouse.
> Kasahara limits restored and the P11-versus-P14 mouse direction claim removed
> (that this also removes the 9.5 claim is my inference from 9.7, not a statement of the original)

- 2026-11-18 and 2026-11-19: the sentence that the age series "straddles P11 and P14" is not a further requirement; the age series is fixed by its own rule (see "Ages").

> the age series straddling P11 and P14 already covers the cheap functional read of gradient maturity.
> the age series straddling P11 and P14 covers the cheap functional read.

### Bumetanide "suppressed the worsening" (superseded 2026-11-18)
- 2026-11-18: line 9.7 of the original, written after the Kasahara 2019 full text was read, weakened the statement of line 9.6; this text keeps only the surviving instruction to state the assay age.

> In a mouse febrile-seizure study, high-dose diazepam or pentobarbital worsened induction at P11 and not at P14, and bumetanide suppressed the worsening (abstract level; sedation is the authors' open rival),
> in 9.6 the sentence that bumetanide "suppressed the worsening" and the assay-age concern built on it are weakened

### The list of "not found" results with diazepam ontogeny (superseded 2026-11-18)
- 2026-11-18: line 9.5 of the original found diazepam ontogeny; the list was rewritten once (see "Sources and their levels").

> three of its "not found" results (lithium and GSK-3 inhibitors; systemic ketamine in mouse pups; mouse valproate) were confirmed by an independent route, the others not (Z944, TTA-A2, mibefradil, ICA-069673, XE991 in vivo, eliprodil, fenfluramine, diazepam ontogeny).
> it was found: diazepam is age-dependent

### Ages of the knockout (superseded 2026-11-19)
- 2026-11-19: the single working window was replaced by the table of documented ages (see "Ages").

> ADV's working window for the knockout is spontaneous seizures after about P12 and death by about 4 weeks (not re-verified here; to be confirmed by the laboratory from its own colony).

### Structure precedes seizure; the carrier latency "equal to the null" (withdrawn 2026-11-19)
- 2026-11-19: the dated correction to line 9.11 withdrew two sentences; this text carries only the corrected forms ("Timing limit" under "Ages" and add-ons (f) and (g)).

> Timing limit: structure precedes seizure. The germline null report (Cheng 2020) describes cortical thinning at E16.5 before any seizure, delayed neuronal maturation (DCX stays high), brain-wide apoptosis about five times control, cerebellar vermis fusion and holoprosencephaly-range findings with brain water unchanged.
> Every acute seizure-drug arm therefore acts on a brain that was already abnormal before seizures; a preventive or early arm cannot be read as a reversal, and the age at which each arm starts must be stated beside every effect.
> The same report gives a transcranial motor-evoked-potential latency in heterozygotes equal to the null with normal amplitude; this brief carries only the bursting incidence for heterozygotes.
> "brain-wide" was my word, not the paper's.
> The audit rows came from dossiers and manifests; I stated them as source facts before reading the sentences, which is the error.
> with an inconsistent n in the legend (8 slices from 5 animals for controls, 8 from 6 for the knockout),
> The audit-derived statements (timing limit, carrier latency, conduction, Olig2) come from dossiers and IT's confirmation; the corrected forms here are binding, and none is to be quoted as a source fact before the sentence is read in the source.

### Selective T-type blocker inside the stage 2 row, and "no dependency" on the slice experiment (2026-11-21)
- 2026-11-21: the T-type arm is optional and has its own row; the slice experiment shares no animals or predictions, but stage 4 is gated on it.

> a selective Cav3 (T-type) blocker arm beside it
> no shared animals, priors or dependency; the slice experiment comes first or in parallel

### The gene-addition benchmark lines (9.14 to 9.16; two statements withdrawn 2026-11-21)
- 2026-11-21: the rest of lines 9.14, 9.15 and 9.16 that is not withdrawn is kept below as detail. The correction to line 9.14 withdrew the survivor-against-non-survivor contrast and the statement about surviving lanes near 10 percent in the cerebellum, and line 9.16 limited the lean of line 9.15; the current sentences are in the section "Out of scope for this laboratory".

> In cortex and midbrain (the regions that carry the printed dose-response) no survivor lies near 6 percent of wild type (lowest 2.0 times wild type in cortex; 0.9 printed in midbrain, 0.56 against the mean of the wild-type lanes on that blot), and in those two regions every non-survivor lane lies below every survivor lane (n 4 against 4, one blot per region, no test, sampling age of the non-survivors unstated).
> The cerebellum is the caveat: surviving lanes near 10 percent exist there (two lanes), and the P180 high-dose lane at 0.1 is not resolved from its knockout lane on the same blot; the source does not say which region matters for survival.
> the survivor-against-non-survivor contrast and the statement about surviving lanes near 10 percent in the cerebellum are withdrawn from line 9.14 (the non-survivors were sampled younger than the survivors, three of four are low dose, and two low-dose lanes drawn as P90 survivors conflict with the survival curve and the main text).
> This is a provisional lean toward a platform effect, not a verdict, and it supersedes the open question of line 9.14 only as a lean.
> So the platform-low reading stands ONLY for regional protein and vector DNA at P30 (the benchmark's Figure 5; one reading of Voronin 2024); the neuron fraction at P17 to P19 is near cortex, and "the cerebellum is lowest" must not be read as "fewer cerebellar neurons transduced
> Westerns are ratios to a loading control, not molecules per cell; wild-type lanes on one blot differ two to three times.
> What stands, high-dose survivors only: cerebellum 0.6 and 0.6 at P90, 0.1 to 0.5 at P180 (the lowest lane equals the knockout lane of that blot), 1.4 (one mouse) and 2.15 (n 3, SD above the mean) at P300; midbrain lowest 1.3 (P180); cortex lowest 2.0 (P90). The cerebellum is the lowest region in the benchmark's high-dose mice at every age; whether that is the platform (regional reach of neonatal intracerebroventricular AAV9 with a neuronal promoter) or this paper is open, so the line reads: cerebellum lowest in this benchmark, cause open.
> expression-range line: the cerebellum is expected lowest (delivery-limited already at the vector-DNA level at P30 in the benchmark, where cerebellum over cortex is about 0.13 at low dose and 0.04 at high dose at protein level and about a tenth at vector-DNA level; one independent neonatal ICV AAV9 neuronal-promoter report points the same way, from one reading that the verifier could not reach and with an unresolved cortex-value mismatch). This is a provisional lean toward a platform effect, not a verdict, and it supersedes the open question of line 9.14 only as a lean. No change to the ataxia endpoint route; RP-037 unchanged. The kinetics gap: an expression time course from P5 to P20 is a missing measure (no source gives the age of first detection or of the plateau), and deaths between 17 and 30 days have no expression reading. Correction of an earlier statement that the benchmark has no blot before P90: it has P30 (its Figure 5: vector DNA, mRNA and protein per region; two readers agree on 32 numbers).
> Neuron fraction carrying the transgene, cerebellum over cortex 0.92 in both cohorts of one laboratory (P17: 51.7 against 55.9 percent; P19: 56.5 against 61.5 percent; n 3 mice; same programme as the benchmark, so not independent);
> Lukashchuk 2016 does not qualify, because each of its bars is relative to the CMV average of its own region.
> Three rivals for the gap, none measured: a lower per-cell level; loss between P19 and P30 by granule-cell division (prior art disease-models/wwox/analysis/cerebellardiscriminationexperiments20260922.md lines 162 to 164 and 376, single-copy host-reference qPCR on archived DNA, no new animals; consistent with, UNTESTED); and a wild-type denominator (cerebellumlayerlocalisation section 5: the wild-type cerebellum is highest in GTEx, so percent of wild type is lowered for the same transgene amount).

### The cold reading of the original (2026-11-18)
- 2026-11-18: a record of one cold reading of the first version; its fixes are in the body, and its remark about the "null" interval is kept in "Analysis plan".

> One cold reader (legend-delegate, sonnet medium requested; it received this file alone) reported 12 ambiguities, 7 inconsistencies, 6 claims stronger than their evidence and the decisions it would be forced to make.
> Fixed in this version: the blinding and allocation scheme (coded syringes, coded genotype, video scored by someone not present, unequal cells accepted); the number of ages in the wild-type age series; the definition of S (1-minute bins, maximum stage, deaths and rescued pups carried forward, with and without); the status definition; the interaction thresholds; the floor and zero-vehicle rule; the cluster method with few knockouts per litter; the criteria for "selective" T-type and "different class" GSK-3 agents; panel animals and shared vehicle; the motor pre-test for every arm; the order of hypotheses if the interaction cannot be sized; the interaction litter arithmetic; a required and optional list; the title, the priors-file timing and stage labels.
> Kept as the laboratory's decisions: doses, exposure times, route, stimulus, window if different, ages, humane endpoints, approvals, the mouse line.
> Not changed: the reader's remark that a "null" interval is hard to reach at the sample sizes in section 3 is true, and is why "unresolved" and "an effect of 0.7 or larger is excluded" exist; the claim that the repository holds the only in vivo drug data is now worded "that the repository holds".

### Dated lines folded without a superseded statement, with their dates
- 2026-11-18, line 9.1: the development-endpoint cohort; folded into "Optional, conditional cohort".
- 2026-11-18, line 9.2: one sentence removed for wording only; no change of content; dropped as wording only.

> one sentence in section 6 item 7 removed for wording; no change of content.

- 2026-11-18, lines 9.3 and 9.4: fixes already in the body of the original (agent names as examples only; treatment start age left to the laboratory; the dose check per age; coding of genotype; sessions and cells; grade categories; shared vehicle groups; multiplicity; the "general" definition); the dated lines are dropped, the body carries them.
- 2026-11-18, lines 9.6 and 9.8: the chloride-window paragraph and the note for any chloride-transport arm; folded into "Ages".
- 2026-11-19, line 9.9: main regimen, optional second regimen, lithium-alone arm; folded into "Regimens and dose checks" and the stage table.
- 2026-11-19, line 9.10: onset ages; folded into the table under "Ages".
- 2026-11-19, line 9.11: folded into "Ages" (timing limit) and add-ons (f) and (g), in corrected form only.
- 2026-11-19: glucose and deletion completeness (add-ons (d), (e)); Olig2 against Mbp (add-on (g)); the predictions file is frozen since 2026-11-18 and was never edited.
- 2026-11-19: after a blind check of the consolidated text, edits to the age, panel and sizing paragraphs (Kasahara limits restored; the "about 75 litters across the three knockout arms" clause restored with a pointer to the corrected figures).
- 2026-11-19: the one-slot order of the optional measurements (add-on (i)); dated lines on the age series and the glucose add-on that changed nothing in the brief; any new age is the laboratory's to decide.
- 2026-11-21, line 9.12 (the calcium add-on): folded into add-on (e2).
- 2026-11-21, line 9.13: folded into add-on (e3).
- 2026-11-22, ADV-170 (IT): dated line added to add-on (e3) (baseline PV-identified excitatory input as an optional state descriptor, evoked against spontaneous kept distinct); no arm, no gate, no design change.
- 2026-11-21, lines 9.14, 9.15 and 9.16: see "Out of scope for this laboratory" and the entry above.
- 2026-11-21, line 9.17: folded into add-on (e4).


### Markers replaced on 2026-11-21 (design-team group B)

The lines below were the open markers of this text before the design team's answers were integrated; they are kept as they stood.

- Marker C06: **CONFLICT-OPEN C06 (owner SCI): The rule that an interaction contrast needs twice the simple-effect number per cell, applied to the stated per-arm bracket of 36 to 109 animals, does not appear to give the stated per-cell bracket of 180 to 320 animals; the inputs of the per-cell figure are not given.**
- Marker C08: **CONFLICT-OPEN C08 (owner SCI): The vehicle group shared by the test arms is to be about twice the size of a test arm, while the planning totals give every cell the same n (about 300 animals at 11 per cell); the vehicle group of an age is also shared by the panel agents, not only by the test arms.**
- Marker Q32: **OPEN-GAP Q32 (owner SCI): Is the vehicle group made about twice a test arm in the 27-cell total of about 300 animals?**
- Marker C25: **CONFLICT-OPEN C25 (owner SCI): The sentence above says wild-type and heterozygous animals are not limiting, while the age series and the panel call for 21 wild-type cells, and the wild-type pups are taken to come from heterozygote crosses (expected 1:2:1) that give about 1.75 knockouts per litter; where the wild-type pups come from is not stated.**
- Marker Q45: **OPEN-GAP Q45 (owner SCI): Where do the wild-type pups of the age series and the panel come from (heterozygote crosses or wild-type breeders), and how many litters does that need?**
- Marker Q73: **OPEN-GAP Q73 (owner SCI): The outcomes table separates E1 from E3 through the interaction, which cannot be sized with the full-hour area summary; what descriptive pattern separates them when the interaction cannot be sized?**
- Marker Q82: **OPEN-GAP Q82 (owner SCI): Which rows of this table carry the lithium readings L1 and L2 (the older table does not label them)?**
- Marker CLAR-S: [Clarification by text work, for SCI to confirm: S is described once as the area under the grade against time over the window and once as the mean grade over 60 minutes; if both use the same per-minute grade series they differ only by a division by the length of the window, which the older texts do not say.]
- Marker CLAR-SERIES: [Clarification by text work, for SCI to confirm: the series contains ages on both sides of P11 and P14 only if the laboratory's assay age is low enough to allow it.]
- Marker CLAR-ORDER: [Clarification by text work, for SCI to confirm: this order is the order for the provoked-seizure design; the one-slot order of the optional measurements under "Optional add-ons" applies to the add-ons only.]
- Marker Q06: **OPEN-GAP Q06 (owner SCI): Is the predictions file supplied to the laboratory, and which definitions of this text does it override, given that it is said to govern any conflict?**
- Marker Q12: **OPEN-GAP Q12 (owner SCI): Is PTZ the provoking stimulus of this experiment, and by what route and schedule, or may the laboratory use another provoked-seizure assay (the lithium replication condition is defined against PTZ)?**
- Marker Q13: **OPEN-GAP Q13 (owner SCI): What PTZ dose, route and volume, and what intervals between the three injections, did Cheng 2020 use for the low-dose PTZ challenge that the lithium replication condition is anchored to?**
- Marker Q14: **OPEN-GAP Q14 (owner SCI): What is the ethosuximide regimen (dose, route, pretreatment interval, number of injections) for the main contrast?**
- Marker Q15: **OPEN-GAP Q15 (owner SCI): Should vehicle pups receive the same number, volume and timing of injections as the lithium arm, and is one shared vehicle valid across agents that may need different vehicles, routes and schedules?**
- Marker Q18: **OPEN-GAP Q18 (owner SCI): What are grades 0, 1, 2 and 6 of the scale, and is grade 6 death?**
- Marker Q19: **OPEN-GAP Q19 (owner SCI): Does the pilot include the panel agent and older ages, and which candidate assay ages are tested?**
- Marker Q20: **OPEN-GAP Q20 (owner SCI): What is a "stage-matched wild-type response" in the stage 1 stop rule, and may the stimulus differ by genotype to reach it?**
- Marker Q21: **OPEN-GAP Q21 (owner SCI): Is the same stimulus used at every age of the series, or re-fixed per age, and who fixes it for the older ages when the pilot is run at candidate assay ages?**
- Marker Q22: **OPEN-GAP Q22 (owner SCI): Which outcome is primary if the pilot shows that S is too variable (S or an incidence such as generalised seizures), who decides, and when?**
- Marker Q23: **OPEN-GAP Q23 (owner SCI): Which cells make up the first run (genotype by arm by age by exposure), as one list?**
- Marker Q31: **OPEN-GAP Q31 (owner SCI): Which n per cell should the laboratory plan for the first run, given that the figures 11, 22, 31, 36 to 109, 44, 50 and 180 to 320 are all stated with different bases?**
- Marker Q33: **OPEN-GAP Q33 (owner SCI): Do the litter figures (19, 25, 53, 75 and the bracket figures) refer to one drug against vehicle or to three knockout arms, and which single figure is the one for a breeding plan?**
- Marker Q34: **OPEN-GAP Q34 (owner SCI): How many pups and litters does the pilot alone need, given "n of 6 to 8 per cell" and unspecified candidate ages and cells?**
- Marker Q37: **OPEN-GAP Q37 (owner SCI): Which ages are the candidate assay ages, and up to what age can knockouts still be tested, given death at about three to four weeks for knockouts in general and by about day 17 in the comparator's panel?**
- Marker Q42: **OPEN-GAP Q42 (owner SCI): Which Wwox-null allele, background strain and source or repository does the laboratory need, and is it the global knockout of Cheng 2020?**
- Marker Q43: **OPEN-GAP Q43 (owner SCI): How, at what age and with what turnaround is genotype determined before the test and before allocation?**
- Marker Q61: **OPEN-GAP Q61 (owner SCI): What triggers a rescue, what is the rescue procedure, and may a rescue drug be used given that it could confound the arm effect?**
- Marker Q62: **OPEN-GAP Q62 (owner SCI): Is death an accepted outcome in vehicle and treated groups, and what death or status rate is expected per arm (only "about half of PTZ-injected knockouts reached status" is given)?**
- Marker Q67: **OPEN-GAP Q67 (owner SCI): What numerical rule declares the panel valid at an age?**
- Marker Q68: **OPEN-GAP Q68 (owner SCI): What numerical value of vehicle S counts as "at the floor"?**
- Marker QA1: **OPEN-GAP QA1 (owner SCI): Which lithium salt, vehicle and route are used in the replication condition, and are the three injections evenly spaced within the hour?**
- Marker QA2: **OPEN-GAP QA2 (owner SCI): What feeding and thermal state, and what time of day, should pups be in during the 60-minute observation (blood glucose is low in null pups by about P14)?**
- Marker QA3: **OPEN-GAP QA3 (owner SCI): Must the laboratory adopt the 0 to 6 scale as defined here, or may it use its own validated scale and map it to this one?**
- Marker QA4: **OPEN-GAP QA4 (owner SCI): Are pilot animals and pilot data reused in the main analysis, and who signs off the pilot's choice of age, stimulus and summary before the main run starts?**
- Marker QA5: **OPEN-GAP QA5 (owner SCI): Does a stop rule (the pilot, or a panel that is invalid at the assay age) end only that stage or the whole experiment, and who is informed?**


### Markers and sentences replaced on 2026-11-21 (design-team group C)

The lines below were the open markers, notes and sentences of this text before the design team's second set of answers was integrated; they are kept as they stood.

- Ages, rule sentence of the wild-type series: Which ages the series contains is fixed by this rule (the assay age and at least two older ages); the earlier remark that the series "straddles P11 and P14" is not a further requirement (it is in the History).
- Note CLAR-SERIES (superseded): [Design-team answer CLAR-SERIES, 2026-11-21; status: corrected by the design team. Not only 'if the assay age is low enough': the series (assay age plus at least two older ages to about P28) straddles P11 and P14 when the assay age is at or below P11; when the assay age is P14 or later P11 is not an older age and is added as a further age (seven more wild-type cells). Minimum three ages if the assay age is at or below P11, four if above.]
- Marker R3C02: **CONFLICT-OPEN R3C02 (owner SCI): The note above adds P11 as a further series age when the assay age is P14 or later, while the rule sentence in Ages says the straddle of P11 and P14 is not a further requirement; the rule sentence was not changed.**
- Note Q19, pilot ages: and uses the ages the brief already names: P11 and P14; knockout feasible ages are bounded above by the earlier of the two documented death statements. A third later age depends on the laboratory's colony survival.
- Marker R3C04: **CONFLICT-OPEN R3C04 (owner SCI): The note above takes the pilot ages to be P11 and P14, while another note takes the working window to be P12 to P17 with P11 only as the chloride-window probe; the pilot ages are not fixed.**
- Status box, sentence on numbers: no number in this text is new. Each number appears as in the older texts;
- Note Q15, Cheng regimen specifics: The two Cheng regimens differ in schedule (lithium three injections within one hour; ethosuximide one injection 45 minutes before PTZ, both in saline, Methods), so a single vehicle group
- Marker Q84: **OPEN-GAP Q84 (owner SCI): Are "P5" and "P8", used in the predictions file and in the table above and in the cohort condition below, labels of sets of predictions and not postnatal days?**
- Table of seizure types, P8: as the predictions file defines "generalised" for P8
- Table of outcomes, P5: (as in the predictions file, E1, E3 and P5)
- Condition for the development cohort, P5: (set P5 of the predictions file:
- Planning, Cheng group sizes: Cheng 2020 used 6 to 7 knockout and 12 to 20 wild-type or heterozygous pups per group;
- Stage 1 row, Cheng scale: (n of 6 to 8 per cell is the Cheng 2020 scale)
- S08 area under the stage: 'area under the stage against time' replaced by 'area under the grade against time' on 1 note line(s)
- S08 stage 6: 'stage 6 IS death' replaced by 'grade 6 IS death' on 1 note line(s)
- S08 stage units: 'stage units' replaced by 'grade units' on 1 note line(s)
- S08 stage-matched response (notes): 'stage-matched wild-type response' replaced by 'wild-type response that is not at the floor' on 2 note line(s)
- Stage 1 row, stage-matched response: cannot be tested at a stage-matched wild-type response
- Marker Q51: **OPEN-GAP Q51 (owner SCI): How is latency defined for each seizure type (from which injection, first minute reaching which grade)?**
- Marker R3C01: **CONFLICT-OPEN R3C01 (owner SCI): The replication condition is the published low-dose stimulus, at which wild type sat near the floor, while a stimulus with a non-floor wild-type response is required for the contrast; the text does not say which wins.**
- Marker R3C05: **CONFLICT-OPEN R3C05 (owner SCI): Outcome E2 is defined by a wild-type floor, while the floor rule says R is not computed and the arm is not interpretable at the floor.**
- Outcomes list, E2: - (E2) age-limited, with a wild-type floor (
- Outcomes table, E2 row: | Ethosuximide | R(+/+) null at the assay age, an effect at the older age (E2) | age-limited with a wild-type floor; the Cheng 2020 pattern is not knockout selectivity |
- Marker R3C09: **CONFLICT-OPEN R3C09 (owner SCI): The sentence above cites 75 litters as a figure of the sections above, but the sample-size table carries 75 only as a derived figure (3 x 44) and, in the History, as a superseded one.**
- Planning scale paragraph, 75 litters: (19 and 53 litters; 75 litters; the dose-check totals) are the optimistic scale and should be read with the 36 to 109 bracket.
- Marker R3C10: **CONFLICT-OPEN R3C10 (owner SCI): A panel that fails is an assay failure, but the rule above also leaves an age unresolved when the flat-profile agent gives neither a null nor an effect; what is done with an unresolved panel age is not stated.**
- Marker R3Q37: **OPEN-GAP R3Q37 (owner SCI): Which single figure of animals and litters is to go into an application, given the planning totals of this section?**


### Conflict markers and sentences replaced on 2026-11-21 (classification of the 13 open conflicts)

The lines below were the conflict markers and sentences of this text before the 13 conflicts left open by the design team's second set of answers were classified: six were repaired in the text, seven became named decisions. They are kept as they stood.

- Sentence (C23, wild-type grade about 1): wild-type grade is about 1 on 0 to 6, close to the floor, that is, so low that a reduction cannot be seen)
- Marker C23: **CONFLICT-OPEN C23 (owner SCI): One passage says wild-type stage is about 1 on 0 to 6, close to the floor, while another gives a mean S of 0.27 to 0.41 for wild-type and heterozygous pups at that stimulus (CV above 1.4), without saying whether each is a peak curve value or a 60-minute mean.**
- Sentence (C03, one family): The design team's literature table holds acute pro-convulsant and chronic threshold-raising results in one mouse PTZ paper family.
- Marker C03: **CONFLICT-OPEN C03 (owner SCI): One item says no regimen in the sources shows a clear sign flip against PTZ and, in the same item, that one mouse PTZ paper family holds an acute pro-convulsant and a chronic threshold-raising result; what the family shows, at what level, and why it is not counted as a sign flip is not stated.**
- Sentence (C02, second regimen): A second regimen is an optional comparator arm (a single injection, PTZ about 30 minutes later), not a design variable of the main contrast.
- Marker C02: **CONFLICT-OPEN C02 (owner SCI): The scope paragraph says this text offers no schedule of its own (the only regimen mentioned being the one stated in Cheng 2020), while the optional second regimen is described as a single injection with PTZ about 30 minutes later without saying whose schedule that is or whether it comes from a source.**
- Sentence (C16, heterozygote bursting incidence): This brief carries only the heterozygote bursting incidence.
- Marker C16: **CONFLICT-OPEN C16 (owner SCI): The last sentence of add-on (f) says this brief carries only the heterozygote bursting incidence, but no heterozygote bursting incidence appears anywhere in the older texts.**
- Marker R2C05: **CONFLICT-OPEN R2C05 (owner SCI): Grade 4 is described without a tonic phase while generalised seizures are grades 4 to 5 with a tonic phase; which grade 4 counts as generalised is not stated.**
- Marker C32: **CONFLICT-OPEN C32 (owner SCI): The calcium add-on (e2) is placed alongside GFAP and Iba1 scoring at P5 to P9, but no such scoring is planned in this design (GFAP appears only in the optional development cohort).**
- Marker C09: **CONFLICT-OPEN C09 (owner SCI): The stage 1 row lists knockout and wild-type vehicle pups only, while its stop rule ("if the panel agent has no effect at any age") and the dose-check decision ("if the lower exposure is effective in the panel agent at an age") need pups given the panel agent.**
- Marker C30: **CONFLICT-OPEN C30 (owner SCI): The human-side line (e4) speaks of calcium and parathyroid hormone and of a lipid statement, but neither parathyroid hormone nor lipid is in the measurement list of the calcium add-on (e2); which of them the add-on measures is not stated.**
- Marker C31: **CONFLICT-OPEN C31 (owner SCI): The glucose series (e) and the calcium add-on (e2) overlap with different measurement lists (glucose, ketone and lactate by age, milk intake or stomach filling against serum total calcium with albumin or ionised calcium, glucose, body weight and a milk-spot score) and different sampling ages (P7 to P14 against P7, P9, P11 and P14).**
- Marker C35: **CONFLICT-OPEN C35 (owner SCI): The multiplicity statement counts five comparisons (95% and 99%, Bonferroni for five), which matches the arm list of the design frame but not the later additions (a lithium-alone arm, an optional second regimen, panel agents at two exposures each).**
- Marker R2C01: **CONFLICT-OPEN R2C01 (owner SCI): The values 0.7 and 1.43 belong to both classes of the thresholds table (genotype specificity: at most 0.7 or at least 1.43; no genotype specificity: 0.7 to 1.43), so a ratio of exactly 0.7 or 1.43 is not classified.**
- Marker R2C09: **CONFLICT-OPEN R2C09 (owner SCI): The ethosuximide comparison is the pre-specified primary, judged at 95%, in one place and is listed as descriptive ratios with intervals in another.**
- Marker R2C10: **CONFLICT-OPEN R2C10 (owner SCI): The condition for the optional cohort, an interaction outside 0.7 to 1.43, also admits a smaller knockout effect, which the outcomes table does not call knockout-enhanced.**
- Sentence (Table row, pointer to C23): | same quantification; see CONFLICT-OPEN C23 above |
- Sentence (Scope sentence, pointer to the second regimen): (See also the CONFLICT-OPEN note on the second lithium regimen, under "Regimens and dose checks".)


### Decision markers and sentences replaced on 2026-11-21 (design-team decisions D01 to D07)

The lines below were the named decisions and sentences of this text before the design team's seven decisions were integrated; they are kept as they stood.

- Marker C09: **OPEN-GAP C09 (owner SCI): DECISION (design science): which pups the pilot carries. The pilot note gives two ages of knockout vehicle, wild-type vehicle and the flat-profile panel agent at one exposure (36 to 48 animals); the stage 1 row lists vehicle pups only; the pilot's stop rule needs the panel agent; the dose-check decision ("if the lower exposure is effective in the panel agent at an age") needs the panel agent at two exposures. Options in the documents: (1) the panel agent at one exposure in the pilot, and the dose check in stage 2; (2) the panel agent at two exposures in the pilot (more wild-type cells than the pilot note counts); (3) vehicle pups only, as the stage 1 row says, with the panel stop rule and the dose check moved to stage 2.**
- Sentence (Stage 1 row, panel cell): | 1 pilot | knockout and wild-type vehicle pups at candidate assay ages;
- Marker C30: **OPEN-GAP C30 (owner SCI): DECISION (design science): whether the add-on (e2) also measures parathyroid hormone and lipids. The human-side line (e4) says that neither is named in any human report read and that this strengthens the add-on measurement; the list of (e2) is serum total calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot score. Options: (1) add parathyroid hormone and a lipid measure to (e2), with the blood volume of a P7 pup addressed (the open question on the add-ons); (2) keep the list of (e2) as written and read (e4) as context only.**
- Marker C31: **OPEN-GAP C31 (owner SCI): DECISION (design science): whether the glucose series (e) and the calcium add-on (e2) are one add-on or two. (e) lists glucose, ketone and lactate by age, and milk intake or stomach filling, at P7 to P14; (e2) lists serum total calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot score at P7, P9, P11 and P14. Options: (1) one combined add-on with the union of the lists at P7, P9, P11 and P14; (2) two add-ons, each with its own list and ages, with glucose and the feeding read taken once. This is the same decision as the open question on serial or separate cohorts.**
- Marker Q57: **OPEN-GAP Q57 (owner SCI): Are (e) and (e2) one add-on or two, and are the measures taken serially in the same pups at P7, P9, P11 and P14 or in separate cohorts, with the blood volume at P7 addressed?**
- Sentence (Multiplicity bullet): - **Shared vehicle and multiplicity.** Where five test arms share one vehicle group per genotype, the vehicle group is made about twice the size of a test arm (the square-root rule, for five arms), and the intervals of the five comparisons are reported at 95% and at 99% (Bonferroni for five). The ethosuximide comparison is the pre-specified primary and is judged at 95%; every other "effect" counts as confirmed only if it holds at 99%.
- Marker C35: **OPEN-GAP C35 (owner SCI): DECISION (design science): how many comparisons the multiplicity statement counts. It counts five test arms sharing one vehicle group per genotype (95% and 99%, Bonferroni for five; vehicle about twice a test arm). The text later adds a lithium-alone arm, an optional second regimen, the optional T-type arm, a second GSK-3 inhibitor, a comparator drug and panel agents at two exposures each. Options: (1) keep five and treat every added arm as outside the family (exploratory, reported at 95% only); (2) recount the family over the arms that share a vehicle group in a session, and state the count and the Bonferroni divisor before data.**
- Marker Q70: **OPEN-GAP Q70 (owner SCI): How many comparisons enter the Bonferroni correction once the lithium-alone arm, a second regimen and the panel agents at two exposures each exist?**
- Marker R2C01: **OPEN-GAP R2C01 (owner SCI): DECISION (design science): the boundary rule for an interaction ratio of exactly 0.7 or 1.43. The thresholds table says "genotype specificity: at most 0.7 or at least 1.43" and "no genotype specificity: 0.7 to 1.43"; prediction P5 of the in vivo priors file and the cohort condition say "outside 0.7 to 1.43" (the endpoints inside the null band). Options: (1) the endpoints belong to the specificity class (as "at most" and "at least"); (2) the endpoints belong to the no-specificity band (as "outside 0.7 to 1.43").**
- Sentence (Thresholds table, no-specificity row): | no genotype specificity (interaction ratio) | 0.7 to 1.43 (as in the in vivo priors file, E1, E3 and its prediction P5) |
- Sentence (Outcomes table, L1 row): lithium effect in all genotypes (interaction between 0.7 and 1.43); second GSK-3 inhibitor effect;
- Sentence (Note Q82, quoted row): the row 'lithium effect in all genotypes (interaction 0.7 to 1.43); second GSK-3 inhibitor effect;
- Sentence (Note Q73, band): the point estimate of the interaction ratio lies in 0.7 to 1.43.
- Marker R2C09: **OPEN-GAP R2C09 (owner SCI): DECISION (design science): which comparison is the single pre-specified primary. One passage says the ethosuximide comparison is the pre-specified primary, judged at 95%; the order of hypotheses lists the ethosuximide effect ratios in the knockout and in the wild type, at the assay age and at the older ages, as descriptive ratios with their intervals, and the interaction as exploratory unless sized. Options (readings of those lists): (1) the knockout ethosuximide ratio at the assay age is the primary, judged at 95%, and every other ratio is descriptive; (2) the knockout and wild-type ratios at the assay age are the primary, the older ages descriptive; (3) no comparison is a confirmatory primary: all ratios are descriptive and the multiplicity statement says so.**
- Sentence (Order of hypotheses, (ii)): as descriptive ratios with their intervals; (iii)
- Marker R2C10: **OPEN-GAP R2C10 (owner SCI): DECISION (design science): whether the condition for the optional development cohort is one-sided. As written it is "interaction outside 0.7 to 1.43" (prediction P5 of the in vivo priors file), which admits a larger knockout effect (ratio at most 0.7) and a smaller one (ratio at least 1.43); the outcomes table calls only the larger one knockout-enhanced. Options: (1) keep P5 as written (two-sided; the priors file is frozen) and state what a smaller knockout effect means for the cohort; (2) make the cohort condition one-sided (ratio at most 0.7, reproduced by the second GSK-3 inhibitor of another class) and say that P5 is then wider than the condition.**
- Sentence (Cohort condition): (prediction P5 of the in vivo priors file: interaction outside 0.7 to 1.43, and the second GSK-3 inhibitor reproducing it while the non-GSK-3 comparator drug does not)
- **Pup sizing and timing (IT 2026-11-28, ADV-311 and ADV-310; superseded text kept).** Before this date the body said that a litter yields about 1.75 knockouts (25 percent of 7) and carried litter counts computed from it (for example 19, 25, 53 and 75 litters), and said that of the structural findings only the E16.5 cortical thinning precedes seizure onset and that the paper states no causal sequence. Cheng 2020 (supplement, page 3) reports Wwox-/- at 5.1 percent (N = 177, WD1) and 6.5 percent (N = 785, WD234) of genotyped pups at postnatal day 5 to 12 from heterozygote intercrosses, so the body now gives the 1.75 figures as an assumed case beside figures derived from that frequency (rounded up); Ludes-Meyers 2009 Table 1 (30 knockouts of 154, day 3, a different line) is the Mendelian contrast and leaves line or background versus loss before genotyping undetermined. One blind round changed seven of 23 fragments before they were applied. Two optional blind-reader points were not applied (T02, T05, T07, T08, T17, T21 wording; and the optional registered missing observation of ADV-311 Y5).

## Out of scope for this laboratory

The following lines of the original concern a gene-addition benchmark paper (a gene-therapy reference), not this provoked-seizure design, which contains no partial-restoration, gene-addition or vector arm. Each has one current sentence; the rest is in the History.

- **Regional expression range (line 9.14, as corrected).** The cerebellum is the lowest region in the benchmark's high-dose mice at every age; whether that is the platform (regional reach of neonatal intracerebroventricular AAV9 with a neuronal promoter) or this paper is open: cerebellum lowest in this benchmark, cause open. Any partial-restoration readout in a design that has one should report the region.
- **Expression-range lean (line 9.15; provisional, one reading).** The cerebellum is expected lowest, delivery-limited already at the vector-DNA level at P30 in the benchmark; this is a provisional lean toward a platform effect, not a verdict, and the kinetics gap (an expression time course from P5 to P20) is a missing measure.
- **Scope of the lean (line 9.16).** The platform-low reading stands only for regional protein and vector DNA at P30 (the benchmark's Figure 5; one reading of Voronin 2024); the neuron fraction at P17 to P19 is near cortex, and "the cerebellum is lowest" must not be read as "fewer cerebellar neurons transduced"; cerebellum lowest in this benchmark, cause open.
