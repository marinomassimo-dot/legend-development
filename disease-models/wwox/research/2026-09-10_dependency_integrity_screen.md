# Dependency-integrity screen — first corpus measurement

**Date:** 2026-09-10 · **Actor:** `plan` (Harness Engineering) · **Task:** `HARNESS-DEPINTEG-001`
**Tool:** [`framework/scripts/dependency_integrity.py`](../../../framework/scripts/dependency_integrity.py)
**Specification:** [`governance/candidates/2026-09-09_sweep_capability_comparison.md`](../../../governance/candidates/2026-09-09_sweep_capability_comparison.md) § 2 P1
**Problem attacked:** [`2026-09-09_actor_retrospective.md`](../analysis/orchestration_reviews/2026-09-09_actor_retrospective.md) § 6.1 S7, § 6.3 H6, § 8.2

> **This file is a report and a review queue. It is not a claim, and it changes nothing.**
> A flag on a dependency is a **prompt to read**. It is not a statement about the citing
> paper, its data, its authors or any claim that rests on it. No registry, no dossier, no
> ledger and none of the four scientific current files were touched by this run, and the
> tool has no code path that could touch them. Every adjudication below is the scientists'.
> **Nothing here is medical advice.**

---

## 1 · What was broken

`retraction_check` in the deep-dive manifests asks NCBI ESummary one question — *has this
PMID been retracted?* It is per-PMID by construction. It therefore cannot see the integrity
status of the papers a paper **depends on**, which is the case § 6.1 S7 actually hit: four
oncology papers that read as four independent bricks share an adenovirus and both
antibodies, all descending from **PMID 16223882** (`10.1073/pnas.0505485102`), which carries
a standing **expression of concern whose scope is precisely the loading-control panel that
would license quantitative comparison**.

The measurement below is that gap, in numbers.

| Screen | Corpus papers it flags |
|---|---:|
| Per-PMID check over the corpus's own DOIs (what exists today) | **1** |
| Dependency screen over the corpus's reference lists (this tool) | **13** |

---

## 2 · Positive control — it reproduces

Required before the tool counts as built. Run through the ordinary screen path, not a
special case:

```
Title:  WWOX gene restoration prevents lung cancer growth in vitro and in vivo
OriginalPaperDOI: 10.1073/pnas.0505485102   OriginalPaperPubMedID: 16223882
RetractionNature: Expression of concern     RetractionPubMedID: 28373548
Reason: Concerns/Issues about Data;Duplication of/in Image;Error in Image;
        Investigation by Company/Institution;Original Data and/or Images not Provided…
verdict: FLAGGED_EXPRESSION_OF_CONCERN
POSITIVE CONTROL: PASS
```

Every field the specification named reproduces, `Reason` included — and the reason names
**image duplication / error in image**, the same class of concern § 7.1 identified as
*"precisely the loading-control panel that would license quantitative comparison."*

---

## 3 · The corpus measurement

Snapshot pinned 2026-09-10, `days_since_fetch` 0 at run time.

| Measure | Value |
|---|---|
| Deep-dive manifests | 81 |
| …carrying a DOI, therefore screenable | **79** |
| …carrying no DOI, therefore **unscreened** (not clean) | 2 — PMID 17803050, 21731849 |
| Corpus papers with ≥1 integrity-flagged dependency | **13 / 79** |
| Corpus papers `SCREENED_CLEAN` | 60 |
| Corpus papers `UNSCREENABLE` (not clean, not flagged) | 6 |
| **Reference DOIs screened / references declared** | **3,995 / 4,341 = 92.0 %** |
| References `UNSCREENABLE_NO_DOI` — never counted clean | 346 (8.0 %) |

**The coverage is a ratio, not a verdict.** 92.0 % of declared references were screened.
The remaining 8.0 % were not screened and are reported as such. The census predicted ~4 %
DOI-less; the measured figure over the whole corpus is **8.0 %**, twice that.

### 3.1 · Review queue — flagged dependencies, most-cited first

