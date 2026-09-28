# Benchmark J · J5 — a heading qualified by its enclosing heading · PREREGISTRATION

> Harness evidence, non-scientific. Written and committed **before** the instrument change below
> exists and before any J5 replay is run. Nothing here changes a claim, the working model, an
> evidence grade or a disease-model conclusion.

## 0 · The question, and what is already known

[`J3_DECISION.md`](J3_DECISION.md) kept the FULL rewrite for `paper_registry_current` because of
exactly one lost edit out of 328: `56c1881` adds a sub-block to `## Purpose`, and the file has two
`## Purpose` sections — one under `# Paper Registry Current`, one under `# FASE 1 TRIAGE CORPUS`
(measured at `56c1881^` and at `main` = `8ce0bfb`: the two `#` parents are distinct). J3 names the
route that would reopen it: *"a heading-path anchor … followed by a new, separately pre-registered
replay."* This file is that pre-registration. The author knows the miss and the proposed fix; the
point of fixing the rule now is that nothing about the rule can move after the replay is seen.

**Question.** With one added anchor qualifier, does record-scoped editing reproduce **every**
legitimate edit the paper registry received in the frozen corpus, with no silent corruption?

## 1 · Instrument change — specified before it is written

`record_scoped_edit.py` gains one optional field, **`under`** (`--under TEXT`, `"under": "…"` in an
ops file):

- valid **only together with `heading`**; `under` without `heading` is refused (`ANCHOR_MISSING`);
- the heading hits (exact text, as today) are kept only when a heading whose exact text equals
  `under` is on the hit's **enclosing chain** — for each strictly lower level, the nearest
  preceding heading of that level;
- zero hits after filtering → `ANCHOR_MISSING`; more than one → `ANCHOR_AMBIGUOUS`;
- nothing else changes: an op without `under` resolves exactly as before, and every existing
  refusal, post-condition and the `UNBOUNDED_SPAN` rule of `e9c9172` stay in force.

The J2 deriver (`record_edit_bench.py`) gains one switch, used only by J5: when it would emit a
`heading` anchor whose text occurs more than once among the parent file's headings, it adds
`under` = the text of the nearest enclosing heading of lower level of that unit in the parent.
With the switch off (J2), its output is unchanged.

## 2 · Corpus and procedure

- **Primary corpus:** the frozen [`j0_corpus.json`](j0_corpus.json) (`rev` `e30b8ecbfd15`),
  `paper_registry_current` family only: **22 unique events, 328 E hunks** (318 `INTENDED` + 10
  `LEGITIMATE_COLLATERAL`; 1 `VERBATIM_COPY_DRIFT`, not an edit). Labels are not re-derived.
- **Replay:** J2 § 5 unchanged — parent bytes from git objects, ops derived from the E hunks,
  applied by the editor at the J5 commit, compared with X (the parent with only E applied), both
  granularities. **Primary granularity: record** (as J2 for this family); range is reported.
- **Out-of-sample, reported and not decided:** the seven post-J4 `BATCH_COMMIT` propagations that
  touched the paper registry (`c99dfe5`, `1cdb1a4`, `95bd885`, `bc09bc9`, `da8b08b`, `c5eec22`,
  `67ac5ec`), labelled with the same cascade.
- **Instrument control:** J2's planted deletion on the same 22 events, re-run.

## 3 · Decision rule — fixed now

The paper-registry family is **supported** iff, in the primary granularity, **all** hold:

1. lost legitimate edits **L = 0** (328 / 328 reproduced);
2. silent corruption **S = 0** in **both** granularities;
3. `outside_units_equal_x` in every event (untouched units byte-equal);
4. the instrument control detects ≥ 95 % of its plants.

A refusal of any code — including `UNBOUNDED_SPAN` from the editor change made after J2 — counts
as a loss, not as an excuse. **Any** S > 0 is disqualifying. If the family is supported, J3's
table gains the fourth row and the verdict for the four current files becomes SUPPORTED **as
evidence**; changing `prompt_batch_commit.md` Phase 4.0 so that `BATCH_COMMIT` actually propagates
the paper registry record by record is a separate step, not taken inside this benchmark. If not
supported, FULL rewrite stays, and the miss is diagnosed.
