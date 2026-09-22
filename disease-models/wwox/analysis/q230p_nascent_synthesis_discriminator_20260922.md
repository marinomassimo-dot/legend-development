# `Q230P` — is the deficit made **before**, **during**, or **after** the measurable mature-protein pool?

**Actor:** Scientist A · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Class:** `DISCOVERY` — **NON-CANONICAL.** No `*_current.md`, registry, ledger, receipt chain, queue or
state manifest was written or read-modified. No `BATCH_COMMIT`. **No git command was run, not even
read-only.** One file was created: this one.

**Nothing here is medical advice.** No dose, no route, no schedule, no clinical framing. Every compound
named is a bench reagent in cell culture, cited at the concentration its own source states. **BLOCK-1 holds.**

**No external contact and no purchase was made or attempted.** Items needing either are parked in §9 as
`HUMAN_REQUIRED` and were not pursued.

**Public edition** — this reasons about a **WWOX-DEE genotype class**, never an individual.

**Alleles, strains and species are held apart throughout.** `Q230P` (human, patient fibroblasts,
homozygous) ≠ `P47T` knock-in ≠ `P252A` ≠ `P282A` ≠ rat `lde/lde` ≠ the several independent mouse nulls ≠
the `gt/gt` hypomorph. No measurement on one is carried to another, and no two appear in the same row.

**Read depth declared up front.** Two bodies were read in full by me in this act (§4). Everything else
external is `abstract-depth` and labelled. Other actors' repository files are cited as **their
attestations**, never as my readings. **No `FULLTEXT_READ_RECEIPT` is claimed and none is owed** — I did
not route through the full-text receipt protocol.

**Tagging convention.** `FIRST-HAND` = I retrieved or computed it in this act. `INHERITED` = taken from
another repository file, which is named.

---

# §0 · `preregister_prediction` — written and timestamped **before** any search or read

These were committed to the session scratchpad at **2026-09-22T16:02:51Z**, after listing directories only
and before any grep of content, any PubMed call, and any read of a sibling analysis. They are reproduced
here **above** the results, unedited. Scored in §10.

| # | Prediction | Explicit falsifier |
|---|---|---|
| **P1** | **No** repository file contains a nascent-protein / pulse-labelling / AHA / HPG / click / puromycin / SUnSET / OP-Puro / ribosome-profiling arm applied to **any** WWOX allele | any `.md`/`.json`/`.jsonl` under `disease-models/wwox/` or `framework/` containing such a method bound to a WWOX measurement |
| **P2** | **No** repository file reports a WWOX polysome-profiling or RNA-in-polysome measurement for any allele | any hit for `polysome\|polisom\|ribosome profiling\|Ribo-seq` bound to WWOX |
| **P3** | A targeted PubMed search for WWOX + nascent/pulse-label/AHA/HPG/SUnSET/puromycin returns 0–2 records, none measuring WWOX synthesis rate allele-specifically | ≥1 record with an allele-resolved WWOX synthesis-rate measurement |
| **P4** | The 5-cell matrix will contain ≥1 **degenerate** row where `H2` and `H3` give identical readouts under bulk metabolic labelling, because bulk labelling + immunocapture cannot distinguish *never made* from *made and destroyed inside the labelling window* | a pulse duration / inhibitor combination that separates them **with no extra perturbation** |
| **P5** | The highest `width × discrimination` measurement will **not** be the CHX chase; it will be a short-pulse labelling + immunocapture readout paired with a degradation block as the **only** perturbed variable | a single-assay alternative covering ≥3 of the 5 matrix cells at equal sensitivity |
| **P6** | Johannsen 2018 Methods remain unreachable; no third route succeeds this act | any retrieval of the Methods text |
| **P7** | The **detection floor** is the binding constraint: no repository row reports a WWOX LOD, so *"no detectable protein"* cannot be converted into a synthesis rate; any matrix must therefore carry an explicit floor-calibration element | a repository row reporting a WWOX detection floor / LOD / calibrated standard curve |

---

# §1 · `enumerate_baseline_before_scoring` — scopes stated, files listed, then grepped

The repository has recorded this primitive **failing twice and succeeding zero times**
(`q230p_three_designs_one_experiment_20260922.md` §5, `INHERITED`). It is run deliberately here, with the
scopes declared so the sweep can be audited or repeated.

### 1.1 Declared scopes

| Axis | Scope actually used |
|---|---|
| **FILE-TYPE** | **Unscoped.** No `--include`. The tree under `disease-models/wwox/` holds **430 `.md`, 102 `.json`, 11 `.jsonl`, 25 `.py`, 19 `.csv`, 5 `.tsv`, 15 `.png`, 2 `.pdb`** (`FIRST-HAND`, `find … \| uniq -c`). A phrase inside a JSON string field is invisible to `--include=*.md`, so nothing was scoped out. |
| **LANGUAGE** | **Bilingual EN/IT.** Both spellings swept for every concept: `translation\|traduzione`, `degradation\|degradazione`, `insoluble\|insolubil`, `polysome\|polisom`, `co-translational\|cotranslazional\|co-traduzional`, `metabolic label\|marcatura metabolic`, `detection floor\|soglia di rilevazione\|floor di rilevazione`, `ribosome stall\|stallo`. |
| **DOCUMENT CLASS** | dossier (`research/fulltext_dossiers/`) · registry (`registries/`) · analysis (`analysis/`) · ledger (`research/*_ledger_current.md`) · manifest (`research/deepdive_manifests/`) · commit candidate · queue · governance · roles · scripts. |
| **DIRECTORY** | `disease-models/`, `framework/`, `governance/`, `roles/`, `scripts/`. |
| **METHOD** | **Directories listed with `find`/`ls` first, then grepped across what was listed.** No filename was guessed. |
| **EXCLUSIONS, and why** | `paper_registry_current.md` and `literature_tracking_log_current.md` were **excluded from grep by rule**, not by oversight: `framework/scripts/README.md` line 20 forbids grepping the two large registries, because *"a grep hit is a fragment: it drops the caveat two lines below it."* They are read by record with `registry_records.py`. **Consequence, stated honestly: every absence claim in §8 is scoped to exclude those two files.** |
| **WORD BOUNDARIES** | Used throughout (`\bAHA\b`, `\bHPG\b`, `\bOP-?Puro\b`, `\b35S\b`). This mattered: an unbounded `35S` matched **`MDA-MB435S`**, the melanoma line, in three dossiers. |

### 1.2 What the sweep returned — term-by-term counts (`FIRST-HAND`)

Lines / files across `disease-models/ framework/ governance/ roles/ scripts/`, two large registries excluded:

| Term | lines | files | | Term | lines | files |
|---|---|---|---|---|---|---|
| `\bnascent\b` | 31 | 18 | | `puromycin` | 23 | 11 |
| `nascent[- ]chain` | 3 | 3 | | `\bOP-?Puro\b` | 7 | 5 |
| `pulse[- ]chase` | 26 | 12 | | `ribosome profil` | 7 | 5 |
| `pulse[- ]label` | 30 | 12 | | `polysome` | 8 | 6 |
| `metabolic[- ]label` | 11 | 6 | | `polisom` | **0** | **0** |
| `marcatura metabolic` | **0** | **0** | | `\bSILAC\b` | 3 | 3 |
| `\bAHA\b` | 15 | 9 | | `Ribo-?seq` | **0** | **0** |
| `azidohomoalanine` | **0** | **0** | | `BONCAT` / `FUNCAT` | **0** | **0** |
| `homopropargylglycine` | **0** | **0** | | `\[35S\]` | **0** | **0** |
| `\bHPG\b` | 2 | 1 | | `radiolabel` | **0** | **0** |
| `click chem` | 2 | 1 | | `cycloheximide\|CHX\|cicloesimide` | **221** | **65** |
| `SUnSET` | 60 | 20 | | | | |

### 1.3 🔴 `P1` and `P2` are **REFUTED**, and the refutation is the most useful thing in this section

The repository already holds a dense, recent, directly-on-topic body of work. Named, because an actor who
does not know these exist will rewrite them:

