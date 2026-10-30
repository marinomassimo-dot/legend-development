# Minimal discriminating design for the ACK1 lever on WWOX protein (IT11 P2.4, scientist-d, 2026-10-30)

Non-canonical research material. A design for discussion with the scientific referent. **Nothing in this file has been executed.** No result is stated. Not medical advice; reference genotype class only. Concentrations, times and cell choices are proposals to be fixed with the referent, and anything marked (proposal) is not sourced.

## 0. The question, in one sentence

In a cell that already makes WWOX protein, does loss of ACK1 activity (by genetics and by chemistry) raise steady-state WWOX and lengthen its half-life, and does the compound effect disappear when ACK1 is absent or the Tyr287 site is mutated?

The design answers **amount and stability only**. Function is a separate, later question (section 6). It does not test Q230P unless a band is found first (gate G0).

## 1. Gates (order matters; each is a stop/go for the next)

| Gate | Question | Pass | If it fails |
|---|---|---|---|
| G0 | Is there a WWOX band in the chosen WWOX-variant system (Q230P fibroblast, residual-protein organoid)? | band with two antibodies against different epitopes, or enrichment by immunoprecipitation, with a WWOX-null control that lacks it | Variant arm is not run; only the wild-type arms (A, B) are run and the result is labelled "mechanism in WWOX-present cells, no variant relevance" |
| G1 | Does the published direction reproduce in a positive-control system? (Arm A) | ACK1 loss raises WWOX in cells that show it in the literature | If not reproduced in either control line, the lever is not reproducible in my hands; stop; no neural arm |
| G2 | Does a neural/neural-like WWOX-present system show any ACK1-dependent change? (Arm B) | genetic TNK2 loss changes WWOX amount or half-life | Lever is cancer-context only; priority falls (section 5) |
| G3 | Do both chemistries agree with the genetic result and is the compound effect ACK1-dependent? | see section 4 | Compound effect without genetic agreement = off-target |

## 2. Cells (WWOX-present systems first)

| Arm | System | Why | What it cannot tell |
|---|---|---|---|
| A (positive control) | A line with published ACK1-dependent WWOX: MHCC-97H (liver; PMID 25738261 knockdown datum) and/or LNCaP with active ACK1 (PMID 16288044 abstract) | Reproduce the direction before spending anything on neural cells | Nothing about neurons or variants |
| B (relevant, wild-type WWOX) | Human neural-lineage cells that express WWOX protein at a measured level (neuroblastoma-type line, iPSC-derived neural progenitors or neurons, wild-type organoid slices) (proposal; WWOX and ACK1 protein levels in each must be measured first, they are not known from this work) | First neural test of the lever | Not a variant |
| C (variant, over-expressed) | P252A in CAL-62 as in PMID 41124647 (the only published variant-plus-compound system), wild type as comparator | Tests whether the ACK1 lever acts on a destabilised SDR-domain missense that is known to go through a lysosome-dependent route; keeps the published chloroquine arm as an internal control | Over-expression; Q230P is a different residue; no transfer |
| D (variant, endogenous) | Q230P patient fibroblasts, SCAR12-class organoids with residual protein | The question that matters for the genotype class | Only if G0 passes; otherwise not run |
| E (genotype control) | The same cell with WWOX knocked out (CRISPR) | Every compound effect on a function readout must be absent here, otherwise it is not WWOX-dependent | - |

## 3. Perturbations

Genetic (the arbiter):
1. TNK2 knockdown with at least two independent sequences (the HCC paper used one: E08), plus scrambled control.
2. TNK2 CRISPR knockout (clone or pool) and re-expression of an RNAi-resistant wild-type TNK2 (rescue), and of a kinase-dead TNK2 (catalytic lysine K158 per the review text, E12; numbering for the construct to be checked) (proposal).
3. Active ACK1 over-expression (as in the primary) with and without kinase-dead; the expected change is down for WWOX.
4. WWOX mutants: Tyr287Phe (insensitive control, not stated in the primary abstract to have been tested for stability: E04), and the exon 5-8 deletion variant already used in the primary as a non-phosphorylated, non-degraded form.

Chemical (concentration-response and time-course, not a single dose):
5. dasatinib and bosutinib (both bind SRC/ABL tighter than ACK1: E15, E16; neither is an independent chemotype for ACK1 specificity).
6. AIM-100 (furopyrimidine, ACK1 IC50 24 nM but LCK 122 nM: E18) and (R)-9b (chloropyrimidine diamine, ligand of 7KP6: E19, E20; kinome selectivity not located). These are structurally distinct from dasatinib/bosutinib and from each other, which is what makes concordance informative.
7. A SRC/ABL inhibitor that binds ACK1 weakly, chosen from the Davis-panel data after the referent agrees (proposal; candidate not named here because I did not verify an ACK1-weak profile). Purpose: if it raises WWOX, SRC/ABL is the cause, not ACK1.
8. Route arms in the same cell: MG-132 (proteasome), chloroquine or ammonium chloride (lysosomal pH), as in PMID 41124647. Note E11: dasatinib and AIM-100 induce adaptive autophagy in a lung model, which touches the lysosomal route.

## 4. Controls that identify ACK1 as the cause (the inference rule)

