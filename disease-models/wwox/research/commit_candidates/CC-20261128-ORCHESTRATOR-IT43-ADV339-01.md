# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-IT43-ADV339-01

**Actor:** `orchestrator` (IT, successor 43) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-339 continuation, ADV decisions of 2026-11-28 in the launch brief) · **Date:** 2026-11-28

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS
**MINOR, no version bump.** Claim records `CLAIM 030` and `CLAIM 031`; one clause each. No status, no direction and no working-model statement changes; `target_wm_version` stays `WM_v7.29`.

| Record | Change | Kind |
|---|---|---|
| `CLAIM 031`, Clinical-meaning sentence «Coerente con Obeid 2026 … mentre nessun antiepilettico lo fa» | the contrast with antiepileptics is no longer attributed to Obeid 2026 (the paper has no antiseizure-drug arm); behaviour, myelin and survival atoms kept with their figures | **edit** (three independent readers agree it failed) |
| `CLAIM 030`, Corroboration paragraph header and first clause («independent secondary source» / «Corroborated independently by») | «a second document, NOT an independent source»; «Concordant with»; `R4 satisfied` kept (it is the batch's review floor, not a claim of independence) | **edit** (three independent readers agree it failed; the paragraph's own later sentence already said the records are not independent) |

Not changed, read by three readers (`RESULT_ADV339_part3_IT43_20261128.md`): CLAIM 016 (H1), 036 (H3, H4), 030 (H5, H6), 035 (S1, S2), 019 (S3, S4), 030 (S5). Reading-dependent cells (CLAIM 035 phospho-β-catenin; CLAIM 019 «una barra per linea» per region, «una sola membrana» with a second harvest not shown; CLAIM 016 «crisi» in +/+ and +/-) are reported there and not edited.

## 2 · Sources
`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv339_exclusivity_it_20261128/` (`SELECTION_IT43.md`, `RESULT_ADV339_part3_*`, `second_reader_tables/`, `DREAM_ADV339_half1_IT43_20261128.md`); operation list `ops_adv339_it43.json`; receipts under `receipts/` (all `queried_not_full_read`, one question-driven reading each).

## 3 · Blind reader on the final text (sonnet, effort high, atoms only, no old sentence, no earlier grade, sources by PMID)
10 atoms (B1-B5 PMID 42422765; C1-C5 PMIDs 26499798 and 33916893): **10 supported, 0 not supported, 0 unsettled** on first composition. Caveats the reader printed (not atoms): Fig 4D and 4E of PMID 42422765 carry `*` (HD higher than WT) where the text says no significant difference, and the rotarod Fig 4K is `*` with HD higher; C5 rests on the citation trace (reference 63 of the 2015 review and reference 62 of Banne 2021 are both Mignot 2015, J Med Genet 52:61-70); Mignot 2015 is held at no depth and was not opened, so «same individuals» is not claimed. The replacement texts were composed from atoms the three readers had already graded; this reader is independent of the first reader of the same sentences. Quoted original sentences (kept here, replaced in the registry): CLAIM 031 «Coerente con Obeid 2026, dove il rescue **neuronale precoce** recupera comportamento, mielina e sopravvivenza, mentre nessun antiepilettico lo fa.»; CLAIM 030 «**Corroboration (BATCH_20260909_001 — independent secondary source, R4 satisfied).** Corroborated independently by Abu-Remaileh et al. 2015,».

## 4 · Rates
Twelve sentences, three readers: 2 of 12 failing on all three (17 percent; 2 of 76 second-reader atoms); six holding sentences reached, so the pattern closes. Disagreements are shown in the RESULT, not collapsed.

## 5 · Cards
`copied_card_sentences.py` is run against both claims before landing (result in the landing note). RP rows: `RP-017` names `CLAIM 030`, `RP-019` names `CLAIM 036` (not edited); ADV owns the rows.

## BATCH DISPOSITION — `BATCH_20261128_013`, append-only
**Verdict:** PROPAGATED (two claim records, two record-scoped operations; working model `WM_v7.29` preserved)
**Status:** PROPAGATED by `batch_commit.py propagate`. MINOR.

**Two copies of the CLAIM 031 sentence are NOT corrected in this batch (found by `git grep` of the replaced wording, 2026-11-28):** `discovery_ledger_current.md` `DL-MECH-039` («il rescue causale funziona; nessun antiepilettico lo fa») and `therapeutic_hypotheses_ledger_current.md` `HYP-20260709-07` («mentre nessun antiepilettico lo fa»). They carry the same misattribution. My scripted in-record replacement of both was refused by the auto-mode classifier ("Undermining Oversight"); it is recorded and not retried or worked around. The proposed operation lists `ops_adv339_it43_discovery.json` and `ops_adv339_it43_hyp.json` stay in this folder, unapplied: a decision for ADV or the operator on how these two ledger records are to be edited.
