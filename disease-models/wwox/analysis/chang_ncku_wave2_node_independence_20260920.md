# Chang/NCKU Wave 2 — node independence, and the closure of the lithium loop

**Date:** 2026-09-20 · Orchestrator work, run while Scientist A (Chang↔Aldaz) and Scientist B
(peptides) worked in parallel. Non-canonical. No canonical file edited.
**Depth:** all findings below are **metadata + PubMed field-census depth**, not full-text readings.
No receipt is claimed for any paper named here that was not already receipted in Wave 1.

---

## 1 · Lithium / GSK3β — the loop closes, and it closes emptier than expected

Field census over all of PubMed (2026-09-20):

```
(WWOX OR Wwox) AND (lithium OR "GSK3 inhibitor" OR "GSK-3 inhibitor"
                    OR tideglusib OR SB216763 OR CHIR99021 OR kenpaullone)
  →  1 record
```

**One.** `PMID 32000863` — the Cheng/Hsu 2020 paper whose lithium arm `CLAIM 016` already records as
**not genotype-specific** (LiCl suppressed PTZ seizures in wild-type, heterozygote and knockout alike).

So, stated precisely:

- There is **no second lithium/WWOX paper anywhere.**
- **No named selective GSK3β inhibitor** — tideglusib, SB216763, CHIR99021, kenpaullone — has ever
  been used in any WWOX context, by anyone.
- Therefore **nobody has ever shown that inhibiting GSK3β corrects any consequence of losing WWOX.**

The decisive question in the batch brief — *"is this a WWOX-specific correction or a generic
anticonvulsant effect?"* — is answered by the absence: **there is no experiment in the literature
that could distinguish them**, and the one experiment that exists points at "generic".

**`TX-005` → DOWN**, on a census rather than on an interpretation. Not `DISMISS`: the *mechanism*
(`CLAIM 035`, WWOX as a residue-mapped direct GSK3β inhibitor) is untouched and got its third source
in Wave 1. What is downgraded is the **drug**, and the reason is that the drug has never been tested
against the disease it is proposed for.

> Acquisition blocker, parked not escalated: `FT-024` (`PMID 15126504`, Sze 2004 *JBC*) has **no
> PMCID**, and in this environment `curl` to NCBI/EBI and `WebFetch` to jbc.org, sciencedirect and
> pmc.ncbi.nlm.nih.gov all return egress refusals. The paper is unobtainable here by any route.
> It still holds the one sentence that would settle whether Sze 2004's *"enhanced phosphorylation of
> GSK-3β"* means the activating pY216 or the inhibitory pS9 — and `CLAIM 035` warns a pS9 readout
> yields a **false negative** in this system. Routes that remain: author contact, WWOX Foundation
> institutional access, ILL. **Not HUMAN_REQUIRED — it is an acquisition task, parked.**

---

## 2 · Has anyone put Zfra into a WWOX-deficient animal? — No.

```
Zfra AND (Wwox OR WWOX) AND (knockout OR deficient OR "null mice" OR heterozygous)  →  3 records
```

All three are already known to this batch and **none is the experiment**: `36498839` (read in Wave 1 —
uses `Wwox+/−` mice for the *aggregation and memory phenotype*, never for Zfra treatment), `29310447`
and `27999774` (both **reviews**).

Wave 1 asserted this gap from reading. It is now established by census: **no Zfra peptide has ever
been administered to a WWOX-deficient animal by anyone**, though the lab that proposes Zfra owns
both the null and the heterozygous mice and uses them in the same papers.

This remains the single cheapest decisive experiment in the whole Chang programme.

---

## 3 · Node independence — the chain's first two nodes are the lab's own proteins

The central research question requires knowing which nodes survive **independent** adjudication.
Both of the cascade's initiating proteins were discovered by the Chang lab:

| Node | Origin | Independent characterisation |
|---|---|---|
| **TIAF1** | **Cloned by Chang N-S**, *BBRC* 1998 (`PMID 9918798`) | essentially none in the aggregation role |
| **TRAPPC6AΔ** | **Isolated by the Chang lab**, *Oncotarget* 2015 (`PMID 25650666`): *"We **isolated** an N-terminal internal deletion isoform, TPC6AΔ, derived from alternative splicing of the TRAPPC6A gene transcript."* | **none for the Δ isoform** — see the split below |

