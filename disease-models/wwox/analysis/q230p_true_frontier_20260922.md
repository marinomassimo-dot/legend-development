# `Q230P` — the TRUE unresolved scientific frontier, reconstructed from all existing repository analysis

**Actor:** Scientist A · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** 🔴 **NON-CANONICAL.** No `*_current.md`, registry, queue, ledger, receipt chain or state
manifest was written or read-modified. No `BATCH_COMMIT`. No git command was run. **One file was
created: this one.** Every canonical file named below was opened **read-only**.
**Nothing here is medical advice.** No molecule, dose, route, compound screen or prognosis appears
anywhere below. A mechanistic hypothesis is not a treatment.
**Alleles and models are held apart throughout:** `Q230P` ≠ `Q230A` ≠ `Q230M` ≠ `Q230G` ≠ `P47T` ≠
`P47R` ≠ `A141T` ≠ `L239R` ≠ `P252A` ≠ `P282A` ≠ `G372R` ≠ `C299R`; `Wwox`-null ≠ `gt/gt` ≠ `lde/lde`
≠ human WOREE ≠ human SCAR12. A measurement on one is never carried to another.
**Public edition** — this reasons about a WWOX-DEE reference **genotype class**, never an individual.
**This file proposes no new science.** It establishes what is already worked out and what genuinely
remains open. Where it says a question is open, that is a statement about this repository's evidence.

---

## 0 · METHOD — the enumeration was unfiltered, and that was the point

A previous wave was invalidated because *the filter was the hypothesis*. The correction applied here:

1. **`ls disease-models/wwox/analysis/`** was run first and read **whole** — **158 entries** (154
   files + `data/`, `near_miss_cases/`, `orchestration_reviews/`, `scripts/`). Then
   `find disease-models/wwox/research -type f` — **320 entries** (109 commit candidates, 81
   deep-dive manifests, 54 full-text dossiers, 41 session evaluations, 7 page adjudications, the
   four research-layer `*_current.md`, `retrieval_manifest.jsonl`, `HUMAN_ACTION_*`,
   `OPERATOR_DECISION_PACKET_6`, locator audits, pattern audits, recursive rereads). Then
   `analysis/data/` (54 artefacts including `WWOX_Q9NZC7_AlphaFold.pdb`,
   `WWOX_ThermoMPNN_saturation.csv`, `WWOX_Q230P_residue_context.csv` and the 22-file
   `data/redteam/` set) and `analysis/scripts/` (28 files, including the MD pilot and its tests).
2. **Only then** were files opened. The brief's candidate list was checked against the full listing
   and was **not** treated as complete: six further Q230P-relevant files were picked up from the
   listing that the brief does not name — `q230p_survival_paradox_20260921.md`,
   `three_designs_one_experiment`, `nmd_adjudication_reference_allele_20260922.md`,
   `DISCOVERY_TRACE_metabolic_gating_20260922.md`, `fold_of_wt_is_undefined_for_vdna_20260922.md`,
   `gln353_gln354del_structural_adjudication_20260922.md`, plus `data/redteam/` and the MD scripts.
3. **`registries/reading_state.md` and `registries/claim_registry_current.md` were read for
   propagation only** — what is CANONICAL versus analysis-only. Nothing was written to either.

### The three independent depths, held apart in every row

| depth | what it measures | why it must not be collapsed |
|---|---|---|
| **SOURCE DEPTH** | how much primary evidence was actually acquired — `TITLE` / `ABSTRACT` / `PASSAGE` / `METHODS` / `FULL BODY` / `SUPPLEMENT` | the fixture: **Johannsen 2018 (PMID 29808465) is `abstract_only`** — `reading_state.md:98` records every one of its ten body fields as `unavailable` |
| **ANALYSIS DEPTH** | what LEGEND already investigated with that material | the same fixture: **~700 lines of existing analysis sit on that abstract** (`johannsen2018_acquisition_and_body_20260922.md`, 700 lines) |
| **PROPAGATION DEPTH** | where the derived knowledge reached — `ANALYSIS ONLY` / `CANDIDATE` / `LEDGER` / `REGISTRY` / `CANONICAL CLAIM` | `CLAIM 019` is `consolidated baseline` (`claim_registry_current.md:345`) and carries an `abstract_only` datum; `CLAIM 030` is `in observation` (`:553`) and carries `PREMISE: DETECTION_FLOOR` |

🔴 **`ABSTRACT_ONLY` at source depth does not imply no prior analysis, and rich analysis does not
imply the source was read.** Both errors are made visible by the columns being separate.

### Status vocabulary, applied mechanically

- **RESOLVED** — answered on evidence the repository holds, with the answer's own class declared.
- **PARTIALLY RESOLVED** — answered on one axis, open on another named axis.
- **EXPERIMENT PROPOSED BUT UNRUN** — a **specified, discriminating** design exists in a named file.
  *A proposal is never a result.*
- **SOURCE-DEPTH LIMITED** — the answer may already exist in a primary source this deployment cannot
  read; the block is acquisition, not science.
- **TRUE EXPERIMENTAL GAP** — LEGEND has identified the question and there is **no specified design,
  no validated implementation, or no reagent/material/readout** that would execute one.
- **HUMAN_REQUIRED** — the block is an external action (acquisition, material, a programme decision).
- **SUPERSEDED** — the repository held a position and has withdrawn or inverted it.

---

# 1 · THE FRONTIER MATRIX

## 1.1 · RNA

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **RNA-1** | Is `Q230P` **transcript abundance** normal? | **Yes, as reported** — qRT-PCR, donor-derived fibroblasts, *"normal levels of WWOX transcripts"* | 🔴 **ABSTRACT_ONLY** — `reading_state.md:98`; `q230p_structural_mechanism_20260922.md` §0.4 | **HIGH** — used to localise the lesion post-transcriptionally (`structural` §0.2); census row 1 (`wwox_missense_abundance_lysis_census_20260922.md` §1.1) | 🟢 **CANONICAL CLAIM** — `claim_registry_current.md:355` (`CLAIM 019`, consolidated baseline); `DL-MECH-029` (`discovery_ledger_current.md:668`) | 🔴 **qPCR amplicon position `UNSTATED`** — a single amplicon outside a skipped region returns *"normal transcript"* and is blind | Two amplicons, one spanning exon 7, one 3′ — `q230p_minimum_discriminator_20260922.md` §1.4 | 🔴 **SOURCE-DEPTH LIMITED** |
| **RNA-2** | Has `Q230P` **mRNA stability / decay** been measured? | **Unknown — and an experiment may exist** | 🔴 **ABSTRACT_ONLY** + MeSH `RNA Stability` present, **absent from every abstract sentence** | **MODERATE** — `johannsen2018_acquisition_and_body_20260922.md` §4 target 3: *"May index a real decay chase **or** merely the indexer's reading"* | ANALYSIS ONLY | Whether a decay chase was run at all; direction and magnitude unknown | Acquisition only — `johannsen2018…` §6.4 extraction list | 🔴 **SOURCE-DEPTH LIMITED** |
| **RNA-3** | Is **NMD** relevant to `Q230P`? | **Yes — answered in the negative for this allele** | Repository full-text sweep + 16-query literature sweep, 708-record denominator | **HIGH** — `wwox_nmd_assay_census_20260922.md` §1–§5: `NEVER TESTED` for **any** WWOX allele, every one of 78 `cycloheximide` / 22 `UPF1` / 19 long-read hits individually disqualified | ANALYSIS ONLY | None **for `Q230P`**: a missense allele with normal transcript is not an NMD question. The gap is real for **PTC alleles**, which are a different allele class | Heterozygote ±NMD-block, allele-specific ddPCR — `wwox_nmd_assay_census` §6 — **for PTC alleles, not this one** | 🟢 **RESOLVED** (not the `Q230P` question) |
| **RNA-4** | Does `c.689A>C` disrupt an **ESE**, causing exon-7 skipping? | **Partly** — splice-**site** risk excluded, ESE residual open | Another actor's attestation (`missense_splice_reclassification_risk_20260921.md`), codon arithmetic validated on nine published c./p. pairs | **MODERATE-HIGH** — `structural` §0.1: `c.689A>C`, exon 7, **66–84 nt from any junction**, splice risk **LOW**; but that addresses splice-site disruption, **not** `ESE`/`ESS` | ANALYSIS ONLY | 🔴 Exon-7 ESE vulnerability **never assessed** (vulnerability is exon-specific: 10 % globally, 60–77 % in named vulnerable exons) | One qPCR well (two amplicons) — `q230p_minimum_discriminator` §1.4 item 2, `RT-MD-10` | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |

## 1.2 · PRODUCTION

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **PROD-1** | Is the `Q230P` polypeptide **translated at a normal rate**? | 🔴 **No — never measured, for any WWOX allele** | 🔴 ABSTRACT_ONLY. `johannsen…` §4 target 4: translation was *"assessed by … Western blotting"* — i.e. **via steady-state protein**, not by a translation assay | **HIGH** — `missense_proteostasis_matrix_20260921.md` row 1: *"Translation: no evidence at all, in either paper"*; `wwox_missense_stability_census_20260922.md` §2.3 verified zero (no ³⁵S, AHA-click, SUnSET, polysome, ribosome profiling) | 🟡 **LEDGER** — `DL-MECH-029` carries the authors' undiscriminated disjunction *"impaired translation or premature degradation"* | 🔴 **No validated implementation.** `proteostasis_discrimination_protocols_20260922.md` rank 4: *"no published instance of protein-specific nascent-synthesis measurement, by pulse-label + IP, for a low-abundance single protein in primary human dermal fibroblasts"*; and SUnSET/OP-puro/AHA-imaging **measure global translation, not one protein** | Named as an arm (`stability census` §9.1 arm 3; `matrix` row 1) but the protocol file scores it a **FLAG, not a candidate** | 🔴 **TRUE EXPERIMENTAL GAP** |
| **PROD-2** | **Nascent-chain generation** — is a polypeptide made at all? | **No** | — | **HIGH** — separated as its own mechanism column `M1′` (synthesis / co-translational triage) in `q230p_direct_discriminator_20260922.md` §3.1 | ANALYSIS ONLY | 🔴 `M1′` is assigned by **row `R2` — all levers negative — i.e. by elimination, which is weaker evidence than measurement** and must be labelled so (`direct discriminator` §5.2) | Lever panel at zero baseline — `q230p_minimum_discriminator` §1.5; `R2` in `direct discriminator` §3.1 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |

