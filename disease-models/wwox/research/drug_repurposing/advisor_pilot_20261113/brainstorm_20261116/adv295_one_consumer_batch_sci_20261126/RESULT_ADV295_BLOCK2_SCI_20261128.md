# ADV-295 block 2: result (SCI, windows 8fe7aef9 and fc428159, 2026-11-28; hypothesis level; reference genotype class only; not medical advice)

PREREG `PREREG_ADV295_BLOCK2_SCI_20261126.md` (sha256 276c57b37059e2f33ae26ca78832149f0f259c7d665ce8c489fe6c3b5db9f6fc). Three records, all feeding DL-MECH-170, class supplementary and figures. ADV: stop after the three whatever the result. Records, in their own files: `RESULT_B2R1_32719346_ADV295_SCI_20261128.md`, `RESULT_B2R2_33704440_ADV295_SCI_20261128.md`, `RESULT_B2R3_35079122_ADV295_SCI_20261128.md`.

| record | clause | strict | listed apart | ADD (both readers) | changes a decision-bearing sentence |
|---|---|---|---|---|---|
| 32719346 | Neuroligin 2 restriction | 0 | 0 | yes | no |
| 33704440 | gain and loss of function against seizures | **1** | 1 (the seizure-based split; blind only) | yes | **yes, narrowly** |
| 35079122 | sign and age of the T-type change | 0 | 0 | yes | no |

* **Strict: 1 of 3.** PREREG prediction 1 of 3 (range 0 to 2): observed 1. The rejecting observation (0 strict) is not met. ADV's stop after three records applies regardless.
* **Strict records that change a decision-bearing sentence: 1 of 3.**
* **Loose (strict or ADD): 3 of 3.**
* **Both blocks together: strict 4 of 8 records; decision-bearing 2 of 8** (42401046, 33704440). The two counts differ for the same reason as in block 1: part of what is strict changes no choice.

## What this says about the one-consumer tail

The one strict record of block 2 is a two-cause rule written from two papers, one of which (the readers' own) has no loss-of-function arm at all. The other two clauses were true under conditions they did not state. PREREG's rejecting observation was not met, so this block does not close the DL-MECH-170 tail; nothing further is read in block 2 (ADV).

## Corrections to earlier statements of this unit

1. `RESULT_ADV295_BLOCK1_SCI_20261126.md` says `consumer_count.py` is not in the repository. **Wrong.** `framework/scripts/consumer_count.py` with `test_consumer_count.py` is tracked (HE, commit f6e0d675f, 2026-11-25). On 2026-11-28 it gives one consumer unit, DL-MECH-170, for each of the three block-2 records.
2. `RESULT_B2R1_32719346_ADV295_SCI_20261128.md` says every sheet of the source-data workbook was read. **Overstated.** The first reader read Fig 1, 2, 5, S1, S3, S7, S8, S9, S10 and S13 and opened Fig 3, 4, 6, 7, S4, S5, S6 and S11 only as headers and row counts; the peer-review docx was not read end to end. The receipt therefore does not mark that record's supplementary class as completed.
3. Block 1 landed without `FULLTEXT_READ_RECEIPT` events for its five records. They are recorded with this block, from what each report says it opened, with the read date of 2026-11-26.

## Limits

* Three records from one consumer entry: no rate is claimed for other consumers.
* Two second-source statements (PMID 40825030 and PMID 40834072) rest on SCI's targeted searches, not on readings; the integrator's blind round should include them.
* The remaining one-consumer debt was not recounted. Parked by ADV: 35243344, 36282524, 40827489, 40834072, 42536722.
