# Priority questions as usable briefs (IT45)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Reuses the investigations table, the open-questions map (rows IT45-Q01..Q03) and the packages named; creates no registry. Ordered by the decision that the answer could change most, not by the number of publications. The K2P-pH relation belongs to SCI45 and is not repeated here.

## B1. INV-08: which KEAP1 reagent pair separates an NRF2-dependent from an NRF2-independent benefit?
* **Decision it can change:** whether the first NRF2 experiment uses one covalent modifier and one non-covalent binder with NFE2L2 knockdown (IT45 design), or only a genetic arm; whether the non-covalent binder is reachable as a reagent.
* **Unresolved premise:** NRF2 protein, nuclear NRF2 and target-gene activity in a WWOX-deficient neural system, per compartment (a new measurement); and what the NRF2-siRNA arm of the binder's source actually showed (values not retrieved in IT45).
* **In-silico work still useful:** read in full the five documents seen only as abstract or database copy (PubMed ids in `generation_it45_20261111/verify_s10/VERDICTS.md`), including the knockdown results of the non-covalent binder and the cell lines and times of the fumarate-ester and sulforaphane values; the primaries of the one catalogued NRF2-lowering row (protein-synthesis effect, concentrations); whether any NRF2 activator or KEAP1 binder has data in neurons or astrocytes.
* **Indispensable measurement:** target-gene set (not NQO1 alone) with and without NFE2L2 knockdown, neurons and astrocytes separately.
* **Favours the alternatives:** loss of effect under knockdown for both compounds favours NRF2-dependence; an unchanged effect favours an independent mechanism (H5); a compartment-specific effect reopens H3.
* **Stop criterion:** stop reading when each of the five documents has a full-text row or a bounded not-reached with the routes tried; stop proposing a compound pair if the binder has no cell-level NRF2-dependence result in any source.

## B2. INV-18: can a Kv7 conductance arm be told from generic hyperpolarisation, and are the channels there at the right age?
* **Decision it can change:** whether the Kv7 opener arm (IT45-Q01, R5) is posable or the Kv7 abstention stays for the experiment too.
* **Unresolved premise:** Kv7 expression in P13–17 layer II/III pyramidal cells (the RNA held is P7 whole-cortex neurons); the Kv7 current at the resting potential and how far an opener shifts activation (the V10 card says the current starts near −70 mV).
* **In-silico work still useful:** a cell-class-resolved expression source at P14–P28 for Kcnq2, Kcnq3, Hcn1, Hcn2 and Kcnj10 (public single-cell cortex data, no download without the existing hash-record route); primary papers on opener-induced shifts in the half-activation voltage in cortical neurons.
* **Indispensable measurement:** the Ba2+-, Kv7-blocker- and Ih-blocker-sensitive difference currents by genotype in the same slices, then the opener arm against an equal current-injection hyperpolarisation.
* **Favours the alternatives:** a smaller Kv7 difference current in the mutant favours (d); an opener better than equal injection favours a Kv7-specific benefit; equal to injection, a generic one; no effect, an inert lever.
* **Stop criterion:** stop if Kv7 genes are low in the P14–P28 pyramidal class; stop reading when each gene has a figure or a bounded not-found with the search strings.

## B3. INV-18 (S12): is astrocytic K+ buffering altered in Wwox-deficient tissue, and is there any Kir4.1/Kir5.1 activator in deposited data?
* **Decision it can change:** whether the astrocytic buffering explanation is carried as a measurement question only (IT45 default) or reopened as a repurposing one; whether Kir4.1/Kir5.1 appears in a Wwox expression dataset at all.
* **Unresolved premise:** Kir4.1 and Kir5.1 amount and function in Wwox-deficient astrocytes (nothing held); Kir5.1 has no ChEMBL target record.
* **In-silico work still useful:** Wwox-deficient astrocyte or glia transcript/protein datasets for Kcnj10, Kcnj16 and Aqp4; Kir4.1 modulator literature outside ChEMBL (primary papers).
* **Indispensable measurement:** Kir4.1-dependent current and extracellular K+ clearance in Wwox-deficient astrocytes.
* **Favours the alternatives:** a reduced Kir4.1 current or slower clearance favours the buffering explanation; normal values leave K+ buffering out of the model.
* **Stop criterion:** stop when a dataset answers expression, or when no dataset exists and the search strings are stated.

**Update 2026-11-11 (IT46 P4).** B2: the 'equal current-injection hyperpolarisation' arm is replaced (see `../generation_it46_20261111/p4_audit_it46.md`). B1: add an exposure-matching phase 0, a second knockdown reagent, an NRF2-independent control gene set and a WWOX genotype factor to the SCI46 comparison rows.