| File (all `INHERITED`, all dated 2026-09-21/22) | What it already settles |
|---|---|
| `proteostasis_discrimination_protocols_20260922.md` (Scientist C) | A **ranked five-entry protocol shortlist** for exactly the three-branch question, from outside the WWOX field, with verbatim locators and two full texts read |
| `q230p_direct_discriminator_20260922.md` (Scientist I) + its ORCHESTRATOR VERIFICATION | An 11-row hypothesis × readout matrix over `A`/`S`/`dS/dA`/`E`/`G`/`L` — but in a **dox-inducible NanoLuc-tagged transgene** system, not endogenous protein |
| `q230p_minimum_discriminator_20260922.md` (Scientist B) | Component-by-component necessity analysis; cuts and keeps, with the permissive-temperature arm withdrawn |
| `q230p_three_designs_one_experiment_20260922.md` (Orchestrator) | The convergence record, and the framing correction: this is a **re-run of a published negative**, not a first measurement |
| `missense_proteostasis_matrix_20260921.md` row 1 | The gap sentence itself: *"No nascent-synthesis measurement for any WWOX missense allele — no metabolic pulse labelling, no polysome or ribosome profiling, no SUnSET/AHA-click."* |
| `DL-MECH-029` (discovery ledger, since 2026-07) | The experiment already named: *"Western/qRT-PCR allele-specifici + pulse-labeling della sintesi + frazionamento solubile/insolubile + pulse-chase"* |

So `P1` and `P2` are refuted **as literal absence claims**. But the sweep also shows precisely what the
hits *are*: with one exception they are the repository **naming the method as a gap or proposing it**, not
evaluating it. The single evaluation is Scientist C's entry 4, which reaches a **dead end** (§3.3). That
dead end is what this file re-opens.

⚠️ **A namespace collision found in the same sweep, worth one line.** Of the 20 files matching `SUnSET`
case-insensitively, **11 are governance files where the word is `sunset`** — a decision sunset, a candidate
sunset. `grep -i SUnSET` in this repository is ~55 % false-positive. The technique hits are confined to
five `disease-models/wwox/` files.

### 1.4 What the sweep found to be genuinely **absent** — and these are the delta

Same scopes, same exclusions, bilingual, word-bounded (`FIRST-HAND`):

| Term | lines | files |
|---|---|---|
| `Puro-?PLA` | **0** | **0** |
| `ribopuromycylation` | **0** | **0** |
| `PUNCH-?P` | **0** | **0** |
| `SunRiSE` | **0** | **0** |
| `eIF5A` | **0** | **0** |
| `collided ribosome\|ribosome collision\|RQC\|ribosome quality control` | **0** | **0** |
| `ZNF598\|EDF1\|GIGYF2\|Hel2` | **0** | **0** |
| `LTN1\|listerin\|NEMF` | **0** | **0** |
| `polyproline\|poly-proline\|di-proline\|PPP motif` | 5 lines / 4 files — **all `PPXY`/`PXPPXYY` WW-domain motif hits, none about elongation** | — |

**`proximity ligation`: 3 lines / 2 files**, and inspection shows none is a translation assay.

> **The delta this file can add is therefore specific and small:** the repository has never considered
> **protein-specific nascent-chain imaging** (`Puro-PLA` / `FUNCAT-PLA`), and has never asked whether
> `Q230P` creates a **co-translational** lesion in the ribosome-quality-control sense. Both are answerable
> now, and one of them is answerable from sequence alone, for free.

---

# §2 · Two first-hand measurements made on the sequence and structure, before any hypothesis is ranked

Both are computed by me in this act from `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb`
(AlphaFold monomer v2.0 for UniProt Q9NZC7, header date 01-AUG-25). Both are cheap, and both kill a
plausible-sounding branch before anyone spends money on it.

### 2.1 🟢 Coordinate-system gate, passed explicitly

This session's characteristic defect is coordinate systems — three off-by-N errors in one day
(`INHERITED`, session brief). So the gate is run and reported, not assumed:

- The model contains residues **1–414**, contiguous, **1-based**, `count = 414`. WWOX is a 414-residue protein.
- **Residue 230 is `GLN`.** The wild-type letter at the row of interest is verified, not inferred. ✅
- Residue 1 is `MET`; residue 2 is `ALA`. Local context **218–244** reads
  `W S L T K D G L E T T F Q V N H L G H F Y L V Q L L Q`, i.e. **`…T228 F229 Q230 V231 N232…`**.
- pLDDT across 220–242 is **96.4–98.9**, so the local backbone is the high-confidence part of the model.

### 2.2 🔴 `Q230P` creates a **strictly isolated** proline — the elongation-stall branch of `H2` is excluded **by sequence**

`FIRST-HAND`, computed from the same file:

- Wild-type WWOX contains **17 prolines**. The nearest to 230 are **P217** and **P252** — **13 and 22
  residues away**.
- The **only `PP` dipeptide anywhere in wild-type WWOX is at residues 19–20**, inside WW1, ~210 residues away.
- Therefore `Q230P` yields the tripeptide **`F229–P230–V231`**: a single proline flanked by Phe and Val.

**Consequence.** The canonical ribosome-stalling motifs that require eIF5A rescue are **poly-proline
runs and `XPP` / `PPX` contexts** (`PPP`, `PPG`, `PPD`, `PPE`, `PPW`). `Q230P` creates **none of them**. An
isolated proline slows peptidyl transfer modestly; it does not generate a stall of the class that recruits
ribosome-quality-control factors. So the version of `H2` that reads *"the mutation impairs elongation at
the mutant codon"* has **no sequence mechanism**, and the version of `H3` that reads *"ribosome-associated
RQC ubiquitinates the nascent chain at the stall"* has **no substrate**.

🔴 **Stated at the strength the evidence allows.** This is a **`INFERENZA` from sequence context against
published motif classes I did not re-derive here**; it is not a measurement of elongation on this mRNA. It
**lowers the prior** on stall-mediated `H2`/`H3a`; it does not close them. It also means a ribosome-profiling
or polysome experiment is now predicted to be **negative for a reason we can state in advance** — which is
different from Scientist C's rejection of those assays (§3.4), and a better reason.

### 2.3 What the structure says about **when** the lesion becomes visible to the cell — `INHERITED`, then extended

`q230p_structural_mechanism_20260922.md` (Scientist, `INHERITED`) establishes, from measurements on these
same coordinates: `Gln230` is a **buried, interior, mid-helix** residue of SDR helix αE
(**relSASA 0.000**; whole segment 226–240 max relSASA 0.107); its backbone amide donates the **i,i−4
helical hydrogen bond to O226 at 3.03 Å with 9° angular deviation**, *"a near-ideal α-helical bond that Pro
cannot make at all"*; and its side chain staples αE to strand βC across ~45 residues via five polar
contacts, **31 heavy-atom contacts and all five polar contacts removed by Q→P**.

**My extension, and it is the hinge of §4.** A lesion at residue **230 of 414**, buried in the middle of
a domain, is not visible to the cytosol at the moment it is polymerised: it sits inside the ribosomal exit
tunnel, which holds ~30–40 residues. It becomes exposed to cytosolic chaperones and triage machinery only
when the chain reaches length **≈ 260–270**. There are then still **~145–155 residues** to synthesise.

This splits `H3` in two, and the split is load-bearing because the two halves are measurable and are **not**
the same object:

- **`H3a` — ribosome-associated disposal (RQC-like)**, requiring a stall. §2.2 says there is no stall motif. **Low prior.**
- **`H3b` — post-exposure, pre-pool disposal**: the chain is completed or nearly completed, the misfolded
  αE is triaged by chaperone-directed degradation within seconds-to-minutes of release, and the molecule
  **never joins the steady-state pool a Western blot loads**. **This is the live version of "during".**

---

# §3 · `diverge_hypotheses` — PRODUCTION vs DECAY, and what each technique structurally cannot see

## 3.1 The question, restated as two rates

Steady-state abundance is `A_ss ≈ k_syn / k_deg` (one-compartment). Johannsen 2018 measured **`A_ss` below
a floor** and **RNA normal**. That single equation has a two-dimensional solution space, and **no
steady-state measurement can locate a point in it.** The repository's five-way hypothesis set maps onto it:

| | maps to |
|---|---|
| `H1` reduced RNA availability | template for `k_syn` reduced — **already constrained**, §5 |
| `H2` impaired translation / nascent production | `k_syn` reduced |
| `H3a` co-translational (RQC) disposal | `k_syn` **effective** reduced, at the ribosome |
| `H3b` immediate post-release disposal | very large `k_deg` acting on a pool the assay never sees |
| `H4` normal synthesis then rapid degradation | `k_deg` increased on the **measurable** pool |
| `H5` synthesis + insoluble sequestration | neither rate changes; the **partition** changes, and the assay discards one phase |
| `H6` mixed | ≥2 of the above |

🔴 **The structural reason a cycloheximide chase cannot answer this.** A CHX chase measures the decay of
**the pool that is already detectable at t = 0**. For `Q230P` that pool is, by the published measurement,
**below the floor**. Two consequences, and the second is the one usually missed:

1. *Mechanically*, a chase from an undetectable band yields an undetectable band at every timepoint — the
   `INHERITED` caveat 2 of Scientist C, which is correct.
