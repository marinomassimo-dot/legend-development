# Does public data already report WWOX in the human postnatal SVZ / RMS?

**Actor:** Scientist K · **Date:** 2026-09-22 · **Status:** non-canonical analysis.
**Scope:** public, disease-level. No individual-level record. **BLOCK-1 respected: no molecule, no
dose, no safety claim anywhere in this file.** Nothing here is medical advice.
**Writes:** this file only. `registries/`, the receipt ledger and the state manifest untouched.

---

## 0 · The answer in four sentences

1. 🔴 **No. No accessible source reports WWOX — transcript or protein — in the human postnatal
   subventricular zone, the rostral migratory stream, the medial migratory stream, or any postnatal
   human germinal compartment. Not in any resource, at any age, at any depth.** The intersection is
   still empty after a query census with validated positive controls.
2. 🟢 **But the compartment gap is narrower than "no public data" suggests, and the resource that
   would close it exists and is postnatal human.** Nascimento et al. 2023 (*Nature*, PMID 38122823)
   performed **single-nucleus RNA sequencing on the periventricular migratory stream microdissected
   from a two-week-old human infant**, and captured a radial-glia cluster with a neurogenic
   trajectory in it. Their text never mentions WWOX (0 occurrences in the served full text). **So a
   dataset covering the right species, the right compartment and almost exactly the right age
   exists and has simply never been asked this question.**
3. 🟡 **"WWOX is reported in human postnatal brain" is TRUE and MEASURED — and it is a different
   claim from the one that matters.** Every human postnatal WWOX readout in reach samples
   **parenchymal regions only** (neocortex, hippocampus, amygdala, striatum, mediodorsal thalamus,
   cerebellar cortex). Not one of them dissected a germinal zone. **A resource that never sampled
   the SVZ cannot report WWOX absence there, and none of these may be read as doing so.**
4. 🔴 **One anatomical near-hit, and it is human protein:** WWOX protein is reported by
   immunohistochemistry in **human ependymal cells** (Nunez 2006, PMID 16941225, abstract-depth) and
   in mouse ependyma and choroid-plexus epithelium (Chen 2004, PMID 15026124; restated by Aldaz 2020,
   PMID 33255508, full-text). The ependymal layer **is** the ventricular-wall lining immediately
   apposed to the SVZ astrocyte ribbon. ⚠️ **Ependyma is not the SVZ stem/neuroblast compartment,
   no age is given for the human tissue, and this is adjacency — not the measurement.**

---

## 1 · Network reality — established once, recorded, not retried

Direct egress to the atlas hosts is blocked at CONNECT in this environment. Probed once,
five hosts, one command, no retries:

```
HPA        https://www.proteinatlas.org/ENSG00000186153-WWOX/brain   curl (56) CONNECT tunnel failed, response 403
BrainSpan  https://www.brainspan.org/                                curl (56) CONNECT tunnel failed, response 403
GTEx API   https://gtexportal.org/api/v2/                            curl (56) CONNECT tunnel failed, response 403
EBI EA     https://www.ebi.ac.uk/gxa/genes/ENSG00000186153           curl (56) CONNECT tunnel failed, response 403
NCBI Gene  https://www.ncbi.nlm.nih.gov/gene/51741                   curl (56) CONNECT tunnel failed, response 403
```

⚠️ **Consequence for every verdict below.** I could not open a single atlas UI. Every resource
verdict in §3 is therefore derived from **published descriptions of those resources in open-access
papers**, plus **what is already local in this repository**. Where a resource's sampling is inferred
from a paper's description rather than read off the resource's own sample manifest, it is labelled
`sampling per published description` and is a weaker claim than reading the manifest would be.

**PubMed MCP worked throughout.** All PMIDs, DOIs and quotations below come from PubMed metadata and
PMC full text, per PubMed attribution requirements.

---

## 2 · The query census — every query, every count, every translation, with controls

