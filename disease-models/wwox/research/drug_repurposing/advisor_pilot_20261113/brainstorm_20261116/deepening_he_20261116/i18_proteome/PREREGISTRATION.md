# I18 · the PY-motif proteome test: PREREGISTRATION (HE, 2026-11-16; written and committed BEFORE any fold change is joined to any motif; non-canonical; hypothesis; not medical advice)

Written for: ADV (conditions i to iv of the meeting reply), SCI, IT. Mechanism level; reference genotype class only.

## Question and why this table
If the WW1 domain of WWOX competes with, or hands over, NEDD4-family ligases at PPxY motifs, then proteins that carry such a motif should move together, at the protein level, when WWOX is silenced: down under the shield variant (M−), up under the adaptor variant (M+). The held table is the one protein-level WWOX perturbation held: TMT mass spectrometry of WWOX-silenced human endothelial cells against control (Zeng 2024, PMID 38563965, Supplemental Table 1, held as a PDF with a clean text layer). No neural assumption is needed. Limits stated now: endothelial cells (non-neural), partial siRNA silencing, the number of independent biological samples is not stated in the text read here ("run in triplicate" is all the methods say about the MS run: biological n UNKNOWN), the silencing efficiency is not stated in the text read here (a keyword search for efficiency found nothing; WWOX protein itself is not a row of the table: UNKNOWN), mRNA of the same samples is not held, and the table is of 2,031 quantified proteins (20 decoys excluded), i.e. the abundant part of the proteome.

## Inputs fixed now (sha256)
* `Supplemental_Table_1.pdf` as held: 774aa45d9eff2d7ffe33a30f74bb09b0d8fc9be0b6dec70dc1b94d6a947e525c; parsed by `parse_zeng_table.py` (2,031 real rows, 20 decoy rows excluded, 0 unparsed) into a TSV kept outside git (third-party table): sha256 of that TSV cae297dce11b3b61cb20ab46ec05799fa30c28dae1099b761cb57ce5be980090.
* Sequences, topology and transmembrane annotation of the 2,031 accessions: UniProtKB public REST, generic client, no contact data; to be fetched AFTER this file is committed; their digest goes into the result file.
* Disclosure of what I have seen: the first 22 rows (AAMDC to ACAT2), NEDD4 (log2FC +0.33, BH 0.016) and the absence of a WWOX row; nothing else of the fold changes of any protein with a motif.

## Carriers and controls
* **Primary carriers (P):** at least one PPxY (regex PP.Y, overlapping) in a part of the protein that is not extracellular or transmembrane: for entries with topology annotation, the annotated cytoplasmic segments; for entries without it, every residue outside annotated transmembrane segments (so a soluble protein is read whole).
* **Secondary carriers (S):** PPxY anywhere in the sequence. **Tertiary (T):** LPxY and no PPxY, same region rule as P.
* **Decoy motifs, same region rule, proteins carrying a PPxY excluded from the decoy sets:** PPxF and PPxA (same proline pair, a residue the ligase does not read in place of Y). A shift of proline-rich proteins in general would show in the decoys.
* **Non-carriers:** quantified proteins that carry none of PPxY, LPxY or the decoys in the same region.

## Statistic
Strata: intensity decile (decile of the mean of the two log2 normalised intensities over the whole table) crossed with compartment (membrane = at least one annotated transmembrane segment in UniProt; soluble otherwise). Strata with fewer than 3 carriers or fewer than 3 non-carriers are dropped (their number is reported). Within each stratum the difference of the median log2 fold change (carriers minus non-carriers); **D** = the carrier-count-weighted mean of the stratum differences. Permutation p: carrier labels shuffled within strata, 10,000 draws, seed 1, two-sided. Interval: stratified bootstrap (carriers and non-carriers resampled within stratum), 5,000 draws, seed 1, 95% percentile interval for D. The same D, p and interval are computed for S, T and the two decoys. Secondary descriptive only (no decision): the share of carriers with BH-adjusted p < 0.05 up and down against non-carriers; the stratum differences; D with proteins ranked in the top 5% of intensity removed.

## Decision rules (both signs; fixed now)
* **SUPPORT M− (shield: carriers fall):** D(P) ≤ −0.05 log2, permutation p < 0.05, and |D| of each decoy below half of |D(P)|.
* **SUPPORT M+ (adaptor: carriers rise):** D(P) ≥ +0.05, p < 0.05, same decoy condition.
* **KILL, for this table:** the 95% interval of D(P) lies entirely inside (−0.05, +0.05). A kill is written as a kill of "PY competition at WWOX WW1 changes protein level" in this one table, with the table's limits (endothelial, partial silencing, unknown n), not as a kill of the idea in neurons.
* **INCONCLUSIVE:** anything else (interval crosses ±0.05, or a decoy shifts as much as P).
* 0.05 log2 is a 3.5% change in abundance; it is chosen before any fold change is joined, and the width of the interval is the power statement (a kill is allowed only if the interval is that narrow).

## What would be written next, whichever way it falls
A SUPPORT gives the sign the P47T arm cannot give, and a list of the carriers that move (for IT and SCI to match with channels). A KILL removes the protein-level reading of I8 from this table and leaves I8 as the Nav-density and interneuron-amplitude route only. INCONCLUSIVE says what the table cannot decide.
