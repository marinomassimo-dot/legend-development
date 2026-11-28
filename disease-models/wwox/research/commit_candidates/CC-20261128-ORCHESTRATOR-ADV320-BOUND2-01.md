# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-ADV320-BOUND2-01

**Actor:** `orchestrator` (IT, successor 34) · **Task:** ORCH-ROADMAP-IT59-20261119 (SCI ADV-320 with HE ADV-323, Chornyy 2025, PMID 41036104; SCI ADV-322 compound dispositions) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's `RESULT_ADV320_CHORNYY2025_SCI_20261128.md` and the comparison with HE's blind `adv323_blind_chornyy_he_20261128/BLIND_READING.md` (the two readings agree on every cell that carries the claim). **Checks:** three blind rounds by `legend-delegate` (sonnet, effort high stated), records and rates in `advisor_pilot_20261113/brainstorm_20261116/adv317_adv320_consumers_it34_20261128/README_BLIND_ROUNDS_IT34.md`. **Status:** PROPAGATED in `BATCH_20261128_008`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR, no version bump.** CLAIM 047 bound (2) "Restriction costs intensity, not reach" is narrowed: the text's 41 percent and "up to 42 percent" of brain area are the largest plotted points of Fig. 4C (about 41.9 and 42.4), not typical animals; the plotted medians are about 23 and 39 percent of area (ratio about 0.60; Table S1 adjusted P 0.0097) and about 124 and 577 RFU (ratio about 0.22); the text's 154.0 and 474.8 are called "mean EGFP intensity" (ratio 0.32). The sentence is now an observation about p546, not a general rule about restriction (GFAP and gfa1405 do not differ from CAG in intensity, Table S1). Same wording in PAPER 225 and the CLAIM 047 working-model row. Bound (1) unchanged.

## 2 · Where the full text is
`make_ops_it34.py` (builds `ops_claims_it34.json`, `ops_paper_it34.json`, `ops_working_model_it34.json`: three record-scoped `replace-within` ops through `batch_commit.py propagate`), in `advisor_pilot_20261113/brainstorm_20261116/adv317_adv320_consumers_it34_20261128/`.

## 3 · Checks and what they changed
Rounds on the Chornyy wording: 2 of 13 MUST CHANGE (15 percent), repaired; 1 of 13 (8 percent, borderline), repaired; 0 of 8 on the changed clauses; the Crawford INV-06 sentence (not applied in this batch): 1 of 13, 0 of 11, 0 of 4. ADV-322 dispositions (compound register, same batch, no schema): sodium dichloroacetate research slot lowered with a timed reopening and the Baryla 2022 (PMID 35328751) fibroblast datum added to its dossier with its limits; lithium with tideglusib recorded as one conditional GSK3 comparison with its missing observation; ganaxolone/etifoxine and bexarotene/montelukast unchanged; 8 of 8 statements of the note confirmed at source with 4 refinements. Clinical positions unchanged.

## BATCH DISPOSITION — `BATCH_20261128_008`, append-only
**Status:** PROPAGATED (paper registry, claim registry and working model by `batch_commit.py propagate`; the compound register and the dichloroacetate dossier by direct edit). MINOR.
