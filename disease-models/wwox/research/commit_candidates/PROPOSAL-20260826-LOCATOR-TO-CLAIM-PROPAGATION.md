# Proposal — measuring the gap between what the repository has read and what its claims say

**Proposal ID:** PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION
**Date:** 2026-08-26
**Status:** proposal only. No gate is implemented here, and one of the four candidates is
**refused** rather than deferred.

---

## 1. The pattern, and the discriminator that makes it measurable

`EVIDENCE_ALREADY_CAPTURED → RELEVANT_CLAIM_EXISTS → CLAIM_DOES_NOT_REFLECT_EVIDENCE`.

🔴 **The pattern as stated is not yet a defect**, and treating it as one is the first mistake a
gate here would make. A reading captured *after* the last `BATCH_COMMIT` has had no lawful
opportunity to reach a claim: it is **queued**, not dropped. The discriminator is therefore
**time**, anchored to `last_batch_commit_date` — currently **2026-08-10** (`BATCH_20260810_005`).

Two live negative controls exist today and must never fire:
`FTR-20260811-18487609-01` (the heterozygote bone reading) and `FTR-20260814-15070730-01`
(the `CLAIM 023` provenance adjudication). Both are exactly this pattern. Both are legitimate.

---

## 2. Cases, from existing repository evidence only

No new literature was searched for this section.

### REAL — evidence pre-dates the last canonical write, no deferral declared

**Case 1 — the ECoG contradiction**
- `SOURCE_EVIDENCE`: continuous 24/7 ECoG, 7 days from P14, blinded, n = 5/group: SWDs
  ≈ 0.63/h in `Wwox`-null vs ≈ 0.02/h in WT, `**** p < 0.0001`, restored to `ns` vs WT by
  AAV9-hSynI-hWWOX.
- `LOCATOR`: `deepdive_manifests/PMID42422765.json` entry 4 (`gr7.jpg`, sha256 `3a01e962…`);
  the Methods and Figure 7 legend in `PMID42422765_Obeid2026_PMC.html`.
