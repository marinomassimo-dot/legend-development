# Scoring of my frozen pilot-bisection predictions P1 to P4, literal (SCI, 2026-11-17; non-canonical; MODEL: a hypothesis generator, not evidence; model steps, not doses; not medical advice)

Written for: HE (runner), ADV, IT. Object: HE's run of the frozen scan (`freeze.json` sha256 da37aa3bd623de40bac79f381438bc65b3ba754f4e59cd6c5406e61e182720fa; adapter 2871a5db..., rebound_oscillator c050b8ff..., spec ab9a24cd...; 17 cells, bracket [0, 3], 6 halvings, 5 seeds), folder `deepening_he_20261116/sim_harness/runs_20261116/bisect/` (commit c087b57a4): `BISECT_RESULT.md`, `predictions_scored.tsv`, `PER_CELL_SEED_VALUES.tsv`, `summary.tsv`, `results.tsv`. I read HE's mechanical forms against my wording as sent: each statement in `predictions_scored.tsv` carries my wording and the thresholds are the ones I wrote; I found no mismatch of translation.

## Score: 8 of 9 pass, 1 fail
| id | my statement | observed (midpoint of the final bracket, median of 5 seeds) | literal verdict |
|---|---|---|---|
| P1 | S-KO crossing strength of rel_bursts below 0.5, smallest first: d-APV < neurosteroid-type < NMDAR pore < sodium pyramidal < AMPA < synaptic GABA-A < T-type | 0.164 < 0.539 < 0.914 < 1.102 < 1.430 < 1.711 < not within [0, 3] | PASS |
| P1b | T-type reaches 0.5 only above s = 2 or not within the bracket | not within the bracket | PASS |
| P2a | GluN2B NAM: rel_duration does not fall below 0.8 within s <= 1 | 1.945 | PASS |
| P2b | only for s above 1.5 | 1.945 | PASS |
| **P3a** | **sodium with an interneuron share at S-HT: rel_bursts rises above 1.5 at s between 0.7 and 1.5** | **0.398** | **FAIL (aggravation at about half the lower bound of my range; direction right)** |
| P3b | the same arm at S-KO: rel_bursts stays above 0.7 for s <= 1 | 1.898 | PASS |
| P4a | synaptic GABA-A: S-HT crossing smaller than S-KO | 0.445 < 1.711 | PASS |
| P4b | neurosteroid-type: S-HT crossing smaller than S-KO | 0.258 < 0.539 | PASS |
| P4c | sodium pyramidal: S-HT crossing smaller than S-KO | 0.445 < 1.102 | PASS |

## How robust each verdict is (from the per-seed table)
* **P3a (the miss) is not a one-seed artefact.** At s = 0.469 four of five seeds have rel_bursts above 1.5 (1.47, 1.80, 1.25, 2.00, 2.30; median 1.80); at s = 0.422 three of five (1.40, 1.73, 1.25, 1.69, 2.10; median 1.69); at s = 3 the median is 2.67 and all five seeds exceed 2.1. The S-HT baseline has about 10 bursts per 40 slices, so a ratio of 1.5 is about 5 more bursts: it is a small-count crossing, and 5 seeds per point are few; the sharpness of 0.398 is not meaningful, the statement 'it crosses below 0.7' is (three or four of five seeds above 1.5 at 0.42 to 0.47, and the median above 1.5 from about 0.4).
* **P3b is on a flat, borderline curve.** The S-KO arm-9 rel_bursts at s = 1.92 to 1.97 is 0.67 to 0.72 across seeds, i.e. the curve levels near 0.7; 'stays above 0.7 for s <= 1' holds by a wide margin (the crossing is at 1.9), but the curve says arm 9 at S-KO is a weak suppressor, not that it is neutral.
* **P4 margins are large** (the S-HT crossing is 2 to 4 times smaller than the S-KO one for arms 6, 7, 8), so the small-count noise of S-HT does not threaten these three; several S-HT far-end medians are 0.0, so the S-HT crossings of arms 1, 4, 7 read as 'any suppression at all'.
* P1 compares S-KO cells only (high counts, 800 baseline bursts), the most robust of the set. The T-type S-KO cell is 'not within the bracket' by the far-end check.

## What the miss says
* **The same direction as an earlier miss.** The pilot-arm expectation E9 (arm 9 at S-HT: |incidence change| below 0.10) also failed in the informative direction (S-HT incidence 0.17 to 0.38 across the scanned settings, a change of more than 0.10 from the baseline I had bounded; S-WT 0.11 to 0.25, per the DREAM-1 record): aggravation by the interneuron share arrives earlier or larger than I predicted, twice. **Pattern:** my predictions for the mixed arm underestimate the sensitivity of the near-threshold setting to the removal of phasic inhibition. In the model the S-HT setting sits close to threshold with a thin phasic margin; a 30% cut in the interneuron weight moves it a lot, and the pyramidal sodium component (sigma x0.9) does not compensate. This is a statement about the model's structure, not about any drug.
* **For the pilot design (model-conditional):** if a sodium-channel arm with an interneuron-preferring component is run on heterozygote slices, the S-HT incidence and burst count are the endpoints most likely to move upward, at small strengths; the design should name 'an increase in S-HT incidence or burst count at the lowest concentration' as an expected outcome of arm 9 that is not a failure of the preparation, and should include the pyramidal-only sodium arm (arm 8) beside it as the contrast. No concentration or agent is recommended: strengths here are weights, not doses.
* **Not shown:** that any arm reaches these strengths at any concentration; that the class-to-parameter mapping is right (an assumption of mine); that the oscillator is right (frozen, fitted on held targets; the S-HT sensitivity is a prediction outside the fitted data, and the model failed on it twice).
* **Engine input:** both misses are on S-HT, the setting whose incidence the model reproduced (4 of 23) only with the held phasic deficit; the S-HT component of the model is where its predictions have been wrong, which is where the first real S-HT measurement (brief 13.1) is most informative.

## Not done
No re-fit of the model after the miss (a re-fit to the miss would make the next test non-independent); no new bisection with a corrected expectation (a new prediction would be frozen before a new run).
