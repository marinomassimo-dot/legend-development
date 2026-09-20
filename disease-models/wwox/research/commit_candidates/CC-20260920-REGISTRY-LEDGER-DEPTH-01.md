# COMMIT CANDIDATE — CC-20260920-REGISTRY-LEDGER-DEPTH-01

**Source:** not a reading. Nine `paper_registry_current.md` records whose `Evidence depth` field
disagrees with the hash-chained receipt ledger, on records **whose kind is already settled**.
**Ledger:** `fulltext_read_receipts.jsonl` — `fulltext_receipts.py verify` → **OK: 156 chained
receipt(s), tail anchored in `framework/state/state_manifest_current.md`** (2026-09-20).
**Change class:** **MINOR**
**Target:** no working-model bump is required or proposed.
**Review floor:** R2. `legend-locator-audit` (R4) **not triggered** — no consolidated baseline claim
is narrowed, reversed, corroborated or removed, and no claim is touched at all (§4).

---

## 1 · What is proposed, and what is refused

**Proposed:** one `Evidence depth` field per record, on **nine** records, recording a reading the
ledger already carries. Nothing else.

**Refused, explicitly:** no new claim · no claim link · no change of `Status` · **no promotion of any
`CORPUS` record to `PAPER`** · no change to any record's kind · no working-model edit · no new field,
vocabulary or convention.

🔴 **This candidate asserts nothing about the papers.** It asserts something about the *registry*:
that a reading which is recorded, chained and manifest-backed should also be visible to a reader of
the record. Every scientific judgement in these nine records — tier, transferability, clinical
relevance, claim links, role — is left exactly as its author left it.

---

## 2 · The nine records

All nine carry a surviving `complete_fulltext_read` receipt and a schema-v2 manifest with a strict
validator verdict of PASS. Declared gaps are the manifest's own, named here rather than smoothed.

| Record | PMID | Receipt | Manifest | Locators | Declared gaps |
|---|---|---|---|---|---|
| `PAPER 018` | 36779245 | `FTR-20260804-36779245-02` | `PMID36779245.json` | 5 | 3 |
| `PAPER 019` | 32000863 | `FTR-20260804-32000863-01` | `PMID32000863.json` | 5 | 3 |
| `PAPER 020` | 32581702 | `FTR-20260810-32581702-01` | `PMID32581702.json` | 10 | 0 |
| `PAPER 021` | 31340538 | `FTR-20260806-31340538-01` | `PMID31340538.json` | 4 | 0 |
| `PAPER 024` | 25012504 | `FTR-20260814-25012504-01` | `PMID25012504.json` | 5 | 0 |
| `CORPUS P222` | 18487609 | `FTR-20260811-18487609-01` | `PMID18487609.json` | 5 | 0 |
| `CORPUS P272` | 24550385 | `FTR-20260810-24550385-02` | `PMID24550385.json` | 7 | 0 |
| `CORPUS P346` | 22634283 | `FTR-20260811-22634283-02` | `PMID22634283.json` | 5 | 0 |
| `CORPUS P397` | 31428585 | `FTR-20260909-31428585-02` | `PMID31428585.json` | 7 | 0 |

**Proposed field**, in the form `CORPUS P261` already uses, one per record:

```
**Evidence depth:** complete_fulltext_read — `<receipt>`; manifest
`deepdive_manifests/PMID<pmid>.json` (<n> locators, schema v2, strict PASS, <g> gaps);
declaration reconciled from the ledger by CC-20260920-REGISTRY-LEDGER-DEPTH-01
```

Eight of the nine records carry **no `Evidence depth` field at all**. The ninth is different and is
the reason this candidate was written at all.

---

## 3 · `PAPER 018` — the record contradicts the ledger, and tells a reader to undo the work

`PAPER 018` is Oliver 2023, *Epilepsia*, `PMID 36779245` — WWOX-DEE epileptology and mortality,
13 patients, 12 families, 5 centres. **Tier T1, clinical relevance HIGH.** It is the most
directly on-axis class of paper this disease model has.

The record says:

```
**Status:** filtered_in
**Evidence depth:** abstract + frammenti Scholar Gateway
**Claim links:** pending
**Next action:** full text retrieval PMC10952634 — alta priorità
```

