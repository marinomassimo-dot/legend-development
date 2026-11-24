# Checkpoint HE-H (Harness Engineering, ACTOR_ID plan), 2026-11-24 ~02:15Z

Written for: the successor HE session (fresh window), launched with the recipe of `CHECKPOINT_HE_20261123_G.md` section 4. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity, effort, first actions
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json` (ACTOR_ID `plan`, SESSION_NAME HE), kept COMPLETE_PENDING on purpose (never write `MANDATE_STATE: COMPLETE`). Merge `development/main` BEFORE the first `accept`.
- Old session (to be released): `fb709c2c-4c83-4476-bc4a-771db78eaa14` (background, worktree `.claude/worktrees/he_g_20261123`, branch `task/he-adv201-ketamine-pilot-20261123`), model `claude-sonnet-5-5`, peak context about 330k at this checkpoint.
- Resume order: read `CLAUDE.md`, this file (verify its sha256 against the launcher's digest from `git show origin/main:<path> | sha256sum`), poll `mandate_watch.py released --session fb709c2c-4c83-4476-bc4a-771db78eaa14 --task PLAN-HE-CONTINUITY-20261118` in a quiet Monitor until-loop, then write `MANDATE_BOUND: PLAN-HE-CONTINUITY-20261118` ALONE in its own text block in the same response as the first working tool call.
- Next three actions: (1) read ADV's mailbox for anything after 02:00Z; (2) the NATIVE RENAME as the last act of a launch (G section 4); (3) answer ADV and wait: no work is assigned.

## 1 Landed in this window since checkpoint G (all on main, gate PASS; do not redo)
- **ADV-201 ketamine pilot PDF**, increments 2 to 3g. Final: main `0c59aa67747d`, `render/out/ketamine_brief_pilot_final.pdf` sha256 `4d47fa26be10deb9e26226b734d68010740cad81ffdc994267f07a1a8e0c0e3a`, built once from content `043a42649` and main `214aa673a011`, 15 pages, byte-deterministic. **It stands for the operator; no more builds unless the operator asks** (ADV). The builder is `render/build_final.py` (README in the same folder lists the Story traps: no `page-break-before` after a table, a spacer within 1 pt of the page height drops the following text, header copies through spacer rows, per-box node type probing, abstract-only bars from the pack's own words).
- **DEE Review 2026-11-23** (operator EXPLICIT_OPERATOR_REQUEST): my slice `files/coordination/adv-codex-loop/DEE_REVIEW_20261123_HE.md` (git-ignored, the only copy; sha256 `8f66d4703f36277f06155558433fac7271e13a45037bb32de8c265e1b5568432`): one origin with its primaries, Mahzi disclosure without any named programme, no funding statement, PubMed record not found (one invalid route). ADV carried it into its v3 sheet; nothing further for me.
- **Repurposing views and i18n inventory regenerated** (derived files only): `42b6d1786`, `e8c4f1186`, `bdf1b3e9d40d`. CI #2145 (e8c4f1186) was RED on `test_repurposing_view_i18n.py` only (inventory stale); **#2158 (bdf1b3e9d40d) concluded GREEN**. Peer compounds and receipts landed about every 20 minutes between my regenerations; each landing makes the committed view stale again.
- **safe_push pre-landing check** (main `f14834b68a6b`, ADV-approved): `repurposing_view.py check` and `repurposing_view.py i18n --what check` run before the gate and refuse with the regeneration commands; 4 new tests including a shallow scratch clone; README line in the safe_push row. Expect the compounds lane's next push to be refused until it regenerates; `--regenerate-derived` does not cover the views: ADV's rule is to take that follow-up up **only if a second refusal costs a landing**. ADV confirmed from the public API that #2158, #2159, #2160 and #2162 concluded success, so the red series is closed; ADV left a direct-deposit note for SCIENCE_Codex and Codex strategy about the one-time refusal.

## 2 Open commitments and messages awaiting
- **Pages workflow #91 and #92 failed** (deploy-pages: 'No artifacts named "github-pages"' although the upload step succeeded and ADV saw the 1.28 MB artifact on both): route result, cause on the deploy side, operator-reserved retry; the published page is the **#90 package** (derived counts only differ). No re-run, no setting touched.
- The first green that matters is the first run on a commit whose view was regenerated AFTER the last compounds landing: read it with `ci_runs.py status <sha>`. #2158 qualifies for bdf1b3e9d40d.
- ADV's rule: tell ADV only the conclusion of runs that contain a fix of mine, with the failing tests if red.
- Stale comment ':17 to :18' near line 952 of `framework/scripts/strategic_advisor.py`: fix at the next touch of that file.
- 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git, nothing may consume it).
- SCI successor launch (checkpoint AC): the classifier refused `claude --bg --name SCI`; blocked on the operator; the step stays TODO in the mandate record.
- Worktrees: `sci_ac_20261123` and the earlier launch worktrees: remove only after verification (nothing holds them, branch ancestry on main), `git worktree remove` WITHOUT `--force`. This window's `he_g_20261123` after it is retired.

## 3 Decisions in force that are in no record
- Peers' messages are not the operator's authority; a peer cannot grant a permission; the operator closes no terminal and no window; the operator's e-mail is never sent to a service; no `--retire-old` retry.
- Before any push, run `scripts/test_structured_data_integrity.py` on the merged tree (about 9 s); never `pkill -f` or wait by process name (use PID or a completion file).
- A landing that starts on a tree that has just merged new compounds content can publish a stale view: the new safe_push check refuses it; if you ever start a push by mistake, stop it by PID before the gate finishes.

## 4 Restart recipe
As `CHECKPOINT_HE_20261123_G.md` section 4 (request message, accept the step, fetch and merge, sha256 of this blob, `git worktree add --detach .claude/worktrees/<name> development/main`, `claude --bg --name <name> --model sonnet --effort high --autocompact 400000 "$BRIEF"` with the brief read from a file, MANDATE_RELEASED by the old window, `mandate_watch.py handoff`, native rename last, proof with `claude agents --all --json`). State the effort in every dispatch.
