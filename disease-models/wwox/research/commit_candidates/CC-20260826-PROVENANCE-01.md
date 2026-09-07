# COMMIT CANDIDATE — provenance repairs: four source records that do not identify their source

**Candidate ID:** CC-20260826-PROVENANCE-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Change class:** MINOR per item, except item A which suspends two `consolidated baseline` claims
and is therefore **MAJOR by consequence**.
**Target WM:** current at BATCH_COMMIT time; rebase required
**Batch gate:** intentionally untouched

> **Binding constraint honoured throughout.** No unread source is marked read. Where a repair
> requires a reading that has not happened, the item stops at `WHAT_REQUIRES_FULL_TEXT` and the
> claim it supports is suspended rather than rewritten. `FT-044` is **not** closed.

---

## A. `PAPER 007` — a record that names no paper

> 🔴 **APPEND-ONLY SUPERSESSION — 2026-08-26, later the same day.** Four cells of the table below
> are now **stale**, and the recommendation built on them is withdrawn.
>
> | Cell | As written | Now |
> |---|---|---|
> | `LOCATORS_AVAILABLE` | *"none. No `deepdive_manifests/PMID36828035.json` exists."* | **26 locators**, 9 of them figure pixels, `MANIFEST STRICT PASS` |
> | `READ_STATUS` | 🔴 *"UNREAD. No receipt of any depth."* | **`partial_fulltext_read`**, receipts `FTR-20260826-36828035-01` and `-02` |
> | Acquisition note | *"Elsevier, likely paywalled; route it through the operator or the foundation"* | **Free.** NIH author manuscript in PMC (PMC10835625, NIHMS1957654, CC BY-NC-ND). No operator routing needed |
> | `WHAT_CAN_BE_REPAIRED_NOW` item (4) | 🔴 *"**Suspend `CLAIM 006` and `CLAIM 007`** … to `flagged for review`"* | ❌ **WITHDRAWN** |
>
> **Why item (4) is withdrawn, and it is not a change of mind.** It was conditional on its own
> stated reason — *"not because their content is disputed, but because neither can be checked
> against a source until the source is read."* **The source has been read.** The precondition is
> discharged, so the recommendation lapses on its own terms.
>
> What replaces it is **narrower and sharper**, in
> [`CC-20260826-PROVENANCE-PAPER007-01`](CC-20260826-PROVENANCE-PAPER007-01.md): identity repair
> is mechanical and suspends nothing; `CLAIM 007` is **verified at the pixels** and needs no
> suspension at all; and `CLAIM 006` needs a **content** repair — its *"progressive microgliosis"*
> is falsified by the source's own Figure 3b — which is a different and better-founded action than
> a provenance suspension.
>
> ⚠️ The table below is **left unedited** so that the reasoning that produced the withdrawn
> recommendation stays legible.

| Field | Value |
|---|---|
| `CURRENT_RECORD` | `PAPER 007` — *Short title:* "Hussain 2023 P47T" · *Full title:* **"P47T model shows progressive neuroinflammation and altered PPxY binding"** (a restatement of the two claims, not a published title) · *Authors:* "Hussain et al." · *Journal/source:* **`pending normalization`** · *Identifier:* **`pending normalization`** · *Status:* `integrated` |
| `TRUE_SOURCE_IDENTITY` | **PMID 36828035 · DOI 10.1016/j.pneurobio.2023.102425 · *Progress in Neurobiology* 2023** · title: ***"WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice"*** |
| `DUPLICATE_OR_SUCCESSOR_RELATION` | **Duplicate.** `CORPUS-STUB-053` already holds the true identity, with `Status: not_processed`, `Claim links: none`. `PAPER 007` is the shadow of that stub, promoted without its identifier. |
| `CLAIMS_AFFECTED` | `CLAIM 006` (`consolidated baseline`, DATO+INFERENZA) · `CLAIM 007` (`consolidated baseline`, DATO). Indirectly `CLAIM 030` (abundance-vs-function), `CLAIM 033`, `CLAIM 037`, and `meta_gaba_paradox_current.md`. |
| `LOCATORS_AVAILABLE` | **none.** No `deepdive_manifests/PMID36828035.json` exists. |
| `READ_STATUS` | 🔴 **UNREAD.** No receipt of any depth. `session_self_eval.py` already reports `[UNREAD PREMISE] PMID 36828035 cited in meta_gaba_paradox_current.md`. |
| `WHAT_CAN_BE_REPAIRED_NOW` | (1) Write the identifier, journal, year, full author list and **published title** into `PAPER 007`. (2) Resolve `CORPUS-STUB-053` as the same record, preserved append-only. (3) Change `PAPER 007` status from `integrated` to **`identified, unread`**. (4) 🔴 **Suspend `CLAIM 006` and `CLAIM 007` from `consolidated baseline` to `flagged for review`** — not because their content is disputed, but because neither can be checked against a source until the source is read. (5) Record in both claims that the published title names **epilepsy** and **cerebellar degeneration**, neither of which any claim carries. |
| `WHAT_REQUIRES_FULL_TEXT` | Everything else. Whether `CLAIM 006`'s "progressive neuroinflammation" is the paper's own framing; whether `CLAIM 007`'s PPxY-binding result is in **this** paper or another; the epilepsy phenotype's onset, penetrance and method; the cerebellar degeneration; and whether the normal-WWOX-abundance-with-severe-phenotype dissociation `[manifest PMID42128308 entry 8]` reports at second hand is first-hand here. **Until then that dissociation stays `IPOTESI`, because its only current source is a review citing an unrefereed preprint.** |

