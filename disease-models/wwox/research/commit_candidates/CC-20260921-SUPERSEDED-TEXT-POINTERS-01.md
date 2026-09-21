# COMMIT CANDIDATE — CC-20260921-SUPERSEDED-TEXT-POINTERS-01

**Source:** not a reading. Four independent instances, found in one session, of **one navigability
defect in append-only correction** — two surfaced by Scientist B with exact coordinates, one by the
Orchestrator. All three re-verified line by line against the files.
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — four pointer lines. **No claim, finding, number or conclusion is
changed anywhere.** Every superseded sentence is preserved verbatim.
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** Nothing is reversed, narrowed or removed. What is added is a **forward
pointer** from superseded text to the correction that already exists elsewhere in the same file.

---

## 1 · The defect, stated once

LEGEND corrects **by appending**. That is right, and it is why this repository can be audited at
all. But an append lands **at the bottom of the file**, and the superseded sentence stays **exactly
where a reader meets it first**. So the correction exists, is durable, is discoverable by search —
and is invisible to the only reader who matters, the one reading forward from the top.

🔴 **This is not hypothetical. It corrupted work inside this session.** The Orchestrator's brief to
Scientist B on `MECHANISM_DOWNSTREAM_WWOX_INDEPENDENT_RESCUE` was built on
`discovery_ledger_current.md:460`, asserted an in-vivo rescue as the node's strongest lead, and was
**wrong** — the correction had been written on 2026-08-14 and propagated to the canonical surfaces,
2,783 lines further down in the same file. Scientist B caught it and said so. The brief cost a
delegate's entire first wave on a premise the repository had already retired.

## 2 · The three instances, with coordinates verified line by line

### 2a · `disease-models/wwox/research/discovery_ledger_current.md:460` — `DL-MECH-020`

Current text (preserved, not changed):

> *"L'inibizione di HIF1α (genetica **e** farmacologica) **reverte** l'uptake di glucosio in vitro
> e in vivo."*

Superseded by **`DL-MECH-095`, same file, line 3243**, Correzione 1:

> *"`DL-MECH-020` dice che l'inibizione farmacologica reverte l'uptake di glucosio *in vivo*. Il
> topo misura invece **glicemia ematica acuta**, 40 minuti dopo una singola iniezione; nessun
> uptake, flux, durata, sopravvivenza o endpoint neurologico in vivo."*

⚠️ **And the canonical side is already correct.** `CC-20260814-25012504-01` carries
`Status: committed — BATCH_20260815_001`, and `paper_registry_current.md:558` and
`claim_registry_current.md:461` both carry the corrected form. **So this is not an uncorrected
claim — it is an uncorrected *path to* the claim.** The distinction matters: nothing canonical is
wrong, and a reader of the compounding memory is still misled.

**Proposed insertion**, immediately after line 460, text preserved above it:

> 🔴 **SUPERSEDED — see `DL-MECH-095` (this file), 2026-08-14.** The in-vivo endpoint is **acute
> blood glucose at 40 minutes after a single injection**, not glucose uptake; no flux, durability,
> survival or neurological endpoint was measured in vivo, and the genetic (shHIF1α) in-vivo arm is
> a **tumour xenograft**, not a `Wwox`-deficient animal. Digoxin is **target validation, not a
> candidate**. Corrected canonically in `BATCH_20260815_001`
> (`CC-20260814-25012504-01`). *The sentence above is kept verbatim because the ledger is
> append-only and because what it once said is itself part of the record.*

### 2b · `disease-models/wwox/research/full_text_queue_current.md:2471` — `FT-059` heading

Current heading (preserved, not changed):

> `## FT-059 — Steinberg 2021, organoidi: 🟡 superficie recuperata, **69 pannelli da leggere**, lettura NON iniziata`

Superseded by an append-only correction **in the same file, line 3437**:

> `## CORREZIONE APPEND-ONLY FT-059 — copertura disponibile completata, debito ristretto alla fonte assente (2026-08-14)`
> *"`FTR-20260814-34268881-03` sostituisce operativamente il vecchio preflight, senza cancellarlo: testo principale letto in tutte le sezioni e 91 referenze enumerate…"*

🔴 **The heading is the single line most likely to be read and least likely to be corrected**, and
here it says the opposite of the truth: *"lettura NON iniziata"* for a paper with a
complete-coverage receipt. **This is the line that reached a delegate brief this session.**

**Proposed insertion**, immediately under the heading:

> 🔴 **THIS HEADING IS SUPERSEDED — see `CORREZIONE APPEND-ONLY FT-059` (this file, 2026-08-14).**
> The reading **was** done: `FTR-20260814-34268881-03`, main text read in all sections, 91
> references enumerated. The residual debt is **the absent source**, not the reading. The heading
> is preserved verbatim because it records what the queue believed on the day it was written.

### 2bis · `disease-models/wwox/research/full_text_queue_current.md:2810` — `FT-062` heading

Found while sizing the problem, i.e. **after** deciding it was a pattern — which is the right order.

Current heading (preserved, not changed):

> `## FT-062 — Salah 2013: la fonte a cui lo stato attribuisce già la stabilizzazione ITCH, mai letta`

Superseded **in the same file, line 3458**:

