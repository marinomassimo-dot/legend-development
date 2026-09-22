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
