# OVERNIGHT CHECKPOINT — 2026-09-22 autonomous run

> 🔴 **Non-canonical operational checkpoint.** READ-ONLY toward the four scientific current files,
> every registry, every ledger, the receipt chain and the state manifest. Nothing here is promoted.
> 🔴 **Nothing here is medical advice.** 🔵 **Public edition** — genotype-class level only.

> ⚠️ **STANDING INSTRUCTION, WRITTEN BECAUSE THIS FILE'S PREDECESSOR FAILED EXACTLY HERE.**
> **Do not trust any "unread" marking in this file, or in any other prose file, as state.**
> An *"X is unread"* assertion is the append-only negative that
> [`scripts/test_no_closed_world_assertions_on_live_state.py`](../../../scripts/test_no_closed_world_assertions_on_live_state.py)
> forbids in test code — *"becomes false the moment X is read. Never safe to pin."* Derive read
> state instead, every time, with **`python3 framework/scripts/reading_state.py --out <path>`**,
> which reads every receipt in the checkout. On 2026-09-22 this session spent acquisition acts on
> two papers `AUTONOMOUS_SESSION_STATE.md` called unread and the ledger called read. The ledger
> was right.

---

## 1 · STATE AT SESSION START, MEASURED NOT ASSUMED

| Axis | Measured |
|---|---|
| HEAD at start | `5829670`, working tree clean |
| Branch | `claude/overnight-autonomous-queue-w09aop`, **identical to `origin/main`** (0 ahead / 0 behind) |
| `current_state` | `READY` |
| Receipt chain | 🟢 **201 chained receipts, tail-anchored** in the state manifest |
| LINT | 🟢 `PASS` (one INFO: `CLAIM 010` background-only, wikilink not required) |
| Growth anchors | 🟢 `PASS` — claims **40** · papers **87** · corpus **361** · literature **398** · registry_only **13** · **`unread_premises = 0`** |
| Public release gate | 🟢 `PASS`, **`BLOCKS: 0`** — REVIEW rows only, unchanged in number and kind from session start |
| Q230P | `ENVIRONMENT-SATURATED / REVIVAL-READY` — **no revival trigger fired** |
| Discovery Method V0 | stable · **`V0 CHANGE = NONE`** · no modification warranted or made |

## 2 · HARNESS §19/§20 — ALREADY LANDED BEFORE THIS SESSION, VERIFIED GREEN

🟢 **No work was needed and none was invented.** The broad-staging guard the brief asked for exists:
`scripts/legend_commit.sh` stages **explicit file paths only**, and **refuses a directory pathspec
outright** (exit 4) because `git add -- <dir>` is directory-scoped and swept a peer's in-flight file
once already (Mirror `REV-EXPOST-20260911-001` F3).

The §20 regression test is present with **the exact failure pattern the brief specifies** —
completed file A, unrelated in-progress file C, land A, C stays unstaged:
`test_commit_is_scoped_and_leaves_a_peers_file_untouched`, which deliberately makes C a **tracked**
file, on the stated argument that an untracked peer file *"would be safe under almost any
implementation … so testing only that would be the adjacent property again."*

**`python3 scripts/test_legend_commit.py` → 6 tests, OK.** Every landing this session used the
wrapper with explicit paths. **No `git add -A` was run at any point.** ⇒ Per §20, **stopped here.**

## 3 · PRIORITIES CLOSED AT START, WITH THE REASON — NOT SKIPPED

Checked against the repository before assigning any Scientist. The brief's queue assumed a frontier
the repository had already moved past; re-running it would have manufactured rediscovery.

