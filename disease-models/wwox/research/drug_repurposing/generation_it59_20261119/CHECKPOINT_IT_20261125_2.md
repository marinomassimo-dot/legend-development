# IT checkpoint 14, 2026-11-25 (IT Orchestrator window 45a8b15c; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's word, context about 363k)

Read after checkpoint 13 (`CHECKPOINT_IT_20261125_1.md`), which is not edited and stays valid. Hypothesis level; nothing is medical advice; reference genotype class only. The only genuine operator message of this window is the launch prompt; everything else was peer messages (ADV, SCI), which are not operator authority.

## 1. Closed in this window (on `main` unless marked; do NOT redo)
| Item | Where | Result in one line |
|---|---|---|
| DC-04 repair | `350c9fe76` | two reopen-table verdict cells, N12 and N17 reopen text, triggers, views regenerated |
| ADV-241 | `it_adv241_20261125/`; `8f86db944` | dated re-triage lines on 11 map rows; DC-05 NOT checked (classifier stop), handed to HE as ADV-245 |
| ADV-244 | `it_adv244wording_20261125/`; `f8e3293dc`, `bca9c45d3` | organoid clone and batch limit ("four knockout organoids of one CRISPR clone against two parental organoids, apparently from one batch") on K01, D01, D02, M01, E02, I01, E01, E03, F01 and INV-16 |
| ADV-246 | `it_adv246_20261125/`; `2c1cad72b` | per-line protein against per-line function (Fig 1D, pixel read-off): NOT TESTABLE; candidate `CC-20261125-ORCHESTRATOR-ADV246-LINE-PROTEIN-01` PROPOSED |
| ADV-248 | `it_adv248_20261125/`; `2c1cad72b` | the week-7 plateau of altered lines is assay-undetermined (no hard cap shown; soft saturation not excluded) |
| ADV-247 wording | `it_adv247wording_20261125/`; `1c6e8abf8` | SCI's independence wording on cards and INV-02/06/07/08/15/16/19 with four-language clauses; candidate `CC-20261125-ORCHESTRATOR-ADV247-INDEPENDENCE-01` (CLAIM 002/005/007/014) PROPOSED |
| ADV-250 | `it_adv250_20261125/`; `1e4d9c86e` | of 7 not-stated unit rows one resolved (H1 weak: RNA-seq n named as mice) and six not resolvable (hippocampal libraries); library count is an upper bound on independent n |
| ADV-250 upper-bound wording | `it_adv250wording_20261125/` (landed after this file was drafted; verify with `git log origin/main -- <folder>`) | cards J01, F03 and INV-06, INV-15 extended; table copy with column `n_as_stated_is_upper_bound`; the first ADV-250 text said "the controls are not the same mice" without the condition: corrected to "if a library is one mouse" in RESULT and in the functional_it13_p3a README line |
| ADV-251 | `it_adv251_20261125/`; `c0a2dfb25` | knockout floor on the authors' own Supp Fig 1K: KO lanes 0.07 and 0.15 of WT (read-off); WT lane not saturated; calibration against the printed rescue values 0.8 and 1.4 FAILED (factor about 6); rule FLOOR_AT_OR_ABOVE_0.1; candidate `CC-20261125-ORCHESTRATOR-ADV251-KO-FLOOR-01` PROPOSED. Predictions P2 and P3 were wrong and are reported as such |
| Map-owner state | `open_questions_map.tsv` | ADV-241 dated lines on RS-NP3B3, RS-R2, DC-04, EN-03, EN-04, NR-01, NR-02, NR-04, NR-05, RS-R8, RS-R9 (no status changes); RS-R9 not yet updated with the ADV-251 floor (ready line below) |

Confirm the ADV-250 wording landing with `git log origin/main -- disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv250wording_20261125` (its first push was refused for generated-view conflicts and re-run).

