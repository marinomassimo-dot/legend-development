# The legacy-reconstruction receipt class — enumeration, ranking, and one test of `N-44`

**Node:** `LEGACY_RECONSTRUCTION_SWEEP` · **Actor:** Scientist A · **Date:** 2026-09-22
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt claimed, no
commit. **Read-only toward every canonical file. Public edition. Not medical advice.**

---

## 1 · The direct answer

**`N-44` is SUPPORTED. One test, on the top-ranked paper, found load-bearing unextracted material — and what
it found contradicts a rule this repository has written into two claims.**

**PMID 24369382 (Mallaret 2014, *Brain*)** sits under **three `consolidated baseline` claims** and is the primary
source of the **P47T** and **G372R** comparator alleles that this repository reasons with constantly. Its receipt
is a legacy reconstruction with every coverage field `unknown_legacy`, `source_fingerprint: null`, and **no
dossier and no manifest**. LEGEND's `PAPER 042` record captures its **human** work in detail and records **nothing
about its mouse work**.

🔴 **The paper's own abstract asserts, in the first person and the indicative, that `Wwox` knock-out mice display
spontaneous and audiogenic seizures.** LEGEND's `CLAIM 037` evidence boundary states the opposite — *"I topi
Wwox-null non hanno epilessia riportata"* — and `CLAIM 003` issues it as a prohibition: *"No canonical statement
may describe a Wwox-null mouse as showing epileptogenesis."* **That prohibition now stands against a
claim-linked primary that says otherwise in its own abstract, and the contradiction was never adjudicated against
this source because this source's mouse result was never extracted.**

Two further results came out of the same test: a **structural datum about P47** that bears directly on the Q230P
burial argument (§5, F-2), and a **verifiable overstatement of read depth inside `CLAIM 003`** (§7, C-2).

⚠️ **And the fetch failed.** `get_full_text_article(PMC3914474)` returned **`full_text: ""` — 0 bytes**, the fifth
such deposit this session. So this test was conducted **on abstracts alone**, which makes the result *stronger*
as a demonstration: if abstract-depth re-reading of a legacy-receipt paper surfaces a contradiction with two
claims, the class is worth sweeping.

---

## 2 · Task 1 — The class, enumerated

Read directly from `disease-models/wwox/registries/fulltext_read_receipts.jsonl` (188 records, non-canonical
append-only ledger — not a registry, so direct reading is permitted).

| Measure | Count | Fraction |
|---|---|---|
| Receipts in the ledger | **188** | — |
| `record_kind: legacy_reconstruction` | **22** | **11.7 %** of the ledger |
| …of those, the **full `N-44` signature**: every coverage field `unknown_legacy` **and** `source_fingerprint: null` **and** no dossier **and** no manifest | **13** | **6.9 %** of the ledger · **59 %** of the legacy class |

**All 22 legacy receipts share three of the four traits** — every one is `partial_fulltext_read`, every one has all
coverage fields `unknown_legacy`, and every one has `source_fingerprint: null`. **The discriminating trait is the
absence of a dossier and a manifest**, which splits the class 13 / 9.

**The 13 with the full signature:**
`23446842` · `24369382` · `24456803` · `24932569` · `26857392` · `27495153` · `30361190` · `30362252` ·
`36537114` · `38161429` · `39101447` · `39420317` · `42193054`

**The 9 legacy receipts that have a dossier and/or a manifest** (and are therefore *not* in the test class):
`33916893` · `34268881` · `34634460` · `34747138` · `39507621` · `40875931` · `41562193` · `42128308` · `42422765`.

🔵 **Note for the record:** `36537114` is in the full-signature 13, and Wave 6 already tested it — finding five
`DATO` items LEGEND did not hold. **So the prediction now has two instances, not one**, and this wave's test was
run on a different and higher-ranked paper.

---

## 3 · Task 2 — Ranking by what each sits under

Ranked by **load-bearing × least verifiable**, not by how broken the receipt looks. Claim statuses read from
`claim_registry_current`.

