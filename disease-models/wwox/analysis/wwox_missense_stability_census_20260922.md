# WWOX missense stability census — has the stability, abundance, solubility or turnover of ANY WWOX missense variant ever been MEASURED?

**Actor:** Scientist S · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** NON-CANONICAL. This file touches no registry, no queue, no ledger, no receipt chain, no
state manifest. It proposes; the Orchestrator verifies and lands.
**Nothing here is medical advice.** No molecule, dose, route or safety claim is recommended anywhere below.
**Genotype classes are held apart throughout and never merged.** A measurement on one variant is
never carried to another.
**Read depth declared per row.** `full-text` = served body read in this act · `abstract-depth` =
PubMed metadata only · `repo-held` = verbatim quotation already in this repository, not re-fetched
here · `panel` = a figure read by a prior wave.

---

## VERDICT UP FRONT

**No stability, solubility, aggregation propensity or turnover rate has ever been measured for
`Q230P`. Not once, in any system, by anybody.** What exists for `Q230P` is a **single abundance
endpoint** — normal transcript, protein not detected on one Western blot of patient fibroblasts
(Johannsen 2018) — whose authors explicitly left two causes open and tested neither.

Across the whole gene, **exactly six** WWOX missense variants carry any protein-level measurement at
all, and **exactly one** of them (`P252A`) has a measured turnover, route and chaperone contact —
and that one variant is **ClinVar `Benign`**, measured on a CMV-driven Flag transgene in thyroid
carcinoma lines, in a person who had no WWOX-related nervous system disease.

And the decisive negative result of this census is not an absence but a **discordance**: when the six
measured variants are ranked by the repository's own ThermoMPNN ΔΔG, the ranking is **inverted**
against the measurements. The variant with the **highest** predicted ΔΔG has demonstrably **normal**
protein in two independent matrices; the variant with the **lowest** predicted ΔΔG is the only one
with **demonstrated accelerated degradation**. §6.1.

🔴 **Therefore: `Q230P`'s folding fate is NOT knowable from existing evidence, and the in-silico
evidence this repository holds cannot be promoted, weakened or "leaned on" — for this protein it is
empirically anti-correlated with every measurement that exists.** The sign of a non-allele-specific
WWOX boost cannot be established today. It requires new wet work, and the cheapest experiment that
settles it is specified in §8.

---

## 1 · Enumeration of every WWOX missense variant the repository records

The repository records missense at three very different depths. They are enumerated separately
because collapsing them is exactly how a benign oncology point mutant acquires the standing of a
disease allele.

### 1.1 Tier A — disease-associated missense the repository *reasons with* (narrative + registry level)

Enumerated by `git grep` over `HEAD` (committed tree only, to avoid self-contamination), counting
three-letter HGVS occurrences across `disease-models/wwox/`. Counts eyeballed from the raw grep
output, not relayed from a summary.

| Variant | 3-letter | cDNA | ClinVar class in the repo's own export | Repo occurrences (3-letter form) |
|---|---|---|---|---|
| `Q230P` | p.Gln230Pro | c.689A>C | **Pathogenic/Likely pathogenic**, multiple submitters | 48 |
| `P47T` | p.Pro47Thr | c.139C>A | **Pathogenic**, no assertion criteria | 20 |
| `P47R` | p.Pro47Arg | c.140C>G | **Pathogenic**, no assertion criteria | 16 |
| `G372R` | p.Gly372Arg | c.1114G>C | **Pathogenic/Likely pathogenic**, multiple submitters | 13 |
| `L239R` | p.Leu239Arg | c.716T>G | **Conflicting classifications** | 3 |
| `C299R` | p.Cys299Arg | c.895T>C | **Likely pathogenic**, single submitter | 5 |
| `A141T` | p.Ala141Thr | c.421G>A | **Conflicting classifications** | 7 |
| `T12M` | p.Thr12Met | c.35C>T | **Likely pathogenic**, single submitter | 13 |
| `E17K` | p.Glu17Lys | c.49G>A | **Conflicting classifications** | 9 |
| `G137E` | p.Gly137Glu | c.410G>A | **Conflicting classifications** | 4 |
| `G137V` | p.Gly137Val | — | (not resolved in the export) | 6 |
| `A141T` | — | — | — | (see above) |
| `M352I` | p.Met352Ile | c.1056G>C | **Pathogenic**, single submitter | 5 |
| `G355R` | p.Gly355Arg | c.1063G>C | **Likely pathogenic**, no assertion criteria | 10 |
| `S304Y` | p.Ser304Tyr | — | **absent from this ClinVar export** | 24 |
| `H46Y` | p.His46Tyr | — | — | 5 |
| `D58N` | p.Asp58Asn | — | — | 5 |
| `G62R` | p.Gly62Arg | — | — | 4 |
| `V190L` | p.Val190Leu | — | — | 4 |
| `F237L` | p.Phe237Leu | — | — | 4 |
| `P252A` | p.Pro252Ala | c.754C>G | 🔴 **Benign**, multiple submitters, no conflicts | 148 (1-letter) |
| `P282A` | p.Pro282Ala | c.844C>G | 🔴 **Benign**, multiple submitters, no conflicts | 4 |
| `L291P` | p.Leu291Pro | — | — | 5 |
| `R310P` | p.Arg310Pro | — | — | 5 |
| `G315R` | p.Gly315Arg | — | — | 4 |
| `M326I` / `M327I` | — | — | — | 4 each |
| `F348S` | p.Phe348Ser | — | — | 4 |
| `S390R` | p.Ser390Arg | — | — | 4 |
| `M374I` | p.Met374Ile | — | — | 4 |
| `L371T` | p.Leu371Thr | — | — | 5 |
| `M1T` / `M1L` | — | — | initiator-codon, not strictly missense | 5 each |
| `Q353H` | p.Gln353His | — | — | 3 |
| `G414S` | p.Gly414Ser | — | — | 3 |

⚠️ **The list above is not complete and must not be treated as complete.** §1.3.

### 1.2 Tier B — engineered / oncology point mutants, NOT disease alleles

These appear at high frequency in the repository and are routinely mistaken for disease variants in
casual reading. They are designed substitutions from cancer-biology papers.

| Mutant | What it is | 1-letter occurrences in `HEAD` |
|---|---|---|
| `Y33R` | designed, abolishes C1q-induced apoptotic morphology (Chang lab, EGFP fusion) | 159 |
| `K274R` | designed | 153 |
| `L404A` | designed; lies in the `ERLIQ` locus; named in the WWOX–GSK3β trap | 97 |
| `Y293F` | designed, conservative, **catalysis-abolishing and fold-preserving by design** | 25 |
| `Y85W` | **reverse** mutation restoring WW2's canonical tryptophan | 22 |
| `S281A`, `K297A`, `Q191A`, `Q406A`, `L187A`, `L311A`, `S161A`, `Y112F`, `Y34F`, `W44F`, `P47A`, `S35G`, `V190A`, `K63R`, `K100R`, `Y287F` | designed alanine/conservative scans | see grep |

🔴 **`P252A` and `P282A` sit in an uncomfortable middle.** They are germline variants of a real
person — and they are **ClinVar `Benign`**, and the repository already holds, verbatim, that *"the
cancer patient harboring germline homozygous P252A and P282A variants did not suffer from
WWOX‐related nervous system disease"* at age 35. They are the **only** WWOX missense variants with a
measured turnover. §4.

### 1.3 Tier C — the bulk ClinVar census, and what it means for "enumerate, do not assume"

`disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` (committed) holds **1,327 rows**.
Filtering to rows whose `protein` field has missense shape (`p.Xxx###Yyy`, excluding `Ter` and
synonymous `=`) gives **465 missense-shaped variants**, eyeballed by direct count, classified:

| ClinVar classification | count |
|---|---|
| Uncertain significance | **400** |
| Conflicting classifications of pathogenicity | 29 |
| Benign | 10 |
| Likely pathogenic | 6 |
| *(blank)* | 5 |
| Pathogenic | 5 |
| Benign/Likely benign | 4 |
| Likely benign | 4 |
| Pathogenic/Likely pathogenic | 2 |