| Brief priority | Repository state | Action |
|---|---|---|
| **P1** OXPHOS / metabolic | `DISCOVERY_TRACE_metabolic_gating_20260922.md` already run, **self-graded `REDISCOVERY`** | **Re-posed, not re-run** — see §4, the expression-level rival is tested first |
| **P2** Purkinje / therapeutic dose | Blocked on **`A-f4`** — tissue retention, *"`HUMAN_REQUIRED` and unknowable from a repository"* (`tx007_purkinje_frontier_20260922.md:146`) | 🔴 **PARKED at start**, per brief §4 |
| **P3** Aqeilan peripheral vDNA qPCR | Packet mature; **same `A-f4` gate**; all of B1/B2/C1 conditional on it | 🔴 **FROZEN at start**, per brief §5 |
| **P5** modifier / resilience | `resilience_and_modifier_census_20260921.md` — came back **negative**; `superior_node_search` records *"not re-run"* | Not re-run |
| **P6** developmental timing | Four files incl. `CC-20260922-POSTDIAGNOSIS-WINDOW-01` | Not re-run |
| Seven Operator-gated candidates | `OPERATOR_DECISION_PACKET_6_20260922.md` | **Untouched, not propagated, not reconstructed** (brief §32) |

🔴 **No external action of any kind was taken.** No lab contacted, no material requested, no funding
committed, no Foundation representation. Every contact remains `HUMAN_REQUIRED` (brief §33).

## 4 · SCIENTISTS DISPATCHED — three slots, all on open ground

| # | Node | Why it is open |
|---|---|---|
| **S1** | **Score `P7`, run `E5`** — subfield- and cell-type-resolved wild-type `Wwox` expression | `new_discovery_node_20260922.md` preregistered P1–P7, scored six, left **`P7` ⚪ UNTESTED**, and `E5` is its **only free, zero-animal, executable-now** component. Adjudicates `H3`. Doubles as the **expression-level rival** that any metabolic explanation of differential vulnerability must beat first |
| **S2** | **Ataxia without cerebellar lesion** — 95% ataxic gait, authors state *"we did not detect any marked pathologic changes in the cerebella"* (`CLAIM 039`, `lde/lde` rat) | An orphan observation the prior node **flagged and deliberately did not pursue**. Never diverged over |
| **S3** | **Public-deposit reanalysis census** | The one continuation class **immune to the `A-f4` freezer gate** that blocks P2 and P3. Reanalysis is rank 1 in the repository's own preference order and has never been systematically censused |

## 5 · ORCHESTRATOR LANE — landed this session

**Commit `a9e1d63`** — one file, path-scoped. See its message for the full argument.

- **Two stale "unread" markings corrected** in `AUTONOMOUS_SESSION_STATE.md`. Both papers were read
  **2026-09-21**; the checkpoint was never updated when the receipts were appended.
- 🟢 **`PMID 35573960` re-fetched in full (~16 k chars) and graded `A — REDISCOVERY`.** Its two most
  promising-looking findings on a fresh read — the **age-dependent MR-spectroscopy lactate** (present
  at 4 months, **absent** at 2 y 4 m) and the authors' **own open question** about the late
  periventricular-leukomalacia-like pattern — were **already held**, at
  `woree_phenotypic_approach_audit_20260921.md:298` and `:247`. The repository was right.
- **Three "untested rather than blocked" rows resolved**, using `convert_article_ids`, the authority
  the repository itself names: `33300063`, `30094525`, `11719429` return **no PMCID at all**. The PMC
  route is **closed** for all three; only publisher/ILL remains ⇒ `HUMAN_REQUIRED`.
- ⚠️ **A prose-surface guard was prototyped and DELIBERATELY NOT SHIPPED** — measured at **12
  candidates, ~4 true** across the tree. Recorded as a measured negative, not a TODO. See §6.

## 6 · 🔴 OPEN DEFECT FOR THE OPERATOR — stale "unread" markings inside append-only files

Adjudicated with `framework/scripts/reading_state.py` (the routed tool), **not** with grep:

| PMID | The prose says | `reading_state.py` says | Verdict |
|---|---|---|---|
| `21212533` | *"non letta"* — `discovery_ledger_current.md:1652` | **`complete_fulltext_read`** — every section read, **including figures, tables and supplementary** | 🔴 **STALE** |
| `19484134` | *"mai letto"* in the **`FT-108` heading** — `full_text_queue_current.md:4910` | **`partial_fulltext_read`** — abstract, introduction, methods, results, discussion all **read** | 🔴 **STALE** |
| `24369382` | *"body … is unread, licence-blocked"* | `partial_fulltext_read`, but **every coverage field is `unknown_legacy`** (a legacy reconstruction) | 🟢 **THE PROSE IS CORRECT** |

