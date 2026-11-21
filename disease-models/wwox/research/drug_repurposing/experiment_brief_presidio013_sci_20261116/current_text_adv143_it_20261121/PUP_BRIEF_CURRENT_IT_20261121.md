# Pup brief, current text: a first provoked-seizure experiment in the Wwox-null pup, to separate the readings of ethosuximide (E1 to E3; E4 no effect and E5 not interpretable are the other outcomes) and of lithium (L1 general, L2 GSK-3-specific)

<!-- STATUS-BOX -->
**STATUS: THIS TEXT GOVERNS. Version and date: 2026-11-21.**

- This is the one current text of this experiment brief. It replaces, for reading, the two older texts: the consolidated brief dated 2026-11-19 and the original brief dated 2026-11-18 with the dated lines appended to it (the last dated 2026-11-21).
- Where this text and an older text differ, this text is the one to follow. Where two older statements disagreed and one was later or more specific, this text follows that one, and the other is kept in the History.
- The older texts are kept unchanged in the repository. Every statement that this text supersedes is kept, word for word, in the section "History (old text kept)" at the end, with its date and the statement that replaced it. The History also names apart the two different things that the older texts both called "9.12": the dated correction of line 9.11, and the calcium add-on line of 2026-11-21. The body of this text does not use that number.
- Markers in the text. **OPEN-GAP** marks a question that cannot be answered by text work: a value or a decision is missing, no value has been invented, and the owner is named (SCI is the design team that wrote this brief; operator is the coordinator of this collaboration; laboratory is the collaborating laboratory). **CONFLICT-OPEN** marks a sentence where two statements of the older texts disagree and the design team has not decided between them; both statements stay in place. **[Clarification by text work, for SCI to confirm: ...]** marks a reading that this text supplies and the design team must confirm.
- No number in this text is new. Each number appears as in the older texts; where the older texts gave different figures for the same thing, both stay, each with its basis. Sections are named, not numbered, so that a reference cannot be confused with the numbering of the older texts.
- The contact route for questions to the design team and the terms of the collaboration are not named in this text: see "Logistics, terms and contact".
<!-- STATUS-BOX -->

Sections, in order: Scope and limits; The question; What this experiment cannot show; What is fixed here and what the laboratory decides; Animals; Stimulus, seizure grades and observation; Ages; Groups to run (stages and the assay-validation panel); Regimens and dose checks; Analysis plan; Sample size and animals needed; Welfare and stopping; What each outcome would favour; Optional add-ons; Optional, conditional cohort; Logistics, terms and contact; Sources and their levels; History (old text kept); Out of scope for this laboratory.

In this text "grade" always means a step of the 0 to 6 seizure scale, and "stage" always means a step of the experimental plan (stages 0 to 4).

## Scope and limits

**Hypothesis level.** Written for a collaborating laboratory that reads this cold. Class labels; no agent is named as a use except as an illustrative reference; no dose; no schedule of our own (the only regimen mentioned is the one stated in Cheng 2020, as the replication condition); no recommendation for or against any use of any agent in any person. Reference genotype class only (a WWOX-related developmental and epileptic encephalopathy genotype class); no individual-level record was used or sought. Not medical advice. NOT a WWOX result: every statement about what an outcome would mean is a hypothesis to be tested. The laboratory chooses its doses, exposure times and stimulus within its own published standard assay and states them before data.

Ethosuximide and lithium are the two agents under test (they are the agents of the one published experiment that this design follows up). Every other agent name in this text is an example from the rodent literature and is not proposed for any use. (See also the CONFLICT-OPEN note on the second lithium regimen, under "Regimens and dose checks".)

Each statement is no stronger than its evidence level, which is given beside it or under "Sources and their levels" (full text read; abstract only; second-hand; read by eye from a figure; hypothesis).

Predictions for the outcome classes were fixed in a predictions file before the original brief was written. Its checksum is sha256 `326846fb5180a9355d4d462217bc83a97bf653054d24ae5dcd6344bde497122e`, and the file was not edited afterwards. Where this text is more specific than the predictions file (the definitions under "Stimulus, seizure grades and observation"), this text adds detail and the predictions file governs any conflict. The weights in it are subjective, not validated probabilities, and are scored literally when data exist. A different predictions file (sha256 `3c567acddf10244602c4536d3153f134cab4eba0690321290edd23772b7d8be0`) belongs to a different experiment (a brain-slice experiment) and is not used here.

**OPEN-GAP R2Q82 (owner operator): Does the laboratory receive the older texts, the operator note and the predictions file, and where are they kept?**

**OPEN-GAP Q06 (owner SCI): Is the predictions file supplied to the laboratory, and which definitions of this text does it override, given that it is said to govern any conflict?**

## The question

In Wwox-null pups, are the seizure-suppressing effects reported for ethosuximide and for lithium specific to the knockout, or are they the same proportional effect any anticonvulsant of that kind would have in a pup of that age, and does lithium act through GSK-3 (glycogen synthase kinase 3)?

**Why this question.** The only in vivo drug data in a Wwox-null animal that the design team holds are one experiment (Cheng 2020, PMID 32000863, global knockout, "preweaning" pups, pentylenetetrazol (PTZ)-provoked seizures scored 0 to 6, one laboratory): lithium lowered the seizure grade in all three genotypes; ethosuximide lowered it in the knockout and was not significant in wild-type and heterozygous pups. **No genotype-by-treatment test was reported or can be computed from the figures** (mean ± SEM curves, one-way ANOVA; no per-animal values; the test age is not stated; the knockout PTZ-alone curves of the two drug panels differ in height by eye, so different cohorts appear to have been used; wild-type grade is about 1 on 0 to 6, close to the floor, that is, so low that a reduction cannot be seen). A claim of knockout selectivity rests on a difference in significance. By eye the proportional reduction by lithium looks similar in the three genotypes (an eye reading of the published image), which fits a general or regimen effect better than a knockout-enhanced one.

