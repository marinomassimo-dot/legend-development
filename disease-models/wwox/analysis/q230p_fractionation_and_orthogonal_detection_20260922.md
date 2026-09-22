# `Q230P` — minimal fractionation architecture and orthogonal detection

**Date:** 2026-09-22 · **Actor:** Scientist B · **Class:** experimental architecture + reagent adjudication + one first-hand sequence derivation
**Scope:** the **WWOX-DEE genotype class** (public edition). No individual is referenced.
🔴 **Nothing here is medical advice. No dose, no route, no clinical framing. `BLOCK-1` holds.**
🔴 **No researcher was contacted. No reagent was purchased. No external correspondence of any kind.**
**Alleles, strains and species are never pooled** — every row carries its own system.

---

## 0 · THE ANSWER UP FRONT

> ## The minimal architecture that separates *absent* from *absent-from-the-soluble-fraction* is **three fractions and one arithmetic gate**, and that architecture is **already specified in this repository**. What is **not** in this repository, and what this file supplies, is the reagent set that can actually read it.

Two findings drive the file, and the second is the one that changes a standing design:

1. 🟢 **`S / P / T` is sufficient and is inherited.** The three-fraction scheme (mild-soluble `S`, strong-denaturing pellet `P`, spin-free total `T`) already exists in `wwox_missense_abundance_lysis_census_20260922.md` §4 and `q230p_minimum_discriminator_20260922.md` §1.1–1.3. I did not improve on it and I say so. What I add is the **degeneracy analysis it lacks** — which fractions answer the branch question, which answer the *foldability* question, and why those are not the same experiment (§1.5).

2. 🔴 **THE FLANKING-ANTIBODY PAIR THAT TWO PRIOR DESIGNS SPECIFY CANNOT BE BUILT.** The lysis census §4 requires *"(ii) a **C-terminal SDR** antibody (immunogen C-terminal to Q230)"*. **No such reagent is documented anywhere in this repository or in the literature this repository holds.** Of 17 censused anti-WWOX primaries, the epitope-documented ones are N-terminal (A1, A2, A6) or span 230 (A3, A5); **the C-terminal-only class is empty.** The design is not merely unfunded — as written it is **unexecutable**, and no prior file states this.
   ⇒ 🟢 **The orthogonal C-terminal arm must therefore come from a non-antibody route.** §3 supplies one, computed first-hand from a sequence that was on this disk the whole time.

---

## A · BASELINE ENUMERATION BEFORE SCORING — scope declared

🔴 **`SEARCH THE REPOSITORY BEFORE DECLARING ANY REAGENT ABSENT.`** Enumerated first, grepped second, and nothing below was guessed from a filename.

| Scope axis | What I actually used |
|---|---|
| **FILE-TYPE SCOPE** | 🟢 **UNSCOPED.** No `--include` filter. Census of the target tree taken first: `disease-models/wwox` holds **609 files — 430 `.md`, 102 `.json`, 25 `.py`, 19 `.csv`, 15 `.png`, 11 `.jsonl`, 5 `.tsv`, 2 `.pdb`**. A string inside a `.json` or a `.pdb` is invisible to a Markdown-scoped grep, and **the single most valuable object in this file came out of a `.pdb`** (§3.1) |
| **LANGUAGE SCOPE** | 🟢 **Bilingual EN/IT.** Swept `antibod\|anticorp`, `insoluble\|insolubil`, `pellet`, `lysis\|lisi`, `fraction\|frazione`, `sequential extraction\|estrazione sequenziale`. The `HPA050992` attestation is an **Italian-language bullet headed *Reagenti riusabili*** inside a canonical ledger — `discovery_ledger_current.md:623` — read first-hand this session |
| **DOCUMENT CLASS** | Registries · ledgers (discovery, therapeutic-hypotheses, claim) · full-text dossiers · deep-dive manifests (`.json`) · commit candidates · locator audits · session evaluations · the 80-file analysis corpus · structure data (`.pdb`) · `framework/`, `ledger/`, `governance/`, `learning/` |
| **AVOIDED** | Blind grep of the two large registries and `corpus_seed_pubmed_20260806.jsonl` (3.9 MB), per `framework/scripts/README.md`. Registry hits were reached through named-line reads |

**Enumerated, then read** — all ten files the brief names are present and were opened: `wwox_antibody_epitope_census_20260922.md` (59 KB) · `wwox_missense_abundance_lysis_census_20260922.md` (72 KB) · `wwox_missense_stability_census_20260922.md` · `q230p_minimum_discriminator_20260922.md` (89 KB) · `q230p_direct_discriminator_20260922.md` (81 KB) · `function_per_molecule_assay_design_20260922.md` · `wwox_sdr_function_per_molecule_census_20260921.md` · `wwox_engagement_partner_adjudication_20260922.md` · `wwox_activity_sensor_census_20260921.md` · `q230p_three_designs_one_experiment_20260922.md`.
**Found by sweeping, not named in the brief, and load-bearing here:** `proteostasis_discrimination_protocols_20260922.md` (the cross-domain solubility ladders), `p282a_control_tension_and_superscript_route_20260922.md` (§4.3), `discovery_ledger_current.md:623` and `:1698`, and `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` (§3.1).

---

## B · ABSENCE CLAIMS — stated in the required form, never as *"X does not exist"*

| # | Absence claim |
|---|---|
| **AB-1** 🔴 | **No anti-WWOX antibody with a documented epitope lying wholly C-terminal to residue 230 was identified** within [the A1–A20 antibody census, the paper/claim/literature registries, the full-text dossiers, the deep-dive manifests, the analysis corpus], in [English and Italian], across [unscoped file types under `disease-models/wwox`, `framework`, `ledger`, `governance`, `learning`], using [`grep -ril 'antibod\|anticorp\|HPA0\|abcam\|sigma-aldrich\|santa cruz\|proteintech\|Atlas Antibodies\|Prestige'`, then a line-by-line read of the census table]. The epitope-documented reagents are **N-terminal** (A1 `32–110`; A2 `≈12/16–93/94`; A6 exons 1–5 ⇒ `1–172`) or **span 230** (A3 full-length `1–414`; A5 exons 1–7 ⇒ `1–≈280`). ⚠️ Vendor datasheets are `EGRESS_BLOCKED` in this deployment, so an epitope a paper does not state **cannot be recovered here at all** — the absence is of a *documented* epitope, not proof that no such antibody is sold |
| **AB-2** | **No sarkosyl-based extraction of WWOX, in any system, was identified** within [the same document classes and scope], using [`grep -rin 'sarkosyl\|sarcosyl'`] → **zero occurrences repository-wide** |
| **AB-3** | **No formic-acid extraction step applied to WWOX was identified** within [same scope], using [`grep -rin 'formic acid'`]. Formic acid occurs **once**, as a cross-domain SOD1 precedent (`proteostasis_discrimination_protocols_20260922.md:73`, `abstract-depth`) — never applied to WWOX |
| **AB-4** | **No analysis of degeneracy between extraction fractions was identified** within [the 80-file analysis corpus], using [`grep -rin 'degenerat'`] — the four hits are *neurodegenerative*, *degenerated*, and one unrelated ratio-degeneracy note. **§1.5 is therefore new to this repository** |
| **AB-5** | **No verification that the peptides computed in §3.2 are proteotypic (WWOX-unique) could be performed** within [this deployment], using [any route]: `rest.uniprot.org`, `www.ebi.ac.uk`, `files.rcsb.org` are `connect_rejected`, no local proteome FASTA exists, and no BLAST binary is installed. 🔴 **This is an absence of verification, not a verification of uniqueness**, and §3.2 is flagged accordingly |
| **AB-6** *(inherited, not re-derived)* | **Zero** WWOX abundance measurements examined a pellet / insoluble / detergent-resistant fraction (0/12 rows, 0/4 patient-derived rows); **zero** stated a detection floor; **zero** stated an epitope position relative to the variant. `INHERITED` from `wwox_missense_abundance_lysis_census_20260922.md` §1.2 |
| **AB-7** *(inherited)* | **Zero** records of targeted MS absolute quantification of WWOX. `INHERITED` from `wwox_sdr_function_per_molecule_census_20260921.md:106` (`total_count: 0`) |

---

## C · PREREGISTERED PREDICTIONS — written before the results section, each with an explicit falsifier

🔴 **Honesty about ordering, because a retrospective prediction is not a prediction.** `P1–P3` were written before the repository sweep. `P4–P6` were written before I opened the `.pdb` and before any peptide was computed. **`P7` is marked `RETROSPECTIVE` and is scored but carries no credit.**

