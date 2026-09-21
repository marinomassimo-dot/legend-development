# COMMIT CANDIDATE — CC-20260921-PAPER025-IDENTITY-01

**Source:** Scientist A, node `TX001_RNA_EVIDENCE_FROM_PUBLISHED_DATA`
([`tx001_public_rna_data_feasibility_20260921.md`](../../analysis/tx001_public_rna_data_feasibility_20260921.md)),
**re-verified by the Orchestrator** against PubMed metadata and against LEGEND's own splice-transcript
census. **No reading occurred beyond abstract depth; no receipt is claimed.**
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — one record's author and title corrected, one record's content
expanded, one queue entry. **No claim reversed, no status moved, no conclusion changed.**
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3.** `PAPER 025` is the cited source of `CLAIM 018`, which is
`consolidated baseline`. Nothing about either claim's **content** is challenged — what is wrong is
**who wrote the paper** — but a consolidated-baseline source deserves the higher floor on principle.

---

## 1 · The defect

`PAPER 025` carries **`PMID 30853297`** attributed to *"Piard et al."*, with a title ending
*"…dysmorphic features"*.

**The record is neither.** Verified from PubMed metadata:

> **Weisz-Hubshman M, … Heimer G** — *"…and dysmorphism among Yemenite Jews"*

🔴 **And LEGEND already knew.** Its own splice-transcript census
(`wwox_splice_transcript_census_20260921.md`) attributes this PMID correctly to
**Heimer / Basel-Salmon**. So the registry and the census **disagree with each other about the same
PMID**, and have done since both were written.

**Why this is not cosmetic in this repository specifically.** `research-group-analyst` exists to
assess the group behind a paper before a deep dive; the research-group knowledge base is keyed on
**names**; and `next_scientist_scout_20260921.md` demoted and promoted whole nodes on **author
identity**, having already caught one surname collision (a `Suzuki H` of Keio mistaken for the
`lde` laboratory). **A wrong byline on a consolidated-baseline source is a wrong node, a wrong
credibility assessment, and a wrong independence judgement, all downstream and all silent.** It is
also the third identifier/byline defect recorded in this repository in three days.

## 2 · What the paper actually carries, which is more than the record says

**(a) 🔴 A MEASURED transcript consequence for `c.517-2A>G`.** Verbatim from the abstract:

> *"Complementary DNA sequencing demonstrated that the WWOX c.517-2A > G splice-site variant causes
> skipping of exon six."*

*(The source prints `c.517-2A > G` with spaces and **"exon six"** as a word. Tokens checked; this is
a quotation of an abstract, and an abstract is not a reading.)*

This matters because LEGEND's own census established that, across 20 relevant records, **three**
papers have ever measured a transcript from a WWOX splice allele. **This is one of them, and the
registry does not say so** — its entry gives no indication that it carries RNA-level evidence at
all.

**(b) 🔴 It is also a `Q230P` primary** (`c.689A>C`). **Both worked-example allele classes — the SDR
missense and a canonical splice-acceptor — meet in one 2019 case series**, which the repository has
been reasoning about through two separate literatures.

## 3 · The allele correction this session owes itself

🔴 **The Orchestrator's own brief conflated two acceptor alleles, and Scientist A caught it.**
`c.517-2A>G` is **exon 6**. The acceptor LEGEND has reasoned about throughout — `DL-MECH-045`,
`DL-MOL-011`, `DL-BIO-002`, `TX-001` — is **`c.1057-2A>G`, exon 9**. They sit **~540 coding
nucleotides apart** and, decisively, **in opposite NMD regimes**:

| | `c.517-2A>G` | `c.1057-2A>G` |
|---|---|---|
| Exon | **6** | **9** |
| Position | mid-gene | 🔴 **the LAST exon** (`DL-MECH-045`) |
| Skip consequence | exon = `c.517–c.605` = **89 nt**; `89 mod 3 = 2` ⇒ **frameshift**; PTC far upstream of the last junction ⇒ **NMD predicted** | last-exon lesion ⇒ **escapes NMD** ⇒ truncated protein |
| Therefore | **degraded transcript, no protein** | **stable transcript, truncated protein** |

