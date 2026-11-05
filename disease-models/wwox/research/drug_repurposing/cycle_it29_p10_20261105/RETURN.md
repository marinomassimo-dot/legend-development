# IT29 P10 steps 5 and 6: return, consumers, next step (2026-11-05)

Non-canonical working record, not medical advice. Public edition, WWOX-DEE reference genotype class.

## Row counts recomputed from the TSVs (not from the READMEs)

| Reader | Rows (TSV) | Ragged rows | By direction (fav / adv / null / ctx / undet) | Receipts | README claim |
|---|---|---|---|---|---|
| F | 9 | none (20 cols) | 1 / 1 / 1 / 2 / 4 | 7 | 9 rows, same split: matches |
| G | 22 | none | 2 / 9 / 6 / 1 / 4 | 5 | 22 rows: matches (README gives no split) |
| H | 11 | none | 1 / 2 / 1 / 1 / 6 | 6 (+3 abstract-only without receipt) | 11 rows: matches |

Total 42 rows, 18 receipts (the host's figure). Depth: F and H are all partial_fulltext or abstract; G has one full_text and three abstract_only. No row claims more than it read.

## Pre-registered consequence table v what came back

| Pre-registered row | Came back? | Outcome |
|---|---|---|
| CNS or neuronal class IIa loss/inhibition adverse for myelin | No | Not met. Nearest: MC1568 after rat stroke, MBP down with larger lesion and deaths (F08, G18, H01): compound-only, no target control, viability confounded, authors read it as secondary to neuron loss. A weak lead, not a sign. |
| Null / neutral in CNS | No | Not met. No CNS class IIa deletion with a myelin readout exists; Nes/Thy1-Cre Hdac4 deletion (23239283) never examined myelin, so it is silent, not null. |
| Nothing found | Yes | MET for CNS oligodendroglia (F) and for the neuron/axon route (H), after bounded search. The "HDAC4 / HDAC5 in CNS oligodendroglia" row stays empty, dated 2026-11-05. |
| Favourable | No class IIa case | One favourable row each in F (Schwann culture gain-of-function, F03), G (two) and H (Scriptaid, class I/II, abstract only): none class IIa-specific and CNS-relevant; recorded as undetermined, no promotion. |
| PNS wording (the one change I did not pre-register) | Yes, three readers agree | The carried sentence is wider than its source. Hdac4+Hdac5 (or +Hdac7) joint Schwann loss gives a transient delay, recovered by P8 and normal in the adult; single deletions null or subtle; mechanism scaffold (NCoR1/SMRT-HDAC3, Mef2-independent). I had pre-registered "keep PNS wording explicit"; the stronger result is that "required" is not supported even in the PNS. |

## Consumers: does the return change anything?

| Consumer | Edit made by the host | Changes anything? |
|---|---|---|
| `generation_it22_p1_20261103/decision_scope_it22.tsv`, `IT21P2-0006` `target:HDAC5` class_limit | IT28 "required" text replaced by the transient peripheral delay, scaffold, no CNS datum | Yes, in wording only. A carried limit, never a veto, so eligibility (220) and hand-overs (15) should not move. Not yet reflected in the generator: `results_s10` (written 09:54:23) still carries the old text (20 hits in `proposals_it21.tsv`, 1 in `handoff_it21.tsv`; scope table edited 10:02:02). Pending regeneration; verify before calling it consumed. |
| `signed_rows_case1_it29.tsv` S1-29, S1-30 | note extended; direction stays `context_dependent` | Text only. Note that G proposes "adverse, transient, adult null" for B38; the table keeps `context_dependent`, which is defensible and conservative. No signed class IIa row enters, so the comparison with the abstaining search layer is unchanged. |
| `p3_B/README.md` | dated note under the empty CNS row | Documentation only; row remains empty. |
| `SELECTION.md` | "needed for myelination" changed to "possible opposed evidence" | Corrects a statement that its cited sources did not contain (LOG #4). |
| Ranking, investigations_it20.tsv, the four scientific current files | none | No HDAC5/class IIa row exists in the investigations view; nothing to move. Not touched. |
| Challenge `CH-IT29-CLASSIIA-CNS-MYELIN` | `challenge_batch.py check`: all three `returned` OK | Return proven; `reevaluate_when` still stands. |

## What the return should NOT be used for

* Not as evidence that class IIa inhibition is safe or neutral for CNS myelination: "nothing found" is absence of data. The search itself had a hole (H: Europe PMC 503s, NCBI 500s, PubMed MCP Boolean queries empty; PubMed-native count unverified).
* Not as a pro-myelinating sign for any class IIa compound, nor as a veto: no signed CNS row exists either way.
* Not as a catalytic result: the Schwann mechanism is scaffold via NCoR/HDAC3 (a class I enzyme), so it neither supports nor refutes a catalytic class IIa inhibitor (TMP269). H08 words it as "needs ... deacetylase activity" from a secondary account; G and F read the primary source and say the HDAC4 catalytic site was not tested. Prefer G/F.
* Not as an HDAC3 clearance: the same scaffold route runs through HDAC3, and class I/HDAC3 loss is adverse for oligodendrocyte maturation (p3_B). Compounds that reach HDAC3 keep the class_limit.
* Not for MC1568 or TMP269 selectivity claims: nobody checked selectivity (H).
* Not to read G19 (Ncor deletion raises oligodendrocyte genes in neural stem cells, in vitro) as class IIa evidence.
* Hdac7/Hdac9 expression along the oligodendrocyte lineage was not searched (F); compensation in CNS is untested.

## Step 6: next useful step

**Chosen: close the loop on the generator, then stop reading on this question.**
1. When the host's S10 regeneration finishes, run the existing stage test and confirm: the 20 + 1 old-text hits become 0, `eligible` stays 220, hand-overs stay 15, only `carried_limits` text changes (same control as IT28 P5). Needs: the finished regeneration, `generation_it29_p5_20261105/test_stage_it29.py`, a diff of the two stages. If anything beyond `carried_limits` moves, that is a defect in the change, not a result.
2. Do not launch a second reading wave: the pre-registered trigger (an unreachable decisive text or a contradiction between readers) is not met; the readers agree on every point except H08's wording, resolved in favour of the primary-source readers. The reopening measurement is not a reading: Olig2/Sox10/Cnp-Cre Hdac4+5(+7/9) deletion with CC1/MBP/g-ratio, or a class IIa compound against a Hdac4/5/7/9 knockout control in purified OPC culture, plus a neuron-conditioned arm because the WWOX driver is neuronal. That has a cost, so it is an operator decision.
3. Record that measurement as an arm of the existing HDAC5 neural experiment in `CH-IT28-HDAC5-LEVER` (human neural cells with catalytic-dead rescue and TMP269): add an "OPC differentiation readout, with and without neuron conditioning" line to the `batch_it28_p3_hdac5_20261105/README.md` experiment paragraph, since the cell system and compounds are shared. Needs: a dated edit, no new reading, no change to the ranking order digest.
Not chosen: a Hdac7/9 atlas search (low yield, transcript context only) and the Wong 2018 interneuron lead (needs a measurement in Wwox tissue).