| # | Prediction | 🔴 Falsifier — what observation would kill it |
|---|---|---|
| **P1** | The repository already holds the soluble/insoluble split design; my contribution will be chemistry and degeneracy, not architecture | Finding no sequential-extraction design anywhere ⇒ the architecture would be mine to invent |
| **P2** | At least one anti-WWOX antibody with a documented C-terminal epitope exists in the repository, making the flanking pair executable | An exhaustive census in which **no** reagent has a documented epitope C-terminal to 230 |
| **P3** | "RIPA" in this corpus will resolve to ≥2 chemically distinct recipes | Every row labelled RIPA carrying the same SDS/DOC composition |
| **P4** | The variant-spanning tryptic peptide will be **PRM-suitable** (7–20 aa, < ~2,500 Da) | A peptide longer than 20 residues or heavier than 2,500 Da |
| **P5** | `Q230P` changes peptide **mass only**, not protease cleavage pattern, under every standard protease | Any protease for which the mutant peptide has a **different length or different boundaries** than the wild-type peptide |
| **P6** | No WWOX sequence is obtainable in this deployment (prior sessions logged UniProt/EBI/RCSB as `connect_rejected`) | A complete WWOX sequence recoverable from a local file without egress |
| **P7** `RETROSPECTIVE` | Full-length WWOX computes to ≈46 kDa, matching the literature's *"46.2 kDa"* band | A computed mass incompatible with the reported band |

---

## D · DIVERGE — five architectures for *"is it absent, or absent from the soluble fraction?"* · **the discriminator column is the value**

| # | Architecture | Distinct because it predicts **this different measurement** | 🎯 Discriminator against the others |
|---|---|---|---|
| **H1** | **Not synthesized** (translation-level failure) | Nothing above LOD in `S`, `P`, **or `T`**, with **both** detection routes, at **both** temperatures, and **no** return under degradation blockade | 🔴 Reached **by elimination**, never by measurement. Only a **nascent-labelling** assay (AHA/click + IP) can assign it positively. Must be labelled as an elimination call |
| **H2** | **Synthesized then cleared** (proteasome/lysosome) | Nothing in `S` or `P` at baseline, but a band **returns in `S`** under bafilomycin A1 or MG-132 | The **inhibitor arm** is the only thing that separates `H2` from `H1`. A pellet is *not* required to see it |
| **H3** | **Synthesized, insoluble** | 🟢 **`P` positive, `S` negative, allele-specific against two control lines** | The **pellet lane itself**. Nothing else in the set can see an aggregated species at all. `INHERITED`: this lane has never been run for any WWOX allele |
| **H4** | **Synthesized, soluble, but epitope-invisible** | `S` negative **by antibody**, `S` **positive by mass spectrometry** at the same cell-equivalents | 🟢 **Route disagreement within one fraction.** This branch is invisible to any antibody-only design, however many fractions it has — and **no prior file names it** |
| **H5** | **Synthesized, soluble, truncated or internally cleaved** | N-terminal route positive at a **reduced size**; C-terminal route negative | 🔴 **SIZE**, not presence. The 25.9 kDa vs 46.7 kDa distinction (§3.3) is the whole discriminator |

⚠️ `H4` and `H5` are the two branches a pellet alone cannot reach, and they are why §3 is not an optional refinement of §1.

---

## 1 · THE MINIMAL FRACTIONATION ARCHITECTURE

### 1.1 🔴 Classification by chemistry, never by label

**Every buffer below is placed by its recipe.** Where a paper gives only a name, the row is `COMPOSITION UNVERIFIED` and belongs to no class. `INHERITED` — the rule and both poles of its worked example come from `wwox_missense_abundance_lysis_census_20260922.md` Amendments 1 and 2; I adopt it and extend the table with the structural recovery ceiling each class carries.

| Class | Chemistry | Verbatim recipes held in this repository | 🔴 What it **structurally cannot recover** (`gate_is_not_quantity`) | What a **negative in this buffer licenses** — and what it does not |
|---|---|---|---|---|
| **C0** **Non-lytic / fixed** | Fixation + light permeabilisation. `0.1% Triton X-100 in PBS` | Steinberg 2021 IF on organoid sections (`PMID 34268881`) | **Size information — entirely.** And epitope access inside a dense aggregate; no antigen-retrieval step is described | Licenses: *"no accessible epitope in situ at this exposure."* 🔴 Does **not** license absent, degraded, soluble or insoluble. 🟢 But it is the **only** class that discards nothing, because nothing is cleared |
| **C1** **Mild non-ionic** — no ionic detergent | ≤1% NP-40 / Triton / Tween, physiological salt | 🟢 Hussain 2023: *"25 mM Tris-HCl pH 7.4, 150 mM NaCl, 1 mM EDTA, **1% NP-40** and 5% glycerol"* · 🟢 Steinberg 2021: *"50 mM Tris (pH 7.5), 150 mM NaCl, 10% glycerol, and **0.5% Nonidet P-40**"* · 🔴 **Wang 2011, LABELLED "RIPA":** *"**RIPA buffer** (100 mM HEPES pH 7.4, 150 mM NaCl, 2 mM EDTA, **0.5% Tween 20, 0.1% Triton X-100**, 1 mM DTT)"* — **neither SDS nor deoxycholate** | Detergent-resistant aggregate · inclusion bodies · amyloid-like species · cytoskeleton- and nuclear-matrix-tethered protein · anything pelleted at the clearing spin | Licenses **only**: *"below LOD in the non-ionic-soluble fraction."* 🔴 Does **not** license absent, not-made, or degraded. **This is the class that produced most of the published WWOX negatives** |
| **C2** **RIPA, correctly defined** — non-ionic **+ deoxycholate + low SDS** | ~1% non-ionic, 0.5–1% DOC, **0.1% SDS** | 🟢 Zhang 2025: *"50 mM Tris-HCl pH 7.5, **1% NP-40, 0.1% SDS, 0.5% sodium deoxycholate**, 0.15 M NaCl, 50 mM NaF, 1 mM EDTA, 1 mM Na₃VO₄, 1 mM DTT"* · 🟢 Tochigi 2019: *"minced and **sonicated** in RIPA lysis buffer (50 mM Tris-HCl pH 7.6, 150 mM NaCl, 1 mM EDTA, **1% sodium deoxycholate, 0.1% Triton X-100, and 0.1% SDS**)"* | 🔴 **SDS-resistant aggregate.** 0.1% SDS is roughly an order of magnitude below the 1–2%-plus-boiling needed to dissolve detergent-resistant species. DOC disrupts membranes and weak protein–protein contacts; it does not dissolve an inclusion | Licenses: *"below LOD in the DOC/low-SDS-soluble fraction."* 🔴 **Still does not license *absent*.** ⚠️ And the **clearing spin is identical to C1's** — the discard step does not change between the classes, which is why a C2 negative is not a meaningful upgrade on a C1 negative for this question |
| **C2-name** 🔴 | **UNCLASSIFIABLE** | Schrock 2016: *"lysed with **RIPA buffer (TFS …)**"* — composition outsourced to a catalogue number | Unknown, because the chemistry is unknown | 🔴 **Licenses nothing about solubility.** `COMPOSITION UNVERIFIED` |
| **C3** **Direct-to-SDS total** | Sample buffer, **≥2% SDS**, boiled, **no prior clearing spin** | 🟡 Wang 2011: *"disrupted in 2X sample buffer (… **4% SDS** …), **boiled for 10 min, centrifuged**"* | Whatever a post-boil spin removes — and **that spin's g-force, duration and retained fraction are unstated**. Also anything trapped in unsheared genomic DNA | 🟢 Strongest published class **in principle**; 🔴 in this instance the unquantified spin reintroduces the discard. Licenses a near-total statement **only if** the spin is specified and the supernatant/pellet relationship is stated |
| **C4** **Chaotrope resolubilisation of the pellet** | **2% SDS / 8 M urea / DTT, 95 °C + sonication** — or the published ladder `TBS → TBS + 5% SDS → TBS + 5% SDS + 8 M urea`, `100,000 × g, 1 h` | The `P` step of the inherited design; ladder verbatim from `PMID 26780369` (α-synuclein, post-mortem brain, CC BY) | True amyloid-core species that remain insoluble in SDS/urea. Native conformation and all activity — **`C4` is terminal for any functional assay** | 🟢 Licenses the positive statement *"a WWOX species exists outside the soluble fraction."* A `C4` **negative**, run beside a valid `T`, is the strongest *absence* this architecture can produce |
| **C5** **Formic acid** | Concentrated formic acid on the `C4` pellet | 🔴 **AB-3** — never applied to WWOX. Cross-domain only: SOD1, *"SDS-insoluble/**formic acid**-soluble species"*, `PMID 16563356`, `abstract-depth`, transgenic mouse spinal cord and COS-7 | Nothing, effectively — it is the ceiling | 🔴 **CUT from the minimum set.** No WWOX amyloid evidence exists to justify it, and it carries an MS-specific hazard: **formic acid formylates peptides**, adding `+27.995 Da` artefact peaks that will corrupt the §3.2 readout |