## 1.3 · EARLY FATE

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **EARLY-1** | **Cotranslational loss / folding-yield ceiling** | **No** | — | **HIGH** — the fifth mechanism, *"separated for free"* by the dox-titration format (`direct discriminator` §3.1 `M1′`) | ANALYSIS ONLY | Whether a matched-abundance point exists at all: *"if `Q230P`'s maximal attainable donor signal lies below wild type's usable working range, there is no matched point"* (`direct discriminator` §5.2) | Dox-titrated single-copy landing pad, overlap window reported as a **primary result** — `direct discriminator` §5, §7.3 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **EARLY-2** | **Folding-associated disposal** — is a near-native species cleared before it matures? | **No** | — | **MODERATE-HIGH** — the question is posed and the block-and-rescue logic imported from HOGA1 and NPC1 (`minimum discriminator` §1.5, `P7` held) | ANALYSIS ONLY | 🔴 *"You cannot chase a band you cannot see"* (repository `Caveat 2`) — every published chase in the reachable material starts from an accumulated or over-expressed pool | Block-and-rescue at zero baseline (bafilomycin A1 + MG-132), which **is** measurable at zero baseline — `minimum discriminator` §1.5 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |

## 1.4 · SOLUBILITY

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **SOL-1** | **What was in the lysate Johannsen loaded?** | 🔴 **No — all eleven extraction targets `METHODS_INVISIBLE`** | 🔴 **ABSTRACT_ONLY.** Springer-closed, `pmc_id: null`, **four independent agent acquisition attempts failed**, most recently under a proven `example.com` egress control | 🔴 **VERY HIGH** — `johannsen2018_acquisition_and_body_20260922.md` §4 enumerates all eleven targets un-filled; §6 is a complete `HUMAN_ACQUISITION_PACKET` with a one-pass ordered extraction list | ANALYSIS ONLY — but it **gates** `CLAIM 019` and `CLAIM 030` | Items 6 (buffer), 7 (spin), 8 (pellet), 10 (antibody+epitope), 11 (floor), plus `n`, amplicon position, and whether the MeSH-indexed **HEK293 arm** exists | `johannsen2018…` §6.3 ranked human routes; `PREREG_johannsen2018_methods_20260922.md` §6.1 `SOURCE_ACQUISITION_PACKET` | 🔴 **HUMAN_REQUIRED** (source-depth limited at root) |
| **SOL-2** | Is `Q230P` protein in the **soluble fraction**? | **Reported not detected — but the buffer is unknown** | 🔴 ABSTRACT_ONLY | 🔴 **VERY HIGH** — `abundance lysis census` §1.1 row 1: *"NO — and not even weakly. Nothing about the loaded lysate is knowable"* | 🟢 **CANONICAL** — narrowed from *"protein absent"* to *"protein **not detected**"* with `PREMISE: DETECTION_FLOOR` (`claim_registry_current.md:559`, `CLAIM 030`) | Whether *"not detected"* means **absent from the soluble fraction only** | `q230p_three_designs_one_experiment_20260922.md` §2 states the mechanism; the re-run is `minimum discriminator` §3.1 | 🔴 **SOURCE-DEPTH LIMITED** |
| **SOL-3** ⭐ | Is `Q230P` protein in the **insoluble pellet**? | 🔴 **No — and nobody has looked, for ANY WWOX allele, in any system, ever** | — | 🔴 **VERY HIGH.** `abundance lysis census` §1.2: **0 / 12** rows examined a pellet, insoluble or fraction; `pellet` 0, `fraction` 0, `insoluble` 0 in the served body of the deepest turnover paper; the patient-derived sub-census is **100 % buffer-blind** | ANALYSIS ONLY — feeds `TX-003` / `HYP-20260709-02`, both **conditional** | 🔴 **This is the branch that decides the therapeutic sign.** `structural` §9: a boost on the insolubility branch is *"actively dangerous"*; on the clearance branch it is coherent | Fully specified, three files converge: `minimum discriminator` §3.1 (`S`·`P`·`T`, one gel, equal cell-equivalents, SDS/urea pellet resolubilisation); `stability census` §9.1 arm 1; `function_per_molecule_assay_design_20260922.md` §4 (*"RUN IT. FIRST. AND DO NOT CALL IT A FUNCTION ASSAY"*) | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **SOL-4** | Is the fractionation **quantitative** — does `S + P = T`? | **No** | Four queries, **no quantification found in either direction** | **HIGH** — `minimum discriminator` §1.3 and `COULD NOT ESTABLISH` item 1; prediction `P2` **refuted**, `T` retained on established practice plus logic, `RT-MD-07` is *"the most reversible decision in the file"* | ANALYSIS ONLY | 🔴 Falsifier `F1`: `S + P ≪ T` in the **wild-type** lane voids every double blank and makes `H1` unassignable by this design | `T` lane (no spin) carried as a control — `minimum discriminator` §1.3, §3.4 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **SOL-5** ⭐ | Is any insolubility **intrinsic to the allele** or **created by the dose**? | **No** | — | **HIGH** — `dS/dA` (the slope of insoluble fraction against induced abundance) is introduced in `direct discriminator` §3.0 as *"the quantity that is in no prior design"*; rows `R3` (flat ⇒ intrinsic) vs `R4` (rising ⇒ dose-driven) | ANALYSIS ONLY | 🔴 `R4` is *"the only cell in the matrix that says raising abundance **creates** the aggregate rather than revealing it"* | `direct discriminator` §3.1 rows `R3`/`R4`, §7.4 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **SOL-6** | Would a **fibroblast-negative** pellet close the question? | 🟢 **Yes — answered NO** | Abstract-depth precedent (ataxin-3, PMID 22113611): the SDS-insoluble species formed **only in patient neurons** and *"was not observed in iPSCs, fibroblasts or glia"* | **HIGH** — `proteostasis_discrimination_protocols` rank 1 counter-evidence; `minimum discriminator` §3.3 item 2 states it as a loss | ANALYSIS ONLY | 🔴 **No neuronal or brain material carrying `Q230P` exists in this repository's reach**, and no WWOX protein measurement in patient brain exists for **any** missense allele (`q230p_survival_paradox_20260921.md` §3 rank 4) | 🔴 **None — this is named as a structural limit of the material, not of the design** | 🔴 **TRUE EXPERIMENTAL GAP** |
| **SOL-7** | Would a detected insoluble species be a **toxic gain of function**? | **No** | — | **MODERATE** — named as *"the fourth branch the ledger does not name"* (`abundance lysis census` §3.3): the reference genotype would be **worse** than functionally null | ANALYSIS ONLY | 🔴 *"The pellet says where the protein is, never whether it harms"* (`minimum discriminator` §3.3 item 3) | 🔴 **None** | 🔴 **TRUE EXPERIMENTAL GAP** |

## 1.5 · DECAY

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **DEC-1** | `Q230P` **mature-pool half-life** | 🔴 **No — `NEVER TESTED`** | — | **HIGH** — `stability census` §4 classifies `Q230P` **ABUNDANCE-ONLY**: stability, solubility and turnover all `NEVER TESTED`; `data/redteam/discriminating_experiment.md:4`: *"`Q230P` … has never been assayed for degradation, HSC70 binding, or lysosomal routing"* | ANALYSIS ONLY | The **magnitude** of any turnover defect; no `t½`, no CI, no comparison with `P252A`'s kinetics | Quantified CHX chase — **deliberately CUT from the minimum set** and re-entering as the **correct second experiment** once a measurable pool exists (`minimum discriminator` §4.2 cut 1, `RT-MD-05`; `stability census` §9.1 arm 4) | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **DEC-2** | **Proteasomal vs lysosomal** fate of `Q230P` | 🔴 **No — no WWOX allele has a route established except `P252A`, a different allele** | FULL BODY for `P252A` (PMID 41124647, PMC12767083) | **VERY HIGH** — `wwox_missense_cma_degradation_audit_20260921.md` + `matrix` row 3: MG-132 negative, CQ and NH₄Cl restore, 3-MA negative. And the **trap is identified**: `proteostasis_discrimination_protocols` §3 shows chloroquine **negative** where bafilomycin was **positive** on the same endogenous mutant protein in the same primary-fibroblast experiment | ANALYSIS ONLY (the `P252A` route itself is ledgered) | 🔴 `P252A` is **ClinVar `Benign`**, on a CMV Flag transgene in thyroid carcinoma, in a person with no WWOX-related nervous-system disease. **The class transfers; the conclusion does not** | Bafilomycin A1 **+** MG-132 at 37 °C, chloroquine cut as a known producer of uninterpretable negatives — `minimum discriminator` §1.5; `protocols` rank 2 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **DEC-3** | Is the route **CMA** (`KFERQ`-like `LRSVQ` 187–191)? | 🟢 **Yes — answered: named, NOT established** | FULL BODY | **HIGH** — `matrix` row 3: the motif was **never mutated**, `LAMP2A`/`LAMP2` occur **zero** times, the colocalisation marker is **LAMP1** not the CMA receptor, and the figure legend is weaker than the Results sentence | 🟡 **LEDGER** — `DL-MECH-052` recorded **WEAKENED** | Whether `Q230P` is a substrate for **any** specific clearance route (`minimum discriminator` `COULD NOT ESTABLISH` item 6) | `LAMP2A` knockdown + `LRSVQ` motif-ablation, CQ as positive, MG-132 as expected negative — `matrix` row 3 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **DEC-4** | Does the **corpus's own lysis chemistry** let "degraded" be told from "in the pellet"? | 🟢 **Yes — answered NO, and the cause is a third kind** | Manifest-level + Methods-level | **HIGH** — `DISCOVERY_TRACE_lysis_chemistry_20260922.md` §4.3: a **schema-side omission** (`C`), distinct from source-side omission (`A`) and hand-back compression (`B`) — *"the deep-dive manifest schema has no slot for reagent or Methods chemistry at all"* | ANALYSIS ONLY | Cause `C` needs a second independent instance before any schema change; §5 **weakens** it | Pre-stated follow-up in §4.4 (executed, §5) | 🟢 **RESOLVED** (as a method finding) |

