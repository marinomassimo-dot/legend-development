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
