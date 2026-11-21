# ADV-151 result: seven named design decisions (SCI window X, 2026-11-21; hypothesis level; no dose; not medical advice)

Pre-registration: `PREREGISTRATION_ADV151_SEVEN_DECISIONS_SCI_20261121.md` (commit `9e5f1affb`; six rules and six predictions fixed before the cited sentences were opened; disclosure: I had read IT's option lists). Numbered replacements for IT's script: `REPLACEMENTS_FOR_IT_ADV151_SCI_20261121.tsv` (D01 to D07). Text edited: none. Sources: the current text, the frozen in vivo priors file, V2, IT's classification table; no new source, no number invented (derived numbers are labelled and were recomputed blind).

## Answer first
| Item | Decision | Rule | Moves a number? |
|---|---|---|---|
| C09 pilot pups | option 1: panel agent at ONE exposure in the pilot (the 36 to 48 animals already counted); dose check in stage 2 | RULE 2 plus the held stage 1 stop rule | no |
| C30 PTH and lipid in e2 | not by default (keep the e2 list; e4 is context); optional extension only if the laboratory can supply the blood volume | RULE 2, RULE 5 | no; one laboratory question |
| C31 e and e2 | default ONE combined add-on (union, P7, P9, P11, P14, serial in the same pups); split into two only if the blood volume forces it; settles Q57 | RULE 2, RULE 5 | no; one laboratory question |
| C35 multiplicity | family = test arms sharing a vehicle group in one session and genotype; **count 6 in wild type per age, 2 in knockout and heterozygote** (the sample-size section already uses them); intervals at 95% and 1 - 0.05/k = **99.17% and 97.5%**; added arms enter the family unless labelled exploratory before data | RULE 4, RULE 3 | **yes: divisor 5 to 6 and 2; the 354-animal total does not move** |
| R2C01 band endpoints | endpoints belong to the specificity class; P5's band is the OPEN interval above 0.7 and below 1.43; 'outside 0.7 to 1.43' becomes 'at most 0.7 or at least 1.43' | RULE 1, RULE 6 | classification of exactly 0.7 or 1.43 only |
| R2C09 primary | knockout ethosuximide ratio at the assay age, at the exposure the laboratory fixes before the first animal, judged at 95%; all else descriptive | RULE 3 | no; one laboratory question (which exposure) |
| R2C10 cohort condition | keep P5 as frozen (two-sided); a smaller knockout effect (ratio at least 1.43) is knockout-attenuated and does not by itself qualify the cohort | RULE 1 | no |

Of seven: five decided by a rule outright (C09, C35, R2C01, R2C09, R2C10), two decided as a default by rule with one laboratory question each (C30, C31). Laboratory-only residue: the blood volume of a P7 pup and across P7 to P14 (C30, C31), the primary exposure (R2C09).

## What the rules turned up that the table did not show
* **C35 was a conflict inside the current text, not only against later arms.** The multiplicity bullet counts five comparisons; the sample-size answer (C08/Q32) already uses six test arms per wild-type age and two per knockout or heterozygote group (66 + 26.9 and 22 + 15.6). V2's five is the stage 2 and 3 agent list and ignores the two-exposure dose check and the panel arms. Bringing the multiplicity statement to the sizing count moves the Bonferroni levels, not the animal total.
* **R2C01: 'outside 0.7 to 1.43' is not the complement of the frozen band.** The frozen file puts the endpoints in the specific class in three places (E1 'at most 0.7'; the E3 rejection 'at most 0.7 or at least 1.43'; the effect rule 'at most 0.7') and states P5's band only as 'lies between'. It is self-consistent only if that band is open; the text's 'outside' (endpoints inside the null band) was IT's reading, and V2 carries the same overlap.
* **Two things I did not decide** (frozen file silent, passed on as notes in D05): 1.43 is the rounded reciprocal of 0.7 (1/0.7 = 1.4286); and whether the interaction thresholds are scored on a point ratio or an interval.

## Predictions scored (pre-registered)
* P1 (at least 4 of 7 decided by a rule): **held** (5 outright, 2 as default plus a laboratory question).
* P2 (R2C01 follows RULES 1 and 6): **held**.
* P3 (R2C09 follows RULE 3): **held**.
* P4 (C30 laboratory-only under RULE 5): **held in part**: the extension is laboratory-bound, but RULE 2 gives a default (keep the list).
* P5 (C35 moves a number and needs the blind check; R2C10 two-sided retained): **held** (P5 not edited; the cohort condition's direction is stated as a separate labelled statement).
* P6 (an unforeseen rule consequence): **held** (the five against six and two count, and the open band of P5).

## Blind check (on the two number-moving choices, C35 and R2C01)
A delegate of a different model (requested `opus`, briefed at effort medium, not read back) received only the frozen priors and V2 and two questions, without my answers and without the current text. **R2C01: agreed.** Every inequality clause of the frozen priors puts exactly 0.7 and 1.43 in the genotype-specific class; the file is self-consistent only if P5's 'between' is the open interval; 'outside 0.7 to 1.43' differs from the complement at the endpoints unless the open reading is fixed. It added the two notes above (reciprocal rounding; point or interval), kept as undecided notes. **C35: agreed.** From V2 alone: wild type at one age k = 6 (ethosuximide x2, flat-profile panel x2, rising-profile panel x2); knockout and heterozygote at the assay age k = 2 each; at n = 11 the vehicle is 26.9 (k = 6) and 15.6 (k = 2) animals, the adjusted levels 99.17% and 97.5% (99% at V2's own five), total 353.9 (355 with vehicles rounded up). It found that V2 itself says five (item 7) and about 300 animals (27 cells at 11, the square-root rule not applied), the same inconsistency with the sizing count. It raised an alternative count per agent (k = 3 and 1) that V2 does not state; not adopted, because V2's cell total counts exposures. My own arithmetic matched before I saw the delegate's.

## Limits
The rules are mine (six, fixed before the cited sentences were opened, after I had seen the option lists) and every decision is labelled INFERENCE; no laboratory has read them. The two undecided notes in D05 stay with ADV or IT. No dose is stated anywhere.

## STOP RULE (ADV, binding) and CHOICE
* After this step the brief closure work stops until the operator names a laboratory or a new source changes a number. What remains is laboratory-facing: the blood volume, the primary exposure, and the other design-team lines a collaborator reshapes.
* **Next verifiable question:** after IT integrates D01 to D07, a reader sees no SCI-owned CONFLICT-OPEN marker and the SCI-owned OPEN-GAPs are only laboratory questions.
* **Rejecting observation:** a laboratory whose arm list gives a different count per session would change k (the rule recounts, no text change); a laboratory that cannot supply the P7 blood volume for the union would split the add-on (stated in D03).
* **What unblocks it:** the operator naming a laboratory.
