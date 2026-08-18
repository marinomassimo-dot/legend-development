---
artifact: BENCH-AB-001 — common benchmark instructions
instructions_version: 1
benchmark_id: BENCH-AB-001
identical_for: scientist-a, scientist-b
---

# BENCHMARK INSTRUCTIONS — common to both readers

**This file is byte-identical in both surfaces.** So is the output schema. Exactly two files
differ between the two readers: `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md`. That is the
experiment.

## 1 · The paper, and the packet

```
PMID 42397075 · doi 10.1093/brain/awag239 · Brain, 2026 · accepted manuscript

files/fulltext/PMID42397075_Aqeilan2026.pdf                          the article
files/fulltext/PMID42397075_Aqeilan2026_fitz.txt                     its extracted text surface
files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File008.pdf   author contributions
                                                          …File009.pdf   detailed Materials and methods
                                                          …File010.pdf   supplementary figures 1–10
                                                          …File011.pdf   resource table
                                                          …File012.pdf   uncropped western blots
```

Every digest is recorded in the benchmark manifest and was verified equal in both surfaces
before handover. **The text surface's identity is its digest, not a recipe**: its declared
extraction command does not regenerate it byte-for-byte, which changes nothing about what it
says and does mean you should quote against the file you have.

**Figure panels are pixels.** Render what you need from the PDF at a resolution where the panel
is legible, write the render into `output/renders/`, and declare it as a `source_artifact` of
kind `figure` with its SHA-256. A caption is not a panel; a panel you did not open is a panel
you did not read.

## 2 · What binds you

Everything in `roles/scientist.md` and `framework/protocols/scientist_reading_modes.md` §3 —
in full, unaltered by this being a benchmark. In particular:

- **full text over abstract**, always, since the full text is here;
- **grep is not a method of analysis**; it finds a place to read, never a substitute for reading;
- **verbatim locators captured while the document is open** — the entry shape is in the output
  schema and is exactly what `framework/scripts/deepdive_manifest.py` accepts;
- **coverage map with no `not_read`** for a complete reading;
- **epistemic typing on every statement you carry out**: `DATO · INFERENZA · IPOTESI ·
  ESPANSIONE`; premise tags on rejections and non-trivial conclusions; a `REVIVAL_TRIGGER` on
  every negative;
- **no hypothesis promoted to observation**, ever, including the authors' own.

## 3 · Depth is not negotiable, and the budget rule is explicit

> **Do not compress depth or coverage for token, time or cost.** A reading shortened for budget
> produces a receipt that overstates itself, and the receipt is what the rest of the system
> trusts.

If you genuinely cannot complete at full depth, **stop and report the partial state with its
coverage map naming exactly what is unread**. A declared partial reading is a legitimate,
useful result. A silently thinned complete reading is a false record, and it is the more
expensive of the two by a wide margin.

You are running `AUTONOMOUS_COMPLETE`: do not ask questions to proceed. If you hit something that
genuinely blocks you, record it as a `BLOCKER` in `output/receipt.json` and continue with
everything that is not blocked.

## 4 · What you produce

Four artifacts, all inside this surface, shapes fixed by `benchmark/OUTPUT_SCHEMA.md`:

```
disease-models/wwox/research/deepdive_manifests/PMID42397075.json   work manifest, schema_version 2
disease-models/wwox/research/fulltext_dossiers/PMID42397075.md      dossier — artifacts + locators
output/claim_candidates.md                                          claim candidates
output/receipt.json                                                 coverage map, blockers, self-check
output/critical_reading.md                                          MODE B ONLY — see your mode directive
output/renders/…                                                    figure renders you made, digested
```

**No other file.** No new schema, no `claims.json`, no second locator format. If you find
yourself inventing a container for something, the container already exists — the schema names
where.

## 5 · Before you declare completion

Run, and record the output verbatim in `output/receipt.json`:

```bash
python3 framework/scripts/deepdive_manifest.py \
    --workspace . --pmid 42397075 --verify-artifacts --require-current-schema
```

`VERDICT: PASS` is a precondition of completion, not a nicety. Then check by hand:

1. every locator's `artifact` is a path **inside this surface**;
2. the coverage map contains no `not_read`;
3. every claim candidate carries the twelve canonical fields **and** the four intermediate
   fields, and its `Type` is one of the four epistemic levels (compound values are allowed and
   are how the registry already writes them);
4. every negative or rejection carries a premise tag and a revival trigger;
5. — MODE B — every mandatory axis is answered, including the ones with nothing to report.

Commit at milestones in this surface's repository. Then declare completion. **Your reading is
frozen at that moment, before anyone reads its content**, and nothing you write afterwards
changes the frozen record — corrections after freeze go in a separate dated file and are
reported as corrections.

## 6 · The two prohibitions that make this a benchmark

```
DO NOT read LEGEND's prior work on this paper, from any path, in any checkout.
DO NOT communicate with the other reader, directly or through anyone.
```

Both are checkable after the fact only in part, and both are the point. If you break one by
accident, **say so in `output/receipt.json`**: a declared contamination is a usable result, and
an undeclared one silently invalidates the experiment for everyone.
