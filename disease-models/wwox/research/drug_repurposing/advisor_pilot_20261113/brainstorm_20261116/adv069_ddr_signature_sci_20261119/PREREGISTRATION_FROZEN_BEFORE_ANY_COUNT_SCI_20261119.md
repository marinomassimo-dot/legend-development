# ADV-069 pre-registration, frozen before any DNA-damage gene value is opened (SCI, 2026-11-19; hypothesis level; no dose, no recommendation; not medical advice)

Question (ADV-069, census choice B). Does the deposited organoid transcriptome (GSE156243) carry a DNA-damage or p53-response signature that (a) is present in both knockout clusters, (b) survives normalisation to proliferation and to neuronal and progenitor composition, and (c) lies outside what random gene sets of matching expression do? And, whatever it shows, what does it change: does any DNA-damage-directed class enter the comparison set at all?

## What the finding is, and what this step can and cannot test (stated from the paper's text, read before this freeze)
* The DNA-damage-response defect in the source paper (Steinberg and colleagues 2021, the organoid paper behind the deposit) is a **protein and imaging finding**: gamma-H2AX and 53BP1 foci in the innermost ventricular-zone layer of **week-6** organoids (gamma-H2AX 1.5 against 0.78 foci per nucleus, rescued by AAV re-expression; 53BP1 similar; wild type 8 and knockout 12 organoids from 3 batches), gamma-H2AX with Ki67 in week 10, a fall in cleaved caspase-3 in the same layer (read by the authors as loss of checkpoint inhibition), and similar foci in WOREE-derived organoids; **SCAR12 forebrain organoids show no difference**. The deposit is a **week-15 bulk transcriptome**, so this step is a **transcript-level, later-age cross-check of an imaging finding at an earlier age; it cannot show DNA damage.**
* **Retrospective elements** (the authors' text reports them; I have not computed them): MDM2 lower; genes of "negative regulation of the cell cycle" lower (the paper's Fig 4B, enrichment analysis). Everything else in the panel below is prospective: I have opened no DNA-damage gene value from this deposit in this session.
* The deposit: hESC line WiBR3, cerebral organoids at 15 weeks, **4 knockout libraries (cko1 to cko4) and 2 wild-type libraries (cwt1, cwt2)**; the authors say two further wild-type libraries failed quality control. **One parental line, one laboratory, one differentiation protocol: one origin.** Whether a library is one organoid or a pool is not stated in the metadata and is not assumed.
* Two knockout clusters: **cko1 + cko2 against cko3 + cko4**, fixed from my earlier whole-transcriptome recomputation for the Wnt and maturation question (not from any DNA-damage gene). IT's reanalysis of the same deposit found maturity and Wnt differing by library (cko3 lowest neuronal and cortical panels, carrying most of the Wnt correlation), so the clusters sit on a maturity axis and the normalisation matters.

## Unit, expression, gene sets (HGNC symbols as used in the count table; fixed now; panels from general knowledge of DNA-damage biology, not from these data; a judgement, not a calibrated list)
* Unit: one library. Expression: log2(CPM + 1) from the deposited Salmon gene counts (CPM per library from the sum of all gene counts). Shift per gene and knockout library = its log2 minus the mean of the two wild-type libraries; signature value per library = mean of the shifts over the genes of a set; cluster value = mean of its two libraries.
* **P53_RESP** (damage-induced p53 target transcripts): CDKN1A, GADD45A, MDM2, BBC3, BAX, PPM1D, SESN1, DDB2, ZMAT3, TP53I3, RRM2B, FAS, TNFRSF10B, AEN.
* **REPAIR_S** (repair genes coupled to S phase): BRCA1, BRCA2, RAD51, RAD51AP1, RAD54L, FANCD2, FANCI, EXO1, TIMELESS, CLSPN.
* **DDR_CORE** (sensors and transducers, largely constitutive): ATM, ATR, CHEK1, CHEK2, TP53, MDC1, TP53BP1, H2AFX, NBN, MRE11, RAD50.
* **CC_NEG** (negative regulators of the cell cycle): CDKN1B, CDKN1C, CDKN2C, RB1, RBL2, BTG1, BTG2.
* Normalisation panels: **PROLIF** (MKI67, TOP2A, CCNB1, CCNA2, CDK1, UBE2C, CENPF, PCNA, MCM2, MCM6, TYMS); **PROG** (SOX2, PAX6, HES1, VIM, NES, FABP7); **NEU** (STMN2, DCX, TUBB3, MAP2, SNAP25, SYT1).

## Normalisations (both must be applied; the verdict needs the signal to survive both)
* **N1 (proliferation):** set shift minus the PROLIF shift of the same library.
* **N2 (composition):** a composite maturity score per library = (NEU shift minus PROG shift); across all six libraries fit set value = a + b x maturity score + c x knockout (1 or 0); c is the genotype term after maturity. Also report c with each single library left out.
* **Null model:** 2000 random gene sets of the same size, drawn from genes whose mean log2(CPM + 1) over the six libraries is within 0.5 of the set's own mean (seeded, seed 20261119); the observed cluster shift is placed in that distribution (two-sided empirical percentile).
* **Noise floor:** the absolute difference between the two wild-type libraries' set values (computed with the same method, each against the other wild-type library); a cluster shift must exceed it.

## Decision rules (thresholds not calibrated)
* **Signal present (S-ok)** for a set: in **both clusters** the N1-adjusted shift has the same sign and magnitude at least 0.3 log2, lies outside the 2.5th to 97.5th percentile of the null, exceeds the wild-type noise floor, **and** the N2 genotype term c has the same sign with magnitude at least 0.3 (and keeps its sign in every leave-one-library-out fit).
* **STOP S1 (ADV's rule): signal in one cluster only** (the other cluster inside the null band, or of opposite sign, or below the noise floor).
* **STOP S2 (ADV's rule): signal lost after normalisation** (N1 or N2 fails the 0.3 criterion).
* **Direction reading, if S-ok:** P53_RESP up = transcriptionally active damage signalling; P53_RESP down = attenuated p53 response (the direction that fits the authors' "loss of checkpoint inhibition" and their lower MDM2); REPAIR_S and DDR_CORE shifts are read only against PROLIF (they track proliferation); CC_NEG down reproduces the paper's retrospective statement and is reported as such.
* The primary set is P53_RESP; the other three sets are reported with the same arithmetic as description.

## What this step cannot show
DNA breaks, their location or their consequence for function; anything at week 6 or week 10; whether any transcript change is cause or consequence of the imbalance of cell populations in the knockout organoids; independence (one line, one laboratory); effects in vivo or in any child; any pharmacological effect. A signal here would not make a DNA-damage-directed agent a candidate; it would only keep the row alive as a one-origin observation with a transcript-level echo.

## Decision it changes (stated before the run)
S-ok in the primary set: the row stays a one-origin observation with a transcript-level echo, and the cheapest next observation is a repair-pathway marker read (gamma-H2AX or 53BP1 foci with and without the rescue vector) at weeks 6 and 15 in the same line; **no DNA-damage-directed class enters the comparison set on this evidence in either case**. S1 or S2: the row stays a descriptive imaging observation in one line and the question is closed for tonight.