**CONFLICT-OPEN C23 (owner SCI): One passage says wild-type stage is about 1 on 0 to 6, close to the floor, while another gives a mean S of 0.27 to 0.41 for wild-type and heterozygous pups at that stimulus (CV above 1.4), without saying whether each is a peak curve value or a 60-minute mean.**

**Readings to separate for ethosuximide.**
- (E1) knockout-selective.
- (E2) age-limited, with a wild-type floor (rat pups lose the PTZ effect of ethosuximide below about 25 days in abstracts from one Prague laboratory family; the mouse ontogeny was not found by two routes; one mouse pup datum exists for a different seizure type, Cortez 2004, PMID 15582027, abstract only).
- (E3) a general anticonvulsant effect, proportional in every genotype.
- (E4) no effect; (E5) not interpretable. These are the two other outcomes.

**OPEN-GAP Q81 (owner SCI): What exactly is outcome E5 ("not interpretable") and how does it differ from E4 ("no effect"), since E5 is named only in the title?**

**Readings to separate for lithium.** (L1) general, against (L2) specific to GSK-3 in the knockout. The inhibitory phosphorylation of GSK-3beta at serine 9 (p-Ser9) is lower in untreated knockout brain (Cheng 2020 Fig. 7c, one representative blot per region); lithium engagement was not measured; lithium has other targets.

**Sizing flag, read this first.** An eye reading of the knockout PTZ-alone curve of Cheng 2020 Fig. 7b, and a later quantification of Fig. 7b and 7d, show a between-animal variability of the full-hour summary that is large. At that variability a simple effect needs many animals per arm, and the genotype-by-treatment interaction is out of reach with that summary. The figures are in one table under "Sample size and animals needed". The brief plans a pilot first and promises no interaction test.

## What this experiment cannot show

**Cannot show:** whether any drug would help spontaneous seizures (spontaneous-seizure burden: there is no video-EEG in the basic design); whether a drug works after seizures start (acute rescue after seizure onset: all arms are pretreatment before a provoked seizure); how a drug works (any mechanism readout); development or survival effects; any statement about people. A provoked-seizure result in a pup says what a drug does to a PTZ seizure at that age, not what it would do to the null phenotype.

**Not attemptable as designed:** a test of "different between genotypes" on the full-hour area summary is **not attemptable** at the published variability, unless the pilot finds a far less variable stimulus or summary (for example the incidence of generalised seizures).

**What may not be ready:** whether any laboratory has the line and the capacity is unknown. Knockout pups are scarce (about one in four from a heterozygote cross) and fragile.

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

**OPEN-GAP Q42 (owner SCI): Which Wwox-null allele, background strain and source or repository does the laboratory need, and is it the global knockout of Cheng 2020?**

**OPEN-GAP Q43 (owner SCI): How, at what age and with what turnaround is genotype determined before the test and before allocation?**

**OPEN-GAP Q44 (owner laboratory): Who holds which code (genotype reader, syringe coder, injector), and may one person hold more than one?**

**OPEN-GAP Q45 (owner SCI): Where do the wild-type pups of the age series and the panel come from (heterozygote crosses or wild-type breeders), and how many litters does that need?**

**OPEN-GAP Q46 (owner SCI): How are knockouts allocated within genotype and litter when a litter yields about 1.75 knockouts?**

**OPEN-GAP Q26 (owner SCI): Which nine genotype-by-arm cells are meant by "all nine genotype-by-arm cells"?**

**OPEN-GAP Q41 (owner laboratory): Which postnatal-day counting convention and which tolerance define "the same postnatal age" in a session, given that cells are filled across litters born on different days?**

**OPEN-GAP Q48 (owner SCI): Is each pup used once only, and are litters standardised or cross-fostered?**

## Stimulus, seizure grades and observation

**Stimulus.** A stimulus that gives wild-type pups a measurable non-floor response, fixed in a pilot (otherwise a wild-type null cannot be told from a floor). The stimulus is the laboratory's own published standard assay; no number is proposed. In the one published experiment the provoking agent was PTZ.

**OPEN-GAP Q12 (owner SCI): Is PTZ the provoking stimulus of this experiment, and by what route and schedule, or may the laboratory use another provoked-seizure assay (the lithium replication condition is defined against PTZ)?**

**OPEN-GAP QA3 (owner SCI): Must the laboratory adopt the 0 to 6 scale as defined here, or may it use its own validated scale and map it to this one?**

**OPEN-GAP QA2 (owner SCI): What feeding and thermal state, and what time of day, should pups be in during the 60-minute observation (blood glucose is low in null pups by about P14)?**

**Seizure grades.**

| Grade or class | What the older texts say |
|---|---|
| 1 to 2 | minimal seizures; the behaviour of grades 0, 1 and 2 is not defined |
| 3 | unilateral forelimb clonus with myoclonic jerk: intermediate, its own category, reported and included in S |
| 4 without a tonic phase | bilateral clonus, reported on its own line |
| 5 | loss of righting, tonic-clonic; reported separately inside the generalised count |
| 4 to 5 with a tonic phase | generalised seizures, as the predictions file defines "generalised" for P8 |
| 6 | a pup that dies keeps grade 6 for the rest of the window; whether grade 6 is death is not stated |
| status | three or more tonic-clonic seizures within the window (the Cheng 2020 definition) |

**OPEN-GAP Q18 (owner SCI): What are grades 0, 1, 2 and 6 of the scale, and is grade 6 death?**

**OPEN-GAP Q84 (owner SCI): Are "P5" and "P8", used in the predictions file and in the table above and in the cohort condition below, labels of sets of predictions and not postnatal days?**

**OPEN-GAP Q52 (owner SCI): How are "three or more tonic-clonic seizures within the window" counted (what separates events, and is grade 5 the same as tonic-clonic), given that the status rule also triggers the rescue rule?**

