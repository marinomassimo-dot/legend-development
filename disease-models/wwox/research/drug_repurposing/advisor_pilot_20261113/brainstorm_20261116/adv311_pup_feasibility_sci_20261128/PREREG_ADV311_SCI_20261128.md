# ADV-311 pre-registration (SCI, window 64fc909a)

Frozen 2026-11-28T08:00:55Z. Assignment: ADV message 2026-11-28 (key pup-brief-feasibility-arithmetic-from-held-genotype-frequencies). Hypothesis level; arithmetic only: no dose, no breeding advice beyond arithmetic, no cost; held sources only, no contact, no spend, no address sent anywhere; PMID 42422765 unopened. **Seen before freezing (disclosed):** the Cheng 2020 sentence with the two frequencies (supplementary methods, page 3) and the genotyping-age sentence (page 2), the Results statement that some severely affected embryos died before birth and that knockouts survive less than a month, and the brief's own sizing paragraph (PUP_BRIEF_V2 section 3: n scenarios and litter counts). **Not seen:** the genotype-frequency, Mendelian-ratio or survival text of Ludes-Meyers 2009, Repudi 2021 (Brain and EMBO Mol Med), Hussain 2019 and 2023, Mallaret 2014, Aqeilan 2008 and any other held line.

## Fixed inputs and definitions
* f = fraction of homozygous knockouts among genotyped pups from heterozygote intercrosses: Cheng WD1 0.051 (N = 177, so 9 knockouts), WD234 0.065 (N = 785, so 51); Mendelian 0.25.
* Litter size L = 7 (the brief's own assumed value; no held source gives another; sensitivity L = 5 and 9 shown). Knockouts per litter = L x f: 0.357, 0.455, 1.75.
* Litters needed for n knockouts = n / (L x f). Pre-genotyping loss is a separate unknown u (fraction of knockouts gone before the first genotyping): the birth frequency would be f / (f + (1 - f)(1 - u)... ) not computed; it is reported as "not recoverable" unless a held source states it.
* Knockout counts taken from the brief: pilot 6 to 8 per cell (stage 1); 11, 31 per arm (simple effect, SD 0.3 and 0.5); 36 to 109 per arm (ADV-061 addendum, ratio 0.7); interaction 22 per cell, 44 knockouts (ADV-061, SD 0.3) and 180 to 320 per cell, 350 to 630 knockouts; whole plan 33 to 150 knockouts. Stage 2 (ethosuximide) uses two knockout arms (vehicle and drug); the brief's planning totals use three knockout arms.
* An alternative preparation: any held line with its own frequency, the neuron-specific Repudi 2021 Brain line first.

## Two explanations
* **E-A (pre-genotyping loss):** knockouts are lost before P5 to P12, so the frequency at the experimental age cannot be recovered from the Cheng sentence; the birth frequency is higher and unknown.
* **E-B (stable P5 to P12 population):** the 5.1 and 6.5 per cent are the population present at the genotyping age and later ages are bounded above by it (knockouts die by about 3 to 4 weeks).
**Rule for support:** E-A is supported if a held source reports prenatal or perinatal loss, a sub-Mendelian frequency near birth, or embryonic lethality in a comparable germline-null line; E-B if a held source reports a near-Mendelian frequency at birth (P0 to P2) and a fall by P5 to P12 or later; **undetermined** if neither (then both bounds are carried).

## Predicted observable
Which of the brief's knockout arms need more than 20 litters: at 20 litters of 7, WD1 yields 7.1 and WD234 9.1 knockouts. **Prediction: every knockout arm of 10 or more animals needs more than 20 litters under both frequencies (11 per arm: 31 and 24 litters); only the pilot at 6 to 8 per cell stays within about 20 (17 to 22 litters under WD1, 13 to 18 under WD234); the 3-arm plan of 33 knockouts needs 92 and 73 litters; the interaction numbers (350 to 630 knockouts) need 980 to 1,760 and 770 to 1,380 litters.** This holds under E-A and E-B alike (the observed frequency is at best an upper bound at later ages), so the observable does not separate the explanations; what separates them is the held-line evidence above.

## Strong counterexample sought
A held germline-null or conditional line with a knockout frequency near Mendelian (at least 20 per cent) at genotyping: it would show the Cheng frequency is specific to its strain or background and not a property of the Wwox-null mouse.

## The number that makes the brief infeasible as written
I fix it at **9.4 per cent** (33 knockouts, the brief's own three-knockout-arm planning minimum at 11 per arm, over a ceiling of 50 litters of 7): below f = 33 / (50 x 7) = 0.094 that planning minimum needs more than 50 litters. The ceiling of 50 is my choice, stated here and not from a held source; the table also gives the frequency at which the same minimum needs 20, 25 and 86 litters (86 is the brief's own upper planning bound). Both Cheng frequencies are below 9.4 per cent.

## What changes
The brief stays executable as written, shrinks to a different preparation, or is parked with the registered missing observation (genotype frequency at birth by strain and background, from the laboratory's own colony).
