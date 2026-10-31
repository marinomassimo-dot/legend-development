# P1.5 ACK1 probe follow-up (IT13, p15)

Not medical advice. Scientist agent p15, 2026-10-31. Public routes only (Europe PMC REST search/fullTextXML, NCBI efetch on PMC for OA text; ChEMBL name search tried).

## Decision first

Both follow-up papers were located and verified by PMID. (a) The 2022 Nat Commun paper is Sridaran et al., PMID 36376335 (PMC9663509): ACK1 phosphorylates CSK Tyr18; (R)-9b is used in mice and in Jurkat cells at 3 uM. It is about T-cell/ICB biology, not WWOX. (b) The 2024 independent report is Murata et al., PMID 39639371 (Cell Biochem Funct 42:e70022): in cell lines, (R)-9bMS and XMD16-5 cause polyploidization that the authors attribute to Aurora B inhibition rather than TNK2 (knockdown did not reproduce it). Only the abstract was read (not open access). (c) The only kinase panel for (R)-9b found is the 34-kinase, single-dose (1 uM) profile in Lawrence 2015 (PMID 25699576, Table 3): JAK2 and TYK2 are inhibited as strongly as ACK1, six more kinases are above 80 percent, and Aurora kinases were not on the panel. (d) No paper was found that measures WWOX after pharmacologic ACK1 inhibition; the only later support is genetic knockdown in HCC cells (Xie 2015, PMID 25738261, abstract only).

Effect on probe choice: (R)-9b/(R)-9bMS alone cannot establish ACK1 dependence of any WWOX readout. Any ACK1-to-WWOX test needs (i) ACK1 knockdown or knockout as the primary perturbation, (ii) (R)-9b at the lowest effective dose with a pY-ACK1 readout, (iii) a second, structurally unrelated ACK1 inhibitor, and (iv) a WWOX readout that is not confounded by mitotic failure or JAK signalling (short exposure, no polyploidy). Dasatinib and bosutinib are multi-kinase (Src/Abl) and unsuitable as selective probes; AIM-100, XMD16-5 and KRCA-0008 selectivity could not be confirmed from sources read here (see UNVERIFIED). No ranking change is proposed; N12 priority unchanged.

## What was read, depth

| Source | Depth |
|---|---|
| Sridaran 2022 Nat Commun (PMC9663509) | Full text via Europe PMC XML, searched for 9b, selectivity, doses, Tnk2; Results not read line by line |
| Murata 2024 (PMID 39639371) | Abstract only (Europe PMC core record); no full text accessible |
| Lawrence 2015 J Med Chem (PMC4605435) | Full text via efetch; selectivity paragraph and Table 3 read; figures not viewed |
| Sridaran and Mahajan 2025 Trends Pharmacol Sci (PMC12935007) | Full text via efetch, keyword passages (AIM-100, dasatinib, WWOX, off-target) read; a review, secondary |
| Xie 2015 Int J Oncol (PMID 25738261) | Abstract only |
| Yang 2025 Cancers review of WWOX (PMC12610808) | Passage on ACK1 read; secondary and cites the 2005 work |

Before looking I knew only the IT12 note (names of the 2022 and 2024 papers unverified). Europe PMC fullTextXML returned HTTP 500 for two PMCIDs on repeated tries; efetch worked. ChEMBL name search returned unnamed IDs for the research compounds, so no ChEMBL activity data were used.

## Findings by item

(a) Sridaran 2022: the abstract states Tnk2-deficient mice show reduced CSK Y18 phosphorylation and T-cell activation, and that (R)-9b recapitulates inhibition of ICB-resistant tumours. Methods give 20 to 24 mg/kg subcutaneous five times a week, and 3 uM in Jurkat cells. Relevance to probe choice: CSK is a Src-family negative regulator; Lawrence Table 3 shows (R)-9b inhibits CSK only 26 percent and Src 71 percent and LCK 88 percent at 1 uM, so effects in T-cell contexts mix ACK1 and Src-family activity. The paper does not mention WWOX (zero hits).

(b) Murata 2024: abstract states (R)-9bMS reduced Aurora B autophosphorylation like XMD16-5, TNK2 knockdown did not, and (R)-9bMS promoted anchorage-independent colony formation at high concentration. Concentrations, cell-line-specific effects and the Aurora B assay design are not known from the abstract. One group, in cancer lines; not neural. Not a replication of anything.

(c) See claim_table.tsv rows C3 to C9. Lawrence also states, as background, bosutinib inhibits ACK1 with IC50 2.7 nM and dasatinib Kd 6 nM (secondary citations inside that paper). The 2025 review gives AIM-100 IC50 21.58 nM and calls the nature of (R)-9b's selectivity "ACK1-specific" (an authors' characterisation that sits against the Table 3 data).

(d) See rows D1 to D3. The 2005 Mahajan mechanism (overexpression, active Ack1) is covered in the IT12 follow-up; no pharmacologic arm exists in anything found.

## Edits this implies (proposals, not applied)

1. N12 / probe notes: record (R)-9b as non-selective (JAK2, TYK2, FGFR1, ABL1, CHK1, ALK, LCK, ROS1 IC50 5 to 206 nM; Src 71 percent at 1 uM) and flagged by an independent Aurora B attribution (2024, abstract level). Do not call it ACK1-specific.
2. IT11 design: add ACK1 siRNA/CRISPR arm as primary, a second chemotype arm, a mitosis/polyploidy control and a JAK2/TYK2 control (a JAK inhibitor without ACK1 activity).
3. Receipts: none proposed (no complete full-text read of the key papers at locator level).

## What a verifier needs

The decisive datum: the full text of Murata 2024 (doi 10.1002/cbf.70022) for the concentrations at which Aurora B and polyploidy appear, compared with the (R)-9b concentrations that Sridaran 2022 uses (3 uM) and that Mahajan-group papers use for pACK1 inhibition.

## Limits and UNVERIFIED

Not located, which describes the perimeter (Europe PMC search, titles/abstracts, English keywords) and not non-existence: a selectivity panel for XMD16-5, KRCA-0008 (only a 2013 ALK paper surfaced, PMID 24095090, title says selective ALK inhibitor; its ACK1 activity is not established here), AIM-100 kinome data; any pharmacologic ACK1 inhibitor plus WWOX measurement; independent replication of (b). Table 3 is single dose at 10 uM ATP on 34 kinases; Aurora was not tested, so absence there is not evidence against Aurora activity. No individual-level data used.