🔴 **Every zero below was checked against its `query_translation` before being believed**, per the
parser-failure discipline. In all five WWOX-intersection queries the translation **expanded
correctly**: the `wwox protein human` Supplementary Concept fired, and `subventricular zone`
expanded to `"lateral ventricles"[MeSH Terms] OR ("subventricular" AND "zone")`. These are parsed
queries and real zeros, not unexpanded echoes.

| # | Query | Count | Translation expanded? | Verdict |
|---|---|---:|---|---|
| Q1 | `WWOX AND subventricular zone` | **0** | ✅ WWOX SC fired; SVZ → `lateral ventricles[MeSH]` | real zero |
| Q2 | `WWOX AND rostral migratory stream` | **0** | ✅ both terms expanded | real zero |
| Q3 | `WWOX AND ventricular zone` | **0** | ✅ (⚠️ expanded to `heart ventricles[MeSH]` — a *wrong* expansion, so Q3 is uninformative and is not counted as evidence) | discarded |
| Q4 | `WWOX AND germinal zone` | **0** | ✅ `germinal OR germinative` AND `zone` | real zero |
| Q5 | `WWOX AND "postnatal neurogenesis"` | **0** | ✅ phrase indexed as `"postnatal neurogenesis"[All Fields]` | real zero |
| Q6 | `WWOX AND (ganglionic eminence OR doublecortin OR olfactory bulb OR neuroblast OR interneuron migration)` | **0** | ✅ all five expanded, incl. `dcx protein human[SC]` | real zero |

**Positive controls — the zeros are informative, not artefacts of a dead query shape:**

| Control | Count | What it proves |
|---|---:|---|
| `DCX AND subventricular zone AND human infant` | **9** | the compartment-plus-age query shape returns records |
| `postnatal neurogenesis AND subventricular zone` | **580** | the compartment literature is large; Q1/Q4/Q5 zeros sit against a 580-record background |
| `WWOX AND neurogenesis` | **5** | the WWOX side of the intersection is alive |
| `WWOX AND (neural stem cell OR radial glia OR neural progenitor)` | **6** | WWOX∩progenitor is non-empty — but every hit is organoid, rodent or in-vitro (§4) |
| `WWOX AND human brain development AND expression` | **16** | WWOX∩human-brain-development is non-empty |
| `WWOX AND BrainSpan` | **1** | only one indexed paper joins WWOX to a developmental atlas by name (§3.1) |
| `WWOX AND infant brain` | **17** | WWOX∩infant is non-empty — all clinical/WOREE, none expression-in-germinal-zone |

🔴 **The standing caveat that limits all of the above:** `[All Fields]` **does not index Methods or
supplementary tables.** A resource could have sampled the SVZ, or a supplementary table could list
WWOX across germinal zones, and **no query count above would see it.** This is why §3 reads each
resource's *sampling* from its own published description instead of from a hit count — and why the
zeros are reported as "nobody has framed a paper around it", not as "the datum does not exist
anywhere".

---

## 3 · Per-resource verdict — and the sampling question, which is the one that matters

The central trap of this task is to read a silent resource as a negative. Each row therefore answers
two separate questions: **does it report WWOX**, and **did it ever sample a postnatal germinal
zone**. A `no` in the second column makes the first column uninterpretable as absence.