| Dependency | Class | Cited by | Corpus PMIDs |
|---|---|---:|---|
| `10.1073/pnas.0505485102` | Expression of concern | **8** | 17360458, 18460020, 18487609, 18974271, 19936220, 20530675, 24510053, 26256646 |
| `10.1074/jbc.m709062200` | **Retraction** | 1 | 21075834 |
| `10.1073/pnas.0931262100` | Expression of concern | 1 | 21318118 |
| `10.1073/pnas.1202081109` | **Retraction** | 1 | 25012504 |
| `10.1073/pnas.0909353106` | **Retraction** | 1 | 29724996 |
| `10.1155/2014/943162` | **Retraction** | 1 | 30755385 |
| `10.1074/jbc.m306104200` | **Retraction** | 1 | 30755385 |

**Two results the 12-paper census sample could not have seen.**

1. **The descent is wider than sampled.** The census screened 12 papers and found 5
   depending on `10.1073/pnas.0505485102`. Over the whole corpus it is **8 of 79** — and
   `24510053` and `26256646` are among them, both papers this repository has read at depth.
2. 🔴 **There are outright retractions in the dependency layer, and the census found none.**
   Five corpus papers cite **four distinct retracted papers**. The census's sample turned up
   only the expression of concern and one correction, so "expression of concern" was the
   whole shape of the problem as it was understood yesterday. It is not.

### 3.2 · What is deliberately NOT in the queue

One `Correction` was found — `10.1038/sj.onc.1209323`, cited by PMID 18460020. It is
reported separately and **is not an integrity flag**. A correction is ordinary scientific
housekeeping; the census said so explicitly and the tool refuses to merge the classes. The
same applies to `Reinstatement`, which is the *opposite* of a flag.

### 3.3 · The six papers that were not screened, and why they are not clean

| PMID | Verdict | Detail |
|---|---|---|
| 27551470 | `UNSCREENABLE_NO_SCREENABLE_REFERENCES` | 17 references deposited, **none carrying a DOI** |
| 28373548 | `UNSCREENABLE_NO_REFERENCE_LIST` | no references deposited — this is the expression-of-concern notice itself |
| 30470736 | `UNSCREENABLE_NO_REFERENCE_LIST` | no references deposited |
| 38355659 | `UNSCREENABLE_NO_REFERENCE_LIST` | no references deposited |
| 42397075 | `UNSCREENABLE_NO_REFERENCE_LIST` | no references deposited |
| 24550385 | `UNSCREENABLE_FETCH_FAILED` | Crossref lookup failed on this run; re-run to resolve |

These six, plus the two DOI-less manifests, are **eight corpus papers about which this
screen says nothing at all**. That is the honest state and it is reported as such.

---

## 4 · Claims whose primary chain touches a flagged paper

Computed read-only by joining the screen onto `claim_registry_current.md` →
`paper_registry_current.md` wikilinks. **6 of 39 claims.**

| Claim | Reached via corpus PMID | Flagged dependency |
|---|---|---|
| CLAIM 9 | 21075834 | `10.1074/jbc.m709062200` (Retraction) |
| CLAIM 9 | 30755385 | `10.1074/jbc.m306104200`, `10.1155/2014/943162` (both Retraction) |
| CLAIM 25 | 29724996 | `10.1073/pnas.0909353106` (Retraction) |
| CLAIM 32 | 17360458 | `10.1073/pnas.0505485102` (EoC) |
| CLAIM 34 | 21075834 | `10.1074/jbc.m709062200` (Retraction) |
| CLAIM 36 | 17360458, 18974271, 19936220 | `10.1073/pnas.0505485102` (EoC) |
| CLAIM 38 | 19936220 | `10.1073/pnas.0505485102` (EoC) |

**> 0 is a reading debt, not a defect**, and this is where the sweep's § 8.2 reasoning
becomes mechanical: *"'Restoring WWOX rescues' is precisely the sentence that would travel
between these contexts unexamined."* Whether it travels is now a question with a list
attached.

Two limits on this join, stated so it is not over-read. It follows the claim's **wikilinked
papers**, which is the registry's own record of what a claim stands on — not a reconstructed
citation graph. And a claim reached through a flagged dependency is a claim whose chain
**touches** a flagged paper; it is not a claim that is wrong, weakened, or in question.
Nothing in this table has been adjudicated by anyone.

---

## 5 · Failure modes — as found, not as predicted

The specification predicted three. Nine are declared in the tool's docstring. These are the
ones that differed from the prediction:

