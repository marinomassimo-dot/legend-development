# COMMIT CANDIDATE — CC-20260920-CLAIM039-CEREBELLAR-01

**Source:** the blunt-instrument claim audit (39 claims screened) **plus a source-verification task
that tested its verdict and found it understated**. Files:
`analysis/blunt_instrument_claim_audit_20260920.md`,
`analysis/blunt_instrument_source_verification_20260920.md`.
**Ledger:** `fulltext_receipts.py verify` → **OK: 168 chained receipt(s), tail anchored**.
**Change class:** **ORDINARY** — a canonical claim's **title** is narrowed on one limb, and a
`BLOCK 2` mirror row gains the endpoint it lacks. Precedent: `CLAIM 023` / `BATCH_20260909_001`.
**Target:** no working-model version bump proposed; the BLOCK 2 row is edited in place, not restructured.
**Status:** ✅ `PROPAGATED — BATCH_20260921_001` (2026-09-21), on the Operator's decision of 2026-09-21. ACCEPT WITH FURTHER NARROWING. The title now says what the source supports — *no marked cerebellar histopathology was detected on light microscopy at ~28 days* — and the evidence boundary records that **neither evidence stream currently establishes nor excludes a cerebellar contribution**: the exclusion is one modal sentence from an unblinded look with no quantitative motor test in 32 locators, and the counter-evidence is one passing sentence, no number, n=3, unblinded, never captured as a locator. The two are compatible (ages disjoint) and neither establishes causality. The BLOCK 2 mirror row moved with the claim. 🔴 **Operator condition honoured: the human MRI material is NOT integrated** — abstract-level, *"We suggest"*, contested. `CLAIM 039` remains a rat-model claim.
**Status (superseded, kept append-only):** `PROPOSED — NOT PROPAGATED`.
**Review floor:** R2. 🔴 **R4 consideration for the operator:** this narrows a canonical **title**, which
is the most-read line of a claim. It does not touch a `consolidated baseline` record, so the R4
trigger does not fire mechanically.

---

## 1 · The finding, and it has two halves

### Half one — what the exclusion actually rests on

`CLAIM 039` asserts in its **title** that the phenotype **"is not cerebellar"**. Its named source is
`PMID 17803050` (Suzuki 2007, *Comparative Medicine*) — **no DOI, no PMCID, permanently unobtainable
in this environment**, so the verification worked from LEGEND's own receipt
`FTR-20260806-17803050-01`, enumerating **all 32 verbatim locators**, plus the dossier.

The entire basis is **one hedged sentence** in the Discussion:

> *"in contrast with the ataxia and male sterility (AMS) mouse, **we did not detect any marked
> pathologic changes in the cerebella of `lde/lde` rats**"*

**No quantitative motor or coordination test exists anywhere in that source** — no rotarod, no
footprint, no beam, no ledge, no catwalk, across all 32 locators and every section. The gait
observation (*"95% of the mutant rats but none of the normal rats had ataxic gait"*) sits inside the
**seizure-observation** section, not a motor battery.

*"We did not detect any **marked** pathologic changes"* on light microscopy is a statement about what
an unblinded histological look could see. It is not *"the phenotype is not cerebellar."* Purkinje-cell
counts, molecular-layer thickness and cerebellar electrophysiology are all things that sentence does
not report.

### Half two — the more sensitive evidence exists, was read, and never landed

🔴 **The audit wrote *"more sensitive evidence — none in the corpus, in either direction."* That is
wrong, and the correction is the more important half of this candidate.**

`PMID 32581702` — **the same `lde/lde` strain, the same colony, with Suzuki H an author of both
papers** — reports at P1:

> *"**the development of cerebellum was delayed in [`lde/lde`] as shown by reduced number of
> foliation**"*

with the Figure 3 caption *"Arrowheads indicate delayed foliation in [`lde/lde`] cerebellum."*

**That sentence appears in none of the 21 locators of that paper's deep-dive manifest.** LEGEND read
the paper and the cerebellar finding never became a locator, so it never reached the claim that
excludes a cerebellar contribution. This is the **same propagation defect** already recorded on
`CLAIM 016`, whose evidence boundary says of the lithium locator: *"esisteva dal giorno della lettura
e non era mai arrivato fin qui: è un difetto di propagazione, non di lettura."* **Second instance,
different claim.**

**No species firewall applies** — both are the same rat strain, unlike the mouse lesion that
`therapeutic_repair_candidates.md` correctly excluded on species grounds.

## 2 · What is proposed, and what is refused

**Proposed.**

**(a)** Narrow the `CLAIM 039` **title** on the cerebellar limb only — from *"it is not cerebellar"*
to language the source supports, e.g. *"no marked cerebellar histopathology was detected on light
microscopy at ~28 days"*.

**(b)** Add to `CLAIM 039` an evidence boundary:

> 🔴 **Evidence boundary — the exclusion is one unblinded look, and a later reading contradicts its
> scope.** The source reports *"we did not detect any **marked** pathologic changes in the cerebella
> of `lde/lde` rats"* and contains **no quantitative motor test of any kind** (32 locators
> enumerated; the ataxic-gait observation sits in the seizure-observation section). `PREMISE:
> LIGHT_MICROSCOPY_FLOOR`. **Counter-directional, same strain and same colony:**
> [[paper_registry_current#PAPER 020]] (`PMID 32581702`) reports at **P1** that *"the development of
> cerebellum was delayed … as shown by reduced number of foliation"*. The two are **compatible as
> measurements** — ages are disjoint (P1 vs ~28 d), and a delay at P1 need not leave *marked*
> pathology at 28 d — which is exactly why the 28-day silence was never evidence of cerebellar
> normality. ⚠️ The P1 finding is **one passing sentence, no number, n=3, unblinded**, and **was not
> captured as a locator** at the time of reading. `REVIVAL_TRIGGER`: any quantitative cerebellar
> endpoint in this strain — Purkinje counts, foliation index, molecular-layer thickness, or a motor
> battery.

**(c)** Give the `BLOCK 2` mirror row (row 189) the endpoint column it lacks, so the exclusion is not
repeated in the working model without the instrument that produced it. The verification confirmed
verbatim that the row carries **no endpoint, no boundary and no `🔴` marker**.

**Refused, explicitly:** the claim is **not** reversed — no cerebellar contribution is asserted · the
`lde/lde` ataxic-gait datum is **untouched** · `PMID 32581702` is **not** re-tiered or re-read here ·
no new claim · no therapeutic entry · no working-model version bump · no new field or vocabulary.

## 3 · Declared limits

- `PMID 17803050` is **permanently unobtainable** here (no DOI, no PMCID). Its cerebellar histology's
  **n, age, stain and section plane are unrecorded in all 32 locators** and cannot be closed from
  this environment. The candidate therefore narrows the claim to what the receipt can support and
  does not assert what the source actually did.
- **No figure panel was inspected.** All Figure 3 panels of `PMID 32581702` — the cerebellar
  arrowheads, the Satb2 panel, the BrdU panel — are unreachable (no PDF tooling, no figure-image
  route). Per `D-14`, the P1 cerebellar finding is carried as **running text only**, and as a
  boundary rather than as a counter-claim.
- Both papers are **unblinded**, n=3 per genotype, uncorrected Student's *t*-tests. The string
  *"blind"* occurs in neither full text.
- 🔴 **For an audit about instrument sensitivity, the missing instrument is itself the finding** — and
  it is recorded here rather than worked around.
