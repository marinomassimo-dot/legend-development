# Ketamine: what the repository can and cannot say (IT merge, 2026-11-17; for the operator; drafted for SCI and HE to correct)

**Nothing here is medical advice.** No dose, no schedule, no recommendation for or against any use of any drug; the decision belongs to the treating clinical team. The question is posed only in the abstract (one exposure to an NMDAR pore blocker within a sedation episode, then a transient improvement lasting weeks). No testimony and no identifier of any person is used or recorded.

## In plain words (five lines)
1. **What we know:** ketamine has never been given to any WWOX system in anything the repository holds; what is held is the class (NMDAR pore blockers) in a model, in a laboratory tool, and in other diseases.
2. **What we do not know:** whether ketamine does anything for the reference genotype class, helps or harms, and what caused any improvement lasting weeks.
3. **What is hypothesis:** a lasting plasticity change is possible in principle, but nothing held contains the slow process it would need; non-drug explanations are more parsimonious, with no model support for a sole drug cause.
4. **The harms:** dissociation and emergence reactions, circulatory and secretion effects, liver and bladder effects, abuse potential, early-life anaesthetic-neurotoxicity concern, and a rebound after the block in the held slice; the harm profile in children is incomplete in the repository.
5. **What we cannot say:** that ketamine was or was not the cause, that it is safe or unsafe for any child, or that any step is advisable; BLOCK-1 safety screening was never run for it.

## Layer 1 - HELD (origin and tier; the harm or limit sits beside each row)
| What is held | Origin and tier | The harm or limit beside it |
|---|---|---|
| Ketamine has never been applied to any WWOX system (animal, tissue, person) in any held file. | repository, absence | no WWOX benefit and no WWOX harm is measured: both unknown |
| In the neuron-specific Wwox-knockout neocortical slice, a competitive NMDAR blocker (d-APV, a laboratory tool, not ketamine) abolishes bursting. | Breton 2021 via the repository; acute slice, tool compound | on washout bursting returned to about 1.85 times baseline (held, image-read, `analysis/therapeutic_repair_candidates.md` line 94): a rebound signal |
| **What the model says.** A pore blocker in the held oscillator shortens bursts (-54 percent) and lengthens intervals (+55 percent); the effect disappears when the block ends. SCI's preregistered hysteresis sweep found no hysteresis over minutes to about an hour. | simulation, tier 3, fitted to the same slice | the sweep covers minutes to about an hour only; a weeks-long carry-over needs a slow variable that is not held; a simulation cannot confirm itself; concentration-to-effect mapping unknown |
| The in vivo hyperexcitability of the null mouse was recorded under ketamine/medetomidine anaesthesia and the genotype contrast still stood. | Repudi 2021 (manifest entry 13) | no ketamine-free arm: it says nothing on ketamine's own effect |
| In other diseases ketamine is reported to stop refractory status epilepticus in about half of cases (retrospective paediatric cohorts and one meta-analysis; abstract level); no effect on development or function beyond seizure control was found. | HE census, abstract level, tier 3 transfer | adverse events needing intervention in a few percent (hypertension, delirium); one guideline-style review grades the evidence insufficient; co-medication confounds |
| Nothing was found, in the queries run, on a transient improvement after intensive care, anaesthesia or sedation in genetic neurodevelopmental conditions. | HE census gap closure | "not found in these queries", not "does not exist" |
| Safety position: the computational BLOCK-1 triage was **never run** for any NMDAR pore blocker (tools absent); ketamine is a prescription drug with labelled dissociative and abuse concerns; SCI's readiness colour is yellow, esketamine red (label wording). | IT BLOCK-1 README; SCI readiness sheets | these are not a verified safety profile; the drug is **not screened or triaged** by the repository |
| Held harm signals in other settings: reversible cholestatic liver injury in adults given ketamine with an AMPAR antagonist (77 against 27 percent, abstract); apoptosis after a few hours of NMDAR block in newborn rat brain (abstract); chronic block in a developing brain acts on activity-dependent maturation (inferred). | F04 packet DR-P9-005, DR-P9-013; SCI note H1 to H3 | transfer from adults or rodents; thresholds unknown |
| Arm table, NMDAR pore blocker: C007, C011, C054 are simulation, tier 3, parked; C010 reaches tier 2 through RNA readings, not a drug effect; four cells have no naming row. | arm table v8, row-level tier table | no cell supports a statement of benefit |

