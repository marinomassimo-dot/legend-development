# Matrix V2 class list: a proposal (PRESIDIO-016, SCI, 2026-11-16; POST-HOC, never scored as a prediction)

Non-canonical working note. Not medical advice; no dose, no recommendation to use any agent; every agent named is a class label with its held source, BLOCK-1 not applied. Reference genotype class only. This is the INPUT for the next iteration's frozen matrix; it changes nothing in the freeze f5b71a3f4. The table is `class_candidates_v2.tsv` (13 rows).

## Answer first
1. **Keep the 15 and make four changes.** Two splits, two new columns: (a) split 'GABA-A PAM (non-benzodiazepine)' into a synaptic-selective class and a neurosteroid (extrasynaptic) class, contingent on the brief reading a tonic current; (b) split 'cannabidiol/fenfluramine-type' so that the one coded outcome class (cannabidiol alone) is not credited with fenfluramine's mechanism; (c) add **HCN (Ih) blockers**, because Breton 2021's measured sag and post-inhibitory rebound (T13, tier 3 for the observation) have no class in the 15 that expresses them; (d) add **neuroinflammation / IL-1 pathway modulators** as a column whose sign is `unknown`, because reactive gliosis (Gfap up in three neuron-deletion contrasts; Aldaz 2019 and the P47T paper) is one of the few axes with two laboratories and the matrix cannot show it. Result: 15 + 2 splits + 2 new = 19 scored columns.
2. **Hold three as WATCH classes, with a named trigger and no column:** chloride-gradient modulators (trigger: any measured E_GABA or driving force in a WWOX preparation; it is the one class whose sign interacts with the matrix's top class), mTOR pathway inhibitors (trigger: a second line or a phospho-S6 measurement; the pre-test fails in two of three model families), KATP/ketone (trigger: the brief's substrate arm). Reject two as columns: endocannabinoid (no held thread, no WWOX evidence) and NPY system (tool class; watch only if the hippocampal unmasking experiment works).
3. **Do not split yet:** NMDAR pore blockers by block type (needs a second pore-blocker arm in the brief and a held thread for synaptic against extrasynaptic), benzodiazepines by subunit (no thread carries GABA-A subunit identity in a WWOX preparation; the subtype dispute itself is unresolved), sodium-channel blockers by state dependence (AH1 first). Split AMPA into competitive and noncompetitive only if the brief runs both arms (the AMPA package already treats it as a pair).

## Rules I propose for V2 (declared before the next freeze, not applied retroactively)
* **R1, a column is scored only if it links to at least one thread at tier >= 1 and directness >= 1 from a held WWOX observation**, not from class expectation alone; otherwise it is a WATCH class (listed, not scored, trigger stated).
* **R2, the informativeness denominator counts scorable classes only.** Adding empty columns inflates 1 - k/N with no new information: the same five-way tie scores 0.667 at N = 15, 0.737 at N = 19 and 0.762 at N = 21, and the one-third claim limit moves from 5 to 6 or 7 classes. For V2 I propose N = classes with at least one non-neutral cell, reported next to the raw 1 - k/15 figure so the V1 and V2 results stay comparable.
* **R3, a split needs two things:** the brief's arms must contain at least two representatives of the sub-classes, and a held thread must distinguish them (synaptic against extrasynaptic is one, tonic current is not yet recorded).

## Table (full text in `class_candidates_v2.tsv`)
| candidate | change | links to | tier now | approved-agent route (class label only) | decision |
|---|---|---|---|---|---|
| neurosteroid GABA-A (extrasynaptic) | split of GABA-A PAM | T2; tonic current unrecorded | 1 | approved for seizures in one other developmental disorder (ganaxolone-type label) | column if the brief reads a tonic current |
| fenfluramine-type (serotonergic/sigma-1) | split of CBD/fenfluramine | none directly | 0 | approved for two developmental epilepsies (label) | column, no scored cells |
| HCN (Ih) blockers | new | T13 (sag, rebound) | 3 for the observation | ivabradine-type approved for a cardiac indication | column |
| neuroinflammation / IL-1 modulators | new | new gliosis thread | 2 | IL-1 antagonist approved for other indications (anakinra label) | column, sign unknown |
| chloride-gradient modulators | new | T2, T14, T17 | 0 (2 to 3 after E_GABA) | NKCC1 inhibitor approved as a diuretic (bumetanide label) | WATCH |
| mTOR inhibitors | new | H-ADV-4 | 1 | everolimus-type approved for TSC seizures | WATCH |
| KATP / ketone | new | T10, H-ADV-2 | 0 | diazoxide-type approved for another indication | WATCH |
| endocannabinoid | new | none | 0 | none | no column |
| NPY system | new | HSCI-5 | 1 | none | WATCH |
| NMDAR pore blockers by block type | split | T1 | 3 | memantine-type approved for another indication | no split yet |
| benzodiazepines by subunit | split | T2 | 3 | approved | no split |
| AMPA competitive against noncompetitive | split | T1 | 1 to 2 | perampanel approved (noncompetitive) | only if both arms are run |
| sodium-channel by state dependence | split | T13, AH1 | 1 to 2 | approved | no split yet |

## Why these, in one paragraph
The 15 classes were written before the threads were: they cover what an antiseizure drug targets, not what the WWOX data measure. The two additions that matter are exactly the measurements the held data already contain and no class expresses: the intrinsic property (sag, Ih) and the glial reaction. The splits are the ones the held sources already make (synaptic against extrasynaptic GABA-A; cannabidiol alone as the coded outcome class). The rest are held back on purpose: each WATCH class has a measurable trigger, and none of them would score today, because no held thread reaches it; adding them as columns would only change the denominator.

## Limits
Class-level labels only; approved routes are labels, not endorsements, and none was checked for pediatric safety or CNS exposure (BLOCK-1 is IT's). Tiers 'now' are read from the held sources named in the table; no new data. The proposal does not decide the scoring of a V2 matrix and is never scored as a prediction.
