# ADV-175 scoring spec: freeze record (HE as scorer, 2026-11-22)

Frozen **before any score file exists and before any outcome is read against a score**. The spec and the scoring script are sealed with the outcome key outside git (they contain label cuts and file composition that the predictor must not see); only their digests are committed here, so the commit time is the freeze time. After IT commits its hashed score file, the spec text is published in this folder and compared with these digests.

| Item | sha256 |
|---|---|
| Scoring spec (`SCORING_SPEC_ADV175_HE_20261122.md`, sealed) | `b29e5d7c53d0f6967d940171f132d1b4c299110aaced2e730d963c43e41bb09c` |
| Scoring script (`score_adv175.py`, sealed; run on random synthetic scores only to test it) | `b4baa89ea7d212dfe2ceff18dda6131c0f2c7e47b8d0a3cedb7d71dfa9e0ef7c` |
| Predictor file given to IT (`predictor_input.tsv`) | `7d63de87e42ea9f8aa2ed5f28790bf61cbad078485e27514e05338badf66f127` |
| Outcome key (sealed) | `accaaceba49ae862e134204b53e6b3ce27d943c1c553054e06ad4524af9e8214` |

What the spec fixes, in one line each, without the composition of the file: two distinct label rules (the paper's 60 percent recovery rule; a separate viability screen of undefined sign and unit); primary endpoint AUC(engine) minus AUC(declared baseline) on the same eligible rows with a paired, stratified cluster bootstrap by exact or alias compound identity (10,000 draws, fixed seed, percentile interval, leave-one-positive-group-out range beside it); the recognition stratum apart; sensitivities (stricter viability, tighter nulls, without the named leads' classes, a descriptive rank check); ADV's reading rule; validity (every id scored, under 5 percent missing); the scope disclosure that follows IT's freeze. Dry run on random scores: the pipeline runs end to end (about 80 seconds) and returns an interval of roughly plus or minus 0.2 around zero, which is the resolving power of this diagnostic.

## Addendum 1 (2026-11-22, written before IT's score file was opened)
Sealed like the spec; digests only. Reason: IT's frozen method names two baselines (B1 class prior, B2 lipophilicity) and its own metric; ADV's return 16 asks for both the original and the addendum metric and fixes the title. Nothing in it uses a score or an outcome. It reads the spec's "declared baseline" as B1 (B2 descriptive), adds the original metric of the frozen method (engine AUC with the same bootstrap, a label-permutation p, the gap to B1) and the addendum metric computed from IT's addendum text as written, scores unchanged, and fixes the title "LLM generic-perturbation rubric against class prior".

| Item | sha256 |
|---|---|
| Addendum 1 text (sealed) | `370b080c8d5a54a4b9e62d9c0bcd85ae9d7a6c23669d1c60d20ec5930b5ddf2b` |
| Scoring script v2 (sealed; reads IT's column names; on a common synthetic file its primary and three sensitivity lines are identical to the frozen v1) | `02b8f4e49da75daa138438df6211825505da37a418d61cee717c38ea99b090cb` |
| Scoring script v1 as frozen above (kept) | `b4baa89ea7d212dfe2ceff18dda6131c0f2c7e47b8d0a3cedb7d71dfa9e0ef7c` |

## Addendum 2 (2026-11-22, after IT's score file was on main, BEFORE any run of any script against the outcome key)
IT's score file (sha256 `9491b18d14192517ef84d5ea465f351635af4e542ad7dfcafced4b57945bd9cc`) and addendum are on main. I have not opened the score file for any purpose but the hash, and the key has not been read against any score. Script v3 adds IT's **addendum metric as written** (IT's `alias_group` column, 2,000 cluster resamples, unstratified, 95 and 90 percent intervals, useful gap 0.10) beside my frozen metric and the original metric; nothing else changed (v2 kept). Scoring script v3 (sealed) sha256 `d42b8bb20bdda26b2669969fb20297a300cc5cd2c0133cff4dfad09005206d72`.
