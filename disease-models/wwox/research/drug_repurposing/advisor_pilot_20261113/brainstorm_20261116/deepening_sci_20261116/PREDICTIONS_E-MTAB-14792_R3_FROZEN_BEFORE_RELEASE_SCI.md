# Predictions for the processed matrix of E-MTAB-14792 (2026 organoid scRNA-seq), written and hashed BEFORE any release or access (SCI, 2026-11-17; hypothesis level; transcripts only, not function; human fetal-like neurons; tier 2 at most)

**Unit and design as I know them (from the paper text only; the matrix itself is not accessible and I have seen none of it):** week-16 neural organoids, 18,007 cells, four genotypes (WT, isogenic WWOX KO, WOREE-derived, SCAR12-derived), 12 clusters (radial glia, neural progenitors, early and late neurons); the number of organoids per condition is not stated in the text I read, so the cell is the unit, pooled per genotype, intervals pseudo-replicated, no significance claimed. A transcript is not function.
**Rule (as [4b] to [4d], [5]):** classes from the deposit's own cluster labels if present; otherwise marker-set argmax (radial glia VIM, SOX2; outer radial glia CRYAB; neurons TUBB3, SATB2, DCX, SYT1; astrocyte-like GFAP, S100B, GJA1). A gene is READABLE in a class if at least 30 cells express it in each of the two genotypes compared. C = log2 mutant over WT of pooled counts per class (log2 CPM + 1 form as before); bins LOW below -0.4, MIDDLE -0.4 to +0.4 inclusive, HIGH above +0.4 (edge value goes to MIDDLE). Contrasts: KO against WT (primary), WOREE against WT, SCAR12 against WT. Class read for prediction: **all neurons pooled (early plus late)**; a second read, late neurons only, is reported without prediction because the mutants carry fewer late neurons. Naive baseline: readable 0.9 and bins 0.1 / 0.8 / 0.1.
**Consumers:** the arm-table cells listed in `TRANSFER_QUALIFICATION_NOTE_SCI_20261117.md` section 'Revision 3' (up to 17 of 75), I21 step 2 in human neurons.

## Predictions (probabilities mine; IPOTESI). Primary contrast KO against WT, all neurons pooled
| gene | P(readable) | LOW / MIDDLE / HIGH given readable | note |
|---|---|---|---|
| GABRB2 | 0.80 | 0.45 / 0.45 / 0.10 | bulk RNA-seq of KO organoids put it among the top-100 down |
| GABRB3 | 0.85 | 0.45 / 0.45 / 0.10 | same |
| GABRD | 0.20 | not scored | few neurons express it |
| GABRA5 | 0.20 | not scored | |
| GAD1 | 0.85 | 0.10 / 0.55 / 0.35 | bulk: up |
| GAD2 | 0.85 | 0.10 / 0.55 / 0.35 | |
| SLC12A2 (NKCC1) | 0.95 | 0.20 / 0.50 / 0.30 | an early-cell gene; mutants have more early neurons |
| SLC12A5 (KCC2) | 0.45 | 0.50 / 0.40 / 0.10 | late-neuron gene; mutants have fewer late neurons |
| GRIN2B | 0.95 | 0.15 / 0.65 / 0.20 | |
| GRIN2A | 0.80 | 0.10 / 0.60 / 0.30 | bulk: up |
| KCNQ2 | 0.80 | 0.25 / 0.55 / 0.20 | |
| KCNK2 | 0.50 | 0.20 / 0.60 / 0.20 | |
| SCN1A | 0.70 | 0.40 / 0.50 / 0.10 | late-neuron signature gene: a maturity effect, not Nav1.1 loss |
| CACNA1G | 0.35 | not scored | |
| CACNA1H | 0.30 | not scored | |
| CACNA1I | 0.40 | not scored | |
| LDHA | 0.97 | 0.15 / 0.60 / 0.25 | |
| LDHB | 0.90 | 0.15 / 0.65 / 0.20 | |
| PKM | 0.98 | 0.15 / 0.60 / 0.25 | |
| HK1 | 0.80 | 0.20 / 0.60 / 0.20 | |
| SLC6A1 | 0.80 | 0.15 / 0.65 / 0.20 | |
| SLC6A11 | 0.30 | not scored | astrocyte-like only |
| KCNJ10 | 0.15 | not scored | |
**Statement the bridge needs:** P(LDHA and LDHB both readable in neurons in the KO and WT pools) = 0.88; P(inhibitory-neuron identity can be read as its own class, at least 30 cells expressing GAD1 and GAD2 in each of KO and WT within one cluster) = 0.35.
**Secondary (WOREE and SCAR12 against WT):** I expect the same signs as KO with smaller sizes for GABRB2, GABRB3 and SCN1A (P = 0.6 that the SCAR12 value is closer to zero than the KO value in each), because the paper reports a milder gradient.
## What would change my reading
A GABRB2 or GABRB3 fall in neurons of the KO matrix that is absent once early and late neurons are compared separately would be a maturity effect; a GAD1 rise present in every neuron class would support the organoid GABAergic-marker finding and keep the H7 conflict with the mouse hippocampal Western blot open. Scored literally by IT from the table; none of it has been seen.
