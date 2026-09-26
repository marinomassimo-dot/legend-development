# STATE MANIFEST — LEGEND (public disease-level fixture)

> **Foundational file.** Active state of the LEGEND system.
> This is the only **state-control** file updatable outside a `BATCH_COMMIT`.
> Designated non-canonical append-only ledgers are explicit carve-outs: they may append
> through their validated writers, but never replace the four scientific current files.
> Every operational event (ingest, lint, commit candidate, batch commit, branch) must update it.
> History is cold: past batch scopes, a lifted gate's narrative, superseded notes and dated
> harness notes live in [`state_history.md`](state_history.md) — read on demand, never at
> startup, and never a source of a current value.
>
> **Public edition note.** This is a **disease-level fixture**, not the operational state of any private working instance. It carries no patient record and no session-specific operational history. It exists so the framework is internally coherent and (eventually) LINT-passable at the disease-model level. Values are illustrative placeholders for the public WWOX disease model.

---

## 0. PURPOSE

Track, unambiguously and readably:

- active framework version
- active disease-model (working-model) version
- state of each `*_current.md` file
- last completed `BATCH_COMMIT`
- last `LINT` run
- current operational state of the system
- where the history of all of the above lives

Without an up-to-date manifest → system in `UNKNOWN` state → `BLOCK_SYSTEM`.

---

## 1. SYSTEM VERSION

```yaml
framework_version: v3.3.1
framework_file: framework/instruction/LEGEND_CORE.md
manifest_schema_version: 1.0
edition: public
```

---

## 2. DISEASE-MODEL (WORKING-MODEL) VERSION

```yaml
working_model_version: WM_v5.0
working_model_file: disease-models/wwox/registries/working_model_current.md
narrative_view: disease-models/wwox/disease_model.md
notes: "Canonical disease-level working model derived from public literature; disease_model.md is its narrative reader-facing view. The private individual-level record is not part of this edition."
```

**Rule:** every `BATCH_COMMIT` that modifies the disease model **must** bump `working_model_version` (format `WM_vMAJOR.MINOR`).

- MINOR bump: claim addition/modification, block update without reversals
- MAJOR bump: reversal of a baseline claim, block redefinition, authorized urgent commit

Commit candidates must declare their intended `target_wm_version`.

---

## 3. CURRENT FILES STATE

### 3.1 Disease-model canonical files

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/registries/working_model_current.md` | present | **canonical** disease-level working model — claim mirror, changelog, decision blocks |
| `disease-models/wwox/disease_model.md` | present | narrative reader-facing view of the same model |
| `disease-models/wwox/registries/claim_registry_current.md` | present | canonical claims (public literature) |
| `disease-models/wwox/registries/paper_registry_current.md` | present | integrated / baseline-linked papers |
| `disease-models/wwox/registries/literature_tracking_log_current.md` | present | lifecycle state of every paper in the pipeline |

### 3.2 Meta-analyses

| File | Status |
|------|--------|
| `disease-models/wwox/meta/meta_index_current.md` | present |
| `disease-models/wwox/meta/meta_network_myelin_glia_current.md` | present |
| `disease-models/wwox/meta/meta_metabolism_current.md` | present |
| `disease-models/wwox/meta/meta_prenatal_structure_current.md` | present |
| `disease-models/wwox/meta/meta_human_spectrum_current.md` | present |
| `disease-models/wwox/meta/meta_gaba_paradox_current.md` | present |

### 3.3 Compounding-memory files (non-canonical, append-only)

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/research/discovery_ledger_current.md` | present | cumulative discovery capital — leads toward biomarkers, molecules, repurposing |
| `disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md` | present | scored hypothesis portfolio from the co-scientist loop |
| `disease-models/wwox/research/dismissal_ledger_current.md` | present | rejections with their `REVIVAL_TRIGGER` — nothing dies in silence |
| `framework/eval/learned_gates_registry.md` | present | reusable error-prevention gates distilled from failures |
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | present | authoritative append-only full-text event ledger; hash-chained and tail-anchored (§6.1), LINT-verified; includes explicitly non-contemporaneous legacy reconstructions |

### 3.4 Operational files (private overlay — not in this repository)

| File | Status | Notes |
|------|--------|-------|
| `inbox_current.md` | not shipped | ingest quarantine |
| `session_commit_log.md` | not shipped | commit-candidate queue; the LINT checks it when present |
| `legend_activity_log.md` | not shipped | operational timeline |
| `capability_scout_log.md` | not shipped | capability-growth log |

