# Sentences for the blind reader, ADV-282 increment 1 (SCI, 2026-11-25)

Each block is a card note as it stands in the repository.

Held source files for every block:
- /home/desktop/legend-development/files/geo/GSE156243/ (Salmon gene count table, two deposited differential-gene lists, family SOFT file)
- /home/desktop/legend-development/files/fulltext/PMID34268881_Steinberg2021_PMC_r2.xml (article of the deposit)
- /home/desktop/legend-development/files/figures/PMID34268881_r2/ (article figures, incl. expanded view)
- /home/desktop/legend-development/files/geo/GSE150123/ (series matrix and raw tar of an unperturbed time course; only where a sentence leans on culture time)

## DA-GSE-PDK-003

Row fields: target_id: human PDK1 transcript and the PDK/PDH transcript set; endpoint: log2 shift, knockout minus wild type; direction: DECREASE

Verbatim repository sentence (the note, whole):

> PDK1 -0.34, lower in sign only (the IT5 same-sets re-analysis gives -0.39, inside the single-gene null, p about 0.30; the datum is the absence of support for a raised PDK1, not a demonstrated decrease; see card I01); the PDK/PDH set +0.17 (P 0.22, not different from chance); LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries). EXPLORATORY NEGATIVES: transcripts are not PDH activity, flux or metabolite, and do not show that PDH or lactate are normal.

Source label the repository gives: GSE156243, the deposit of the 2021 organoid paper (PMID 34268881); exploratory set-level analysis by scientist-c

## DA-L01-003

Row fields: target_id: IL1B, IL6, TNF, NFE2L2, KEAP1 and NRF2 target transcripts, human KO organoid; endpoint: descriptive cpm ratio KO/WT (4 v 2 libraries), no test; direction: UNKNOWN

Verbatim repository sentence (the note, whole):

> IL6 0 counts in all six libraries; IL1B 0-11; TNF 0-1; P2RY12 0: no cytokine-expressing compartment. NFE2L2 0.75x, KEAP1 0.93x, NQO1 0.73x, G6PD 0.75x, SLC7A11 0.65x, BACH1 0.73x; HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x: no coherent NRF2 signature. Unplanned look at a deposit used by other packages; 4 v 2 libraries, one laboratory; transcripts are not NRF2 activity. Design (IT11 P2.3 verification, deposit and paper read): WT is one parental line; the 2 WT libraries are the survivors of a post hoc exclusion (one low-quality, one non-clustering); KO clone and batch are not assigned in the deposit; only NFE2L2 is in the authors' DE list (padj 1.43E-02, log2FC -0.58, above the stated alpha 0.01); NQO1 0.73x and HMOX1 1.67x are in neither list. NFE2L2 and NQO1 transcripts are lower in all four KO libraries (the arm-R-compatible direction) while HMOX1, SRXN1 and GSR are higher (the adaptive direction): descriptive, not a test.

Source label the repository gives: GSE156243 (deposit of PMID 34268881); unplanned descriptive reading in this package

## DA-W2-012

Row fields: target_id: human oligodendrocyte-lineage transcripts; endpoint: CPM, knockout minus wild type; direction: UNKNOWN

Verbatim repository sentence (the note, whole):

> PDGFRA and OLIG1 are nominally higher in knockouts, SOX10, MOG and OLIG2 are not; counts are very low and composition differs; a week-15 organoid has no compact myelin. Not myelin evidence.

Source label the repository gives: GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/README.md

## DA-J01-007

Row fields: target_id: reactive-astrocyte and cytokine transcripts in the WWOX-deficient human organoid; endpoint: counts per million, four knockout against two wild-type libraries; classified by the rule declared before the data were opened; direction: NO_CHANGE

Verbatim repository sentence (the note, whole):

> Microglial markers are at or near zero (P2RY12, CX3CR1, PTPRC, TREM2) so the tissue cannot test a microglial arm; of seven reactive-pan genes above 5 CPM only VIM and CD44 are raised (both radial-glia or progenitor associated), SERPINA3, TIMP1 and SOCS3 are lower, C3 and STAT3 not separated; IL1B, IL6, TNF are not informative (under 20 raw counts). Not a gliosis measurement and not myelin or seizure evidence.

Source label the repository gives: GSE156243 (the deposit of PMID 34268881), descriptive panel by scientist-a

## DA-K01-002

Row fields: target_id: EPAS1, HK2, SLC2A1, ARNT, HIF1A transcripts; endpoint: ratio of normalised counts, knockout over wild type; direction: INCREASE

Verbatim repository sentence (the note, whole):

> EPAS1 3.80 times, HK2 4.73 times, SLC2A1 2.67 times, ARNT 1.46 times; HIF1A mRNA 0.84 times (flat, as expected for a protein-level axis); PDK1 0.78 times. Four versus two libraries, one laboratory; the glycolytic genes also fall with elapsed culture time in unperturbed spheroids, so composition or maturity can contribute. IT10 P2.1 (premises a2, a3): the elevation is selective, a partly canonical hypoxia-response pattern and not a uniform glycolytic upshift (ADM, HK2, P4HA1, SLC2A1, BHLHE40, ANKRD37, EGLN3, DDIT4 up; PGK1, ALDOA, ENO1, PKM, PFKP, NDRG1, CA9 flat), compatible with HIF activity, with oxygen limitation of the organoid and with MYC (MYC +0.56 log2); the knockout's offsets in 12 progenitor and neuronal marker genes predict only a small maturity-related shift (median +0.08 to +0.16 log2 for HK2, SLC2A1, LDHA) against the observed +2.18, +1.40 and +0.75, which makes marker-measured maturity a minor contributor but does not exclude composition by unmeasured subpopulations or culture state (exploratory, calibration from another laboratory). HK2, SLC2A1 and PDK1 belong to the six-gene IT7 readout (guard IT7_READOUT6): they are observations here and cannot be used to evaluate any compound.

Source label the repository gives: GSE156243, the deposit of the 2021 organoid paper (PMID 34268881); descriptive extraction in the IT9 P4c-e package (organoid_target_gene_rows.tsv); not an evaluation by reversal of any gene set

## DA-I01-001

Row fields: target_id: human PDK1 transcript (WWOX-knockout cerebral organoid); endpoint: log2 shift, knockout minus wild type (sign only); direction: DECREASE

Verbatim repository sentence (the note, whole):

> PDK1 -0.39, LOWER IN SIGN ONLY: inside the single-gene null (p about 0.30), so the datum is the absence of support for a raised PDK1, not a demonstrated decrease (the earlier card E03 prints -0.34 for the same comparison; the two runs differ in method and the difference is not reconciled here). The PDK set as a whole is indistinguishable from chance. Transcript, not PDK protein, PDH phosphorylation or activity. The maturity confound of this deposit applies.

Source label the repository gives: GSE156243 (deposit of PMID 34268881), set-level and gene-level re-analysis by scientist-c; wwox_systems_comparison_it5_20261029.md section 2
