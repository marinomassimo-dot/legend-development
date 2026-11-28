# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-IT42-ADV339-01

**Actor:** `orchestrator` (IT, successor 42) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-339 repairs, ADV decisions of 2026-11-28 recorded in the launch brief) · **Date:** 2026-11-28

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS
**MINOR, no version bump.** Claim records `CLAIM 003`, `CLAIM 004`, `CLAIM 005` and `CLAIM 011`; scope words only. No status, no direction and no working-model statement changes; `target_wm_version` stays `WM_v7.29`. Arm and line assignments are untouched: both readers confirmed them everywhere the sources could test them.

| Record | Change | Kind |
|---|---|---|
| `CLAIM 003`, `O-KO` evidence-boundary sentence (S1) | the age atom: "no later age than P17" becomes "no histological, molecular or electrophysiological reading beyond P17-P18"; weight shown to P16, survival to about 120 days, clasping image at P18 | **edit** (both readers agree it failed) |
| `CLAIM 011` title (T3) | "NOT on survival" and "demonstrated on expression" dropped; survival is graded by Fig 3B, expression is mostly not significant (Fig 5), body weight is untested | **edit** (both readers agree) |
| `CLAIM 011` Italian sentence on the P90 arm, S7I and gliosis (T5) | "no untreated disease arm at P90" scoped to the behavioural study; "bytes absent" for S7I and Fig 6F removed (both are held); Iba1 has no LD-versus-WT difference | **edit** (both readers agree) |
| `CLAIM 003` S2 ("the only oligodendrocyte-lineage datum") | dated pointer, text unchanged | reading-dependent |
| `CLAIM 004` wave note S4 ("every behavioural endpoint ... wild type only") | dated pointer, text unchanged | reading-dependent |
| `CLAIM 005` S5 ("in a single study") | dated pointer, text unchanged; the failing atom is a literature count, outside the PREREG rule | reading-dependent |

Not changed: the ADV-339 T1, T2, T4 and the part 1 S3 and S6 sentences (HOLDS on both readers). T2's microglia atom rests on a third paper (Tochigi 2019, PMID 31340538); noted here only.

## 2 · Sources
`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv339_exclusivity_it_20261128/` (`PREREG_ADV339.md`, `RESULT_ADV339_part1_*`, `RESULT_ADV339_part2_*`); operation list `ops_adv339_it42.json`; receipts `FTR-20261128-33914858-43`, `FTR-20261128-42422765-02`, `FTR-20261128-42397075-02`, `FTR-20261128-34747138-39` (all `queried_not_full_read`, one question-driven blind reading each, see `receipts/`).

## 3 · Second reader on the final text (sonnet, effort high, blind: atoms only, no old sentence, no earlier grade, sources by PMID)
32 gradable atoms (A1-A10 `O-KO` line of PMID 33914858; B1-B17 PMID 42422765; C1, C3-C6 for the pointers; C2 asked for a description and is not counted). First composition: **30 supported, 2 not supported (6 percent of 32 atoms), 0 unsettled**. The two: A10 (my wording "no functional reading beyond P17-P18" is false for survival to about 120 days) and B12 (I wrote that the `KO+RI` animals are dead by about P25; Fig 3B shows about P17-P18). Counted per repaired unit (S1 sentence, title, T5 sentence): **2 of 3 contained a failing atom** on first composition. Both were reworded (narrowed to histological, molecular or electrophysiological; P18, read from the axis) and re-graded by the **same reader**: 2 of 2 supported (a delta check, **not an independent reading** of the two reworded atoms).
Quoted original sentences (kept here, replaced in the registry): S1 "... consiste in peso e sopravvivenza fino a circa 120 giorni, in un'immagine di hind-limb clasping e in un solo confronto anti-MBP a P17: nessuna microscopia elettronica, ... e nessuna età successiva a P17."; T3 "AAV9-hSynI-hWWOX in Wwox-null murine model: durable survival rescue at the high dose only, with dose-grading demonstrated on expression, P20 glycaemia and motor score and NOT on survival, body weight, ECoG/SWD, myelination or gliosis"; T5 "E non esiste alcun braccio di malattia non trattato a P90, per costruzione ... attestazione di pannello dichiarata su S7I, byte assenti ... gliosi (RESCUE a dose alta, NO_RESCUE a dose bassa)".
Side findings of the reader (not atoms, not written into a record): Fig 7C plots two to three points per arm with p = 0.2 while the text says "significant"; Fig 4D,E and 4K show `*` where the text says "indistinguishable"; S7I is labelled about P90 for LD although Fig 3B has all LD dead by about P78; S7A and S7C label untreated KO at P20 although Fig 3B has `KO+RI` dead by about P18; the wild-type Iba1 baseline differs between S7B and S7F. Limits: values are read from axes and boxplots; the Fig 4 panel conflict (4D-4G) is not re-adjudicated here (the file `gr4.jpg` is present: presence only). The first adjudication sentence "dead by about P25" in `RESULT_ADV339_part2` was an arithmetic of the adjudicator, now replaced by the axis reading.

## 4 · Cards
`EB-GROWTH-AX-01` (packet and card, `cards_early/`) restated the old `CLAIM 011` title in its `temporal_or_model_limit`; packet edited, card rebuilt by the bridge, `check_cards.py` PASS. No `RP-` row cites `CLAIM 011` (ADV checked the portfolio); `CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01` and `CC-20261120-ORCHESTRATOR-WM103-DOSE-WORDING-01` are append-only and keep the old wording as history.

## BATCH DISPOSITION — `BATCH_20261128_012`, append-only
**Verdict:** PROPAGATED (four claim records, seven record-scoped operations; working model `WM_v7.29` preserved)
**Status:** PROPAGATED by `batch_commit.py propagate`. MINOR.