An effect of a compound is attributed to ACK1 only if all of these hold:
- (i) the same direction and a comparable size with TNK2 knockdown and knockout (two sequences);
- (ii) the compound effect is lost (or much smaller) in TNK2-null cells and is restored by wild-type but not kinase-dead re-expression;
- (iii) the effect is lost on WWOX Tyr287Phe;
- (iv) at least two structurally distinct ACK1 inhibitors agree (dasatinib and bosutinib count as one chemotype family for this purpose; AIM-100 and (R)-9b are the other families);
- (v) the SRC/ABL-weak-ACK1 compound (item 7) does not reproduce it;
- (vi) target engagement is shown in the same cell and dose (ACK1 autophosphorylation, for example Y284 per E12, and a downstream ACK1 mark such as AKT pY176 or the HCC paper's p-AKT), with SRC-family engagement measured in parallel.

## 5. Endpoints

Amount and stability (primary):
- Steady-state WWOX by immunoblot with two antibodies (different epitopes), blot quantification stated, loading control stated, n of at least 3 independent biological replicates (proposal; no power calculation made).
- WWOX mRNA by RT-qPCR in the same samples (the HCC paper did not measure it: E09), so that "protein" is not confused with "transcript".
- Cycloheximide chase (for example 0, 2, 4, 8, 12 h; proposal) with compound versus vehicle and TNK2 knockdown versus control; half-life fitted per replicate; a viability/translation-shutoff control because dasatinib is cytotoxic and shuts off signalling widely; a short-lived protein as chase control.
- Route arms (MG-132, chloroquine) in the chase.
- Phospho-Tyr of immunoprecipitated WWOX (anti-phospho-tyrosine; a Tyr287-specific antibody is not known to exist: UNVERIFIED), ubiquitin on immunoprecipitated WWOX (denaturing IP).

Localisation (secondary, because the Mahajan abstract and the ITCH data both involve compartment, E03, IT10 L15): nuclear/cytoplasmic fractionation with compartment markers, to ask where the surviving protein sits. Descriptive only.

Function (kept separate; chosen with the referent before the experiment, not after): the function readout must be a known WWOX-dependent measure in the chosen cell, shown to change between WWOX-wild-type and WWOX-null cells of the same background, and then tested for (a) response to the compound, (b) absence of that response in WWOX-null cells (arm E), (c) loss of response when the increase in WWOX protein is blocked. Candidate readouts are not proposed here because none of them has been read or chosen in this package (UNVERIFIED which is appropriate).

## 6. Alternative outcomes and what each does to priority

Priority here means research priority of the ACK1 mechanism probe; it is not a claim about benefit, and development requirements (CNS exposure, tolerability) are tracked separately.

| Outcome | Reading | Effect on priority of N12 |
|---|---|---|
| G0 fails (no Q230P band) | The lever does not apply to the fibroblast datum; stays a wild-type-cell mechanism question | Variant relevance stays zero; keep only if arm B/C is positive; the compensation rationale (section 8 of the README) becomes the only route for Q230P and has no evidence |
| G1 fails (published direction not reproduced) | The cancer-context effect is not robust (one shRNA, one line in the HCC paper) | Drop to low |
| Arm A positive, arm B null | Context-restricted lever (cancer cells with active ACK1) | Low for the genotype class; closes the question for neural cells in the tested lines |
| Arm B positive for genetics, compounds disagree with genetics | Compounds act off-target; genetic route real but no drug-like inhibitor | Raise the question of selective ACK1 tools ((R)-9b, degraders), lower the dasatinib/bosutinib entries; development path unfavourable |
| Genetics and at least two distinct chemotypes agree, ACK1-dependent (G3 passes), amount and half-life up | The ACK1-WWOX lever works in neural WWOX-present cells | Raise to "mechanism supported in WWOX-present cells"; still no function claim; next: arm C then arm D if G0 |
| Amount up but half-life unchanged | Not a stability effect; transcription/translation or a loading artefact | Do not call it stabilisation; lower |
| P252A (arm C) responds to ACK1 loss | ACK1 contributes to a missense degradation route | Raise for missense class; test Q230P if G0 |
| P252A responds only to chloroquine, not to ACK1 loss | Lysosomal route independent of ACK1 | ACK1 lever lowered for destabilised missenses; lysosomal arm (T3) stays the lead |
| WWOX up and function unchanged | Protein is not function | Priority unchanged for mechanism, no therapeutic reading |
| Compound lowers viability or translation (chase confounded) | Uninterpretable chase | Repeat at lower dose with shutoff control; do not interpret |
| Compounds raise WWOX also in TNK2-null cells | Not ACK1 | Attribute to SRC/ABL or other; redirects to the compensation question, not to ACK1 |

## 7. Smallest first step (needs no new cell line)

Immunoblot WWOX in Tnk2-null versus wild-type mouse tissue or primary cells where such material is already held by a group (Tnk2-/- mice exist: E21, abstract level), together with the TNK2 knockdown in MHCC-97H with a second shRNA and WWOX mRNA. This tests direction, specificity at the genetic level and the transcript confound before any compound is used. Whether any group would share tissue is UNVERIFIED.

## 8. What this design cannot do

It cannot show benefit, safety or CNS exposure; it cannot show function; it cannot rescue a cell that has no protein; it does not transfer from P252A to Q230P; a negative result in the chosen lines does not close the question for other cell types.