**Priority note.** This is the corpus's **only long-lived WWOX mouse** — every other mouse in the
registry dies at 3–4 weeks, which is why nothing in the model speaks to adult-onset or
progressive disease. Acquisition is *Prog Neurobiol*, Elsevier, likely paywalled; route it
through the operator or the foundation, as `FT-041` and `FT-042` were.

---

## B. `PAPER 027` / `PAPER 030` — one PMID, two records, wrong author, stale depth

| Field | Value |
|---|---|
| `CURRENT_RECORD` | `PAPER 027`: *Authors:* **"Schrock et al."** · title *"WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response"* · PMID 25331887 · `Status: integrated` · `Claim links: 029`. `PAPER 030`: **same PMID**, *Authors:* "Abu-Odeh 2014" · **`Evidence depth: abstract reviewed (PubMed metadata; full text not yet extracted)`** · `Claim links: 029`. |
| `TRUE_SOURCE_IDENTITY` | PMID 25331887 · PMCID PMC4226089 · DOI 10.1073/pnas.1409252111 · *PNAS* 2014. Verified here against `PMID25331887_AbuOdeh2014_PMC.html` (sha256 `8c629a54…`): the article title matches, and 🔴 **the string `Schrock` does not occur anywhere in it.** |
| `DUPLICATE_OR_SUCCESSOR_RELATION` | **Duplicate**, not successor. Same identifier, same claim link, contradictory metadata. Third instance of the invented-metadata class after `PAPER 021` (Tochigi/Kumada, corrected 2026-08-06) and `PAPER 007`. |
| `CLAIMS_AFFECTED` | `CLAIM 029` (`in observation`, DATO+INFERENZA prudente). |
| `LOCATORS_AVAILABLE` | **29 verified locators** in `deepdive_manifests/PMID25331887.json`, including three declared contradiction pairs. |
| `READ_STATUS` | `partial_fulltext_read`, receipt **`FTR-20260810-25331887-01`**. Local artifacts: PDF + PMC HTML + assets. |
| `WHAT_CAN_BE_REPAIRED_NOW` | Merge `PAPER 030` into `PAPER 027` (preserve the merged record append-only); correct the authorship to **Abu-Odeh M, Salah Z, Herbel C, Hofmann TG, Aqeilan RI**; replace `abstract reviewed` with `partial_fulltext_read` naming receipt `FTR-20260810-25331887-01` and the 29-locator manifest. All four facts are on disk. |
| `WHAT_REQUIRES_FULL_TEXT` | Promotion of `CLAIM 029` beyond `in observation` — the receipt is explicitly **partial**, so nothing licenses upgrading the claim's strength as part of this repair. |

---

## C. `PAPER 001` — a `consolidated baseline` sourced to `Identifier: preprint`

| Field | Value |
|---|---|
| `CURRENT_RECORD` | `PAPER 001` — *Short title:* "Steinberg 2024 organoids" · *Journal/source:* **bioRxiv** · *Identifier:* **`preprint`** (no DOI) · *Full title:* "WWOX deficiency impairs neurogenesis and neuronal function in human organoids" · `Status: integrated` · `Claim links: 002` |
| `TRUE_SOURCE_IDENTITY` | The refereed version is **PMID 42397075 · DOI 10.1093/brain/awag239 · *Brain*.** 🔴 It has **no PAPER record** — `grep "42397075" paper_registry_current.md` returns nothing. |
| `DUPLICATE_OR_SUCCESSOR_RELATION` | **Successor**, not duplicate. The preprint record must be preserved append-only as superseded, not deleted — `[manifest PMID42128308 entry 25]` records that the 2026 review still cites the preprint DOI, so the preprint identity has downstream traffic and must stay resolvable. |
| `CLAIMS_AFFECTED` | `CLAIM 002` (`consolidated baseline`). |
| `LOCATORS_AVAILABLE` | **30 verified locators** in `deepdive_manifests/PMID42397075.json`. |
| `READ_STATUS` | **`complete_fulltext_read`**, receipt `FTR-20260810-42397075-04`, all ten supplementary figures inspected as rendered images. |
| `WHAT_CAN_BE_REPAIRED_NOW` | Create the PAPER record for PMID 42397075 with its manifest, receipt and locator count; mark `PAPER 001` **superseded by** it, preserved append-only; repoint `CLAIM 002`'s Source. Then apply the qualifications the refereed reading already carries and the claim does not: the missing WT-vs-treated bracket at Fig. 6A(ii); *"rescued neuronal functional phenotypes without correcting RG abnormalities"*; the **0.4×–7× WWOX protein spread across lines with the same vector**; the engineered-KO-specific composition phenotype; no randomization or blinding. |
| `WHAT_REQUIRES_FULL_TEXT` | Nothing — this is the one item where the reading is already **complete**. 🔴 **It is pure propagation debt**, and the repair is bookkeeping over evidence that has been in the repository since 2026-08-10. |