> `## CORREZIONE APPEND-ONLY FT-062 — Salah 2013 LETTO E CHIUSO (2026-08-14)`
> *"Lettura completata in una sola corsa: XML strutturato e PDF di nove pagine, tutte le sezioni,
> 6/6 figure e 23/23 pannelli, 66/66 riferimenti… Manifest schema-v2 strict PASS, dossier
> `PMID23370280.md`, scoperta `DL-MECH-104`, candidate `CC-20260814-23370280-01`, receipt
> `FTR-20260814-23370280-01`."*

**Identical shape to `FT-059`, same date, same file, 648 lines apart.** Two headings saying a paper
was never read, above two corrections saying it was read completely with every figure and panel.

**Proposed insertion**, immediately under the heading:

> 🔴 **THIS HEADING IS SUPERSEDED — see `CORREZIONE APPEND-ONLY FT-062` (this file, 2026-08-14).**
> Salah 2013 (`PMID 23370280`) was read completely — all sections, 6/6 figures, 23/23 panels,
> 66/66 references — receipt `FTR-20260814-23370280-01`. *"mai letta"* records what the queue
> believed when the entry was opened and is preserved for that reason only.

### 2c · `disease-models/wwox/registries/paper_registry_current.md:7161` — `PAPER 094`

Current text:

> *"**Evidence depth:** complete_fulltext_read — `FTR-20260810-42397075-04`; manifest
> `deepdive_manifests/PMID42397075.json` (**6 locators**, schema v2, strict PASS, 0 gaps)"*

**The manifest holds 30.** Verified: `verbatim_locators` is an object whose `entries` array has
**30** members; `discovery_ledger_current.md:2333` independently says 30; and the receipt
`FTR-20260810-42397075-04` states *"30 locators in a schema-v2 manifest validating PASS under
MANIFEST STRICT"*.

> ⚠️ **Recorded because it nearly went the other way.** The Orchestrator's first check returned
> "6" and briefly read as a *receipt over-claiming its manifest* — the more alarming direction.
> It was a counting error: `len()` on the `verbatim_locators` **object** returns its six keys
> (`waived`, `source_fulltext_indexed`, `source_fulltext_indexed_evidence`,
> `abstract_anchoring_waived`, `surface_note`, `entries`), not its entries. Scientist B's number
> was right. **A count is a measurement and needs the same care as a quotation** — and the
> registry's own "6" is very plausibly the identical mistake made once before.

🔴 **`paper_registry_current.md` is one of the four canonical scientific current files.** It is
**not** edited here. The correction is proposed for application at `BATCH_COMMIT`:

> *"… manifest `deepdive_manifests/PMID42397075.json` (**30 locators**, schema v2, strict PASS,
> 0 gaps)"*

## 3 · What is proposed, in full

| # | File | Line | Action |
|---|---|---|---|
| a | `research/discovery_ledger_current.md` | after 460 | insert the `DL-MECH-095` forward pointer |
| b | `research/full_text_queue_current.md` | after 2471 | insert the `FT-059` heading-superseded banner |
| b2 | `research/full_text_queue_current.md` | after 2810 | insert the `FT-062` heading-superseded banner |
| c | `registries/paper_registry_current.md` | 7161 | `6 locators` → `30 locators` (**canonical — `BATCH_COMMIT` only**) |
| d | `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US` | — | one row, `D-20` |

**`D-20`:**

> **D-20** · *"the correction is in the file, so the file is corrected"* · **Why it is FALSE here:**
> append-only correction puts the fix at the **bottom** and leaves the superseded sentence **where
> a reader meets it first**. Four instances in one day — `DL-MECH-020` (corrected 2,783 lines
> below), `FT-059`'s heading (corrected 966 lines below), `PAPER 094`'s locator count — and the
> first two **both reached delegate briefs in this session and cost a wave of work each**. The
> canonical surfaces were right the whole time; the paths to them were not.
> **Detection rule:** when appending a correction, add a one-line forward pointer at the superseded
> text **in the same commit**. A correction without a pointer is a correction only its author can
> find. **Headings first** — a stale heading outranks a stale sentence, because it is read by
> people who read nothing else.

## 4 · What is explicitly REFUSED

- ❌ **Nothing is deleted or rewritten.** Every superseded sentence stays verbatim. Append-only
  means the wrong sentence is part of the record, and this candidate strengthens that rather than
  weakening it.
- ❌ **No new gate, auditor, registry or mandatory workflow** (§26). ⚠️ A detector — *"a
  `CORRECTION`/`SUPERSEDED` entry that names an earlier entry which carries no pointer back"* — is
  **conceivable and is deliberately not proposed here.** Four instances justify a habit, not a
  guard, and the operator's standing instruction is to correct the science and reuse existing
  mechanism. If it recurs after `D-20` exists, that is the evidence a guard would need.
- ❌ **No scientific conclusion moves.** `DL-MECH-095`'s corrections were already propagated in
  `BATCH_20260815_001`; `FT-059`'s reading already has its receipt; `PAPER 094`'s manifest already
  validates strict PASS with 30 locators. **This candidate changes navigation, not knowledge.**

## 5 · Growth delta

`claims +0 · papers +0 · corpus +0`.

---

*No canonical file edited by this candidate. Item (c) is canonical and is proposed for
`BATCH_COMMIT` only. No reading occurred; no receipt claimed. Not medical advice.*
