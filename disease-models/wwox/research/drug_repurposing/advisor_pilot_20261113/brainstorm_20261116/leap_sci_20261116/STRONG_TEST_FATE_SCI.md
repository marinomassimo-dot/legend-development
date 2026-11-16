# Strong-test fate: IT's frozen thresholds executed on held data (SCI, 2026-11-16; non-canonical)

**The strong-test metric says how many hypotheses were ever testable on held data, not how many were right.** Of 31 rows (the 29 hypotheses and the planted pair), the setter, who saw only table names, marked 9 as rejectable on held data and 22 as not; those 22 are U by construction. I executed the 9 thresholds as written (`test_setting.tsv`, sha256 30f6109f...1f61, checked): **R 2, N 4, U 25.** Per row: `STRONG_TEST_FATE.tsv`; every measured value: `strong_test_output/strong_test_values.tsv`; script `strong_test_run.py`.

## The two numbers
| | R (threshold met) | N (executed, not met) | U |
|---|---|---|---|
| (1) strong-test category, 31 rows | 2 (M08, M29) | 4 (M04, M11, M17, M30) | 25 (22 by construction + M10, M12, M23 partial) |
| (2) setter: could held data reject it | yes 9 | no 22 | |
Of the 9 'yes' rows, 6 were executed in full (M04, M08, M11, M17, M29, M30) and 3 only in part (M10, M12, M23): so 6 of 31 were fully testable on what is held, and 2 of those 6 were rejected.

## What each executed row found
* **M08 R** (maturation axis, the organoid projection): Spearman of observed against projected change is -0.71 over seven genes (threshold <= 0); GRIN2A +1.11 against a projected -1.66, SLC12A5 +0.73 against -0.14. The other two branches of the OR are not met (4 of 7 agree; 2 of 4 named genes opposite).
* **M29 R** (the Snap25-positive fraction): control 0.729, knockout 0.760; the knockout fraction is higher, and the rule rejects at a difference >= -2 SE (-0.022). A census of two pools only.
* **M04 N**: Mbp 0.25 and Mobp 0.22 of control in the hippocampal null contrast; the rule rejects only if both are >= 0.80 in both regions.
* **M11 N**: valproic acid is negative in 4 of 4 neuron-like signatures and its family value ranks 29 of 256, outside the central rank 65 to 192.
* **M17 N**: the S-line cortical Npy rise (log2 0.96) is smaller than the hippocampal (2.52): difference -1.55, rejection needs >= -0.5.
* **M30 N**: neuron over astrocyte FPKM is 0.31 and 0.06 (mouse Slc6a1, Slc6a11), 1.56 and 0.24 (human; one neuron library); none reaches 2.

## Partial executions (reported as such; categories are U)
* **M10 (mTORC1):** branch 1 is NOT met (P47T hallmark NES 1.54 to 2.06, q <= 0.0085 in all four regions, IT12 reimplementation); branch 2 (organoid enrichment after composite adjustment) cannot be computed: the hallmark gene set is not on this host and no organoid hallmark result is held. DEVIATION, not scored: with my own declared 25-gene panel as a stand-in, branch 2 would read as met (organoid median -0.11, p 0.21). The setter's wording also presupposes an organoid enrichment that does not exist.
* **M12 (ErbB4):** the P47T half of the AND is met (Erbb4 ratio >= 0.90 in 3 of 4 regions); the table-3 half is not testable (Erbb4 sits below the committed table's |cLFC| >= 0.585 cut and no cortex null contrast exists), and R needs both.
* **M23 (timing of development):** the rule needs at least 4 children with documented pre-treatment imaging; the table states it for 2 of 6. Under the lenient reading (all six first imaging findings) it is N (2 contradicting, 4 confirming).

## Limits (read before using the counts)
* One reader (me) executed everything; IT second reads. I propose the six rows where a reading choice decides: **M08, M10, M12, M23, M29, M30.**
* **Recognition:** I pre-tested all 29 hypotheses earlier today, so I recognised the content of most rows. I recognised my own five with certainty (M09 = HSCI-2, M17 = HSCI-5, M20 = HSCI-1, M21 = HSCI-3, M22 = HSCI-4; column `sci_recognised_as_own_item`); I know the other rows by content but do not list them, since IT holds the key. No threshold, direction or reading was changed because of that; the setter fixed the thresholds before any table was opened by anyone for this purpose.
* The setter's own declared limits stand (11 rows with no labelled rejecting observation, M23 self-contradicting, three partial tests of the first disjunct of an 'or'), and a partial test of one disjunct cannot reject the whole OR: M04, M12 and M17 test one disjunct each.
* Pool tables carry no variance; the committed mouse table is the |cLFC| >= 0.585 file only; transcript is not function. R here means a transcript-level threshold was met, not that a mechanism is excluded.
* The two R rows say a held table could reject and did; the 22 'no' rows say nothing about truth, only that no held table speaks to them: the reach of held data is the finding.