> 🔴 **Mechanical disruption is an axis independent of detergent, and no prior file separates it.** Tochigi 2019 **sonicated**; Zhang 2025 did not. Sonication shears genomic DNA and releases nuclear-matrix-trapped protein that **no detergent in classes C1–C2 will release**. Two buffers of identical chemistry, one sonicated and one not, are **not the same extraction**. Any comparison across published rows that ignores this is comparing two variables.

### 1.2 🔴 What this does to the published `Q230P` negative — precisely, and no further

Johannsen 2018 (`PMID 29808465`) reports *"normal levels of WWOX transcripts but **absence of WWOX protein**"* in donor-derived fibroblasts from two sisters homozygous at Gln230. **Its Methods are `PREMISE: METHODS_INVISIBLE`** — Springer-closed, no PMCID, PMC and Scholar-Gateway routes already failed and are logged. `INHERITED`.

⇒ **The founding datum cannot be assigned to any class in §1.1.** It is not a C1 negative or a C2 negative; it is an **unclassifiable** negative. On §1.1's own licensing column, an unclassifiable negative licenses **nothing** about solubility. 🔴 The buffer line is the single line that would resolve it, and it is three sentences of a closed Methods section.

### 1.3 · `verify_the_omitted_clause` — the sentence beside the headline

The headline everyone quotes is *"absence of WWOX protein."* The clause beside it is the authors' own mechanism list: **"impaired translation or premature degradation."**

> 🎯 **The omitted term is the third one.** The authors named branch `H1` and branch `H2`. **They did not name insolubility**, `H3`. `INHERITED`, and it is the premise of this whole line of work — but note what follows and is *not* inherited: **the authors' own two-item list maps exactly onto the two branches their buffer could not have separated from each other either.** A cleared soluble lysate cannot distinguish *not made* from *cleared*; only the inhibitor arm does. So the omission is not one branch, it is three — the published sentence offers a two-way choice that the published experiment could not have adjudicated **in either direction**.

A second omitted clause, from the decisive precedent. The Tochigi 2019 headline is that a band appeared. The sentence beside it is the authors' own dismissal: *"it is unlikely that this faint expression … would have substantial effects"*, and **they ran no functional assay on the residual species.** 🔴 `abundance ≠ function` applies to a naturally occurring residual species exactly as to a rescued one. Nothing in that paper says the `lde` rat has useful WWOX. `INHERITED`.

### 1.4 · THE MINIMAL PROTOCOL SKELETON — numbered, with the chemistry of every buffer

**Material.** `Q230P/Q230P` fibroblasts · **two unrelated** healthy-control lines · one `WWOX`-null or silenced line as true negative. Arms at **37 °C**; the 30 °C arm is **Tier 2**, conditional (§1.6). 🔴 Obtaining the lines is `HUMAN_REQUIRED` and **was not attempted**.

| Step | Operation | Chemistry, explicitly | Why this and not the obvious alternative |
|---|---|---|---|
| **0** | Split each culture; harvest at equal cell number | — | **Cell-equivalents, not protein**, is the loading currency from here on |
| **0a** | 🟢 **`T` — take before any spin** | Aliquot straight into **2% SDS / 50 mM Tris / DTT**, 95 °C 10 min, **sonicate** | 🔴 `T` is the **only lane in the design with no spin**. A design that answers a discard problem using only spin-derived lanes has doubled the discard. `INHERITED` (`q230p_minimum_discriminator` §1.3) |
| **1** | **`S`** — mild extraction | **1% NP-40 / 150 mM NaCl / 50 mM Tris pH 7.5** + protease inhibitors, 30 min on ice. Spin **16,000 × g, 20 min, 4 °C**. Supernatant = `S` | 🟢 **Class C1 deliberately** — so the `S` lane *reproduces what every published WWOX blot measured*. The point is the comparison, not a better `S`. `INHERITED` |
| **2** | Wash the pellet **once** in the same C1 buffer; spin again; **discard the wash, but record it** | — | 🔴 The wash is a **second discard**. It is the handling artefact most likely to manufacture a false double-negative — which is precisely why step 0a exists |
| **3** | **`P`** — strong resolubilisation | **2% SDS / 8 M urea / 50 mM Tris / DTT, 95 °C 10 min, + sonication to shear DNA** | 🟢 **Class C4.** 🔴 **RIPA does not substitute** — 0.1% SDS + 0.5% DOC does not dissolve detergent-resistant species (§1.1, C2). ⚠️ **Do not boil urea-containing samples above 60 °C if they will go to MS**: urea carbamylates peptides (`+43.006 Da`) at high temperature. For the blot arm, 95 °C is correct; **for the MS arm, run `P` at 37 °C in urea or swap urea for 2% SDS alone** |
| **4** | Load `S`, `P`, `T` at **equal cell-equivalents on one gel** | — | 🔴 Equal-**protein** loading of a pellet is meaningless — the pellet's composition is not the lysate's. `INHERITED`; the single commonest way this experiment is run wrongly |
| **5** | **Loading control: total-protein stain** (stain-free or Ponceau) on every lane | — | 🔴 **Never β-actin, GAPDH or α-tubulin**: they partition differently between `S` and `P` — that partitioning *is* the premise under test — and under low temperature the WWOX literature records **α-tubulin down > 70%, β-actin < 50%**. `INHERITED` |
| **6** | **Detection floor, on the same membrane** | ≥5-point dilution series of a WWOX-positive lysate | 🔴 0/12 published rows state a floor. *"Not detected"* is reported **only** as *"below X ng, N = 3."* `INHERITED`; `CLAIM 030` already carries `PREMISE: DETECTION_FLOOR` |
| **7** | 🟢 **THE ARITHMETIC GATE — run on the wild-type lane, read before any allele lane** | Does `S + P ≈ T`? | 🔴 **If `S + P < T` in the wild-type lane, the fractionation is not quantitative in these hands and NO DOUBLE BLANK IN THE EXPERIMENT MAY BE READ AT ALL.** `INHERITED` (`q230p_minimum_discriminator` §1.3). I carry it forward as the **entry gate of the §5 decision tree**, which no prior file does |
| **8** | Transcript control on the same wells | qRT-PCR | Confirms the Johannsen mRNA result reproduces **in these cells** before any protein conclusion |

### 1.5 🟢 **DEGENERACY — which fractions are interchangeable, and for which question** *(new to this repository — `AB-4`)*

**Degeneracy is question-relative.** Two fractions are degenerate when swapping them cannot change the answer to the question being asked. The architecture has **two** questions, and they have **different** degeneracy structures — which is why the "minimum number of fractions" has two different answers.

**Question 1 — the branch question: *is there WWOX outside the soluble fraction?***

| Fraction pair | Degenerate? | Why |
|---|---|---|
| **C2 extract vs C4 extract** (as the `P` step) | 🟢 **DEGENERATE** | Both answer *"yes, a species exists that the mild buffer did not recover."* The branch call (`H3` vs `H1`/`H2`) is identical either way ⇒ **collapse them into one `P` lane.** Use **C4**, because it is the one with the higher ceiling and a C2 `P` would leave a C4-only species unseen |
| **C4 vs C5** (urea vs formic acid) | 🟢 **DEGENERATE**, absent amyloid evidence | ⇒ **C5 is CUT.** `REVIVAL_TRIGGER RT-FR-01` below |
| **`S` vs `T`** | 🔴 **NOT degenerate** | They coincide **only if no insoluble pool exists** — which is the proposition under test. Assuming it is the error the whole file exists to remove |
| **`T` vs `S + P`** | 🔴 **NOT degenerate** | `T` is the only spin-free lane; it is the **recovery control** (step 7), not a redundant total |

⇒ 🟢 **Minimum for Question 1 = three fractions: `S`, `P`, `T`.** Already inherited. **I could not reduce it below three and I did not try to inflate it.**

**Question 2 — the foldability question: *what kind of insoluble?* (which selects between §5 branches B and C)**

| Fraction pair | Degenerate? | Why |
|---|---|---|
| **C2 extract vs C4 extract** | 🔴 **NOT degenerate — the collapse that was free in Question 1 is exactly what is lost here** | A species recovered by **C2** is a loosely associated, detergent-extractable assembly; one recovered **only by C4** is detergent-resistant. **Those have opposite therapeutic implications**: the first is plausibly shiftable, the second is the class in which a non-allele-specific WWOX boost *adds substrate to an aggregating species* |

