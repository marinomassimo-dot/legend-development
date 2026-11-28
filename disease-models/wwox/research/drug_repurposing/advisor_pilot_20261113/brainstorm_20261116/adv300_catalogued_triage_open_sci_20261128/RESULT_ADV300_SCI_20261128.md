# ADV-300 result: abstract triage of catalogued-only records, second increment, openly readable part (SCI, window 919d2041, 2026-11-28; hypothesis level; reference genotype class; not medical advice)

PREREG `PREREG_ADV300_SCI_20261128.md` (sha256 cfa368d0004c3d09192b4e800679f1bd43685f5f605ce44cf649ffcaaff09057, commit 23e93eb18, frozen before the route test and before any record was drawn). Draw `draw_adv300.py`, seed 202611282 (output `DRAW_ADV300_SCI_20261128.txt`, route table `ROUTE_TEST_ADV300_SCI_20261128.tsv`, commit 92c7bf176, before any abstract).

## Verdict

**Not decidable, under both readings.** Fewer than 7 of 10 records reached a full-text check. ADV accepted this and stops sampling the tail; the tail is read at depth instead (ADV-302).

| | PREREG reading (primary) | Record 4 not counted |
|---|---|---|
| Records checked in step B (floor 7) | 6 | 5 |
| Misses | 2 (records 4 and 6) | 1 (record 6) |
| Confirmed calls | 3 (records 1, 3, 5) | 3 |
| Readers disagree, listed apart | 1 (record 2) | 1 |
| Outcome | not decidable | not decidable |

Why two readings: one response of the batch 2 reader was withheld by a safety classifier after it had read record 4's supplementary text; the reader went on and returned both records. The PREREG says unreturned records are not checked, so record 4 counts; ADV's later wording could be read as dropping it. Fixed with ADV before any blind check: PREREG primary, both shown, a flip means not decidable.

**Said plainly:** under the primary reading two misses were observed, which is the count the rejecting observation names ("two or more misses: abstract-only triage is not safe"). The frozen floor of 7 checked records overrides it, so no rejection is claimed.

## What the route test found

* Pool: 191 catalogued-only records without a receipt, 184 after leaving out ADV-297's ten and the excluded PMID; 5 without exactly one PMID; 179 tested.
* 65 have a PMCID; **39 passed** (all by NCBI efetch with a body; none held already). 114 have no PMCID.
* So the question could only ever be answered for 39 of 184 records, about one in five. Europe PMC `fullTextXML` answered 500 for 22 PMC records without an efetch body and timed out for 3: results, not retried.

## Step A (abstract and metadata only)

READ-NOW 0, READ-LATER 9, DISCARD 1 (record 5). With one DISCARD the parking observation (zero misses with seven or more DISCARD) was already unreachable after step A.

## The ten records

| Draw | PMID | Step A | Outcome |
|---|---|---|---|
| 1 | 43036373 (commentary, no abstract) | READ-LATER | checked: no datum met the rule (confirmed) |
| 2 | 20535528 | READ-LATER | checked: one borderline datum, blind reader disagreed (apart) |
| 3 | 29662317 | READ-LATER | checked: no datum met the rule (confirmed) |
| 4 | 28769061 | READ-LATER | checked: **MISS** (record counted under the PREREG; see above) |
| 5 | 25710931 (review) | DISCARD | checked: no datum met the rule (confirmed) |
| 6 | 35563688 | READ-LATER | checked: **MISS** |
| 7 | 25295115 | READ-LATER | not checked: reader stopped by a safety classifier |
| 8 | 29845204 | READ-LATER | not checked: same reader |
| 9 | 30211123 (review) | READ-LATER | not checked: reader stopped by a safety classifier |
| 10 | 32606933 | READ-LATER | not checked: same reader |

Records 7 to 10 were not retried, not re-dispatched, not given to another model and not read by SCI. Reviews, apart: record 5 checked with nothing, record 9 not checked.

## The two misses

* **Record 6 (35563688), bladder cancer lines.** Stable WWOX overexpression lowers total GSK3β protein (GAPDH-normalised), WWOX/control 0.32, 0.52 and 0.87 in RT-112, HT-1376 and CAL-29. Changes CLAIM 016's sentence that the causal statement moves from "elevated" to "de-repressed": an abundance effect is measured too, under gain of function in cancer cells. SCI checked the printed means, ratios and the triplicate statement in the text. Both readers note that in CAL-29 the raw band is higher with WWOX and the fall comes from the normalisation; SCI did not view the figure.
* **Record 4 (28769061), lncRNA PARTICLE.** Knockdown raises and overexpression lowers WWOX mRNA. Adds a fourth lever on the endogenous WWOX transcript to a sentence that lists three. SCI checked the main text: the figure 3 legend says U2OS, the Discussion says MDA-MB-361. **Limit for this record:** its blind check saw the main text and Figure 3 only, by ADV's instruction; no supplement and no sequence material. The first reader's second datum (a predicted site cluster in intron 8) rests on a supplement table, had no blind check and is not counted.
* **What the abstracts hid.** Record 4's abstract states the inverse change in WWOX transcripts, and record 6's states WWOX-dependent targets in bladder cancer lines. Both step A calls were READ-LATER by the rule's non-neural clause. The step A reader had said what each full text could hold.
* **Weight:** narrow. Neither reverses a conclusion, need, card direction or ranking. Both are non-neural cancer-cell data.

## Departures from the PREREG

* Open supplements and figures were fetched where Europe PMC or the PMC open-data bucket gave them. Records 1 and 2 have no figure and no supplement. Record 8: Europe PMC answered 500; its figures came from the bucket, which lists no supplement.
* Step B readers got figure images where available. One batch 3 reader listed the scratch parent folder and saw report file names without opening them; the earlier reports were then moved out before batches 4 and 5.
* Disk fell to 0.94 GB once (06:28Z, other sessions' pushes); batch 2 was already running and was left to finish; no dispatch until `df -h` showed 1.5 GB.

## Delegates

All legend-delegate, claude-sonnet-5-5, effort high on every model turn read back. One at a time. Step A, five step B batches, two blind checks.

## Side findings (see `SENTENCES_FOR_IT_ADV300_SCI_20261128.md`)

A held status line is stale (TS-01 says PMID 43036373 was not read); two ledger lines still place P282A in the SDR domain against a later correction on the same files; record 3's rs3764340 may be P282A (identity not stated in the paper, not verified here).

## What this says about the method, not about the tail

Two draws in one day were both lost partly to safety classifier stops (ADV-297: three records; ADV-300: four records and one withheld response). Full-text reading of this tail by delegates loses records that way; a plan with a frozen minimum should assume it.

## Limits

One draw, 6 checks, one model family for every reader. Counts are not a rate. The ADV-297 and ADV-300 rule wordings differ, so the draws are not pooled.