## 2. Open items for the successor (none is mine to redo)
1. **ADV-251 line for RS-R9** and the radar question IT18: one dated line each (floor 0.07 to 0.15, calibration failed, no G137V value). Ordinary edit.
2. **Re-read the printed densitometry values on the other panels** (1L: 0.2, 0.4, 0.4, 0.9; 1M: 0.1, 0.1, 0.3, 7) against the originals on File012 pages 6 and 7: about 30 minutes, held raster; proposed to ADV in the ADV-251 result (DREAM). It would say whether the 0.1 to 0.3 values are themselves reproducible; ADV-251 showed the printed 1K rescue values are not reproduced from the same file's strip.
3. **DC-05** re-check is HE's (ADV-245); EN-03 is HE's.
4. **Candidates queued (all PROPOSED, nothing applied):** ADV238 P47T, ADV246 line-protein, ADV247 independence, ADV251 KO floor; the two reserved ones (CLAIM035 S9 wording part 2, WM103 dose wording part 2) stay the operator's.
5. Draft letters to authors, including the unit question for the hippocampal libraries and the neurosphere preparations, are the operator's to send; nothing sent by me.
6. **ADV-249 wording (relayed by SCI at ADV's request, 2026-11-25; not started by me):** (1) DL-MECH-032 (PMID 36572560): "this 2022 paper only lists WWOX among GID-motif proteins; binding and direction rest on Wang 2012 (CLAIM 035). No repurposing inference follows from this paper"; card D02 names the lead. (2) DL-BIO-003 and PAPER 050 (PMID 26857392): "a junction-versus-core RT-qPCR used in lymphoblastoid lines; not validated for detecting exon 9 loss; alternative 3' ends in intron 8 are cited from databases"; PAPER 050 says 'full text reviewed' while its only earlier receipt is all 'unknown_legacy' (a declaration is not an attestation; claim text only through a candidate). (3) DL-MECH-025: the notice is PMID 35680840, the lead gives the retracted article's PMID 28151481 as the retraction's. (4) DL-BIO-006: no change. Source: `brainstorm_20261116/adv249_unread_lead_primaries_sci_20261125/RESULT_ADV249_UNREAD_LEAD_PRIMARIES_SCI_20261125.md` (main 683e9535f). Ledger, paper registry and cards are the successor's lane; run test_batch_queue and the registry anchors before any registry edit. Held question, no action required: what the exon 8 to 9 amplicon loses with an exon 9 acceptor-site allele (RT-PCR exon 7 into the 3' UTR or long reads, carrier and control, with and without NMD block).

## 3. Lessons (for the role's active-lessons file, not for an operator memory)
1. **A peer-relayed inference can overreach; re-derive the condition before sending it.** I told ADV "the controls cannot be the same four mice" from 2 hippocampal against 4 cortical libraries; it holds only if a library is one mouse. Caught the same day, corrected in RESULT and README.
2. **A printed densitometry value is not an anchor until the strip reproduces it.** ADV-251's calibration check failed by a factor of about 6; a pre-registered calibration check is worth its cost.
3. **Rescue-lane band position can differ from the wild-type band** (16 rows above in the 1K strip), so a fixed window excludes it; report the registered window first and the post-hoc one as exploratory.
4. **Text-level insertion into packet JSON** keeps the file's indentation; rewriting with `json.dumps` produced a roughly 1000-line diff.
5. **The i18n helper's EDIT task** fails with a KeyError when the old key has no Italian entry (INV-15); drop the `it` entry for that task and let the baseline gap stand.
6. **Scripts that read downloaded images stay in a different directory from the data** (Python `-I` drops the script directory from the path; insert it explicitly).

## 4. DREAM line
Not consumed: arm sizes alone bound the independent n from above whatever a library contains, so the column `n_as_stated_is_upper_bound` could stand for every carried inference; the table copy exists in `it_adv250wording_20261125/`, SCI's original is unchanged. The ADV-251 floor makes RP-045's frozen prediction (untouched) a possible reader of the G372R limb once the candidate is applied.

## 5. First moves for the successor
1. Read this file and `git log origin/main --oneline -20`; confirm that the ADV-250 wording landed (ADV-251 is `c0a2dfb25`).
2. Bind per the mandate recipe; proceed message right after BOUND; never end a turn on the bind.
3. Take ADV's next assignment; with none open, propose the panel 1L/1M re-read (section 2, item 2) to ADV.
4. Landing recipe: new worktree from `development/main`, the six guard suites plus `legend_lint.py .`, `safe_push.py development main --expect-sha <sha> --serialize` through nohup with an exit marker and a Monitor; no commit in a worktree while its push waits.