| Rank | PMID | Identity | What it sits under | Why here |
|---|---|---|---|---|
| **1** ⭐ | **24369382** | **Mallaret 2014, *Brain* — WWOX in SCAR12 (P47T / G372R)** · `PAPER 042` | **`CLAIM 007` consolidated baseline · `CLAIM 008` consolidated baseline · `CLAIM 019` consolidated baseline · `CLAIM 030` in observation** | **Three consolidated baselines — more than any other in the class.** It is the primary source of **both comparator alleles** the repository reasons with: **G372R**, the natural mild-phenotype SDR comparator in `CLAIM 030` and in `TX-003`'s design; and **P47T**, whose read-across was retracted in `proteostasis_rationale.md` §2. Its registry note is rich on the human work and **silent on its mouse work** |
| **2** | **42193054** | Sapuppo 2026 — WOREE syndrome plus | `CLAIM 012` **consolidated baseline** | One consolidated baseline; phenotype-severity refinement. Lower reach than rank 1 |
| **3** | **26857392** | Schirmer 2016 — Sp1 site, exon 8→9 junction assay · `PAPER 050` | `Claim links: none — biomarker/assay seed` | **No claim, but high leverage**: it is the entire basis of `DL-BIO-003` and the published template for `TX-001`'s efficacy endpoint. A legacy receipt under an *assay template* is a different risk from one under a claim |
| **4** | **30361190** | Shaukat 2018 — West syndrome / DEE · `PAPER 045` | `CLAIM 001` conflicting evidence · `CLAIM 031` in observation | Feeds an actively conflicted safety claim |
| **5** | **36537114** | Chong 2023 · `PAPER 017` | `CLAIM 001` conflicting · `009` · `013` in observation | **Already tested (Wave 6) — prediction supported** |
| **6** | **39101447** | You 2024 vigabatrin case · `PAPER 016` | `CLAIM 001` conflicting evidence | Safety-relevant, single claim |
| **7–9** | 24456803 · 27495153 · 24932569 | Abdel-Salam 2014 · Elsaadany 2016 · Aldaz 2014 review | `CLAIM 030`/`031`/`032`, all *in observation* | Supporting, none consolidated |
| **10** | **39420317** | Cell Commun Signal 2024 WWOX/TRAF2 | `CLAIM 028` **flagged for review** | Already flagged; `VERY LOW` direct relevance |
| **11–12** | 38161429 · 30362252 | Battaglia 2023 · Davids 2019 | `none — background` | **38161429 is now effectively verifiable** — I read its full PMC deposit in Wave 1, so its legacy receipt understates actual coverage |
| **13** | **23446842** | corpus paper 179 | `Status: not_processed` · `clinical relevance: LOW` · no claims | **The floor of the class** — a legacy receipt on a paper nothing rests on. Included to show the ranking is by reach, not by receipt condition |

---

## 4 · Task 3 — The single test: PMID 24369382

### Surface and depth, declared

| Route | Result | Measured |
|---|---|---|
| `get_article_metadata(["24369382"])` | full record; abstract returned; **PMCID `PMC3914474` present**; DOI `10.1093/brain/awt338`; MeSH terms | — |
| `get_copyright_status(["24369382"])` | **`checked_sources: ["pubmed","pmc"]`** · **`found_in_pmc: 1`** · `pmc_id: PMC3914474` · `is_open_access: false` · *"© The Author (2013). Published by Oxford University Press on behalf of the Guarantors of Brain. All rights reserved."* | — |
| `get_full_text_article(["PMC3914474"])` | 🔴 **`full_text: ""`** — deposit exists, **body empty** | **0 bytes** |

⇒ **Depth reached: abstract only, from two routes.** 🔴 **Nothing below is a reading of the full text.** LEGEND's
`PAPER 042` records `Evidence depth: full text reviewed (via PMC web; non-OA all'API)` — a prior session reached
the body by a route not available now, which is precisely why the receipt could not be fingerprinted.

⭐ **A reusable by-product.** `get_copyright_status` returning `checked_sources: ["pubmed","pmc"]` **with a real
`pmc_id` and `is_open_access: false`** is the signature that predicts `full_text: ""`. This session has burned
five fetches discovering that empirically (PMC4692203, PMC1863559, PMC4374002, PMC5016130, PMC3914474). **Running
`get_copyright_status` first is a one-call pre-test for whether a fetch will return a body.**

### Attribution check, performed BEFORE reporting — per my own Wave 6 caveat

Every item below comes from **PubMed's record for PMID 24369382** and **PMC's record for PMCID PMC3914474**,
addressed by identifier. **No passage-ID inference, no Scholar Gateway, no cross-reference-marker matching**
(`FT-126` limbs 1 and 2, both respected). **And the items fall inside the paper's own declared scope**: its
abstract covers the human genetics *and*, explicitly, the mouse observation. The attribution test passes.

