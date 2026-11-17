# Predictions: unread per-class transcripts (Cacna1g, Ldha, Ldhb, Hk1, Pkm, Slc2a1) in the two held nuclei sets (SCI, 2026-11-17 06:5xZ; written and hashed BEFORE the tables are opened; hypothesis level; transcripts only, not function)

**Unit and sets (first line):** both datasets are one animal or pool per arm in the S-line set and three animals against three in the neocortex set. (a) GSE158684: S-line hippocampus, P17, nucleus unit, pooled per genotype, n = 1 per arm, intervals over nuclei are pseudo-replicated; (b) GSE334405: PV-Cre Scn1a F/+ against +/+ neocortex, 6 months, per-animal pseudobulk 3 against 3, its own genotype control failed ([4d]). A transcript is not function. Not a Wwox statement in (b).
**Rule (as [4c], [4d]):** marker-set argmax classes; a gene is READABLE in a class if at least 30 nuclei express it in each arm (in (b), summed over animals per group); C = log2 mutant over control; bins: C below -0.4 LOW, -0.4 to +0.4 inclusive MIDDLE, above +0.4 HIGH (edge value goes to MIDDLE). Classes read: excitatory, inhibitory, astrocyte. Scripts: copies of `c4c/snuc_4c.py` and `c4d/snuc_multi.py` with only the gene list replaced (digests in the message that carries this file). One run per dataset.
**Consumer:** I21 step 2 (Ldha and Ldhb are the premise of the Ldh-type hit), I4 and I1 resource class, T-type cells, RP-023.

## Predictions (probabilities mine; IPOTESI)
Readable = P(at least 30 nuclei express in both arms). Bins = P(LOW / MIDDLE / HIGH) given readable. Naive baseline: readable 0.9 and bins 0.1 / 0.8 / 0.1 for every row (housekeeping genes sit near zero).
| dataset | gene | class | P(readable) | LOW / MIDDLE / HIGH |
|---|---|---|---|---|
| (a) S-line | Ldha | excitatory | 0.92 | 0.15 / 0.65 / 0.20 |
| (a) | Ldhb | excitatory | 0.90 | 0.15 / 0.60 / 0.25 |
| (a) | Pkm | excitatory | 0.95 | 0.15 / 0.70 / 0.15 |
| (a) | Hk1 | excitatory | 0.80 | 0.20 / 0.60 / 0.20 |
| (a) | Cacna1g | excitatory | 0.50 | 0.25 / 0.50 / 0.25 |
| (a) | Cacna1g | inhibitory | 0.10 | not scored |
| (a) | Slc2a1 | excitatory / astrocyte | 0.30 / 0.55 | not scored |
| (a) | Ldha, Ldhb | astrocyte | 0.80, 0.85 | not scored |
| (b) neocortex | Ldha | excitatory | 0.97 | 0.10 / 0.75 / 0.15 |
| (b) | Ldhb | excitatory | 0.95 | 0.10 / 0.70 / 0.20 |
| (b) | Pkm | excitatory | 0.97 | 0.10 / 0.80 / 0.10 |
| (b) | Hk1 | excitatory | 0.85 | 0.15 / 0.70 / 0.15 |
| (b) | Cacna1g | excitatory | 0.60 | 0.20 / 0.60 / 0.20 |
| (b) | Cacna1g | inhibitory | 0.10 | not scored |
| (b) | Slc2a1 | excitatory / astrocyte | 0.40 / 0.70 | not scored |
| (b) | Ldha, Ldhb | astrocyte | 0.90, 0.90 | not scored |
**Step-2 statement (the one the I21 bridge needs):** P(Ldha and Ldhb are both readable in excitatory nuclei in both datasets) = 0.85. If it holds, step 2 is passed and says nothing about whether a Wwox-null neuronal phenotype is metabolic. Not predicted: any Wwox row, any composition row.
## What would change my reading
A LOW or HIGH bin for Ldha or Ldhb in (a) would be the first neuronal transcript hint of the glycolytic shift in a Wwox neuronal deletion (n = 1 per arm: not significance); in (b) it would show that the shift is a state of epileptic tissue, not of Wwox. Both are exploratory.
