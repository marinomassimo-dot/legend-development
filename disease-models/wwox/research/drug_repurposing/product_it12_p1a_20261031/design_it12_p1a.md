# Minimal discriminating design for the referent (IT12 P1-main, scientist-a, 2026-10-31)

Non-canonical. A proposal for discussion; nothing here was executed; no wet-lab result is claimed. Reference genotype class only. Not medical advice. Cell choices, times and doses are proposals (unsourced).

## Which models (from `models_wwox_protein_it12_p1a.tsv`)

* **Model 1 (variant arm): WPM G372R (SCAR12) organoids or NSC derivatives, with the same-family heterozygous parents (WPM F2/M3) and the WiBR3/JH-iPS11 KO clone as floor.** Only neural, endogenous, patient-derived line with a quantified faint band (0.1-0.3, EV1N). Conditional on gate G0.
* **Model 2 (WWOX-present arm): WT NSCs (WiBR3 WT, strong band, EV5B) and, as a controllable-level arm, AAV9-hSyn-WWOX-treated KO or patient organoids.** Tests whether ACK1 loss changes WWOX amount/half-life in neural cells at all (gate G2 of IT11). Says nothing about a variant.

Q230P fibroblasts, P47T (normal level), WOREE lines, KO and conditional mice are not substrates (table).

## Question

In neural cells that make measurable WWOX, (a) does TNK2/ACK1 loss raise steady-state WWOX and lengthen its half-life, ACK1-dependently, and (b) in the G372R line, is the faint band real protein from the endogenous allele, and does it respond?

## Gate G0 (before any compound)

Faint band must be shown to be WWOX and above floor: two antibodies against different epitopes (N-terminal region and a C-terminal or SDR-domain one; epitope of each stated), KO lane and heterozygote-parent lane on the same membrane, non-saturated WT lane with a dilution series of WT lysate to define linear range and detection limit, IP-then-blot enrichment (or targeted mass spectrometry, proposal) with WWOX-KO IP as control. WWOX mRNA by RT-qPCR in the same samples. Fail: variant arm not run; Model 2 only.

## Perturbations and controls

Genetic (arbiter): TNK2 knockdown with two sequences and scrambled; TNK2 knockout with RNAi-resistant WT and kinase-dead rescue; active vs kinase-dead ACK1 over-expression; WWOX Tyr287Phe (insensitive control; only meaningful on WT-sequence WWOX, so use AAV/transgene arm in KO background). Chemical: dasatinib or bosutinib (one chemotype family for ACK1 purposes), AIM-100, (R)-9b, plus an SRC/ABL inhibitor chosen ACK1-weak with referent (not named here); lysosome (chloroquine, NH4Cl) and proteasome (MG-132) arms. ACK1 target engagement (autophosphorylation, a downstream mark) and ACK1/TNK2 protein in each cell type measured first (not known in neurons, IT10 L24). SRC-family engagement in parallel.

## Endpoints kept separate

1. Steady-state WWOX, two antibodies, linear-range blot, loading control stated, n>=3 independent differentiations (organoid batch is the unit, not the lane).
2. Cycloheximide chase 0-12 h (proposal), compound vs vehicle and TNK2-null vs control, half-life per replicate, translation shut-off and viability control, short-lived protein as chase control; in the G372R line the chase is only interpretable if G0 passed.
3. Route (MG-132, chloroquine) inside the chase.
4. WWOX mRNA.
5. Localisation (fractionation), descriptive.
6. Function, chosen with the referent beforehand, in WWOX-KO background as null control (candidate readouts not proposed here).

## Alternative outcomes and consequence on N12/ACK1 priority

| Outcome | Reading | Priority |
|---|---|---|
| G0 fails in G372R | band is floor or antibody artefact; no variant substrate known in any neural line | variant relevance of the whole stability axis stays zero; N12 falls to low, kept only as WT-cell mechanism question |
| G0 passes, band >= floor, TNK2 loss raises it, two chemotypes agree, ACK1-dependent | lever works on a destabilised endogenous neural missense | rise: first variant-relevant support; then function |
| G0 passes, no response to ACK1 loss but chloroquine raises it | lysosomal route independent of ACK1 | ACK1 down, lysosomal arm (T3) up |
| Model 2 negative (WT neural cells: no ACK1 dependence) | cancer-context only | down |
| Amount up, half-life unchanged | not stabilisation | down |
| Compound effect persists in TNK2-null | off-target (SRC/ABL) | redirects to compensation question |
| Protein up, function not | protein is not function | mechanism only, no therapeutic reading |
| Band unchanged and stable-but-inert (G372R function absent) | more protein would not help | lever moot for that allele |

Smallest first step: G0 on existing lysates (a blot, no new cells) at the lab that holds them.

## Cannot do

Benefit, safety, CNS exposure, transfer G372R -> Q230P (different residues, different cells), function. The group holding the lines (Aqeilan lab) is the natural partner; nothing was sent.