## 1.6 · DETECTION

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **DET-1** ⭐ | **Which antibody produced `Q230P`'s founding blot, and where is its epitope?** | 🔴 **No — `NOT ATTRIBUTABLE`** | 🔴 ABSTRACT_ONLY / `METHODS_INVISIBLE`. No vendor, no catalogue, no clone, no host, no immunogen | 🔴 **VERY HIGH** — `wwox_antibody_epitope_census_20260922.md` §4.3: *"The two published 'absent WWOX protein' results that this disease model depends on most — `Q230P` and `G372R` — are the two the census cannot attribute to any antibody at all"* | ANALYSIS ONLY; `CLAIM 030` carries `PREMISE: DETECTION_FLOOR` | 🔴 **0 / 12** census rows state an epitope position relative to the variant (`abundance lysis census` §1.2) | Acquisition target 10 — `johannsen2018…` §4 | 🔴 **HUMAN_REQUIRED** / source-depth limited |
| **DET-2** | Does a **flanking antibody pair** (N- and C-terminal to `Q230`) exist? | 🟢 **Yes — answered: NO. Zero of seventeen** | Vendor datasheets **`EGRESS_BLOCKED`** for `CST 4045S`, `ab238144`, `ab189410`, `ABN413` | **VERY HIGH** — `antibody epitope census` §2.1: the N-terminal member exists and is excellent (**`HPA050992`, aa 32–110**, printed in a peer-reviewed Methods section); the C-terminal member has **no candidate at all** | ANALYSIS ONLY — it **rewrites** the procurement line of `minimum discriminator` §1.8 | 🔴 The C-terminal epitope is **unverifiable from this deployment**, and the census refuses to say what an unread datasheet "should" contain | 🟢 **Two bench substitutes specified**: `S1` epitope tag with band **size** scored; `S2` **fragment competition** against the already-defined GST fusions `ww (1–110)` and `ADH (110–414)` — *"two bacterial preps, two blots, one afternoon"* — `antibody census` §2.2 | 🔴 **SOURCE-DEPTH LIMITED** (with a bench workaround already designed) |
| **DET-3** | Could a **stable N-terminal species** have been missed? | 🟢 **Yes — answered: YES for `Q230P`, and nothing excludes it** | — | 🔴 **VERY HIGH** — `antibody census` §4: 10 *"absent/reduced"* results audited row by row; **4/10** could have missed an N-terminal species; **1 is demonstrated to have happened in print** — the `lde` rat, where *"no protein"* became *"a very weak band … due to greater sensitivity of the new antibody, directed against amino acids 32–110"* | ANALYSIS ONLY | For a **point substitution** a fragment is not the leading hypothesis, but a **fold-dependent epitope loss** in the SDR is, and it is unexcludable with an unknown epitope | Two epitope-stated antibodies flanking 230, **score by band size, not signal alone** — `minimum discriminator` §1.8 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **DET-4** | What is the **detection floor**? | 🔴 **No number exists anywhere** | — | **HIGH** — `abundance lysis census` §1.2: **0 / 12** rows state a floor, an LOD or a dilution series; `survival paradox` §3 rank 2: the floor *"is not merely unmeasured but unreadable from here"* | 🟢 **CANONICAL** — `PREMISE: DETECTION_FLOOR` on `CLAIM 030` (`claim_registry_current.md:559`) | 🔴 **Without a number, *"absent"* is a sentence, not a measurement**, and `H1` (nothing is made) cannot be assigned from it at all | ≥5-point dilution series on the same membrane, **LOD in ng**, *"not detected"* written only as *"below X ng, N = 3"* — `minimum discriminator` §1.8; the calibrated, epitope-mapped, series-commensurable blot in `survival paradox` §3 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |

## 1.7 · FUNCTION

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **FUN-1** ⭐ | **Function per total protein** — does a `Q230P` molecule work? | 🔴 **No.** *"No functional measurement has ever been made on a WWOX missense protein whose abundance was restored"* | FULL BODY for the two source papers | 🔴 **VERY HIGH, and adjudicated twice from opposite directions** — `function_per_molecule_assay_design_20260922.md` §3 recommends a **donor-saturation NanoBRET** with the NanoLuc donor channel as the same-molecule denominator; `wwox_functional_readout_tractability_20260922.md` §6 counters with a **mass-matched recombinant GST-WWOX kinase-inhibition titration** | ANALYSIS ONLY — `matrix` names it *"the single biggest missing link"* | 🔴 The two designs measure **different things**: engagement competence per molecule (cellular) vs catalytic output per µg (recombinant). Neither has been run | `function_per_molecule` §3; `tractability` §6; `matrix` *"best next experiment"*; `direct discriminator` §7 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **FUN-2** | Is **`POLE4`** a usable numerator? | 🟡 **Partly — and weakened** | FULL BODY of PMID 41124647; 🔴 **Figure S9 (Supporting Information) NOT obtained** | **HIGH** — `direct discriminator` §6: `POLE4`'s binding site on WWOX is **unmapped** (`SDR`/`short-chain`/`dehydrogenase` = **0** in the body); *"SDR-span"* is the reader's arithmetic; every WWOX–`POLE4` measurement in existence was made **after UV**; `P282A` is now `OVEREXPRESSION-ARTEFACT SUSPECT` (rs3764340, ClinVar `Benign`, 18 healthy homozygous controls) | ANALYSIS ONLY | 🔴 `RT-MD-08`: *"all four links currently fail"* — the repair is Fig S9 at **matched WWOX input**, a fragment/deletion series, or a ±UV comparison | `P282A` kept **as a direction, never as a magnitude**; `H-3` parks Fig S9 — `minimum discriminator` §7.3 | 🔴 **SOURCE-DEPTH LIMITED** (supplement unobtained) |
| **FUN-3** | Is **`GSK3β`** a numerator or a ruler? | 🟢 **Yes — answered: a RULER, not a co-primary numerator** | FULL BODY (PMID 22193544) | **HIGH** — `direct discriminator` §6: `G` owns exactly one cell (`R6`) and no mechanism column; used **only in its strong direction** (loss ⇒ global), never in its weak one (normal ⇒ folded) | 🟢 **CANONICAL** — `CLAIM 035` (`claim_registry_current.md:644`, in observation): residue-mapped, Axin-like docking 388–407 / `L404`, **S9-independent**, neuronal output requires Tau | 🔴 `RT-MD-09`: whether presenting aa 388–407 **requires the SDR core fold has never been measured** — `PREMISE: UNVERIFIED` | 🟢 It **tests its own premise for free** inside the plate: `G` low for `Q230P` while WT/`Q230A`/`Q230M` are normal would be the first evidence that SDR folding is required — `direct discriminator` §6 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **FUN-4** | Is any **true catalytic** readout usable for this question? | 🟢 **Yes — answered: CLOSED, on five independent grounds** | 🔴 The only WWOX enzymology paper (PMID 21476439) is **`UNREAD_PRIMARY`** — no PMCID, three independent PMC checks negative | **VERY HIGH** — `function_per_molecule` §5.3: no denominator, no attribution (`E. coli` lysate carries endogenous NAD(P) dehydrogenases; no dead-triad control), **wrong lesion class** (12.60 Å from the cofactor-cleft axis, 6.79–9.68 Å from the triad, side chain 141° away), unresolved reaction direction, and the method is unread | ANALYSIS ONLY | 🟢 **One element survives: `E1`** — express WT and `Q230P` SDR side by side in a heterologous host and blot soluble vs inclusion-body pellet, **no activity readout at all** | `function_per_molecule` §5.3 (`E1` minimum modernisation); `wwox_sdr_function_per_molecule_census_20260921.md` §8 (deorphanise, with the controls the 2011 paper did not have) | 🟡 **PARTIALLY RESOLVED** (closed for discrimination; `E1` proposed) |
| **FUN-5** | Are there **alternative readouts** at all? | 🟢 **Yes — an 11-candidate inventory, scored** | Mixed: FULL BODY for `A1`/`A3`, abstract for `A6`, unread for `A5` | 🔴 **VERY HIGH** — `tractability` §2: **two rows pass criteria 1–3** (`A1` GSK3β/Tau kinase inhibition; `A2` its GS-1 variant); `A4` WWOXtide is the **calibrator**; `A3` turbidimetry is **disqualified for missense work** (a misfolded prep scatters at 350 nm and reads as rescue); `A11` pS9 is a **documented false-negative generator**; every pull-down/co-IP/FRET/NanoBRET is scored 🔴 on criterion 1 **by construction** | ANALYSIS ONLY | 🔴 **(d2)** — that any of these is a **demonstrated physiological function of WWOX** — is `NOT SATISFIED for any WWOX readout in existence`. The substrate is undiscovered after twenty years | `tractability` §6 compressed experiment | 🟡 **PARTIALLY RESOLVED** |
| **FUN-6** | Can a function readout be run in **pooled / multiplexed** format? | 🟡 **Partly — the abundance half is portable, the function half is not** | ⚠️ **5 of 6 MAVE papers `UNTESTED` for retrievability**; only the degron preprint verified open | **HIGH** — `missense_rescue_methodology_census_20260921.md` §2–§4: VAMP-seq measures steady-state abundance of thousands of variants and **needs no substrate**; paired abundance+function MAVEs exist on two oxidoreductases (CYP2C9, CYP2C19) — *"WWOX has simply never been put through it"* | ANALYSIS ONLY; therapeutic classification **`MECHANISTIC PROBE ONLY`** | 🔴 *"Whether any of those [SDR-partner binding readouts] can be run in pooled, multiplexed format is the open question this census hands forward, and it is unanswered"* | 🔴 **None** | 🔴 **TRUE EXPERIMENTAL GAP** |

