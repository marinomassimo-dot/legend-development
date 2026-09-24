# Retrieval capability retest — is the "permanently evidence-blocked" list wrong?

> **Non-canonical, read-only.** ACTOR_ID `scientist-9`, 2026-09-22. Nothing here is medical advice.
> Public edition, genotype-class level. Alleles are never pooled: `lde/lde` is a **rat** allele and
> nothing in it transfers to a human WWOX-DEE genotype class.
>
> 🔴 **No receipt was written and `fulltext_receipts.py record` was NOT run.** §6 proposes payloads
> as field tables only. The Orchestrator decides whether any of them is persisted.

**The question.** Scientist 7 showed that `PMID 19500159`, recorded throughout this repository as
unretrievable, comes back through `mcp__Scholar_Gateway__semanticSearch`. If the blocked list was
built against routes that never included Scholar Gateway, **how much of it is wrong?**

**The answer, in one line.** 29 blocked papers retested; **4 recoverable, 25 not**; and
**publisher predicts recoverability perfectly** — every recoverable paper is on a Wiley-hosted
journal and every non-Wiley paper is absent. **Two genuinely new recoveries**
(`PMID 18371080`, `PMID 26345274`); the other two were already known reachable. The blocked list is
**86 % correct**, and the 14 % it gets wrong is exactly the Wiley subset.

---

## § 0 · Read depth per source

| Source | Depth | Note |
|---|---|---|
| [`CLAUDE.md`](../../../CLAUDE.md) | 🟢 read in full | router; §0 and §1 followed |
| [`framework/state/state_manifest_current.md`](../../../framework/state/state_manifest_current.md) | 🟡 §0–§3 read | header, version block, current-files block |
| [`AUTONOMOUS_SESSION_STATE.md`](AUTONOMOUS_SESSION_STATE.md) | 🟡 lines 790–931 read verbatim; head read in preview | the blocked section, its table, and all four appended corrections |
| [`surface_census.md`](../research/surface_census.md) | 🟢 read in full | all 147 rows + loss ledger |
| [`acquisition_packet_20260920.md`](../research/acquisition_packet_20260920.md) | 🟢 read in full | A1–A9 + priority order |
| [`acquisition_A9_packet_20260921.md`](../research/acquisition_A9_packet_20260921.md) | 🟡 §1–§2 read in full (lines 1–200) | **R4 is load-bearing and was read**: Scholar Gateway already tested on `35984507`, twice, not in corpus |
| [`full_text_queue_current.md`](../research/full_text_queue_current.md) | 🟠 **targeted, not end-to-end** — 7 261 lines | grepped for every blocked marker, then read `FT-041`/`FT-042`/`FT-043`/`FT-044` and `FT-130`/`FT-156`–`FT-170` in full |
| [`acquisition_wave_20260922.md`](acquisition_wave_20260922.md) | 🟡 §1 route table + §2.4–2.6 read | the prior Scholar Gateway test on `41776383` |
| [`framework/protocols/fulltext_read_receipt.md`](../../../framework/protocols/fulltext_read_receipt.md) | 🟡 lines 1–90, 265–315 | depth states + required payload schema |
| **External sources** | see §4 and §10 | PubMed metadata (first-hand); Scholar Gateway **passage depth only** — 29 queries |

🔴 **A Scholar Gateway passage is not a full text.** It is a publisher-side chunk. Where a paper is
called recoverable below, the **number of distinct chunks obtained out of the article's declared
`total_chunks`** is stated, and nothing is called a complete read that is not.

---

## § 1 · The assembled blocked list — **total 29**

Deduplicated across the five named sources plus tonight's stalls. `41776383`, `40235507` and
`36247526` were recorded blocked in `acquisition_wave_20260922.md` rather than in the five named
files; `33914858` is both a tonight stall and a Group-A row and is counted once.

| # | PMID | Group | Where the repo records it blocked | Stated reason |
|---:|---|---|---|---|
| 1 | `15126504` | A | `AUTONOMOUS_SESSION_STATE` blocked line · packet `A1` · `FT-024` | no PMCID |
| 2 | `27569545` | A | blocked line · packet `A2` · `FT-105` | licence wall, verified |
| 3 | `15026124` | A | blocked line · packet `A3` | no PMC deposit |
| 4 | `33914858` | A + E | blocked line · packet `A4` · `FT-044` | no PMCID; surface rejected |
| 5 | `24369382` | A | blocked line · packet `A5` | PMC body empty |
| 6 | `17803050` | A | blocked line · `FT-041` | no DOI, no PMCID |
| 7 | `18371080` | B | 2026-09-21 table · packet `A6` · `FT-109` | no PMCID; Wiley paywall |
| 8 | `25416187` | B | 2026-09-21 table · packet `A7` · `FT-090` | `PMC4935222` metadata-only stub |
| 9 | `26345274` | B | 2026-09-21 table · packet `A8` · `FT-032` | no PMCID |
| 10 | `33134515` | B | 2026-09-21 table · `FT-098` | licence wall |
| 11 | `33300063` | B | 2026-09-21 table · `FT-074` | ⚠️ **untested, not blocked** (own correction) |
| 12 | `31966718` | B | 2026-09-21 table · `FT-074` | verified unobtainable |
| 13 | `36621327` | B | 2026-09-21 table · `FT-074` | verified unobtainable |
| 14 | `30094525` | B | 2026-09-21 table · `FT-032` | ⚠️ **untested, not blocked** |
| 15 | `11719429` | B | 2026-09-21 table · `FT-032` | ⚠️ **untested, not blocked** |
| 16 | `17360458` | B | 2026-09-21 table · `FT-032`/`FT-064` | `PMC1820689` not OA-licensed |
| 17 | `28123895` | B | 2026-09-21 table · `FT-018` | `idIsNotOpenAccess` / `pdf_only` |
| 18 | `21444760` | C | surface census + queue line 2959 · `FT-019` | `idIsNotOpenAccess` / `pdf_only` |
| 19 | `17823927` | C | queue line 2895 · `FT-057` | `idIsNotOpenAccess` / `pdf_only` |
| 20 | `16941225` | C | queue line 2896 · `FT-079` | `idIsNotOpenAccess` / `pdf_only` |
| 21 | `35984507` | D | packet `A9` | zero-length PMC body (operator later supplied PDF) |
| 22 | `19500159` | D | `FT-042`; census `pdf_only` | 8 automated tiers refused — **positive control** |
| 23 | `41776383` | E | `FT-162` · `acquisition_wave` §2.5 | no PMCID; SAGE-walled |
| 24 | `40235507` | E | `FT-161` · `acquisition_wave` §2.4 | `PMC11998783` serves `full_text: ""` |
| 25 | `36247526` | E | `FT-160` · `acquisition_wave` §2.2 | body served but **gene symbols + GEO accession stripped** |
| 26 | `41442931` | F | queue `EVIDENCE_BLOCKED`, verified | no PMCID; Elsevier |
| 27 | `21476439` | F | queue `FT-130`, two routes | no DOI, no PMCID |
| 28 | `41538440` | F | queue, metadata-only | no PMCID; publisher `403` |
| 29 | Gribaa 2007 (`FT-033`) | F | queue line 6757; census `doi_only` | no PMCID; DOI `10.1093/brain/awm078` |

