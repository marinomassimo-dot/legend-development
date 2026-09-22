# Has WWOX ever been measured in a Purkinje cell? — a cell-type census of the cerebellum, and the SCAR12 pole

**Actor:** Scientist F · **Date:** 2026-09-22 · **Axis:** cell-type resolution, not magnitude and not layer localisation
**Question class:** `EXISTENCE OF A MEASUREMENT` — for each candidate: species · age · method · **marker** · what was measured · locator

**Not medical advice.** Nothing here is a treatment, dose, route or diagnostic recommendation.

> **Scope discipline.** The dose non-monotonicity premise is **CLOSED** (`CC-20260826-DOSE-ADJUDICATION-01` § 6) and
> is not reopened anywhere in this file, including from expression data. The layer-localisation verdict of
> [`cerebellum_layer_localisation_20260922.md`](cerebellum_layer_localisation_20260922.md) — divergence present at
> **layer 2, VECTOR GENOME**, **per-nucleus**, not attributable to transcription, with a shared transcript→protein
> ceiling — is **carried, not re-derived**. Its `MAB377 = clone A60` reagent finding is the premise this file starts from.
> Survivor selection applies to every P240/P300 observation. `NOT ASSAYED` is never `NORMAL` and never `ABSENT`.

---

## 0 · The answer, before the evidence

| The brief asks | Answer |
|---|---|
| **Has WWOX ever been measured in Purkinje cells, in any species, by anyone?** | 🟡 **Once, and only as a LAYER.** One human immunohistochemistry observation reports WWOX protein in the somata of **all three layers of human cerebellar cortex, the Purkinje cell layer named explicitly**. 🔴 **No Purkinje MARKER was ever used** — not calbindin, not PCP2/L7, not Car8, not parvalbumin — so it identifies a *layer*, not a *cell*. And it survives only as a sentence in a **review**; the primary body is not retrievable. |
| **Resolved by cerebellar cell type?** | 🟡 **Yes, in one mouse single-cell atlas, and Purkinje cells are not in it.** DropViz puts the top cerebellar clusters at **GABAergic basket cells** and, less so, **granule cells**. A Purkinje cluster is **not reported in either direction.** |
| **Does the SCAR12 pole supply cerebellar cell-type evidence the WOREE literature lacks?** | 🔴 **No. It supplies less.** One second-hand line of *mild cerebellar atrophy on MRI in two children*, whose primary abstract names a **different finding in a different number of patients**; no neuropathology, no post-mortem, no cell-type observation of any kind, and its founding genetics paper is **paywalled**. |
| **Any cerebellar WWOX measurement free of the clone-A60 confound?** | 🟢 **Exactly one that could see a Purkinje cell** — the human layer-resolved IHC above. Every other A60-free cerebellar measurement is free of the confound only because it has **no cell-identity channel at all**. |
| **The nearest existing thing?** | A **human cerebellar single-nucleus multiome of 103,861 nuclei that already separates Purkinje from granule clusters and has never been queried for WWOX.** One database query away. |

🔴 **And the finding that is new to this repository:** the Purkinje-layer sentence exists in a paper this repository
recorded as a **`complete_fulltext_read` on 2026-08-06 with four verbatim locators**, and it was not captured. The
string `Purkinje cell layer` occurs **zero times anywhere at `HEAD`** (verified § 1.5). Three independent downstream
sources — including that paper's **own abstract** — transmit its cerebellar cell-type statement as *"basket cells and
granule cells"* and drop the Purkinje layer. **That is the mechanism by which "WWOX in the cerebellum" became a
statement with no Purkinje cell in it.**

---

## 1 · Positive-control census — every extraction surface, validated before any negative claim

Five surfaces. Each is shown working on a named positive control **before** any zero from it is carried, and the zeros
that are carried are separated from the zeros that are **discarded**.

### 1.1 Surface A — the PubMed `[All Fields]` search index

**Positive controls that fire.** Every `query_translation` below was checked **term-by-term** against the OR block I sent.

| Query | Hits | Translation verdict | Positive control inside it |
|---|---|---|---|
| `WWOX AND cerebellar` | **10** | ✅ correct; `cerebellum`[MeSH] + `cerebellar`[All Fields] | ✅ returns **`24369382`** (Mallaret, the SCAR12 founder) and **`32581702`** (rat `lde/lde`) |
| `WWOX AND cerebellum` | **5** | ✅ correct | ✅ returns `33255508`, `32000863`, `26345274` |
| `WWOX AND Purkinje` | **2** | ✅ correct; `purkinje` + `purkinje s` | ✅ both hits are known-positive Purkinje papers (`36828035`, `32000863`) |
| `WWOX AND (calbindin OR parvalbumin OR Pcp2 OR Car8 OR "carbonic anhydrase 8" OR L7)` | **1** | ✅ **all six terms present** | ✅ returns `30290271`, the parvalbumin interneuron paper — the surface indexes marker names |
| `WWOX AND (granule OR Bergmann OR "deep cerebellar nuclei" OR "molecular layer" OR "dentate nucleus")` | **2** | ⚠️ all five present, but `granule` over-expands into the `cytoplasmic granules` MeSH block | ✅ `33255508` |
| `WWOX AND ("single-cell RNA" OR … OR "cell type")` | **7** | ✅ all six present | ✅ `42397075`, `33255508` |
| `WWOX AND (autopsy OR "post-mortem" OR postmortem OR neuropathology OR "brain biopsy" OR fetus OR fetal)` | **17** | ✅ all seven present | ✅ `36828035`, `32581702`, `25716914` |
| `WWOX AND (nystagmus OR dysarthria OR "cerebellar ataxia") AND missense` | **1** | ✅ all three present | ✅ `24369382` — the SCAR12 clinical vocabulary maps to exactly one indexed WWOX paper |

**🔴 Three zeros produced today, and they are NOT equivalent. Two are discarded; one is carried with a named boundary.**

**(i) DISCARDED — failure mode (a), the query was echoed unexpanded.**
`WWOX AND (Gly372Arg OR G372R)` → **0 hits**, and `query_translation` came back as the **literal input string**,
`"WWOX AND (Gly372Arg OR G372R)"` — no `[All Fields]`, no `[Supplementary Concept]`, no expansion of any term.
⇒ **The engine did not run a translated query. This zero carries no information about `G372R` and is discarded.**

**(ii) DISCARDED — failure mode (f), a quoted term silently DROPPED from an OR block, caught live.**
I sent six terms: `"Pro47Thr" OR "P47T" OR "Gly372Arg" OR "G372R" OR "c.1114G>C" OR "c.140C>A"`.
The returned translation was:
> `"WWOX"[All Fields] AND ("Pro47Thr"[All Fields] OR "P47T"[All Fields] OR ("c 1114g"[All Fields] AND "c"[All Fields]) OR "c 140c"[All Fields])`

⇒ **`Gly372Arg` and `G372R` are absent from the translation entirely**, and both cDNA terms were mangled by
punctuation into different search objects. The 2 hits returned are informative about `P47T` **only**.
🔴 **A six-term OR block came back as a four-term OR block and the tool reported no error.** This is the exact trap
the brief names, reproduced on the first attempt, and it is the reason every translation in § 1.1 was read term-by-term.

**(iii) CARRIED, with its boundary named — failure mode (e), Methods invisibility.**
`Wwox AND (Pcp2 OR "L7-Cre" OR "Purkinje-specific" OR Nestin-Cre OR "Syn-Cre" OR "Synapsin-Cre" OR "brain-specific")`
→ **0 hits**, with a translation in which **all six terms are present and correctly formed**, and a working left arm.
🔴 **This zero is nevertheless NOT a scientific zero**, and the repository itself proves it: `CLAIM 037`'s evidence
boundary records that no continuous EEG exists *"for the Aldaz/EIIA null, `Wwox^+/−`, **`Nes-Cre`, `Syn-Cre`**"* — i.e.
**Cre-driver `Wwox` mice exist in this literature and none of them is findable by this query.** Cre drivers, floxed
alleles and antibody clones are named in Methods, and `[All Fields]` does not index Methods.
⇒ Recorded as **`PREMISE: METHODS_INVISIBLE`**, not as an absence. The conditional-allele question in § 2.4 is
therefore answered from a **read body**, not from this zero.

### 1.2 Surface B — a full-text semantic corpus (Scholar Gateway), **scripted**, both arms controlled

This surface indexes bodies including Methods, so it is the instrument that can see what Surface A structurally cannot.
Query: *"Is the WWOX protein expressed in cerebellar Purkinje cells? Has WWOX immunostaining been co-localised with
calbindin or another Purkinje cell marker?"* — 20 passages, 116,257 bytes, **counted by script, not by eye**:

| Positive controls (must be non-zero) | count | | Validated negatives | count |
|---|---|---|---|---|
| `Purkinje` | **146** | | `NeuN` | **0** |
| `cerebell` | **192** | | `MAB377` | **0** |
| `WWOX` | **87** | | `A60` | **0** |
| `WOX1` | **61** | | | |
| `calbindin` | **57** | | | |
| `granule` 26 · `Bergmann` 5 · `basket cell` 3 · `SCAR12` 1 | — | | | |

⇒ **Both arms of the intersection fire, and they fire hard.** The corpus is rich in WWOX and rich in
Purkinje/calbindin. Then, per result, programmatically:

🔴 **20 of 20 passages are single-sided. Eight contain WWOX or WOX1 and no `Purkinje`. Twelve contain `Purkinje`
and no WWOX. ZERO passages contain both.**

That is a **controlled negative**: not a parser zero, not a case-sensitivity artefact, not a silent omission — a
full-text corpus with 146 `Purkinje` tokens and 87 `WWOX` tokens returns **no document in which the two meet**.

### 1.3 Surface C — PMC full text via the MCP route

| Target | Result | Verdict |
|---|---|---|
| `PMC7727818` (Aldaz & Hussain 2020) | ✅ **complete body served**, §§ 1–4 read sequentially end to end | ✅ **POSITIVE CONTROL — the surface works.** This is where the Purkinje-layer sentence is |
| `PMC10757851` (Battaglia 2023) | ✅ **complete body served**, including **Table 1** in linearised form | ✅ POSITIVE CONTROL |
| `PMC4144810` (**Nunez 2006** — the primary IHC paper) | 🔴 **`full_text: ""`** — valid PMCID, zero-length body | 🔴 **`SOURCE_BLOCKED`, not absent.** `get_copyright_status` → `is_open_access: false`, `© Springer Science+Business Media B.V. 2006`, `checked_sources: ["pubmed","pmc"]` ⇒ **a LICENCE, not a route failure.** Independently reproduced by me today; **third** confirmation in this repository (also `wwox_myelin_oligodendrocyte_census_20260921.md` L119 and `wwox_postnatal_svz_expression_20260922.md` L245) |
| `17470496` (**Gribaa 2007** — the SCAR12 clinical founder) | 🔴 **no PMCID at all**; `source: "not_available"`, `checked_sources: ["pubmed"]` | 🔴 `SOURCE_BLOCKED`. **A PMCID is not a body — and here there is not even a PMCID.** |
| `24369382` (**Mallaret 2014** — the SCAR12 genetics founder) | 🔴 `is_open_access: false`; `PMC3914474` deposit exists, body not licensed | 🔴 `SOURCE_BLOCKED`, repo-attested (`wave7_verification_mallaret_chain_20260922.md` § 2b) and unchanged |

