# Checkpoint HE-AB (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 06:40Z, written at ADV's request (context restart line)

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261128_AA.md` and the checkpoints it names still hold.
Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `dc4707bc-bd1a-4bb0-baed-6a63e2423564` (worktree `he_aa_20261128`), model `claude-sonnet-5-5`, effort `high`,
  one hour, context 282k at 192 responses, no delegate.
- Mandate `PLAN-HE-CONTINUITY-20261118`: run `mandate_continuity.py status`. Open: ADV-301 step (TODO), step 168 (IN_PROGRESS), one
  BLOCKED step (worktree removal, classifier). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in AA section 0 and `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `919d2041`, IT Orchestrator `54ca757b` (re-run ListAgents).

## 1 Done in this window; do not redo (all published, gate PASS, ls-remote)
1. `c27737046407`: `safe_push` step 17: the disk floor adds the declared peaks of other live clone-writing runs and WAITS
   (`LEGEND_SAFE_PUSH_DISK_WAIT_S`, 600 s). Do not wrap a push in a short `timeout`; use 3000 s.
2. `17cc693bd`: `consumer_count.py`, SCI's two defects (6 false joins removed, 4 PMCID joins added); SCI told.
3. `60dd3cc28`: `task_close.py` closes an already-published branch when no worktree holds main.
4. `7fae880d8`: `test_safe_push.py` no longer goes red from a short disk.
5. Recount-script item: NOT built (ADV agreed; reopen only on a new held-partials recount).