🔴 **I did not hand-edit either file.** `discovery_ledger_current.md` and `full_text_queue_current.md`
are **append-only ledgers that append through their validated writers**; hand-editing them is exactly
the class of act the receipt chain exists to prevent. **Operator decision required** on whether these
two markings are corrected through their writers.

🎯 **Why the `24369382` row is the most useful one here.** It is a case where the prose was **right**
and a naive scanner would have called it an offence. That is not a hypothetical false positive — it
is a measured one, and it is the reason the guard in §5 was not shipped.

## 7 · QUEUE — ranked, refilled as slots free

1. 🔵 **RUNNING** — S1 `P7`/`E5`, expression atlas
2. 🔵 **RUNNING** — S2 ataxia without cerebellar lesion
3. 🔵 **RUNNING** — S3 public-deposit reanalysis census
4. ⚪ Verify each hand-back's load-bearing claim, then land path-scoped
5. ⚪ Recursive reread, **only if** an S1/S2/S3 result genuinely changes the question asked of an
   already-read paper — not manufactured for the metric
6. ⚪ Reassess the metabolic node **only if** S1 kills the expression-level rival; if expression
   explains the vulnerability pattern, the metabolic hypothesis is redundant and closes

## 8 · REVIVAL TRIGGERS ON EVERYTHING PARKED TONIGHT

| Parked | Reopens when |
|---|---|
| **P2 Purkinje** · **P3 peripheral qPCR** | 🎯 **`A-f4` answered** — a human confirms whether 2021/2026 tissue, FFPE blocks or extracted DNA survive. **One answer unblocks both.** |
| **P1 metabolic** | S1 shows vulnerability does **not** track baseline `Wwox` expression, leaving a gap the metabolic state could fill |
| **Q230P** | Unchanged — `ENVIRONMENT-SATURATED / REVIVAL-READY`, **no trigger fired**; MD (GROMACS) WT vs Q230P on SASA/RMSF of residues 187–191 remains the named discriminator |
| **Prose-guard** | A higher-precision signal than same-line prose exists — do **not** re-prototype the scanner without one |
| `33300063` · `30094525` · `11719429` | A publisher or ILL route is opened by a human |

---

# WAVE 1 — COMPLETE. Three Scientists landed, three claims verified, one refuted.

**HEAD after wave 1:** `8c2bfbb`. Commits `f2b6c38` (S2) · `3aca32d` (S3) · `8c2bfbb` (S1).
Every landing was **path-scoped through `scripts/legend_commit.sh`** naming one file.

## Verification of each hand-back's load-bearing claim — the step that earned its keep

Each Scientist nominated the single claim most damaging if wrong. **One of the three broke.**

| Scientist | Nominated claim | Verdict |
|---|---|---|
| **S2** | The Tochigi 2019 attribution sentence exists, and is absent from this repository | 🟢 **CONFIRMED, both halves** |
| **S3** | The accession-deletion is a property of the extraction surface, not evidence of no deposit | 🟢 **CONFIRMED verbatim** |
| **S1** | `PMID 33914858` has never been successfully read by this repository | 🔴 **PARTIALLY REFUTED — sent back and corrected** |

