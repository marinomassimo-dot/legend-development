# G1 and I4 — the two residual roadmap items, decided

> **Non-normative design record**, harness only. Actor `junior-harness`, 2026-09-26, operator
> mandate *complete Harness roadmap v1.1*. Nothing here changes a claim, the working model, an
> evidence grade or a disease-model conclusion; no scientific current file was edited and no
> `BATCH_COMMIT` was run. Measured at `main` = `990b6f6`.

| Item | Decision | One-line reason |
|---|---|---|
| **G1** working-model split | **(i) NO SPLIT WARRANTED — not proposed, not implemented** | the file now grows almost only in history, but the three G0 blockers all still hold, and the only harness-side cut (drop `## Changelog` from the read) saves 9 % of the pair every route loads while rewriting a normative "load whole" rule |
| **I4** reverse-link retrieval | **CLOSED — NOT PURSUED (superseded by K1)** | K1 already shipped the reverse link that pays (CURRENT 13 → 17 / 29, default semantics); the one remaining reverse-link form measured here adds **1** target for 2.3× the bytes, and the I3 SUPPORTED rule stays out of reach |

---

## A · G1 — the working model, re-censused from zero

Surface: `disease-models/wwox/registries/working_model_current.md`, `WM_v5.2_2026-09-26`,
**58,467 B**, 284 lines. Section bytes are line-range sums (`wc -c` semantics), measured by one
splitter at `9666003` (the G0 commit; the file is byte-identical to G0's `e9db3ee`) and at `HEAD`.
G0's own table in [`state_hot_cold_20260924.md`](state_hot_cold_20260924.md) used slightly
different cuts (its rows sum to 53,873 B); its history-shaped total, 23,989 B, matches this
re-measure to 1 B.

### A1 · Section census

| Section (lines now) | Bytes now | Bytes at G0 | Δ | Class |
|---|---:|---:|---:|---|
| title, version, date (1–6) + public-edition note (12–18) | 1,108 | 1,108 | 0 | live — identity and contract |
| `**Last update:**` stack (7–11) — **5 lines** (G0: 3) | 9,033 | 6,934 | **+2,099** | **live qualification inside history-shaped text** |
| Disease identity · genotype rules · worked examples (19–45) | 2,295 | 2,295 | 0 | live model |
| Mechanistic architecture (46–78) | 6,624 | 6,624 | 0 | live model |
| BLOCK 1 one-pager (79–147) | 5,884 | 5,884 | 0 | live model |
| BLOCK 2 claim mirror (148–198) | 10,537 | 10,451 | +86 | live model (LINT: mirror ⊇ registry) |
| BLOCK 3 · monitoring endpoints · gene-therapy context (199–237) | 3,552 | 3,552 | 0 | live model |
| `## Changelog` (238–270) | 18,123 | 15,743 | **+2,380** | history, with live residue (see A3) |
| `BATCH_20260714_001` repair (271–284) | 1,311 | 1,311 | 0 | **live qualification inside history-shaped text** (CLAIM 019 cause unresolved; stabilizer `conditional / not design-ready`) |
| **total** | **58,467** | **53,902** | **+4,565** | |

**History-shaped subset: 28,467 B (48.7 %)** — up from 23,988 B (44.5 %) at G0. Live-model
sections: 30,000 B, up **86 B** in two batches.

### A2 · Growth since G0 (`git log 9666003..HEAD -- <file>`)

| Commit | Version | Bytes | `Last update` lines | `Last update` bytes | `## Changelog` bytes | History share |
|---|---|---:|---:|---:|---:|---:|
| `9666003` (G0) | WM_v5.0 | 53,902 | 3 | 6,934 | 15,743 | 44.5 % |
| `8564279` `BATCH_20260926_ALDAZ` | WM_v5.1 | 56,418 | 4 | 8,107 | 17,000 | 46.8 % |
| `1e3e5d2` ALDAZ Mirror repairs | WM_v5.1 | 56,578 | 4 | 8,171 | 17,096 | 47.0 % |
| `6cc8d62` `BATCH_20260926_MALLARET` | WM_v5.2 | 58,467 | 5 | 9,033 | 18,123 | 48.7 % |

**98.1 % of the growth is history** (4,479 of 4,565 B). Each MINOR batch rewrites its claim
rows in place (BLOCK 2: +86 B over two batches) and then writes its narrative **twice**: a
prepended `Last update` line (862–1,237 B) and a Changelog row (≈1.0–1.3 KB). Rate: ≈2.3 KB
per batch. At that rate history passes 60 % of the file after ≈8 more batches.

### A3 · Live qualifications that live only in history-shaped text (spot-checked, not exhaustive)

| Qualification | Where it is in the WM | Also in the claim registry? |
|---|---|---|
| Formal epileptogenesis is **unmeasured in every WWOX model** (the `CLAIM 005` prohibition as retargeted) | `Last update` 2026-09-22 (line 9) and Changelog rows only; no live section says it | yes (1 occurrence) |
| Lithium suppressed PTZ seizures **in all three genotypes, wild-type included** (`CLAIM 016` boundary) | `Last update` 2026-08-10 (line 11) only | yes |
| Q230P cause **unresolved**; SDR stabilizer `conditional / not design-ready` | repair section; also genotype rules (line 38) and BLOCK 1 (line 97) | yes |

So G0's condition 5 still fails **for the file taken alone**: moving the `Last update` stack
or the repair out would remove qualifications a reader of the working model sees nowhere else in
it. It is not a loss for any current route only because every route that loads the working
model loads the claim registry whole beside it — an accident of routing, not a property of the
file, and not one a split should rely on.

### A4 · Who preloads it, and what it costs per route

| Route | Loads the WM | When | WM bytes | WM + claim registry |
|---|---|---|---:|---:|
| `HARNESS` profile; `legend-start` first read; `plan`, `junior-harness` | no | — | 0 | 0 |
| `MINIMAL` / `STANDARD` (`operator_manual.md` § 1.1, § 1.2, § 2) | whole | at comparison, after the first pass (`SOURCE_FIRST`) | 58,467 | 193,566 |
| `FULL` / `BATCH_COMMIT` | whole | start | 58,467 | 193,566 (+ everything) |
| `legend` autopilot step 3 | whole | comparison | 58,467 | 193,566 |
| `legend-deepdive` skill + agent | whole | stage 4 (after first pass) | 58,467 | 193,566 |
| `legend-discovery` 2b | whole, *"where the novelty check needs the global state"* | comparison | 58,467 | 193,566 |
| `legend-hypothesis-forge` 0 | whole | start (`SYNTHESIS`) | 58,467 | 193,566 |
| `legend-aso-designer` 0 | the working model | start | 58,467 | — |

Every row that loads it grew by 4,565 B since G0. The claim registry is 135,099 B.
`## Changelog` alone is **31.0 %** of the WM and **9.4 %** of the WM + claim-registry pair; the
whole history-shaped subset is 14.7 % of the pair.

### A5 · The three options

**(ii) A split through a future `BATCH_COMMIT`** — not warranted now. All three G0 blockers hold
unchanged: the file changes only by `BATCH_COMMIT`; it declares itself *"canonical, complete … the
full version changelog"* and `scripts/test_canonical_structure.py`
(`test_working_model_keeps_required_architecture`) pins `## Changelog` with
`BATCH_20260710_A`, `BATCH_20260714_001`, `WM_v2.1`, `WM_v3.0` inside it; and A3 shows condition 5
still failing. A candidate that moved history would first have to be a scientific edit — writing
the A3 qualifications into the live sections — and that is the Scientist's call, not a harness
proposal. **No commit candidate written.**

**(iii) A harness read of only the live sections** — not implemented. What exists:
`registry_records.py` already parses this file (level-1 `BLOCK n` records), but its `BLOCK 3`
record runs to end of file (23,690 B rendered, Changelog and repair included) and lines 1–78 are
a preamble no record owns — so no current `get` returns "the live model". A new
`--exclude-changelog` view would save 18,123 B per route (9.4 % of the pair, less than one
mid-size full text) and would require rewriting the normative *"`working_model_current.md` —
intero"* in `operator_manual.md` § 1.1/§ 1.2/§ 2 and four skills — a change to what a scientific
route has read, justified by a Changelog audit that A3 shows is not clean (the 2026-09-22 row
repeats the epileptogenesis qualification; the 2026-08-10 batch has no row at all). Not clearly
beneficial, not clearly safe: the rule of the mandate says do not.

**(i) No split warranted — the decision.**

**Revival trigger** (any one): the working model exceeds **80 KB**; the history-shaped share
exceeds **60 %**; or the Scientist lands a `BATCH_COMMIT` that writes the A3 qualifications into
the live sections, which would make condition 5 pass and (ii) a clean structural candidate.

### A6 · Defects found in the canonical file — recorded, not repaired (canonical; `BATCH_COMMIT` only)

1. **No Changelog row for `BATCH_20260810_005`.** That batch's record exists only as the fifth
   `Last update` line; no `WM_v4.2` string appears anywhere in the file.
2. **Changelog rows are not in date order**: the `WM_v4.3` (2026-08-15) row sits above `v1.0`;
   `WM_v4.4` (2026-09-09) and `WM_v4.5` (2026-09-21) sit between `v1.2` and `v1.3`.
3. **The fifth `Last update` line nests five earlier notes** after `Prev:` markers (5,254 B,
   2026-07-14 → 2026-08-10) — a changelog inside a header line.

No test detects 1 or 2. They are structural, harmless to LINT, and belong to a Scientist-owned
structural candidate if and when one is written.

---

## B · I4 — reverse-link retrieval

### B1 · What K1 changed

K1 ([`k1_citation_by_record_link_20260926.md`](k1_citation_by_record_link_20260926.md), `4c1d250`)
shipped as **default semantics** exactly the repair Benchmark I had reverted post hoc: a record
that wikilinks to an **identity record** of the queried PMID/DOI is a `mention (links to …)` hit.
`test_registry_records.py` `CaseEReachableOnlyByExpansion` was changed deliberately in K1, not
worked around. The I4 idea of an opt-in `--backlinks` flag over unchanged forward-only semantics
is therefore moot: the backward link to the identity record is no longer opt-in.

### B2 · The figures

`i1_results_after_K1.json` (frozen fixtures, primary configuration):

| STRONG — 22 fixtures, 29 targets | CURRENT | PROGRESSIVE |
|---|---:|---:|
| before K1 | 13 / 29 at 2.6 % | 25 / 29 at 83.3 % |
| after K1 (= post-hoc backlink-as-mention, row for row) | **17 / 29 at 3.5 %** | 26 / 29 at 83.3 % |

The remaining reverse-link form — **INBOUND1**: CURRENT plus every claim that wikilinks to *any*
record CURRENT returned, not only to identity records — measured here with the frozen fixtures at
each event's parent
([`i4_posthoc_inbound_hop.py`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/i4_posthoc_inbound_hop.py) →
[`i4_posthoc_inbound_hop.json`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/i4_posthoc_inbound_hop.json)):

| STRONG, 29 targets | CURRENT (K1) | INBOUND1 |
|---|---:|---:|
| targets retrieved | 17 | **18** (+ I16 `CLAIM 017`) |
| fixtures fully retrieved | 11 / 22 | 12 / 22 |
| median claim-byte fraction | 3.6 % | **8.1 %** (2.3×) |
| max claim-byte fraction | — | 45.2 % (I07) |

The CURRENT column reproduces the after-K1 figure (17 / 29) with today's tool, which is the
check that the experiment measures the same thing. Fractions here divide by the summed bytes of
the claim records, I1 by the registry file's bytes — hence 3.6 % against I1's 3.5 %.

### B3 · Why no link-graph route gets much further

Of the 11 targets INBOUND1 still misses, **7 fixtures return no claim at all** (I01, I02, I05,
I09, I17, I21, I23): at the event's parent, no record reached from the paper links to any claim,
and no claim links to anything reached. Benchmark I labels a target by the event **adding**
references to the paper in that claim; very often the claim did not cite the paper before the
event. A route built on existing links cannot find a relation the registry does not yet record —
which is the question a comparison is asking. The remaining misses are the I1 classes (common
vocabulary, dropped acronym, unrecorded trigger), not link-graph gaps.

### B4 · Decision

**I4 CLOSED — NOT PURSUED.** The cheap reverse link is already in `main` as K1; the one further
form buys 1 / 29 for 2.3× the bytes. **I3 is unchanged:** its pre-registered SUPPORTED rule needs
**29 / 29** STRONG targets at a material reduction (under half the registry); the best
deterministic figures are 18 / 29 at 8.1 % (INBOUND1) and 26 / 29 at 83.3 % (PROGRESSIVE).
**TARGETED RETRIEVAL NOT SUPPORTED; the claim-registry preload stays.** No flag added, no routing
change, no change to `registry_records.py`.

**Reopen when:** a candidate route reaches all STRONG targets of this fixture set and of any new
events at under half the registry — which, by B3, requires a signal other than the link graph.

---

## DEFAULTS_TAKEN

- **G1 option (i)** over (ii) and (iii): (ii) would have to start as a scientific edit (A3); (iii)
  rewrites a normative load rule for a 9 % saving. The mandate reserved implementation for a
  change that is *clearly* beneficial and safe.
- **No commit candidate for the A6 defects**: a structural edit of a scientific current file is
  the Scientist's to propose; recording them here keeps them from being rediscovered.
- **The I4 experiment is kept as a benchmark artefact** (script + JSON beside the frozen I1
  files, which are untouched), not as a shipped tool: it sits outside the three routed tool roots,
  so `scripts/test_tool_routing.py` has nothing to route.
- Route bytes are the static proxy of G0 (file bytes of what each route's own documentation says
  to load whole), not provider tokens.
