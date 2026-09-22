# `Q230P` — pharmacological rescue PRECEDENTS: are there real cases, with measured function?

> **Actor:** Scientist K · **Date:** 2026-09-22 · **Canonical main at start:** `8d367f3`
> **Canonical status:** 🔴 **`DISCOVERY` — non-canonical throughout.** Not a `CANDIDATE`, not
> `CANONICAL`, not a commit candidate. No registry, queue, ledger, receipt or `*_current.md` file
> was touched. No `BATCH_COMMIT`. No git command was run.
> **Nothing here is medical advice, and no compound is recommended for any person.** The
> interventions named below are cited as *published experiments on other proteins*; several are
> drugs, and none of them is proposed for use by anyone.
> **Public edition.** Reasoning is about the WWOX-DEE reference genotype class, not an individual.

**Source attribution.** According to PubMed, the primary records below were retrieved with
`mcp__PubMed__search_articles` / `get_article_metadata`; passage retrieval used
`Scholar_Gateway semanticSearch`, whose `ai_generated` summary was **not** used as evidence.
DOIs are given as links, as the tool's terms require.

---

## 0 · What I inherited and did not re-derive

Read first, and treated as settled for the purposes of this act:

- [`q230p_therapeutic_mechanism_expansion_20260922.md`](q230p_therapeutic_mechanism_expansion_20260922.md) §§3, 4, 10 — the six-route evidence-class ranking, the four chaperone entry criteria, the `MIXED` mechanism verdict, the orchestrator verification block.
- [`q230p_structural_mechanism_20260922.md`](q230p_structural_mechanism_20260922.md) — SASA 0.00 Å², burial 83.8th percentile, the 1.44 Å Cδ/Glu226-O hard overlap, the deleted i,i−4 amide hydrogen.
- [`wwox_missense_stability_census_20260922.md`](wwox_missense_stability_census_20260922.md).

**Carried forward unchanged, not restated in full:**

| inherited fact | carried as |
|---|---|
| **Lou 2018** (PMID 29141528): in an SDR, *"most of the mutations in β-sheet core … became more stable than wild type, unfortunately, **all** the mutations suffered dramatic activity loss"*; all seven lost activity, best case 28.7 % | 🔴 **THE CONSTRAINT.** Stability/solubility rescue cannot proxy functional rescue. This is *why* a precedent must carry a measured functional readout — it is methodological, and it is **not** evidence that `Q230P` is unrescuable |
| **NmrA** (SDR superfamily): NAD⁺ raises Tm +3.6 °C in WT, **+5.8 °C in a destabilised variant**; **SDRvv**: Kd(NADPH) 3.5 µM vs Kd(NADP⁺) 242 µM | inherited, not re-derived |
| **Kabir 2016** (PMID 27595938): in NAD(P)-dependent oxidoreductases the **sign** of a stabiliser **inverts** with cofactor occupancy; all four combinations observed | inherited; extended in §4 below |
| `WWOX homodimerises via the SDR` = **`PREMISE: UNVERIFIED`** | not built on anywhere in this file |
| `P282A` = **`OVEREXPRESSION-ARTEFACT SUSPECT`** (18 healthy adult homozygous controls; ClinVar Benign) | not used as a control |
| No validated WWOX activity assay; no purified folded WWOX SDR; nobody has looked in the pellet for any allele | carried; it is the hinge of §5 |

**Pre-search, run before the trace was written** (`FIND ISSUE → CLAIMS → CANDIDATES → DISCOVERY LEDGER`): the inherited expansion file's §4 ranking is the repository's current statement of this question, and its own §9.1 records the routes it left blocked. **No defect is declared in this file**; §2's finding is an *addition and one correction* to §4.4 of that file, and is labelled as such.

---

## 1 · 🔴 §13 PROSPECTIVE DISCOVERY TRACE

> **Written and persisted to disk BEFORE the first targeted search of this act.** The text of §§1.1–1.6 is reproduced verbatim from that pre-search artefact; §§1.7–1.10 were appended after.

### 1.1 OBSERVATION

All six intervention routes in the inherited file were retrieved through **one** vocabulary:
*pharmacological chaperone*. Not one was retrieved through the vocabulary of **cofactor- and
vitamin-RESPONSIVE inborn errors of metabolism** — where the intervention *is* the cofactor, the
readout *is* enzyme activity, and the rescue has been demonstrated in patients. Trap (e) of the
six-ways-a-PubMed-zero-lies list is exactly this: a term invisible to an otherwise perfect
expansion.

### 1.2 DIVERGE — seven non-paraphrastic explanations for "no SDR precedent found"

| # | explanation |
|---|---|
| **D1** | **True absence.** No SDR disease allele has ever been pharmacologically rescued |
| **D2** | **Vocabulary miss.** SDR rescues exist but are indexed as *vitamin-responsive* / *cofactor-responsive*, never as *chaperone* |
| **D3** | **Precursor-level miss.** Rescue is reported for the vitamin PRECURSOR (riboflavin, pyridoxine, niacin) so cofactor queries miss it |
| **D4** | **Fold, not family.** Rescue exists in NAD(P)/FAD Rossmann oxidoreductases that are not SDR; what transfers is the cofactor cleft, not the family label |
| **D5** | **Split reporting.** Abundance and activity are measured in different papers, so the two-measurement precedent is rare by REPORTING convention, not by biology |
| **D6** | **Engineering, not disease.** SDR stabilisation literature is biocatalysis |
| **D7** | **Wrong ligand class.** The rescuing ligand is substrate/product/inhibitor, not cofactor |

### 1.3 CONNECT — four adjacent domains not previously mined here

