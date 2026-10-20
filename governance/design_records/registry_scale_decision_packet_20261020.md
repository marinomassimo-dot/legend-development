# Registry scale — decision packet for the operator (N9, 2026-10-20)

> **Non-normative design record.** Written by Harness Engineering (`plan`) for task
> `PLAN-HARNESS-FROM-METABOLIC-BATCH-20261020`, need N9. **The decision is the operator's.**
> Nothing in this packet changes a registry, a current file or a tool. Every figure below was
> measured on 2026-10-20 at commit `b2b98e36` of the task branch (registries identical to
> `main` `a2559a30`), and each names its command.

## 1 · The question

Mirror review A7 (`research/mirror_review_BATCH_20261019_006_and_harness.md`) accepted the second
deferral of the paper-registry sharding decision on one condition: *"A third renewal should be
refused until the operator has decided on sharding."* The current acknowledgement
(`growth_anchors.jsonl`, `scale_ack.papers = 1,539,001` bytes, `BATCH_20261019_006`) expires at
1,923,751 bytes. Batch report 007 and the Orchestrator's self-evaluation disagree on whether the
registry is already past the re-raise point; the measurement settles it: **it is not** (1,541,499
bytes, 0.2 % above the acknowledgement), but at the measured growth rate it will be within days.

## 2 · Measurements

| Surface | Bytes 2026-09-20 | Bytes 2026-10-20 | Records | Bytes/record | Scale anchor |
|---|---:|---:|---:|---:|---|
| `paper_registry_current.md` | 439,067 | 1,541,499 | 815 | ≈ 1,890 | trigger 1 MiB, acknowledged at 1,539,001, expires 1,923,751 |
| `literature_tracking_log_current.md` | 492,206 | 964,192 | 704 | ≈ 1,370 | trigger 1 MiB, **not yet crossed** (about 84 KB away) |
| `discovery_ledger_current.md` | 590,071 | 810,852 | 286 | — | **none**: not in `growth_anchors.REGISTRIES`; 470,808 bytes of it are one `## Change-log` block |

Sizes: `git cat-file -s <rev>:<path>` at the last commit of each date; records:
`registry_records.py index`. The paper registry grew 3.5× in a month (≈ 1.1 MB/month); the
metabolic batch alone added 4,231 lines in seven commits (`git log --numstat --since=2026-10-19`).

**What the size costs today, measured:**

| Cost axis | Measurement | Scales with size? |
|---|---|---|
| Session context | 0 bytes preloaded at any profile below FULL; `registry_records.py get --pmid <a well-linked PMID> --hops 1` returns whole records in **0.83 s** | latency only, linear |
| LINT | `legend_lint.py .` **7.85 s** over everything | linear |
| A record-scoped edit | `record_scoped_edit.py replace` dry run on `PAPER 005` **0.17 s** | linear, negligible |
| Depth/locator screens | `locator_count_crosscheck.py --depth` **0.62 s** over 434 depth lines | linear, negligible |
| Code coupled to the path | 20 tools + 26 tests name `paper_registry_current`; 11 + 11 the literature log; 6 + 9 the discovery ledger (`git grep -l`) | fixed cost of any split |
| Prose coupled to the path | 372 / 163 / 215 Markdown files link the three (record wikilinks into the registry among them) | fixed cost of any split, and the large one |
| Parallel conflicts | every new record is appended at the end of one file, so two branches that add records always conflict there — **independent of size** | no |
| Agent `Read` of the whole file | not possible in one call above a few hundred KB — and never needed: the routing table forbids it | already past |

**What the measurements say.** No cost measured in the batch is attributable to the file's size.
Context cost was removed by record-level access (2026-09-11) and stays at zero; tool latencies are
sub-second to seconds and linear. The one structural pain — append conflicts between parallel
branches — does not depend on size and is not cured by sharding by record range (all new records
land in the last shard). The real cost of any split is fixed and paid once: ≈ 20 tools, ≈ 26 tests
and ≈ 370 linking documents.

## 3 · Options

| | Option | Context | Tools | Batch ops | Reversibility | Cost |
|---|---|---|---|---|---|---|
| **A** | **Status quo, trigger re-founded on cost.** Keep one file per registry. Replace the byte trigger (a size nobody can relate to a harm) with the costs above, measured by `growth_anchors.py`: re-raise when `get --hops 1` exceeds 2 s or LINT exceeds 30 s. Add the literature log's and the discovery ledger's sizes to the same probe so all three are watched. | none | one function in `growth_anchors.py` | none | full (one revert) | ≈ 2 h |
| **B** | **Shard by record range** (`paper_registry/PAPER_0001-0500.md`, …) behind one resolver in `registry_records.py`. | none | ≈ 20 tools re-pointed through the resolver | `record_scoped_edit` and `batch_commit propagate` resolve the shard | medium: a scripted move, but ≈ 370 documents' links must be rewritten or redirected | ≈ 2–3 days |
| **C** | **Shard by publication year.** As B; new records spread over years, so parallel appends conflict less. | none | as B, plus a year must be known at record creation | as B | as B | ≈ 3 days |
| **D** | **Event store** — JSONL records, Markdown rendered on demand. | none | every reader moves to the store | `BATCH_COMMIT` Phase 4 rewritten | low: the canonical format changes | ≈ 1–2 weeks, and a change to how the four current files are written |
| **E** | **Cold/hot split of history inside the record** (the pattern already applied to the working model, `working_model_history.md`, and to the state manifest). Status-update paragraphs older than the record's current state move to a `paper_registry_history.md`, record by record, through `record_scoped_edit.py`. | none | `registry_records.py` gains one hop to the history file | one more propagate target | full, record by record | ≈ 1 day; it changes a current file, so it is a `BATCH_COMMIT` |

For the discovery ledger alone, a smaller move exists: its 470,808-byte `## Change-log` block is
history, not leads (`registry_records.py` already excludes it from record access). Moving it to
`discovery_ledger_history.md` would cut the file by 58 % with no tool change beyond one path; the
ledger is not one of the four current files.

## 4 · Recommendation

**A now, E when a measured cost appears; B–D not now.** Option A answers Mirror A7 honestly — it
does not renew a byte deferral, it replaces a trigger that measures nothing with one that measures
the harm the trigger was meant to anticipate, and it extends watching to the two files that have no
anchor. If the operator prefers to act on size anyway, E is the cheapest real reduction, and its
pattern is already proven twice in this repository; the discovery-ledger change-log move is the
cheapest of all.

**Default if the operator does not answer:** none is taken. The acknowledgement in force stands
until 1,923,751 bytes; when it expires `growth_anchors.py check` reports `SCALE_TRIGGER` and, per
Mirror A7, it is not renewed by an agent.

## 5 · What the operator pastes back

One line, for example: `N9: A` · `N9: A + discovery change-log split` · `N9: E` · `N9: B`.
Harness Engineering implements A or the change-log split at T0 on that line; E, B, C or D become a
task with their own record.