---

## D. `PAPER 039` — a declared complete read the ledger contradicts

Found while assembling item C; not in the 2026-08-25 candidate.

| Field | Value |
|---|---|
| `CURRENT_RECORD` | `PAPER 039` (PMID 34268881, Steinberg 2021, *EMBO Mol Med*) declares **`Evidence depth: full text reviewed (coverage_status: complete_fulltext_read; Expanded-View raw tables non incluse)`** · `Status: claim_linked` · `Claim links: 002, 030, 032` |
| `TRUE_SOURCE_IDENTITY` | correct as recorded — PMID 34268881 / PMCID PMC8350905 / DOI 10.15252/emmm.202013610 |
| `DUPLICATE_OR_SUCCESSOR_RELATION` | none |
| `CLAIMS_AFFECTED` | `CLAIM 002`, `CLAIM 030`, `CLAIM 032` — **all three of the claims this session repairs** |
| `LOCATORS_AVAILABLE` | no `deepdive_manifests/PMID34268881.json` |
| `READ_STATUS` | 🔴 **two receipts, both `partial_fulltext_read`**: `FTR-20260726-34268881-01`, whose own `evidence_basis` opens by flagging this very mismatch, and `FTR-20260810-34268881-02`, which states *"DECLARED PARTIAL BECAUSE IT IS PARTIAL, AND DELIBERATELY NOT STARTED AS A COMPLETE READ"*. |
| `WHAT_CAN_BE_REPAIRED_NOW` | Correct `Evidence depth` to `partial_fulltext_read`, naming both receipts. This is a **downgrade of a declaration, not of a datum**: nothing measured in the paper is demoted. Also: `PAPER 039`'s `Note` presents *"**GABA depolarizzante** — GAD67/GAD1/GAD2 ↑, VGLUT1 invariato, GABRB2/3 ↓"* under the word *Findings*; the first term is a Discussion inference and the three that follow are the transcript measurements — see [`CC-20260826-CLAIM002-01`](CC-20260826-CLAIM002-01.md) §3. Split the line so the transcript findings keep `DATO` and the polarity keeps `IPOTESI`. |
| `WHAT_REQUIRES_FULL_TEXT` | A complete read of PMID 34268881 with a schema-v2 manifest, if `CLAIM 002`/`030`/`032` are ever to rest on it at full strength. Queue it; do not assume it. |

---

## E. Two meta-file corrections that follow from the above

**D-meta — `meta_gaba_paradox_current.md`, line 19.** Its provenance correction reads
*"Seizures are a RAT phenotype in this literature, and they are explicitly ABSENT in Wwox-null
mice."* That sentence is **false** — see [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md).
It is also framed by its own counter-examples at lines 17 and 23. Replace with the seven-way
split, and keep the part that is correct and valuable: that the chain which imported the seizure
premise into the mouse literature was a citation chain, not a measurement.

**E-meta — `meta_network_myelin_glia_current.md`, line 92.** *"Abudiab 2025 (cuprizone / SOX10)
shows a cell-autonomous oligodendroglial role of WWOX"* must carry the qualification the manifest
already records: bioRxiv 10.1101/2025.11.22.689900, **unrefereed**, cited by the review seven
times and never labelled as a preprint `[manifest PMID42128308 entry 24]`. Status `IPOTESI`.

---

## F. What this candidate deliberately does not do

- Does **not** mark PMID 36828035 as read. It is unread, and `CLAIM 006`/`CLAIM 007` are
  suspended rather than rewritten.
- Does **not** close `FT-044`. PMID 33914858 remains `pdf_only` / `SUSPECT`; the page-level
  adjudications in this session's candidates support **no text locator** and clear no debt.
- Does **not** upgrade `CLAIM 029`: PMID 25331887's receipt is `partial`.
- Does **not** delete any placeholder or superseded record; every merge is append-only.

---

## G. Review required

Item **A** requires operator authorization: suspending two `consolidated baseline` claims is a
status change on baselines. Items **B**, **C**, **D** and **E** are review-only — they correct
metadata and declarations against artifacts already on disk, and demote no experimental datum.