**C1** vitamin-responsive inborn errors (riboflavin-responsive MADD; B6-responsive homocystinuria; BH4-responsive PKU) · **C2** *structural*, non-catalytic cofactor sites as stabilisers (G6PD's allosteric NADP⁺ site) · **C3** small-molecule agonist/structural-corrector chemistry on a NAD-dependent oxidoreductase (ALDH2*2 / Alda-1) · **C4** osmolyte/temperature rescue of a human SDR — the 11β-HSD2 row already in the repository, whose **activity** readout (as distinct from its half-life) had never been checked here.

### 1.4 HYPOTHESIS

The precedent class this question needs **exists**, but is indexed under cofactor-responsive
metabolic disease rather than under pharmacological chaperones; within it the strongest instances
are **NAD(P)/FAD-dependent oxidoreductases** in which the cofactor, its precursor, or a small
molecule at a cofactor site **both** raises steady-state protein **and** restores a measured
catalytic or physiological readout. D2 + D4 dominate; D1 is false for the Rossmann fold at large,
but may be **true for the SDR family specifically**.

### 1.5 EX-ANTE PREDICTIONS

| # | prediction | expectation written before searching |
|---|---|---|
| **P1** | A riboflavin-responsive-MADD / `ETFDH` query returns ≥1 paper reporting BOTH increased protein amount AND increased activity for a named missense | SUPPORTED |
| **P2** | The 11β-HSD2 destabilised-missense work includes an **activity** measurement under the stabilising condition, not only a half-life | SUPPORTED |
| **P3** | G6PD has a small molecule acting at a cofactor site with measured activity rescue in patient-derived cells | SUPPORTED |
| **P4** | Across all families, precedents carrying BOTH a measured abundance increase AND a measured functional rescue in the SAME missense protein are few (order of half a dozen) | SUPPORTED |
| **P5** | PMID 21476439 will not permit assignment of WWOX cofactor occupancy (crude extract), so the cofactor screen stays sign-undetermined | SUPPORTED |
| **P6** | **No** precedent will exist in which a small-molecule DRUG stabilised a pathogenic human **SDR-family** missense with measured functional rescue | SUPPORTED as an absence |

### 1.6 DISCRIMINATOR — chosen before looking

Run the cofactor-responsive vocabulary **twice**: unrestricted, and restricted to the SDR family,
each with a positive control that must fire. **If** unrestricted returns many and SDR-restricted
returns ~zero **with its positive control firing**, the absence is real *within the SDR family* and
**D4 (fold, not family)** is operative — the precedent must then be imported at the level of the
Rossmann cofactor cleft, and the transferability filter must say so explicitly. **If**
SDR-restricted returns hits, **D2 (vocabulary miss)** was operative and the gap was in the
inherited file, not in the field.

### 1.7 RESULT — including the predictions that failed

| # | outcome |
|---|---|
| **P1** | 🟢 **SUPPORTED, decisively.** Cornelius 2012 measured *"the steady-state level **and** the activity of variant ETF-QO proteins"* under riboflavin and temperature, in cells |
| **P2** | 🟢 **SUPPORTED.** Atanasov 2007: *"Enzymatic activity of Tyr(338)His was **partially retained** at 26 °C or in the presence of the chemical chaperones **glycerol and dexamethasone**"* — a measured functional rescue in a human SDR. 🔴 But the **abundance change under rescue is not stated in the abstract**, and the body is unread here |
| **P3** | 🟢 **SUPPORTED, then QUALIFIED.** Hwang 2018 found AG1; Pakparnich 2021, independently, found *"AG1 … only marginally increased G6PD enzymatic activity and stability"* |
| **P4** | 🟡 **SUPPORTED but not quantified.** A chaperone × oxidoreductase × activity query returned **14 records total**; I do not claim a census, only that the class is small. Recorded as a bounded observation, not a number |
| **P5** | 🟢 **SUPPORTED, and on design grounds rather than on the body** — see §4.2 |
| **P6** | 🟢 **SUPPORTED as an absence.** No small-molecule drug rescue of a pathogenic human SDR-family missense with a measured functional readout was found. The one SDR precedent uses an osmolyte, a temperature shift and a steroid — not a designed drug |
| 🔴 **The discriminator itself** | **D2 WON, and with a mechanically identifiable cause.** See §1.7a |

#### 1.7a 🔴 The discriminator's verdict, and the exact reason the inherited file missed the SDR precedent

The SDR-restricted chaperone query returned **4 records, none of them an SDR rescue**, and its
positive control fired (an unrelated hydroxysteroid-dehydrogenase paper came back). By the
pre-registered rule that reads as D1/D4. **It is wrong, and the reason is mechanical.**

The precedent — Atanasov 2007 — *does* contain the words *"chemical chaperones"* and *is* about a
short-chain dehydrogenase. It was missed because the gene's name is written
**`11beta-hydroxysteroid dehydrogenase type 2`**, and PubMed tokenises `11beta-hydroxysteroid` as a
single term: **the family phrase `"hydroxysteroid dehydrogenase"` does not match it.** This is
trap (a)/(c) — a hyphenated numeric prefix silently defeating a family-level phrase search — and it
is systematic: it will hide **every** `11beta-`, `17beta-`, `3beta-` HSD paper from any
family-level SDR query written that way.

🔵 **Operational consequence, and it is reusable:** any SDR family sweep in this repository must
enumerate the gene symbols (`HSD11B1/2`, `HSD17B1…14`, `HSD3B1/2`, `RDH5/11/12`, `CBR1/3`, `SPR`,
`DHRS…`, `WWOX`) **alongside** the family phrase, because the phrase alone is provably lossy.

**Two further tool traps hit and cleared in this act**, recorded so nobody repeats them:

| trap | what happened |
|---|---|
| **(f) silent OR-block drop** | A query containing `"ligand-assisted folding"` came back with that term **absent from `query_translation`** — dropped without error. Checked term-by-term; the result was re-read as a query about the *remaining* terms only |
| **(a) punctuation stripped** | `"NAD+"[Title/Abstract]` and `"NADP+"[Title/Abstract]` were translated to `"nad"` and `"nadp"` — the `+` vanished. A zero, or a hit, on either would have meant something different from what it appears to mean |
| **wildcard rejection** | A query containing the literal allele name `ALDH2*2` returned **0** records. The `*` is a wildcard the tool refuses. **That zero is meaningless**; the same question asked without it returned 23 |

### 1.8 NOVELTY ORIGIN — graded in the repository's own vocabulary, and honestly low

| element | grade | justification |
|---|---|---|
| The precedent question itself | 🔴 **`PROMPT-SEEDED`** | The brief posed it. Not my idea, not graded as one |
| The six precedents of §2 | **`CORPUS-DERIVED`** | Retrieved from literature in this act. Real work, zero conceptual novelty |
| **The tokenisation cause of the SDR miss (§1.7a)** | 🟡 **`AGENT-NOVEL`, methodological only** | Not a scientific finding. It is a reusable defect in how this repository queries its own fold family, with a stated fix |
| **The correction to §4.4's "no ligand" (§2.8)** | 🟡 **`AGENT-NOVEL`, weak, and it is a CORRECTION not a discovery** | The inherited file states the migalastat route fails on *"no substrate, no activity, no ligand"*. At abstract-depth, **the first and third are not supported**: PMID 21476439 reports steroid substrates with determined Km values, and a review asserts a named WWOX SDR-domain ligand. The *"no activity"* half stands and is still decisive |
| **Cofactor-loss-as-the-lesion (NQO1 model), §4.3** | **`CROSS-DOMAIN-DERIVED`** | The field states it plainly; I transferred it. It sharpens §4.2's sign problem but does not replace it |
| The §7 classification | **`INFERENCE`** over inherited + new material |

### 1.9 GRADE

> ## 🟡 **C — PRECEDENT IMPORT WITH ONE CORRECTION.**

**Explicitly NOT `F`.** An `F` requires a *genuinely new plausible intervention class*. This act
produced none. Every intervention named in §2 was already, in class, on the inherited ranking:
cofactor stabilisation (rank 1), small-molecule conformational correction (rank 3/4), chemical
chaperone / permissive temperature (rank 5). **What changed is the evidence under them, not the
list.** The inherited file could name **zero** SDR-family precedents with measured function; this
act names **one**, plus five in the adjacent Rossmann/flavin folds. Restating the brief as a finding
would be the failure mode the brief warned about, and it is declined here.

### 1.10 EXPERIMENT

Written prospectively; the post-search version, with its cost and what it forecloses, is §6.

> **One blot, two lanes, one split.** Load `Q230P` patient-fibroblast lysate at 50 µg/lane with an
> **SDS-soluble / SDS-pellet split**, against WT, on a luminescent denominator. It is the cheapest
> measurement in the entire file and it gates every other one: **no precedent in §2 applies to a
> protein that is never made.**

---

## 2 · 🥇 THE PRECEDENT TABLE

> 🔴 **EVERY ROW IS TRANSFERRED. NOT ONE DATUM IS ABOUT WWOX.**
> 🔴 **Inclusion rule, applied strictly:** a row is a *precedent* only if a **functional readout was
> measured under the intervention**. Rows that raise abundance without measuring function are
> included **as cautions**, marked 🚫, and are explicitly **not** precedents for this question.
> Depth is stated per row. `abstract-depth` means the body was not read here.

| # | protein (fold) | disease | variant | intervention | **measured abundance / stability change** | **measured FUNCTIONAL rescue** | evidence class · depth |
|---|---|---|---|---|---|---|---|
| **1** ⭐ | **11β-HSD2** (`HSD11B2`) — **SDR** | Apparent mineralocorticoid excess (AME) | **Y338H** (and R337H) | **26 °C permissive temperature; glycerol; dexamethasone** (a steroid ligand of the enzyme) | 🟡 **Destabilisation quantified in the untreated state**: t½ WT **21 h** → Y338H **3 h**, R337H **4 h**; degradation proteasomal. 🔴 **Abundance change *under* rescue is NOT stated in the abstract** | 🟢 **YES** — *"Enzymatic activity of Tyr(338)His was **partially retained** at 26 °C or in the presence of the chemical chaperones glycerol and dexamethasone"* | `EXPERIMENTAL`, transferred · **`abstract-depth`** · Atanasov 2007, *JASN* 18(4):1262–70, PMID 17314322, [DOI](https://doi.org/10.1681/ASN.2006111235) |
| **2** ⭐ | **ETF:QO** (`ETFDH`) — FAD oxidoreductase | Riboflavin-responsive MADD | several patient missense | **Riboflavin (FAD precursor) + temperature**, in HEK293 | 🟢 **YES — steady-state level measured** | 🟢 **YES — activity measured in the same system.** Verbatim: *"the influence of riboflavin and temperature on the **steady-state level and the activity** of variant ETF-QO proteins"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Cornelius 2012, *Hum Mol Genet* 21(15):3435–48, PMID 22611163, [DOI](https://doi.org/10.1093/hmg/dds175) |
| **3** | **ETFβ** (`ETFB`) — flavoprotein | Mild MADD | **D128N** | **FAD (flavinylation)**, incl. at 39 °C to mimic fever | 🟢 **YES, as resistance to degradation**: *"the presence of flavin **prevented proteolytic digestion** by avoiding protein destabilization"* | 🟢 **YES** — *"**FAD exerts the effect of a pharmacological chaperone**, improving ETF conformation, and yielding a more stable **and active** enzyme"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Henriques 2009, *JBC* 284(7):4222–9, PMID 19088074, [DOI](https://doi.org/10.1074/jbc.M805719200) |
| **4** ⭐ | **NQO1** — FAD oxidoreductase | cancer-risk polymorphism `NQO1*2` | **P187S** | **A designed small molecule**, N-(2-bromophenyl)pyrrolidine-1-sulfonamide | 🟢 **YES, conformationally**: *"a small molecular chaperone … **repopulates the native wild-type conformation**"* (in vitro). 🔴 **Cellular abundance not the readout** | 🟢 **YES** — *"the **enzymatic activity** of the P187S variant protein is **strongly improved** in the presence of the molecular chaperone in vitro"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Strandback 2019, *FEBS Lett* 594(3):424–38, PMID 31605637, [DOI](https://doi.org/10.1002/1873-3468.13636) |
| **4b** | **NQO1** — same | same | **P187S + H80R** | **genetic suppressor, NOT pharmacological** | 🟢 stabilisation of the FAD site | 🟢 *"**reactivates P187S** by enhancing **FAD binding affinity** through local and dynamic stabilization of its binding site"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Medina-Carmona 2017, *Hum Mol Genet* 26(18):3531–44, PMID 28911204, [DOI](https://doi.org/10.1093/hmg/ddx238) |
| **5** | **G6PD** — NADP oxidoreductase | G6PD deficiency | Canton **R459L** + several common variants | **AG1**, a small molecule found by HTS, acting via the **allosteric/structural NADP⁺ site** | 🟡 **Stability reported** (Protein Stability indexed); magnitude contested | 🟡 **YES, then QUALIFIED.** Hwang 2018: *"AG1 … **increases the activity** of the wild-type, the Canton mutant and several other common G6PD mutants"*, reduced oxidative stress in cells, zebrafish and human erythrocytes. 🔴 **Independent replication**: Pakparnich 2021 — *"**AG1 … only marginally increased** G6PD enzymatic activity and stability"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Hwang 2018, *Nat Commun* 9:4045, PMID 30279493, [DOI](https://doi.org/10.1038/s41467-018-06447-z) · Pakparnich 2021, *Sci Rep* 11:24307, PMID 34934109, [DOI](https://doi.org/10.1038/s41598-021-03800-z) |
| **5b** | **G6PD** — same | same | Class I variants | **oligomer/NADP-site stabilisation as a strategy** | 🟢 stability measured (DSF, SEC-SAXS) | 🟢 *"stabilizing the dimer and tetramer **improved protein stability** in clinical variants … with tetramerization also **improving the activity**"*; loss of allosteric NADP⁺ binding *"cause[s] the **deactivation and destabilization**"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Garcia 2022, *JBC* 298(3):101610, PMID 35065072, [DOI](https://doi.org/10.1016/j.jbc.2022.101610) |
| **6** | **ALDH2** — NAD oxidoreductase | Asian alcohol-flushing / `ALDH2*2` | **E487K** | **Alda-1**, small molecule | 🔴 **not the readout**; the mechanism is conformational, with crystal structures of the bound complex | 🟢 **YES** — *"**restores near-wild-type activity** to ALDH2*2 … by acting as a **structural chaperone**"* | `EXPERIMENTAL`, transferred · `abstract-depth` · Perez-Miller 2010, *Nat Struct Mol Biol* 17(2):159–64, PMID 20062057, [DOI](https://doi.org/10.1038/nsmb.1737) |
| **C1** 🚫 | **MVK** (mevalonate kinase) | MKD / hyper-IgD syndrome | **V377I** | **Prestwick 1280-compound FDA library**, hit = clobetasol propionate | 🟢 **YES** — NanoLuc bioluminescence of an MK-V377I–nLuc reporter increased | 🔴 **NO.** The hits act *"through **glucocorticoid receptor signaling**"* and *"**increases gene transcription of MVK**"* via SREBP-2. **Transcriptional, not stabilising, and MK activity was not the reported rescue readout** | 🚫 **CAUTION, NOT A PRECEDENT** · `abstract-depth` · Politiek 2023, *J Inherit Metab Dis* 47(2):302–16, PMID 38131282, [DOI](https://doi.org/10.1002/jimd.12698) |
| **C2** 🚫 | **HSD3B1** — **SDR** | castration-resistant prostate cancer | **1245A→C** (gain-of-stability) | **none — natural variant** | 🟢 *"a **more stable** protein that is **resistant to degradation**"* | 🟢 *"thus **increased production** of potent androgens"* — i.e. degradation rate sets enzymatic output in vivo | 🚫 **SIGN CONTROL, NOT A RESCUE** · `abstract-depth` · Sabharwal & Sharifi 2019, *Endocrinology* 160(9):2180–88, PMID 31271415, [DOI](https://doi.org/10.1210/en.2019-00366) |

### 2.7 🔴 What the table says, in four sentences

1. **Row 1 is the only human SDR-family precedent in existence that I could find, and it clears the functional bar.** A destabilising missense in a human SDR, causing a recognised Mendelian disease, had its **enzymatic activity partially restored** by a chemical chaperone, a steroid ligand and a permissive temperature. The inherited file carried this protein as a *half-life* row; it is in fact a **functional-rescue** row.
2. **The intervention in row 1 is not a drug.** Glycerol is an osmolyte, 26 °C is not a therapy, and dexamethasone's effect on 11β-HSD2 is confounded in this very literature (independent reports of glucocorticoid-mediated *inhibition*, of transcriptional *induction*, and of no effect). **P6 stands: nobody has drugged a pathogenic SDR missense back to function.**
3. **Rows 2–6 are all one fold-step away** — NAD(P)/FAD Rossmann oxidoreductases, not SDRs — and they are where the *methods* live: steady-state-level-and-activity in the same cells (row 2), cofactor-as-chaperone with a fever-temperature arm (row 3), a designed small molecule repopulating the native conformation (row 4), a structural-cofactor-site activator with an honest failed replication attached (row 5).
4. **Rows C1 and C2 are the discipline.** C1 is a well-run, well-powered abundance screen whose hits turned out to be transcriptional and whose functional rescue was never demonstrated — **exactly the outcome a WWOX abundance screen would be at risk of**. C2 shows that in a human SDR, degradation rate really does set enzymatic output — the premise the whole abundance axis rests on — but it shows it in the *gain* direction, in cancer, with no intervention.

### 2.8 🔴 One correction to the inherited file, stated narrowly

The inherited §4.4 blocks the migalastat-class route on *"no substrate, no activity, no ligand."*
At `abstract-depth` **two of those three are not supported by the record**:

- **Substrate:** PMID 21476439 reports *"a course of enzymatic reactions for **selected steroid substrates**, and determined related **Km values**."* Steroid substrates with measured Km exist in the literature, in crude extract.
- **Ligand:** a review states *"**17β-estradiol (E2) binds WWOX at an NSYK motif in the C-terminal SDR** … domain"* — Liu 2018, *Front Neurosci* 12:563, PMID 30158849, [DOI](https://doi.org/10.3389/fnins.2018.00563). 🔴 **`PREMISE: UNVERIFIED_PRIMARY`.** This is a review sentence; the primary was not located in this act, the provenance is a laboratory the repository already handles with caution, and **no Kd, no ITC, no thermal shift and no structure accompanies it anywhere I could find**. It is recorded as *a lead to verify*, not as a fact.
- **Activity:** 🟢 **the block STANDS and is still decisive.** There is no readout meeting the `PMID 28540421` standard, so amenability cannot be scored.

🔵 **Why this narrow correction matters therapeutically:** it changes *which* prerequisite is
missing. If a candidate ligand and candidate substrates exist on paper, then a first-pass ligand
experiment can be designed around a **binding/thermal-shift** readout instead of an activity
readout — which is precisely how rows 3, 5b and the inherited NmrA/SDRvv rows were done, and it
**breaks the circularity** the inherited file identified as fatal (amenability scored on activity
WWOX cannot supply). 🔴 It does **not** make the route available: it still needs purified WWOX SDR
protein, which does not exist, and the ligand claim is unverified.

---

## 3 · §6 TRANSFERABILITY FILTER — per precedent

> **Import experimental strategy. Do not pretend another SDR disease is WWOX.**

### 3.1 Row 1 — 11β-HSD2 Y338H

| | |
|---|---|
| 🟢 **WHAT TRANSFERS** | **Assay architecture:** measure half-life first, then re-measure **activity** under each stabilising condition, on the same construct, in the same cells — abundance and function scored separately and in that order. **Rescue principle:** a *thermodynamic* destabilisation produced by a point substitution in a human SDR is, at least partially, **reversible by shifting the folding equilibrium** rather than by repairing the residue. **Ligand strategy:** the enzyme's own **steroid ligand** was used as the chaperone, alongside an osmolyte — no novel chemistry, no inhibitor design. **Stabilisation mechanism:** osmolyte + permissive temperature acting on folding, with the degradation route (proteasome) established independently. **Experimental sequence:** patient → mutation → half-life → route → chaperone arms → **activity under each arm**. That sequence is directly copyable |
| 🔴 **WHAT DOES NOT** | **Substrate:** cortisol. WWOX has no established physiological substrate. **Active site:** 11β-HSD2 has a validated catalytic assay with a nanomolar Km and a clinical biomarker (the urinary THF/THE ratio); **WWOX has no activity readout at all**, which is the single most important non-transfer in this file. **Tissue:** renal cortical collecting duct epithelium vs developing CNS. **Disease biology:** a salt-sensitive hypertension of adult physiology vs a recessive developmental encephalopathy with a window problem. **Pharmacology:** dexamethasone's effect on 11β-HSD2 is *contested in its own literature* (inhibition, induction and no effect all reported) — **the compound does not transfer and neither does its sign**. **Cofactor state:** 11β-HSD2 is an **NAD⁺-preferring 11-oxidase** with its catalytic domain facing the cytoplasm; WWOX's cofactor preference, direction and occupancy are all open (§4). **Position:** Y338 sits in a **C-terminal cluster 335–339** essential for stability; `Q230P` is a **buried core backbone lesion** in the middle of the domain. Nothing about position transfers |

### 3.2 Row 2 — ETF:QO / riboflavin

| | |
|---|---|
| 🟢 **WHAT TRANSFERS** | **The two-measurement design, which is the one thing this whole question needs**: steady-state level *and* activity, same cells, same variants, one intervention axis (riboflavin) crossed with a second (temperature). **The genotype-stratified readout:** responsive, partially responsive and non-responsive variants analysed *side by side*, so the assay's dynamic range is calibrated by variants at both ends. **The Hsp60-association readout** as an orthogonal folding-defect indicator that needs no activity assay |
| 🔴 **WHAT DOES NOT** | **Cofactor:** FAD, covalently-adjacent and required for electron transfer; NAD(P) in an SDR is a dissociable hydride carrier. **Compartment:** mitochondrial matrix with a chaperonin system; WWOX is cytosolic/mitochondrial-associated with a **lysosomal** route on the one allele ever routed. **Disease biology:** a fatty-acid-oxidation crisis triggered by fever; WWOX-DEE is not episodic. **Pharmacology:** riboflavin is a vitamin with a transporter, a tissue distribution and a safety record — **none of which exists for any WWOX intervention**. 🔴 **And the decisive non-transfer:** ETF:QO variants have **residual measurable activity to raise**. `Q230P` has no measurable activity of any kind |

### 3.3 Rows 3 and 4b — cofactor / cofactor-site as the chaperone

| | |
|---|---|
| 🟢 **WHAT TRANSFERS** | **Mechanism class, stated at full strength:** in a flavin oxidoreductase, a destabilising missense can act **by lowering cofactor affinity**, and restoring cofactor occupancy restores activity — *"much lower activity … primarily due to its **substantially reduced affinity for FAD** which results from lower stability"* (Pey 2019, *Biosci Rep* 39(1), PMID 30518535, [DOI](https://doi.org/10.1042/BSR20180459)). **Stabilisation mechanism:** stabilise the *cofactor-binding site*, not the whole protein. **Experimental sequence:** ligand → Kd → conformational stability → proteolysis resistance → activity, with a **fever-temperature arm** built in. **And a design idea worth keeping:** a *genetic* suppressor (row 4b) is a legitimate proof-of-principle that a site is druggable, and costs no chemistry |
| 🔴 **WHAT DOES NOT** | **Cofactor identity and chemistry:** FAD is not NAD(P). **Active site / substrate:** quinones, not steroids. **Disease biology:** a cancer-risk polymorphism in adults vs a recessive developmental encephalopathy. **Tissue:** none of this is neuronal. 🔴 **And the premise:** NQO1's FAD dependence, Kd and holo-fraction are *measured*. **For WWOX, every one of those three numbers does not exist** — so the mechanism transfers as a *hypothesis to test*, and the numbers transfer not at all |

### 3.4 Rows 5 / 5b — G6PD and the structural cofactor site

| | |
|---|---|
| 🟢 **WHAT TRANSFERS** | **The concept of a *structural*, non-catalytic cofactor site whose occupancy sets both stability and activity** — a site a ligand can occupy **without being a substrate analogue and without inhibiting catalysis**, which is the one property the migalastat class lacks. **Assay architecture:** DSF + analytical SEC + SEC-SAXS to score oligomer state and stability together. **And the honesty:** a headline activator reported in *Nature Communications* was independently found to be only *"marginally"* effective. **That replication is itself the transferable lesson** — a single HTS hit is a starting point, not a result |
| 🔴 **WHAT DOES NOT** | **Fold:** G6PD is not an SDR and not a Rossmann SDR cleft. **Oligomer:** the whole strategy is dimer/tetramer stabilisation, and 🔴 **`WWOX homodimerises via the SDR` is `PREMISE: UNVERIFIED`** — this route is blocked for WWOX by the same gap that blocks tafamidis. **Tissue:** erythrocytes, which have no protein synthesis and a 120-day lifespan. **Disease biology:** episodic oxidant-triggered haemolysis |

### 3.5 Row 6 — ALDH2 / Alda-1

| | |
|---|---|
| 🟢 **WHAT TRANSFERS** | **The proof that a small molecule can act as a *structural* chaperone at a site adjacent to the cofactor cleft and restore near-WT catalysis in a NAD-dependent oxidoreductase carrying a single destabilising substitution.** **Method:** co-crystallise the compound with both WT and variant, and use the structure to *show* the rescue mechanism rather than infer it. That is the strongest form of mechanism evidence in this file |
| 🔴 **WHAT DOES NOT** | **Fold:** ALDH superfamily, tetrameric, not SDR. **Substrate:** acetaldehyde/4HNE. **Variant class:** E487K is a **surface-charge / subunit-interface** substitution that disorders the NAD-binding and catalytic region *at a distance*; `Q230P` is a **buried backbone** lesion with a 1.44 Å hard overlap — **a different lesion class**, and the inherited file's own §6.1 excludes the interface component for `Q230P` at SASA 0.00 Å². **Abundance:** never measured as a rescue endpoint here, so this row does **not** answer the abundance half of the question |

### 3.6 Row C1 — MVK / the FDA-library screen

| | |
|---|---|
| 🟢 **WHAT TRANSFERS, and it is the most immediately usable thing in this file** | **A destabilised missense protein C-terminally fused to NanoLuc, expressed from a defined promoter in a stable reporter line, screened against a 1280-compound FDA library, with the reporter clone chosen because it *behaved most similarly to patient fibroblasts*, and with a CRISPR knockout of the presumed mediating receptor (`NR3C1`) used to prove the mechanism of the hits.** Glycerol and a temperature axis were built into clone selection. 🔵 That architecture is **directly compatible** with the repository's existing donor-saturation NanoBRET design and would cost nothing new in principle |
| 🔴 **WHAT DOES NOT — and this is the warning** | **The screen's hits raised the reporter by raising *transcription*.** A luminescent-fusion abundance screen **cannot distinguish a stabiliser from a transcriptional inducer**, and in the one published instance of this exact design the answer was *inducer*. 🔴 **Any WWOX version of this screen must carry an mRNA arm and a cycloheximide-chase arm from day one**, or it will find the same class of hit and mean the same nothing. **Substrate, active site, tissue, disease biology and pharmacology transfer not at all** — MVK is a cytosolic kinase in an autoinflammatory disease |

---

## 4 · 🔴 §8 THE COFACTOR ISSUE

### 4.1 What the WWOX record actually says

According to PubMed, the only WWOX enzymology primary is Sałuda-Gorgul *et al.* 2011,
*Z Naturforsch C* 66(1–2):73–82, **PMID 21476439** (Medical University of Łódź; **no DOI and no PMCID
in the PubMed record**). Verbatim from the abstract:

> *"Due to its potential role in sex-steroid metabolism, **using two bacterial expression systems, we
> have cloned WWOX fusion proteins showing oxidoreductase activity in a crude extract**, defined a
> course of enzymatic reactions for selected steroid substrates, and determined related Km values.
> Our results show that the SDR domain of the WWOX protein has dehydrogenase activity and is
> **reactive both in the presence of NAD⁺ and NADP⁺ for all examined steroid substrates**. On the
> other hand, with the same substrates and **reduced cofactors (NADH and NADPH) reduction activity
> was not observed**."*

**Status of this evidence, stated plainly:** `EXPERIMENTAL`, **`abstract-depth`**, body unread.
Crude extract. No purity, no yield, no Tm, no monomer fraction, **no cofactor Kd**, and no
apo/holo determination. A 2015 review disagrees on the direction of the reaction. The paper is
**not open access and has no PMCID**; retrieval was **PARKED** rather than pursued, under
`TOOL_BLOCKED → PARK → CONTINUE` and under the brief's instruction not to open an enzymology
programme.

### 4.2 🔴 Why reading the body would not resolve the question anyway — the design argument

**P5 is supported on design grounds, which is stronger than supporting it on the body.**

The experiment reported is: express a fusion protein in bacteria, lyse, **add exogenous NAD⁺ or
NADP⁺ to the crude extract**, and observe turnover of a steroid substrate. That design answers
*"can this preparation use NAD⁺/NADP⁺?"*. It **cannot, even in principle,** answer any of the three
questions the sign problem needs:

| question the screen needs answered | can a crude-extract turnover assay answer it? |
|---|---|
| Does WWOX bind NAD(P) with a defined Kd? | 🔴 **No.** Turnover with added cofactor does not give an affinity |
| Is the protein apo or holo at physiological cofactor concentrations? | 🔴 **No.** Cofactor was added; endogenous occupancy was destroyed by lysis and swamped by addition |
| Does cofactor binding **stabilise** WWOX? | 🔴 **No.** No Tm, no proteolysis, no CD, no DSF was run |

🔴 **Therefore the cofactor occupancy state of WWOX is UNDETERMINED BY CONSTRUCTION, not merely
unmeasured — and reading the body of PMID 21476439 would not change that.** That is a stronger
conclusion than the inherited file's, and it is reached without spending the retrieval.

### 4.3 What the new precedents add to the sign problem — one sharpening, one warning

🔵 **The sharpening (rows 3, 4b, 5b).** Kabir 2016 frames cofactor occupancy as a *confounder* that
inverts the sign of a stabiliser. The NQO1 and G6PD precedents frame it as something else: **in a
flavin or NADP oxidoreductase, reduced cofactor occupancy can be the LESION ITSELF** — P187S is
inactive *because* it binds FAD poorly, and restoring site stability restores both. Garcia 2022:
loss of allosteric NADP⁺ binding *"cause[s] the deactivation and destabilization"* of Class I G6PD
variants. **If that model applied to WWOX, the cofactor would not be a nuisance variable in the
screen — it would be the target.**

🔴 **The warning, which is larger.** That model *cannot be applied to WWOX*, because it requires
knowing that WWOX is a cofactor-dependent holo-enzyme in the first place — the exact fact §4.2 shows
is undetermined by construction. And the inherited SDRvv row is the reason this is not a hedge: in a
single SDR, the two **redox states of the same cofactor** differ in affinity by **73-fold**
(Kd(NADPH) 3.5 µM vs Kd(NADP⁺) 242 µM). The 2011 WWOX result — activity with **oxidised** NAD⁺ and
NADP⁺, **none** with the reduced forms — is precisely the pattern that would place WWOX in a
**single, specific** redox/occupancy quadrant of Kabir's four. **Which quadrant is unknown, and the
sign of a candidate stabiliser differs between them.**

### 4.4 🔴 VERDICT

> ## 🔴 **`COFACTOR-SCREEN BLOCKED BY STATE UNCERTAINTY`**
>
> A WWOX stability screen run in an unknown cofactor state **could select destabilisers silently**,
> because the sign of a stabiliser inverts with occupancy (Kabir 2016) and WWOX's occupancy is
> undetermined by construction (§4.2). **No cofactor-based stabiliser screen is recommended, and
> none is designed here.**

### 4.5 The MINIMUM experiment that would unblock it — and it is deliberately small

> ⚠️ **This is one protein prep and one plate. It is explicitly NOT an enzymology programme, and it
> deliberately does not attempt kinetics, substrate identification, or a direction-of-reaction
> determination.**

**Express the WWOX SDR domain alone** (the construct boundaries the repository's structural file
already defines) as a solubility-tagged fusion in *E. coli* — **a route the literature says has
worked at least twice** (PMID 21476439's two bacterial systems) — purify one preparation, and run
**one differential scanning fluorimetry plate**:

| arm | what it reports |
|---|---|
| apo | baseline Tm — **and whether a folded, cooperatively melting WWOX SDR exists at all**, which nobody has ever shown |
| + NAD⁺ · + NADP⁺ | ΔTm and its **sign** in the oxidised states the 2011 paper reports activity in |
| + NADH · + NADPH | ΔTm and its sign in the reduced states the 2011 paper reports **no** activity in |
| + one steroid from the 2011 substrate list, ± cofactor | whether a substrate/ligand stabilises, and **whether its sign flips with cofactor occupancy** — Kabir's experiment, run once, on WWOX |

**What one plate decides:** (i) does a purified WWOX SDR fold; (ii) does it bind a nicotinamide
cofactor at all; (iii) in which redox state; (iv) **the sign** of stabilisation in each state.
Outcome (i) negative ends the cofactor axis permanently at low cost. Outcome (iv) is the single
number that converts `COFACTOR-SCREEN BLOCKED` into a designable screen.
**Cost:** catalogue reagents, one prep, one plate. **What it does NOT do:** it does not measure
function, does not identify a substrate, and **says nothing whatever about `Q230P`**, which is a
separate protein that may not be expressible at all.

---

## 5 · 🔴 §7 FINAL CLASSIFICATION

> ## 🔴 **`CURRENTLY UNTESTABLE`**
>
> **Not `LOW PLAUSIBILITY`** — the precedent dimension is now genuinely strong, and nothing found
> in this act argues that `Q230P` is unrescuable.
> **Not `PLAUSIBLE BUT UNPROVEN`** — that label implies an experiment exists that has not been
> done. **Here the experiment cannot be run**: there is no functional readout to score rescue on,
> no purified protein to stabilise, and no confirmed protein in patient cells to raise.
> **Not `MECHANISTICALLY COHERENT`** — four of the six dimensions below are unmeasured.

🔴 **This classification is NOT made on ΔΔG, and ΔΔG is given no weight anywhere in it.** The
inherited file records that for this allele the predictor ranks proline **fourth of nineteen**,
that two predictors disagree about proline specifically, and that the lesion is a **backbone**
lesion a side-chain ΔΔG predictor cannot see. That reasoning is adopted and not repeated.

### 5.1 The six required dimensions, each answered

| # | dimension | answer | evidence class | what it rests on |
|---|---|---|---|---|
| **1** | **Protein existence** | 🔴 **NOT ESTABLISHED.** Transcript normal; protein **not detected** on the one Western ever run. "Not detected" is a **detection floor**, not a zero. Nobody has loaded 50 µg/lane, used a luminescent denominator, or looked in the pellet. The epitope-artefact alternative is unexcluded | `EXPERIMENTAL`, **`abstract-depth`**, unread primary | inherited §5.1 |
| **2** | **Instability evidence** | 🟡 **PREDICTED at moderate-high confidence · 🔴 ZERO as a measurement.** SASA 0.00 Å², 1.44 Å Cδ/Glu226-O overlap, deleted i,i−4 amide H, no cheap accommodation. **No turnover, no Tm, no half-life has ever been measured for any WWOX missense** | `MODEL` + `INFERENCE`; fold-family support `EXPERIMENTAL`, transferred | inherited structural file; row 1 and Lou 2018 as transferred fold-family support |
| **3** | **Aggregation evidence** | 🔴 **NOT SUPPORTED, NOT EXCLUDED, NEVER LOOKED FOR.** No WWOX allele has ever been fractionated into soluble and pellet. My searches added no core-SDR aggregation instance — **an absence across queries, not a demonstrated negative** | `INFERENCE` | inherited §6.1; this act added nothing |
| **4** | **Functional competence** | 🔴 **UNKNOWN, and the fold-family prior is adverse.** Lou 2018: in an SDR, core substitutions gave protein *"more stable than wild type"* with *"dramatic activity loss"* in **every** case, five with no detectable activity. 🟢 **Counterweight from this act:** rows 1–6 show that destabilised oxidoreductase variants *can* be functionally competent once folded — in six proteins, including one SDR. **Neither settles `Q230P`** | `INFERENCE` from transferred `EXPERIMENTAL` | Lou 2018 vs §2 |
| **5** | 🔴 **AVAILABILITY OF A FUNCTIONAL ASSAY** | 🔴 **NONE. THIS IS THE BINDING CONSTRAINT AND IT DECIDES THE LABEL.** No WWOX readout meets the `PMID 28540421` standard. No functional measurement has **ever** been made on a WWOX missense protein whose abundance was restored — not once, for any allele. The one published WWOX rescue read out **band intensity** only. **Every single precedent in §2 scores amenability on a functional readout. WWOX cannot supply one** | — | inherited §5.4; confirmed by §2 |
| **6** | ⭐ **ANALOGOUS RESCUE PRECEDENTS** | 🟢 **YES — and this dimension MOVED in this act, from weak to strong.** **One human SDR-family precedent with measured functional rescue** (row 1) and **five in adjacent NAD(P)/FAD oxidoreductases** (rows 2–6), including a designed small molecule (row 4) and a cofactor acting as a pharmacological chaperone with both stability and activity measured (row 3). 🔴 **Bounded by:** none is WWOX, none is a neuron, none is a buried-backbone proline, **and none used a drug on an SDR** | `EXPERIMENTAL`, transferred, `abstract-depth` throughout | §2 |

### 5.2 🔴 What this classification means, and what it does not

**It means:** the obstacle is no longer *conceptual*. Before this act the honest position was "the
field has no precedent for what we would be attempting." That is no longer true. **The obstacle is
now entirely local, entirely on the WWOX side, and — importantly — mostly cheap.** Dimensions 1 and
3 are settled by one blot with a pellet lane. Dimension 2's first half is settled by the §4.5 plate.
Dimension 5 is the expensive one and it is the one that decides.

**It does not mean** that `Q230P` is rescuable, that any compound should be tried, or that
`Q230P` protein exists. It also does **not** license an abundance screen: row C1 shows what a
well-run abundance screen returns when function is not measured, and Lou 2018 shows what a
stability gain means in an SDR when activity is measured.

---

## 6 · The MINIMUM experiment that would move the classification

> 🔴 **Not the cofactor plate.** §4.5's plate unblocks the *cofactor screen*; it does not move the
> §7 classification, because it says nothing about `Q230P`.

> ## **One blot. Two lanes. One SDS-soluble / SDS-pellet split.**
>
> `Q230P` patient fibroblast lysate and matched WT, loaded at **50 µg/lane**, fractionated into
> SDS-soluble and SDS-insoluble pellet, on a luminescent denominator, with the antibody's epitope
> position looked up **before** the blot is run.

**Why this one, over everything else in this file:**

| outcome | what it decides |
|---|---|
| **Protein appears in the soluble fraction** at high load | Dimension 1 flips to **established**. The detection-floor hypothesis is confirmed, `Q230P` protein exists, and **every precedent in §2 becomes relevant at once** — the classification moves to `PLAUSIBLE BUT UNPROVEN` on the spot |
| **Protein appears in the PELLET** | Dimension 3 flips to **supported**, and 🔴 **the entire abundance-raising axis stops**, regardless of everything else in this file. Raising the level of an aggregating protein is not a therapy |
| **Nothing in either fraction, at 50 µg** | The lesion is a **folding-yield ceiling** (nothing is completed), degradation is removed as the operative step, and the classification stays `CURRENTLY UNTESTABLE` — but for a *different and now-measured* reason |
| **Epitope maps to 226–240** | The whole non-detection result is uninterpretable and must be re-run with a second antibody. **This is one line of a Methods section, and checking it costs nothing** |

**Compression:** four mechanisms, one membrane. **Deliberately excluded from the first pass:** no
chase (you cannot chase an undetectable band), no pulse-label, no purified protein (none exists),
no compound of any kind, and **no rescue arm at all** — because a rescue arm on a protein whose
existence is unestablished measures nothing.

---

## 7 · What I could not establish

| # | item | status |
|---|---|---|
| **1** | **Whether abundance rose under rescue in the one SDR precedent (row 1).** The abstract reports the activity rescue and the untreated half-lives, but not a protein-level measurement under glycerol / dexamethasone / 26 °C | 🔴 **`abstract-depth`, body unread.** The row is therefore a **function-rescue** precedent with the abundance half **unverified**, and it is labelled that way in §2 |
| **2** | **The body of PMID 21476439.** No DOI, no PMCID, not open access | 🟡 **PARKED, not retried** (`TOOL_BLOCKED → PARK → CONTINUE`). §4.2 shows the design cannot answer the occupancy question regardless, so the park costs less than it appears to |
| **3** | **The primary behind "E2 binds WWOX at an NSYK motif in the SDR domain."** Found only as a review sentence | 🔴 **`PREMISE: UNVERIFIED_PRIMARY`.** Recorded as a lead. **Not built on**, and §2.8's correction is stated so that it survives this claim being wrong |
| **4** | **Any WWOX cofactor Kd, apo/holo fraction, Tm, or purified folded SDR domain** | 🔴 **Does not exist.** Twelve records matched a WWOX × structural-biophysics query and none supplies one |
| **5** | **A numeric census of how many two-measurement precedents exist** (P4) | 🟡 **Bounded observation only.** A chaperone × oxidoreductase × activity query returned 14 records total; I report that number as a bound on my search, **not** as a count of the field |
| **6** | **Whether `Q230P` protein exists at all** | 🔴 Unchanged from the inherited file, and it is §6's whole point |
| **7** | **Any SDR-family precedent using an actual drug** | 🔴 **Searched and not found.** P6 is recorded as an **absence across the queries run**, which is weaker than a demonstrated negative |
| **8** | **Whether the C1 screen architecture would even work for WWOX** | 🔴 Untested. It requires a WWOX fusion that expresses, which for `Q230P` is dimension 1 again |

### 7.1 Hard-bound compliance, stated explicitly

Prediction and measurement are kept apart throughout (§1.5 vs §1.7; §5.1 dimension 2). Every
transferred datum is labelled transferred and carries its protein of origin. **Abundance,
stability, solubility and function are scored in separate columns in §2 and never merged.**
`EXPERIMENTAL` / `HOMOLOGY` / `MODEL` / `INFERENCE` are separated per row and per dimension. No
cross-variant generalisation is made — `P252A`, `P282A` and `Q230P` are not pooled anywhere. Flags
precede conclusions. **No external human action was taken or proposed**; no author was contacted,
no service was purchased, no spend was incurred. A `DISCOVERY` is not a `CANDIDATE` and not
`CANONICAL`, and §0 records the `FIND ISSUE → CLAIMS → CANDIDATES → DISCOVERY LEDGER` order that
preceded the trace. **Nothing here is medical advice, and no compound is recommended for any
person.**

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · The headline was verified first-hand, and every clause of the quote is exact

I re-pulled `PMID 17314322` independently. According to PubMed,
[DOI](https://doi.org/10.1681/ASN.2006111235) — Atanasov AG, Ignatova ID, Nashev LG, Dick B,
Ferrari P, Frey FJ, Odermatt A, *J Am Soc Nephrol* 2007;18(4):1262–70. The transmitted sentence
matches the abstract **word for word**, including the half-lives (21 h / 3 h / 4 h) and the
rescue clause. `MeSH`: `Enzyme Stability`, `Protein Folding`, `Thermodynamics`,
`Mineralocorticoid Excess Syndrome, Apparent`. 🟢 **VERIFIED.** Depth remains `abstract`.

## V2 · 🔴 The clause the report did not carry is the one that decides the transfer

The abstract's own conclusion: *"impaired 11beta-HSD2 protein stability **rather than** reduced
gene expression **or loss of catalytic activity** seems to be responsible."*

**That is why the chaperone worked.** `Y338H` sits in a C-terminal cluster (335–339) identified in
the same paper as *"essential for protein stability"* — i.e. the lesion is in a stability element
and the catalytic machinery is **intact**. A chaperone that restores the fold therefore restores a
functioning enzyme, because there was never anything wrong with the enzyme.

**WHAT TRANSFERS to `Q230P`:**
- An existence proof at the right taxonomic level: a **pathogenic human SDR missense**, causing a
  real disease, functionally rescued by **osmolyte** and by **permissive temperature**. This was
  the single weakest link in the chaperone argument and it is now occupied.
- Both lesions are **non-catalytic**. WWOX's catalytic triad is `S281`/`Y293`/`K297` (held in
  `wwox_sdr_function_per_molecule_census_20260921.md`); `Q230` is 51 residues N-terminal of `S281`.
  So neither case is a direct hit on the active site, and the Lou 2018 objection — that engineered
  stabilisation of an SDR cost activity — does not automatically apply to a *natural* destabilising
  lesion being restabilised.

**WHAT DOES NOT TRANSFER:**
- 🔴 **The lesions are in different structural classes.** `Y338` is a C-terminal **stability
  element**; `Q230` is **buried**, `SASA 0.00 Å²` (verified earlier this session), and the
  substitution is a **proline**, which perturbs the backbone of the core fold rather than a
  peripheral degron. A chaperone can extend the life of a protein that *can* fold. It cannot
  supply a native state to a sequence that has none. **Foldable-but-unstable and fold-incompetent
  are different diseases with the same western blot.**
- 🔴 **The dexamethasone arm does not transfer, and its mechanism is not stated.** The abstract
  labels glycerol and dexamethasone together as "chemical chaperones" and says nothing about how
  dexamethasone acts on this enzyme. Whether it is osmolyte-like or ligand-assisted is
  `PREMISE: METHODS_INVISIBLE` at abstract depth. WWOX has no verified ligand of that class
  (§4.4's own correction rests on `PMID 21476439` at `PREMISE: UNREAD_PRIMARY`). **Only the
  glycerol and 26 °C arms are safely transferable**, and those are exactly the two that need no
  ligand.

## V3 · 🎯 The proposed experiment is correct and is one plate short of being a discriminator

§7's minimum experiment — *one blot, two lanes, SDS-soluble / pellet split on `Q230P`
fibroblasts* — is the right instrument and I endorse it. But as specified its outcome
distribution is **narrow on the question that matters**: it reports whether protein is present
and where it partitions, not **why**, and both of the competing mechanisms above predict reduced
soluble protein.

**Add one arm, at zero reagent cost: run the same cells in parallel at 26–30 °C before lysis.**
This is the arm Atanasov 2007 actually used, and it is the one that separates the two states:

| Observation at 37 °C | Observation at 26–30 °C | Reading |
|---|---|---|
| low soluble, detectable pellet | **soluble fraction rises** | 🟢 **foldable but thermodynamically unstable** — the precedent set in §2 becomes applicable, and `CURRENTLY UNTESTABLE` moves |
| low soluble, detectable pellet | no change | 🔴 **fold-incompetent or degron-independent** — chaperone route loses its premise |
| nothing in either fraction | nothing | folding-yield or epitope ceiling — measured, not assumed (epitope position looked up **first**, as §7 already requires) |

Cost: one extra plate and one extra lane pair on a blot that is already being run. This is the
session's `outcome_distribution_width` rule applied — *an experiment's value is the width of its
outcome distribution, not the importance of the quantity it measures.*

⚠️ **Bound.** A permissive-temperature response is evidence about **folding**, not about
**function**. It cannot be reported as functional rescue, and §5.1's *"functional assay — NONE"*
remains the binding constraint on the whole axis. This arm makes the binding constraint **worth
paying for**; it does not relieve it.

## V4 · The tokenisation trap is accepted as a method finding and generalised

`11beta-hydroxysteroid` tokenising as a single term, so that the family phrase
`"hydroxysteroid dehydrogenase"` cannot match it, is a **seventh** distinct way a PubMed zero can
be meaningless in this corpus, alongside the six already established. It belongs with trap (f)
(a quoted term silently dropped from an `OR` block), which this delegate also hit and logged.
**Rule adopted: an SDR family sweep enumerates gene symbols beside the family phrase, always.**

## V5 · Grade

The delegate graded itself **C** and declined **F**. I agree with **C** and note it was earned in
the harder direction: the file's own headline is a precedent it found by escaping a search trap it
diagnosed, and it kept the abundance-under-rescue gap open rather than closing it by assumption.
The correction in §4.4 is narrow and correctly flagged. **No row of this file is canonical, and
none is proposed for `BATCH_COMMIT` here.**