- `CLAIM_ID`: `CLAIM 037` (and `CLAIM 005`'s evidence boundary).
- `CURRENT_CLAIM_STATUS`: `in observation`, headline *"explicitly absent in Wwox-null mice"*.
- `EXPECTED_IMPACT`: **the headline is false**; a canonical prohibition built on it forbids a
  true statement.
- `PROPAGATION_FAILURE_TYPE`: 🔴 **none of the five offered labels fits.** The evidence *was*
  declared — `CLAIM 011`'s flag note says in writing that Figure 3B *"non risolve gli altri
  domini della claim (ECoG/SWD…)"* and defers them. Nothing was hidden. What happened is that a
  **second claim asserted the negation of a domain a first claim had explicitly deferred.**
  Proposed sixth label: **`CANONICAL_CROSS_CLAIM_CONTRADICTION`**.

**Case 2 — the glial sign**
- `SOURCE_EVIDENCE`: *"the expression level of Iba1 in cerebral cortices were significantly
  **lower** in lde/lde than in +/+ rats at the all ages examined"*, GFAP likewise; the authors
  state the discordance themselves.
- `LOCATOR`: `deepdive_manifests/PMID31340538.json` entries 5 and 8.
- `CLAIM_ID`: `CLAIM 005`, `CLAIM 006`, `meta_network_myelin_glia_current.md`.
- `CURRENT_CLAIM_STATUS`: `consolidated baseline`; the meta asserts *"gliosis as a downstream
  response"* as settled.
- `EXPECTED_IMPACT`: the P6 axis has evidence for both directions and states one.
- `PROPAGATION_FAILURE_TYPE`: **`CONTRADICTORY_EVIDENCE_NOT_PROPAGATED`.** The 2026-08-06 batch
  consumed this reading's **prenatal** half and left its **glial** half behind.

**Case 3 — the homozygous-Q230P cohort case**
- `SOURCE_EVIDENCE`: *"Case 23 is homozygous for Q230P"* — a missense/missense (`M/M`) patient at
  an allele the model records as abolishing the protein.
- `LOCATOR`: `deepdive_manifests/PMID40875931.json` entry 5.
- `CLAIM_ID`: `CLAIM 013`, `CLAIM 033`.
- `CURRENT_CLAIM_STATUS`: `in observation`. `CLAIM 013` records *"Q230P presente in 2 individui"*
  and names case 11 as `N/M`; neither claim records that the other is **homozygous**.
- `EXPECTED_IMPACT`: `CLAIM 033`'s reservation (1) — that the genotype class is syntactic, not
  functional — currently argues abstractly. Case 23 is a **concrete instance inside the very
  cohort**: a functionally null/null patient sitting in the mildest class.
- `PROPAGATION_FAILURE_TYPE`: **`QUALIFIER_NOT_PROPAGATED`.**

**Case 4 — the Olig2-Cre experiment**
- `SOURCE_EVIDENCE`: PMID 33914858 Fig. 1J–L — the oligodendroglial deletion exists and is free
  of gross, weight and survival phenotype to ~120 days.
- `LOCATOR`: **none.** The paper is unread (`FT-044` suspended); this session's evidence is a
  page-level adjudication that emits no locator.
- `CLAIM_ID`: `CLAIM 003`.
- `CURRENT_CLAIM_STATUS`: `consolidated baseline`, boundary asserting *"non promuovibile senza
  una delezione … Olig2/CNP-specific"*.
- `EXPECTED_IMPACT`: the claim's decisive experiment is misspecified; the correct one is ~10×
  cheaper.
- `PROPAGATION_FAILURE_TYPE`: **`NEGATIVE_EVIDENCE_NOT_PROPAGATED`**, with a caveat that matters
  for gate design: 🔴 **no receipt exists, so no receipt-driven gate can see this case.** The
  only machine-visible trace was in `paper_registry_current.md` all along — `PAPER 004`'s
  **published title**, which names a phenotype (`epilepsy`) that no linked claim carries.

**Case 5 — the declared depth of `PAPER 039`**
- `SOURCE_EVIDENCE`: two receipts, both `partial_fulltext_read`, the second explicitly declaring
  itself partial by intent.
- `LOCATOR`: `FTR-20260726-34268881-01`, `FTR-20260810-34268881-02`.
- `CLAIM_ID`: `CLAIM 002`, `CLAIM 030`, `CLAIM 032`.
- `CURRENT_CLAIM_STATUS`: all three rest on a record declaring `complete_fulltext_read`.
- `PROPAGATION_FAILURE_TYPE`: **`SOURCE_IDENTITY_NOT_PROPAGATED`** — the ledger moved and the
  declaration did not.

**Case 6 — paper→claim link asymmetry (17 instances)**
- `SOURCE_EVIDENCE`: 17 `**Claim links:**` entries in `paper_registry_current.md` naming a claim
  whose body references neither the paper number nor its PMID.
- `CLAIM_ID`: 009, 013, 019, 028 ×5, 029, 030, 031, 032 ×2, 007, 008 ×2, 038.
- `PROPAGATION_FAILURE_TYPE`: **`SOURCE_IDENTITY_NOT_PROPAGATED`**, and it is the only case class
  here that is **fully mechanical**.

### PENDING — post-batch, legitimately not yet propagated

| # | Evidence | Read | Claim | Type if it survives the next batch |
|---|---|---|---|---|
| 7 | `CLAIM 023` sourced to `CORPUS P206`, `Identifier: PENDING`, flagged as possibly identical to an abstract-only record reporting the **opposite** Tyr33 direction | 2026-08-14 | `CLAIM 023`, `consolidated baseline` | `UNRESOLVED_ADJUDICATION_NOT_PROPAGATED` |
| 8 | heterozygote bone μCT, `DL-META-097` | 2026-08-11 | `CLAIM 032` | `CONTRADICTORY_EVIDENCE_NOT_PROPAGATED` |
| 9 | Breton Table 1 heterozygote, S-CTL pooling | 2026-08-10 (batch day) | `CLAIM 032`, `CLAIM 021` | `QUALIFIER_NOT_PROPAGATED` |
| 10 | PMID 42397075, 30 locators, complete read | 2026-08-10 | `CLAIM 002` / `PAPER 001` | `SOURCE_IDENTITY_NOT_PROPAGATED` |
| 11 | PMID 42128308 entries 8, 9, 24 | 2026-08-10 | `CLAIM 030`, `CLAIM 003`, meta:92 | `QUALIFIER_NOT_PROPAGATED` |

**Counts: 11 cases · 6 real · 5 pending.** Cases 7 and 8 are the designated negative controls
for every gate below.

---

## 3. Gates proposed

### G1 — `BIDIRECTIONAL_CLAIM_LINK_GATE` — recommended, build first

- `INPUT`: each `## PAPER n` block's `**Claim links:**` field (**excluding**
  `**Claim links (corroborates):**`), plus the full body text of each `## CLAIM c` block.