### 1.4 Surface D — the network, with `example.com` as the control

```
example.com                          → HTTP 000
ebi.ac.uk/europepmc/webservices/rest → empty
eutils.ncbi.nlm.nih.gov              → empty
```
⇒ **The control itself fails, so general egress is closed and the MCP tools are the only route.** Therefore
`proteinatlas.org`, `dropviz.org`, `mousebrain.org` and the Allen Brain Atlas API are **`SOURCE_BLOCKED` by the
allowlist, not by the publishers**. `SOURCE_BLOCKED → set a REVIVAL_TRIGGER → CONTINUE`. **No retries, no external
human action, no correspondence** (§ 8).
Also confirmed: `files/` and `files/fulltext/` **do not exist in this worktree**, so no local body, figure or
supplement was available to me for any paper.

### 1.5 Surface E — this repository, read with `git grep … HEAD` and never over my own output

| Probe | Result |
|---|---|
| `git grep -c -i "purkinje cell layer" HEAD` | 🔴 **ZERO hits, whole tree** |
| `git grep -n -i "all three layers" HEAD` | 🔴 **ZERO hits, whole tree** |
| `git grep -c -i "Purkinje" HEAD -- 'disease-models/**'` | ✅ 31 files — the token is richly present, so the two zeros above are **specific absences, not a grep failure** |
| `git grep -n "DropViz\|Allen Mouse Brain\|basket cell" HEAD` | ✅ present in `wwox_postnatal_svz_expression_20260922.md` LL111–113, `paper_registry_current.md` L7192, `CC-20260826-CLAIM006-*` |

⇒ **The atlas material IS held. The Purkinje-layer sentence is NOT.** Positive control passes on the same probe.

### 1.6 Prior-art sequence, executed before anything below is declared new

`FIND ISSUE` → `SEARCH EXISTING CLAIMS` → `SEARCH EXISTING CANDIDATES` → `SEARCH DISCOVERY LEDGER`.

| Already held — **not** rediscovered here | Where |
|---|---|
| `MAB377` = clone A60 ⇒ the ≈61% cerebellar `NeuN⁺WWOX⁺` excludes Purkinje cells from its own denominator | `cerebellum_layer_localisation_20260922.md` § 6.2 |
| Divergence at layer 2 **VECTOR GENOME**, **per-nucleus**, ~9–12× below cortex; density already divided out | same, §§ 3.2a, 4.3, 7 |
| `HD/LD` within-region: vDNA `2.28×`, mRNA `2.57×`, protein `0.74×` (cbl) / `0.98×` (hip) ⇒ ceiling at transcript→protein, **shared** | same, § 4.2 |
| GTEx cerebellum **1.6–2.2× above** cortex/hippocampus ⇒ uniform-baseline fold-WT overstates by ~2× ⚠️ human RNA vs mouse protein | same, §§ 5.2, 11.1 |
| Cerebellum treated as one granule-dominated homogenate; `Purkinje` 0 / `granule` 0 / `calbindin` 0 in the 2026 body | same, § 6.1 |
| The only dose-resolved "ataxia score" is **hindlimb clasping**; rotarod supra-WT; ECoG electrode **cortical**; `gait`/`beam`/`catwalk` = 0 | same, § 3.6 |
| `PMID 36828035` Fig 5d **calbindin⁺ Purkinje** counts + Fig 5e **Hcn1⁺ basket cells `ns`**, `n = 3`, medians, survivor selection | `deepdive_manifests/PMID36828035.json`; `CC-20260826-CLAIM006-HARDENING-01` §§ 45–46, 129–132 |
| `PMID 32000863` foliation defects lobules V/VI/VII, Purkinje ≈18 vs ≈7 per area | `deepdive_manifests/PMID32000863.json` L176–181 |
| `CLAIM 039` narrowed: ataxic gait 95% vs 0% in rat `lde/lde`, **no marked cerebellar histopathology at ~28 d**, `PREMISE: LIGHT_MICROSCOPY_FLOOR`; cerebellar contribution neither established nor excluded | `claim_registry_current.md` CLAIM 039; `CC-20260920-CLAIM039-CEREBELLAR-01` |
| `PMID 33255508` = `PAPER 095`, read 2026-08-06, landed on the **myelin/oligodendrocyte** axis, **4 locators**, DropViz + Allen captured | `fulltext_dossiers/PMID33255508.md`; `deepdive_manifests/PMID33255508.json` |
| WOREE vermis hypoplasia + "small inferior vermis" at day 7, pons/dentate signal at 2 y 4 m | `discovery_ledger_current.md` L554; `FTR-20260921-35573960-01` |
| `PREMISE: DETECTION_FLOOR` — *not detected* ≠ *absent* | `CC-20260920-DETECTION-FLOOR-01` |

**What is new in this file, and only this:** § 2.1 (the Purkinje-layer IHC sentence and its provenance chain);
§ 2.4 (the floxed allele exists and the authors named the missing cross in 2020); § 3.2 (three secondary
transmissions all drop the Purkinje layer); § 3.3 (the GTEx entry question answered from the primary source's own
numbers); § 4 (the SCAR12 cerebellar census and its count/finding divergence against Gribaa's abstract); § 4.4 (the
WOREE vermis count at 2/101 against a held "most cases"); § 5 (the A60-freedom table); § 6 (the nearest existing
thing); § 7 P4 and P5.

---

## 2 · Purkinje-specific WWOX — every hit

### 2.1 🎯 THE ONE HIT, and it is a LAYER, not a CELL