### 🔴 The split that matters, and it cuts both ways

`TRAPPC6A AND (Alzheimer OR aggregation OR plaque OR neurodegeneration OR amyloid)` → **7 records.**
Four are Chang-lab. The other three are **fully independent and they support the GENE**:

- `PMID 21766012` — Hamilton 2011, **Lothian Birth Cohorts 1921 + 1936** (Edinburgh, n=505 + 998):
  a *TRAPPC6A* haplotype associates with **nonverbal reasoning in both cohorts and combined**.
  Honest scope: single-SNP analyses did **not** survive multiple-testing correction, and the
  haplotype explains **1.8%** of variance. The authors call it warranting further investigation.
- `PMID 33134515` — Park 2020, **ADNI + AddNeuroMed** (Indiana / KCL): *TRAPPC6A* is among the
  functional genes composing a blood transcriptional risk score associated with AD diagnosis,
  hippocampal volume and entorhinal thickness. Rated **Class III** by the journal.
- `PMID 41390778` — Fu 2025, *Sci Rep*, **UCLA Health (N=416,212) validated in All of Us (N=52,493)**:
  *TRAPPC6A* is one of eight shared-risk SNPs for **late-onset epilepsy AND Alzheimer's disease**.

**So the finding is not "the node is fabricated" — it is sharper than that:**

> **The GENE `TRAPPC6A` has independent, large-cohort human-genetic support for a neurocognitive
> role, including a shared epilepsy–AD risk signal. The ISOFORM `TRAPPC6AΔ` — the N-terminal
> 14-residue deletion product that is the actual first node of the Chang cascade — has been
> reported by no group other than Chang's, and its founding paper is in *Oncotarget* (2015).**

Every downstream step of the cascade (Ser35 phosphorylation, polymerisation, TIAF1 recruitment,
caspase activation, Aβ generation) is a property of **the isoform, not the gene**. The independent
human genetics therefore corroborates the *neighbourhood* of the chain while leaving its *first
mechanistic step* entirely single-lab.

⚠️ **Author-disambiguation trap, caught and recorded.** `PMID 41390778`'s senior author is
**Chang, Timothy S. (UCLA)** — no relation to **Chang, Nan-Shan (NCKU)**. A naive
author-name independence check would have scored this independent paper as Chang-lab and destroyed
the very finding it supports. Any future automated independence screen in this repository must
disambiguate on affiliation, not surname.

### TIAF1, and a direction problem

`TIAF1` → 20 records, most of them Chang-lab. The one independent human-genetics result points the
**wrong way** for the model: `PMID 32020597` (Curtis 2020, >10,000 exomes, Alzheimer's Disease
Sequencing Project) reports that *"variants in TIAF1 and/or NDRG2 might have a **protective**
effect."* Chang's model has TIAF1 aggregation as **pathogenic**. Curtis states the result as
suggestive, not established, and it concerns coding variants rather than aggregation — so this is a
**flag, not a refutation**. Recorded because it is counter-directional and nobody has reconciled it.

---

## 4 · Consequence for the central research question

The chain as proposed is:

```
WWOX loss → pY33/pS14 → TRAPPC6AΔ → TIAF1 → tau/Aβ → mitochondria → GSK3β → proteostasis → neuronal dysfunction
```

Wave 1 graded the arcs. Wave 2 adds the orthogonal grading — **who else has seen this node at all**:

| Node | Independently observed? |
|---|---|
| WWOX loss → neurological disease | **YES** — human genetics, multiple groups, not in dispute |
| pY33 / pS14 phospho-switch | **NO** — Chang-lab antibodies, Chang-lab papers |
| **TRAPPC6AΔ (isoform)** | **NO** — single lab. *(gene TRAPPC6A: YES, three independent cohorts)* |
| **TIAF1 (aggregation role)** | **NO** — single lab; one independent genetic hit points the opposite way |
| tau / Aβ aggregation | YES as biology, but not as a WWOX-driven cascade |
| GSK3β dysregulation | **YES** — Wang/Lu 2012 is an independent lab (`PAPER 056`) |
| proteostasis / lysosome | partial — and Wave 1 showed it concerns WWOX's *substrates*, not WWOX |