---

## 5 · The findings

| # | Finding | Tag | Does LEGEND hold it? |
|---|---|---|---|
| **F-1** 🔴 | **The paper asserts a mouse seizure phenotype in the first person and the indicative.** Verbatim: *"Moreover, we observed that the short-lived Wwox knock-out mouse display spontaneous and audiogenic seizures, a phenotype previously observed in the spontaneous Wwox mutant rat presenting with ataxia and epilepsy, indicating that homozygous WWOX mutations in different species causes cerebellar ataxia associated with epilepsy."* | **`DATO`** that the assertion exists and is first-person; **strength UNVERIFIABLE** — no methods, no n, no strain attribution, no scoring criteria at abstract depth | 🔴 **NO.** `PAPER 042`'s Note records only the human P47T work — Western blot, pull-down, patient ages, *"Nessuna menzione di Gln230"*. **The mouse result is absent from LEGEND's record of this paper.** See §6 |
| **F-2** ⭐ | **P47 is described as a fold-stabilising core residue.** Verbatim: *"Proline 47 is a highly conserved residue that is part of the WW motif consensus sequence and is part of the hydrophobic core that stabilizes the WW fold."* | **`DATO`** (source statement) + **`INFERENZA`** (its consequence) | 🔴 **NO.** LEGEND holds P47T as *"a WW1/PPxY binding defect"* with normal protein levels. It does **not** hold that P47 is a **buried, fold-stabilising core residue**. 🔵 **Why this matters:** `DL-BIO-001` and `HYP-20260709-08` reason from Q230's burial (`relSASA 0.000`, core packing, 88th percentile) toward a folding-and-turnover lesion. **P47T is a substitution at a fold-stabilising hydrophobic-core residue that does NOT reduce protein levels** — a published counter-example to *burial ⇒ destabilisation ⇒ degradation*, inside the very paper LEGEND uses as the comparator. **It does not overturn the P47T retraction** (normal protein levels remain the decisive difference from Q230P) — it **strengthens** the retraction's reasoning while **weakening** an inference used elsewhere |
| **F-3** | **Two mouse strain backgrounds are indexed**: MeSH `Mice, 129 Strain` **and** `Mice, Inbred C57BL`, alongside `Mice, Knockout` | **`DATO`** that both are indexed; **`IPOTESI`** as to significance | 🔴 **NO.** ⚠️ **FLAGGED, NOT SCORED.** Wave 4 §5 concluded no neurodevelopmental strain-background modifier has been *tested* in WWOX. MeSH indexing of two backgrounds is **not** a background comparison — mixed-background animals are routinely indexed this way. **This is a lead to check in the body, not a finding**, and Wave 4's negative stands unchanged |
| **F-4** | The PMC record returns a **commentary-style preamble absent from the PubMed abstract**: *"The genetic basis of many recessive cerebellar ataxias is unknown. Mallaret report mutations in the WW domain-containing oxidoreductase gene, associated with ataxia plus mental retardation and tonic-clonic seizures in two consanguineous families, and with upper motor neuron disease in one of them. knockout mice displayed audiogenic seizures."* (italic gene tokens deleted by the extractor) | **`DATO`** | 🔴 **NO** — and it independently corroborates F-1 from a *Brain* editorial summary, i.e. a second voice inside the same deposit |
| **F-5** | Index-family provenance: *"a 19 Mb interval in 16q21-q23 by homozygosity mapping of a large consanguineous Saudi Arabian family"* | **`DATO`** | 🟡 **Partly.** `PAPER 042` records *"due famiglie"* but not the mapping interval. Relevant to §12-style overlap work, since other WWOX series draw on families from the same region |

---

## 6 · What F-1 does and does not do to `CLAIM 037` and `CLAIM 003`

**FLAG FIRST.** This is a **contradiction between a claim's evidence boundary and a claim-linked primary's own
abstract**. It is reported as that, and **not** scored as a reversal.

**What LEGEND holds.** `CLAIM 037` evidence boundary: *"🔴 **I topi Wwox-null non hanno epilessia riportata** —
affermato tre volte in PMID 19500159 e formalizzato in Table 2, dove la riga `Epilepsy` è compilata solo per
`lde/lde`."* `CLAIM 003` evidence boundary goes further and makes it a rule: *"**No canonical statement may
describe a Wwox-null mouse as showing epileptogenesis.**"*