**So the denominator is 465, the measured numerator is 6, and 400 of the 465 are VUS.**
The repository "records" 465 WWOX missense variants in the sense of holding a ClinVar row for each.
It reasons with roughly 30. It has a protein-level measurement for **six**. Any statement of the
form *"WWOX missense variants are…"* is, at best, a statement about 6/465 = **1.3%** of them.

---

## 2 · Repository sweep — locators, verbatim quotes, measurement vs prediction

Method: `git grep -n <term> HEAD -- disease-models/wwox/` throughout, against the **committed** tree,
so that nothing written by this session can be found by this session. Terms swept: `western blot`,
`immunoblot`, `half-life`, `cycloheximide`, `pulse-chase`, `solubilit*`, `insoluble`, `aggregat*`,
`thermal shift`, `DSF`, `melting`, `proteasom*`, `MG132`, `lysosom*`, `chaperon*`, `Hsp70`, `Hsp90`,
`turnover`, `degradation rate`, `misfolding`, `abundance`, `protein level`, `stabilit*`, each crossed
against every Tier-A and Tier-B variant token.

### 2.1 What the repository holds that IS a measurement

**(a) `Q230P` — abundance only.**
`disease-models/wwox/registries/claim_registry_current.md:355` (`CLAIM 019`, `consolidated baseline`),
`repo-held`, primary = Johannsen 2018, PMID 29808465:

> *"Johannsen et al. 2018, Neurogenetics 19(3):151-156 (PMID 29808465) studia **esattamente Q230P** in
> due sorelle omozigoti. Nei **fibroblasti di paziente**: **qRT-PCR → livelli di trascritto WWOX
> normali; Western blot → proteina WWOX non rilevata**. Gli autori lasciano aperte due alternative:
> **traduzione compromessa oppure degradazione prematura**. Non misurano sintesi, solubilità, emivita
> o via di smaltimento. Il DATO è quindi l'endpoint `mRNA normale + proteina non rilevata`, non un
> meccanismo post-traduzionale."*

