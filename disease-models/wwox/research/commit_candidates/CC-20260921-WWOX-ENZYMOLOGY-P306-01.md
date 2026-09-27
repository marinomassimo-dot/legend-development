# COMMIT CANDIDATE — CC-20260921-WWOX-ENZYMOLOGY-P306-01

**Source:** a field-wide census run by Scientist A on the node
`MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE`
([`wwox_sdr_function_per_molecule_census_20260921.md`](../../analysis/wwox_sdr_function_per_molecule_census_20260921.md)),
**independently re-verified by the Orchestrator** against PubMed metadata and against
`registry_records.py`. **No reading occurred** — the paper is abstract-only from this
environment — and **no receipt is claimed**.
**Ledger:** `fulltext_receipts.py verify` → **OK: 188 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — one corpus record re-tiered and queued, two prose narrowings, one
ledger row. **No claim added, reversed or narrowed. No status changed.**
**Target:** `working_model_version` MINOR bump at batch time. No `BLOCCO 1` change.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** No canonical claim is touched. What changes is a **reading priority**, a
**therapeutic-strategy obstacle line**, and a **statement of absence** that turns out to be false.

---

## 1 · The finding

> 🔴 **An assay of WWOX catalysis exists. It has existed since 2011. It is in LEGEND's own
> registry, tiered `C`, marked `background only`, and has never been read.**

**PMID 21476439** — Sałuda-Gorgul A, Seta K, Nowakowska M, **Bednarek AK**, *Z Naturforsch C J
Biosci* 2011;66(1–2):73–82, **"WWOX oxidoreductase — substrate and enzymatic characterization."**

Verbatim, from the PubMed metadata abstract (copied in the same act; **no DOI is present in the
record and none is asserted here**):

> *"Due to its potential role in sex-steroid metabolism, using two bacterial expression systems,
> we have cloned WWOX fusion proteins showing oxidoreductase activity in a crude extract, defined
> a course of enzymatic reactions for selected steroid substrates, and **determined related Km
> values**."*

> *"Our results show that **the SDR domain of the WWOX protein has dehydrogenase activity and is
> reactive both in the presence of NAD+ and NADP+ for all examined steroid substrates**."*

> *"On the other hand, with the same substrates and **reduced cofactors (NADH and NADPH) reduction
> activity was not observed**."*

**Its state in LEGEND, verified with `registry_records.py get --pmid 21476439`:**

| Field | Value |
|---|---|
| Record | `CORPUS P306` / `LIT-0306` |
| `Tier (FASE 1)` | **C** |
| `clinical relevance` | **LOW** |
| `Filter decision` | **background only** |
| `Priority` | **low / background** |
| `Date processed` | **triage only** (2026-04-18) |
| `Claim links` | **none — triage only** |
| Receipts | `fulltext_receipts.py status --pmid 21476439` → **`[]`** |

## 2 · Why it matters, stated without inflating it

`sdr_missense_readout_assessment_20260920.md` asked whether any readout of WWOX **SDR function**
exists, answered **`NO`** — *"Not 'not yet', not 'partially'"* — and closed with:

> *"Identifying a physiological substrate is the experiment that would make a genuinely
> complementary second readout possible. It is not in this corpus, and **on the census run here it
> is not anywhere**."*

**That last clause is false, and the correction is owed.** An *in-vitro* activity with Km values
on steroid substrates was published once. ⚠️ **What does NOT change** — and this is the larger
half:

- the activity was measured **in a crude extract**, not on purified enzyme;
- **wild-type protein only** — **no disease allele was tested**;
- **no catalytically-dead triad control** (the `S281A / Y293F / K297A` mutants exist only as
  *"Aldaz laboratory unpublished observations"*);
- **no folded-monomer normalisation**, so it is an activity *report*, not an assay;
- and the substrates are **steroids**, consistent with WWOX's highest expression being testis,
  prostate and ovary — **not** a demonstrated neural substrate.