---

## 4. LAST BATCH_COMMIT

```yaml
last_batch_commit_id: BATCH_20260926_ALDAZ_R1
last_batch_commit_date: 2026-09-26
last_batch_commit_type: REGISTRY_ONLY
```

Every batch's scope — the candidates it propagated, newest first back to `BATCH_20260810_001`,
with the keys written beside each and the notes on `BATCH_20260806_002` — is in
[`state_history.md`](state_history.md) § 4. Nothing there is a current value; the three
`last_batch_*` fields above are.

---

## 5. LAST LINT

```yaml
last_lint_type: LINT_AUTOMATIC
last_lint_id: LINT_20260909_BATCH_AQEILAN54
last_lint_date: 2026-09-09
last_lint_result: PASS
```

---

## 6. OPERATIONAL STATE

```yaml
current_state: READY
deep_dive_gate: OPEN
ingest_gate: OPEN
batch_commit_gate: OPEN
```

> 🔴 **Branch and worktree state is not declared here.** `active_parallel_branches` was removed on
> 2026-09-20: no script in the repository ever read it, and on that date it still said `none`
> while a branch had been five commits ahead of `main` for two days. A field that nothing
> consults cannot be wrong loudly — it can only be wrong quietly, which is worse than absent.
> Git is the primary source for branches and worktrees (`git branch -a`, `git worktree list`,
> `git ls-remote --heads origin`); it is always current by construction, and keeping a second
> copy in step would cost more than reading the first.

The narrative of `batch_commit_gate` closing on 2026-08-09 and reopening on 2026-08-10 by
road 3 — with the `PMID 17803050` text-surface debt that `FT-041` carries — is in
[`state_history.md`](state_history.md) § 6.

## 6.1 FULL-TEXT RECEIPT LEDGER ANCHOR

The full-text receipt ledger is append-only. A per-event hash chain makes a rewritten or
deleted historical event detectable; it cannot detect a *truncated tail*, because the
surviving prefix stays self-consistent. The anchor below closes that gap: it pins how many
events the ledger must hold and the digest of its last one. `LINT_AUTOMATIC` verifies both,
and a mismatch is `BLOCK_SYSTEM` — reading history you cannot trust is worse than none.

```yaml
fulltext_ledger_path: disease-models/wwox/registries/fulltext_read_receipts.jsonl
fulltext_ledger_events: 236
fulltext_ledger_head: 646eadee10832ff166f50c7b5d2c2629981a3e70b46c66f756c17d7f48990332
```

Maintained automatically — `fulltext_receipts.py record` re-anchors after every append.
To re-anchor by hand after an authorized repair:

```bash
python3 framework/scripts/fulltext_receipts.py anchor
python3 framework/scripts/fulltext_receipts.py verify
```

## 6.1bis SYNC EPOCH LEDGER ANCHOR

Several actors work in their own worktrees against one shared checkout. Realigning that
checkout is what turns a landed state into a **dependency** other actors must consume, so the
decision to move it — **and the decision not to move it** — is operational state. Announced in
a message it survives until the session ends; recorded in the ledger it survives the session.

The full history lives in the JSONL and is **not** duplicated in these notes. Only the anchor
is here, for the same reason as §6.1: a hash chain cannot see a truncated tail.

```yaml
sync_epoch_ledger_path: framework/state/sync_epochs.jsonl
sync_epoch_ledger_events: 1
sync_epoch_ledger_head: 1f10fc71a601d092fee56b9ced6ced72772e3c928de51e33f9463b2b18df1fdf
```

Plan is the only writer. Other actors read the ledger, measure state with allowlisted
read-only commands, supply **attributed** observations and may propose a trigger; they do not
append, re-anchor or move the shared checkout.

```bash
python3 framework/scripts/sync_epochs.py record --event event.json
python3 framework/scripts/sync_epochs.py verify
python3 framework/scripts/sync_epochs.py status
```

## 6.2 GROWTH ANCHORS

Every constant below that says *"how big the system is right now"* is written by
[`growth_anchors.py`](../scripts/growth_anchors.py) and by nothing else. **No value in this
section may be typed by hand.** The rule it enforces is stricter than "automate it": *updating
a constraint must cost at least as much as complying with it.* The recorder re-measures the
registries and refuses a declared delta that does not match them, so a number cannot be bumped
to make a suite green — the only way to move it is to have made the change you declare.