- `RELATION`: every supports-link (PAPER n → CLAIM c) must be mirrored by a reference to
  `PAPER n` **or** to that paper's PMID somewhere in the claim's body.
- `FAIL_CONDITION`: neither reference present → `WARN_BUT_PROCEED`, listing the pair.
- `NEGATIVE_CONTROL`: (i) `PAPER 029`'s **8** `corroborates` links must not fire — a review that
  corroborates a claim need not be cited by it; (ii) `PAPER 027 → CLAIM 029` and
  `PAPER 057/058 → CLAIM 005` must not fire, because those claims cite by PMID. Both controls
  were run: the raw count **28** falls to **20** when `corroborates` is excluded and to **17**
  when PMID references are accepted.
- `FALSE_POSITIVE_RISK`: **low, and measured** — 11 of 28 candidate firings were eliminated by
  refining the relation, and each elimination was a real distinction, not a threshold tweak.
  Residual risk: a claim citing a paper by author-year only. Mitigation: accept a short-title
  match as a third form of reference, or accept the residual as `INFO`.
- **Live count today: 17.**

### G2 — `DECLARED_DEPTH_vs_LEDGER_GATE` — recommended

- `INPUT`: each PAPER record's `Evidence depth` string; the maximum receipt depth in
  `fulltext_read_receipts.jsonl` for that record's identifier.
- `RELATION`: a record may declare `complete_fulltext_read` / `full text reviewed` only if a
  receipt of that depth exists for its identifier.
- `FAIL_CONDITION`: declared depth exceeds ledger depth → `BLOCK_BATCH_COMMIT` if any
  `consolidated baseline` claim links the record, else `WARN_BUT_PROCEED`.
- `NEGATIVE_CONTROL`: the **20** historical `full text reviewed` registry declarations already
  tracked by the registry-declaration ratchet must be routed through that ratchet and **not**
  re-flagged here — otherwise the gate re-reports a debt the system already counts, which is the
  duplicated-guard failure CLAUDE.md names. `PAPER 060` (PMID 37519886, `DISCOVERY_ONLY`, no
  claim link) must not fire.
- `FALSE_POSITIVE_RISK`: **low** — string-to-string against an append-only ledger, no semantics.
  The real risk is *duplication* of an existing ratchet, not a wrong verdict.
- **Live count today: at least 1 (`PAPER 039`), pending a full sweep.**

### G3 — `PRE_BATCH_READING_DECLARATION_GATE` — recommended as `WARN` only

- `INPUT`: every receipt whose `analysis_at` is strictly earlier than `last_batch_commit_date`
  in the state manifest, joined to the PAPER record for its identifier.