⇒ **An assay of WWOX *catalysis* exists once. An assay of WWOX *function per molecule* — the thing
`TX-003` is blocked on — still exists nowhere, for any allele.** `PROTEIN AMOUNT` and `PROTEIN
FUNCTION` remain different questions, and only the first has ever been measured on a WOREE allele.

## 2bis · 🔴 The two halves stated as a rule, on Operator note (2026-09-21)

Both halves are already argued above; they are restated here as a standing rule because they are
the two ways this finding will be mis-carried, and they fail in **opposite** directions.

> ✅ **HALF ONE — treat the 2011 Km / cofactor / substrate evidence as a REAL HISTORICAL
> BIOCHEMICAL RESULT until a primary reading determines otherwise.** It is a peer-reviewed primary
> reporting cloned fusion proteins, a defined steroid-substrate panel, cofactor dependence and Km
> values. **It is abstract-only from here, which is a statement about this environment, not about
> the paper.** It must not be discounted, hedged into vagueness, or described as "claimed" —
> `PREMISE: UNREAD_PRIMARY` is the correct tag, and it means *owed a reading*, **not** *doubted*.

> 🔴 **HALF TWO — do NOT infer that it provides a validated functional assay for disease alleles.**
> Crude extract, **wild-type protein only**, **no disease allele of any kind**, no
> catalytically-dead triad control, no folded-monomer normalisation, and **no physiological
> substrate assigned**. An activity **report** is not an **assay**. Nothing about `Q230P`,
> `P47T`, `G372R` or any other variant follows from it.

**Why both are needed together.** Half one alone invites *"WWOX catalysis is characterised"*, which
would make `TX-003` look unblocked when it is not. Half two alone invites *"there is no WWOX
enzymology"*, which is the sentence this candidate exists to withdraw. 🔵 **The honest position is
the narrow one: an assay of WWOX CATALYSIS exists once, and an assay of FUNCTION PER MOLECULE
exists nowhere, for any allele.**

⚠️ **And one live contradiction sits across the substrate question** and must travel with any use of
this result: a 2015 **review** proposes the catalytic domain is a **retinal** oxidoreductase acting
**reversibly** on all-trans-retinal, while the 2011 primary observed **oxidation only** — *"with the
same substrates and reduced cofactors (NADH and NADPH) reduction activity was not observed."*
**They disagree on reversibility, which is the one property an assay design must choose, and no
experiment has ever been run that could tell them apart.**

## 3 · How it was missed, and the root cause that is now fixed

`unread_gold.py` exists precisely to catch this (failure mode `FM-011`). It missed this paper on
**both** of its paths, for **three** independent reasons, all measured today:

1. 🔴 **Its selector regexes matched the wrong field spelling.** `tier` looked for
   `**Tier (PHASE 1):**` — the registry writes `**Tier (FASE 1):**`, **187 records, zero in
   English**. `relevance` looked for `**Relevance:**` — the registry writes
   `**clinical relevance:**`, **254 records, zero of the short form**. Both matched **nothing**,
   so the default filter could never fire and printed *"No unread Tier-A / Relevance-HIGH
   CORPUS"* — **a parse failure wearing the costume of an all-clear**. This is the repository's
   own §3 rule turned on its own instrument: *a zero from a parser is not evidence of absence
   until the parser is shown to be reading the document.*
2. 🔴 **Even parsing correctly, the default filter is structurally blind here.** Of 164 unread
   corpus placeholders, **155 are `C` / `LOW`** and **none is `A` / `HIGH`**. The FASE-1 triage
   gave the whole 221–400 window the same label, so the tier field carries no discriminating
   information and a tier-gated tool cannot find gold in it **even when it works**. It can only
   find gold that triage already called gold — which is the one case that needs no tool.
