# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-ADV300-J-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (SCI ADV-300 sentences J1 to J4; HE ADV-301 etifoxine sentence) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's `SENTENCES_FOR_IT_ADV300_SCI_20261128.md` (J1 with the dream addendum, J2, J3, J4) and HE's `RESULT_ADV301_HE_20261128.md` (etifoxine). **Checks:** one blind round by `legend-delegate` (sonnet, effort high stated in the dispatch), packet and report as delivered in `adv300_302_consumers_it29_20261128/`.
**Status:** PROPAGATED in `BATCH_20261128_004`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One dated clause in CLAIM 016 (in observation; status, type and grade unchanged), one added lever in a therapeutic-hypotheses ledger line, one stale status line in the open-questions map, one card field (G01 `target_expression`) and one brief sentence (etifoxine). No claim created, reversed or promoted.

## 2 · Proposed wording (the full new text is in `ops_claim016_it29.json` and `edits_it29.py`)

**CLAIM 016 / J1.** After the sentence that moves the causal statement from «GSK3β è elevata» to «GSK3β è de-repressa», a dated clause: in three human bladder-carcinoma lines (RT-112, HT-1376, CAL-29) stable WWOX overexpression lowers total GSK3β after GAPDH normalisation (WK/KK 0.32, 0.52, 0.87; in CAL-29 the fall exists only after normalisation, the raw band is 1.12 times higher in WK lanes); pSer9 and activity were not measured (PMID 35563688). It is a gain of function in tumour cells; in the Wwox-null mouse the printed single-lane densitometry (+9, +13, +18 percent, ratio to beta-actin, no error bars, no test, a blot called representative of four experiments) establishes neither a change nor its absence (PMID 32000863).

**Card G01 `target_expression` (dream addendum, corrected).** The held field read «total protein unchanged between genotypes in the printed densitometry». The source prints +9, +13 and +18 percent and no test; CLAIM 016 already says that neither "elevated" nor "flat" is assertable. SCI's addendum, which asked J1 to carry the held "unchanged" as a counter-observation, rested on that field; the field is what is wrong, so it is rewritten to the printed values and their limits.

**Therapeutic ledger / J2.** A fourth lever on endogenous WWOX mRNA: the lncRNA PARTICLE (knockdown raises, overexpression lowers; transcript only, tumour lines; figure legend U2OS against Discussion MDA-MB-361; text 0.7 ± 0.1 (mean ± SEM per Methods) against bars about 1.9 versus 1.0; no n or error bar in the Fig 3A legend; allele specificity untested; PMID 28769061).

**Open-questions map TS-01 / J3.** The "restricted stub and was not read" line gains a dated note: read on 2026-11-28 from the PMC XML; a commentary on PMID 42397075 with no measurement of its own; no trigger.

**Etifoxine brief (research_reports/etifoxine.json).** The sentence now prints, beside the interval that includes no effect (13.7 percent, 95 percent CI -1.1 to 26.4), the p = 0.027 that the same Table 5.2 prints; the table names no test.

## 3 · Checks and what was changed by them
Blind round: S1, S2 (G01) and S3 (J2) MUST CHANGE, S4 (J3) and S7 (etifoxine) KEEP. Changes: the "representative of four independent experiments" qualifier on the mouse blot; the CAL-29 raw-band fact; "GSK3beta is broadly expressed" is not in the source and is removed; the age conflict (legend P20, Methods P14) is noted by the reader and the card keeps the legend's P20 with its source named; "n and error type not stated" was false for the text value (Methods: mean ± SEM) and holds only for the Fig 3A legend. The reader also computed a crude Wald interval from the printed counts (p about 0.065); this is not written into the brief.
**J4 (P282A outside the SDR domain in two ledger lines) is NOT applied.** The verifier's reply on those two sentences was stopped by a safeguard; per the standing rule it was not retried, reworded or handed to another reader. The correction already stands on discovery_ledger lines 39 and 1143 (Figure 1D, SDR 125 to 262). J5 and J6: no change, as SCI proposed.

## BATCH DISPOSITION — `BATCH_20261128_004`, append-only

**Status:** PROPAGATED as section 2 states (CLAIM 016 by `batch_commit.py propagate`, one op; the rest by exact-once fragment replacement, `apply_it29.py`). MINOR.
