# Checkpoint IT28 part 2 (session 54ca757b), written 2026-11-28 at the ADV handover (tick read 289k)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119. Replies to the operator in Italian, files in English. Read `CHECKPOINT_IT_20261128_1.md` too; this file adds only what happened after it.

## 1. First moves for the successor
1. `df -h /` (3.1 GB at the end of this window; push needs 2.0 GB, a delegate dispatch 1.5 GB; below 1.0 GB stop and tell ADV). Delete only your own job-tmp scratch. The 19 GB old scratchpad, 36 clean worktrees and 244 browser profiles are operator items, reported by ADV; do not ask anyone to delete them.
2. Read, in this order: `advisor_pilot_20261113/brainstorm_20261116/adv300_catalogued_triage_open_sci_20261128/SENTENCES_FOR_IT_ADV300_SCI_20261128.md` (J1 to J6), then the etifoxine correction (below), then do C3.
3. Disclosure rules that held this window: say what you had read before a freeze; open a table before naming it; every figure value read by a delegate and re-read by a second one; blind readers get whole sources and never a card or my conclusion.

## 2. Open commitments (in order)
| # | Item | State | What to do |
|---|---|---|---|
| 1 | SCI ADV-300 sentences J1 to J6 | file on main, not started | J1 = CLAIM 016 (needs BATCH_COMMIT: `test_batch_queue`, snapshot, propagate via `batch_commit.py propagate --file <f> --ops <ops json path>` dry run then `--apply`, lint, state files, CC candidate) and must carry the dream addendum: card G01 reports total GSK3beta unchanged in the Wwox-null, so the gain-of-function abundance effect is not a loss effect. J2 = a fourth lever on WWOX mRNA. J3 = TS-01 still says PMID 43036373 was not read. J4 = two ledger lines still place P282A in the SDR domain. J5 and J6: no change proposed. One blind round (legend-delegate, sonnet, effort high stated), then the view trio if a card or map PMID changes. |
| 2 | Etifoxine sentence (HE ADV-301) | not started | The etifoxine brief omits the p = 0.027 that the same Table 5.2 prints next to the interval that includes no effect. One sentence, one blind round, ordinary route. HE's result: `briefcheck_adv301_he_20261128/RESULT_ADV301_HE_20261128.md`. |
| 3 | ADV-286 C3 recipe | due 2026-11-30 | Repeat the recipe of the design note (each GEO series or E-MTAB accession named in a held full text, plain request for status and any printed release date; candidate = status other than Public AND a date). Say to ADV on or before 2026-11-30 whether C1 (AES poster, 2026-12-05) and C2 (E-MTAB-14792, "Study not accessible") are retrievable; the retrospective-hold fallback stands unless one is. **Freeze by 2026-12-04** (files, one sha256 each, landed commit, prediction-ledger entry with weight zero; "retrospective hold, not a prospective test"). Design: `adv286_prospective_hold_it_20261126/DESIGN_NOTE_ADV286_IT_20261126.md`. Add to the metric the first-composition rates from the self-evaluation (below). |
| 4 | DR-A01-002 "every target of the lot" | withdrawn | stays withdrawn pending SCI's re-read of 30266908, 42157447 and 42587736. |
| 5 | N10 (card H02, universe row 30, vigabatrin sentence) | NOT ASSESSED | never read, rewritten or retried in any wording. |
| 6 | CI | to report in one line | #2770 (122edc93f) was in progress; CI of 41c50294e, d363da15b, 009b4cb14, e709c1e68, 349265be0, 0ee773abe not yet looked at. |

## 3. Landed in this part (all on development/main, gate PASS)
`81d9523bc`/`122edc93f` ADV-295 b1 and ADV-298 table; `41c50294e` BATCH_20261128_002 (ADV-295 b2 and ADV-297 ledger sentences, P214 note, ADV-298 consumers); `d363da15b` self-evaluation, `fragment_source_check.py` (+ test, routing row) and BATCH_20261128_003; `009b4cb14` NQ-A close; `e709c1e68` DREAM note (corrected in `349265be0`); `349265be0` ADV-303; `0ee773abe` ADV-304. Self-evaluation: `disease-models/wwox/research/session_evaluations/2026-11-28_it28_adv_batches.md`.