3. 🔴 **The mechanism lens had no vocabulary for catalysis.** `MECHANISM_RE` hunted allele,
   protein fate, proteostasis and interaction terms — the *proteostasis* half of the missense
   question (**is the protein there?**) — and had no term at all for the other half (**does the
   protein work?**): no `enzym`, `substrate`, `catalytic`, `oxidoreduct`, `dehydrogenas`, `Km`,
   `cofactor`, `NAD`. Its one "function" group was `binding|interact|partner|rescue`, i.e. exactly
   the interaction proxies the SDR-readout assessment had **rejected** as not being measures of
   SDR function. **The lens encoded the same blind spot the science had.**

**Repaired at T0, with regressions** (`framework/scripts/test_unread_gold.py`, 12 tests, **mutation-tested:
4 fail when the fixes are reverted**): both field spellings accepted, a catalysis clause added,
and the tool now **cross-checks the receipt ledger**. Effects, measured:

- `P306` and five other records now surface on the mechanism lens (79 → 85);
- **19 of 164 placeholders were found to be advertised as "never deep-dived" while carrying
  complete- or partial-read receipts** — stale rows that would each have dispatched duplicate
  work, the `FT-102` failure waiting to happen 19 more times. They are **annotated, not hidden**:
  a stale registry row is a finding.

## 4 · What is proposed

**(a) `CORPUS P306` → full-text queue at HIGH, and acquisition packet.** It is **not** promoted to
a `PAPER` record: no reading stands behind it and it must not acquire the appearance of one.

> **`FT-130` / packet item `A11` — `PMID 21476439`.** ⚠️ *This line previously cited a queue
> number that was never written; the dead pointer and its repair are recorded in `FT-130`.* Re-tier `CORPUS P306` from `C` / `LOW` to
> **`Tier: A` / `clinical relevance: HIGH`**, `Filter decision: **deep-dive — full text required**`,
> with the re-tier reason recorded in `Note`. **Acquisition status:** `convert_article_ids` returns
> the PMID alone — **no PMCID**; the metadata record carries **no DOI**; *Z Naturforsch C*
> (De Gruyter), 2011. **Not retrievable by any automated route in this environment.**
> **What to ask a human for, precisely:** the **Km table** and the **substrate list with cofactor
> conditions**, plus the Methods paragraph describing the expression construct and whether any
> purification step preceded the activity measurement.

**(b) Narrow `sdr_missense_readout_assessment_20260920.md` § 6.** Append a dated correction (do not
rewrite — the file is append-only in practice and its reasoning is sound):

> 🔴 **Correction, 2026-09-21.** *"on the census run here it is not anywhere"* is too strong and is
> withdrawn. **`PMID 21476439` (2011) measured WWOX dehydrogenase activity on steroid substrates
> with NAD⁺ and NADP⁺ and reported Km values** — in a crude extract, on wild-type protein, with no
> disease allele and no catalytically-dead control. The narrowed statement that survives: **no
> *physiological* substrate is assigned, and no function-per-molecule assay exists for any allele.**
> The paper was in this repository as `CORPUS P306`, `background only`, throughout.

**(c) `TX-003` — narrow the obstacle line.** Current text: *"WWOX is an oxidoreductase with
undefined physiological substrate/activity"*. Proposed:

> WWOX's SDR domain has **measured in-vitro dehydrogenase activity** on steroid substrates with
> both NAD⁺ and NADP⁺, and published Km values (`PMID 21476439`, 2011) — **oxidation only; no
> reduction activity was observed with NADH/NADPH**. ⚠️ **This is not yet an assay**: crude
> extract, wild-type only, no disease allele, no catalytic-triad control, no folded-monomer
> normalisation, and no **physiological** substrate assigned. **`TX-003`'s blocker is therefore
> narrower than "no activity is known" and sharper than it was: the activity exists on paper and
> has never been pointed at an allele.** `PREMISE: UNREAD_PRIMARY` — abstract-only, acquisition
> item `A11`.

**(d) `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`** — one row:

