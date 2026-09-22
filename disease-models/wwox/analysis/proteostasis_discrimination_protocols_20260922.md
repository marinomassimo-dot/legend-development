# Discriminating reduced synthesis vs accelerated turnover vs insolubility for a single missense allele in patient-derived fibroblasts — a ranked protocol shortlist from outside the WWOX field

**Date:** 2026-09-22 · **Actor:** Scientist C (Domain D) · **Status:** non-canonical analysis. Touches no registry, no receipt ledger, no state manifest.
**Nothing in this file is medical advice.** Every inhibitor named here is a bench reagent in cell culture at published in-culture concentrations, never a therapy.

**Question.** For the reference genotype's SDR missense allele Q230P, `CLAIM 019` / `DL-MECH-029` record a measured human endpoint — normal WWOX transcript by qRT-PCR, no detectable WWOX protein by Western blot in patient fibroblasts (Johannsen 2018) — and three unresolved branches: **(a) reduced synthesis**, **(b) normal synthesis + accelerated turnover**, **(c) normal synthesis + insolubility**. The in-silico route is closed: `relSASA`/ΔΔG do not predict measured abundance in this gene (P47 has the highest ΔΔG, +2.81, and **measured** normal protein). This file asks what **measured** experimental protocol, published outside the WWOX field, separates the three in primary human fibroblasts.

---

## 0 · What the repository already holds — so this file is a delta, not a rediscovery

Read first, as instructed: `HYP-20260709-08` and the historical updates under it in [`therapeutic_hypotheses_ledger_current.md`](../research/therapeutic_hypotheses_ledger_current.md), `DL-BIO-001` in [`discovery_ledger_current.md`](../research/discovery_ledger_current.md), and the row-1 / row-6 cells of [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md).

**Already held — do not re-report as new:**

| Already in the repository | Where |
|---|---|
| The three-way question itself, named in these exact terms, with the falsifiable statement | `HYP-20260709-08`, *"se Q230P è sintetizzata a velocità normale e degradata prematuramente…"* |
| The **five-step minimal experiment**: (1) WB on donor-derived fibroblasts, (2) qRT-PCR, (3) **nascent synthesis + pulse-chase with soluble/insoluble fractionation**, (4) orthogonal turnover probes, (5) function-if-rescued | `HYP-20260709-08` "🧪 Esperimento minimo che decide" |
| A **lysosomal inhibitor arm with concentrations**: chloroquine **40 µM / 24 h**, NH₄Cl **250 µM / 24 h**; **MG-132 as the expected NEGATIVE control**; 3-MA as second negative | `DL-BIO-001` update 2026-09-21, from PMID 41124647 |
| HSC70 co-IP and LAMP1 co-localisation as associative readouts, **not** proof of CMA; KFERQ motif never mutated; `LAMP2A` zero occurrences in that body | `DL-MECH-047`, `DL-BIO-001` |
| 4-PBA/TUDCA are the **wrong compartment** (ER stress) for a cytosolic/mitochondrial protein on a lysosomal route; arimoclomol **withdrawn** because HSC70 amplification may accelerate, not slow, degradation | `HYP-20260709-08`, update 2026-07-12 |
| "Stable-but-inert" is a **demonstrated** phenotype for a WWOX SDR missense substitution (P282A) — abundance and function are separable | `HYP-20260709-08`, `DL-BIO-001` |
| The CFTR/Trikafta, tafamidis, migalastat, sapropterin, ambroxol precedents — but **only as therapeutic paradigms** | `TX-003`, [`mechanism_intervention_map.md`](mechanism_intervention_map.md), [`proteostasis_rationale.md`](proteostasis_rationale.md), `T7` in [`wwox_sdr_function_per_molecule_census_20260921.md`](wwox_sdr_function_per_molecule_census_20260921.md) |
| The explicit gap statement: *"No nascent-synthesis measurement for any WWOX missense allele — no metabolic pulse labelling, no polysome or ribosome profiling, no SUnSET/AHA-click. No soluble/insoluble fractionation"* | [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md), row 1 |

**Repository-absence check, with the queries and the counts** (a zero from a grep is not evidence of absence unless the grep is shown to read):

