# VPS recovery — 2026-09-25

> 🔴 **DO NOT DELETE `backup/vps-main-2026-09-25` OR `~/legend-vps-backup-2026-09-25.bundle`
> UNTIL RECOVERY GROUP G4 IS CLOSED.** Today they are the only copy of every file listed in §5.
> Neither is published, and neither may be: both are local to the VPS.

**What this note is.** An index of work done on the VPS checkout between 2026-09-12 and
2026-09-17 that never reached `main`. That work lived on a `main` that had diverged from
`origin/main` (325 local commits against 244 remote ones). It is recovered **as files, never as
history**: no merge, cherry-pick or rebase of those commits.

| Item | Value |
|---|---|
| Source branch (local only, never published) | `backup/vps-main-2026-09-25` → `06ee25a` |
| Offline copy | `~/legend-vps-backup-2026-09-25.bundle` (verified with `git bundle verify`) |
| Divergence point | `83ec6be` (2026-09-11) |
| `main` at recovery | `84b0585` |
| Task branch | `task/aldaz-recovery-20260925` |

The scientific current files, `state_manifest` and `reading_state` were **not** copied from the
backup; what the VPS batches changed in them is to be redone by a new `BATCH_COMMIT` on the
current state, in recovery group G4 (a separate session).

## 0 · What has landed

| Group | Content |
|---|---|
| G1 | harness tooling, commit `4be7217` (§4 lists what was left out) |
| G2 | this note and [`inventory.tsv`](inventory.tsv). The 75 task records first recovered under `ledger/tasks/<actor>/` (all 77 VPS task IDs were free on `main`) were withdrawn: they cite commits such as `started_at_head` values that exist only in the backup, so on a clone of GitHub they can never resolve (`test_task_record_commit_hashes`). They are listed in the inventory like every other historical record |
| G3 → G4 | moved to G4 at the operator's decision, to land as one coherent step: the 29 full-text dossiers, the 28 new deep-dive manifests and the updated `PMID36828035` manifest, the page adjudication, the 29 read receipts (via `fulltext_receipts.py rechain`, never by hand), the validator rule below, and the full-text queue entries (`FT-…`) those artefacts cite |

The historical records (reports, session evaluations, Mirror consultations, phase packets,
verifications, comparison notes) are **not** kept in the repository: they cite tools, files and
queue entries that do not exist on `main`, and the repository's own reader-journey, documented-command
and link-target suites check every Markdown file. They stay in the backup, one `git show` away (§5).

## 1 · Identifiers that mean something else here

The VPS and `main` assigned the same identifiers independently. **In every file of the backup,
these identifiers carry their VPS meaning.** They
are not the `main` records with the same number.

| Identifier in these files | Meaning on the VPS | On `main` the same identifier is |
|---|---|---|
| `PAPER 093` | PMID 14526170 | a different paper |
| `PAPER 094` | PMID 28283473 | a different paper |
| `PAPER 095` | PMID 30285739 | a different paper |
| `PAPER 096` | PMID 15064722 | PMID 34140629 |
| `WM_v4.5` | result of `BATCH_20260913_001` | the result of `BATCH_20260921_001` |
| `WM_v4.6` · `WM_v4.7` · `WM_v4.8` | `BATCH_20260913_002` · `_003` · `_004` | not used |
| `WM_v4.9`–`WM_v4.11` | `BATCH_20260914_005` … `BATCH_20260915_009` (per-batch mapping in the archived batch reports) | not used |
| `BATCH_20260913_001`–`_004`, `BATCH_20260914_005`–`_008`, `BATCH_20260915_009` | VPS batches; **none of them exists on `main`** | — |

G4 note: the current working model is `WM_v5.0` (the state manifest still reads `WM_v4.5`, a
known drift to be healed through `BATCH_COMMIT`), so the recovery batch will not be `WM_v4.6`.
The next free `PAPER` number must be re-derived from `paper_registry_current.md` at that time.

## 2 · Instructions carried to G4

**Receipts.** 27 of the 29 VPS receipts rechain cleanly onto `main`'s ledger (dry run: 207 → 234
events, none of them citing the two below). Two cannot be recorded truthfully with today's
validator, which refuses a second root reading (`prior_receipt: null`) of a study, while the only
earlier receipt of each study on `main` is *later* than the VPS reading:

| VPS receipt | `analysis_at` | Committed in the backup at | `main`'s later receipt |
|---|---|---|---|
| `FTR-20260913-27869163-01` (complete) | 2026-09-13T15:10:14Z | `3751e3f935e1de05289ccd84e9e9319bff42c913` (2026-09-13 15:11:44 UTC) | `FTR-20260921-27869163-01` (partial, 2026-09-21) |
| `FTR-20260913-39868255-01` (complete) | 2026-09-13T14:13:08Z | `be0b5e484e79792fd05efc2346e9e19be106e788` (2026-09-13 14:16:54 UTC) | `FTR-20260923-39868255-01` (partial, 2026-09-23) |

The commit SHAs prove the `analysis_at` values are not backdated. Rule agreed with the operator:
`prior_receipt: null` is accepted **only** when `analysis_at` is **strictly earlier** than every
other receipt of the same study; equal or later stays refused. Tests: a positive case, a
negative case (a newer root) and a same-date case. `analysis_at` values are kept as recorded.
After the rechain, `fulltext_receipts.py status` for 27869163 and 39868255 must show the
complete VPS reading.

