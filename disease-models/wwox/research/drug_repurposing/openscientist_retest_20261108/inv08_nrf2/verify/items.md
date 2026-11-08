# Items for the blind verifier (statement, report anchor, source, locator hint, class) — the producer's reasoning and prior-check notes are withheld

## D01
- statement: DATO (module record, one blot): GSK-3beta Ser9 phosphorylation is lower with total GSK-3beta unchanged in Wwox-null mouse brain at P20, and lithium reduced PTZ seizure stage in all genotypes including wild type; INFERENZA: this is a regulatory proxy, so GSK-3beta as elevated causal node (link 1 of the chain) is not established, and the report's three-region claim is not located.
- report anchor: L30; L52-54; E03 E04
- source cited or found: PMID 32000863 (cited); module records wwox_table W10, W11
- locator hint: Results, GSK-3beta blot and PTZ-lithium figure
- class: WWOX datum

## D02
- statement: DATO: the GSK-3beta to Fyn/Src nuclear-import step and the Tyr568 export step are cited to PMID 21690096, an article retracted in full (notice PMID 28159761, expression of concern and correction January 2016); INFERENZA: links 2 and 3 have no usable support in the report; the retraction does not prove the relation false.
- report anchor: L30; L59-62; E05 E06 E07 E09
- source cited or found: PMID 21690096 retracted by PMID 28159761
- locator hint: retraction notice text (reason unreached by every route so far)
- class: transfer from other system

## D03
- statement: DATO (abstract, liver of diabetic mice with zinc chelation): lower Nrf2, lower GSK-3beta phosphorylation and more nuclear Fyn co-occur; the authors propose Akt restrains Fyn nuclear entry. INFERENZA: this corroborates co-occurrence in liver only; it does not show GSK-3beta drives Fyn, nor Fyn phosphorylating NRF2 Tyr568, nor any neural effect.
- report anchor: L30; L105; E08
- source cited or found: PMID 23251339 (read this session)
- locator hint: Results, nuclear Fyn and Nrf2 panels; Discussion
- class: transfer from other system

## D04
- statement: DATO (abstracts, earlier package): a GSK-3 beta to beta-TrCP route (Neh6 phosphodegron) lowers NRF2 stability in fibroblasts and mouse liver/hippocampus, independent of the retracted Fyn chain; two papers from one laboratory line. INFERENZA: the only candidate GSK-3beta to NRF2 mechanism that survives is not mentioned by the report and has no WWOX measurement.
- report anchor: not in report (absent); compare L30
- source cited or found: PMID 21245377; PMID 22751928 (earlier package)
- locator hint: Results: mutant 6S/6A ubiquitination; hippocampal GSK-3beta absence
- class: transfer from other system

## D05
- statement: INFERENZA: 'NRF2 is impaired in WWOX deficiency' is a prediction; no NRF2 protein, nuclear NRF2 or NQO1 activity is reported in any WWOX-deficient mammalian neural system. Absence perimeter: PubMed tool (WWOX/Wwox with NRF2/Nrf2/NFE2L2/KEAP1) 1 hit (hepatocellular cancer cells), Europe PMC title/abstract same string 1 hit, plus redox/neural string 3 hits (none an NRF2 measurement), searched 2026-11-08; module transcripts are mixed (organoid NFE2L2 and NQO1 lower, HMOX1 higher; shWWOX NFE2L2 lower, NQO1 higher; MEF early higher).
- report anchor: L9; L82; L118; E02 E13 E56
- source cited or found: report itself; module needs/needs.json NEED-REDOX-NRF2 O1-O3; queries Q01-Q03
- locator hint: wwox_table W01-W08
- class: absence

## D06
- statement: DATO (abstract): RTA 408 given after status epilepticus in a rodent acquired-epilepsy model reduced late seizures by 94 percent and raised ATP; INFERENZA: this is a prevention/disease-modification result after an insult, not evidence that KEAP1 inhibition helps a genetic developmental encephalopathy; transfer needs a WWOX-deficient system and a dependence control. RTA 408 is the compound the module calls omaveloxolone.
- report anchor: L17; L19; L96; E33 E38
- source cited or found: PMID 29538645 (read this session)
- locator hint: Results, in vivo status epilepticus experiments
- class: compound/class

## D07
- statement: DATO (titles only, not read): constitutive NRF2 activation in transgenic mouse heart causes reductive stress and cardiomyopathy. INFERENZA: a ceiling for brain is not shown; the report's titration advice is an IPOTESI; already-high NRF2 in WWOX would not by itself prove harm from more activation.
- report anchor: L22-24; L99-100; E39 E41 E54
- source cited or found: PMID 40729961; PMID 24747945 (identity checked, abstracts not read)
- locator hint: Results, transgenic dose groups; Discussion on tissue specificity
- class: transfer from other system