```
$ grep -ril "<term>" disease-models/wwox/   →   files matching
  SUnSET 1  ·  pulse-chase 7  ·  cycloheximide 28  ·  CFTR 4  ·  F508del 4
  alpha-1 0 · antitrypsin 0 · rhodopsin 0 · P23H 0 · HaloTag 0 · SNAP-tag 0 · SILAC 0
  "filter trap" 0 · "detergent-insoluble" 0 · "Triton X-100" 0 · SDD-AGE 0 · "semi-denaturing" 0 · "click chemistry" 0
```
The single `SUnSET` hit and the single `AHA-click` mention are both the same sentence in `missense_proteostasis_matrix_20260921.md` row 1 — i.e. the repository names these methods **as a gap**, and nowhere evaluates them. `CFTR`/`F508del` appear only as therapeutic analogies, never as a source of measurement methods. **So the delta this file can add is: which of these methods actually works on primary human fibroblasts, at what cost, and which of them the repository's current design would get wrong.**

---

## 1 · The headline answer, stated plainly — a negative result

> **No single validated protocol separates all three branches in primary human fibroblasts.** The literature I could read supports a **two-stage** design, not a one-shot assay:
>
> - **Branch (b), accelerated turnover, is well served.** There is a published, worked, primary-patient-fibroblast protocol with exact reagents and concentrations, on endogenous protein, for a missense allele with the same signature as Q230P (normal mRNA, protein nearly absent). **`measured`, full text read.**
> - **Branch (c), insolubility, is served by protocols but not by precedent in fibroblasts.** The sequential-solubility ladder is standard and cheap, but I could find **no** published instance of it detecting a disease-relevant insoluble species in primary human dermal fibroblasts — and one Nature paper reports the opposite: the aggregation phenotype it measured *"was not observed in iPSCs, fibroblasts or glia."*
> - **Branch (a), reduced synthesis, is the worst served and is the expensive one.** Every non-radioactive translation assay I found (SUnSET, OP-puro, AHA/HPG click) measures **global** translation. None of them tells you the synthesis rate of *one* protein. Protein-specific nascent synthesis still requires pulse-label **plus immunoprecipitation** — i.e. ³⁵S, or AHA + click + IP — and I found no validated instance of either for a low-abundance single protein in primary human fibroblasts.

**Consequence for experimental design, and it is the practical point of this file:** do not try to answer (a) first. Answer **(c) then (b)** with two cheap assays that share one lysate; only if both are negative does the expensive synthesis measurement become necessary — and at that point a negative (b) and a negative (c) have already made (a) the surviving branch by elimination, which is weaker evidence than measuring it, but may be enough to act on.

---

## 2 · Ranked shortlist

Ranked by the stated criterion: *can this be done on a skin biopsy from one person, in a normally-equipped lab, this year.*

All cost/time figures below are **my own order-of-magnitude estimates (`STIMA`)**, not values taken from any source. No source I read states a cost.

---

### 🥇 RANK 1 — Solubility re-blot of the existing lysate (sequential detergent extraction)

**1. What it measures, and what it separates.** Total protein partitioned between a mild-detergent-soluble fraction and a progressively harsher-solvent-soluble pellet. It separates **(c) from (a)+(b)** — and only that. It does **not** distinguish (a) from (b).

**Why it ranks first despite separating only one branch:** it is the only candidate that can be run on a lysate that is *already being made anyway* for the Western blot that is step 1 of `HYP-20260709-08`. It is a re-analysis, not a new experiment. And it tests the one branch that, if true, makes every other result on this allele uninterpretable — because a "protein absent" Western on a cleared soluble lysate is *the same observable* whether the protein was never made, was destroyed, or is sitting in the discarded pellet. `INFERENZA`, and a direct one: Johannsen 2018's "protein absent" result has never been shown to have interrogated the pellet.

**2. Reagents and equipment.** Ordinary lysis buffers plus SDS and urea. A bench microcentrifuge suffices for a crude soluble/insoluble split. **Flag:** the canonical published ladder uses **ultracentrifugation at 100,000 × g**, which not every lab has. No radioactivity, no BSL constraint, no mass spectrometer, no custom antibody, no new cells.

**3. Run in primary human fibroblasts?** **No — and this is the honest weakness.** The protocol I read in full is on **post-mortem human brain tissue**, not fibroblasts. The closest solubility-ladder precedent on a missense allele is in **transgenic mouse spinal cord and COS-7 cells** (`abstract-depth`). I found **no** published instance in primary human dermal fibroblasts.