## 1.8 · STRUCTURE

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **STR-1** | **Where is `Gln230`** in the fold? | 🟢 **Yes — RESOLVED as a statement about the model** | Own numpy geometry on `data/WWOX_Q9NZC7_AlphaFold.pdb` (pLDDT 98.50 at 230) | 🟢 **VERY HIGH** — `q230p_structural_mechanism_20260922.md` §1.3: **relSASA 0.000 / SASA 0.0 Å²**, burial 200 (83.8th %ile), 22 heavy-atom contacts ≤5 Å; five side-chain polar contacts, **three long-range** (Δseq −44 to −46), forming a Q230·D223·A185/L187 staple of helix αE to strand βC | ANALYSIS ONLY — **and it corrects the repository's own held record** (§1.4: the *"salt bridge"* to D223 is a **neutral-donor hydrogen bond**; the *"6-residue helix"* is an artefact of the strictest of three criteria) | 🔴 It is a **predicted monomer**; side-chain rotamers are the weakest part of any predicted model | — | 🟢 **RESOLVED** (model-class) |
| **STR-2** | Does **proline at 230 disrupt the backbone**? | 🟢 **Yes — and the honest half is stated** | Own geometry | 🟢 **VERY HIGH** — §3.1: **φ is NOT the problem**; §3.2: the modelled Pro Cδ lands **1.60 Å** from the Glu226 carbonyl oxygen — a **1.44 Å hard overlap** — and cannot donate the i,i−4 amide hydrogen N230 donates to O226 (3.03 Å, 9° deviation) | ANALYSIS ONLY | 🔴 Which accommodation the helix takes — **fraying (Branch A) or kinking (Branch B)** — §3.3: both are expensive, the nearest coil is four residues too far upstream | 🔴 **`md_q230p_protocol.md`** — pre-registered, observable corrected to **backbone H-bond occupancy propagation** (explicitly **not** counting `O226···N230`, lost by construction), SDR-only box, HMR/4 fs, ≥3 replicas. 🔴 **MD engine BLOCKED — `md_status.py` 0/12, no openmm, no gromacs** | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** (tooling-blocked) |
| **STR-3** ⭐ | Is `Gln230` at an **oligomer / dimer interface**? | 🟢 **Yes — answered NO, by a topology-independent argument** | Own geometry | 🟢 **VERY HIGH** — §5.1: a residue at **relSASA 0.000** cannot be buried further by a partner subunit; ≥12.5 Å to the nearest exposed residue of either documented SDR interface mode; 226–240 has no exposed face | ANALYSIS ONLY — **and it contradicts a premise quoted forward through three analysis files** (`discovery_ledger_current.md:852`) | 🔴 **§5.5: the premise underneath the question did not survive checking.** A fully-expanded PubMed query for WWOX dimerisation returns **one** record, about p-WWOX/p-p53 **hetero**-dimers. *"I could not find a published source establishing that WWOX homodimerises through its SDR at all."* `PREMISE: UNVERIFIED` | 🟢 **§10 item 1: run AlphaFold-Multimer on WWOX ×2 and measure ΔSASA at residue 230 — no wet work, no spend.** Plus §10 item 2: trace `discovery_ledger_current.md:852` to its source — *"minutes of work"* | 🔴 **TRUE EXPERIMENTAL GAP** (cheap, computational — the one falsifier of the therapeutic sign achievable today) |
| **STR-4** | **`Q230A` / `Q230M`** controls — is the lesion backbone or side-chain? | 🔴 **No — designed, never run** | — | **HIGH** — `direct discriminator` §3.2 gives the full four-row reading (proline-backbone-specific · side-chain polar network · amide-specific · volume/packing) and its consequence: *"no ligand restores a hydrogen bond the chain cannot donate"*. `q230p_therapeutic_mechanism_expansion_20260922.md` §7.3 makes the series **the core refinement**; `Q230G` is **excluded** (perturbs side chain and backbone at once) | ANALYSIS ONLY | 🔴 They are **transgene arms** and are correctly **cut** from the endogenous fibroblast experiment (`minimum discriminator` §1.7), so the two designs cannot both carry them | `direct discriminator` §3.2; `therapeutic expansion` §7.3 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **STR-5** | Do **SDR fold-family analogies** transfer? | 🟢 **Yes — answered with the transfer direction stated** | Passage/abstract depth | **HIGH** — `stability census` §8: the degradation side is well documented; the **aggregation** side is rarer and the exemplar's trigger is **interface substitution** (PMID 18775764), which is **not `Q230P`'s class** (`structural` §7.1) | ANALYSIS ONLY | 🔴 *"Not the known trigger"* is not *"will not aggregate"*; the family supplies a **prior**, not an answer, and the prior **forks on a structural fact nobody has determined** | — | 🟡 **PARTIALLY RESOLVED** |
| **STR-6** | **Residue-level conservation** at position 230 | 🔴 **Not established** | 🔴 UniProt / EBI / RCSB all `connect_rejected`; no local MSA | **MODERATE** — §6.2: ESM-2 prefers **G/A over Q** at 230, so the glutamine's own identity is **not** the conserved element; §6.1: the literature supplies whole-protein, not residue-level, conservation | ANALYSIS ONLY | ⚠️ It can only strengthen or weaken §2 row 5 (the network); **it cannot touch §5**, which rests on geometry | Fetch ~20 orthologue sequences through an allowlisted route — `structural` §10 item 5 | 🔴 **SOURCE-DEPTH LIMITED** (egress) |
| **STR-7** | **Physical stability** (Tm / CD melt / ΔG) of the `Q230P` SDR | 🔴 **No — `NEVER TESTED`, and not available at any price today** | — | **HIGH** — `stability census` §3.4: the only WWOX biophysics that exists (PMID 35716775) covers residues **16–91** and tested no disease variant. **No purified folded WWOX SDR exists; expressing one is itself an unsolved problem in this literature** | ANALYSIS ONLY | 🔴 A falsifier is named (*"Tm indistinguishable from wild type"*) and is explicitly **unobtainable** (`structural` §8.3) | Only the indirect `E1` soluble-vs-inclusion split (`function_per_molecule` §5.3) | 🔴 **TRUE EXPERIMENTAL GAP** |

## 1.9 · THERAPEUTIC — mechanism qualification only

🔴 **No compound, dose, route, screen or repurposing sweep appears in this section or anywhere in this
file.** Reagents named in cited files are bench reagents in culture, or published experiments on other
proteins. `TX-003` and `HYP-20260709-02` remain **conditional** exactly as the ledger has them; nothing
here de-conditions either.