- `RELATION`: each such reading must be **named** by at least one of — (a) a claim body,
  (b) the paper record's evidence-depth line, (c) an explicit deferral in
  `full_text_queue_current.md` or `dismissal_ledger_current.md`, (d) that batch's `*_scope`
  field in the state manifest.
- `FAIL_CONDITION`: named by none of (a)–(d) → `WARN_BUT_PROCEED`. **Never `BLOCK`.**
- `NEGATIVE_CONTROL`: `FTR-20260811-18487609-01` and `FTR-20260814-15070730-01` — both post-batch,
  both must be silent. Plus `PAPER 060`, read and deliberately linked to no claim, which passes
  via (b).
- `FALSE_POSITIVE_RISK`: **moderate and bounded by what it checks.** It detects **silence, not
  disagreement**: a reading that legitimately changed nothing passes by saying so in one line.
  It cannot see Case 4, which has no receipt.

### G4 — `EVIDENCE_CONTRADICTS_CLAIM` — 🔴 **REFUSED, not deferred**

The tempting gate is one that reads a locator proposition and a claim's text and decides whether
the claim reflects the evidence. **It is refused**, because it cannot distinguish these three:

| | Case | Correct verdict |
|---|---|---|
| a | Obeid's SWD data against `CLAIM 037`'s *"explicitly absent"* | **defect** |
| b | Tochigi's reduced GFAP against Hussain's increased GFAP | **possibly a real species/region dissociation** — a contradiction to record, not a claim to fix |
| c | `DL-META-097`'s heterozygote bone data, deliberately declared `ESPANSIONE` and deliberately not transferred to humans | **correct behaviour** |

(a), (b) and (c) are lexically indistinguishable — each is "a locator says X, a claim does not say
X" — and only (c) carries an explicit marker. A gate firing on all three teaches reviewers to
dismiss it, and CLAUDE.md's own rule then applies: a control that is noise at scale is a future
alarm nobody hears. **Do not build it.**

**What replaces it is a person, on a schedule the machine sets.** G3 mechanically produces the
list of pre-batch readings; the integrator writes **one line each** — `propagated` /
`deferred, because…` / `no canonical effect` — as a required step of `BATCH_COMMIT`. The machine
supplies completeness; the human supplies judgement. That division is the only one that survives
the three-way distinction above.

---

## 4. One further mechanical check, cheap and orthogonal

**`SOURCE_TITLE_PHENOTYPE_COVERAGE` (`INFO` only).** For each PAPER record, extract phenotype
terms from its **published title** (`epilepsy`, `seizure`, `ataxia`, `degeneration`,
`lethality`, `myelin`, …) and report any term appearing in **no** claim linked to that record.
- Live examples: `PAPER 004` — *"…causes **epilepsy** and myelin defects"* → `CLAIM 003` carries
  only myelination; `CORPUS-STUB-053` — *"…induces **epilepsy**, progressive neuroinflammation,
  and **cerebellar degeneration**"* → no claim carries either.
- `FALSE_POSITIVE_RISK`: **high by design**, which is why it is `INFO`. A paper's title routinely
  names things a claim legitimately does not cover. Its value is not the verdict but the
  **list**: it is the only check in this proposal that would have caught Case 4, the one with no
  receipt and no locator.
- 🔴 It also depends on the title being right — which `PAPER 007` and `PAPER 027` show it is not
  always. Chain it behind a `TITLE_FIDELITY` check against the corpus seed, or it inherits the
  defect it is meant to surface.

---

## 5. What this proposal asks for

1. Build **G1** — highest ratio of defects found to risk taken, and fully mechanical.
2. Build **G2**, wired **into** the existing registry-declaration ratchet, not beside it.
3. Build **G3** as `WARN`, and make its output a required, hand-annotated step of `BATCH_COMMIT`.
4. Add **`CANONICAL_CROSS_CLAIM_CONTRADICTION`** to the failure taxonomy — Case 1 fits none of
   the five existing labels, and it is the most consequential case in this list.
5. Do **not** build G4.