**4. Verbatim locators.**

- The ladder, with exact buffers — *"Prepare TBS-SDS buffer by adding 5% w/v Sodium dodecyl sulphate (SDS) to 1X TBS (pH 7.4) buffer."* … *"Prepare TBS-SDS-Urea buffer by adding urea to a final concentration of 8 M w/v to 1X TBS-SDS buffer (pH 7.4)."* … *"Centrifuge at 100,000 x g for 1 hr at 4 °C. Retain supernatant as this is the TBS-soluble fraction."*
  → **Source:** Protocol §1 and §2, *"Sequential Extraction of Soluble and Insoluble Alpha-Synuclein from Parkinsonian Brains"*, J Vis Exp, PMID 26780369, PMCID PMC4781043, [DOI 10.3791/53415](https://doi.org/10.3791/53415). **Full text read via PubMed/PMC, CC BY 3.0 US.** Matrix is post-mortem brain, explicitly: *"Take a chunk of frozen human tissue (approximately 0.5 g in weight from the basal ganglia region)"*.
- The three-step ladder applied to a **missense** allele — *"Mutant SOD1 specifically altered to insoluble forms, which were sequentially separated into Triton X-100-insoluble/sodium dodecyl sulfate (SDS)-soluble and SDS-insoluble/formic acid-soluble species."*
  → **Source:** abstract, Koyama S *et al.*, Biochem Biophys Res Commun 2006;343(3):719–30, PMID 16563356, [DOI 10.1016/j.bbrc.2006.02.170](https://doi.org/10.1016/j.bbrc.2006.02.170). **`abstract-depth` — I did not read the body.** System is transgenic mouse spinal cord and COS-7, **not** patient fibroblasts.
- 🔴 **The counter-evidence, and it is the most important sentence in this file for branch (c)** — *"Aggregate formation was further dependent on functional Na(+) and K(+) channels as well as ionotropic and voltage-gated Ca(2+) channels, and **was not observed in iPSCs, fibroblasts or glia**, thereby providing an explanation for the neuron-specific phenotype of this disease."*
  → **Source:** abstract, Koch P *et al.*, *Nature* 2011;480(7378):543–6, PMID 22113611, [DOI 10.1038/nature10671](https://doi.org/10.1038/nature10671). **`abstract-depth`.** For ataxin-3 in Machado-Joseph disease, the SDS-insoluble species formed **only in patient-derived neurons** and was **absent in the same patients' fibroblasts**. This is a published demonstration that a fibroblast-negative solubility result can be a **false negative for the disease-relevant cell type**. It does not transfer automatically to WWOX — the mechanism there is excitation- and calpain-dependent and WWOX is not a polyQ protein — but it establishes the failure mode, and `HYP-20260709-08` already carries the matching caveat in its own words (*"Il dato è su fibroblasti, non neuroni. La stabilità proteica è tessuto-specifica."*).

**5. Cost / time.** `STIMA`: reagent cost **~10¹ EUR** (buffers the lab already owns); **~1 day** of bench time on top of a Western that is being run anyway. This is the cheapest informative experiment available on this allele, by an order of magnitude.

**Query-verified literature count, since this is a near-absence claim:** PubMed query `SDS-insoluble aggregates patient fibroblasts disease` → `total_count: 2` (PMIDs 22113611, 16563356). Neither is a positive detection in primary human fibroblasts; one is an explicit **negative** in fibroblasts. The parser was reading correctly — the same tool returned 8, 12, 29 and 30 on adjacent queries in this session.

---

### 🥈 RANK 2 — Degradation-route inhibitor panel + cycloheximide chase, on endogenous protein in primary patient fibroblasts

**1. What it measures, and what it separates.** (i) Whether blocking a degradation route makes the missing protein **re-appear**, and by which route; (ii) after re-appearance, the decay rate of the existing pool under translational block. Together they separate **(b) from (a)+(c)**. Combined with Rank 1 on the same cells, the pair separates all three — **by elimination for (a), not by measurement of (a)**. That distinction is load-bearing and must not be collapsed.

**2. Reagents and equipment.** Bafilomycin A1, MG132, epoxomicin, chloroquine, cycloheximide — all catalogue reagents, all named with vendor codes in the source. Standard Western blot. **Flags:** none of the blocking flags apply — no radioactivity, no BSL facility, no mass spectrometer, no custom antibody, no cells the reference genotype does not have. An anti-WWOX antibody validated for endogenous protein in fibroblasts is required and is **not** a custom reagent, but its sensitivity floor is the limiting instrument (see §3 caveat 3).

**3. Run in primary human fibroblasts?** ✅ **Yes — endogenous protein, primary patient fibroblasts, named Coriell lines, for a missense allele with the same signature as Q230P.** This is the strongest fit in the shortlist. The lines are named in the source: *"GM08399 (CTRL), GM18453 (I1061T/I1061T), GM17912 (P1007A/T1036M), GM03123 (C.1947+5G>C/I1061T), GM17926 (I1061T/Y509S), and GM17924 (451ΔAG/Y825C)"* — i.e. exactly the "one person's skin biopsy" matrix, including **compound heterozygotes**, which the reference genotype is.

**4. Verbatim locators.** All from the **full text**, read via PubMed/PMC: Schultz ML *et al.*, *"Coordinate regulation of mutant NPC1 degradation by selective ER autophagy and MARCH6-dependent ERAD"*, Nat Commun 2018;9(1):3671, PMID 30202070, PMCID PMC6131187, [DOI 10.1038/s41467-018-06115-2](https://doi.org/10.1038/s41467-018-06115-2). CC BY 4.0, open access confirmed by `get_copyright_status` pre-test before retrieval.

- **The design, in primary fibroblasts:** *"we analyzed lysates from control (CTRL) cells expressing WT and homozygous primary fibroblasts after treatment with the proteasome inhibitors MG132 or epoxomicin (Epox) at non-toxic concentrations"*.
- **The cycloheximide chase, exact:** *"Cycloheximide chase: Cells were treated with 60 μg/ml cycloheximide for the indicated times. Serum starvation was induced by replacing cell culture media with cycloheximide containing MEM media without FBS."* (Methods, "Cells").
- 🔴 **THE FINDING THAT CONTRADICTS THE REPOSITORY'S CURRENT DESIGN** — *"Consistent with previous reports, treatment with the lysosomal inhibitor **chloroquine did not significantly alter I1061T protein levels** (Supplementary Fig.). While this difference likely reflects an increased efficacy of Baf to neutralize lysosomal pH relative to chloroquine, other possibilities cannot be excluded."* — against, in the **same cells, same protein, same experiment**: *"Unexpectedly, **Baf treatment also recovered I1061T protein to WT levels**… indicating that the lysosome is a major compartment utilized in I1061T degradation."*
- **The baseline that matches Q230P's signature:** *"Like cells homozygous for [I1061T], these lines showed **low baseline levels (5–34%)** of mutant NPC1 protein relative to WT."*
- **The discipline point, demonstrated in primary patient fibroblasts:** *"Although both MG132 and Baf increased I1061T protein levels (Fig.), **neither one rescued cholesterol accumulation** (Fig.). … These data indicated that the **accumulating I1061T protein was non-functional**."*
- **The two-route result:** *"We conclude that several NPC1 missense mutants, including I1061T, are degraded by **both the lysosome and proteasome**."*

**5. Cost / time.** `STIMA`: reagent cost **~10²–10³ EUR**; **~2–4 weeks** of bench time including fibroblast expansion, dose-finding and replicates. No capital equipment beyond a standard Western setup.

---

### 🥉 RANK 3 — Chemical-chaperone / permissive-temperature accumulation test

**1. What it measures, and what it separates.** Whether lowering the folding burden (growth at ~30 °C) or adding a chemical chaperone makes the protein re-appear. A positive separates **(b)+(c) from (a)**: if protein appears when folding conditions improve, it was being **made** and then lost. This is the closest thing in the literature to a *direct* test that synthesis is intact, without a pulse label.

**2. Reagents and equipment.** A second CO₂ incubator set to a permissive temperature, plus catalogue chemical chaperones. **Flag:** the chemical chaperones in the canonical worked example are ER-directed; `HYP-20260709-08` and `DL-MECH-047` already record that **4-PBA/TUDCA are the wrong compartment** for a cytosolic/mitochondrial protein on a lysosomal route — so the **temperature arm, not the chaperone arm, is the transferable part**. No radioactivity, no BSL, no MS, no custom antibody.

**3. Run in primary human fibroblasts?** ✅ **Yes** — the canonical statement is explicitly in *"human fibroblasts homozygous for the … mutation."* ⚠️ **But I have this at `abstract-depth` only.**

**4. Verbatim locator.** *"To gain insight into the molecular mechanism by which the [I1061T] mutation causes disease, we examined expression of the mutant protein in **human fibroblasts homozygous** for the [I1061T] mutation. Despite similar [NPC1] mRNA levels between wild type and [I1061T] fibroblasts, NPC1 protein levels are decreased by 85% in [I1061T] cells. Metabolic labeling studies demonstrate that … NPC1[I1061T] protein … exhibits a reduced half-life (6.5 h) versus wild type Endo H-resistant species (42 h). **Treatment with chemical chaperones, growth at permissive temperature, or inhibition of proteasomal degradation increases NPC1[I1061T] protein levels**, indicating that the mutant protein is likely targeted for endoplasmic reticulum-associated degradation (ERAD) due to protein misfolding."*
→ **Source:** abstract, Gelsthorpe ME *et al.*, J Biol Chem 2008;283(13):8229–36, PMID 18216017, PMCID PMC2276376, [DOI 10.1074/jbc.M708735200](https://doi.org/10.1074/jbc.M708735200).
🔴 **`abstract-depth`, and the body is not retrievable here.** `get_copyright_status(["18216017"])` returned `license.is_open_access: false`, copyright *"© 2008, The American Society for Biochemistry and Molecular Biology, Inc."* A PMCID exists (PMC2276376) and **is not a body**: the retrieval returned `"full_text": ""`. **This candidate is therefore a FLAG, not a scored candidate** — the method, its controls and its detection floor are unverified. Note also an unresolved discrepancy I cannot adjudicate without the bodies: Gelsthorpe's abstract gives WT half-life as **42 h** (Endo H-resistant species), while Schultz 2018's body gives *"the wildtype (WT) protein is degraded with a half-life approximating of 9 h"*. Two papers on the same protein, two WT half-lives. This is itself a caution about how much a single published half-life is worth.

**5. Cost / time.** `STIMA`: reagent cost **~10¹–10² EUR**; **~1–2 weeks**. The temperature arm costs essentially nothing but incubator time.

---

### 4 — Protein-specific nascent-synthesis measurement (³⁵S or AHA + click, **plus immunoprecipitation**)

**1. What it measures, and what it separates.** Label incorporated into WWOX specifically during a short pulse = the **synthesis rate**. This is the **only** candidate that measures branch (a) directly rather than by elimination. With a chase series it also yields turnover in the same experiment, so in principle it separates **all three** when combined with solubility fractionation of the same labelled lysate. This is exactly step 3 of `HYP-20260709-08` — the repository already specifies it. **This file's contribution is not the idea; it is the finding that the idea has no cheap validated implementation.**

**2. Reagents and equipment.** ³⁵S-Met/Cys route: **radioactivity — hard flag**, requiring a licensed isotope facility, methionine-free medium, and either a phosphorimager or film. AHA/click route: methionine-free medium, AHA, copper-click or strain-promoted click reagents — no radioactivity, but the click chemistry adds cost and an optimisation burden. **Both routes require immunoprecipitation of WWOX from the labelled lysate, which requires an antibody that works for IP, not merely for Western** — a distinct and frequently failing requirement.

**3. Run in primary human fibroblasts?** ⚠️ **Partly, and not for this purpose.** ³⁵S metabolic labelling in patient fibroblasts is routine in one specific niche — mitochondrial translation assays — and Gelsthorpe 2008 states *"Metabolic labeling studies"* in patient fibroblasts (`abstract-depth`, body not retrievable). But I found **no** published instance of protein-specific nascent-synthesis measurement, by pulse-label + IP, for a **low-abundance single protein** in primary human dermal fibroblasts.

🔴 **The trap this entry exists to prevent.** The three non-radioactive translation assays a reader is most likely to reach for — SUnSET, OP-puro and AHA/HPG imaging — **all measure global translation and none of them measures one protein.** SUnSET's own definition, verbatim: *"We developed a nonradioactive fluorescence-activated cell sorting-based assay, called surface sensing of translation (SUnSET), which allows the monitoring and quantification of **global protein synthesis** in individual mammalian cells and in heterogeneous cell populations."* → abstract, Schmidt EK *et al.*, *Nat Methods* 2009;6(4):275–7, PMID 19305406, [DOI 10.1038/nmeth.1314](https://doi.org/10.1038/nmeth.1314); `abstract-depth`, and the abstract is the definition. **A normal SUnSET/OPP signal in Q230P fibroblasts would say nothing whatever about whether WWOX is being translated.** Global translation is not the question; it is a different question that happens to use the same reagents. If this appears in a future protocol without an IP step attached, it is a design error.

**4. Verbatim locator.** As above for SUnSET. For the pulse-label-in-patient-fibroblasts precedent, the only locator I can offer is Gelsthorpe's *"Metabolic labeling studies demonstrate that …"* — `abstract-depth`, body unavailable. **I could not verify any method detail of a protein-specific pulse-chase in primary fibroblasts.** This is a FLAG, not a candidate.

**5. Cost / time.** `STIMA`: **~10³–10⁴ EUR** plus isotope-licence overhead or click-reagent cost; **~1–3 months** including IP development. An order of magnitude above Ranks 1–3, which is precisely why it should be staged last.

---

### 5 — Polysome profiling / ribosome profiling · **REJECT for this question**

Named only to close it off. Polysome profiling needs an ultracentrifuge and gradient fractionator; ribosome profiling needs sequencing. Both report **ribosome occupancy on the mRNA**, which for a missense allele with normal transcript is the wrong observable: a codon substitution at position 230 has no mechanism by which it would reduce ribosome loading, and the branch (a) hypothesis Johannsen actually named — *"impaired translation"* — is not a loading defect but, if anything, a co-translational folding/quality-control defect that these assays do not see. `INFERENZA`, flagged as mine. `STIMA` cost **~10⁴ EUR**. Not worth staging.

---

## 3 · Three caveats that apply to the whole shortlist, and one that changes the running order

**Caveat 1 — the canonical folding-disease literature's central readout does not transfer to WWOX.**
CFTR-F508del, NPC1-I1061T, alpha-1-antitrypsin Z and rhodopsin P23H are all **secretory or membrane glycoproteins**, and the assay that makes their literature so powerful is **glycosylation maturation** — EndoH-sensitive vs EndoH-resistant, CFTR "band B vs band C". Schultz 2018 leans on it throughout: *"Upon trafficking to the medial Golgi, these glycans are modified so that they are resistant to digestion by endoglycosidase H (EndoH)… In contrast, I1061T was sensitive to EndoH digestion (Fig.), indicating a failure to traffic through the medial Golgi."* The repository already holds that **WWOX is cytosolic/mitochondrial** (`HYP-20260709-08`, update 2026-07-12: *"WWOX è citosolica/mitocondriale"*), and a cytosolic protein has no glycan clock. ⚠️ **I have not verified from a primary source that WWOX is not N-glycosylated** — I am inferring it from the repository's localisation statement, and it is flagged as `INFERENZA` and **unverified**, not asserted. If it holds, the consequence is sharp: **the CFTR/NPC1 paradigm gives this programme its inhibitor panel and its discipline, but not its central assay.** That is why `T7` in the SDR census was right to call it *"Paradigm only."*

**Caveat 2 — you cannot chase what you cannot see, so the repository's step order is wrong.**
`HYP-20260709-08` lists pulse-chase at step 3 and the inhibitor arms at step 4. But Q230P protein is **undetectable** at steady state by Western blot. A cycloheximide chase starting from an undetectable band yields an undetectable band at every timepoint — no half-life, no information, a wasted month. The chase becomes interpretable **only after** an inhibitor has accumulated a measurable pool. `INFERENZA`, but a mechanical one, and Schultz 2018's own sequence is consistent with it: the inhibitor panel establishes accumulation first, and the cycloheximide chase appears later, used to measure clearance of an accumulated pool under serum starvation. **Proposed correction: inhibitor panel → chase, not chase → inhibitor panel.**

**Caveat 3 — "not detected" is a detection floor, not a zero, and the floor is the antibody.**
`HYP-20260709-08` already carries this as uncertainty 3 (*"«Assenza» al Western blot è un limite di sensibilità, non uno zero assoluto"*). Every protocol here inherits it. Schultz 2018's own answer is brute-force loading: *"To visualize I1061T-NPC1, 50 µg was loaded per well."* — roughly an order of magnitude above a routine load. That is a free, concrete improvement to step 1 of the minimal experiment.

**🔴 The caveat that changes the running order — the repository's lysosomal arm has a documented false-negative risk in exactly the cell type it plans to use.**
`DL-BIO-001` and `HYP-20260709-08` currently specify **chloroquine 40 µM / 24 h** and **NH₄Cl 250 µM / 24 h** as the lysosomal arm, imported from PMID 41124647 — where that experiment was run in **CAL-62 thyroid-carcinoma cells stably over-expressing a Flag transgene**. Schultz 2018, on **endogenous protein in primary patient fibroblasts**, found chloroquine **negative** and bafilomycin A1 **positive on the same mutant protein in the same experiment**, and says so in as many words (quoted in Rank 2 above). The repository has already been bitten once by exactly this failure mode: `DL-MECH-047` records that MG-132 as the *sole* degradation probe would have produced a false negative and *"killed the best-scored hypothesis in the portfolio."* **This is the same trap one reagent to the left.**
→ **Concrete correction: add bafilomycin A1 as a third lysosomal arm alongside chloroquine and NH₄Cl.** It is one more catalogue reagent and a few more wells. If chloroquine alone is run and comes back negative, the result is not interpretable as "not the lysosome."

---

## 4 · What I could not verify

| Item | Why not |
|---|---|
| Gelsthorpe 2008 (PMID 18216017) — the single best-fitting worked example (patient fibroblasts, normal mRNA / 85% protein loss, metabolic labelling, permissive temperature, proteasome inhibition) | `get_copyright_status` → `is_open_access: false`; PMCID PMC2276376 exists but the retrieval returned an **empty body**. A PMCID is not a body. **`abstract-depth` only.** |
| Nakasone 2014 (PMID 24891511) — HSP-modulation rescue in I1061T patient fibroblasts, directly relevant to the withdrawn arimoclomol arm | `is_open_access: false`. `abstract-depth` only. Its abstract does report *"In human fibroblasts carrying the I1061T mutation, adenovirus-mediated expression of Hsp70 or treatment with an HSP-inducer geranylgeranylacetone (GGA) increased the level of the mutant protein"* — which, if it held for WWOX, would point the **opposite** way to the repository's HSC70 concern. I am **not** promoting this; it is abstract-depth, a different chaperone axis, a different compartment, and a different protein. Flagged for a future full-text attempt. |
| Merrill 2019 (PMID 31511325), OP-puro original (PMID 22160674), and the Elsevier mitochondrial-labelling papers | All `is_open_access: false` on the one-call pre-test. Not attempted further. |
| Whether WWOX is N-glycosylated | Not checked against any primary source. Caveat 1 depends on it and is flagged as unverified `INFERENZA`. **This is a one-query check someone should do before Caveat 1 is relied on.** |
| Any cost figure from any source | None of the sources states a cost. All cost/time entries above are my own order-of-magnitude estimates, labelled `STIMA`. |
| Whether a WWOX antibody exists that works for **immunoprecipitation** from primary fibroblast lysate | Not checked. Rank 4 is unexecutable without it, and this is a cheap catalogue check that gates a ~10³–10⁴ EUR experiment. |

---

## 5 · What contradicts or qualifies something the repository currently asserts

1. 🔴 **Chloroquine as the lysosomal arm.** `DL-BIO-001` / `HYP-20260709-08` import CQ 40 µM + NH₄Cl 250 µM from an over-expression cancer-line experiment. Schultz 2018 shows, in primary patient fibroblasts on endogenous protein, that **chloroquine can be negative where bafilomycin A1 is strongly positive**. The repository's designed arm carries a false-negative risk it does not currently state. **Add bafilomycin A1.** *(Qualifies, does not overturn — CQ was positive in the CAL-62 system, and Schultz's own explanation is potency, not mechanism.)*
2. 🔴 **The step order of the `HYP-20260709-08` minimal experiment.** Pulse-chase at step 3 before inhibitor arms at step 4 is not executable on an undetectable band. Inhibitor-first.
3. 🟢 **"Stable-but-inert" is corroborated in a second, better matrix.** The repository holds this from P282A in an over-expressing thyroid-carcinoma line. Schultz 2018 demonstrates the same logic on **endogenous protein in primary patient fibroblasts**: *"neither one rescued cholesterol accumulation… the accumulating I1061T protein was non-functional."* The repository's insistence that the readout must be functional, not band intensity, is now supported by a primary-fibroblast instance, not only a transgene one. **This strengthens an existing position; it is not new.**
4. 🟡 **Branch (c) is harder in fibroblasts than the repository assumes.** `HYP-20260709-08` step 3 specifies solubility fractionation in donor-derived fibroblasts as though a negative would be informative. Koch 2011 shows a disease-relevant insoluble species that formed **only in patient neurons and not in the same patients' fibroblasts**. A negative solubility result in fibroblasts therefore **cannot** close branch (c) for the disease-relevant cell type. The caveat the repository already carries about tissue-specific stability now has a published instance behind it, and it applies to insolubility specifically, not only to turnover.
5. 🟡 **The CFTR paradigm is thinner than a reader might assume.** The repository cites Trikafta/CFTR-F508del in `TX-003`, `mechanism_intervention_map.md` and `proteostasis_rationale.md` as a therapeutic precedent. As a **measurement** precedent it largely does not transfer, because its power comes from glycan maturation and WWOX is cytosolic. `T7` in the SDR census already says *"Paradigm only"*; this file supplies the mechanistic reason.

---

## 6 · The minimal design this analysis supports

Stated as a design, not a recommendation, and conditional on donor-derived fibroblasts existing — which `DL-BIO-001` records only as *"la biopsia cutanea è una procedura diagnostica standard"*, i.e. feasible, not documented as available.

| Stage | Assay | Separates | `STIMA` cost / time |
|---|---|---|---|
| **1a** | WWOX Western at high load (~50 µg/lane), **soluble + pellet fractions blotted separately**, patient vs ≥2 healthy controls; qRT-PCR on the same cells | **(c)** from (a)+(b) | ~10¹ EUR · ~1 day on top of a blot already planned |
| **1b** | Inhibitor panel, same cells: **bafilomycin A1** (new) + chloroquine + NH₄Cl (lysosomal) · MG132 + epoxomicin (proteasomal, expected negative) · 3-MA (macroautophagy, negative) — with a viability control | **(b)** from (a)+(c) | ~10²–10³ EUR · ~2–4 weeks |
| **1c** | Permissive-temperature arm (~30 °C), no drug | **(b)+(c)** from (a) | ~10¹ EUR · ~1 week |
| **2** | Cycloheximide chase (60 µg/ml), started **from an inhibitor-accumulated pool**, not from baseline | quantifies (b) | ~10² EUR · ~1 week |
| **3** | **Only if 1a–1c are all negative:** pulse-label + WWOX IP (³⁵S or AHA-click) | measures (a) directly | ~10³–10⁴ EUR · ~1–3 months |
| **4** | **Mandatory whatever the outcome:** function, localisation and partner binding on any re-emerged protein — never band intensity | — | already specified in `HYP-20260709-08` step 5 |

Stages 1a, 1b and 1c share one cell expansion and largely one set of lysates. **That is the whole cost argument: the three cheapest arms together answer two of the three branches and leave the expensive one addressable by elimination.**

---

*Sources retrieved through the PubMed MCP tools. According to PubMed, the full texts read in this analysis are PMID 30202070 / [DOI 10.1038/s41467-018-06115-2](https://doi.org/10.1038/s41467-018-06115-2) and PMID 26780369 / [DOI 10.3791/53415](https://doi.org/10.3791/53415); abstract-depth findings are PMID 18216017 / [DOI 10.1074/jbc.M708735200](https://doi.org/10.1074/jbc.M708735200), PMID 24891511 / [DOI 10.1074/jbc.M114.549915](https://doi.org/10.1074/jbc.M114.549915), PMID 19305406 / [DOI 10.1038/nmeth.1314](https://doi.org/10.1038/nmeth.1314), PMID 22113611 / [DOI 10.1038/nature10671](https://doi.org/10.1038/nature10671), PMID 16563356 / [DOI 10.1016/j.bbrc.2006.02.170](https://doi.org/10.1016/j.bbrc.2006.02.170), PMID 35159129 / [DOI 10.3390/cells11030319](https://doi.org/10.3390/cells11030319). No PMID or DOI in this file was reconstructed from memory; every one was returned by a tool call in this session. No living researcher's contact details appear in this file.*