> **D-19** · *"the tool that finds unread gold reported none, so there is none"* · **Why it is
> FALSE here:** `unread_gold.py` printed *"No unread Tier-A / Relevance-HIGH CORPUS"* while its two
> selector regexes matched **zero** records in the live registry — it was not reporting a clean
> registry, it was reporting that it could not read one. **The repository's own rule, applied to
> its own instrument: a zero from a parser is not evidence of absence until the parser is shown to
> be reading the document.** And a second, subtler half: even once parsing, a **tier-gated** filter
> over a corpus where 155 of 164 unread records share one tier can only surface what triage already
> ranked — it cannot correct triage, which is the only job it has.
> **Detection rule:** before trusting any selector-based tool's empty result, check that its
> selectors match **more than zero** records in the live document.

⚠️ **Numbering:** `D-17` was proposed on 2026-09-21 and **DEFERRED by the operator**; it is **reserved, not free**, and is not in the ledger. This session's candidates propose `D-18`–`D-23`, one each. **Do not renumber into `D-17`.**

## 5 · What is explicitly REFUSED

- ❌ **No claim is created.** An abstract is not a reading. Nothing about WWOX enzymology enters
  the claim registry from this candidate.
- ❌ **No promotion to `PAPER`.** `CORPUS P306` becomes a **queued** record, not an integrated one.
- ❌ **No neurosteroid bridge.** The substrates are steroids and the brain has neurosteroids; that
  is a *resemblance*, not evidence, and it is named here only to be refused until someone measures
  a neural substrate.
- ❌ **No new gate, auditor or registry** (§26). The repair is to an **existing, already-routed
  tool**, with regressions — and one ledger row carrying a detection rule.
- ❌ **`TX-003`'s score does not move.** A wild-type in-vitro activity with no allele arm changes
  the *description of the blocker*, not the *probability of the strategy*.

## 6 · Growth delta

`claims +0 · papers +0 · corpus +0`. `CORPUS P306` is **re-tiered and queued**, not added.

---