**An assay designed for one is mis-specified for the other**, and so is a therapeutic argument.
`CLAIM 002` keeps them properly separate; the brief did not. ⚠️ The frame arithmetic above is
**PREDICTED** — derived from the acceptor-to-acceptor interval with **no RefSeq access in this
environment** — while the **exon-six skip is MEASURED** by the source quoted in §2(a). The two must
not be reported at the same confidence. **Cryptic-acceptor potential: NOT ASSESSED.** No SpliceAI or
MaxEntScan result for `c.517-2A>G` exists in LEGEND or within reach, and inventing one would be
invention.

⚠️ And the measured skip **does not** make the NMD prediction safe: the transcript **was
sequenceable in 2019**, so NMD is not absolute here. **No WWOX splice allele has ever been assayed
with an NMD inhibitor**, so the degraded-versus-stable fraction is unknown for both alleles.

## 4 · What is proposed

**(a) `paper_registry_current.md`, `PAPER 025`** — correct the byline and title to the PubMed
record (**Weisz-Hubshman M … Heimer G**), and add to its `Note`:

> Carries a **measured** RNA outcome — cDNA sequencing shows `c.517-2A>G` causes **skipping of exon
> six** — one of only three measured transcripts from any WWOX splice allele. **Also a `Q230P`
> primary** (`c.689A>C`). ⚠️ **Read depth: abstract only.** `CLAIM 018` (`consolidated baseline`)
> and `CLAIM 019` both cite this record; neither is challenged on content.

**(b) `CLAIM 018` / `CLAIM 019`** — no change to either claim's content or status. Add a one-line
`PREMISE` note recording that the cited source is held at **abstract depth** and that its byline was
corrected in this batch.

**(c) `full_text_queue_current.md`** — `FT-117`, already opened, records the depth debt and the
retrievability question. No change proposed here.

**(d) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-22** · *"two surfaces in the same repository that name the same paper agree about it"* ·
> **Why it is FALSE here:** `paper_registry_current.md` and
> `wwox_splice_transcript_census_20260921.md` have named `PMID 30853297` with **different first
> authors** for as long as both have existed, and nothing noticed, because every check verifies a
> record against **itself** and none verifies two records against **each other**. The registry's
> byline is also the input to group-credibility and node-independence judgements, so the error
> propagates into decisions that never mention the paper.
> **Detection rule:** when two surfaces name the same identifier, they are two assertions about one
> fact — compare them. Cheapest form: on any PMID you are already handling, glance at every surface
> that names it before you use any of them.
> ⚠️ **Numbering:** `D-17` is **reserved** (proposed 2026-09-21, **DEFERRED by the operator**, not in
> the ledger). `D-18`–`D-21` are proposed by this session's other candidates. Do not renumber into
> `D-17`.

## 5 · What is explicitly REFUSED

- ❌ **No claim content changes.** `CLAIM 018` and `CLAIM 019` are correct on substance. A wrong
  byline is not a wrong finding, and this candidate does not pretend otherwise.
- ❌ **No promotion of the exon-six skip into a claim.** It is quoted from an **abstract**. It goes
  into the record as what the source states, at the depth the source was read.
- ❌ **No transfer of `DL-MECH-045`'s reasoning to `c.517-2A>G`** — §3 shows why it cannot travel.
- ❌ **No new gate** (§26). One ledger row with a detection rule.

## 6 · Growth delta

`claims +0 · papers +0 · corpus +0`. `PAPER 025` is corrected, not added.

---

*Sources retrieved from **PubMed / PubMed Central**.
🔴 **`PMID 30853297` has NO DOI and NO PMCID in the PubMed ID-converter record** —
`convert_article_ids(["30853297"])` returns the PMID alone, verified 2026-09-21. **No DOI is
asserted here.** An earlier draft of this line carried one reconstructed from the journal; it was
removed rather than published, which is the same near-miss recorded in
`CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01` § attribution, in the same session, by the same
actor. **Twice in one session is a pattern, not an accident: this actor reaches for a plausible
identifier when none is in hand.** Whatever DOI `PAPER 025` currently carries should be treated as
unverified until someone copies it from the publisher's page.
The **byline correction** above **was** verified by direct metadata retrieval and is not affected.
Not medical advice.*