**What LEGEND had already done, and it is substantial.** `CLAIM 003` explicitly traced this premise: *"Early death
and epileptogenesis were attributed here to PMID 19936220 and Mallaret 2014."* It then established that
epileptogenesis *"is not measured there in any form"* in PMID 19936220, and that the chain's terminus
(PMID 19500159) **asserts the opposite for the mouse**. **That work is prior art and is not rediscovered here.**

**What is new.** The trace concluded about **19936220** and **19500159**. It did **not** record what **Mallaret
2014 itself reports about mice** — and Mallaret 2014 reports it in the **first person** (*"we observed"*), not as
a citation. So the repository currently holds:
- a prohibition — no canonical statement may describe a Wwox-null mouse as epileptogenic;
- against a source carrying **three consolidated-baseline claims**, whose abstract asserts exactly that;
- with **no record in LEGEND of that source's mouse result at all**.

**Why this is a flag and not a reversal — four reasons, all limiting:**
1. **Abstract depth only.** No methods, no n, no scoring criteria, no strain attribution. An abstract assertion cannot overturn a Table-2 negative read in full (`FTR-20260806-19500159-01`, `complete_fulltext_read`).
2. **`CLAIM 037`'s own authors left the door open** — mice may die before seizing — and the repository already records that the earliest rat seizure onset (day 16) exceeds the mouse null's lifespan. A mouse seizure observation is therefore *surprising*, which is a reason for scrutiny, not acceptance.
3. **The alleles and laboratories differ**, and the operator's §12 rule applies with full force: Mallaret's mouse, the Aldaz line and the Aqeilan line are **not one animal**. The abstract does not say whose mouse it is. *(Aldaz CM is a co-author, which is a lead, not an attribution.)*
4. **Not independent.** Chong 2023, read in Wave 6, states *"Wwox knockout mice exhibit spontaneous seizures at 2 weeks of age"* citing Mallaret 2014 — so the secondary literature propagates this assertion from the same single source. **One source, repeated, is still one source.**

**What would resolve it:** the mouse methods paragraph and figure of PMID 24369382 — how seizures were observed,
in how many animals, on which background, against which controls. **That is a precise acquisition ask, on a paper
whose PMC deposit exists but is closed.**

---

## 7 · Corrections

| # | Standing text | Correction | Basis |
|---|---|---|---|
| **C-1** 🔴 | `PAPER 042`'s Note, which records Mallaret 2014's human findings in detail. | **Incomplete, not wrong.** The paper's abstract carries a **first-person mouse seizure observation** (F-1) and a **structural characterisation of P47 as a fold-stabilising core residue** (F-2). Neither is in LEGEND's record. **The record's human content is accurate; its scope is partial** — exactly as the receipt's `partial_fulltext_read` declares. **Flagged, not edited.** | this wave |
| **C-2** 🔴 | **`CLAIM 003` evidence boundary: *"All three links of that chain have since been read in full."*** | **Verifiably not true of the third link.** Receipt depths: PMID 19936220 → `complete_fulltext_read` (×2, contemporaneous); PMID 19500159 → `complete_fulltext_read` (contemporaneous); **PMID 24369382 → `partial_fulltext_read`, `record_kind: legacy_reconstruction`, every coverage field `unknown_legacy`, `source_fingerprint: null`.** **Two of three were read in full; the third was not.** ⚠️ This is a claim's prose asserting a depth its own receipt contradicts — and it is checkable in one command, which is what makes it worth recording | ledger, this wave |
| **C-3** ⚠️ | The general reading of `N-44`'s signature. | **Refine it.** All 22 legacy receipts share `partial_fulltext_read` + all-`unknown_legacy` + `source_fingerprint: null`; **those three traits do not discriminate.** The **discriminating trait is the absence of a dossier and a manifest** (13 of 22). A future sweep should filter on that, not on the receipt fields | this wave |
| **C-4** ℹ️ | Fetch practice across this session. | **`get_copyright_status` is a one-call pre-test for an empty body.** `checked_sources: ["pubmed","pmc"]` + real `pmc_id` + `is_open_access: false` predicted `full_text: ""` in every instance encountered. Five fetches were spent establishing this empirically | this wave |

---

## 8 · Task 4 — The prediction's status

