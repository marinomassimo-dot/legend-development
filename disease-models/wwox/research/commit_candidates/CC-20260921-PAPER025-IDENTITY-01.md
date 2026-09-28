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

## 2bis · 🔴 The sharper diagnosis, found hours later: this is TWO PAPERS CONFLATED

The byline is not a random slip. **`Piard J` is the first author of a different 2019 WWOX paper** —
*"The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and
review of the literature"*, *Genet Med* 2019;**21**(7), established from the erratum
**`PMID 30783266`** (`article_types: Published Erratum`,
DOI [10.1038/s41436-019-0460-y](https://doi.org/10.1038/s41436-019-0460-y)).

So `PAPER 025` holds **the identifier of one paper and the byline of another**:

| | |
|---|---|
| Identifier carried | `PMID 30853297` — Weisz-Hubshman M … Heimer G, *"…and dysmorphism among Yemenite Jews"* |
| Byline carried | *"Piard et al."* — first author of the **WOREE phenotypic-spectrum cohort**, a different paper |

**Checked immediately, and the answer completes the diagnosis rather than deepening it.** The Piard
cohort is **`PMID 30356099`** and it is **not missing** — but it is not a `PAPER` either:

> `CORPUS-STUB-059` / `LIT-0083` · **`Authors: not yet extracted`** · `Short title: corpus paper 59`
> · **and it carries a read receipt.**

🔴 **That is the mechanism, and it is more instructive than the error.** One of the larger
genotype–phenotype series in this disease — 20 additional WOREE cases — has been **read**, and
still sits as an **un-promoted stub whose author field was never filled in**. A record with no
byline cannot defend its own byline. So when *"Piard et al."* was needed somewhere, nothing in the
repository connected that name to `30356099`, and it landed on `30853297` instead.

**Corrected against myself:** the draft of this section speculated the Piard cohort *"may have no
record of its own"*. It has one. **The defect is not a missing paper — it is a read paper left in
a form that carries none of its own identity**, next to a `PAPER` record wearing it.

⚠️ **What the erratum does NOT do**, stated so the word *"Correction"* on a load-bearing cohort
paper is never re-opened in alarm: it records only that *"one patient [was] investigated through
genome sequencing rather than exome sequencing as originally published"*, with amendments to the
Abstract and Methods and added authors. **No case count, genotype, phenotype or outcome changes.**

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

**(c) 🔴 Promote `CORPUS-STUB-059` (`PMID 30356099`) to a `PAPER` record with its authors
extracted.** It is **read, receipted, and cited across the model's cohort reasoning**, and it has
no byline of its own. Correcting `PAPER 025`'s byline without this would fix the symptom and leave
the cause: a read paper with an empty `Authors` field is a name available to be borrowed. Its
erratum `PMID 30783266` (`FT-121`) should be linked to it at the same time, with the note that the
correction is **administrative and changes no case count, genotype, phenotype or outcome**.

**(d) `full_text_queue_current.md`** — `FT-117` records the depth debt on `30853297`; `FT-121`
records the two harvested-but-unregistered records. No change proposed to either here.

**(e) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

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

---

# 🎯 ADDENDUM — 2026-09-23, after the primary source was acquired and read

> **The candidate is NOT propagated by this addendum.** Status remains `PROPOSED — NOT PROPAGATED`.
> What changes is that three of its statements were made at **abstract depth** and can now be made
> at **full-text depth**, and one of its stated refusals can be lifted.

## A1 · The byline correction is now confirmed by a **third, independent** surface

The candidate rested on PubMed metadata versus LEGEND's own splice-transcript census. Two further
independent surfaces now agree, and neither is PubMed:

1. 🟢 **The publisher's own figure package**, slide 1, verbatim: *"Novel WWOX deleterious variants
   cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphism among
   Yemenite Jews · **M. Weisz-Hubshman**, H. Meirson, … D.M. Behar, **G. Heimer** · European Journal
   of Paediatric Neurology · Volume 23 Issue 3 Pages 418-426 (May 2019)."*
   🔴 **`Piard` returns 0 hits across the full body — an *earned* zero** (positive controls `WWOX`
   49, `splice` 18, `patient` 47).
2. 🟢 **Oliver 2023's Supplementary Table S1**, which names *"Weisz-Hubshman M et al. Eur J Paed
   Neurol 2019"* and *"Piard J et al. Genet in Med. 2018"* as **separate rows for separate papers**.

⇒ §1's defect is confirmed at the highest available strength. `D-22`'s detection rule
(*"when two surfaces name the same identifier, they are two assertions about one fact — compare
them"*) is **vindicated**: four surfaces now agree and the registry is the only outlier.

## A2 · 🔴 THE DOI REFUSAL IS LIFTED — and the reason it existed was itself the error it warned about

The candidate's closing block states:

> *"🔴 `PMID 30853297` has **NO DOI and NO PMCID** in the PubMed ID-converter record …
> **No DOI is asserted here.** … Whatever DOI `PAPER 025` currently carries should be treated as
> **unverified** until someone copies it from the publisher's page."*

**That caution was correct practice and is now discharged.** The DOI is verified **twice**, neither
time by reconstruction:

| Route | Value |
|---|---|
| PubMed `get_article_metadata(["30853297"])`, 2026-09-23 | `doi: 10.1016/j.ejpn.2019.02.003`, `pii: S1090-3798(18)30411-2` |
| The publisher's own file, supplied by the Operator | `PIIS1090379818304112.pdf` — **the filename IS the PII**, `S1090-3798(18)30411-2`, character-for-character |

🎯 **And the root cause is a rediscovery of a lesson this repository had already learned and then
re-broke.** `FT-122` records it for `PMID 29808465`: *"a PMC-backed converter's silence is evidence
about PMC, never about the article."* `convert_article_ids` returned the bare PMID for `30853297`
and that silence was again read as *"no DOI exists"* — **the identical inference, about a second
paper, in the same repository, days apart.** The correct statement was always the narrower one:
*the ID converter returned no DOI*, which is a fact about the converter.

🔴 **Consequence for proposal (a):** the byline and title correction should now land **with** the
verified DOI, not with a DOI-shaped hole.

## A3 · Proposal (c) — `CORPUS-STUB-059` can now be promoted with **verified** metadata

The candidate asked to promote `PMID 30356099` to a `PAPER` record *"with its authors extracted"*,
on the ground that *"a read paper with an empty `Authors` field is a name available to be borrowed."*
Retrieved 2026-09-23:

> **Piard J**, Hawkes L, Milh M, Villard L, … Kini U, Philippe C. *"The phenotypic spectrum of
> WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature."*
> **Genet Med 2019;21(6):1308–1318** · `doi:10.1038/s41436-018-0339-3` · `PMC6752669` ·
> online **2018-10-25**.

🔴 **And the online-first/issue-year trap is live for this record specifically.** Oliver's Table S1
cites it as *"Piard J et al. Genet in Med. **2018**"*; PubMed's citation block says **2019**.
**One paper.** A `PAPER` record created from Oliver's string alone would duplicate the one created
from PubMed's. This is exactly the duplicate class the Operator brief §2 names, and it is **not**
hypothetical here.

## A4 · The read-depth caveat in proposal (a) is now stale

Proposal (a) asks to add *"⚠️ **Read depth: abstract only.**"* to `PAPER 025`'s note.
🔴 **That line must not land as written.** The paper was read at full-body depth on 2026-09-23 —
`FTR-20260923-30853297-01`, `partial_fulltext_read`, all nine body pages plus the publisher figure
package, `figures: read`, `supplementary: not_present`.

**Replacement wording proposed**, and it is *stronger* than the original because the exon-six result
is no longer quoted from an abstract:

> Carries a **measured** RNA outcome — RT-PCR on **blood**-derived cDNA across exon 6 gives products
> of **593 bp** (wild type) and **504 bp** (mutant), an **89 bp** difference equal to the length of
> exon 6, in the homozygote *"only the 504 bp band"*. 🟡 **Sequencing is stated in the abstract
> AND in Methods §2.4** (*"gel electrophoresis and sequencing by ABI Prism 3100 Genetic Analyzer"*),
> while the **Results as presented** document the consequence through the 593/504 bp products and the
> stated 89 bp exon-six deletion, without displaying a junction chromatogram. Also a `Q230P`
> primary (`c.689A>C`): four carriers, all within one family, **zero homozygotes**. 🔴 **The
> 1:177 founder carrier rate measured in this paper (2/353 controls) belongs to `c.517-2A>G`
> alone**; no founder-population denominator of any kind was measured for the missense allele, so
> the rate must never be attached to it. ⚠️ **No protein work of any kind**
> (`Western` 0, earned), so `CLAIM 030`'s `PREMISE: DETECTION_FLOOR` is untouched by this source.

## A5 · What is still explicitly REFUSED — unchanged, and one refusal now *strengthened*

§5's four refusals all stand. One is reinforced by the reading rather than relaxed:

- ❌ **Still no promotion of the exon-six skip into a claim.** It is no longer abstract-quoted, but
  the Results **display** sizes rather than a junction read, from **one lane, one individual**, with no
  densitometry, no replicate and no NMD block. 🔴 **The full text made the evidence *more* precisely
  bounded, not more promotable.** ⚠️ **Corrected 2026-09-23:** an earlier draft of this addendum said the
  abstract *"over-claims its own Results"*. It does not — Methods state the sequencing. The phrasing is
  withdrawn and must not be propagated.
- ❌ **Still no claim that the allele is leaky or non-leaky.** The paper shows **no *detected*
  correct splicing**; it does not exclude it and never claims to. The qPCR amplifies **exons 8–9,
  downstream of exon 6**, so it counts the skipped transcript too — the residual ~10 % mRNA is
  **not** evidence of residual correct splicing.

## A6 · Ten source-internal defects are now on record

Logged in [`ft117_weiszhubshman2019_fulltext_read_20260923.md`](../../analysis/ft117_weiszhubshman2019_fulltext_read_20260923.md) §5.
The two that bear on any future use of this paper's data:

1. 🔴 **The Fig. 4C legend calls `V-2` *"the compound heterozygote father"*, while Fig. 1C prints his
   genotype as `c.517-2A>G/WT` — a simple carrier.** The only gel is family **3**; there is **no
   family-2 lane**. So the paper's compound-heterozygote two-band statement is **prose with no shown
   data**.
2. 🔴 **The control count is internally inconsistency:** *"A total of 12 controls"* versus *"four
   different runs (4 different controls to each run)"* = **16**. The `P = 0.0003` is reported
   against **n = 1 patient**, so it is carried as **descriptive**.

**Growth delta unchanged: `claims +0 · papers +0 · corpus +0`.** `PAPER 025` is corrected, not added;
`CORPUS-STUB-059` is promoted, not created.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `splice_sdr` · **Verdict: split.**
- **(a) identity of `PAPER 025` — byline, title, short title, DOI → `READY_MINOR`** (ops below).
- **(c) promotion of `CORPUS-STUB-059` / `LIT-0083` with verified metadata → `READY_MINOR`** (ops below).
- **(a)'s and A4's NOTE CONTENT — the measured-RNA wording with 593/504 bp, the 1:177 carrier rate and
  the Methods § 2.4 quotation → `DEFERRED`.** One line why: **the evidence bytes are gone from this
  checkout** — `FTR-20260923-30853297-01/-02` declare
  `files/fulltext/PMID30853297_WeiszHubshman2019.pdf` and the publisher figure package, and **neither
  file exists here** (`files/` is gitignored, so a branch transports the receipt and not the evidence),
  while the article has **no PMC deposit** and is **not open access** on any free route (Unpaywall
  `is_oa: false`; Europe PMC *"Subscription required"*). No locator can be persisted against bytes that
  are absent, and no paid access was attempted. **What exactly would unblock it:** the operator-supplied
  `PIIS1090379818304112.pdf` restored to `files/fulltext/PMID30853297_WeiszHubshman2019.pdf`, fingerprinted,
  a deterministic extracted TXT declared as `article_text`, and then the three A4 quotations persisted as
  locators in a new `deepdive_manifests/PMID30853297.json`.
- **(b) the `PREMISE` note on `CLAIM 018` / `CLAIM 019` → `CLOSE`, closing status `NOT INTEGRATED`.**
  Evidence: A4 establishes that *"Read depth: abstract only"* is **false** — the paper was read at body
  depth on 2026-09-23 — so the abstract-depth `PREMISE` note (b) proposes would enter the claim registry
  as a statement contradicted by the receipt ledger. It must not land in any form, and nothing replaces
  it: the claims' content was never in question (§5).

**`context_policy` declared: `QUESTION_DRIVEN`** — the questions were bibliographic identity (who wrote
`PMID 30853297`, what is its title, what is its DOI, and what is `PMID 30356099`'s byline) and the
presence of the declared evidence artifacts. Registry records were reached with `registry_records.py`.

### 1 · What was done

1. **The byline, title and DOI were re-verified at the source** — PubMed metadata, retrieved 2026-09-27:
   first author **Weisz-Hubshman M**, last author **Heimer G**, 24 authors, title *"Novel WWOX
   deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and
   dysmorphism among Yemenite Jews"*, `Eur J Paediatr Neurol` 2019;**23**(3):418–426,
   **`doi: 10.1016/j.ejpn.2019.02.003`**, `pii: S1090-3798(18)30411-2`. This is a **fourth** surface
   agreeing with §1 and A1, and the registry remains the only outlier. According to PubMed;
   [DOI](https://doi.org/10.1016/j.ejpn.2019.02.003).
2. **`PMID 30356099`'s metadata were verified for the promotion** — **Piard J**, Hawkes L, Milh M,
   Villard L, … Kini U, Philippe C; *"The phenotypic spectrum of WWOX-related disorders: 20 additional
   cases of WOREE syndrome and review of the literature"*; `Genet Med` 2019;**21**(6):1308–1318;
   `doi: 10.1038/s41436-018-0339-3`; `PMC6752669`; **electronic publication 2018-10-25**, which is the
   online-first/issue-year trap A3 names, live for this record. According to PubMed;
   [DOI](https://doi.org/10.1038/s41436-018-0339-3).
3. 🔴 **An evidence-locality finding, recorded because it bears on more than this candidate.** Both
   receipts for `PMID 30853297` name artifacts that are **not present in this checkout**, so a reading
   this repository counts as done cannot be re-verified here at all. The receipt is historically true and
   operationally unverifiable — exactly the condition `fulltext_read_receipt.md` warns about — and it is
   what makes A4's note content undeliverable rather than merely unfinished.
4. **No reading was performed for this item**, and none is claimed: nothing here rests on the body of
   either paper. No receipt is written by this package for `PMID 30853297` or `PMID 30356099`.

### 2 · Exact operation list for the batch executor

#### OP 1 — `paper_registry_current.md` · `PAPER 025` (**FULL REWRITE** file; described as full-rewrite edits)
- `replace-within`: old `**Short title:** Piard 2019 EJPN exon 6 / Q230P` → new `**Short title:** Weisz-Hubshman 2019 EJPN exon 6 / Q230P`
- `replace-within`: old `**Full title:** Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphic features` → new `**Full title:** Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphism among Yemenite Jews`
- `replace-within`: old `**Authors:** Piard et al.` → new `**Authors:** Weisz-Hubshman M, Meirson H, Michaelson-Cohen R, Beeri R, Tzur S, Bormans C, Modai S, Shomron N, Shilon Y, Banne E, Orenstein N, Konen O, Marek-Yagel D, Veber A, Shalva N, Imagawa E, Matsumoto N, Lev D, Lerman Sagie T, Raas-Rothschild A, Ben-Zeev B, Basel-Salmon L, Behar DM, Heimer G`
- `replace-within`: old `**Journal/source:** *European Journal of Paediatric Neurology*` → new `**Journal/source:** *Eur J Paediatr Neurol* 2019;23(3):418-426`
- `replace-within`: old `**Identifier:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003` → new `**Identifier:** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003 (verified at PubMed and against the publisher PII S1090-3798(18)30411-2, 2026-09-27) / no PMCID`
- `replace-within`: old `**Note:** important for allele-specific logic and exon-based pathogenicity` → new

```text
**Note:** important for allele-specific logic and exon-based pathogenicity. 🔴 **Byline corrected 2026-09-27:** the record carried *"Piard et al."*, the first author of a DIFFERENT 2019 WWOX paper (`PMID 30356099`, Genet Med, the 20-case WOREE cohort) — the identifier of one paper with the byline of another. Corrected against four independent surfaces (PubMed metadata, the publisher's own figure package, this model's splice-transcript census, and Oliver 2023's Table S1, which lists the two papers as separate rows). Nothing about `CLAIM 018` or `CLAIM 019` changes: a wrong byline is not a wrong finding. ⚠️ **Read depth is NOT abstract-only** — `FTR-20260923-30853297-01/-02`, `partial_fulltext_read`, body pages read — and any note asserting abstract depth for this record contradicts the receipt ledger. 🔴 The declared evidence artifacts are **absent from this checkout**, so the reading cannot be re-verified here; the content of that reading (RT-PCR product sizes, the founder carrier rate, Methods § 2.4) is therefore NOT written into this record until the bytes are restored and locatored.
```

#### OP 2 — `paper_registry_current.md` · `CORPUS-STUB-059` → a new `PAPER` record (full rewrite)
Promote with the verified metadata of item 2 above. Required fields as drafted:
`Short title: Piard 2019 Genet Med — WOREE phenotypic spectrum, 20 additional cases` ·
`Authors:` the verified byline (Piard J … Philippe C) · `Journal/source: *Genet Med* 2019;21(6):1308-1318` ·
`Identifier: PMID 30356099 / PMCID PMC6752669 / DOI 10.1038/s41436-018-0339-3` ·
`Status: processed` · `Evidence depth: partial_fulltext_read (FTR-20260811-30356099-01, FTR-20260921-30356099-02)` ·
`Role: largest WOREE cohort in the model's cohort reasoning; genotype-phenotype correlation, null genotypes most severe` ·
`Note:` carry (i) the erratum `PMID 30783266` link with *"administrative: one patient investigated by genome rather than exome sequencing; no case count, genotype, phenotype or outcome changes"*, and (ii) 🔴 **the online-first trap, by name:** *"issue year 2019, electronic publication 2018-10-25; Oliver 2023's Table S1 cites it as 'Piard J et al. Genet in Med. 2018'. ONE paper — a PAPER record created from Oliver's string would duplicate this one."*
**The stub is replaced by the PAPER record, not kept beside it**, and `CORPUS-STUB-059` is removed in the
same rewrite so that no record with an empty `Authors` field survives for a byline to be borrowed from
again.

#### OP 3 — `literature_tracking_log_current.md` · `LIT-0083` (record-scoped)
- `replace-within`: old `**Short title:** corpus paper 59` → new `**Short title:** Piard 2019 Genet Med — WOREE phenotypic spectrum (20 additional cases)`
- `replace-within`: old `**Authors:** not yet extracted` → new `**Authors:** Piard J, Hawkes L, Milh M, Villard L, Borgatti R, Romaniello R, Fradin M, Capri Y, Héron D, Nougues MC, Nava C, Tarta Arsene O, Shears D, Taylor J, Pagnamenta A, Taylor JC, Sogawa Y, Johnson D, Firth H, Vasudevan P, Jones G, Nguyen-Morel MA, Busa T, Roubertie A, van den Born M, Brischoux-Boucher E, Koenig M, Mignot C, Kini U, Philippe C`
- `replace-within`: old `**Year:** unknown` → new `**Year:** 2019 (issue) / 2018-10-25 (online first) — one paper, two citable years`
- `replace-within`: old `**Source type:** not yet screened` → new `**Source type:** primary cohort + review`
- `replace-within`: old `**Journal/source:** not yet extracted` → new `**Journal/source:** Genet Med 2019;21(6):1308-1318`
- `replace-within`: old `**Status:** discovered` → new `**Status:** processed`
- `replace-within`: old `**Next action:** screening and tier assignment` → new `**Next action:** none — promoted to a PAPER record 2026-09-27; erratum PMID 30783266 linked (administrative)`

#### OP 4 — `dismissal_ledger_current.md` · `D-22` row
As drafted in §4(e), **number allocated by the batch** (`D-17` reserved). Text unchanged.

### 3 · What is still pending

The three A4 quotations, and with them A4's replacement `Note` wording and the `1:177`-belongs-to-the-splice-allele
caveat. All three are **one restored PDF away**, and none of them is needed for the identity ops above.

> ⚠️ **Record-scoped, and one of these strings is not unique:** `**Authors:** not yet extracted` occurs
> **145** times in `literature_tracking_log_current.md` on the current tree. The executor addresses
> `LIT-0083` and replaces within that record; the `PAPER 025` strings above were each measured as
> occurring **exactly once** in `paper_registry_current.md`.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

**(a)** `OP 1` applied to `PAPER 025` (short title, full title, byline, journal, identifier, and the byline-correction note). **(c)** `OP 2` applied: `CORPUS-STUB-059` is **replaced** by the new record `PAPER 117` and `OP 3` completes `LIT-0083` and points it there — papers 106 → 107, corpus 361 → 360, declared with `growth_anchors.py record`. **(e)** the ledger row landed as **`D-22`**, the number the candidate proposed, with `D-17` left reserved. 🔴 **DEFERRED, for the reason the readiness section gives:** the A4 note content (the 593/504 bp measured-RNA wording, the 1:177 carrier rate, the Methods § 2.4 quotation) — the evidence bytes are absent from every checkout reachable here, and no locator may be written against bytes nobody can open. **(b)** stays **NOT INTEGRATED**: the abstract-depth `PREMISE` note contradicts the receipt ledger and must not land in any form.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `DEFERRED`.** **Confirmed deferred, and the reason was re-measured rather than carried.** The A4 note content — the 593/504 bp measured-RNA wording, the 1:177 carrier rate and the Methods § 2.4 quotation — needs the operator-supplied `PIIS1090379818304112.pdf`. Searched this session across the root checkout's whole `files/` tree (`fulltext/`, `supplement/`, `supplements/`, `page_renders/`, `figure_renders/`): **no file matching that PII or that paper exists in any of them**. No locator may be written against bytes nobody can open. **What would unblock it:** the operator's PDF restored to `files/`, fingerprinted, declared in a manifest with its acquisition recipe, and the three A4 quotations persisted as verbatim locators. Everything else in this candidate landed in `BATCH_20260927_003`; proposal **(b)** stays `NOT INTEGRATED` for the reason that batch gave — an abstract-depth `PREMISE` note contradicting the receipt ledger must not land in any form.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.

---

## BATCH DISPOSITION — `BATCH_20260928_007` (2026-09-28, ACTOR_ID `orchestrator`), append-only

**Nothing above this line was rewritten.** Operator instruction, verbatim: *«procedi sempre»*. The residue was re-derived against `main` `7352d52`; every op was produced by a reader other than the batch actor and verified by the batch actor against the source bytes before propagation.

**Verdict:** PROPAGATED

The A4 note is propagated to `PAPER 025`. The operator's PDF was found in the upload cache and restored byte-identical to the receipted fingerprint; the three A4 quotations (plus the Fig. 4C legend) are persisted as `rendered_text` locators in `deepdive_manifests/PMID30853297.json` (the text layer is refused by the suspect-surface screen) under `FTR-20260928-30853297-03`. 🔴 **A blind locator audit changed the note:** Fig. 4C has no family-2 lane (the two-band lane belongs to a family-3 relative whose legend genotype label disagrees with the pedigree; pedigree detail omitted in this public edition); the Abstract states exon-six skipping as *demonstrated* while the Results hedge it; gnomAD 3/246,218 is the missense allele's only population figure. Two defects in the prior receipt (a *no space characters* instrument claim; *Redload/PerkinElmer*) are corrected forward in the new receipt. Proposal (b) stays NOT INTEGRATED.

**Not medical advice.**