### 🔴 The one that broke, and what it cost to catch
S1 asserted `PMID 33914858` was never read. Verified: **no receipt has it as `study_id.pmid`** (all 5 matching ledger lines are *other* papers' receipts citing it), no dossier, retrieval `FAILED_HTTP_403_CLOUDFLARE`. **But it was read in full** — `learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md`, 810 lines, **30 verbatim locators**, actor `lettore-c` — and is un-receipted by **principled abstention**, its § 15 stating that issuing one *"would decide that question by doing it."*

🎯 **The corrected claim is stronger than the original.** The defect is **reachability, not absence**: the pilot's own § 1 records that *"every text surface for this paper is gitignored and local to one machine. CI sees none of them. **A reader on a fresh clone has nothing.**"*

**S1 then found a second error of its own that this Orchestrator had missed**, and withdrew it: it had written that the `non-cell-autonomous` arrow *"loses its warrant."* It does not. `L02`/`L18` test **necessity**, `L16` tests **sufficiency**. Revised to **trigger `DATO`, route `IPOTESI`, negative arm conditional** — which matches the pilot's own typing of `P3` as `INDIRECT_UNKNOWN_INTERMEDIATES` (*"no mediator identified"*) and `P8` as a negative with *"Supp. Fig. 8 unseen; Cre validation unseen"*. Correcting it made S1's Part B refutation **stronger**, moving the OPC→oligodendrocyte row from supporting the rival to confounded, 4 of 7 → **3 of 7**.

## What wave 1 actually established

1. 🎯 **Differential vulnerability does NOT track baseline `Wwox` expression.** Refuted on a *measurement*: the highest-expressing isocortical cell type is normal in number, thickness and lamination while the oligodendrocyte lineage fails. `P7` **SUPPORTED** on its qualitative half; **no numeric subfield value exists** anywhere and the file leads with that.
2. `H3` **splits** rather than dying — fails on CA1, **survives on the amygdala** (Allen ISH names `BLAa`/`BLAp` among only two top regions, and the amygdala vacuolates). **Neither half had been noticed.**
3. 🔴 **`CLAIM 039`'s "the ataxia has no structural explanation" is incomplete as a statement about the literature.** The source paper's authors attribute it to hypomyelination **one sentence after** a sentence the repository did quote and used only as a timing landmark. Verified: the attribution appears in **zero** repository files.
4. 🔴 **`NOT_SECTIONED` has been read as `NORMAL`.** No `lde/lde` study has sectioned cerebellum, brainstem, cord, nerve or muscle — while the same paper's western blot puts `Wwox` protein in all of them.
5. **The reanalysis continuation class is nearly empty**, and the arrival/expression/function question has **no** reanalysis route — both gene-therapy papers deposited nothing. `A-f4` is promoted from *a* blocker to *the only* route for that question class.
6. 🎯 **A cerebellar RNA-seq in a named WWOX allele appears to exist and to have gone unreported** (`PMID 36828035` Methods §4.14 collects it, Results §2.8 reports forebrain only). **Frozen, `HUMAN_REQUIRED`, deliberately not ranked.**

## 🔴 CONSEQUENCE THE OPERATOR MUST SEE — `BATCH_COMMIT` is blocked

`unread_premises: 5/0` ⇒ LINT `BLOCK_BATCH_COMMIT`. **The publication gate is unaffected — `PASS`, `BLOCKS: 0`.** The five:

`PMID 18676360` · `19918364` · `41776383` (S2) · `36247526` (S1) · `40235507` (S3)

🔴 **The citations were NOT deleted to clear the gate.** The signal is **true** — tonight's reasoning does lean on five papers nobody opened — and suppressing it would be gaming the gate the repository built to catch exactly this. The correct fix is to open them, and Scientist 5 is doing so. What cannot be read becomes a queue entry, which is an operator act.

## WAVE 2 — dispatched, running

| # | Node | Why |
|---|---|---|
| **S4** | **Cerebellar measurement census** — was the cerebellum ever *collected*, *sectioned*, *assayed*, *reported*? | 🎯 **Three Scientists converged on this gap from three unrelated directions** and none could see it alone. If the cerebellum was never sampled, `A-f4` custody is the **second** problem, not the first |
| **S5** | **Acquisition wave** — the five unread premises, `PMID 18676360` first | An `lde/lde` primary from the founding laboratory in **zero** repository files. Instructed to establish read-state **before** fetching, because that trap already cost this session one act |
| **S6** | **Metabolic node, re-posed** | Reopened **only** because S1 killed the expression rival. Bounded by `L02`/`L18`: glial deletion does nothing, so **no metabolic story may locate the lesion in glial metabolism**. Explicitly licensed to **close the node** |

## Queue behind wave 2
1. ⚪ **The surviving amygdala half of `H3`** — the one place expression and lesion coincide; unworked
2. ⚪ Land and verify wave 2; resolve `unread_premises` where papers prove readable
3. ⚪ Recursive reread — **one genuine instance already occurred** (S2 re-asked an already-quoted paper a new question and found the dropped attribution); do not manufacture a second