**Three wikilinks.** When the verification records are brought back, three wikilinks resolve by
heading text to the `main` record with the same number, which is a different paper. They are to
be turned into inline code, and nothing else in the text changed:

| File in the backup (under `disease-models/wwox/research/verifications/`) | Line | Original link, exact | Meaning on the VPS |
|---|---|---|---|
| 2026-09-13_aldaz_batch004_reexamination.md | 245 | `[[paper_registry_current#PAPER 093]]` (already inside a code span) | PAPER 093 = PMID 14526170 |
| 2026-09-14_aldaz_linkage_consultation.md | 339 | `[[paper_registry_current#PAPER 096]]` | PAPER 096 = PMID 15064722 |
| 2026-09-14_science_consultation_C.md | 315 | `[[paper_registry_current#PAPER 094]]` | PAPER 094 = PMID 28283473 |

Every other fragment wikilink in the recovered files was checked target by target against both
sides; the remaining differences (`CLAIM 007`, `TX-001`) are the same record with its text moved
on, not a numbering collision.

## 3 · Where the rest stands

See §0 for what landed and §4 for what did not; §5 lists every file.

## 4 · What was not recovered, and why

**Awaiting operator decision — the mandate-continuity package, in full.** It changes §21c
(reserved to the operator) and how agents behave: the `SAFE_DEFAULTS` additions to
`LEGEND_CORE` §21c and the §22 rewrite of "Stay passive. Await input."; the Stop hook in
`.claude/settings.json` and `.claude/settings.json.example`; `mandate_continuity.py` and its
test; `deployment/claude_settings_mandate_hook.json`; `roles/orchestrator.md` (goal and queue
execution); `governance/annex_a_task_contract.md` (A.1a, A.1c); `cross_session_transport.md`
(§8b, §12); the `CLAUDE.md` §1/§3 pointers; the legend-start step 3b;
`task_id_collision.py`, `task_dispatch.py`, `test_harness_followups.py`, which depend on it.

**To migrate in G4 — the LIT-status lint check** (lit_status.py, lit_status_legacy.json,
the lint function `_check_lit_statuses`). Its grandfather snapshot was taken on the VPS log of 2026-09-13 and
blocks 45 LIT records written on `main` since; re-snapshotting or migrating them is a
`BATCH_COMMIT` act.

**Also G4:** the 37 new commit candidates and the `BATCH DISPOSITION` blocks appended to 51
older ones (they point at VPS batches); the dismech reseal (`analysis/data/*`,
`reseal_dismech_baseline.py` and its test); the VPS-only updates to `PMID29724996`
(dossier and manifest), `PMID25331887` and `PMID42128308_partial_locators` dossiers, and
`retrieval_manifest.jsonl`.

**Left out because they would have changed newer `main` behaviour or turned a green suite red:**
the `claim_links` adoption in `trace_claim_foundation.py`, `pathograph.py` and
`generate_semantic_graph.py` (claim–paper bindings 189 → 140 on `main`'s registries; the
`claim_links.py` module itself is recovered for `support_linkage`); the stricter
`session_self_eval.unread_premises` (unread premises 0 → 45); the `registry_records.py`
rewrite (`main` solved the same defects differently; `two_sided_notices` and the "OUT OF SCOPE"
message are not ported) and `comparison_check.py`, which depends on it; the neutral-subject
block in `scripts/legend_commit.sh`, contradicted by a newer `main` test; the skill description
rewrites and `skill_description_census.py`; the VPS `scientist_standing_brief.md`.


## 5 · Every file that exists only in the backup, or differs there

[`inventory.tsv`](inventory.tsv), next to this note, lists every path the VPS commits touched
whose blob in `06ee25a` is not the blob in this repository after G2 — absent on `main`, or
present with other content (for a harness file recovered in part, the backup holds the whole VPS
version). 458 rows, one per file, tab-separated: `group`, `original_path`, `blob_in_06ee25a`,
`state_now`, `recover_with`. It is a TSV and not a table here because most of those paths do not
exist on `main`, and the repository's documentation suites rightly refuse a Markdown file that
names a missing script.

Each row's `recover_with` is the exact command, `git show 06ee25a:<original_path>`;
`git cat-file -p <blob_in_06ee25a>` returns the same bytes. Counts per group:

| Group | Files |
|---|---|
| Commit candidates (G4) | 80 |
| Comparison notes (analysis) | 11 |
| Comparison notes (research) | 16 |
| Consolidation verifications | 4 |
| Deep-dive manifests (G4) | 30 |
| Full-text dossiers (G4) | 32 |
| Harness files not recovered or recovered in part (see §4) | 67 |
| Learning records not recovered (mandate-continuity package) | 2 |
| Mirror consultations | 9 |
| Other disease-model files (reports, current surfaces, analysis) | 66 |
| Page adjudications (G4) | 1 |
| Phase packets | 8 |
| Registries and receipt ledger (G4: redo via BATCH_COMMIT / rechain) | 8 |
| S2 second reading | 7 |
| Session evaluations | 18 |
| Task records (recovered in G2, withdrawn: they cite commits that exist only in the backup) | 75 |
| Task records not recovered (mandate-continuity package) | 2 |
| Verifications | 22 |