**Outcomes per animal, not only a mean grade.**
- (a) **S** = area under the grade against time over a **60-minute window (as in Cheng 2020; any other window is stated before data)**, the grade assigned per 1-minute bin as the maximum grade in that bin; **a pup that dies keeps grade 6 for the rest of the window, and a pup rescued under the status stopping rule keeps its last grade carried forward to the end of the window; both are flagged, and the results are reported with and without them** (primary).
- (b) **Seizure type:** incidence and latency of minimal seizures (grades 1 to 2), **intermediate seizures (grade 3, its own category, reported and included in S)**, generalised seizures (**grades 4 to 5 with a tonic phase; grade 4 without a tonic phase is reported on its own line, and grade 5 is reported separately inside the generalised count**) and **status** (three or more tonic-clonic seizures within the window).

**CONFLICT-OPEN R2C05 (owner SCI): Grade 4 is described without a tonic phase while generalised seizures are grades 4 to 5 with a tonic phase; which grade 4 counts as generalised is not stated.**
- Reason: in rat pups several agents suppress generalised seizures while **raising minimal seizures** (MK-801 at P12, memantine, phenobarbital at P7 and P12, carbamazepine at P7 and P12), and wild-type pups sit at minimal-seizure level, so a mean grade can cancel two opposite effects.

[Clarification by text work, for SCI to confirm: S is described once as the area under the grade against time over the window and once as the mean grade over 60 minutes; if both use the same per-minute grade series they differ only by a division by the length of the window, which the older texts do not say.]

**OPEN-GAP Q49 (owner SCI): In what units is S, and is the area, the sum or the mean grade the primary summary?**

**OPEN-GAP Q50 (owner SCI): In item (a) above, what is primary: S, or the reporting with and without deaths and rescued pups?**

**OPEN-GAP Q51 (owner SCI): How is latency defined for each seizure type (from which injection, first minute reaching which grade)?**

**OPEN-GAP Q22 (owner SCI): Which outcome is primary if the pilot shows that S is too variable (S or an incidence such as generalised seizures), who decides, and when?**

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

**OPEN-GAP Q37 (owner SCI): Which ages are the candidate assay ages, and up to what age can knockouts still be tested, given death at about three to four weeks for knockouts in general and by about day 17 in the comparator's panel?**

**Wild-type age series** (no null animal needed): wild-type pups, same stimulus and scale, at the assay age and at **at least two older ages up to about P28**, spaced by the laboratory, vehicle against each test agent; knockouts are tested at the assay age only (they cannot be matched at older ages). Purpose: to see whether a wild-type non-response is age. Which ages the series contains is fixed by this rule (the assay age and at least two older ages); the earlier remark that the series "straddles P11 and P14" is not a further requirement (it is in the History).

