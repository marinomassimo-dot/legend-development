# VPS recovery — 2026-09-25

> 🔴 **DO NOT DELETE `backup/vps-main-2026-09-25` OR `~/legend-vps-backup-2026-09-25.bundle`
> UNTIL THE HELD SCIENCE BATCH (§7) IS DECIDED AND CLOSED.** Today they are the only copy of every
> file listed in §5 as `DISPOSITIONED` — above all the VPS batch reports and the claim, ledger and
> working-model text §7 would re-derive.
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

| Group | Content | Commit |
|---|---|---|
| G1 | harness tooling (§4 lists what was left out) | `4be7217` |
| G2 | this note and [`inventory.tsv`](inventory.tsv); the 75 VPS task records were withdrawn again (they cite commits that exist only in the backup) | `d44c3e5`, `d626cde` |
| G4.1 | the manifest aligned with `WM_v5.0` / `BATCH_20260922_SEIZURE` (a state-control update, no batch) | `7b8b8d4` |
| G4.2 | receipt validator: a null parent admitted for a strictly earlier independent reading | `2690265` |
| G4.3 | the readings as one step: dossiers, manifests, queue entries (renumbered, §6), 29 receipts by rechain (207 → 236), the 37 VPS candidates re-queued, and the seven notes the receipts declare as outputs | `af09f7a`, `55803b5` |
| G4.4 part 1 | `BATCH_20260926_ALDAZ_R1`: the 25 readings registered in the paper registry, nothing propagated (PAPER 098–115) | `a364dab` |
| G4.4 science | **HELD for the operator** — §7 | — |
| G4.5–G4.6 | inventory accounting (every row RECOVERED or DISPOSITIONED); the retrieval manifest's +85-line append | this note's commit |

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

**Status 2026-09-26: carried out.** The validator rule landed in G4.2 (`2690265`, three tests plus a
missing-time case) and all 29 receipts were rechained in G4.3 (`af09f7a`); `fulltext_receipts.py
status` shows the complete VPS reading for 27869163 and 39868255 beside `main`'s later partial ones.
The three verification records below were not recovered (decision A1), so their links stay as they
are in the backup; the instruction applies if they are ever brought in.

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
`state_now`, `recover_with`, `disposition`, `detail`. It is a TSV and not a table here because most of those paths do not
exist on `main`, and the repository's documentation suites rightly refuse a Markdown file that
names a missing script.

Each row's `recover_with` is the exact command, `git show 06ee25a:<original_path>`;
`git cat-file -p <blob_in_06ee25a>` returns the same bytes. Counts per group:

| Group | RECOVERED | DISPOSITIONED |
|---|---:|---:|
| Commit candidates (G4) | 37 | 43 |
| Comparison notes (analysis) | 2 | 9 |
| Comparison notes (research) | 1 | 15 |
| Consolidation verifications | 0 | 4 |
| Deep-dive manifests (G4) | 30 | 0 |
| Full-text dossiers (G4) | 32 | 0 |
| Harness files not recovered or recovered in part (see §4) | 11 | 56 |
| Learning records not recovered (mandate-continuity package) | 0 | 2 |
| Mirror consultations | 0 | 9 |
| Other disease-model files (reports, current surfaces, analysis) | 3 | 63 |
| Page adjudications (G4) | 1 | 0 |
| Phase packets | 0 | 8 |
| Registries and receipt ledger (G4: redo via BATCH_COMMIT / rechain) | 1 | 7 |
| S2 second reading | 0 | 7 |
| Session evaluations | 3 | 15 |
| Task records (recovered in G2, withdrawn: they cite commits that exist only in the backup) | 0 | 75 |
| Task records not recovered (mandate-continuity package) | 0 | 2 |
| Verifications | 0 | 22 |
| **Total (458)** | **121** | **337** |

No row is unaccounted. The `disposition` and `detail` columns of the TSV give, per file, the landing commit or the one-line reason.

## 6 · G4.3 — full-text queue renumbering (VPS → `main`)

All 17 queue entries the VPS created collide with different entries on `main` (which runs to `FT-174`), and none shares its subject paper with a `main` entry, so each became a new entry, in order. Every reference to them in the recovered dossiers, manifests, commit candidates and queue entries was rewritten; each new entry says in its own text which VPS number it was.

| VPS entry | `main` entry |
|---|---|
| `FT-097` | `FT-175` |
| `FT-098` | `FT-176` |
| `FT-099` | `FT-177` |
| `FT-100` | `FT-178` |
| `FT-101` | `FT-179` |
| `FT-102` | `FT-180` |
| `FT-103` | `FT-181` |
| `FT-104` | `FT-182` |
| `FT-105` | `FT-183` |
| `FT-106` | `FT-184` |
| `FT-108` | `FT-185` |
| `FT-109` | `FT-186` |
| `FT-110` | `FT-187` |
| `FT-111` | `FT-188` |
| `FT-112` | `FT-189` |
| `FT-113` | `FT-190` |
| `FT-114` | `FT-191` |

