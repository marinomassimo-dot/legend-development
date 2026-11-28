# Checkpoint HE-AG (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 14:00Z

Written for: the successor HE session (ADV launches it), past the context line (270k at turn 120). The traps of `CHECKPOINT_HE_20261128_AF.md`
and of the checkpoints it names still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `0a29d266-6ebe-43f8-bcaf-cfeb7990d12a` (worktree `he_af_20261128`, detached), model `claude-sonnet-5-5`, effort `high`.
  No delegate running, no monitor needed. It releases when the successor asks.
- Mandate `PLAN-HE-CONTINUITY-20261118`: 191 steps, TODO 0, DONE 189, BLOCKED 2 (step 166, step 182). `mandate_continuity.py status` says
  ALL_BLOCKED; never write `MANDATE_STATE: COMPLETE`. New work arrives as an ADV assignment: accept it with `mandate_continuity.py accept` (one distinct `--source` each).
- Reply to the operator in Italian, write files in English. Codex lane PAUSED. Peers change names: run ListAgents before each message.

## 1 Done in this window; do not redo (all on `development/main`)
- **CI watch:** #2855 failed on `test_trace_claim_foundation` only (it predates IT's `012cbea51`), #2856 succeeded; ADV told.
- **Landing selector, `f71e635fd`:** the red streak #2811 to #2826 (55 minutes) came from CLAIM 016 breaking `test_derive_dismech_sidecar`,
  which no landing ran; the selector now runs its one reproduction test on a claim, paper, receipt or DisMech-data change.
  Measured: fails at `e8f112188`, passes at `8c5fef3f3`; about 6 s.
- **ADV-318** (`81ca3dd48`): blind Crawford 2010 reading, `brainstorm_20261116/adv318_blind_crawford_he_20261128/BLIND_READING.md`.
- **ADV-323** (`1c49447d9`): blind Chornyy 2025 reading under `advisor_pilot_20261113/brainstorm_20261116/adv323_blind_chornyy_he_20261128/`;
  Table S1 checked 55 of 55 against the PDF text layer.
- **ADV-324** (`a522ab0f1`): `programme_cards` display groups fixed (two regexes); 40 of 199 cards moved; the blind reader agreed with
  all 200. Counts before and after: Targeted comparison 81 to 111, Assessment available 37 to 0, Follow-up deferred 83 to 90, Priority 2
  and Lower 1 unchanged. Record: `advisor_pilot_20261113/brainstorm_20261116/adv324_programme_cards_he_20261128/RESULT_ADV324_HE.md`.
  It does not create a research-priority ordering; ADV and SCI's ADV-322 decide that.

## 2 Open, in order
1. **ADV-324 gap:** the README's shareable-view classes (`test_repurposing_view.py DeepenedCasesShareable ShareableAudit It6P13Data
   It21P7InvestigationsContext`) were stopped at 342 s by HE when host memory fell to about 500 MB; no result. The audit reads card names and links,
   never `group`, so no effect is expected. Rerun only if ADV asks and the host is quiet (see traps).
2. **2026-11-29 or later:** recheck and delete `files/adv174_negraes_custodian_he/` in the root checkout (sealed, outside git). Step 182, BLOCKED on the date only.
3. **Worktree removal is frozen** (ADV, 2026-11-28) until the operator decides; obey `branch_hygiene.py --removal`, never `git status` alone. Step 166 stays BLOCKED (classifier, never retry).
4. The two operator questions of AE section 2 item 4 (`/tmp/claude-1000` scratch, the `LEGEND_REGRESSION_JOBS` CI line) are unanswered and not HE's to decide.
5. After the custodian recheck, if ADV has no assignment: tell ADV and propose one measured micro-upgrade.

## 3 Traps of this window
- **Memory:** the view suite plus its Chromium took 1.3 GB while available memory was 495 MB; the harness reaped a waiting `until` loop and
  said not to restart it on its own. Check `free -m` before any browser suite; stop your own PID (never by name).
- No writes to the worktree while a `safe_push` runs (REFUSED unclean tree); a delegate writes only under `$CLAUDE_JOB_DIR/tmp`.
- `cd` in the Bash tool persists: a `cd <result folder>` changed the working directory for the next calls. Start commands with the worktree path.
- A blind reader that returns only two classes in 41 s used a lexical rule: say so in the record (done in ADV-324 section 1).
- Delegates: model and effort were read back with `session_model_census.py --json <subagents>/agent-<id>.jsonl`; a delegate told not to open repository files
  does not read `delegation_budget.md`, which is why its dispatch states model and effort.
- A guard run needs a rejecting observation: run the new selector rule or test on the red tip and the green tip, and on the old module (`PYTHONPATH` order).

## 4 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Ask the old session to release; bind in the same response as the first working call, verify in the next, merge `development/main` before any accept.
3. Section 2, then tell ADV when idle. Rename nothing.
