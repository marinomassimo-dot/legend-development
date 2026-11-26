# Checkpoint HE-Z (Harness Engineering, ACTOR_ID plan), 2026-11-26, written at ADV's request

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261125_Y.md`, `..._W.md` and of the
checkpoints they name still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state

- Outgoing session `6e20e53e-b8fc-4a37-8618-b14adfa0fd96` (worktree `he_y_20261125`, branch `task/he-y-20261125`),
  model `claude-sonnet-5-5`, effort `high` on 155 of 155 turns; peak context 366k with one compaction.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. Never
  write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`, except
  its worktree keep-age line (section 3).
- Peers at writing: ADV `a5e6f2ad`, SCI `488a3ad0`, IT Orchestrator `b0ccd111` (re-run ListAgents; names roll over).

## 1 Done in this window; do not redo

- **Coverage `check` wired** into `candidate_tree_freshness.py`, with regeneration passes so coverage then ranking
  settle in one run (fb48f8fd4, published d746bc3aa). `--all` 21.2 s before, 25.2 s after.
- **`repurposing_join.py check`**, `join/` regenerated (it was last committed 2026-11-20), `join/cards.json` now a
  surface of the copied-sentence check; views rebuilt in every language (published e26debb56). A marked clip of the
  current card sentence no longer counts as a stale copy.
- **Gate side scans, ten-landing byte comparison:** 10 of 10 stdout identical (old b07ec007b against new). Standalone
  gate median 104.5 s old, 78.5 s new. ADV: KEEP. The lock saving is counted from landing logs only (a landing is
  shorter only when the gate is the longest check).
- **Copied-sentence check, replay of 12 refusals:** each had at least one copy that was truly stale (replaced later by
  a rebuild); none was wholly false. Four also carried a clip of the sentence that the documented repair could not
  clear; marked clips now pass. Language pages need `view run --lang all` (the hint says so).
- **Copied-sentence check, watch since d37743c77:** 17 publications, one changed cards (b29ec350f) and the check
  **did not run** on it: the pushing process had the older `safe_push.py` in memory. Replayed: 8 stale texts in 13
  files, all cleared later on main (true lags). Zero refusals so far.
- **`safe_push.py` refuses when the merge changed `safe_push.py` itself** (published 82df54cbad6b7fa9e114f405aaf0729e11d01f99,
  58 tests; the new test fails without the refusal). It protects only processes started from this version on.
- **`branch_hygiene.py --removal` keep-age:** 6 h for a window that released its mandate, 24 h otherwise (0bcb39077).

## 2 Open, in order

1. **CI red read after 2026-11-26 11:21Z** (the one TODO mandate step; method in section 6 of
   `HE_CI_MINUTES_GATECACHE_20261125.md`; reds before and after 565196e5e apart, selector gaps apart).
2. **Copied-sentence check:** nothing owed by count (more than ten publications since landing), but only one changed
   cards and it was not checked; look at the next card-changing landings when IT's queued card edits land.
3. **Worktree removal: BLOCKED on the operator** (section 3).
4. Standing: 2026-11-29 recheck and delete `files/adv174_negraes_custodian_he/`; the gate cache, the 4-worker CI line
   and the workflow patches stay operator-reserved.

## 3 Disk

- **The auto mode classifier denied the removal batch** ("Destructive or Unwanted Actions") at about 00:09Z on
  2026-11-26. Nothing was removed or moved. Not retried, not passed to another session; the operator was asked in
  chat and given the command. Do not retry it in another form.
- Keep-age provenance: ADV's decision record (meeting `MEETING-20261121T113510Z-83lyojx8.md`, entry 23:46Z) says the
  "PREVIOUS window of the last 24 h" line is ADV's own brief text, not the operator's, and replaces it with 6 h for
  released windows under five conditions. The operator may change it.
- Free at 00:09Z: 15,530 MiB. A worktree is about 0.5 GB (research/drug_repurposing 385 MB of 508); windows rotating
  as on 11-25 add about 12 GB a day.
- Rule met at 00:08Z: he_n, he_o, he_s, it_17, it_18, it_20, sci_ag, sci_ah, and it_19 once its ignored `backup/` is
  moved to `/home/desktop/legend-keep/`. Later: sci_aj and it_21 00:39Z, he_t 00:40Z, then through 06:07Z; run
  `branch_hygiene.py --removal` for the live list.