| # | Question | Already answered? | Source depth | Analysis depth | Propagation depth | Remaining uncertainty | Experiment already proposed (file) | Status |
|---|---|---|---|---|---|---|---|---|
| **THX-1** | Are the **four chaperone entry criteria** met? | 🟢 **Yes — each answered separately** | Mixed | 🔴 **VERY HIGH** — `minimum discriminator` §5: **(a) substrate exists — UNKNOWN**; **(b) instability/misfolding supported — NOT SUPPORTED** (the ΔΔG carries no weight in either direction); **(c) the state can be shifted — UNTESTED for WWOX**; **(d) a functional readout exists — the binding condition.** `tractability` §1 then splits (d) four ways: **(d1) SATISFIED**, **(d2) NOT SATISFIED for any WWOX readout**, **(d3) not satisfiable in a patient cell at any price / cheap on a recombinant prep**, **(d4) satisfiable today and never attempted** | ANALYSIS ONLY; `TX-003` / `HYP-20260709-02` stay **conditional** | 🔴 The classification stands as **`CHAPERONE PROGRAM — MECHANISTIC QUALIFICATION`** — *"not a screen, not a candidate list, not a therapeutic route"* | The classification **is** the output | 🟡 **PARTIALLY RESOLVED** |
| **THX-2** ⭐ | **Sign** of a non-allele-specific WWOX boost | 🟡 **Yes — answered: NOT-DANGEROUS-ON-THIS-EVIDENCE, and STILL UNDETERMINED** | — | 🔴 **VERY HIGH** — `structural` §9 removes the **identified** red flag (`Q230P` is not an interface-substitution lesion) and then refuses to green the axis on three independently sufficient grounds: the pellet has never been looked in; abundance ≠ stability ≠ solubility ≠ function; and the evidence base is **90.9 % empty** (10 of 11 alleles with no experimental evidence, by the source's own denominator) | 🟡 **LEDGER** — `therapeutic_hypotheses_ledger_current.md:216`: *"il segno del beneficio dipende **interamente** dal destino di folding di Q230P, ad oggi **ignoto**"* | 🔴 It rests **entirely** on `SOL-3`. One lane decides it | The solubility split — `stability census` §9.1 arm 1; `function_per_molecule` §4 | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **THX-3** | **Proteostasis** — which lever class is coherent? | 🟡 **Ranked, with each rank's own killer stated** | Passage-depth | **HIGH** — `q230p_therapeutic_mechanism_expansion_20260922.md` §4: rank 1 (cofactor/natural activator) is killed by **sign inversion with cofactor occupancy** (§4.2); rank 4 chemical chaperones fail on **compartment mismatch** (§4.5); `q230p_pharmacological_precedents_20260922.md` §4.4 refuses the cofactor arm outright | ANALYSIS ONLY | 🔴 WWOX's cofactor occupancy, preference and direction are **all unknown**, and PMID 21476439 is unread | `precedents` §4.5 minimum experiment; `expansion` §8.1 | 🟡 **PARTIALLY RESOLVED** |
| **THX-4** | **Translation rescue** as an intervention class | 🔴 **No** | — | **MODERATE** — the branch is named: on `M1′` a boost *"adds substrate to a failing step"* and *"a proteostasis inhibitor does nothing"* (`stability census` §5) | ANALYSIS ONLY | 🔴 **No intervention class has ever been enumerated for the `M1′` branch anywhere in this repository.** The other two branches each have a named class; this one has none | 🔴 **None** | 🔴 **TRUE EXPERIMENTAL GAP** |
| **THX-5** | Does **abundance rescue give functional rescue**? | 🟢 **Yes — answered: it does not follow, and both directions are documented** | FULL BODY / passage | 🔴 **VERY HIGH** — `minimum discriminator` §4.1 sets two published precedents of the **same intervention class with opposite outcomes**: NPC1 patient fibroblasts, where proteasome inhibitors *"partially recovered their activity"*; and ubiquitin-activating enzyme E1 `TS20`, whose own figure legend reads *"**Stabilizing E1 mutant is not sufficient to rescue the temperature-sensitive phenotype**"*. `P282A` is the standing WWOX proof: stable and functionally dead | ANALYSIS ONLY | 🔴 *"More protein is not more functional WWOX"* — and `DL-MECH-049` records that in WWOX *"la stabilità si compra con l'occlusione"* | The abundance-clamped, domain-resolved function-per-molecule comparison — `matrix` *"best next experiment"* | 🟡 **EXPERIMENT PROPOSED BUT UNRUN** |
| **THX-6** | Does the **survival advantage of the "≥1 missense" class** attach to `Q230P`? | 🟢 **Yes — answered: neither offered option is correct** | Mixed; 🔴 the per-individual data sit in a **supplementary table absent from the retrievable body** | 🔴 **VERY HIGH** — `q230p_survival_paradox_20260921.md` §1–§3: within homozygous `Q230P` the recorded endpoint runs from **death at 3 y 3 m** to **alive at 23 y 11 m**; the association **fails to replicate** (*p* = 0.432, direction inverted); `Q230P` is ~a third of the class | 🟢 **CANONICAL** — `CLAIM 033` in observation (`:604`); the file proposes a **fifth reservation** and that `TX-003` **stop citing the survival statistic as support** | 🔴 The recomputation **cannot be performed from published sources** | Calibrated, epitope-mapped, series-commensurable Western against a recombinant standard curve — `survival paradox` §3 | 🔴 **SOURCE-DEPTH LIMITED** |
| **THX-7** | Is **material** (`Q230P` fibroblasts / an isogenic knock-in pair) obtainable? | 🔴 **No — `PREMISE: UNVERIFIED`** | — | — | ANALYSIS ONLY | 🔴 **The binding cost of every design in this matrix.** *"Not a scientific question, and not mine to act on"* | `H-2` — `minimum discriminator` §7.3. **No external action was taken by any actor** | 🔴 **HUMAN_REQUIRED** |

## 1.10 · Positions the repository has WITHDRAWN — recorded so they are not re-derived

| # | Withdrawn position | Why | Where | Status |
|---|---|---|---|---|
| **SUP-1** | **26–30 °C permissive temperature as a folding-specific lever** | Mild hypothermia is **simultaneously a global degradation inhibitor** — *"the degradation rates of all mRNAs and proteins examined were much reduced at 27 °C"*, with 9 of 17 changed proteins being **chaperones**. A band appearing at 30 °C is ambiguous between *folded* and *no longer cleared* — the exact pair the experiment exists to separate | `minimum discriminator` §1.6 (refutes three prior files); `three_designs` §4 strike-through; `precedents` ORCHESTRATOR WITHDRAWAL | 🔵 **SUPERSEDED** (demoted to Tier 2 with named triggers, `RT-MD-01`) |
| **SUP-2** | **ThermoMPNN ΔΔG `+1.514` as evidence of instability** | The predictor is **inverted against the six measurements that exist**: the highest predicted ΔΔG (`P47T`, +2.81) has **normal** protein in two matrices; the lowest has the only demonstrated accelerated degradation | `stability census` §6.1 | 🔵 **SUPERSEDED** (evidentially empty in **both** directions) |
| **SUP-3** | **The *"rescuable window ΔΔG 0.8–3.5"* heuristic** | Self-declassed: *"La finestra non discrimina"* | `discovery_ledger_current.md:838`; internal correction in `CLAIM 019` | 🔵 **SUPERSEDED** |
| **SUP-4** | **`C299R` as an off-route killer control** | The 3.44 Å used was **backbone-backbone**; SG(C299)–NZ(K297) = **10.706 Å** | `data/redteam/premises_epistemic_table.csv:13`; `md_q230p_protocol.md` | 🔵 **SUPERSEDED** |
| **SUP-5** | **`P282A` as a simple complete-loss control** | It is **rs3764340, ClinVar `Benign`, 18 healthy homozygous controls**, on a CMV transgene in thyroid carcinoma — now `OVEREXPRESSION-ARTEFACT SUSPECT`; kept **as a direction, never as a magnitude** | `abundance lysis census` §1.1 row 10; `therapeutic expansion` §7.2; `direct discriminator` §6 | 🔵 **SUPERSEDED** |
| **SUP-6** | **`Q230P` "first measurement" framing** | The experiment **has already been performed once**, and its ambiguity is why three independent designs exist. Both designs were proposing a *first* measurement of something with a **published prior** | `q230p_three_designs_one_experiment_20260922.md` §1, §5 | 🔵 **SUPERSEDED** (reframed as a re-run under discriminating conditions) |

---

# 2 · THE TRUE FRONTIER — the smallest set of genuinely unresolved questions NOT already worked out in LEGEND

**Only rows whose status is `TRUE EXPERIMENTAL GAP` or `SOURCE-DEPTH LIMITED` appear here.** Ranked by
(information gain × therapeutic consequence × executability). 🔴 **Every other row in §1 is either
resolved, superseded, partially resolved with the open axis named, or already carries a specified
discriminating design that has simply not been run. A design is not a result — but it is also not a
frontier.**

| rank | frontier item | what LEGEND already knows | why it is still open | the next discriminator |
|---|---|---|---|---|
| **1** ⭐ | **Johannsen 2018's Methods — buffer, spin, pellet, antibody + epitope, detection floor, `n`, qPCR amplicon, and whether the MeSH-indexed HEK293 arm exists** (`SOL-1`, `DET-1`, `RNA-1`, `RNA-2`, `DET-4`) | The endpoint (*normal transcript, protein not detected*), that it is the **only** functional study of the gene's **most recurrent allele — 8 patients, 6 families**, and that all eleven extraction targets are enumerated and un-filled | 🔴 Springer-closed, `pmc_id: null`, **four independent agent acquisition attempts have failed**, the most recent under a proven egress control. It is not a retrieval task an agent can complete | **One PDF, obtained by a human** (author contact / WWOX Foundation / ILL), read against the one-pass ordered extraction list in `johannsen2018…` §6.4. It is **`NEW ANALYSIS ONLY`, costs nothing but access**, and item 6 alone (the buffer) is falsifier `F7`: a denaturing whole-cell lysate would mean `H3` was excluded in 2018 and would **collapse the most expensive component of the entire programme** |
| **2** ⭐ | **Does WWOX homodimerise through its SDR at all — and is residue 230 within contact distance of a partner chain?** (`STR-3`) | `Gln230` has **relSASA 0.000**, is ≥12.5 Å from either documented SDR interface mode, and a residue at exactly 0.0 Å² cannot be buried further by a partner. The homodimer premise is quoted forward through three analysis files from `discovery_ledger_current.md:852` **with no citation**, and a fully-expanded PubMed query returns **one** record — about hetero-dimers | 🔴 No AlphaFold-Multimer or dimer model of WWOX exists in this repository; `files.rcsb.org`, `rest.uniprot.org` and `www.ebi.ac.uk` are all `connect_rejected`. The fork was treated as a live 50/50 on an **unsourced** premise | **Run any dimer predictor on WWOX ×2 and measure ΔSASA at residue 230** — *no wet work, no spend, no material*. It is the single falsifier of the therapeutic sign achievable computationally today, and it would simultaneously place the exposed W335/W336 patch. Paired with a **minutes-long record move**: trace `discovery_ledger_current.md:852` to its source and label it |
| **3** | **The C-terminal half of the flanking antibody pair** (`DET-2`) | The N-terminal member exists, is excellent and is already in the canonical ledger — **`HPA050992`, aa 32–110**, published in a Methods section. The C-terminal member is **zero of seventeen** | 🔴 Every route to the four candidate reagents' epitopes is a **vendor datasheet**, and every vendor datasheet is `EGRESS_BLOCKED` in this deployment. The census refuses to invent what an unread page "should" say | 🟢 **Do not buy it — map it.** Fragment competition against the GST fusions **`ww (1–110)`** and **`ADH (110–414)`**, already defined verbatim in PMID 22193544: *"two bacterial preps, two blots, one afternoon"*. It converts an unreachable datasheet into a measured fact — the method the field already had and has not used for twenty years |
| **4** | **A protein-specific nascent-synthesis measurement for a low-abundance protein in primary human fibroblasts** (`PROD-1`) | That the branch is live, that it is one of exactly three causes compatible with *normal mRNA + no protein*, and that **SUnSET / OP-puro / AHA-imaging all measure global translation and would say nothing about WWOX** | 🔴 There is **no published instance** of the measurement in this matrix, and it needs an anti-WWOX antibody validated for **immunoprecipitation from primary fibroblast lysate** — a cheap catalogue check (`B13`) that has never been done and that gates a ~10³–10⁴ EUR experiment | ³⁵S or AHA-click pulse **plus WWOX immunoprecipitation**, staged **last**, and preceded by the one-line reagent check. Until then `M1′` is reachable only **by elimination** (row `R2`), which is weaker evidence than measurement and must be labelled so |
| **5** | **Figure S9 of PMID 41124647 — the `P252A`–`POLE4` co-IP at matched WWOX input** (`FUN-2`) | That `POLE4`'s binding site on WWOX is unmapped, that every WWOX–`POLE4` measurement was made after UV, and that `P282A` is now an overexpression-artefact suspect — *"all four links currently fail"* | 🔴 Supporting Information was never retrieved; the body was read, the supplement was not | **Obtain the supplement** (`H-3`). It repairs link 1 of the numerator chain. Failing that, a fragment/deletion series mapping `POLE4`'s site, or a ±UV comparison showing constitutive engagement — any one repairs a different link |
| **6** | **Whether a fibroblast result transfers to the disease-relevant cell type** (`SOL-6`) | A published demonstration that an SDS-insoluble species formed **only in patient neurons and not in the same patients' fibroblasts**, and that **no WWOX protein measurement in patient brain exists for any missense allele** | 🔴 No neuronal, iPSC-derived or post-mortem `Q230P` material is in reach, and the repository records that the highest-value material in this field **has already been destroyed once** — an FFPE fetal brain from a homozygous carrier with no RNA taken | 🔴 **No design exists, and this is named as a limit of the material, not of the design.** The only concrete standing ask is procedural: **when WWOX post-mortem or termination material is next handled, snap-freeze or RNAlater a fragment before fixation.** One tube |
| **7** | **Physical stability of the WWOX SDR domain** (`STR-7`) | That it has never been measured for any disease variant; that the only WWOX biophysics in existence covers residues **16–91**; and that the named falsifier (*Tm indistinguishable from WT*) is explicitly unobtainable | 🔴 **No purified folded WWOX SDR exists, and expressing one is itself an unsolved problem in this literature** — it must be costed separately, never assumed | The **indirect** substitute only: `E1` — express WT and `Q230P` SDR side by side in one heterologous host and blot **soluble fraction vs inclusion-body pellet, with no activity readout at all**. ⚠️ Bacterial folding is not mammalian folding; it yields a **prior**, not an answer |
| **8** | **PMID 21476439 — the only WWOX enzymology paper ever published** (`FUN-4`) | That it reports oxidoreductase activity in a **crude extract**, with no purified amounts, no dead-triad control and no named negative-lysate control; that the reaction **direction** is in open conflict with a 2015 review; and that the catalytic route is **closed for the discrimination question** on five independent grounds | 🔴 No PMCID; three independent PMC checks negative; publisher egress blocked. *"You cannot modernise a method nobody has read"* | Author contact or ILL (`H-4`). It is the only source that could say whether WWOX binds NAD(P) at all — which the entire cofactor-cleft geometry currently **assumes from the fold** — and it gates the cofactor question that the chaperone qualification refuses on sign-inversion grounds |
| **9** | **Whether any WWOX function readout can be scored in POOLED format** (`FUN-6`) | That the **abundance** half of a MAVE is portable to WWOX today (VAMP-seq needs no substrate), that paired abundance+function MAVEs exist on two oxidoreductases, and that the candidates for a WWOX function are **binding**, not catalysis | 🔴 CYP2C9/CYP2C19 are tractable **because their substrates are known**. WWOX's is not — *"the substrate and product of the enzyme reaction that it catalyses are yet to be discovered"*. And 5 of the 6 template papers are **`UNTESTED` for retrievability** | Fetch the six templates first (one call each), then ask the single unanswered question: **can an SDR-partner engagement readout be arrayed in a pooled, sequencing-scored format?** If not, the many-allele route is closed and the one-allele design stands alone |
| **10** | **No intervention class has ever been enumerated for the `M1′` (synthesis / co-translational triage) branch** (`THX-4`) | That on `M1′` *"a boost adds substrate to a failing step"* and *"a proteostasis inhibitor does nothing"* — i.e. that both of the repository's named therapeutic classes are **inert or harmful** on this branch | 🔴 The other two branches each have a named lever class. **This one has none, and the absence has never been worked** — it is the only mechanism column in the whole matrix with an empty therapeutic row | 🔴 **Enumerate first, do not search first.** Before any lever is proposed, `SOL-3` and the lever panel must assign the branch — a class proposed for a branch that turns out not to be the lesion costs more than the delay |
| **11** | **Residue-level conservation at position 230** (`STR-6`) | That ESM-2 prefers **G/A over Q** at 230, so the glutamine's own identity is **not** the conserved element, and that SDR **interface** residues are not conserved even between orthologues | 🔴 UniProt, EBI and RCSB are all `connect_rejected`; there is no local MSA | Fetch ~20 orthologue sequences through an allowlisted route. ⚠️ **Bounded before it is run:** it can only strengthen or weaken the polar-network row. **It cannot touch the interface exclusion, which rests on geometry** |
| **12** | **`Q230P` mRNA stability, and the per-individual survival table** (`RNA-2`, `THX-6`) | That `RNA Stability` is a MeSH descriptor on Johannsen with **no matching abstract sentence** — `PREMISE: INDEXED_EXPERIMENT_EXISTS`; and that the survival recomputation needs a supplementary table absent from the retrievable body | 🔴 Both are acquisition, not science. Both ride on documents a human can obtain | Rank-1's PDF answers the first. The second needs **Oliver 2023's supplementary per-individual table** — and the file that names it already states that removing `Q230P` from the class *"cannot be computed from published sources"* |

---

## 3 · HEADLINE VERDICT — stated as bluntly as the evidence permits

> ## 🔴 **The frontier is small, and it is not mostly scientific.**

**Of ~40 distinct questions enumerated across nine groups:**

| status | count | reading |
|---|---|---|
| 🟢 **RESOLVED** | 5 | mostly structural geometry computed in-house, plus two verified field-wide zeros |
| 🟡 **PARTIALLY RESOLVED** | 5 | answered on one axis with the open axis explicitly named |
| 🟡 **EXPERIMENT PROPOSED BUT UNRUN** | 15 | 🔴 **the single largest class** |
| 🔴 **SOURCE-DEPTH LIMITED** | 7 | |
| 🔴 **TRUE EXPERIMENTAL GAP** | 7 | of which **two are cheap** and one needs only a procedural instruction |
| 🔴 **HUMAN_REQUIRED** | 3 | acquisition, material, and one programme decision |
| 🔵 **SUPERSEDED** | 6 | positions the repository has withdrawn, recorded so they are not re-derived |

**The three things this reconstruction establishes, in order of how much they should change behaviour:**

1. 🔴 **Almost everything mechanistic about `Q230P` is already worked out — to the point of a
   specified, falsifiable, discriminating design that nobody has run.** Fifteen of ~40 rows are a
   design waiting on material. The designs are not vague: they name the buffer, the spin, the
   loading discipline (equal **cell-equivalents**, never equal protein), the loading control (total
   protein stain, never β-actin), the lever panel (bafilomycin A1 **and** MG-132, chloroquine cut),
   the read order, seven named falsifiers of the design itself, and eleven revival triggers. **The
   binding cost is not knowledge. It is material access and one PDF.**
2. 🔴 **The two data points that carry the most patients in this disease are both `abstract-depth`.**
   `Q230P` is the most recurrent WWOX allele of any class — **8 patients across 6 families** — and
   both of its experimental facts come from one unread abstract. Meanwhile **0/12** published WWOX
   missense measurements examined a pellet, **0/12** stated an epitope, and **0/12** stated a
   detection floor. **The emptiness is the field's, not this allele's** — of 19 enumerable WWOX
   missense alleles, exactly one has ever had RNA examined.
3. 🔴 **Only two items on the frontier are both genuinely open and cheaply executable today**, and
   neither needs a bench: the **dimer/ΔSASA computation** that would falsify the therapeutic sign's
   residual branch, and the **fragment-competition epitope map** that makes the detection design
   purchasable. Everything above them is acquisition; everything below them needs material,
   reagents or a substrate nobody has found.

🔴 **What I refused to manufacture.** I found **no** mechanistic question about `Q230P` that LEGEND
has not already posed, and I have not invented one to pad the frontier. Where a row's honest status
was *"already designed, simply not run"*, it is recorded as that and kept **out** of §2. The one
genuinely under-worked cell in the entire matrix is `THX-4` — **no intervention class has ever been
enumerated for the synthesis/co-translational-triage branch** — and even that should not be worked
until `SOL-3` says whether that branch is the lesion.

---

## 4 · Declared limits of this file

1. 🔴 **No source was read at this file's own hand.** Every external datum is cited as **another
   actor's attestation**, at the source depth that actor declared. **No `FULLTEXT_READ_RECEIPT` is
   claimed and none is owed**, because no full-text route was taken.
2. 🔴 **Source depths are transcribed, not re-verified**, except `reading_state.md:98`
   (`PMID 29808465 = abstract_only`, ten body fields `unavailable`), which was read directly.
3. **Propagation depths** were taken from `claim_registry_current.md` (`CLAIM 019` line 343–360,
   `CLAIM 030` line 551–565, `CLAIM 033` line 602–619, `CLAIM 035` line 642), `discovery_ledger_current.md`
   (`DL-BIO-001`, `DL-MECH-019`, `DL-MECH-029:668`, `DL-MECH-049:1156`, `DL-MECH-052:1293`) and
   `therapeutic_hypotheses_ledger_current.md` (`HYP-20260709-02:210`, `HYP-20260709-08:291`), all
   **read-only**.
4. 🔴 **Counts in §3 are counts of the rows in §1 of this file**, not of the repository. They measure
   this reconstruction's own enumeration and are labelled as such.
5. **No claim was promoted, weakened, revived or retired**, and no commit candidate was produced.
6. 🔴 **No external contact, no purchase, no acquisition attempt and no egress was performed.** Every
   `HUMAN_REQUIRED` item is transcribed from the file that parked it and **re-parked**, not pursued.
7. **A fibroblast is not a neuron**; every cellular statement above concerns donor-derived fibroblasts
   or heterologous lines. **Nothing here is prognostic for any person**, and the survival row cuts
   explicitly against prognostic use: within one genotype the recorded outcomes span death at
   3 y 3 m to alive at 23 y 11 m.
8. 🔴 **Nothing in this file is medical advice.**

**END OF FILE — `q230p_true_frontier_20260922.md`.**

---

# 🎯 AMENDMENT — 2026-09-23, after `PMID 29808465` was read at full-body depth

> **Appended, not rewritten.** Every row above records the state when the load-bearing primary was
> `ABSTRACT_ONLY`. The Operator supplied the Johannsen 2018 PDF on 2026-09-23; it was read to receipt
> depth (`FTR-20260923-29808465-02`) and the five predictions preregistered on 2026-09-22 were scored
> **5/5 `SUPPORTED`**. This section supersedes the rows it names. Working file:
> [`johannsen2018_fulltext_q230p_revival_20260923.md`](johannsen2018_fulltext_q230p_revival_20260923.md).
> 🔴 **Nothing canonical is propagated by this amendment.** `CLAIM 019` and `CLAIM 030` are untouched.

## A · Rows whose status changes

| Row | Was | Now | Driver |
|---|---|---|---|
| `SOL-1` | 🔴 `HUMAN_REQUIRED` — eleven extraction targets `METHODS_INVISIBLE` | 🟢 **DISCHARGED.** Buffer, spin, pellet handling, antibody, load and detection are all now quoted verbatim | The Methods were read |
| `SOL-2` | 🔴 `SOURCE-DEPTH LIMITED` | 🟢 **RESOLVED.** *"Not detected"* means **not detected in the RIPA-soluble supernatant**, explicitly and only | *"the supernatant containing cellular proteins was collected"* |
| `RNA-1` | 🔴 `SOURCE-DEPTH LIMITED` — *"qPCR amplicon position `UNSTATED`"* | 🟢 **RESOLVED — positions stated.** Core = **exons 4–6** (277 bp), 3′ = **exons 8–9** (200 bp), both primer pairs printed | Methods, *"Quantification of WWOX transcription"* |
| `RNA-2` | 🔴 `SOURCE-DEPTH LIMITED` — MeSH `RNA Stability` suggested a decay chase | 🟢 **RESOLVED — NEGATIVE. No stability experiment exists.** `stabilit*` = 0 across the body, an earned zero | The MeSH term was indexer-assigned and is not backed by an experiment |
| `DET-1` ⭐ | 🔴 `NOT ATTRIBUTABLE` — *"no vendor, no catalogue, no clone, no host, no immunogen"* | 🟡 **`ATTRIBUTED, EPITOPE UNKNOWN`** — Santa Cruz **`sc-20528`**, goat, 1:200. Census row **`A21`** | Methods, *"Assessment of WWOX protein"* |

## B · Rows CONFIRMED at source — previously inferred, now measured

`SOL-3` (pellet never examined, for any WWOX allele) · `DET-4` (no detection floor anywhere) ·
`PROD-1` (no synthesis-rate measurement) — all three were **predictions**; all three are now **read
Methods**. 🔴 **Their status does not improve. It hardens.** The uncertainty they describe is no longer
provisional on an unread source.

## C · 🆕 A row that did not exist, because it was hidden inside `RNA-1`

| Row | Question | Status |
|---|---|---|
| **`RNA-1b`** ⭐ | **Is exon 7 present in the mature `Q230P` transcript?** | 🔴 **`TRUE EXPERIMENTAL GAP` — never interrogated by any published assay** |

`c.689A>C` sits in **exon 7** (`c.606`–`B`, `754 ≤ B ≤ 843`). Johannsen's core amplicon ends at the end
of exon 6 (`c.605`); the 3′ amplicon begins at the start of exon 8 (`≥ c.755`). **The two amplicons
bracket the exon carrying the variant and cover none of it, for every admissible `B`.** An exon-7 event
would therefore leave **both** gel bands at their expected size, so the paper's *"normal … length"*
control is blind to it by construction.

🔴 **This licenses nothing in either direction.** It is not evidence that exon 7 is skipped, and it is not
evidence that the exon-7 junction is normal. It converts an *assumed-answered* question into an
*openly unanswered* one, which is the only honest move available.

**Consequence for `RNA-4`** (exon-7 `ESE` disruption): unchanged at `EXPERIMENT PROPOSED BUT UNRUN`, but
now with the added finding that **the single published RNA experiment on this allele could not have
detected the outcome `RNA-4` asks about.**

## D · Two inferences this repository made, now REFUTED by the source

Both came from indexer-assigned MeSH terms in `PREREG_johannsen2018_methods_20260922.md` §5.3:

- **`HEK293 Cells`** was read as implying *"a heterologous expression arm … a second, independent
  measurement of `Q230P` protein in a non-patient context."* 🔴 **REFUTED.** Fig. 3c legend: *"Model cell
  lines for pancreatic (PaTu-8988t) and colon (SW620) cancer **as well as HEK293 were employed as
  positive controls for WWOX protein expression**."* There is **no transfection and no `Q230P` expressed
  in any heterologous cell.** `SOL-1`'s extraction target *"whether the MeSH-indexed HEK293 arm exists"*
  is answered: **it does not.**
- **`RNA Stability`** was read as implying transcript stability *"was assessed as such"*. 🔴 **REFUTED**
  (see `RNA-2`).

🎯 **The transferable lesson, and it is sharper than the caveat that failed to prevent it.** §5.3 correctly
bounded MeSH as *"indexer-assigned … a pointer, not a datum"* — and then reasoned from the pointer for two
paragraphs anyway. **A caveat attached to an inference does not weaken the inference; only refusing to draw
it does.** Both MeSH-derived leads were wrong in the same direction: each invented an **experiment** out of
an **index term**.

---

# 🎯 AMENDMENT 2 — 2026-09-23, executability audit and the exon-7 assay

> Working files:
> [`q230p_spt_executability_and_exon7_20260923.md`](q230p_spt_executability_and_exon7_20260923.md) ·
> [`repudi2021_file013_wwox_by_genotype_20260923.md`](repudi2021_file013_wwox_by_genotype_20260923.md) ·
> [`q230p_person_count_reconciliation_20260923.md`](q230p_person_count_reconciliation_20260923.md).
> 🔴 **Nothing canonical propagated.** No claim touched, no gated candidate touched.

## E · `DET-1` moves again — the reagent has a name, a host, and a documented false negative

`sc-20528` (Johannsen's antibody, census `A21`) **is the same catalogue item** as the unnamed *lde*-rat
antibody the census carried as `A17`. Verbatim, Suzuki 2009 Methods: *"goat anti-Wwox polyclonal
antibody (1:100; **sc-20528**, Santa Cruz Biotechnology)"*.

| | |
|---|---|
| **Host** | 🟢 `goat`, polyclonal — now **`DATO`**, previously entailed from a secondary |
| **Epitope** | 🟡 A **negation only**: *"did not contain the region altered by the `lde` mutation"* — excludes ≈ the last 44 residues and **says nothing about residue 230**. Provenance: **a 2009 personal communication from the vendor.** Not a datasheet, not an experiment |
| **Current catalogue status** | 🔴 **`UNKNOWN — VENDOR DATASHEET BLOCKED`.** Live in 2009, citable in 2018; 2026 listing could not be determined and **was not guessed** |

> ### 🔴 `H6` (detection artefact) is no longer merely "not excluded" — there is a published precedent, with this exact reagent
>
> In the `lde` rat, **`sc-20528` reported both products *"undetectable"***. A later study of the same
> model, using `HPA050992` (aa 32–110), detected ***"a very weak band of slightly lower mobility."***
>
> 🔴 **STATE IT PRECISELY — this is an `ASSAY-CONDITIONED DETECTION DISCREPANCY`, not a verdict on the
> antibody.** ⚠️ **Corrected 2026-09-23:** an earlier draft of this block called `sc-20528` *"the
> antibody with an in-print false negative"*. That phrasing indicts the reagent; the evidence does
> not support it. What is demonstrated is that **with that particular combination of sample, method
> and antibody, Wwox was not detected, while a different antibody in a later study detected a faint
> band.** ⇒ **strong evidence that *"not detected"* is a property of the whole detection
> architecture**, and **no evidence that `sc-20528` is intrinsically a poor antibody in any other
> context.** In Johannsen's own hands it is a fully specified instrument — `sc-20528` **1:200**,
> 20–40 µg, 12 % gel, ECL / `LAS 4000` — with **three CRISPR-KO clones as a true negative**, which
> remains the best-controlled human specificity in the census.
>
> ⚠️ **Bounded honestly.** The later authors attribute the difference to *"greater sensitivity of the new
> antibody"* — **an author attribution that nobody has tested**, and three variables differ between the
> two runs (antibody, sonication, ECL vs infrared detection). Both lysis buffers are *real* RIPA with a
> stated recipe, so lysis class is **not** the difference. `IPOTESI`, not `DATO` — **and the experiment
> in §F tests it for free by running both antibodies on one membrane.**

## F · The S/P/T experiment: 🟡 **`MINOR ADAPTATION`** — not `EXECUTABLE NOW`, and not `NEW REAGENT`

**Nothing has to be invented.** What fails is the *two-flanking-antibody* design, and the reason is
precise: of the reagents with an **orderable catalogue number** (`ab238144`, `ab189410`, `ABN413`,
`4045S`, `ab216660`), **every single epitope is `UNSTATED`, and every datasheet route returns 403**.
Of the reagents with a **stated epitope**, `A5`/`A6` carry **no catalogue number at all** — *an antibody
you cannot order is not a reagent* — and `A1`/`HPA050992` is attested in a 2019 Methods section with
its 2026 listing `UNKNOWN`.

🎯 **So the design drops to the smallest configuration that actually exists: ONE antibody with a stated
N-terminal epitope (`HPA050992`, aa 32–110, ending 120 residues before Q230) run beside `sc-20528` on
the same membrane.** That is not a flanking pair and must not be described as one — but it is an
orthogonal second epitope, and it **converts the untested sensitivity attribution above into a measured
comparison at zero extra cost.**

🎯 **Host compatibility, by luck rather than design:** `HPA050992` is **rabbit**, `sc-20528` is
**goat** ⇒ **one membrane, two infrared channels, no stripping**, a pairing Suzuki 2009 already
published. **Measured availability:** orderable anti-WWOX primaries **7** · with any epitope statement
**2** · with an epitope placed relative to residue 230 **1** · wholly C-terminal to 230 **0**.
🔴 **A flanking pair is not available at any price today.** Vendor status was checked first-hand and
is `UNKNOWN — VENDOR DATASHEET BLOCKED`: `scbt.com`, `ptglab.com`, `sigmaaldrich.com`, `eutils.ncbi`,
`rest.ensembl`, `ebi` and `ucsc` all returned 403 / connect-rejected. **Not guessed.**

### F.0 · 🔴 THE NORMALISATION RULE — load by input-equivalents, never by equal total protein per fraction

> **`S`, `P` and `T` must be compared on a common INPUT basis — equal cell-equivalents (or
> equal-volume aliquots of a common starting lysate) — NOT by loading an equal mass of total protein
> from each fraction.**

🔴 **Why this is not a detail.** The hypothesis under test (`H5`) is that `Q230P` has **moved** from
`S` into `P`. The soluble and insoluble fractions have **very different total-protein content**, so
normalising each lane to the same µg re-scales every fraction to an equal denominator — **and a
redistribution between fractions is exactly what an equal-denominator comparison cannot see.** It
would divide out the signal the experiment exists to detect, and could even invert its direction.

🟢 A total-protein stain is still run — **as a transfer/loading-fidelity control**, never as the
normaliser. **Report signal per cell-equivalent.** Same rule for the LOD: express the floor in
**cell-equivalents** unless a quantified recombinant standard is sourced (existence `UNKNOWN`).

### F.1 · 🔴 Two protocol defects the audit found, each of which would have cost the experiment

| | Defect | Correction |
|---|---|---|
| **(i)** | `q230p_minimum_discriminator_20260922.md` specifies **95 °C** for the resolubilisation buffer | 🔴 **8 M urea must be heated at ≤ 50 °C.** Above that it **carbamylates lysines**, shifting and smearing exactly the band the experiment exists to detect. A correct-looking protocol that destroys its own readout |
| **(ii)** | The `WWOX`-null lane was specified as Johannsen's CRISPR-KO clones | 🔴 Those are **his freezer, not a catalogue.** A siRNA/shRNA knockdown substitutes — and **a knockdown is *reduced*, not null**, so it bounds specificity without supplying a true zero |

⚠️ **And one commensurability limit, declared rather than hidden:** Johannsen's RIPA **composition is
unrecoverable** (prediction `P2`), so `S` reproduces his fraction **by class, never by identity.**

🔴 **The binding constraint is not a reagent.** It is **`Q230P` fibroblasts**, `HUMAN_REQUIRED`, and it
was already `HUMAN_REQUIRED` before today. Also `UNKNOWN`: whether a **quantified recombinant human
WWOX standard** exists for an LOD in ng — without one, the floor is expressed in **cell-equivalents**,
not ng.

🔴 **Branch discipline, preregistered before any further search:** six outcome branches, each with an
explicit *does-NOT-support* column. **None converts to function.** Notably, branch (a) — pellet-positive
while soluble-negative — **raises rather than lowers the proteostasis safety bar**, and **no branch
transfers to neurons.**

## G · `RNA-1b` (exon 7): 🟡 **`MINOR NEW ASSAY`**, and the primers already exist in print

🎯 **Neither of Johannsen's two published primer pairs can see exon 7 — but the FORWARD of pair 1
cross-paired with the REVERSE of pair 2 spans it entirely.**

```
pair 1 (exons 4–6, 277 bp)   forward ──►                    reverse ◄──
pair 2 (exons 8–9, 200 bp)                     forward ──►             reverse ◄──
CROSS-PAIR:                  forward ──►  ................................. reverse ◄──
                                          spans exon 7 (c.606–B) entirely
```

### G.0 · 🎯 EXON-7 GEOMETRY IS EXACT, AND THE REPOSITORY ALREADY HELD IT

⚠️ **Corrected 2026-09-23.** The bracket *"exon 7 = 149–238 nt"* used above and in the working file was
re-derived from one paper's IGV statement — **while a precise, ClinVar-observed value was already in
this repository**, in [`CC-20260922-EXON7-NATURAL-EXPERIMENT-01`](../research/commit_candidates/CC-20260922-EXON7-NATURAL-EXPERIMENT-01.md) §2:

> **Exon 7 = `c.606–791`. Length 186 nt. `186 mod 3 = 0` ⇒ IN-FRAME.**
> Independently corroborated there by codon arithmetic reproducing a **352-aa** product from 414.

🔴 **Same failure mode as `A17`≡`A21` earlier today: the answer was on disk and a weaker bracket was
re-derived instead.** Twice in one session, so it is a pattern, not an accident — **and both times it
was caught by an outside reader, not by me.**

**Three consequences, and the third changes the biology of the question:**

| | |
|---|---|
| **1 · The shift is exact** | Δexon-7 shortens the cross-amplicon by **exactly 186 bp**, whatever the primers' positions within their exons. **The discriminating quantity is now a number, not a range** |
| **2 · The absolute size is still bounded, not fixed** | With exon 7 = `c.606–791`, exon 8 = `c.792–1056`, exon 9 from `c.1057`: pair 2's forward must sit at `c.858–1056` to give its stated 200 bp across the junction, and pair 1's amplicon ends somewhere in exon 6 (`c.517–605`) ⇒ **cross-amplicon 729–1015 bp**. 🔴 **One BLAT of the two published primers against `NM_016373.2` collapses this to a single number** — `HUMAN_REQUIRED`, sixty seconds. **The assay is interpretable without it** (the WT lane is the size reference); the exact value is needed only to call a band without a control |
| **3 · 🎯 An exon-7 skip is IN-FRAME, and it DELETES `Q230` itself** | It fuses `c.605` to `c.792`, removing residues **203–263** — so **no PTC, no NMD substrate, and a stable 352-aa product is expected rather than decay.** 🔴 **This is the opposite of the exon-6 case** (89 nt, frameshifting). It means `H1b` is **not** a "silent RNA loss" hypothesis: if exon 7 were skipped, the Q230P variant residue would be **absent from the protein entirely**, and the Western's `~46 kDa` window would be the wrong place to look |

- Cross-amplicon **729–1015 bp**; exon-7 skipping shortens it by **exactly 186 bp** — trivially
  resolved on a 1.5 % gel, and **the identical readout class Weisz-Hubshman used to demonstrate
  exon-6 skipping** (593 → 504 bp).
- 🟢 **Zero novel oligonucleotide design.** Both sequences are published verbatim.
- 🟢 **Preferred over Weisz-Hubshman's own pair**, whose reverse primer is provably 3′ of exon 6 but
  whose exact exon is `UNKNOWN` — if it lies *in* exon 7, skipping gives a **dropout**, and a dropout is
  indistinguishable from PCR failure. The cross-pair's reverse is in exon 9 by construction, so the
  readout is always a **shift**, never an absence.
- 🔴 **Declared:** different PrimerBank pairs, annealing temperatures never reported together (one
  gradient PCR settles it); ~800–1000 bp is endpoint RT-PCR, not qPCR — fine, because the readout is
  **size**, not ΔΔCt; and **a size ratio must never be read as an isoform ratio**, since a long amplicon
  under-represents the longer species.
- 🟢 **One BLAT of `AGGATGCACTGCGTTCGAC` against `NM_016373.2` closes both the exon-8-vs-exon-7
  question and the exact expected amplicon size, in sixty seconds** — and `NM_016373` is unreachable from this deployment, so no sequence was
  reconstructed and no coordinate invented.
- 🔴 **Why `MINOR NEW ASSAY` and not `EXISTING MATERIAL`:** **no `Q230P` RNA exists anywhere in this
  repository's reach**, and whether Johannsen's 2018 cDNA or fibroblast stock survives is **`UNKNOWN`** —
  the paper states only that *protein* was stored at −80 °C. **One email settles it.**

🔵 **A structural note, not a complaint.** Weisz-Hubshman's qPCR reverse primer and Johannsen's exon 8–9
reverse primer are **the same site, offset by one nucleotide**. Two independent laboratories converged
on the same 3′ anchor. **The exon-7 blind spot is therefore structural to the field's default assay, not
an oversight by one group.**

## H · An outside datum that bears on `SOL-6`, from `PMID 33914858` File013

Per-genotype disaggregation of the pooled `Wwox log2FC −3.14` gives residual transcript of
**6.8 % / 10.1 % / 18.7 %** (Nestin-Cre KO / constitutive null / Synapsin-Cre KO), i.e. **no genotype
reaches zero**. 🔴 **This must NOT be read as residual WWOX function.** The conditional allele is floxed
on **exon 1 only** of a ~913 kb locus, so gene-level counts retain reads from exons 2–9; the
constitutive null is a **different allele on a different background** whose deleted interval this paper
never states, leaving its 10.1 % **unexplained**. Recorded so that a future reader does not import a
quantification artefact into allele-severity or hypomorph reasoning.

---

# 🔒 CLOSURE — 2026-09-23. `Q230P` is parked behind two ordered experiments.

> **This is a stopping point, not a pause for breath.** Nothing below reopens science. The frontier
> is left in a state where the *next* action is an experiment, not another reading.

## The model as it now stands — no theory added, the space of wrong questions reduced

| Layer | State |
|---|---|
| **RNA** — abundance, exons 4–6 and 8–9 | 🟢 Substantially normal in the one fibroblast line studied |
| **RNA** — architecture, exon 7 | 🔴 **UNKNOWN.** Never interrogated by any published assay |
| **Protein** — RIPA-soluble supernatant | 🟢 **Not detected**, replicated at two harvests |
| **Protein** — pellet / insoluble | 🔴 **Not interrogated** |
| **Protein** — total strongly-denatured pool | 🔴 **Not interrogated** |
| **Protein** — quantitative LOD | 🔴 **Absent** |
| **Detection architecture** | 🟡 **Now known to warrant caution** — an assay-conditioned discrepancy is documented for this reagent class |
| **Mechanism** — impaired synthesis · cotranslational disposal · rapid degradation · insoluble sequestration · detection artefact / mixed state | 🔴 **All five open** |

🎯 **What this session added is not a theory. It is the removal of the questions that could not have
been answered.**

## The two experiments, in order

### `E1` — exon-7 RT-PCR · **run this first**
**Decides whether we have been assuming the RNA's structure.** Cheapest by a wide margin: two
already-published primers cross-paired, no new oligonucleotide design, a **186 bp** expected shift,
Sanger-sequenceable for the junction at nucleotide level.
🔴 **Its outcome reframes `E2`.** An exon-7 skip is **in-frame and deletes `Q230`**, so a positive
`E1` would mean the protein question was being asked at the wrong molecular weight — and `E2` would
need redesigning before it was run, not after.

### `E2` — S/P/T + quantified LOD + orthogonal detection · **run second**
**Decides whether a recoverable protein population exists to chase at all.** `MINOR ADAPTATION`:
load by **input-equivalents, never equal total protein per fraction** (§F.0); urea **≤ 50 °C**;
knockdown, not Johannsen's KO clones, for the null lane; `HPA050992` (rabbit) beside `sc-20528`
(goat) on one membrane in two IR channels. Binding constraint is **`Q230P` fibroblasts**,
`HUMAN_REQUIRED`.

## 🔴 The ordering rule, stated so it is not quietly broken

> **Chaperone / proteostasis work does not resume until `E1` and `E2` have reported.**

**Why:** every proteostasis strategy presupposes a molecular entity to rescue. Right now that entity
is unidentified in **two independent ways at once** — the transcript may not contain the exon that
carries the variant, and no protein population has been shown to exist anywhere in the cell.
🔴 **Searching for a drug before knowing what it should rescue is the failure this ordering exists
to prevent.** `TX-003` and `HYP-20260709-02` stay conditional, and the therapeutic sign remains
branch-dependent exactly as `q230p_structural_mechanism_20260922.md` §9 states.

🔴 **Nothing here is medical advice.** No dose, route, schedule or clinical framing, for any genotype.