| Resource | Reports WWOX? | Sampled postnatal germinal zone (SVZ/RMS/MMS)? | May be read as evidence of WWOX absence in SVZ? |
|---|---|---|---|
| **Human Brain Transcriptome (HBT)** — the human developmental array resource | 🟢 **YES, measured, human, mRNA, conception→adult** | 🔴 **NO.** Regions named in the published description: NCX, HIP, AMY, STR, MD, CBC — six parenchymal regions, zero germinal zones | 🔴 **NO** |
| **BrainSpan / Allen developmental human resources** | 🟡 one indexed paper joins WWOX to BrainSpan by name (PMID 42101182) — **and its window is 8–37 post-conception weeks, i.e. prenatal only**, across 11 regions | 🔴 **NO postnatal germinal zone.** `sampling per published description`: the paper states "8 to 37 pcw" and "11 brain regions" | 🔴 **NO** |
| **GTEx** | 🟢 **YES, measured** — and the values are **already local** (§5) | 🔴 **NO — and adult only.** 13 brain regions, all parenchymal; no germinal zone, no pediatric donor | 🔴 **NO** |
| **Human Protein Atlas (brain / single-cell)** | ⚠️ **could not verify — host 403.** HPA is not cited by any WWOX paper I read | 🔴 **NO.** `sampling per published description` (Sjöstedt 2020, PMID 32139519): "10 major brain regions and multiple subregions" in **human, pig and mouse** — a regional adult dissection, no germinal zone, no infant human | 🔴 **NO** |
| **Allen Mouse Brain Atlas (ISH)** | 🟢 **YES, measured** — focal signal in medial entorhinal cortex L2, basolateral amygdala, isocortex L5, cerebellum | 🔴 **NO — and mouse, adult.** Also 🔴 the mouse cannot substitute for this compartment at all: Sanai 2011's own control found no MMS in mouse at P4/P8/P16/P20 (held in `postdiagnosis_window_evidence_20260922.md`) | 🔴 **NO** |
| **Mouse brain cell-type RNA-seq (BrainRNAseq), P7** | 🟢 **YES, measured, postnatal** — uniform across neurons and all glia; **highest in progenitor oligodendrocytes, lower in mature myelinating oligodendrocytes** | 🟡 **NO SVZ** — but it is a **postnatal progenitor-vs-mature contrast**, the nearest existing analogue | 🔴 **NO** |
| **DropViz (mouse adult scRNA-seq)** | 🟢 **YES** — cerebellar basket/granule cells, frontal L5, medial EC; ⚠️ **"ependymal cells and choroid plexus cells (data not shown)"** | 🔴 **NO — mouse, adult; ependyma is a ventricular *lining*, not the SVZ niche.** And the ependymal result is explicitly **data not shown** | 🔴 **NO** |
| **Nascimento 2023 snRNA-seq (PMID 38122823)** — EC stream + germinal zones + postnatal EC | 🔴 **NO — 0 occurrences of "WWOX" in the served full text** | 🟢 **YES, PARTLY, AND THIS IS THE PRIZE.** The EC-stream sample is **postnatal human, microdissected from a two-week-old**, and its snRNA-seq **captured a radial-glia cluster** with a neurogenic trajectory. ⚠️ The dedicated *germinal-zone* samples are gestational ("germinal zones in gestation", Methods) | 🔴 **NO — the gene was never queried** |
| **Paredes 2016 (PMID 27846470)** — the "Arc", postnatal human SVZ, birth→15 y | 🔴 **NO — 0 occurrences** | 🟢 **YES, EXTENSIVELY** — birth, 1, 1.5, 3, 5, 7 months, 2 y, 6 y, 15 y; tiers 1–4 around the lateral ventricle | 🔴 **NO — the method was a fixed marker panel, not transcriptomics** |
| **Human WWOX protein IHC across normal tissues (PMID 16941225)** | 🟢 **YES — human, protein: "neurons, ependymal cells and astrocytes"** ⚠️ **abstract-depth only** | 🔴 **NO.** Tissue-microarray cores across >30 organs; no germinal-zone dissection asserted, **and no donor age given anywhere in the abstract** | 🔴 **NO** |

### 3.1 · The one WWOX↔BrainSpan hit, and why it is not the answer

