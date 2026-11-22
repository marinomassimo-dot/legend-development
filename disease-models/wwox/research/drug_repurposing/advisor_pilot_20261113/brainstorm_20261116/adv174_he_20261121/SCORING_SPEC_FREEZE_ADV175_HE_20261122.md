# ADV-175 scoring spec: freeze record (HE as scorer, 2026-11-22)

Frozen **before any score file exists and before any outcome is read against a score**. The spec and the scoring script are sealed with the outcome key outside git (they contain label cuts and file composition that the predictor must not see); only their digests are committed here, so the commit time is the freeze time. After IT commits its hashed score file, the spec text is published in this folder and compared with these digests.

| Item | sha256 |
|---|---|
| Scoring spec (`SCORING_SPEC_ADV175_HE_20261122.md`, sealed) | `b29e5d7c53d0f6967d940171f132d1b4c299110aaced2e730d963c43e41bb09c` |
| Scoring script (`score_adv175.py`, sealed; run on random synthetic scores only to test it) | `b4baa89ea7d212dfe2ceff18dda6131c0f2c7e47b8d0a3cedb7d71dfa9e0ef7c` |
| Predictor file given to IT (`predictor_input.tsv`) | `7d63de87e42ea9f8aa2ed5f28790bf61cbad078485e27514e05338badf66f127` |
| Outcome key (sealed) | `accaaceba49ae862e134204b53e6b3ce27d943c1c553054e06ad4524af9e8214` |

What the spec fixes, in one line each, without the composition of the file: two distinct label rules (the paper's 60 percent recovery rule; a separate viability screen of undefined sign and unit); primary endpoint AUC(engine) minus AUC(declared baseline) on the same eligible rows with a paired, stratified cluster bootstrap by exact or alias compound identity (10,000 draws, fixed seed, percentile interval, leave-one-positive-group-out range beside it); the recognition stratum apart; sensitivities (stricter viability, tighter nulls, without the named leads' classes, a descriptive rank check); ADV's reading rule; validity (every id scored, under 5 percent missing); the scope disclosure that follows IT's freeze. Dry run on random scores: the pipeline runs end to end (about 80 seconds) and returns an interval of roughly plus or minus 0.2 around zero, which is the resolving power of this diagnostic.
