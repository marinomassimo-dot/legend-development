# OPERATOR DECISION PACKET — remote passages and the receipt schema

**Date:** 2026-09-23 · **Prepared by:** Orchestrator · **Status:** 🔴 **DECISION ONLY. NOTHING BUILT.**

> 🔴 **No schema migration. No implementation. No new receipt type. No governance expansion.**
> `framework/protocols/fulltext_read_receipt.md` was **not edited**. `fulltext_receipts.py record` was
> **not run**. No fixture, validator, field or ledger entry was created.
> 🔴 Nothing here is medical advice. 🔵 Public edition.

**Scope.** One question, four options, one recommendation. It is deliberately the shortest packet in
this repository.

---

## § 1 · PROBLEM

On 2026-09-22 a source recorded for months as unretrievable (`PMID 19500159`) was retrieved through
`mcp__Scholar_Gateway__semanticSearch` at **13 of 18 chunks**, including Results text and a figure
legend. Three more followed. The route is **measurably publisher-bound**: Wiley-hosted 4/4, everything
else 0/25 (`retrieval_capability_retest_20260922.md` § 3).

These passages are **scientifically useful now** — they locate exact primary clauses, they adjudicate
sibling claims, and one of them supplied a human comparator for `CLAIM 039`. The repository is
currently using them, correctly, as `REMOTE PASSAGE — ANALYSIS-VALID / CANONICALIZATION PENDING`.

🎯 **The question is narrow: can the existing receipt contract represent such a retrieval faithfully,
and if not, what is the smallest honest fix?**

### 1.1 What the existing schema ALREADY handles — and it is more than expected

Read directly from `framework/protocols/fulltext_read_receipt.md`:

| Need | Existing field | Verdict |
|---|---|---|
| A depth that is **not** a full read | `evidence_depth: queried_not_full_read` — *"Indexed/RAG-searched or selected passages inspected"*, `counts as full text analysed: No` | 🟢 **Exact fit. It was written for this.** |
| A remote source | `source_kind: fulltext_remote` | 🟢 Fits |
| No local bytes to hash | *"Remote locators … have nothing to hash and stay `null` for partial/legacy events"* | 🟢 **Already permitted.** The fingerprint rule is **not** the blocker it was assumed to be |
| Which sections were seen | `coverage: {abstract, introduction, methods, results, figures, tables, discussion, limitations, supplementary}` | 🟡 Fits approximately — see § 1.2 |

🔴 **Correction to the standing framing, and it should be made before anything is built:** the
obstacle was described as *"not representable under current fingerprint assumptions."* That is
**wrong**. `source_fingerprint: null` is explicitly lawful for a remote locator on a non-complete
receipt, and `queried_not_full_read` exists precisely for RAG-retrieved passages. **A conforming
receipt for a Scholar Gateway retrieval can be written today with zero schema change.**

### 1.2 What it genuinely CANNOT represent — three things, and only three

| # | Gap | Why it matters |
|---|---|---|
| **G1** | **The retrieval is not reproducible and nothing records that.** A semantic query returns a chunk set that depends on the query string, `topN`, and the provider's corpus version. Re-running the same query later may return a different set. `source_locator` is free text and holds none of this | A receipt's purpose is *"I read **this**"*. Without the query and the corpus version, a later reader cannot tell what was read |
| **G2** | **No chunk denominator.** The provider returns `total_chunks` per article; the repository's own routing guidance already says *"report the chunk set you obtained"* — but there is **no field to report it into** | `13 of 18` and `6 of 6` are different epistemic objects. Both currently collapse to `queried_not_full_read` |
| **G3** | **`coverage` assumes sections; a chunk set is not sectioned.** A returned chunk may straddle Results and a figure legend, and the provider does not label sections | Marking `results: read` from a chunk that touched Results overstates; marking it `not_read` understates |

🔴 **G1 is the only one that bears on trust.** G2 and G3 are precision losses, not fidelity failures.

---

## § 2 · MINIMAL OPTION — a bounded remote-passage receipt

**Not a new record kind. Not a new depth. One optional block on the existing receipt**, populated only
when `source_kind: fulltext_remote` **and** `evidence_depth: queried_not_full_read`:

```yaml
remote_retrieval:            # optional; omitted entirely for every other receipt
  provider: scholar_gateway
  queries: ["<query_as_executed>", ...]   # verbatim, as the provider echoes them
  chunks_obtained: 13
  chunks_total: 18            # null if the provider does not declare it
  provider_corpus_version: "2026-09"      # as declared by the provider, verbatim
  retrieved_at: 2026-09-22T00:00:00Z      # the provider's own timestamp
```

**That is the whole proposal.** Five fields and a provider name.

### 2.1 REQUIRED FIELDS — and why each one is genuinely needed

| Field | Needed because | Dropped if… |
|---|---|---|
| `provider` | Route-specific reproducibility differs per provider; a bare "remote" is not actionable | never — it is one string |
| `queries` | 🎯 **The single load-bearing field.** It is the only thing that makes the retrieval repeatable **at all**, and it closes `G1` by itself | never |
| `chunks_obtained` / `chunks_total` | Closes `G2`; distinguishes a complete narrative from one paragraph | acceptable to drop `chunks_total` when the provider omits it |
| `provider_corpus_version` | A remote corpus is mutable. Without it, *"the same query returns nothing"* is uninterpretable | 🟡 **droppable** if the Operator judges the timestamp sufficient |
| `retrieved_at` | The provider stamps it; it costs nothing and bounds the corpus version | 🟡 droppable if `provider_corpus_version` is kept |

