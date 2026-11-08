# NB-2 (IT35 P7): paired Tau-phospho and beta-catenin readouts by GSK3 inhibitor class

## Answer

* DATO: no source reached reports, in a neuronal system, both a phosphorylated-Tau readout and a beta-catenin readout under two or more GSK3 inhibitors of different class with both readouts stated for each class. This is "not found in the routes searched" (three PubMed strings, Europe PMC open-text check), at abstract depth only; it is not a null.
* DATO: the nearest source is the 2005 study in CHO cells and rat cultured neurons (PMID 16014628): lithium gave beta-catenin nuclear translocation with decreased tau phosphorylation; SB415286 (ATP-competitive) also gave beta-catenin translocation. Tau for SB415286 is not stated in the abstract. Row R1.
* DATO: no class showed a split between the two readouts in any abstract read. The one divergence found is lithium versus SB216763 on MEK/ERK, not on Tau versus catenin (R2).
* DATO: the earlier SH-SY5Y inhibitor series (PMID 39798400) pairs p-tau Ser396 (down) with beta-catenin (up) for one compound, one class (R3). Re-qualified: one class, so it cannot be compared by class.
* DATO: PMID 33621689 (SH-SY5Y) has three inhibitors (BIO, SB216763, lithium) on the Tau side; beta-catenin was reported only for the arsenite insult (R4).
* INFERENZA: of the four alternatives, "readouts move together" is the only one with positive (abstract-level) support; "split by class", "split is off-target" and "no neural source reports both" are not decided. The last is contradicted in part, since single-class neural pairs exist (R1 to R4).
* INFERENZA: a Tau-versus-catenin discriminator for `NEED-GSK3B-DEREPRESSION` has no demonstrated precedent; R1 is a lead for one, conditional on its full text.
* IPOTESI: the discriminator needs its own controls, a lithium arm, an ATP-competitive arm and a substrate-competitive or allosteric arm, each with p-Tau and a Wnt reporter in the same neuronal culture. A split would show only if the arms diverge; the full text of R1 would first show whether SB415286 tau was measured.
* Nothing here promotes a compound, and nothing bears on seizure control, development or quality of life.

## Evidence, depth and gaps

All four sources read were `abstract_only` (PubMed record). Full text was not reachable by an open route: Europe PMC shows no PMC copy or open flag for 16014628, 14511119 or 39798400; the JBC page returned HTTP 403 (a 5,505-byte access stub), and that route was not retried. No methods, figures or magnitudes were read, so assays and effect sizes are `undetermined` except where an abstract states them. R5 and R6 are carried from the module's earlier table and were not re-read. R2's cell type is inferred from the abstract's sentence order (astrocytes) and may not be neuronal.

Substrate-competitive and allosteric compounds (L803-mts, TDZD-8, tideglusib) returned no hit in a paired search (zero hits); that string was narrow, so a real paired source with different wording can exist.

Files: `evidence.tsv`, `queries.tsv`, `receipts/INDEX.tsv` (four staged receipts, suffix 90, each passes the staged check; not recorded).

## Re-audit (verify/audit_nb2.md, blind, abstract depth; own absence searches)
Rows R1-R6 quotes confirmed at abstract level with these corrections: PMID 14511119 concerns **astrocytes** (inferred from the abstract's passage order and MeSH), so it is excluded from the neuronal rows; the lithium divergence there concerns MEK/ERK, not Tau versus catenin; PMID 39798400 is one compound in one series (the abstract supports neither "Western" nor the inhibitor class); the inhibitor-class labels of 16014628 and 33621689 are not in their abstracts; PMID 26819000 is a HEK293 DKK1/LRP6 paper, outside the null; 37235865 stays unverifiable at abstract level; the R1 quote exceeds 25 words. A source the producer left out: PMID 16919965 (cultured neurons: DKK1 lowers the TCF reporter and beta-catenin and raises Tau hyperphosphorylation, lithium rescues in vivo; one GSK3 inhibitor, Wnt perturbed rather than GSK3: it does not break the null). **The null is narrowed**: no abstract-level PubMed record in a neuronal system reports both readouts under two or more GSK3 inhibitor classes; 16014628 (does the full text give a Tau readout under SB415286?) and 33621689 (is beta-catenin measured under the three inhibitors?) need full text and are possible counterexamples; the substrate-competitive and allosteric probe (L803-mts, TDZD-8) was not screened (an OR string returned 333 hits); the PubMed tool ANDs terms and maps "tau" to a journal name, so some probes collapsed. It is not an absence from the primary literature.
