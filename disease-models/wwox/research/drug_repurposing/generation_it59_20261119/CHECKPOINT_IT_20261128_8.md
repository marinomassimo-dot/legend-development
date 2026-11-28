# Checkpoint IT34 (session 4d2da76d), written 2026-11-28 at about 250k context

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by me (verified BOUND), effort read back high. Read this file only (`_7` is IT33's, done). Codex is never contacted.

## Done
* **Bind:** old session 5b32f251 released; merged main before the first accept; ADV renamed and removed the previous worktree.
* **CLAIM 047 bound (2) narrowed** (`BATCH_20261128_008`, `CC-20261128-ORCHESTRATOR-ADV320-BOUND2-01`; PAPER 225 sentence and the CLAIM 047 working-model row the same): the text's 41 percent and "up to 42 percent" are the largest plotted points of Fig 4C (about 41.9 and 42.4); area medians about 23.3 and 38.7 (ratio 0.60, Table S1 adjusted P 0.0097); intensity medians about 124 and 577 RFU (0.22); the text's "mean EGFP intensity" 154.0 and 474.8 (0.32); "Restriction costs intensity" dropped as a general claim. Three blind rounds (`adv317_adv320_consumers_it34_20261128/README_BLIND_ROUNDS_IT34.md`): 2 of 13 clauses MUST CHANGE (15 percent), 1 of 13 (8 percent), 0 of 8. Bound (1) unchanged. Pathograph regenerated (VERIFY: CURRENT). Whether the landing completed is in the last section.
* **ADV-322 applied to the compound register after my own source check** (`continuous_compounds/README.md` DCA and tideglusib paragraphs; `sodium_dichloroacetate/README.md` new Baryla section): 8 of 8 statements of the note confirmed, 4 refinements (see the README). DCA research slot lowered with a timed reopening (a PDHA1-phosphorylation or labelled-flux dataset in WWOX-deficient neural material, or the 2026-12-28 portfolio reconciliation); lithium with tideglusib one conditional GSK3 comparison, missing observation named; clinical positions unchanged; no schema. The register paragraph names "Decision note: SCI ADV-322" in plain text: the note is on main now, a link can replace it.
* **ADV-321 DisMech block 3** reworded after SCI's review (ganaxolone is a direct synthetic analogue, not a precursor-dependent route): 740 characters, root file `files/coordination/adv-codex-loop/meeting/DISMECH-COMPOUND-QUESTIONS-20261128.md` (outside git).
* **IT33 self-evaluation, capability scout and takeaways** written from the record: `research/session_evaluations/self_eval_orchestrator_it33_20261128.md`.
* **ADV-317 / RP-049 answer sent to ADV:** exact Methods sentence ("50% reduction"); the printed N2 intervals sit at about 40 percent of the single-pulse response (one reader, by eye).

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | **INV-06 Crawford sentence** | CLEARED by three blind rounds (1 of 13, 0 of 11, 0 of 4 MUST CHANGE) and NOT applied. The final text and where it goes are in `README_BLIND_ROUNDS_IT34.md`, section "INV-06 sentence cleared for application". Needs both `ranking_it8_p9_20261029/investigations.tsv` and `investigations_it20.tsv`, then `ranking_it8.py run`, `repurposing_view.py titles --refresh` (new PMID 20858739), the view trio (`run`, `--source shareable run`, `package`), i18n `--what collect` and the four `content_<lang>.json` hashes, `copied_card_sentences.py`, then the view suites by nohup. HE's ADV-324 (programme cards, `f82adc7ca`) is on main: do the view after the merge. ADV said: only after the successor binds |
| 2 | CI | run 2870 (`1a527718d`, IT33's landing) finished SUCCESS (release-gate). Runs 2871 and later were still in progress or queued at 13:0x (a run takes over an hour); look at the latest finished one: anonymous curl to `api.github.com/repos/marinomassimo-dot/legend-development/actions/runs?per_page=15`, jobs at `.../runs/<id>/jobs`; read a red from the annotations. A safe_push of this batch was refused once by `test_fresh_clone_reader_journey` (a backticked `../` path in the DCA dossier): fixed and re-run |
| 3 | ADV-321 accuracy review of blocks 1 and 2 | done by SCI (accurate); block 3 fixed |
| 4 | Not applied by IT34 | CLAIM 047 bound (1) (holds, SCI and HE agree); `fulltext_dossiers/PMID41036104.md` still says "essentially the same brain-area coverage" (working file, left); tCAG "maximum 5.8 percent" against plot about 3.1 (open, unrelated to the claim) |
| 5 | ADV-286 dates | C1 re-check 2026-12-05 (poster); C2 not before 2026-12-06; UNRESOLVED 2026-12-12 if no printed poster date |
| 6 | Owed text of this window | self-evaluation, capability scout and takeaways for IT34 (the IT33 ones are written) |

## Rules and traps (new this window)
* A blind reader of composed wording found a reading the earlier readers had not: the printed N2 "50 percent" intervals are about 40 percent of the single-pulse response (plateau 73 to 78 percent). A printed definition ("50% reduction") can differ from the plotted fit: calibrate the plotted curve before quoting the definition.
* "Restriction costs X" from one promoter pair is a general claim; a blind reader overturned it with Table S1 (GFAP and gfa1405 do not differ from CAG in intensity). State the observation about the promoter that was measured.
* A boxplot legend that does not define the whiskers: check whether any dot lies beyond them; here the ends are the extreme plotted points and the text's single area values equal plotted maxima.
* A link from a register to a peer's file that is not on main yet breaks the link check: write plain text, then link after the merge.
* Resuming a finished delegate by SendMessage for round 3 reuses its calibration (cheap, still blind to the notes); its earlier clauses are in its context.
* Disk 15 GB free at the last look; push floor 1.5 GB.

## Peers at writing
ADV a5e6f2ad (launches IT35 itself), SCI ba384503, HE 0a29d266 (re-run ListAgents).

## Landing state of BATCH_20261128_008
Committed as one commit, `development/main` merged without conflict, derived surfaces verified current (pathograph, both view checks), suites green before the merge (trace claim 22, pathograph 32, batch queue 52, candidate freshness 37, public claims 2, documented commands 4, section references 13; LINT WARN, no BLOCK). Pushed by `safe_push` at the end of this window; confirm with `git log development/main --grep BATCH_20261128_008` and `ci_runs.py status <sha>` or the anonymous API (item 2 above).