⇒ 🟡 **Minimum for Question 2 = four fractions**, by splitting `P` into `P₁` (**C2**: 1% NP-40 / 0.5% DOC / 0.1% SDS, from the `S` pellet) and `P₂` (**C4**: 2% SDS / 8 M urea, from the `P₁` pellet).

> 🎯 **The load-bearing consequence, stated plainly:** the inherited two-step `S/P` design answers Question 1 and **is degenerate with respect to Question 2**. It can tell you the protein is insoluble; it **cannot tell you whether that insolubility is of the shiftable kind**. Two prior files route their chaperone reasoning through a readout that does not carry it. **The `P₁`/`P₂` split costs one extra lane and one extra spin** and is the cheapest thing in this file.

### 1.6 What is deliberately **not** in the minimum set

| Cut | Why | `REVIVAL_TRIGGER` |
|---|---|---|
| **Formic acid (C5)** | Degenerate with C4 absent amyloid evidence; formylation corrupts the MS arm | `RT-FR-01`: a C4-negative / T-positive result — i.e. mass unaccounted for after urea |
| **30 °C permissive arm** | 🔴 **Mild hypothermia is also a degradation inhibitor**, so a 30 °C shift alone does not demonstrate folding. `INHERITED` (`q230p_minimum_discriminator` §1.6). 🔴 **And never 4–22 °C** — the WWOX cold-shock confounder lives below 22 °C | Re-enters automatically on a positive `P` lane, or on a 30 °C clearance-rate measurement showing the route is unchanged |
| **Ultracentrifugation at 100,000 × g** | A bench microcentrifuge suffices for a crude split; 100,000 × g is the α-synuclein brain protocol's requirement, not this question's. `INHERITED` | A `P` lane that is positive but irreproducible across replicates |

---

## 2 · ANTIBODY / EPITOPE — what exists, and the design that cannot be built

### 2.1 The reagents, and their side of 230 · `INHERITED` from `wwox_antibody_epitope_census_20260922.md` §1.1 — **not re-derived**

| Tag | Reagent | Epitope, as attested | Side of **230** | Usable in the flanking design? |
|---|---|---|---|---|
| **A1** ⭐ | `HPA050992` · Sigma-Aldrich, **rabbit polyclonal** (HPA/PrEST class) | 🟢 **STATED:** *"directed against **amino acids 32–110 of human Wwox protein**, a sequence **100% identical** to that of rat Wwox"* | 🟢 **N-TERMINAL** — ends **120 residues** before Q230 | 🟢 **YES — the N-terminal arm** |
| **A2** ⭐ | Aldaz-lab affinity-purified, **in-house, no catalogue number** | 🟢 STATED twice: *"residues 16–93"* / *"residues 12–94"*; **plus** *"preadsorption … to a GST fusion protein containing the WWOX **WW domains** completely eliminated … reactivity"* | 🟢 **N-TERMINAL**, fixed by range **and** by competition | 🟡 Yes in principle — 🔴 **not orderable: in-house** |
| **A6** | Abcam, supplier named, **catalogue number not given** | 🟢 By exon range: *"exons 1–5"* ⇒ **aa 1–172** | 🟢 **N-TERMINAL** | 🟡 Catalogue number missing |
| **A5** | ProteinTech, catalogue number not given | 🟢 *"exons 1–7"* ⇒ aa 1–≈280 | 🔴 **SPANS 230** | 🔴 No — a spanning reagent is not a flanking reagent |
| **A3** | Huebner/Croce GST-Wwox antiserum, custom | 🟢 Immunogen = full-length **aa 1–414**; epitope **within** it **unmapped** | 🔴 **SPANS 230** | 🔴 No |
| **A11/A12** | `ab193624` / `ab129881`, **phospho-Y33** | 🟡 Anchored to `Y33` only | 🟢 N-terminal | 🔴 **No — detects only the phosphorylated form**, so it can never be an abundance arm |
| **A7–A10, A13–A17** | `ab238144`, `ab189410`, `ABN413`, CST `4045S`, `ab216660`, + five in-house | 🔴 **Epitope `UNSTATED`**; vendor datasheets `EGRESS_BLOCKED` | 🔴 **UNSTATED** | 🔴 No — an unstated epitope cannot flank anything |
| **A17** | Suzuki 2009 anti-Wwox, *lde* rat | 🟡 *"**does not recognize the C-terminal amino acid sequence** of Wwox"* | 🟡 **NOT C-terminal** — the only *negative* epitope statement in the literature | 🔴 No — it gives no boundary, so it cannot be placed |

### 2.2 🔴 `HPA050992` — exactly what attests the epitope, verified before use

**Two independent attestations, both read first-hand this session:**

