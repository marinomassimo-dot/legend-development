# SCI score of the hashed forecast for the stage-1 checklist test (2026-11-18)

Non-canonical. The forecast file `FORECAST_CHECKLIST_TEST_SCI_20261118.md` is unchanged; its sha256 re-computed before scoring is `712a48fafff233d42e46dbd489c63be34022ce4063fe1f091eecda913483a2ca` (sent to HE and ADV at 00:20:40Z). Scored from the numbers HE reported (T7 only, a tuned-on target, two tool-free runs; HE scored, not blind). I did not read HE's output files for this score.

**Observed (HE):** zinc named as a lowering modulator in 2 of 2 runs (LOOSE); also carried into a step or hypothesis in 1 of 2 (STRICT); the Zn2+ item answered yes in both runs; 29 and 26 of 77 items answered yes.

**A scoring mismatch, stated first.** My table was written for four runs (counts 0 to 4) and my scoring rule was the natural-log probability the table gives to the observed count, against a uniform 0.20. The test that ran has two runs, so the committed rule cannot be applied literally. The numbers below are a mechanical rescaling that I fix here, after seeing the result, and so they are a post hoc reading, not the preregistered score: per-run rates taken from my expected counts (loose 1.2 of 4 = 0.30; strict 0.5 of 4 = 0.125), runs treated as independent, naive baseline uniform over the three counts 0, 1, 2 (ln 1/3 = -1.10). Independence is generous to my table: the runs share one target, and the observed pair is positively correlated.

| Line | My forecast | Observed | Probability my table gives | ln (nats) | Naive baseline (nats) |
|---|---|---|---|---|---|
| Runs naming the atom, LOOSE | 0.30 per run | 2 of 2 | 0.09 | -2.41 | -1.10 |
| Runs naming the atom, STRICT | 0.125 per run | 1 of 2 | 0.219 | -1.52 | -1.10 |
| At least one run LOOSE (my 0.60 of 4 runs; 0.51 rescaled to 2 runs) | yes more likely than no | yes | 0.51 | -0.67 | -0.69 (0.50) |
| At least one run STRICT (my 0.35 of 4; 0.23 rescaled) | no more likely than yes | yes | 0.23 | -1.47 | -0.69 (0.50) |
| A run marks 25 or more of 77 items yes | 0.60 | 2 of 2 (29, 26) | 0.36 for both | -1.02 | not defined |
| Zinc item answered "not known" in every run | 0.45 | no | 0.55 | -0.60 | -0.69 |

**Reading.**
1. On the counts, my table is worse than the naive uniform on both LOOSE (-2.41 against -1.10) and STRICT (-1.52 against -1.10). I under-predicted how often the item-by-item pass puts the atom in view: I expected about 0.3 per run and saw 1.0. The direction I named in words (the item list puts the atom in view better than the uncued history, loose more common than strict) was right; the size was not.
2. The part that held: I said the "not known" damping would be common (0.45) and that dilution by many "yes" marks would keep strict below loose. Strict was below loose (1 of 2 against 2 of 2), and the many-yes dilution was present in both runs (29 and 26 of 77).
3. What the result does not show: T7's atom is the one the checklist's own category list was tuned on, so 2 of 2 on loose says the enumeration step can put a known, listed atom in view, not that it retrieves a member that is not in view. My stated reading rule from the forecast ("if strict is reached on a target whose atom is not zinc ... a cue effect") does not apply: the atom is zinc. The question the test was built for (a non-tuned target) was not run, so my view that the checklist helps only modestly at the strict level and not at all upstream of retrieval is neither supported nor refuted by this.
4. A calibration note for my own next forecast: when an input category list contains the atom, put the per-run loose rate near 0.8, not 0.3; keep strict near 0.5 and say it is conditional on carry-over into the hypotheses.