[Clarification by text work, for SCI to confirm: the series contains ages on both sides of P11 and P14 only if the laboratory's assay age is low enough to allow it.]

**OPEN-GAP Q21 (owner SCI): Is the same stimulus used at every age of the series, or re-fixed per age, and who fixes it for the older ages when the pilot is run at candidate assay ages?**

**Timing limit: state the age and the structural state beside every effect.** In the germline null report, of the structural findings **only the E16.5 cortical thinning precedes seizure onset** (seizures "commonly observed after postnatal day 12"). The doublecortin increase is at P14 (n = 5), brain-size and weight reduction at P20, and the apoptosis ratio (about five times control) and the cerebellar vermis fusion are at about P19 to P20 (one reading of the source, not re-checked), so these are concurrent with or after seizure onset. The paper states no causal sequence, and "brain-wide" is not its word. A preventive or early arm cannot be read as a reversal in respect of the E16.5 finding only.

**State the chosen age against the chloride-gradient window** (the developmental period over which the neuronal chloride gradient matures; E_GABA is the GABA reversal potential). No Wwox system has a measured E_GABA. The one mouse study that suggested a P11 to P14 window (Kasahara 2019, full text read, groups of 4 to 5) is confounded: clonic incidence at P11 was not raised (5 of 5 in saline); the worsening is in latency, threshold temperature and LFP (local field potential) events; bumetanide (a blocker of the chloride importer NKCC1) did not block the latency effect and alone lowered incidence; there were 5 of 5 deaths on high-dose diazepam at both ages; and body temperature was near normal in the co-treatment arms. No other source supports a P11 to P14 chloride window (slice and in vivo data put the switch earlier, with region caveats). An NKCC1-blocker arm is **not** proposed (no brain-engagement control, narrow pup age effect, ototoxicity and diuresis signals in neonatal trials).

**The one mouse datum, febrile-seizure induction worsened at P11 and not at P14, does not show a direction change**, because its source is the confounded study above. A direction change between P11 and P14 is a rat-level possibility, not a mouse finding, and the age series is the more needed for that reason. An earlier line that an agent can change direction between P11 and P14 in the mouse is withdrawn here; whether the withdrawal follows from the later chloride-window line is an inference of the design team, not a statement of the original line. The panel names no benzodiazepine. Diazepam is age-dependent in rat pups (status epilepticus not stopped at P9, stopped at P15 and P21; abstract level).

**For any chloride-transport arm added** (none is proposed): a wild-type-on-agent group (a bumetanide effect on seizure latency was the same in wild type and mutant in one model); assignment by animal within litter, or analysis by litter (litter-level randomisation analysed per animal was a confound in the one genetic-DEE pup dataset); benzodiazepine tests timed from the onset of status, not from the convulsant; a sedation measure; and developmental endpoints kept separate from timing endpoints (a shift of a self-resolving phenotype is not a change in development).

**OPEN-GAP T72 (owner SCI): Which dataset is "the one genetic-DEE pup dataset"?**

## Groups to run (stages and the assay-validation panel)

**Stages (each has a stop rule).**

| Stage | What | Why this order | Stop or branch |
|---|---|---|---|
| 0 (not in vivo) | the brain-slice experiment (a separate experiment and a separate package, with its own predictions and no shared animals) | needs no animal harm assessment; independent of this assay | runs first or in parallel for stages 1 to 3; **stage 4 does not start before it has run**; otherwise this text does not depend on its result |
| 1 pilot | knockout and wild-type vehicle pups at candidate assay ages; stimulus and window fixed; within-genotype variability of S estimated **on the scale of the primary analysis (ratio of means with a bootstrap over litters; report the CV of S (coefficient of variation) and the SD of log S among animals with S above zero, since log S is undefined at S = 0)** (n of 6 to 8 per cell is the Cheng 2020 scale) | fixes the assay age, the non-floor stimulus and the sample size | stop if knockout vehicle pups cannot be tested at a stage-matched wild-type response, or if the panel agent has no effect at any age |
| 2 ethosuximide (the arm whose outcome decides between the three readings of ethosuximide: selective, age-limited or general) | ethosuximide against vehicle in all genotypes **with the wild-type age series and the panel** | the only arm whose outcome decides between selective, age-limited and general | if the panel is not valid at the assay age, move the assay age, do not read the null |
| 2, optional | a selective Cav3 (T-type calcium channel) blocker arm beside ethosuximide (class label; it asks whether a T-type route is the reason; "selective" = the laboratory states its criterion, at least published selectivity for Cav3 over other voltage-gated calcium, sodium and potassium channels at the exposure used and published rodent brain exposure; illustrative examples from the abstract-level literature: TTA-A2, Z944; no evidence that the drug reaches and acts on its target in the pup brain (an engagement control) exists in pups and no rodent pup datum for the selective blockers was found, so a null is not interpretable unless the laboratory adds one) | the only way to ask whether a T-type route is the reason | none |
| 3 lithium (optional) | lithium against vehicle in all genotypes **in the same session**, with the lithium-alone arm (see "Regimens and dose checks"), **one second GSK-3 inhibitor of a different class** (chemically unrelated to lithium, published selective GSK-3 inhibition at the exposure used and published rodent brain exposure; illustrative examples: SB216763, CHIR99021, TCS2002) and **one general non-GSK-3 anticonvulsant comparator drug** effective across ages (valproate in the rat literature) | separates "GSK-3 route" from "general property"; lithium alone cannot (it also acts on other targets); **the second GSK-3 inhibitor of another class becomes more necessary, not less** | none |

**OPEN-GAP R2Q43 (owner SCI): For stage 3, in the same session as what, and at the assay age only or across the whole age series?**
| 4 last (optional) | the NMDA-receptor pore-blocker arm (class label; channel-blocking antagonists such as ketamine and MK-801), **only with harms and stopping rules written first** (provoked-seizure aggravation, ataxia, status) and its predictions written then | aggravation is the class's best-documented harm; the slice arm should come first | predictions not fixed here |

**CONFLICT-OPEN C09 (owner SCI): The stage 1 row lists knockout and wild-type vehicle pups only, while its stop rule ("if the panel agent has no effect at any age") and the dose-check decision ("if the lower exposure is effective in the panel agent at an age") need pups given the panel agent.**

**OPEN-GAP Q19 (owner SCI): Does the pilot include the panel agent and older ages, and which candidate assay ages are tested?**

**OPEN-GAP Q20 (owner SCI): What is a "stage-matched wild-type response" in the stage 1 stop rule, and may the stimulus differ by genotype to reach it?**

**OPEN-GAP Q34 (owner SCI): How many pups and litters does the pilot alone need, given "n of 6 to 8 per cell" and unspecified candidate ages and cells?**

**OPEN-GAP Q23 (owner SCI): Which cells make up the first run (genotype by arm by age by exposure), as one list?**

**OPEN-GAP Q25 (owner SCI): Does the lithium-alone arm receive PTZ, in which genotypes, and is it counted among the arms that share a vehicle group?**

**OPEN-GAP Q27 (owner operator): Is the brain-slice experiment of stage 0 to be run by this laboratory, by another laboratory or by nobody, given that stage 4 is gated on it?**

**OPEN-GAP Q30 (owner SCI): Is "vehicle" vehicle plus PTZ only, or is a no-PTZ control (vehicle only, no provocation) also needed?**

**Order if resources are limited.** If resources allow only one step: the pilot (stage 1), then the ethosuximide arm with the age series and panel (stage 2). **Required:** stages 1 and 2 with the panel and the age series. **Optional:** the T-type arm (it needs an engagement control to be readable), stage 3, stage 4, and the add-ons. The laboratory costs the number of arms, agents and ages from these lists; the animal counts are illustrative until the pilot gives the SD. [Clarification by text work, for SCI to confirm: this order is the order for the provoked-seizure design; the one-slot order of the optional measurements under "Optional add-ons" applies to the add-ons only.]

**OPEN-GAP Q35 (owner SCI): If the laboratory can obtain only a fixed number of knockouts, what is the smallest stage 2 that remains informative?**

**Assay-validation panel** (called "the panel"). Separate wild-type pups at every age, sharing that age's vehicle group, so that a null is read only at an age where the assay can show a drug effect. The valproate effect in mouse pups is unknown, so the panel's validity is established empirically at each age, and **a failed panel is reported as an assay failure, not as a negative**. The panel has: a **flat-profile** agent (an agent whose efficacy does not change with age in the cited literature: valproate protects against PTZ at every rat age tested; mouse unknown, so it is itself a check); one **rising-profile** agent (efficacy rising with age in rat PTZ abstracts: carbamazepine, or cannabidiol); and, if an NMDA-receptor arm is included, one **falling-profile** agent (efficacy falling with age: ifenprodil or Ro 25-6981; ifenprodil effective in mouse at P7 and P10 and not at P14 or P21, in rat up to P18 on one assay and proconvulsant on afterdischarges at P18 and P25; Ro 25-6981 effective at P12 and failing at P25 in rat). **All agent names are examples from the rodent literature only, not proposed for any use; the laboratory chooses** (abstract level; one laboratory family is the origin of many rat rows).

**OPEN-GAP Q67 (owner SCI): What numerical rule declares the panel valid at an age?**

## Regimens and dose checks

- **Main lithium contrast.** One regimen is the main lithium contrast: the Cheng 2020 repeated pretreatment (three injections within one hour before a low-dose PTZ challenge), as the replication condition. The laboratory states any other regimen before data.
- **Source evidence on regimen.** No regimen in the sources shows a clear sign flip against PTZ (the one acute pro-convulsant abstract is from one laboratory family, with interval and method unreadable and the full text closed). The design team's literature table holds acute pro-convulsant and chronic threshold-raising results in one mouse PTZ paper family.

**CONFLICT-OPEN C03 (owner SCI): One item says no regimen in the sources shows a clear sign flip against PTZ and, in the same item, that one mouse PTZ paper family holds an acute pro-convulsant and a chronic threshold-raising result; what the family shows, at what level, and why it is not counted as a sign flip is not stated.**

- **Optional second regimen.** A second regimen is an optional comparator arm (a single injection, PTZ about 30 minutes later), not a design variable of the main contrast.

**CONFLICT-OPEN C02 (owner SCI): The scope paragraph says this text offers no schedule of its own (the only regimen mentioned being the one stated in Cheng 2020), while the optional second regimen is described as a single injection with PTZ about 30 minutes later without saying whose schedule that is or whether it comes from a source.**

- **Lithium-alone arm.** A lithium-alone arm is added, with a sedation, righting-reflex and weight readout at the PTZ time and the recorded interval from the last injection to PTZ (Cheng's panel has no lithium-alone arm and states no sedation, weight or interval; a low grade cannot tell protection from reduced behavioural output).
- **Second GSK-3 inhibitor.** The second GSK-3 inhibitor of another class becomes more necessary, not less.
- **Dose check per age.** Because potency shifts with age and **no pup exposure measurement was found for any agent**, "an effect of the drug" is defined only together with a **dose check per age: two exposures per agent (or a published pup exposure) at each age of the series, or a measured exposure if the laboratory has the means (not required)**. A non-effect at an exposure that was not checked at that age is a **dose null, reported as unresolved**, not as no effect.

**OPEN-GAP Q13 (owner SCI): What PTZ dose, route and volume, and what intervals between the three injections, did Cheng 2020 use for the low-dose PTZ challenge that the lithium replication condition is anchored to?**

**OPEN-GAP QA1 (owner SCI): Which lithium salt, vehicle and route are used in the replication condition, and are the three injections evenly spaced within the hour?**

**OPEN-GAP Q14 (owner SCI): What is the ethosuximide regimen (dose, route, pretreatment interval, number of injections) for the main contrast?**

**OPEN-GAP Q15 (owner SCI): Should vehicle pups receive the same number, volume and timing of injections as the lithium arm, and is one shared vehicle valid across agents that may need different vehicles, routes and schedules?**

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
| no genotype specificity (interaction ratio) | 0.7 to 1.43 (as in the predictions file, E1, E3 and P5) |

**CONFLICT-OPEN R2C01 (owner SCI): The values 0.7 and 1.43 belong to both classes of the thresholds table (genotype specificity: at most 0.7 or at least 1.43; no genotype specificity: 0.7 to 1.43), so a ratio of exactly 0.7 or 1.43 is not classified.**

- **Floor rule.** If vehicle S in a genotype is zero or at the floor, R is not computed and the arm is not interpretable.
- **A null is hard to reach.** A "null" interval is hard to reach at these sample sizes, which is why "unresolved" and "an effect of 0.7 or larger is excluded" exist.
- **Interval method.** With about 1.75 knockouts per litter the bootstrap over litters is the primary interval; with fewer than 10 litters in a cell the laboratory uses a permutation test or a mixed model with a litter random effect and says so before data. The absolute-scale interaction is a secondary report.
- **Shared vehicle and multiplicity.** Where five test arms share one vehicle group per genotype, the vehicle group is made about twice the size of a test arm (the square-root rule, for five arms), and the intervals of the five comparisons are reported at 95% and at 99% (Bonferroni for five). The ethosuximide comparison is the pre-specified primary and is judged at 95%; every other "effect" counts as confirmed only if it holds at 99%.
- **Why a ratio.** A bounded scale (0 to 6, floor at 0) makes a proportional effect look smaller in absolute grade where the baseline is low; that is why the ratio scale is primary and the floor rule exists.
- **Order of hypotheses (fixed before data).** (i) panel validity at each age; (ii) the ethosuximide effect ratios in the knockout and in the wild type at the assay age and at the older ages, as descriptive ratios with their intervals; (iii) the interaction ratio with its interval, **exploratory unless the pilot SD makes it sized**. Where the interaction cannot be sized, the answer comes through (i) and (ii).

**CONFLICT-OPEN R2C09 (owner SCI): The ethosuximide comparison is listed as primary in one place and as descriptive ratios with intervals in another; whether it is tested at the stated confidence level is not stated.**

**CONFLICT-OPEN C35 (owner SCI): The multiplicity statement counts five comparisons (95% and 99%, Bonferroni for five), which matches the arm list of the design frame but not the later additions (a lithium-alone arm, an optional second regimen, panel agents at two exposures each).**

**OPEN-GAP Q70 (owner SCI): How many comparisons enter the Bonferroni correction once the lithium-alone arm, a second regimen and the panel agents at two exposures each exist?**

**OPEN-GAP Q68 (owner SCI): What numerical value of vehicle S counts as "at the floor"?**

**OPEN-GAP Q69 (owner SCI): How is an increase of seizure burden (aggravation, R above 1) classified, since "effect" is defined only as R at most 0.7?**

**OPEN-GAP Q71 (owner SCI): To whom and in what form is the analysis plan "stated before data" delivered (registry, collaborator, time stamp)?**

**OPEN-GAP Q73 (owner SCI): The outcomes table separates E1 from E3 through the interaction, which cannot be sized with the full-hour area summary; what descriptive pattern separates them when the interaction cannot be sized?**

## Sample size and animals needed

All figures here are ASSUMED values, hypothesis level, not a forecast, and illustrative until the pilot gives the SD. Cheng 2020 used 6 to 7 knockout and 12 to 20 wild-type or heterozygous pups per group; with a heterozygote cross and about 7 pups per litter, a litter yields about 1.75 knockouts. Where two older statements gave different figures for the same quantity, the later statement is used and the earlier one is in the History.

| Quantity | Value as stated | Basis |
|---|---|---|
| simple effect of ratio 0.7 (ln = -0.357), animals per arm | about 11, 31 or 79 for a within-genotype SD of 0.3, 0.5 or 0.8 | two-sided 0.05, power 0.80; the SD of 0.3 is the optimistic case |
| simple effect, from an eye reading of Cheng 2020 Fig. 7b (knockout PTZ-alone curve, N = 6; SEM bars of about a third to a half of the mean) | an SD of S of 0.7 to 1 times the mean, about 0.6 to 0.8 on the log scale; roughly 44 to 79 animals per arm | the number 44 here is a simple-effect number per arm; see the note below the table |
| simple effect, from a quantification of the means and upward SEM bars of Fig. 7b and 7d (per-minute SD = SEM times the square root of N; S = mean grade over 60 minutes; bounds from independent to fully correlated minutes; N assumed constant) | knockout PTZ-alone groups: a CV of S of 0.58 to 1.19 at a within-animal correlation of 0.6 to 1.0 (log SD about 0.54 to 0.94; the rigorous upper bound is 0.67 for 7b and 0.94 for 7d); about 36 to 109 animals per arm for a ratio of 0.7 | hypothesis level; the "log SD 0.6 to 0.8" of the eye reading is inside this bracket; the optimistic SD of 0.3 is not credible (it needs a within-animal correlation of 0.05 to 0.15) |
| wild-type and heterozygous pups at that published stimulus | at the floor: mean S 0.27 to 0.41, CV above 1.4; a ratio of 0.7 would need about 140 to 210 per arm, so a stimulus with a non-floor wild-type response is a requirement, not an option | same quantification; see CONFLICT-OPEN C23 above |
| a binary outcome such as generalised seizure (assume 50% in vehicle knockouts) | a fall to 10% needs about 20 per arm; a fall to 20% about 38 | assumed values |
| interaction contrast (genotype by treatment), per cell | **twice** (not four times) the simple-effect number per cell; with the bracket above, about **180 to 320 animals per cell**; four cells; about 700 to 1,300 animals and 350 to 630 knockouts (200 to 360 litters) for one drug against vehicle | the later statement; the older statement of four times is in the History |
| the same interaction contrast at the optimistic SD of 0.3 | 22 per cell, 88 animals, 25 litters for one drug against vehicle | optimistic scale |
| three knockout arms, simple effect only | at 11 per arm about 19 litters; at 31 per arm about 53; at 36 to 109 per arm, 108 to 327 knockouts, about 62 to 187 litters | the figures at 11 and 31 are the optimistic scale; the figures at 36 to 109 follow the bracket |
| planning total for the required stages with the dose check (two exposures per agent per age, panel included; for planning, not a promise) | about 27 cells (the wild-type age series: 3 ages times vehicle, ethosuximide at two exposures, one flat-profile and one rising-profile panel agent at two exposures each = 21 cells; knockout and heterozygote at the assay age: vehicle and ethosuximide at two exposures = 6 cells), i.e. about 300 animals at 11 per cell or about 1,350 at 50 per cell, of which 33 to 150 knockouts (19 to 86 litters) | optimistic scale (the basis of the per-cell figure of 50 is not stated); the pilot decides the dose check first: if the lower exposure is effective in the panel agent at an age, one exposure per agent at that age is enough and the totals fall accordingly |

Note on the number 44. The older texts used it for two different quantities: (i) a simple-effect number of 44 to 79 animals per arm at log SD 0.6 to 0.8 (the eye reading above); (ii) an interaction number of 44 per cell at SD 0.3 in the original arithmetic, which is superseded (see the History). Only the first is current.

**Planning scale.** The 36 to 109 animals per arm for the knockout is the scale for planning. The litter and animal totals of the sections above (19 and 53 litters; 75 litters; the dose-check totals) are the optimistic scale and should be read with the 36 to 109 bracket.

**An independent reading** of the same curves agrees within about 20 percent (per-minute means within 0.05 and 0.15 grade; SD of the summed grade 9.5 to 62 and 10.9 to 69 against 11.4 to 71.5 and 9.2 to 56.9 for the first reading, whose values are given only here) and concludes that the sizing flag stands.

**Limit on direction.** The bracket assumes the legend N over the whole hour; whether animals that die keep grade 6 or leave the mean is not stated, and the two possibilities bias the SD in opposite directions (fewer contributing animals than the legend N makes the bracket overstate the per-minute SD; survivor-only curves make it understate the full-cohort SD); the net direction needs the authors' per-animal data and does not change the order of magnitude of the sizing.

**The genotype-by-treatment contrast is therefore not attemptable with the full-hour area summary at the variability these curves show;** it is attemptable only if the pilot finds a stimulus or a summary (for example an incidence of generalised seizures) with far lower variability. The order of hypotheses under "Analysis plan" stands: panel validity and the effect ratios by genotype and age come first, and the interaction is an exploratory interval. The brief says so rather than promising an interaction test.

**A stage that runs in a different session carries its own vehicle group per genotype** (the shared vehicle holds only within a session).

Wild-type and heterozygous animals are not limiting.

**CONFLICT-OPEN C25 (owner SCI): The sentence above says wild-type and heterozygous animals are not limiting, while the age series and the panel call for 21 wild-type cells, and the wild-type pups are taken to come from heterozygote crosses (expected 1:2:1) that give about 1.75 knockouts per litter; where the wild-type pups come from is not stated.**

**CONFLICT-OPEN C06 (owner SCI): The rule that an interaction contrast needs twice the simple-effect number per cell, applied to the stated per-arm bracket of 36 to 109 animals, does not appear to give the stated per-cell bracket of 180 to 320 animals; the inputs of the per-cell figure are not given.**

**CONFLICT-OPEN C08 (owner SCI): The vehicle group shared by the test arms is to be about twice the size of a test arm, while the planning totals give every cell the same n (about 300 animals at 11 per cell); the vehicle group of an age is also shared by the panel agents, not only by the test arms.**

**OPEN-GAP Q31 (owner SCI): Which n per cell should the laboratory plan for the first run, given that the figures 11, 22, 31, 36 to 109, 44, 50 and 180 to 320 are all stated with different bases?**

**OPEN-GAP Q32 (owner SCI): Is the vehicle group made about twice a test arm in the 27-cell total of about 300 animals?**

**OPEN-GAP Q33 (owner SCI): Do the litter figures (19, 25, 53, 75 and the bracket figures) refer to one drug against vehicle or to three knockout arms, and which single figure is the one for a breeding plan?**

## Welfare and stopping

**Humane endpoints and approvals are the laboratory's.** About half of PTZ-injected knockouts reached status epilepticus in Cheng 2020. A stopping rule for status (when to rescue, by the laboratory's own approved procedure; the pup then stays in the analysis with its last grade carried forward, flagged), written before the first animal, is a design requirement, not an option. The laboratory's own ethics approval for PTZ-provoked status epilepticus in fragile knockout pups is needed, and the laboratory decides whether stage 2 is possible at all. Stage stop rules are in the stage table.

**OPEN-GAP Q61 (owner SCI): What triggers a rescue, what is the rescue procedure, and may a rescue drug be used given that it could confound the arm effect?**

**OPEN-GAP Q62 (owner SCI): Is death an accepted outcome in vehicle and treated groups, and what death or status rate is expected per arm (only "about half of PTZ-injected knockouts reached status" is given)?**

**OPEN-GAP Q63 (owner laboratory): What are the conditions of the 60-minute observation of fragile pups (dam present or isolated, heat support, handling)?**

**OPEN-GAP Q65 (owner laboratory): What experiment-level stopping rules exist (for example cumulative knockout deaths) beyond the pilot and stage stop rules?**

**OPEN-GAP Q66 (owner laboratory): What is the total procedural burden on one pup in the lithium arm (three injections, pre-test, PTZ, observation, possible tissue)?**

**OPEN-GAP QA5 (owner SCI): Does a stop rule (the pilot, or a panel that is invalid at the assay age) end only that stage or the whole experiment, and who is informed?**

**OPEN-GAP QA4 (owner SCI): Are pilot animals and pilot data reused in the main analysis, and who signs off the pilot's choice of age, stimulus and summary before the main run starts?**

## What each outcome would favour

Hypothesis; each row is one stated reading.

| Arm | Pattern (panel valid at the age, wild type above floor) | Favours | Does not show |
|---|---|---|---|
| Ethosuximide | R(-/-) effect; R(+/+) null; interaction at most 0.7 (E1) | a knockout-selective effect | a T-type route; spontaneous-seizure benefit |
| Ethosuximide | R(+/+) null at the assay age, an effect at the older age (E2) | age-limited with a wild-type floor; the Cheng 2020 pattern is not knockout selectivity | that the knockout effect is absent |
| Ethosuximide | similar effects in all genotypes (E3) | a general anticonvulsant effect | selectivity or its absence at other ages |
| Ethosuximide | no effect anywhere (E4) | the Cheng 2020 knockout effect did not replicate at this age and stimulus | any statement about other ages or exposures |
| Selective T-type blocker beside ethosuximide | same pattern as ethosuximide in the knockout (C1) | a T-type route is plausible (not proven without engagement or genetics) | Cav3 expression in the knockout |
| Selective T-type blocker | no effect where ethosuximide has one (C2); applies only if the laboratory has added an engagement control, since without one a T-type null is not interpretable | ethosuximide's effect is not carried by selective T-type block at this exposure and age, or the exposure was inadequate | which |
| Lithium, second GSK-3 inhibitor, general comparator drug | lithium effect in all genotypes (interaction between 0.7 and 1.43); second GSK-3 inhibitor effect; comparator effect | a general anticonvulsant effect of GSK-3 inhibition and of the comparator | GSK-3 specificity in the knockout |
| Lithium | knockout-larger effect, **reproduced by the second GSK-3 inhibitor and not by the comparator** | GSK-3 route, knockout-enhanced | p-Ser9 change or kinase activity (needs the add-on) |
| Any arm | minimal-seizure incidence up while generalised incidence down | seizure-type-specific action | benefit or harm in the null phenotype |

The weights for these classes are in the predictions file; they are scored literally when data exist and are not calibrated probabilities.

C1 and C2 are labels of the two T-type rows (the blocker matches ethosuximide, or does not).

[Clarification by text work, for SCI to confirm: the first lithium row appears to correspond to reading L1 and the second to reading L2; the older table carries no L1 or L2 labels.]

**OPEN-GAP Q82 (owner SCI): Which rows of this table carry the lithium readings L1 and L2 (the older table does not label them)?**

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

**OPEN-GAP R2Q79 (owner SCI): How are the inhibitory currents and phospho-ErbB4 to be measured (region, age, method, tissue plan) in animals of the same cohort as the calcium and serum add-on?**
- **(e4) The human side** (dated 2026-11-21; class level, no dose). The human side is empty too: calcium and parathyroid hormone are named in no human WWOX-DEE or SCAR12 (a human WWOX-related disorder) report read (20 reports and 4 reviews read at full-text depth; 15 further reports not obtained and unread at full text, a named access gap), and no lipid statement exists at an infant age (the single human lipid statement is "low" in one case at 21 months, not infant, at the edge of the spectrum). This strengthens the add-on measurement of (e2); it settles nothing in either direction.

**CONFLICT-OPEN C31 (owner SCI): The glucose series (e) and the calcium add-on (e2) overlap with different measurement lists (glucose, ketone and lactate by age, milk intake or stomach filling against serum total calcium with albumin or ionised calcium, glucose, body weight and a milk-spot score) and different sampling ages (P7 to P14 against P7, P9, P11 and P14).**

**CONFLICT-OPEN C32 (owner SCI): The calcium add-on (e2) is placed alongside GFAP and Iba1 scoring at P5 to P9, but no such scoring is planned in this design (GFAP appears only in the optional development cohort).**

**CONFLICT-OPEN C30 (owner SCI): The human-side line (e4) speaks of calcium and parathyroid hormone and of a lipid statement, but neither parathyroid hormone nor lipid is in the measurement list of the calcium add-on (e2); which of them the add-on measures is not stated.**

**OPEN-GAP T44 (owner SCI): Name the neuron-targeted line (S-KO), its allele, its cross and its source, and define "S-HT", used in (g).**

**OPEN-GAP Q57 (owner SCI): Are (e) and (e2) one add-on or two, and are the measures taken serially in the same pups at P7, P9, P11 and P14 or in separate cohorts, with the blood volume at P7 addressed?**

**OPEN-GAP Q54 (owner SCI): For add-on (b), when is tissue taken relative to the last injection and to PTZ, at which age and in which regions?**

**OPEN-GAP Q56 (owner laboratory): How does add-on (d), deletion completeness, apply to a germline null, and what is the laboratory to measure?**

**OPEN-GAP Q60 (owner SCI): For video-EEG on "a subset of knockout pups", which subset size, age and electrode plan?**

- **(f) A heterozygote carrier readout (candidate, one source).** In the germline-null report (3-week-old mice; chloral hydrate; legend SEM; one laboratory) transcranial motor-evoked-potential (Tc-MEP) **onset latency was 1.39 +/- 0.13 ms in wild type (n = 10), 2.13 +/- 0.22 ms in heterozygotes (n = 5; P < 0.05 against wild type) and 2.44 +/- 0.37 ms in nulls (n = 4; P < 0.01), amplitude 59.2 +/- 9.0, 59.6 +/- 17.2 and 11.8 +/- 5.4 microvolts**: a **partial latency prolongation with normal amplitude in heterozygotes, not equal to the null**; the authors write "a partial Tc-MEP deteriorative change"; **there is no heterozygote-against-null test**. This brief carries only the heterozygote bursting incidence.

**CONFLICT-OPEN C16 (owner SCI): The last sentence of add-on (f) says this brief carries only the heterozygote bursting incidence, but no heterozygote bursting incidence appears anywhere in the older texts.**

**OPEN-GAP Q55 (owner SCI): What is the heterozygote bursting incidence that this brief is said to carry, and from which source?**

- **(g) Myelin or conduction endpoints.** The endpoints with demonstrated neuronal-rescue evidence are structural (electron microscopy myelinated-axon counts per animal, g-ratio, MBP (myelin basic protein) and CC1 (an oligodendrocyte marker) immunostaining). **Callosal conduction latency was measured once**: n = 8 slices from 5 animals (controls) and 8 from 6 (knockout), the control n identical to another experiment's S-HT n (possibly copied), effects read from graphs (first-peak latency about 2.5 against 3.2 ms), neuron-targeted line only, acute slices P13 to P17, no rescue, no velocity: **a candidate needing re-measurement with a rescue arm and animal-level statistics, not yet an endpoint.** A published contrast of Olig2 (corpus callosum) against Mbp (parietal cortex) in the report called P47T in the sources compares different regions (the Mbp panels are Supplementary Figure S6 of the same paper, held by the design team; caption read, panels not opened: parietal cortex above the corpus callosum, 80 and 250 days, n = 3 per genotype, unpaired t-test not significant) and supports only a composition caveat.
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
- **Condition for running it:** only after the provoked assay shows a lithium effect that is **selective, with the genotype-by-treatment term** (set P5 of the predictions file: interaction outside 0.7 to 1.43, and the second GSK-3 inhibitor reproducing it while the non-GSK-3 comparator drug does not). **Fallback if the interaction cannot be sized (it usually cannot):** the interaction term is then exploratory and does not by itself decide; the condition becomes GSK-3 pharmacology in the knockout (lithium effect with R at most 0.7 reproduced by the second GSK-3 inhibitor of another class and not by the non-GSK-3 comparator drug), with the interaction interval reported as exploratory. **"General" is defined once, for the condition, the fallback and the drop rule: the lithium effect is also reproduced by the non-GSK-3 comparator drug** (with an interaction that cannot be sized, genotype specificity cannot be used to tell general from specific). If the provoked assay shows lithium to be general in that sense, the development arm has no rationale beyond a general anticonvulsant and should be dropped. The prior is thin (a divided GSK-3 sign for myelination, no pup exposure data) and an early floor is likely because untreated knockouts die by about day 17.

**CONFLICT-OPEN R2C10 (owner SCI): The condition for the optional cohort, an interaction outside 0.7 to 1.43, also admits a smaller knockout effect, which the outcomes table does not call knockout-enhanced.**

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
- 2026-11-21, lines 9.14, 9.15 and 9.16: see "Out of scope for this laboratory" and the entry above.
- 2026-11-21, line 9.17: folded into add-on (e4).

## Out of scope for this laboratory

The following lines of the original concern a gene-addition benchmark paper (a gene-therapy reference), not this provoked-seizure design, which contains no partial-restoration, gene-addition or vector arm. Each has one current sentence; the rest is in the History.

- **Regional expression range (line 9.14, as corrected).** The cerebellum is the lowest region in the benchmark's high-dose mice at every age; whether that is the platform (regional reach of neonatal intracerebroventricular AAV9 with a neuronal promoter) or this paper is open: cerebellum lowest in this benchmark, cause open. Any partial-restoration readout in a design that has one should report the region.
- **Expression-range lean (line 9.15; provisional, one reading).** The cerebellum is expected lowest, delivery-limited already at the vector-DNA level at P30 in the benchmark; this is a provisional lean toward a platform effect, not a verdict, and the kinetics gap (an expression time course from P5 to P20) is a missing measure.
- **Scope of the lean (line 9.16).** The platform-low reading stands only for regional protein and vector DNA at P30 (the benchmark's Figure 5; one reading of Voronin 2024); the neuron fraction at P17 to P19 is near cortex, and "the cerebellum is lowest" must not be read as "fewer cerebellar neurons transduced"; cerebellum lowest in this benchmark, cause open.
