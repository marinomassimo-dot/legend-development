# Checkpoint HE-AJ (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 20:20Z

Written for: this same window if it compacts, or a successor if ADV launches one (ADV prefers compaction: a successor costs 0.5 GB).
The traps of `CHECKPOINT_HE_20261128_AI.md` still hold (AH to AE are background). Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Session `7ec59b7e-77be-41cb-b6ee-18e5418ea490` (roster "HE - CURRENT 7ec59b7e"), worktree `he_ai_20261128`, model `claude-sonnet-5-5`, effort `high`.
  Bound to `PLAN-HE-CONTINUITY-20261118` (verified BOUND). Predecessor c72e94ee released and PREVIOUS.
- Mandate: 197 steps, 195 DONE, 2 BLOCKED (166 classifier, 182 dated); `status` says ALL_BLOCKED; never write COMPLETE.
- Reply to the operator in Italian, files in English. Codex lane PAUSED by the operator (the PAUSED file stops only the timer: a Codex app-server was
  live and landing on 2026-11-28; do not contact, wake or read it). Peer names change: run ListAgents before each message (IT is "IT Orchestrator - CURRENT <id>").
- Context peak 270k at 20:12Z; ADV asked for compaction rather than a successor. Disk 3.07 GB free at 20:13Z, falling about 1.5 GB per hour; push floor 1.5 GB, stop below 1.0.

## 1 Done in this window (all on `development/main`)
- Disk drop measured and attributed (successor worktrees 0.5 GB each; Codex files; transient landing clones): reports sent to ADV.
- `framework/scripts/disk_born.py --since ISO [--until ISO]` (e0d8a3206): what was born in a window by birth time, read-only, 69 s; README row; `test_disk_born.py`.
- `HE_PAGES_SMOKE_PATCH_20261128.md` in this folder: operator-reserved retry-on-mismatch patch for the Pages smoke step; not applied.
- ADV-338 (86eb87f8e): blind image read of Repudi 2021 Suppl Fig 5G and 7F; sent to ADV and IT40.
- ADV-339 packet H1-H6 for IT43: `files/coordination/adv339_it43/he_table.tsv` (HOLDS 37, NOT_SUPPORTED 1, UNSETTLED 3, NOT_GRADED 5); delegate raw table beside it. Closed.
- Receipt-artefact hunt (PMIDs 17803050, 19500159, 23254685, 17360458): digest search over files/, uploads, jobs, /tmp (not claude-1000), tmp, Downloads; result sent to IT44 (receipt owner) and ADV:
  23254685 MISPLACED as another form (PMC XML sha256 09901452ce85..., under `~/.claude/jobs/9945c156/tmp/verify3/out/pmc/23254685.xml`);
  17360458 html ABSENT, manifest PDF present and digest-correct; 17803050 and 19500159 ABSENT. Repair is IT44's (new receipt with prior_receipt; dated pointers).

## 2 Open, in order
1. **CI #2974** (tip 2488f1f4, the first run containing IT42's repair 79f886ef7; red runs #2962-#2968 were `test_manifest_receipt_provenance`) and #2982: read the
   annotations when completed (`python3 framework/scripts/ci_runs.py status <sha>`), tell ADV green or the failing suite. A background loop was armed in the old
   context and dies with it; re-arm a poll every 5 minutes if this is a new window.
2. **2026-11-29 not before 00:01Z: custodian step (mandate step 182).** Recheck that nothing consumes `files/adv174_negraes_custodian_he/` (root checkout, outside git,
   9 entries: key, predictor file, scorers v1/v2/v3, sealed note; see memory `adv175-scoring-pitfalls` and `RESULT_HE_ADV174_NEGRAES_20261122.md` section 6),
   ask ADV once whether any reader needs a sensitivity, then delete that folder and record step 182. Arm your own wake (CronCreate for 00:03Z is session-only);
   the one armed in this window (job f587a8a5) dies with this session.
3. **Disk:** ADV wants a report if disk is above 3 GB at 23:30Z or a successor decision. Largest reclaimable pile found: `/tmp/tmp*` 3.05 GB, 3.01 GB older than
   24 h (old Chromium probe profiles); not removed, ADV decides. `disk_born.py --since <ISO>` answers the next drop in one command.
4. Worktree removal stays FROZEN until the operator decides (`branch_hygiene.py --removal` is the only rule; step 166 stays BLOCKED).
5. ADV sends data tasks with a named consumer; if idle, tell ADV.

## 3 Traps of this window
- Tool-shell `find` is bfs; `/usr/bin/find` (GNU) has no `-newerBt`. Python statx (birth time) works; a zero result is a result only if the inode count is not zero.
- `safe_push --serialize` already regenerates derived surfaces, runs the landing suites and the gate; start it with `nohup bash -c '...' < /dev/null` and a completion
  file, watch with a Monitor on the file. Never commit while one waits.
- A blind reader's non-HOLDS atoms and the tables behind the contested atoms must be re-read by you before hand-back; the delegate's raw table is kept.
- Image panels: `pdftocairo -svg` per page, parse paths, calibrate on the drawn ticks; the SEM computed from the extracted points equals the drawn error bar when no
  point is hidden.
- Memory notes: `he-ai-find-and-disk-pitfalls`, `vector-figures-before-pixels` (updated).

## 4 First moves for a reader of this file
1. State manifest (`current_state: READY`), this file (verify its sha256 from `development/main` after `git fetch development main`), `mandate_continuity.py status`.
2. Section 2, in order. Rename nothing.
