# COMMIT CANDIDATE — CC-20260920-EIGHT-RECORD-CLASSIFICATION-01

**Source:** not a reading. Eight completely-read studies carrying a surviving
`complete_fulltext_read` receipt and no registry declaration, whose record KIND was decided by
the operator on 2026-09-20 — the decision `CC-20260920-REGISTRY-LEDGER-DEPTH-01` § 5 declared out
of its own scope and parked.
**Ledger:** `fulltext_receipts.py verify` → **OK: 156 chained receipt(s), tail anchored in
`framework/state/state_manifest_current.md`** (2026-09-20).
**Change class:** **MINOR**
**Target:** no working-model bump is required or proposed.
**Review floor:** R2. `legend-locator-audit` (R4) **not triggered** — no claim is created,
narrowed, reversed, corroborated or removed (§ 5).

---

## 1 · What is proposed, and what is refused

**Proposed:** three `PAPER` records, four corpus placeholders resolved into the `CORPUS P###`
record of their own harvest number, and one record whose identifier allocation is deferred with its
reason. Each carries the
`Evidence depth` its receipt already backs.

**Refused, explicitly:** no new claim · no claim link · no working-model edit · **no general
PAPER/CORPUS rule** — the operator's instruction is that this decision is local and is not to be
generalised, and `CC-20260920-REGISTRY-LEDGER-DEPTH-01` § 6 measured why: the rationale the corpus
states for keeping a read source as `CORPUS` (T3, LOW, no claim link) describes all three existing
`CORPUS` full-text records **and eleven `PAPER` records too**, so it never was a rule.

🔴 **The classification here is the operator's, and the candidate records it as such.** Nothing in
this file derives it, and no future candidate should cite it as precedent.

---

## 2 · Three records classified as PAPER

| PMID | Today | Proposed | Receipt | Manifest | LIT |
|---|---|---|---|---|---|
| 39416860 | `CORPUS-STUB-175` | **`PAPER 093`** | `FTR-20260810-39416860-01` | 7 locators, schema v2, strict PASS, 0 gaps | `LIT-0191` exists |
| 42397075 | no record | **`PAPER 094`** | `FTR-20260810-42397075-04` | 6 locators, schema v2, strict PASS, 0 gaps | **`LIT-0417`** new |
| 33255508 | `CORPUS-STUB-004` | **`PAPER 095`** | `FTR-20260806-33255508-01` | 4 locators, schema v2, strict PASS, 0 gaps | `LIT-0031` exists |

- *39416860* — Feng 2024, *Front Pediatr*: WWOX-related epileptic encephalopathy from a novel
  variant, case report. On-axis WWOX-DEE.
- *42397075* — 2026, *Brain*: disrupted WWOX–MYC interplay impairs neurogenesis in human brain
  organoids. On-axis mechanistic neuroscience.
- *33255508* — 2020, *Int J Mol Sci*: WWOX loss of function in neurodevelopmental and
  neurodegenerative disorders. A review, and that is not a bar: fifteen `PAPER` records declaring
  full text are reviews.

`PAPER` numbers are sequential allocation and the registry's highest is `PAPER 092`, so 093–095
invent nothing. **The two placeholders are preserved append-only**, in the exact form
`CORPUS-STUB-119` already uses:

```
**Status:** promoted — see [[paper_registry_current#PAPER 0NN]] (BATCH_…, `CC-20260920-EIGHT-RECORD-CLASSIFICATION-01`)
**Registry role:** corpus placeholder only — conservato append-only come storia di audit, mai cancellato
**Next action:** none — risolto per promozione
```

---

## 3 · Five records classified as CORPUS — four determined, one deferred

**`CORPUS-STUB-###` and `CORPUS P###` are one index in two forms, and that settles the
representation.** Measured: 168 stubs numbered 1–179, 188 `P` records numbered 182–400, **zero
overlap**, every stub declaring a `Corpus paper no` equal to its own number, and 168 + 188 = 356,
the `corpus` figure `growth_anchors.py` reports. The stub is the placeholder form of a corpus paper
and `CORPUS P###` is the form that carries content — which is why all three corpus records
declaring full text today (`P261`, `P268`, `P308`) are `P` records and none is a stub.

