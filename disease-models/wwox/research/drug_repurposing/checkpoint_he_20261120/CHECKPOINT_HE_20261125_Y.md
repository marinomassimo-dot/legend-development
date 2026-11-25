# Checkpoint HE-Y (Harness Engineering, ACTOR_ID plan), 2026-11-25, written at ADV's request (context 264k)

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261125_W.md` and of the checkpoints it names
still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state

- Outgoing session `9c2cb46c-8e60-4327-a0d2-8bd697b72d51` (worktree `he_x_20261125`, branch `task/he-x-20261125`),
  model `claude-sonnet-5-5`, effort `high`.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. Never
  write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `ae0002e7`, IT Orchestrator `8e1d62bc` (re-run ListAgents; names roll over).

## 1 Done in this window; do not redo

- **Row-by-row re-check of the twelve ADV-098 compound sheets** (8a25046c9): 170 claims, 46 wrong or incomplete,
  corrected; report `RECHECK_ROWWISE_HE_20261125.md` in the sheets folder. The checks are now in
  `RECIPE_pull_activities.txt` (f9a8968c5).
- **Gate side scans in a second process** (9be73bce4, ADV GO, five conditions, landed alone):
  `HE_GATE_SIDE_SCANS_20261125.md`.
- **Report on stale card copies** (sent to ADV; summary in section 3 below).
- **Copied-card-sentence check** (item 1 of ADV's order): `framework/scripts/copied_card_sentences.py`, step 15 of
  `safe_push.py`, `--no-copied-sentence-check` leaves a trailer commit. Published d37743c774f12a6b85b7ff2ab2a85aed8a7097a7 (gate PASS, `ls-remote`); that push changed no card.
  - Replay over the 46 card-changing publications in the `development/main` reflog: it would have refused 12. The four
    inspected held the old text on the page at that publication (rebuilt later). The other eight were not inspected.
  - Seconds: median 2.9, at most 6.8; five cards with their packets (10 files) 4.3 s.
  - Not seen by it: paraphrases, translations, a clipped copy under 200 characters that is not a whole sentence.

## 2 Open, in order

1. **Ten-landing byte comparison of the gate side scans** (mandate step): when ten publications after 9be73bce4
   exist, `files/coordination/he_gate_proto_20261125/read_ten_landings.sh b07ec007b <ten SHAs>`, outside the lock.
   Old = the gate at b07ec007b. Any stdout difference reverts the gate change. Report gate and lock seconds to ADV:
   the lock is shorter only when the gate is the longest check (first landing: suites 121 s, gate 86 s, no saving).
   A later change of `scripts/public_release_gate.py` inside the window would make a difference legitimate: say so.
2. **Read after 2026-11-26 11:21Z** (mandate step; method in section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`).
3. **Queued by ADV, item 2:** wire `repurposing_coverage.py check` into `candidate_tree_freshness.py`; after wiring,
   regenerate once so the tree is current, as a separate landing. Today: DRIFT (`coverage_matrix.json` input hash;
   `priorities.json` reading-depth counts, `abstract_only` 6 against 5).
4. **Queued by ADV, item 3:** a `check` subcommand for `repurposing_join.py`, last. The 28 derived cards differ from
   a fresh run (18 s); regenerate once by the writer first, if IT agrees nobody reads it today. After it is current
   and checked, add `join/` to the surfaces of the copied-sentence check.
5. **Sheet corrections from IT's blind verifier** (when `VERIFIER_REPORT_AS_DELIVERED_A_IT24.txt` is on main, under
   `.../it24_checkpoint23_queue_20261125/`; one pass, dated first-written lines):
   - batch 6: the three-subtype panel CHEMBL1909046 ranks M4 first, so the M1-first order is the 2020 document's;
   - batch 7: miconazole CYP2C19 16 and CYP3A4 30 nM lie below CYP51 200 nM (and CHEMBL5096242 gives 0.02 and 1 nM,
     identical in rat and mouse microsomes: looks like another unit, check before use); rodent rows exist; the
     benztropine 0.95 nM row names no tissue; clobetasol IC50 against IC50 is about 2-fold (3.17 against 1.46 nM);
   - batch 8: PDK4 below PDK1 below PDK3 recurs in both documents that carry all three (PDK3 a bound in
     CHEMBL6121009); "the order is that document's only" is too strong;
   - batch 9: further flagged rows: AR-A014418 beta 104 uM (2023, activity 26184476) beside the 2011 one (6347904);
     the 2015 LY2090314 pair 1.5 and 0.9 uM (26228923/4) is flagged "Potential transcription error".
   Then tell ADV the added count (the 46 of 170 was what one reader found).
6. Standing: disk removals are ADV's; 2026-11-29 recheck and delete `files/adv174_negraes_custodian_he/`; the gate
   cache, the 4-worker CI line and the workflow patches stay operator-reserved. Free space at writing about 19 GB.

## 3 Copies of card sentences, their refresh and owner

Measured on 9be73bce4 (sentences of at least 60 characters; owner = who committed it since 2026-11-01).

| Copy | Built by | At landing | Owner |
|---|---|---|---|
| `view/index*.html`, `view/shareable_package/index.html` | `repurposing_view.py run`, `package` | view checks refuse; they compare against their inputs, so a stale input passes | IT |
| `ranking_it8_p9_20261029/ranking.json`, `units.tsv`, `unit_members.tsv`, `selections.tsv`, `member_evidence.tsv`, `investigations.tsv` | `ranking_it8.py run` | regenerated by `--regenerate-derived` (default) | IT |
| `ranking_it8_p9_20261029/investigations_it20.tsv` | by hand (curated positions) | only the copied-sentence check | IT (89 of 92 commits), ADV 3 |
| `coverage/assertion_pertinence.tsv` | by hand (curated judgements) | only the copied-sentence check | IT |
| `coverage/priorities.json`, `coverage_matrix.json` | `repurposing_coverage.py run` | not checked (item 3 above) | IT |
| `join/cards.json` | `repurposing_join.py run` | not checked, last committed 2026-11-20 (item 4) | IT |

Recommendation on the two hand-kept tables (report only): do not generate them. Their rows are judgements, not
projections; the repeated sentences are now guarded by the check.

## 4 Traps met in this window

- A ratio or range written from the rows in view: query all rows first (46 of 170 claims).
- A stale-copy detector must treat a page that shows the new card string in parts as current, or it refuses most
  honest card landings (17 of 46 before the rule, 12 after).
- A Monitor loop that greps the whole log each turn repeats one line forever: wait for the end marker only.
- `repurposing_join.py run --out <empty folder>` marks every adapter `NOT_ATTEMPTED`: copy `join/` there first.

## 5 First moves for the successor

1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE sections 21c to 21e, this file
   and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block,
   verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 item 5 if IT's report is on main; items 1 and 2 when their conditions hold; then item 3.
