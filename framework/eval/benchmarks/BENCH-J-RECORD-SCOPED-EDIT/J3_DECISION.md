# Benchmark J · J3 — architecture decision

> Harness evidence and a propagation-path decision; non-scientific. Nothing here changes a claim,
> the working model, an evidence grade or a disease-model conclusion.

## Decision

**PARTIALLY_SUPPORTED.** Record-scoped editing replaces the full whole-file rewrite for
**`working_model_current`, `claim_registry_current` and `literature_tracking_log_current`**.
`paper_registry_current` keeps the full rewrite.

The pre-registered rule ([`PREREGISTRATION.md`](PREREGISTRATION.md) § 6), applied row by row:

| Condition | Required | Measured ([`J2_RESULTS.md`](J2_RESULTS.md)) | Met |
|---|---|---|---|
| silent corruption S | 0 | **0** (1,126 accepted operations, both modes) | ✅ |
| families eligible (≥ 5 unique events, ≥ 20 E hunks) | ≥ 3 for a valid result | **4 / 4** — claims 15 / 64 · literature log 18 / 263 · working model 10 / 41 · papers 22 / 328 | ✅ |
| judgement share of non-drift hunks | ≤ 10 % | **1.8 %** (13 / 707) | ✅ |
| instrument control | ≥ 95 % | **100 %** (69 / 69) | ✅ |
| claim registry: L = 0 | — | **0** lost of 64 | supported |
| literature log: L = 0 | — | **0** lost of 263 | supported |
| working model: L = 0 | — | **0** lost of 41 | supported |
| paper registry: L = 0 | — | **1** lost of 328 (`ANCHOR_AMBIGUOUS`) | **not supported** |
| SUPPORTED needs all four | — | three of four | ✗ |
| PARTIALLY_SUPPORTED needs S = 0, ≥ 1 supported, every miss diagnosed | — | S = 0, three supported, the one miss diagnosed | ✅ |

## Why, in the order the evidence arrived

1. **Every legitimate edit in three files is expressible.** 368 edits over 43 events —
   claim narrowings, new claims, literature-log status sweeps, working-model mirror rows,
   changelog rows, version lines, separators — were reproduced byte for byte by operations
   addressed to one record or one range, with every other byte proven unchanged, in both the
   record and the range granularity.
2. **The one miss is an address, not an edit.** The paper registry has two `## Purpose`
   sections; the conflict resolution of `56c1881` added a sub-block to the first. The editor
   refuses an ambiguous heading by design, and nothing else in its vocabulary reaches that
   section. A heading-path anchor would; it is a new capability, so under the pre-registered
   repair rule the miss stands and the family is not supported. The other 327 paper-registry
   edits, all of them to records, replayed exactly.
3. **The observed benefit is a guarantee, not a repair.** In 72 events the rewrite, as practised,
   introduced no accidental collateral and one cosmetic drift (a displaced separator, which the
   editor prevented). The case for adoption is that "copied verbatim" becomes a checked
   post-condition instead of an instruction; it is not that history shows damage.

## What changes (J4), and what does not

- **`BATCH_COMMIT` Phase 4 propagation** into the three supported files goes through
  `record_scoped_edit.py` — one atomic `apply --ops` per file, dry run first — wrapped by
  `batch_commit.py propagate`, which refuses the files this decision does not cover. The rule
  lives in `framework/protocols/prompt_batch_commit.md` § Phase 4 ("4.0"), and the
  `legend-commit` skill step 4 points there.
- **Granularity for the working model: range.** Its records are three `#` BLOCKs and BLOCK 3
  holds the changelog, so a whole-record `replace` of BLOCK 3 rewrites 88 % of the file; the
  same 41 edits replayed as `replace-within` wrote 3.8 %.
- **`paper_registry_current` keeps the full rewrite**, unchanged sections copied verbatim, as
  before. Nothing else in the protocol changes: snapshot, post-LINT, restore on ABORT, all or
  nothing.
- A file the editor refuses mid-batch (a new ambiguity) is not forced: the refusal is recorded
  in the batch report and that file falls back to the full rewrite for that batch.

## What would reopen this

- **For the paper registry:** a heading-path anchor (`--heading "Paper Registry Current >
  Purpose"`) or a structural batch that makes the two `Purpose` headings distinct, followed by a
  new, separately pre-registered replay. A post-hoc re-run of this corpus with a new anchor is
  post-hoc and decides nothing.
- **For the three supported files:** the first refusal or post-condition failure in production
  — recorded, investigated, and, if it is a lost edit rather than a correct refusal, a reason
  to withdraw the family.
- **The corpus is small and mostly additive** (85 inserted units, no rename, deletion or move),
  and its edits were practised with care. New batch types — renames, record splits, deletions —
  are exercised only by the unit suite until history contains them.