**Total: 29.**

⚠️ **What this list is not.** It is not every blocked entry in the 7 261-line queue. Rows 26–29 are
the ones a grep for blocked markers surfaced with an identifier and an explicit status line; there
are further `abstract_only` rows whose blockage is asserted but not measured. The §7 rule is written
so it applies to those too without needing them enumerated.

⚠️ **Not re-litigated, per the brief.** The three rows marked ⚠️ *untested* (`33300063`, `30094525`,
`11719429`) were tested with `convert_article_ids` by the Orchestrator tonight and **no PMCID exists
for any**. That is taken as settled. They are retested here **only** against Scholar Gateway, which
is a different question.

---

## § 2 · The retest table

Method: one or more `mcp__Scholar_Gateway__semanticSearch` calls per paper, each a natural-language
question **only that paper could answer**, so a hit is identifiable. **29 queries total.** Four papers
(`33134515`, `28123895`, `21444760`, `30094525`) had a first query that was mis-targeted against the
paper's actual subject and were **re-tested with a paper-specific query**; `31966718` and `17803050`
also received a second query. All second queries agreed with the first. Journal and
publisher from PubMed metadata, first-hand.

| # | PMID | Journal | Publisher | Why the repo called it blocked | Scholar Gateway result | Verdict | What it would unblock |
|---:|---|---|---|---|---|---|---|
| 22 | `19500159` | *Genes Brain Behav* | **Wiley** | 8 automated tiers refused; `pdf_only`, `SUSPECT`-adjacent | **13 of 18 chunks** across 5 queries: abstract, Introduction, Results incl. Fig. 1 legend, Discussion, Table 1, Table 2 | 🟢 **RECOVERABLE** (positive control holds) | a clean, quotable surface for `CLAIM 038`/`CLAIM 039` — see §4.1 |
| 7 | `18371080` | *Eur J Neurosci* | **Wiley** | no PMCID; Wiley paywall; packet `A6` | **9 of 17 chunks**: abstract, Introduction ×2, **complete Materials & Methods** ×2, Results ×2 incl. Fig. 6/9 legends, **Discussion** | 🟢 **RECOVERABLE** | 🎯 packet `A6` in full — peptide mechanism, dose, route, vehicle, controls. See §4.2 |
| 9 | `26345274` | *Am J Med Genet A* | **Wiley** | no PMCID; packet `A8` | **6 of 6 chunks** — abstract, Introduction+Methods, Results ×2 incl. all three figure legends, Discussion ×2 | 🟢 **RECOVERABLE — complete narrative** | 🎯 packet `A8` in full; `CLAIM 039`'s human-imaging counterpart. See §4.3 |
| 19 | `17823927` | *Genes Chromosomes Cancer* | **Wiley** | `idIsNotOpenAccess` / `pdf_only` | **9 of 14 chunks** | 🟢 **RECOVERABLE** — ⚠️ **already known**: `wwox_antibody_epitope_census_20260922.md` quotes this DOI via Scholar Gateway | the `Wwox^gt/gt^` gene-trap primary at passage depth |
| 1 | `15126504` | *J Biol Chem* | ASBMB | no PMCID | 0 passages for it; a Wiley **conference abstract** (Kindy 2008, `10.1016/j.jalz.2008.05.262`) surfaced instead | 🔴 **NOT IN CORPUS** | — |
| 2 | `27569545` | *Am J Hum Genet* | Elsevier / Cell Press | licence wall | 0 | 🔴 NOT IN CORPUS | — |
| 3 | `15026124` | *Neuroscience* | Elsevier | no PMC deposit | 0 | 🔴 NOT IN CORPUS | — |
| 4 | `33914858` | *Brain* | Oxford Univ. Press | no PMCID | 0 (query named Synapsin/Nestin/Olig2/GFAP-Cre explicitly) | 🔴 NOT IN CORPUS | — |
| 5 | `24369382` | *Brain* | Oxford Univ. Press | empty PMC body | 0 | 🔴 NOT IN CORPUS | — |
| 6 | `17803050` | *Comparative Medicine* | AALAS | no DOI, no PMCID | **0 across 2 independent queries** (vacuole/cerebellum; serum chemistry/GH) | 🔴 **NOT IN CORPUS** | — |
| 8 | `25416187` | *Exp Biol Med* | SAGE | metadata-only stub | 0 | 🔴 NOT IN CORPUS | — |
| 10 | `33134515` | *Neurol Genet* | Wolters Kluwer / AAN | licence wall | 0 across **2** queries (first mis-targeted; the paper is *"Association of blood-based transcriptional risk scores with biomarkers for Alzheimer disease"*) | 🔴 NOT IN CORPUS | — |
| 11 | `33300063` | *Mol Med Rep* | Spandidos | untested→no PMCID | 0 | 🔴 NOT IN CORPUS | — |
| 12 | `31966718` | *Int J Clin Exp Pathol* | e-Century | unobtainable | 0 across **2** queries (second named EBV-LMP1 / AKT-mTOR / nasopharyngeal carcinoma, the paper's own subject) | 🔴 NOT IN CORPUS | — |
| 13 | `36621327` | *Int Immunopharmacol* | Elsevier | unobtainable | 0 | 🔴 NOT IN CORPUS | — |
| 14 | `30094525` | *Neurol Sci* | Springer | untested→no PMCID | 0 across **2** queries (second named the WWOX-encephalopathy phenotypic spectrum and genotype–phenotype correlation) | 🔴 NOT IN CORPUS | — |
| 15 | `11719429` | *Cancer Res* | AACR | untested→no PMCID | 0 | 🔴 NOT IN CORPUS | — |
| 16 | `17360458` | *PNAS* | NAS | not OA-licensed | 0 | 🔴 NOT IN CORPUS | — |
| 17 | `28123895` | *Oncoimmunology* | Taylor & Francis | `idIsNotOpenAccess` | 0 across **2** queries (first mis-targeted; the paper is *"The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis"*) | 🔴 NOT IN CORPUS | — |
| 18 | `21444760` | *J Lipid Res* | ASBMB / Elsevier | `idIsNotOpenAccess` | 0 across **2** queries (second named the mouse QTL map / human HDL GWAS, the paper's own subject) | 🔴 NOT IN CORPUS | — |
| 20 | `16941225` | *J Mol Histol* | Springer | `idIsNotOpenAccess` | 0 | 🔴 NOT IN CORPUS | — |
| 21 | `35984507` | *Cell Mol Life Sci* | Springer | zero-length PMC body | 🔁 **prior measurement reused** — packet `A9` R4, two queries 2026-09-21, corpus does not contain it | 🔴 NOT IN CORPUS | — |
| 23 | `41776383` | *Mult Scler* | SAGE | no PMCID; SAGE wall | 0 — **second independent confirmation** (first in `acquisition_wave` §1) | 🔴 NOT IN CORPUS | — |
| 24 | `40235507` | *Res Sq* (preprint) | Research Square | `full_text: ""` | 0 (query returned Wiley *Alzheimer's & Dementia* conference abstracts of adjacent work, incl. `10.1002/alz70855_105855`) | 🔴 NOT IN CORPUS | — |
| 25 | `36247526` | *IBRO Neurosci Rep* | Elsevier | GEO accession stripped by extractor | 0 — **the accession stays unreachable** | 🔴 NOT IN CORPUS | — |
| 26 | `41442931` | *Pediatr Neurol* | Elsevier | no PMCID | 0 | 🔴 NOT IN CORPUS | — |
| 27 | `21476439` | *Z Naturforsch C* | De Gruyter | no DOI, no PMCID | 0 | 🔴 NOT IN CORPUS | — |
| 28 | `41538440` | *Science* | AAAS | no PMCID; publisher 403 | 0 | 🔴 NOT IN CORPUS | — |
| 29 | Gribaa 2007 | *Brain* | Oxford Univ. Press | no PMCID | 0 (covered by the SCAR12 carrier-parents query, which returned 13 Wiley articles and no *Brain*) | 🔴 NOT IN CORPUS | — |

**Totals: 4 RECOVERABLE · 0 PARTIAL-only · 25 NOT IN CORPUS.** No paper returned a single ambiguous
passage, so the `PARTIAL` cell is empty — the corpus boundary is sharp, not graded.

---

## § 3 · Does publisher predict recoverability? — **yes, perfectly, with a correction to how you test it**

| | Recoverable | Not in corpus | Total |
|---|---:|---:|---:|
| **Wiley-hosted journal** | **4** | 0 | 4 |
| Any other publisher | 0 | **25** | 25 |
| Total | 4 | 25 | **29** |

Sensitivity 4/4 = **100 %**. Specificity 25/25 = **100 %**. Under the null that recoverability is
independent of publisher, the probability of a split this clean is
`1 / C(29,4) = 1/23 751 ≈ 4.2 × 10⁻⁵` (Fisher exact, one-sided).

⚠️ **This is a confirmation, not a discovery, and it was not blind.** The hypothesis was supplied in
the dispatch and the publisher of each paper was known from PubMed before its query ran. What is
measured is the **outcome**, not the guess. The repository also already carried the rule in one
line, at `full_text_queue_current.md:4847` — *"Scholar Gateway indicizza Wiley"* — written on
2026-09-21 and never generalised into a routing rule. **The finding here is that the one-liner is
exactly right and load-bearing, and that it was never applied to the blocked list.**

### 🔴 The correction that matters: **DOI prefix does not predict. Journal host does.**

A rule of the form *"try Scholar Gateway if the DOI starts `10.1002` or `10.1111`"* would have
missed four of the corpus hits observed tonight and would be wrong about a fifth class:

| Observed in corpus | DOI prefix | Why it is nevertheless Wiley |
|---|---|---|
| `10.2164/jandrol.108.005066` — *J Androl* (Takenaka 2008, the `lde/lde` sibling) | `10.2164` | title migrated to Wiley; served from `onlinelibrary.wiley.com` |
| `10.1016/j.jalz.2008.05.262` — *Alzheimer's & Dementia* | `10.1016` | Wiley journal on a legacy Elsevier prefix |
| `10.1016/j.ijdevneu.2019.10.003` — *Int J Dev Neurosci* | `10.1016` | same |
| `10.1684/epd.2018.1005` — *Epileptic Disorders* | `10.1684` | John Libbey → Wiley |
| `10.1155/2013/108486` — Hindawi titles | `10.1155` | Hindawi is Wiley-owned |
| `10.1113/JP272822` — *J Physiol* · `10.1096/fj…` — *FASEB J* · `10.1634/stemcells…` · `10.1046`/`10.1034` legacy Blackwell | various | all Wiley-hosted |

Conversely `10.1016/j.ibneur…` (`36247526`, Elsevier-owned *IBRO Neurosci Rep*) is **absent**, on the
same prefix as two present articles. **The discriminator is "is this journal currently served from
`onlinelibrary.wiley.com`", not the DOI registrant.** That is checkable from the PubMed journal title
without any fetch, and it is what §7 encodes.

### What this costs and what it saves

- **The blocked list is 25/29 = 86 % correct.** It is not "substantially wrong". It is wrong in one
  predictable place.
- **2 of the 4 recoverables were genuinely new** (`18371080`, `26345274`); `19500159` was shown
  tonight by Scientist 7 and `17823927` was already being quoted through this route on 2026-09-22.
  So the honest yield of this retest is **two papers**, both from acquisition packets, both `HIGH`.
- **The saving is the other 25.** Every future session now has a one-line test that tells it not to
  spend an acquisition act on a non-Wiley blocked paper.

---

## § 4 · What was recovered, per paper

All quotations are from Scholar Gateway passage bodies, publisher-side rendering. The extractor
**strips italics markers and some mathematical symbols** (`lde/lde` arrives as `*lde/lde*`,
`P < 0.05` may arrive with the comparator missing) — the same italic-class defect this repository
documents for the PMC route. Quotations below are reproduced as served; nothing is silently repaired.

### 4.1 · `PMID 19500159` — positive control, and it pays a dividend

Suzuki H *et al.* 2009, *Genes Brain Behav* 8(7):650–660, [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x).
**13 of 18 chunks.** Sections seen: abstract (chunk 0), Introduction (1), **Results (8)**,
Discussion (13, 15), Table 1, Table 2, Fig. 1 legend.

🎯 **The subfield and laminar detail the dispatch wanted from `17803050` exists here, as this
paper's own data** — not Suzuki 2007's. **Results, verbatim:**

> "Histological examination detected many extracellular vacuoles in the hippocampi of all affected
> (*n* = 9) (Fig. 1b,d) and the amygdala of six affected backcross progeny, but not in any of
> the normal rats (*n* = 10) (Fig. 1a,c)."

**Figure 1 legend, verbatim:**

> "***Coronal sections of hippocampus in normal (a, b) and affected backcross (c, d) female rats at
> 28 days of age.** (a, b) Many vacuoles were dispersed in the CA1 region of the lateral hippocampus
> (bar = 1 mm). (c, d) Many vacuoles with various seize were present around pyramidal layer cells.
> The high magnification of open square in (a) and (b) (bar = 100 m).*"

⚠️ **Two cautions, both real.** (i) The legend's panel lettering is **internally inconsistent** with
the Results sentence — Results says normal = a,c and affected = b,d; the legend says normal = a,b and
affected = c,d, while describing vacuoles in "(a, b)". One of the two is mislabelled in the source.
**Do not quote the panel letters.** The *content* — CA1 region, vacuoles around pyramidal-layer
cells, 28 days, 9/9 vs 0/10 — is stated twice and is safe. (ii) `sieze` for *size* is the source's
typo, reproduced.

🔴 **The cerebellum question is NOT answered.** Two dedicated queries returned no cerebellar
histology statement from any `lde/lde` primary. The only cerebellar sentence in this paper is about
**expression in mice, cited to a third paper**:

> "The Wwox protein has been reported to be widely expressed in the murine developing nervous system
> including cerebral cortex, corpus striatum, limbic system, hypothalamus, cerebral peduncles and
> cerebellum (Chen *et al.*2004)."

The sibling sentence the dispatch quoted — *"we did not detect any marked pathologic changes in the
cerebella"* — **was not located in any retrievable source.** It stays `HUMAN_REQUIRED` (§5).

**And the `CA1 + amygdaloid body` attribution to Suzuki 2007 is confirmed as second-hand**, from the
Wiley-hosted sibling `PMID 18676360` (Takenaka 2008, *J Androl*, `10.2164/jandrol.108.005066`),
which is in the corpus:

> "In a previous histological study, we found many extracellular vacuoles in the CA1 region of the
> hippocampus and the amygdaloid body of the *lde*/*lde* brain at 28 days of age. … (Suzuki et al,
> 2007)."

⇒ The CA1/amygdaloid-body localisation of the Suzuki 2007 data remains 🔴 **SIBLING-ATTESTED**. What
changes is that a **second, independent sibling now attests it**, and `19500159`'s own backcross
cohort reproduces the same localisation first-hand in a different genetic background.

### 4.2 · 🎯 `PMID 18371080` — packet `A6` answered, and the closure it rests on survives

Lo C-P, … Chang N-S, Chen S-T 2008, *Eur J Neurosci* 27(7):1634–1646,
[DOI](https://doi.org/10.1111/j.1460-9568.2008.06139.x). **9 of 17 chunks**, including the
**complete Materials and methods**, the Results arm on the peptide, and the Discussion.

The `A6` checklist, answered item by item from the body rather than the abstract.

**(3) Was the peptide ever tested in a WWOX-depleted background?** — **No. Materials and methods,
verbatim:**

> "We have made short synthetic peptides of WOX1, without (WWpep) or with Tyr33 phosphorylation
> (pYWWpep; amino acid # 2838) at the first WW domain (Chang *etal*., 2003a). To investigate
> the effect of these synthetic WOX1 peptides on neuronal survival and death, rats were injected with
> these peptides in the presence or absence of MPP^+^ as follows: (i) MPP^+^ iodide (50mm);
> (ii) WWpep or pYWWpep (2mm); (iii) WWpep (or pYWWpep) and MPP^+^ or (iv) sterile saline.
> Intracranial injection to the brain striatum (1L injection in 5min) was performed as described
> above."

⇒ **Dose 2 mM · route intracranial, direct into striatum · volume 1 µL over 5 min · vehicle sterile
saline · animals 50 mature male Sprague-Dawley rats, 300–350 g.** Every arm is an
**MPP⁺-intoxicated wild-type** rat. There is **no genetic WWOX manipulation anywhere**, so the
paper cannot speak to a WWOX-deficient brain.

**(4) The non-phospho control.** Present and negative — Results, verbatim:

> "Importantly, pYWWpep alone did not effectively cause cell death, but significantly blocked
> MPP^+^induced neuronal apoptosis (Fig.9A). WWpep could not inhibit the effect of MPP^+^
> (data not shown)."

⚠️ **"data not shown" is doing load-bearing work for the control arm.** The peptide's specificity
rests on an unshown panel.

**(1) The mechanism, from the Discussion — decoy, not substitution:**

> "we further substantiate our observations by showing that the phosphoWOX1 peptide blocks nuclear
> translocation of CAD and pJNK1 in the rat brains, suggesting that the phosphopeptide binds CAD and
> JNK1 and blocks their activities. Short peptides do not normally possess tertiary structures in
> solutions. Thus, they cannot represent the actual functional properties of the fulllength WOX1.
> Whether the phosphoWOX1 peptide binds specific enzymes, thereby blocking neuronal death, remains
> to be established."

🎯 **`HYP-20260709-04`'s refutation and `DL-MOL-008`'s closure both hold, and they no longer rest on
an abstract.** The peptide is an 11-residue WW-domain fragment injected into the striatum that acts
by **sequestering CAD and JNK1**, and the authors say in their own Discussion that it cannot
represent full-length WWOX. It supplies nothing. 🔴 There is also **no BBB question to answer** —
the route is direct intracranial injection, so the abstract's "therapeutic potential" is not a
systemic claim.

⚠️ **One thing narrows rather than confirms the repository's reading.** The same Discussion states a
**protective** role for WWOX in the physiological setting:

> "activated WOX1 protects against chronic neuronal damage under physiological conditions. Further
> upregulation of activated WOX1 is needed to enhance the death of damaged neurons in the diseased
> brains."

So this paper does **not** say WWOX activation is uniformly a death signal; it proposes a
**dose/context-dependent** role. Any repository statement of the form *"this laboratory holds that
activated WWOX kills neurons"* is **over-flattened** and should be qualified to the MPP⁺-intoxicated
setting. That is a narrowing of a premise, not a reversal, and it is the kind of thing the abstract
could not have shown.

🔴 **What was NOT recovered:** chunks 4, 7–10, 12, 16 — parts of Methods (peptide synthesis /
immunohistochemistry), Results Figs. 1–5 and 8, and the reference list. Figure **panels** are not
inspectable by any route here. ⇒ `partial_fulltext_read` at best, never complete.

### 4.3 · 🎯 `PMID 26345274` — packet `A8` answered in full; `CLAIM 039` gets its human comparator

Tabarki B, AlHashem A, AlShahwan S, Alkuraya FS, Gedela S, Zuccoli G 2015, *Am J Med Genet A*
167A(12):3209–3213, [DOI](https://doi.org/10.1002/ajmg.a.37363). **6 of 6 chunks — the complete
served narrative**: abstract, Introduction + Methods, Results ×2 (incl. all three figure legends),
Discussion ×2.

**(1) How "spared" was determined — Methods, verbatim:**

> "Retrospective review of the patient charts including their clinical history and molecular genetic,
> neuro diagnostics, and neuro radiological investigations. … All five patients had EEG and ERG, and
> all patients underwent brain MRI."

⇒ **Retrospective qualitative chart review. No volumetry. No blinding to genotype. No sequence
protocol stated beyond the sequences named in the figure legends (sagittal T1, axial T2).**

**(3) Is sparing stated for all five, or some? — Results, verbatim:**

> "The neuro imaging revealed multiple brain abnormalities. The first patient's MRI demonstrated
> progressive atrophy of the periventricular white matter resulting in volume loss of the corpus
> callosum and the upper brainstem likely reflecting Wallerian degeneration. **The cerebellum
> including the vermis was spared from the neurodegenerative process** (Figs. and ). In the second
> patient, marked atrophy of the corpus callosum was noted, and mild degeneration of the upper
> brainstem which appeared flattened on midsagittal images. **The cerebellar vermis and tectal plate
> remained within normal limits.** T2weighted images showed focal lesions in the medial nuclei of the
> thalami (Fig. )."

🔴 **The prose describes the imaging of two patients, not five.** "The cerebellum is spared" is
asserted of **Patient 1 and Patient 2 only**; patients 3–5 have no imaging description in the served
text and Table I carries no imaging row. **The abstract's generalisation to all five is not supported
by the body.**

**(2) Age at imaging — Figure 2 and Figure 4 legends, verbatim:**

> "*Patient 1. Diffuse thinning of the corpus callosum (A, arrowheads) which is, however, completely
> formed and a normal brainstem (A, arrow) are noted at the ages of 17 days. Followup examination
> obtained at the age of 11 months demonstrate interval volume loss of the corpus callosum
> (B, arrowheads) and of the upper brainstem with flattening of the mesencephalon and enlargement of
> the cerebral aqueduct of Sylvius (B, arrow).*"
>
> "*Patient 2. (21 weeks). Sagittal T1weighted image delineates a markedly hypoplastic corpus callosum
> (A, arrowheads) and flattening of the brainstem reflecting early neurodegeneration (A, arrow).
> Axial T2weighted images show bilateral symmetrical lesions in the medial nuclei of the thalami
> (B, arrows) and posterior periventricular white matter loss (B, arrowheads).*"

🎯 **This is decisive for the contradiction the packet flagged.** Sparing is asserted at **17 days,
21 weeks and 11 months** — all under one year. `PMID 35573960` (Riva 2022, read in full here) reports
inferior-vermis hypoplasia at **7 days** and again at **2 y 4 m**. ⇒ **The two sources are not
directly contradictory on age, and they are not measuring the same thing**: Tabarki reports *no
progressive degeneration of an initially normal cerebellum* over 0–11 months; Riva reports
*hypoplasia*, a developmental size statement, from day 7. **"Spared" and "hypoplastic" are
compatible**, and the packet's own correction — that midline vermian hypoplasia on MRI and an
unremarkable cerebellar cortex are different propositions — is **confirmed by the primary text**.

⚠️ **Read the mood.** The Discussion's closing is a proposal, and it **drops the cerebellum clause
that the abstract carries**:

> "We suggest that neuroimaging in these patients reveals a characteristic pattern of
> neurodegeneration that could help with early diagnosis."

⇒ The phrase *"in which the cerebellum is spared"* appears in the **abstract** and in **Results for
two patients**, and **not** in the Discussion's conclusion. The re-voicing hazard the repository named
on 2026-09-21 applies exactly here.

**(4) Natural history — Results + Table I, verbatim:** epilepsy onset **2–3 months**; seizures
multifocal or focal-with-secondary-generalisation evolving to infantile spasms then Lennox-Gastaut;
*"medically intractable being resistant to multiple antiepileptic medications even when used in
combination"*; progressive microcephaly −4 SD to −4.6 SD; spasticity in the first 3 months; *"All
five of our patients died before their third birthday"*; *"One of the two families had history of
four spontaneous abortions."*

**(5) Retinopathy:** *"The ERG was abnormal in two patients (family 2, IV:1, IV:2) and normal in
three patients (family 1, IV:1, IV:2, IV:4)."* ⇒ **ERG only**; no fundus or OCT characterisation.

**Allele class — Results, verbatim, and it matters for the reference genotype's acceptor allele:**

> "This mutation abolishes the canonical splice acceptor (1 position). Unfortunately, RTPCR could
> not be performed to empirically test the consequence of the mutation but it is highly likely to
> result at least in skipping of the downstream exon seven with consequent inframe loss of 62 amino
> acids (p. (Pro203_Arg264del)). Such a deletion will remove the mitochondrial targeting sequence
> (209273) and a large portion of the C terminal shortchain dehydrogenase/reductase domain (125330)."

🔴 **The splicing consequence was never measured.** *"RT-PCR could not be performed"* — the in-frame
62-residue deletion is a **prediction**, not a result. Any repository line treating
`c.606-1G>A` → `p.(Pro203_Arg264del)` as an observed transcript outcome must be demoted to inferred.
🔴 **And it is a different allele from the reference genotype's acceptor variant. Same class is not
same allele; nothing is pooled.**

⚠️ **One error inside the source, recorded not repaired.** The Discussion says *"`WWOX` induced
audiogenic seizures in `Wwox` **Knockout rats** [Suzuki et al., ]"*. Suzuki 2009 is a **spontaneous
13-bp exon-9 deletion**, not a knockout. The repository must not inherit that description.

### 4.4 · `PMID 17823927` — recoverable, already known

Ludes-Meyers JH *et al.* 2007, *Genes Chromosomes Cancer* 46(12):1129–1136,
[DOI](https://doi.org/10.1002/gcc.20497). 9 of 14 chunks. Not deep-dived here: the repository is
already quoting this DOI through this route in
[`wwox_antibody_epitope_census_20260922.md`](wwox_antibody_epitope_census_20260922.md). Recorded so
the blocked-list row for `FT-057` can be corrected.

---

## § 5 · What stays blocked, and why

🔴 **`HUMAN_REQUIRED` — 25 papers, rows 1–6, 8, 10–18, 20, 21, 23–29 of §1.** Every automated route
available in this deployment is now exhausted for them: PMC (`get_full_text_article`), the PMC
licence probe (`get_copyright_status`), identifier resolution (`convert_article_ids`), and — new
tonight — **Scholar Gateway**. `find-fulltext` remains inoperable because every tier of its cascade
is an HTTP fetch to an egress-blocked host. **No further automated route exists to try.**

Three of them deserve a named line because they block something specific and nothing else can reach
it:

| PMID | What stays unreachable | Consequence |
|---|---|---|
| `17803050` | 🎯 **the `lde/lde` brain primary.** The cerebellar-histology sentence, the sampling frame (which organs and brain regions were sectioned), n, stain and section plane | **The cerebellum question in `lde/lde` is not answerable here by any route.** `CLAIM 039`'s *"ataxia without structural correlate"* rests on a statement nobody in this deployment can read. Worse: the repository's own surface for this paper was **rejected** on 2026-08-09 (34 `U+001D` corruptions), so the 2026-08-06 reading's 29 text locators are unverifiable **and** `files/fulltext/` is gitignored, so a fresh clone has nothing at all |
| `33914858` | the conditional-Cre genetics that parked `HYP-20260709-07` | remains held **second-hand** through Obeid 2026. *Brain* is OUP; Scholar Gateway will never carry it. **Human institutional access only** |
| `36247526` | the **GEO accession**, stripped by the PMC extractor | the one species-matched hippocampal-subfield dataset in existence stays unusable. Scholar Gateway does not index *IBRO Neurosci Rep* |

🔴 **No external action was taken.** No author was contacted, no PDF requested, no form filled, no
laboratory emailed. Paywalled ⇒ recorded and moved on, per the dispatch.

---

## § 6 · 🔴 Proposed receipt payloads — **NOT written to the ledger**

`fulltext_receipts.py record` was **not run**. These are proposals as field tables. Two of them are
`queried_not_full_read`, which the protocol explicitly states **does not count as full text
analysed** — that is the honest depth for passage retrieval, and it is offered deliberately rather
than inflating a passage into a read.

### P-1 · `PMID 18371080`

| Field | Proposed value |
|---|---|
| `event_id` | `FTR-20260922-18371080-01` |
| `record_kind` | `contemporaneous_receipt` |
| `study_id` | `{pmid: "18371080", doi: "10.1111/j.1460-9568.2008.06139.x"}` |
| `workflow` | `scientist-9 retrieval-capability retest, Scholar_Gateway semanticSearch` |
| `evidence_depth` | 🔴 **`partial_fulltext_read`** |
| `source_locator` | `https://onlinelibrary.wiley.com/ai/10.1111/j.1460-9568.2008.06139.x` (publisher-side passage rendering) |
| `source_fingerprint` | `null` — no lawful local artifact exists |
| `source_kind` | `fulltext_remote_passages` ⚠️ **not a value the protocol defines; the Orchestrator must decide whether to extend the enum or refuse the receipt** |
| `coverage` | abstract `read` · introduction `read` · methods `read` · results `partial` · figures `captions_only` (Figs. 1,2,3,4,6,7,9 legends only) · tables `not_present` · discussion `read` · limitations `not_present` · supplementary `not_read` · references `unavailable` |
| `chunks` | 9 of 17 declared (`0,1,2,3,5,6,13,14,15`) |
| `outputs` | this file |
| `prior_receipt` | `null` |
| `reread_reason` | `first_read` |

### P-2 · `PMID 26345274`

| Field | Proposed value |
|---|---|
| `event_id` | `FTR-20260922-26345274-01` |
| `record_kind` | `contemporaneous_receipt` |
| `study_id` | `{pmid: "26345274", doi: "10.1002/ajmg.a.37363"}` |
| `workflow` | same as P-1 |
| `evidence_depth` | 🔴 **`partial_fulltext_read`** — 6/6 chunks is the **complete served narrative**, but figure **panels** were never inspected and the reference list is absent, so `complete_fulltext_read` is refused |
| `source_locator` | `https://onlinelibrary.wiley.com/ai/10.1002/ajmg.a.37363` |
| `source_fingerprint` | `null` |
| `source_kind` | `fulltext_remote_passages` ⚠️ same enum question |
| `coverage` | abstract `read` · introduction `read` · methods `read` · results `read` · figures `captions_only` (Figs. 1–4) · tables `read` (Table I) · discussion `read` · limitations `not_present` · supplementary `not_read` · references `unavailable` |
| `chunks` | **6 of 6** (`0,1,2,3,4,5`) |
| `outputs` | this file; would discharge packet item `A8` |
| `prior_receipt` | `null` |
| `reread_reason` | `first_read` |

### P-3 · `PMID 19500159` — **supplementary, not a new read**

| Field | Proposed value |
|---|---|
| `event_id` | `FTR-20260922-19500159-02` |
| `record_kind` | `contemporaneous_receipt` |
| `evidence_depth` | 🔴 **`queried_not_full_read`** — 13/18 chunks, but a complete read already exists |
| `prior_receipt` | `FTR-20260806-19500159-01` |
| `reread_reason` | `adversarial_re_retrieval` — *the 2026-08-06 surface was a locally transcribed PDF text layer; this is an independent publisher-side rendering of the same body and can re-anchor locators the 2026-08-09 surface rejection left unverifiable* |
| `why it matters` | 🎯 **this is the strongest operational consequence in this file** — see §7 note |

### P-4 · `PMID 17823927`

| Field | Proposed value |
|---|---|
| `event_id` | `FTR-20260922-17823927-01` |
| `evidence_depth` | `queried_not_full_read` — 9/14 chunks, retrieved as a capability test, not read for content |
| `note` | the blocked-list row for `FT-057` should simply be corrected; a receipt may not be warranted |

⚠️ **The enum problem, stated once.** `source_kind: fulltext_local` and `source_fingerprint: <sha256>`
assume a lawful local artifact. Scholar Gateway passages are remote and cannot be fingerprinted here.
**Either the protocol gains a remote-passage kind with the chunk set as its integrity statement, or
this route can never produce a receipt and its output is limited to non-canonical analysis files like
this one.** That is a governance decision, not a scientific one, and it is handed back unresolved.

---

## § 7 · The proposed routing rule

🔴 **Proposed text only. `framework/scripts/README.md` was NOT edited.**

> ### When a paper is recorded as blocked
>
> Blocked is a statement about routes tried, not about the paper. Before spending an acquisition act
> or asking a human, run this ladder. It is four cheap steps and it stops at the first that returns a
> body.
>
> | # | Step | Tool | Stop if |
> |---:|---|---|---|
> | 1 | Does a PMCID exist? | `mcp__PubMed__convert_article_ids` | No PMCID ⇒ skip step 2 entirely |
> | 2 | Does the PMC record serve a **body**? | `mcp__PubMed__get_full_text_article`, then **measure `len(full_text)`** | Body length > 0 ⇒ read it. **A PMCID is not a body** (`PMC4935222`, `PMC11998783`, `PMC12734678` all resolve and serve `""`) |
> | 3 | 🎯 **Is the journal served from `onlinelibrary.wiley.com`?** | the PubMed journal title is enough — no fetch needed | **Yes ⇒ `mcp__Scholar_Gateway__semanticSearch`.** **No ⇒ stop, mark `HUMAN_REQUIRED`, do not query** |
> | 4 | Everything else | — | `find-fulltext` is **inoperable in this deployment** — every tier of its cascade is an HTTP fetch to an egress-blocked host. Do not dispatch it |
>
> **Step 3 is decided by the journal's current publisher, NOT by the DOI prefix.** Measured on
> 2026-09-22 over 29 blocked papers: Wiley-hosted 4/4 recoverable, everything else 0/25.
> In corpus: `10.1002`, `10.1111`, `10.1046`, `10.1034`, `10.1096` (*FASEB J*), `10.1113`
> (*J Physiol*), `10.1155` (Hindawi), `10.1634` (*Stem Cells*), `10.1684` (*Epileptic Disorders*),
> **and Wiley titles on legacy prefixes** — `10.2164` (*J Androl*), `10.1016/j.jalz`
> (*Alzheimer's & Dementia*), `10.1016/j.ijdevneu`, `10.1016/j.febslet` (FEBS).
> Absent: Elsevier proper (incl. Cell Press and `10.1016/j.ibneur`), Springer Nature, Oxford
> University Press, SAGE, Taylor & Francis, AACR, ASBMB, PNAS/NAS, AAAS, Wolters Kluwer, Spandidos,
> De Gruyter, AALAS, Research Square.
>
> **Querying Scholar Gateway is semantic, so ask a question only that paper can answer** — a title or
> keywords will return the topic and not the paper. Judge presence by the returned **DOI**, never by
> topical similarity.
>
> **What comes back is chunks, not a full text.** The response declares `total_chunks` per article;
> issue several queries aimed at different sections and **report the chunk set you obtained**. Do not
> call a paper read on one passage, and never quote figure **panels** — only legends are served.
>
> ⚠️ **Step 3 also applies to papers already recorded as read.** A Wiley paper whose local surface was
> rejected or is gitignored can be **re-anchored** from this route without an acquisition act.

🎯 **The consequence worth more than any recovered paper.** `files/fulltext/` is gitignored, so a
fresh clone carries no evidence bytes. Of the papers this repository has read from operator-supplied
PDFs, **the Wiley ones are re-derivable on demand**: `PMID 19500159` (surface intact but
machine-local), `PMID 33914858` — ❌ no, OUP — and `PMID 17803050` — ❌ no, AALAS. So the rule
**restores reachability for `19500159` and for `17823927`, and cannot restore it for `17803050` or
`33914858`.** Stated plainly because the tempting over-generalisation is that the gitignore problem
is now solved. **It is solved only for the Wiley subset.**

---

## § 8 · What I could not verify

1. **The cerebellar-histology sentence attributed to a sibling paper** — *"we did not detect any
   marked pathologic changes in the cerebella"* — **was not found in any retrievable source.** Two
   dedicated queries returned nothing. It may live in `17803050` itself, which is unreachable. **I
   cannot confirm that this sentence exists.** Whatever file quotes it should state its provenance.
2. **The blocked list is not exhaustively enumerated.** The queue is 7 261 lines; §1 rows 26–29 came
   from a grep, not a full read. Additional blocked entries may exist.
3. **`PMID 41538440`, `PMID 21476439`, `PMID 11719429`, `PMID 33300063`, `PMID 36621327`,
   `PMID 15126504`, `PMID 27569545`, `PMID 15026124`, `PMID 24369382`, `PMID 25416187`,
   `PMID 17360458`, `PMID 16941225`, `PMID 41442931`, `PMID 41776383`, `PMID 40235507`,
   `PMID 36247526`, `PMID 33914858` and Gribaa 2007** were each tested with **one** paper-specific
   query. A single semantic miss is weaker evidence of absence than the two-query tests. Their
   publisher predicts absence, so the two lines of evidence agree — but the queries alone are
   one-shot. 🔴 **Four of my first-pass queries were mis-targeted against the paper's real subject**
   (`33134515`, `28123895`, `21444760`, `30094525`), which I caught only by checking PubMed titles
   after the fact. All four were re-tested correctly and all four are still absent — but the near
   miss is the reason the §7 rule says *ask a question only that paper can answer*, and the reason a
   one-shot absence should be treated as weak.
4. **`PMID 35984507` was not re-queried tonight.** Its `NOT IN CORPUS` verdict is a reused prior
   from packet `A9` R4 (two queries, 2026-09-21), cited rather than re-measured.
5. **Figure panels are inspectable by no route here.** Every figure statement above is a **legend**.
6. **The Scholar Gateway extractor's damage profile was not characterised.** Italics markers survive
   as `*…*` and superscripts as `^…^`, which is *better* than the PMC route — but comparators and
   some symbols are dropped (`P < 0.05` → `P  0.05`, `c.606-1G>A` → `c.6061G>A`). **No numeric
   comparator from this surface should be quoted without adjudication.** This repository already
   forbids quoting **variant coordinates** from this surface (`FT-126`); tonight's evidence is that
   the prohibition is correctly placed — `c.606-1G>A` arrived mangled.
7. **Whether Scholar Gateway's coverage is stable.** The response declares *"Last corpus update:
   September 2026"*. A non-Wiley absence measured today is not a permanent property of the tool.
8. **The publisher rule was not tested on a held-out set.** n = 29, all from one blocked list, all in
   one topic area.

---

## § 9 · Novelty grade — **B**

Conservative, and `B` is the honest ceiling. This is **capability work**: no new biology, no new
claim, no model change proposed. What it produces is a measured routing rule and two papers moved
from `HUMAN_REQUIRED` to passage-depth reachable. The publisher hypothesis was **supplied in the
dispatch** and a one-line version of it already existed in the repository, so the contribution is
**measuring it across the whole blocked list and turning it into a rule**, not discovering it.

It is not `A` because nothing was rediscovered against a repository that was wrong in an interesting
way — the repository was right about 25 of 29 papers, and its own 2026-09-21 note already named
Wiley. It is not `C` because two acquisition-packet items were genuinely discharged and the
`§7` ladder removes a class of wasted acts.

---

## § 10 · Source attribution

*Article metadata retrieved from **PubMed**; full-text passages retrieved by **Scholar Gateway**
(Wiley-backed publisher-side corpus, 29 `semanticSearch` queries, 2026-09-22). AI-generated
summaries were not used as evidence — every quotation above is from a retrieved passage body.*

**Recovered and quoted:**

- Suzuki H, Katayama K, Takenaka M, Amakasu K, Saito K, Suzuki K. *A spontaneous mutation of the
  Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy.* Genes Brain Behav
  2009;8(7):650–660. PMID `19500159` · [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x)
- Lo C-P, Hsu L-J, Li M-Y, Hsu S-Y, Chuang J-I, Tsai M-S, Lin S-R, Chang N-S, Chen S-T.
  *MPP+-induced neuronal death in rats involves tyrosine 33 phosphorylation of WW domain-containing
  oxidoreductase WOX1.* Eur J Neurosci 2008;27(7):1634–1646. PMID `18371080` ·
  [DOI](https://doi.org/10.1111/j.1460-9568.2008.06139.x)
- Tabarki B, AlHashem A, AlShahwan S, Alkuraya FS, Gedela S, Zuccoli G. *Severe CNS involvement in
  WWOX mutations: description of five new cases.* Am J Med Genet A 2015;167A(12):3209–3213.
  PMID `26345274` · [DOI](https://doi.org/10.1002/ajmg.a.37363)
- Takenaka M, Yagi M, Amakasu K, Suzuki K, Suzuki H. *Retarded differentiation of Leydig cells and
  increased apoptosis of germ cells in the initial round of spermatogenesis of rats with lethal dwarf
  and epilepsy (lde/lde) phenotypes.* J Androl 2008;29(6):669–678. PMID `18676360` ·
  [DOI](https://doi.org/10.2164/jandrol.108.005066)
- Ludes-Meyers JH *et al.* Genes Chromosomes Cancer 2007;46(12):1129–1136. PMID `17823927` ·
  [DOI](https://doi.org/10.1002/gcc.20497) — presence confirmed, content not re-read here

**Tested and absent (metadata only, PubMed):** `15126504`
[DOI](https://doi.org/10.1074/jbc.M401399200) · `27569545`
[DOI](https://doi.org/10.1016/j.ajhg.2016.06.036) · `15026124`
[DOI](https://doi.org/10.1016/j.neuroscience.2003.12.036) · `33914858`
[DOI](https://doi.org/10.1093/brain/awab174) · `24369382`
[DOI](https://doi.org/10.1093/brain/awt338) · `17803050` (no DOI) · `25416187`
[DOI](https://doi.org/10.1177/1535370214561952) · `33134515`
[DOI](https://doi.org/10.1212/NXG.0000000000000517) · `33300063`
[DOI](https://doi.org/10.3892/mmr.2020.11754) · `31966718` (no DOI; `PMC6965410`) · `36621327`
[DOI](https://doi.org/10.1016/j.intimp.2022.109671) · `30094525`
[DOI](https://doi.org/10.1007/s10072-018-3528-6) · `11719429` (no DOI) · `17360458`
[DOI](https://doi.org/10.1073/pnas.0609783104) · `28123895`
[DOI](https://doi.org/10.1080/2162402X.2016.1253653) · `21444760`
[DOI](https://doi.org/10.1194/jlr.M009175) · `16941225`
[DOI](https://doi.org/10.1007/s10735-006-9046-5) · `35984507`
[DOI](https://doi.org/10.1007/s00018-022-04508-7) · `41776383`
[DOI](https://doi.org/10.1177/13524585261417130) · `40235507`
[DOI](https://doi.org/10.21203/rs.3.rs-6264481/v1) · `36247526`
[DOI](https://doi.org/10.1016/j.ibneur.2022.09.009) · `41442931`
[DOI](https://doi.org/10.1016/j.pediatrneurol.2025.12.001) · `21476439` (no DOI) · `41538440`
[DOI](https://doi.org/10.1126/science.adw1803) · Gribaa 2007
[DOI](https://doi.org/10.1093/brain/awm078)

---

*Not medical advice. This page describes retrieval routes and what they return, and reports
genotype-class-level literature content. `lde/lde` is a rat allele; `c.606-1G>A` is a human allele
distinct from the reference genotype's acceptor variant. Nothing is pooled across species or alleles.*