The ledger says the full text was retrieved and read completely on **2026-08-04**
(`FTR-20260804-36779245-02`, `reread_reason: inadequate_prior_coverage`, manifest with 5 locators,
strict PASS), after a first partial pass (`-01`) and before a later, narrower one
(`-03`, 2026-08-10, whose output is `full_text_queue_current.md#FT-056`).

So the registry asks a reader to retrieve, at high priority, a paper that was read in full
six weeks earlier. That is not a cosmetic disagreement: it is an instruction to repeat work,
on the highest-relevance record in the disagreeing set.

🔴 **Why the later `partial` receipt does not withdraw the complete one.** `receipt_depth_index`
keeps the **deepest surviving** receipt per identifier, and its docstring states the reason: an
invalidation names one event, and a reading that happened does not un-happen. A narrower later pass
adds a pass; it does not retract the earlier complete read. `FTR-20260804-36779245-02` is not
invalidated. This was checked before writing this candidate, because if the rule had been
"latest wins" the numerator itself would have been wrong and this candidate would have been the
wrong repair.

**Proposed for `PAPER 018` only, in addition to the field above:** `Next action:` is replaced by
`none — full text retrieved and read 2026-08-04 (FTR-20260804-36779245-02)`. `Status`, `Claim
links: pending`, and every scientific field stay untouched: whether that reading produces a claim is
not this candidate's question.

---

## 4 · Verification scope — stated, not implied

🔴 **The locators behind these nine readings were NOT re-verified, and this candidate does not claim
they were.** `files/` is gitignored, so no source artefact is present in this checkout;
`deepdive_manifest.py --pmid <n>` returns PASS with the scope it prints itself:

> `STRUCTURE ONLY: local artifact existence, SHA-256 and exact text locators NOT VERIFIED`

What this candidate rests on is therefore named exactly:

1. the receipt ledger's **hash chain verifies** and its tail is anchored in the state manifest;
2. each manifest **exists, is schema v2 and is structurally complete** with its gaps declared;
3. the receipts are **not invalidated**.

Re-verifying the locators would require re-acquiring the sources, and a re-acquisition is a **new
reading**, not a verification of the old one — `reacquire.py` names that `EXTRACTOR_DRIFT` rather
than agreement. Nothing here is offered as a substitute for that. A reviewer who wants the locators
audited should say so; this candidate would be unaffected, because it proposes no claim that a
locator could support or refuse.

`legend-locator-audit` is **not triggered**: its triggers are a reading that narrows, reverses,
corroborates or removes a `consolidated baseline` claim, or a MAJOR change class. This candidate
touches no claim and is MINOR.

---

## 5 · Deliberately out of scope — ten records this candidate will not touch

Ten further records carry a `complete_fulltext_read` receipt and no registry declaration, and each
would require deciding **what kind of record should exist**, which is a scientific decision this
candidate has no authority to take:

| PMID | Current state | Receipt |
|---|---|---|
| 33255508 | `CORPUS-STUB-004` | `FTR-20260806-33255508-01` |
| 31075076 | `CORPUS-STUB-022` | `FTR-20260811-31075076-02` |
| 38182577 | `CORPUS-STUB-027` | `FTR-20260810-38182577-02` |
| 38499540 | `CORPUS-STUB-113` | `FTR-20260909-38499540-02` |
| 27308504 | `CORPUS-STUB-123` | `FTR-20260810-27308504-01` |
| 39416860 | `CORPUS-STUB-175` | `FTR-20260810-39416860-01` |
| 42082822 | no record in any registry | `FTR-20260811-42082822-01` |
| 30470736 | no record in any registry | `FTR-20260909-30470736-01` |
| 28373548 | no record in any registry | `FTR-20260909-28373548-01` |
| 42397075 | no record in any registry | `FTR-20260810-42397075-04` |

A `CORPUS-STUB` is a placeholder from the 2026-08-06 corpus harvest, not a record of a source; and
four of these ten exist in no registry at all. Turning either into a `PAPER` or a `CORPUS` is the
open question recorded in §6. **Naming them here is the point:** they are not forgotten, they are
parked, and their reading is not thereby unrecorded — the receipt carries it.