So a read stub classified as `CORPUS` becomes the `P` record **of its own number**. Nothing is
allocated and no provenance is invented: the number is the one the 2026-08-06 harvest already gave
that paper.

| PMID | Today | Proposed | Receipt | Manifest | LIT |
|---|---|---|---|---|---|
| 31075076 | `CORPUS-STUB-022` | **`CORPUS P022`** | `FTR-20260811-31075076-02` | 9 locators, schema v2, strict PASS, 0 gaps | `LIT-0049` |
| 38182577 | `CORPUS-STUB-027` | **`CORPUS P027`** | `FTR-20260810-38182577-02` | 7 locators, schema v2, strict PASS, 0 gaps | `LIT-0054`, `LIT-0416` |
| 38499540 | `CORPUS-STUB-113` | **`CORPUS P113`** | `FTR-20260909-38499540-02` | 7 locators, schema v2, strict PASS, 0 gaps | `LIT-0133` |
| 27308504 | `CORPUS-STUB-123` | **`CORPUS P123`** | `FTR-20260810-27308504-01` | 12 locators, schema v2, strict PASS, 0 gaps | `LIT-0142` |

Each gains its metadata, `Evidence depth`, `Claim links: none` and `Status: read — corpus
placeholder resolved into its own corpus record`. The stub block is **preserved append-only** and
points at it, exactly as `CORPUS-STUB-119` points at `PAPER 082`.

🔴 **DEFERRED — PMID 42082822, and the reason is identifier provenance, not evidence.**
`FTR-20260811-42082822-01`, 5 locators, schema v2, strict PASS, 0 gaps, no invalidation: the
reading is not in question. What cannot be done honestly is placing it in the index. It is a **2026
publication, later than the 2026-08-06 harvest** — which is also why it has no `LIT` entry — so it
holds no corpus-paper number. `P401` would claim a position in a harvest it was never in, and the
31 gaps inside 182–400 are the numbers of other papers. Two options, neither chosen here:

1. a `CORPUS` record identified by PMID with no `P###`, leaving the index to mean what it means;
2. a declared extension of the index for post-harvest papers.

Both are registry-convention decisions, so neither is this candidate's. The same question does not
arise for `PAPER 094`: `PAPER` numbers are sequential allocation and carry no harvest provenance.

---

## 4 · Verification performed, and its scope

For all eight, checked on `main` at the commit named in § 8:

1. a surviving `complete_fulltext_read` receipt — `receipt_depth_index` returns it, so it is **not
   invalidated**;
2. a schema-v2 manifest, `deepdive_manifest.py --pmid` verdict **PASS**, **0 declared gaps** on
   every one of the eight;
3. the hash chain verifies and its tail is anchored in the state manifest;
4. existing locators and provenance are **carried unchanged**: this candidate adds no locator,
   edits none, and re-interprets nothing the receipt and manifest do not already support.

🔴 **The locators were NOT re-verified, and this candidate does not claim they were.** `files/` is
gitignored, so `deepdive_manifest.py` returns PASS declaring its own scope — *"STRUCTURE ONLY:
local artifact existence, SHA-256 and exact text locators NOT VERIFIED"* — and re-acquiring a
source is a new reading, which `reacquire.py` names `EXTRACTOR_DRIFT` rather than agreement. The
same scope as `CC-20260920-REGISTRY-LEDGER-DEPTH-01` § 4, and for the same reason.

---

## 5 · The two `PARENT_OF_ORIGIN_ATTRIBUTED` findings — reviewed, nothing to correct

The publication gate raises `REVIEW / PARENT_OF_ORIGIN_ATTRIBUTED` on
`deepdive_manifests/PMID39416860.json:116` and `PMID42082822.json:22,84`. Read, as the finding asks.

Both are **verbatim quotations of the published paper's own subjects**:

- 39416860, Table 1 row: `c.911C>A (p.Ser304Tyr) Homozygote … AR Paternal/maternal Unclear clinical
  significance` — the paper's own inheritance column;