2. *Conceptually, and this is the deeper one*: **even if an inhibitor first accumulates a measurable pool,
   the chase then measures the decay of the molecules that survived long enough to be accumulated.** It is
   structurally blind to molecules disposed of before entry. A normal-looking half-life measured that way
   is fully compatible with 95 % of molecules never arriving.

> 🔴 **This is the repository's standing `EX-ANTE PREDICTION`, and it stays labelled that way.** A CHX chase
> could show an apparently normal `Q230P` half-life while missing molecules lost *before* entering the
> measurable mature-protein pool. **It has never been tested.** Nothing in this file tests it. What this
> file adds is that the prediction is now **reachable**: §3.3 names a measurement that sees the molecules
> the chase cannot.

## 3.2 `gate_is_not_quantity` — what each candidate technique **structurally cannot see**

Selected on the brief's five criteria — allele-specific interpretability · sensitivity · practicality in
patient fibroblasts · compatibility with a possibly sub-floor abundance · ability to separate synthesis
from degradation. **Not on familiarity.** `FIRST-HAND` where a locator is given; the gate column is my
analysis of the cited method description.

| Technique | Measures | 🔴 `gate_is_not_quantity` — what it **structurally cannot** see | Verdict here |
|---|---|---|---|
| **SUnSET** (surface sensing of translation) | **global** protein synthesis per cell | **The identity of the protein.** Its own definition is *"monitoring and quantification of **global protein synthesis** in individual mammalian cells"* (Schmidt 2009, `abstract-depth`, `INHERITED` from Scientist C). A normal SUnSET signal in `Q230P` cells says **nothing** about WWOX. | ❌ **REJECT alone.** Retained only as a **whole-cell normaliser** (§6) |
| **OP-Puro / OPP-click** | global synthesis, imaging-compatible | same gate as SUnSET — no protein identity | ❌ REJECT alone; usable as normaliser |
| **AHA / HPG + click, bulk** | global newly-synthesised proteome | no protein identity without a capture step | ❌ REJECT alone |
| **AHA-click + WWOX immunoprecipitation** | WWOX synthesis rate, quantitatively | **Anything below the IP's own recovery floor**, and it requires an anti-WWOX antibody validated **for IP**, not merely for Western — a distinct and frequently failing requirement (`INHERITED`, Scientist C). Also **AHA replaces methionine only** | 🟡 **Tier 2.** Quantitative but gated on a reagent nobody has checked |
| **³⁵S-Met/Cys pulse + IP** | same, classically | same IP floor; plus **radioactivity**, licensed facility, Met-free medium | 🟡 Tier 2, worse practicality |
| **Ribosome profiling / polysome profiling** | ribosome **occupancy on the mRNA** | **Everything downstream of the ribosome.** And §2.2 now predicts a null result *a priori* | ❌ REJECT — see §3.4 for the corrected reason |
| **Dynamic SILAC / pSILAC** | proteome-wide synthesis and turnover | mass-spectrometric detection floor; WWOX must be **quantified in the MS run**, which for a low-abundance protein in primary fibroblasts is not assured | 🟡 Tier 3, not costed here |
| **HaloTag / SNAP-tag pulse-chase** | birth-cohort fate, cleanly | **The endogenous allele.** Requires a knock-in tag; a tag on a destabilised protein perturbs the variable under study | ❌ REJECT for this question |
| **CHX chase** | decay of the **pre-existing detectable** pool | **Every molecule that never entered that pool** (§3.1) | 🟡 Keep as the `k_deg` cell only, and **only after** a pool exists |
| 🟢 **Puro-PLA** | **abundance of nascent chains of one named protein**, per cell, in situ | **Length-gated** (§3.3) and **perturbing** (§3.3) | ⭐ **SELECT — production** |
| 🟢 **FUNCAT-PLA pulse–chase** | **fate of a birth-cohort of one named protein** | slower, ~10× dimmer, Met-gated | ⭐ **SELECT — decay of molecules followed from birth** |

## 3.3 ⭐ The two techniques the repository has never named, verified first-hand

