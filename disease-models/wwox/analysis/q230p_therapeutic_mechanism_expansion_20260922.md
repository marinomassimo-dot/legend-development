# `Q230P` — therapeutic mechanism expansion: is increasing abundance coherent, and by what intervention class?

**Actor:** Scientist H · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Status:** 🔴 **NON-CANONICAL.** No registry, queue, ledger, receipt chain, state manifest or
`*_current.md` was written. No `BATCH_COMMIT`. No git command was run. One output file was created:
this one. It proposes; the Orchestrator verifies and lands.
**Nothing here is medical advice.** No molecule, dose, route, prognosis or safety claim is
recommended anywhere below, and no therapeutic recommendation follows from any of it.
**Genotype classes are held apart throughout.** `Q230P` ≠ `P47T` ≠ `P252A` ≠ `P282A` ≠ `G372R` ≠
`A141T` ≠ `L239R` ≠ `Gln353_Gln354del`. A measurement on one is never carried to another.
**Source classes are never merged:** `EXPERIMENTAL` · `HOMOLOGY` · `MODEL` · `INFERENCE` are labelled
at every point of use. Predicted coordinates are not experimental structure. A prediction is never a
measurement.
**This is the public edition and reasons about a WWOX-DEE reference genotype class, not an individual.**

---

## 0 · What I inherited and did not re-derive

Read first, in full or by section, before any act in this file:
[`q230p_structural_mechanism_20260922.md`](q230p_structural_mechanism_20260922.md) (Scientist B) ·
[`wwox_missense_stability_census_20260922.md`](wwox_missense_stability_census_20260922.md) (Scientist S) ·
[`function_per_molecule_assay_design_20260922.md`](function_per_molecule_assay_design_20260922.md) (Scientist D) ·
[`wwox_engagement_partner_adjudication_20260922.md`](wwox_engagement_partner_adjudication_20260922.md) (Scientist E) ·
[`p282a_control_tension_and_superscript_route_20260922.md`](p282a_control_tension_and_superscript_route_20260922.md) (Orchestrator) ·
[`gln353_gln354del_structural_adjudication_20260922.md`](gln353_gln354del_structural_adjudication_20260922.md) §§5, 9 (Orchestrator).

Additionally located by repository search during the mandatory novelty check, and treated as
**delta-defining prior art** rather than as something to rediscover:
[`proteostasis_discrimination_protocols_20260922.md`](proteostasis_discrimination_protocols_20260922.md) ·
[`proteostasis_rationale.md`](proteostasis_rationale.md) ·
[`mechanism_intervention_map.md`](mechanism_intervention_map.md) `TX-003` ·
[`wwox_sdr_function_per_molecule_census_20260921.md`](wwox_sdr_function_per_molecule_census_20260921.md) `T1`/`T5`/`T7`.

**Established, carried forward without re-derivation** (each is another actor's attestation, labelled
as theirs): `Gln230` SASA 0.00 Å², fully core-buried, helical, pLDDT 98.5, burial 83.8th percentile;
NOT interface (topology-independent exclusion), NOT cofactor site, NOT substrate pocket, NOT
solvent-exposed; φ(230) = −65.4° is already proline-compatible so **φ is not the lesion**, the
operative fact is the modelled Pro Cδ at **1.60 Å from Glu226 O — a 1.44 Å hard overlap** — plus
seven further clashes, with both accommodations (fraying, kinking) expensive and **no cheap escape**;
ESM2 ranks P worst of 19 at 230. `WWOX homodimerises via the SDR` is **`PREMISE: UNVERIFIED`**.
ΔΔG is **anti-correlated** with every WWOX measurement that exists, so `Q230P`'s +1.514 carries no
evidential weight. Turnover, solubility and aggregation are `PREMISE: NOBODY_LOOKED` for every WWOX
allele. No purified folded WWOX SDR protein exists; heterologous expression reported ≥2× with
activity in crude extract only. `P252A`'s route is lysosomal, MG-132-negative, HSC70-positive, `t½`
never reported, ClinVar **Benign**. Both `Q230P` data points are `abstract-depth` from a body nobody
here has read. `Q230P` is the most recurrent WWOX allele of any class — **8 patients / 6 families** —
and is not a cryptic splice allele.

---

## 1 · PROSPECTIVE DISCOVERY TRACE

> 🔴 **Persisted at 2026-09-22, BEFORE any confirmatory external search was run.** The only searching
> that preceded it was the mandatory repository novelty check (`FIND ISSUE → SEARCH CLAIMS → SEARCH
> CANDIDATES → SEARCH DISCOVERY LEDGER`), whose result is recorded in §1.9 and which was run to avoid
> re-deriving prior art, not to confirm a hypothesis. Nothing below was edited after the searches;
> **RESULT** (§1.7) and the grading in §1.8 were appended, and where a prediction failed it is
> recorded as failed rather than rewritten.

### 1.1 OBSERVATION

A buried, mid-helix, zero-SASA glutamine in the SDR core is replaced by proline. The backbone torsion
is already proline-friendly, so the textbook "proline breaks helices because φ is wrong" explanation
**does not apply here** — yet the substitution still forces a 1.44 Å hard steric overlap between the
proline Cδ and the i−4 carbonyl oxygen that the wild-type amide hydrogen donates to, and there is no
nearby coil to absorb the strain. Meanwhile the only protein-level observation in the patient is
**normal transcript, protein not detected on one Western** — an *abundance* endpoint whose three
possible causes (reduced translation, accelerated turnover, insolubility) have **never been
separated**, for this or any WWOX allele. And the one WWOX missense protein whose function was
measured at normal abundance (`P282A`) was **functionally dead while stable**.

**The observation that actually generates this trace is the mismatch:** the structural analysis says
"this is a folding lesion" with unusual specificity, while the therapeutic question being asked —
*should we raise abundance?* — depends on a property (does a useful fold exist at all, at any
abundance?) that **no structural analysis can supply and nobody has measured**.

### 1.2 DIVERGE — seven mechanistically distinct explanations, not paraphrases

Each is distinguished by **where in the protein's lifetime the lesion acts** and **what rescue
variable, if any, could change the outcome**. Two of them predict a *normal* abundance, which is why
they are not paraphrases of the other five.

| # | mechanism | where it acts | rescue variable it implies |
|---|---|---|---|
| **D1** | **Co-translational folding-yield ceiling.** The nascent chain cannot reach a foldable state; ribosome-associated QC triages it before a native-like species ever exists | during synthesis | none post-hoc; only a change to the folding landscape *while the chain emerges* (cofactor availability, ribosome speed, Hsp70/NAC capacity) |
| **D2** | **Post-folding accelerated turnover of a marginally-folded species.** The protein does reach a native-like fold, is thermodynamically marginal, exposes a degron, is cleared — the `P252A` shape at a different residue | after folding | classical stabiliser or degradation-route inhibitor; the textbook chaperone case |
| **D3** | **Insolubility / kinetic partitioning into an off-pathway aggregate**, invisible on a soluble-lysate Western; abundance is *apparently* zero while protein mass is in the pellet | during or after folding | aggregation suppression; 🔴 **raising synthesis here is harmful, not neutral** |
| **D4** | **Cofactor-coupled folding deficit.** If the SDR's stable species is the **holo** form, the folding reaction is a *ligand-binding* reaction, and a core lesion 12.6 Å from the cleft can fail specifically at the cofactor-capture step while the apo intermediate is degraded | folding, cofactor-dependent | a cleft-binding ligand or raised intracellular cofactor — **a different intervention class from D2's generic chaperone, at a site the lesion does not touch** |
| **D5** | **Detection-floor / epitope artefact.** "Protein not detected" is a floor, not a zero; if the antibody epitope overlaps the distorted 226–240 segment, a conformational or epitope loss could mimic absence at near-normal abundance | in the assay, not the protein | none — the whole abundance axis would be moot and the question changes |
| **D6** | **Kinked-helix alternative native state.** The chain accommodates the proline by kinking, displacing 231–240 into a remodelled but stably folded core — a folded, soluble protein with a rearranged interior | folding, resolved | none needed for abundance; the lesion, if any, is functional |
| **D7** | **Function-dead by helix propagation, independent of abundance.** Asn232 sits 5.82 Å from the cofactor-cleft axis, two residues from the helix a proline at 230 must distort — a restabilised `Q230P` could be abundant and inert: the `P282A` outcome reached by a different road | after folding | 🔴 **none that abundance can supply.** This is the branch that makes the whole boost axis futile |

🔴 **D5, D6 and D7 are the three that the brief's chaperone framing would skip**, and they are the
three that decide whether the first prerequisite (*protein can adopt a useful fold*) holds. D5 and D6
predict the abundance premise is **wrong**; D7 predicts the abundance premise is **right and
irrelevant**.

### 1.3 CONNECT — four adjacent biological domains

| domain | what it is being asked for | why it is adjacent, not decorative |
|---|---|---|
| **C1 · SDR / HSD enzymology and cofactor-assisted folding** | Whether NAD(P)(H) acts as a *folding* ligand in SDRs — apo unstable, holo stable — and whether disease missense in SDRs is rescued by cofactor rather than by chaperone | The Rossmann dinucleotide-binding motif is the **first** structural element to form in many NAD-binding folds; if that holds for SDRs, folding and cofactor capture are one reaction, and D4 becomes a real mechanism instead of a speculation |
| **C2 · Proline substitutions in structured regions across disease genes** | The *general* answer to "what happens when a buried helix residue becomes proline" — degradation, aggregation, or neither — and with what frequency | This is the class `Q230P` belongs to, and it is the only class-level empirical evidence available, since no WWOX measurement exists |
| **C3 · Pharmacological-chaperone practice (Fabry/migalastat, PKU/sapropterin, TTR/tafamidis, CF/correctors)** | The **entry criteria** the field itself uses to decide a variant is "amenable", and specifically whether amenability is scored on abundance or on activity | The field has already made this exact mistake and corrected it; its correction is the entry criteria in Task 4 |
| **C4 · Variant-abundance atlases (VAMP-seq, Parkin/`PTEN` abundance maps, 29–30 °C arms)** | Method transfer only: how a low-abundance variant class is separated from a low-function variant class **at scale**, and what that literature found about the correlation between the two | It supplies the *measurement architecture* for "keep abundance and function apart" — and the honest base rate for how often abundance rescue implies function rescue |

### 1.4 HYPOTHESIS

> **`Q230P` is a FOLDING lesion whose therapeutic coherence is gated not by whether protein can be
> accumulated, but by whether a cofactor-competent fold can be completed — and the correct
> intervention class is therefore NOT a generic proteostasis regulator but, if anything, a
> cleft-directed ligand-assisted folding strategy, which WWOX cannot currently support because its
> cofactor binding has never been demonstrated.**

Stated as the mechanistic class asked for: **`FOLDING`, with `STABILITY/DEGRADATION` as the expected
*consequence* rather than the primary lesion, `AGGREGATION/INSOLUBILITY` not excluded, and
`COFACTOR/CATALYTIC DEFECT` entering by an indirect, propagation route (D7) rather than as a direct
lesion.** The honest composite label if the evidence does not separate these is **`MIXED`**, and if
the first prerequisite cannot be tested at all it is **`UNRESOLVED`**.

🔴 **The hypothesis is deliberately constructed so that it can lose.** It loses if (a) the SDR
literature does not support cofactor-coupled folding, in which case D4 collapses and the answer
reverts to plain D2/D3; (b) proline-in-core substitutions in SDRs turn out to aggregate rather than
degrade, in which case D3 dominates and the boost axis is dangerous; or (c) `P282A` turns out to be a
common allele that is not function-dead, in which case the repository's standing proof that
"stable-but-inert" is real weakens and D7 loses its only empirical anchor.

### 1.5 EX-ANTE PREDICTION — if the hypothesis is true, what else should we observe?

Written before the searches. Each is falsifiable by a literature observation, not by an opinion.

| # | prediction | what would falsify it |
|---|---|---|
| **P1** | In the SDR/HSD family, buried-core missense causes **low steady-state protein with normal mRNA**, cleared by a QC route, and is **temperature- or chemical-chaperone rescuable in at least some instances** | SDR core missense reported as normally abundant but inactive, as the family default |
| **P2** | **Cofactor (NAD(P)(H)) will be documented as a stabilising / folding ligand for SDR-family or Rossmann-fold enzymes**, with an apo-vs-holo stability difference reported somewhere in the family | No apo/holo stability distinction reported; cofactor treated purely as a substrate-cycle reagent |
| **P3** | **Aggregation in the SDR family will remain interface-associated**, i.e. a search for *core* SDR missense aggregation comes back thin or negative — corroborating §7.1's class assignment rather than merely repeating it | Core SDR substitutions reported to aggregate, which would move D3 to the front and turn the boost axis red |
| **P4** | **`rs3764340` will be a common allele** (appreciable MAF, homozygotes observed), which is incompatible with `P282A` being a complete null for a tumour suppressor | A rare allele (MAF ≪ 1%, no homozygotes), which would rehabilitate `P282A` as a strong negative |
| **P5** | In the pharmacological-chaperone literature, there will be **documented instances where abundance was restored and function was not** — i.e. the field's own base rate says abundance rescue ≠ function rescue | Every reported chaperone rescue restores function proportionally to abundance |
| **P6** | Proline substitutions specifically (as opposed to missense generally) will be **over-represented among severe/degraded alleles** and **under-represented among chaperone-rescuable ones**, because a proline lesion is a backbone lesion and a bound ligand cannot restore a backbone hydrogen bond | Proline substitutions reported as routinely chaperone-rescuable at the same rate as side-chain substitutions |

### 1.6 DISCRIMINATOR

**For the mechanism class:** the single discriminator that separates D1/D2/D3 is **where the protein
mass is and whether it can be made to appear** — a solubility split plus an accumulation arm on the
same lysate. It cannot separate D6/D7, which need a function readout at matched abundance.

