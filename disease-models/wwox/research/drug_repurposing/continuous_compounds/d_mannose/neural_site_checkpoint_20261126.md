# D-mannose · neural glycopeptide calibration and disposition

26 November 2026 · SCI_CODEX · context_policy: QUESTION_DRIVEN · detected regions for deglycosylated human peptides from one 20-postconception-week hemisphere, compared with intact-glycoform labels in human iPSC-derived cultures

The previous step required a stage-relevant neural reference for a site-level assay. Two human datasets offer different parts of that reference. Neither is a WWOX or mannose intervention dataset. [Developmental calibration and competing mechanisms](processing_discriminator_20261126.md)

## Reproducible cross-study check

Kimura et al. show an intact-glycopeptide approach along a human iPSC-to-dopaminergic differentiation series, with changes in the fucosylated bisected-glycan candidate HN5H3F at sites on L1CAM and PLXNB2, among other proteins. In the dopaminergic endpoint, the authors found increases in HN5H3F signal on plexins B1/B2 alongside lower corresponding protein levels. This is a reason to keep protein and glycoform measurements separate. It is not a calibrated site-occupancy or cortical lineage benchmark. [Kimura et al., Results, Fig. 5 caption and Methods, Data analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8160270/)

Bandiera et al. use sialylated-glycopeptide enrichment and remove glycans before measurement. The atlas gives developmental detectability across 18 regions in **one** human hemisphere at 20 weeks postconception. Its signal depends on glycan enrichment and protein abundance. It cannot count unoccupied sites or recover the intact glycoform at a detected site. [Bandiera et al., Methods §2.7, Results §3.7, Fig. 6 and Supplementary Table S2](https://onlinelibrary.wiley.com/doi/full/10.1111/joa.70170) · [PXD065788](https://proteomecentral.proteomexchange.org/ui?pxid=PXD065788)

I extracted atlas records for three nominated proteins. The check joins the abbreviated Table S2 peptide ID to a unique full sequence from Table S1f using the same accession, peptide prefix and length. It then requires a unique canonical match, an explicitly numbered peptide-local Asn and an N-X-S/T motif with X other than proline. A region counts only with positive author-reported glyco abundance. No abundance was averaged over regions.

- **SV2A N498 and N573** matched the author-specific deglyco-peptide IDs `SV2A_VEHV_16_N7` and `SV2A_LINS_10_N3`, each detected in **18 of 18** regions in this donor. They are controls for assay detectability.
- **PLXNB2 N844** also matched in **18 of 18** fetal regions. The abbreviated atlas identifier `PLXNB2_NCSF_8_N1` alone has two candidate starts, N759 and N844. The complete Table S1f peptide `NCSFQPER` uniquely matches N844 in O15031. Kimura lists a glycoform at the same reported integer. The fetal atlas only independently verifies a detectable deglycopeptide at that position. The glycoform and exact peptide match between studies remain unverified.
- **The other six L1CAM/PLXNB2 integer positions** do not land on Asn in today's canonical UniProt accessions. Exact peptide sequences and reference isoforms from both studies would be required to place them. The discrepancy rejects a join on protein name and residue number alone.

[Filtered counts and coordinate checks](neural_site_results.tsv) · [Reproduction script](neural_site_check.py) · [Curated human L1CAM](https://www.uniprot.org/uniprotkb/P32004/entry) · [PLXNB2](https://www.uniprot.org/uniprotkb/O15031/entry) · [SV2A](https://www.uniprot.org/uniprotkb/Q7L0J3/entry)

## Decision

**Park D-mannose for WWOX trial priority.** The developmental reference makes a paired site assay feasible in principle. The causal evidence still lacks stage-matched WWOX donor pools, a baseline occupancy deficit and an exposure-linked neural correction. Use SV2A N498/N573 as detectability controls and PLXNB2 N844 as a candidate maturation site. Before using a site as a biological WWOX endpoint, establish a quantifiable unoccupied peptide and at least two relevant intact glycoforms in both the deficient and corrected cells. Then pair those measurements with intermediate pools, coatomer localization and function. Reopen if that comparison demonstrates low GDP-mannose or early site occupancy with a genotype-selective correction at measured exposure. A mature glycoform deficit persisting after early occupancy normalizes would favor a later processing bottleneck. Review the assay and peptide mapping before interpreting any such result. These references do not change the pediatric exposure and safety gaps.

## Replay

The input directory contains the public author tables and current canonical UniProt FASTA files under the names below. Source files stay in the local evidence area. Run `python3 -B neural_site_check.py INPUT_DIRECTORY | cmp - neural_site_results.tsv`.

| File | Source | SHA-256 |
|---|---|---|
| PXD065788_S1.xlsx | [Author Table S1](https://raw.githubusercontent.com/Carlyle-Lab/PCW20_PTM_Proteomics/HEAD/Supplementary%20tables/Table%20S1.xlsx) | `7b1cde777ad0709f9d9283fd282355d63d95d6aba9417dcf408ee4afb1eaa1ba` |
| PXD065788_S2.csv | [Author Table S2](https://raw.githubusercontent.com/Carlyle-Lab/PCW20_PTM_Proteomics/HEAD/Supplementary%20tables/S2%20Master_table.csv) | `db0b31ae3c102d1c86088bcf642ac0e6f8d1caee068258c54ae0365309c30f88` |
| P32004.fasta | [UniProt FASTA](https://rest.uniprot.org/uniprotkb/P32004.fasta) | `de2acff9a9c31ea8533493af283f2ed687c33254aefa75792a29aefe8f9bdcd3` |
| O15031.fasta | [UniProt FASTA](https://rest.uniprot.org/uniprotkb/O15031.fasta) | `965165daf8d73ab830e3bbb1756fdc25d3ff0f296eaa42935cea636adc530f31` |
| Q7L0J3.fasta | [UniProt FASTA](https://rest.uniprot.org/uniprotkb/Q7L0J3.fasta) | `5ab4fe40845baeba5ea535db45721fa596d10aefc1c15c07ae299828340cf03e` |