# `N-44`: **SUPPORTED**

**Stated precisely:** one test on the top-ranked member of the full-signature class found **five items LEGEND does
not hold**, of which **two are load-bearing** — one contradicting the evidence boundary of two claims (F-1), one
weakening an inference used in `DL-BIO-001` and `HYP-20260709-08` (F-2). **With Wave 6's independent instance on
`36537114`, the class now has two tests and two positives.**

**The reasons to believe it, and they are specific rather than general:**
- The find was made at **abstract depth**, with the full text unreachable. A signature that yields load-bearing material from abstracts alone is a strong signal about the class.
- The unextracted material is **not obscure**: it is in the paper's own abstract, in the first person, and it concerns the mouse model — a whole experimental arm that LEGEND's record of this paper omits entirely.
- The mechanism is legible: **a legacy reconstruction records that a read happened without recording what was covered**, so nothing flags the omission. `CLAIM 003`'s *"read in full"* (C-2) is that gap becoming an error in prose.

**The reasons to hold it loosely — and they are real:**
- **n = 2, and both were chosen as top-ranked.** The class was ranked by reach, so the test is biased toward finding consequences. **That is the right design for deciding whether to sweep, and the wrong design for estimating a rate.** No rate is claimed.
- **The floor of the class argues against sweeping indiscriminately**: `23446842` is `not_processed`, `LOW` relevance, no claims. A sweep of all 13 would spend most of its effort there.
- **F-1 is a flag, not a finding** — abstract-depth, single-source, and limited by four stated reasons (§6). The prediction is supported by the *existence* of consequential unextracted material, not by F-1 being true.

**What a later session should do — and it is narrower than a sweep:** re-read **ranks 1–4 only** (24369382,
42193054, 26857392, 30361190) — the two consolidated-baseline sources, the assay template under `DL-BIO-003`, and
the conflicted safety claim. **Ranks 10–13 should not be swept**; their receipts are weak because nothing rests on
them, which is the correct allocation of effort, not a defect.

🔵 **And carry my Wave 6 caveat, which held here:** anything surfaced while working one node inherits that node's
attribution risk. **The attribution check in §4 was run before these findings were reported, not after** — by
identifier, not by passage marker. That is the discipline that `N-33` and `N-35` lacked.

---

## 9 · Declaration

Author: **Scientist A**. Date: **2026-09-22**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record created or amended (C-1, C-2 flagged only), no receipt recorded, no
commit candidate produced, no git operation performed. This file is the single file written. The receipts ledger
was **read only** — no append, no hand-edit; its hash chain is untouched.

🔴 **Public edition compliance.** No contact details and no identifying information of any living person. F-5
reports a family's geographic origin **only as the source's own mapping description**, with no age, sex, clinical
detail or family identifier attached to it — the stack is not assembled.

**Not medical advice.**

**Declared limits.** 🔴 **The full text of PMID 24369382 was NOT read**: the PMC deposit exists and returned
**0 bytes**. All findings are at **abstract depth from two routes**, and F-1's *strength* — n, strain, scoring,
controls — is **unverifiable** at that depth; only the *existence and mood* of the assertion are established. F-3
is **flagged, not scored**: MeSH indexing of two mouse strains is not a background comparison, and Wave 4's
negative on strain-background modifiers stands. No figure panel was inspected. No variant coordinate is quoted
from any corpus surface. No content is attributed by passage or cross-reference ID. The enumeration in §2 is a
census of one ledger file on 2026-09-22, not a statement about any other repository state.

*Article metadata from **PubMed**; PMC availability and deposit body tested via **PubMed Central**.*

**DOIs — verified on two routes each** (`get_article_metadata.identifiers.doi` **and**
`get_copyright_status.available_at.doi_url`; the converter was not relied on):
[24369382](https://doi.org/10.1093/brain/awt338) — Mallaret M *et al.*, *Brain* 2014;137(Pt 2):411–419 ·
[36537114](https://doi.org/10.1002/ajmg.a.63074) — verified in Wave 6 on both routes.

**Cited from LEGEND's own records without re-verification this wave** (flagged rather than asserted as verified):
PMIDs 19936220, 19500159, 42193054, 26857392, 30361190, 39101447, 39420317, 24456803, 27495153, 24932569,
38161429, 30362252, 23446842 — all appear here as **ledger and registry entries**, not as sources read or cited
for scientific content.
