# WWOX missense protein-abundance census — *what was in the lysate that was loaded?*

**Actor:** Scientist L · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** NON-CANONICAL ANALYSIS. This file touches no `*_current.md`, no registry, no queue, no
ledger, no receipt chain and no state manifest. No `BATCH_COMMIT` was run. No external action was
taken and nobody was contacted — contact, purchase and any external commitment are `HUMAN_REQUIRED`.
**Nothing here is medical advice.** No molecule, dose, route or clinical recommendation appears below.
**Alleles are never pooled.** Each row is one measurement on one allele in one system.

> **The question this file asks, and the one it does not.**
> It does **not** ask *"is there WWOX protein?"* — [`wwox_missense_stability_census_20260922.md`](wwox_missense_stability_census_20260922.md)
> (Scientist S, today) already enumerated every WWOX missense variant with any protein-level
> measurement and found six. This file asks the strictly narrower, strictly methodological question
> that sits underneath every one of those six:
>
> 🔴 **A Western blot reading "protein absent" is a statement about the lysate that was loaded, not
> about the cell.** An aggregation-prone variant partitions into the insoluble pellet; a mild
> non-denaturing lysis (NP-40, Triton, digitonin) discards that pellet at the clearing spin, before
> the gel is loaded. In that case *"absent"* means *"absent from the soluble fraction"* and the
> protein may be entirely present.
>
> So: **for every published WWOX-missense protein-abundance measurement, what buffer, what fraction,
> what antibody epitope, what loading, what detection floor — and can "degraded" be told from
> "insoluble" as run?**

**Read depth per row.** `full-text` = served body read in this act · `abstract-depth` = PubMed
metadata only, carries `PREMISE: UNREAD_PRIMARY` · `repo-held` = verbatim already in this repository.
Source of bibliographic records and served bodies: **PubMed / PMC** (DOI links per row); one
publisher-side passage retrieval via **Scholar Gateway**.

**Extraction-damage notice, applied throughout.** Every served body below reached me through PMC
text extraction, which in this corpus silently deletes superscripts, subscripts, variant labels and
reference callouts, and leaves empty parentheses where a token was removed. Where I restore a
deleted token I mark it `[restored]` and say what the raw string was. E-notation is used for every
exponent. A case-sensitive false negative is assumed possible for every string count.

---

## 0 · VERDICT UP FRONT

> ## **Twelve measurements. Zero can tell "degraded" from "insoluble" as run. One partially escapes, and it is not a blot.**

- **Zero** WWOX missense measurement, in any system, ever examined a pellet, an insoluble fraction,
  or ran a soluble/insoluble split. The strings `pellet`, `insoluble` and `fraction` return **0**
  in the served body of the one paper with the deepest turnover work (Zhang 2025).
- **Zero** rows state an antibody **epitope position relative to the variant**. Not "few" — none.
- **Zero** rows state a detection sensitivity floor, a limit of detection, or a dilution series.
- **Two** rows state a numeric loading amount.
- **Four** of the eight papers that attempted a WWOX-missense protein measurement state a lysis
  buffer at all; in **four** it is invisible or absent — two of those four because the body is
  closed to this deployment, two because the authors simply did not write one down.
- The one measurement that partially escapes the trap is **immunofluorescence on fixed organoid
  sections** (`G372R`, Steinberg 2021) — because nothing is discarded at a clearing spin when
  nothing is lysed. It escapes the *lysis-loss* artefact and **not** the *epitope-masking* artefact,
  and its antibody is undistributed.

🔴 **The consequence for `DL-MECH-029` is not the one I expected, and §3 states it at the strength
the evidence allows rather than at the strength that would be dramatic: the reference genotype's
"functionally null/null" inference does NOT weaken. What weakens is the narrower molecular claim
that carries Johannsen's own title — "complete loss of WWOX protein" — and the census opens a
fourth branch the ledger does not name, in which the reference genotype would be *worse* than
functionally null rather than better.**

---

## 1 · The census

Each row is one measurement. Verbatim strings are quoted exactly as the served body renders them,
with `[restored]` marking a token I put back after extraction deleted it.

### 1.1 The table