- **Operator items, nothing done:** (a) 24 orphan headless Chrome roots, 292 processes, all older than the fix
  16a01c945; they pin he_g (roots 2287716, 2314090, 2340084), p022b (1777302), it_successor_n (4127341) and
  `~/legend_browser_tmp` (1.6 GB). (b) `~/q230p-tooluniverse-blind` 5.9 GB (possibly the only copy). (c)
  `files/geo/GSE92742` 55.9 GB (remove only after a checksum proves re-download). (d) The two `/tmp` input folders
  of the paused Codex lane (2.4 GB, public downloads; SCI: no open item; created by rollout 2026-11-23T07-37-06;
  ADV: HOLD). SHA-256 taken 2026-11-25:

```
baf63adf424d1a07e5430984b90b0387fb30dc730d2faa35bc974bced7a3c499  /tmp/legend-ethosuximide-inputs/GSM3590948_hNSC.bed.gz
a4c66d8f9b953401037c1995815770e598e4eca2cc7a5cd785ce546125527204  /tmp/legend-ethosuximide-inputs/GSM3590949_hNSC_WWOX_del.bed.gz
ec54c0cab6eea8c78012179fd8b3511f07f238b0e430c6bcbeb96b7d28eb9bfb  /tmp/legend-ethosuximide-inputs/GSM3590950_neurons.bed.gz
01310b88ccc5bc15f8974c2aeeaf458e87fc98c0fb37ae16449358a2cde0b4a7  /tmp/legend-ethosuximide-inputs/GSM3590951_neurons_WWOX_del.bed.gz
daf41b6c1a7465f71e0de1e680b973249b9345bab6adad15b48acd620ea30062  /tmp/legend-ethosuximide-inputs/hg19-ncbiRefSeqCurated.txt.gz
d8f149adc357633c844c5979b48c175fcc56c3aadcc5641d25f6b8b295458d85  /tmp/legend-wwox-qr-inputs/GSE158681_family.soft.gz
a8cbe334cf6b6f5087a9af043bf23c94a5585020e3c4e51a262f1075588d85a0  /tmp/legend-wwox-qr-inputs/GSE158682_family.soft.gz
0bb3012f45e2474b8ce79911c47de0fc216bd574c60f1ddc8a8d911cd8a32b4d  /tmp/legend-wwox-qr-inputs/Homo_sapiens.GRCh38.cdna.all.fa.gz
c1dd87068c254eb53d944f71e51d1311964fce8de24d6fc0effc9c61c01527d4  /tmp/legend-wwox-qr-inputs/hg38.fa.gz
56d575332384e2386b6e6dae427248db26d259af5fa903f3315419f56f73c7db  /tmp/legend-wwox-qr-inputs/NM_000826.6.gb
```

## 4 The eight ADV-098 sheets with no blind check (for ADV to route; do not run the pass)

Folder `advisor_pilot_20261113/adv098_agent_sheets_he_20261119/`. Batches 6, 7, 8 and 9 had IT's blind check
(corrections a35593273). "Consumers" is a name search of 2026-11-25, not a reading of each document.

| Batch | Compounds | Claims | Card consumer | Other consumers |
|---|---|---|---|---|
| 1 | ethosuximide, lithium, memantine | 15 | none found | selection and assignment documents (14) |
| 2 | Kv7: ezogabine, azetukalner, ICA-069673, XE991 | 11 | none found | selection and assignment documents (11) |
| 3 | ganaxolone, gaboxadol | 13 | J01 | |
| 4 | NMDAR class: ketamine, memantine, dAP5 | 20 | none found | selection and assignment documents (7) |
| 5 | vigabatrin, bumetanide | 11 | none found | selection and assignment documents (9) |
| 10 | tazemetostat, TMP195, 10058-F4 | 15 | M01 | |
| 11 | T-type: apinocaltamide, ulixacaltamide, TTA-A2 | 14 | H01 | |
| 12 | M1 comparators and TMP195 class IIa null | 8 | none found | `batch_sci_20261105/map/open_questions_map.tsv` |
| total | | 107 | | |

The one earlier row-by-row pass by the same author corrected 46 of 170 claims, and IT's blind check of four batches
still found more.

## 5 Traps met in this window

- `pkill -f <pattern>` kills your own shell when the pattern is in its command line: act on PIDs.
- A "no process in this worktree" count must match cwd by prefix: mine matched only the root and reported none where
  six Chrome processes sat in `framework/scripts/`.
- A task id merely quoted in a transcript is not a bind: judge the marker lines.
- A harness change lands on disk before the publisher's process has it: ask which version RAN before reading silence
  as a pass.

## 6 First moves for the successor

1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE sections 21c to 21e, this file
   and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block,
   verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2: item 1 when its time has come; item 3 only on the operator's answer.
