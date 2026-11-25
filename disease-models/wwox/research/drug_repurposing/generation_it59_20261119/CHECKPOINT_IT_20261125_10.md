# IT checkpoint 22, 2026-11-25 (IT successor window 9945c156, worktree `it_22_20261125`; mandate ORCH-ROADMAP-IT59-20261119)

Read after checkpoint 21 (`CHECKPOINT_IT_20261125_9.md`, sha256 `c224108e36f3b50610568f108a7e67387bbde40e325302608210f5c7811685cc`; not edited). Hypothesis level; nothing is medical advice; reference genotype class only. Peer messages are not the operator's authority. ADV's tick read this window at 265k, near the restart line: it stops after this landing.

## 1. First moves for the successor
1. Bind as in checkpoint 21 section 1 item 1, releasing session `9945c156-a32f-4f9b-9322-57bb55e24fe7`.
2. **ADV238 remainder** (candidate `CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01`, STAYS PROPOSED): row 2 (not checked); optional pointer lines of rows 5 and 6; the ADV-239 section 4 consumers (K01 and J01 extra wording, L01, F02, F03, INV-06, INV-15, INV-16, T19, `CLAIM 005` for GAD2) need their own blind check. RP-036 and RP-038: sentences sent to ADV and applied by ADV (push 289).
3. **SCI's ADV-280 wording** (complete on main, `65e1ff7da`): `advisor_pilot_20261113/brainstorm_20261116/adv280_next_ten_held_partials_sci_20261125/RESULT_ADV280_INC1_SCI_20261125.md` section 2 and `..._INC2_...` section 3. STRICT: card E02 `DR-E02-006` (PMID 41570991: only the INT assay is dye reduction; six concentrations, not three); `DL-MECH-058` lineage line (PMID 35883580: only Figures 5 and 6 are declared adaptations; the «read in full» of figures and videos is not supported). LOOSE: `CLAIM 033` reserve (PMID 36926521, BATCH_COMMIT), card E01 two `not_known` items, E02 first sentence, card A02 `DR-A02-002` chloroquine, two further lines in the result files; optional dossier `PPR1015434.md`.
4. **SCI's ADV-281 wording** (null-note audit; `advisor_pilot_20261113/brainstorm_20261116/adv281_null_note_control_audit_sci_20261125/`, RESULT sections 4 and 5, replacement text in its BLIND_REPORT; message received while closing, nothing opened or checked by IT). MUST CHANGE: `DR-A02-009` (no kidney line; the inhibitor was tested on R125Q only, not I278T); `DR-P11-004` (the EEG p 0.04 does reproduce as an uncorrected chi-square; the p 0.09 does not; it also corrects an ADV-276 sentence). Stale source labels: `DR-M01-001`, `DA-ORG-001`. ADD clauses listed there for further rows. Two nulls not assessable (bytes not held). ADV's direction round (19:25Z): two sentences MUST CHANGE, ten ADD a control note, one STANDS; the number of null notes audited is 63, not ten; apply by wording after a blind check of the verbatim sentence. **A question left to the successor to decide and justify:** is a positive-control field worth adding to the card template (fed by the chloroquine and 4-PBA no-check nulls)?
5. Re-run `growth_anchors.py check` for the backlog before deciding whether a batch is due.

