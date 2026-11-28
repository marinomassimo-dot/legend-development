# Corroboration-independence batch, IT44 (2026-11-28; hypothesis level; not medical advice)

Input: SCI BI's RESULT (`../corroboration_independence_sci_20261128/RESULT_CORROBORATION_INDEPENDENCE_SCI_20261128.md`): 23 multi-source
sentences, 10 BLOCKED-SKIP (not checked), 13 checked. SCI edits nothing; this batch (`BATCH_20261128_014`) is the edit.
Rules as ADV-339: record-scoped edits, UNSETTLED gets a dated pointer and no change to the sentence, second reader on the text,
no ranking, need or candidate-state change.

## What was edited and what was only pointed at

| claim line | SCI / second reader | action |
|---|---|---|
| CLAIM 014 evidence boundary («multi-paper convergence») | HOLDS / FAILS (judgement call) | edit: one collaboration; only PMID 32581702 observes development before birth in its own material |
| CLAIM 030 severity sentence («Steinberg … independently») | HOLDS | edit: Steinberg poses a question; family identity not stated; «(null)» read from the genotype |
| CLAIM 030 corroboration paragraph | FAILS | already repaired in `BATCH_20261128_013`; no second edit |
| CLAIM 036 qualification («reproduce early systemic collapse») | HOLDS (one lab line) | edit: three records are one laboratory line; independent pair is with PMID 19936220 |
| CLAIM 025 «confirmed in vivo» | UNSETTLED | dated pointer only |
| CLAIM 028 «multi-paper convergence (207, 218, 206, 214)» | UNSETTLED | dated pointer only |
| CLAIM 036 rat half (two independent negatives) | UNSETTLED | dated pointer only (rat texts not held) |
| CLAIM 038 «misura convergente» | UNSETTLED | dated pointer only (PMID 17803050 not held) |

Not touched: K10, K11, K13, K20 (HOLDS), K02 (declares its own limit). The 10 BLOCKED-SKIP sentences remain unchecked.

## Blind reader on the composed text
`legend-delegate`, sonnet, effort high, atoms and PMIDs only (no old sentence, no earlier grade), sources in `files/fulltext/`.
16 atoms: **13 SUPPORTED** (A1-A6, C1, C3, C4, D1, D3, D4, D5), **1 NOT SUPPORTED as worded** (A7, «PMID 31543760 contains no in vivo
brain observation»: the paper has an atlas expression comparison, Fig 1, fetal 20-33 weeks vs adult; my final text says «atlas
expression comparison» instead), **2 UNSETTLED** (C2 «same family as PMID 24369382»: the main text cites Mallaret for the mutation and
never says «same family»; D2 «PMID 18974271 restates earlier work»: the held XML is front matter and abstract only). Both unsettled atoms
are written as what the reader could see: C2 as «cited to PMID 24369382, family identity not stated», D2 as «the abstract presents
lethality and bone-growth defects as the group's earlier finding». Atom A5 reworded to the reader's own finding (BrdU at E16.5 in dams,
pups examined at P1). The reworded sentences were composed from the reader's locators and were not sent a second time: a limit.
Other disclosures: PMID 32581702's Methods name one control fetus and its Results say three (not used); PMID 23254685's Discussion
says that Ludes-Meyers 2009 already reported the same conditional-allele lethality and bone defects (it compares its mice with them).

## Rates (denominator stated)
* Batch: 7 record-scoped operations in 6 claims: 3 edits of the sentence (014, 030 severity, 036 qualification) and 4 dated pointers (025, 028, 036 rat half, 038), from 13 checked sentences.
* Composed text: 1 of 16 atoms not supported as first worded, 2 of 16 unsettled; 13 of 16 held as written.
* SCI's checked sentences: 2 of 10 graded failing (K16 known beforehand; K04 by the second reader's judgement call).

## Calibration
Predicted failing share about 35 percent (prereg); observed 10 to 20 percent (SCI 1 of 10, with the second reader's K04 2 of 10; this
batch's atom check 1 of 16 as first worded). The prediction was too high for sentences that name papers; the weak points were the
sentences that name no source (K12, K14: placeholders) and the shared-author collaborations that the first/last rule does not see.
Disclosed: the 10 skipped drug/vector sentences are outside this rate.

## Source artefacts (HE's hunt, 2026-11-28)
PMID 23254685: the receipted HTML (`a83d0390…`) is absent; the PMC XML (`09901452…`) found in a verification scratch is now held as
`files/fulltext/PMID23254685_Abdeen2013_PMC3943428_nihms445139.xml` (provenance of the scratch not recorded; identity checked: PMID,
title) and carries a new receipt. PMID 17803050 and 19500159: absent, pointers written, bytes need the operator's browser. PMID
17360458: PDF present, HTML absent. PMID 18974271: the receipted HTML is not held under its name either; only the r2 XML (front matter and
abstract) is. The deepdive manifest of PMID 23254685 still names the absent HTML; no tool changes a manifest's source path (hand edit
forbidden): left to HE.
