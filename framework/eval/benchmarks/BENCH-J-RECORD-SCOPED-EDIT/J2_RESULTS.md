# Benchmark J · J2 — historical replay with the record-scoped editor

> Harness evidence, non-normative, non-scientific. Replayed in memory on git objects of a
> full-history clone at `e30b8ec`; no registry on any checkout was written.
> Editor frozen at `50d9d39` (J1), corpus and rules frozen at `32e91ad` (J0). Raw results:
> [`j2_results.json`](j2_results.json), by `python3 framework/scripts/record_edit_bench.py j2
> --repo <full-history clone>`. Re-running J0 with the J2 version of the script reproduces
> `j0_corpus.json` byte for byte.

## What the replay can and cannot show

The replacement text of every operation comes from history — the actual child, restricted to
its `INTENDED` + `LEGITIMATE_COLLATERAL` hunks — so J2 does **not** test whether an author
would write the right record. It tests the three things the architecture question turns on:
**can every legitimate edit be addressed** (an unambiguous anchor, an operation that expresses
it), **does the editor keep everything else byte-identical while doing it**, and **would it
have refused to carry what the rewrite changed without meaning to**. Refusal paths that never
arise in this history (fenced anchors, nested records, H1 swallowing, re-segmentation) are
exercised by `framework/scripts/test_record_scoped_edit.py`, not here.

## Headline (unique patches: 72 events, 26 commits)

| Family (file) | Events | E hunks | (a) `INTENDED` reproduced | (b) `LEGITIMATE_COLLATERAL` reproduced | (d) lost | refusals | R = X | R = actual child |
|---|---:|---:|---:|---:|---:|---|---:|---:|
| `claim_registry_current` | 15 | 64 | **61 / 61** | **3 / 3** | **0** | — | 15 / 15 | 15 / 15 |
| `literature_tracking_log_current` | 18 | 263 | **210 / 210** | **53 / 53** | **0** | — | 18 / 18 | 18 / 18 |
| `working_model_current` | 10 | 41 | **14 / 14** | **27 / 27** | **0** | — | 10 / 10 | 10 / 10 |
| `paper_registry_current` | 22 | 328 | **317 / 318** | **10 / 10** | **1** | 1 × `ANCHOR_AMBIGUOUS` | 21 / 22 | 20 / 22 |
| meta ×3, research lines (reported, not decided) | 7 | 11 | 11 / 11 | — | 0 | — | 7 / 7 | 7 / 7 |
| **all** | **72** | **707** | **613 / 614** | **93 / 93** | **1** | 1 | 71 / 72 | 70 / 72 |

The same figures hold in both modes: **record** (one `replace` per edited unit, 421 operations)
and **range** (one `replace-within` per edited hunk group, 707 operations). Each lost / refused
count above is per mode, not summed.

- **Silent corruption S = 0.** No accepted operation produced a unit that differs from X, and no
  accepted operation moved a byte outside its range. Every one of the 1,126 accepted (1,128 attempted, the 2 refusals below)
  operations passed the editor's own post-conditions *and* the independent comparison with X.
- **(c) Prevented: 1 of 1.** The only non-edit hunk in the corpus — the `---` separator that
  left `PAPER 095` when `PAPER 096` was inserted above it (`3f65917`) — is absent from R, which
  keeps `PAPER 095`'s bytes; that is one of the two events where R ≠ the actual child. No
  `ACCIDENTAL_COLLATERAL` exists in this history to prevent.
- **Instrument control: 69 / 69 planted deletions labelled non-`INTENDED` (100 %,** threshold
  95 %). 55 went to judgement (R9), 13 were separators (R1 → drift), and **one was labelled
  `LEGITIMATE_COLLATERAL`**: a deleted version line in a meta preamble passes R3, which fires on
  the line's shape, not on whether the unit was targeted — a known blind spot of the cascade, not
  of the editor (a deleted version line outside the target is a drift the editor would still
  prevent). Non-edit detection 68 / 69 (98.6 %).

## (d) The one lost edit, diagnosed

| Event | Unit | Label | Diagnosis |
|---|---|---|---|
| `56c1881` (the conflict-resolution merge of `BATCH_20260926_ALDAZ_R2`) | `## Purpose` of `paper_registry_current` | `INTENDED` (R8) — adds the `### Pathway-code legend` sub-block | **`ANCHOR_AMBIGUOUS`** — the file has **two** `## Purpose` sections (line 11 under `# Paper Registry Current`, line 2504 under `# FASE 1 TRIAGE CORPUS`). `--heading Purpose` is refused by design; no other anchor in the J1 vocabulary reaches it: the enclosing `#` section contains records (`NESTED_RECORD`), and a `###` block cannot be inserted as a standalone block (`RESEGMENTATION`). |

**Not an implementation defect** — the editor did what § 4 specifies, and addressing the first of
two identical headings needs a new kind of anchor (a heading path, e.g. `Paper Registry Current >
Purpose`). Under the pre-registered repair rule it is a **limitation and stays a lost edit**. It
is the only duplicated heading in the four current files today (the working model, claim registry
and literature log have none; no file has a duplicated record id).

## Scope of what the operations write

A full rewrite writes 100 % of the file. The operations of the replay carry (new records
included):

| Family | Bytes of the parent files | Record mode | Range mode |
|---|---:|---:|---:|
| claim registry | 1,619,232 | 12.1 % | 2.7 % |
| literature log | 8,753,926 | 2.1 % | 0.5 % |
| paper registry | 9,335,527 | 5.2 % | 1.9 % |
| working model | 463,538 | **87.8 %** | 3.8 % |

The working model is the outlier in record mode because its records are three `#` BLOCKs and
BLOCK 3 holds the whole changelog: replacing "the record" rewrites most of the file. Range mode —
a `replace-within` on the changelog table, a version line, a mirror row — is the granularity that
fits it, and it reproduces the same 41 / 41 edits.

## What J2 did not find

- no duplicated record id, fenced anchor, nested record or H1-swallowing case in the edits history
  actually made (these stay covered by the unit suite);
- no rename, deletion or reordering of a unit anywhere in 72 events — every structural change a
  batch made was an **insertion** (85 new units);
- no `ACCIDENTAL_COLLATERAL` and one cosmetic drift: on this history the full rewrite, as actually
  practised, did not damage untargeted text. The editor's benefit here is a guarantee, not a
  repair.