- 42082822, Results second sentence: *"the patient is homozygous for the WWOX c.421G > A variant,
  with the father being homozygous and the mother heterozygous for the same mutation"* — and that
  sentence **is** the finding, because it says the variant does not segregate with the phenotype.

The gate already distinguishes exactly this. Its rule raises `BLOCK / PARENT_OF_ORIGIN_PAIRING`
when a pairing is *not* attributed to a published study, and `REVIEW / PARENT_OF_ORIGIN_ATTRIBUTED`
when it is and the reference genotype is absent — and
`test_public_release_gate.py` uses **PMID 39416860 itself** as its worked example of the correct
case, with a second test (`test_the_suppression_is_reported_and_not_silent`) existing so the
exemption can never become invisible.

**Verdict: resolved, no change.** There is no wording to repair — the parent-of-origin *is* the
scientific substance in both — and no decision to escalate: the existing mechanism classifies both
correctly, the release gate reports **PASS / BLOCKS 0**, and no new gate is warranted or proposed.

---

## 6 · The two editorial notices — not studies, and already represented correctly

PMID 30470736 (`Author Correction: WWOX controls hepatic HIF1α …`) and PMID 28373548 (`Editorial
Expression of Concern: WWOX gene restoration prevents lung cancer growth …`) are **out of this
candidate entirely**, per the operator's decision. Checked against the machinery that already
holds them:

| | 30470736 | 28373548 |
|---|---|---|
| `corrections` | `ErratumFor:29724996` | `ExpressionOfConcernFor:16223882` |
| direction | notice side | notice side |
| `_integrity` | `erratum_notice` | `concern_notice` |
| hold | **none** — correct: holding the notice would forbid the source that documents the hold | **none** |
| affected paper present | `CORPUS-STUB-073` (PMID 29724996) | `CORPUS-STUB-119` (PMID 16223882), carrying `Integrity status: PUBLICATION_INTEGRITY_HOLD` |

Direction, the link to the affected paper, provenance (the seed's own `corrections` column) and
admissibility as an audit source are all preserved by the existing model. **Nothing is proposed for
them, and no new record type is created.**

*(The `erratum_notice` value is new as of 2026-09-20: `ErratumFor` had been falling through to
`corrected`, the value belonging to the affected paper, so a correction notice and the paper it
corrects were indistinguishable. Repaired in `batch_queue.py` with two regression arms; eligibility
is unchanged in both directions, because an erratum is not an integrity event.)*

---

## 7 · Named, not resolved

- **PMID 38182577 becomes `CORPUS` while its correction notice is already `PAPER 092`.** The
  annotation therefore outranks the paper it annotates. This follows from the operator's decision
  and from a 2026-09-09 batch that predates it; it is recorded here because a reader who meets the
  pair should see that it was noticed, not inferred as a convention.
- **PMID 38182577 carries two literature entries**, `LIT-0054` and `LIT-0416`. Possible duplicate,
  checked only for existence here. Resolving it is a registry question this candidate does not open.
- **PMID 42082822's identifier**, per § 3.

---

## 8 · Effect on the coverage guard, stated in advance

`test_coverage_is_not_overstated_against_the_registry` currently reads **80 counted-as-read against
71 registry records claiming full text**, gap 9, after `BATCH_20260920_001`. Seven of the eight
records here add to the registry side and none to the queue side:

```
before   80 / 71   gap 9
after    80 / 78   gap 2
```

The residual 2 is PMID 42082822 (§ 3, deferred) plus the two editorial notices of § 6, less one
unit of slack from `PAPER 059`, which declares full text and matches no seed.

🔴 **The remaining gap will not close by propagation alone, and that is the honest statement.** The
two editorial notices are counted as studies by `batch_queue.build`, which resolves read depth from
the receipt and cannot ask whether the thing read was a study — while the operator's decision is
that they are not studies and must not enter the study population. Closing that last unit means
correcting the numerator's semantics, with the classifier § 6 describes, and **not** the guard.
It is named here and proposed nowhere: it is the next decision, not this candidate's.