**For the therapeutic question, which is the question actually asked:** the discriminator is not a
mechanism assignment at all. It is **the coupling coefficient between abundance and engagement** —
i.e. whether ∂(engagement)/∂(abundance) for `Q230P` is the wild-type slope or zero. That single
quantity answers "is increasing abundance therapeutically coherent" **without** requiring the
mechanism to be named first, which is why it, not the mechanism label, is the object of §8.

🔴 **The trap this discriminator is designed to avoid:** every mechanism label in the brief's list is
compatible with *both* therapeutic answers except `AGGREGATION` (always no) and a pure abundance-only
lesion (always yes). **Naming the mechanism is therefore not sufficient to answer the therapeutic
question, and a file that names the mechanism and stops has not done the task.**

### 1.7 RESULT

*(Appended after the searches of §§2–4. Predictions that failed are recorded as failed.)*

→ **See §6.4.**

### 1.8 NOVELTY ORIGIN — graded honestly, and mostly low

| element | grade | justification |
|---|---|---|
| The chaperone hypothesis itself | 🔴 **`PROMPT-SEEDED`** | The brief handed it to me, named it, and told me not to start with it. It is not my idea and is not graded as one |
| The abundance/function dissociation, `P282A` as its proof | **`REDISCOVERY`** | Standing in the repository since `discovery_ledger_current.md:1104`; restated, not found |
| The three-cause decomposition of "protein not detected" | **`REDISCOVERY`** | `HYP-20260709-08` and Scientist S's census both carry it |
| Proline-in-SDR as a *class* question | **`CROSS-DOMAIN-DERIVED`** | Assigned by the brief as Task 2; the answer is transferred from outside WWOX |
| **D4 — cofactor-coupled folding as a distinct mechanism and a distinct intervention class** | 🟡 **`AGENT-NOVEL`, provisionally, pending §3** | Repository novelty check: `cofactor-assisted` 0 files, `cofactor-mediated` 0 files, `holoenzyme` 0 files, `apo/holo` 1 file (and that one is a *crystallography* mention in a deorphanisation protocol, not a folding claim). The repository holds migalastat as an **active-site ligand** paradigm (`TX-003`, `T5`) but **not** cofactor-as-folding-chaperone. 🔴 **Downgrade to `CROSS-DOMAIN-DERIVED` if the SDR literature already states it** — which is exactly what P2 tests |
| **D5 — epitope/detection-floor as a competing explanation of the `Q230P` Western** | 🟡 **`AGENT-NOVEL`, weak** | `PREMISE: DETECTION_FLOOR` exists (`CLAIM 030`) but is about *sensitivity*; the **epitope-overlap** variant of it — that the antibody's epitope may sit in the very segment predicted to distort — is not in the repository. ⚠️ It is also cheap to overstate, and it is graded weak because it may simply be untestable without knowing the antibody |
| **The coupling-coefficient framing of the discriminator** (§1.6) | 🟡 **`AGENT-NOVEL`, methodological only** | Scientist D's design already measures the two quantities; the contribution is the argument that **the ratio, not the mechanism label, is the therapeutic answer** — a reframing of an existing design, not a new experiment. Graded as methodological, not scientific, novelty |
| Everything in §§2–5 | **`CORPUS-DERIVED`** | Retrieved from literature in this act |

### 1.9 CANONICAL STATUS

🔴 **`DISCOVERY` — non-canonical throughout.** Not a `CANDIDATE`, not `CANONICAL`, not a commit
candidate. Nothing in this file is proposed for `BATCH_COMMIT`. D4 and D5 are **hypotheses**, not
claims; neither has an experimental observation behind it and both are labelled `IPOTESI` wherever
used below. The repository pre-search (`FIND ISSUE → SEARCH CLAIMS → SEARCH CANDIDATES → SEARCH
DISCOVERY LEDGER`) was run before this trace was written and is reported in §1.8 rather than
asserted.

### 1.10 EXPERIMENT — smallest, highest information gain, with compression stated

Written prospectively; the post-search refinement is §7 and the single best discriminator is §8.

> **One lysate set, one plate, three channels.** Take the existing donor-saturation architecture
> (Scientist D §3, Scientist E §4) and run it once with `Q230P`, `WT`, `P282A`, `P252A` under a
> **single** abundance-raising lever, reading **abundance (donor luminescence)**, **engagement per
> molecule (fitted BRET<sub>max</sub>)** and, on the same lysates, **the soluble/insoluble split** —
> then compute one number: **the ratio of the `Q230P` engagement slope to the `WT` engagement slope
> across the induced abundance range.**

