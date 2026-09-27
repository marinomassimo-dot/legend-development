# CC-20260922-VERMIS-HYPOPLASIA-FREQUENCY-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Target:** `discovery_ledger_current.md` L554 (the `CLAIM 039` cerebellar note) · and the interpretive
gloss carried alongside receipt `FTR-20260921-35573960-01`
**Change class:** **QUALIFY a frequency claim.** No imaging finding is denied; a *"most cases"* is
bounded. **The receipt is NOT touched** — receipts are append-only and the reading is not in question.
**Review floor:** R2. **BLOCK-1:** no molecule, no dose, no route. Nothing here is medical advice.

---

## 1 · The claim as held

`discovery_ledger_current.md` L554, verbatim (Orchestrator-verified):

> *"cerebellar vermis hypoplasia … **have been described in most cases**."*

Sourced to Riva, `PMID 35573960`, whose reading is receipted as `FTR-20260921-35573960-01`
(Orchestrator-verified present, 1 record).

## 2 · The counter-evidence

According to PubMed, **`PMID 38161429` / `PMC10757851`** — Battaglia et al. 2023, *Front Pediatr*
11:1301166, [DOI](https://doi.org/10.3389/fped.2023.1301166) — is *"**Neuroimaging features of WOREE
syndrome: a mini-review of the literature**"*, i.e. a collation whose **explicit subject is the
radiological spectrum**: *"We focused on neuroradiological findings to better delineate the WOREE
phenotype."* Co-authored from IRCCS Gaslini, Genoa. **This is the most directly on-point denominator
the literature offers for a WOREE imaging frequency**, and it is a stronger instrument for a
*frequency* than a single-case report is.

Scientist F reports, from Table 1 **eyeballed** (its attestation, not an Orchestrator read):
- cerebellar vermis hypoplasia in **2 patients from 1 study**, against a **101-patient** collation;
- the review calls the finding **"less specific"**;
- Tabarki's five-patient cohort recorded as *"Of note, **the cerebellum was not affected**."*

⚠️ **F's own caveat, preserved:** the linearised table drops blank cells, so its assignment of that
`2:2` to Iacomino rests on prose plus that cohort's `n = 2`, **not** on the table's geometry.

## 3 · Why this is a defect and not a disagreement

> **"Described in most cases" is a claim about a DENOMINATOR.** A case report and a small series can
> establish that a finding **occurs**; neither can establish that it occurs in **most** patients. The
> ledger's phrasing takes a finding reported in a handful of patients and gives it a prevalence it
> was never measured to have.

🔴 **And the direction matters for `CLAIM 039`.** L554 explicitly offers this note as evidence *"in
the opposite direction to cerebellar sparing"* (*"va nella direzione opposta al risparmio
cerebellare"*). A frequency inflated from *"occurs"* to *"most cases"* **overstates exactly the
thing the note was recruited to establish.**

## 4 · Proposed edit

**BEFORE** …*"cerebellar vermis hypoplasia … have been described in most cases."*

**AFTER** …*"cerebellar vermis hypoplasia **è stata descritta** in casi WOREE"* — ⚠️ **frequenza NON
stabilita.** La revisione neuroradiologica dedicata (`PMID 38161429` / `PMC10757851`, Battaglia 2023,
*Front Pediatr*) la registra in **2 pazienti da 1 studio** su una collazione di **101**, la qualifica
come **"less specific"**, e riporta una coorte di cinque pazienti in cui *"the cerebellum was not
affected."* 🔴 `PREMISE: FREQUENCY_UNESTABLISHED`. `REVIVAL_TRIGGER`: una collazione con denominatore
dichiarato e criteri radiologici uniformi.

## 5 · What this candidate does NOT do

- ❌ Does **not** deny that vermis hypoplasia occurs in WOREE. The Riva observations (*"a small
  inferior vermis"* at 7 days; dentate-nuclei signal change; *"inferior cerebellar vermis
  hypoplasia"* in Discussion) are **in prose in the primary** and stand untouched.
- ❌ Does **not** touch the receipt. `FTR-20260921-35573960-01` records a **reading**, and the reading
  is not disputed — only the frequency gloss built on it. The ledger is append-only.
- ❌ Does **not** resolve `CLAIM 039` in either direction. It removes an overstated prop, which leaves
  that claim **more open**, not settled.
- ❌ Does **not** treat F's Table-1 counts as Orchestrator-verified. They are its attestation, with
  its own caveat carried.

## 6 · Verification before propagation

1. 🔴 **Read `PMC10757851` Table 1 directly** and confirm the `2 / 101`, the *"less specific"*
   wording, and the Tabarki sentence. **This is the blocking item** — the paper is open access
   (`PMC10757851`), so it is cheap.
2. Confirm nothing else in the registries carries the same *"most cases"* frequency.
3. Check whether Riva itself states a frequency, or only describes its own case.

---

## WAVE-2 READINESS (2026-09-27)

**context_policy declared:** `QUESTION_DRIVEN`, declared before the source was opened. Held going
in: this candidate, the discovery-ledger sentence it targets, and the fact that the only receipt for
PMID 38161429 was `FTR-20260726-38161429-01`, partial, every coverage field `unknown_legacy`.
Question, stated as narrowly as locating the facts required: does this collation contain a
vermis-hypoplasia count, its own characterisation of that finding's specificity, and a cohort in
which the cerebellum was unaffected.

**Actor:** `scientist`, wave-2 package `provenance`.

### What I did — §6.1's blocking item, discharged at the source

The candidate's blocker was that the counts were **Scientist F's eyeballed attestation from a
linearised table**, with no receipt, no manifest and no locator behind them. I acquired the article
free (NCBI efetch `db=pmc id=10757851`; `files/fulltext/PMID38161429_Battaglia2023_PMC_2026-09-27.xml`,
sha256 `5bea706afd5e69ca08bf4e822707b025e036c26e1c36388ac81690e5a83f8fd2`) and read it.

**All three confirmed first-hand, and the third attributed rather than assumed:**

| Item | Verbatim | Where |
|---|---|---|
| the 2 : 2 | `Hypoplasia of the cerebellar vermis 2:2` | Table 1; last row `Total number of patients 101`; footnote `+, number of patients unspecified` |
| *"less specific"* | *"cerebellar vermis hypoplasia were observed in a lower percentage of cases, and therefore these findings seem to be less specific"* | Results, closing sentence before the Discussion |
| the unaffected cerebellum | *"Of note, the cerebellum was not affected"* | Results, closing the **Tabarki et al.** paragraph — *"five patients from two unrelated families"*, reference 51. **F's own caveat is discharged**: the attribution is in the prose, not inferred from table geometry |
| what IS predominant | *"hypoplasia of the corpus callosum and brain atrophy appeared to be the predominant MRI alterations"* | Discussion |

**Artefacts produced:** `deepdive_manifests/PMID38161429.json` — new, schema v2, 4 locators,
`deepdive_manifest.py --verify-artifacts --require-current-schema` = **PASS with 1 declared gap**
(35 gene-direct references enumerated and queued, none resolved). Receipt JSON written to
`…/scratchpad/receipts_pending/provenance_38161429_1.json` as
`FTR-20260927-38161429-02`, `partial_fulltext_read`, `prior_receipt FTR-20260726-38161429-01`,
`reread_reason inadequate_prior_coverage`. 🔴 **`fulltext_receipts.py record` was deliberately NOT
run** — the ledger is a hash chain and other wave-2 packages append to it in parallel; the receipt
is handed to the integrating actor.

**Applied outside batch** — `discovery_ledger_current.md`, the `CLAIM 039` cerebellar note, as an
**append-only** correction block (the ledger is append-only; the earlier text stands). The
frequency clause *"have been described in most cases"* is withdrawn as a frequency statement and
replaced by *"è stata descritta in casi WOREE"* + ⚠️ **frequenza NON stabilita**,
`PREMISE: FREQUENCY_UNESTABLISHED`, with the four quotations above and a `REVIVAL_TRIGGER` (a
collation with a declared denominator and uniform radiological criteria).

**Three things the correction does not do**, and they are in the block: it does not deny that
vermis hypoplasia occurs — Riva's prose findings stand untouched; it does not touch
`FTR-20260921-35573960-01`, because what is withdrawn is the gloss built on the reading, not the
reading; and it does not resolve `CLAIM 039`, which is left **more open**, not settled. A limit of
the new source is stated too: Battaglia 2023 carries **no cohort of its own**, so it can show that
no collated denominator makes the finding common — not that the finding is rare.

### Verdict — **CLOSE**, closing status **PROPAGATED**

The only target this candidate names is the discovery-ledger line, and it is corrected. No
canonical file is touched; `CLAIM 039` is untouched by this act.

**Change class:** QUALIFY a frequency claim — MINOR, non-canonical. **Applied outside batch:**
`disease-models/wwox/research/discovery_ledger_current.md`.

**Pending:** one receipt to append (`provenance_38161429_1.json`), by whoever holds the ledger lock.
