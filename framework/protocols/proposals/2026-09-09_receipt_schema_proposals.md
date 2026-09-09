# Two receipt-schema proposals for the operator — 2026-09-09

> **Status: PROPOSED. Neither is implemented, and neither may be implemented by an agent.**
>
> The third question from the same review — §4.2, `identity_correction` — is **not** here: it
> changes no guarantee, so under [`LEGEND_CORE` §21e](../../instruction/LEGEND_CORE.md#21e-agile-operating-mode)
> ("a guard rule, a gate, a role contract, a protocol, an annex or a skill is harness, and
> harness is T0") it was implemented and applied the same day. Its contract is in
> [`fulltext_read_receipt.md`](../fulltext_read_receipt.md).
>
> **These two are different in kind, and that is the whole reason they are a document instead
> of a commit.** Each changes what an attestation already written *means* — §4.1 changes what
> "complete" is asserted of, §4.3 changes what `surface` distinguishes — and that is a change
> to a fundamental guarantee, which §21d reserves to the operator.

Author: `schema-eng`. Source: [`2026-09-09_residual_cases.md`](../../../disease-models/wwox/analysis/orchestration_reviews/2026-09-09_residual_cases.md) §4.1 and §4.3.

---

## 🔴 The constraint both designs are built to satisfy

> **Do not retroactively reinterpret past readings.** — the operator, 2026-09-09

A schema that silently upgrades an old `partial` to `complete` because a later event filled a
gap is exactly what is forbidden. Both designs below therefore obey one rule:

> **An old record's meaning is fixed. Any new assertion is a NEW record that cites its parents
> and asserts nothing they did not.**

"Asserts nothing they did not" is not a promise in a docstring in either design. It is a field
that names, per section, *which parent* said it — so the claim is checkable by a command rather
than by trusting the writer.

---

## 1 · Study-level coverage rollup (review §4.1)

### The problem, in one sentence

Two studies hold full coverage **across** their events yet remain `partial`, because no field
records that the *union* of two coverage maps is complete.

### Before — two real records, today

`25331887` (Abu-Odeh 2014, *PNAS*). Neither event can declare `complete_fulltext_read`: the
first has no supplement, the second read almost nothing but the supplement.

```json
{
  "event_id": "FTR-20260810-25331887-01",
  "record_kind": "contemporaneous_receipt",
  "study_id": { "doi": "10.1073/pnas.1409252111", "pmid": "25331887" },
  "evidence_depth": "partial_fulltext_read",
  "coverage": {
    "abstract": "read",       "introduction": "read",  "methods": "read",
    "results": "read",        "figures": "read",       "tables": "not_present",
    "discussion": "read",     "limitations": "read",   "references": "read",
    "supplementary": "unavailable"
  },
  "prior_receipt": null,
  "reread_reason": "first_read"
}
```

```json
{
  "event_id": "FTR-20260909-25331887-02",
  "record_kind": "contemporaneous_receipt",
  "study_id": { "doi": "10.1073/pnas.1409252111", "pmid": "25331887" },
  "evidence_depth": "partial_fulltext_read",
  "coverage": {
    "abstract": "not_read",   "introduction": "not_read", "methods": "read",
    "results": "not_read",    "figures": "read",          "tables": "not_present",
    "discussion": "not_read", "limitations": "not_read",  "references": "not_read",
    "supplementary": "read"
  },
  "prior_receipt": "FTR-20260810-25331887-01",
  "reread_reason": "inadequate_prior_coverage"
}
```

### After — the two records above are **byte-identical**, and a third is appended

```json
{
  "event_id": "FTR-20260909-25331887-03",
  "record_kind": "study_coverage_rollup",
  "study_id": { "doi": "10.1073/pnas.1409252111", "pmid": "25331887" },
  "event_at": "2026-09-09T21:40:00Z",
  "analysis_at": null,
  "analysis_time_precision": "unknown",
  "workflow": "rollup over persisted receipts; no document was opened",
  "evidence_depth": "complete_fulltext_read",
  "source_locator": "disease-models/wwox/registries/fulltext_read_receipts.jsonl",
  "source_fingerprint": null,
  "source_kind": "metadata",
  "parent_receipts": ["FTR-20260810-25331887-01", "FTR-20260909-25331887-02"],
  "coverage": {
    "abstract": "read",       "introduction": "read",  "methods": "read",
    "results": "read",        "figures": "read",       "tables": "not_present",
    "discussion": "read",     "limitations": "read",   "references": "read",
    "supplementary": "read"
  },
  "coverage_provenance": {
    "abstract": "FTR-20260810-25331887-01",  "introduction": "FTR-20260810-25331887-01",
    "methods": "FTR-20260810-25331887-01",   "results": "FTR-20260810-25331887-01",
    "figures": "FTR-20260810-25331887-01",   "tables": "FTR-20260810-25331887-01",
    "discussion": "FTR-20260810-25331887-01","limitations": "FTR-20260810-25331887-01",
    "references": "FTR-20260810-25331887-01",
    "supplementary": "FTR-20260909-25331887-02"
  },
  "outputs": ["disease-models/wwox/registries/coverage_report.md"],
  "evidence_basis": ["the two parent receipts named above; no new reading"],
  "prior_receipt": "FTR-20260909-25331887-02",
  "reread_reason": "study_coverage_rollup"
}
```

**`coverage_provenance` is the load-bearing field, not `coverage`.** Every section names the
parent that asserted it, and a rollup is refused if any section names a parent that did not
declare that value. That turns "asserts nothing its parents did not" from an intention into a
check: the union cannot contain a section no event read, because there would be no parent to
name.

### 🔴 Measured impact — and the measurement found the trap first

```bash
python3 framework/scripts/legend_lint.py .   # unaffected; the measurement is the script below
```

The script is committed beside this document as
[`measure_4_1.py`](measure_4_1.py); run it from the repository root:

```bash
python3 framework/protocols/proposals/measure_4_1.py
```

| quantity | measured 2026-09-09 |
|---|---:|
| studies with at least one active receipt | 96 |
| studies whose union qualifies as complete, **parents restricted to real full-text readings** | **2** — `25331887`, `34268881` |
| receipts those rollups would cite as parents | 6 |
| **existing receipts whose meaning changes** | **0** |
| **existing manifests whose meaning changes** | **0** |
| studies whose union qualifies under the *naive* predicate | **4** |

Zero is not an optimistic reading of the design; it is what "additive" means here. No existing
record is rewritten, no `evidence_depth` is recomputed, no coverage map is edited. The two
`partial` receipts on `25331887` go on saying exactly what their authors wrote: *this event
read these sections*. The rollup says something their authors never said and never could —
*the union of these two events is complete* — and it says it in a record of its own.

🔴 **The gap between 4 and 2 is the finding, and my first predicate landed on 4.** I wrote the
obvious rule — *no section is `not_read`, and at least one is `read`*, which is verbatim the
predicate `validate_receipt` already enforces for `complete_fulltext_read` — and it promoted
**two abstract-only receipts** to complete:

```json
{
  "event_id": "FTR-20260726-20067585-01",
  "evidence_depth": "abstract_only",
  "coverage": {
    "abstract": "read",        "introduction": "unavailable", "methods": "unavailable",
    "results": "unavailable",  "figures": "unavailable",      "tables": "unavailable",
    "discussion": "unavailable","limitations": "unavailable", "references": "unavailable",
    "supplementary": "unavailable"
  }
}
```

Nothing is `not_read`; `abstract` is `read`. It satisfies the complete-read coverage predicate
exactly, and nobody opened the body. `29808465` is the same shape.

**The reason today's writer never trips on this is that `evidence_depth` is AUTHORED, and the
coverage map only constrains it.** The predicate is a *veto* over a human claim, never a
derivation of one. A rollup has no author to veto, so re-using the predicate as a derivation
inverts what it was built to do. Hence the extra condition, which is not decoration:

> **A rollup may cite only parents whose own `evidence_depth` is `partial_fulltext_read` or
> deeper, and every `read` section in the union must be attributed to such a parent.**

With that condition the count is 2, matching the review. Without it, 4 — and two of them
would be false complete reads manufactured out of `unavailable`.

### Compatibility strategy

| concern | how old records keep meaning what they meant |
|---|---|
| an old `partial` receipt | never touched. Append-only forbids it, and the design does not want it: `partial` on `FTR-20260810-25331887-01` continues to mean *this reading did not have the supplement*, which is true and stays true |
| an old **complete** receipt | unaffected; a study already at complete gets no rollup (the measurement skips it) |
| a consumer that does not know rollups | sees a record whose `evidence_depth` is `complete_fulltext_read` under a `record_kind` it does not recognise. **This is the one real migration cost** and it must be paid deliberately: `receipt_depth_index` and `active_receipts` decide what counts, and both would need the new kind added explicitly. A consumer that filtered on `record_kind == "contemporaneous_receipt"` keeps its old, narrower answer rather than silently gaining a new one |
| a parent later invalidated or identity-corrected | **the rollup must fall with it.** A rollup rests entirely on its parents; if one is superseded the union is no longer evidenced. The rule to enforce: a rollup naming a superseded parent is itself inactive, and `validate_ledger_sequence` reports it. Without this the rollup becomes the one record in the ledger that can outlive its own evidence |
| the registry / `BATCH_COMMIT` | a rollup is a receipt-ledger fact. Whether it may satisfy the registry's `full text reviewed` declaration — and so the `UNBACKED_FULLTEXT_DECLARATION` ratchet — is **a second operator decision**, not a consequence of the first. Recorded here rather than assumed |

### The regression the review specifies, restated as three fixtures

1. two receipts whose maps union to complete → rollup validates as `complete`;
2. a union with a surviving gap → rollup must be `partial`, and **must fail if it says
   `complete`**;
3. a rollup declaring a section absent from **both** parents → refused.

Plus two this measurement earned:

4. a rollup whose only parents are `abstract_only` → refused, however clean its coverage map;
5. a rollup whose parent is later invalidated → the rollup stops being active.

---

## 2 · Coupled panel relations on adjudicated locators (review §4.3)

### The problem, in one sentence

Under rule 5e an adjudicated text locator carries `surface: figure`, and the coupled-relation
marker belongs on the figure entry — so relations are undeclarable **exactly in the papers
whose surface is worst**, which are the papers where adjudication is needed most.

### The exact mechanism

`deepdive_manifest.py:1261` refuses a coupling whose **target** is not a text surface:

```python
elif entries[target].get("surface") not in TEXT_SURFACES:   # {"body", "table", "supplement"}
```

That check is right for what it was written against: *what a panel contradicts is something the
text said*. But rule 5e makes an adjudicated **text** quotation declare `surface: figure`,
because it is verified against a rendered page crop rather than against a character stream. The
sentence is therefore text, and its `surface` says `figure`, and the pointer refuses it.

`surface` is now carrying two incompatible jobs: *what kind of artifact the quote was verified
against* (an image) and *what kind of thing the quote is* (running text). Only the first was
ever its job, and rule 5e is what made the two come apart.

### Before — the real case, `PMID16223882`, entries `[1]` and `[15]`

```json
{
  "proposition": "The Results assert that tumour growth was COMPLETELY suppressed in the Ad-WWOX H460 arm - a categorical claim that neither Figure 5A nor Table 1 supports.",
  "snippet": "tumor growth was completely suppressed in mice inoculated with Ad-WWOX-infected H460 cells",
  "surface": "figure",
  "artifact": "disease-models/wwox/research/page_adjudications/PMID16223882/p04_h460_completely_suppressed.png",
  "page_anchor": { "page": 5, "dpi": 400, "needle": "suppressed in mice inoculated with Ad-WWOX-infected H460", "image_sha256": "3551246009278662501b9c9f8d644c1b063cf1ceddfaf97935c67e2c7b306f18" },
  "panel_text_relation": "panel_only",
  "note": "An ADJUDICATED TEXT locator. `panel_only` is the least-wrong admitted value and it is not right: the crop is a rendering of the running text, not a panel."
}
```

```json
{
  "surface": "figure",
  "panel_text_relation": "panel_only",
  "note": "This is the panel that bears on entries[1]. The coupled relation text_contradicted_by_panel cannot be declared, because entries[1] is an ADJUDICATED text locator and therefore carries surface 'figure', which the validator refuses as a coupling target. The relation is stated here and argued in the dossier instead."
}
```

**A genuine contradiction, found by a reader, present in the manifest as prose, and absent from
every field a command can query.** `scientist-c` had three of these on this paper and could
declare none.

### After — one authored field, and `surface` keeps its old job

```json
{
  "surface": "figure",
  "adjudicated_surface": "text",
  "page_anchor": { "page": 5, "dpi": 400, "needle": "suppressed in mice inoculated with Ad-WWOX-infected H460", "image_sha256": "3551246009278662501b9c9f8d644c1b063cf1ceddfaf97935c67e2c7b306f18" },
  "panel_text_relation": "text_only"
}
```

```json
{
  "surface": "figure",
  "adjudicated_surface": "figure",
  "panel_text_relation": "text_contradicted_by_panel",
  "contradicts": "entries[1]",
  "contradicts_needle": "completely suppressed"
}
```

The coupling-target rule becomes:

```python
target_entry = entries[target]
is_text = (target_entry.get("surface") in TEXT_SURFACES
           or ("page_anchor" in target_entry
               and target_entry.get("adjudicated_surface") == "text"))
```

🔴 **`adjudicated_surface` must be AUTHORED and must never be inferred**, and that is the entire
design. Nothing in the JSON distinguishes a crop of a paragraph from a crop of a blot — both are
a rectangle of pixels with a SHA-256. Only the reader who drew the crop knows which it is.
Inferring it (from the needle looking sentence-like, from crop aspect ratio, from the caption)
would be the shape this repository keeps catching in itself: *a plausible predicate that answers
a different question from the one you asked*, and it would answer it invisibly, because the
result would be well-formed either way.

**Why a new `surface` value (`page_adjudicated_text`) is the weaker option.** It is fewer
concepts, and it is the review's own first suggestion — but it overloads the field that is
already overloaded, and it makes an adjudicated table crop and an adjudicated figure crop need
their own values too. A separate axis says the true thing once: `surface` is *what I verified
against*, `adjudicated_surface` is *what the crop shows*.

### 🔴 Measured impact

Run from the repository root:

```bash
python3 framework/protocols/proposals/measure_4_3.py
```

| quantity | measured 2026-09-09 |
|---|---:|
| manifests scanned | 80 |
| locator entries | 1458 |
| coupled-relation locators | **131** — 130 on `figure`, 1 on `body` |
| page-adjudicated locators (carrying `page_anchor`) | **74**, across **6** manifests |
| ...of which declare `surface: figure` | **74 — all of them** |
| ...that self-declare "ADJUDICATED TEXT" in their note | **17** (12 on `16223882`, 5 on `28373548`) |
| page-adjudicated locators carrying a coupled relation today | **0** |
| **existing locators whose meaning changes** | **0** |
| **existing receipts whose meaning changes** | **0** |
| existing manifests that would become *editable* to gain the field | 6 (an operator decision — see below) |

The collision as a single number: on the `figure` surface there are now **74 page crops and
421 direct panel readings**, and `surface` says `figure` for both. How many of the 74 show
running text rather than a panel is **not derivable from the manifests at all** — the 17 above
are only those whose author wrote it in a `note`, which is a lower bound and not a measurement.
That is not a gap in this audit; it is the thing the proposal exists to fix. That
ratio is what makes the current rule unenforceable rather than merely inconvenient — and it is
why open item 4 of the protocol ("a rule stated in a comment, enforced by nothing") **cannot be
enforced as written** until this is decided. Turning that comment into a check today would
refuse 74 legitimate locators.

🔴 **The count that is NOT a measure of the harm.** `0` relations on adjudicated locators does
not mean no relation was lost — it is the count of relations that could be *recorded*, and the
mechanism under discussion is precisely what stops them being recorded. The three on `16223882`
are known only because their reader wrote prose about them in a `note`. A reader who hit the
same wall and moved on leaves nothing for any query to find. **The measurable quantity and the
quantity of interest are different, and only the first is in the table.**

### Compatibility strategy

| concern | how old records keep meaning what they meant |
|---|---|
| the 74 existing adjudicated locators | keep `surface: figure` and gain nothing. Absent `adjudicated_surface` they remain **not** valid coupling targets — exactly their status today. The field is **required on new locators only**; absence keeps the old, stricter answer |
| the 131 existing coupled locators | untouched. The pointer rule only *widens* what may be pointed AT; nothing that validates today stops validating |
| the 1 coupled locator on `body` (`PMID23435430` `entries[9]`) | unchanged, and still the incompletely modelled case open item 4 describes. This proposal does not resolve it and must not be read as doing so |
| a validator that does not know the field | `additionalProperties` on the manifest schema decides this. If it is closed, the field must be added there in the same change or every new manifest fails |
| the 3 undeclared relations on `16223882` | 🔴 **left undeclared.** They can only be recorded by editing a manifest whose receipt is already persisted and hash-chained — which is a second question, and the wrong one to answer as a side effect of a vocabulary change. The honest position: the schema stops *creating* this debt; whether the existing debt is repaid by a manifest revision, and under what attestation, is the operator's call |

### The regression the review specifies

1. an adjudicated text locator declaring `adjudicated_surface: "text"` may be a coupling target
   and passes strict validation;
2. the existing rule stays red: a coupled relation pointing at a **non**-adjudicated `figure`
   entry is still refused;
3. an adjudicated locator with `adjudicated_surface: "figure"` is **not** a valid coupling
   target — a crop of a blot is not a sentence, and this is the mirror of (1) that stops the
   field being a blanket exemption;
4. a locator carrying `page_anchor` and no `adjudicated_surface` behaves exactly as it does
   today — the fixture that proves no old record was reinterpreted.

---

## What I am asking for

| | decision | if yes |
|---|---|---|
| §4.1 | may a rollup record assert study-level completeness its parents did not individually claim? | implement `study_coverage_rollup` with `coverage_provenance`, the parent-depth floor, and the fall-with-parents rule; 2 studies gain a rollup, 0 records change |
| §4.1b | may a rollup satisfy the registry's `full text reviewed` declaration? | separate answer needed; it moves the `UNBACKED_FULLTEXT_DECLARATION` ratchet |
| §4.3 | may `surface` stop being the sole discriminator, with an authored `adjudicated_surface` beside it? | implement the widened coupling-target rule; 0 records change, and open item 4 becomes enforceable |
| §4.3b | may the 6 manifests already carrying adjudicated text be revised by their authors to gain the field? | the 3 known relations on `16223882` become declarable; otherwise they stay prose |