```yaml
growth_anchor_ledger: framework/state/growth_anchors.jsonl
growth_anchor_events: 29
growth_anchor_head: 4f73044a98d7b991b21574104f668032a76c9c202400d8c272ab7177c730554f
```

```bash
python3 framework/scripts/growth_anchors.py check     # live vs anchors
python3 framework/scripts/growth_anchors.py verify    # chain + tail anchor
python3 framework/scripts/growth_anchors.py record --batch <ID> --claims +4 --papers +3
python3 framework/scripts/growth_anchors.py tighten   # a ratchet fell; re-anchor it
```

The two ratchets documented below keep their own fields for backwards compatibility —
`legend_lint.py` and `session_self_eval.py` read them directly — but those fields are now
**written by `growth_anchors.py tighten`**, never by a person. The asymmetry is deliberate and
recorded here so a later reader does not mistake it for an oversight.

### Registry-declaration ratchet

Twenty registry records carry a historical `full text reviewed` declaration with no
surviving complete-coverage receipt. They are kept visible rather than deleted or
retroactively upgraded — the work happened, the evidence of *how completely* did not
survive. The baseline below is a **ratchet**: history is grandfathered by both count and
exact record identity. A count alone is insufficient because one old declaration could be
removed while a different unsupported declaration is added. Any *new* full-text declaration
must be backed by a persisted `complete_fulltext_read` receipt, or `LINT_AUTOMATIC` returns
`BLOCK_BATCH_COMMIT`.

```yaml
registry_only_fulltext_declarations_baseline: 10
registry_only_fulltext_declaration_ids: ["PAPER 012", "PAPER 014", "PAPER 016", "PAPER 028", "PAPER 043", "PAPER 044", "PAPER 045", "PAPER 046", "PAPER 049", "PAPER 050"]
```

Lowering the baseline is the intended direction of travel: back-fill a record with real
evidence, re-run `coverage_report.py`, then lower the number and remove that resolved ID
from the grandfathered list.

### Unread-premise ratchet

The incident that motivated it is in [`state_history.md`](state_history.md) § 6.2.

A separate and harsher debt, measured on 2026-07-26 by `session_self_eval.py`. The *reasoning*
layer — metas, therapeutic strategies, the analysis files — cites papers as **support for
conclusions**. The first measurement found seventeen of eighteen PMIDs with **no
complete-read receipt, no registry full-text declaration and no full-text-queue entry**. The
ratchet has since fallen as papers were read or their debt was made explicit; the current
baseline below must equal the live count, never preserve historical padding.

```yaml
unread_premise_baseline: 0
unread_premise_measured_on: 2026-09-26
```

**It is a ratchet, not a wall.** Blocking on the whole legacy backlog would only teach sessions
to route around the check; capping it makes every *new* unread premise a visible regression
(`UNREAD_PREMISE` → `BLOCK_BATCH_COMMIT`). Three things clear a citation, and only three: a
persisted `complete_fulltext_read` receipt, a registry record declaring the full text reviewed,
or an explicit `full_text_queue_current.md` entry. The third is what keeps the check honest
rather than punitive — **declared reading debt is legitimate work in progress; silence is not.**

### 6.4 — `panel_text_relation`: manifests that do not say whether anyone looked at the panel

The incidents behind the field and behind `panel_qualifies_text` are in
[`state_history.md`](state_history.md) § 6.4; the rules that bind stay here.

So each schema-v2 locator declares `panel_text_relation`: `text_only` · `panel_only` ·
`text_confirmed_by_panel` · `text_contradicted_by_panel` · `panel_qualifies_text` ·
`unknown_legacy`. The two **coupled** relations must name the locator they bear on, as
`contradicts: "entries[N]"` and `qualifies: "entries[N]"`, and that pointer is a `BLOCK` when
missing — an unpointed assertion about another locator is prose in a JSON field that no reader
can trace and no command can check.

The needle field is `qualifies_needle`, not the bare `needle` the value was first emitted
with. That is the **smaller** vocabulary, not the larger: `contradicts`/`contradicts_needle`
already fixes the grammar as `<pointer>`/`<pointer>_needle`, so a bare `needle` would be a
second naming convention living beside the first.

