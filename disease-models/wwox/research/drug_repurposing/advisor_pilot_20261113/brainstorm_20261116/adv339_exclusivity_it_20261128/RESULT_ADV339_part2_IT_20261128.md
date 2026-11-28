# ADV-339 part 2 — sentences 7 to 11 (IT41, 2026-11-28)

Hypothesis level; nothing here is medical advice. PREREG unchanged (`PREREG_ADV339.md`). Sentences from the enumerator's list in claim order: T1 CLAIM 005 (#48), T2 CLAIM 005 (#49), T3 CLAIM 011 title (#62), T4 CLAIM 011 (#68 and #69 joined: one blockquote the sentence splitter had cut), T5 CLAIM 011 (#72). Two readers, both sonnet at high effort, both with the complete source list (figures, supplements and PDFs searched by PMID first); the second blind to the first. Naming: in Repudi 2021 Brain the astrocyte line is G-KO, the oligodendrocyte line O-KO, the neuronal line S-KO.

| Sentence | First reader | Second reader | Agreed grade |
|---|---|---|---|
| T1 no seizure measure in the two-week mice; neuron-restricted deletion shifts astrocyte-activation transcripts at P17 | HOLDS | HOLDS (scope: "two-week mice" must mean Hussain's; Repudi S-KO mice P13-17 do have recordings) | **HOLDS** |
| T2 no Wwox in rat microglia; astrocyte-specific deletion scored only for delay, weight, survival | UNSETTLED (microglia atom not in the two papers searched) | HOLDS: the microglia atom rests on Tochigi 2019 (PMID 31340538, rat PND21 cortex and corpus callosum, Fig 6D, one antibody); astrocyte arm G-KO Fig 1M-O, no gliosis assay | **HOLDS**, with the microglia atom resting on a third paper and a narrow scope |
| T3 title: dose-grading demonstrated on expression, P20 glycaemia, motor score and NOT on survival, body weight, ECoG/SWD, myelination or gliosis | TOO_NARROW | TOO_NARROW | **TOO_NARROW** on two atoms (below) |
| T4 Fig 7E no low-dose arm; myelination never quantified in any treated arm; gliosis binary, no disease comparator, no KO+RI arm in the dose panels | HOLDS (flag: reads as a blanket it is false, S7B/D and S8I do have KO arms) | HOLDS (only "binary" is undefined) | **HOLDS** as scoped to S7F/H |
| T5 no untreated disease arm at P90; myelination UNRESOLVED, bytes absent on S7I; gliosis RESCUE at HD, NO_RESCUE at LD | TOO_NARROW | TOO_NARROW | **TOO_NARROW** on three atoms (below) |

## The failing atoms (both readers, same locators)
* **T3 "NOT on survival"** is contradicted: Fig 3B legend, HD vs LD survival "p < 0.0001", LD vs KO+RI "p < 0.0001", text "a clear dose-response relationship"; LD n = 20 all dead by about P78, HD n = 30 about 77 percent alive at P300. **T3 "demonstrated on expression"** is weak: Fig 5 has one `*` (hippocampal vector DNA), the other vector DNA panels and all mRNA panels ns (p = 0.08, 0.06 in two), protein "a trend". Body weight is UNSETTLED (no LD-vs-HD test in Fig 3C, curves apart at P20-25 and equal at P30). This is the title of CLAIM 011: **a decision-relevant wording, ADV's call**.
* **T5 "no untreated disease arm at P90"** holds for behaviour (the quote is in the Fig 4 section) but not as a blanket: Suppl S5A-D legend, "P90 in wild-type, untreated Wwox-null (KO) ..." with a KO lane per blot (also S5E-G at P180, S6A, S6H), in conflict with Fig 3B where KO+RI are dead by about P25 (a source inconsistency, not resolved here). **"Bytes absent" on S7I is stale:** S7I is in `supplement/PMID42422765_r2/mmc1.pdf` (page 9) and in mmc2; Fig 6F is `gr6.jpg`. **Iba1 NO_RESCUE at LD** has no test behind it (S7F, WT v LD ns); the GFAP labels hold (S7H, LD `**`, HD ns).
* Side findings (not atoms): Fig 7C plots 2 WT and 3 KO points with p = 0.2 while the legend says n = 5 and p < 0.05; the S7 legend lists `*` and `***` but panel H shows `**`.

## Rate across both parts (11 sentences; PREREG bands: E1 under 10 percent, E2 30 percent or more not holding)
| Reading | Sentences not holding | Atoms not supported (all readers' tables, not deduplicated) |
|---|---|---|
| Second readers' strict grades | **6 of 11** (55 percent): S1, S2, S4, S5, T3, T5 | part 1 second reader 4 of 44; part 2 second reader 4 of 39 (first reader 4 of 37) |
| Adjudicated firm (both readers agree the exclusion or title fails) | **3 of 11** (27 percent): S1 age atom, T3, T5 | |
| Reading-dependent or outside the rule | 3: S2 (literal vs WWOX-by-lineage), S4 (qualitative KO image), S5 (the failing atom is a literature count) | |
Under the bands the result is **undecided to E2**: more than E1 allows on every reading, between 27 and 55 percent. Arm assignments ("which line carries it") held in every sentence the sources could test; what failed was almost always a **scope word**: an age, "every", "only one study", a title list of "NOT on ...", a "by construction". The six-hold stopping observation was not met in either part.

## Repairs proposed (none applied; a BATCH_COMMIT after `test_batch_queue.py` only for decisions)
Part 1 repairs: see `RESULT_ADV339_part1_IT_20261128.md`. Part 2: **CLAIM 011 title (ADV decides; touches RP premises that cite it):** drop "NOT on survival" (survival is graded by Fig 3B) and "demonstrated on expression" (mostly ns), keep the other NOT-atoms, and name body weight as untested. CLAIM 011 line of T5: "no untreated disease arm in the behavioural study at P90" (not "no arm"), delete "byte assenti" (S7I and Fig 6F are held), state that Iba1 has no LD-vs-WT difference. CLAIM 005 T2: add "(Tochigi 2019, PMID 31340538, rat cortex and corpus callosum, one antibody)".

## Limits
Values are read from bars and boxplots. mp4 and xlsx not opened. The enumerator's borderline list and about 25 further counted sentences (CLAIM 013, 016, 017, 019, 025, 030 to 047) are unchecked; the net misses markerless exclusivity. T2's third paper was found by the second reader, not by the packet. This result is two readers per sentence, no third blind reading of the adjudication.