And the primary's own abstract, `abstract-depth`, re-read today
([DOI](https://doi.org/10.1007/s10048-018-0549-5)):

> *"Functional studies showed normal levels of WWOX transcripts but absence of WWOX protein. … This
> could be explained by the functional data indicating an impaired translation or premature
> degradation of the WWOX protein."*

**Class: ABUNDANCE. Not stability, not solubility, not turnover.** `PREMISE: DETECTION_FLOOR` already
stands on it in `CLAIM 030` (registry line 559): *"non rilevata non è assente: la soglia
dell'immunoblot non è misurata."* The repository's own paper-registry note names the missing pieces:
*"Da recuperare dal PDF: N e controlli del WB, densitometria, e soprattutto **se sia stata testata
l'inibizione del proteasoma o un chaperone chimico**"* (`paper_registry_current.md:6358`). No PMCID
is listed for PMID 29808465 and no PMC body exists; the `n`, the controls and the densitometry are
**unread to this day**.

**(b) `P47T` — abundance, twice, in two matrices, both NORMAL.**
Human: `paper_registry_current.md`, PAPER 042 (Mallaret 2014), `repo-held` verbatim:

> Western blot on the **`P47T`** patient's fibroblasts (**passages 10/13/14 vs 4 controls**) →
> *"similar amounts of the mutant and wild-type WWOX protein"*; *"the mutation does not alter global
> protein levels"*.

Mouse, knock-in, neural tissue — Hussain 2023, PMID 36828035, PMC10835625, read `full-text` in this
act ([DOI](https://doi.org/10.1016/j.pneurobio.2023.102425)):

> *"To determine whether the P47T mutation affected the gene and protein expression, we measured mRNA
> and protein levels in CB samples. The average mRNA expression levels between and CB were comparable,
> with no significant difference in n = 6 mice tested in each group. **Western blot analyses also
> showed similar levels of Wwox protein expression in homozygous mutant and wildtype mice** (see, Wwox
> 10% input panel)."*

⚠️ **The repository's own receipt `FTR-20260826-36828035-01` already carries the correct bound and it
must ride with the quote:** *"the protein evidence is the 10% input lane of a pull-down blot, not a
dedicated quantified western, and the pull-down is n=2/group."* Confirmed from pixels in
`FTR-20260826-36828035-02`. **Class: ABUNDANCE, qualitative, n=2 visually.**

**(c) `G372R` — abundance, once, qualitative, in a progenitor compartment.**
Steinberg 2021, PMID 34268881, PMC8350905, `repo-held` verbatim in
`nascimento_accession_and_g372r_20260922.md` §3.2:

> *"while in the VZ of WPM F2 and WPM M3, WWOX was detected, **barely any signal was observed in WPM
> D1 and S1**, consistent with WWOX levels in the iPSCs (Appendix Fig)."*

Method: **immunofluorescence in situ**, forebrain-organoid ventricular zone. **n = 2 affected
homozygotes vs 2 heterozygous carrier parents, same family.** Not quantified — no densitometry, no
intensity ratio, no statistic. The iPSC corroboration sits in an Appendix figure PMC does not
distribute. **Class: ABUNDANCE, qualitative, comparator arm is itself a carrier genotype on a
baseline the same paper calls widely variable.**

**(d) `P252A` — the only measured TURNOVER in the gene.**
Zhang 2025, PMID 41124647, PMC12767083, *Adv Sci*, `repo-held` verbatim in
`missense_proteostasis_matrix_20260921.md` and
`data/redteam/provenance_data_vs_inference.csv`:

| Measurement | Verbatim / record | Class |
|---|---|---|
| mRNA control | *"the mRNA level of WWOX mutant was not decreased"* | transcription excluded |
| Degradation | *"the WWOX mutant exhibited significantly **enhanced protein degradation**, compared to its wild-type counterpart and the WWOX mutant"* | **TURNOVER** |
| Method | *"To determine the **half-life** … a **CHX chase** assay was performed … 50 µg mL CHX … 0, 2, 4, 6, 8, and 10 h"* | **cycloheximide chase** |
| Proteasome | *"MG-132 treatment **did not** induce the accumulation of WWOX, WWOX, and WWOX proteins"* | route: not proteasomal |
| Lysosome | *"lysosome inhibitors, chloroquine (CQ) and NH₄Cl treatment, **restored** WWOX protein level … whereas no significant effect … with 3-MA"* | route: lysosomal, non-macroautophagic |
| Chaperone contact | *"co-IP revealed an interaction between **HSC70** and WWOX mutant protein, but not wild-type WWOX protein and WWOX mutant protein"* | **chaperone binding** |
| Ubiquitin | P252A is **strongly K63-polyubiquitinated** (`provenance_data_vs_inference.csv:9`) | not ubiquitin-free |
| Localisation | colocalises with **LAMP1** (generic lysosome), **not LAMP2A** | route under-determined |

🔴 **Four bounds that must never be stripped from this row, each already in the repository:**
1. **The `t½` number was never reported.** The string `half` occurs **once** in the whole body — the
   Methods sentence of intent. *"Significantly enhanced protein degradation"* is an adjective; the
   quantity the assay was performed to obtain appears nowhere in the text.
2. **CMV-driven Flag transgene**, not endogenous, not knock-in, not patient-derived.
3. **CAL-62 anaplastic thyroid carcinoma / BCPAP / HEK293T / nude-mouse xenograft.** `neuron` 0,
   `seizure` 0 in the body.
4. **`SDR`, `ADH` and `short-chain` occur ZERO times in the body.** Placing P252 in the SDR span is
   **the reader's arithmetic, not the paper's claim** (`missense_proteostasis_matrix_20260921.md` row 6).
5. **ClinVar `Benign`**, multiple submitters, no conflicts. A measured degradation route on a benign
   allele is not a mechanism for a pathogenic one.

**(e) `P282A` — the standing demonstration that abundance and function are separable.**
Same paper. `discovery_ledger_current.md:1104`, `repo-held`:

> *"**Corollario scomodo (DATO). P282A**: stessa domain SDR, **proteina stabile, nessun HSC70** — e
> **funzione completamente persa**. → **Stabilità e funzione sono separabili nel SDR di WWOX.**
> 'Stabile ma inerte' è un **fenotipo dimostrato**, non più un timore."*

**Class: a NEGATIVE stability result with a positive control in the same figure** — the strongest
form of "no stability defect" in the whole census, because the assay demonstrably detected a defect
in the sister construct.

### 2.2 What the repository holds that is NOT a measurement, and must never be promoted

| Item | Locator | Why it is not a measurement |
|---|---|---|
| ThermoMPNN ΔΔG `Q230P` **+1.514 kcal/mol** | `data/WWOX_ThermoMPNN_saturation.csv` (value eyeballed at position 230, Q→P) | **Deep-learning prediction.** Never calibrated against a WWOX measurement. §6.1 falsifies it. |
| ESM-2 650M LLR `−9.08` | `analysis/README.md` pipeline | **Evolutionary likelihood.** Not a physical quantity. |
| AlphaFold relSASA `0.000`, α-helix placement | `data/WWOX_Q9NZC7_AlphaFold.pdb` | **Static model of a monomer.** The repository's own limit: *"relSASA e SSE sono calcolati su un **monomero**, ma WWOX **omodimerizza via SDR** e l'interfaccia non è modellata"* (`discovery_ledger_current.md:852`). |
| pLDDT high in SDR | same | Confidence in the *structure*, not in a stability prediction. Same locator. |
| *"rescuable window"* ΔΔG 0.8–3.5 heuristic | `WWOX_pathogenic_missense_classified.csv`; `discovery_ledger_current.md:838` | 🔴 **Already self-declassed:** *"**La finestra non discrimina.**"* |
| C299R *"acts via catalysis"* | `data/redteam/premises_epistemic_table.csv:13` | 🔴 **Already RETRACTED** by the repo's own second audit: SG(C299)–NZ(K297) = 10.7 Å, the earlier 3.4 Å was a backbone contact. |
| Aldaz & Hussain 2020 on `G372R` abundance | `nascimento_accession_and_g372r_20260922.md` §3.1 | 🔴 **A review sentence.** §7. |

### 2.3 Verified zeros in the repository — `PREMISE: NOBODY_LOOKED`

| Question | Any WWOX variant | Evidence for the zero |
|---|---|---|
| Nascent-synthesis rate (pulse labelling, ³⁵S, AHA-click, SUnSET, ribosome profiling) | **none, ever** | `missense_proteostasis_matrix_20260921.md` row 1: *"**Translation: no evidence at all, in either paper.**"* |
| Soluble / insoluble fractionation | **none, ever** | same row: *"no soluble/insoluble fractionation, so 'protein not detected' on a soluble lysate has never been separated from 'protein present but insoluble'"* |
| Thermal shift / DSF / CD melting / urea denaturation on a **disease** variant | **none, ever** | §3.4 — the only WWOX biophysics that exists covers residues 16–91 and tested no disease variant |
| Aggregation assay on a WWOX missense protein | **none, ever** | `git grep` for `aggregat*` × variants returns only the Chang-lab TRAPPC6AΔ/TIAF1/tau cascade, which is about **partner** proteins, not about a WWOX missense protein |
| Chemical/pharmacological chaperone on any WWOX allele | **none, ever** | `discovery_ledger_current.md:807`: *"I chaperoni chimici (4-PBA, TUDCA) … **non compaiono in nessuno di questi paper**"* — corroborated by a clean PubMed zero, §3.3 |
| Any degradation assay on `Q230P` itself | **none, ever** | `data/redteam/discriminating_experiment.md:4`: *"**Q230P — the actual patient allele — has never been assayed for degradation, HSC70 binding, or lysosomal routing.**"* |
| Protein or transcript work on `L239R` | **none** | `l239r_intraallelic_comparator_20260921.md` §4: *"This paper contributes **no** protein-level or transcript-level datum."* |

---

## 3 · Literature sweep — queries verbatim, `query_translation`, counts, and what each rests on

🔴 **Standing caution, established today and confirmed below: for a search about METHODS, a PubMed
zero is nearly worthless.** `[All Fields]` does not index Methods, supplements or data-availability.
Every verdict below states what it rests on.

### 3.1 The variant-string block, and the five ways a zero lies

| # | Query verbatim | `query_translation` (abridged where identical) | n | Reading |
|---|---|---|---|---|
| Q1 | `WWOX AND "Q230P"` | `("wwox protein human"[Supplementary Concept] OR … OR "wwox"[All Fields]) AND "Q230P"[All Fields]` | **0** | **Expansion FLAWLESS on both terms. The zero is still FALSE.** See Q3. |
| Q2 | `WWOX AND "p.Gln230Pro"` | `WWOX AND "p.Gln230Pro"` — 🔴 **echoed UNEXPANDED** | **0** | **Meaningless.** Trap (a), punctuation in a quoted string. Exactly as predicted in the brief. |
| Q3 | `"Q230P"` | `"Q230P"[All Fields]` | **2** | 🔴 **Neither is WWOX.** Both are **GTPBP3** (PMID 41957021 *Nat Commun* 2026; PMID 38515655 *Heliyon* 2024). **A coincidence of nomenclature, not evidence — see §3.6.** |
| Q4 | `WWOX AND "230P"` | `… AND "230P"[All Fields]` | **0** | Consistent with Q1. |
| Q5 | `WWOX AND Gln230` | `… AND "Gln230"[All Fields]` | **1 → PMID 29808465** | ✅ **The positive control fires.** |

🔴 **Q1/Q5 together are the cleanest proof of trap (e) I have produced.** Johannsen 2018 — *the*
`Q230P` paper, whose title is *"A novel missense variant in the SDR domain of the WWOX gene leads to
complete loss of WWOX protein…"* — is **invisible** to `WWOX AND "Q230P"` with a perfect expansion of
both terms, because its abstract spells the residue `Gln230` and never the string `Q230P`. **A
PubMed zero on a variant string in this gene carries no information whatsoever.**

**`G372R` compounds the trap with a sixth failure mode, newly observed today:**

| # | Query verbatim | `query_translation` | n | Reading |
|---|---|---|---|---|
| Q6 | `"G372R"` | `"G372R"` — 🔴 **echoed UNEXPANDED** | **0** | Meaningless. |
| Q7 | `WWOX AND G372R` | `WWOX AND G372R` — 🔴 **echoed UNEXPANDED** | **0** | Meaningless. |
| Q8 | `WWOX AND ("G372R" OR "Gly372" OR "P47T" OR "Pro47" OR "c.1114G" OR "c.140C")` | `… AND ("Gly372"[All Fields] OR "P47T"[All Fields] OR "Pro47"[All Fields] OR "c.1114G"[All Fields] OR "c.140C"[All Fields])` | **2** | 🔴 **NEW TRAP (f): `"G372R"` was SILENTLY DROPPED from the OR block.** The translation contains five of the six terms. A quoted term can vanish from an expanded query without any error being raised, and the result count then silently under-reports. **Recommend this be added to the tool-trap register.** |

Q8's two hits: **PMID 36828035** (Hussain 2023, `P47T` knock-in — §2.1b) and **PMID 39868255**
(De La Cruz 2025 bioRxiv, `Wwox` partial-LoF sepsis; no missense stability content).

### 3.2 The method block — and the 100% miss rate, re-verified

| # | Query verbatim | `query_translation` | n | What it rests on |
|---|---|---|---|---|
| Q9 | `WWOX AND cycloheximide` | `("wwox protein human"[Supplementary Concept] OR … OR "wwox"[All Fields]) AND ("cycloheximid"[All Fields] OR "cycloheximide"[Supplementary Concept] OR "cycloheximide"[All Fields] OR "cycloheximide"[MeSH Terms])` | **0** | 🔴 **BOTH TERMS EXPAND PERFECTLY AND THE ZERO IS FALSE.** Zhang 2025 (PMID 41124647) ran a CHX chase on WWOX P252A with a full Methods paragraph. **Miss rate 100%. Re-verified today.** |
| Q10 | `WWOX AND ("protein stability" OR "thermal stability" OR "thermal shift" OR "differential scanning fluorimetry" OR "circular dichroism")` | full expansion, all five terms present | **4** | 37897534, 35716775, 31230746, 25595191 — **not one is a disease-missense stability measurement.** §3.4. |
| Q11 | `WWOX AND ("pulse-chase" OR "half-life" OR turnover OR "protein degradation")` | ⚠️ `turnover` drew a **wrong MeSH expansion** (`"personnel turnover"[MeSH Terms]`) alongside the correct free-text term — **the MeSH limb is discarded, not counted** (trap d) | **7** | 41677633, 37897534, 34359949, 34109992, 29067327, 25447306, 19144635 — **every one is about WWOX regulating OTHER proteins' turnover** (Bcl-XL/Mcl-1, p27, HIF-1α, ACK1), or WWOX's own regulation as wild-type. **None concerns a WWOX missense variant.** |
| Q12 | `WWOX AND (MG132 OR "proteasome inhibitor" OR chloroquine OR bafilomycin OR "chaperone-mediated autophagy" OR HSPA8 OR HSC70)` | full expansion | **4** | **41124647** (Zhang, P252A — ✅ **the positive control fires**), 27339895, 19144635, 14695174. **Zhang is the only missense entry.** |
| Q13 | `WWOX AND (solubility OR insoluble OR "detergent-soluble" OR fractionation OR aggregation OR misfolding)` | full expansion | **33** | Dominated by the Chang-lab TRAPPC6AΔ/TIAF1/tau/Aβ aggregation cascade. **Those are aggregation assays on WWOX's PARTNERS, run mostly as transient EGFP/ECFP/EYFP overexpression in COS7/SCC-9/HEK293. Not one is a solubility or aggregation assay on a WWOX missense protein.** |
| Q14 | `WWOX AND (missense OR variant OR mutant) AND ("western blot" OR immunoblot OR "protein expression" OR "protein level" OR "protein levels")` | full expansion | **9** | 🔴 **This is the query that found the new datum.** §3.3. |
| Q15 | `WWOX AND ("4-phenylbutyrate" OR "sodium phenylbutyrate" OR TUDCA OR "chemical chaperone" OR "pharmacological chaperone")` | full expansion, all five terms present, `TUDCA`→`"ursodoxicoltaurine"[Supplementary Concept]` | **0** | ⚠️ Zero, expansion clean, **but method-invisibility applies**. Corroborated by the repository's own independent full-text observation (`discovery_ledger_current.md:807`). Recorded as `PREMISE: NOBODY_LOOKED`, **not** as proof of absence. |
| Q16 | `(WWOX[Title] OR WWOX[Title/Abstract]) AND (WOREE OR DEE28 OR SCAR12 OR "epileptic encephalopathy")` | full expansion | **54** | ✅ Corpus-scale positive control: the WWOX neuro literature is ~54 records and the repository tracks it. |

### 3.3 🔴 NEW FINDING — a sixth measured variant the repository does not hold: `A141T`

Query Q14 returned **PMID 42082822**, *Reprod Sci* 2026;33(5):1020–1025, PMC13230315,
[DOI](https://doi.org/10.1007/s43032-026-02112-9). **Read `full-text` in this act.** `git grep`
over `HEAD` for `42082822`, `Ala141`, `A141T` and `hypospadias` returns **no repository record** —
the variant appears only as a ClinVar row (`WWOX_clinvar_all_variants.csv:155`, *Conflicting
classifications*). **This paper is new to the repository.**

Verbatim, Results:

> *"Western blot analysis revealed significantly reduced WWOX protein levels in both the proband and
> the father compared to healthy controls, indicating that the mutation results in impaired protein
> expression."*

Verbatim, Methods:

> *"DNA samples were isolated from the **peripheral blood** of the patient and their parents, as well
> as from 100 healthy pediatric controls. … After preparing the **total cell lysate**, protein
> concentrations were determined using a Qubit device … WWOX protein was detected using the WWOX
> Protein Antibody (CST 4045S) and ß-Actin (13E5) … as a loading control."*

| Field | Value |
|---|---|
| **Class** | **ABUNDANCE.** Not stability, not solubility, not turnover. |
| **Matrix** | **Peripheral blood total cell lysate.** ⚠️ Not stated explicitly as the WB source; the blood provenance is stated for the DNA and the WB says only *"total cell lysate"*. **Recorded as probable, not certain.** |
| **`n`** | **1 proband + 1 homozygous father** vs *"healthy controls"* — 🔴 **the number of WB controls is never stated.** The "100 healthy pediatric controls" are the **sequencing** controls. |
| **Statistic** | 🔴 **None.** *"Significantly reduced"* carries no test, no densitometry, no error bar, no replicate count. |
| **Material of origin** | **Human, 46,XY DSD / hypospadias.** **NOT oncology, NOT neurology.** |
| **Authors' own limit, verbatim** | *"functional validation was limited to Western blot analysis; more detailed investigations, such as cell-based assays, immunohistochemistry, or CRISPR-based modeling, will be required"* |
| **Prediction discordance inside the paper** | *"the discordance between PolyPhen ('probably damaging') and SIFT ('tolerated') highlights the inherent uncertainty of computational predictions"* |

🔴 **The finding that matters most here is the father.** He is **homozygous** for `A141T`, he carries
the same *"significantly reduced"* WWOX protein, and he is an adult with **no neurological disease**
— his only reported issue is infertility, and *"he refused a genital examination and verbally stated
that his testicles and penis were normal."* **A homozygous WWOX missense with measurably reduced
protein in a neurologically well adult** is a hard counterweight to any inference running
`reduced protein → severe phenotype`. ⚠️ Bound it properly: this is n=1, unexamined, self-reported,
in a different tissue and a different phenotype domain from WWOX-DEE. It does **not** establish that
reduced WWOX is benign. It establishes that the abundance→severity arrow has at least one documented
counter-instance.

### 3.4 The only biophysics on WWOX protein that exists — and what it did not test

**PMID 35716775**, Rotem-Bamberger *et al.* 2022, *J Biol Chem* 298(8):102145, PMC9293652,
[DOI](https://doi.org/10.1016/j.jbc.2022.102145). **Read `full-text` in this act.**

This is the **only** paper in the WWOX literature that measures the physical stability of WWOX
protein. Methods actually run: **urea denaturation monitored by tryptophan fluorescence**;
**far-UV CD, 190–260 nm**; **SEC–MALS**; **ITC**; **¹H,¹⁵N-HSQC NMR**. Verbatim:

> *"Monitoring tryptophan fluorescence changes in urea denaturation experiments showed that **WW1 is
> structured only within the context of the WW1–WW2 tandem domain, but not in its isolated form**,
> indicating significant stabilization of WW1 by WW2."*

🔴 **Three facts about this paper decide its value for the census:**

1. **The constructs are residues 16–91 only.** Verbatim, Experimental procedures: *"PCR products WWOX
   WW1–WW2 (**amino acids 16–91**), WWOX ww1 (**amino acids 16–50**), and WWOX WW2 (**amino acids
   57–91**)"*. 🔴 **The SDR domain was never expressed, never purified, never measured.** There is no
   purified WWOX SDR protein anywhere in this literature — which is why no thermal shift, DSF or CD
   melt on `Q230P` is possible today without first solving an expression problem nobody has solved.
2. **No disease variant was measured.** The only protein point mutants in the paper are `Y85W` (a
   *reverse* mutation restoring WW2's tryptophan) and `A35V` (used solely as an NMR assignment aid,
   *"data not shown"*). 🔴 **`P47` lies inside the WW1 construct (16–50). The reagent existed and
   `P47T` was not run.**
3. **The paper states, unprompted, the exact caution this repository needs.** Verbatim, Discussion:

   > *"AlphaFold2 **cannot be used to assess effects of point mutations, since it relates to point
   > mutations as 'local noise'** and will by default converge on the same result."*

   ⚠️ This is about AlphaFold2, not about ThermoMPNN or ESM-2, and must not be over-extended. It is
   nonetheless a structural-biology group saying in print that the structural pipeline this
   repository ran on `Q230P` is not a variant-effect instrument.

The other three hits of Q10 are not on-axis: **37897534** measures **p53** protein stability in
*Wwox*-KO MEFs; **31230746** is a lncRNA stabilising **wild-type** WWOX in hepatocellular carcinoma;
**25595191** is a review.

### 3.5 What the literature sweep establishes, and what it rests on

| Proposition | Verdict | Rests on |
|---|---|---|
| No `Q230P` stability/turnover/solubility measurement exists | **Established** | (i) full-text read of the only `Q230P` paper's abstract + the repository's held record of its content; (ii) Q9/Q12 method queries with a firing positive control; (iii) the repository's own red-team statement that `Q230P` *"has never been assayed"*; (iv) no purified WWOX SDR protein exists (§3.4) |
| No thermal/CD/DSF measurement exists on any WWOX **disease** variant | **Established** | §3.4 — the one biophysics paper covers 16–91 and used no disease variant |
| No solubility fractionation exists on any WWOX variant | **Established** with a method-invisibility caveat | Q13 inspected by title; corroborated by the repository's independent full-text negative |
| No aggregation assay exists on any WWOX **missense protein** | **Established** with the same caveat | Q13; the 33 hits are partner-protein aggregation |
| No chemical chaperone has been tried on WWOX | `PREMISE: NOBODY_LOOKED` | Q15 zero + independent full-text corroboration. **Not** an establishment. |

---

### 3.6 🔴 A trap I nearly walked into, recorded so the next reader does not

Query Q3 (`"Q230P"`) returns **PMID 41957021**, *Nat Commun* 2026, whose abstract reads:

> *"we identify two genetic variants (**c.689 A > C (p.Q230P)** and c.1120 A > G (p.N374D)) … **Q230P**
> and N374D mutations induce **protein multimerization/aggregation, protease degradation**, decreased
> GTPase activity…"*

**The gene is `GTPBP3`, not `WWOX`.** By coincidence the cDNA change is also `c.689A>C` and the
protein change is also `Q230P`. 🔴 **This is not WWOX evidence of any kind, and it is the single most
citable-looking false positive in this whole search space** — a same-nomenclature, same-cDNA,
measured aggregation-and-degradation result for a different mitochondrial GTPase. **It must never be
allowed into a WWOX row.** Recorded here precisely so that a future grep for `Q230P` + `aggregation`
finds this warning rather than the paper.

---

## 4 · Per-variant classification

`MEASURED` requires a named method, system, `n` and result. `NEVER TESTED` requires a verified zero
with controls shown. `UNRESOLVED` means I could not bound it and I say why.

| Variant | Abundance | Stability (physical) | Solubility | Turnover | **Overall** |
|---|---|---|---|---|---|
| **`Q230P`** | **MEASURED** — Western blot, homozygous patient fibroblasts, *protein not detected*; qRT-PCR transcript normal; Johannsen 2018 PMID 29808465. 🔴 `n` **unread**, controls **unread**, densitometry **unread**, no PMC body | **NEVER TESTED** (§3.4: no purified SDR protein exists) | **NEVER TESTED** | **NEVER TESTED** (repo red-team: *"never been assayed for degradation, HSC70 binding, or lysosomal routing"*) | 🔴 **ABUNDANCE-ONLY. Folding fate UNRESOLVED and untested.** |
| **`P47T`** | **MEASURED ×2, both NORMAL** — (a) human fibroblasts, passages 10/13/14 vs **4 controls**, *"similar amounts"* (Mallaret 2014); (b) mouse cerebellum, `Wwox^P47T/P47T` knock-in, *"similar levels"*, mRNA n=6/group — but the protein panel is the **10% input lane of a pull-down, n=2/group** (Hussain 2023) | **NEVER TESTED** — and §3.4 shows the reagent (WW1 construct 16–50) **existed in 2022 and was not used** | **NEVER TESTED** | **NEVER TESTED** | **MEASURED (abundance, normal, two matrices). Stability/solubility/turnover NEVER TESTED.** |
| **`G372R`** | **MEASURED, qualitative** — immunofluorescence, forebrain-organoid VZ, *"barely any signal"*, **n=2 affected vs n=2 heterozygous parents**, same family, no densitometry, no statistic (Steinberg 2021) | **NEVER TESTED** | **NEVER TESTED** | **NEVER TESTED** | **MEASURED (abundance, qualitative, matrix-split). See §7.** |
| **`A141T`** 🆕 | **MEASURED, qualitative** — Western blot, human total cell lysate (probably peripheral blood), *"significantly reduced"*, **n=1 proband + 1 homozygous father**, control number unstated, **no statistic** (Ongen 2026 PMID 42082822) | **NEVER TESTED** | **NEVER TESTED** | **NEVER TESTED** | **MEASURED (abundance, reduced) — in a 46,XY DSD family, in a neurologically well homozygous adult.** |
| **`P252A`** | **MEASURED** — Flag-transgene WB, CAL-62/BCPAP, reduced; mRNA control normal | **NEVER TESTED** (no biophysics; "stability" here means steady-state level under chase) | **NEVER TESTED** | 🟢 **MEASURED — the only one in the gene.** CHX chase 0–10 h; MG-132 **negative**; CQ 40 µM/24 h and NH₄Cl 250 µM/24 h **rescue**; 3-MA negative; HSC70 co-IP **positive**; LAMP1 colocalisation; K63-polyUb. 🔴 **`t½` never reported** | 🟢 **MEASURED (turnover + route) — on a CMV transgene in thyroid carcinoma, on a ClinVar-`Benign` allele.** |
| **`P282A`** | **MEASURED — normal** | **NEVER TESTED** | **NEVER TESTED** | **MEASURED — no defect, with the positive control (P252A) in the same figure** | 🟢 **MEASURED: no stability defect, function abolished. The cleanest verified negative in the gene.** |
| **`P47R`** | **NEVER TESTED** | NEVER TESTED | NEVER TESTED | NEVER TESTED | **NEVER TESTED.** ⚠️ And the repository already records that P47R's severity **cannot** be separated from the null-like `D16fs` allele in trans. |
| **`L239R`** | **NEVER TESTED** — the one paper reporting it *"contributes **no** protein-level or transcript-level datum"* | NEVER TESTED | NEVER TESTED | NEVER TESTED | **NEVER TESTED.** The repository's own structural prediction for it **remains untested and must be recorded as such.** |
| **`C299R`** | **NEVER TESTED** | NEVER TESTED | NEVER TESTED | NEVER TESTED | **NEVER TESTED.** Its only repository content is a structural inference whose original form was **retracted**. |
| **`T12M`, `E17K`, `G137E`, `G137V`, `M352I`, `G355R`, `S304Y`, `H46Y`, `D58N`, `G62R`, `V190L`, `F237L`, `L291P`, `R310P`, `G315R`, `M326I`, `M327I`, `F348S`, `M374I`, `L371T`, `S390R`, `Q353H`, `G414S`, `M1T`, `M1L`** | **NEVER TESTED** on every axis | | | | **NEVER TESTED.** No protein-level measurement of any kind was found for any of them, in the repository or in the literature sweep. |
| **The remaining ~430 ClinVar missense (400 of them VUS)** | **UNRESOLVED** | | | | **UNRESOLVED** — I did not attempt a per-variant search for 430 variants. The bound is: no WWOX missense method query (Q9–Q15) surfaced any paper measuring any of them. That bound is weak because of method-invisibility. |

**Aggregate: 6 variants measured on abundance (5 of them abundance-only), 1 on turnover, 1 verified
stability-negative, 0 on physical stability, 0 on solubility, 0 on aggregation. Out of 465.**

---

## 5 · Distinguishing abundance from stability from function — applied to the reference genotype

The repository's standing requirement is to separate **synthesis**, **solubility** and **degradation**
and to tie abundance to a **functional** readout. Applied to `Q230P`, here is the complete state:

| Lesion candidate | Would produce `mRNA normal + protein not detected`? | Tested for `Q230P`? | Therapy it implies | Therapy it forbids |
|---|---|---|---|---|
| **Reduced synthesis / translation** (co-translational folding-yield failure) | Yes | **No** | translation-adjacent; a boost adds substrate to a failing step | a proteostasis inhibitor does nothing |
| **Insolubility / aggregation** (protein made, lost from the soluble lysate) | **Yes — and a soluble-lysate Western cannot tell it from either other option** | **No** | anti-aggregation | 🔴 **a boost is ACTIVELY DANGEROUS** |
| **Accelerated degradation** (made, folded badly, cleared) | Yes | **No** | chaperone / proteostasis / lysosomal block | — |

🔴 **All three remain live. Johannsen names two of them and tests neither; the repository has already
recorded insolubility as the un-named third.** The Western blot that produced the datum was run on a
lysate whose insoluble fraction was never examined — so **"protein not detected" is compatible with a
pellet full of aggregated Q230P**, and nobody has looked in the pellet.

And even if the lesion were degradation and even if abundance were restored, the repository holds the
demonstration that this is not enough: **`P282A` is stable and functionally dead**, and
`DL-MECH-049` records that in WWOX *"la stabilità si compra con l'occlusione"* — stability and
function are in structural tension. A buried proline imposes a backbone constraint no chaperone
removes. 🔴 **"More protein" is not "more functional WWOX."**

---

## 6 · What the predictions are worth, tested against the measurements

### 6.1 🔴 The central negative result: predicted ΔΔG is inverted against measured abundance

All ΔΔG values read directly out of `disease-models/wwox/analysis/data/WWOX_ThermoMPNN_saturation.csv`
at `HEAD`, by position and wild-type/mutant residue, **eyeballed individually, not relayed**.

| Variant | ThermoMPNN ΔΔG (kcal/mol) | Measured protein-level result | Matrix | Source |
|---|---|---|---|---|
| **`P47T`** | 🔴 **+2.806 — the HIGHEST of the disease set** | **NORMAL abundance**, twice | human fibroblasts; mouse cerebellum | Mallaret 2014; Hussain 2023 |
| `L239R` | +2.819 | *(never tested)* | — | — |
| `P47R` | +2.532 | *(never tested)* | — | — |
| `G137E` | +2.320 | *(never tested)* | — | — |
| **`A141T`** | +2.261 | **reduced abundance** | human blood lysate | Ongen 2026 🆕 |
| `C299R` | +2.028 | *(never tested)* | — | — |
| **`P282A`** | +1.898 | 🟢 **NO stability defect** (positive control in same figure) | CAL-62 transgene | Zhang 2025 |
| **`G372R`** | +1.583 | **"barely any signal"** | organoid VZ | Steinberg 2021 |
| **`Q230P`** | +1.514 | **not detected** | patient fibroblasts | Johannsen 2018 |
| **`P252A`** | 🔴 **+1.298 — the LOWEST of the disease set** | 🟢 **accelerated degradation, CHX-chase demonstrated, lysosome-rescued** | CAL-62 transgene | Zhang 2025 |
| `T12M` | +0.043 | *(never tested)* | — | — |
| `M352I` | −0.044 | *(never tested)* | — | — |

**Read the six measured rows in order.** The variant the predictor ranks **most destabilising**
(`P47T`, +2.81) has **normal** protein in two independent matrices including neural tissue. The
variant it ranks **least destabilising** of the disease set (`P252A`, +1.30) is the **only one with a
demonstrated turnover defect**. `P282A` at +1.90 has **no stability defect at all**. `Q230P` and
`G372R` sit in the middle at +1.51 and +1.58 and have opposite clinical severities.

⚠️ **Stated with its bounds and no further.** n = 6, the six measurements are **not commensurable**
with each other (Western on fibroblasts, Western on blood, input lane of a pull-down on mouse
cerebellum, IF on organoid VZ, transgene Western on carcinoma lines) — this is `FM-014`, and it is
the reason I compute **no correlation coefficient and claim no statistic**. What the table supports
is a qualitative statement that is nonetheless decisive:

🔴 **ThermoMPNN ΔΔG has no demonstrated predictive relationship to measured WWOX protein abundance or
turnover, and on the two best-measured variants its ranking is exactly backwards. The `+1.514
kcal/mol` for `Q230P` therefore carries no evidential weight about `Q230P`'s folding fate — in
either direction.** It cannot be used to argue that `Q230P` is destabilised, and it cannot be used to
argue that it is not.

This **extends** the repository's existing self-correction — `discovery_ledger_current.md:838`,
*"**La finestra non discrimina**"* — from three variants to six, and adds the two variants
(`P252A`, `P282A`) that carry the only real turnover data in the gene. The repository does not
currently hold this six-variant comparison; `git grep` for the values `1.298` and `2.806` at `HEAD`
returns only the raw saturation CSV.

### 6.2 What survives

- `Q230` is buried (relSASA 0.000) on an α-helix in the AlphaFold **monomer** — a structural
  description, still a prediction of nothing about turnover.
- 🔴 **The homodimer interface is not modelled**, and §7.2 shows why that specific gap is now
  load-bearing rather than merely honest.

---

## 7 · `G372R` specifically — does any real measurement exist?

**Answer: YES — exactly one, and it is not the one the repository was almost persuaded by.**

I verified this independently and did **not** inherit the repository's framing in either direction.

| Candidate source | Is it a measurement? | Verdict |
|---|---|---|
| **Aldaz & Hussain 2020**, PMID 33255508, PMC7727818 — *"Analysis from patient fibroblasts showed that **both described missense mutations** do not alter WWOX protein expression…"* | 🔴 **NO.** A narrative-review sentence describing Mallaret 2014 (*"In the same study"*). **No method** — the word "Western" never appears. **No `n`. No controls.** And two sentences earlier the same authors write that `G372R`'s *"functional consequence is **unclear at this point**"* | **NOT A MEASUREMENT.** Independently confirmed. |
| **Steinberg 2021**, PMID 34268881, PMC8350905 — *"barely any signal was observed in WPM D1 and S1"* | 🟢 **YES.** Immunofluorescence, in situ, forebrain-organoid ventricular zone, **n=2 affected homozygotes (WPM D1, WPM S1) vs n=2 heterozygous parents (WPM F2, WPM M3), same family** | **A REAL MEASUREMENT — the only one.** |
| **Mallaret 2014**, PMID 24369382, PMC3914474 | 🔴 **UNREADABLE.** `get_full_text_article(["PMC3914474"])` returns `full_text: ""`. `FT-128` records the cause as **licensing, not routing**. The repository's held verbatim record from this body documents a fibroblast Western **for `P47T` only** | **UNRESOLVED — `PREMISE: UNVERIFIED`** on whether a `G372R` blot exists in the unread body |
| **Any other source** | My independent literature sweep found none. Q6/Q7 zeros are meaningless (unexpanded). Q8's translation **silently dropped** `"G372R"`. The only surviving route — `Gly372` — returned nothing beyond the two known papers | **No additional measurement found.** The search is weak for the reasons in §3.1 and I say so rather than claim a zero. |

**Verdict, stated without inheriting either side:**

1. 🟢 **A real `G372R` protein-level measurement exists.** It is Steinberg's organoid-VZ
   immunofluorescence, and it says *"barely any signal"*.
2. 🔴 **It is ABUNDANCE, not stability.** No `G372R` half-life, solubility, aggregation or route has
   ever been measured. On the census axes that matter, `G372R` is **NEVER TESTED**.
3. 🔴 **Its quality is low on three independent axes**, and the third is one the repository's audit
   added yesterday and it matters: not quantified; n=2 vs 2; and **the comparator arm is itself a
   carrier genotype** on a baseline the same paper describes as widely variable among healthy
   heterozygotes.
4. **The repository's conclusion — "matrix-split and unresolved" — is correct, and I reach it
   independently.** I add one thing: the counter-source is not merely weaker, it is **not a
   measurement at all**, so there is **no same-measurement conflict to adjudicate.**

🔴 **On `G372R` as a "natural negative control": the repository is right to have retracted that
framing and must not un-retract it.** A variant whose protein is *"barely detectable"* by a
qualitative IF in a progenitor compartment, with no half-life, no solubility and no route, is **not a
control for anything**. The burial argument's decisive comparator is `P47T`/`P47R` — same residue,
near-identical predicted ΔΔG (+2.81 vs +2.53), opposite phenotypes — and §6.1 now shows that even
that comparison cannot be run through ΔΔG.

---

## 8 · The SDR fold family — degradation vs aggregation

> 🔴 **EVERYTHING IN THIS SECTION IS TRANSFERRED EVIDENCE. NOT ONE DATUM BELOW IS ABOUT WWOX.**
> A mechanism class can transfer. A conclusion cannot. Every row carries its own organism, matrix
> and method, and none of them licenses a statement about `Q230P`.

**Question asked:** in the short-chain dehydrogenase/reductase fold, are destabilising missense
variants known to be **degraded** rather than to **aggregate**? The two have opposite therapeutic
implications: degradation invites a proteostasis approach; aggregation makes a boost actively
dangerous.

**Answer: the fold family's documented default is DEGRADATION — with one specific, structurally
defined exception that maps uncomfortably well onto WWOX.**

### 8.1 The degradation side — well documented, with the exact experiment this census needs

| Protein | Fold | Variants | Method | Result | Source |
|---|---|---|---|---|---|
| **11β-HSD2** (`HSD11B2`) — apparent mineralocorticoid excess | **SDR family** | **Tyr338His, Arg337His** (patient variants) | **Half-life determination**; temperature shift; **chemical chaperones**; proteasome-pathway test | 🟢 **WT `t½` = 21 h; Tyr338His = 3 h; Arg337His = 4 h.** Activity **partially retained at 26 °C** or with the chemical chaperones **glycerol and dexamethasone**, *"indicating thermodynamic instability and misfolding"*. Degradation of both mutant and WT *"occurs through the **proteasome** pathway"* | Atanasov 2007, *JASN* 18(4):1262–70, PMID 17314322, `abstract-depth`, [DOI](https://doi.org/10.1681/ASN.2006111235) |
| **HSD17B10 / SDR5C1 / MRPP2** — HSD10 disease | **SDR family** (explicitly) | **p.V12L, p.V176M** (patient variants) | Recombinant expression + biochemical characterisation | 🟢 **Two DIFFERENT mechanisms from two missense in ONE SDR:** p.V12L → *"reduced stability"*; p.V176M → *"impaired kinetics and complex formation"* — *"two distinctive molecular mechanisms"* | Oerum 2017, *BBA Mol Basis Dis* 1863(12):3294–302, PMID 28888424, `abstract-depth`, [DOI](https://doi.org/10.1016/j.bbadis.2017.09.002) |
| **HSD17B10 / SDR5C1** | SDR | multiple HSD10-disease missense | functional + complex assays | 🟢 *"Some mutations **disrupt the homotetramerization** of SDR5C1 and/or impair its interaction with TRMT10C"* | Vilardo & Rossmanith 2015, *Nucleic Acids Res* 43(10):5112–9, PMID 25925575, `abstract-depth`, [DOI](https://doi.org/10.1093/nar/gkv408) |

🔴 **Atanasov 2007 is, structurally, the exact experiment `Q230P` needs and has never had** — an SDR
disease missense taken to a measured half-life, a temperature-rescue arm, a chemical-chaperone arm
and a route determination, in one paper, on a fold family member. **It is also a warning:** the route
there was the **proteasome**, whereas the only WWOX route ever measured (`P252A`) was explicitly
**MG-132-insensitive and lysosome-dependent**. **The fold does not fix the route. It must be measured
per allele.**

### 8.2 The aggregation side — rarer, and the exception is interface-specific

An SDR-fold aggregation query returned only **2** records
(`("short-chain dehydrogenase" OR "SDR family" OR "Rossmann fold") AND (aggregate OR aggregation OR
"inclusion bodies" OR amyloid) AND (missense OR mutant) AND (cell OR patient)`; translation clean on
all limbs) against **44** for the degradation-shaped query. ⚠️ **That asymmetry is suggestive, not
probative** — `[All Fields]` under-indexes methods, so a fractionation done in a Methods section is
invisible. But one of the two hits is precisely on point:

| Protein | Fold | Substitutions | Result | Source |
|---|---|---|---|---|
| **17β-HSD** from *Cochliobolus lunatus* (`17β-HSDcl`) | **SDR superfamily, NADPH-dependent, functions as a homodimer** | **F124, F132, F133, F177** — hydrophobic residues **at the dimer interface** | 🔴 *"Phenylalanine substitutions introduced **at the dimer interface** produced **inactive aggregates and oligomers with high molecular masses**"* | Brunskole 2008, *Mol Cell Endocrinol* 301(1-2):47–50, PMID 18775764, `abstract-depth`, [DOI](https://doi.org/10.1016/j.mce.2008.07.023) |

### 8.3 What transfers, and the one thing that does not

**Transfers as a mechanism class:**
- In the SDR fold, a destabilising missense **located in the monomer core** characteristically yields
  a short-half-life protein cleared by a quality-control route, and that phenotype is
  **temperature-rescuable and chemical-chaperone-rescuable** in at least one human disease gene.
- The **route is allele- and protein-specific** (proteasome for 11β-HSD2; lysosome, MG-132-negative
  for WWOX `P252A`). It must be measured, never assumed.
- Two missense in the **same** SDR can fail by **two different mechanisms** (HSD17B10 V12L vs V176M),
  which is the fold-family restatement of `P252A` vs `P282A`.

**Transfers as a warning, and this is the one that bites:**
- 🔴 **SDR destabilisation AT THE DIMER INTERFACE produces AGGREGATES, not clearance.** WWOX
  **homodimerises via the SDR**, and the repository's own structural work explicitly records that the
  interface **was not modelled** — *"relSASA e SSE sono calcolati su un **monomero**, ma WWOX
  **omodimerizza via SDR** e l'interfaccia non è modellata"*. **Whether `Gln230` sits at the
  WWOX SDR dimer interface is unknown, and it is the single structural fact that would flip the
  transferred prior from `degradation` to `aggregation` — i.e. from "a boost is worth trying" to
  "a boost is dangerous".**

**Does NOT transfer:**
- Any statement about `Q230P`. Not one of these proteins is WWOX; none is measured in a neuron; the
  matrices are recombinant protein, fungal enzyme, and kidney/mitochondrial systems.
- 🔴 **`GTPBP3` p.Q230P must not be transferred either** (§3.6), notwithstanding that it is a
  *measured* aggregation-and-degradation result at an identical cDNA and protein coordinate. It is a
  different gene, a different fold, a different disease.

---

## 9 · VERDICT — is `Q230P`'s folding fate knowable from existing evidence?

# 🔴 NO. It requires new wet work.

**The reasoning, compressed:**

1. `Q230P` has **one** protein-level datum: *protein not detected on a Western blot of patient
   fibroblasts, with normal transcript*. That endpoint is **compatible with all three** of reduced
   synthesis, insolubility and accelerated turnover — **its own authors say so** — and **not one of
   the three has ever been tested for this allele, in any system, by anybody.**
2. The pellet has never been looked in. **"Protein not detected" in a soluble lysate is exactly what
   an aggregating protein looks like**, and aggregation is the one outcome under which a
   non-allele-specific boost is actively harmful.
3. The in-silico evidence cannot substitute, and not merely because a prediction is not a
   measurement: **§6.1 shows the predictor is inverted against the six measurements that exist.**
   The `+1.514 kcal/mol` is evidentially empty in both directions.
4. Read-across is closed in every direction the repository has: `P47T` is a WW1 lesion with normal
   protein and a retracted read-across; `G372R` is a qualitative organoid IF with a carrier-genotype
   comparator; `P252A` is a **ClinVar-`Benign`** CMV transgene in thyroid carcinoma; `A141T` is a
   different tissue, a different phenotype, n=1, no statistic. **Q230P ≠ P47T ≠ G372R ≠ A141T ≠ P252A.**
5. The fold-family transfer (§8) supplies a **prior**, not an answer — and it supplies a prior that
   **forks on a structural fact nobody has determined**: monomer core → degradation (proteostasis
   approach viable); dimer interface → aggregation (**boost dangerous**).
6. Even a resolved folding fate would not settle the sign, because `P282A` demonstrates that a
   stable WWOX missense protein can be functionally dead, and a buried proline imposes a backbone
   constraint a chaperone cannot remove. **Any abundance restoration must be read per unit protein
   against a function.**

**Consequence for the reopened axis.** The `therapeutic_hypotheses_ledger_current.md:216` statement
stands exactly as written and is, if anything, understated: *"il segno del beneficio dipende
**interamente** dal destino di folding di Q230P, ad oggi **ignoto**."* 🔴 **It is not merely unknown;
the instrument the repository was implicitly leaning on to guess it is demonstrably unreliable for
this protein.** A non-allele-specific WWOX upregulation cannot be assigned a sign today.

### 9.1 The cheapest experiment that separates synthesis, solubility and turnover

**One lysate, one blot, four arms. Donor-derived cells carrying the allele, against a healthy
control and — where obtainable — an isogenic knock-in pair.**

| # | Arm | Reads out | Cost | Decides |
|---|---|---|---|---|
| **1** | **Solubility fractionation FIRST.** Lyse in a non-denaturing buffer; spin; blot **soluble supernatant AND the resuspended pellet in SDS** on the same membrane, same exposure | 🔴 **Is the protein there at all?** | ~1 day, one extra lane | 🔴 **This single lane is the most informative measurement in the whole design and it has never been done.** Protein in the pellet ⇒ **INSOLUBLE/AGGREGATING ⇒ a boost is dangerous, stop.** Protein in neither ⇒ synthesis or turnover; proceed |
| **2** | **Lysosome vs proteasome block**, side by side, on the soluble fraction: CQ 40 µM/24 h and NH₄Cl 250 µM/24 h vs **MG-132 20 µM/6 h**, with 3-MA 10 mM/12 h as a second negative | Turnover route | days | Mutant band re-emerges under lysosomal block ⇒ **turnover is the bottleneck**, and the `P252A` mechanism class transfers to this allele. Re-emerges under MG-132 ⇒ a **different** route from `P252A` and the transfer fails. 🔴 **Running MG-132 alone would have been the trap:** a negative would have read as *"degradation is not the bottleneck"* and would have been wrong |
| **3** | **Nascent synthesis**: 15–30 min AHA-click or ³⁵S pulse, immunoprecipitate WWOX, read label incorporated at t=0 | Synthesis rate | days | Low incorporation with an empty pellet ⇒ **translation/folding-yield defect**, and neither a chaperone nor a proteostasis lever is indicated |
| **4** | **Quantified CHX chase with a reported `t½`**: 50 µg/mL CHX, 0/2/4/6/8/10 h, band intensity loading-normalised, `t½` fitted with CIs, **3 biological replicates** | Half-life, as a **number** | ~1 week | Delivers the quantity Zhang 2025 ran the assay for and never reported |

**Why arms 1 and 2 are the minimum and arm 1 comes first.** Arm 1 alone can **stop the therapeutic
axis** — if `Q230P` is in the pellet, the sign of a non-allele-specific boost is negative and no
further work is needed to say so. Arms 1+2 together discriminate all three lesions. Arms 3 and 4
quantify. **The whole design extends the `HYP-20260709-08` minimal experiment already in the
repository rather than replacing it, and it uses only reagents and doses already published in the
WWOX literature.**

**And the mandatory rider, which is not optional:** every arm must be read against a **functional,
abundance-normalised, domain-resolved** readout — an **SDR-domain partner** (tau or GSK3β, or POLE4)
as the discriminating assay, with a **WW1-dependent partner** as the control that must stay normal
for an SDR lesion. 🔴 **A rescue that restores a band and never measures a function has not shown
recovery**, and `P282A` is the standing proof.

**One reagent-level note that costs nothing to act on:** the cheapest possible *physical* stability
measurement on `Q230P` — a thermal shift or CD melt — is **not currently available at any price**,
because **no purified WWOX SDR protein exists** (§3.4). Expressing and purifying the WWOX SDR domain
is itself an unsolved problem in this literature and should be costed separately, not assumed.

---

## 10 · What I could not establish

1. 🔴 **Johannsen 2018's `n`, controls and densitometry for the `Q230P` Western.** PMID 29808465 has
   **no PMCID**. The repository has owed this since 2026-07 and it is still owed. **This is the single
   highest-value unread page in the whole census**, because it is the only measurement on the actual
   allele and nobody has seen its error bars.
2. 🔴 **Whether Mallaret 2014's body contains a `G372R` fibroblast Western.** `PMC3914474` returns
   `full_text: ""` — licensing, not routing (`FT-128`). Acquisition is a human action. `PREMISE:
   UNVERIFIED` stands. I did not retry blocked publisher hosts.
3. **Steinberg's Appendix figures** (the iPSC corroboration of the `G372R` result) are not
   distributed by PMC. Recorded as a reading debt, not a second read-out.
4. **Zhang 2025's figure panels**, which are where the `P252A` half-life number would be if it exists
   anywhere. The text reports an adjective.
5. **The matrix of the `A141T` Western blot.** The paper says *"total cell lysate"* and states blood
   provenance only for the DNA. Probable, not certain. **Also unestablished: how many control lanes
   the blot carried** — the paper never says.
6. 🔴 **Whether `Gln230` lies at the WWOX SDR homodimer interface.** This is the fact that forks the
   fold-family transfer between degradation and aggregation (§8.3), and the repository's structural
   pipeline was run on a **monomer**. It is in principle answerable in silico at zero external cost
   by re-running the interface, and that is the one computational task in this census with real
   decision value — **but a predicted interface is still a prediction, and §6.1 is the reason not to
   treat the answer as more than a prior.**
7. **Whether any of the ~430 unmeasured ClinVar missense has a measurement buried in a Methods
   section.** Method-invisibility makes this unbounded by PubMed alone. I did not attempt 430
   per-variant searches and I do not claim a zero.
8. **Whether the aggregation-vs-degradation asymmetry in the SDR fold literature (2 records vs 44) is
   real biology or a search artefact.** Both are consistent with the counts.

---

## 11 · Proposed for the Orchestrator — no canonical file touched

1. **`A141T` (PMID 42082822, PMC13230315) is new to the repository** and is a **sixth measured
   variant**. Propose ingest through the normal quarantine. Its most load-bearing content is the
   **neurologically well homozygous father with measurably reduced WWOX protein**, which is
   counter-directional to any `reduced protein → severe phenotype` inference.
2. **The six-variant prediction/measurement discordance table (§6.1) is new** and extends the
   repository's existing self-declassification of the "rescuable window" from 3 variants to 6.
   Propose it be considered for the discovery ledger as a **methodological negative**: ThermoMPNN
   ΔΔG has no demonstrated relationship to measured WWOX abundance and is inverted on the two
   best-measured alleles.
3. **New tool trap (f) for the register:** a quoted term can be **silently dropped** from an OR block
   in `query_translation` without error (Q8: `"G372R"` vanished). Any OR-block count must be checked
   term-by-term against the returned translation.
4. **New trap for the `Q230P` namespace:** `GTPBP3` p.Q230P / c.689A>C (PMID 41957021) is a measured
   aggregation-and-degradation result at an **identical coordinate in a different gene** (§3.6).
5. **§3.4 supplies a citable, unprompted structural-biology statement** that AlphaFold2 *"cannot be
   used to assess effects of point mutations"* — relevant to how this repository's in-silico
   pipeline is described.
6. **Nothing here licenses flipping any `G372R` row in either direction.** §7's conclusion matches
   the repository's existing one, reached independently.

---

**END OF FILE — complete run.** Eleven sections, all written. No registry, queue, ledger, receipt
chain, canonical file or state manifest was read-modified-written by this act. No `BATCH_COMMIT` was
run. According to PubMed, the literature content above derives from the records cited, each with its
DOI linked at first use.