| # | allele | system | lysis buffer and detergent, **verbatim** | denaturing or native | soluble/insoluble or pellet fraction examined? | antibody and **epitope position relative to the variant** | loading | detection + stated sensitivity floor | reported result | **can "absent" be told from "insoluble" AS RUN?** |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | `Q230P` (p.Gln230Pro, c.689A>C) | donor-derived **patient fibroblasts**, two homozygous sisters | 🔴 **`PREMISE: METHODS_INVISIBLE`** — Springer-closed; PMC holds no body; two retrieval attempts logged in §1.3 | **UNSTATED** | 🔴 **UNSTATED — and no sentence anywhere in the served surface mentions a fraction** | **UNSTATED** — no vendor, no catalogue, no immunogen, no epitope | **UNSTATED** | **UNSTATED** | *"Functional studies showed normal levels of WWOX transcripts but **absence of WWOX protein**"* (abstract, `abstract-depth`) | 🔴 **NO — and not even weakly. Nothing about the loaded lysate is knowable.** |
| **2** | `Q230P` | 🆕 **HEK293 cells** — existence inferred, content unknown | `PREMISE: METHODS_INVISIBLE` | UNSTATED | UNSTATED | UNSTATED | UNSTATED | UNSTATED | 🔴 **UNKNOWN — the abstract describes no HEK293 experiment.** See §1.4: the PubMed record carries the MeSH descriptor **`HEK293 Cells`**, so a heterologous-expression arm very probably exists in the closed body and **is not in the abstract this repository has been reasoning from.** `INFERENZA`, tagged with `FM-009` | — | 🔴 **NO — the experiment itself is invisible.** |
| **3** | `Q230P` | second, independent family — 4 homozygous `c.517-2A>G` + **2 compound het `c.517-2A>G / Q230P`**, Yemenite Jewish ancestry | — | — | — | — | — | — | 🔴 **NO PROTEIN MEASUREMENT AT ALL.** cDNA sequencing only (*"causes skipping of exon six"*). `abstract-depth`, `PREMISE: NOBODY_LOOKED` | 🔴 **N/A — nobody looked.** The only second `Q230P` cohort in existence ran no blot. |
| **4** | `P47T` (p.Pro47Thr, c.139C>A) | **patient fibroblasts**, passages 10/13/14 vs 4 controls | 🔴 **`PREMISE: METHODS_INVISIBLE`** — `get_full_text_article(["PMC3914474"])` returns `full_text: ""`; Europe PMC and publisher egress are blocked in this deployment; the Wiley-side passage corpus does not hold this OUP title (§1.3) | UNSTATED | **UNSTATED** | **UNSTATED** | **UNSTATED** | **UNSTATED** | *"similar amounts of the mutant and wild-type WWOX protein"*; *"the mutation does not alter global protein levels"* (`repo-held`) | 🔴 **NO.** ⚠️ And note the asymmetry: for a **normal** result the insolubility trap is far less dangerous — a protein you *can* see in the soluble fraction is soluble. This row is the one place where buffer-blindness costs least. |
| **5** | `G372R` (p.Gly372Arg, c.1114G>C) | same paper, same matrix — **does a `G372R` blot even exist?** | `PREMISE: METHODS_INVISIBLE` | — | — | — | — | — | 🔴 **UNRESOLVED.** The repository's held verbatim from this body documents a fibroblast Western **for `P47T` only**. A 2020 review sentence asserting *"both described missense mutations do not alter WWOX protein expression"* is **a review sentence, not a measurement**, and the same review calls `G372R`'s consequence *"unclear at this point"* | **N/A — existence unverified.** |
| **6** | `P47T` | **`Wwox^P47T/P47T` knock-in mouse cerebellum (CB)**, n=2/group | 🟢 **STATED, verbatim:** *"washed using lysis buffer (25 mM Tris-HCl pH 7.4, 150 mM NaCl, 1 mM EDTA, **1% NP-40**[restored: raw text reads `1% NP-40%`] and 5% glycerol with protease inhibitor cocktail)"* | 🔴 **NATIVE / MILD NON-DENATURING.** No SDS, no deoxycholate, no urea | 🔴 **NO.** `pellet` **0**, `insoluble` **0** in the served body. A clearing spin is not described; a bead pull-down in practice requires one — `INFERENZA`, not `DATO` | *"1:1000 dilution of **rabbit anti-Wwox**"* — 🔴 no vendor, no catalogue, no immunogen. **Epitope `UNSTATED`.** `P47` sits in **WW1 (aa ~16–50)**, the extreme N-terminus, so an antibody raised on a C-terminal SDR immunogen would be blind to an N-terminal truncation and fully sighted on the variant itself | *"CB lysate (**100 μg, 10%**) was used as input"* | *"analyzed by western blotting"*; 🔴 **detection chemistry never stated** (`ECL` **0** in the body). **No floor.** | *"**Western blot analyses also showed similar levels of Wwox protein expression** in homozygous mutant and wildtype mice (see, **Wwox 10% input panel**)"* | 🔴 **NO.** ⚠️ Compounded: this is the **input lane of a pull-down**, not a dedicated quantified blot, n=2/group — the bound already recorded on this repository's own receipt. |
| **7** | `G372R` | **forebrain organoids**, ventricular zone; n=2 affected homozygotes vs n=2 heterozygous parents, same family | **N/A — no lysis.** Fixed sections. Verbatim: *"sections were warmed to room temperature and washed in PBS for rehydration, **permeabilized in 0.1% Triton X-100 in PBS (PBT)**"* | **N/A (fixed, permeabilised)** | 🟡 **N/A — nothing is discarded, because nothing is cleared.** ⚠️ Note separately that this paper *does* fractionate — *"organoids were grinded in a **hypotonic lysis buffer** … then **0.5% NP-40** was added … After centrifugation, the **cytoplasmic fraction** was collected. Afterwards, **nuclear fraction** was obtained by incubating remaining pellet in a hypertonic nuclear extraction buffer"* — but that is **cytoplasmic/nuclear on the KO lines, not soluble/insoluble on the missense**, and a hypertonic-KCl nuclear extract is not an insoluble-fraction step. Its total-protein buffer is *"50 mM Tris (pH 7.5), 150 mM NaCl, 10% glycerol, and **0.5% Nonidet P-40 (NP-40)**"* — mild, non-denaturing | 🔴 **UNSTATED in the distributed body** — the antibody table is an appendix PMC does not distribute, and the citation callout was deleted by extraction (`Table` with an empty reference). **Epitope `UNSTATED`.** | **N/A** (IF) | Confocal IF. 🔴 **Not quantified** — no densitometry, no intensity ratio, no statistic, no floor | *"while in the VZ of WPM F2 and WPM M3, WWOX was detected, **barely any signal was observed in WPM D1 and S1**"* | 🟡 **PARTIALLY — the only row that escapes anything.** It excludes the **lysis-loss** artefact, because an aggregate stays in a fixed cell. It does **not** exclude **epitope masking** inside a dense aggregate, 0.1% Triton is a light permeabilisation, **no antigen-retrieval step is described**, and the antibody is unknown. And its comparator arm is itself a **carrier genotype**. |
| **8** | `A141T` (p.Ala141Thr, c.421G>A) | human **total cell lysate** (DNA came from peripheral blood; the WB source is never named), proband + **homozygous father** | 🔴 **UNSTATED — and this is an authored omission, not a retrieval failure.** The entire preparation is one clause: *"**After preparing the total cell lysate**, protein concentrations were determined using a Qubit device"*. No buffer, no detergent, no spin, no speed | 🟡 **AMBIGUOUS.** The *sample* was denatured — *"denatured with SDS-sample buffer by heating at 95 ºC for 5 min"* — but denaturing the **supernatant** of an unstated lysis does not recover a pellet already discarded | 🔴 **NO.** The words pellet / insoluble / fraction do not occur | 🟢 **NAMED:** *"WWOX protein was detected using the **WWOX Protein Antibody (CST 4045S)**"*, β-actin (13E5) as loading control. 🔴 **Epitope `UNSTATED` in the paper**, and the vendor datasheet is **unreachable from this deployment** (egress to `cellsignal.com` blocked) — recorded as `PREMISE: REAGENT_EPITOPE_UNVERIFIABLE_HERE`, never guessed | 🔴 *"equal amounts of protein (µg/mL) from each sample"* — **a damaged/vacuous statement**: the empty parenthetical is where the number was, and `µg/mL` is a concentration, not a load | *"chemiluminescent imaging was performed using the **Pierce kit**"*, C-DiGit scanner. **No floor.** | *"Western blot analysis revealed **significantly reduced** WWOX protein levels in both the proband and the father compared to healthy controls"* — 🔴 *"significantly"* with **no test, no densitometry, no error bar, no replicate count, and the number of WB controls never stated** | 🔴 **NO.** Closest of any row to escaping — an SDS-boiled sample — and it still fails, because what was boiled is the product of an unwritten lysis. |
| **9** | `P252A` (p.Pro252Ala, c.754C>G) · 🔴 **ClinVar `Benign`**, multiple submitters | **CAL-62** anaplastic thyroid carcinoma + BCPAP, **CMV-driven Flag transgene**, stable | 🟢 **STATED, verbatim:** *"cells were lysed in lysis buffer (50 mM[restored] Tris-HCl pH 7.5, **1% NP-40, 0.1% SDS, 0.5% sodium deoxycholate**, 0.15 M[restored] NaCl, 50 mM[restored] NaF, 1 mM[restored] EDTA, 1 mM[restored] Na₃VO₄[restored: raw `NaVO`], 1 mM[restored] DTT) with protease inhibitor … for 30 min on ice. **Protein lysis was collected by centrifugation at 13300 × rpm for 10 min at 4 °C**"* | 🟡 **RIPA-EQUIVALENT — intermediate stringency, NOT denaturing.** 0.1% SDS + 0.5% DOC solubilises more than plain NP-40 and **does not solubilise detergent-resistant aggregate**. See §2.4 | 🔴 **NO — and this is the strongest verified zero in the census.** In the served body: `pellet` **0**, `fraction` **0**, `insoluble` **0**. *"collected by centrifugation"* is the supernatant; **the pellet was discarded and never named** | 🟢 *"Anti-FLAG antibody (**clone M2**, #F1804)"* — 🔴 **the epitope is the TAG, not WWOX.** That cuts both ways and §2.3 works it out. Tag terminus: *"cloned into **pCMV-3Tag** expression vector (#240195, Agilent)"* — the 3Tag family has both N- and C-terminal members and **the paper does not say which**, so the tag's position relative to P252 is `UNSTATED`. A second reagent exists — *"Anti-WWOX antibody (#ab238144)"* — with **epitope `UNSTATED`** and no stated assignment to the mutant panels | 🟢 *"**20 µg of protein samples** were separated on SDS-PAGE"* | *"Blots were developed by using the **chemiluminescence system (NcmECL Ultra)**"*. **No floor, no dilution series, no linear-range statement** | *"the WWOX^P252A^ mutant exhibited **significantly enhanced protein degradation**"*; MG-132 20 µM/6 h **negative**; CQ 40 µM/24 h and NH₄Cl 250 µM/24 h **restore**; 3-MA 10 mM/12 h negative; HSC70 co-IP positive; LAMP1 colocalisation; K63-polyUb. 🔴 The **t½ was never reported** | 🔴 **NO.** ⚠️ And here the failure is *expensive*, because this is the only turnover dataset in the gene: **a CHX chase read on a cleared lysate cannot distinguish "cleared faster" from "partitions into the pellet faster".** CQ rescue narrows it — a lysosomal inhibitor restoring a **soluble** band is hard to explain by pure aggregation — but does not close it. |
| **10** | `P282A` (p.Pro282Ala, c.844C>G) · 🔴 **`OVEREXPRESSION-ARTEFACT SUSPECT` — rs3764340, ClinVar `Benign`, 18 healthy homozygous controls; MUST NOT be used as a simple complete-loss control** | same paper, same lines, same transgene | **identical to row 9** | **identical** | 🔴 **NO — identical zero** | **identical** | **20 µg** | **identical, no floor** | **Stability normal — a NEGATIVE stability result with the positive control (P252A) in the same figure** — and function abolished (no POLE4 binding, no growth or invasion suppression) | 🟡 **NO — but the direction of the error is harmless here.** A *normal* soluble band cannot be an insolubility artefact. What this row **cannot** support is its most quoted use: it is a **benign polymorphism on a CMV transgene in thyroid carcinoma**, and it is **not** a complete-loss control for anything. |
| **11** | `W44F/P47A` — 🔴 **DESIGNED, not a disease allele** (WW1-ablating double substitution) | MDA-MB-231, doxycycline-inducible full-length; also GST-fusion fragments in HEK293T | 🟢 **STATED, verbatim:** *"cells were lysed with **RIPA buffer (TFS …)** supplemented with Halt Protease Cocktail Inhibitors … or when detecting Brca1, and lysed with **low salt NP40 buffer** as described"* — 🔴 the composition is **outsourced to a catalogue number and a citation**, so the actual SDS/DOC percentages are not in the paper | 🟡 RIPA-class / mild NP-40 for the co-IP arm | 🔴 **NO** | *"Wwox"* antisera **cited by reference number only** — the callout was deleted by extraction. **Epitope `UNSTATED`** | 🔴 *"Approximately **20 μg of antisera**"* is the **antibody** amount for co-IP; the **lysate load for the immunoblot is never stated** | 🔴 **UNSTATED** | The blot *"demonstrates the **inducibility** of Wwox expression in these cell lines"* — i.e. an abundance readout on designed missense constructs, used only as an expression control | 🔴 **NO** |
| **12** | `Y293F` — 🔴 **DESIGNED, not a disease allele** (conservative, catalysis-abolishing **by design**, fold-preserving by intent) | same | **identical to row 11** | identical | 🔴 **NO** | identical, **epitope `UNSTATED`** | **UNSTATED** | **UNSTATED** | Same inducibility blot. Functionally: *"the SDR mutant Wwox-expressing cells **are sensitive to radiation** because they retain a WW1 domain"* | 🔴 **NO** — and note it cannot serve as a fold-intact control either, because **no protein level, stability or localisation was measured** for it. |

