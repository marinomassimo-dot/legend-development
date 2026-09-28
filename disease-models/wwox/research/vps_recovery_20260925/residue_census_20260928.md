> **Provenance.** Persisted by the Orchestrator's dispatch of 2026-09-28 from a read-only census
> produced by ACTOR_ID `junior-harness`; the repository was not modified by it.
>
> **ONE MECHANICAL TRANSFORMATION, and no word, figure or heading is changed.** §2.2's table names
> `LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md` as an inline repository path — and says in the same
> cell that it is *"absent on `main`"*, which is exactly what
> `scripts/test_fresh_clone_reader_journey.py::test_inline_repository_paths_resolve` refuses: a
> reader-facing document may not name a file a fresh clone does not have. The one occurrence was
> rewritten into the retrieval command for it, which is this recovery's own established convention
> for a path that exists only on another ref (README §6: *"inline paths or links to records kept in
> the backup became `git show 06ee25a:<path>` commands"*). The path itself is unchanged inside the
> command, and the sentence around it is untouched. Nothing else in the text is altered — the
> classifications, counts, verdicts, honest limits and DEFAULTS_TAKEN are the census author's own
> words. The publication gate was PASS with 0 blocks before and after, and needed no digest expanded.

# VPS residue census — 2026-09-28

**Actor:** `junior-harness` (READ-ONLY mandate). **Repository:** `/home/desktop/legend-development`.
**Measured against:** `main` = `cf40b737a2b274afeb09f2bf40495d1a7b8b2f3b`.
**Nothing in the repository was written and no git ref was changed by this census.** The only
writes are this file and a scratch extraction of the backup tree, both under the session
scratchpad. No `checkout`, `merge`, `cherry-pick`, `push`, `reset`, branch or worktree removal.

---

## 0 · The frame, re-derived

| Fact | Measured value | How |
|---|---|---|
| `main` | `cf40b737a2b274afeb09f2bf40495d1a7b8b2f3b` | `git rev-parse main` |
| `origin` and `development` heads | **identical, 13 refs each**; `refs/heads/main` = the same SHA | `git ls-remote --heads` on both, diffed |
| Nothing unpushed on `main` | confirmed | local `main` SHA = remote `main` SHA |
| `backup/vps-main-2026-09-25` | tip `06ee25a`, **325 commits ahead / 416 behind**, **311 unique patches** | `git rev-list --left-right --count`, `git cherry` |
| Divergence point | `83ec6be9fff33e14fef5253a1fc2a7d58cdb7aa8` (2026-09-11) | `git merge-base` |
| Paths the VPS branch touched | **488** (merge-base → tip) | `git diff --name-only` |
| Paths differing today (backup-only + differing) | **499** (222 backup-only, 277 differing; 320 further paths exist only on `main`) | `git diff --name-status main backup` |
| Offline bundle | `~/legend-vps-backup-2026-09-25.bundle`, 21 050 409 bytes, **okay, complete history**, exactly `06ee25a2e80ee61c8c7fd888bfbb51b6fc09f1d9` | `git bundle verify` |
| Receipt ledger | **OK, 259 chained receipts**, tail anchored | `fulltext_receipts.py verify` |
| Structural LINT | **WARN** (no BLOCK), matching the manifest's `last_lint_result` | `legend_lint.py .` |

Two independent copies of the VPS `main` therefore exist (branch + bundle) and both are intact.
Neither may be pushed, published or deleted — reserved under LEGEND_CORE §21d
("irreversible deletion of unique material", "publication to the public release repository").

---

## 1 · The 311 unique patches, classified

### 1.1 Method

The 311 patches are classified **by the fate of their content**, not by whether git considers
the patch applied. Three measurements compose the verdict:

1. **Blob equality** of every one of the 488 VPS-touched paths between `06ee25a` and `main`.
2. **The recovery `inventory.tsv` disposition** for the 458 rows it carries (audited in §1.4).
3. **Where a disposition is a promise rather than a fact** — the 20 "held for the operator"
   rows and the 43 "re-disposition belongs to the held science batch" rows — the promise is
   **tested against `main`'s current state**: for the 37 recovered commit candidates, the
   verdict in their *last* `BATCH DISPOSITION` block; for claims, the narrowing record now in
   the registry.

Content-loss control: for each of the 75 `RECOVERED` rows whose path differs from `main`, the
fraction of the backup version's substantive lines (>25 chars) absent from `main`'s version was
measured. **Median 1.6 %; zero rows above 20 %.** The differences are the documented
transformation (FT renumbering §6, `PAPER 093`–`096` → `PAPER 101`–`104`, VPS batch ids
annotated in place), not dropped content.

### 1.2 File-level classification — all 488 VPS-touched paths, by subject group

Legend: **a** = on `main` (re-derived or landed by another route) · **b** = not on `main`, still
live · **c** = not on `main`, superseded/obsolete · **d** = harness/tooling · **e** = private or
unpublishable · **R** = reserved to the operator.

| Subject group | a: on `main` | a: on `main`, `main` moved since | b: live (open candidate) | b: live (deferred) | c: historical, backup-only | c: obsolete by construction | d: harness superseded | R: reserved | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Task-ledger + learning records | 3 | 0 | 0 | 0 | 0 | **75** | 0 | 4 | 82 |
| Commit candidates | 75 | 0 | **4** | **1** | 0 | 0 | 0 | 0 | 80 |
| Reading artefacts (dossiers, manifests, adjudications) | **63** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 63 |
| Harness scripts and tests | 29 | 4 | 0 | 0 | 0 | 0 | **17** | 7 | 57 |
| Other disease-model files (analysis, research, therapeutics) | 12 | 0 | 0 | 0 | **44** | 0 | 0 | 0 | 56 |
| Verifications, consultations, second readings | 0 | 0 | 0 | 0 | **42** | 0 | 0 | 0 | 42 |
| Harness docs, protocols, roles, skills | 6 | 1 | 0 | 0 | 0 | 0 | **22** | 9 | 38 |
| Comparison notes | 3 | 0 | 0 | 0 | **24** | 0 | 0 | 0 | 27 |
| Session evaluations | 3 | 0 | 0 | 0 | **15** | 0 | 0 | 0 | 18 |
| Registries, current files and metas | **16** | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 17 |
| Phase packets | 0 | 0 | 0 | 0 | **8** | 0 | 0 | 0 | 8 |
| **TOTAL** | **210** | **5** | **4** | **1** | **133** | **75** | **40** | **20** | **488** |

Zero paths unclassified.

**Group totals in the mandate's own vocabulary:**

| Class | Paths | What it is |
|---|---:|---|
| **(a) on `main`** | **215** (210 + 5) | 121 by the recovery's own landings (G1/G4.1–G4.3/R1–R7), 46 byte-identical, the rest re-derived or regenerated from `main`'s inputs. The 5 are paths the recovery landed and `main` has since moved on again. |
| **(b) not on `main`, still live** | **5** | 4 open commit candidates + 1 deferred. Named in §3. |
| **(c) not on `main`, superseded/obsolete** | **208** | 133 kept in the backup by the operator's decision A1 as historical record; 75 task records that cite commits existing only in the backup (`test_task_record_commit_hashes` refuses them on `main` by construction). |
| **(d) harness/tooling** | **97 total** — 29+4 on `main`, **40 superseded**, 7+9 = 16 reserved, 1 registry-side | the 40 are the §4 "would have changed newer `main` behaviour or turned a green suite red" set: the `claim_links` adoption in three generators, the stricter `session_self_eval.unread_premises`, the `registry_records.py` rewrite and `comparison_check.py`, the `legend_commit.sh` neutral-subject wrapper, the 20 skill-description rewrites and `skill_description_census.py`. |
| **(e) private / patient-level / unpublishable** | **0** | see §1.5 |
| **(R) reserved to the operator** | **20** | the mandate-continuity package in full (§21c/§21d change). Distinct class: reserved is not private. |

### 1.3 Commit-level rollup — "would replaying this patch add anything to `main`?"

Each of the 311 patches is labelled by its **worst-case** path (the class furthest from
"landed"), because a patch carrying one unlanded file is not a landed patch.

| Verdict | Patches |
|---:|---|
| 150 | every remaining path is an **obsolete-by-construction** task/ledger record |
| 45 | every remaining path is a **historical backup-only** record (decision A1) |
| 44 | carries **harness content superseded by newer `main`** |
| 43 | **fully absorbed** — every path is on `main` |
| 23 | carries **reserved** mandate-continuity content |
| 3 | fully absorbed, `main` has since moved the same paths |
| **2** | carries an **open live commit candidate** |
| **1** | carries the **one deferred live candidate** |
| 0 | merge / empty-tree commits |

**Only 3 of the 311 patches carry scientifically live content not on `main`.** By dominant
subject: task ledger + learning 103 · other disease-model files 57 · registries/current/metas 39
· verifications 35 · harness scripts 20 · reading artefacts 17 · commit candidates 13 · harness
docs 12 · comparison notes 9 · phase packets 4 · session evaluations 2.

### 1.4 Testing `inventory.tsv`'s claim — where it holds and where it fails

**The coverage claim holds.** Tested three ways:

- All **458** rows name a path the VPS commits genuinely touched (`458 − 488 = 0` inventory rows
  outside the VPS-touched set).
- The **30** VPS-touched paths the inventory omits were **byte-identical to `main` at the
  inventory's own epoch** (`e1173ca`), which is exactly the criterion §5 states — correctly
  excluded, they had landed in G1.
- Of the **89** paths that differ today but are absent from the inventory, **60** already
  differed at `e1173ca` — but **all 60 are paths the VPS commits never touched**. They differ
  because `main` moved after the divergence point. **True inventory omissions: 0.**

**The RECOVERED claim holds.** All 121 `RECOVERED` rows exist on `main` at their stated path
(46 byte-identical, 75 differing by the documented renumbering; zero absent; zero above 20 %
line loss).

**Where the claim fails — the `disposition` column is stale, and it is stale in the one place
that matters.** `inventory.tsv` was last written at `e1173ca` (2026-09-26) and has **not** been
regenerated since, while the README header *was* updated twice afterwards (`59f7af3`,
`6af2182`). Consequences now measurable:

1. **20 rows still read "held for the operator: science the VPS batches propagated into this
   surface; re-derivation stopped by the mandate's STOP rules".** That hold was discharged by
   `BATCH_20260926_ALDAZ` and `_R1`–`_R7`. A reader who trusts the TSV believes the VPS science
   is still parked; a reader who trusts the README header knows it is not. The two disagree, and
   the TSV is the machine-readable one.
2. **43 rows still read "re-disposition belongs to the held science batch".** Measured: **39 of
   the 43 now carry a post-2026-09-26 `main` disposition**; only 4 do not (§3.2). The TSV cannot
   distinguish the 39 from the 4.
3. **"No row is unaccounted" is true of rows and false of work.** `DISPOSITIONED` conflates
   "decided never to bring in" (208 rows) with "deferred to a batch that has since partly run"
   (63 rows). The column has no state for *deferred-and-since-discharged*, so the only way to
   learn which of the 63 are done is the measurement in this census.
4. **The recovered-candidate count is 37 in §5 and §4, and 37 files are on `main`** — the
   earlier reading of "36" is an artefact of globbing `CC-2026091[345]-*`: the 37th is
   `CC-20260912-29724996-02.md`, dated before the 0913 prefix. The README's own count is right;
   any census that greps by the three dates undercounts by one.

**The one thing the inventory never claimed and should not be read as claiming:** it is a
*file* census. It does not assert that the content of a `DISPOSITIONED` historical record is
redundant, only that the file was accounted for. See §5.

### 1.5 Class (e) — private, patient-level or unpublishable material: measured, and empty

The backup tip was extracted to a scratch tree (1 541 files) and the repository's own
publication instrument was run against it:

```
python3 scripts/public_release_gate.py --root . --mode staging --skip-clean-clone
VERDICT: PASS      BLOCKS: 0      exit=0
```

Thirteen `[REVIEW]` lines (twelve `PARENT_OF_ORIGIN_ATTRIBUTED`, one
`PUBLIC_BIBLIOGRAPHIC_AUTHOR`), every one attributed to a published study whose variants are not
the reference genotype's — the same review class `main` carries. **No block, in any class.**

So the prohibition on the backup branch is **not** a privacy finding. It rests on §21d's
*irreversible deletion of unique material* and *publication to the public release repository*,
and on the operator's standing instruction. Stated plainly so nobody retires the branch on the
grounds that "the gate says it is clean": the gate says it is clean; the reservation is about
uniqueness and publication, not contamination.

---

## 2 · The two unmerged remote branches — 27 unique patches

**Every other `origin/claude/*` branch is fully contained in `main`.** Verified for all twelve:
ten are `git merge-base --is-ancestor <branch> main` = true with **0** unique patches
(`aqp-benchmark-i-retrieval-95sng8`, `aqp-hot-cold-state-qmlnl1`,
`legend-architecture-evaluation-zovohw`, `legend-v0-q230p-tx007-9im8zv`,
`main-sync-debt-audit-jsy454`, `overnight-autonomous-queue-w09aop`,
`overnight-frontier-expansion-bd1hbc`, `primary-evidence-ingestion-6bjq6h`,
`wwox-next-scientist-batch-n74f0z`, `wwox-woree-autonomous-scout-paqlty`). **None of the twelve
is contained in the backup** — they are a different lineage entirely.

### 2.1 `origin/claude/legend-autonomous-woree-tv6gz8` — 20 unique patches, last 2026-09-21

28 paths. **The four scientific current files are NOT touched.** What it touches beyond
`analysis/`: the receipt ledger (append-only carve-out), `state_manifest_current.md`
(state-control), and four derived surfaces (`batch_queue.md`, `coverage_report.md`,
`reading_state.md`, `surface_census.md`) plus `full_text_queue_current.md`.

| Class | Paths | Detail |
|---|---:|---|
| **(a) on `main`** | **13** | byte-identical: the Adelaide and Lodz node discriminators, the c517−3 RNA-rescue handle, the FT-116 cohort triage, the human genotype/`CLAIM 025` wave-1b and prenatal-infant wave-1 notes, the lectin readout note, the MAVE-portability note, the missense rescue-methodology census, the missense/splice reclassification-risk note, the next-node scout, the staging-dossier audit, the WOREE therapeutic-class census, the WWOX activity-sensor census |
| **(a) on `main`, `main` ahead** | **9** | `main`'s version is a superset or a later regeneration: `mechanism_intervention_map.md` (6 % of branch lines absent), `wwox_myelin_oligodendrocyte_census` (6 %), `batch_queue.md` (7 %), `full_text_queue_current.md` (9 %), `reading_state.md` (12 %), `coverage_report.md` (20 %), `surface_census.md` (33 %), `AUTONOMOUS_SESSION_STATE.md` (60 % — a per-session scratch state, not content), `state_manifest_current.md` (45 % — state-control, never copied) |
| **receipt ledger** | 1 | 🟢 **`fulltext_read_receipts.jsonl`: 0 of 200 branch lines absent from `main`'s ledger.** Every receipt this branch appended is already chained on `main`. |
| **(b) not on `main`** | **4** | `analysis/claim_foundation_spot_check_20260921.md`, `analysis/tx007_window_and_ceiling_20260921.md`, `analysis/wwox_localization_third_lab_20260921.md`, `therapeutics/tx007_monitor_update_20260921.md` — **zero references to any of the four anywhere on `main`** |

Of those four, the TX-007 window/ceiling material reached canon by another route:
`CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01` is on `main` and was propagated by
`BATCH_20260927_004`. The remaining three (claim-foundation spot check, third-lab localization,
TX-007 monitor update) are **analysis-layer files with no canonical counterpart** — live but
non-canonical; landing them changes no current file. **(d)/(e): none.**

### 2.2 `origin/claude/q230p-molecular-state-systemic-yruqvc` — 7 unique patches, last 2026-09-22

13 paths. **The four scientific current files are NOT touched.** No registry, no ledger, no
state manifest. It touches `analysis/`, `research/`, one commit candidate, and two files under
`framework/instruction/`.

| Class | Paths | Detail |
|---|---:|---|
| **(a) on `main`, `main` ahead** | **4** | `full_text_queue_current.md` (1 % of branch lines absent), `LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md` (1 %), `native_primitive_scorecard_20260922.md` (30 %), `AUTONOMOUS_SESSION_STATE.md` (8 %, scratch state) |
| **(b) not on `main`, live** | **8** | `analysis/q230p_fractionation_and_orthogonal_detection_20260922.md`, `analysis/q230p_nascent_synthesis_discriminator_20260922.md`, `analysis/systemic_rescue_mechanism_and_peripheral_panel_20260922.md`, `research/recursive_reread_3_4_units_20260922.md`, `research/FINAL_REPORT_fifth_run_20260922.md`, `research/OPERATOR_DECISION_PACKET_7_20260922.md`, `research/session_evaluations/2026-09-22_orchestrator_fifth_autonomous_run.md`, **`research/commit_candidates/CC-20260922-CLAIM038-UNIT-CLASS-02.md`** |
| **(d) harness** | **1** | `git show origin/claude/q230p-molecular-state-systemic-yruqvc:framework/instruction/LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md` — absent on `main`; the PROPOSAL beside it is on `main` and 1 % ahead. A shadow-mode instruction file for a method that shipped as the optional `legend-discovery-method` skill: **probably superseded**, and that judgement needs a reader, not a count. |

The load-bearing item is **`CC-20260922-CLAIM038-UNIT-CLASS-02.md`**: `main` carries
`…-UNIT-CLASS-01`, and `-02` is the later revision. It is the only commit candidate on either
remote branch that `main` does not hold in any version.

**Summary for both branches:** 27 unique patches · 12 paths absent from `main` · **0 touch the
four scientific current files** · 1 commit candidate at issue · 0 private/unpublishable
material · the receipt ledger is fully absorbed.

---

## 3 · The scientific residue, ranked — §7's two STOP rules tested against the current registries

Measured with `registry_records.py get --id …` (never by reading a registry wholesale) and by
reading each candidate's **last** `BATCH DISPOSITION` block.

### 3.1 STOP rule 1 — conflict with consolidated-baseline claims: **DISCHARGED**

| §7 target | State on `main` at `cf40b73` | Verdict |
|---|---|---|
| `CLAIM 006` | Title now *"P47T model shows progressive hippocampal astrogliosis; microglial progression shown for morphology only"*; `Evidence boundary` carries the pseudoreplication (subfields/cells as the unit, n = 3 mice), the two-time-point "direction not rate" inference, the undeclared multiple-comparison correction. Carries a **Narrowing record (`BATCH_20260926_ALDAZ`)** that names the blind locator audit (R4, three rounds) over `FTR-20260913-36828035-03`, no proposition OVERSHOOT/UNDERSHOOT/NOT_IN_SOURCE. `consolidated baseline` kept. | ✅ narrowed **and audited** |
| `CLAIM 007` | Title now *"P47T abolishes **or near-abolishes** WWOX recovery by two PPPY peptides in vitro"*; summary carries n = 2/group, the faint lane-discrete residual band, protein present in all four lanes and unquantified. Narrowing record as above, **plus** a *Mechanism provenance boundary* from `BATCH_20260926_ALDAZ_R7` with its blind audit at `research/locator_audits/2026-09-26_B7_blind_audit.md`. | ✅ narrowed **and audited twice** |
| `CLAIM 030` | touched by `BATCH_20260926_MALLARET`, `BATCH_20260927_003`, `BATCH_20260928_001` | ✅ reached |
| `CLAIM 033` | touched by `BATCH_20260927_003`, `_004` | ✅ reached |
| `PAPER 007` | survival-curve boundary, white-matter/Olig2 boundary with the region-vs-animal pseudoreplication (locator entry 64, `BATCH_20260928_001`), the `CC-20260826-PROVENANCE-PAPER007-01` clinical-relevance proposal explicitly **not adopted** | ✅ reached |
| `PAPER 042` | touched by `BATCH_20260926_MALLARET`, `BATCH_20260927_002` | ✅ reached |
| `DL-MECH-033` | carries `FM-014` — *"abundance ≠ function, and abundance measures are not commensurable"* — naming the three non-commensurable assays by construct | ✅ the dissociation caution is written |

**§7's rule 1 no longer fires.** Nothing in the VPS residue narrows an unaudited baseline claim.

### 3.2 STOP rule 2 — overlap with the pre-existing backlog: **DISCHARGED, 33 of 34**

Of the 34 distinct backlog candidates §7 tabulated across `CLAIM 004/005/006/007/011/016/025/030/032/033/037`:

| State | Count | Which |
|---|---:|---|
| **Consumed** by a `main` batch disposition | **32** | `BATCH_20260926_ALDAZ` (the four `CLAIM 006`/`007` provenance and hardening candidates), `_R6` (`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01`), and `BATCH_20260927_001` / `_002` / `_003` / `_004` (the remaining 27) |
| **Dispositioned `DEFERRED`** — stays queued | **1** | `CC-20260909-25331887-01` |
| **Open**, no disposition block at all | **1** | `CC-20260826-PMID36828035-01` |

**Every overlap §7 named is resolved except one open and one deferred candidate.** Total
commit-candidate queue today: 153 files, 130 with a `BATCH DISPOSITION` block, **23 without**.

⚠️ **A counting trap the Orchestrator should know about.** The 37 recovered VPS candidates all
carry a `## BATCH DISPOSITION` header — but for 13 of them the *first* such block is the **VPS**
disposition, naming `BATCH_20260913_004` / `BATCH_20260914_006`, batches that never existed on
`main`. Any tool that answers "is this candidate consumed?" by testing for the presence of a
`BATCH DISPOSITION` heading counts those as done on the strength of a batch that does not exist.
The honest test is the **last** block's actor and batch id. Run that way: **36 of 37 recovered
candidates are `PROPAGATED` by a real `main` batch**; one is `DEFERRED`.

### 3.3 The residue, ranked — and the smallest candidate set that lands it

Five items, in descending order of what landing them would change.

| # | Item | What is at issue | Blind locator audit? | MINOR / MAJOR by §7 rules |
|---:|---|---|---|---|
| **1** | `CC-20260826-SEIZURE-RECONCILIATION-01` (426 lines, open, no disposition) | Its own declaration: *"a `DATO` claim's headline is false, and a canonical prohibition in a `consolidated baseline` claim forbids statements that three other canonical claims already make."* Targets `CLAIM 004/005/011/015/016/037/040`, `PAPER 011`. | 🔴 **YES** — it declares MAJOR and touches consolidated-baseline claims | 🔴 **MAJOR** (baseline reversal → MAJOR `WM_v` bump) |
| **2** | `CC-20260826-PMID36828035-01` (254 lines, open, no disposition) | The **only** candidate §7 named that no `main` batch has touched. Self-declares *"MINOR (claim additions + a duplicate-record normalisation) with one MODERATE"*; targets `CLAIM 005/016/032/035`, `PAPER 006/007`. Its sibling `-02` (survival curve) was verified at source and is already in `PAPER 007`. | Probably not — claim *additions*, not a baseline narrowing; confirm against the final text | **MINOR** |
| **3** | `CC-20260922-CLAIM038-UNIT-CLASS-02` (on `origin/claude/q230p-molecular-state-systemic-yruqvc`, absent from `main` in any form) | The later revision of a candidate whose `-01` is on `main`. `CLAIM 038` unit class. | Not by §7's trigger unless it narrows a baseline claim — read the `-01`/`-02` delta first | **MINOR**, pending that delta |
| **4** | `CC-20260914-15870886-01` — the **one** deferred recovered VPS candidate | `BATCH_20260927_004` verdict: *"Confirmed deferred. §2's registry fields declare a reading that no receipt in the ledger backs, and this batch cannot emit that receipt because it is not the reader."* Its own header says *no claim changes, nothing reaches the working model*; it is adjacent to `CLAIM 018` (`c.517-2A>G` exon-6 skipping, `consolidated baseline`) and names `CLAIM 029/032/033`. | **No — and no batch can clear it.** It needs a *reading*, not a batch: a contemporaneous `complete_fulltext_read` receipt from whoever reads the paper. | **no WM bump** (its own declaration) |
| **5** | `PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION` and `PROPOSAL-20260810-EVIDENCE-PAIR-RATCHET` (open, no disposition) | Proposals, not candidates. The first names 13 claims and 8 papers and says *"proposal only. No gate is implemented here."* | n/a | **not a batch item** — harness proposals; §21e T0 territory for `plan` |

Also still queued and not to be mistaken for done: **`CC-20260909-25331887-01`**, whose
disposition block is a 🔴 **DEFERRED** verdict. Per the operator's standing note, a `DEFERRED`
candidate stays queued; it is not residue *of the VPS recovery* (it predates it) but it will be
counted twice by anyone who treats "has a disposition block" as "consumed".

**The smallest set of commit candidates that would land the live scientific residue: three.**

```
CC-20260826-SEIZURE-RECONCILIATION-01          MAJOR · blind locator audit REQUIRED
CC-20260826-PMID36828035-01                    MINOR · audit unlikely, confirm at final text
CC-20260922-CLAIM038-UNIT-CLASS-02             MINOR · read the -01/-02 delta first
                                               (must first be brought off
                                               origin/claude/q230p-molecular-state-systemic-yruqvc)
```

Item 4 is **not** in that set on purpose: no `BATCH_COMMIT` can discharge it. It is a reading
task. Items 5 are harness proposals, not batch candidates.

Because item 1 declares MAJOR and touches consolidated-baseline claims, the batch that carries
it is a **MAJOR** working-model bump and owes a blind locator audit before it touches canon. If
the Orchestrator wants a MINOR-only batch, items 2 and 3 compose one on their own.

---

## 4 · What is safe to retire — the eight worktrees

Measured per worktree: HEAD, distance from `main`, ancestry in the backup, unique patches
against the backup, working-tree cleanliness.

| Worktree (`.claude/worktrees/…`) | HEAD | Ahead of `main` | Ancestor of backup? | Unique patches vs backup | Dirty files | Removing it loses |
|---|---|---:|---|---:|---:|---|
| `batch-20260913-001` | `3326202f` | 31 | ✅ yes | **0** | 0 | **nothing** |
| `d8-dismech-20260913` | `b266dcd7` | 38 | ✅ yes | **0** | 0 | **nothing** |
| `growth-anchors-cc-20260913` | `27a886a6` | 42 | ✅ yes | **0** | 0 | **nothing** |
| `orch-batch-prep-20260913` | `397c7d3d` | 28 | ✅ yes | **0** | 0 | **nothing** |
| `orch-consolidation-20260913` | `0b037dd6` | 18 | ✅ yes | **0** | 0 | **nothing** |
| `orch-m4b-cost-20260912b` | `6f9c98f9` | 14 | ✅ yes | **0** | 0 | **nothing** |
| `orch-m4b-v3-20260913` | `feb55a3d` | 26 | ✅ yes | **0** | 0 | **nothing** |
| `orch-s2-close-20260913` | `cc2c4cd6` | 21 | ✅ yes | **0** | 0 | **nothing** |

**Verdict: all eight are safe to retire.** Every HEAD is an ancestor of
`backup/vps-main-2026-09-25`, so every commit each one holds is reachable from the backup ref
**and** from the verified bundle. `git cherry backup <head>` returns zero unique patches for all
eight. All eight working trees are clean, so `git worktree remove` will not refuse and no
uncommitted work is at risk. Removing a worktree removes a *checkout directory and its
administrative entry*; it removes no object, because the objects are held by the backup ref —
which is why this is not the reserved act of deleting unique material. **This census removed
none of them.**

One command, for the Orchestrator:

```bash
for w in batch-20260913-001 d8-dismech-20260913 growth-anchors-cc-20260913 \
         orch-batch-prep-20260913 orch-consolidation-20260913 orch-m4b-cost-20260912b \
         orch-m4b-v3-20260913 orch-s2-close-20260913; do
  git worktree remove ".claude/worktrees/$w"
done
```

🔴 **Precondition, and it is the whole safety argument:** `backup/vps-main-2026-09-25` must
still exist when this runs. Delete the branch first and these eight detached HEADs become the
only references keeping 325 commits reachable — at which point removing the worktrees *is* the
reserved act. **Branch first, worktrees never.**

**The other worktrees, checked because population counts decay (§21c SAFE_DEFAULTS).** Eleven
further worktrees exist (`agent-a1a227e5abdea6021`, `agent-a3737b95d8a4f34df`,
`agent-a69028edcb8dbcc33`, `agent-a74b22baca015607b`, `agent-a84cc1d77251535c4`,
`agent-a88845e6eddd2aa79`, `b8`, `b12`, `mallaret`, `pathway-legend`, plus four under `/tmp/`).
**Every one of their HEADs is an ancestor of `main` with 0 unique patches** — `cf40b73`,
`6ab877f`, `bc7346a`, `75973c4`, `747702d`, `b9faa7f`, `875d484`, `752ae4a`, `09f2243`,
`5e5f160`, `7c6b7b6`, `e30b8ec`, `87fe753`, `59f7af3`. They hold nothing. Five branch names are
still checked out in them (`task/b12-registry-completion`, `task/harness-manifest-receipt`,
`task/orch-b12-repair`, `task/orch-b3-discovery`, `task/orch-r4-r6-replay`,
`task/scientist-r7`), all landed — §21e item 4 ("rest state — nothing unmerged") says those are
landed branches due for deletion, and that is Harness Engineering's weekly sweep, not this
census's act.

---

## 5 · The honest limits

What I could **not** measure, and why — stated so no figure here is read as stronger than it is.

1. **Whether the 133 "decision A1" historical records hold science not recorded elsewhere.** I
   measured that they are files the operator decided to keep in the backup, and that their paths
   are absent from `main`. I did **not** read them. A file being dispositioned is not evidence
   that its content is redundant. Measuring that means reading 133 records (22 verifications, 9
   mirror consultations, 15 session evaluations, 24 comparison notes, 8 phase packets, 7 S2
   second-reading files, 4 consolidation verifications, 44 other disease-model files) against
   `main`'s current canon. That is a reading task with a budget, and it is the single largest
   unmeasured quantity in this census.
2. **Whether `main`'s version is *better* than the backup's on the 75 differing RECOVERED rows
   and the 13 differing remote-branch files.** I measured line containment (median 1.6 % of the
   backup's substantive lines absent on `main`). A 1.6 % difference could be a renumbering or a
   dropped caveat, and the arithmetic cannot tell them apart. Per the operator's standing note,
   a distortion built from two carried sentences is invisible to a presence check. Sampling
   confirmed the pattern is the documented FT/PAPER renumbering; it is a pattern, not a proof.
3. **Whether `CC-20260922-CLAIM038-UNIT-CLASS-02` adds anything over the `-01` on `main`.** I
   established only that `-02` exists on the branch and nowhere on `main`. The `-01`/`-02` delta
   is unread — that is why item 3 in §3.3 carries "read the delta first" rather than a class.
4. **Whether `LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md` is superseded by the shipped
   `legend-discovery-method` skill.** Plausible from the names and the fact that the PROPOSAL
   beside it is on `main`. Not measured: it needs a reader comparing the shadow-mode file to the
   skill. Recorded as "probably superseded", never as superseded.
5. **The release gate's PASS on the backup tree is an instrument result, not a proof of
   absence.** It found 0 blocks in every class and 13 review lines of the same kind `main`
   carries. A gate that passes has not proven there is nothing to find; it has proven its own
   rules found nothing. I did not run the release-regression battery against the backup tree
   (`run_release_regressions.py` on a 2026-09-11-era tree would report reds attributable to the
   epoch, not to the content — an uninterpretable figure, so it was not derived).
6. **Three §7 quantities I could not re-derive independently.** §7's record-level three-way
   comparison ("claim registry 11, paper registry 21, literature log 48, working model 4,
   discovery ledger 14 …") is a divergence-point/VPS/`main` comparison at the 2026-09-25 state.
   `main` has since moved through eleven batches; re-deriving those twelve numbers against
   today's registries would require the same three-way tooling and would not be checkable
   against the original. I tested §7's *conclusions* against the current registries instead —
   which is the question the mandate asked — and left its table where it is, as a dated
   snapshot.
7. **The 75 withdrawn VPS task records are obsolete *by construction*, which is a statement
   about `test_task_record_commit_hashes`, not about their content.** They cite commits that
   exist only in the backup, so `main` cannot hold them without failing that test. Whether any
   of the 75 records a *decision* that ought to be re-recorded on `main` in a form that does not
   cite a backup-only SHA is unmeasured, and would need the same reading budget as limit 1.

---

## DEFAULTS_TAKEN

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| The mandate says the eight worktrees are "14–42 commits ahead"; it did not say whether other worktrees exist | Re-derived the whole worktree population (`git worktree list`, 19 entries + 4 under `/tmp/`) rather than trusting the count of eight | §21c SAFE_DEFAULTS: "population counts that decay (refs, worktrees) → re-derive at start, never wait". The eight were confirmed exactly as stated; eleven more were found and measured | Nothing in the eight-worktree verdict. Had I not swept, §4's finding that eleven further worktrees hold nothing either would be missing |
| `inventory.tsv`'s claim had to be tested, but the inventory was written against an *older* `main` | Tested coverage at the inventory's **own epoch** (`e1173ca`, the commit that last wrote it) as well as today | Testing a 2026-09-26 census against a 2026-09-28 `main` would manufacture ~60 false "omissions" out of `main`'s own progress. The epoch test is the only one that can distinguish an omission from drift | Without it I would have reported 60 or 89 inventory omissions. The true count is **0** |
| The mandate asked to classify 311 patches; several are merges or touch only files `main` later moved | Classified at **file level** (488 paths, the authoritative table) and rolled up to commits by **worst-case** path | A commit-level-only answer hides that most patches mix landed and non-landed paths. Worst-case rollup answers the operational question — "would replaying this patch add anything?" — without overstating | A subject-only grouping would have shown "263 patches not on main", which is true of byte-equality and false of content |
| No instrument was named for class (e), private/unpublishable material | Extracted the backup tip with `git archive` into the scratchpad and ran `scripts/public_release_gate.py --mode staging --skip-clean-clone` against it | It is the repository's own privacy instrument, it is read-only, and it does not touch the checkout. `git archive` writes nothing into the repository | Hand-grepping for identifier shapes would have produced an unverifiable guess where an instrument exists |
| `~/legend-vps-backup-2026-09-25.bundle` is outside the repository and the mandate did not ask for it | Ran `git bundle verify` on it | Read-only, and it is the fact the whole worktree-retirement argument rests on: two independent copies, both intact, both carrying exactly `06ee25a` with complete history | The retirement verdict in §4 would have rested on one copy instead of two |
| §7's twelve record-level counts could not be re-derived checkably | Did not derive them; tested §7's **conclusions** against the current registries instead, and said so in §5 limit 6 | §21c: "prior-report figures not re-derivable in minutes → treat as hypothesis, proceed". Deriving an uncheckable number would have been worse than naming the gap | A table of twelve numbers nobody could verify |
| The recovered-candidate count read 36 by one glob and 37 by the README | Re-derived it from `inventory.tsv`'s own rows and located the 37th (`CC-20260912-29724996-02.md`, outside the `CC-2026091[345]-*` prefix) | The README's count is correct; the glob was wrong. Recorded as a census trap in §1.4 so the next reader does not repeat it | I would have reported a one-candidate discrepancy against the README that does not exist |

## STOP_LOG

No stop. No class-1 (reserved) act was required: the census is read-only throughout, and every
act reserved under §21d — pushing, deleting the backup branch, removing a worktree, publishing —
was measured and **not performed**. No class-2 condition arose: every missing figure either had
a safe default (above) or is named as an honest limit (§5).

## DECISIONS_TAKEN

| What | Alternatives rejected | Consulted | Reversibility |
|---|---|---|---|
| Classify "consumed" by a candidate's **last** `BATCH DISPOSITION` block and the actor/batch it names, not by the presence of the heading | Presence-of-heading (would have counted 13 VPS-batch dispositions as done on the strength of batches that never existed on `main`) | none — measurement, recorded in §3.2 | fully; the measurement is re-runnable |
| Report the mandate-continuity package as its own class **R (reserved)** rather than folding it into class (e) | Folding it into (e) private/unpublishable | none | fully; the 20 paths are listed by their inventory group |
| Treat `AUTONOMOUS_SESSION_STATE.md` and `state_manifest_current.md` differences as scratch/state-control rather than content residue | Counting them as live residue (they show 60 % and 45 % line divergence, the two largest on either remote branch) | none — both are declared non-content surfaces (§ the manifest is the state-control carve-out) | fully; both are named explicitly in §2.1 |