## D08
- statement: INFERENZA: NAC as an NRF2-independent antioxidant-only control is an assumption not supported by a cited source; NAC (glutathione precursor, thiol donor) can leave redox signalling pathways, so benefit from NAC without NRF2 activation would show redox-sensitivity, not NRF2 independence. IPOTESI: use NAC as one comparator with NFE2L2 loss as the dependence control.
- report anchor: L13; L35; L42; L134; E25 E67
- source cited or found: PMID 23140664 and PMID 36130098 (cited for PV rescue, not read)
- locator hint: Methods, NAC arm and controls
- class: binding/action/benefit

## D09
- statement: INFERENZA: Wwox;Nfe2l2 double mutant plus re-expression is a valid epistasis design only if Nfe2l2 loss alone has no phenotype in the readout; the cited precedents are stroke (adult Nrf2-KO, sulforaphane) and primary cultures (tBHQ, astrocytic Nrf2); a cell-based NFE2L2-loss cross answers the question earlier than a new mouse.
- report anchor: L40; L51-53; L131; E28 E64
- source cited or found: PMID 36244590 (abstract read this session); PMID 14762128 (earlier abstract)
- locator hint: Methods, KO and rescue groups; Results, Nrf2-KO versus WT
- class: independent confirmation or same-origin reuse

## D10
- statement: DATO (abstract, sepsis brain inflammation): sulforaphane protection was lost in Nrf2-KO at the lower exposure with a partial effect at the higher exposure; INFERENZA: a residual effect in the knockout is unexplained, not proof of electrophile chemistry; the E-selectin/VCAM-1 downregulation is stated for human brain endothelial cells in vitro, not as the cause of the KO residue.
- report anchor: L41; L111; E29 E30
- source cited or found: PMID 27401964 (read this session)
- locator hint: Results, dose arms in WT and Nrf2-KO; Discussion
- class: binding/action/benefit

## D11
- statement: DATO (titles/identity only): PV interneurons are selectively vulnerable to glutathione deficit in Gclm-KO and oxidative models and NAC reverses it; INFERENZA: this identifies a vulnerable cell type, not a low-NRF2 WWOX state; loss of PV cells, marker reduction, delayed maturation and survival are distinct endpoints, and the same cell types may be lost through other WWOX routes.
- report anchor: L35; L11; E20-E24
- source cited or found: PMID 23140664; 36130098; 23671099; 42439630 (cited, not read)
- locator hint: Results, PV counts and PNN staining; review sections on oligodendrocyte lineage
- class: transcript/protein/activity/phenotype

## D12
- statement: DATO (abstract, cuprizone demyelination): microglial miR-155-5p binds the Nrf2 3'UTR in OPCs and inhibits their differentiation; blocking it improved remyelination. INFERENZA: NRF2 is shown to be a target restrained in a demyelination model, not shown to be required for, or limiting in, the developmental OPC maturation failure of WWOX loss; IPOTESI for stage-resolved test.
- report anchor: L44; L113; E43 E46
- source cited or found: PMID 40902898 (read this session; identity matches)
- locator hint: Results, OPC differentiation assays and Nrf2 3'UTR reporter
- class: transfer from other system

## D13
- statement: DATO (abstract of a hepatocellular carcinoma study found by the search, not cited by the report): drug-induced WWOX activation lowered nuclear NRF2 by ubiquitination; INFERENZA: that predicts higher NRF2 with WWOX loss, the opposite of the report's sign, in a gain-of-function non-neural cancer system; unfavourable to the impaired-NRF2 prediction but not a WWOX-DEE datum.
- report anchor: not in report; counter to L82
- source cited or found: PMID 39894307 (earlier package, abstract)
- locator hint: Results, nuclear translocation and ubiquitination panels
- class: transfer from other system

## D14
- statement: DATO: the report header says 35 papers reviewed and 7 confirmed findings; the evidence table lists 19 PMIDs and F001-F007; INFERENZA: 16 papers are unidentified, so the stated breadth cannot be audited. All 19 PMIDs were identity-checked (title and first author match the stated roles); 42439630 is a 2026 review and 40902898 a 2025 paper, both resolving to real records.
- report anchor: L6; L95-114
- source cited or found: pubmed_identity_check.py, 19 PMIDs
- locator hint: report header line and evidence table
- class: absence