## Layer 2 - GENERAL KNOWLEDGE, UNVERIFIED (recollection; not held; check against a label or review before any use)
**This layer carries HE's caveat: the repository's harm profile for ketamine in children is incomplete; emergence reactions, repeated-exposure, liver and bladder effects, abuse liability and human anaesthetic-neurotoxicity cohorts were not retrieved.**
* Ketamine blocks the open NMDAR channel with a short half-life (hours) and active metabolites; adult mood effects after a single low exposure are reported to last about a week. This possible **benefit** is paired with its **harms**: dissociation and emergence reactions, raised blood pressure and heart rate, increased secretions, bladder and liver effects with repeated use, abuse potential.
* Early-life anaesthetic-neurotoxicity concern (rodent data convincing, human data contradictory and confounded) applies to infants and young children.
* Benefits seen with other sedatives (calm, sleep, seizure control during an infusion) are paired with their **harms**: respiratory depression, hypotension, rebound or withdrawal on sudden stop, delirium.
* The label status of ketamine in a child with a severe neurological condition is not held; a clinician decides what applies.

## Layer 3 - HYPOTHESIS (rival explanations of a weeks-long improvement after an intensive-care episode; none is evidence about any person)
| Explanation | Why it is a rival | Harm or caution beside it |
|---|---|---|
| An illness or inflammation resolved (fever, infection, pain, metabolic derangement) | a return to the pre-illness baseline on the same weeks timescale | relapse if the driver returns; the same illness may have caused the loss |
| Co-given sedatives, rest and sleep restoration | GABAergic sedatives suppress bursts in the model; sleep debt is a known provoker | sedation, respiratory and withdrawal risks |
| **Co-given anticholinergic agents that reduce secretions** (often given with ketamine; the agent class must be recorded) | a centrally acting anticholinergic can change alertness, tone and seizure threshold; a peripherally acting one has no brain effect: the class decides | anticholinergic delirium, sedation, heat and urinary effects; class and timing are unrecorded here |
| An antibiotic treated a driver infection | improvement tracks the infection | some classes lower the seizure threshold |
| A medication change at admission (held, stopped or reduced) | the benefit would reverse on restart | stopping an antiseizure drug is itself a risk |
| Lower seizure or discharge burden from any drug | the one capacity the model speaks to | burden may rebound on withdrawal (the 1.85 times washout overshoot) |
| The NMDAR block itself through a lasting plasticity change | needs a slow variable (plasticity, maturation, bistability); none is held | the same window carries the aggravation counterpart: chronic block removes a signal for maturation |
| Regression to the mean and reporting effects | a recorded low point, then a return | none: this is why a blinded, standardised measure matters |
| Several of the above together | co-occurring components cannot be separated by any amount of records | unknown |
**Judgements (SCI's, from the timescales of the table, not measurements):** the non-drug or non-NMDAR components are more parsimonious for a weeks-long course (about 0.85 that at least one explains part of it), and a sole NMDAR cause has no model support here (about 0.15). They are judgements, not data about any person.

## What a clinical team or a registry would need (generic; not advice to any family; not an experiment on a person)
To separate the rivals from records that already exist or from many cases: (1) a documented pre-illness baseline range; (2) the order of events in time (onset against each exposure and each illness-resolution day); (3) the full medication administration record per episode, including **sedatives, antibiotics and the anticholinergic class**, and any drug stopped; (4) seizure or EEG records and sleep records before and after; (5) a blinded or standardised measure at fixed time points; (6) comparison episodes of the same condition with the same sedatives **without** ketamine; (7) illness markers (temperature, inflammatory markers, cultures). Limit: confounding by indication (sicker people get ketamine more often) and components that co-occur in every episode cannot be separated by any amount of records.

Limits: built from held files and abstract-level censuses; layer 2 is unverified recollection; SCI's own data-collection frame (her reply file) was not on main when this was merged and replaces item list above where it differs; not medical advice.
