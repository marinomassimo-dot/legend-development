# COMMIT CANDIDATE — CC-20260922-CLAIM005-CHAIN-NAMING-01

**Source:** Orchestrator, verifying Scientist A's Wave 7 hand-back before landing it
([`wave7_verification_mallaret_chain_20260922.md`](../../analysis/wave7_verification_mallaret_chain_20260922.md) §1–§2).
**Trigger:** a delegate reported `CLAIM 003` as containing a false statement. The statement is in
`CLAIM 005`, and it is **true** — but the misreading was reproducible from the claim text alone,
and chasing it opened a live contradiction the repository had already met once and explained away.
**Change class:** **MINOR** on the naming repair; **MINOR but consequential** on the conflict flag —
one `REVIVAL_TRIGGER` added to two claims, no claim reversed, no status moved, no prohibition lifted.
**Target:** `working_model_version` MINOR bump at batch time. **No `BLOCCO 1` change. No therapeutic
recommendation.**
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3.** `CLAIM 005` and `CLAIM 037` are both `consolidated baseline`, and §2 below
touches the one sentence in this repository that is written as a **prohibition on future canonical
text**. It is not weakened here — it is given its counter-evidence.
**Proposes:** `D-25` — *"a chain whose links are named in the batch log and not in the claim is a
chain the reader will reassemble wrongly."* (`D-17` remains **reserved — operator-deferred**.)

---

## 1 · The naming repair — why a correct sentence still needs fixing

`claim_registry_current.md:116`, inside `CLAIM 005`, reads:

> *"Early death and epileptogenesis were attributed here to PMID 19936220 and Mallaret 2014.
> **All three links of that chain have since been read in full.**"*

The sentence is **true**. The three links are named in `working_model_current.md:260`
(`BATCH_20260806_002`): **PAPER 057** (PMID 19936220), **PAPER 058** (PMID 19500159), **PAPER 059**
(PMID 17803050). Ledger check:

| PMID | receipt | `record_kind` | `evidence_depth` |
|---|---|---|---|
| 19936220 | `FTR-20260806-19936220-01` | `contemporaneous_receipt` | `complete_fulltext_read` |
| 19500159 | `FTR-20260806-19500159-01` | `contemporaneous_receipt` | `complete_fulltext_read` |
| 17803050 | `FTR-20260806-17803050-01` | `contemporaneous_receipt` | `complete_fulltext_read` |

**Three of three.**

🔴 **But the claim block names only two of them** (`19936220`, `19500159`) and never names
`17803050` — while the sentence immediately *before* "all three links" names `19936220` **and
Mallaret 2014**. A reader holding only the claim assembles the triple
`{19936220, Mallaret 2014, 19500159}`, finds Mallaret at `partial_fulltext_read` /
`legacy_reconstruction`, and concludes the claim is lying. That is precisely what happened, to a
competent reader, today.

**Proposed edit — `CLAIM 005`, evidence boundary.** Replace:

> *"All three links of that chain have since been read in full."*

with:

> *"All three links of that chain — PMID 19936220 (`PAPER 057`), PMID 19500159 (`PAPER 058`) and
> its terminus PMID 17803050 (`PAPER 059`) — have since been read in full, with persisted receipts.
> ⚠️ **Mallaret 2014 (PMID 24369382), co-attributed in the same sentence, is not one of those links
> and has never been read in full** (`FTR-20260726-24369382-01`, `legacy_reconstruction`); see the
> conflict recorded below."*

Cost: one sentence. It removes a reproducible misreading of a baseline claim and makes the claim
self-sufficient — a reader no longer has to hold a batch log from a different file open to check it.

---

## 2 · 🔴 The conflict the chase uncovered — and why it is not a reversal