`WWOX AND BrainSpan` returns exactly one record: **PMID 42101182** ([DOI](https://doi.org/10.1080/01677063.2026.2649162)),
a curation of sulfate-pathway gene expression in the human fetal brain from BrainSpan.
⚠️ **I could not determine why WWOX matched.** The served abstract has every italic gene token
silently deleted — the characteristic extraction defect — leaving bare comma runs like
`sulfotransferases (,)`, so **WWOX is plausibly one of the deleted symbols and I cannot confirm it
without the rendered text.** `convert_article_ids` returns **no PMCID**, so no full text was
obtainable. It is recorded as unresolved, not as evidence. Even at its best it would be
**8–37 post-conception weeks — prenatal, and the wrong side of birth for this question.**

---

## 4 · What IS measured about WWOX and progenitors — stated at its real depth

| Finding | Species / compartment / age | Depth | What it does **not** license |
|---|---|---|---|
| WWOX mRNA present across human brain **conception → adulthood**; higher in early embryonal life, **decreasing during fetal development until birth, then increasing again in postnatal life and early childhood up to adolescence**; cerebellar cortex shows a **distinct, larger early-postnatal rise** | human, 6 parenchymal regions, prenatal→adult | 🟢 **full-text**, Aldaz 2020 §2, describing the HBT figure — **a secondary description of a public database, not a measurement by these authors** | Nothing about any germinal zone. And mRNA ≠ protein for this gene — the repository already holds the corpus's own statement that the two dissociate |
| GTEx adult: cerebellum highest (median **12.1 TPM**), frontal cortex **6.9**, amygdala **6.2**, hippocampus **5.6** | human, adult, bulk parenchyma | 🟢 **full-text** + 🟢 **local CSV cross-check passes** (§5) | Anything postnatal-pediatric; anything periventricular |
| Wwox **highest in progenitor oligodendrocytes, lower in mature myelinating oligodendrocytes** | **mouse, P7 — postnatal** | 🟢 full-text (already held in the repository's own dossier for this paper) | It is the oligodendrocyte lineage, not the neurogenic SVZ lineage |
| Wwox protein in mouse **ependymal cells and choroid-plexus epithelium** in the **adult** brain; expression "decreased after birth" in brainstem and spinal cord | mouse | 🟡 Chen 2004 **abstract-depth** (repository records the Results as unread); restated full-text by Aldaz 2020 | 🔴 **Directly contradicts the human HBT postnatal rise in direction** — see §6 |
| WWOX protein in **human** "neurons, **ependymal cells** and astrocytes" | human, age unstated | 🟡 **abstract-depth** (PMC body served **empty** for PMC4144810 — a PMCID that returns nothing, exactly the failure mode the discipline warns of) | No age, no compartment, no periventricular dissection |
| WWOX loss preferentially affects **radial glial cells**, with G2/M–S accumulation, MYC overexpression and reduced neuronal generation | **human iPSC-derived neural organoids** — in vitro, prenatal-equivalent | 🟡 abstract-depth here (PMID 42397075; the repository holds the organoid line of work) | An organoid radial glial cell is not a postnatal SVZ B1 cell, and carries no gestational or postnatal date |

---

## 5 · Local-first check — what the repository already has

Per the check-the-repository-first discipline (needed eight times today):

- 🟢 **`analysis/data/WWOX_tissue_expression_GTEx.csv` exists and is a clean positive control.**
  It holds 54 GTEx tissues with TPM. Its brain values **match the published GTEx figures exactly**:
  `Brain_Cerebellar_Hemisphere 12.1278` vs published median 12.1; `Brain_Frontal_Cortex_BA9 6.8204`
  vs 6.9; `Brain_Amygdala 6.16809` vs 6.2; `Brain_Hippocampus 5.58518` vs 5.6. **Two independent
  routes to the same numbers — the local extract is trustworthy.**
  🔴 **And it contains no germinal-zone row, because GTEx has none.** Its 13 brain rows are all
  parenchymal and all adult. The nearest periventricular neighbour is
  `Brain_Caudate_basal_ganglia 6.81567` — the caudate abuts the lateral-ventricle wall, but a bulk
  caudate dissection is **not** an SVZ dissection and must not be read as one.
- `analysis/data/` holds **no** BrainSpan, HBT, HPA or single-cell matrix. Repo-wide literal counts:
  `BrainSpan 0`, `Allen Brain 0`, `Human Protein Atlas 0`, `proteinatlas 0`, `HDBR 0`,
  `germinal zone 0`. **No developmental-atlas data is local.**
- The repository has **already fully read** Aldaz 2020 (PMID 33255508 — dossier records all nine
  figures inspected) and already holds the OPC-progenitor gradient, the Chen 2004 ependymal quote,
  and an HBT readout **via a different secondary** (PMID 34359949).

---

## 6 · Delta against the repository — including two contradictions

**Already held; I re-derived and did not double-count:** the empty WWOX×postnatal-SVZ cell itself
(`postdiagnosis_window_evidence_20260922.md` §7 and its `FT-132` debt), Sanai 2011's window,
the OPC gradient, the Chen 2004 ependymal sentence, the organoid radial-glia phenotype.

**New to this repository:**

1. 🟢 **PMID 38122823 (Nascimento 2023, *Nature* 626:1056–1065) is absent from the repository
   (0 hits) and is the single highest-value paper found today for this question.** A human
   **two-week-old** periventricular migratory compartment was microdissected and sequenced at
   single-nucleus resolution, and the dataset contains a radial-glia cluster. **Two weeks is inside
   the WOREE presentation window (median 5 weeks).**
2. 🟢 **PMID 27846470 (Paredes 2016, *Science*) is absent (0 hits).** It establishes that postnatal
   human SVZ tissue at birth, 1, 1.5, 3, 5, 7 months, 2 y, 6 y and 15 y **has been collected,
   sectioned and banked**, and that the migratory population peaks at **~1.5 months** and is mostly
   gone by 7 months. This converts "needs banked human tissue" from a wish into a named,
   demonstrably existing specimen series.
3. 🟢 **An entorhinal convergence nobody in this repository has stated.** The compartment with
   **WWOX's highest focal brain expression** — medial entorhinal cortex layer 2, concordant across
   Allen ISH and DropViz — is fed by a **postnatal human migratory stream that is open at the WOREE
   diagnostic age**: the EC stream, tangential migration persisting to ~1 year, radial dispersal to
   ~2–3 years, delivering LAMP5/RELN inhibitory interneurons (PMID 38122823; reviewed PMID 39308952).
   ⚠️ **Labelled `predicted`/`inferential`, and it is a co-location of two separate literatures, not
   a measurement.** WWOX has never been measured in the EC stream either.
4. 🟡 **PMID 32139519 (Sjöstedt 2020) is absent (0 hits)** and is the citable statement of what HPA's
   brain resource actually sampled — needed to keep HPA silence from being misread as HPA negative.
5. 🔴 **CONTRADICTION — the human HBT developmental shape.** The repository's
   `wwox_developmental_timing_audit_20260920.md` records the HBT readout as **FLAT** — *"no reduction
   … from prenatal to the teenage period"* (PMID 34359949 §8.1). Aldaz 2020, describing the **same
   HBT dataset** in full text, reports a **U-shape**: higher in early embryonal life, *"slowly
   decreasing during fetal development until birth to slightly increase again … in postnatal life
   and early childhood up to adolescence"*. **Two secondary descriptions of one public database
   disagree about its shape, and the repository currently holds only the flat one.** This matters
   directionally: a postnatal rise argues the target is on-line at the diagnostic age; a trough at
   birth argues the newborn window is the weakest point. 🟢 **The repository can arbitrate this at
   desk cost** — its own dossier states all nine Aldaz figures were inspected, so the HBT figure is
   already in hand. ⚠️ Neither description is a measurement by its author, and mRNA ≠ protein here.
6. 🟡 **CONTRADICTION — species direction across birth.** Mouse: *"its expression decreased after
   birth"* (brainstem, spinal cord). Human HBT per Aldaz: increases after birth. Rat (already held):
   increases PND5→21 in cortex. The mouse-down result is **abstract-depth** and regionally
   restricted to caudal CNS, so this may be regional rather than species-level — but a
   mouse-derived assumption that WWOX falls after birth should not be carried into a human
   postnatal-window argument.

---

## 7 · Ranked shortlist to close the gap — cheapest first

**Desk analysis — no tissue, no consent, no spend:**

| # | Action | Cost | What it would settle | Risk |
|---|---|---|---|---|
| **D1** | 🟢 **Read WWOX out of the Nascimento 2023 snRNA-seq object** (EC stream, 2-week-old human; plus its gestational germinal-zone and postnatal-EC samples). Per cluster: radial glia, immature CGE/MGE inhibitory neurons, astrocytes, postnatal EC neurons | **desk, hours** — once egress exists | 🟢 **The first WWOX measurement in a human postnatal periventricular migratory compartment.** Would also give WWOX in a human postnatal radial-glia cluster | ⚠️ **n = 1 postnatal donor.** 🔴 Needs a dropout control: WWOX at ~6 TPM bulk is not guaranteed detectable per-nucleus, so **a zero would be uninterpretable without a matched-abundance control gene** |
| **D2** | 🟢 **Arbitrate the FLAT-vs-U-shape contradiction (§6.5) from the Aldaz HBT figure the repository already inspected** | **desk, ~1 hour, zero external access** | Which postnatal direction the human mRNA record actually supports | It settles a *description*, not a measurement; mRNA≠protein caveat stands |
| **D3** | Query HPA's brain and single-cell sections for WWOX and **record its sample manifest**, so HPA silence is never misread as HPA negative | desk, minutes once reachable | Whether any HPA subregion is periventricular | 🔴 Blocked today (403) |
| **D4** | Check the **Allen prenatal laser-microdissection** germinal-zone series (VZ/SVZ-class dissections, mid-gestation) for WWOX | desk | A **prenatal** germinal-zone WWOX value — the floor under the postnatal question | 🔴 Prenatal. Does **not** answer the postnatal question; its value is as a positive control that WWOX is detectable in a germinal-zone dissection at all |
| **D5** | Re-run the Nascimento/Paredes-adjacent literature for any **supplementary table** listing WWOX, since `[All Fields]` cannot see supplements | desk | Possibly a free answer hiding in a supplement | Low yield; high cheapness |

**Tissue work — only if every desk route above is exhausted:**

| # | Action | Cost | Note |
|---|---|---|---|
| **T1** | WWOX **immunohistochemistry** on the **already-banked** postnatal human SVZ/Arc series (birth → 7 months), co-stained with DCX/PSA-NCAM to put WWOX on or off the migrating cells themselves | tissue request, **not** new collection | 🟢 **Cheapest tissue route by a wide margin**, because Paredes 2016 documents that the specimens, the sectioning and the marker panel already exist. The question is one added antibody on existing slides |
| **T2** | Spatial transcriptomics across the postnatal periventricular streams | expensive | Named as the field's own next step in the 2024 review; WWOX would come free with the panel |
| **T3** | New prospective collection | most expensive | 🔴 **Should not be proposed while T1 is unattempted** |

🔴 **The headline for the Orchestrator: the gap was named as needing banked human tissue. It does
not — at least not first. D1 and D2 are desk analyses, and D2 needs nothing but a file this
repository has already opened.**

---

## 8 · What I could not verify — stated as such

- 🔴 **No GEO/dbGaP accession for the Nascimento snRNA-seq data.** The data-availability statement is
  **not present in the PMC body as served** — it is deferred to the publisher DOI, which is behind
  the 403. **I therefore name no accession. Per discipline I do not reconstruct one from memory, and
  any accession that appears later must be seen in running text before use.**
- 🔴 **PMID 16941225 (human WWOX IHC) is abstract-depth only.** `get_full_text_article` on
  **PMC4144810 returned an empty body** despite a valid PMCID. So the human ependymal-cell protein
  result is **abstract-depth**, with no donor age, no region list and no image inspected.
- 🔴 **PMID 42101182** — why it matched `WWOX` is unresolved; gene tokens are deleted from the served
  abstract and there is no PMCID. Recorded as unresolved, not as evidence.
- 🔴 **No atlas UI was opened.** HPA, BrainSpan, GTEx, Ensembl and NCBI are all 403 at CONNECT.
  Every atlas *sampling* verdict in §3 rests on a published description, not on the resource's own
  manifest.
- 🟡 **The HBT region list and postnatal direction are Aldaz's prose about a figure**, not values I
  read off the figure. D2 exists precisely to remove that layer of indirection.
- 🟡 Nascimento 2023 and Paredes 2016 were read in **served full text**; their figures were not
  inspected and their supplementary tables were not retrieved. A WWOX row in a supplement would not
  have been seen.

---

## 9 · Sources

According to PubMed:

| PMID | Source | DOI | Depth reached here | In repo before today |
|---|---|---|---|---|
| 38122823 | Nascimento MA, … Sorrells SF. Protracted neuronal recruitment in the temporal lobes of young children. *Nature* 2023;626:1056–65 | [DOI](https://doi.org/10.1038/s41586-023-06981-x) | 🟢 **full text** (PMC10901738) | 🔴 **no** |
| 27846470 | Paredes MF, … Alvarez-Buylla A. Extensive migration of young neurons into the infant human frontal lobe. *Science* 2016;354:6308 | [DOI](https://doi.org/10.1126/science.aaf7073) | 🟢 **full text** (PMC5436574) | 🔴 **no** |
| 39308952 | Sorrells SF. Which neurodevelopmental processes continue in humans after birth? *Front Neurosci* 2024;18:1434508 | [DOI](https://doi.org/10.3389/fnins.2024.1434508) | 🟢 full text, **review (secondary)** | 🔴 no |
| 33255508 | Aldaz CM, Hussain T. WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders. *IJMS* 2020;21:8922 | [DOI](https://doi.org/10.3390/ijms21238922) | 🟢 **full text** (PMC7727818), **review (secondary)** | ✅ yes, read |
| 16941225 | Nunez MI, Ludes-Meyers J, Aldaz CM. WWOX protein expression in normal human tissues. *J Mol Histol* 2006;37:115–25 | [DOI](https://doi.org/10.1007/s10735-006-9046-5) | 🟡 **abstract-depth** — PMC body empty | ✅ yes |
| 15026124 | Chen ST, … Chang NS. Expression of WOX1 in the developing murine nervous system. *Neuroscience* 2004;124:831–9 | [DOI](https://doi.org/10.1016/j.neuroscience.2003.12.036) | 🟡 abstract-depth | ✅ yes |
| 32139519 | Sjöstedt E, … Mulder J. An atlas of the protein-coding genes in the human, pig, and mouse brain. *Science* 2020;367:6482 | [DOI](https://doi.org/10.1126/science.aay5947) | 🟡 abstract-depth | 🔴 no |
| 42397075 | Steinberg DJ, … Aqeilan RI. Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [DOI](https://doi.org/10.1093/brain/awag239) | 🟡 abstract-depth | ✅ yes |
| 42101182 | Vijayakumar P, Summers KM, Dawson PA. Expression of sulfate pathway genes in human neurodevelopment. *J Neurogenet* 2026;40:60–79 | [DOI](https://doi.org/10.1080/01677063.2026.2649162) | 🟡 abstract-depth, **match unresolved** | 🟡 1 hit |
| 31340538 | Tochigi Y, … Suzuki H. Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination. *IJMS* 2019;20:3596 | [DOI](https://doi.org/10.3390/ijms20143596) | metadata only | ✅ yes, read |
| 42128308 | Obeid M, … Aqeilan RI. WWOX in brain development and disease. *Neurobiol Dis* 2026;225:107446 | [DOI](https://doi.org/10.1016/j.nbd.2026.107446) | metadata only | ✅ yes |

**Reading-debt note.** The two papers this analysis leans on hardest — PMID 38122823 and
PMID 27846470 — were read in **served full text** but **without figures or supplements**, and neither
had a prior repository entry. They are declared as a full-text reading debt in `FT-133`. 🔴 **No PMID
in this file has been stripped to avoid declaring debt.**