**Sources, with DOIs.** According to PubMed: row 1–2 Johannsen J *et al.*, *Neurogenetics* 2018;19(3):151-156, PMID 29808465, [DOI](https://doi.org/10.1007/s10048-018-0549-5) · row 3 Weisz-Hubshman M *et al.*, *Eur J Paediatr Neurol* 2019;23(3):418-426, PMID 30853297, [DOI](https://doi.org/10.1016/j.ejpn.2019.02.003) · rows 4–5 Mallaret M *et al.*, *Brain* 2014;137(2):411-419, PMID 24369382, PMC3914474, [DOI](https://doi.org/10.1093/brain/awt338) · row 6 Hussain T *et al.*, *Prog Neurobiol* 2023;227:102425, PMID 36828035, PMC10835625, [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425) · row 7 Steinberg DJ *et al.*, *EMBO Mol Med* 2021;13(8):e13610, PMID 34268881, PMC8350905, [DOI](https://doi.org/10.15252/emmm.202013610) · row 8 Öngen YD *et al.*, *Reprod Sci* 2026;33(5):1020-1025, PMID 42082822, PMC13230315, [DOI](https://doi.org/10.1007/s43032-026-02112-9) · rows 9–10 Zhang X *et al.*, *Adv Sci* 2025;13(1):e07602, PMID 41124647, PMC12767083, [DOI](https://doi.org/10.1002/advs.202507602) · rows 11–12 Schrock MS *et al.*, *Oncogene* 2017;36(16):2215-2227, PMID 27869163, PMC5398941, [DOI](https://doi.org/10.1038/onc.2016.389). Scholar Gateway · publisher-side passage retrieval · 2 queries · 18 passages · 16 articles.

### 1.2 The counts the brief asked for

| Count | Value | Note |
|---|---|---|
| Measurement rows in the census | **12** (across 8 papers, 7 distinct alleles/constructs) | rows 3 and 5 are *attempted* measurements that do not exist; they are counted because a census of readings must count the zeros |
| Rows that **CAN** distinguish "degraded" from "insoluble" **as run** | 🔴 **0** | not one |
| Rows that **PARTIALLY** escape | **1** (row 7, `G372R` IF) | escapes lysis-loss, not epitope masking |
| Rows that **CANNOT** | **11** | |
| — of which fail because the buffer is a **cleared soluble lysate, explicitly** | **5** (rows 6, 9, 10, 11, 12) | the buffer is stated and the pellet is discarded |
| — of which fail because the method is **invisible** (`PREMISE: METHODS_INVISIBLE`) | **4** (rows 1, 2, 4, 5) | closed bodies: Springer, OUP |
| — of which fail because the authors **wrote no buffer down** | **1** (row 8) | `"After preparing the total cell lysate"` is the whole preparation |
| — of which are **not measurements at all** (`PREMISE: NOBODY_LOOKED`) | **1** (row 3) | the second `Q230P` family ran no blot |
| Rows examining a **pellet / insoluble / detergent-resistant fraction** | 🔴 **0** | verified zero in every served body |
| Rows stating an **antibody epitope position relative to the variant** | 🔴 **0 / 12** | |
| Rows stating a **detection sensitivity floor / LOD / dilution series** | 🔴 **0 / 12** | |
| Rows stating a **numeric loading amount** | **2 / 12** (20 µg; 100 µg as 10% input) | |
| Rows with a **permissive-temperature (26–30 °C) arm** | 🔴 **0** | see §2.6 for the confounder that would have to be controlled |
| Rows on **patient-derived material** | **4** (rows 1, 4, 5, 8) — of which **3** are `METHODS_INVISIBLE` and **1** states no buffer | 🔴 **the patient-derived sub-census is 100% buffer-blind** |

### 1.3 The Johannsen and Mallaret retrieval attempts, logged

Per the brief, no more than two attempts on Johannsen 2018. Both are logged; both failed; the paper's
lysis conditions stand as `PREMISE: METHODS_INVISIBLE`.

| Paper | Attempt | Route | Result |
|---|---|---|---|
| Johannsen 2018 | 1 | `get_article_metadata(["29808465"])` — checks for a PMCID and any deposited body | 🔴 **No PMCID exists.** Springer-closed. ✅ **Yielded the MeSH by-product in §1.4.** |
| Johannsen 2018 | 2 | `Scholar_Gateway semanticSearch`, methods-specific phrasing naming the buffer, the antibody and HEK293 | 🔴 **Body not in the corpus.** 12 passages, 10 articles, **none is Johannsen**; the closest is a *Am J Med Genet A* citing paper that only re-reports the endpoint. ⚠️ **And that citing paper misprints the variant as `p.Gln239Pro`** — a one-digit corruption of `Gln230` in the citing literature. Recorded so a future search for `Gln239` is not read as a second variant. |
| Mallaret 2014 | 1 | `get_full_text_article(["PMC3914474"])` | 🔴 `full_text: ""` — deposited but **not licensed for distribution**. Consistent with this repository's own `FT-128`. |
| Mallaret 2014 | 2 | Europe PMC REST `fullTextXML`, then `WebFetch` | 🔴 **`EGRESS_BLOCKED`** — `www.ebi.ac.uk` blocked by the network egress proxy. |
| Mallaret 2014 | 3 | `Scholar_Gateway semanticSearch`, methods-specific | 🔴 Not in the corpus (OUP title). ✅ **Yielded the Abdeen 2012 buffer lineage in §2.2.** |
| CST 4045S epitope | 1 | `WebFetch` vendor datasheet | 🔴 **`EGRESS_BLOCKED`** — `www.cellsignal.com`. **No vendor datasheet is reachable from this deployment**, so no epitope in this census could have been recovered from a catalogue even in principle. Recorded as a deployment limit, not as an absence in the literature. |

### 1.4 🆕 A lead the abstract does not contain: Johannsen 2018 has a HEK293 arm

The PubMed record for PMID 29808465 carries the MeSH descriptor list *"Afghanistan, Age of Onset,
Cells Cultured, Child, Consanguinity, Developmental Disabilities, Epilepsy, Family, **HEK293 Cells**,
Humans, Infant Newborn, Mutation Missense, Pedigree, Protein Domains, **RNA Stability**, Severity of
Illness Index, Spasms Infantile, Tumor Suppressor Proteins, WW Domain-Containing Oxidoreductase"*.

**`HEK293 Cells` and `RNA Stability` appear in no sentence of the abstract**, which describes only
patient fibroblasts, qRT-PCR and Western blotting.

- `INFERENZA` — the closed body very probably contains a **heterologous-expression arm in HEK293**,
  i.e. a transfected `Q230P` construct, and an **RNA-stability** experiment.
- 🔴 **Bounded by this repository's own `FM-009`**: *"I termini MeSH non sono contenuto sperimentale"*
  — Tochigi 2019 is indexed with three MeSH descriptors matching **no** experiment in the paper. A
  cell-line descriptor is more mechanical than a disease descriptor and I weight it higher, **but
  this is an inference about a paper I have not read and it is tagged as one.** It is not evidence
  that such an experiment exists; it is evidence that one should be asked for.
- **Why it matters disproportionately.** If a transfected `Q230P` construct was blotted in HEK293
  and *was* detected, the fibroblast "absence" is a cell-context or an allele-dosage phenomenon
  rather than an intrinsic property of the polypeptide. If it was blotted and was *not* detected,
  the two systems agree and the case for a folding/turnover lesion strengthens. **Either way this is
  the single highest-value unread fact about the reference genotype's missense allele**, and it is
  three sentences of a closed Methods section.

---

## 2 · DISCOVERY_TRACE — predictions written before the search, then scored

🔴 **Protocol followed.** The ten predictions below were written to
`scratchpad/predictions_sealed_20260922.md` **before** the first `grep` of this repository for an
allele string and **before** the first literature query of this task. They are reproduced verbatim
in substance, with point estimates intact. A refuted prediction is a good outcome here; a vague one
would be worthless.

| # | Prediction (sealed, before searching) | Outcome | Score |
|---|---|---|---|
| **P1** | **Majority (55–75%) of rows will state NO lysis buffer** (invisible or simply unstated) | Of the **8 papers** attempting a measurement: buffer stated in **4** (Hussain, Zhang, Steinberg, Schrock), absent in **4** (Johannsen, Mallaret, Öngen, and Weisz-Hubshman which has no blot). **50%, below my lower bound of 55%.** And the composition in one of the four "stated" cases (Schrock) is outsourced to a catalogue number | 🔴 **REFUTED** (narrowly). I over-predicted the field's opacity about buffers. The opacity is real but it sits in the *fraction* and the *epitope*, not the buffer |
| **P2** | Of stated-buffer rows, **≥70% will be a mild non-denaturing detergent lysis** (NP-40 / Triton / Igepal) with a clearing spin | Mild non-denaturing: Hussain **1% NP-40**, Steinberg **0.5% NP-40** = **2/4 = 50%**. The other two are RIPA-class (Zhang: NP-40 + 0.1% SDS + 0.5% DOC; Schrock: commercial RIPA) | 🔴 **REFUTED.** ⚠️ **But see §2.4: being refuted on the buffer class does not rescue a single row**, because RIPA does not solubilise detergent-resistant aggregate and the clearing spin removes it anyway. The prediction failed and the conclusion it was probing did not |
| **P2b** | *Corollary:* direct boiling of the whole well in Laemmli/SDS with **no clearing spin** will appear in **0 or 1** rows | **0 rows.** Öngen 2026 boils in SDS sample buffer, but boils the *product* of an unstated lysis | 🟢 **SUPPORTED** |
| **P3** | Rows examining a **pellet / insoluble fraction**: **0–1** in patient systems, **0–2** overall; **ZERO** in patient-derived material | **0 overall. 0 in patient-derived material.** Verified as string-level zeros in every served body | 🟢 **SUPPORTED**, at the strong end of my own range |
| **P4** | Has **ANY** WWOX missense paper run a soluble/insoluble split? **No** for patient-derived; **possibly yes** in an overexpression/aggregation context | **No — anywhere.** The WWOX "aggregation" literature (18 hits) is **entirely about partner proteins**: TRAPPC6AΔ, TIAF1, tau, Aβ, Zfra, plus GWAS noise. Not one is a solubility or aggregation assay on a WWOX missense protein | 🟢 **SUPPORTED** for the main clause; 🔴 **REFUTED** for my own hedge — I expected the overexpression literature to contain one and it does not |
| **P5** | Antibody **epitope UNSTATED in ≥75%** of rows; where stated, mostly C-terminal / full-length immunogen | **0/12 state an epitope. 100% UNSTATED** — stronger than predicted. The "where stated" clause is **vacuous**: there is no such row. Two rows name a catalogue number (CST 4045S; ab238144), one names a **tag** antibody (anti-FLAG M2), the rest name the antibody only as *"rabbit anti-Wwox"* or by a deleted citation callout | 🟢 **SUPPORTED** (and my point estimate was too generous to the field) |
| **P6** | **0 rows**, possibly 1, will state a sensitivity floor / LOD / linear range | **0 rows** | 🟢 **SUPPORTED** |
| **P7** | Loading amount stated in **fewer than half** the rows | **2/12 ≈ 17%** | 🟢 **SUPPORTED** |
| **P8** | A **permissive-temperature (26–30 °C) arm** has **never** been run on any WWOX missense allele in any system: **0 rows** | **0 rows.** ⚠️ **But an unanticipated finding sits next to it**, and it changes the experiment in §4: temperature work on WWOX *does* exist — Chen SJ *et al.*, *Cell Commun Signal* 2024;22(1):505, PMID 39420317, PMC11487720, [DOI](https://doi.org/10.1186/s12964-024-01866-6) — on **wild-type** WWOX at 4/10/22/37 °C, reporting a *"temperature-sensitive nuclear WWOX/TRAF2 complex"* and that *"UV/cold shock effectively downregulated the expression of many proteins such as the housekeeping α-tubulin (> 70%) and β-actin (< 50%)"* | 🟢 **SUPPORTED** as stated — with a confounder I did not predict and which §4 now has to design around. 🔴 **Note what that quote does to row 8 and to every future low-temperature arm: β-actin is not a valid loading control under cold shock.** |
| **P9** | **≥80%** of rows cannot tell "degraded" from "insoluble" as run; **100%** for patient-derived | **12/12 cannot fully. 1 partially escapes and it is not a blot. 4/4 patient-derived rows cannot.** | 🟢 **SUPPORTED** |
| **P10** | At least one **additional** designed point mutant, beyond the `P282A` case the brief flags, will turn out to be pooled in prose with disease alleles | `Y293F` and `W44F/P47A` were found and are designed mutants — but **Schrock 2016 keeps them explicitly distinct** and labels them as engineered. The pooling hazard is real **inside this repository's own reading habits** (its Tier-B list already records that `Y33R`, `K274R`, `L404A`, `Y293F` are *"routinely mistaken for disease variants in casual reading"*), not in the published sources I read today | 🟡 **AMBIGUOUS.** I cannot score this SUPPORTED without pointing at a published sentence that pools them, and I did not find one |

**Trace score: 6 SUPPORTED · 3 REFUTED · 1 AMBIGUOUS (with one sub-clause supported and two
sub-clauses refuted).** The three refutations are the useful part: I mis-modelled the field as
*careless about buffers* when it is in fact **careful about buffers and completely silent about
fractions and epitopes** — and §2.4 shows that being careful about the buffer, in the way this
field is careful, buys nothing.

### 2.2 🆕 The buffer lineage — why "mild NP-40" is the field's default even where it is unstated

A by-product of the Mallaret retrieval attempt. Abdeen SK *et al.*, *J Cell Physiol* 2013;228(7):1377-1382, PMID 24308844, [DOI](https://doi.org/10.1002/jcp.24308), from the laboratory that produced a large share of the WWOX protein literature, states its whole protocol in two sentences:

> *"Whole cell lysates were prepared using **0.5% NP40-containing buffer** (Aqeilan et al., 2004c). Antibodies used were **monoclonal anti-WWOX (Aqeilan et al., 2004a)** and monoclonal anti-GAPDH."*

Two things follow, and they must be kept apart.

1. `DATO` — **the reference protocol for WWOX immunoblotting in that lineage is 0.5% NP-40, mild and
   non-denaturing**, and the same 0.5% NP-40 recurs verbatim in Steinberg 2021 (row 7) fifteen years
   later.
2. `DATO` — **the antibody is identified by a citation, not by an epitope**, in 2013 and again in
   2017 (row 11). The field's convention is to inherit the reagent rather than to describe it.
3. `INFERENZA`, and flagged as one — a WWOX blot whose buffer is unstated is **more likely than not**
   a mild NP-40 soluble-fraction blot. 🔴 **This does not license filling in rows 1, 4 or 8.** It
   licenses exactly one thing: refusing to treat *"buffer unstated"* as *"buffer probably adequate"*.

### 2.3 The tag-antibody twist — why anti-FLAG makes rows 9–10 better and worse at once

The `P252A` / `P282A` abundance and CHX-chase panels were read with **anti-FLAG M2**, whose epitope
is `DYKDDDDK` — a short linear tag, not a WWOX surface.

- 🟢 **Better:** a linear tag epitope is **fold-independent**. A misfolded WWOX that would be invisible
  to a conformational anti-WWOX antibody is still visible to M2. So rows 9–10 are **immune to the
  epitope-masking artefact** that rows 1–8 cannot exclude.
- 🔴 **Worse:** the tag reports **only the terminus it is attached to**. A cleaved or truncated
  species that has lost that terminus vanishes, and the paper does not say which terminus the tag is
  on (`pCMV-3Tag`, family, vector number given, member not named).
- 🔴 **Unchanged:** a fold-independent antibody applied to a **cleared supernatant** still never sees
  the pellet. The epitope problem and the fraction problem are independent, and rows 9–10 solve one
  of them.

### 2.4 🔴 Why RIPA does not rescue the census, and why being wrong about P2 changed nothing

My prediction P2 assumed the field mostly uses plain NP-40; it uses RIPA-class buffers half the
time. That refutation does **not** move a single row from NO to YES, for three reasons stated
plainly rather than asserted:

1. **0.1% SDS with 0.5% deoxycholate is not a denaturing lysis.** It disrupts membranes and weak
   protein–protein contacts; it does not dissolve detergent-resistant aggregate, amyloid-like
   species, or inclusion bodies, which need 1–2% SDS with boiling, or urea, or formic acid.
2. **The clearing spin is the discard step, and it is identical in both buffer classes.** Zhang's
   *"collected by centrifugation at 13300 × rpm for 10 min at 4 °C"* removes exactly what an
   insolubility hypothesis predicts will be there, in RIPA as in NP-40.
3. **Nobody looked in what was removed.** `pellet` = 0, `fraction` = 0, `insoluble` = 0. A buffer
   argument is a proxy; the direct observation is that the discarded material was never blotted, in
   any paper, for any WWOX missense allele.

🔴 **The generalisation holds regardless of buffer class: in this literature, "WWOX protein absent"
means "WWOX protein absent from a supernatant nobody compared to its pellet."**

### 2.5 What a zero from PubMed did and did not establish here

Per the brief's seven failure modes, every absence asserted above names what it rests on.

| Absence asserted | Rests on | Failure modes observed **in this session** |
|---|---|---|
| No pellet / insoluble / fraction examined in Zhang 2025, Hussain 2023, Schrock 2016, Steinberg 2021 (missense arm) | 🟢 **READS of the served bodies**, with string counts taken on the text I read | — (this is a read, not a query) |
| No WWOX-missense solubility or aggregation assay anywhere | `WWOX AND (aggregation OR "detergent-insoluble" OR "insoluble fraction" OR "soluble fraction" OR solubility)` → **18 hits**, expansion clean on all five quoted terms, **every hit inspected by title and abstract**: partner-protein aggregation (TRAPPC6AΔ/TIAF1/tau/Aβ/Zfra ×9), GWAS/linkage (×4), reviews (×3), unrelated (×2) | ⚠️ `[All Fields]` does **not index Methods or supplements**, so a solubility split buried in a Methods section would be invisible. Carried as **`PREMISE: METHODS_INVISIBLE`, not as proof of absence** |
| No permissive-temperature arm on a WWOX missense | `WWOX AND ("permissive temperature" OR "30 degrees" OR "temperature-sensitive" OR …)` → **1 hit**, and it is wild-type WWOX cold-shock biology | ⚠️ Same Methods-invisibility caveat. `PREMISE: NOBODY_LOOKED` |
| Reagent epitopes | — | 🔴 **New failure mode for this deployment: `EGRESS_BLOCKED`.** No vendor datasheet is reachable. An epitope that the paper does not state **cannot be recovered here at all**, so `UNSTATED` is final for this session rather than provisional |
| **Trap (f) reproduced twice today** | `WWOX AND ("G372R" OR "Gly372" OR "P47T" OR …)` and `WWOX AND (Q230P OR Gln230 OR "p.Gln230Pro" OR … OR G372R …)` | 🔴 **`"G372R"` and `"p.Gln230Pro"` were SILENTLY DROPPED from the returned `query_translation` in both queries.** The translation carried the other terms and raised no error. This is the sixth failure mode, independently reproduced, and it means **any result count from an OR block in this gene under-reports by an unknown amount.** |

### 2.6 The confounder P8 did not anticipate

A permissive-temperature arm (§4) is the standard separator of *foldable-but-unstable* from
*fold-incompetent*. In this gene it carries a specific, published hazard that a generic protocol
would walk into: WWOX itself has **temperature-dependent behaviour** — a nuclear WWOX/TRAF2 complex
that *"dissociates"* at low temperature — and cold shock in that system *"effectively downregulated
the expression of many proteins such as the housekeeping **α-tubulin (> 70%)** and **β-actin
(< 50%)**"*. `DATO` on wild-type WWOX in COS7; `abstract-depth`, `PREMISE: UNREAD_PRIMARY`.

Two design consequences, both folded into §4: **stay at 30 °C and never go to 4–22 °C**, and **do
not normalise a low-temperature arm to β-actin or α-tubulin.**

---

## 3 · The consequence for the reference genotype, at exactly the strength the evidence allows

`DL-MECH-029` currently supports the inference that the reference genotype — formally `null/missense`
— *"potrebbe essere **funzionalmente null/null**"*, on the strength of Johannsen's `mRNA normale +
proteina non rilevata`, and that inference is what removes the survival advantage Oliver 2023 grants
the `≥1 missense` class.

**The honest answer is that this census does not weaken that inference, and I will not manufacture a
weakening in order to have found something.** Here is the reasoning, separated by claim.

### 3.1 What does NOT weaken — and why the intuitive argument fails

The intuitive argument runs: *"if 'absent' only means 'absent from the soluble fraction', the protein
may be there, so the allele may not be null."* 🔴 **That argument is wrong, and it is worth being
explicit about why, because it is the error this file could most easily have committed.**

An insoluble, aggregated WWOX polypeptide is **functionally absent**. It cannot homodimerise through
a buried SDR interface, cannot bind tau, GSK3β or TRAPPC6AΔ across the SDR span, cannot be
catalytically competent. Every one of the three live causes — impaired translation, insolubility,
premature degradation — terminates at **no functional WWOX from that allele**.

`INFERENZA` (strong): **the functional inference is invariant across the entire disjunction the
ledger records.** It does not weaken **by any amount**. It weakens **0%**.

And the repository already holds the standing demonstration that abundance would not have been
enough anyway: `P282A` is stable, present, and functionally dead. **"Present" was never the claim
that mattered.**

### 3.2 What DOES weaken, precisely, and by how much

Three narrower things weaken, and they are not the same claim.

| Claim | Status before this census | Status after | How much |
|---|---|---|---|
| *"The reference genotype's missense allele yields no functional WWOX"* | `INFERENZA` (strong) | 🟢 **`INFERENZA` (strong), unchanged** | **0%** |
| *"There is **complete loss of WWOX protein**"* — the wording of **Johannsen's own title** | quoted as if `DATO` | 🔴 **Demoted to `INFERENZA` with a named alternative.** The title asserts a property of the cell; the experiment measured a property of a supernatant, under a buffer nobody can read, with an antibody nobody named, against a floor nobody set | 🔴 **Substantially — this is a title that outruns its own Methods, and 12/12 rows of this census show the field has no instrument that could have licensed it** |
| *"The cause is one of {impaired translation, insolubility, premature degradation}, undiscriminated"* — the ledger's careful formulation | `IPOTESI`, three branches | 🟡 **Correct, and it should stay exactly as written.** This census does not narrow the three branches by one; it establishes that **no published WWOX work could have narrowed them**, which converts "undiscriminated" from an accident of one paper into a **field-wide, 12/12 structural gap** | **Strengthened as a statement about the field; unchanged as a statement about the allele** |

### 3.3 🆕 The fourth branch the ledger does not name

`DL-MECH-029` lists three causes and treats all three as routes to *absence*. The census adds a
branch that is not absence, and it points the wrong way.

> 🔴 **If `Q230P` partitions into an insoluble aggregate, the species is not merely non-functional —
> it may be a toxic gain-of-function species**, and the reference genotype would then be **worse**
> than functionally null, not better. `IPOTESI`, explicitly speculative, with no WWOX evidence
> behind it in either direction — the WWOX aggregation literature that exists is about partner
> proteins, and no WWOX missense protein has ever been tested for aggregation (§2.5).

Why record a speculation at all: because it inverts the therapeutic sign of the most obvious move.
`HYP-20260709-02` already records that a non-allele-specific WWOX expression boost has an uncertain
direction. 🔴 **On the insolubility branch, a boost is not merely useless — it adds substrate to an
aggregating species.** The repository's proteostasis matrix says the same in one line: *"a boost is
ACTIVELY DANGEROUS."* The census now supplies the reason that branch cannot be excluded: **nobody
has ever looked in the pellet, for any WWOX missense allele, in any system.**

### 3.4 What must not be inferred from this file

- 🔴 **Not** that `Q230P` protein is present. **Nobody knows.** Four rows of patient-derived material
  are 100% buffer-blind.
- 🔴 **Not** that Johannsen's blot was wrong. A soluble-fraction blot is a valid measurement of the
  soluble fraction. What is wrong is the inferential leap from it to *"complete loss."*
- 🔴 **Not** that `P252A`'s lysosomal route transfers to `Q230P`. Different allele, benign in
  ClinVar, CMV transgene, thyroid carcinoma line, and — per §2.3 — measured through a tag epitope
  on a cleared supernatant.
- 🔴 **Not** that the prognostic anchor changes. Oliver 2023's `≥1 missense` curve is a population
  statistic and this file supplies no new individual-level or genotype-level survival information.

---

## 4 · The one experiment that settles it

**ONE experiment. One material, one gel design, two temperatures. Compressed, not expanded.**

> **THE Q230P SOLUBILITY-AND-FOLDABILITY SPLIT.** Take donor-derived `Q230P/Q230P` fibroblasts
> (Johannsen family lines, or any banked `Q230P` homozygote), two unrelated healthy-control
> fibroblast lines, and one WWOX-null or `WWOX`-silenced line as the true-negative. Split each
> culture: **37 °C** and **30 °C for 48 h**. From every well, run a **sequential two-step extraction
> with both fractions loaded at equal cell-equivalents on the same gel.**

| Element | Specification | Why exactly this, and not the obvious alternative |
|---|---|---|
| **Buffer, step 1 (S)** | 1% NP-40 / 150 mM NaCl / 50 mM Tris pH 7.5 + protease inhibitors, 30 min on ice; spin **16,000 × g, 20 min, 4 °C**; keep supernatant = **S** | Deliberately the **field's own mild buffer**, so the S lane reproduces what every published WWOX blot has been measuring. The point is the comparison, not a better S |
| **Buffer, step 2 (P)** | Wash the pellet once in the same buffer, then resolubilise it in **2% SDS / 8 M urea / 50 mM Tris + DTT, 95 °C, 10 min**, sonicate to shear DNA = **P** | This is the step that has never been performed in this gene. RIPA would not do it (§2.4) |
| **Loading** | **Equal cell-equivalents**, not equal protein — a fixed fraction of S and of P from the same well, side by side | 🔴 Equal-protein loading of a pellet is meaningless: the pellet's protein composition is not the lysate's. This is the single most common way this experiment is run wrongly |
| **Loading control** | **Total-protein stain** (stain-free gel or Ponceau), on both lanes | 🔴 Not β-actin, not GAPDH, not α-tubulin: they partition differently between S and P, **and the WWOX cold-shock literature records α-tubulin down >70% and β-actin down <50% under low temperature** (§2.6). A housekeeping band would silently destroy the 30 °C arm |
| **Antibodies** | **Two**, on the same membrane or on paired membranes: (i) an **N-terminal / WW-domain** antibody (immunogen within aa 1–100, i.e. **N-terminal to Q230**) and (ii) a **C-terminal SDR** antibody (immunogen C-terminal to Q230). **Both epitopes stated in the write-up by residue range** | 🔴 The census's hardest finding is that **0/12 published rows state an epitope**. Two epitopes flanking the variant are what distinguish: full-length present · N-terminal fragment only (translation/cleavage) · a masked SDR epitope on a misfolded but present protein. One antibody cannot separate these, and the field has never used two |
| **Sensitivity floor** | A **dilution series of a WWOX-positive lysate** (or recombinant WWOX) on the same membrane, ≥5 points, to define the **LOD in ng**. *"Not detected"* is reported **only** as *"below X ng, N = 3"* | 🔴 0/12 rows state a floor. `CLAIM 030` in this repository already carries `PREMISE: DETECTION_FLOOR` on exactly this point; this turns the premise into a number |
| **Permissive-temperature arm** | **30 °C for 48 h**, run through the identical S/P split, with the healthy control **also** at 30 °C | Separates **foldable-but-unstable** (P shrinks, S grows at 30 °C) from **fold-incompetent** (no shift) from **not made** (neither lane, either temperature, with both antibodies, above the stated LOD). 🔴 **30 °C and not 26 °C, and never 4–22 °C**: the WWOX cold-shock confounder in §2.6 lives below 22 °C, and the control arm is what makes a global cold effect separable from an allele-specific one |
| **Transcript control** | qRT-PCR on the same wells, both temperatures | Confirms the Johannsen mRNA result is reproduced in *these* cells before any protein conclusion is drawn |

**The readout is a decision table, fixed before the gel is run:**

| S lane | P lane | 30 °C shift | Conclusion | What it does to the reference genotype |
|---|---|---|---|---|
| absent (< LOD) | **present** | any | 🔴 **INSOLUBLE.** Johannsen's "absence" was a fraction artefact | Functionally null stands; **a WWOX boost becomes contraindicated**; anti-aggregation becomes the route; §3.3's fourth branch goes live |
| absent | absent, **both antibodies** | none | **NOT MADE, or cleared below LOD** | Functionally null stands; the target is **translation or turnover**, and a chase/labelling study is next |
| absent | absent | **S appears at 30 °C** | 🟢 **FOLDABLE-BUT-UNSTABLE** — the best possible outcome | Functionally null stands **today**, but the allele is **rescuable in principle**; `TX-003` (pharmacological chaperone) stops being conditional |
| present | — | — | The fibroblast result does not reproduce | Re-open everything, including the `HEK293` arm of §1.4 |

**Cost class: 🟡 NEW CELL WORK.** Not a new animal cohort, not a new staining of existing material —
it needs living `Q230P` fibroblasts, which exist but are not in this repository's hands. One
investigator, four genotype/temperature arms, three biological replicates, two gels, ~2–3 weeks of
bench time once the lines are in culture. **Everything else in the protocol is standard reagents.**
🔴 **Obtaining the lines requires contacting the holding institution, which is `HUMAN_REQUIRED` and
was not attempted.**

**Cheaper predecessor, for completeness and then dropped:** re-reading Johannsen's closed Methods
and its probable HEK293 arm (§1.4) is `NEW ANALYSIS ONLY` and costs nothing but access. It cannot
settle the question — no published WWOX work ever loaded a pellet — but it could tell us which
buffer produced the founding datum, and it could reveal a second, unread `Q230P` measurement.

---

## 5 · REVIVAL_TRIGGERs and COULD NOT ESTABLISH

### 5.1 REVIVAL_TRIGGERs

Nothing above dies in silence. Each rejection below names what would reopen it.

| ID | What is currently rejected / held | What would revive it |
|---|---|---|
| `RT-LYS-01` | *"'WWOX protein absent' in any published WWOX-missense paper means the protein is absent from the cell"* — rejected, 12/12 | **Any** published or supplied blot in which an SDS/urea-resolubilised pellet from a WWOX-missense system is loaded beside its supernatant. One gel retires this |
| `RT-LYS-02` | *"Johannsen 2018's fibroblast lysis conditions are unknowable"* — held as `METHODS_INVISIBLE` after 2 attempts | The PDF or the Methods section reaching this repository by **any** route: an institutional copy, an author-supplied Methods, an ILL delivery, or a future corpus update that ingests Springer *Neurogenetics* |
| `RT-LYS-03` | *"Johannsen 2018 contains no HEK293 experiment"* — **not** asserted; §1.4 asserts the opposite as `INFERENZA` | Reading the body. If a transfected `Q230P` HEK293 blot exists and shows detectable protein, **§3.2 row 2 and §3.3 must both be rewritten the same day** |
| `RT-LYS-04` | *"No WWOX missense protein has ever been tested for aggregation"* — held with a Methods-invisibility caveat | A Methods-level or supplementary-level solubility, filter-trap, FRAP, semi-denaturing detergent agarose gel or sedimentation assay on any WWOX missense construct, in any paper, including one indexed under an unrelated title |
| `RT-LYS-05` | *"Anti-FLAG M2 rows (9–10) are epitope-masking-immune"* — asserted in §2.3 | Evidence that the `pCMV-3Tag` member used places the tag such that a truncation would remove it, **or** any report of WWOX proteolysis at a specific terminus. Then rows 9–10 lose their one advantage |
| `RT-LYS-06` | *"`P282A` is not usable as a complete-loss control"* — held, per the brief and per rs3764340 with 18 healthy homozygous controls | Would require a pathogenic reclassification of rs3764340 with population evidence. Absent that, this rejection is **permanent for this repository** |
| `RT-LYS-07` | *"A permissive-temperature arm has never been run on a WWOX missense allele"* — `PREMISE: NOBODY_LOOKED` | Any 26–33 °C culture arm on any WWOX missense system, including one reported only in a figure legend or a supplement |
| `RT-LYS-08` | *"The reference genotype's 'functionally null/null' inference does not weaken"* — §3.1 | 🔴 **A demonstration that an insoluble or aggregated WWOX species retains a measurable function** (partner binding at the SDR span, or catalytic activity). That would break the invariance argument and is the only thing that would |

### 5.2 COULD NOT ESTABLISH

| # | What I could not establish | Why, exactly |
|---|---|---|
| 1 | **Johannsen 2018's lysis buffer, antibody, loading, detection or `n`** | Springer-closed, no PMCID, not in the publisher-side passage corpus. Two attempts, both logged (§1.3). `PREMISE: METHODS_INVISIBLE` |
| 2 | **Whether Johannsen 2018 contains a HEK293 `Q230P` expression experiment, and what it showed** | MeSH-level inference only (§1.4), bounded by this repository's own `FM-009` |
| 3 | **Mallaret 2014's lysis buffer or antibody, and whether a `G372R` blot exists at all** | PMC returns an empty body (licensing); Europe PMC and publisher egress are **`EGRESS_BLOCKED`** in this deployment |
| 4 | **The epitope of CST 4045S, Abcam ab238144, the Aqeilan-lineage monoclonal, or Hussain's "rabbit anti-Wwox"** | Unstated in every paper, and **no vendor datasheet is reachable from this deployment**. Not guessed |
| 5 | **The terminus of the FLAG tag in `pCMV-3Tag` (#240195)** | The vector family has both orientations; the paper names the family and not the member |
| 6 | **Whether Zhang 2025's CHX chase would survive a pellet analysis** | Only the supernatant was ever blotted. The CQ-rescue arm argues against pure aggregation but does not exclude it |
| 7 | **A numeric t½ for any WWOX missense protein** | Never reported. `half` occurs once in Zhang's body and it is the Methods sentence of intent |
| 8 | **Whether any Methods-buried solubility split exists in the WWOX corpus** | `[All Fields]` does not index Methods or supplements. The zero is `PREMISE: METHODS_INVISIBLE`, not proof |
| 9 | **How many WWOX OR-block query results were lost to trap (f)** | `"G372R"` and `"p.Gln230Pro"` were silently dropped from two `query_translation`s today. The loss is unquantifiable by construction |
| 10 | **Anything about the reference individual** | Out of scope by design. This is the public edition; it reasons about a WWOX-DEE genotype class and carries no individual-level record |

---

## 6 · Self-grade

### **B+**

**What earns it.**

- The census is a **read**, not a grep: seven bodies were served and read for their Methods, and
  every verbatim buffer string in §1.1 was taken from text I had open.
- The central counts are **verified zeros inside served bodies**, not query zeros: `pellet` 0,
  `fraction` 0, `insoluble` 0 in the paper with the deepest turnover work.
- The DISCOVERY_TRACE was **sealed before the first search** and contains three refutations,
  including one (P2) that refuted my model of the field without rescuing the field — which is the
  most informative shape a refutation can have, and I said so rather than quietly reframing.
- §3 **declines the dramatic answer.** The obvious payoff for a file with this title is *"the
  functionally-null inference collapses."* It does not collapse, the invariance argument in §3.1 is
  the reason, and writing that down was the main intellectual work here.
- Two findings were not in the brief and are not in the repository: the **MeSH-level HEK293 lead**
  on the single most consequential closed paper (§1.4), and the **cold-shock confounder** that a
  naive permissive-temperature arm would have walked into (§2.6), including the fact that β-actin
  is an invalid loading control there.
- Alleles are held apart throughout; `P282A` is flagged at every appearance and never used as a
  loss control; designed mutants are separated from disease alleles in the table itself.

**What holds it below A.**

- 🔴 **The most important single row is empty.** `Q230P`, the allele the whole file exists for, is
  `METHODS_INVISIBLE`, and so is the one independent human `P47T`/`G372R` fibroblast blot. Four of
  twelve rows are holes. A census with a hole where its subject should be is a map of the hole.
- The `n=8 papers` denominator is small, and P1's refutation turns on a 50%-vs-55% boundary that
  one more paper would move. I reported it as REFUTED rather than rounding it into a SUPPORT, but
  it is a weak refutation and should not be cited as a finding about the field.
- The HEK293 lead is a **MeSH inference**, i.e. exactly the class of evidence this repository has a
  named failure mode against (`FM-009`). I weighted it up because a cell-line descriptor is more
  mechanical than a disease descriptor; that weighting is a judgement, not a measurement.
- I did not attempt an exhaustive sweep of engineered-mutant overexpression blots (Y33R, K274R,
  L404A, the Chang-lab EGFP-fusion series). Rows 11–12 are a **sample** of that class, chosen
  because their paper was served and their Methods stated a buffer. The designed-mutant sub-census
  is therefore **incomplete and declared incomplete**.
- `P10` scored AMBIGUOUS because I could not point at a published sentence pooling designed and
  disease mutants. That is a prediction that was not sharp enough to be scorable, and it is the one
  I would rewrite.

**Not graded F, per the brief, and no restatement of the brief appears as a finding.**

---

## 7 · Session control records (§21c / §21d)

**STOP_LOG.** Class 1 (reserved act): **0 stops taken.** Obtaining `Q230P` fibroblast lines and any
author contact are reserved / `HUMAN_REQUIRED`; both are **named in §4 and §5 rather than attempted**,
which is the sanctioned alternative and not a stop. Class 2 (no safe default): **0**. Class 3: **0**.

**DEFAULTS_TAKEN.**

| Condition | Default taken | Why safe | What would have differed |
|---|---|---|---|
| Johannsen 2018 body unreachable after 2 attempts | Recorded `PREMISE: METHODS_INVISIBLE`, logged both attempts, proceeded with the generalisation | The brief caps attempts at two, and the census does not depend on that one paper | A third attempt would have cost budget for a route (Springer) that this deployment cannot reach |
| Mallaret 2014 PMC body empty; Europe PMC and publisher egress blocked | Same treatment; recorded the egress block as a deployment fact | Recording a retrieval failure as a retrieval failure, never as an absence | — |
| Vendor datasheets unreachable | Every epitope left `UNSTATED`, never inferred from a catalogue number | Guessing an epitope is precisely the error §1.1 is built to expose | A reachable datasheet would have filled 2 of 12 epitope cells, and no more |
| A prior same-day census (`wwox_missense_stability_census_20260922.md`) already covers the allele enumeration | Built **on** it, cross-linked it, and did not re-derive the variant list | Re-deriving would have duplicated work and risked a second, divergent count | — |
| Predictions vs. a corpus a peer session had already touched | Sealed predictions **before** reading that file | Otherwise the trace would be post-hoc and worth nothing | — |

**DECISIONS_TAKEN.**

| Decision | Alternatives rejected | Reversibility |
|---|---|---|
| Count rows 3 and 5 (non-existent measurements) inside the census denominator | Excluding them, giving a cleaner "10 rows, 0 distinguish" | Fully reversible — both are labelled and the sub-counts in §1.2 allow either denominator. A census of readings that drops its zeros is the false-negative failure `epistemic_discipline` §2 exists to prevent |
| Score row 7 (`G372R` IF) as **PARTIALLY** rather than NO | Scoring it NO for tidiness | Reversible; the reasoning is in the cell, and it is the one row where the artefact class genuinely differs |
| Report §3 as **"does not weaken"** | Reporting a weakening, which the file's framing invites | Reversible on `RT-LYS-08`, which names the single evidence class that would overturn it |
| Include rows 11–12 (designed mutants) in the table | Confining them to a footnote | Reversible; the brief names transfected cells as in scope, and both rows are flagged `DESIGNED` in the allele cell itself |

**Canonical surfaces touched: none.** No `*_current.md`, registry, queue, ledger, receipt or state
manifest was read for writing or modified. No `git` command was run. No `BATCH_COMMIT`. One file
written, at the path the brief specified.

---

*Scholar Gateway · 2 queries · 18 passages · 16 articles · 2007-06-07–2026-08-06 — Results retrieved by Scholar Gateway · Summary generated by AI — verify claims against source documents · Last corpus update: September 2026 · [Content coverage details](https://support.scholargateway.ai/s/article/Available-Content)*

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V0 · Declared deviation

One read-only `git status --porcelain`, self-declared. Nothing written outside the one file —
confirmed against the working tree. **Accepted, recorded, not repeated.**

## V1 · 🟢 The MeSH finding is VERIFIED, and it is the best thing in this file

I re-pulled `PMID 29808465` independently. According to PubMed,
[DOI](https://doi.org/10.1007/s10048-018-0549-5). The MeSH list carries **`HEK293 Cells`** and
**`RNA Stability`**, and **neither word appears anywhere in the abstract**. 🟢 **CONFIRMED.**

Indexers assign `HEK293 Cells` when the paper reports work in them. So a **heterologous `Q230P`
expression arm very probably exists inside a body this laboratory has never read**, and `RNA
Stability` suggests the transcript work went beyond one steady-state qPCR — a decay measurement
would make *"normal levels of WWOX transcripts"* a materially stronger statement than it currently
reads. Both stay `INFERENZA` from an indexing field, per `FM-009`; neither may be cited as a
result.

**🆕 Two things in the same record that this file did not extract:**

1. 🔴 **The functional data are `n = 1`.** Abstract, verbatim: *"Functional WWOX analysis was
   performed in **fibroblasts of one patient**."* Two sisters are homozygous; **one** was assayed.
   The single most load-bearing measurement for the reference genotype's missense allele is
   therefore unreplicated, in one cell type, from one individual. The discovery ledger's
   `DL-MECH-029` says *"fibroblasti donor-derived"* without a number and should carry the `n = 1`.
2. 🟢 The title — *"leads to **complete loss of WWOX protein**"* — is verified verbatim, which
   makes this file's demotion of it from `DATO` to `INFERENZA` a correction to a published
   **title**, not to a paraphrase. That demotion is right: the title asserts a property of the
   cell; the experiment measured a property of a supernatant.

## V2 · 🔴 The Chen 2024 confounder is real but the justification is OVERSTATED — corrected, and the design survives

Verified verbatim (`PMID 39420317`, According to PubMed,
[DOI](https://doi.org/10.1186/s12964-024-01866-6)): *"**UV/cold shock** effectively downregulated
the expression of many proteins such as the housekeeping α-tubulin (> 70%) and β-actin (< 50%),
and cortactin (> 70%) in WWOXf **COS7** cells."*

**Three bounds this file does not carry:**
- The effect is **UV *plus* cold shock**, not cold alone. A bare temperature shift with no
  irradiation is not the demonstrated condition.
- The temperatures studied are **4, 10, 22 and 37 °C**. 🔴 **30 °C is not among them**, so the
  source says nothing directly about the arm this file designs.
- The cells are **COS7**, not fibroblasts, and the laboratory is Chang/NCKU — whose `TPC6AΔ`
  biology this repository has already downgraded to belief **BASSO** as non-independently
  replicated. That provenance caution travels with the citation.

🟢 **The design rule survives, on a better footing.** Use a **total-protein stain, never β-actin or
α-tubulin**, and use **30 °C with a WT arm at the same temperature** — not because Chen 2024
demonstrates a housekeeping collapse at 30 °C, but because **nobody has measured whether one
occurs**, and Chen 2024 establishes that WWOX-status × temperature × housekeeping interactions are
real in this gene under *some* conditions. `PREMISE: NOBODY_LOOKED`, not `DATO`. The rule is
adopted; the evidence for it is weaker than stated and is now stated correctly.

## V3 · 🔴 §3 is right on two branches and too strong on the third — and this file's own headline is what breaks it

§3 concludes the *"functionally null/null"* inference *"does not weaken. Not by 10%, not by any
amount."* I endorse the reasoning for **insolubility** (an aggregated WWOX cannot dimerise, bind
`tau`/`GSK3β`/`TRAPPC6AΔ`, or catalyse) and for **premature degradation** (no protein, no
function). Declining the dramatic answer on those two was correct and is the right instinct.

🔴 **It does not hold for the translation branch, and the reason is §1.** *"Impaired translation"*
is not *abolished* translation. A missense allele translated at, say, one-twentieth of normal
yields **structurally normal, fully functional WWOX** at a level no blot in this census could see —
because **0 of 12 rows state a sensitivity floor**, which is this file's own strongest finding.
With the floor unset, *"absent"* is consistent with anything from zero to some unmeasured
percentage of normal. Against a **null** sibling allele, the difference between 0 % and a few
percent is not nothing: it is the entire content of the word *hypomorph*.

**So the inference weakens on exactly one of three branches, and by an amount that is
unquantifiable — because the instrument that would quantify it was never calibrated.** That is a
sharper result than either "it survives intact" or "it collapses", and it is the one the evidence
supports.

⚠️ **Proportion, stated rather than implied.** The translation branch is the least mechanistically
favoured of the three — a single missense codon rarely depresses translation much. But this
repository does not discharge a disjunct on plausibility, and the authors themselves listed it
first.

🔴 **And §3 is internally inconsistent with §4's own fourth branch.** If an aggregated species could
be a toxic gain-of-function, then the branches do **not** terminate at the same place — one is
*worse* than null. §3 cannot claim invariance while §4 names a branch that breaks it. The correct
unified statement: **the endpoint (no detectable functional WWOX from that allele) is shared by two
branches; the therapeutic sign is branch-dependent across all four** — a non-allele-specific
expression boost yields functional protein under impaired translation, more aggregate under
insolubility, and is actively dangerous under toxic gain-of-function. That is why the branch
matters even when the endpoint does not.

## V4 · Endorsed without amendment

🟢 **0 pellets examined in 12 rows, verified as in-body string-level zeros rather than query zeros** —
the right instrument for the right claim, and the single most reusable number in the file.
🟢 **0/12 epitope positions stated.** 🟢 **Equal cell-equivalents, not equal protein** — correct,
and the error it prevents is the one that would make a degradation result look like a loading
artefact. 🟢 **Two antibodies with stated residue ranges flanking Q230**, separating full-length
from N-terminal fragment from masked epitope — never done in this field.
🟢 **The buffer-lineage observation** (`0.5% NP-40` recurring verbatim from Abdeen 2012 to
Steinberg 2021) licenses exactly what the file says it licenses and nothing more.
🟢 **Trap (f) reproduced twice today** on `"G372R"` and `"p.Gln230Pro"` — a seventh and eighth
instance of a silent `OR`-block drop.

## V5 · Grade

**B+ endorsed.** Earned by reading bodies for Methods rather than trusting abstracts, by verifying
zeros in-body, by a sealed trace with three informative refutations, and by declining the dramatic
answer in §3 — the last of which I have nonetheless had to correct on one branch, using this
file's own census result. That is the good kind of correction: it was available only because the
census was done properly.

**No row is canonical; none is proposed for `BATCH_COMMIT`.** Acquiring patient lines remains
`HUMAN_REQUIRED` and was correctly not attempted.

---

# 🔴 ORCHESTRATOR AMENDMENT — 2026-09-22, later the same day

## A name is not a composition, and §1 classifies partly by name

A recursive re-read of `PMID 22193544` (`recursive_reread_2_cdd2011_20260922.md`) found this, in a
paper this repository has held at `complete_fulltext_read` since July. According to PubMed,
[DOI](https://doi.org/10.1038/cdd.2011.188):

> *"lysed in ice-cold **RIPA buffer** (100 mM HEPES pH 7.4, 150 mM NaCl, 2 mM EDTA, **0.5% Tween 20,
> 0.1% Triton X-100**, 1 mM DTT, …)"*

**RIPA is defined by SDS and sodium deoxycholate. That buffer contains neither.** It is a mild
non-ionic Tween/Triton buffer carrying the name of a stringent one.

**Consequence for this census.** §1 places rows in a stringent or mild class partly on the strength
of the word the authors used. **Every row whose buffer is recorded by NAME rather than by RECIPE is
hereby re-graded `COMPOSITION UNVERIFIED`** — including the row recorded as *"Schrock 2016
commercial RIPA"*. Rows with a verbatim recipe (Zhang 2025's `1% NP-40, 0.1% SDS, 0.5% sodium
deoxycholate`; Hussain 2023's `1% NP-40`; Steinberg 2021's `0.5% Nonidet P-40`) are unaffected.

🟢 **This strengthens the file's headline rather than weakening it.** A row that looked stringent may
have been mild. The count *"0 of 12 rows can separate degraded from insoluble as run"* stands, and
the reason a reader might have discounted it — *"but some of them used RIPA"* — is now closed.

## Two further Methods facts from the same re-read, both on this census's axis

- **A GST pull-down with no lysis step written down at all.** *"GST or GST–WWOX proteins expressed
  in BL21 (DE3) were adsorbed to glutathione-agarose beads … after three washes with PBS."* No
  sonication, no lysozyme, no buffer, no clarifying spin. Whether the construct came from the
  soluble fraction or from washed inclusion bodies is `METHODS_INVISIBLE`.
- **A direct-to-SDS whole-cell western lysis with an unquantified spin.** *"disrupted in 2X sample
  buffer (… **4% SDS** …), **boiled for 10 min, centrifuged**"* — maximally denaturing, therefore
  much less prone to a solubility artefact than this census's mild-buffer rows; but *"centrifuged"*
  carries **no g-force, no time and no statement of which fraction was loaded**, so the same 0/12
  defect applies even here.

**Neither changes §3.** The three-branch analysis and the Orchestrator's correction to it (the
translation branch is where the *"functionally null/null"* inference weakens, by an amount
unquantifiable because no floor was ever set) are untouched.

---

# 🔴 ORCHESTRATOR AMENDMENT 2 — a thirteenth row, and it is the one the census needed

**Tochigi 2019**, `PMID 31340538` / `PMC6678113`, According to PubMed,
[DOI](https://doi.org/10.3390/ijms20143596). Retrieved and read by the Orchestrator.

| field | value |
|---|---|
| allele | rat `lde/lde` — `c.1190_1202del`, exon 9 frameshift, `p.Leu371Thrfs*53` |
| system | whole brain and cerebral cortex, PND 5–21 |
| **lysis, verbatim** | *"organs were minced and **sonicated** in RIPA lysis buffer (50 mM Tris-HCl pH 7.6, 150 mM NaCl, 1 mM EDTA, **1% sodium deoxycholate, 0.1% Triton X-100, and 0.1% SDS**)"* |
| denaturing? | 🟢 **genuinely stringent** — deoxycholate **and** SDS, **plus mechanical disruption** |
| pellet examined? | 🔴 **not stated** |
| antibody / epitope | 🟢 **`HPA050992`, Sigma — epitope `aa 32–110`, STATED IN THE PAPER.** The only epitope-stated row in the census |
| result | prior report: *"no Wwox protein was detected"*. **This paper: *"weak expression of a slightly heavier protein (46.2 kDa)"***, at the mass the frameshift predicts (*"theoretically 0.8 kDa larger"*) |
| can *absent* be told from *insoluble* as run? | 🟡 **partially — the first row where it can.** Stringent extraction plus sonication makes a soft-lysis artefact unlikely; **but no pellet was examined**, so it is not closed |

## Why this row changes the census rather than extending it

1. 🎯 **It is the in-gene demonstration of the census's own thesis.** A published *"no protein"*
   became *"present, faint, N-terminally intact"* **with the antibody as the only changed
   variable** — and the antibody that found it is the only one in the census with a stated epitope,
   `N`-terminal to a `C`-terminal lesion. The census argued that *absent* may mean *not seen*; here
   it demonstrably did.
2. 🔴 **It does not rescue the other twelve rows** — it makes them worse. If a faint species was
   missed once by reagent choice, the eleven rows with `UNSTATED` epitopes cannot exclude the same.
3. **`RIPA` means two different chemistries in this corpus.** Wang 2011 calls a Tween/Triton buffer
   with neither DOC nor SDS *"RIPA"*; this paper uses the name correctly. **Classify by recipe,
   never by name** — the rule of Amendment 1, now with both poles of the example in hand.

⚠️ **Bounds.** Rat, not human; a frameshift, not a missense; and the authors run **no functional
assay** on the residual species, judging only that *"it is unlikely that this faint expression …
would have substantial effects"*. **`abundance rescue ≠ functional rescue` applies to a naturally
occurring residual species exactly as to a rescued one.** Nothing here says the `lde` rat has
useful WWOX.

`REVIVAL_TRIGGER`: any WWOX abundance measurement made with **two** antibodies flanking the lesion;
or any pellet examined alongside a stringent lysate.
