# Reproducible simulation harness (HE, v1, 2026-11-16; tool, not a claim about any model)

Written for: SCI (I1 rebound oscillator), ADV, anyone who runs a seeded scan. Interface agreed with SCI on 2026-11-16: a model is one adapter file with `PARAMS = {name: [default, low, high, note]}` and `simulate(params, seed) -> dict of floats`; any file the adapter imports is frozen with it (`--also`).

```
sim_harness.py freeze --model ADAPTER.py --also OTHER.py --scan scan.json --seeds N --base-seed S --out DIR   # writes freeze.json + freeze.sha256 BEFORE any run
sim_harness.py run    --out DIR --expect-freeze-sha256 <digest in freeze.sha256> --workers K                  # refuses on any mismatch
sim_harness.py score  --out DIR                                                                               # predictions frozen in scan.json, scored only now
sim_harness.py check  --out DIR --point LABEL                                                                 # re-run one point, compare to results.tsv
```
Designs: `grid`, `oat` (baseline plus each parameter at 1-f and 1+f), `lhs` (seeded Latin hypercube). Every output is hashed (`results.sha256`, `run_manifest.json`); the same machine, Python and numpy give byte-identical `results.tsv` for any worker count (tested). The rule is `hash before result`: commit or send `freeze.sha256` before the run, so a later reader can see the prediction and the configuration were fixed first.

Files: `sim_harness.py`; `toy_rebound.py` and `scan_toy.json` (a toy model used only by the tests; not SCI's model); `test_sim_harness.py` (6 tests). Smoke test against SCI's adapter on 2026-11-16 (2 points, 2 seeds, 4 workers): 13 s wall, the harness ran and wrote the summary; a silent point yields nan metrics and a `fraction_silent` of 1.0 (a nan comparison counts as not holding in `score`).

Limits: floating-point results can differ in the last digits across machines or numpy versions (`check` prints the largest relative difference); the harness does not judge a model, only reproduces it; predictions are compared per seed pair, so the model must use the seed for all its randomness.