---

## 6 · The PAPER-versus-CORPUS convention, as observed and as it actually behaves

Two 2026-09-09 candidates state the rationale for keeping a completely-read source as `CORPUS`:

- `CC-20260909-20530675-01` § 1 — *"The paper is Tier C, clinical relevance LOW, `Claim links:
  none`, and its transfer verdict toward the reference genotype is `ESPANSIONE` / T3 … Promoting it
  would import an oncology record into a disease model whose consolidated baseline is entirely
  WWOX-DEE neurobiology … **read completely and promoted are different acts.**"*
- `CC-20260909-21731849-01` § 1 — *"It is a REVIEW … a secondary source … **No promotion to
  `PAPER`.**"*

Measured against the registry on 2026-09-20, that rationale **describes the three `CORPUS`
full-text records exactly and does not separate them from `PAPER`**:

| | records | Tier / relevance |
|---|---|---|
| `CORPUS` declaring full text | 3 (`P261`, `P268`, `P308`) | **T3 / LOW, all three** |
| `PAPER` declaring full text | 59 | 30 are T3; **11 are T3 *and* LOW** |
| `PAPER` declaring full text that are Reviews | 15 | 9 of them with no claim link |

So *every* `CORPUS` full-text record is T3/LOW with no claim link — and so are eleven `PAPER`
records, and "it is a review" does not separate them either, because fifteen `PAPER` records are
reviews. **The stated convention is necessary and not sufficient.** What actually separates the two
sets is how the record was created: `CORPUS P###` numbers come from the 2026-08-06 harvest and stay
`CORPUS` when later read, `PAPER` records come from the pipeline.

🔴 **Recorded as an observed convention, not proposed as a rule.** This candidate does not turn it
into governance and does not resolve it. It records that the distinction currently in force is one
of record provenance with a scientific rationale attached retrospectively, so that whoever decides
§5 decides it knowing that, and not on a rule that looks derivable and is not.

---

## 7 · One false lead, named so it is not "repaired"

Twelve `PAPER` records declare `full text reviewed` while their deepest receipt is
`partial_fulltext_read`: `PAPER 012, 014, 016, 028, 042, 043, 044, 045, 046, 049, 050, 053`.

**This is not an overstatement and must not be corrected.** Those twelve receipts are
`record_kind: legacy_reconstruction`, `workflow: public-registry-legacy-reconstruction`, all written
at one timestamp on 2026-07-26, and their own `evidence_basis` says which direction the derivation
ran:

> `"PAPER 043 declares Evidence depth: full text reviewed (coverage_status: complete_fulltext_read)",
>  "section-by-section coverage map did not survive in the public fixture; complete status not
>  reconstructed"`

The receipt was reconstructed **from** the registry when the public edition was built, and typed
conservatively because the section map did not survive de-identification. Re-typing the registry to
match would propagate the reconstruction's own caution back onto the record it was derived from.

---

## 8 · Effect on `test_batch_queue`, stated in advance

`test_coverage_is_not_overstated_against_the_registry` currently measures **80 counted-as-read
against 62 registry records claiming full text**. This candidate, once propagated, adds nine records
to the registry side and none to the queue side:

```
before   80 / 62   gap 18
after    80 / 71   gap  9
```

The residual nine is exactly the ten records of §5 less one unit of slack — `PAPER 059` declares
full text and corresponds to no record in the seed corpus, so it sits on the registry side of the
comparison with nothing opposite it.

🔴 **The guard is not touched by this candidate and must not be.** The gap falls because the registry
comes to agree with the ledger. If §5 is resolved, the gap closes on the same terms; if it is
resolved by deciding that some of those readings should not be declared, the numerator is what
moves, and that too is a scientific decision, not a threshold.

---

## 9 · Provenance of this candidate

Every figure above was re-derived on `main` at `1708af5` on 2026-09-20 with the tools already in the
repository — `fulltext_receipts.py verify`, `deepdive_manifest.py --pmid`, `batch_queue.build`, and
the registry read through `registry_records.py`. No file outside this candidate was written.
