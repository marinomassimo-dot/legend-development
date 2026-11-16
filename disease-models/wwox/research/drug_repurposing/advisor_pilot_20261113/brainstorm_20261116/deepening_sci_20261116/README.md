# Deepening round, SCI folder (2026-11-16; non-canonical; hypotheses, not findings; mechanism-level; not medical advice)

Read first: the first block ("Answer first") of each dossier, in this order: `DOSSIER_I1_REBOUND_OSCILLATOR_SCI.md`, `DOSSIER_I3_COMPENSATION_ASYMMETRY_SCI.md`, `DOSSIER_I6_CHLORIDE_SCI.md`.

* Model: `rebound_oscillator.py` (numpy only, seeded), `fit_baseline.py` + `fit_baseline_result.json` (fit to the held Breton 2021 medians), `i1_harness_model.py` (adapter for HE's harness), `scan_oat.json`, `scan_grid.json`, `scan_lhs.json` (scans for the harness; predictions inside).
* Predictions: `PREDICTIONS_FROZEN_BEFORE_RUN.md` (sha256 in `predictions_frozen.sha256`), `predict_classes.py`, `score_predictions.py`, `scan_out/` (class scan, one-at-a-time scan, score), `pam_sign_scan.py` and its two outputs, `brake_cliff.py`, `chloride_headroom.py`. `bash run_all.sh` reproduces them.
* Held-data context: `regional_baseline.py` and `regional_baseline.tsv` (cortex and hippocampus control and knockout TPM of circuit genes, GSE158681 and GSE158682; downloads under `files/deepening_downloads/`, gitignored), `outside_set_label_screen.py` and `.tsv` (boxed-warning screen of public DailyMed labels; the XML are under `files/deepening_downloads/labels/`).
* `run1_signbug/`: the first run, made with a sign error in the chloride term (found and fixed the same day); kept as a record, not used.
Every model output is a hypothesis generator, not evidence. No dose, no recommendation to use any agent; a label with no boxed warning is not 'safe'.