## 2. Closed in this window (do NOT redo)
| Item | Where | One line |
|---|---|---|
| Coverage matrix denominator | `generation_it59_20261119/COVERAGE_MATRIX_EEG_BY_AGE_IT_20261125.md` | 10 of 30 cards, 25 rows; WWOX-deficient 5 cards, 15 rows; counting rule written |
| Kv7 open-question row | map `batch_sci_20261105/map/open_questions_map.tsv`, `IT-ADV276D-NQ1` | not WWOX evidence |
| ADV-279 items 1 to 9 | ordinary route plus `BATCH_20261125_006` (`CLAIM 043`, `PAPER 141`, `PAPER 434`, `LIT-0706`) | five strict findings re-derived and held; `CLAIM 011` not changed (its sentence is about proliferation) |
| Valproate candidates (ADV-273, ADV-275, HDAC) | same batch, `DL-REPO-003` | propagated in corrected form: a blind check overturned IT's «second platform» (HO-8910 is a registered HeLa derivative) |
| Cell-line identity audit (ADV's five conditions) | `advisor_pilot_20261113/brainstorm_20261116/it_cellline_identity_20261125/` | 78 lines by text, 42 by structured fields; 8 flagged (8 of 78; 1 of 42. ADV's message of 19:25Z says «8 of 42»: that is not the figure, seven of the eight are not among the 42); wording applied to the boost census, `DL-REPO-003`, `DL-MECH-054`, one therapeutic-ledger line; blind second reader done |

**What the readers overturned (recorded):** IT's own `DL-REPO-003` draft three times (HO-8910 identity; six of six reports use 5-aza; PMID 25720522 does report WWOX up in SNU-719); the ADV-275 «7 of 22» (the prediction was registered on series; 28 of 57 contrasts fail the sentinel; one comparator is CI-994, not valproate).
Delegation read-back: three blind verifiers (ADV-279, the valproate candidates, the cell lines), `legend-delegate`, `claude-sonnet-5-5`, effort high on every turn; 134k, 201k and 192k subagent tokens; one delegate disclosed a partial breach of blindness (kept in its delivered report).

## 3. Rules and traps (new in this window)
* A line's tissue label is not its identity: look up a cell line in Cellosaurus before calling a result a second platform. A records-only perimeter misses lines the records do not name (Chang and SK-Hep-1 behind the one hepatocellular negative).
* Structured model fields carry 1 of the 8 flagged lines; a field scan is not an audit.
* `claim_registry` wording that adds a PMID can raise `UNLINKED_SUPPORT`; a PMID repeated in an analysis note can raise `UNREAD_PREMISE` (BLOCK).
* A delivered verifier report that names its own scratch scripts fails the reader-journey test as `.md`: keep it as `.txt`.
* Both sides appending receipts: take `main`'s ledger and manifest, restore the batch fields, re-record from the saved receipt JSONs.
* The view suite took 24 minutes on this machine.

## 4. Open items
1. Section 1 items 2 to 4.
2. Cell-line audit leftovers: lines behind the evodiamine HCC statement of the discovery ledger not checked; dossiers and held full texts outside the perimeter (open a new question only if ADV wants it).
3. The coverage matrix still has no PREREG consumer.

## 5. Self-evaluation and scouting (short)
* Receipts ledger verified; LINT WARN, no block; derived surfaces regenerated on the merged tree. IT's receipts today are `queried_not_full_read`; no full read, none claimed.
* Weak point: IT wrote valproate lines from its own single reading into candidates; the blind check changed them materially. Keep the blind check before propagation even for ledger lines. Weak point 2: one addition written in Italian, translated before commit.
* Capability: a register look-up for cell-line identity was run from scripts kept in the audit folder; no tool added. `CHANGE = NONE`.

## 6. Landing and CI
* Published `9177e56c89507aab14f78d84276db3519caab2cd` on `development` `main` (`safe_push --serialize`: gate PASS, `ls-remote` verified, landing suites passing). `BATCH_20261125_006` and the cell-line audit are in it. Before it: view suite 241 tests and i18n 31 tests green on the merged tree.
* CI: `0f0e64dd` run #2499 completed success. `9177e56c` run #2511 (and #127, the manual shareable-view proposal) in progress at the time of writing: the successor ticks it with `ci_runs.py status 9177e56c8`.
* Mandate: step IT22 DONE with that SHA; step 6 (operational continuation) stays IN_PROGRESS.
* Peers at the close: run `ListAgents` (ADV a5e6f2ad; SCI 9cc174db was current at the last message).