*Sources retrieved from **PubMed / PubMed Central**. `PMID 21476439` carries no DOI in its PubMed
record; none is invented here. Other DOIs — [24932569](https://doi.org/10.1016/j.bbcan.2014.06.001) ·
[38161429](https://doi.org/10.3390/ijms25010316).
Not medical advice.*

---

## BATCH DISPOSITION — `BATCH_20260927_001` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** DEFERRED

Deferred by this batch's own scope: the Km and cofactor statements it would write into `TX-003` rest on the PubMed **abstract** only — the paper is unacquirable on every route (`FT-130`: no DOI, no PMC), so no receipt and no verbatim locator is possible — and this batch does not write abstract-depth quantities into a therapeutic record. The re-tier of `CORPUS P306` and `LIT-0306` travels with the same candidate and is held with it rather than split, so that the tier and the reason land together. The optional `D-19` row is not landed.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `splice_sdr` · **Verdict: split, and the split is the
point.**
- **(a) re-tier of `CORPUS P306` / `LIT-0306`, with a corrected acquisition line → `READY_MINOR`** (ops
  below).
- **(b) narrowing of `sdr_missense_readout_assessment_20260920.md` § 6 → APPLIED OUTSIDE BATCH** (analysis
  file, non-canonical, append-only respected).
- **(c) `TX-003`'s obstacle line → `DEFERRED`.** One line why: the Km / cofactor / substrate statements
  rest on the **PubMed abstract only**, no receipt and no verbatim locator is possible while the paper is
  unread, and this package does not write abstract-depth quantities into a therapeutic record. What would
  unblock it: **the full text** (see the corrected route below), then a receipt and locators for the Km
  table and the substrate/cofactor list.
- **(d) the `D-19` row → `READY_MINOR`**, number unallocated (the batch allocates `D-18`+ in one pass;
  `D-17` is reserved, operator-deferred).

**`context_policy` declared: `QUESTION_DRIVEN`** — the question was the paper's acquisition state and
nothing about its content; the registry record was reached with `registry_records.py get --pmid 21476439`
and the queue entry read at its own lines.

### 1 · 🔴 The acquisition verdict in `FT-130` and in §4(a) is WRONG, and the correction is cheap

`FT-130` records *"`PMID 21476439` · no DOI · no PMCID"* and *"all consulted routes agree: no DOI, no PMC
deposit"*, on `convert_article_ids`, `get_article_metadata` and `get_copyright_status`. Re-checked
2026-09-27 on routes **outside** that family:

| route | result |
|---|---|
| Crossref bibliographic query | **`DOI 10.1515/znc-2011-1-210`** — *"WWOX Oxidoreductase – Substrate and Enzymatic Characterization"*, *Zeitschrift für Naturforschung C*, 2011 (a legacy `10.5560/znc.2011.66c0073` resolves to the same article) |
| Unpaywall on that DOI | `is_oa: true`, one OA location, publisher-hosted PDF |
| OpenAlex on that DOI | `is_oa: true`, `oa_status: hybrid`, `any_repository_has_fulltext: false` |
| direct fetch of the publisher PDF URL | **HTTP 202, zero bytes** — an automated-traffic challenge, on two publisher hosts and on the HTML surface too |

🔴 **So the paper is not *"not retrievable by any automated route"* because it has no digital deposit; it
is unretrieved because the publisher refuses automated fetches.** Those are different blockers with
different unblocks, and the second one costs a human **one click**.

⚠️ **And the methodological lesson is sharper than the one `FT-130` drew.** That entry congratulated
itself on using *"two independent routes… all consulted routes agree"*. **All three were PubMed-family
routes.** Agreement among siblings is not independence — and this is the same error class the entry was
written to avoid, one level up. That belongs in the dismissal ledger next to `D-19`, and is proposed
below as one row.

### 2 · Exact operation list for the batch executor

#### OP 1 — `paper_registry_current.md` · `CORPUS P306` (**FULL REWRITE** file; described as full-rewrite edits)
- `replace-within`: old `**Tier (FASE 1):** C` → new `**Tier (FASE 1):** A`
- `replace-within`: old `**clinical relevance:** LOW` → new `**clinical relevance:** HIGH` *(within the `CORPUS P306` record only)*
- `replace-within`: old `**Role:** background corpus only` → new `**Role:** deep-dive — full text required; the only published assay of WWOX catalysis`
- `replace-within`: old `**Identifier:** PMID 21476439` → new `**Identifier:** PMID 21476439 / DOI 10.1515/znc-2011-1-210`
- `replace-within` the `Note`: old

```text
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.
```

  new

```text
**Note:** FASE 1 triage 221–400 — no deep-dive performed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration. 🔴 **Re-tiered 2026-09-27 (C / LOW → A / HIGH):** this is the only published measurement of WWOX catalytic activity — dehydrogenase activity on steroid substrates with NAD⁺ and NADP⁺ and published Km values, oxidation only (abstract depth; `PREMISE: UNREAD_PRIMARY`, no receipt, no locator). **Acquisition, corrected:** a DOI DOES exist — `10.1515/znc-2011-1-210` — and Unpaywall and OpenAlex both classify the article hybrid open access with a publisher-hosted PDF; the publisher answers automated fetches with HTTP 202 and zero bytes. The blocker is an automated-traffic challenge, **not** the absence of a deposit: one human fetch of the publisher PDF closes it, at no cost (`FT-130`, packet item `A11`). **NOT promoted to a PAPER record:** no reading stands behind it.
```

#### OP 2 — `literature_tracking_log_current.md` · `LIT-0306` (record-scoped)
- `replace-within`: old `**Filter decision:** background only` → new `**Filter decision:** deep-dive — full text required`
- `replace-within`: old `**Tier:** C` → new `**Tier:** A`
- `replace-within`: old `**clinical relevance:** LOW` → new `**clinical relevance:** HIGH`
- `replace-within`: old `**Identifier:** PMID 21476439` → new `**Identifier:** PMID 21476439 / DOI 10.1515/znc-2011-1-210`
- `replace-within`: old `**Next action:** background-only; escalate only on convergence signal` → new `**Next action:** record as UNACQUIRED, not unread — hybrid-OA publisher PDF exists at DOI 10.1515/znc-2011-1-210 and is blocked only by an automated-traffic challenge; one human fetch closes it (FT-130 / packet A11). Do not re-run automated acquisition.`
- `replace-within`: old `**Current status:** screened — C` → new `**Current status:** queued for deep-dive — A; unacquired, not unread`

#### OP 3 — `dismissal_ledger_current.md` · `🩸 DEFAULTS THAT BIT US` · two rows (numbers allocated by the batch)
- **row A (this candidate's `D-19`):** *"the tool that finds unread gold reported none, so there is none"* — full text as in §4(d), including the detection rule: **before trusting any selector-based tool's empty result, check that its selectors match more than zero records in the live document.**
- **row B (new, 2026-09-27):** *"three routes agreed that the paper has no DOI, so it has none"* — **why it is FALSE here:** the three routes were `convert_article_ids`, `get_article_metadata` and `get_copyright_status`, **all PubMed-family**; Crossref returns a DOI and Unpaywall/OpenAlex return a hybrid-OA PDF for the same paper. **Detection rule:** before recording an identifier or an acquisition state as absent, check **one route outside the family that just answered** — agreement among siblings is not independence.

#### OP 4 — `full_text_queue_current.md` · `FT-130`
**Op:** `append` a dated correction block to the entry (append-only; the wrong verdict is preserved and
labelled, not rewritten), carrying §1's table and the corrected next action. ⚠️ **Not applied by this
package**: the queue is edited by several wave-2 packages and a same-file append is where their edits
would collide.

### 3 · `TX-003`: why DEFERRED and not READY

§4(c)'s replacement text is **correct as prose and unsupported as a record**: every quantity in it comes
from the abstract. The batch disposition of `BATCH_20260927_001` already deferred this candidate on
exactly that ground and this section **agrees with it rather than overriding it** — but it narrows the
deferral: the re-tier (OP 1/OP 2) is **not** abstract-depth prose in a therapeutic record, it is a
reading-priority change with its reason attached, and it is ready now. **Nothing about `TX-003`'s score
moves under any reading of this item** (§5).

### 4 · What is still pending

One human fetch of the publisher PDF. After it: a `FULLTEXT_READ_RECEIPT`, verbatim locators for the Km
table and the substrate/cofactor list, and only then §4(c)'s `TX-003` line.

> ⚠️ **Every `old text` above is RECORD-SCOPED, and several of these strings are not unique in the file.**
> Measured on the current tree: `**Note:** FASE 1 triage 221–400 — no deep-dive performed. …` occurs **176**
> times, `**Role:** background corpus only` **147**, `**Filter decision:** background only` **156**,
> `**Tier:** C` / `**clinical relevance:** LOW` / `**Current status:** screened — C` and
> `**Next action:** background-only; …` similarly. The executor addresses the **record**
> (`CORPUS P306`, `LIT-0306`) and replaces within it; a file-wide replace would rewrite a third of the
> corpus. `record_scoped_edit.py` refuses an ambiguous anchor, which is the safety net, not the plan.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

**(a)** `OP 1` and `OP 2` applied: `CORPUS P306` re-tiered `C / LOW → A / HIGH` with the corrected acquisition line, and `LIT-0306` re-tiered and recorded as **UNACQUIRED, not unread**. Every anchor was addressed **record-scoped**, exactly as the readiness section's warning required — the same strings occur 147–176 times file-wide. **(d)** landed as **`D-18`** and the family-agreement row as **`D-19`**; the numbers are the batch's allocation and shift the candidate's own proposal by one, because `D-24` was already taken and `D-17` is reserved. 🔴 **(c) `TX-003`'s obstacle line stays DEFERRED:** every quantity in it is abstract-depth, and no receipt or locator can exist while the paper is unread. **(OP 4, `FT-130`)** was not applied by this batch either: the queue is a shared-append surface and the readiness section explicitly withheld it.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.
