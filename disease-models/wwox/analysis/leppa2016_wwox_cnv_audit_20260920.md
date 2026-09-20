# Leppa 2016 — WWOX CNV audit against the primary

**Target:** Leppa VM, Kravitz SN, Martin CL, Andrieux J, Le Caignec C, Martin-Coignard D, DyBuncio C,
Sanders SJ, Lowe JK, Cantor RM, Geschwind DH. *Rare Inherited and De Novo CNVs Reveal Complex
Contributions to ASD Risk in Multiplex Families.* **Am J Hum Genet** 2016;99(3):540–554.
PMID **27569545** · PMCID **PMC5011063** · DOI [10.1016/j.ajhg.2016.06.036](https://doi.org/10.1016/j.ajhg.2016.06.036)
(article metadata and abstract retrieved from **PubMed**; the body was not retrievable — see below).

**Auditor:** Scientist B, batch `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`.
**Date:** 2026-09-20. **Canonical files touched:** none. This file is non-canonical analysis.
**Purpose:** discharge the declared limit in `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` §5 —
*"Leppa 2016 … reached at abstract/metadata depth … the OR figures reaching this batch are
review-reported, not read"* (`FT-103`).

---

## 0 · Declared read depth — READ THIS BEFORE ANY OTHER LINE

> **DECLARED READ DEPTH: `abstract_and_metadata_only`. The body of this paper was NOT read.
> The limit that `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` §5 declared is NOT discharged.
> It is now *characterised* — we know exactly why it cannot be discharged on this surface — but
> it stands.**

| Item | Status |
|---|---|
| Abstract | ✅ **obtained, complete and unstripped**, via `get_article_metadata` |
| Author list, affiliations, MeSH, citation | ✅ obtained |
| **Results section / body text** | ⛔ **NOT OBTAINED** |
| **Main tables (incl. any WWOX CNV table)** | ⛔ **NOT OBTAINED** |
| **Figures / panels** | ⛔ **NOT OBTAINED** — no PDF route, no image route; **no panel was inspected and none is claimed** |
| **Supplementary tables** | ⛔ **NOT OBTAINED — and not obtainable here at all.** Supplementary material was never reachable, because the *article itself* was never reachable. If the per-family WWOX CNV detail lives in a supplement (which for an AJHG CNV paper of this design is likely), **those numbers are not verifiable in this environment by any route available to this laboratory.** |

### Why — the acquisition record, so nobody repeats it

1. `mcp__PubMed__get_full_text_article` with `pmc_ids: ["PMC5011063"]` → **returns
   `"full_text": ""`**. Retried with the bare numeric id `["5011063"]` → identical empty body.
   The record resolves (correct title, PMID, DOI) — the deposit simply carries no retrievable body.
2. `mcp__PubMed__get_copyright_status` for PMID 27569545 explains it:
   > `"copyright": {"statement": "Copyright © 2016 American Society of Human Genetics. Published by
   > Elsevier Inc. All rights reserved."}`, `"license": {"type": "All rights reserved",
   > "is_open_access": false}`, `"summary": {"found_in_pmc": 0}`
   **The article is in PMC but is not in the PMC open-access subset.** The MCP full-text route serves
   the OA subset only. This is a licence wall, not a transient failure — **do not re-queue this PMID
   for the PMC route; it will return empty every time.**
3. Egress probes (bounded, three requests, then stopped): `api.openalex.org`,
   `api.unpaywall.org`, `api.semanticscholar.org` → all **`curl: (56) CONNECT tunnel failed,
   response 403`**. `$HTTPS_PROXY/__agentproxy/status` confirms gateway-level `connect_rejected`
   for `eutils.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `europepmc.org`, `api.openalex.org`. The
   pre-declared blocks on eutils / EBI / PMC / ScienceDirect were **not** re-tested.
4. `mcp__Scholar_Gateway__semanticSearch`, three queries → the corpus indexed there is
   **Wiley-published literature**; AJHG is Elsevier, and **no passage from the Leppa primary is in
   it**. What it did return is a *third* second-hand account, which is reported in §6 and which
   **does not agree with the second-hand account we already had**.

**Net: every reading surface available to this laboratory has been tried. The primary body is
unobtainable here. Everything below that is not the abstract is explicitly labelled as such.**

---

## 1 · What are the actual WWOX CNV numbers?

**ANSWER: not obtainable from the primary. The primary's abstract gives no WWOX-specific count,
percentage, p-value or odds ratio.**

Verbatim, the complete relevant clause of the abstract (PubMed, `get_article_metadata`):

> "We also identified a rare risk locus for ASD and language delay at chromosomal region 2q24
> (implicating *NR4A2*) and another lower-penetrance locus involving inherited deletions and
> duplications of *WWOX*."

That is the **entire** WWOX content of the abstract. It contains **no numerator, no denominator, no
percentage, no p-value and no odds ratio for WWOX.**

The two ORs that *are* in the abstract belong to **other** analyses and must not be transplanted
onto WWOX:

> "We observed a higher burden of large, rare CNVs, including inherited events, in individuals with
> ASD than in their unaffected siblings (odds ratio [OR] = 1.7)"

> "In previously characterized ASD risk loci, we identified 49 CNVs, comprising 24 inherited events,
> 19 de novo events, and 6 events of unknown inheritance, a significant enrichment in affected
> versus control individuals (OR = 3.3)."

⚠️ **OR = 1.7 is the genome-wide large-rare-CNV burden; OR = 3.3 is the aggregate over
previously-characterised ASD risk loci. Neither is a WWOX odds ratio.** If any downstream LEGEND
text ever attaches 1.7 or 3.3 to WWOX, that is a fabrication and must be struck.

**Cohort sizing — and a discrepancy that matters.** The abstract states the study's own denominator:

> "We analyzed 1,532 families from the Autism Genetic Resource Exchange (AGRE)"

The second-hand figures carried into this batch use denominators of **3,565** and **2,633**, which
are **more than double** the 1,532 families the abstract says were analysed. That is not
self-contradictory — Leppa plausibly pooled AGRE with an additional cohort (the Simons Simplex
Collection is the obvious candidate) for the locus-specific test, and the batch's own prior note
records the comparison as "AGRE + SSC" — but **we cannot confirm the composition of a 3,565-family
denominator from anything we actually read.** The only denominator verified from the primary is
**1,532 AGRE families**.

**Whether Leppa computed an OR for WWOX at all: UNRESOLVED, and this is the sharp end of the
question.** The paper is MeSH-indexed under `Odds Ratio` (NLM indexing, not author text), and it
certainly reports ORs for other analyses, so it is *capable* of having reported one for WWOX. But
the abstract does not, and the second-hand sources disagree with each other about whether a numeric
OR exists (§6). **LEGEND must not assert "Leppa reported OR = 8.8" — that attribution is not
verified.**

---

## 2 · Deletions, duplications, or both? Intragenic or whole-gene? Which exons?

**Both — this much is confirmed from the primary's own abstract.** Verbatim:

> "another lower-penetrance locus involving inherited **deletions and duplications** of *WWOX*"

🔴 **This is a substantive point that the framing of `CLAIM 032` must absorb.** The signal is
**bidirectional**: losses *and* gains of WWOX dosage are both in the associated class. A locus where
duplication and deletion are both associated with the same phenotype is behaving like a
**dosage-sensitive / dosage-balance locus**, or like a **structurally fragile locus whose breakage
is the marker** — it is *not* behaving like a clean haploinsufficiency locus, where only loss should
count. **A duplication cannot be evidence for haploinsufficiency.** Any use of Leppa to argue that
half-dose WWOX is harmful has to explain why extra-dose WWOX sits in the same finding.

**Intragenic vs whole-gene, and exon-level detail: NOT OBTAINABLE.** The abstract does not say. The
NLM MeSH indexing for this record includes `Exons`, `Promoter Regions, Genetic` and
`Untranslated Regions`, which indicates the paper discussed sub-genic structure somewhere — **but
MeSH terms are indexer-assigned descriptors, not the authors' words, and I am recording them as a
hint about where the detail lives, not as a finding.** No exon number, no breakpoint coordinate and
no del/dup split can be quoted from this paper.

*Non-primary context, clearly labelled:* Aldaz & Hussain 2019 (*Genes Chromosomes Cancer*,
[10.1002/gcc.22693](https://doi.org/10.1002/gcc.22693), read as full-text passages via Scholar
Gateway) says of the Leppa CNVs — and this is that review's characterisation, not Leppa's words:

> "Even though some of the duplications shown in Figure of individuals with ASD extend 5 upstream of
> *WWOX* (none >0.5 Mbp), Leppa et al concluded that *WWOX* is the target of a rare lowpenetrance ASD
> associated locus."

So at least some events were **not intragenic** — they extended 5′ beyond the gene. That is a
review's reading of a Leppa figure, and **I did not see that figure.**

---

## 3 · Inherited from whom, and were the transmitting parents phenotyped?

**ANSWER: the primary says the events were INHERITED and says nothing else that we can read. The
transmitting parents' phenotype is NOT recoverable from anything obtained.**

The only verbatim statement of inheritance from the primary:

> "another lower-penetrance locus involving **inherited** deletions and duplications of *WWOX*"

The abstract establishes that the study design had full parental genotypes and that inherited events
were the study's whole point in multiplex families:

> "the contribution of both de novo and inherited CNVs to ASD in families with multiple affected
> individuals (multiplex families) is less well understood"

> "In 21 of the 30 families (71%) in whom at least one affected sibling harbored an established ASD
> major risk CNV, including five families harboring inherited CNVs, the CNV was not shared by all
> affected siblings, indicating that other risk factors are contributing."

🔴 **On parental phenotype the primary, at the depth read, says NOTHING — and I want that recorded as
a positive finding rather than a gap in my reading.** No statement about whether transmitting mothers
or fathers were assessed, diagnosed, sub-threshold, or unaffected is present in the abstract. The
question is not answered here in either direction. Note also that **AGRE multiplex families are
ascertained on having two or more affected children**, so whatever the parents' phenotypes are, they
are drawn from families already loaded with ASD liability, and are not a random-population carrier
sample. **Any claim about "Leppa's carrier parents" is presently unsourced.**

One adjacent, clearly-labelled second-hand datum, about *different* families (Mignot, not Leppa),
from Aldaz & Hussain 2019 — it speaks to WWOX carrier parents generally and is the closest thing in
hand:

> "Mignot et al identified deleterious *WWOX* deletions in children affected with infantile epileptic
> encephalopathy (EIEE28, OMIM: 616211) in families where either both parents were carriers of
> heterozygous *WWOX* copy number deletions or one parent harbored a heterozygous copy number deletion
> and the other parent a heterozygous loss of function *WWOX* point mutation."

Those parents were **ascertained as obligate carriers and are not described as affected** — i.e. the
carrier-parent literature continues to describe transmitting heterozygotes without a stated
phenotype. That is Mignot via a review, not Leppa, and it does not close question 3.

---

## 4 · How do the authors qualify penetrance?

**ANSWER: with one word in the abstract, and that word is the strongest verbatim hedge we have.**

> "another **lower-penetrance** locus involving inherited deletions and duplications of *WWOX*"

Note the exact comparative form: **"lower-penetrance"**, not "low-penetrance". It is written
*relative to the other loci in the same sentence and the same paper* — the established ASD major
risk CNVs and the 2q24/*NR4A2* locus. WWOX is being placed **below** those in penetrance, by the
authors, in the abstract, in the same breath in which they report it. That is the authors demoting
their own finding.

Two further author hedges in the abstract bear directly on how much weight any single locus in this
paper can carry:

> "In 21 of the 30 families (71%) … the CNV was not shared by all affected siblings, **indicating that
> other risk factors are contributing**."

> "The genetic architecture in multiplex families … **is complex, warranting more complete genetic
> characterization of larger multiplex ASD cohorts**."

The paper's own closing posture is that its architecture is multi-factorial and its cohorts are too
small. `Penetrance` is also in the record's MeSH list (NLM indexing), consistent with penetrance
being an explicit topic of the body — which we did not read.

⚠️ **What "lower-penetrance" does NOT mean.** It does not mean "mild disease in carriers". It means
**most carriers do not have the phenotype at all.** A lower-penetrance allele is, by construction,
*compatible with a large majority of carriers being clinically well* — which is precisely the
observation about WWOX-DEE carrier parents. The authors' own hedge is therefore not in tension with
`CLAIM 032`; it is the mechanism by which both can be true.

---

## 5 · Dosage sensitivity, and is FRA16D fragility raised as a confounder?

**Dosage: implicitly yes, in the primary — "deletions *and* duplications" is a dosage statement,
and both directions are in it (§2).** No verbatim from Leppa uses the word "dosage".

**FRA16D as a confounder: NOT ADDRESSED ANYWHERE IN WHAT WE OBTAINED — and I am recording this as an
omission I cannot attribute.** The abstract does not mention FRA16D, fragile sites, or genomic
instability. Whether the body discusses it is **unknown**, and it would be wrong to write "Leppa did
not consider FRA16D" — the honest statement is **"we could not determine whether Leppa considered
FRA16D."** 🔴 **This is the single most important unresolved methodological question about the
finding, and it is unresolved.**

Why it is decisive, from Aldaz & Hussain 2019 (*Genes Chromosomes Cancer*, a **review**, full-text
passages via Scholar Gateway — verbatim):

> "*WWOX* is one of the largest human genes spanning over 1.11 Mbp in length at chr16q23.1q23.2 and
> containing *FRA16D*, the second most common chromosomal fragile site. *FRA16D* is a hot spot of
> genomic instability, prone to breakage and for causing germline and somatic copy number variations
> (CNVs). … **Germline CNV polymorphisms affecting *WWOX* are extremely common in humans across
> different ethnic groups.** Importantly, structural variants datasets allowed us to identify a
> specific hot spot for germline duplications and deletions within intron 5 of WWOX coinciding with
> the 5 edge of the *FRA16D* core and various RFLS."

And, on the same locus in neural tissue specifically:

> "these investigators identified the mouse *Wwox* gene among a very limited number of long neural
> genes harboring recurrent DSB clusters undergoing genomic rearrangements in primary neural
> stem/progenitor cells … these recurrent DSB clusters were detected upon aphidicolininduced mild
> replication stress"

🔴 **The confound in one sentence: a locus that breaks more often than average, in everyone, will
generate CNV calls in any cohort — and a cohort ascertained for a neurodevelopmental phenotype is
also a cohort more likely to have been arrayed, more deeply, on better platforms.** Without an
explicit statement that Leppa matched platform, coverage and calling pipeline between the 3,565
cases and the 2,633 siblings, a modest case/sibling excess at the second-most-common fragile site in
the genome is exactly the shape a technical artefact takes. **We cannot check that here.** The prior
LEGEND audit already logged the population baseline from the same review family: germline WWOX CNVs
are "significantly enriched, overlapping a clear hotspot within intron 5", with DGV putting >100 kb
WWOX CNVs at 0.10% of 27,263 individuals — **a general-population rate of the same order as the
0.34% case rate being claimed.**

---

## 6 · Did the second-hand numbers survive?

**Claimed (reaching this batch via Aldaz & Hussain 2020, PMID 33255508): 12/3565 ASD families
(0.34%) vs 1/2633 unaffected siblings (0.04%), p = 0.01, OR = 8.8.**

| Figure | Verdict against the primary |
|---|---|
| 12 cases | ⛔ **NOT FINDABLE in the primary** — and **contradicted by a second secondary source** (below) |
| /3565 | ⛔ **NOT FINDABLE**; the only denominator the primary states is **1,532 AGRE families** |
| 0.34% | ⛔ **NOT FINDABLE** |
| 1/2633 siblings (0.04%) | ⛔ **NOT FINDABLE**; "unaffected siblings" as the comparison group **is** consistent with the abstract's framing of the burden analysis, but the counts are not verifiable |
| p = 0.01 | ⛔ **NOT FINDABLE**. (Per batch rule: extraction can drop exponents — but nothing was dropped here, because **no p-value for WWOX was present to drop**) |
| OR = 8.8 | ⛔ **NOT FINDABLE, and specifically at risk.** The abstract carries OR = 1.7 and OR = 3.3 for other analyses and **no WWOX OR at all**. Whether 8.8 is Leppa's number, or was **computed by the review from a 2×2**, cannot be determined here |
| "lower-penetrance locus", inherited, del **and** dup | ✅ **CONFIRMED verbatim from the primary's abstract** |
| WWOX is the gene | ✅ **CONFIRMED** — `get_article_metadata` returns the gene symbols intact |

**VERDICT ON THE SECOND-HAND NUMBERS: NOT CONFIRMED AND NOT REFUTED — NOT FINDABLE. They remain
review-reported. `FT-103` does not close.**

### 🔴 And it got worse: the two second-hand accounts do not agree with each other

This audit turned up a **third** report of the same Leppa result, from **the same senior author**
(C. Marcelo Aldaz) one year earlier — Aldaz & Hussain 2019, *Genes Chromosomes Cancer*,
[10.1002/gcc.22693](https://doi.org/10.1002/gcc.22693). Verbatim:

> "Several of these CNVs were recently reported by Leppa et al in which they analyzed 1532 families
> to assess the impact of CNVs on the risk of ASD in families with multiple affected individuals.
> **They observed both deletion and duplication of inherited variants spanning *WWOX* in 9 affected
> children, with very high odds ratio.** Even though some of the duplications shown in Figure of
> individuals with ASD extend 5 upstream of *WWOX* (none >0.5 Mbp), Leppa et al concluded that *WWOX*
> is the target of a rare lowpenetrance ASD associated locus."

| | Aldaz & Hussain **2019** (GCC) | Aldaz & Hussain **2020** (PMID 33255508) |
|---|---|---|
| Count | **9 affected children** | **12 families** |
| Unit | **children** | **families** |
| Denominator cited | **1,532 families** (matches the primary's abstract) | **3,565 families** |
| Odds ratio | **"very high odds ratio"** — *no number* | **OR = 8.8** |
| p-value | none given | p = 0.01 |

**Two reviews from the same laboratory, describing the same paper, give different counts, different
units, different denominators, and one of them gives no numeric OR at all.** At most one of them can
be a faithful transcription. This is not a quibble about 9 vs 12 — it means **the chain of custody
for every one of these numbers is broken**, and it is the `D-15` failure mode caught in the act. The
2019 phrasing "**with very high odds ratio**", with no figure attached, is consistent with — though
it does not prove — the possibility that **the 2020 review's "OR = 8.8" was computed or imported
rather than quoted from Leppa.**

🔴 **Operational consequence: `12 / 3565 / 0.34% / 1 / 2633 / 0.04% / p = 0.01 / OR = 8.8` must not
appear anywhere in a LEGEND canonical file, claim, or commit candidate without an attribution that
names the review as the source and flags the 9-vs-12 conflict.** The only WWOX facts from this paper
that may be stated as Leppa's are the four confirmed rows in the table above.

---

## 7 · VERDICT

> ### `CANNOT DETERMINE ON THIS SURFACE`

The primary's body, tables, figures and supplementary material are behind an "All rights reserved"
licence that the only available reading route does not serve, and every other egress path is closed
at the gateway. **No quantitative WWOX finding from Leppa 2016 is verifiable in this environment.**

What *is* verified, from the authors' own abstract, is qualitative and is worth having:
**WWOX is a lower-penetrance ASD-associated locus, involving inherited deletions *and* duplications,
in multiplex families whose own authors conclude that "other risk factors are contributing".**

Had the numbers been verifiable, the most that finding could support is
`WEAK, LOW-PENETRANCE, DOSAGE-ASSOCIATED ONLY` — and I record that as the ceiling, not as the
verdict. The reasons the ceiling is low are independent of whether the numbers check out:
**(a)** duplications sit in the same finding as deletions, and a duplication cannot evidence
haploinsufficiency; **(b)** "lower-penetrance" is the authors' own demotion of the locus relative to
the other loci in their own paper; **(c)** FRA16D makes WWOX a site where CNVs arise in healthy
people at a population rate (DGV 0.10%) of the same order as the case rate being claimed (0.34%),
and we could not establish that the authors addressed it; **(d)** the design is multiplex
ASD-ascertained families, not a population carrier survey.

**This paper does not bear materially on `CLAIM 032`, and no change to `CLAIM 032`,
`CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01`, or the working model is proposed on the strength of
it.** The candidate's §5 limit — *"Leppa 2016 … abstract/metadata depth … review-reported, not
read"* — should be **retained and hardened** with the 9-vs-12 conflict, and `FT-103` re-queued as
**acquisition-blocked (licence wall), not merely unread**.

---

## 8 · Reconciliation with clinically well WWOX-DEE carrier parents

**These two observations do not conflict, and the appearance that they might rests on reading
"lower-penetrance" as "mild" when it means "usually absent".** A low-penetrance risk allele is
defined by most of its carriers being unaffected; an allele conferring even a genuine eightfold
relative risk on a base rate near 0.3% still leaves the overwhelming majority of carriers without
the phenotype, and would be entirely invisible in the handful of WWOX-DEE carrier parents ever
described — a sample far too small to detect a shift of that size even if one existed. The
reconciliation is therefore statistical, not biological, and it requires no revision to the
proposition that heterozygous loss of WWOX is compatible with normal clinical status. Three further
considerations push the same way. First, the Leppa signal is **bidirectional** — duplications as
well as deletions — so it is not a haploinsufficiency signal at all; it is a dosage-*disturbance* or
locus-*fragility* signal, and a WWOX-DEE carrier parent carries a specific loss-of-function allele,
not a fragile-site rearrangement. Second, the families are **multiplex ASD pedigrees**, loaded with
other liability, and the authors say so themselves: *"other risk factors are contributing."* Third,
the truly relevant comparison — the ASD rate among the transmitting parents of the Leppa CNVs
themselves — **is exactly the datum the paper may or may not contain and that we could not read**;
until it is read, the reconciling fact is asserted, not demonstrated. 🔴 **The honest summary is
that clinically well WWOX-DEE carrier parents and a weak, bidirectional, fragile-site-confounded
ASD-risk association at WWOX are comfortably co-true, and that this paper neither strengthens nor
weakens `CLAIM 032` at the depth it could be read.** The one thing it does do is sharpen a caution
already in the batch: if WWOX dosage variation in *either* direction tracks with neurodevelopmental
outcome, then a gene-therapy dose argument built on "partial restoration may suffice" must also
name a **ceiling**, not only a floor — overexpression is not automatically safe on this evidence.

---

## 9 · What would actually close this

1. **The AJHG PDF or the publisher HTML of 10.1016/j.ajhg.2016.06.036** — any environment with
   ScienceDirect or institutional access. The WWOX analysis will be in Results and near-certainly in
   a table; check the **supplementary** tables for the per-family CNV list.
2. Specifically, four things to extract: **(i)** the WWOX case/sibling counts and their denominators
   and cohort composition; **(ii)** whether a WWOX-specific OR and p-value are stated by the authors,
   or whether 8.8 was the review's arithmetic; **(iii)** the del/dup split and breakpoints, and
   whether events are intragenic; **(iv)** any sentence about FRA16D, fragile sites, platform
   matching between cases and siblings, or transmitting-parent phenotype.
3. Failing that, **write to the corresponding author** — Daniel H. Geschwind, dhg@mednet.ucla.edu
   (UCLA), listed as electronic contact on the PubMed record.
4. **Correct the provenance in `wwox_heterozygote_phenotype_audit_20260920.md` line 76 and §"Third,
   the human monoallelic signal"**, which currently carries `12 (0.34%) vs 1 (0.04%), p = 0.01,
   OR = 8.8` with a review citation. The flag `⚠️ review-reported, primary body not read` is already
   there and was correct; what must be **added** is the 9-vs-12 conflict with Aldaz & Hussain 2019.

---

*Sources read for this audit: PubMed record for PMID 27569545 (abstract + metadata + copyright
status), via the PubMed MCP — [DOI](https://doi.org/10.1016/j.ajhg.2016.06.036). Secondary passages
from Aldaz & Hussain 2019, Genes Chromosomes Cancer —
[DOI](https://doi.org/10.1002/gcc.22693) — retrieved as full-text passages via Scholar Gateway and
labelled throughout as second-hand. According to PubMed, no full text for PMC5011063 is available
through the open-access route.*