Also applied in G4.3: the VPS updates to six existing entries `main` never changed (`FT-010`, `FT-038`, `FT-045`, `FT-057`, `FT-079`, `FT-085`); `FT-096` was left as it is, both sides having added the same separator. In the recovered live files, `PAPER 093`–`096`, VPS `WM_v4.x` and VPS batch ids are annotated in place `(VPS numbering, PMID …)` / `(VPS batch, never on main)`, and inline paths or links to records kept in the backup became `git show 06ee25a:<path>` commands.

## 7 · HELD for the operator — the science the VPS batches propagated

`BATCH_20260926_ALDAZ` (the re-derivation of `BATCH_20260913_001`–`004`, `BATCH_20260914_005`–`008` and `BATCH_20260915_009` on the current state) was **not run**. Two STOP rules of the recovery mandate fire, each on its own:

1. **Conflict with consolidated-baseline claims.** The VPS readings *narrow* two claims that are `consolidated baseline` on `main`, and `main` has not changed either since the split:
   - `CLAIM 006` — "progressive microgliosis and astrogliosis" becomes astrogliosis demonstrated as a *direction, not a rate* (pseudoreplicated statistics, n = 3 mice), microglial progression demonstrated for **morphology only**, microglial abundance unchanged between ages;
   - `CLAIM 007` — "P47T abolishes PPxY binding" becomes *near-abolishes* WWOX recovery by two PPPY oligopeptides *in vitro* (faint residual, n = 2/group; protein present in both genotypes).
   The same readings reach `CLAIM 030`, `CLAIM 033`, `PAPER 007`, `PAPER 042` ("the abundance/severity dissociation is NOT demonstrated") and `DL-MECH-033`. A locator audit is due before any of this touches a baseline claim.
2. **Overlap with the pre-existing backlog.** Every claim the VPS batches touched has open candidates on `main` (70 pre-existing, excluding the 37 recovered):

| Claim | Open backlog candidates on the same claim |
|---|---|
| `CLAIM 004` | 5: `CC-20260826-AAV9-ENDPOINT-SPLIT-01`, `CC-20260826-DOSE-ADJUDICATION-01`, `CC-20260826-DOSE-DECISION-TABLE-01`, `CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01`, `CC-20260826-FIVECLAIM-PACKAGE-01` |
| `CLAIM 005` | 7: `CC-20260826-EGABA-CLOSURE-01`, `CC-20260826-EGABA-EXPERIMENT-01`, `CC-20260826-FIVECLAIM-PACKAGE-01`, `CC-20260826-INDEX-PRIORITY`, `CC-20260826-PMID36828035-01`, `CC-20260826-UPSTREAM-CITATION-FAILURE-01`, `CC-20260922-CLAIM005-CHAIN-NAMING-01` |
| `CLAIM 006` | 4: `CC-20260826-CLAIM006-01`, `CC-20260826-CLAIM006-HARDENING-01`, `CC-20260826-PROVENANCE-01`, `CC-20260826-PROVENANCE-PAPER007-01` |
| `CLAIM 007` | 2: `CC-20260826-PROVENANCE-01`, `CC-20260826-PROVENANCE-PAPER007-01` |
| `CLAIM 011` | 12: `CC-20260825-ADVERSARIAL-FALSIFICATION-01`, `CC-20260826-AAV9-ENDPOINT-SPLIT-01`, `CC-20260826-CLAIM032-01`, `CC-20260826-CLAIM037-01`, `CC-20260826-CROSS-CLAIM-CENSUS-02`, `CC-20260826-DOSE-ADJUDICATION-01`, `CC-20260826-DOSE-DECISION-TABLE-01`, `CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01`, `CC-20260826-FIVECLAIM-PACKAGE-01`, `CC-20260826-INDEX-PRIORITY`, `CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01`, `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01` |
| `CLAIM 016` | 6: `CC-20260825-32000863-POINTER-01`, `CC-20260825-CLAIM016-DRIFT-01`, `CC-20260826-FIVECLAIM-PACKAGE-01`, `CC-20260826-GSK3B-S9-AXIS-01`, `CC-20260826-LITHIUM-BOUNDARY-01`, `CC-20260826-PMID36828035-01` |
| `CLAIM 025` | 2: `CC-20260825-GRAPH-MATERIALIZATION-01`, `CC-20260922-CLAIM025-SIGN-INVARIANCE-01` |
| `CLAIM 030` | 2: `CC-20260909-25331887-01`, `CC-20260920-DETECTION-FLOOR-01` |
| `CLAIM 032` | 5: `CC-20260826-CLAIM032-01`, `CC-20260826-INDEX-PRIORITY`, `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01`, `CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01`, `CC-20260922-GTGT-CNS-QUALIFICATION-01` |
| `CLAIM 033` | 1: `CC-20260921-CLAIM033-REPLICATION-01` |
| `CLAIM 037` | 8: `CC-20260825-ADVERSARIAL-FALSIFICATION-01`, `CC-20260826-CLAIM037-01`, `CC-20260826-CROSS-CLAIM-CENSUS-02`, `CC-20260826-CROSS-CLAIM-CENSUS-03`, `CC-20260826-FIVECLAIM-PACKAGE-01`, `CC-20260826-INDEX-PRIORITY`, `CC-20260826-UPSTREAM-CITATION-FAILURE-01`, `CC-20260922-CLAIM005-CHAIN-NAMING-01` |