**Compression, stated explicitly:** one measurement separates D1 (no donor signal at any induction),
D2 (signal appears under the lever, slope = WT), D3 (signal appears but mass is in the pellet), and
D6/D7 (signal present, slope ≈ 0). **Four mechanisms, one plate.** The measurements deliberately
*not* included: no CHX chase (cannot chase an undetectable band — `proteostasis_discrimination_
protocols_20260922.md` Caveat 2), no pulse-label (only reachable by elimination and 10³–10⁴ EUR), no
MD, no docking, no purified protein (none exists), no ±UV arm in the first pass (it collides with the
abundance levers — Scientist E's `D-2`).

---

## 2 · `rs3764340` — RESOLVED, with numbers, in three ancestries

> ## 🟢 **RESOLVED. `rs3764340` is a COMMON polymorphism. Control-group minor-allele frequency 4.2 %–8.6 % depending on ancestry, and — the decisive number — 18 homozygous `GG` (= homozygous `P282A`) individuals were enrolled as HEALTHY ADULT CONTROLS across two studies I read first-hand.**
>
> ## ⇒ Classification: 🔴 **`OVEREXPRESSION-ARTEFACT SUSPECT`.**

🔵 **Attribution.** All bibliographic records, abstracts and the two full texts in §2.2 were retrieved
**from PubMed / PubMed Central** in this act; §2.3's passages were retrieved through
**`Scholar_Gateway semanticSearch`**. Every referenced article carries its DOI at the point of use.
**No PMID, PMCID, DOI or frequency below was reconstructed from memory** — each was returned by a
tool call in this session, and the one remembered-looking number in the whole section (dbSNP's
Caucasian MAF) is presented **as a quotation of a primary paper quoting dbSNP**, not as my own
lookup, because my own lookup was blocked (§2.1).

### 2.1 Every route attempted, and what each returned

| # | Route | Result | Evidence for the result |
|---|---|---|---|
| 1 | **gnomAD** (`gnomad.broadinstitute.org`, `api.gnomad.broadinstitute.org`) | 🔴 **BLOCKED** | HTTP `000`; proxy status names it: `connect_rejected`, *"gateway answered 403 to CONNECT (policy denial or upstream failure)"* |
| 2 | **dbSNP / NCBI E-utilities** (`eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`) | 🔴 **BLOCKED** | same, `connect_rejected` |
| 3 | **Ensembl REST + FTP** (`rest.ensembl.org`, `ftp.ensembl.org`) | 🔴 **BLOCKED** | same, `connect_rejected` |
| 4 | **Allowlist control** (`example.com`) | 🔴 `000` | 🟢 **The control behaves exactly as the brief predicts — this is the allowlist, not a transient failure.** `TOOL_BLOCKED → PARK ROUTE → CONTINUE` |
| 5 | **ClinVar — LOCALLY HELD, not blocked** | 🟢 **RETURNED** | `analysis/data/WWOX_clinvar_all_variants.csv` |
| 6 | **PubMed `rs3764340`** | 🟢 **9 records** | `query_translation: "rs3764340"[All Fields]` — a full expansion, not a `[UID]` misfire |
| 7 | **PubMed Central full text of the open-access members of that set** | 🟢 **RETURNED, with genotype-count tables intact** | §2.2 |
| 8 | **`Scholar_Gateway semanticSearch`** on the association literature | 🟢 **RETURNED, including the European control frequency and dbSNP's own Caucasian value** | §2.3 |

🔴 **Four of eight routes are blocked and none of them was retried.** 🟢 **And the blocks did not stop
the question**: the frequency was obtained at higher resolution than a gnomAD popmax would have
given, because a primary case–control table supplies **genotype counts**, which is what the argument
actually needs, and gnomAD would have supplied only an allele frequency.

### 2.2 The hard numbers — control-group genotype counts, read first-hand from PMC

According to PubMed, both tables below are from the **healthy-control arms** of case–control studies
whose bodies I retrieved from PMC in this act.

**(a) Cheng *et al.* 2016, oral squamous cell carcinoma, Taiwan** — PMID 27655721, PMC5342485,
*Oncotarget* 7(43):69384–96, [DOI](https://doi.org/10.18632/oncotarget.12082). **Controls N = 1199**,
verbatim from Table 3:

> *"rs3764340 · CC 1016 (84.7%) · CG 173 (14.4%) · **GG 10 (0.9%)** · CG+GG 183 (15.3%)"*

and, verbatim, *"In these controls, the genotypic frequency of … rs3764340 … **were in the
Hardy-Weinberg equilibrium** (p = 0.383, χ² value: 0.759)."*

**(b) Lee *et al.* 2017, hepatocellular carcinoma, Taiwan** — PMID 28426730, PMC5398630, *PLoS ONE*
12(4):e0176141, [DOI](https://doi.org/10.1371/journal.pone.0176141). **Controls N = 708**, verbatim
from Table 2:

> *"rs3764340 · CC 594 (83.9%) · CG 106 (15.0%) · **GG 8 (1.1%)** · CG+GG 114 (16.1%)"*

**My arithmetic on those two published tables** (`INFERENCE` from `EXPERIMENTAL` counts — the counts
are theirs, the division is mine):

| cohort | N | CC | CG | **GG** | G alleles / total | **MAF(G)** | homozygote rate |
|---|---|---|---|---|---|---|---|
| Cheng 2016 controls | 1199 | 1016 | 173 | **10** | 193 / 2398 | **8.05 %** | 1 in 120 |
| Lee 2017 controls | 708 | 594 | 106 | **8** | 122 / 1416 | **8.62 %** | 1 in 89 |
| **pooled** | **1907** | 1610 | 279 | **18** | 315 / 3814 | **8.26 %** | **1 in 106** |

### 2.3 Ancestry variation — and dbSNP's own number, quoted through a primary source

Retrieved through `Scholar_Gateway semanticSearch`; passage text is the evidence, the tool's
`ai_generated` summary is not and was not used.

**Cancemi *et al.* 2011, differentiated thyroid carcinoma, Pisa, Italy** — PMID 21520031,
*Int J Cancer* 129(12):2816–24, [DOI](https://doi.org/10.1002/ijc.25937). 1741 cases / **1042
controls**, verbatim from Results:

> *"The genotype frequencies were in Hardy-Weinberg equilibrium both among cases (p = 0.257) and
> among controls (p = 0.135) … The frequency of the G-allele was 0.062 in cases and **0.044 in
> controls, which is remarkably similar to that reported in dbSNP for Caucasians (0.042)**."*

🟢 **This is dbSNP's own Caucasian MAF — 0.042 — reaching this file by quotation rather than by
lookup, because the lookup route is blocked.** ⚠️ **Its correct label is `abstract/body-quoted
secondary value`, not a first-hand database query**, and it is used only where an order of magnitude
is what the argument needs.

| population | source | control MAF(G) | homozygotes |
|---|---|---|---|
| **Caucasian (dbSNP, quoted)** | Cancemi 2011 | **0.042** | — |
| **Italian controls, n = 1042** | Cancemi 2011 | **0.044** | HWE p = 0.135 (all three genotype classes modelled) |
| **Southern + Eastern Han Chinese, n = 1679 controls** | Huang *et al.* 2012, *Mol Carcinog*, [DOI](https://doi.org/10.1002/mc.21934) — verbatim: *"the frequency of variant G allele was significantly higher in cases than controls (**0.082 vs. 0.067**)"*; *"rs3764340 GC/GG risk genotypes (which occurred at a frequency of **12.7 % in the controls**)"* | **0.067** | carrier rate 12.7 % |
| **Northern Han Chinese, n = 596 controls** | Guo *et al.* 2013, *Environ Mol Mutagen* 54(2):112–23, PMID 23197378, [DOI](https://doi.org/10.1002/em.21748) — verbatim: *"The GG genotype of rs3764340 was very rare (**1.0 % in controls**, and 1.6 % in GCA cases)"*; CC 523 (87.8 %) / CG+GG 73 (12.2 %) | ≈0.066 | GG 1.0 % |
| **Northern Han Chinese, ESCC control arm** | Guo *et al.* 2013, *Mol Carcinog* 52(4), PMID 22213016, [DOI](https://doi.org/10.1002/mc.21853) — negative-family-history controls: CC 496 (87.8) / CG 63 (11.2) / **GG 6 (1.0)** | ≈0.066 | GG 6 |
| **Taiwanese Han, n = 1907 controls** | §2.2 | **0.083** | **GG 18** |
| **Taiwanese Han, n = 316 controls** | Su *et al.* 2018 cervical, PMID 30013442, [DOI](https://doi.org/10.7150/ijms.25553) — *"conformed to Hardy-Weinberg equilibrium in the normal controls [p = 0.720, χ² value: 0.13 < 5.99, **degree of freedom = 2**]"* 🔵 **df = 2 requires all three genotype classes** | — | present |

**Range: MAF 4.2 %–8.6 %. Expected homozygote frequency q²: 0.18 % (European) to 0.74 % (Taiwanese).**

### 2.4 The classification, and the argument that forces it

🔴 **The decisive observation needs no population statistic and no extrapolation: 18 individuals
homozygous for `P282A` were recruited, genotyped and reported as HEALTHY ADULT CONTROLS in two
studies whose tables I read.** They were enrolled *because* they were cancer-free adults. A complete
functional null of `WWOX` does not reach cancer-free adulthood — WWOX-DEE is an ultra-rare, severe,
biallelic disorder whose per-allele patient counts in this repository are single digits.

Three further, independent lines point the same way:

1. 🔴 **The genetic model that corresponds to the functional experiment is the one model that is
   NULL.** The functional claim was made on a **biallelic** construct. The meta-analysis
   (Yang *et al.* 2018, PMID 29662317, PMC5892619, *OncoTargets Ther* 11:1657–65,
   [DOI](https://doi.org/10.2147/OTT.S152140); 8 studies, **6177 cases / 6606 controls**) reports
   the heterozygous and dominant and allele models as significant but modest — *"CG vs CC: OR = 1.31,
   95% CI: 1.12–1.53 … GG/CG vs CC: OR = 1.31 … G vs C: OR = 1.28"* — and the **homozygous and
   recessive models as NOT significant**: *"GG vs CC: OR = 1.36, 95% CI: **0.90–2.04** … GG vs CC/GC:
   OR = 1.30, 95% CI: **0.88–1.93**."* **Homozygous `P282A` carries no demonstrated excess risk even
   of cancer**, let alone of a developmental encephalopathy.
2. 🔵 **The repository's own n = 1 human says the same thing.** Zhang 2025's proband was **homozygous
   for `P282A` and homozygous for `P252A`** and, verbatim from that body,
   *"did not suffer from WWOX-related nervous system disease"* at 35 — with the authors' own reading,
   *"WWOX and WWOX mutants may have some residual protein function to maintain the development of the
   neurological system."*
3. 🟢 **ClinVar agrees, and it is held locally rather than blocked.** `VCV000260745`,
   `NM_016373.4(WWOX):c.844C>G (p.Pro282Ala)` → **`Benign`**, *"criteria provided, multiple
   submitters, no conflicts"*, last evaluated **2026-02-03**, asserted against *Autosomal recessive
   spinocerebellar ataxia 12* and *Developmental and epileptic encephalopathy 1 / 28*. ⚠️ **A ClinVar
   classification is a clinical-assertion aggregate, not an allele frequency**, and it is cited here
   as corroboration of the direction, not as the frequency.

**Why `OVEREXPRESSION-ARTEFACT SUSPECT` and not one of the other three labels:**

| label | verdict | reason |
|---|---|---|
| `VALID STRONG NEGATIVE` | 🔴 **EXCLUDED** | 18 healthy adult homozygotes; null recessive model; ClinVar Benign. A complete function-dead anchor cannot be carried by ~1 % of a population |
| `PARTIAL-LOSS CONTROL` | 🔴 **NOT AVAILABLE** | To call it a partial-loss control you must state the magnitude of the partial loss. **Nobody has measured `P282A`'s function at physiological abundance in any system.** The only functional readout is an all-or-nothing overexpression rescue reported as *"indistinguishable from empty vector"* — which supplies no graded value to calibrate against. Assigning this label would assert a measurement that does not exist |
| **`OVEREXPRESSION-ARTEFACT SUSPECT`** | 🟢 **ASSIGNED** | The entire "complete loss" claim rests on **CMV-driven Flag-tagged transgene rescue in WWOX-deficient cancer lines** — colony formation, viability, invasion, wound healing, xenograft, comet, γH2AX and an I-SceI/EJ2GFP reporter — i.e. a **supraphysiological gain-of-function rescue assay with no matched-abundance arm and no dose–response**. Its readout is incompatible with the population genetics. *Suspect*, not *disproved*: the assays were real and internally controlled |
| `UNRESOLVED` | 🔴 **NOT APPLICABLE** | The frequency question resolved. Refusing to classify here would be the opposite error from forcing resolution |

### 2.5 🔴 A third reconciliation the brief's list does not contain, and it is testable

The brief offered three reconciliations: (i) the assay overstates, (ii) a mild hypomorph read as
complete, (iii) the two literatures measure different things. **Two independent bodies I read this
session name a fourth possibility that is a sharpened (iii), and it has a mechanical consequence for
the assay.**

Huang 2012 (*Mol Carcinog*, [DOI](https://doi.org/10.1002/mc.21934)), verbatim:

> *"bioinformatics analysis showed that the rs3764340 C>G belongs to **ESE** which usually enhance
> pre-mRNA splicing. Therefore, it is conceivable that rs3764340 C>G variation **may induce the
> selective splicing in exon 8 and increase the incidence of deletion of exon 8**."*

and Yang 2018 (PMC5892619) repeats it: *"rs3764340 C>G is an **exonic splicing enhancer** … this SNP
may enhance the selective splicing in exon 8, leading to a high incidence of deletion of the exon."*

🔴 **If any part of `rs3764340`'s real effect is exonic-splicing-enhancer-mediated, then a cDNA
expression construct — which has no introns — CANNOT reproduce it, while it simultaneously
exaggerates any protein-structural effect by overexpression. The functional assay and the
association literature would then be measuring two different lesions of the same nucleotide.**

⚠️ **Bounds, stated before anyone leans on this.** Both statements are **`MODEL` / bioinformatics
prediction** (SNPinfo web server), **not a measurement**; no minigene, no RT-PCR, no RNA-seq of
exon 8 in a `G`-allele carrier is reported in either body. Its correct label is `PREMISE:
NOBODY_LOOKED`. It is recorded here because it is **cheap to test and it changes the interpretation
of the control**, not because it is established. 🔴 **And it must not be carried to `Q230P`**, which
is `c.689A>C` in exon 7 and has already been excluded as a cryptic-splice allele by another actor.

### 2.6 🔴 What this does to the recommended assay — a correction, not a demolition

Scientist D's design (§3.2, §3.4) and Scientist E's adjudication (§4.1) both give `P282A` the job of
**the go/no-go gate**: it *"must read engagement-dead at normal donor signal"*, and *"if it does not,
the assay is not sensitive to the lesion class and nothing else on the plate means anything."*

🔴 **That gate can no longer bear that weight, and the reason is not the label — the label is
verified — but the calibration.** Concretely:

- 🟢 **`P282A` keeps its place on the plate.** It remains the only WWOX readout in the literature
  reported to fail in a missense protein with no measured stability defect (criterion C6), and
  Scientist E label-verified that on five surfaces. **Nothing here retracts that.**
- 🔴 **What it loses is the entitlement to license the inference *"our assay can detect a functionally
  dead but stable WWOX protein."*** If `P282A` retains enough physiological function that ~1 % of a
  population is homozygous and healthy, then either the `POLE4` engagement loss is **condition-
  specific** (it was measured **only after UV**, per Scientist E's `D-2`), or **overexpression-
  specific**, or **real but not the function that matters**. All three leave the gate uncalibrated.
- 🟢 **The fix is one sentence in the protocol, not a new experiment:** `P282A` is demoted from
  *"complete-null go/no-go gate"* to **"an engagement-reduced reference point of unstated
  magnitude,"** and the plate's claim to sensitivity must come from a **graded** control instead —
  which §7 supplies.
- 🔴 **`L404A` cannot silently inherit the vacated job.** Scientist E's `D-4` already states why: its
  own abundance was never reported, so an engineered loss-of-binding control whose abundance is
  unmeasured is not an abundance-independent anchor either.

---

## 3 · Proline substitution inside a structured SDR region — cross-domain findings

> 🔴 **EVERY ROW BELOW IS TRANSFERRED. NOT ONE DATUM IS ABOUT WWOX.** A **method** and a **mechanism
> class** can transfer; a **disease conclusion** cannot. Each row states `WHAT TRANSFERS` and
> `WHAT DOES NOT` separately, and where the row is `abstract-depth` it says so.

**Queries and their expansions, recorded because a PubMed zero lies in six ways.** The SDR/proline
block expanded fully — `"short chain dehydrogenase reductases"[Supplementary Concept] OR … OR
"hydroxysteroid dehydrogenases"[MeSH Terms] … AND ("proline"[MeSH Terms] …) AND ("misfolding" OR
"degradation" OR "instability")` — **7 records, no term silently dropped** (checked term by term in
the returned `query_translation`), and the **positive control fired**: the set contains `HSD11B2`,
the gene the repository's own § 7 fold-family table already carries. Where I used
`Scholar_Gateway semanticSearch`, the **passage text is the evidence and the `ai_generated` summary
is not**, and was not used.

### 3.1 🥇 THE DIRECT HIT — proline substitution engineered into an SDR, measured both ways

**Lou *et al.* 2018**, *Clostridium absonum* **7α-hydroxysteroid dehydrogenase (CA 7α-HSDH)** — an
SDR. PMID 29141528, *Protein Pept Lett* 25(3):230–235,
[DOI](https://doi.org/10.2174/0929866524666171113113100). `abstract-depth`; the abstract is
unusually complete (it carries Methods and per-mutant results). Verbatim:

> *"The two mutants, **A104P and G105P** were prepared by over-lapping PCR … Thermostability was
> measured by circular dichroism (CD) spectrometer … **thermostability of the two mutants, A104P and
> G105P (in the coil between βD and αD) resulting from the proline substitution method decreased
> significantly** … activity of the five mutants, P124L, A125L, N171L, **A104P and G105P cannot be
> detected** … **CA 7α-HSDH may suffer structural destruction resulting from the proline substitution
> in A104 and G105.**"*

🔴 **This is the opposite of what the engineering literature predicts, and that is the finding.**
"Proline substitution" is a standard *rational thermostabilisation* method — it works by lowering the
configurational entropy of the unfolded state, and it is deliberately applied **at coils and turns**,
the site class most tolerant of a proline. Here it was applied at exactly that favoured site class,
in an SDR, and it **lowered** Tm **and** abolished detectable activity.

| | |
|---|---|
| **WHAT TRANSFERS** | 🟢 **In the SDR fold, introducing a proline is not benign even where theory says it should be**, and the phenotype observed was **combined** — thermostability down **and** activity undetectable, not one or the other. 🟢 And a **method**: CD thermal melt on purified protein as the primary stability readout, paired with a specific-activity assay on the same preparation, is the minimal two-channel design that keeps stability and function apart. |
| **WHAT DOES NOT** | 🔴 Bacterial enzyme, **engineered** not disease, **different position**, **different site class (coil, not mid-helix)**, GST-fusion purified protein, **and no cellular abundance, turnover, solubility or aggregation measurement of any kind**. 🔴 It says nothing about `Q230P`, and nothing about whether a proline in a **helix** behaves as a proline in a **coil** — indeed the whole point is that the tolerant site class was **not** tolerant, which is an argument about SDRs, not an argument about helices. 🔴 `abstract-depth`; no body read; no receipt claimed or owed. |

### 3.2 🔴 THE SECOND FINDING IN THE SAME ABSTRACT, AND IT IS THE ONE WITH THERAPEUTIC TEETH

Same body, verbatim:

> *"**most of the mutations in β-sheet core predicted by MAESTRO became more stable than wild type,
> unfortunately, all the mutations suffered dramatic activity loss.**"*

and

> *"**Although all the mutants' activities decreased**, the mutant L197E with the maximum activity
> retain suggested that the loop structure (residues 194 to 211) may be the favored candidate sites
> to enhance thermostability."*

🔴 **In an SDR, deliberately stabilising the core by design produced protein that was MORE STABLE AND
FUNCTIONALLY DEAD — in essentially every mutant tried.** The best case retained **28.7 %** of
catalytic efficiency; five mutants had **no detectable activity**.

| | |
|---|---|
| **WHAT TRANSFERS** | 🔴 **The `P282A` pattern — "stable but inert" — arrives independently from the SDR fold family, as the DEFAULT rather than the exception, whenever the core is perturbed.** This is a direct, experimental, fold-matched hit on the third chaperone prerequisite (*stabilisation can increase functional protein*): in this fold, **stability and activity moved in opposite directions**. 🟢 It also supplies the reason: an SDR core is not inert scaffolding — it positions the catalytic tetrad and the cofactor cleft, so anything that changes core packing changes the active site. **That is the fold-family form of Scientist B's own Asn232 propagation route (§9 item 4), and it arrives by a completely independent road.** |
| **WHAT DOES NOT** | 🔴 These are **engineered stabilising substitutions**, not a **ligand** binding a pre-formed site; a pharmacological chaperone does not mutate the core. So this does **not** show that a small-molecule stabiliser would kill an SDR — it shows that *changing core packing* does. 🔴 Bacterial, purified, `abstract-depth`, and every activity number is on **this** enzyme's own substrate, which WWOX does not have. |

### 3.3 Disease-associated proline substitutions in human SDR/HSD genes

According to PubMed:

| gene · variant | fold | what was observed | class | source · depth |
|---|---|---|---|---|
| **HSD3B2 `A82P`** (3β-HSD2) | SDR/HSD | Homozygous, salt-wasting 3βHSD deficiency with ambiguous genitalia. *"Alanine is a conserved amino acid in the membrane binding domain of the enzyme and **proline substitution was predicted to destabilize the protein**"* | 🔴 **`MODEL` only — "predicted", no measurement** | Rabbani 2012, PMID 22579964, [DOI](https://doi.org/10.1016/j.gene.2012.04.080), `abstract-depth` |
| **HSD3B2 `P222Q`** | SDR/HSD | Homozygous, CAH. Homology modelling *"emphasizes codon 222 as an important residue for the **folding pattern** of the enzyme"* | 🔴 **`HOMOLOGY`/`MODEL` only.** ⚠️ **Reverse direction** — a native proline removed | Lusa 2010, PMID 21340167, [DOI](https://doi.org/10.1590/s0004-27302010000800018), `abstract-depth` |
| ⭐ **HSD11B2 `P227L`** (11β-HSD2) | **SDR — the same gene family member the repository's §7 table already carries for core missense** | Homozygous, and the phenotype was **MILD**: *"conversion of cortisol to cortisone was **58 %** compared with **0–6 % in typical patients** with AME"*; *"In vitro expression studies showed an **increase in the Km (300 nM) over normal (54 nM)**"* | 🟢 **`EXPERIMENTAL` — but a KINETIC defect, not an abundance defect.** ⚠️ **Reverse direction** — a native proline replaced | Wilson 1998, PMID 9707624, PMC21485, [DOI](https://doi.org/10.1073/pnas.95.17.10200), `abstract-depth` |

**WHAT TRANSFERS** from the `P227L` row specifically: 🔵 **a substitution at a proline position in an
SDR produced a graded, kinetic, partly-functional enzyme with a measurable Km shift — i.e. in this
fold, "hypomorph with altered catalysis" is a real and documented outcome class, and it is
distinguishable from "degraded" only because somebody measured Km.** 🔴 **WHAT DOES NOT:** it is the
*reverse* substitution direction (Pro→Leu, not X→Pro), it is a membrane-associated enzyme, and it
says nothing about what introducing a proline into a helix does.

### 3.4 🔴 A POSITION-230 TRAP IN AN SDR — flagged so nobody walks into it

**Miura *et al.* 2008**, monomeric **carbonyl reductase 3 (CBR3)** — an SDR — PMID 18983987,
*Chem Biol Interact* 178(1-3):211–4, [DOI](https://doi.org/10.1016/j.cbi.2008.10.005). Verbatim:

> *"the tryptophan residue at **position 230** is highly conserved while **human CBR3 possesses rigid
> amino acid, proline, at that position** instead … **The substitution of tryptophan for proline in
> hCBR3 failed to affect the enzymatic characteristics.** Similarly, the substitution of proline for
> tryptophan in either Chinese hamster CBR3 or rat CBR3 showed no significant change."*

🔴 **This is an SDR, at residue 230, where proline is the WILD-TYPE HUMAN RESIDUE and swapping it in
either direction changes nothing.** It is the most citable-looking false positive in this section and
it is a *second* instance of the namespace class the brief warned about with `GTPBP3 p.Q230P`
(PMID 41957021 — different gene, different fold, a **measured aggregation** result at an identical
`c.689A>C`, and **still not transferable**).

**WHAT TRANSFERS:** 🟢 one genuine methodological rule — **residue numbering does not align across SDR
family members, and a position match is meaningless without a structural alignment.** CBR3's 230 is,
in the authors' own words, *"in the hinge region at the substrate-binding loop"*; WWOX's 230 is, on
another actor's measurement, **SASA 0.00 Å², mid-helix αE, 6.8–9.7 Å from the substrate triad**.
**Two different structural positions that share an integer.**
**WHAT DOES NOT:** 🔴 **everything else.** No inference about `Q230P` may be drawn from this row, in
either direction — neither "proline at 230 in an SDR is harmless" nor anything else.

### 3.5 A same-position substitution series in a tumour suppressor — the method I take forward

**Shimazu *et al.* 2011**, **menin / MEN1**, *Cancer Science* 102(11):2097–2102,
[DOI](https://doi.org/10.1111/j.1349-7006.2011.02055.x) (retrieved via `Scholar_Gateway`). Verbatim
from the Discussion:

> *"Different amino acid substitutions at the same position differently influenced the stability as
> exemplified by the **normal stability of L22M and L22V mutants**, which substitute similarly
> hydrophobic amino acids for leucine, and the **reduced stability of L22P, which replaces leucine
> with the inflexible proline residue.** The MEN1-associated mutant L22R, which introduces a charged
> residue at the uncharged site, was the least stable mutant at this position."*

| | |
|---|---|
| **WHAT TRANSFERS** | 🟢 **A METHOD, and it is the most directly useful thing in this whole section: the same-position substitution series as the control that proves a lesion is PROLINE-SPECIFIC rather than SIDE-CHAIN-LOSS-specific.** Two neutral substitutions at the same codon, measured side by side with the proline, separate "the wild-type side chain was load-bearing" from "the proline itself is the lesion" — and they do it **in one extra pair of wells**. §7 applies this to `Q230`. |
| **WHAT DOES NOT** | 🔴 Menin is not an SDR and has no fold relationship to WWOX; the readout is nuclear immunoblot stability in a transfection system; `abstract/passage-depth`. **No statement about menin transfers to WWOX**, and the observation that *L22P* was destabilising in menin says nothing whatever about `Q230P`. |

### 3.6 What §3 establishes, and the prediction it fails

| prospective prediction (§1.5) | outcome |
|---|---|
| **P1** — SDR core missense → low protein / normal mRNA, QC-cleared, sometimes temperature- or chaperone-rescuable | 🟡 **PARTLY SUPPORTED, and weaker than I predicted.** The repository's inherited §7 table has the one strong instance (11β-HSD2 Tyr338His/Arg337His, t½ 21 h → 3–4 h, rescued at 26 °C and by glycerol/dexamethasone). **This session added no new instance of the cellular-abundance phenotype in an SDR** — the new SDR material is all purified-protein biophysics. The claim stands on the inherited row, not on anything I found |
| **P3** — aggregation in the SDR family stays interface-associated; a search for *core* SDR aggregation comes back thin | 🟢 **SUPPORTED, weakly and by absence.** No core-SDR aggregation instance surfaced in any of the four searches. ⚠️ **An absence in four queries is not a demonstrated negative**, and `PREMISE: NOBODY_LOOKED` still stands for WWOX. It corroborates §7.1's class assignment without strengthening it much |
| **P6** — proline substitutions under-represented among chaperone-rescuable variants | 🔴 **FAILED — NOT CONFIRMED AND NOT REFUTED.** A dedicated query found **no** literature stratifying pharmacological-chaperone amenability by substituting residue. The nearest statement is generic (*"Mutations that introduce proline into protein sequences are functionally unique, because the cyclical structure of its side chain confers conformational rigidity"* — Pace 2019, GJA1, [DOI](https://doi.org/10.1002/mgg3.882)). 🔴 **I record this as a prediction that did not land.** The mechanistic argument in §5 for why a ligand cannot restore a backbone hydrogen bond therefore rests on **first principles, not on evidence**, and is labelled accordingly |

---

## 4 · Proteostasis mining, ranked by evidence class

🔵 **This section is a DELTA.** The repository already holds
[`proteostasis_discrimination_protocols_20260922.md`](proteostasis_discrimination_protocols_20260922.md)
(the NPC1/CFTR protocol shortlist, the bafilomycin correction, the inhibitor-before-chase step
order), [`proteostasis_rationale.md`](proteostasis_rationale.md), `TX-003` in
[`mechanism_intervention_map.md`](mechanism_intervention_map.md), and `T1`/`T5`/`T7` in the SDR
census. **None of that is repeated.** What follows is what those files do not contain:
**cofactor-mediated stabilisation and ligand-assisted folding**, and the field's own **entry
criterion** stated in its own words.

🔴 **No drug shortlist is produced, and no docking was run, consulted or cited.** The ranking below
is by **evidence class**, exactly as the brief specifies: (1) experimentally rescued missense
protein · (2) **restored FUNCTION, not just abundance** · (3) mechanism compatible with the SDR /
protein state · (4) transferable assay.

### 4.1 🥇 RANK 1 — Cofactor / natural-activator as the stabiliser. Class (1)+(2)+(3)+(4).

**The precedent, stated at full strength and no higher — PMM2-CDG.** Sodano *et al.* 2026,
*IUBMB Life* 78(4), [DOI](https://doi.org/10.1002/iub.70101) (via `Scholar_Gateway`), verbatim:

> *"The complete absence of PMM2 activity is incompatible with life, and **all patients carry at
> least one missense destabilising variant that allows residual enzymatic function. This makes
> PMM2-CDG amenable to pharmacological chaperone treatment.** **Glucose-1,6-bisphosphate is PMM2's
> natural activator and stabiliser**, but its clinical application is severely limited due to its
> unfavourable physicochemical profile. Here, we applied the bioprecursor prodrug strategy to design
> and synthesise Lipo-Glc-1,6-P₂ … confirmed through metabolomics-based studies in **fibroblasts
> derived from PMM2-CDG patient**."*

| | |
|---|---|
| **WHAT TRANSFERS** | 🟢 **The intervention class: an enzyme's own cofactor or natural activator, delivered as a prodrug, used as the pharmacological chaperone.** It requires no inhibitor, no substrate analogue, and no novel chemistry — the ligand already exists and its binding site is already evolved. 🟢 **And the assay: patient-derived fibroblasts + metabolomic readout**, i.e. rescue scored on a downstream consequence rather than on band intensity. |
| **WHAT DOES NOT** | 🔴 PMM2 is not an SDR; its cofactor is a sugar bisphosphate, not a nicotinamide dinucleotide; and **the whole strategy is licensed by a sentence WWOX cannot say** — *"allows residual enzymatic function."* 🔴 PMM2 has a measured activity, a known substrate and a known Kd. **WWOX has none of the three.** |

**Is cofactor-assisted folding real in this fold?** 🟢 **Yes, and P2 is confirmed — which means D4
must be DOWNGRADED from `AGENT-NOVEL` to `CROSS-DOMAIN-DERIVED`.** The phenomenon has a name and a
literature. Chen & Park 2020, *Protein Science* 29(7):1667–78,
[DOI](https://doi.org/10.1002/pro.3880), *"Chaperone action of a cofactor in protein folding"*,
verbatim:

> *"a significant body of experimental evidence has shown that the interactions with the cofactor may
> also occur **even before apoproteins are fully folded** … we have discovered that ATP interacts
> with a **partially folded form** of *E. coli* GAPDH, **modifying the thermodynamics and kinetics of
> its folding** … Our study suggests that **a cofactor can speed up the folding process by
> interacting with partially folded intermediate** through part of its structure."*

**And measured inside the SDR fold itself, with numbers:**

| system | measurement | source |
|---|---|---|
| **SDRvv** (*V. vulnificus* atypical SDR) | Thermofluor run explicitly *"to identify ligands that **stabilize the native state**"* with NADPH / NADP⁺ / NADH / NAD⁺; ITC gives **Kd(NADPH) = 3.5 µM vs Kd(NADP⁺) = 242 µM — a 73-fold difference between the two redox states of the same cofactor** | Buysschaert 2013, *FEBS J* 280(5):1358–70, [DOI](https://doi.org/10.1111/febs.12128) |
| ⭐ **NmrA** — the founding member of *"a structural superfamily which includes the short-chain dehydrogenase/reductases"* | **Tm by DSC: WT 48.0 °C → +NAD⁺ 51.6 °C (+3.6). And in the DESTABILISED variant E193Q/D195N: 38.0 °C → +NAD⁺ 43.8 °C (+5.8)** | Lamb 2009, *Protein Science* 13(12):3127–38, [DOI](https://doi.org/10.1110/ps.04958904); superfamily assignment from Stammers 2001, *EMBO J* 20(23):6619–26, [DOI](https://doi.org/10.1093/emboj/20.23.6619) |

🟢 **That NmrA row is the single most encouraging datum in this file: in an SDR-superfamily protein, a
DESTABILISED VARIANT WAS RESCUED MORE BY COFACTOR THAN THE WILD TYPE WAS (+5.8 °C vs +3.6 °C).**
`HOMOLOGY` + `EXPERIMENTAL`, on another protein. **It is the mechanistic existence proof that D4 is
not fantasy.**

### 4.2 🔴 RANK 1's OWN KILLER — the sign of a stabiliser INVERTS with cofactor occupancy

**Kabir *et al.* 2016**, aldo–keto reductases AKR1A1 and AKR1B10 — PMID 27595938, *Protein Science*
25(12):2132–41, [DOI](https://doi.org/10.1002/pro.3036), **open access**. Verbatim:

> *"Ligands such as enzyme inhibitors stabilize the native conformation of a protein upon binding to
> the native state, but **some compounds destabilize the native conformation upon binding to the
> non-native state**. The former ligands are termed **"stabilizer chaperones"** and the latter ones
> **"destabilizer chaperones."** … **when the coenzyme NADP⁺ was absent**, inhibitors such as
> isolithocholic acid **stabilized** the aldo-keto reductase AKR1A1 upon binding … but
> **destabilized** AKR1B10. **In contrast, in the presence of NADP⁺, they destabilized AKR1A1 and
> stabilized AKR1B10.**"*

🔴 **In an NAD(P)-dependent oxidoreductase, the SIGN of a candidate pharmacological chaperone's
effect flips depending on (a) which enzyme and (b) whether cofactor is bound.** Four combinations,
all four observed, two of each sign.

| | |
|---|---|
| **WHAT TRANSFERS** | 🔴 **A blocking constraint on any WWOX chaperone programme, and it is the most important single finding of §4.** WWOX's cofactor identity, occupancy and even whether it binds NAD(P) at all are **`PREMISE: UNREAD_PRIMARY`** — the only WWOX enzymology paper (PMID 21476439) has never been read by anyone here, and the cofactor-cleft geometry the repository reasons with is **inferred from the fold**. ⇒ **The sign of any candidate WWOX stabiliser is UNDETERMINED BY CONSTRUCTION, not merely unknown.** A screen run in the wrong cofactor state could select compounds that destabilise the protein it is meant to rescue, and the assay would not say so. 🟢 It also supplies the **fix**: run any WWOX stability screen **in both apo and holo conditions**, or establish the cofactor state first. |
| **WHAT DOES NOT** | 🔴 AKRs are a different superfamily (TIM barrel, not Rossmann); these are **purified proteins in DSF/CD-urea**, not cells; and the compounds are bile acids irrelevant to WWOX. **No molecule, no sign and no prediction transfers — only the structural fact that the sign is cofactor-state-dependent.** |

### 4.3 🥈 RANK 2 — Degradation-suppression in a cytosolic TUMOUR SUPPRESSOR. Class (1)+(2)+(4).

**Kampmeyer *et al.* 2017**, PMID 28779490, *Genes Chromosomes Cancer* 56(12):823–31,
[DOI](https://doi.org/10.1002/gcc.22487). Verbatim:

> *"the PQC system operates by following a **better-safe-than-sorry principle** and is thus prone to
> target proteins that are **only slightly structurally perturbed, but still functional** … For a
> number of specific germline or somatic missense variants in different tumor suppressor genes it has
> already been shown that the encoded proteins are subject to rapid proteasomal degradation. Among
> these rapidly degraded proteins, a few such as **von Hippel-Lindau (VHL), BRCA1 and MSH2** have been
> found to **retain at least partial physiological function in cell-based models** … **Increasing the
> amounts of such proteins by stabilizing with chemical chaperones, or by targeting molecular
> chaperones or the ubiquitin-proteasome system, may thus avert or delay the disease onset.**"*

| | |
|---|---|
| **WHAT TRANSFERS** | 🟢 **The closest disease-class analogue available: a cytosolic, non-secretory, non-glycosylated TUMOUR SUPPRESSOR rescued by suppressing degradation, with residual function verified in cell-based models.** It sidesteps `Caveat 1` of the repository's own protocol file (the CFTR/NPC1 paradigm's glycan-maturation readout does not transfer to a cytosolic protein) — because these proteins are cytosolic too. 🟢 And the triage principle: *"identify those whose mechanism of action is via the recognition and clearance of **destabilized, but otherwise functional** protein"*, distinguishing them from *"variants … that would cause disease via other mechanisms such as, for example, **disrupting the active site of an enzyme**."* **That is the entry-criteria question, asked by the field, in the field's words.** |
| **WHAT DOES NOT** | 🔴 The route in these genes is **proteasomal**; the one WWOX allele ever routed (`P252A`) is **lysosomal and MG-132-negative**. 🔴 None of VHL/BRCA1/MSH2 is an SDR or an enzyme of this class. 🔴 And `WWOX`-DEE is a **recessive developmental encephalopathy**, not a cancer-susceptibility syndrome — the onset window, the tissue and the therapeutic timing are all different, and the repository already holds that the developmental window is a live and unresolved constraint. |

**The companion instance of "stable but functionally dead" at an ENDOGENOUS locus** — Rath *et al.*
2019, MSH2 Lynch-syndrome variants knocked into human embryonic stem cells by CRISPR-Cas9,
*Human Mutation* 40(11):2044–56, [DOI](https://doi.org/10.1002/humu.23848), verbatim:

> *"In the other three abrogated lines (p.G674A, p.S723F, and p.D748Y), **while the protein levels
> appear stable, the variants affect residues in the ATPase domain** of MSH2 … which is crucial to
> MSH2 function. Thus, the impairment of MSH2-dependent signaling may be due to **defective adenosine
> nucleotide processing**."*

🔵 **WHAT TRANSFERS — and it is an assay, not a conclusion:** **CRISPR knock-in at the endogenous
locus separates abundance from function without overexpression**, and in that architecture the
variants that came out *stable-but-dead* were the ones in the **nucleotide-binding domain**. 🔴
**WHAT DOES NOT:** MSH2's ATPase is not an SDR cofactor cleft, hESCs are not neurons, and
**no inference about `Q230P` follows** — the parallel is structural-logical, not biological.

### 4.4 🥉 RANK 3 — The classical pharmacological chaperones. Class (1)+(2), but CLASS (3) FAILS.

Retrieved via `Scholar_Gateway`; these are **paradigms**, and the repository already labels them so
(`T7`: *"Paradigm only"*). What this session adds is **the reason class (3) fails, in the field's own
sentences**:

> *"Migalastat … **selectively binds and stabilizes α-Gal A leading to enhanced cellular levels and
> activity for all those mutated variants of the enzyme with remaining residual activity**"* —
> Muntau 2014, *J Inherit Metab Dis* 37(4):505–23, [DOI](https://doi.org/10.1007/s10545-014-9701-z)
>
> *"these misfolded proteins are consequently retained and degraded by ERAD, **although they would
> otherwise be catalytically fully or partially active**. **Active-site directed competitive
> inhibitors** are often effective active-site-specific chaperones **when they are used at
> sub-inhibitory concentrations** … acting as a **folding template**"* — Fan & Ishii 2007,
> *FEBS J* 274(19):4962–71, [DOI](https://doi.org/10.1111/j.1742-4658.2007.06041.x)
>
> *"a missense mutation can cause a deficiency of mutant proteins, **even if they potentially retain
> sufficient biological activity to fulfill their physiological roles**"* — Fan 2007,
> *FEBS J* 274(19):4943, [DOI](https://doi.org/10.1111/j.1742-4658.2007.06043.x)

🔴 **Read them together and the field's entry criterion is unmistakable, and it is not the one the
chaperone framing usually foregrounds. It is not "the protein is degraded." It is "the protein would
be ACTIVE if it folded" — and amenability is scored on ACTIVITY.** 🔴 **For WWOX that criterion is
not unmet; it is UNTESTABLE, because there is no activity to score.**

**The one PC mechanism that does not need an active site — and why it is blocked here too.**
Matalonga 2016, *J Inherit Metab Dis* 40(2):177–93, [DOI](https://doi.org/10.1007/s10545-016-0005-3),
verbatim on tafamidis:

> *"**Tafamidis is an allosteric ligand** … **stabilizes the weaker dimer–dimer interface** against
> heterotetramer dissociation **without interacting in the substrate pocket**."*

🔴 **That route requires a known oligomer interface — and `WWOX homodimerises via the SDR` is
`PREMISE: UNVERIFIED`, asserted uncited, with no published source found by a query census.** So the
one PC class that would not need WWOX's missing substrate is blocked by WWOX's other missing premise.
🔵 **Two independent WWOX knowledge gaps close the two independent PC routes.** The remaining
allosteric precedents — **ambroxol** for Gaucher (*"not interfering with the activity of the rescued
enzyme by competitive inhibition"*), **ciclopirox** for congenital erythropoietic porphyria,
**N-acetylcysteine** as *"a novel allosteric chaperone for the GAA enzyme"* (Gil-Martínez 2022,
PMID 36205620, *Proteomics* 22(23-24), [DOI](https://doi.org/10.1002/pmic.202200222); Muntau 2014) —
were all found by **screening against an activity readout**, which returns to the same blocker.

### 4.5 🔴 RANK 4 — Chemical chaperones (4-PBA, TUDCA). Compartment mismatch STANDS.

Gil-Martínez 2022 confirms their standing use is **ER-directed** (urea-cycle disorders, primary
biliary cirrhosis) with trials in ALS and Alzheimer's. 🔴 **The repository's existing objection is not
overturned:** `HYP-20260709-08` and `DL-MECH-047` already record that **4-PBA/TUDCA are the wrong
compartment** for a cytosolic/mitochondrial protein on a lysosomal route, and nothing found this
session changes that. 🟢 **The transferable part of the arm remains the PERMISSIVE TEMPERATURE, not
the chemical** — which is what the repository's own protocol file already concluded.

### 4.6 One structural caution about the base rate, from the same review

Gil-Martínez 2022, verbatim: *"**Random missense mutations are most often quasi-neutral to
thermodynamic stability** … **Decreased protein stability is the most frequent mechanism associated
with a congenital pathogenic missense mutation.**"*

🔵 Both halves matter and they are usually quoted separately. The first is why a **predicted** ΔΔG
carries little information for any single allele. The second is why "folding lesion" is the correct
**prior** for a pathogenic missense — **a prior, not a finding**, and the repository's own data
(ΔΔG anti-correlated with every WWOX measurement) show what happens when a prior is used as a
measurement.

### 4.7 The evidence-class ranking, on one line each

| rank | intervention class | (1) rescued missense protein | (2) **function** restored | (3) compatible with SDR / WWOX state | (4) transferable assay | verdict |
|---|---|---|---|---|---|---|
| 🥇 **1** | **Cofactor / natural-activator stabilisation** | 🟢 PMM2-CDG; NmrA variant +5.8 °C | 🟢 yes (PMM2 metabolomics) | 🟡 **fold-compatible, WWOX-BLOCKED** — cofactor binding unproven, sign inverts with occupancy (§4.2) | 🟢 DSF/thermofluor ± NAD(P) | 🟡 **Best-ranked and NOT actionable.** Gated on reading PMID 21476439 and on a purified WWOX SDR that does not exist |
| 🥈 **2** | **Degradation suppression in a cytosolic tumour suppressor** | 🟢 VHL, BRCA1, MSH2 | 🟢 *"retain at least partial physiological function in cell-based models"* | 🟡 route mismatch (proteasomal vs WWOX's lysosomal) | 🟢 CRISPR knock-in + endogenous readout | 🟢 **The closest disease-class analogue, and the only one whose compartment matches** |
| 🥉 **3** | **Active-site pharmacological chaperone (migalastat class)** | 🟢 abundant | 🟢 abundant | 🔴 **FAILS — no substrate, no activity, no ligand** | 🔴 amenability is scored on activity | 🔴 **BLOCKED.** The repository's `T5` already said so; §4.4 supplies the field's own sentences for *why* |
| **4** | **Allosteric interface stabiliser (tafamidis class)** | 🟢 | 🟢 | 🔴 **FAILS — requires a known oligomer interface; WWOX's is `PREMISE: UNVERIFIED`** | 🟡 | 🔴 **BLOCKED by a second, independent gap** |
| **5** | **Chemical chaperones 4-PBA / TUDCA** | 🟡 | 🟡 | 🔴 **compartment mismatch, already on the books** | 🟢 (temperature arm only) | 🔴 **Keep the temperature arm, drop the chemical** |
| **6** | **Lysosomal-route inhibition (CQ / NH₄Cl / bafilomycin)** | 🟢 for `P252A` — abundance restored | 🔴 **NO FUNCTIONAL ASSAY WAS RUN UNDER RESCUE**, per the repository's own receipt | 🟡 matches the one measured WWOX route — **on a different, `Benign` allele** | 🟢 cheap, catalogue reagents | 🟡 **A level-raising lever for the plate, NOT a therapy candidate.** `P252A` ≠ `Q230P` |

---

## 5 · The four chaperone entry criteria — each stated explicitly, met or unmet

> ## 🔴 **ONE OF FOUR IS MET. ONE IS UNTESTABLE TODAY. TWO ARE UNMET.**
>
> ## ⇒ **A pharmacological-chaperone strategy for `Q230P` is NOT COHERENT ON PRESENT EVIDENCE — not because it was refuted, but because three of its four preconditions have never been tested and one of them cannot be tested with any WWOX reagent that exists.**

### 5.1 `substrate` — does `Q230P` protein exist, or can it be made to exist?

🟡 **UNMET, AND IT IS THE CHEAPEST ONE TO SETTLE.**

| for | against |
|---|---|
| 🟢 **Transcript is normal** (qRT-PCR, patient fibroblasts) ⇒ the lesion is post-transcriptional ⇒ the ribosome is being handed a message | 🔴 **Protein was NOT DETECTED** on the one Western ever run |
| 🟢 **"Not detected" is a DETECTION FLOOR, not a zero** — `PREMISE: DETECTION_FLOOR`, `CLAIM 030`. Schultz 2018's own fix, already in the repository's protocol file, is brute-force loading at **50 µg/lane** | 🔴 Nobody has ever loaded more, used a luminescent denominator, or looked in the pellet |
| 🟢 **Heterologous expression of WWOX has been reported at least twice** (PMID 21476439: two bacterial systems; plus a GST-fused SDR fragment) | 🔴 **No yield, purity, Tm or monomer fraction is reported anywhere**, and activity was in **crude extract** only. **No purified, folded, biophysically characterised WWOX SDR protein exists** |
| — | 🔴 **And both `Q230P` data points are `abstract-depth`** from a body nobody here has read: n, controls, densitometry and the qRT-PCR amplicon position are unread |

🔴 **The honest statement: we do not know whether `Q230P` protein exists below the blot floor, exists
in the pellet, or is never completed.** ⚠️ **D5 (epitope/detection artefact) remains live and is not
excluded** — if the antibody epitope overlaps 226–240, the segment predicted to distort, a
conformational epitope loss would mimic absence. 🔴 **Nobody here knows which antibody Johannsen 2018
used or where its epitope maps**, and that is one line of a Methods section in an unread paper.

### 5.2 `defect` — is instability / folding / degradation plausible as the lesion?

🟢 **MET — as a PREDICTION, at moderate-high confidence. 🔴 ZERO as a measurement.**

This is the one criterion that clears, and it clears on another actor's geometry, not mine:
SASA 0.00 Å², burial 83.8th percentile, a measured **1.44 Å Cδ/Glu226-O hard overlap**, loss of a
near-ideal i,i−4 helical hydrogen bond (3.03 Å, 9° deviation), and **no cheap accommodation** because
the nearest coil is four residues upstream and **L234 — the most buried residue in the whole chain —
lies in the segment that a kink would displace**. Transferred fold-family support: §3.1's SDR proline
result, and the inherited 11β-HSD2 row (t½ 21 h → 3–4 h, temperature- and glycerol-rescuable).

🔴 **Four things this criterion does NOT establish, and they are exactly the three lesions the
therapy has to tell apart:** it is a **prediction on a predicted monomer**; `Q230P`'s **ΔΔG carries
no evidential weight** (anti-correlated with every WWOX measurement that exists); **turnover,
solubility and aggregation are `PREMISE: NOBODY_LOOKED`** for every WWOX allele; and the geometry
cannot distinguish *degraded* from *insoluble* from *never-synthesised*.

🔵 **And a specific new reason not to lean on ΔΔG for THIS allele, computed here.** Read at
`position = 229` (**0-based**) with `wildtype = Q` verified before use, the local saturation table
ranks the substitutions at 230 as: `E +0.129 · C +0.253 · M +0.305 · H +0.492 · V +0.493 · F +0.499 ·
A +0.580 · T +0.725 · Y +0.737 · I +0.854 · S +0.957 · W +0.985 · L +0.988 · D +1.033 · N +1.363 ·
**P +1.514** · G +1.599 · K +1.667 · R +1.807`. 🔴 **The predictor ranks proline FOURTH of nineteen,
behind arginine, lysine and glycine — it does not single proline out at all**, while the sequence
model (per another actor) *"ranks P worst of all 19."* **The two predictors disagree about proline
specifically.** The mechanistic explanation is the point: a ΔΔG predictor scores a **side-chain
substitution in a fixed backbone**, and `Q230P`'s lesion is a **backbone** lesion — a hard Cδ/carbonyl
overlap and a deleted amide hydrogen. **The predictor cannot see the mechanism, which is a better
reason to discount it than the empirical anti-correlation, and it is consistent with it.**

### 5.3 `rescue variable` — is there something that can change the state?

🟡 **PARTLY MET FOR ABUNDANCE. 🔴 UNMET FOR FOLD.** And the two are not the same criterion.

| lever | status | bound |
|---|---|---|
| **30 °C permissive temperature** | 🟢 **AVAILABLE, reagent-free** | The only fold-directed lever that needs nothing WWOX does not have. Inherited precedent is a variant-abundance atlas, hedged by its own authors with *"Presumably"* |
| **Chloroquine / NH₄Cl** | 🟢 **AVAILABLE** | 🔴 Lysosomotropic and lysosome-wide; the published WWOX instance is on **`P252A`**, a **ClinVar `Benign`** allele, as a **CMV-Flag transgene in thyroid carcinoma**, and **no functional assay was run under rescue.** 🔴 **Add bafilomycin A1** — the repository's protocol file documents chloroquine going **negative** where bafilomycin was strongly positive on endogenous protein in primary fibroblasts |
| **Proteasome inhibition** | 🔴 **EXPECTED NEGATIVE** | MG-132 was negative for `P252A`. ⚠️ Route does not transfer between alleles; run it as a control, expect nothing |
| **Cofactor / ligand-assisted folding** | 🔴 **UNAVAILABLE** | §4.1–4.2. WWOX's cofactor is unproven, and the **sign of a stabiliser inverts with cofactor occupancy** |
| **Active-site pharmacological chaperone** | 🔴 **UNAVAILABLE** | No substrate, no activity, no ligand |
| **Interface stabiliser (tafamidis class)** | 🔴 **UNAVAILABLE** | Homodimerisation `PREMISE: UNVERIFIED` |

🔴 **The distinction that decides this criterion: every available lever raises ABUNDANCE. None of
them repairs a FOLD.** Chloroquine does not make a protein fold; it stops a lysosome eating it.
Temperature is the only listed lever that acts on the folding equilibrium itself — and a permissive
temperature is not a therapy for a human being.

🔴 **And a first-principles caution that §3.6 records as EVIDENCE-FREE, so it is labelled as
reasoning and not as a finding:** `Q230P`'s primary lesion, as measured by another actor, is the
**deletion of a backbone amide hydrogen and a hard steric overlap involving a backbone carbonyl**.
A ligand binding elsewhere can shift a folding equilibrium; **it cannot restore a hydrogen bond that
the polypeptide can no longer donate.** ⚠️ **This is an argument, not an observation. The dedicated
literature search for it (P6) came back empty in both directions.** It is offered as a reason to
*test* the prerequisite, not as a reason to conclude.

### 5.4 `functional assay` — can rescue be tested INDEPENDENTLY OF ABUNDANCE?

> ## 🔴 **UNMET. AND THIS IS THE ONE THAT DECIDES.**

**`PROTEIN INCREASE ≠ THERAPEUTIC RESCUE`**, and for WWOX the gap is not a caveat — it is the whole
state of the field:

1. 🔴 **WWOX has no demonstrated physiological function of any kind.** No substrate, no validated
   cellular activity readout, no assay that meets the `PMID 28540421` standard (active-site **and**
   cofactor-site mutants each abolishing the readout, *in vitro* and *in vivo*).
2. 🔴 **No functional measurement has ever been made on a WWOX missense protein whose abundance was
   restored.** Not once, for any allele. The one published rescue (`P252A`, CQ/NH₄Cl) read out
   **band intensity** and ran **no** colony, invasion, comet, γH2AX or NHEJ assay under rescue.
3. 🔴 **The best available surrogate is ENGAGEMENT, not function** — and the design's own author says
   so: *"engagement competence per molecule … not a demonstrated physiological function."*
4. 🔴 **And the go/no-go control that was supposed to prove the surrogate could detect a
   stable-but-dead protein is now `OVEREXPRESSION-ARTEFACT SUSPECT`** (§2.6).
5. 🔴 **The fold family says the null hypothesis should be stable-and-dead, not stable-and-alive.**
   §3.2: in an SDR, core-stabilising substitutions produced *"more stable than wild type"* protein
   with *"dramatic activity loss"* in every case, five of them with **no detectable activity**.
6. 🔴 **And the field's own entry criterion is the one WWOX cannot state.** *"All patients carry at
   least one missense destabilising variant **that allows residual enzymatic function**"* — PMM2-CDG.
   *"All those mutated variants of the enzyme **with remaining residual activity**"* — migalastat.
   **For `Q230P` nobody can say either sentence, and nobody can currently run the experiment that
   would let them.**

### 5.5 The four criteria on one line each

| # | criterion | verdict | what would change it |
|---|---|---|---|
| 1 | **`substrate`** — protein exists or can exist | 🟡 **UNMET, cheap to settle** | One high-load Western with a **soluble/pellet split** on `Q230P` patient fibroblasts. One blot, two lanes |
| 2 | **`defect`** — instability/folding/degradation plausible | 🟢 **MET as a prediction · 🔴 zero as a measurement** | A thermal melt on purified `Q230P` SDR — 🔴 **not available at any price today**; no one has ever purified this domain |
| 3 | **`rescue variable`** — something can change the state | 🟡 **MET for ABUNDANCE · 🔴 UNMET for FOLD** | A demonstration that WWOX binds NAD(P), which would open the cofactor route — gated on PMID 21476439, unread |
| 4 | **`functional assay`** — rescue testable independently of abundance | 🔴 **UNMET, and decisive** | A WWOX readout meeting the `PMID 28540421` standard; or, short of that, an **engagement** readout with a **graded, abundance-independent** calibrator that `P282A` can no longer be |

---

## 6 · MECHANISM VERDICT

> ## 🟡 **`MIXED`, and the composition is lopsided and specific: `FOLDING` is the primary lesion class, `STABILITY/DEGRADATION` is its most likely CONSEQUENCE rather than the lesion itself, `AGGREGATION/INSOLUBILITY` is unexcluded, and `COFACTOR/CATALYTIC DEFECT` enters only by an indirect propagation route.**
>
> ## 🔴 **And the therapeutic answer does not follow from that label. On the therapeutic question actually asked — *is increasing `Q230P` abundance coherent* — the verdict is `UNRESOLVED`, because three of four chaperone entry criteria are untested and the fourth cannot be tested with any WWOX reagent in existence.**
>
> ## 🔴 **Intervention class, if the prerequisites were met: NOT a pharmacological chaperone. The two PC routes that WWOX could in principle use are each blocked by a DIFFERENT unresolved WWOX premise, and the best-ranked route by evidence class — cofactor/natural-activator stabilisation — is blocked by a third.** `IPOTESI`.

### 6.1 Per component, with a confidence statement on each

| component | verdict | confidence | source class | rests on |
|---|---|---|---|---|
| **`FOLDING`** — primary lesion class | 🟢 **SUPPORTED** | **moderate-high** as prediction · 🔴 **ZERO** as measurement | `MODEL` (predicted monomer) + `INFERENCE` | 1.44 Å Cδ/O226 overlap; deleted i,i−4 amide H; SASA 0.00; no cheap accommodation; **independently corroborated as a fold-class risk by §3.1's SDR proline result** (`EXPERIMENTAL`, transferred) |
| **`STABILITY/DEGRADATION`** — consequence | 🟡 **PLAUSIBLE, UNMEASURED** | **low-moderate** | `INFERENCE` from `HOMOLOGY` | Fold-family default for monomer-core lesions (11β-HSD2, inherited row). 🔴 **The route does not transfer** — proteasomal there, lysosomal in the one WWOX allele ever routed. 🔴 `PREMISE: NOBODY_LOOKED` for `Q230P` |
| **`AGGREGATION/INSOLUBILITY`** | 🟡 **NOT SUPPORTED, NOT EXCLUDED** | **low** | `INFERENCE` | The documented SDR aggregation trigger is **interface substitution**, and `Q230P` at SASA 0.00 is not that class. 🔴 **But nobody has looked in the pellet, for any WWOX allele, ever.** My §3 searches added no core-SDR aggregation instance — an absence in four queries, not a negative |
| **`INTERFACE DEFECT`** | 🟢 **EXCLUDED** | **moderate-high** | `MODEL`, topology-independent | SASA 0.00 in the free monomer; an interface residue requires `SASA_monomer > 0`. 🔴 The premise the fork rested on (`WWOX homodimerises via the SDR`) is itself `PREMISE: UNVERIFIED` |
| **`COFACTOR/CATALYTIC DEFECT`** — direct | 🟢 **EXCLUDED** | **high** | `MODEL` | 12.60 Å from the cleft axis; 10.01 Å from `TGANSGIG`; side chain 141° from Y293-OH |
| **`COFACTOR/CATALYTIC DEFECT`** — indirect (D7) | 🟡 **GEOMETRICALLY AVAILABLE, UNTESTED** | **very low** | `INFERENCE` from `MODEL` | Asn232 sits 5.82 Å from the cleft axis, two residues from the helix a proline must distort. 🔵 **§3.2 raises this from "a geometric possibility" to "the fold family's observed default when the core is perturbed"** — still not a measurement |
| **`PARTNER-SPECIFIC DEFECT`** | 🔴 **NOT ASSESSABLE** | — | — | No WWOX-DEE allele has ever been tested against **any** partner. `PREMISE: NOBODY_LOOKED` |
| **Abundance (the observable)** | 🟡 **one non-detection, cause untested** | 🔴 **capped — `abstract-depth`** | `EXPERIMENTAL`, unread primary | Normal transcript + protein not detected. Three causes — reduced translation, accelerated turnover, insolubility — **none separated.** ⚠️ **D5 (detection floor / epitope) is a fourth and is not excluded** |

### 6.2 Why the composite label is `MIXED` and not `FOLDING`

**Because two of the components cannot be separated with the evidence that exists, and the brief's
list treats them as alternatives when for this allele they are a sequence.** A backbone lesion that
prevents a fold *produces* a degradation or insolubility phenotype; calling the result
`STABILITY/DEGRADATION` names the consequence and hides the cause, and calling it `FOLDING` alone
asserts that the protein folds badly rather than not at all — **which is precisely the D1-vs-D2
distinction nobody has measured.** `MIXED` is the label that does not overstate.

🔴 **And `MIXED` is not a hedge, because it has a therapeutic consequence the pure labels do not:**
a `STABILITY/DEGRADATION` lesion is treated by slowing clearance, and a `FOLDING` lesion is treated by
changing the folding equilibrium. **Every rescue lever WWOX currently has does the first. None does
the second.** If the lesion is mostly `FOLDING`, the available levers are acting on the wrong step.

### 6.3 🔴 What would falsify this verdict — stated as specific observations

| component | one observation that falsifies it |
|---|---|
| `FOLDING` as primary | **`Q230A` and `Q230M` read as badly as `Q230P`** in the same-position series (§7.3). That would make the lesion side-chain-network, not proline-backbone, and would put `COFACTOR`-adjacent H-bonding back in play |
| `STABILITY/DEGRADATION` as the consequence | **`Q230P` protein accumulates under NO condition** — not 30 °C, not CQ, not bafilomycin, not at 50 µg/lane. That is D1 (folding-yield ceiling), and it removes degradation as the operative step |
| `AGGREGATION` not supported | 🔴 **`Q230P` protein found in the SDS pellet.** One lane. **This single observation stops the entire abundance-raising axis regardless of everything else in this file** |
| `INTERFACE` excluded | An experimental or AlphaFold-Multimer WWOX dimer placing residue 230 within 5 Å of the partner chain. 🟢 **Achievable with no wet work and still not done** |
| the therapeutic verdict `UNRESOLVED` | **A published WWOX activity readout meeting the `PMID 28540421` standard.** That single development converts criterion 4 from *untestable* to *testable* and reopens every route in §4 |
| `OVEREXPRESSION-ARTEFACT SUSPECT` for `P282A` | A measurement of `P282A` function **at matched, physiological abundance** — e.g. CRISPR knock-in at the endogenous locus (§4.3's architecture) — showing it is genuinely engagement-dead. Then §2.6's demotion reverses |
| **the whole file** | A demonstration that WWOX binds NAD(P) with a measured Kd **and** that the SDR is an obligate holo-protein. Then the apo monomer model every geometry number rests on is the wrong conformation, and §4.1 becomes the lead route instead of a blocked one |

### 6.4 RESULT — filling §1.7, including the predictions that failed

| # | prediction | outcome |
|---|---|---|
| **P1** | SDR core missense → low protein, normal mRNA, QC-cleared, sometimes rescuable | 🟡 **PARTLY — and I added nothing.** The claim still stands on the inherited 11β-HSD2 row. My searches returned SDR **biophysics**, not SDR **cell biology** |
| **P2** | Cofactor documented as a folding/stabilising ligand in SDR / Rossmann enzymes | 🟢 **CONFIRMED, with numbers** (Chen & Park; SDRvv thermofluor + ITC; NmrA Tm +3.6 °C WT / **+5.8 °C in a destabilised variant**). 🔴 **⇒ D4 downgraded `AGENT-NOVEL` → `CROSS-DOMAIN-DERIVED`** |
| **P3** | SDR aggregation stays interface-associated | 🟢 **SUPPORTED WEAKLY, by absence.** Four queries, no core-SDR aggregation instance. Not a demonstrated negative |
| **P4** | `rs3764340` is common, homozygotes exist | 🟢 **CONFIRMED DECISIVELY.** MAF 4.2–8.6 %; **18 GG homozygotes enrolled as healthy adult controls** |
| **P5** | Chaperone field has cases of abundance restored without function | 🟡 **REDIRECTED, and the redirect is better than the prediction.** I found **no catalogue of chaperone failures** — what I found instead is that the field **pre-empts the failure by an entry criterion**: it only attempts variants with demonstrated **residual activity**. 🔴 **The prediction was aimed at the wrong target: the risk is not that chaperones fail silently, it is that WWOX cannot even be screened for amenability.** And the SDR fold supplied the missing failure instance directly (§3.2) |
| **P6** | Proline substitutions under-represented among chaperone-rescuable variants | 🔴 **FAILED. Not confirmed, not refuted, nobody has stratified.** Recorded as a failed prediction; the §5.3 backbone argument is labelled first-principles reasoning in consequence |

🔴 **The hypothesis of §1.4 is PARTLY WRONG, and the part that is wrong matters.** I predicted the
gate would be *"whether a cofactor-competent fold can be completed."* **It is not.** The gate is one
step earlier and much cruder: **there is no way to measure whether ANY fold of WWOX is competent at
anything**, cofactor or otherwise. D4 turned out to be real biology (P2 confirmed) attached to a
WWOX-specific blocker I had not weighted — the **sign inversion** of §4.2 — which makes it not merely
unavailable but *unsafe to screen for* until the cofactor state is known. **The prediction that
carried the most weight in §1.4 is the one that came back least useful.**

---

## 7 · The refined minimal assay architecture

🔵 **This is a REFINEMENT of an existing design, not a new one, and it is scored as such.** The
donor-saturation NanoBRET architecture is Scientist D's (§3); the `POLE4` + `GSK3β` co-primary
numerators, the `BRCA1` WW1 negative control and the `HSC70` inverse-sign channel are Scientist E's
(§4). **I am not re-deriving any of it.** §7 changes **four** things and adds **two constructs**, and
every change is forced by a finding in §§2–5.

🔴 **No MAVE campaign and no activity-sensor programme is proposed.** Both are materially new
research programmes and the Operator's decision. §7.6 parks the one thing that genuinely needs one.

### 7.1 What survives unchanged — stated first, so the changes are visible

🟢 The NanoLuc **donor channel as the same-molecule abundance denominator** (the single reason the
design exists — it turns *"not detected"* into a number). 🟢 **BRET, not split-complementation.**
🟢 **Donor-saturation titration with curve fitting** — abundance becomes the x-axis instead of a
confound. 🟢 **WWOX-depleted host.** 🟢 **`BRCA1` (WW1) as the domain-specificity negative**, kept in
its published co-IP format on the same lysates for the first pass. 🟢 **`HSC70` as a third,
inverse-sign channel.** 🟢 **The soluble/insoluble split on the same lysates.** 🟢 **`tau` stays
struck.** 🟢 **The solubility split on patient fibroblasts runs FIRST in time**, because it is the one
measurement that can stop the axis by itself.

### 7.2 🔴 CHANGE 1 — `P282A` is demoted from go/no-go gate to an uncalibrated reference point

Forced by §2. `P282A` stays on the plate — it is still the only WWOX readout reported to fail in a
missense protein with no measured stability defect. **But the plate may no longer claim sensitivity
on the strength of reproducing it**, because an allele carried homozygously by healthy adults cannot
anchor "complete function-dead." Concretely:

- **Delete** from the protocol: *"`P282A` must read engagement-dead at normal donor signal; if it
  does not, discard the plate."*
- **Replace** with: *"`P282A` is expected to read engagement-REDUCED at normal donor signal, by an
  amount that has never been quantified at physiological abundance. Its value on the plate is as a
  **direction**, not a magnitude, and the plate's sensitivity claim rests on §7.3 instead."*
- 🔴 **`L404A` does not inherit the job** — its own abundance was never reported (`D-4`).

### 7.3 ⭐ CHANGE 2 — ADD THE SAME-POSITION SUBSTITUTION SERIES. Two constructs. This is the core refinement.

**Method transferred from §3.5 (menin `L22M`/`L22V`/`L22P`/`L22R`); applied to `Q230`; novel in this
repository** (`Q230A`, `Q230G`, `Q230L` return **zero** occurrences across the whole tree).

Add **`Q230A`** and **`Q230M`** alongside `Q230P`. Chosen on the local saturation table read at
`position = 229` (**0-based**) with `wildtype = Q` verified:

| construct | ΔΔG_pred | what it removes | what it does NOT add |
|---|---|---|---|
| **`Q230M`** | **+0.305** (3rd-lowest of 19) | the amide's hydrogen-bonding capacity | keeps chain length and hydrophobic bulk; **no backbone constraint** |
| **`Q230A`** | **+0.580** | the entire side chain and all five of its polar contacts, including the three long-range ones (Δseq −44 to −46) | **no backbone constraint** |
| **`Q230P`** | **+1.514** | the same side chain **plus** the i,i−4 amide hydrogen — **and adds a Cδ that overlaps Glu226 O by 1.44 Å** | — |

**What two wells buy — and this is the compression:**

| `Q230A` | `Q230M` | `Q230P` | reading | consequence |
|---|---|---|---|---|
| 🟢 normal | 🟢 normal | 🔴 dead | **The lesion is PROLINE-SPECIFIC — backbone and secondary structure** | 🔴 **The hardest possible reading for the chaperone axis:** no ligand restores a hydrogen bond the chain cannot donate. Confirms §6.1 row 1 and makes criterion 3 (fold rescue) the binding constraint |
| 🔴 dead | 🔴 dead | 🔴 dead | **The lesion is the SIDE-CHAIN POLAR NETWORK** | 🟢 **Better news:** a packing/network lesion of the kind ligands and osmolytes *can* shift. It also **falsifies** the sequence model's preference for G/A over Q at 230 |
| 🟢 normal | 🔴 dead | 🔴 dead | The **amide hydrogen-bonding** specifically | Network lesion, residue-resolved |
| 🔴 dead | 🟢 normal | 🔴 dead | **Volume / packing**, not chemistry | Points at core repacking |

🔵 **Why this is worth two wells and nothing else on the plate is.** It is the **only** addition that
(a) resolves a question the structural adjudication explicitly left open — its § 2 row 5 is 🟡
*"network YES, conserved-glutamine NO"* — (b) **supplies the graded, abundance-independent calibrator
that §7.2 just removed**, because `Q230A`/`Q230M` are expected to sit *between* wild type and
`Q230P`, and (c) **needs no new reagent class, no new instrument and no new read** — same vector,
same tag, same plate, same fit.

### 7.4 🔴 CHANGE 3 — the first-pass lever set, corrected

| arm | status | why |
|---|---|---|
| **30 °C** | 🟢 **KEEP — and promote it to the primary fold-directed lever** | §5.3: it is the *only* available lever that acts on the folding equilibrium rather than on clearance |
| **Chloroquine** | 🟢 keep | but never alone |
| **Bafilomycin A1** | ⭐ **ADD** | The repository's own protocol file documents CQ going **negative** where bafilomycin was strongly positive on **endogenous protein in primary fibroblasts**. One catalogue reagent, a few wells. **If CQ alone is run and comes back negative, the result is not interpretable as "not the lysosome"** |
| **MG-132** | 🟢 keep as a control, **expect negative** | ⚠️ route does not transfer between alleles |
| **4-PBA / TUDCA** | 🔴 **DO NOT ADD** | Wrong compartment for a cytosolic/mitochondrial protein on a lysosomal route — already on the repository's books, and §4.5 found nothing to overturn it |
| **±UV** | 🔴 **KEEP OUT OF THE FIRST PASS** | Scientist E's `D-2`: UV perturbs the same stress pathways as the CQ and 30 °C arms. Run the ±UV question on a separate `POLE4`-only plate |
| **Any cofactor / NAD(P) arm** | 🔴 **DO NOT ADD** | §4.2: **the sign inverts with cofactor occupancy**, and WWOX's occupancy is unknown. Adding it would produce an uninterpretable result in either direction |

### 7.5 🔴 CHANGE 4 — the partner line, amended by §2

🟢 **`POLE4` and `GSK3β` stay co-primary.** Neither is displaced by anything in this file, and the
reasons they complement each other are unchanged. Two amendments:

1. 🔴 **`POLE4`'s credential is now WEAKER THAN IT READS.** Its entire claim to criterion C6 is the
   `P282A` result — and §2 makes that result `OVEREXPRESSION-ARTEFACT SUSPECT`, measured **only after
   UV**, in a **transgene**, in **thyroid carcinoma**. **`POLE4` no longer carries a
   demonstrated abundance-independent failure; it carries a reported one whose conditions are all
   confounded.** It stays because nothing better exists, and the protocol must say that.
2. 🟢 **`GSK3β`'s standing caution is unchanged and must travel with it verbatim:** 388–407 is a
   **linear docking motif at the extreme C-terminal end** of the span, `Q230` is **174 residues**
   away, and whether presenting that motif requires the SDR core fold **has never been measured**.
   🔴 **⇒ A NORMAL `GSK3β` curve for `Q230P` is WEAK evidence of an intact fold and must not be read
   as one.** 🔵 **§7.3's series partly relieves this**: if `Q230A` and `Q230M` also read normal on
   `GSK3β` while differing on `POLE4`, the `GSK3β` channel is behaving as a
   fold-insensitive control rather than as a numerator — **and the plate finds that out by itself.**

### 7.6 `HUMAN_REQUIRED` — parked, not pursued. No external action was taken.

🔴 **No email was sent, no author or laboratory was contacted, no material was requested, and no
molecule, dose or route is recommended anywhere in this file.**

| # | item | why it needs a human, and why it is not a substitute for §7 |
|---|---|---|
| **H-1** ⭐ | **Obtain PMID 29808465 (Johannsen 2018).** `unrecoverable_by_these_routes`, `pmc_id: null`, closed at Springer. Needed: **n, controls, densitometry, the qRT-PCR amplicon position — and the ANTIBODY and its EPITOPE**, which decides whether D5 is live | **Both** experimental data about **the most recurrent WWOX allele in the disease — 8 patients, 6 families** — are `abstract-depth`. One PDF is the cheapest evidence purchase in this node |
| **H-2** | **Obtain PMID 21476439** — the only WWOX enzymology paper ever published | It is the only source that could say whether WWOX binds NAD(P). **It gates §4.1, the best-ranked intervention class, and §4.2's sign problem** |
| **H-3** | **Obtain Figure S9 (Supporting Information) of PMID 41124647** — `P252A`'s `POLE4` co-IP | Scientist E's `D-1`, still the single highest-value unopened item for the numerator |
| **H-4** | **Confirm `Q230P` patient-derived fibroblasts exist and are obtainable** | `PREMISE: UNVERIFIED` on material availability. **The solubility split — the one measurement that can stop the therapeutic axis — cannot run without it** |
| **H-5** | 🔴 **A PROGRAM DECISION, not a task: whether to commission a WWOX activity readout meeting the `PMID 28540421` standard.** This IS a materially new research programme and it is the Operator's call. §7 deliberately does **not** propose it | 🔴 **It is the only thing that converts entry criterion 4 from *untestable* to *testable*.** Everything in §7 is a **surrogate** until it exists, and §7 says so rather than pretending otherwise. **Stating this as `HUMAN_REQUIRED` is the correct output here, not a workaround** |

### 7.7 The refined architecture, in one paragraph

**One plate series. Constructs: `WT`, `Q230P`, `Q230A`, `Q230M`, `P282A`, `P252A`. Channels: NanoLuc
donor (abundance denominator), BRET to `POLE4` and to `GSK3β` (engagement per molecule, fitted
BRET<sub>max</sub>), `HSC70` co-IP (inverse-sign misfolding channel), and `BRCA1` WW1 co-IP on the
same lysates (domain control). Levers: 30 °C, chloroquine, bafilomycin A1, MG-132 control. On every
lysate, the soluble/insoluble split. Read out one quantity per allele: the slope of engagement
against donor luminescence across the induced range, expressed as a fraction of the wild-type
slope.** Two constructs and one reagent more than the design it refines; one control demoted; one
arm deferred; one arm refused.

---

## 8 · The single best discriminating experiment

> ## 🔴 **IT IS NOT THE PLATE. It is one blot with four lanes, and it runs first because it is the only measurement in this entire node that can STOP the therapeutic axis by itself.**

### 8.1 The experiment

**On `Q230P` patient-derived fibroblasts and ≥2 healthy controls: lyse in a non-denaturing buffer,
spin, and blot the soluble supernatant and the resuspended SDS pellet on the SAME membrane at the
SAME exposure, loading ~50 µg per lane — with an arm grown at 30 °C.**

Four lanes: patient-soluble, patient-pellet, control-soluble, control-pellet. Plus the 30 °C
duplicate. Existing material, catalogue reagents, roughly one day on top of a blot already planned.

### 8.2 What it discriminates — four mechanisms, one membrane

| observation | mechanism | therapeutic consequence |
|---|---|---|
| Protein **in the pellet** | 🔴 **D3 — insolubility / aggregation** | 🔴 **STOP. A non-allele-specific boost is actively dangerous, regardless of everything else in this file.** No other single measurement in this node can do this |
| Protein **in the supernatant at 50 µg**, absent at routine load | 🟢 **D2 — present, below the old detection floor** | 🟢 The `substrate` criterion clears, and the whole plate of §7 becomes worth building |
| **Neither fraction**, at 50 µg, with normal transcript | 🔴 **D1 — folding-yield / synthesis ceiling** | 🔴 An abundance-raising strategy has nothing to act on. Go to the synthesis arm, which §4/the protocol file both price at 10³–10⁴ EUR |
| **Nothing at 30 °C either** | Strengthens D1 against D2 | The one fold-directed lever has been tried and failed |
| Protein appears **only at 30 °C**, in the **supernatant** | 🟢 **Folding-limited and rescuable** | 🟢 The single best possible result: `substrate` **and** `defect` **and** a fold-directed `rescue variable` all clear at once |

### 8.3 Why THIS one, over the plate and over everything else

| | |
|---|---|
| **It is the only one that can stop the axis** | Every other experiment in this node refines a therapeutic hypothesis. **This one can end it.** A pellet result makes the `MIXED` verdict's aggregation component decisive and forecloses the boost route for the allele with the largest constituency in the disease |
| **It answers the criterion that gates all the others** | Criterion 1 (`substrate`). 🔴 **If `Q230P` protein does not exist, §7's plate measures a transgene's behaviour and tells you nothing about the patient's allele.** Order matters |
| **It is the cheapest thing in the file by two orders of magnitude** | One day, catalogue reagents, existing material. The plate is months and constructs |
| **It is endogenous, untagged, unamplified** | 🔴 It is the **only** measurement proposed anywhere in this node that touches the real allele in a real patient-derived cell at its real expression level. Everything else is a transgene — and §2 is a demonstration of what transgenes do to a conclusion |
| **It is compression, not omission** | Soluble/insoluble **×** high load **×** ±30 °C = **three variables, one membrane, four mechanisms separated.** The measurements deliberately left out: no CHX chase (**you cannot chase an undetectable band** — the repository's own `Caveat 2`), no pulse-label (reachable by elimination, 10³–10⁴ EUR), no MD, no docking, no purified protein, no ±UV |
| 🔴 **What it is NOT** | **It is NOT a function assay and has no numerator at all.** Reporting a pellet-vs-supernatant blot as evidence about function would be the precise error `P282A` exists to prevent. It decides **where the protein is**, which is a prerequisite for the function question — not an answer to it |
| 🔴 **Its one hard dependency** | `Q230P` patient fibroblasts. `PREMISE: UNVERIFIED` on availability — **`HUMAN_REQUIRED` H-4**, and the only thing standing between this node and its most informative measurement |

🔵 **The honest note on origin: this experiment is not mine.** Its core is Scientist S's census § 9.1
arm 1, adopted unchanged by Scientist D's § 4. **What §8 contributes is the ORDERING argument and two
additions** — the 50 µg load (from the repository's own NPC1 reading) and the 30 °C arm folded into
the same membrane, which converts a two-way discriminator into a four-way one at no extra cost.
**Graded `REDISCOVERY` plus a method increment, not a discovery.**

---

## 9 · What I could not establish

| # | open item | why it did not resolve | cheapest move |
|---|---|---|---|
| **1** ⭐ | **Whether `Q230P` protein exists at all** | Never measured below the blot floor; never fractionated; body of PMID 29808465 unread | 🟢 **§8.** One blot, four lanes |
| **2** ⭐ | **Whether WWOX binds NAD(P), and in which redox state** | PMID 21476439 `PREMISE: UNREAD_PRIMARY`, no PMCID, three independent checks confirm no PMC deposit | `HUMAN_REQUIRED` **H-2**. 🔴 **It gates §4.1 — the best-ranked intervention class — and §4.2's sign problem makes it unsafe to screen without it** |
| **3** | **`P282A`'s function at physiological abundance** | Every functional measurement is CMV-driven overexpression in cancer lines; no matched-abundance arm, no dose–response, no endogenous-locus experiment | CRISPR knock-in at the endogenous locus (§4.3's architecture). 🔴 **Not a small task, and not proposed here** |
| **4** | **Whether `rs3764340` has a real exonic-splicing-enhancer effect on exon 8** | Both statements found are **`MODEL`** (SNPinfo prediction). No minigene, no RT-PCR, no RNA-seq of a `G`-allele carrier exists | A minigene or an RT-PCR on a `GG` carrier. ⚠️ It would change how the control is interpreted; it says nothing about `Q230P` |
| **5** | **European / African / South Asian homozygote COUNTS for `rs3764340`** | gnomAD, dbSNP, Ensembl and 1000 Genomes are all `connect_rejected`. What I have is **MAF** for Europeans (0.042 dbSNP-quoted / 0.044 measured) and **counts** only for East Asians | One gnomAD lookup, the moment egress allows it. 🔵 **The conclusion does not depend on it** — 18 East Asian healthy adult homozygotes already settle the question |
| **6** | **Whether Johannsen 2018's antibody epitope overlaps 226–240** (D5) | One line of a Methods section in an unread paper | `HUMAN_REQUIRED` **H-1**. 🔴 **If it does, "protein not detected" may be an epitope artefact and the entire abundance premise changes** |
| **7** | **Whether proline substitutions are differentially chaperone-refractory** | 🔴 **Prediction P6 FAILED.** A dedicated query found no literature stratifying amenability by substituting residue — **not confirmed and not refuted** | A systematic re-analysis of the published amenability datasets. ⚠️ That is a new programme; §5.3's argument is labelled first-principles in the meantime |
| **8** | **Whether residue 230 contacts a partner subunit in a real WWOX dimer** | No dimer model exists here; `files.rcsb.org` off the allowlist | 🟢 **AlphaFold-Multimer on WWOX ×2, ΔSASA at 230. No wet work, no spend.** Inherited as the highest-value cheap item and **still not done** |
| **9** | **Whether `Q230P` has ANY partner-specific defect** | No WWOX-DEE allele has ever been tested against any partner | §7's plate — which is exactly why it exists |
| **10** | 🔴 **The cellular-abundance behaviour of a core proline in a HUMAN SDR** | §3 found the fold-family proline result in **purified bacterial protein** and the human-SDR proline variants only at **`MODEL` depth**. 🔴 **P1 was not strengthened by anything I found** | An unresolved gap, recorded as one |

### 9.1 Routes recorded as blocked — once each, not retried

| route | state | evidence |
|---|---|---|
| gnomAD · dbSNP/NCBI E-utilities · Ensembl REST + FTP | 🔴 **BLOCKED** | `connect_rejected`, *"gateway answered 403 to CONNECT"*, per the proxy's own status endpoint |
| general web egress (`example.com` control) | 🔴 **allowlist confirmed** | the control behaves exactly as predicted |
| PMID 29808465 · PMID 21476439 full text | 🔴 no PMCID exists | prior-session checks, three independent methods; not re-attempted |
| PubMed for the GAPDH cofactor-chaperone paper by title | 🔴 **0 records** | `"Chaperone action of a cofactor in protein folding"[Title]` → 0. 🔵 **A meaningless zero, correctly not treated as evidence** — the paper was already in hand from `Scholar_Gateway` with a full citation line and DOI |

### 9.2 🔴 Two PubMed traps hit and cleared in this act

1. **A guessed-author zero.** `pharmacological chaperone rare disease reduced protein stability
   review Pey Martinez-Limon` → **0 records**, and the `query_translation` shows why: it contains
   `"Pey"[All Fields] AND "Martinez-Limon"[All Fields]` — **author surnames I supplied on a guess.**
   🔴 **A zero from a guessed author name is not evidence of anything.** It was not reported as one;
   the review was then found by a different route and is PMID **36205620**.
2. ⭐ **A wrong-MeSH expansion, caught in the same query set.** In the search that *did* find the
   review, `"Millet"` (an author surname) expanded to **`"millets"[MeSH Terms] OR "millets"[All
   Fields] OR "millet"[All Fields]`** — 🔴 **the cereal.** The query returned the right paper only
   because the other terms carried it. **Had the other terms been weaker, this would have been a
   silent, confidently-wrong retrieval.** Recorded because trap (d) is normally invisible: you see it
   only by reading the `query_translation`, and it fires on **surnames that are also common nouns**.

### 9.3 🔴 Self-contamination avoided, and what this file did not touch

No count in this file was obtained by grepping a tree containing this file; repository counts were
taken with `git grep … HEAD`. **No registry, queue, ledger, receipt chain, canonical file or state
manifest was written. No `BATCH_COMMIT`. No git command was run.** One output file was created: this
one. No `FULLTEXT_READ_RECEIPT` is claimed for anything above, and **none is owed**: the two PMC
bodies in §2.2 were read for two table rows each and are recorded at `partial-depth` for that
purpose only, and everything reached through `Scholar_Gateway` is **passage-depth**, which cannot
substitute for a full read. Other actors' files are cited as **their** attestations, not as my
readings.

### 9.4 Nothing here is medical advice

No molecule, dose, route, prognosis or safety claim is recommended anywhere above. The sign of a
therapeutic axis is an epistemic bookkeeping statement about this repository's evidence, not a
clinical statement about any person. **No prognosis attaches to a genotype class, and this file makes
none.** A `DISCOVERY` hypothesis is not a `CANDIDATE` and not `CANONICAL`; D4, D5 and the
same-position-series reading are `IPOTESI` throughout.

---

**END OF FILE — `q230p_therapeutic_mechanism_expansion_20260922.md`. Sections 0–9 all present:
inherited bounds in §0, the prospective DISCOVERY_TRACE in §1 (persisted before confirmatory search;
RESULT appended at §6.4 with two failed predictions recorded as failed), `rs3764340` in §2,
proline-in-SDR in §3, evidence-ranked proteostasis mining in §4, the four chaperone entry criteria in
§5, the mechanism verdict with per-component confidence and falsifiers in §6, the refined assay and
the `HUMAN_REQUIRED` packet in §7, the single best discriminating experiment in §8, and what could
not be established in §9.**

---

## 10 · ORCHESTRATOR VERIFICATION — added 2026-09-22 after hand-back

### 10.1 🟢 The substitution series verified locally — and one member must be EXCLUDED

Re-read from `analysis/data/WWOX_ThermoMPNN_saturation.csv` at `position = 229` (0-based),
`wildtype = Q` confirmed:

| substitution | ΔΔG | what it perturbs | usable as a discriminator? |
|---|---|---|---|
| **Q230M** | **0.3047** | side chain present, **amide absent** | 🟢 isolates the **H-bond chemistry** |
| **Q230A** | **0.5800** | side chain removed past Cβ, **backbone normal** | 🟢 isolates the **side-chain network** |
| Q230L | 0.9882 | bulky, non-polar, backbone normal | 🟡 redundant with A/M |
| **Q230P** | **1.5143** | **backbone NH removed, φ constrained** | 🟢 the **backbone** arm |
| **Q230G** | **1.5994** | ⚠️ side chain removed **AND** backbone flexibility added | 🔴 **NO — confounded** |

✅ `Q230A`, `Q230G`, `Q230L`, `Q230M` each appear **0 times** in the entire repository at `HEAD`. The
series is genuinely unused. ✅ `P` ranks **4th of 19**, as reported — and the reason matters: **a ΔΔG
rotamer model cannot see a backbone lesion**, which is why it disagrees with ESM2's 1st.

🔴 **My addition, and it is a trap in the proposal itself: `Q230G` scores HIGHEST of all five — above
`Q230P` — and must NOT be used as the discriminator.** Glycine removes the side chain **and** adds
backbone freedom, so it perturbs **both** variables at once and cannot separate them. Anyone picking
arms by ΔΔG rank would choose it first. **The clean design is `Q230A` (side chain) + `Q230M` (amide)
against `Q230P` (backbone); `Q230G` belongs nowhere in this comparison.**

### 10.2 🟢 Lou 2018 VERIFIED — and it is STRONGER than reported

According to PubMed: Lou et al. 2018, *Protein Pept Lett* 25(3):230–235,
[DOI](https://doi.org/10.2174/0929866524666171113113100), *C. absonum* 7α-HSDH — **an SDR**. Verbatim:

> *"Although most of the mutations in β-sheet core predicted by MAESTRO **became more stable than wild
> type, unfortunately, all the mutations suffered dramatic activity loss**."*
> *"thermostability of the two mutants, **A104P and G105P** … resulting from the **proline substitution
> method decreased significantly**"* · *"activity of the five mutants … **A104P and G105P cannot be
> detected**"* · *"CA 7α-HSDH may suffer **structural destruction** resulting from the proline
> substitution"*

🔴 **Two facts not carried in the report, and both sharpen it:**
1. *"**Although all the mutants' activities decreased**"* — **every one of the seven**, including the
   stabilising ones.
2. The **best** case, `L197E`, *"maximally maintained **28.7%** of catalytic efficiency."*

> ⇒ **The correct statement is not "stabilising the core can produce dead protein". It is: in this
> SDR, across the entire engineered panel, STABILISATION AND ACTIVITY WERE ANTI-CORRELATED, and the
> single best stabilising mutant retained barely a quarter of activity.**

**Why this is the most therapeutically consequential finding of the wave:** it is a **fold-matched**
warning that raising stability in an SDR does not deliver function, arriving independently of WWOX —
and it converges on `P282A`, the repository's own stable-but-dead WWOX variant. **It reinforces the
`functional assay UNMET and decisive` verdict from the fold-family side**, and it means the **±30 °C
arm of the recommended experiment measures SOLUBILITY rescue only — a solubility rescue would not
license expecting function.**

🔴 **Firewalls, and none may be dropped:** a **bacterial** enzyme; **engineered** mutations, not
disease variants; **thermostability engineering**, not pharmacological chaperoning; activity assayed
on **taurocholic acid**, a substrate WWOX does not share; and WWOX has **no validated activity assay
at all**, which is the whole problem. `WHAT TRANSFERS`: the **anti-correlation pattern** and the
**design warning**. `WHAT DOES NOT`: any quantitative expectation for WWOX.

### 10.3 🟢 The position-230 coincidence trap VERIFIED — and it is worth keeping

Miura et al. 2008, *Chem Biol Interact* 178(1–3):211–4,
[DOI](https://doi.org/10.1016/j.cbi.2008.10.005). Verbatim: *"the tryptophan residue at position 230
is highly conserved while **human CBR3 possesses rigid amino acid, proline, at that position
instead**"*; *"The substitution of tryptophan for proline in hCBR3 **failed to affect the enzymatic
characteristics**"*; *"the substitution of the amino acid residue at position **230 alone has no
apparent impact**."*

> 🔴 **Another SDR-family member carries PROLINE AT POSITION 230 as WILD TYPE, and swapping it changes
> nothing.** A search for *"proline 230 SDR"* surfaces this first and it says **nothing whatever about
> WWOX** — different protein, different numbering, different position in the fold. **A number
> coinciding is not a position coinciding.** Kept as a **tripwire**, exactly as the `GTPBP3 p.Q230P`
> namespace trap is kept.

### 10.4 On the `rs3764340` resolution

🟢 The route is better than the one I would have taken. gnomAD, dbSNP, Ensembl and 1000 Genomes are
all `connect_rejected`, and rather than stopping there the search went to **primary case–control
tables, which report genotype counts** — a **higher** resolution than an aggregate MAF, because it
yields **homozygote counts directly**. **18 individuals homozygous for `P282A` enrolled as healthy
adult cancer-free controls**, with the meta-analysis's **homozygous model null** (GG vs CC OR 1.36,
CI **0.90–2.04**) and ClinVar **Benign, multiple submitters, no conflicts**.

⚠️ **The classification `OVEREXPRESSION-ARTEFACT SUSPECT` is the right call and `PARTIAL-LOSS CONTROL`
is correctly refused** — the latter would assert a partial-loss magnitude nobody has measured. **My
earlier flag is thereby resolved**: I raised the common-SNP tension without a frequency; the frequency
now exists, and it settles the tension against the "complete null" reading.
