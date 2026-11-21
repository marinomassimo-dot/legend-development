# RP-041 blind second reader: result

Model sonnet, effort high (as stated at dispatch). Sources: Document A (pup brief v2), Document B (original brief with dated lines), QUESTIONS_ONLY.tsv only.

## Answer first

Of 85 questions: **ANSWERED 7, PARTLY 60, NOT_ANSWERED 18, UNCLEAR 0.**
Most questions are not wholly unanswerable: for 60 the documents give part of the answer, or two texts disagree. Only 7 are fully answered in the text, so the first reader missed little. Per-question detail is in VERDICTS.tsv.

## ANSWERED (where the first reader missed something)

- Q24: the T-type arm sits in the stage 2 row but is listed as optional ("Optional: the T-type arm (needs an engagement control), stage 3, stage 4, and the add-ons of section 5", A section 3, "If resources allow only one step").
- Q29: heterozygotes are in the vehicle and ethosuximide cells at the assay age, in "all genotypes" for lithium, and not in the interaction ratio, which is R(-/-) over R(+/+) (A section 3 totals; A 2.7).
- Q38: Cheng 2020's test age is not stated, only "preweaning" ("the test age is not stated", A section 1); the assay age is the laboratory's.
- Q47: sex is recorded; no balancing or stratification is specified (A 2.1; A 5(h)). Borderline: it is an answer by absence of any balancing rule.
- Q58: yes, one cohort can carry all of it (B 9.13: "A single animal cohort can carry all of it").
- Q59: both the heterozygote latency and the conduction endpoint are optional add-ons, conduction "not yet an endpoint" (A section 5 header, 5(f), 5(g)).
- Q72: litter bootstrap is primary; fewer than 10 litters in a cell requires a permutation test or a mixed model with litter random effect (A 2.7).

## NOT_ANSWERED (18)
Q13, Q14, Q20, Q36, Q41, Q45, Q48, Q51, Q55, Q60, Q63, Q65, Q68, Q69, Q71, Q75, Q78, Q80.
(Q14 is explicitly left to the laboratory: "no dose, no schedule of our own".)

## Text conflicts I found while testing (PARTLY verdicts)
- Two different "9.12": A's appendix counts its dated correction to 9.11 as 9.12 ("binding"); B has a separate "Dated line 9.12" (2026-11-21, calcium add-on). Neither document notes it (Q03).
- A section 1 sizing flag: "176 animals for one drug against vehicle, 88 of them knockouts" and "75 litters ... about 132 fragile knockouts" in one passage; section 3 says 75 litters = three knockout arms and 25 litters = one drug (Q33). Also "44 per cell" interaction in section 1 against "twice" the simple-effect number in the ADV-061 paragraph (Q31).
- Stage 1 (pilot) row lists vehicle pups only but its stop rule refers to the panel agent (Q19).
- A 2.3 keeps "the window to about P28" after A 2.2 dropped B's definition of "ADV's working window" (Q40).
- Knockout death "about 4 weeks" (A 2.2) against "about day 17" (A section 7, comparator's panel) is not reconciled in the text (Q37).
- B body not rewritten for later dated lines (B 6.3 still lists diazepam ontogeny as "not found"; B 2.9 still calls the regimen a design variable) while A carries the changes (Q04).
- "Stage" means a seizure grade (0 to 6) and an experimental stage (0 to 4) with no terminology note (Q83); "comparator" means the non-GSK-3 anticonvulsant and the AAV9 comparator (Q85).

## Questions I would add (not in the list)
1. Which lithium salt, vehicle and route are to be used in the Cheng 2020 replication condition, and are the three injections evenly spaced within the hour?
2. What feeding and thermal state should pups be in at the time of the 60-minute observation (maternal separation, time since last milk, temperature, time of day), given that the documents note low blood glucose in null pups by P14?
3. Must the laboratory adopt the 0 to 6 scale as defined in the brief (stages 3, 4, 5 and 6) or may it use its own validated scale and map it?
4. Are pilot animals and pilot data reused in the main analysis, and who signs off the pilot's choice of age, stimulus and summary before the main run starts?
5. Does a stage stop rule (pilot, or panel invalid at the assay age) end only that stage or the whole experiment, and who is informed?