**What the held batch would touch** (record-level three-way comparison, divergence point / VPS / `main`):

| Surface | Records the VPS changed |
|---|---|
| claim registry | 11 |
| paper registry | 21 |
| literature log | 48 |
| working model | 4 |
| discovery ledger | 14 |
| therapeutic hypotheses ledger | 2 |
| therapeutic strategies | 1 |
| research candidates | 1 |
| research lines | 3 |
| meta index | 1 |
| meta metabolism | 2 |
| disease_model.md | 1 |

Of the claim records, `CLAIM 005`, `011`, `016`, `030` and `037` were also changed on `main` after the split (`CLAIM 032` and `CLAIM 005` by `BATCH_20260921_001` / `BATCH_20260922_SEIZURE`): the VPS text must never be reapplied over them.

**Decisions this needs, per claim:** whether the narrowing of `CLAIM 006` / `007` enters canon (with the locator audit); for each overlapping claim, whether the recovered candidate or the backlog candidate goes first, or both in one batch. Also left with this batch: the LIT-status lint check (exception list calibrated on the VPS log; not activated), the 51 older candidates whose VPS disposition names a VPS batch, and the next working-model version (after `WM_v5.0`, MINOR or MAJOR by manifest § 2 — MAJOR if a baseline claim is narrowed).

## 8 · G4.0 collision map (VPS identifier → `main`)

| VPS | `main` | How |
|---|---|---|
| `FT-097` | `FT-175` | queue entry, §6 |
| `FT-098` | `FT-176` | queue entry, §6 |
| `FT-099` | `FT-177` | queue entry, §6 |
| `FT-100` | `FT-178` | queue entry, §6 |
| `FT-101` | `FT-179` | queue entry, §6 |
| `FT-102` | `FT-180` | queue entry, §6 |
| `FT-103` | `FT-181` | queue entry, §6 |
| `FT-104` | `FT-182` | queue entry, §6 |
| `FT-105` | `FT-183` | queue entry, §6 |
| `FT-106` | `FT-184` | queue entry, §6 |
| `FT-108` | `FT-185` | queue entry, §6 |
| `FT-109` | `FT-186` | queue entry, §6 |
| `FT-110` | `FT-187` | queue entry, §6 |
| `FT-111` | `FT-188` | queue entry, §6 |
| `FT-112` | `FT-189` | queue entry, §6 |
| `FT-113` | `FT-190` | queue entry, §6 |
| `FT-114` | `FT-191` | queue entry, §6 |
| `PAPER 093` (VPS) | `PAPER 101` | PMID 14526170, registered by `BATCH_20260926_ALDAZ_R1` |
| `PAPER 094` (VPS) | `PAPER 102` | PMID 28283473, registered by `BATCH_20260926_ALDAZ_R1` |
| `PAPER 095` (VPS) | `PAPER 103` | PMID 30285739, registered by `BATCH_20260926_ALDAZ_R1` |
| `PAPER 096` (VPS) | `PAPER 104` | PMID 15064722, registered by `BATCH_20260926_ALDAZ_R1` |
| `WM_v4.5`–`WM_v4.11` (VPS) | none | never on `main`; `main` is at `WM_v5.0` |
| VPS batch ids `BATCH_20260913_001`…`BATCH_20260915_009` | none | never on `main`; annotated in place in recovered files |

Other identifier families checked (LIT, CLAIM, CORPUS, DL, DIS, TX, HYP): the VPS created none, so nothing collides. New registry records took the next free numbers on `main` (PAPER 098–115; `main` stopped at PAPER 097).