1. 🔴 **`RetractionNature` has five values, not three.** Predicted: `Retraction`,
   `Expression of concern`, `Correction`. Measured in the pinned snapshot: those three plus
   **`Reinstatement` (160 rows)** and **blank (218 rows)**. A tool built to the predicted
   three would have had to guess at a reinstatement — the one value that means the *opposite*
   of a flag.
2. **218 rows are unreachable by this method entirely.** Every blank-nature row also carries
   no `OriginalPaperDOI` (218 of 218, measured). A DOI-keyed screen cannot see any of them.
   A regression test measures this rather than assuming it, so if a future snapshot gives one
   of them a DOI, the suite says so.
3. **DOI-less references are 8.0 %, not ~4 %.** The census sampled 17 of 400; the corpus
   figure is 346 of 4,341.
4. 🔴 **A paper can have references and still be unscreenable.** Predicted as "no DOI on a
   reference". Found: PMID 27551470 deposits **17 references and not one DOI**. The first
   version of this tool reported it `SCREENED_CLEAN` — the exact failure class the dispatch
   named in red, *a screen that returns CLEAN without screening anything*. Its own regression
   suite caught it before it shipped; the verdict
   `UNSCREENABLE_NO_SCREENABLE_REFERENCES` exists because of that catch, and mutation M13
   holds it shut.
8. **The release suite refused a second copy of a canonical pattern.** The claim-chain join
   was first written with its own `^## PAPER (\d+)` regex.
   `test_no_consumer_declares_its_own_record_heading_regex` rejected it by name and pointed at
   `growth_anchors.RECORD_PATTERNS`. Refactoring to the shared matcher also fixed a defect the
   red had not named: the paper registry carries **CORPUS placeholders**, so a splitter given
   only the `papers` convention lets a placeholder's body join the PAPER record above it. Both
   conventions are now passed, mutation M14 holds that shut, and the claim numbers are
   unchanged — the second copy was producing the right answer, which is exactly how a second
   copy survives long enough to drift.
5. **The snapshot goes stale faster than "eventually".** 72,450 rows on 2026-09-09;
   **72,476** on 2026-09-10 — 26 new rows in one day. `days_since_fetch` accompanies every
   verdict for that reason.
6. **The `Reason` field's semantics remain undescribed and undescribable today.** It is
   passed through verbatim and never parsed, thresholded or scored. This is the one
   inclusion-contract item still open on the `_external_repos/MANIFEST.md` entry, and it is
   why that entry is `AUDITED` rather than `REPRODUCED`.
7. **The dataset licence could not be verified in this run.** CC0 is asserted for the data by
   Crossref, but the endpoint sends no licence header and `api.labs.crossref.org/openapi.json`
   declares **MIT for the API software** — a different thing, and an easy conflation. The
   manifest row records the licence as unverified.

---

## 6 · Reproducing this

```bash
python3 framework/scripts/dependency_integrity.py fetch        # ~66 MB, key-less, free
python3 framework/scripts/dependency_integrity.py pin --write
python3 framework/scripts/dependency_integrity.py verify
python3 framework/scripts/dependency_integrity.py control      # must PASS
python3 framework/scripts/dependency_integrity.py corpus --json <out.json>
python3 framework/scripts/dependency_integrity.py claims --from-json <out.json>
python3 framework/scripts/test_dependency_integrity.py         # 60 assertions, 14 mutations
```

**Zero external spend. No API key. No email address is sent to any endpoint** — the Crossref
labs data path was measured serving the complete CSV without one, and the tool has no code
path that accepts a contact address. (The labs `/docs` path *does* return `not-polite` 403
without one; the data path does not, and the data path is the only one used.)

The snapshot is ~66 MB and lives under `files/`, which is gitignored. What is versioned is
the pin: [`framework/config/retraction_watch_pin.json`](../../../framework/config/retraction_watch_pin.json)
— sha256, byte count, row count, fetch date, URL.

---

## 7 · What a scientist would do with this

Not proposed as a decision, only as the shape of the debt:

- **8 papers depending on `10.1073/pnas.0505485102`** is the § 8.2 non-independence finding
  at corpus scale rather than lot scale. The reagent-descent question § 6.1 S7 raised for
  four papers now has a candidate list of eight.
- **The five papers citing a retracted paper are a different and newer question**, and none
  of them was part of the sweep that produced this tool.
- **The eight papers this screen could not read at all** are the honest gap; a screen that
  reported them clean would be worse than no screen.
