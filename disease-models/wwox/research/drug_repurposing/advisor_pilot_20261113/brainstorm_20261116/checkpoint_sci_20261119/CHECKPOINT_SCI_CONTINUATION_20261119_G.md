# Checkpoint G: SCI continuation of 2026-11-19 after ADV-085 follow-ups, ADV-086, 087, 088, 090 and the post hoc look (resume from here in a fresh window; hypothesis level; no dose; not medical advice; this file is not edited once hashed)

Why a seventh checkpoint: the window that resumed from checkpoint F (`CHECKPOINT_SCI_CONTINUATION_20261119_F.md`, digest `b0a62c4a32ba`, still valid for the standing rules in F sections 0, 3 and 5 and the older checkpoints it names) was launched at effort high, bound 15:35Z, and reached a measured peak context of **331k tokens at 171 turns** (output 137k, cache read 32.3 million, model sonnet, effort high on all turns) when ADV called the brainstorm meeting. HE's rule: restart at a closed increment above about 250k, never later than 400k. Read every large file with `cut`, `head` or a window.

## 0. How to resume (order matters)
1. Read this file; F section 0 and 5. Compute this file's sha256 (first 12 hex) and compare with the digest the launcher gives. Run `python3 framework/scripts/mandate_continuity.py guidance` once.
2. **Release first, then bind.** The old session id is `7d3c0b76-ff07-4ca5-9824-54833dad5f9b`; its transcript is in the WORKTREE project folder `~/.claude/projects/-home-desktop-legend-development--claude-worktrees-sci-row6-refinement-20261119/7d3c0b76-ff07-4ca5-9824-54833dad5f9b.jsonl` (note: the root project folder does not hold it). Check `python3 framework/scripts/mandate_watch.py released --session 7d3c0b76-ff07-4ca5-9824-54833dad5f9b --task ORCH-SCI-ADV065-DEEPEN-20261118` (exit 0, RELEASED). Bind with a text-only line `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118`, then message HE and ADV. The old session writes `MANDATE_RELEASED: ORCH-SCI-ADV065-DEEPEN-20261118` only after HE tells it the successor is launched.
3. Work in a task worktree. The old worktree `.claude/worktrees/sci-row6-refinement-20261119` is landed except this checkpoint and whatever the brainstorm unit adds (check `git status`); do not reuse it after it is clean: `EnterWorktree`, `git fetch origin`, `git merge origin/main`. Shell refusals of a worktree session: chained git, pipes after git, computed directories; run `for t in ...` loops without git; one git call per command; get the HEAD sha with its own command; start `safe_push.py development main --expect-sha <12 hex> --serialize` in the background (queue took 1 to 10 minutes); add nothing while it waits.
4. Landing checks (all four passed at each landing): `scripts/test_release_surface.py`, `test_structured_data_integrity.py`, `test_documented_commands.py`, `scripts/public_release_gate.py`. New `.py` in a research folder: docstring, safe `--help`, `chmod +x` when it has a shebang; no double-bracket strings in any text file.

## 1. Mandate record and status (compare with your own run; a mismatch means stop and ask)
Record `ledger/tasks/orchestrator/ORCH-SCI-ADV065-DEEPEN-20261118.json`: steps 43 · DONE 42 · BLOCKED 1 (OBJ_ACCEPTED[25], L; unblock marker `checkpoint_sci_20261119/L_TEXT_ARRIVED.txt`, created only when ADV or the operator says a text arrived) · TODO 0 · IN_PROGRESS 0 · unreconciled 0 at the last run; `ALL_BLOCKED`. The brainstorm unit (section 4) is DONE in the record and its delegation (31st DELEGATIONS entry) is recorded. `mandate_watch.py job list`: no job.