According to PubMed, **PMID 24369382** ([DOI](https://doi.org/10.1093/brain/awt338) — Mallaret M,
Synofzik M, Lee J, … **Aldaz CM**, Koenig M, *Brain* 2014;137(Pt 2):411–9) states in its abstract:

> *"Moreover, **we observed** that the short-lived Wwox knock-out mouse display spontaneous and
> audiogenic seizures, a phenotype previously observed in the spontaneous Wwox mutant rat presenting
> with ataxia and epilepsy…"*

**`we observed`** — a first-person observation claim about the mouse null, in a paper co-authored by
**the investigator whose laboratory produced that mouse**.

This is the direct negation of the source the prohibition rests on. PMID 19500159 states three
times, plus a Table 2 whose `Epilepsy` row is empty for both mouse models, that Wwox-null mice show
no epilepsy. On that basis `CLAIM 005` concludes: *"No canonical statement may describe a Wwox-null
mouse as showing epileptogenesis."* `CLAIM 037`'s evidence boundary records the same and **does not
mention Mallaret at all**.

### 2a · The repository had already met this and got it wrong

`fulltext_dossiers/PMID30370248.md` — a **completed full-text read** — caught a review asserting
mouse seizures and diagnosed it as a miscitation:

> *"Reference 53 is not a mouse experiment: it is the human SCAR12 paper. … the sentence points to
> the wrong species and source."*

🔴 **The premise is true and the conclusion does not follow.** Reference 53 *is* the human SCAR12
paper, and that paper reports a mouse observation in its own abstract. The review's citation is
**faithful**; it inherited the claim from Mallaret. Establishing that a reference is a human
genetics paper is **not** establishing that no mouse observation stands behind the sentence. An
append-only correction has been written into that dossier.

### 2b · The body is paywalled, and that is a measurement, not an assumption

`get_copyright_status(["24369382"])` → `checked_sources: ["pubmed","pmc"]` (PMC **was** consulted),
`license.is_open_access: false`, *"© The Author (2013) … All rights reserved."*, `PMC3914474` present
as a deposit. **A PMCID is not a body** — fifth instance this session, and the first whose cause is
licensing rather than an empty stub.

⚠️ **This is a paywall, not a route failure.** The distinction is load-bearing and this session has
now drawn it in both directions: PMID 36779245's Table S1 was open access and unreachable → a route
problem. This is reachable-in-principle and not licensed → a human acquisition. Per §27, a tool or
access boundary is not a scientific `HUMAN_REQUIRED` stop; the science around it proceeds.

### 2c · Proposed addition to `CLAIM 005` and `CLAIM 037` — evidence boundary

> ⚠️ **Contested, and the contesting evidence is unread.** PMID 24369382 (Mallaret 2014, *Brain*,
> **Aldaz co-author** — the knockout mouse's own laboratory) asserts in its abstract, first-person,
> that *"the short-lived Wwox knock-out mouse display spontaneous and audiogenic seizures."* Its body
> is **paywalled and has never been read** (`legacy_reconstruction`), so the assertion is at
> abstract depth and **is not promoted** — the `LIT-0405` precedent governs, where *"decreased
> plasma GH"* was refused as a reading and the body reported it as not significant. **The
> prohibition stands.** What is recorded is that it is opposed, by a first-hand claim from the
> model's originators, and that the opposition has never been examined.
> `REVIVAL_TRIGGER`: **acquisition of PMID 24369382's body.**

🔵 **And the question sharpens.** Suzuki's own escape hatch is that the mice may die before seizing.
A second, symmetrical possibility now sits beside it: **the mice may never have been watched the way
the rats were.** 19500159's 95% is a figure obtained *on audiogenic stimulation* — a provocation,
not a passive observation — and the rat's earliest onset (day 16) nearly exhausts the mouse null's
entire lifespan (77% dead by day 17). *"The mouse has no epilepsy"* and *"nobody provoked, EEG'd, or
outlived the mouse"* have the same appearance and different consequences. **That is measurable from
the published record without acquiring Mallaret**, and is dispatched as a census task this wave.

### 2d · What is explicitly NOT proposed

- ❌ **No lifting of the prohibition.** An abstract is not a read.
- ❌ **No promotion of the Mallaret sentence to `DATO`**, and no `PAPER`-level statement that the
  mouse seizes.
- ❌ **No demotion of `CLAIM 037`.** The rat `lde/lde` data are full-text-read and unaffected.
- ❌ **No new gate, auditor, registry or workflow.** §26 boundary respected: the defect here is
  scientific and its repair is scientific text, not machinery. What made this findable was reading
  the source — which the existing discipline already requires.

---

## 3 · Provenance and integrity

- **Canonical files touched by this candidate at propagation:** `claim_registry_current.md`
  (`CLAIM 005` evidence boundary, `CLAIM 037` evidence boundary). No registry cardinality change,
  no receipt written, no ledger touched, no manifest anchor moved.
- **`UNREAD_PREMISE` impact: none, and the direction is favourable.** `24369382` was already
  `partial_fulltext_read` / `legacy_reconstruction` before this wave and remains so. No premise is
  newly imported. What changes is that a canonical claim will now **say** that one of its
  co-attributed sources is unread and asserts the opposite — hidden debt converted into declared
  debt, which is the ratchet working in the intended direction.
- **Quotation integrity:** both Mallaret quotations are verbatim from the PubMed metadata record
  retrieved this session, including the italic-free rendering of *Wwox*; the `we observed` emphasis
  is mine and is marked as emphasis, not as the source's. The `CLAIM 005` and dossier quotations are
  verbatim from the files at the line numbers given.
- **Date/cohort integrity:** *Brain* 2014;137(Pt 2):411–9, PubMed `publication_date` 2013-12-24
  (online) — **the 2013 copyright year and the 2014 issue year are the same paper**, recorded here
  explicitly because a year mismatch of exactly this shape produced a defect earlier in this session.