🔴 **And the pointer alone is not enough, because `entries[N]` is a position in an array that
can be reordered.** The three checks around it — the target exists, it is a text surface, it
is not this one — are every one of them blind to a **slip**: insert a locator above the target
and the index silently resolves to a different sentence, with all fields still well formed.
The prevention was already in the repository and had been **half-copied**: `adjudications.json`
never writes `entries[N]` alone, it writes it beside a **needle**, and `check_needles` asks two
arithmetic questions — does the needle occur exactly once, and is it a fragment of the snippet
of the locator it names. `contradicts` had taken the addressing grammar and left behind the
half that makes the address safe. So a contradiction now also carries `contradicts_needle`: a
fragment that must belong to the snippet the index resolves to and to **no other entry's**.
Address by content as well as by position — the move this repository makes everywhere else,
applied to the one place it had been left uncovered.

### 6.5 — the commit-candidate backlog: read, and not promoted

The measurements that shaped the backlog count are in
[`state_history.md`](state_history.md) § 6.5; the rules that bind stay here.

§6.3 measures what the reasoning layer leans on **without having read it**. Nothing measured
the mirror: a reading finished and never propagated. Leaning on a paper writes nothing
anywhere — and neither does stopping one step short of the registry.

The state is therefore **derived, never declared**. A `candidate_status:` field would be a
value someone must remember to flip, and flipping costs less than propagating — so on the day
the queue is inconvenient the field moves instead of the work. The signal already existed,
written for another purpose: **every `batch_*_scope` in `state_history.md` § 4 names the
candidates that batch propagated.** Consumed = named in a scope; pending = on disk and named nowhere. The only way
to lower the number is to propagate, because the scope is what records it.

**A trigger, deliberately not a ratchet.** A ratchet would make accumulating candidates an
offence, and it is not one — between batches the backlog is *supposed* to grow, because the
system reads faster than it propagates. What must not happen is that it grows silently, so
above the trigger the next `BATCH_COMMIT` either propagates or records why not. Same contract
as `SCALE_TRIGGER`: nothing is wrong, something is due.

```yaml
panel_relation_legacy_baseline: 13
panel_relation_legacy_ids: ["PMID17803050", "PMID19500159", "PMID19936220", "PMID22193544", "PMID24871327", "PMID30290271", "PMID30755385", "PMID31340538", "PMID33255508", "PMID34747138", "PMID35716775", "PMID37519886", "PMID40875931"]
```

🔴 **The eighteen are `unknown_legacy`, and the field is NOT backfilled by inference.** A
`surface: body` locator is not `text_only` by construction — it may be contradicted by a panel
nobody has opened. **The absence of a recorded contradiction is not evidence of its absence**,
so deriving the relation from the surface would manufacture eighteen manifests' worth of
reassurance out of no observation at all. `unknown_legacy` is the honest answer, and it is
paid down by re-reading, not by deducing.

**The split, and why it is a split.** `deepdive_manifest.validate` checks what one manifest can
answer about itself — that the value is in the enum, and that a contradiction names a text
locator that exists and is not itself. Whether a manifest is *allowed* to omit the field is a
fact about the corpus, not about the file, so it lives here: a manifest already in
`panel_relation_legacy_ids` is grandfathered, and one that is **not** appears as a new member
of a ratchet that may only fall (`RATCHET_VIOLATION` → `BLOCK`). That is "the validator refuses
new work without it", enforced where the information actually is.

**Why the ID list and not just the count.** Same reason as §6.3: a number is something a hand
can edit to make a suite green, and this repository has watched that happen, diligent comment
and all. The list is a claim the tool re-derives — lowering the baseline means naming which
manifest left the set, and `growth_anchors.py evaluate` goes and looks. Both fields are written
only by `growth_anchors.py record` / `tighten`; neither is typed by a human.

Membership is per manifest and one bare locator is enough. A reading that classified nineteen
locators and left one unclassified **has an unclassified locator** — the way out of the set is
to finish, not to average.

---

## 7. NOTES

Dated operational notes are in [`state_history.md`](state_history.md) § 7; a new one is
appended there, not here.

This fixture is intentionally free of any individual patient's operational history. The public edition separates three layers: the generic `framework/`, the disease-level `disease-models/wwox/`, and a private N-of-1 overlay that is **not** part of this repository.