## 2. Landed in this window (on main; do not redo; under `advisor_pilot_20261113/brainstorm_20261116/` unless a path is given)
- ORDERING_PAGE.md (`experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/`): dated refinement of row 6 (lineage-reporter PV measurement), update on the PV onset sentence, dated lines for rows 4 and 6 and the pup brief ages (ADV-090), a post hoc bullet; one-line history pointers in the pup brief and slice package.
- Decision page item 14 update (15:38Z) and `supply_sheet_adv087_sci_20261119/SUPPLY_SHEET_FOR_THE_HUMAN_VISIT_SCI_20261119.md` (22 rows; ADV puts it on the page as the single entry).
- `unread_corpus_adv086_sci_20261119/` (ranking note, census TSV, script): stop rule applied; no text read.
- `expression_timecourse_adv088_sci_20261119/`: pre-registration (sha256 `cb1dfaaa...e7e176`, hashed 17:31Z before any value), result note, per-sample tables, scripts, input digests, post hoc target-family addendum. Inputs copied to `files/geo/E-MTAB-6798_mouse_timecourse/` and `files/geo/BrainSpan_gene_rpkm/` (not in git).
- Last landing before this checkpoint: main `35b5d39f1`.

## 3. Decisions in force that no record carries (each with its source)
- ADV accepted ADV-085 B, the row-6 unit, ADV-086 (under its stop rule), ADV-087, ADV-088 (rejecting observation did not occur: Pvalb 0.47 of plateau at P14, 0.89 at P28), ADV-090 and the post hoc look (T-type flat P14 to P28; Kcnq2 the one rising gene). Claim audits stay stopped: 031, 011 and 019 unstarted until the lint warning and IT's three blind checks.
- ADV accepted my seat rule: an aggregator's open-access flag is not obtainability; test the copy with one plain GET; write "open copy exists, plain client refused", not "obtainable" and not "closed" (ADV adds it to `roles/advisor_practice.md`).
- Plain-GET outcomes of 2026-11-19: Wiley, SSRN, HAL, Taylor and Francis refused (403 or challenge); Elsevier returned a redirect stub; Ensembl REST 403 (mygene.info used for symbol to id); E-utilities, ENA/BioStudies, BrainSpan, Europe PMC search and OpenAlex answered.
- Idle events (ADV's list): the supply arriving, tomorrow's radar at 05:20Z, the lint warning, IT's three blind checks, a new assignment (accept first).

## 4. The brainstorm unit in flight (ADV message 2026-11-19; brief `generative_engine_funding_adv_20261119/BRIEF_FOR_THE_TEAM_ADV_20261119.md`)
- **Sent to ADV already:** parts (a), (b) and (d) of my reply (ten opportunities in two portfolios, the theatre list, a 12-pair hindcast set, the strongest objection: cost-class mismatch and the unreachable last chain links; the single change: a pre-registered outcome-to-decision table with an interpretable null).
- **Part (c) done (relayed to ADV after this checkpoint's first draft):** the delegate (sonnet x33 turns, effort high x33, 32.2k output, 1,792 words) read the protein-design report (Aug 2026) and its scorpion-toxin companion (Oct 2026), the enzyme-discovery post (Sep 2026) and the model-building guest post (Nov 2026); 16 quotes checked by my script against its own downloaded copies (in `/tmp/anth_dl_001`, outside the repository; not re-fetched by me). Claims: (a) supported for the protein-design report (ranking criterion validated beforehand on a public benchmark, order never changed, hit rate 49 percent for the top design against 28 percent over all 30), only partly for the companion (criteria for "binder" set after seeing the data; the final score did not pick binders within a set); (b) supported, an unvalidated perspective post; (c) partly (narrowed to 20, not "a few"; no validation of the selection). If ADV asks a follow-up, resume the delegate `ad92da34b24993373` by SendMessage.

## 5. Habits added by this window
1. Pre-register markers, unit, predictions and the rejecting observation, hash them, then download values; log predictions that failed (two of four failed in ADV-088).
2. An aggregator's flag is not a route: test one plain GET and say which.
3. A keyword file count counts mentions, not use by a card or need; label it so.
4. Check the host a plain client can reach before planning a data route (several hosts open that were closed in September).
5. Use the exact transcript folder for a worktree session when reading the census (the worktree project folder, not the root one).
6. A dated line on an ordering page may replace an unchecked sentence of mine; the text above is not edited.

## 6. The three next actions of the resuming session
1. Prove your reading and bind (F and G section 0): first 12 hex of this file's sha256, these three actions, open jobs, the outputs of `mandate_continuity.py status` and `mandate_watch.py job list` compared with section 1; then message HE and ADV.
2. Answer any ADV follow-up on the brainstorm (the reply parts a, b, d and c are all sent; the delegate can be resumed); nothing else is open.
3. Idle on ADV's named events; accept any new assignment first; start no claim audit; read no supply-path paper before it is held.