1. **Primary, in a Methods section.** Tochigi 2019, `PMID 31340538` / `PMC6678113`, [DOI](https://doi.org/10.3390/ijms20143596), Methods §4.2: *"rabbit anti-Wwox (1:1000 for IH **and WB**, **HPA050992, Sigma-Aldrich**, St. Louis…)"*, with the residue range given in the Results: *"the new antibody, directed against **amino acids 32–110 of human Wwox protein**, a sequence **100% identical** to that of rat Wwox."* `INHERITED` verbatim via `wwox_antibody_epitope_census_20260922.md:399` and `:107`.
2. **Repository attestation, Italian, canonical ledger.** `discovery_ledger_current.md:623`, read first-hand: *"**Reagenti riusabili**: anti-Wwox Sigma **HPA050992** (epitopo aa 32-110, 100% identico nel ratto); APC clone CC-1; MBP clone 1; CNP clone 11-5B; NeuN A60."*

**What attests it, stated precisely:** the residue range `32–110` is attested by **the authors of the paper that used it**, in their own Results text — **not** by a vendor datasheet, which is `EGRESS_BLOCKED` in this deployment and was not fetched. 🟢 That is a stronger attestation class than a catalogue listing.

| Status | Verdict |
|---|---|
| Epitope `32–110`, N-terminal to 230 | 🟢 **VERIFIED** — two attestations, one a Methods/Results pair in a PMC body |
| 🔴 **Validation class** | 🟡 **Biological negative only** — no normal-mobility band in `lde/lde` rat brain. **Not a KO validation, not peptide-blocked.** Do not describe it as validated |
| 🔴 **Purchasable today?** | **`UNVERIFIABLE — EGRESS_BLOCKED`**, flagged **`HUMAN_REQUIRED`**. One human, one browser, ten minutes. **No purchase was attempted or proposed** |
| Decisive precedent | 🟢 A published *"no protein"* became *"present, faint, N-terminally intact"* at **46.2 kDa** **by changing the antibody and nothing else**. `INHERITED` — the in-gene demonstration that *absent* can mean *not seen* |

### 2.3 🔴 THE CORRECTION — the specified flanking pair is unexecutable

> The lysis census §4 specifies: *"**Antibodies** — **Two**… (i) an N-terminal / WW-domain antibody… and (ii) a **C-terminal SDR** antibody (immunogen C-terminal to Q230)."*
> **Per `AB-1`, reagent (ii) does not exist in anything this repository holds.** The design's own hardest requirement — *"Both epitopes stated in the write-up by residue range"* — **cannot be met on the C-terminal side by any documented anti-WWOX antibody.**

This is not a funding problem or an access problem. It is a **specification problem**, and two prior designs carry it unflagged. Three consequences:

1. 🟢 **The N-terminal arm is solved** (A1, with a caveat class stated).
2. 🔴 **The C-terminal arm must be non-antibody.** §3 supplies it.
3. ⚠️ **An epitope tag is not a general substitute:** a C-terminal tag requires a construct, therefore a **heterologous/transfected arm**, and **can never be applied to patient fibroblasts**. `INHERITED`. §3.4 states which questions each arm can and cannot answer.

---

## 3 · ORTHOGONAL DETECTION — the antibody-independent C-terminal arm

### 3.1 🟢 **FIRST-HAND — the WWOX sequence was on this disk the whole time**

Prior sessions recorded the sequence as unobtainable: *"no FASTA could be fetched (UniProt, EBI both `connect_rejected`), no SDR-family MSA could be built"* (`q230p_structural_mechanism_20260922.md:583`). **That is true of egress and false of the repository.**

`disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` — one of the **2 `.pdb` files** the §A file-type census surfaced — carries the complete sequence in its `ATOM` records. I parsed it this session.

| Check | 🟢 Result, **FIRST-HAND** |
|---|---|
| Residue numbering | **1-based**, contiguous, **first residue 1, last residue 414, 414 residues, no gaps** |
| **Length** | **414 aa** — matches UniProt `Q9NZC7` canonical |
| 🎯 **Wild-type residue at 230** | **`Q` (Gln)** — 🟢 **CONFIRMED.** Context `215–245`: `ALPWSLTK DGLETTF` **`Q`** `VNHLGHFYLVQLLQD` |
| **Wild-type residue verified at every control position used anywhere in this repository** | `W44` = **W** 🟢 · `P47` = **P** 🟢 · `Y33` = **Y** 🟢 · `P252` = **P** 🟢 · `P282` = **P** 🟢 · `Y293` = **Y** 🟢 · `G372` = **G** 🟢 · `A141` = **A** 🟢 — **8 / 8 concordant**. No off-by-one anywhere in this repository's variant labels |
| **Computed full-length average mass** | **46.68 kDa** — 🟢 cross-checks the literature's *"46 kDa"* and Tochigi's **46.2 kDa** band |

🔴 **Bound, stated:** an AlphaFold model's sequence is the **deposited UniProt sequence**, so this verifies *internal numbering consistency and this repository's variant labels*. It is **not** an independent re-sequencing, and `exon9_cryptic_acceptor_test_20260922.md:137` already flags a possible error in the deposited `Q9NZC7` sequence at a **different** residue (354). **Nothing here inherits confidence about position 354.**

### 3.2 🟢 **FIRST-HAND — the protease map, computed on that sequence**

Cleavage rules applied: trypsin after `K`/`R` **not before `P`**; GluC after `D`/`E` not before `P`; chymotrypsin after `F`/`Y`/`W`/`L` not before `P`. Monoisotopic residue masses, `+H₂O`.

**(a) The variant-spanning peptide, three proteases:**

| Protease | Wild-type peptide | `Q230P` peptide | Verdict |
|---|---|---|---|
| **Trypsin** | **223–249**, 27 aa, `DGLETTFQVNHLGHFYLVQLLQDVLCR`, **3157.60 Da** | **223–249**, 27 aa, `DGLETTF`**`P`**`VNHLGHFYLVQLLQDVLCR`, **3126.60 Da** | 🔴 **Δ = −31.0058 Da**, same boundaries. **27 residues / 3.16 kDa is too long and too heavy for routine PRM** (target 7–20 aa). Contains **`C247`** ⇒ carbamidomethylation `+57.0215` must be added to both. **`P4` REFUTED** |
| **GluC** | **227–245**, 19 aa, `TTFQVNHLGHFYLVQLLQD`, **2272.16 Da** | **227–245**, 19 aa, `TTF`**`P`**`VNHLGHFYLVQLLQD`, **2241.16 Da** | 🟢 **The better allele-specific target** — 19 aa, no Cys, no Met, Δ = **−31.0058 Da**, boundaries unchanged |
| **Chymotrypsin** | **230–234**, 5 aa, `QVNHL`, 609.32 Da | **226–234**, **9 aa**, `ETTF`**`P`**`VNHL`, **1056.52 Da** | 🔴🎯 **NOT A MASS SHIFT — A CLEAVAGE-SITE ABOLITION.** Residue 229 is `F`. Chymotrypsin cleaves after `F229` in the wild type; in `Q230P` the new proline **blocks that cleavage**, so the upstream boundary retreats to `L225` and an entirely **different peptide of different length** appears. **`P5` REFUTED** |

> 🎯 **`P5`'s refutation is the most transferable thing in this file.** A proline substitution is not only a mass change: **it can delete a protease cleavage site**, because essentially every common protease refuses to cut `X–P`. Any targeted-MS design for a `→Pro` variant that assumes *"same peptide, lighter by 31 Da"* is **correct for trypsin and GluC here and wrong for chymotrypsin** — and would be wrong for trypsin too if residue 229 had been `K` or `R`. **It is `F`; I checked** (§3.1). This generalises to every `→Pro` allele in any gene.

**(b) 🟢 The flanking PRM pair — the antibody-independent replacement for the reagent `AB-1` says does not exist.** Tryptic, 7–20 aa, no Met, no Cys, no missed cleavage:

| Peptide | Position | Mass (monoisotopic, neutral) | Side of **230** | Role |
|---|---|---|---|---|
| `VVVVTGANSGIGFETAK` | **126–142** | 1647.883 Da | 🟢 **N-TERMINAL** | 🥇 **N-arm.** ⚠️ It is the SDR **Rossmann-fold glycine-rich cofactor motif** — sequence-conserved across the SDR superfamily, so it is the **peptide in this list most at risk of not being proteotypic** (`AB-5`) |
| `SVQHFAEAFK` | **189–198** | 1162.577 Da | 🟢 **N-TERMINAL** | 🥈 N-arm alternate — closer to 230, and not in a conserved motif |
| `LAFTVDDNPTKPTTR` | **90–104** | 1674.858 Da | 🟢 **N-TERMINAL** | N-arm alternate, adjacent to the `HPA050992` epitope ⇒ **cross-checks the antibody directly** |
| `VIVVSSESHR` | **255–264** | 1111.599 Da | 🟢 **C-TERMINAL** | 🥇 **C-arm — the reagent that does not exist as an antibody** |
| `FTDINDSLGK` | **265–274** | 1108.540 Da | 🟢 **C-TERMINAL** | 🥈 C-arm confirmatory |
| `TTYLDPR` | **83–89** | 864.434 Da | 🟢 N-TERMINAL | Short; inside the A1 epitope region |

🔴 **`AB-5` applies to every row: proteotypicity is UNVERIFIED and unverifiable here.** No BLAST, no local proteome, `rest.uniprot.org` and `www.ebi.ac.uk` `connect_rejected`. **A one-hour check by one human with a browser resolves it** — `HUMAN_REQUIRED`. **Until then no peptide above may be used as a quantitative standard**, and `VVVVTGANSGIGFETAK` should be assumed guilty.

⚠️ **Buffer/MS compatibility, from §1.4 step 3**: run the `P` fraction for MS **without 95 °C urea** (carbamylation `+43.006`) and **without formic acid** (formylation `+27.995`).

### 3.3 🟢 SCORE EVERY BAND BY SIZE — the predicted sizes, computed first-hand

| Species | Residues | Computed mass |
|---|---|---|
| **Full-length WWOX** | 1–414 | 🟢 **46.68 kDa** |
| N-terminal fragment ending at the variant | 1–230 | **25.86 kDa** |
| C-terminal fragment from the variant | 231–414 | **20.84 kDa** |
| SDR core only | ~120–414 | **32.90 kDa** |
| WW1+WW2, the `HPA050992` epitope region | 1–110 | **12.85 kDa** |

⇒ A `HPA050992` band at **~47 kDa** and one at **~26 kDa** are **different molecular claims**. Presence alone cannot tell them apart; **size can, and size is free.**

### 3.4 🔴 WHAT EACH DISAGREEMENT PATTERN LICENSES — and what it does not

> 🔴 **DO NOT INFER TRUNCATION MERELY BECAUSE TWO ROUTES DISAGREE. Antibody disagreement is a discriminator, not a molecular conclusion.** What converts a disagreement into a conclusion is **size** plus **both floors**.

| Pattern (N-route = `HPA050992` 32–110 · C-route = PRM `VIVVSSESHR` 255–264) | 🟢 Licenses | 🔴 Does **NOT** license |
|---|---|---|
| **N⁺ at ~47 kDa · C⁺** | Full-length WWOX is present in that fraction, intact across 230 | Anything about folding, activity or localisation |
| **N⁺ at ~26 kDa · C⁻** | *"A species bearing the N-terminal epitope migrates below full length, and the C-terminal peptide is below its stated LOD."* 🟡 **Consistent with** an N-terminal fragment | 🔴 **"The protein is truncated."** Not until you exclude: (i) the C-peptide's LOD and ionisation efficiency, (ii) non-proteotypicity (`AB-5`), (iii) **post-lysis proteolysis** — a fragment made in the tube, not in the cell, which a protease-inhibitor-free control detects, (iv) differential extraction of the two species |
| 🎯 **N⁺ at ~47 kDa · C⁻** | 🟢 **A technical failure of the C-route, almost certainly.** A 47 kDa species carrying residues 32–110 **must** contain residue 264 — there is not enough mass for it not to | 🔴 **Never truncation.** **This is the row where SIZE adjudicates the disagreement and presence alone would have concluded the opposite.** Fix the MS, do not re-model the protein |
| **N⁻ · C⁺** | Either the N-terminal epitope is masked/modified, or an N-terminally processed species exists | Truncation at the N-terminus — an HPA polyclonal against 32–110 can be defeated by a single modification |
| **N⁻ · C⁻ in `S`; N⁺ or C⁺ in `P`** | 🟢 **`H3` — insoluble.** The founding *"absence"* was a fraction artefact | That the insoluble species is foldable, or of the shiftable class — **that needs `P₁`/`P₂` (§1.5)** |
| **N⁻ · C⁻ in `S`, `P` **and** `T`, both floors stated, gate step 7 passed** | The strongest absence this architecture can produce | 🔴 **Not `H1`.** *Not made* and *cleared below LOD* remain degenerate until the **inhibitor arm** runs. Reached by elimination — **must be labelled so** |

### 3.5 Which arm can answer which question

| Question | **Patient-fibroblast arm** (endogenous, no construct) | **Heterologous/transfected arm** (construct + C-terminal tag) |
|---|---|---|
| Is the endogenous `Q230P` protein absent or insoluble? | 🟢 **YES — this is the only arm that can answer it** | 🔴 No — CMV-driven over-expression changes folding load, degradation flux and aggregation propensity |
| Is there a C-terminal detection route? | 🟡 **MS only** (§3.2) — 🔴 **no tag is possible without a construct**, therefore no tag on patient cells, ever | 🟢 Yes — and **the tag's terminus must be stated in writing.** 🔴 The failure to do so is a live defect in the corpus: `pCMV-3Tag` has both N- and C-terminal members and the paper does not say which (A18) |
| Engagement per molecule at matched expression | 🔴 **No** — endogenous level can be observed, not set | 🟢 Yes — this is what the transgene plate is for |
| Does the result transfer to the genotype class? | 🟢 Directly | 🟡 Indirectly, and **never as a substitute** |

---

## 4 · FUNCTION COMES AFTER MOLECULAR STATE

> ## 🔴 `ABUNDANCE ≠ FUNCTION` · `SOLUBILITY ≠ FUNCTION` · `STABILITY ≠ FUNCTION`
> **No chaperone or proteostasis result counts as therapeutic rescue without a functional readout.**

**The cross-domain constraint, `INHERITED` and not re-derived.** **Lou 2018** (`PMID 29141528`, an unrelated SDR): stabilisation and activity **anti-correlated** across an engineered panel. **Atanasov 2007** (`PMID 17314322`): a pathogenic human SDR missense (11β-HSD2 `Y338H`) functionally rescued by osmolyte + permissive temperature. 🎯 **They disagree, and that is the point**: in an SDR, stability and activity are decoupled **with a sign that depends on where the lesion sits**. Neither predicts `Q230P`; together they forbid assuming either direction.

### 4.1 What each candidate readout actually interrogates

| | **POLE4 engagement** | **GSK3β engagement** |
|---|---|---|
| **Which domain** | 🔴 **UNMAPPED.** No fragment mapping, no deletion series, no WW control. `PREMISE: NOBODY_LOOKED` | 🟢 **aa 388–407 required.** `L404A` abolishes binding in GST pull-down **and** cellular co-IP; `L311A` does not; `Δ286`/`Δ389` do not bind — five orthogonal assays, one point mutation |
| **Which activity** | A protein–protein interaction, nominated from **261 IP-MS partners by a DNA-repair pathway filter — not by interaction strength** | A **linear C-terminal docking motif** presented to a kinase |
| **Which compartment / condition** | 🔴 **Nucleus, and only after UV.** *"without UV" / "no UV" / "untreated" / "mock"* = **0** in the body — **every measurement in existence was made after UV** | 🟢 Cytosolic, **basal**, with an **endogenous co-IP from mouse brain** — the only non-oncological row in the inventory |
| **Blind to** | Everything non-nuclear, everything unstressed, and — because the site is unmapped — **it cannot report the fold of any domain** | SDR catalysis, cofactor binding, WW-domain function, and 🔴 **whether the SDR core is folded at all** — a linear motif at the extreme C-terminus may be presented by an unfolded chain. It sits **158 residues** from Q230 |
| **Distance from Q230** | Undefined | 158 residues |

### 4.2 Verdict — retain both? No. And **"redundant" is the wrong word**

- **`GSK3β` — 🟢 RETAIN, as a *ruler*, in its strong direction only.** Loss ⇒ *something global has happened*. 🔴 **A normal reading is close to uninformative for `Q230P`**, and a low one is ambiguous between *the fold is gone* and *the protein is gone* — which is exactly why §1's abundance gate must run first, at matched input. `INHERITED`, and I endorse the demotion from numerator to ruler.
- **`POLE4` — 🔴 NOT REDUNDANT, BUT NOT YET A READOUT.** It genuinely interrogates a **different compartment and a different stress state** than GSK3β, so it is not the same measurement. ⚠️ **But its credential chain is broken at every link** (`INHERITED`, `q230p_minimum_discriminator` §4.3): its only allele anchor is **`P282A`**, its binding site is unmapped, and a residue lying inside a domain does not make its partner a reporter of that domain's fold. **Plus a disqualifier specific to this experiment: a UV-dependent numerator is the wrong instrument for a fibroblast experiment whose purpose is to avoid stress artefacts**, and UV perturbs the very clearance axes the inhibitor arm manipulates.
  ⇒ **Simplify to GSK3β for the fibroblast arm.** `POLE4` survives **only** on the transgene plate where its ±UV gate can actually be run. 🎯 **The distinction matters: "redundant" would mean cutting it forever; "unqualified" names what would bring it back** — fragment mapping of the POLE4 site on WWOX, plus a non-UV baseline.
- 🔴 **F-3, the honest ceiling, carried forward unchanged.** Both are **engagement proxies, not function**. WWOX has **no demonstrated physiological function, no assigned substrate and no validated cellular activity readout**. Commissioning one is a programme decision, `HUMAN_REQUIRED`, and **this file does not propose one**.

### 4.3 🔴 `P282A` — what it actually is, and the only control roles it can serve

| | |
|---|---|
| **What it is** | **`rs3764340`, a common SNP**, carried through case-control association studies across **seven** cancers, with **18 healthy homozygous cancer-free adult controls** and a **null homozygous meta-analysis model**. Measured on a **CMV-driven Flag transgene in thyroid carcinoma lines**. Stability **normal**; POLE4 binding lost; growth/invasion suppression lost. The authors themselves: *"the precise molecular mechanism underlying the loss-of-function of the WWOX `P282A` variant is **still unknown**."* `INHERITED`, verified first-hand in `p282a_control_tension_and_superscript_route_20260922.md` |
| 🔴 **CANNOT serve as** | A complete-function-null control · a pathogenic-allele comparator · an anchor for any reporter's credential · evidence that any partner reports domain integrity. **A common polymorphism reported as a complete loss of tumour-suppressive activity is an internally strained pair of statements, not a null allele** |
| 🟢 **CAN serve as** | **(i) A within-figure NEGATIVE stability control.** It is a variant that **does not** destabilise, run in the same figure as `P252A`, which does. That is genuinely useful: it demonstrates the stability assay can return *normal*, which protects against reading every result as loss. **(ii) An assay-level positive control for the POLE4 co-IP readout only** — a condition known to lose that band, so that *"no band"* is not silently a technical failure. **Both roles are about the assay, never about the allele.** |
| ⚠️ Note on its companion | `P252A`'s reduced POLE4 binding is attributed by the authors to *"the **low abundance** of the unstable `WWOX^P252A^` mutant"* — 🎯 **an abundance confound in the only comparison that could have calibrated the reporter.** This is `ABUNDANCE ≠ FUNCTION` failing inside the source paper itself |

### 4.4 Order of operations — not negotiable

**F-0 · the gate.** §1 returns a row. **No engagement number is worth reading until it does.**
**F-1 · cheapest, same material.** If a soluble species exists: endogenous **GSK3β** co-IP or proximity assay from the **soluble** fraction **at matched WWOX input**, read only in its strong direction. 🔴 **Matched input is the binding constraint; on a low-abundance allele it may be unreachable — in which case F-1 is not run, and says so.**
**F-2 · per molecule.** Transgene plate only. `BRET₅₀` and `BRET_max` in **separate channels**; every curve fitted to **both** hyperbolic and linear models, because a quasi-linear curve is **bystander transfer from crowding** and reads as preserved engagement if the test is skipped. `INHERITED`.

---

## 5 · CHAPERONE DECISION TREE — mapped onto the §1–§4 readouts

> ## 🔴 **CLASSIFICATION: `CHAPERONE PROGRAM — MECHANISTIC QUALIFICATION`. Not a screen, not a candidate list, not a therapeutic route. NO COMPOUND SCREEN IS PROPOSED HERE OR ANYWHERE BELOW.** `INHERITED` and carried unchanged.
> **Refused by name so nothing returns as "obvious":** no compound library, no repurposing sweep, no 4-PBA or TUDCA (wrong compartment), no NAD(P)/cofactor arm (**the sign of a cofactor stabiliser inverts with occupancy**, and WWOX's occupancy, preference and direction are all unknown), no dexamethasone, **no molecule proposed for any person.**

### 5.0 🔴 ENTRY GATE — read before any branch

**Step 7 of §1.4: does `S + P ≈ T` in the WILD-TYPE lane?**
- 🔴 **NO ⇒ the tree is VOID.** No double blank may be read, and no branch may be selected. Fix the fractionation and re-run.
- 🟢 **YES ⇒ proceed.** *(No prior file places this gate at the head of the therapeutic tree; it belongs there, because every branch below turns on whether a blank lane is real.)*

### 5.1 The branch table — which readout pattern selects which branch

| Readout pattern (`S` · `P₁` · `P₂` · `T` · MS · inhibitor · 30 °C) | Branch | Call |
|---|---|---|
| `S`⁻ `P`⁻ `T`⁻ MS⁻ · **signal RETURNS under bafilomycin A1 or MG-132** · transcript normal | **A** — synthesized → unstable/degraded | 🟡 **`CHAPERONE/PROTEOSTASIS HIGH PRIORITY` — as a QUALIFICATION.** 🔴 The recovered protein's **function is unmeasured**, and the cross-domain pair (§4) shows recovered abundance is compatible with complete functional failure. **Priority to qualify, not licence to screen** |
| `S`⁻ · **`P₁`⁺** (detergent-extractable), allele-specific vs **two** controls, band scored at **~47 kDa** | **B-shiftable** — insoluble, loosely associated | 🟢 **`FOLDING/CHAPERONE ROUTE PLAUSIBLE`** — the branch where a folding lever could plausibly bite |
| `S`⁻ · `P₁`⁻ · **`P₂`⁺ only** (SDS/urea-resistant) | **B-resistant** | 🔴 **Folding route implausible; and a non-allele-specific WWOX BOOST IS ACTIVELY DANGEROUS — it adds substrate to an aggregating species.** `INHERITED`. 🎯 **This branch and the one above are the pair the inherited two-step `S/P` design is DEGENERATE BETWEEN (§1.5). Without `P₁`/`P₂` you cannot tell them apart, and they have opposite therapeutic consequences** |
| Abundance restored (inhibitor **or** 30 °C) · **GSK3β engagement at matched input still low** | **C** | 🔴 **`ABUNDANCE RESCUE INSUFFICIENT`.** The Lou 2018 direction. **Stop the proteostasis route; the lesion is not quantity** |
| `S`⁻ `P`⁻ `T`⁻ MS⁻ **both routes, both floors stated** · inhibitor **negative** · transcript **normal** | **D** | 🟡 **`TRANSLATION / RNA / EXPRESSION ROUTE`** — 🔴 **reached BY ELIMINATION and must be labelled so.** A positive assignment requires **nascent labelling (AHA/click + IP)**, which this architecture does not contain |
| Anything else — faint `S` at an **unexpected size**; `P`⁺ but **not allele-specific**; route disagreement per §3.4 | **E** | 🟡 **Discriminating follow-up:** the **four-fraction ladder** (§1.5) **+ the MS flanking pair** (§3.2) **+ the protease-inhibitor-free control** (post-lysis proteolysis) |

### 5.2 The four qualification conditions — status today

| # | Condition | Status | Moved by |
|---|---|---|---|
| **(a)** | A `Q230P` protein population exists | 🔴 **UNKNOWN.** Nobody has looked in the pellet for **any** WWOX allele in **any** system | Branch B or A. 🔴 On branch D the programme **stops**, it does not proceed at reduced confidence |
| **(b)** | Instability/misfolding experimentally supported | 🔴 **NOT SUPPORTED.** ThermoMPNN's `+1.514 kcal/mol` carries **no** weight — the predictor is **anti-correlated** with every WWOX abundance measurement that exists | An allele-specific `P` lane the controls do not show. 🔴 **A ΔΔG prediction is not a measurement, and a 30 °C response alone is not one either** |
| **(c)** | That state can plausibly be shifted | 🔴 **UNTESTED for WWOX.** Only the **osmolyte** and **temperature** arms of the 11β-HSD2 precedent transfer; **dexamethasone does not** | Observed movement of mass from `P` to `S` under a defined condition |
| **(d)** ⭐ | **A functional readout exists** | 🔴 **NOT SATISFIED — TODAY, FOR ANY WWOX ALLELE, AT ANY PRICE** | 🎯 **This is the binding condition and the reason the classification is a QUALIFICATION and not a screen** |

**Status unchanged by this file:** `TX-003` and `HYP-20260709-02` remain **conditional**. This file supplies no basis for de-conditioning either. 🔴 **No therapeutic class is forced.**

---

## 6 · WHAT IS GENUINELY NEW HERE — strict

| Item | Verdict |
|---|---|
| The `S` / `P` / `T` three-fraction architecture, equal cell-equivalents, total-protein stain, dilution-series floor, 30 °C caveat, `S+P≈T` gate | 🔴 **INHERITED** — `wwox_missense_abundance_lysis_census` §4, `q230p_minimum_discriminator` §1.1–1.3. **Not mine. I could not improve it.** |
| *Classify buffers by recipe, never by name*; both poles of the RIPA example | 🔴 **INHERITED** — Orchestrator Amendments 1 and 2 |
| `HPA050992`, its `aa 32–110` epitope, and the *"absent → present by changing the antibody"* precedent | 🔴 **INHERITED** — `discovery_ledger_current.md:623` + the antibody census. **Verified, not re-derived** |
| POLE4's broken credential chain; GSK3β as ruler; the `P282A`/`rs3764340` tension; the chaperone qualification conditions | 🔴 **INHERITED** — `q230p_minimum_discriminator` §4.3/§5, `p282a_control_tension…` |
| PRM/SRM with a heavy standard as a route (`T8`) | 🔴 **INHERITED** — `wwox_sdr_function_per_molecule_census:136` |
| **Structural recovery ceiling per buffer class, and what each negative licenses (§1.1)** | 🟢 **NEW** |
| **Mechanical disruption as an axis independent of detergent (§1.1)** | 🟢 **NEW** — no prior file separates sonicated from non-sonicated rows |
| **Fraction degeneracy analysis; the `P₁`/`P₂` split; the finding that the inherited `S/P` design is DEGENERATE between the shiftable and resistant insolubility branches (§1.5, §5.1)** | 🟢 **NEW, and the most consequential thing in this file** — `AB-4` |
| 🔴 **That the specified C-terminal flanking antibody DOES NOT EXIST in anything this repository holds, making two prior designs unexecutable as written (§2.3, `AB-1`)** | 🟢 **NEW** |
| **The WWOX sequence recovered from a local `.pdb`; 414 aa; Gln230 confirmed 1-based; 8/8 control residues confirmed; 46.68 kDa computed (§3.1)** | 🟢 **NEW, FIRST-HAND** |
| **Protease map: the GluC 19-mer as the preferred allele-specific target; `Δ = −31.0058 Da`; and `Q230P` ABOLISHING a chymotryptic cleavage site (§3.2)** | 🟢 **NEW, FIRST-HAND** |
| **The flanking PRM peptide pair — `VVVVTGANSGIGFETAK` (N) / `VIVVSSESHR` (C) — as the antibody-independent replacement for the missing C-terminal reagent (§3.2)** | 🟢 **NEW, FIRST-HAND** |
| **The disagreement-licensing table, including the row where SIZE overturns what presence would conclude (§3.4)** | 🟢 **NEW** |
| **The `S+P≈T` gate promoted to entry gate of the therapeutic decision tree (§5.0)** | 🟢 **NEW placement** of an inherited check |

🔴 **What I explicitly did NOT claim as first:** the solubility/insolubility question, the pellet lane, the two-antibody principle, the permissive-temperature arm, the inhibitor panel, and targeted MS. **All six were already here.** *(Two recent delegates proposed as first measurements an experiment published in 2018; this table exists so that does not happen again.)*

---

## 7 · PREDICTION OUTCOMES

| # | Prediction | Outcome | What actually happened |
|---|---|---|---|
| **P1** | Architecture already held; my delta is chemistry and degeneracy | 🟢 **CONFIRMED** | `S/P/T` was fully specified in two files. §1.5 and §3 are the delta |
| **P2** | A C-terminal-epitope antibody exists in the repository | 🔴 **REFUTED — and this is the file's most useful refutation** | **Zero of 17.** Two prior designs specify a reagent that does not exist (`AB-1`, §2.3) |
| **P3** | "RIPA" resolves to ≥2 distinct chemistries | 🟢 **CONFIRMED** | A Tween/Triton buffer with **neither** DOC nor SDS (Wang 2011) and a genuine DOC+SDS buffer (Tochigi 2019) both carry the name |
| **P4** | Variant-spanning tryptic peptide will be PRM-suitable | 🔴 **REFUTED** | **27 aa / 3157.60 Da**, and it contains `C247`. ⇒ GluC's 19-mer adopted instead |
| **P5** | `Q230P` changes mass only, not cleavage pattern | 🔴 **REFUTED** | **Chymotrypsin: the new proline abolishes the `F229` cleavage site** — different peptide, different length, not a mass shift. Generalises to every `→Pro` allele |
| **P6** | No WWOX sequence obtainable in this deployment | 🔴 **REFUTED** | It was in `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` on this disk |
| **P7** `RETROSPECTIVE` | ≈46 kDa full length | 🟢 **CONFIRMED** (no credit — recorded after the computation) | **46.68 kDa**, against the literature's 46 kDa and Tochigi's 46.2 kDa band |
| **—** | Is `Q230P` absent or insoluble? | 🔴 **UNTESTED — and NOT RESOLVED** | **No experiment was run. This file is an architecture, not a result.** The question remains open and the founding datum remains unclassifiable (§1.2) |

**4 refuted, 2 confirmed, 1 retrospective, 1 untested.** Three of the four refutations changed the design.

---

## 8 · NEW TOOL TRAPS — described so the next actor does not repeat them

| # | Trap |
|---|---|
| **T-1** 🔴🎯 | **`EGRESS_BLOCKED ≠ DATA_ABSENT`.** Prior sessions recorded *"no FASTA could be fetched (UniProt, EBI both `connect_rejected`)"* and proceeded as though the WWOX sequence were unavailable. **It was on disk the whole time**, inside `WWOX_Q9NZC7_AlphaFold.pdb`. **A `.pdb` file IS a sequence file** — its `ATOM` records carry the full residue list. ⇒ **Before recording an external route as blocking, census the local file types.** The `.pdb` extension was **2 files out of 609** and is invisible to any `--include=*.md` sweep |
| **T-2** 🔴 | **The `X–P` protease rule.** Trypsin, GluC and chymotrypsin all refuse to cleave before proline. A **`→Pro` variant can therefore DELETE a cleavage site**, producing a peptide of different length and boundaries rather than the expected mass shift. Verified here for chymotrypsin at `F229`–`Q230P`. 🔴 **Always check the residue immediately N-terminal to a `→Pro` substitution**: had residue 229 been `K` or `R` instead of `F`, the **tryptic** design would have broken too |
| **T-3** | **Arithmetic, caught in-session.** `Gln → Pro` is **−31.0058 Da**, not −30. I mislabelled it once mid-computation and the recomputation caught it. Any allele-specific PRM window built on −30 misses the peak |
| **T-4** | **Buffer artefacts that masquerade as protein species in MS.** Urea above ~60 °C **carbamylates** (`+43.006 Da`); formic acid **formylates** (`+27.995 Da`). Both are introduced by exactly the strong-extraction chemistry this architecture requires ⇒ the blot arm and the MS arm need **different `P` preparations** (§1.4 step 3) |
| **T-5** | **A UniProt namespace adjacency in this repository.** `discovery_ledger_current.md:1698` correctly cites **`UniProt P49841` — canonical 420 aa** — for **GSK3β**. WWOX is **`Q9NZC7`, 414 aa**. A reader grepping `UniProt` in this repo meets a 420-residue canonical isoform that **is not WWOX**. Both entries are correct; the adjacency is the hazard |
| **T-6** *(confirmed, inherited)* | **PubMed `[All Fields]` does not index Methods or supplements — and antibody catalogue numbers live in Methods.** `WWOX AND ("HPA050992" OR …)` returns **0** for a catalogue number verbatim in a PMC body. 🎯 **That zero is a worked demonstration of the failure mode, not evidence.** I therefore ran **no** reagent-existence query in this session: the route is known non-informative, and the repository was the correct instrument |
| **T-7** *(inherited, respected)* | The **`Q230P` namespace trap** — a bare `"Q230P"` returns 2 records, **neither WWOX**, both **GTPBP3** `c.689A>C (p.Q230P)`, one carrying a *measured aggregation result*. 🔴 **Not cited here, anywhere.** Note the coincidence that makes it dangerous: **GTPBP3's nucleotide change is `c.689A>C`, identical to WWOX's.** Two genes, same cDNA coordinate, same substitution, same three-character label |

---

## 9 · WHAT I COULD NOT ESTABLISH · `HUMAN_REQUIRED` — parked, not pursued

| # | Open item | Route that would close it |
|---|---|---|
| **H-1** | Johannsen 2018's lysis buffer and antibody — **the single line that classifies the founding negative** | Springer-closed, no PMCID; PMC and Scholar-Gateway logged as failed. **One human, one institutional login.** 🔴 **No author was contacted and none will be** |
| **H-2** | Whether `HPA050992` is purchasable today | One browser, ten minutes. 🔴 **No purchase proposed** |
| **H-3** | Proteotypicity of the §3.2 peptides (`AB-5`) | One BLAST/PeptideAtlas query per peptide. 🔴 **Until done, no peptide is a quantitative standard** |
| **H-4** | Access to `Q230P/Q230P` fibroblasts | Requires contacting the holding institution. 🔴 **`HUMAN_REQUIRED`; not attempted** |
| **H-5** | A validated WWOX activity readout meeting the `PMID 28540421` standard (active-site **and** cofactor-site mutants each abolishing it) | 🔴 **Does not exist. A programme decision, deliberately not proposed here** |
| **H-6** | Whether the `SDR homodimerisation` premise holds | 🔴 **`PREMISE: UNVERIFIED` — carried as such, used as a fact nowhere in this file.** Our structure is a **monomer with the interface unmodelled**. It once got amplified into a therapeutic fork; it does not get amplified here |

---

## V0 · SHADOW TRACE

- **BASELINE** — File-type census first (609 files; **430 `.md`, 102 `.json`, 11 `.jsonl`, 2 `.pdb`**), then unscoped bilingual grep, then read. Confirmed all ten named files present; **found four load-bearing files the brief did not name**, including the `.pdb` that supplied §3.
- **DIVERGE** — Five architectures (§D), each defined by a different predicted measurement. 🟢 **`H4` (soluble-but-epitope-invisible) and `H5` (truncated) are new to this repository's branch set** and are the two a pellet alone cannot reach.
- **CONNECT** — α-synuclein sequential ladder (`PMID 26780369`), SOD1 three-step ladder (`PMID 16563356`), the SDR stability/activity pair (Lou 2018 vs Atanasov 2007). 🔴 **All four cross-domain and all four already in the repository — I connected, I did not import.**
- **PREDICT** — Seven predictions with falsifiers, ordering declared honestly, one marked `RETROSPECTIVE` and given no credit (§C).
- **SEARCH** — 🔴 **PRODUCED NOTHING EXTERNAL, DELIBERATELY AND BY DESIGN.** No PubMed query was run: `T-6` establishes the route is structurally blind to reagents named only in Methods, which is the entire reagent class at issue, and `T-7` makes a bare-label query actively hazardous. **The repository was the correct instrument and it answered.** ⚠️ The cost is real and is stated: **`AB-1` is bounded by what this repository holds, not by the world** — a C-terminal anti-WWOX antibody may well be sold and merely undocumented here.
- **ADJUDICATE** — **4 of 7 predictions refuted, and three of the four changed the design**: `P2` removed a specified reagent and forced the MS arm; `P4` moved the allele-specific target from trypsin to GluC; `P5` produced `T-2`. `P6`'s refutation produced §3 entirely.
- **REVISIT** — 🟢 Revisited the inherited `S/P` design and found it **degenerate between two branches with opposite therapeutic consequences** (§1.5) — the one place where re-examining an inherited answer, rather than extending it, was the whole value. 🔴 **Revisited and left standing, unchanged:** the three-fraction minimum, the `S+P≈T` gate, GSK3β-as-ruler, and the chaperone qualification. **Nothing was changed merely to have changed something.**

---

**Not medical advice.** No dose, no route, no clinical recommendation. `BLOCK-1` holds throughout.
**Read-only session.** No canonical file, registry, ledger, receipt or queue was modified. **No git command was run.** This is the only file written.