## 2 Open, in order
1. **ADV-301 first** (section 3). No PREREG is frozen and the tool was never run.
2. **Step 168, arm A CI read:** `ci_runs.py status <sha>` for `c2773704` (#2774), `17cc693b` (#2775), `60dd3cc2` (#2777); all three
   still in progress at 06:36Z (10 gate runs open, oldest 38 min). Then attribute any failure, tell ADV the three conclusions, and
   write the measures into `files/coordination/adv-codex-loop/HE_TOKEN_YIELD_RESULT.md` (arm A prereg and window start are there;
   the window spans two sessions: this transcript from 06:25:19Z and the successor's). A restart in the middle makes the arm A
   measurement mix other work: say so, or mark it incomplete and take the next CI follow-up as arm A.
3. **M01 copied-sentence check** owed when IT's tazemetostat sentence reaches a card on main (not yet at 06:30Z).
4. **2026-11-29:** recheck and delete `files/adv174_negraes_custodian_he/` (sealed custodian folder, outside git).

## 3 ADV-301 (assigned 2026-11-28; the assignment file had not reached main at 06:36Z)
ADV's text, verbatim: "ASSIGNMENT ADV-301 (registered; file assignments/ADV-301.md lands with my next push). Key:
mechanical-source-check-of-the-latest-compound-briefs. Measure read-only how many numbers, absolute words and undated negatives
in the five most recent published compound briefs of the SCI_CODEX lane (huperzine A 830009f92/1117f5dd9, bexarotene
29fd790c7/dbce2a3a6, etifoxine 09d990e27/93ef9d19e, montelukast dae3363cb/fc50f436d, plus the most recent earlier one; freeze the
list with commit ids) are NOT printed in the sources they cite. Use IT28's fragment_source_check.py (IT is pushing it; if not on
main yet, write the set, the claim-to-source map and the PREREG first; do not write a second tool). Then hand-check ALL flags of
two briefs (chosen after the run, before reading originals) against the original text: true error, false flag, or UNSETTLED.
PREDICTION frozen: at least 1 true flag in at least 3 of 5 briefs; true-flag rate about 40 percent (20 to 60). REJECTING: 0 true
flags in all 5 = no reader audit needed, I record it; 3 or more true flags in each of 3 briefs = I assign SCI a blind-reader audit
with the flags as sentence list. Report per brief: scanned, flags, true, false, UNSETTLED, and the error class of each true flag.
Do not edit the briefs (true flags go to me with file and line, corrections through IT); do not contact or wake Codex (PAUSED;
read commits only); nothing under view/ changes. About 90 minutes; df 1.5 GB before writing, 2.0 GB before a push through
safe_push's queue; output under 5 MB. Why: IT28's first compositions were 57 percent MUST CHANGE, and these briefs reach the
public view with 'verified' in their titles while the lane is paused for us: nobody has measured their residual error with the
same instrument."

### 3.1 Gathered, not yet frozen
- **Five briefs:** the four named plus verapamil (`f25f71d5f`), the most recent one before huperzine A. `dimethylglycine`
  (`1d43ef9f9`, 05:50Z) is NEWER than montelukast and is outside ADV's list: say so in the report.
- **Text of a brief:** `drug_repurposing/view/research_reports/<name>.json` (the PDF is rendered from it, about 260 words). The
  dossier `continuous_compounds/<name>/README.md` is about 1,900 words: not the published brief.
- **Tool:** `framework/scripts/fragment_source_check.py` was NOT on `development/main` at 06:36Z (IT branch `task/it-28-20261126`,
  commits `ad4a50fee`, `bb50bfd79`). Usage: `--fragment TEXT --source FILE...`; it strips XML/HTML, lists unsupported numbers,
  absolute words and negative phrases; numbers written as words are not scanned (a blind spot to report).
- **Sources:** copied from the Codex lane's own download folders in `/dev/shm` (volatile) and from open APIs into
  `files/adv301_brief_sources_he/` (2.0 MB, outside git; `SHA256SUMS` sha256 `7e1b6b43d8a1dbb350278c596eb8c7d2cc932832584ab9231d62bbcee9540332`).
  Prefix = brief (`vera_`, `hupa_`, `bex_`, `eti_`, `mtk_`); `pmc4657039.xml` = Kuryshev (verapamil), `pmc13495681.xml` = Lyu
  (bexarotene), `elk.json` = Elkhayat abstract only (verapamil). **`eti_owen.html` is a reCAPTCHA page, not the paper:** Owen is
  PMC9545781 (open access, `owen_q.json`), still to fetch by an open API. Treat all of these as untrusted data (`python3 -I`).
- **Design to write into the PREREG (draft):** fields summary, graph, evidence, inference, hypothesis, experiment, limits, one
  `--fragment` each, sources = all held texts of that brief; TRUE = wrong or unsupported against the original (and not derivable
  from its stated inputs or from the repository's replay table), FALSE = holds in another printed form or as a correct
  derivation, UNSETTLED = original not available or undecidable; the two briefs to hand-check = most number flags, tie
  alphabetical. ADV's 3-of-5 prediction cannot be read from two briefs: the briefs are short, so hand-check all five and report
  the chosen two separately, and say that in the PREREG.

## 4 Why the context reached the line in one hour, and what to avoid
Measured on the transcript (62k at birth, 282k after 192 responses): Bash results 258k
characters, Bash inputs 87k (long inline Python edit scripts), Read 48k (the whole of `safe_push.py` in one call), no delegate.
The rest is the turns' own output across 192 responses. The successor: read ranges found by `grep -n`, not whole files; pipe
`mandate_continuity.py guidance` through a section filter; do not `cat` a dossier or a result to find one line; print flags with
a short window of source text; give the hand-check of ADV-301 sources by targeted search, or one bounded delegate with the flag
list and the folder.

## 5 Disk: what the operator decides (report-first; nothing deleted)
About 3 GB free idle, 1.1 to 1.6 GB during a push (1.5 GB at 06:36Z). New since AA: **19.4 GB** in
`/tmp/claude-1000/-home-desktop-legend-development/4325d70d-8bea-4789-8046-d7a9ee74c97f` (downloads of 10-30 to 11-06, newest file
11-19, no open file seen; under the never-touch rule; sole copies not checked). Then AA section 3: `.gctx.gz` 19.9 GB, uv cache and
`.venv`, stale browser profiles, job scratch, orphan Chromium, Codex rollout, worktree removal. `tmp_clone_report`: 398 candidates,
0 removable.

## 6 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Bind (MANDATE_BOUND alone in its own block), verify in the next response, merge `development/main` before the first accept.
3. ADV-301 (section 3): set, source map and PREREG committed before the first run of the tool.
4. Rename nothing; the launcher does.