## 4. Results to know, in one line each
* ADV-298: no held Wwox preparation has a conduction/latency readout with a rescue or drug arm; heterozygote Tc-MEP latency is not a clean central-myelin readout; slope plan stays a plan.
* ADV-303 (RP-036): P47T cerebellar mature-marker median +0.500 with OPC markers not rising; forebrain mature markers down (-0.19 to -0.62); composition NOT rejected; stage split unresolved. ADV patches the portfolio line.
* ADV-304 (RP-049 route 1): UNRESOLVED, parked. Palma 2022 calibration fails (g-ratio change predicts 0.3 to 2.4 percent against 16 percent measured velocity drop), so g-ratio at fixed calibre is not a sufficient structural proxy; Wwox Fig 5C readback (+0.03, +0.21, +0.80 ms at 0.5, 1.0, 1.5 um) is descriptive. ADV patches the RP-049 row (not me).
* Resume conditions: RP-036 needs class-resolved sterol expression in P47T cerebellum (new data); RP-049 needs a Wwox callosal series with at least three distances plus absolute early recruitment plus EM of the same animals (raw data on request only; contact operator-reserved), or an independent callosal source with both in the same animals.
* NQ-A (RP-048): parked, duplicate of ADV-232/236; IT-B and IT-C already sit on the WO-03 and NR-03 map rows.
* Public callosal deposits from HE (ADV-306/307): Rictor knockout (doi:10.5061/dryad.gk117, public copy zenodo.org/records/4999038), shiverer (doi:10.6084/m9.figshare.4040070). Quote a Rictor slope only with "early recruitment not controlled (no stimulus intensity)"; never use the sheet's columns G or I as velocity; not usable as the matched relation (other animals and ages, paper contradicts itself on g-ratio).

## 5. Rules and traps (new, beyond checkpoint 1)
* Supplement sheet "Supplementary_data.xlsx" of PMID 36828035 lists only significant genes; use `files/deepening_downloads/gse215425/GSE215425_processed_data.csv.gz` (37 libraries) with `adv198.../composition_bound_adv198.py` functions. Name a table only after opening it.
* El Ghaleb 2021 Supplementary Table S1 IS held (`files/supplement/PMID33704440_r2/`): put the supplement folder in blind packets when a clause rests on it.
* The Palma 2022 figure pages are in `files/figure_renders/PMID35372341_r3c/`; Repudi Brain Fig 5 is a 150 ppi raster on PDF page 11.
* `safe_push` refuses untracked files: write result notes into the worktree only when no push is queued; do not commit while a push waits for the lock; disk below 2 GB: run it from a loop that waits for `df` (ADV's pattern).
* `fragment_source_check.py` (new, advisory): run it on a fragment against the cited source text before the blind round; count its flags against the blind reader's findings on the next batch and tell ADV (agreed). First sample: flags 29, 281 and "no such" on three real first-composition texts; one false flag on a date.
* First-composition MUST CHANGE rates for ADV-286: INC4-6 10/24, ADV-287 ext 2/23 (11/23 any change), ADV-295 b2 + ADV-297 4/7, consumers 1/8.
* Operator: no spend; no contact with authors or outside parties (draft letters exist, unsent); Codex paused; the operator closes no terminal; never send the operator e-mail to any service; a challenge page, 403, 401 or 429 is a result. The Obeid 2026 perimeter and adv174/adv175 stay unopened.

## 6. What filled the context (estimate; I cannot read the counter)
Largest consumers, in descending order: (1) subagent hand-backs returned whole into the context (blind-check reports and two figure-readback reports, about 6 to 12k each, about 15 of them); (2) reading repository result notes in full for steps 0 (ADV-198 result, ADV-236, ADV-232, ADV-298 sections, callosal_propagation.md); (3) long bash outputs (lint, session_self_eval, view rebuild logs, diff stats, gene tables); (4) peer messages with full briefs (about 2 to 4k each, about 25); (5) the state-file and CC candidate writing. A next window should have a delegate return a short structured summary (a table plus the file path) instead of the whole hand-back, and should read only the numbers it needs from result notes.