**Source, read in full by me in this act:** tom Dieck S, Kochen L, Hanus C, Heumüller M, Bartnik I,
Nassim-Assir B, Merk K, Mosler T, Garg S, Bunse S, Tirrell DA, Schuman EM. *"Direct visualization of newly
synthesized target proteins in situ."* **Nat Methods 2015;12(5):411–4. PMID 25775042, PMCID PMC4414919,**
[DOI 10.1038/nmeth.3319](https://doi.org/10.1038/nmeth.3319). Retrieved via the PubMed MCP tools; full text
read. `FIRST-HAND`.

The method couples metabolic labelling to a proximity ligation assay between **two** antibodies: one against
the label (anti-puromycin, or anti-biotin after AHA-click) and one against **a specific epitope in the
protein of interest**. Signal requires both. **There is no immunoprecipitation step** — which is exactly the
requirement that dead-ended Scientist C's entry 4.

**Four verbatim facts that decide the design:**

1. **The N-versus-C epitope experiment is in the original paper, as the specificity control** —
   *"As protein synthesis proceeds from N- to C-terminal and puromycin truncates the nascent protein chain,
   we reasoned that antibodies directed against the N terminus should generate more Puro-PLA labeling than
   C-terminal antibodies against the same protein. Indeed we found that the N-terminal Puro-PLA signal was
   higher than C-terminal Puro-PLA signal (even when controlling for epitope availability) thus supporting
   the idea that the Bassoon Puro-PLA signal is primarily due to the binding of two antibodies to the same
   nascent polypeptide."* Reagents named: `rb-Bassoon-Nterm (sap7f)` and `rb-Bassoon-Cterm (Synaptic
   Systems 141002)`. **§4 repurposes this validated control as a positional discriminator.**
2. **FUNCAT-PLA measures turnover of a birth-cohort, and it was cross-validated** — AHA pulse (2 h) then
   chase; TrkB and Bassoon half-lives of **0.7 and 2.6 days**, and the authors state the result is
   *"consistent with half-life values determined by biochemical means."* **This is decay measured from the
   moment of synthesis, not from steady state — the measurement a CHX chase cannot make.**
3. 🔴 **Puro-PLA's own `gate_is_not_quantity`, in the authors' words** — *"puromycin incorporation results
   in premature truncation of polypeptide chains and degradation of truncated proteins is enhanced."*
   Puromycylation **destroys the molecule it counts.** So Puro-PLA can report production and **cannot**
   follow fate. Against this, for AHA: *"There is no indication that AHA incorporation changes a protein's
   spatial fate."*
4. **Relative sensitivity, measured in that paper** — at a matched 15-min labelling time and the same POI
   antibody, *"a roughly ten-fold higher signal with Puro-PLA than with FUNCAT-PLA"*; Puro-PLA is linear
   with time from **seconds to minutes**, FUNCAT-PLA linear but needing longer.

**That division of labour is exactly the brief's axis:** Puro-PLA = **production rate**, fast and sensitive
but perturbing; FUNCAT-PLA pulse–chase = **decay of molecules followed from birth**, non-perturbing but
dimmer. Neither is a CHX chase, and together they span both rates.

### 🔴 The critique of Puro-PLA, and `verify_the_omitted_clause` applied to it

Anyone who reaches for Puro-PLA will be pointed at **Hobson BD, Kong L, Hartwick EW, Gonzalez RL, Sims PA.
*"Elongation inhibitors do not prevent the release of puromycylated nascent polypeptide chains from
ribosomes."* eLife 2020;9:e60048. PMID 32844746, PMCID PMC7490010,**
[DOI 10.7554/eLife.60048](https://doi.org/10.7554/eLife.60048). **Read in full by me in this act**
(`FIRST-HAND`). Its title is usually cited as *"Puro-PLA is broken."*

**The sentence beside the headline says the opposite, for this use.** Results, verbatim:

> *"Therefore, we conclude that while the eL22-HA/Puro PLA is specific for the presence of antigen and
> antibody, **it reports primarily on the cytoplasmic abundance of puromycylated NPCs**, regardless of
> whether they are currently bound to ribosomes."*

**Cytoplasmic abundance of puromycylated nascent chains is precisely and only what I want to measure.** The
paper refutes the *spatial* claim — that the signal marks the **site** of translation — and in the same
sentence **affirms the abundance claim**. For *"is WWOX being synthesised?"* the site is irrelevant. The
critique does not apply; it validates.

**A second omitted clause, and it constrains the design rather than the conclusion.** Discussion, verbatim:

> *"…growing concerns that PLA can produce false positive signals **when both antigens are highly abundant
> and have overlapping subcellular distributions**… This issue of 'non-specific proximity' may broadly
> affect puromycin-based PLAs… **However, it should be noted that our assay is an outlier in this regard,
> as both antigens are extremely abundant and broadly distributed throughout the cytoplasm.**"*

Their false-positive mode arose because **both** partners were ribosome-scale abundant. In a WWOX Puro-PLA
one partner is **scarce** — the opposite regime, and the authors explicitly flag their own assay as the
outlier. Their stated mitigation is adopted in §6: *"The use of direct-conjugated primary antibody PLA
probes would be expected to reduce the frequency of false positives."*

**Two further first-hand facts from Hobson 2020 that change the protocol:**

- Half-life of the puromycylated-chain–ribosome complex is **< 40 s** with emetine, extended by only ~2 min
  with cycloheximide; SunTag puncta are undetectable **~5 min** after puromycin. ⇒ **pulse short, wash fast, fix fast.**
- tom Dieck's protocol includes a **355 µM cycloheximide, 30 min pre-treatment** *"which stalls the truncated
  protein at the ribosome and enhances puromycylation."* Hobson 2020 shows that stalling **does not happen**.
  ⇒ **Drop the CHX pre-treatment.** It was only ever for localisation, it does not work, and dropping it
  removes a perturbation — which is the brief's constraint that an added arm must perturb **only** the
  variable in question.

### Precedent outside neurons, at the honest depth

- **Chin A, Lécuyer E.** *"Puromycin Labeling Coupled with Proximity Ligation Assays to Define Sites of
  mRNA Translation in Drosophila Embryos and **Human Cells**."* Methods Mol Biol 2021;2381:267–284. **PMID
  34590282**, [DOI 10.1007/978-1-0716-1740-3_15](https://doi.org/10.1007/978-1-0716-1740-3_15).
  `abstract-depth` — no PMCID returned, body not retrieved. Its abstract states the method *"can be used to
  study the mechanisms driving the translation of select mRNAs and **to access the impact of genetic
  mutations on local protein synthesis**"*, and that it runs *"in chambered slides, or in a high-throughput
  setup with 96-well plate."* MeSH includes **Humans**. A step-by-step protocol exists, in human cells,
  framed for exactly this use.
- **Moissoglu K, Yasuda K, Wang T, Chrisafis G, Mili S.** eLife 2019;8:e44752. **PMID 31290739, PMCID
  PMC6639073**, [DOI 10.7554/eLife.44752](https://doi.org/10.7554/eLife.44752). `abstract-depth` — I did not
  read the body. Keywords include `puro-PLA`; the system is *"human and mouse, migrating, mesenchymal
  cells"*. MeSH: Humans, Cells Cultured.
- tom Dieck 2015's own non-neuronal control system is the **mouse fibroblast L-cell line (ATCC CRL-2648)**,
  with transfected and untransfected cells **mixed in the same dish** as an internal control. 🔴 **A mouse
  fibroblast cell line is not a primary human dermal fibroblast, and I do not carry the result across.**

## 3.4 Where I disagree with an inherited verdict, and where I do not

`proteostasis_discrimination_protocols_20260922.md` entry 5 **rejects** ribosome/polysome profiling on the
ground that *"a codon substitution at position 230 has no mechanism by which it would reduce ribosome
loading."*

- **I agree with the verdict and reject the reason.** *Loading* was never the candidate mechanism; the
  candidate was **elongation**, and a Gln→Pro substitution is a genuinely plausible elongation-stall
  hypothesis a careful reader would raise. The correct reason it fails is the one measured in §2.2: the
  substitution creates a **strictly isolated proline** (`F229-P230-V231`, nearest Pro 13 residues away, the
  only wild-type `PP` at 19–20), so **no eIF5A-dependent stalling motif is created.** Same verdict, a
  falsifiable reason, and it costs nothing.
- **Entry 4's dead end is where I part company.** Scientist C concluded that protein-specific nascent
  measurement *"still requires pulse-label plus immunoprecipitation"* and found no validated instance for a
  low-abundance single protein in primary human fibroblasts. **That conclusion is correct for IP-based
  routes and does not survive the existence of PLA-based routes**, which need no IP. Their §4 does not name
  Puro-PLA or FUNCAT-PLA; the repository-wide count for both is **0** (§1.4).

---

# §4 · ⭐ The discriminator: a **two-epitope Puro-PLA ratio** that straddles residue 230

This is the one genuinely new instrument in this file. It is built from inherited reagent facts and a
validated control, and it is quantitative.

## 4.1 The reagent facts it stands on

| Fact | Source | Tag |
|---|---|---|
| Anti-WWOX **Sigma `HPA050992`, epitope aa 32–110**, already used by this programme | `discovery_ledger_current.md` L623 — *"anti-Wwox Sigma HPA050992 (epitopo aa 32-110…)"* | `INHERITED` |
| That antibody turned a rat `lde/lde` *"absent protein"* into a **detectable faint 46.2-kDa species** | session brief | `INHERITED` |
| A WWOX epitope at **aa 286–299** is characterised in the literature | `CC-20260920-PAPER34140629-PROMOTION-01.md`; PMID 34140629 | `INHERITED` |
| The full-text queue **already asks** for *"the antibody and its epitope position relative to Gln230"* | `full_text_queue_current.md` L6972 | `INHERITED` |
| The N-term-vs-C-term Puro-PLA comparison is a **validated specificity control** | tom Dieck 2015, verbatim §3.3 | `FIRST-HAND` |

> The repository already flagged epitope position relative to Gln230 as an open question, and already owns
> an antibody whose epitope is **N-terminal** to it. What is new is turning that pair into a measurement.

## 4.2 The mechanism, and the arithmetic

Puromycin terminates chains at whatever length the ribosome has reached. A Puro-PLA signal therefore
requires the POI epitope to be **already synthesised** in that truncated chain. The epitope position is a
**length gate**, not an abundance gate — and with two epitopes straddling residue 230 the gate becomes a
**position report on where chains are being lost**.

All figures `FIRST-HAND`, computed from the 414-residue sequence:

| Quantity | Value |
|---|---|
| ORF length `L` | **414 aa** |
| N-arm epitope (aa 32–110) complete at chain length | `ℓ ≥ 110` → detectable window **304 positions = 73.4 %** of the ORF |
| C-arm epitope (aa 286–299) complete at chain length | `ℓ ≥ 299` → detectable window **115 positions = 27.8 %** of the ORF |
| Lesion at residue 230 clears the exit tunnel (~30–40 aa) at | `ℓ ≈ 260–270` (**265** used) |
| **Null-hypothesis ratio** `R₀ = N:C` under uniform ribosome density | **304 / 115 = 2.643** |

Every chain the **C-arm** sees (`ℓ ≥ 299`) has **already passed the lesion and already exposed it**.
Of the chains the **N-arm** sees, **155 of 304 positions (51 %) are pre-exposure**.

Let `d` = fraction of chains disposed of once the lesion is exposed. Then
`N ∝ 155 + 149(1−d)` and `C ∝ 115(1−d)`, so with `R = N/C` and **`ρ = R / R₀`** — in which every
antibody-efficiency constant cancels, because `ρ` is a ratio of ratios compared patient-to-control:

| `d` (co-translational / pre-pool disposal) | `R` | **`ρ`** |
|---|---|---|
| 0.00 | 2.64 | **1.00** |
| 0.10 | 2.79 | 1.06 |
| 0.25 | 3.09 | 1.17 |
| 0.50 | 3.99 | **1.51** |
| 0.75 | 6.69 | 2.53 |
| 0.90 | 14.77 | **5.59** |
| 0.95 | 28.25 | 10.69 |
| 0.99 | 136.1 | 51.5 |

Inverted: **`d = 1 − 155 / (115·R − 149)`** — the experiment returns a **number**, not a direction.

🟢 **Robustness of the one soft assumption.** Varying the exit-tunnel length across its full plausible range
(30 → 40 aa) moves `ρ` by **< 6 %** (at `d = 0.5`, ρ = 1.49 → 1.53; at `d = 0.9`, ρ = 5.44 → 5.74). The
discriminator does not depend on getting the tunnel length right.

🔴 **Declared assumptions, each falsifiable.** (i) **Uniform ribosome density** along the ORF — false in
detail for every mRNA; it biases `R₀`, which is why `ρ` is measured **against the control genotype's own
`R`**, not against 2.643. (ii) Puromycylation efficiency is position-independent — controlled the same way.
(iii) Both epitopes survive fixation and permeabilisation in both genotypes — an explicit
antibody-leave-out and total-protein-PLA control, as tom Dieck's Methods require.

## 4.3 What `ρ` reads, per hypothesis

| Hypothesis | N-arm (abs.) | C-arm (abs.) | **`ρ`** | Why |
|---|---|---|---|---|
| `H1` reduced RNA | ↓ | ↓ | **≈ 1** | fewer templates, no positional bias |
| `H2` uniformly impaired production | ↓ | ↓ | **≈ 1** | initiation/elongation scales both arms equally |
| `H3a` RQC at a stall | ↓ | ↓↓ | **> 1** | but §2.2 gives it no stall motif ⇒ low prior |
| `H3b` post-exposure, pre-pool disposal | ~↓ | ↓↓ | **> 1, rising with `d`** | only chains past ~265 are removed |
| `H4` degradation of the mature pool | **≈ WT** | **≈ WT** | **≈ 1** | nascent production is untouched |
| `H5` insoluble sequestration | ≈ WT | ≈ WT | ≈ 1 | partition changes, synthesis does not |
| `H6` mixed | mixed | mixed | 1 < ρ < observed | read with the other four cells |

**`ρ` is the single quantity that separates "during" from "before" and "after".** It is blind to `H1`/`H2`
versus `H4`/`H5` — which is what the other four matrix cells are for.

---

# §5 · Ranking `H1`–`H6` against the evidence that already exists

Not equally plausible. Ranked, with how far the constraint goes.

| | Hypothesis | Status | How far the existing evidence constrains it |
|---|---|---|---|
| **`H1`** | reduced RNA availability | 🟢 **LARGELY EXCLUDED** | Johannsen 2018 measured **normal WWOX transcript by qRT-PCR** in the same fibroblasts (`INHERITED`, `DL-MECH-029` / `CLAIM 019`). `DL-MECH-029` adds that NMD is excluded on structural grounds — *"non c'è NMD (è un missense, non un PTC)"*. 🔴 **Residual, and it is why RNA stays in the matrix as a control:** qRT-PCR measures **steady-state total transcript**, not ribosome-associated or translationally competent transcript, and I could not establish the amplicon position or the reference gene (§8). |
| **`H4`** | normal synthesis then rapid degradation of the mature pool | 🟡 **THE AUTHORS' HYPOTHESIS, UNTESTED** | *"impaired translation or premature degradation"* is Johannsen's own disjunction. 🔴 **Not evidence** — it is the authors' interpretation of a negative blot. No inhibitor arm, no chase, no half-life was reported for this allele. |
| **`H5`** | synthesis + insoluble sequestration | 🟡 **NOT EXCLUDED, AND SYSTEMATICALLY UNDER-TESTED** | `INHERITED` census: **zero** WWOX abundance studies explicitly examined an insoluble pellet; patient-derived abundance rows are largely buffer/epitope-limited. 🔴 **The authors' disjunction omits insolubility altogether** — and a mild non-denaturing lysis discards the pellet *before* the gel, so *"absent"* would mean *absent from the soluble fraction*. Johannsen's buffer is **`PREMISE: METHODS_INVISIBLE`**. Counterweight, `INHERITED` from Scientist C: Koch 2011 (PMID 22113611, `abstract-depth`) reports an insoluble species forming in patient **neurons** and *"not observed in iPSCs, fibroblasts or glia"* — so a **negative** solubility result in fibroblasts cannot close this branch for the disease-relevant cell type. |
| **`H3b`** | post-exposure, pre-pool disposal | 🟠 **STRUCTURALLY FAVOURED, NEVER MEASURED** | The lesion is a **buried, mid-helix, backbone-hydrogen-bond-abolishing** substitution (`INHERITED`, §2.3) exposed to the cytosol at chain length ~265 with ~150 residues still to go (`FIRST-HAND`, §2.3). That is the textbook substrate geometry for chaperone-directed triage before pool entry. **No measurement of any kind exists.** This is the hypothesis the repository has least instrumented and the one §4 targets. |
| **`H2`** | impaired translation / nascent production | 🟠 **PARTLY NARROWED, `FIRST-HAND`** | The **elongation-stall** version is excluded by sequence (§2.2: isolated proline, no polyproline motif). The **initiation / global-rate** version has no mechanism either — a missense at codon 230 does not plausibly alter initiation — but it is not measured. So `H2` survives only in a weak form, and `ρ ≈ 1` with both arms low is what would revive it. |
| **`H3a`** | RQC at a ribosomal stall | 🔴 **DOWN-WEIGHTED, `FIRST-HAND`** | No stall motif is created (§2.2); no PTC, so no RQC substrate of the canonical class. Retained only as the `ρ > 1` alternative that the matrix cannot distinguish from `H3b` without a collided-ribosome readout. |
| **`H6`** | mixed | 🟡 **LIVE, and arguably expected** | The inherited structural verdict predicts a folding-primary lesion with degradation **and** aggregation downstream (`INHERITED`, `q230p_direct_discriminator` row R9). A folding lesion of this class is not obliged to pick one disposal route. |

🔴 **What must not be concluded from any of the above.** The correct current state is
**`MOLECULAR FATE UNRESOLVED`**. *"No detectable protein"* is an **assay result**, not a molecular-state
description. Nothing here converts it into a claim that `Q230P` protein exists, nor into a claim that it
does not.

🔴 **ΔΔG carries no weight in either direction and is not used above.** `INHERITED`: across all six WWOX
missense variants with a value, ΔΔG is **anti-correlated** with measurement — `P47T` at **+2.806** has
**NORMAL** protein; `P252A` at **+1.298** is the only one with demonstrated accelerated degradation.
`Q230P` at **+1.514** sits between them. It is not evidence here.

🟢 **One simplification nobody has foregrounded, and it removes a whole class of confound.** `DL-MECH-029`
records that the Johannsen sisters are **homozygous** at Gln230 (*"due sorelle … omozigoti"*, `INHERITED`).
In `Q230P/Q230P` fibroblasts **every WWOX transcript is the mutant**, so **no allele-specific assay is
required** — `DL-MECH-029`'s own experiment line asks for *"Western/qRT-PCR allele-specifici"*, which is
necessary for the **reference genotype** (formally `null/missense`) but **not** for these cells. ⚠️ The
converse is the limit: a result in homozygous cells transfers to the `null/missense` reference genotype
only under the assumption that the missense allele behaves the same beside a null, which is untested.

---

# §6 · EXPERIMENT COMPRESSION — one matrix, five cells, minimum measurements

**Not five experiments.** Cells `①`–`③` share **one plate and one fixation**; `④`–`⑤` share **one lysate**
from the sister plate. Two plates, one cell expansion.

## 6.1 The measurement set

| # | Cell | Measurement | Perturbation |
|---|---|---|---|
| **①** | **RNA** | WWOX qRT-PCR, **amplicon position and reference gene declared**, ≥2 healthy controls | none |
| **②** | **NASCENT PROTEIN** | **Puro-PLA, two arms**: N-epitope (aa 32–110) and C-epitope (aa 286–299). Puromycin 1–3 µM, **2–5 min**, two fast pre-warmed washes, immediate fix. **No CHX pre-treatment** (§3.3). Read `S_N`, `S_C`, **`ρ`** | puromycin only |
| **③** | **PRE-POOL DISPOSAL** | ② repeated **+ bafilomycin A1** and **+ MG-132**, each as the **only** changed variable, one arm at a time | one inhibitor |
| **④** | **SOLUBLE / INSOLUBLE** | one plate → **non-denaturing lysis → spin → blot supernatant AND SDS/urea-resolubilised pellet separately**, high load (~50 µg/lane, `INHERITED` from Schultz 2018 via Scientist C) | none |
| **⑤** | **DECAY** | **FUNCAT-PLA pulse–chase**: AHA pulse, chase 0/6/24/48 h. *Only if* ③ accumulates a measurable pool: a CHX chase **from that pool**, reported as what it is | AHA, then CHX |

**Mandatory calibration element, from `P7`.** ② and ④ each carry a **dilution series of control-fibroblast
lysate / a cell-number titration** to place a **numeric detection floor** on the axis. `INHERITED` census:
**zero** WWOX abundance studies reported a detection floor. Without it, every "absent" in this matrix
repeats the defect it exists to fix.

**Controls that are not optional** (tom Dieck 2015 Methods, `FIRST-HAND`): antibody leave-out (each
primary, separately); no-puromycin; **anisomycin 40 µM, 30 min** pre-treatment as the translation-block
negative; single-primary "total protein" PLA to normalise epitope availability between genotypes;
direct-conjugated PLA probes where available (Hobson 2020's stated mitigation).
**Plus one design element adopted from tom Dieck's L-cell control:** patient and control fibroblasts
**mixed in the same dish**, distinguished by a cell-tracker dye, so staining, ligation and amplification
variance cancel within-field. A whole-cell **SUnSET or OPP** channel rides along as the global-translation
normaliser — the only defensible use of an assay that cannot name a protein.

## 6.2 🔴 THE MATRIX — observation patterns × mechanism

Columns are the four mechanism classes the brief names. **Every row is a pattern across the five cells**;
every cell says what that pattern implies. `✅ REQUIRES` · `❌ EXCLUDES` · `⚪ silent`.

Readouts abbreviated: **RNA** ① · **`S_N`/`S_C`** ② absolute vs control · **`ρ`** ② the two-epitope ratio ·
**INH** ③ response to bafilomycin/MG-132 · **SOL/PEL** ④ · **τ** ⑤.

| # | **OBSERVATION PATTERN** | **Translation** (`H1`/`H2` — before) | **Early disposal** (`H3a`/`H3b` — during) | **Degradation** (`H4` — after) | **Insolubility** (`H5`) |
|---|---|---|---|---|---|
| **W1** | RNA **↓** · `S_N`,`S_C` ↓ · **ρ ≈ 1** · INH − · SOL/PEL both ↓ | ✅ **REQUIRES** — template-limited (`H1`) | ❌ EXCLUDES — nothing positional | ❌ EXCLUDES | ❌ EXCLUDES |
| **W2** | RNA **≈WT** · `S_N`,`S_C` **↓ equally** · **ρ ≈ 1** · INH **−** · SOL/PEL both ↓ · τ n/a | ✅ **REQUIRES** — `H2`, production-limited with template present. 🔴 §2.2 says no stall mechanism supports it, so this pattern would be **mechanistically unexplained and interesting** | ❌ EXCLUDES — disposal would be positional or inhibitor-sensitive | ❌ EXCLUDES | ❌ EXCLUDES |
| **W3** | RNA ≈WT · `S_N` mildly ↓ · `S_C` **strongly ↓** · **ρ ≈ 1.5–5.6** · INH **+ (ρ falls toward 1)** · PEL − | ❌ **EXCLUDES** — production past the epitope is normal; loss is downstream of it | ✅ **REQUIRES** — `H3b`, and **`d` is read off `ρ`** via `d = 1 − 155/(115R − 149)` | ⚪ silent — a mature pool may also turn over, ⑤ decides | ❌ EXCLUDES — nothing in the pellet |
| **W4** | RNA ≈WT · `S_N`,`S_C` **≈WT** · **ρ ≈ 1** · INH **+** · SOL ↓, PEL − · **τ short** | ❌ EXCLUDES — synthesis is normal | ❌ EXCLUDES — nascent chains are all present | ✅ **REQUIRES** — `H4`, classical post-pool degradation | ❌ EXCLUDES |
| **W5** | RNA ≈WT · `S_N`,`S_C` ≈WT · **ρ ≈ 1** · INH − · **PEL ↑, SOL ↓** · τ long in pellet | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES — blocking clearance changes nothing | ✅ **REQUIRES** — `H5`. 🔴 **And it is the row that retrospectively re-reads Johannsen's negative as an artefact of the discarded pellet** |
| **W6** | RNA ≈WT · `S_N`,`S_C` ≈WT · ρ ≈ 1 · INH − · SOL **≈WT**, PEL − | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES | ❌ EXCLUDES → 🔴 **NOT A MECHANISM ROW.** No lesion detected. Either the cells are wrong, **or the original *"protein not detected"* was a detection-floor / epitope artefact** — which cell ②'s floor calibration makes a **testable reading**, not a caveat |
| **W7** | RNA ≈WT · `S_N` ↓ · `S_C` ↓↓ · ρ > 1 · INH **+** · **PEL ↑** · τ short | ⚪ silent | ✅ partially | ✅ partially | ✅ partially → ✅ **`H6` MIXED, folding-primary.** ⭐ The pattern the inherited structural verdict predicts |
| **W8** | 🔴 `S_N`,`S_C` **both at or below the floor**, floor calibration shows the floor is **above** plausible WT signal | — | — | — | — → 🔴 **NOT A MECHANISM ROW. The assay is underpowered.** `DISCARD` and re-pilot at higher cell number / longer amplification. **This row exists only because ② carries floor calibration**, and without it W8 would be misread as W2 |

## 6.3 🔴 The DEGENERATE rows — the most important output, because each names a missing measurement

| Degeneracy | Which mechanisms give the identical pattern | Why the matrix cannot separate them | **The measurement that would** |
|---|---|---|---|
| **D1 · W1 ≡ W2 without cell ①** | `H1` vs `H2` | Both give `S_N`,`S_C` ↓ with `ρ ≈ 1`. **RNA is the only thing that separates them.** | Cell ① — which is why RNA stays in the matrix as a **control** although `H1` is largely excluded. Removing ① to save money recreates the degeneracy. |
| **D2 · `H3a` ≡ `H3b` inside W3** 🔴 | RQC-at-a-stall vs post-exposure triage | Both remove chains **after** the lesion is exposed, so both give `ρ > 1` with the same sign and a similar magnitude. **`ρ` reads *where*, not *by what machinery*.** | **A collided-ribosome / disome readout** (disome profiling, or ZNF598/EDF1 dependence) — a sequencing-scale experiment **not** in this matrix. §2.2 makes `H3a` a low prior, which is an argument, not a measurement. **Recorded as the matrix's principal blind spot.** |
| **D3 · W4 ≡ W5 if the pellet is discarded** | `H4` vs `H5` | *"Absent from the soluble fraction"* is the same observable whether the protein was destroyed or partitioned out. | Cell ④'s **pellet lane**. This is the `INHERITED` finding of `q230p_three_designs_one_experiment` §2 and it is unchanged: **the lysis buffer is the discriminator.** |
| **D4 · W2 ≡ W3 at very high `d`** 🔴 | `H2` vs `H3b` | As `d → 1`, `S_C` falls below the floor. `ρ` is then **unmeasurable**, not large, and the pattern collapses to "both arms low" — which reads as W2. | **The inhibitor arm, cell ③.** Under `H3b` a degradation block **restores `S_C` and drives `ρ` back toward 1**; under `H2` it does nothing. ⇒ 🔴 **Cell ③ is not optional. It is what rescues the discriminator in exactly the regime the published negative suggests we are in.** This is `P4`, confirmed and then **broken by the inhibitor arm** — see §10. |
| **D5 · W4 ≡ W7 with a single inhibitor** | `H4` vs `H6` | A single negative probe mis-assigns the route. `INHERITED`: `DL-MECH-047` records that MG-132 alone would have produced a false negative and *"killed the best-scored hypothesis in the portfolio"*; and Schultz 2018 found **chloroquine negative where bafilomycin A1 was strongly positive on the same mutant protein in the same experiment**. | **Both routes, always** — bafilomycin A1 **and** a proteasome inhibitor. Never one. |
| **D6 · every row, fibroblast vs neuron** | all | `INHERITED`: Koch 2011 shows a disease-relevant insoluble species forming **only in patient neurons**, *"not observed in iPSCs, fibroblasts or glia"*. | **The same matrix in a neuronal model.** Out of scope here. 🔴 A fibroblast is not a neuron, and **a negative in cell ④ cannot close `H5` for the disease-relevant cell type.** |

---

# §7 · `OUTCOME WIDTH × HYPOTHESIS DISCRIMINATION` — scored, with the revised rule

The revised rule: score the **product**, not the width. A wide but non-discriminating outcome is low value;
a narrow but hypothesis-separating measurement can be high. The primitive **failed once** by being applied
to a readout that could not carry the discrimination — so each row below states **which hypotheses the
readout can actually separate**, and every arm is checked to perturb **only** the variable in question.

| Measurement | Outcome width | Discrimination | Perturbs only its own variable? | **Product** |
|---|---|---|---|---|
| ⭐ **② two-epitope Puro-PLA, `ρ`** | **Medium** — a continuous ratio, but it cannot see `H5` at all | **Very high** — the **only** readout separating *during* (`H3`) from *before* (`H1`/`H2`) and *after* (`H4`), and it returns `d` as a number | ✅ puromycin only; CHX pre-treatment dropped (§3.3) | 🥇 **HIGHEST** |
| 🥈 **④ soluble / insoluble split at high load, with floor calibration** | **High** — re-reads the entire published negative | **Medium-high** — separates `H5` from everything, one branch only | ✅ no perturbation at all; a re-analysis of a lysate already being made | 🥈 **RUNNER-UP** |
| **③ inhibitor arm (baf A1 + proteasome)** | Medium | High **but conditional** — it is what breaks degeneracy **D4**, and it is nearly valueless alone | ✅ one inhibitor per arm | 🥉 high **as a rescue of ②**, not standalone |
| **⑤ FUNCAT-PLA pulse–chase** | High — real half-lives from birth | Medium — separates `H4` from `H3b` **only if a cohort is labelled at all** | ✅ AHA is non-perturbing (tom Dieck, verbatim §3.3) | Tier 2 — ~10× dimmer than ②, stage after |
| **① RNA qRT-PCR** | **Narrow** — the answer is already known to be "normal" | **High for one thing**: without it, **D1** is unbreakable | ✅ | Keep, cheap, as a **control** |
| **CHX chase alone, from baseline** | Narrow — undetectable at every timepoint | **~Zero** in the current abundance regime | ✅ | ❌ **Do not run first.** The `INHERITED` step-order correction stands: inhibitor → chase, never chase → inhibitor |
| **SUnSET / OPP alone** | High (global) | **Zero for this question** | ✅ | ❌ Normaliser only |
| ~~26–30 °C permissive-temperature arm~~ | — | — | 🔴 **NO** | 🔴 **NOT REINSTATED.** Roobol 2008 (`PMID 19054067`, `INHERITED`) shows mild hypothermia is itself a **global degradation inhibitor**, so a band at 30 °C is ambiguous between *folded* and *no longer cleared* — the exact pair the experiment exists to separate. It perturbs two variables. **Excluded.** |

> **The one measurement with the highest `width × discrimination` is the two-epitope Puro-PLA ratio `ρ`
> (cell ②), read against a calibrated detection floor, with cell ③ attached as its degeneracy-breaker.**
> **The runner-up is the soluble/insoluble split at high load (cell ④)** — which is also the cheapest thing
> on the list, runs on a lysate that is being made anyway, and is the only arm that can retrospectively
> reinterpret the published negative.

🔴 **Stated as a loss, not waved away.** `ρ` is **blind to `H5`**: an insoluble species is synthesised
normally and would give `ρ ≈ 1` with both arms normal. ② and ④ are therefore **complements, not
alternatives**, and running ② alone would produce a confident "synthesis is normal" that is compatible with
the protein sitting in a discarded pellet.

---

# §8 · What I could not resolve — absence claims in the required form

Each reads: *"No X was identified within [document classes], [languages], [file/source scope], using
[queries/routes]."* None reads *"X does not exist."*

1. **No WWOX detection floor, limit of detection or calibrated standard curve was identified** within
   dossiers, analyses, ledgers, commit candidates, queues, manifests, governance and scripts, in **EN and
   IT**, **unscoped by file type** across `disease-models/`, `framework/`, `governance/`, `roles/`,
   `scripts/` — **excluding `paper_registry_current.md` and `literature_tracking_log_current.md`, which are
   read by record and were not grepped, by rule** — using `detection floor|limit of detection|\bLOD\b|floor
   di rilevazione|soglia di rilevazione` (72 lines / 24 files, all inspected; none reports a numeric WWOX
   floor). ⇒ `P7` **CONFIRMED**.
2. **No Puro-PLA, FUNCAT-PLA, ribopuromycylation, PUNCH-P or SunRiSE reference was identified** within the
   same document classes, languages and scope, using those literal terms plus `proximity ligation`. Counts:
   **0 / 0 / 0 / 0 / 0**; `proximity ligation` 3 lines / 2 files, none a translation assay.
3. **No eIF5A, ribosome-collision or RQC-factor reference was identified** within the same scope, using
   `eIF5A`, `collided ribosome|ribosome collision|RQC|ribosome quality control`, `ZNF598|EDF1|GIGYF2|Hel2`,
   `LTN1|listerin|NEMF`. All **0**.
4. **No Puro-PLA application in human fibroblasts was identified** on **PubMed** via
   `mcp__PubMed__search_articles`, using `Puro-PLA human fibroblasts` → **0**. 🔴 **Positive control run:**
   the bare term `Puro-PLA` → **4 records**, so the term is indexed and the zero is a real narrowing of an
   indexed term — **but the technique is badly under-indexed by that string** (papers write *"puromycin
   proximity ligation assay"*), so this absence is **weak**. The nearest published systems found are
   *"human and mouse, migrating, mesenchymal cells"* (PMID 31290739, `abstract-depth`) and *"Drosophila
   Embryos and Human Cells"* (PMID 34590282, `abstract-depth`).
5. **The Methods of Johannsen 2018 (PMID 29808465) were not retrieved.** No route was attempted by me in
   this act — two routes (PMC/PubMed; `Scholar_Gateway semanticSearch`) are already recorded as failed by
   other actors, Springer-closed, no PMCID. **`PREMISE: METHODS_INVISIBLE` stands unchanged.**
   `REVIVAL_TRIGGER`: any Springer route, an author-hosted copy, or a later paper quoting Johannsen's lysis
   buffer. ⇒ `P6` **CONFIRMED, trivially** — I did not test it, so it is confirmed only in the weak sense
   that nothing changed.
6. **Could not establish: whether an anti-WWOX antibody against aa 286–299 exists as a catalogue reagent
   validated for immunofluorescence/PLA.** The epitope is characterised in the literature (PMID 34140629,
   `INHERITED`); **an epitope is not an antibody**. The C-arm of §4 is **unexecutable until this is
   checked**, and it is a catalogue lookup that gates the whole design. `HUMAN_REQUIRED` — **no vendor was
   contacted and nothing was purchased.**
7. **Could not establish: whether `HPA050992` performs in PLA** (it is used by this programme for
   immunoblot/IHC, `INHERITED`). Antibody performance is assay-specific; tom Dieck's Methods require
   per-antibody titration before any biological question. `HUMAN_REQUIRED`.
8. **Could not establish: the qRT-PCR amplicon position or reference gene in Johannsen 2018**, which
   determines how much `H1` is really excluded. Blocked by (5).
9. **Could not establish: whether donor-derived `Q230P/Q230P` fibroblasts are available to anyone.**
   `INHERITED` (`DL-BIO-001`) records only that *"la biopsia cutanea è una procedura diagnostica
   standard"* — feasible, not documented as available. **Every design in this file is conditional on
   material that is not documented to exist.** `HUMAN_REQUIRED`; no researcher was contacted.
10. **Not attempted: a PubMed search pairing WWOX with any nascent-labelling method.** 🔴 Deliberately.
    `INHERITED` trap: PubMed `[All Fields]` **does not index Methods sections or supplements**;
    `WWOX AND cycloheximide` returns **0** with a flawless expansion while ≥3 indexed WWOX papers ran it —
    miss rate in this gene **100 %**. Such a query **could not have produced evidence either way**, so
    `P3` is scored **UNTESTED**, not confirmed. Spending a call to manufacture an uninterpretable zero
    would have been the error the trap exists to prevent.

---

# §9 · Tool traps hit in this act — described so the next actor does not repeat them

1. 🔴 **NEW — the `SUnSET` / `sunset` collision.** `grep -ri SUnSET` over this repository returns **20
   files, of which 11 are governance files using the ordinary word *sunset*** (decision sunset, candidate
   sunset). **~55 % false-positive rate.** The technique hits live only under `disease-models/wwox/`.
   ⇒ Scope the directory, or grep case-sensitively for `SUnSET`.
2. 🔴 **NEW — PubMed silently expands `single` to `"single person"[MeSH Terms]`.** The query
   `azidohomoalanine click immunoprecipitation newly synthesized single protein fibroblasts` returned **0**,
   and `query_translation` shows `("single person"[MeSH Terms] OR ("single"[All Fields] AND "person"[All
   Fields]) OR "single person"[All Fields] OR "single"[All Fields] …)`. A **demographic** MeSH concept was
   injected into a molecular-biology query. Removing two words
   (`azidohomoalanine click immunoprecipitation newly synthesized protein`) still returned **0**; the bare
   term `azidohomoalanine` returned **193**. ⇒ The zero was **query construction, not absence**. Read
   `query_translation` **term by term**, as the standing trap says — and treat everyday English words
   (`single`, `control`, `lead`, `cell`) as MeSH-expansion hazards.
3. 🔴 **NEW — word boundaries, in the repository, in the direction nobody checks.** An unbounded `35S`
   matched **`MDA-MB435S`** — a melanoma cell line — in three dossiers. The standing `\bBUN\b`/*abundance*
   warning generalises to **isotope and clone names embedded in cell-line identifiers.**
4. ⚠️ **Confirmed, not new — `get_copyright_status.is_open_access` is a licence field.** Not re-tested by
   me; carried forward because §8(6)–(7) will need it. **A PMCID is not a body. ORDER an attempt; never SKIP.**
5. 🟢 **The trap that did *not* fire, recorded because avoiding it was the point.** I did **not** issue a
   bare `"Q230P"` query. `INHERITED`: it returns 2 records, **neither WWOX** — both **GTPBP3** at an
   identical `c.689A>C (p.Q230P)`, one carrying a *measured aggregation result*, which is the most
   citable-looking false positive in this search space. Nothing in this file rests on any bare-`Q230P`
   literature search.
6. 🟢 **Positive controls carried with every negative count**, per the standing rule: `Puro-PLA` → 4 (for a
   0 on `Puro-PLA human fibroblasts`); `azidohomoalanine` → 193 (for a 0 on the conjunction);
   `ribopuromycylation` → 26 (for a 0 on a five-term conjunction).

---

# §10 · `PREDICTION OUTCOME`

| # | Outcome | What it taught |
|---|---|---|
| **P1** | 🔴 **REFUTED** | Six repository files already hold pulse-labelling / nascent-synthesis content, including a **ranked protocol shortlist** written today. Had I skipped §1 I would have re-derived Scientist C's entire shortlist and presented it as new — **the exact failure `q230p_three_designs_one_experiment` §5 records happening twice already.** The refutation is what forced this file to become a *delta* (§1.4) rather than a restatement, and the delta is the only reason it has content. |
| **P2** | 🔴 **REFUTED** | `polysome` appears in 6 files and `ribosome profil` in 5 — and one of them **rejects** those assays. Reading the rejection made me test *its reason*, which is how §2.2 happened. **A refuted prediction produced the file's cheapest finding.** |
| **P3** | ⚪ **UNTESTED, deliberately** | The `[All Fields]`-does-not-index-Methods trap (100 % miss rate in this gene) means the query could not have produced evidence either way. Recording it as UNTESTED rather than manufacturing an uninterpretable zero is the honest score. |
| **P4** | 🟡 **CONFIRMED, then partly broken — and the breaking is the result** | The degeneracy is real and is **D4**: as `d → 1`, `S_C` drops below the floor and `H3b` collapses into `H2`'s pattern. But my falsifier was *"a pulse duration / inhibitor combination that separates them **with no extra perturbation**"* — and **cell ③ is exactly that**, at the cost of one perturbation I had forbidden myself. So: confirmed under my own stated constraint, broken as soon as one inhibitor arm is allowed. 🔴 **The lesson is about the falsifier, not the prediction:** I wrote "no extra perturbation" into the falsifier without asking whether that constraint was worth keeping. It was not — a one-variable inhibitor arm is exactly the kind of perturbation the brief's own rule permits. |
| **P5** | 🟢 **CONFIRMED** | The winner is a short-pulse labelling readout with a degradation block as the only perturbed variable (§7), and the CHX chase scores ~zero standalone. But the confirmation is **narrower than I predicted**: I expected the winner to need **immunocapture**, and the actual winner (`Puro-PLA`) needs **none** — which is precisely why it is executable where the IP route dead-ends. |
| **P6** | 🟢 **CONFIRMED (weakly)** | I attempted no new route, so this is confirmed only in the sense that nothing changed. **Not a finding.** |
| **P7** | 🟢 **CONFIRMED** | 72 lines across 24 files discuss detection floors; **not one reports a numeric WWOX LOD**. The matrix carries floor calibration as a consequence, and row **W8** exists only because of it — without it an underpowered assay reads as `H2`. |

**Two of seven refuted, one untested, one half-broken.** The two refutations produced §1.4 and §2.2, which
are the two things in this file that were not already in the repository.

---

# §11 · `V0` SHADOW TRACE

Observational instrumentation, not a gate.

- **BASELINE** — Listed the tree (`find`), declared file-type / language / document-class scopes, then swept
  bilingually with word boundaries, excluding the two large registries by rule. **Refuted `P1` and `P2`**
  and surfaced six sibling files. *Produced the most.*
- **DIVERGE** — Eleven candidate techniques enumerated with a `gate_is_not_quantity` column each (§3.2);
  `H3` split into `H3a`/`H3b` on structural grounds. *Produced the technique table and the hypothesis split.*
- **CONNECT** — Local-translation neuroscience (`Puro-PLA`/`FUNCAT-PLA`) joined to a patient-fibroblast
  abundance question; the repository's own `HPA050992` epitope coordinates joined to Puro-PLA's length gate.
  *Produced §4, the only new instrument here.*
- **PREDICT** — Seven pre-registered predictions with explicit falsifiers, timestamped before any content
  search. *Produced two useful refutations and one instructive half-break (`P4`).*
- **SEARCH** — PubMed via MCP; two bodies read in full (PMC4414919, PMC7490010), five records at
  abstract-depth; positive controls carried with every zero. *Produced the `verify_the_omitted_clause` find.*
- **ADJUDICATE** — Hobson 2020 re-read against its headline: the sentence beside it **affirms** the
  abundance readout the title appears to destroy; the false-positive caveat is explicitly scoped by its own
  authors to the abundant-abundant regime that WWOX is not in. Scientist C's polysome verdict endorsed,
  its reason replaced. *Produced the strongest single item in this file.*
- **REVISIT** — Re-derived the matrix after `P4` half-broke, which added cell ③ as a **required**
  degeneracy-breaker rather than an optional arm, and added row **W8**. *Produced D4 and W8.*
- **`null`** — No step produced nothing. **The step that produced least was PREDICT-`P6`**, which confirmed
  only that I had not attempted a retrieval I never attempted.

---

# §12 · Declared limits

1. **Non-canonical.** Nothing here is a claim, a commit candidate, or a change to any `*_current.md`. No
   `FULLTEXT_READ_RECEIPT` is claimed or owed.
2. **`MOLECULAR FATE UNRESOLVED` is unchanged by this file.** No measurement was made on `Q230P` protein.
   Everything in §4–§7 is a **design**, and a design is not a result.
3. **Two bodies read in full** (PMC4414919, PMC7490010). Five records are `abstract-depth` and labelled:
   PMID 34590282, 31290739, 32435426, 40084072, and the `INHERITED` items carried from other actors' files
   at the depth **they** declared.
4. **§2's computations are on an AlphaFold model**, not an experimental structure. Residue identity,
   numbering, sequence composition and Met/Pro positions are sequence facts and are robust; the pLDDT and
   the secondary-structure context are model properties. The `INHERITED` structural verdict I build on was
   measured by another actor on these same coordinates, and carries that actor's caveats.
5. **§4's arithmetic is a prediction, not a calibration.** `R₀ = 2.643` assumes uniform ribosome density,
   which is false in detail for every mRNA — which is why the experiment reads `ρ = R_patient / R_control`
   and never compares a measured `R` to 2.643.
6. **The C-arm is unexecutable until §8(6) is checked.** An epitope is not an antibody. If no aa-286–299
   PLA-grade antibody exists, §4 degrades to a single-arm Puro-PLA, which measures production but **loses
   `ρ` entirely** — i.e. loses the whole "during" discrimination. **This is the single point of failure of
   the top-scored design and it is a catalogue lookup.**
7. **A fibroblast is not a neuron** (degeneracy **D6**), and homozygous `Q230P/Q230P` cells are not the
   `null/missense` reference genotype (§5). Both transfers are assumptions, both untested.
8. **No external contact, no correspondence drafted or sent, no purchase made or attempted.** All such
   items are parked in §8 as `HUMAN_REQUIRED`.
9. **Nothing in this file is medical advice.**

---

*Sources retrieved through the PubMed MCP tools. According to PubMed, the full texts read by me in this act
are PMID 25775042 / PMCID PMC4414919 / [DOI 10.1038/nmeth.3319](https://doi.org/10.1038/nmeth.3319) and
PMID 32844746 / PMCID PMC7490010 / [DOI 10.7554/eLife.60048](https://doi.org/10.7554/eLife.60048).
Abstract-depth records are PMID 34590282 / [DOI 10.1007/978-1-0716-1740-3_15](https://doi.org/10.1007/978-1-0716-1740-3_15),
PMID 31290739 / [DOI 10.7554/eLife.44752](https://doi.org/10.7554/eLife.44752),
PMID 32435426 / [DOI 10.1016/j.csbj.2020.04.014](https://doi.org/10.1016/j.csbj.2020.04.014) and
PMID 40084072 / [DOI 10.21769/BioProtoc.5224](https://doi.org/10.21769/BioProtoc.5224).
Records cited as other actors' attestations, at the depth those actors declared, are PMID 29808465
/ [DOI 10.1007/s10048-018-0549-5](https://doi.org/10.1007/s10048-018-0549-5), PMID 30202070, PMID 26780369,
PMID 18216017, PMID 22113611, PMID 16563356, PMID 19305406, PMID 19054067 and PMID 34140629.
No PMID or DOI in this file was reconstructed from memory; every one was returned by a tool call in this
session or carried from a named repository file. No living researcher's contact details appear in this file.*