**The two nodes that convert "WWOX loss" into "protein aggregation" are exactly the two nodes no
laboratory outside NCKU has ever reported.** That is the structural answer to *"does the chain
survive independent adjudication?"* — the ends are corroborated, the middle is not.

> 🔴 **UPGRADE OF THE NEGATIVE — 2026-09-21, after reading the founding paper.** The table above
> says of the two middle nodes only that **no one else has reported them**. Having now read
> `PMID 25650666` adversarially (receipt `FTR-20260921-25650666-02`, audit
> [`trappc6a_delta_founding_paper_audit_20260921.md`](trappc6a_delta_founding_paper_audit_20260921.md)),
> that is too generous in two distinct ways.
>
> **First: they are not two nodes. They are one measurement.** `TRAPPC6AΔ` and `TIAF1` come from the
> same laboratory, the same tissue bank (*"Department of Pathology, University of Colorado Health
> Sciences Center (by Dr. CI Sze, before 2005)"*), the **same filter-retardation membranes**, the
> same overexpression figure and the same unvalidated antibody practice — and the paper itself
> writes *"Similar results were observed with TIAF1 aggregates."* Listing them as two rows
> **double-counts one observation**. Corroboration weight for the pair is **one**, and the table
> should be read that way.
>
> **Second: the founding paper disclaims its own load-bearing step.** Its Discussion summarises
> *"We determined that TGF-β1 causes dissociation of WWOX from TPC6AΔ, thus leading to the
> aggregation of TPC6AΔ and TIAF1 and subsequent events…"*, and the **same Discussion** states
> *"Whether TGF-β1 regulates the binding of WWOX with TPC6AΔ **is unknown** and is being determined
> in this laboratory."* **There is no binding assay in the paper at all** (*immunoprecipit*, *co-IP*,
> *pull-down*: zero occurrences, roman-type method words, so the count is informative). The arc
> `WWOX ⟶ TRAPPC6AΔ` is therefore not merely uncorroborated from outside — **it is undemonstrated
> inside its own source.**
>
> Three further facts that bear on the same row: the **isoform's splicing origin is a web-tool
> prediction**, never junction-sequenced; the **antisera are validated by peptide competition
> alone**, with no genetic null, although the lab uses a `TPC6Asi` siRNA elsewhere in the same
> paper; and the **human post-mortem arm is a null** (*"No significant difference was shown in
> TPC6A or TIAF1 aggregation"*) between controls deliberately **21 years younger** than the cases,
> which the abstract renders as a temporal ordering.
>
> **What this does to the central research question.** It does not change the shape of the answer —
> the ends are corroborated and the middle is not — but it changes its severity. The middle of the
> chain is **one laboratory's single, internally contradicted observation**, not two independent
> single-lab observations that happen to agree. **And the one thing this paper does show cleanly
> points the right way for the disease and the wrong way for a therapy:** less WWOX means more
> aggregation (*"without WWOX, TPC6A and TIAF1 start to polymerize or aggregate"*), which makes
> aggregation a **consequence** of the genotype rather than an intervention point upstream of it.

---

## 5 · Findings registered, not acted on

- Acquisition: `WebFetch` is blocked by the same egress policy as `curl` for jbc.org,
  sciencedirect.com, pmc.ncbi.nlm.nih.gov. `WebSearch` works but returns snippets, and a snippet is
  not a read. The **PubMed MCP server is the only reading route in this environment**, and it
  reaches PMC open-access deposits only.
- `CORPUS-STUB-156` (TRAPPC6, never processed) is the registry's only trace of this node. Not
  promoted here — promotion is a commit-candidate action and this wave read no full text of it.

---

**Wave 2 orchestrator segment closed. Scientist A and Scientist B outputs integrate separately.**


---

## 🔴 CORRECTION — 2026-09-21: the epilepsy signal I cited does not survive reading

This file concluded that *"the **GENE** `TRAPPC6A` has independent, large-cohort human-genetic support
for a neurocognitive role, including a **shared epilepsy–AD risk signal**"*, resting on three cohorts
of which `PMID 41390778` (UCLA, 416,212 records, validated in All of Us) was the strongest.

**That paper has now been read, and the epilepsy half of the claim fails.**

- **The epilepsy arm is null on replication.** All of Us, the full shared genetic risk score against
  late-onset epilepsy alone: **OR 1.01 (0.96–1.06), p = 0.80**, variance explained **< 0.01%**. In
  UCLA discovery, LOE p = 0.1.
- **Seven of the eight SNPs came from the AD GWAS**, and "shared" was defined by **coefficient sign
  agreement only** — not by an epilepsy association.
- **The one LOE-positive result excludes `TRAPPC6A`.** It is built from the four variants the authors
  themselves enumerate as lying **outside** the APOE region (two on chr2, one on chr8, one on chr10).
  `TRAPPC6A` is chr19q13.32, so by the authors' own enumeration it falls in the chr19 group they call
  *near* the APOE region — and that positive result failed to replicate anyway (AoU p = 0.11).
- **APOE-independence was never tested.** No conditional analysis, no LD clumping; Elastic Net was
  chosen *because* it tolerates LD. So `TRAPPC6A` cannot be separated from the APOE signal here.
- The authors concede **"minimal evidence supporting epilepsy-specific pathways"**, and LDSC had
  returned **no** genetic correlation before the model was built.
- **Seventh abstract-versus-results inversion in this literature:** an exact null (OR 1.01, p = 0.80)
  sits beneath the abstract's claim that the score *"effectively stratified patients into distinct
  AD-LOE risk groups."*

**What this does to the node-independence finding: it makes it MORE negative, not less.** The split
this file drew — *the gene is corroborated, the isoform is not* — still holds in form, but the
corroboration is weaker than stated: the strongest of the three cohorts turns out to be an
**APOE-region annotation in an AD-driven screen whose epilepsy arm is null**. `TRAPPC6AΔ`, splicing,
transcript and `TIAF1` occur **zero** times in it; it is gene-level throughout, so it never spoke to
the isoform in any case.

And even a clean positive would not have transferred: **a common-variant risk locus for late-onset
epilepsy in adults is a different causal regime from biallelic loss of function in a neonate.** That
was true when this file was written and should have been said then.

*(Receipt for the reading: see the wave's ledger entry. Method note: the same extraction defect
applies — `TRAPPC6A` occurs zero times in the body text and survives only in the PubMed abstract
record, so any grep-based gene audit over this tool's PMC text will produce false negatives.)*
---

## 🔴 FULL RETRACTION — 2026-09-21: the gene-level corroboration is withdrawn in its entirety

The correction above softened the node-independence finding. It was not enough. The third leg has
now been read, and **all three legs are down.** The blockquoted claim in § 3 —

> *"The GENE `TRAPPC6A` has independent, large-cohort human-genetic support for a neurocognitive
> role, including a shared epilepsy–AD risk signal."*

— **is retracted in full. It is not narrowed, not rescoped and not "weaker than stated". There is
no demonstrated independent human-genetic support for this gene reachable from this laboratory.**

| Leg | As written in § 3 | On reading |
|---|---|---|
| `PMID 21766012` — Lothian Birth Cohorts | *"a haplotype associates with nonverbal reasoning in both cohorts and combined"* | **Failed the authors' own permutation correction in the discovery cohort.** Verbatim: *"These SNP windows were not significant postpermutation analysis of the LBC1936."* |
| `PMID 33134515` — ADNI + AddNeuroMed | *"among the functional genes composing a blood transcriptional risk score"* | **Unread — and, 🔴 corrected 2026-09-21, NOT licence-walled.** Counts in neither direction. |
| `PMID 41390778` — Fu 2025, UCLA + All of Us | *"one of eight shared-risk SNPs for late-onset epilepsy AND Alzheimer's disease"* | **Epilepsy arm null on replication**: OR 1.01, 95% CI 0.96–1.06, p = 0.80. |

**On the Lothian paper specifically** — the leg this file leaned on hardest, and the only one that
had survived the first correction. The audit is
[`lothian_trappc6a_audit_20260921.md`](lothian_trappc6a_audit_20260921.md); receipt
`FTR-20260921-21766012-01`. Four things, each of which alone would have disqualified it as
corroboration:

1. **It failed its own stage-2 permutation in the discovery cohort.** The authors' Results:
   *"Though not significant postpermutation analysis in the LBC1936, this finding was replicated in
   the LBC1921 and in post permutation analysis of the combined cohort."* The only permutation it
   passes is computed on a **combined dataset containing the discovery cohort** — which is not an
   independent test of the discovery cohort's result.
> 🔴 **CORRECTION TO THIS TABLE — 2026-09-21, same day, against myself.** The row for
> `PMID 33134515` said **"licence-walled"**. **That was never measured; it was inferred from
> `get_copyright_status`, whose `is_open_access: false` came with `checked_sources: ["pubmed"]` —
> PMC was never consulted.** A fetch attempt made later the same day returned a **full body from
> `PMC7577551`**. The paper is **retrievable**, and `FT-098` should be re-opened.
>
> **This does not revive the retracted claim, and the reason matters.** The leg is still **unread**,
> so it still counts in neither direction — what changes is that its silence is now *our* debt
> rather than the publisher's. ⚠️ And a caution travels with it: the MCP extractor renders that
> paper's Results as *"Among 6 target genes identified by COLOC and SMR from AD-associated SNPs
> with< 1 × 10, 2 genes (and) and 4 genes (,,, and) were labeled as high expression and low
> expression, respectively"* — **every gene symbol deleted**. **No negative about `TRAPPC6A` may be
> drawn from that surface**, and adjudicating `FT-098` properly needs the publisher's HTML or PDF.

2. **It is a subgroup finding.** Significance was reached **in the APOE-ε4-negative subgroup only**,
   on matrix reasoning.
3. **The replication was nominal and on a different instrument.** Threshold: uncorrected p ≤ .05.
   Effects: β −0.21 / **1.8%** of variance (LBC1936), β −0.18 / **1.3%** (LBC1921).
4. **It was never a candidate-gene test of this gene at all.** The SNPs entered as incidental
   chr19/APOE-region tiling coverage, are **not in LD with the motivating GWAS SNP rs597668**
   (D′ = 0.22), and the authors themselves write: *"it is unclear whether our results are detecting
   the same effect."* Their closing position is *"These findings warrant further investigation."*

§ 3 recorded point 3 as "honest scope" and stopped there. It did not record that the result **had
failed the correction the authors themselves applied** — which is not scope, it is the finding
being negative. That omission is what made the leg look load-bearing.

**What I got wrong, stated plainly.** I built a three-cohort independence claim from search-result
abstracts and titles. Every one of the three collapsed on contact with the primary text or turned
out to be unreachable. The failure mode is the one this framework names repeatedly and which I
reproduced anyway: **a census was treated as evidence.** Seven records returned by a query became
"three independent cohorts support the gene" without one of them being read.

**What is unchanged, and it was always the load-bearing point.** *None of the three papers ever bore
on the isoform.* All three are locus-level or genotype-level human genetics with no transcript-level
readout — the Lothian unit of analysis is a 3-SNP genomic window spanning 1442 bp, which cannot
distinguish `TRAPPC6AΔ` from full-length `TRAPPC6A` because it has no instrument that sees
transcripts. So the split this file drew — *gene corroborated, isoform not* — was answering a
question **adjacent to the one that matters** even in the version where it was true. The cascade
depends on the isoform. The isoform remains **reported by no group other than Chang's.**

**Net effect on the central research question: none of this rescues or damages the therapeutic
argument, because it never touched it.** A common-variant association with nonverbal reasoning in
healthy 70-year-olds, had it held, would still be a different causal regime from biallelic loss of
function in a neonate. The node-independence status of `TRAPPC6AΔ` after all three readings is what
it was before: **single-laboratory, uncorroborated.**

**Method note, and it applies to every gene audit run over this tool's output.** The string counts
originally offered for both `41390778` and `21766012` are **withdrawn as evidence**. The MCP
extractor deletes every italicised token, and gene symbols in these journals are italicised:
`TRAPPC6A` occurs **zero** times in the Lothian body text — and so do `APOE`, `APP`, `BIN1`, `CLU`
and `PICALM`, which that paper is *entirely about*. The damage is visible in what the tool returns
(*"One 3-SNP window from thelocus reached significance"*). Under `D-15`, **a zero count produced by
an instrument known to delete the class of token being counted is an instrument reading, not a
negative.** The isoform conclusion above rests on study **design**, stated in the papers' own
Methods, and not on any count.

*(Orchestrator, 2026-09-21. Retraction recorded by append, per the append-only discipline: the
original claim in § 3 is left standing above so that what was claimed, and on what basis, remains
readable. No canonical current file is modified by this note; no commit candidate is created.)*