According to PubMed, **`PMID 33255508` / `PMC7727818`** — Aldaz CM & Hussain T 2020, *WWOX Loss of Function in
Neurodevelopmental and Neurodegenerative Disorders*, *Int J Mol Sci* 21:8922,
[DOI](https://doi.org/10.3390/ijms21238922) — § 2 *"WWOX Expression in CNS"*, **first-hand, verbatim from the served
body**:

> "In early observations, we showed **robust WWOX protein expression in soma from cells of all three layers of human
> cerebellar cortex viz., Purkinje cell layer, molecular layer, and granular layer.** WWOX-positive immunostaining
> was also observed in cerebrum samples, including soma and dendrites of pyramidal neurons from frontal and occipital
> cortices and nucleus caudate, in pons and nuclei olivaris of the medulla, and astrocytes from all such regions.
> Neuropils and small neurons were also immunoreactive to the WWOX antibody, while low to negative expression was
> observed in substantia nigra. Additionally, neurons at autonomic ganglia also showed intense cytoplasmic WWOX
> staining []."

**The record, at the resolution the brief asks for:**

| Field | Value |
|---|---|
| **Species** | **Human** |
| **Age** | 🔴 **NOT STATED.** No donor age anywhere in the served text or in the primary's abstract |
| **Method** | **Immunohistochemistry**, a *"very specific anti-WWOX polyclonal antibody"*, tissue microarray cores across >30 organs plus whole sections (primary's abstract) |
| **Marker** | 🔴 **NONE. No calbindin, no PCP2/L7, no Car8, no parvalbumin, no co-stain of any kind.** The assignment is **anatomical-layer**, read off cerebellar cytoarchitecture |
| **What was measured** | **Presence and qualitative intensity** of WWOX protein immunoreactivity in **somata**, per cerebellar cortical layer. *"Robust"* — 🔴 no quantity, no per-cell intensity, no positive fraction, no `n`, no statistic |
| **Locator** | `PMC7727818`, § 2, paragraph 2, sentence 1 — verbatim above |
| **Comparator** | Cerebrum, pons, olivary nuclei, autonomic ganglia, substantia nigra (*"low to negative"*) — a **within-paper negative control region**, which is worth having |

🔴 **Why this is a layer statement and not a Purkinje-cell statement, and it matters.** The **Purkinje cell layer**
is a monolayer that contains Purkinje somata **and** the somata of **Bergmann glia** and **candelabrum
interneurons** (`PREMISE: DEFAULT_FROM_TEXTBOOK`, from cerebellar-anatomy sources retrieved on Surface B: White &
Sillitoe 2012, [DOI](https://doi.org/10.1002/wdev.65) — *"Sandwiched between the Purkinje cells are specialized glial
cells called Bergmann glia, and in lower numbers candelabrum cells"*; and Hashimoto & Hibi 2012,
[DOI](https://doi.org/10.1111/j.1440-169X.2012.01348.x) — *"The PCL contains the somata of PCs, Bergmann glia, and
candelabrum interneurons"*). The sentence says **"soma from cells of"** that layer, which rules out a pure-neuropil
reading and is more than nothing — but it does **not** say which soma. **Without a Purkinje marker, layer occupancy is
not cell identity.**

🔴 **PROVENANCE CEILING, and it is severe.** This is a **review restating its own laboratory's earlier primary work**,
and the citation marker is **stripped to `[]`** in the served surface. My attribution of the primary to
**`PMID 16941225`** — Nunez MI, Ludes-Meyers J, **Aldaz CM**, *WWOX protein expression in normal human tissues*,
*J Mol Histol* 2006;37:115–25, [DOI](https://doi.org/10.1007/s10735-006-9046-5) — is an **`INFERENZA` from four
converging descriptors**, not a read citation:
(a) same laboratory, same senior author; (b) *"early observations"* and *"we showed"*; (c) the primary's abstract
independently reports *"significant WWOX protein expression in various cell types of neural origin including
**neurons, ependymal cells and astrocytes**"* with *"a very specific anti-WWOX polyclonal antibody"* — the same
reagent description and the same downstream cell list; (d) the primary's abstract also carries the matching negative,
*"No expression of WWOX was detected in adipose, connective, and lymphoid tissues, **myelinized structures** and blood
vessels."* **It is a strong inference and it is still an inference.**
And 🔴 **the primary body is not retrievable** (§ 1.3). ⇒ **Status: `SECONDARY · LAYER-RESOLVED · MARKER-FREE ·
QUALITATIVE · PRIMARY BODY BLOCKED`.** It is the strongest existing thing, and it does not answer the marker question.

### 2.2 The two `WWOX AND Purkinje` hits measure Purkinje **number**, not WWOX

Both are already held. Neither is a WWOX measurement in a Purkinje cell, and the distinction is the whole point.

| PMID | Species · allele | Age | Method · **marker** | What was measured | Locator |
|---|---|---|---|---|---|
| **36828035** (Hussain 2023, *Prog Neurobiol* 223:102425, [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425)) | mouse, **`Wwox^P47T/P47T`** knock-in — 🔴 **the SCAR12 allele** | **80 d and 250 d** | IF, **calbindin⁺** (Purkinje) and **Hcn1⁺** (basket), cerebellar **vermis**, `n = 3`/group, box-and-whisker, median line | **Purkinje cell NUMBER**: median ≈82 → ≈25 at 80 d; ≈100 → ≈42 at 250 d, `*` both, no within-genotype bracket. **Basket cell number `ns` at BOTH ages.** Molecular layer WT 190→222 vs mutant flat 165→162; granular layer WT 103→130 vs mutant 90→92 | Fig 5d/5e/5g/5h; `deepdive_manifests/PMID36828035.json` entries 244–246 (**REPO-ATTESTED** figure attestation) |
| **32000863** (Cheng 2020, `Wwox^-/-`) | mouse, **null** | not recorded here | **cresyl violet**, midline sagittal — 🔴 **no marker** | Foliation defects lobules V, VI, VII; **Purkinje counts ≈18 vs ≈7 per area** | Results, cerebellar hypoplasia section; Fig 5b/5d; `deepdive_manifests/PMID32000863.json` L176–181 |

🔴 **The critical distinction, stated once and then relied on: `36828035` uses calbindin as a COUNTING reagent. WWOX
was never placed in that channel.** A calbindin⁺ Purkinje count in a `P47T` mutant tells you **how many Purkinje
cells survive**; it tells you **nothing about how much WWOX a Purkinje cell contains**, in mutant or in wild type.
This is the same category error as collapsing `NeuN⁺WWOX⁺ fraction` into `WWOX per transduced cell`, one level up:
**a cell count is not a protein measurement.**
⚠️ Carried from the prior record and not re-litigated: the ≈25 → ≈42 median rise is **most plausibly survivor
selection** in the 250-day cohort, the 80-day mutant box's lower whisker reaches **0**, and the panels do not decide
between selection and recovery. Any statement about that shift must name the statistic.
⚠️ **Allele and species firewall, explicit:** `Wwox^P47T/P47T` ≠ `Wwox`-null ≠ `Wwox^gt/gt` ≠ rat `lde/lde` ≠ human
WOREE ≠ human SCAR12. Nothing in this table transfers between those rows.

### 2.3 What is `PREMISE: NOBODY_LOOKED`, enumerated

🔴 **In the AAV model (`PMID 42422765`, `PMID 34747138`), all of the following are NOT ASSAYED — and that is neither
`NORMAL` nor `ABSENT`:**
Purkinje-cell transduction · Purkinje-cell vector-genome load · Purkinje-cell WWOX protein or transcript · any
cerebellar layer-resolved value of any kind · `hSynI` promoter activity in any cerebellar cell type.
Validated negatives on the 2026 body, carried from the sibling file: `Purkinje` 0 · `granule` 0 · `calbindin` 0 ·
`molecular layer` 0 · `lobul` 0 · `vermis` 0, with positive controls (`cerebell` 7, `NeuN` 2, `hSynI` 17) passing.

🔴 **Across the whole corpus, in any species:** no WWOX **in-situ hybridisation resolved to a cerebellar layer**; no
WWOX **single-cell measurement with a Purkinje cluster**; no **cerebellar organoid** (every organoid in this
literature is forebrain/cerebral — `PMID 42397075`); no **Purkinje-specific conditional allele** (§ 2.4).

### 2.4 🎯 NEW — the floxed allele **exists**, and the authors named the missing cross in 2020

This is what a **read body** gives that the Surface-A zero could not.

**First-hand, `PMC7727818` § 3.3, verbatim:**
> "while developing models to study the role of WWOX in cancer, we generated a full knockout () model using **mice
> harboring loxP sites flanking exon 1 of the gene** () crossed to mice expressing **Cre-recombinase controlled by
> adequate promoters** to obtain whole-body deletion []."

**First-hand, same paper, Conclusions, verbatim:**
> "new conditional targeted models and models with longer lifespan are needed to provide more valuable mechanistic
> insights. For instance, **targeted CNS ablation using promoters driving Cre recombinase to specific mouse brain
> regions such as the cerebellum**, cortex, hippocampus, or **specific cell types**, such as excitatory neurons or
> microglia, **will be highly informative**."

⇒ 🎯 **A conditional `Wwox` allele exists and has been in hand since the knockout was built. No cerebellar or
Purkinje-restricted cross has been reported, and the allele's own makers stated the gap in print in 2020.** Six years
on, § 1.1(iii)'s Methods-invisible zero and this body agree: **it is still open.** ⚠️ Whether an unpublished cross
exists is not determinable from here. `HUMAN_REQUIRED` if anyone wants to ask; **I have not.**

---

## 3 · Cerebellar cell-type resolution more broadly, including single-cell atlases

### 3.1 The complete table — every dataset in which WWOX is reported with any cell-type or layer resolution

All rows first-hand from `PMC7727818` § 2 unless stated. 🔴 **Every one of these is a WILD-TYPE expression map. Not
one is a WWOX-deficient or AAV-treated system.**

| Dataset | Species · age | Resolution achieved | Purkinje reported? | What it says about WWOX |
|---|---|---|---|---|
| 🎯 **Human cerebellar-cortex IHC** (§ 2.1; primary = `PMID 16941225`, body blocked) | human, age **NOT STATED** | 🟢 **LAYER** — all three cortical layers named | 🟡 **Purkinje cell LAYER yes; Purkinje CELL not identified** | *"Robust WWOX protein expression in soma from cells of all three layers"* — **qualitative only** |
| **DropViz** scRNA-seq (Saunders 2018) | **mouse**, adult | 🟢 **CELL TYPE** — clusters and sub-clusters | 🔴 **NOT REPORTED, IN EITHER DIRECTION** | Top cerebellar clusters = **interneurons (`Pvalb`⁺)** and **granule cells (`Gabra6`⁺)**; on sub-clustering, *"specifically **GABAergic basket cells** (i.e., interneurons) and, to lesser extent, **granular neurons** are the top cell types"* |
| **Allen Mouse Brain Atlas** ISH | mouse, adult | 🔴 **REGION only** | 🔴 no | *Wwox* probe *"clearly visible in cerebellum cortex"*; strongest signal in **ENTm2**, **BLAa/BLAp**, isocortex **L5**. 🔴 **No cerebellar layer or cell type in the served text** |
| **Brain-cell-type RNA-seq (P7)** | mouse, **P7** | 🟡 broad classes | 🔴 no | *"uniform expression … in neurons and all glial cell types"*; within oligodendrocytes, **progenitors > mature myelinating**. 🔴 Not cerebellum-specific |
| **HBT** (Human Brain Transcriptome) | human, conception→adult | 🔴 **REGION only** | 🔴 no | 🎯 **CBC behaves differently from every other region** — *"a more significant increase in early postnatal life and remaining higher (compared to other tissues) up to adolescence"* |
| **GTEx** | human, adult | 🔴 **REGION only** | 🔴 no | Cerebellum **median 12.1 TPM**; FC 6.9, AMY 6.2, HIP 5.6 — *"cerebellum is the CNS structure with the highest expression levels in adults"* |
| **Rat brain IHC** (Tochigi 2019, restated) | **rat** | 🟡 broad classes | 🔴 no | *"almost all brain regions, including … cerebellum … and in various cell types including **neurons, astrocytes, and oligodendrocytes**"* — 🔴 **general classes, not cerebellar cell types** |
| **Mouse embryo/adult ISH** (Chen 2004, `PMID 15026124`, restated; body not retrievable, no PMCID) | mouse, E8→adult | 🔴 REGION | 🔴 no | ⚠️ **Adult list is `choroid plexus`, `ependymal cells`, and *"low to moderately expressed in the cerebral cortex, striatum, optic tract, and cerebral peduncle"* — CEREBELLUM IS NOT IN IT.** Recorded because it does not obviously agree with the human/GTEx picture; I cannot adjudicate it from a restatement |
| Human **forebrain/cerebral organoids** (`PMID 42397075`) | human iPSC | 🟢 cell type — **but forebrain** | ⛔ n/a | 🔴 **No cerebellar organoid exists anywhere in this literature** |

🔴 **The DropViz Purkinje absence must be read as `NOT ASSAYED`, and there is a named methodological reason.**
DropViz is Drop-seq on dissociated adult mouse brain. `PREMISE: DEFAULT_FROM_TEXTBOOK` and offered as a
**hypothesis, not a fact — I did not read Saunders 2018**: dissociation protocols for adult cerebellum recover
very large, elaborately arborised neurons poorly, and Purkinje cells are the largest neurons in the cerebellum, so
**a Purkinje cluster's absence from a cerebellar Drop-seq atlas is at least as likely a representation property of
the protocol as a statement about the cells.** ⇒ A single-cell atlas that does not report Purkinje cells is a
`DETECTION_FLOOR`-class silence. **`NOT ASSAYED` is never `ABSENT`, and it is never `LOW`.**

### 3.2 🎯 NEW — three independent secondary transmissions, and **every one of them drops the Purkinje layer**

| Source | What it transmits, verbatim | Purkinje? |
|---|---|---|
| **The paper's own abstract** (`PMC7727818`) | *"GABAergic basket cells and granule cells from cerebellar cortex are the specific neuronal subtypes that display the highest expression levels"* | 🔴 **dropped** |
| **The paper's own Conclusions** | *"in specific cell types, such as basket cells and granule cells"* | 🔴 **dropped** |
| **Battaglia 2023** (`PMID 38161429`, [DOI](https://doi.org/10.3389/fped.2023.1301166)) | *"the WWOX protein is mostly expressed in the cerebellar cortex and in specific cell types, such as basket cells and granule cells"* | 🔴 **dropped** |
| **You 2024** (`MGG` 12(8), [DOI](https://doi.org/10.1002/mgg3.2500)), Discussion, via Surface B | *"At the cellular level, the **granulosa cells** of GABAergic neurons showed the highest expression levels."* | 🔴 **dropped, and the sentence is garbled** — *"granulosa"* is an **ovarian** cell type, and basket and granule cells have been merged into one non-existent category |

⇒ 🔴 **The Purkinje-layer observation survives in exactly one place — the review's own § 2 body — and has been dropped
by its own abstract, its own conclusions, and every downstream citation I could read.** This is the propagation
mechanism, and it explains the repository's own gap at § 1.5: two prior actors read this paper in full and captured
the abstract-level cell-type statement, which is the one with no Purkinje cell in it.

### 3.3 🎯 NEW — the GTEx entry question, answered from the primary source's own numbers

`cerebellum_layer_localisation_20260922.md` § 11.1 leaves open **which** of the two cerebellar GTEx entries the
1.77×/2.17× ratios require, and asks that the entry be named. **The review states its own four values, and they
decide it.** Checked by me today against the repository's local extract
`disease-models/wwox/analysis/data/WWOX_tissue_expression_GTEx.csv`:

| Aldaz 2020, stated | Local CSV row | Value | Match |
|---|---|---|---|
| cerebellum **12.1** | `Brain_Cerebellar_Hemisphere` | **12.1278** | ✅ **exact to one decimal** |
| HIP **5.6** | `Brain_Hippocampus` | **5.58518** | ✅ exact |
| AMY **6.2** | `Brain_Amygdala` | **6.16809** | ✅ exact |
| FC **6.9** | `Brain_Frontal_Cortex_BA9` 6.8204 · `Brain_Cortex` 6.84932 | — | ⚠️ **both round to 6.8, not 6.9** |
| *(not used by Aldaz)* | `Brain_Cerebellum` | 11.2144 | → would round to **11.2**, not 12.1 |

⇒ 🎯 **The primary source uses `Brain_Cerebellar_Hemisphere` (12.1), not `Brain_Cerebellum` (11.2).** So the sibling
file's **1.771× / 2.172×** are the ratios its own source implies, its § 11.1 request is satisfied, and the entry is
now named. Its own internal check (*"2.172 — exact"*) is independently confirmed: `12.1278 / 5.58518 = 2.1714`.
⚠️ **One value does not reconcile** — 6.9 against 6.82/6.85 — plausibly a GTEx release difference or a fifth cortical
entry. Not resolved; recorded. 🔴 **And the bound that dominates all of this is unchanged and still governs: GTEx is
HUMAN RNA and the experiment is MOUSE PROTEIN.** This is indicative of a direction, not an applicable correction, and
**nothing here licenses restating any published fold-of-WT as corrected.**

---

## 4 · 🎯 The SCAR12 pole — kept strictly separate from WOREE

**Two families. Six affected individuals by the founding accounts. Both alleles homozygous missense, both hypomorphic.**

| | Family 1 | Family 2 |
|---|---|---|
| Allele | **`p.Pro47Thr`** homozygous — **WW1 domain** | **`p.Gly372Arg`** homozygous — **SDR domain** |
| Origin | large consanguineous, Saudi Arabia | Israeli-Palestinian |
| Affected | **4 siblings** | **2 siblings** |
| Seizure onset | **9–12 months**, all four | first two years of life |
| Walking | delayed to **2–3 years** | — |
| Phenotype | *"Moderate to mild cerebellar ataxia and psychomotor retardation … severe dysarthria, nystagmus, diminished reflexes, and severe intellectual disability"* | *"generalized tonic-clonic epilepsy, developmental delay, intellectual disability, **spastic ataxia, and paraplegia**"* |
| 🎯 **Cerebellar imaging** | **"Mild cerebellar atrophy … in MRI of two affected children"** 🔴 second-hand, see § 4.2 | 🔴 **NONE REPORTED, in any source I read** |
| Protein | normal level; **PPxY binding abolished** (P47T) | normal level; consequence *"unclear at this point"* |
| Outcome | **alive at 17–26 years** (repo-attested, `CLAIM 030`) | — |

All quotations first-hand from `PMC7727818` § 3.1. **`CLAIM 030` and `CLAIM 008` govern the genotype–phenotype
reading and are not modified here.**

### 4.1 The complete SCAR12 cerebellar census

| Evidence class | Status |
|---|---|
| **Imaging** | 🟡 **ONE line only** — *"Mild cerebellar atrophy was seen in brain magnetic resonance imaging (MRI) of two affected children"* (P47T family). 🔴 **SECONDARY and it does not reconcile — § 4.2.** Nothing for G372R |
| **Neuropathology / autopsy / post-mortem** | 🔴 **NONE, and a verified zero.** `WWOX AND (autopsy OR "post-mortem" OR postmortem OR neuropathology OR "brain biopsy" OR fetus OR fetal)` → **17 hits, complete correct translation, positive controls firing, and not one is a SCAR12 patient.** Independently expected: the SCAR12 patients are recorded **alive at 17–26 years**, so there is no post-mortem to find |
| **Any cell-type observation** | 🔴 **NONE, in any tissue.** `PREMISE: NOBODY_LOOKED` |
| **Vermis vs hemispheres; atrophy vs hypoplasia** | 🔴 **NOT RESOLVED.** The single line says *"cerebellar atrophy"* — i.e. **atrophy, not hypoplasia** — with **no compartment named**. Vermis is never mentioned in the SCAR12 material, which is the opposite of the WOREE material (§ 4.4) |
| **Quantitative cerebellar endpoint** | 🔴 **NONE.** No volumetry, no vermis measurement, no serial imaging, no motor battery, no eyeblink conditioning, no VOR |
| **The only tissue assay in the pole** | Mallaret 2014: Western blot and peptide pull-down on **patient FIBROBLASTS**. 🔴 **Says nothing about cerebellum.** Body **paywalled** (§ 1.3) |
| **The only biopsy in the pole** | Gribaa 2007: a **MUSCLE** biopsy — *"vacuolization of the sarcotubular system"*. 🔴 **Muscle, not cerebellum** |

### 4.2 🔴 NEW — the one cerebellar imaging datum does not reconcile with its own primary abstract

The cited primary is **`PMID 17470496`** — Gribaa M, Salih M, Anheim M, … **Koenig M**, *A new form of childhood onset,
autosomal recessive spinocerebellar ataxia and epilepsy is localized at 16q21-q23*, *Brain* 2007;130(Pt 7):1921–8,
[DOI](https://doi.org/10.1093/brain/awm078). According to PubMed, its abstract states, **first-hand, verbatim**:

> "We report here a large consanguineous family from Saudi Arabia with four affected children presenting with
> generalized tonic-clonic epilepsy, ataxia and mental retardation, but neither myoclonus nor mental deterioration.
> **MRI and muscle biopsy of one patient revealed, respectively, posterior white matter hyperintensities** and
> vacuolization of the sarcotubular system."

🔴 **Two divergences from the review's restatement, and they run in the same direction:**

| | Aldaz 2020 (secondary) | Gribaa 2007 abstract (primary) |
|---|---|---|
| **How many patients imaged** | *"**two** affected children"* | *"MRI … of **one** patient"* |
| **What the MRI showed** | *"Mild **cerebellar atrophy**"* | *"**posterior white matter hyperintensities**"* |

⚠️ **Stated at its real strength, in both directions.** An abstract compresses, and a 2007 *Brain* Results section
could easily report both a white-matter finding and mild cerebellar atrophy, in one patient or in two. **I am not
asserting that the review is wrong.** What I am asserting is that **the only cerebellar imaging datum in the entire
SCAR12 pole is a secondary restatement whose patient count and named finding both differ from the primary abstract,
and the primary body cannot be opened from here** — `17470496` has **no PMCID at all** (§ 1.3).
⇒ **`PREMISE: SECONDARY_UNVERIFIED`.** It must not be relayed as *"cerebellar atrophy is documented in SCAR12"*
without this boundary attached. `REVIVAL_TRIGGER` in § 8.

### 4.3 🎯 The verdict on the brief's question 3 — and the allele irony that is the real answer

🔴 **No. The SCAR12 pole does not supply cerebellar cell-type evidence the WOREE literature lacks. On cell type it is
emptier than the WOREE pole.** What it supplies is a *milder, later-onset, ataxia-dominant clinical syndrome* with
**survival into adulthood** — which is scientifically valuable for other reasons and is **not** cell-type evidence.
Six patients, zero neuropathology, zero cell-type observation, one unverified second-hand imaging line.

🎯 **But the pole's real contribution is indirect, and it is load-bearing:**

> **The only calbindin-resolved cerebellar cell-type data in the entire WWOX literature sit on the SCAR12 allele.**
> `Wwox^P47T/P47T` (`PMID 36828035`) **is** the P47T SCAR12 allele, knocked into a mouse. Its Fig 5d/5e are the only
> place in this literature where a **Purkinje marker** and a **cerebellar-interneuron marker** are counted side by
> side, with a **`ns` specificity control** — *"a cerebellar interneuron population is spared beside a Purkinje
> population reduced to a quarter"*.

So the ataxia pole does reach the cerebellum at cell-type resolution — **by way of a mouse, and it counts Purkinje
cells rather than measuring WWOX in them.** Three boundaries on using that, all of which must travel with it:
1. 🔴 **Species and allele:** a **mouse** carrying a **knocked-in human SCAR12 missense allele** is not a human SCAR12
   patient, and it is not the `Wwox`-null mouse the AAV experiments use. Three different systems.
2. 🔴 **Quantity:** Purkinje **number**, not Purkinje **WWOX**. And in this allele **protein level is normal** — so the
   Purkinje loss happens *at a normal WWOX abundance*, which is why `CLAIM 030` holds that **severity tracks residual
   function, not abundance**.
3. ⚠️ **Survivor selection** on the 250-day cohort, already flagged.

### 4.4 🔴 The WOREE pole, held strictly separate — and a held repository statement that this narrows

First-hand from **`PMID 38161429` / `PMC10757851`** (Battaglia *et al.* 2023, *Front Pediatr* 11:1301166,
[DOI](https://doi.org/10.3389/fped.2023.1301166)), a systematic neuroimaging collation of **101 WOREE patients across
9 studies**. Recorded here **only** to keep the two poles separate and to correct a propagated count.

**Table 1, cerebellar row, eyeballed in the served linearisation:**
> `Hypoplasia of the cerebellar vermis` → **`2:2`** — a **single** value, against nine study columns.

⚠️ **A structural check on that reading, because a linearised table can mislead.** The
`Hypoplasia of the corpus callosum` row returns **nine** values for nine study columns, so the linearisation is
**order-preserving**; the `Brain atrophy` row returns **seven**, so **blank cells are dropped rather than emitted**.
⇒ A one-value row genuinely means **eight studies are blank**, but 🔴 **the column that value belongs to is NOT
determinable from the linearised text.** My assignment to **Iacomino (`n = 2`)** rests on two prose facts, not on the
table's geometry: Iacomino's cohort is `n = 2`, and the body states, verbatim, *"Notably, hypoplasia of cerebellar
vermis related to WOREE syndrome was **first reported in this study**"* (of Iacomino). Flagged as an inference.

**Three further first-hand statements from the same body:**
> *"cerebellar vermis hypoplasia were observed in a lower percentage of cases, and therefore these findings seem to be
> **less specific**."*
> Of Tabarki's five patients: *"a brain MRI revealed a peculiar pattern of neurodegeneration … **Of note, the
> cerebellum was not affected**."*
> Fig 1 legend: *"Fetal MRI and **high-resolution post-mortem MRI** of an affected patient were performed at 21
> gestational weeks, demonstrating **mild hypoplasia of the cerebellar vermis** … The laminar organization of the
> cerebral hemispheres and cortical gyration are appropriate for the gestational age."*

🔴 **THIS NARROWS A HELD REPOSITORY STATEMENT, and I flag it rather than edit it.**
`discovery_ledger_current.md` L554 and receipt `FTR-20260921-35573960-01` carry, from Riva 2022 (`PMID 35573960`), the
literature-level sentence *"cerebellar vermis hypoplasia … **have been described in most cases**."* A systematic
collation of **101 patients** puts it at **2 patients from 1 study**, calls it **less specific**, and records that one
five-patient cohort found the cerebellum **unaffected**.
⇒ **"most cases" is not supportable and should not be propagated.** The prior actor's own caveat — that midline
vermian hypoplasia on MRI and an unremarkable cerebellar cortex on light microscopy *can both be true* — stands and
is strengthened. `FIND ISSUE` → prior-art sequence run (§ 1.6) → **no registry, ledger or receipt edited.**
🟢 **And one genuinely useful thing exists in the WOREE pole that the SCAR12 pole lacks: a post-mortem.** It is a
**high-resolution post-mortem MRI at 21 gestational weeks** — 🔴 **imaging, not histology**, with **no cerebellar
cell-type work of any kind.**

---

## 5 · 🎯 Which cerebellar WWOX measurements are free of the clone-A60 confound

The A60 confound bites **only** measurements that use **NeuN as the cell-identity channel**. Freedom from it is
therefore necessary and nowhere near sufficient — and separating the two failure modes is the point of this table.

| Measurement | A60-free? | **Can it see a Purkinje cell?** | Verdict |
|---|---|---|---|
| 🎯 **Human cerebellar-cortex IHC** (§ 2.1) — layers, no NeuN | 🟢 **YES** | 🟢 **YES — and it does.** Purkinje cell layer named | ✅ **THE ONLY ONE.** 🔴 And it is qualitative, human, wild-type, **marker-free**, and its primary body is blocked. Free of the A60 confound and free of nothing else |
| `PMID 36828035` Fig 5d/5e — **calbindin⁺**, **Hcn1⁺** | 🟢 **YES** | 🟢 **YES** | 🔴 **Measures the wrong quantity.** A clean cell-type measurement of Purkinje **number**; WWOX is not in the channel |
| `PMID 32000863` — cresyl violet Purkinje counts | 🟢 YES | 🟡 morphologically | 🔴 No marker, no WWOX channel |
| **DropViz** scRNA-seq | 🟢 YES | 🔴 **No Purkinje cluster reported** | 🔴 Cell-type resolved and **Purkinje-silent** (§ 3.1) |
| **Allen ISH · HBT · GTEx** | 🟢 YES | 🔴 **no cell-identity channel at all** | 🔴 **Free of the confound because it has no cell types.** Not an answer |
| **2026 vDNA / mRNA / immunoblot panels** (Fig 5A–5L, S5J/K) | 🟢 YES | 🔴 **no** — whole-cerebellum homogenate, granule-dominated | 🔴 Same: A60-free and cell-type-blind |
| 🔴 **`%NeuN⁺WWOX⁺` cerebellum ≈61% (2026 S3C) and ≈57% (2021 Fig 2G)** | 🔴 **NO** | 🔴 **NO — excluded by reagent construction** | 🔴 **CONFOUNDED.** `MAB377` = clone A60; Purkinje cells are outside numerator **and** denominator |

⇒ 🎯 **One cerebellar WWOX measurement in the whole literature could have seen a Purkinje cell, and it is the
Aldaz/Nunez human IHC.** Everything else either cannot see cell types at all, or sees them through a reagent that
is blind to the one that matters, or measures cell number instead of WWOX. **That is why the answer to the brief's
headline question is "once, as a layer".**

---

## 6 · 🎯 The nearest existing thing, and the single step that would make it answer the question

Four candidates, ranked, each with **one** step.

### 🥇 1 · `PMID 16941225` — the human cerebellar IHC that already contains the answer
**What it is.** Nunez, Ludes-Meyers & Aldaz 2006, *J Mol Histol* 37:115–25,
[DOI](https://doi.org/10.1007/s10735-006-9046-5). Human, protein, immunohistochemistry, *"a very specific anti-WWOX
polyclonal antibody"*, tissue microarrays across >30 organs plus whole sections — and per § 2.1 it **already reports
somatic WWOX in the Purkinje cell layer**.
**The one step.** 🎯 **Retrieve the body and the cerebellar figure, and read whether any panel shows a Purkinje soma
at magnification.** That converts a review sentence into an inspectable image with a stated antibody, and it is a
**reading step, not an experiment** — the cheapest thing named in this file.
🔴 **Blocked here:** `PMC4144810` → `full_text: ""`; `is_open_access: false`, `© Springer` ⇒ **a licence, not a route
failure**, reproduced today and now confirmed three times in this repository. Parked `HUMAN_REQUIRED`; **no external
action taken, no correspondence, no request.**

### 🥈 2 · The `Wwox` floxed exon-1 allele — the only route to *necessity* rather than *presence*
**What it is.** A conditional `Wwox` allele, `loxP` flanking exon 1, in the Aldaz laboratory since the knockout was
built (§ 2.4, first-hand).
**The one step.** 🎯 **Cross it to `Pcp2`/`L7`-Cre.** Every measurement in §§ 2–5 asks *"is WWOX present in a Purkinje
cell?"* This is the only design that asks *"does a Purkinje cell need it?"* — and it is the cross the allele's own
makers named in print in 2020 and nobody has reported. Cost: a mouse cross, no new construct, no new reagent.
⚠️ It answers a different question from the AAV problem and does **not** discriminate the delivery hypotheses in § 7.

### 🥉 3 · A public human cerebellar single-nucleus dataset that already resolves Purkinje cells
**What it is.** Cheng, Feng, Flanagan, Bonakdarpour & Cummings 2025, *Alzheimer's & Dementia* 21(S1),
[DOI](https://doi.org/10.1002/alz70855_105855) — retrieved on Surface B, open access. **snRNA-seq + snATAC-seq
multiome, 103,861 nuclei, post-mortem HUMAN cerebellum** plus frontal cortex, with **Purkinje and granule clusters
explicitly separated** and gene-level results reported per cluster (*"SEZ6L2 in Purkinje cells and KANSL1 in granule
cells"*).
**The one step.** 🎯 **Query the existing matrix for `WWOX` in the Purkinje cluster.** Zero wet work, zero new tissue,
zero reagent. It converts the central premise from `NOBODY_LOOKED` to a measured yes/no **in a human Purkinje
nucleus** — and, uniquely among the candidates, it also returns **chromatin accessibility at the `WWOX` locus per
cerebellar cell type**, which no other dataset in this census can.
🔴 **Bounds, and they are real.** ⚠️ It is a **conference abstract**: the accession, the data-availability terms and
the cluster definitions are **`NOT STATED`** in what I read. ⚠️ It is **human post-mortem AD/ADRD and control
cerebellum** — **not** WWOX-disease tissue, **not** a developmental timepoint, and **not** a mouse. It answers *"is
`WWOX` transcribed in a human Purkinje nucleus, and is its locus accessible there"* and **nothing** about WWOX disease.
**Second instance, non-mammalian:** Takeuchi *et al.* 2016, *J Comp Neurol* 525:1558–85,
[DOI](https://doi.org/10.1002/cne.24114) — **FACS-purified granule vs Purkinje transcriptomes by RNA-seq and ISH,
zebrafish larvae.** Same one step (query for `wwox`), with a whole-species firewall on the answer.

### 4 · Human Protein Atlas — a possible second, independent, marker-era human answer, blocked by the allowlist
HPA's brain section annotates **cerebellum immunohistochemistry by cell type, including Purkinje cells**, and the
repository already holds `PMID 32139519` (Sjöstedt 2020, [DOI](https://doi.org/10.1126/science.aay5947)) at
abstract depth. 🔴 `proteinatlas.org` is unreachable (§ 1.4, control confirmed). **One page, potentially a second
independent human Purkinje answer with a stated antibody.** `REVIVAL_TRIGGER` in § 8.

### 🎯 If only one step can be taken
**Take #3.** It is free, the tissue is already collected, the nuclei are already sequenced, the Purkinje cluster is
already called, and it needs **no antibody, no animal, no licence and no reagent** — the four things that block #1,
#2 and #4 respectively. #1 is cheaper in principle and is **licence-blocked here**; #2 is the only one that tests
necessity and is a months-long cross; #4 is one page and is **network-blocked**.
⚠️ **And what #3 cannot do:** it cannot say whether a Purkinje cell is **transduced** by AAV9, which is the question
§ 7 is about. For that, the cheapest move remains the sibling file's: **calbindin + WWOX, or calbindin +
`AAV9-hSynI-EGFP`, on sections that already exist.**

---

## 7 · Five mechanistically distinct hypotheses for the per-nucleus cerebellar vector-genome deficit

**Given:** the deficit is at **layer 2, VECTOR GENOME**, is ~9–12× below cortex, is **per host nucleus** because the
qPCR loads a fixed **DNA mass**, and therefore **cell density is already divided out and cannot explain it**
(sibling file §§ 3.2a, 4.3). **No winner is selected. No numerical probabilities.** Each is `IPOTESI`.

🔴 **Overlap declared up front so nothing double-counts.** The sibling file already holds **H1** denominator ·
**H2** mitotic dilution · **H3** `hSynI` promoter mismatch · **H4** regional turnover · **H5** loading-control drift ·
**H6** Purkinje invisibility · **H7** pre-existing lesion. This file adds hypotheses that act at **genome arrival and
genome counting** — the layer where the deficit is actually established — and marks **P2** as carried-not-new.
Promoter mismatch (H3) and pre-existing lesion (H7) are **carried unchanged** and are not layer-2 genome-arrival
mechanisms, so neither competes with P1/P3/P4/P5.

### P1 · Receptor and glycan availability — AAV9 needs terminal galactose, and the cerebellum's glycan surface differs
**Mechanism.** AAV9's primary attachment factor is **terminal N-linked galactose**, with entry depending on the
AAV receptor AAVR/KIAA0319L. If cerebellar parenchyma presents **less terminal galactose** — or is more heavily
**sialylated**, which caps and masks galactose — then fewer capsids bind and internalise **per cell exposed**. This
gives fewer genomes per nucleus at the **same local capsid concentration**. It is an **uptake-efficiency** mechanism:
not access (P3), not dilution (P2), not counting (P4), not composition (P5).
**Also predicts.** Neuraminidase pre-treatment, which de-sialylates and exposes galactose, raises cerebellar
transduction **disproportionately** · a capsid with a different glycan requirement (AAV1, AAVrh10, AAV-PHP.eB) shows
a **different** cerebellum/cortex vDNA ratio at matched dose and route · 🎯 **the ratio is ROUTE-INVARIANT** · regional
AAVR protein levels differ · the deficit reproduces in adult as well as neonatal delivery.
**Supporting.** The deficit is **per-nucleus** and **dose-proportional** — cerebellar vDNA `2.28×` against a nominal
`2.1382×` (sibling § 4.2). Proportionality with dose is what a **fixed per-cell binding efficiency** produces: halving
the efficiency scales the output and leaves the slope proportional. Nothing in either paper measures capsid binding,
receptor level or glycosylation.
**Against.** 🔴 Nothing is measured in **any** direction — no binding assay, no AAVR, no glycan analysis, in either
paper or anywhere in this corpus. ⚠️ `PREMISE: DEFAULT_FROM_TEXTBOOK` on AAV9 galactose biology: **not tested, stated
or cited in either paper**, and it must never be quoted as a result of `PMID 42422765`.
**Cheapest discriminating experiment.** 🎯 **A capsid-binding assay at 4 °C on acute cortical and cerebellar slices
from wild-type mice** — binding only, no expression step, no vector cohort, no antibody, no baseline. If binding per
nucleus is equal, P1 is dead and the deficit is downstream of attachment. The confirmatory version is **two capsids
side by side in one neonatal ICV cohort**, reading only vDNA per nucleus in cortex and cerebellum.

### P2 · Mitotic dilution of episomal genomes in the postnatally-dividing granule lineage
🔴 **NOT NEW — this is the sibling file's H2, carried unchanged and NOT re-derived.** Listed so the set is complete
and so its falsifier is not double-counted. Mechanism, predictions, support and the S8 counter-evidence are at
`cerebellum_layer_localisation_20260922.md` § 8 H2.
🎯 **One addition that is new and does not overlap.** That file's "against" leans on the S8 statement that HD delivery
at any point P0–P5 rescued, which is weak because five days is short against granule-cell proliferation. A sharper,
**age-series-free** falsifier is available: **episomal AAV genomes are diluted by division; an integrated genome is
not.** So deliver an **integrating reporter** (lentiviral, or an AAV-integrase system) at P0 alongside the AAV9, and
read per-nucleus copy number in cerebellum vs cortex at P30 **in the same animals**. If the cerebellar deficit is
present for the episomal vector and **absent for the integrating one**, it is dilution. One cohort, one timepoint.

### P3 · CSF-route access — the deficit is **arrival**, and it is geometric
**Mechanism.** After neonatal ICV into the lateral ventricles, vector reaches cerebellum only by travelling caudally
(third ventricle → aqueduct → fourth ventricle) or through the subarachnoid space over the cerebellar surface.
Periventricular forebrain is exposed **first, at higher concentration, for longer**. Cerebellar parenchyma is then
transduced **from its pial surface inward**, so per-nucleus load falls with depth — and the **granular layer**, which
supplies the great majority of cerebellar nuclei, lies **deep** to the molecular layer.
**Also predicts.** 🎯 **A depth gradient inside the cerebellar cortex** — molecular > Purkinje > granular > deep
nuclei — which a homogenate averages away · a **lobule gradient**, vermis and surface folia above hemispheric depths ·
intracisternal or intrathecal delivery **narrows or reverses** the cerebellum/cortex ratio · 🎯 **the ratio is
ROUTE-DEPENDENT.** That single contrast — route-invariant (P1) against route-dependent (P3) — is what separates them
with one experiment.
**Supporting.** 🔴 **Neither paper measures delivery at all.** First-hand from the sibling file § 3.1: no CSF tracer
distribution, no vector-spread time course, no injection-site verification histology, no measurement of what reaches
the fourth ventricle. The 2021 Trypan blue visualises **the dispensed liquid at the needle** and **no distribution
result is reported anywhere in that paper.** Cerebellar access is **assumed**; the gradient is measured, its cause
is not.
**Against.** 🔴 The deficit is **dose-proportional** (`2.28×`), and a purely geometric account with a saturating
surface would tend to predict **sub**-proportionality at the higher dose. ⚠️ `PREMISE: DEFAULT_FROM_TEXTBOOK` — this
is background, not evidence from either paper. ⚠️ And volume is a **stated constant** `2.0 µL/hemisphere` across
arms, so "HD spread further" is REFUSED and already held.
**Cheapest discriminating experiment.** 🎯 **One cohort, two routes** — neonatal ICV against intracisternal — reading
only vDNA per nucleus in cortex and cerebellum. **If the ratio moves, it is access. If it does not, access is not the
explanation** and P1/P4/P5 survive.

### P4 · 🔴 NEW — the "per nucleus" denominator is **estimated, never measured**, and can be biased region-specifically
**Mechanism — a measurement mechanism, not a biological one.** The assay loads **50 ng of DNA per reaction with one
primer pair and no host reference amplicon** (sibling § 3.2, first-hand Methods). The step
*"50 ng ⇒ a fixed number of nuclei"* holds **only if DNA mass per nucleus is equivalent in the two tissues**, and two
things can break that in cerebellum specifically. **(a) Recovery.** Cerebellar granule nuclei are small and
heterochromatin-dense; homogenisation and lysis efficiency is **not uniform across nuclear types**, so the nuclei
actually **represented** in 50 ng of recovered DNA need not match the tissue's nuclear composition. **(b) Non-nuclear
DNA.** Mitochondrial DNA counts toward the 50 ng while contributing **no nuclear genome**, and mitochondrial content
per unit tissue differs markedly between a granule-cell-dominated compartment and a cortex with large pyramidal
arbours. Either way, the denominator "host nuclei" is **inferred from mass**, and the bias can be **region-specific**.
**Also predicts.** Adding a **single-copy autosomal host amplicon** to the same reactions **changes** the
cerebellum/cortex ratio · mtDNA copies per ng of total DNA differ between the two tissues · the ratio measured on
**purified nuclei** differs from the ratio on whole-tissue DNA · 🎯 and the sharp one: the ratio measured by
**DNA-FISH on intact, visibly-identified nuclei** — which counts genomes per nucleus with **no mass assumption at
all** — **disagrees** with the qPCR ratio.
**Supporting.** 🎯 **The one control that would test this is precisely the control the assay lacks.** First-hand
validated negatives in the sibling file: `reference gene` 0 · `single-copy` 0 · `standard curve` 0 ·
`absolute quant` 0 · `copies` 0 · `diploid` 0. And the panel's own caption is *"normalized to WT levels"*, which is
🔴 **undefined for a quantity wild-type animals do not have**, so whether Fig 5A–5D plots copies per reaction at all
is `NOT READABLE`. **The absence of the control is the evidence that the assumption is untested.**
**Against.** 🔴 The bias is of **unknown sign** and would have to be **enormous — roughly 9–12× — to carry the whole
deficit**, which is not plausible for a lysis-efficiency or mtDNA effect. So it most plausibly **inflates** rather
than **creates**. And it does **not** explain the mRNA deficit, which rides a different denominator (total RNA mass).
**Cheapest discriminating experiment.** 🎯 **Re-run the archived DNA with a single-copy host reference amplicon in the
same wells.** Same samples, same plate, **one extra primer pair** — and it retro-fits every published vDNA number in
this literature. This is the cheapest experiment named anywhere in either file, and it targets **the strongest
single result the sibling file establishes**, which is exactly why it should be run before that result is built on
further.
🔴 **Distinctness, stated because it is easy to confuse:** this is **NOT** the sibling file's **H5**. H5 is drift in
the **protein loading control** at layer 5. P4 is drift in the **DNA denominator** at layer 2 — and the sibling file
itself names the gap P4 fills: *"the cerebellar deficit **also appears in vDNA**, a DNA-mass-normalised measurement
**with no protein loading control anywhere in it**. So H5 cannot be the whole account."* **P4 is the hypothesis that
closes that escape route.**

### P5 · 🔴 NEW — composition is doing the work, because a homogenate average over cell types of very different size is not a per-cell rule
**Mechanism.** The measured quantity is
`genomes per average nucleus = Σᵢ (fraction of nuclei of type i) × (genomes per nucleus of type i)`.
Cerebellum's nuclear population is **overwhelmingly granule-cell**; cortex's is a far more even mix of pyramidal
neurons, interneurons and glia. Suppose per-nucleus genome load scales with something like **membrane surface or
arbour extent per nucleus** — bigger cells present more surface to the interstitium, sample more capsid, and end with
more genomes per nucleus. Then **granule-cell nuclei are intrinsically poor per-nucleus carriers**, and the cerebellar
average is dragged down **by composition**, even though **every cell type obeys the same rule**. 🎯 Under P5 there is
**no cerebellum-specific biology at all**: there is a cell-size rule, and the cerebellum is simply the tissue where
the small-cell type dominates the nuclear count.
**Also predicts.** 🎯 Per-nucleus vDNA **scales with soma/arbour size across cell types, within and between regions** ·
🎯 **a cerebellar Purkinje nucleus — among the largest neurons in the brain — carries NEAR-CORTICAL OR HIGHER load**,
which is the **opposite** of what a delivery-limited account predicts for the cell type ataxia implicates ·
cerebellar **deep-nuclei** neurons, also large, likewise read high · the **granular layer** reads lowest · a cortical
field artificially enriched for small neurons reads low.
**Supporting.** The assay's denominator **is** nuclei (sibling § 3.2a), and cerebellar nuclei are overwhelmingly
granule (`PREMISE: DEFAULT_FROM_TEXTBOOK`; first-hand negatives `Purkinje` 0 / `granule` 0 in the 2026 body). And it
is **consistent with the observation that started this whole line**: the cerebellum's positive fraction is the
**highest** of three regions while its load is the **lowest**. Under `V ≈ F × C`, near-universal coverage at small
per-cell amounts is **exactly** what a many-small-cells compartment looks like — positivity is a **threshold**
measure, load is a **quantity**, and they do not conflict.
**Against.** 🔴 **Untested in every direction**, and it makes a prediction the field would find surprising — that
Purkinje cells are **well** transduced. It cannot explain the within-region dose behaviour, and it says nothing about
protein. ⚠️ It is also **not** the sibling file's H6: H6 is the **gap** (*"no existing measurement could tell"*);
P5 is a **directional bet** whose falsification the same experiment would deliver.
**Cheapest discriminating experiment.** 🎯 **Calbindin + WWOX — or calbindin + `AAV9-hSynI-EGFP`, which both
laboratories already own — on sections that already exist**, reporting **per-cell intensity distributions** for
Purkinje against granule cells **in the same field**. One antibody, existing material.
🎯 **And this is the reason to run it that H6 alone does not supply: P5 and a delivery-limited account predict
OPPOSITE Purkinje results from the SAME homogenate number.** H6 says nobody can tell; **P5 says which way it will go
and can be wrong.** One stain adjudicates, and this entire census exists because that stain has never been done.

### 7.1 Distinctness check

| | P1 receptor/glycan | P2 mitotic dilution *(carried)* | P3 CSF access | P4 DNA denominator | P5 composition |
|---|---|---|---|---|---|
| **Layer it acts at** | 1→2, **uptake per cell** | 2, **post-entry loss** | **1, arrival geometry** | **measurement of 2** | **2, as a weighted average** |
| Biological or measurement? | biological | biological | biological | 🔴 **measurement** | 🔴 **measurement + a cell-size rule** |
| Predicts low genomes **per exposed cell**? | **yes** | **yes** | no (low **exposure**, not low uptake) | no (apparent only) | **yes, for granule cells only** |
| Predicts a **within-cerebellum depth gradient**? | no | 🟡 layer-wise, by lineage | 🔴 **YES — pial-inward** | no | 🟡 by cell size, not depth |
| **Route-dependent?** | 🔴 **NO — invariant** | no | 🔴 **YES** | no | no |
| Predicts **Purkinje cells are well transduced**? | no | 🟡 yes (post-mitotic early) | 🔴 **no** (they sit deep to the molecular layer) | silent | 🔴 **YES, strongly** |
| Dies if a **host reference amplicon** leaves the ratio unchanged? | no | no | no | 🔴 **DIES** | no |
| Dies if **4 °C capsid binding per nucleus is equal**? | 🔴 **DIES** | no | no | no | no |
| Dies if an **integrating** vector shows the same deficit? | no | 🔴 **DIES** | no | no | no |
| Dies if **intracisternal delivery leaves the ratio unchanged**? | no | no | 🔴 **DIES** | no | no |
| Dies if **calbindin⁺ Purkinje load is LOW**? | no | 🟡 weakened | no | no | 🔴 **DIES** |

**Five mechanisms, five distinct falsifiers, and four cheap experiments that between them kill at least four of
them.** No two collapse onto the same measurement. **No winner is selected, because no discriminating evidence
exists.**

### 7.2 🎯 The ordering that falls out
1. **A single-copy host reference amplicon in the archived wells** (P4) — one primer pair, same plate, and it either
   confirms or destroys the strongest result in the sibling file. **Run this first**, because everything else is
   built on that number.
2. **Calbindin + WWOX / calbindin + EGFP on existing sections** (P5, and closes H6) — one antibody, existing
   material, and it is the measurement this whole census establishes nobody has made.
3. **4 °C capsid binding on acute cortical vs cerebellar slices** (P1) — wild-type only, no vector cohort.
4. **One cohort, two routes** (P3) and **episomal vs integrating reporter** (P2) — both need an animal cohort and
   both are therefore last.

---

## 8 · `REVIVAL_TRIGGER`s

| Blocked / unresolved item | Status | `REVIVAL_TRIGGER` |
|---|---|---|
| 🎯 **`PMID 16941225` body and cerebellar figure** — the primary behind the ONLY Purkinje-layer WWOX observation | 🔴 **`SOURCE_BLOCKED` by LICENCE.** `PMC4144810` → `full_text: ""`; `is_open_access: false`, `© Springer`. Third confirmation in this repository | **Any legitimate route to the body.** On opening, record: **donor age**, **antibody vendor/catalogue/clone**, whether a **cerebellar figure panel** exists, whether any **Purkinje soma is shown at magnification**, and whether **any counterstain or co-stain** was used. 🎯 **This is the single highest-value acquisition in this file.** Parked `HUMAN_REQUIRED` for an interlibrary route; **no external action taken** |
| 🎯 **`PMID 17470496` (Gribaa 2007) body** — whether SCAR12's *"mild cerebellar atrophy"* is in the primary, and in how many patients | 🔴 **`SOURCE_BLOCKED`. No PMCID at all**; `source: "not_available"` | **Any route to the body.** On opening, record: **how many patients were imaged**, whether **cerebellar atrophy** is reported and in **which compartment (vermis vs hemispheres)**, whether **atrophy or hypoplasia**, at **what age**, and how it sits beside the abstract's *"posterior white matter hyperintensities"*. Until then the claim is **`PREMISE: SECONDARY_UNVERIFIED`** and must not be relayed bare |
| **`PMID 24369382` (Mallaret 2014) body** — the SCAR12 genetics founder | 🔴 **PAYWALL**, unchanged; `PMC3914474` deposit not licensed | **Standing** (`wave7_verification_mallaret_chain_20260922.md`). 🎯 **This file adds a second item to record on opening: any cerebellar imaging, volumetry or neurological-examination detail for EITHER family, and any imaging at all for the `G372R` siblings** — for whom no imaging is reported anywhere I read |
| 🎯 **A human Purkinje-resolved WWOX value from an existing public dataset** | 🔴 `PREMISE: NOBODY_LOOKED` | **Query the Cheng 2025 cerebellar multiome** ([DOI](https://doi.org/10.1002/alz70855_105855), 103,861 nuclei, Purkinje and granule clusters separated) **for `WWOX`** — expression **and** locus accessibility per cerebellar cell type. On arrival, record cluster definitions, `n` nuclei per cluster, and whether Purkinje recovery is stated. ⚠️ It is a **conference abstract**: accession and data terms are `NOT STATED` |
| **Human Protein Atlas WWOX cerebellum cell-type annotation** | 🔴 **`SOURCE_BLOCKED` by the ALLOWLIST**, not the publisher (`example.com` control → 000) | **Any actor with egress:** read the HPA cerebellum IHC annotation for WWOX and record **which cell types are annotated, the antibody ID, and the reliability score**. Potentially a **second independent marker-era human Purkinje answer**, and it is one page |
| **DropViz / mousebrain.org / Allen atlas APIs** | 🔴 `SOURCE_BLOCKED` by the allowlist | On any route: read the **cerebellar cluster list** and record 🎯 **whether a Purkinje cluster exists in the atlas at all, and how many nuclei it contains** — which decides whether Aldaz's Purkinje silence is biological or a dissociation artefact (§ 3.1) |
| 🎯 **Purkinje-restricted `Wwox` conditional** | 🔴 **NOT REPORTED**, and the floxed allele **exists** (§ 2.4) | Any `Pcp2`/`L7`-Cre × `Wwox^fl/fl` cross, **or** any cerebellum-restricted `Wwox` ablation, in any publication or preprint. ⚠️ The Surface-A zero for Cre drivers is **`PREMISE: METHODS_INVISIBLE`** and must not be cited as evidence none exists |
| **Any `%NeuN⁺WWOX⁺` cerebellar figure met in future reading** | — | 🔴 **Standing, and it is a recording rule:** record it as **granule-lineage, Purkinje-EXCLUDED**, whatever the number. `MAB377` = clone A60 |
| **Any calbindin / PCP2 / Car8 co-stain with WWOX or a vector reporter** | 🔴 `PREMISE: NOBODY_LOOKED` | Standing from the sibling file. 🎯 **This file adds what to report when it arrives: the full per-cell intensity DISTRIBUTION for Purkinje and granule cells separately, and the positive fraction separately from the intensity** — because P5 and a delivery-limited account predict opposite answers from the same section |
| 🔴 **WOREE vermis hypoplasia stated as *"most cases"*** in `discovery_ledger_current.md` L554 / `FTR-20260921-35573960-01` | 🔴 **NOT SUPPORTABLE** — a 101-patient collation puts it at **2 patients, 1 study**, *"less specific"* (§ 4.4) | **Flagged, not edited.** Any actor authorised to touch the discovery ledger should reconcile that line against `PMID 38161429` Table 1. No registry, ledger, queue or receipt was modified by me |
| **SCAR12 patient count: 6 or 8?** | 🔴 **NOT ADJUDICATED** | Mignot 2014 (`PMID 25411445`) abstract, first-hand: *"reported in **eight individuals of two families**"*; Aldaz 2020 describes **4 + 2 = 6**; Banne 2021 (repo-attested) counts **6 SCAR12**. Same two families, two counts. Resolve on opening either founder's body |
| **GTEx frontal-cortex value 6.9 vs local 6.82/6.85** | ⚠️ minor, unresolved | Any GTEx release/version statement for the figure in `PMID 33255508`. Does not affect the cerebellar entry, which matches exactly (§ 3.3) |
| **Chen 2004 (`PMID 15026124`) adult mouse region list omits cerebellum** | ⚠️ **NOT ADJUDICATED**; no PMCID, body not retrievable | On any route: record whether cerebellum was examined and with what result. It is the one restatement in this census that does not obviously agree with the human/GTEx picture |

---

## 9 · What I could not establish

1. 🔴 **Whether WWOX has ever been measured in an identified Purkinje CELL.** The single existing observation is
   **layer-based and marker-free**, and the Purkinje cell layer also contains Bergmann glia and candelabrum somata.
   **`NOT ASSAYED` — which is neither `NORMAL` nor `ABSENT`.**
2. 🔴 **Whether that observation's primary source shows a Purkinje soma at all.** `PMID 16941225`'s body is
   licence-blocked; I have only a review's restatement with the **citation marker stripped**, and my attribution of
   the primary is an **`INFERENZA` from four converging descriptors**, not a read citation.
3. 🔴 **Any quantitative Purkinje WWOX value, in any species.** The one existing statement is the word **"robust"** —
   no intensity, no per-cell distribution, no positive fraction, no `n`, no statistic, no comparator quantity.
4. 🔴 **Whether Purkinje cells appear in DropViz's cerebellar cluster set at all.** The review reports the **top**
   clusters; a cluster that is absent from a top-N list and a cluster that does not exist in the atlas are different
   facts, and I cannot separate them without the atlas (blocked, § 1.4). **The Drop-seq large-neuron recovery concern
   is my hypothesis, not a fact — I did not read Saunders 2018.**
5. 🔴 **Whether SCAR12's *"mild cerebellar atrophy"* is in Gribaa 2007's Results, and in how many patients.** The
   review says two children and cerebellar atrophy; the primary abstract says one patient and posterior white-matter
   hyperintensities. Both divergences stand unresolved and the primary has **no PMCID**.
6. 🔴 **Any cerebellar imaging for the `G372R` SCAR12 family.** Not reported in anything I read. `NOT REPORTED`.
7. 🔴 **Vermis versus hemispheres, and atrophy versus hypoplasia, in SCAR12.** The single line names neither
   compartment. In the **WOREE** pole the finding is consistently **vermian** and **hypoplastic**; in **SCAR12** it is
   *"cerebellar atrophy"* with no compartment. **The two poles are not on a common imaging axis and must not be
   differenced.**
8. 🔴 **Whether an unpublished Purkinje-restricted `Wwox` conditional exists.** The allele exists and the authors named
   the missing cross in 2020; publication status is all I can read. **Parked `HUMAN_REQUIRED`; no correspondence
   attempted or recommended as an action of mine.**
9. 🔴 **Which column Table 1's `2:2` vermis value belongs to** in `PMID 38161429`. The linearisation drops blanks, so
   the assignment to Iacomino rests on **prose plus that cohort's `n = 2`**, not on the table's geometry.
10. 🔴 **Whether any cerebellar WWOX measurement exists in a WWOX-DEFICIENT cerebellum at cell-type resolution.**
    Every cell-type-resolved WWOX dataset in § 3.1 is **wild type**. The only cell-type-resolved measurements in a
    mutant (`PMID 36828035`, `PMID 32000863`) measure **cell number**, not WWOX.
11. 🔴 **The SCAR12 patient count** — 6 or 8, same two families.
12. 🔴 **Whether Chen 2004's adult-mouse regional list genuinely omits cerebellum** or whether the review's
    restatement compressed it.
13. ⚠️ **Nothing about the Cheng 2025 dataset's availability.** Accession, terms of use, Purkinje nucleus count and
    cluster definitions are all `NOT STATED` in a conference abstract. The "one query away" claim is about the
    **design** of that dataset, not a verified fact about my access to it.
14. ⚠️ **No hypothesis in § 7 is discriminated.** Five mechanisms, five falsifiers, **zero discriminating evidence in
    hand.** No winner is selected and no probability is attached to any of them.

---

## Summary for the orchestrator

- 🎯 **Purkinje WWOX has been measured ONCE, and only as a LAYER.** `PMID 33255508` § 2, first-hand:
  *"robust WWOX protein expression in soma from cells of all three layers of human cerebellar cortex viz.,
  **Purkinje cell layer**, molecular layer, and granular layer."* Human, protein, IHC. 🔴 **No marker — no calbindin,
  no PCP2, no Car8, no parvalbumin** — so it identifies a layer that also contains Bergmann glia and candelabrum
  somata, not a cell. Qualitative (*"robust"*), age `NOT STATED`, and the **primary body (`PMID 16941225`) is
  licence-blocked**, reproduced by me today.
- 🔴 **NEW TO THIS REPOSITORY, and it is a propagation defect.** `Purkinje cell layer` occurs **zero times anywhere at
  `HEAD`**. `PMID 33255508` was read as a `complete_fulltext_read` on 2026-08-06 with **four locators**, landing on
  the myelin axis. Three independent downstream sources — **including that paper's own abstract and conclusions** —
  transmit its cell-type statement as *"basket cells and granule cells"* and **drop the Purkinje layer**; one
  (You 2024) garbles it into *"granulosa cells"*, an ovarian cell type. **That is how "WWOX in the cerebellum" became
  a statement with no Purkinje cell in it.**
- 🎯 **Cerebellar cell-type resolution exists in exactly one dataset, and Purkinje cells are not in it.** DropViz
  (mouse, adult): top clusters **`Pvalb`⁺ interneurons** and **`Gabra6`⁺ granule cells**; on sub-clustering,
  *"GABAergic basket cells and, to lesser extent, granular neurons."* 🔴 **A Purkinje cluster is not reported in
  either direction** — `NOT ASSAYED`, with a named `DETECTION_FLOOR`-class reason (Drop-seq recovers very large
  neurons poorly). Allen ISH: cerebellum visible, **no layer or cell type**. GTEx and HBT: **region only**.
- 🔴 **The two `WWOX AND Purkinje` hits measure Purkinje NUMBER, not WWOX.** `PMID 36828035` uses **calbindin as a
  counting reagent** (median ≈82→≈25 at 80 d, ≈100→≈42 at 250 d, `n=3`, survivor selection flagged) with **`Hcn1`⁺
  basket cells `ns` at both ages**; `PMID 32000863` uses cresyl violet. **A cell count is not a protein measurement** —
  the same category error as collapsing positivity into load, one level up.
- 🎯 **SCAR12 supplies LESS cerebellar cell-type evidence than WOREE, not more.** Two families, six patients, **zero
  neuropathology, zero post-mortem, zero cell-type observation** (verified zero, positive controls firing; and the
  patients are **alive at 17–26 years**, so no autopsy exists to find). One imaging line only —
  *"mild cerebellar atrophy … in MRI of two affected children"* — and 🔴 **its primary abstract says ONE patient and
  POSTERIOR WHITE MATTER HYPERINTENSITIES.** `PREMISE: SECONDARY_UNVERIFIED`; Gribaa 2007 has **no PMCID**.
  No imaging at all for `G372R`. Its only tissue assay is **patient fibroblasts**; its only biopsy is **muscle**.
- 🎯 **The pole's real contribution is an allele irony:** the only calbindin-resolved cerebellar cell-type data in the
  whole literature sit on **the SCAR12 allele** — `Wwox^P47T/P47T` in a **mouse** — where **protein level is normal**
  and Purkinje cells are nonetheless lost. Three firewalls travel with it: species, allele, and number-versus-amount.
- 🔴 **A held statement narrowed (flagged, not edited).** `discovery_ledger_current.md` L554 carries WOREE vermis
  hypoplasia as *"described in most cases"*. A **101-patient** systematic collation (`PMID 38161429` Table 1,
  eyeballed) puts it at **2 patients from 1 study**, calls it *"less specific"*, and records one five-patient cohort
  in which *"the cerebellum was not affected"*. **"Most cases" is not supportable.**
- 🟢 **Exactly one cerebellar WWOX measurement is free of the clone-A60 confound AND able to see a Purkinje cell** —
  the human layer-resolved IHC. Every other A60-free cerebellar measurement is free of it **because it has no
  cell-identity channel at all**, which is not an answer.
- 🎯 **The nearest existing thing, and one step: a human cerebellar snRNA-seq + snATAC-seq multiome of 103,861 nuclei
  with Purkinje and granule clusters already separated** (Cheng 2025, [DOI](https://doi.org/10.1002/alz70855_105855)).
  **Query it for `WWOX`.** Zero wet work, zero reagent, zero animal — and it also returns **locus accessibility per
  cerebellar cell type**, which nothing else in this census can. ⚠️ Conference abstract; accession `NOT STATED`; AD
  post-mortem tissue, not WWOX disease. Runner-up **`PMID 16941225`** is cheaper in principle and **licence-blocked**.
- 🎯 **And the step that changes the biology, which the authors themselves named in 2020: the `Wwox` floxed exon-1
  allele EXISTS** (first-hand, § 3.3 of that review), and its makers wrote *"targeted CNS ablation using promoters
  driving Cre recombinase to specific mouse brain regions such as **the cerebellum** … will be highly informative."*
  **Cross it to `Pcp2`/`L7`-Cre.** Six years on, still unreported. ⚠️ The PubMed zero for Cre drivers is
  **`PREMISE: METHODS_INVISIBLE`**, not evidence of absence.
- 🎯 **Five distinct hypotheses for the per-nucleus vDNA deficit, no winner, no probabilities.** **P1** AAV9
  galactose/receptor availability (route-**invariant**) · **P2** mitotic dilution *(carried from the sibling file, plus
  a new age-series-free falsifier: an **integrating** reporter alongside the episomal one)* · **P3** CSF-route access
  (route-**dependent**, predicts a **pial-inward depth gradient**) · **P4 (NEW)** the **DNA denominator itself** — "50 ng
  ⇒ fixed nuclei" is **estimated, never measured**, and the assay lacks the one control that would test it ·
  **P5 (NEW)** **composition**, under which there is **no cerebellum-specific biology at all** and **Purkinje cells are
  predicted to be WELL transduced.**
- ⚡ **Run in this order:** (1) **a single-copy host reference amplicon in the archived qPCR wells** — one primer pair,
  same plate, and it either confirms or destroys the strongest result in the sibling file; (2) **calbindin + WWOX (or
  calbindin + the `AAV9-hSynI-EGFP` both laboratories already own) on existing sections**, reporting the per-cell
  intensity **distribution** — because **P5 and a delivery-limited account predict OPPOSITE Purkinje results from the
  same section**, which makes the stain informative rather than merely completing; (3) 4 °C capsid binding on acute
  slices; (4) the two cohort experiments.
- 🔴 **Tool traps caught live and documented:** failure mode **(a)** — `WWOX AND (Gly372Arg OR G372R)` returned the
  **raw query as its own translation** and 0 hits ⇒ **discarded**; failure mode **(f)** — a **six-term OR block came
  back as four**, with `Gly372Arg` and `G372R` **silently dropped** and both cDNA terms mangled by punctuation, with
  no error reported; failure mode **(e)** — a Cre-driver query returned 0 with a **flawless translation**, and the
  repository's own `CLAIM 037` proves such mice exist. **`example.com` control → HTTP 000**, so every non-MCP route
  is allowlist-blocked. **20/20 full-text passages single-sided with 146 `Purkinje` and 87 `WWOX` tokens present** —
  a controlled negative, counted by script.
- ✅ **No registry, queue, ledger, receipt or canonical file was edited. No `BATCH_COMMIT`. No git command was run.
  No external human action, no correspondence, no material request. This file is the only output.**

*End of file. Complete run.*

---

## 12 · ORCHESTRATOR VERIFICATION — added 2026-09-22 after hand-back

### 12.1 🟢 The propagation defect is CONFIRMED, and the abstract diagnoses its mechanism

Verified independently:

| check | result |
|---|---|
| `git grep -c -i "purkinje cell layer" HEAD -- disease-models/` | **0 — whole tree** |
| positive control: files containing `Purkinje` | **31** |
| `PMID 33255508` on record as `complete_fulltext_read` with 4 locators | ✅ |

🎯 **And the mechanism is visible in the paper's own abstract, which I retrieved directly.** According
to PubMed, Aldaz & Hussain 2020 (*Int J Mol Sci* 21:8922,
[DOI](https://doi.org/10.3390/ijms21238922)) says, verbatim:

> *"…single-cell RNA-seq data which indicate that neurons from the medial entorhinal cortex, Layer 5
> from the frontal cortex as well as **GABAergic basket cells and granule cells from cerebellar
> cortex** are the specific neuronal subtypes that display the highest expression levels."*
> *"Higher expression in **interneurons and granule cells** from cerebellum points to a direct link to
> the described cerebellar ataxia…"*

**No Purkinje cell appears anywhere in that abstract.** So the defect is not carelessness — it is a
**modality substitution**:

| | measurement | species | modality | cerebellar cell types named |
|---|---|---|---|---|
| **abstract** | scRNA-seq (DropViz) | **mouse** | **transcript** | basket + granule |
| **body § 2** | IHC, anti-WWOX polyclonal | **human** | **protein** | **all three layers, incl. Purkinje cell layer** |

> 🔴 **Two different measurements, and only the transcript one propagated.** Everything downstream
> inherited the abstract's mouse-transcript summary as though it were the whole cerebellar story —
> which is how *"WWOX in the cerebellum"* became a statement with **no Purkinje cell in it**, and how
> a further step garbled `granule` into `granulosa` (an ovarian cell type).

⚠️ **The recovered observation is thin and must not be overstated.** It is **layer-level, not
cell-level** — the Purkinje cell layer also contains Bergmann glia and candelabrum somata — with
**no marker**, **no stated age**, and a quantity that is the word *"robust"*. Its primary
(`PMID 16941225`) is **licence-blocked**, third confirmation. **So the honest state is: one
human protein observation, at layer resolution, from a secondary — not a Purkinje measurement.**

### 12.2 🟢 The GTEx entry question is closed, in favour of the hemisphere entry

§ 11.1 of the sibling file asked which cerebellar entry the `1.77×`/`2.17×` ratios require. **Answered
by the primary's own stated values**: Aldaz's `12.1 / 6.2 / 5.6` match the local CSV at
`Brain_Cerebellar_Hemisphere` **12.1278**, `Brain_Amygdala` **6.16809**, `Brain_Hippocampus`
**5.58518**. ⇒ **the source uses the cerebellar-hemisphere entry (12.1), not `Brain_Cerebellum`
(11.2)**, and `2.172` reproduces exactly. My precision point is resolved — **in favour of the
hemisphere reading.** ⚠️ One value does not reconcile (`6.9` vs local `6.82`/`6.85`), recorded. 🔴 **The
human-RNA-versus-mouse-protein bound is unchanged and still governs.**

### 12.3 🎯 The allele irony is the most therapeutically consequential line in this file

> **The only calbindin-resolved cerebellar cell-type data in the entire WWOX literature sit on the
> SCAR12 allele — `Wwox^P47T/P47T`, in a MOUSE — where WWOX protein level is NORMAL and Purkinje
> cells are lost anyway** (medians ≈82→≈25 at 80 d; ≈100→≈42 at 250 d; `n = 3`; `Hcn1`⁺ basket cells
> `ns` at both ages; survivor selection carried).

**Purkinje loss with normal protein abundance.** If that transfers, then Purkinje degeneration is
**not an abundance problem**, and **no amount of raising WWOX would address it** — which bears
directly on the reopened upregulation axis and on what `TX-007` can be expected to rescue.

🔴 **Three firewalls travel with it and none may be dropped:** **species** (mouse, not human),
**allele** (`P47T` is the SCAR12 pole, not the reference genotype), and **number-versus-amount** (a
**cell count** is not a protein measurement — the same category error as collapsing positivity into
load, one level up). `IPOTESI`, and it is queued as a hypothesis, not a finding.

### 12.4 The run order I endorse, and why

F's ordering is right and the reason is worth stating: **the single-copy host reference amplicon in
the archived qPCR wells comes first** — one primer pair, same plate — because it **confirms or
destroys the strongest result in the sibling file** (the per-nucleus reading), and no other experiment
is worth designing on top of a denominator that has not been tested. F's **P4** is the hypothesis that
the *"50 ng ⇒ fixed nuclei"* assumption is **estimated, never measured**, and that is the escape the
sibling file's own H5 explicitly could not reach.

🟢 **Second: calbindin + WWOX, and calbindin + `AAV9-hSynI-EGFP`, on existing sections**, read as a
**per-cell intensity distribution** — because **F's P5 (composition, no cerebellum-specific biology,
Purkinje cells predicted WELL transduced) and a delivery-limited account predict OPPOSITE Purkinje
results from the same section.** That is what makes the stain informative rather than gap-filling.