🔴 **Explicitly NOT proposed:** no new `evidence_depth` value; no new `record_kind`; no new
`source_kind`; no change to `source_fingerprint`; no chunk-text storage; no per-chunk locator; no
change to `coverage`; no validator change beyond accepting an optional block; **no promotion path.**
A `queried_not_full_read` receipt still does **not** count as full text analysed, and `G3` is left
**unsolved on purpose** — the honest handling of an unsectioned chunk set is to leave `coverage`
conservative, not to invent a field for it.

---

## § 3 · RISKS — what cannot be guaranteed compared with local full text

1. 🔴 **Irreproducibility remains, it is only now documented.** The remote corpus can change or
   withdraw an article. A receipt with `queries` lets a future reader *try*; it does not let them
   *succeed*. This is the irreducible difference from a hashed local artefact.
2. 🔴 **No integrity guarantee.** There is no digest. A passage cannot be shown to be unaltered
   between retrieval and quotation. A local PDF with a SHA-256 can.
3. 🔴 **Selection bias is invisible.** A semantic query returns what it judges relevant. A paper's
   most important sentence may never be served and nothing in the receipt would show it. **This is why
   the depth must stay `queried_not_full_read` whatever else is decided.**
4. 🔴 **Extractor damage is silent.** The route strips italics and some comparators (`lde/lde` →
   `*lde/lde*`, `P < 0.05` losing its operator). Same class as the PMC route's defects, already
   documented; not made worse by this proposal, and not fixed by it.
5. 🟡 **Schema creep.** Every optional block is a future maintenance surface and a future
   "why is this null here" question. Five fields is small; it is not zero.
6. 🟡 **A second-order risk worth naming:** once a receipt exists for a passage, the temptation to
   treat it as a read grows, because a receipt *looks* like a read. The mitigation is entirely in the
   depth field, which is a word, not a gate.

---

## § 4 · ALTERNATIVE — keep passages analysis-only, permanently

**Change nothing. Never write a receipt for a remote passage. Keep using them for discovery,
hypothesis generation, analysis, locating primary clauses and adversarial verification, and keep every
such passage classified `REMOTE PASSAGE — ANALYSIS-VALID / CANONICALIZATION PENDING`.**

| | Minimal option (§ 2) | Alternative (§ 4) |
|---|---|---|
| Schema surface added | 5 optional fields | **none** |
| `G1` closed | 🟢 yes | 🔴 no |
| Passage becomes canonical evidence | 🔴 **no, under either** | 🔴 no |
| Retrieval traceable to a named query | 🟢 yes | 🟡 only in prose analysis files, which is where it is today |
| Risk of a passage being mistaken for a read | 🟡 **higher** — a receipt looks like a read | 🟢 lower |
| Cost if later reversed | 🟡 an optional block to deprecate | 🟢 nothing |

🎯 **The honest case for the alternative:** the passages are **already** traceable — every one of them
is quoted in a dated analysis file that names the query, the chunk count and the provider. The receipt
ledger would add a hash chain over a claim it cannot verify. **Analysis files are the right home for
irreproducible evidence; the ledger is the right home for reproducible evidence.**

---

## § 5 · RECOMMENDATION

🟡 **ACCEPT THE ALTERNATIVE (§ 4) FOR NOW, with one non-schema act.**

Three reasons, in order of weight:

1. 🎯 **The premise that forced this question is false.** § 1.1 shows the existing schema already
   admits a conforming receipt for a remote passage. There is no blocking defect — so the decision is
   *whether we want these in the ledger*, not *whether we can put them there*. That is a much lower-stakes
   question and it does not need to be answered today.
2. **Volume does not justify a schema surface.** Four papers have been recovered by this route, all
   Wiley-hosted, and the rule predicts the reachable set is small. Five fields for four rows is a poor
   trade until the set grows.
3. **The one real gap, `G1`, is already closed in prose.** Every recovered passage is quoted in a dated
   analysis file naming the query and the chunk count.

**The non-schema act, and it is the only thing this packet asks for:** adopt the **routing rule** already
drafted at `retrieval_capability_retest_20260922.md` § 7 into `framework/scripts/README.md`. It is a
four-step ladder that saves an acquisition act per non-Wiley blocked paper, it changes no schema, and it
is independent of everything above. 🔴 **It was NOT adopted by me** — `README.md` is untouched.

**`REVIVAL_TRIGGER` for reopening § 2:** the recovered-passage set exceeds **~15 papers**, **or** a
passage becomes load-bearing for a `consolidated baseline` claim, **or** a second provider appears
(at which point `provider` stops being a constant and the block starts earning its cost).

---

## § 6 · WHAT THIS PACKET DOES NOT DECIDE

- 🔴 Whether the four already-recovered passages may be canonicalised. **They may not**, under both
  options, and no request to do so is made.
- 🔴 The two stale append-only "unread" markings (`discovery_ledger_current.md:1652`,
  `full_text_queue_current.md:4910`). **A separate, unrelated Operator decision.** Not hand-edited.
- 🔴 The four proposed receipt payloads at `retrieval_capability_retest_20260922.md` § 6. They remain
  proposals; under § 5 they stay unwritten.
