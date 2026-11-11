# SCI44 blind audit V1 (A2 expression, A3 pharmacology) — verifier pk-v, 2026-11-10

Non-canonical research material. Not medical advice. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI.
Read before the verdicts: `VERIFIER_BRIEF_V1.md`, `A1_before_search.md` up to "Predictions fixed before any new reading",
`output/{isoform_expression,decisive,function_neural,symbols,priors_scored,evidence,queries,figure_notes}.tsv`, `output/a3/{activity_primary,
repository_rows_vs_primary,symbol_check,decisive,evidence,queries}.tsv`, the producers' receipts and scripts. Not opened: `output/answers.md`,
`output/a3/answers.md`, any `phase_note.md`, any README. Producer scripts were read, not run; every number below comes from my own code
(`recompute_expression.tsv`). Claim actor `pk-v`; 32 staged receipts (suffix -97) validated with `staged_receipt_check.py --check-doi`, none recorded.

## 0. Counts

| Unit | Checked | Correct | Defective |
|---|---|---|---|
| Expression table rows (isoform_expression.tsv) | 360 (126 GEO, 117 HPA snRNA, 63 HPA scRNA, 54 HPA IHC) | 360 | 0 numeric |
| Decisive rows A2 D01-D16 | 16 | 12 | 4 (D02, D05, D09, D15: none wholly wrong) |
| Decisive rows A3 A3D01-A3D14 | 14 | 7 | 7 (A3D02, A3D05, A3D06, A3D07, A3D09, A3D10, A3D11) |
| Evidence rows (31 A2 + 22 A3) | 53 | 51 | 2 (EV10, EV11: quote not verbatim) |
| Staged receipts spot-checked | 7 (3 A2, 4 A3) | 6 | 1 (coverage inconsistency), plus uniform timestamps in all |
| Priors P1-P5 | 5 | 5 | 0 |

Substantive errors (change a statement the decision lines rest on): (1) D02/D03 region label of the HPA aggregate; (2) A3D05 reading for
AZD7545 on PDK3; (3) D09 group sizes; (4) CHEMBL257158 named as the selenazoline although the ChEMBL structure is the thiazoline; (5) A3D09
omits the measured PDK4 DCA datum; (6) D05 species wording. No wrong expression number was found.

## 1. A2 D01-D04, D05, D06 — re-extraction (item 1)

DATO, own code. Mouse: GSE52564, 17 per-sample xls sheets "UCSC Genes FPKM" (tar sha256 4cb522fb...427d0, equal to the producer's), two samples per
class (Neuron1-2, Astrocyte1-2, OPC1-2, NFO1-2, MO1-2, Microglia1-2, Endothelial1-2; whole cortex WC1-3 not used for a class). Human: GSE73721
table (sha256 140f376a...fcef), 45 data columns, allocated by explicit ranges: mature astrocytes 12 (8yo-63yo, two columns of 63yo), fetal
astrocytes 6, neuron 1 (25yo), oligodendrocytes 5 (22yo, 63yo A, 63yo B, 47yo, 63yo 3), myeloid 3, endothelium 2, whole cortex 4, tumour 4,
hippocampus 4 (epilepsy region), mouse adult astrocytes 4. The earlier 10-of-12 slip is not present: the producer's mature-astrocyte rows use all 12.

| Class (n columns) | PDK1 | PDK2 | PDK3 | PDK4 | unit |
|---|---|---|---|---|---|
| mouse neurons (2) | 5.31 | 13.75 | 4.27 | 2.17 | FPKM |
| mouse astrocytes (2) | 6.08 | 17.27 | 4.61 | 63.70 | FPKM |
| mouse OPC / NFO / MO (2 each) | 4.03/9.69/4.02 | 16.62/36.22/33.23 | 9.24/20.88/23.97 | 1.08/0.48/1.71 | FPKM |
| mouse microglia (2) / endothelium (2) | 9.87 / 9.12 | 7.19 / 6.04 | 6.06 / 8.92 | 0.65 / 14.73 | FPKM |
| human mature astrocytes (12) | 0.94 | 7.52 | 1.54 | 22.59 | FPKM |
| human fetal astrocytes (6) | 1.53 | 6.80 | 1.63 | 1.42 | FPKM |
| human neuron (1) | 2.50 | 1.10 | 5.60 | 3.30 | FPKM |
| human oligodendrocytes (5) | 0.68 | 0.62 | 0.94 | 7.44 | FPKM |
| human myeloid (3) / endothelium (2) | 3.20 / 1.05 | 0.33 / 1.40 | 3.23 / 0.60 | 192.50 / 17.70 | FPKM |

All equal the producer's rows to two decimals (replicate values are in `recompute_expression.tsv`). Symbol mapping: the mouse isoform sheet
lists NM_172665 (Pdk1), NM_133667 (Pdk2), NM_145630 (Pdk3), NM_013743 (Pdk4) and NM_011062 (Pdpk1), checked in nuccore; Pdk1 and Pdpk1 are
separate rows in both tables (mouse neuron 5.31 against 12.29; human mature astrocyte 0.94 against 2.89), so the kinase used is not PDPK1. The human
table uses mouse-style symbols for human columns; for the human rows I can show only that Pdk1 and Pdpk1 are distinct rows with different values,
not the Ensembl identity behind the symbol. FPKM (GEO) and nCPM (HPA) are never mixed inside a comparison in D01-D06; the adult-mouse astrocyte
column of the 2016 table (Pdk2 42.35, Pdk4 9.45) comes from another pipeline (Galaxy/TopHat2) than the 2014 values (Cufflinks) and the producer says so.

Open points: (i) the three oligodendrocyte columns labelled 63yo and the two astrocyte columns labelled 63yo: the paper states 5 and 12 patients, but
the labels alone cannot show they are distinct patients (Table S1 of the paper was not opened): UNVERIFIABLE; (ii) neurons of the 2016 table are
one Thy1-purified sample (Fig 1 legend) from a patient aged 25; (iii) the 2014 neuron sample is L1CAM-selected after depletion of endothelial,
OPC and microglia cells, P7, so excitatory and inhibitory neurons are mixed (the producer says so).

### HPA single-nucleus numbers and design (what the file states, what the pages state)

All 117 snRNA rows reproduce (zip sha256 a287c1ab...b02f2a, extracted tsv 1bd8bc5b...5fff2). Clusters the producer used: 7 neuron superclusters
(upper-layer IT, deep-layer IT, deep-layer near-projecting, deep-layer corticothalamic and 6b, MGE, CGE, LAMP5-LHX6 and Chandelier), astrocyte,
oligodendrocyte, OPC, committed OPC, CNS macrophage, endothelial cell, pericyte. The file carries only four columns (Gene, Gene name, Cluster type, nCPM)
and states nothing about design. **The design statement exists on the HPA pages** (producer did not open these): `humanproteome/single+cell/single+nuclei+brain`
and its `/data` page state that the data are the Siletti et al. 2023 snRNA-seq set (more than 3 million cells, 461 clusters), shown as 34 supercluster
cell types, summarised "from 11 brain regions", with the cerebral cortex represented by a random 500,000-cell subset and 2,526,725 cells displayed in total;
the region table lists cell counts per region (for example amygdala 187,165, cerebellum 151,940, cerebral cortex 500,000). The Siletti abstract (PubMed
record, abstract only) gives three postmortem donors, more than three million nuclei, about 100 dissections. Donor ages and sexes are not on the
pages I opened. Consequences: (a) the "cluster type" file is an **11-region aggregate**, not cortex: D02's "adult human cortical neuron clusters" is wrong
(the cluster names are cortical-style but, for example, "deep-layer near-projecting" includes 221 amygdala cells flagged "included in aggregation" in the region
table); the table rows already say "brain-wide cluster type", the decisive row does not. (b) The same download set has `rna_single_nuclei_brain_cluster.tsv`
with region = cerebral cortex. Cortex-only values (nCPM, PDK1/PDK2/PDK3/PDK4): upper-layer IT 21.6/31.4/121.1/0.3; deep-layer IT 23.2/29.3/101.6/0.3;
deep-layer near-projecting 24.5/16.2/74.0/0.0; deep-layer corticothalamic 23.4/26.9/97.6/0.4; MGE 22.3/25.9/101.9/0.2; CGE 23.6/28.8/59.6/1.5;
LAMP5-LHX6 27.1/26.9/114.3/2.6; astrocyte 11.2/35.2/33.9/138.2; oligodendrocyte 13.7/19.3/20.2/75.2; OPC 13.1/17.2/25.7/27.8; CNS macrophage
55.0/11.3/116.6/57.9; endothelial 44.1/15.3/23.0/147.7. The ranks that D02-D04 use are unchanged (neurons PDK3 first; astrocyte and oligodendrocyte
PDK4 first); the numbers in the decisive text should be the cortex-only ones if the word "cortical" is kept. (c) File header says nCPM, the pages say nTPM:
a unit-name inconsistency in HPA itself; keep "nCPM (file header)". (d) The aggregation weights donors unknown; nuclei are not donors.

### D05 and the species wording

Numbers reproduce. The mouse-to-human gap in microglia PDK4 (0.65 against 192.50 FPKM, about 300-fold) is stated as "by species", but preparation is
confounded with species: the human sample is CD45-immunopanned myeloid from surgically resected temporal cortex (microglia and macrophages not
separable, three patients 276.4/247.4/53.7), the mouse sample is perfused P17-suspension CD45-panned microglia. The human snRNA macrophage cluster gives
PDK4 22.6 nCPM in the aggregate and 57.9 in the cortex-only file, so two human datasets already differ 3- to 8-fold. Write "differ between the mouse
and human preparations" and name the human disagreement.

## 2. A3D02, A3D03, A3D05 — the sign of AZD7545 (item 2)

Kato 2007 (PMC author manuscript, Results, Discussion, Experimental Procedures, Fig 2A-D viewed). DATO as the paper states it:
- Assay with core: 50 nM SUMO-PDK1 or SUMO-PDK3, 1.5 uM human E1p, 50 nM E2/E3BP core, 50 uM [gamma-32P]ATP, 25 C, 30 min pre-incubation, 2% DMSO.
  IC50 87 nM (PDK1) and 600 nM (PDK3); at 10 uM AZD7545 leaves 28% (PDK1) and 31% (PDK3) of control. Fig 2A curves: PDK1 plateau about 29%,
  PDK3 about 37% at 100 uM (raster, INFERENZA).
- Without core (free E1p, 10 uM AZD7545, bars are averages of two experiments, no error bars): PDK1 about 128% (the text: 1.3-fold, "marginal
  stimulation"), PDK3 about 1005% (10-fold). The authors write: "AZD7545 appears to be a dual-role ligand for PDK3 ... dependent on the presence and
  absence of the E2p/E3BP core". They add that under physiological conditions PDK3 is tightly bound to the E2p/E3BP scaffold, so the inhibition (not
  the stimulation) is the one they expect in situ.
- PDK2: no measurement in this paper. The text says its core-bound result is "consistent with an earlier proposition that AZD7545 inhibits the
  E2p-dependent stimulation of PDK2 activity" (Morrell 2003; Tuganova 2007).
- Also read: DCA at 40 mM with core leaves 4% (PDK1) and 28% (PDK3); without core about 4% and 17% (Fig 2D, raster).

So "the sign depends on the scaffold" is what the paper shows for PDK3 (large effect, explicit statement); for PDK1 the 1.3-fold core-free rise is a
marginal effect the authors report but do not interpret as a sign change. Wynn 2008 (Table 3): PDK4 kcat 35.1 min-1 alone, 2.6 with 0.25 mM DCA, 98.3 with
10 uM AZD7545 (E1p, 0.5 mM ATP, no E2p/E3BP mentioned; 98.3/35.1 = 2.80); Kd 48 nM carries footnote 5 "unpublished results". The paper states
PDK4 is "only modestly stimulated by the E2p/E3BP core"; there is no core-bound AZD7545 measurement on PDK4.

Is the producer's A3D05 justified? "Missing PDK3/PDK4 rows must not be filled with inhibitor": **PDK4 yes** (only core-free stimulation exists); **PDK3 no
as worded**: A3D05 says the effect is "activation without the E2 scaffold" and omits that the same paper measured an inhibition IC50 of 0.60 uM with
the scaffold, which is the in-situ condition by the authors' reading. The repository row for PDK3 can carry the measured value with its condition
(core-bound IC50 0.60 uM, residual 31% at 10 uM; core-free 10-fold stimulation), flagged as not comparable with the PDK1 value of the 2003 paper.
"PDK3/PDK4 were measured later" is true; "whether the 2003 panel included them is unknown" is right.

## 3. A3D04 and Q3e (item 3)

Morrell 2003 (14641019): one plain request to the doi route returned HTTP 403 (portlandpress), recorded, not retried; I read only the PubMed
abstract (no isoform, no number). Without it: the repository's PDK1 pIC50 7.43 is about 37 nM; Kato's 87 nM is 2.3-fold higher, which fits his sentence that his
IC50 is "greater than 2-fold higher than that reported previously" (he attributes it to 40 against 50 nM kinase and cites a personal communication, a
weak explanation for a 2-fold shift); the earlier assay's species and the PDK2 8.19 stay unverifiable. The repository's "Human" for the 2003 row is
unverified (not shown to be unsupported: PubMed's rat MeSH terms may refer to tissue used in vivo).

ChEMBL REST (no login): activities 1108140 (nandrolone IC50 = 120 uM, assay CHEMBL764813, document CHEMBL1131823, BMCL 1999, target CHEMBL2096665
Homo sapiens family, assay organism empty), 1115406 (DCA acid IC50 > 2,000 uM, same assay), 125975 (sodium dichloroacetate IC50 > 1,000 uM, assay
CHEMBL767696, Sus scrofa), 125976 (EC50 = 130 uM, assay CHEMBL767695 "in vivo ... increased oxidation of lactate", type F, assay organism Homo sapiens as
recorded), 305159 (IC50 > 1,000 uM, CHEMBL769458, "porcine pyruvate dehydrogenase kinase", Sus scrofa, document CHEMBL1133733, J Med Chem 2000);
125977 is a rat target record. Target CHEMBL2096665 is a PROTEIN FAMILY with four components (Q15119 PDK2, Q15120 PDK3, Q16654 PDK4, Q15118 PDK1).
The fan-out reading is correct: one measurement per record becomes four rows. The censored relations (">") and the porcine organism are as A3D14 says;
the single-isoform 2017 rows for the acid mentioned in A3D14 were not queried by me.

## 4. A3D06-A3D08 (item 4)

Moore 2014 (open-data bucket text and PDF, Figs 2 and 3 viewed). Table 1 as quoted: IC50 35 (n=5), 84 (n=2), 40 (n=3), 91 (n=4) nM for PDK-1 to -4; pIC50 =
9 - log10(nM) gives 7.456, 7.076, 7.398, 7.041, i.e. 7.46, 7.08, 7.40, 7.04 as in the repository. Methods: enzyme 10 nM (PDK-1, -2, -3) and **20 nM (PDK-4)**, 300 nM E1,
5 uM ATP, 1 h at 30 C, DELFIA with anti-phospho-Ser293, no E2. Constructs: PDK-1 residues 30-436, PDK-2 16-407, PDK-3 9-406, PDK-4 1-412, "full length cDNA
clones (Qiagen)", His-tagged; species not named (only the crystallised PDK-2 is "Human"). INFERENZA: human PDK1, PDK2, PDK3 have 436, 407, 406
residues (rodent Pdk1 434), human PDK4 411 (mouse and rat 412), so PDK-1 numbering fits human and PDK-4 numbering fits a rodent sequence or a
construct with an extra residue; the paper does not say, and the repository's "human" for all four rows is therefore unverified. A3D06's "four
truncated constructs" is wrong for PDK-4 (full length). PC-3: Table 1 gives p(Ser293)E1alpha IC50 266 nM at 0% serum (n=4), 1.45 uM at 10% FCS (n=1); FP IC50 79 nM
(n=3); ITC Kd 150 nM. Fig 3A bars (raster reads): 20 uM VER-246608 about 138%, 10 uM about 148%, 3 uM Nov3r about 129% of DMSO: **INFERENZA, not DATO** (A3D07
is labelled DATO). Fig 3B: oxygen consumption bar difference of 66% is given in the text beside "P = 0.08" in the panel. Both quoted inconsistencies are real:
text 266 and 55 nM against Table 1's 5 nM for Nov3r; and in Kato the text gives radicicol IC50 "230 mM for PDK1 and 400 uM for PDK3" while Fig 2B labels PDK1 400 uM and PDK3
230 uM. I found a third small one: the text cites Fig 2C for HSP-70 induction while Fig 2C is the Ser232 ELISA (HSP-70 is in Fig 2E).
A3D08 stands as INFERENZA; add that Nov3r's roughly 2-fold stimulation concerns PDK-3 and PDK-4 only ("data not shown") and that the 3 nM IC50 is PDK-1 in
the E1/E2 assay.

## 5. A3D11-A3D13 (item 5)

- Celecoxib: the open-data text of the 2012 review says "PDK1 (encoded by gene PDPK1)". DGIdb live: celecoxib-PDK1 row hgnc:8809 source ClinPGx, publication
  22336956; a separate PDPK1 row (hgnc:8816) with other sources. Confirmed.
- OSU-03012: DGIdb PDK1 row hgnc:8809, source TdgClinicalTrial, attribute AR-12 and Novel Target, no type; its PDPK1 row (hgnc:8816) lists ChEMBL, Repurposing Hub,
  TTD and GtoPdb with "3-phosphoinositide dependent protein kinase-1 inhibitor". Confirmed.
- GlcNAc-selenazoline paper (Kim 2010): "The inhibitors also reduced the activation of PDK1 and AKT (data not shown)", insulin-signalling context. Confirmed.
  **Identity defect:** CHEMBL257158 in ChEMBL is C8H13NO4S (sulfur), i.e. GlcNAc-thiazoline = compound 1 of that paper; the selenazoline is compound 2.
  `output/a3/symbol_check.tsv` SC02, `decisive.tsv` A3D11 and `repository_rows_vs_primary.tsv` call CHEMBL257158 "GlcNAc-selenazoline (ChEMBL structure)".
  Conclusion unaffected (the DGIdb row still links the insulin-signalling paper).
- 3-hydroxyanthranilic acid: abstract says "specifically targeting PDK1" in T-cell NF-kappaB signalling; PubMed MeSH lists the dehydrogenase-kinase
  heading, the paper's pathway is the signalling kinase (INFERENZA from the abstract).
- DCA row: Meng 2014 abstract: dual PDHK/HSP90 inhibitors, "inhibited PDHK1 with an IC50 value of 17 nM" (own compound).
- HGNC: PDPK1 (HGNC:8816) has alias_symbol PDK1; PDK1 is an approved symbol of the dehydrogenase kinase (HGNC:8809); the alias search for PDK1 returns only PDPK1.
  UniProt (looked up, not recalled): Q15118 PDK1, Q15119 PDK2, Q15120 PDK3, Q16654 PDK4 ("kinase isozyme N, mitochondrial"); O15530 PDPK1 with gene synonym PDK1.
- Devimistat: Stuart 2014 Background: CPI-613 "specifically induces inactivating phosphorylation of tumor cell PDH via stimulation of PDKs 1 to 4"; it is
  a statement about the authors' earlier paper (authors hold sponsor interests); in this paper CPI-613 inhibits KGDH and a PDK knockdown protects partially. "The four
  DGIdb rows carry no inhibitor evidence" stands (rows have no interaction type).
- GtoPdb ligand pages were not tried by me (producer: HTTP 401); the typed AZD7545 and VER-246608 target identity rests on the papers.

## 6. A2 D07 and D15 (item 6)

D07 (absence): my searches (PubMed tool, gene-led and proteomics-led, plus a text search of the Sharma 2015 article for PDK/pyruvate dehydrogenase strings: 0 hits) found no
per-cell-type PDK protein amounts; supplementary tables of the mouse proteome were not retried by me (the producer's proof-of-work record stands). Adequate for the stated perimeter.
D15: logic confirmed (two oligodendrocyte-lineage "PDK1" papers define PDK1 as 3-phosphoinositide-dependent kinase 1 in their abstracts). The same query re-run today
returns 44 hits; the producer screened the first 25. Records in the 44 that bear on the lever and are absent from the package (abstract level, mine):
26931482 (Pdk2/Pdk4 gene-deficient mice exist and have a nociceptive phenotype), 34358226 (Wnt signalling predominantly in neurons with PDK4 as a Wnt target gene after status epilepticus; the abstract does not give the cell type of the PDK4 rise, so it bears on the neuron PDK4 question only for the injured state), 33251681 (PDK2 in satellite glia, abstract) and, by title only, 42665101 (LCN2-PDK axis in glia), 28123081 (HDAC inhibitors and PDH dysfunction in Huntington's disease) and 26769971. My other strings added 33219201 (cell-type-specific ablation of Pdk2 in hypothalamic astrocytes, mouse: a genetic arm exists), 39161415 (astrocytic PDK4 up
in spinal dorsal horn), 40485011 (a PDK4 axis in cuprizone white-matter injury, no PDK loss test), 30873027 (melatonin raising PDK4 and remyelination, title only; same topic as D13),
35444068 (Drosophila: PDK protects dopaminergic neurons in DJ-1 null flies, a H-B type result) and 32504000 (a human PDK3 p.R158H variant in X-linked Charcot-Marie-Tooth
iPSC motor neurons, which bears on PDK3 in neurons, D02). None changes an A2 number; 32504000, 34358226, 35444068 and 33219201 bear on the decision lines and were not read beyond abstracts or titles by me.

## 7. Lower-depth rows (item 7)

D08: infarct 10.8 +/- 1.9 to 5.0 +/- 1.0 mm3, n = 25 and 24, PDH activity p = 0.0396, MCAO sentence, n = 6: found. **D09: defect.** Percentages (PDK2 +83.1, PDH -62.1, phospho-Ser293 +62.3, ATP -42.5, CA1 neurons +36.8) are
in the text, but Methods 2.4 "n = 5 for each sham group, n = 8 for each seizure group" holds for the design and the behaviour panel (Fig 7); the legends of the
blot panels state n = 3 or n = 4 per group and the staining panels n = 4 per sham and n = 5-7 per seizure group. D09 and E21's "n=8 per seizure group, 5 per sham" must be replaced. D10-D12, D16
checked at abstract level (the producer labels them abstract_only; D10's "worsening" is the authors' "slightly proconvulsant", which they link to a 23% fall in
total PDH; the abstract also gives PDH protein -37% and Ser300 phosphorylation +52% in chronic epileptic mice, which weakens a phosphorylation-only reading of the 65% activity loss). D13: 10.33 +/- 2.16 against
5.363 +/- 1.87, n = 8 per group; the 32-mice and F(4,35) mismatch stays open. D14: N = 3, BV2 limitation sentence found. A3D01: IC50s, conditions found. A3D09: Li 2009
Table 1 WT PDK2 0.29 +/- 0.02 (basal) and 0.48 +/- 0.08 mM (core), n = 3-5: found; 1998 abstract Ki 0.2 mM (PDK2) to 8 mM (PDK3) found, but the abstract does not state the species of the
recombinant isoenzymes ("rat-isoenzyme" in A3D09 is an inference from tissue mRNA wording and MeSH). A3D10: DCA in the N-terminal helix bundle of PDK1 and "local conformational changes
communicated to both nucleotide-binding and lipoyl-binding pockets ... leading to the inactivation" are in Kato's abstract; "closes the kinase" is the PDK2/PDK4 structural language of Wynn and Li. A3D09 also
**omits the datum Wynn 2008 Table 3 gives for DCA on PDK4**: 0.25 mM DCA lowers the core-free kcat from 35.1 to 2.6 min-1 (one concentration, E1p only).
Labels: D01-D04 "favourable/unfavourable" follow from the row for the compound-isoform pairs but not as a benefit statement; no benefit wording was found in the decisive text.

## 8. Priors P1-P5 (item 8)

With my values: P1 failed (PDK2 top only in mouse neurons and mouse oligodendrocyte lineage; human oligodendrocyte PDK2 0.62 is lowest, below PDK3 0.94 and PDK1 0.68); P2 failed (PDK3 top in human
neuron clusters and the macrophage cluster, cortex-only 116.6); P3 held (RNA; the IHC PDK4 "High" in neuronal cells against neuron-cluster nCPM of 0.0-2.6 is the RNA-protein
disagreement P5 records); P4 failed overall (held in mouse neurons, astrocytes and oligodendrocyte lineage); P5 held (human only). The verdicts stand.

## 9. Evidence rows and receipts (item 9)

All 31 A2 and 22 A3 evidence rows checked: quotes are verbatim at the stated locator for 51; **EV10 and EV11 are not verbatim** ("ICvalue of 3 nM", "ICvalues of 266 and 55 nM": the 50 subscript was lost
in the text layer; the source reads "IC50 value of 3 nM" and "IC50 values of 266 and 55 nM"; the producer notes the loss). E04 matches once the HTML entity for ">" is decoded. E08, E09, E30, E31, EV19-EV21 are database
or title fields, checked against the file, the HGNC record and the ChEMBL and DGIdb records (PharmGKB ids PA33154 and PA33160 in EV21 not checked). No quote exceeds 25 words (the longest is 25).
Receipts spot-checked: A2 `FTR-20261110-25186741-96` (coverage lists results `not_read` while its own locator is a Results sentence; supplementary `read` for GEO tables is acceptable),
A2 `...-39177920-96` and `...-36432491-96` (coverage consistent; the second's "group sizes" rationale is what the D09 defect rests on), A3 `...-17683942-96`, `...-25404640-96`, `...-18658136-96` and `...-14641019-96` (consistent with what I found in the sources). Every A2 receipt shares
analysis_at 22:30 and event_at 22:41 and every A3 receipt 22:53 and 22:58: placeholders rather than individual times. All prior_receipt fields are null except the 36432491 reread, correct for first reads.

## 10. Transfers and logic (item 10)

- D02: brain-wide aggregate called cortical (above). D05: preparation carried as species (above).
- D03: "PDK4 dominance appears with maturation" holds in the human immunopanned series (fetal 1.42 against mature 22.59); in the same GEO table the mouse series goes the other way (P7 PDK4 63.70 in the 2014
  table, adult 9.45 in the 2016 table) across two pipelines; the producer flags it, but a reader of the first sentence alone is misled. Keep the sentence limited to human.
- D04: "AZD7545's PDK1/PDK2 rows fit the mouse lineage better" compares mouse P17 lineage-stage cells with human adult mixed-stage oligodendrocytes (independence of the 63yo columns unverified): label stays transfer.
- D01/D02/D03 sorting for AZD7545: with Kato's PDK3 IC50 (0.60 uM, 7-fold weaker than PDK1) the neuron-dominant PDK3 is a measured, weaker, scaffold-conditional target, not an unmeasured one.
- Wynn's PDK4 kcat is core-free; the astrocyte-dominant PDK4 therefore has an AZD7545 datum of unknown sign in situ and a DCA datum (inhibition) in the same condition.
- No class error found beyond those listed; I re-checked every row of the classes affected: all 360 expression rows (numeric), all 53 evidence rows (quotes), all 14 A3 decisive rows and 16 A2 decisive rows (statements).

## 11. Corrections the producer or Orchestrator must make

| File and row | Change |
|---|---|
| `output/decisive.tsv` D02 | replace "adult human cortical neuron clusters (HPA single-nucleus aggregate)" with "seven neuronal supercluster types of the HPA single-nucleus cluster-type aggregate (34 supercluster types pooled over 11 brain regions; Siletti 2023, three postmortem donors); cortex-only region values give the same ranking (PDK3 59.6-121.1, PDK2 16.2-31.4, PDK4 0.0-2.6 nCPM)". Replace "AZD7545 has no recorded PDK3 or PDK4 row" with "the repository has no PDK3 or PDK4 row; Kato 2007 measured PDK3 (IC50 0.60 uM with core; 10-fold stimulation without)". |
| `output/decisive.tsv` D03 | limit "the PDK4 dominance appears with maturation" to human; add that the mouse series in the same table goes the other way. |
| `output/decisive.tsv` D05 | replace "differ by species" with "differ between the mouse and human preparations; two human datasets differ 3-8 fold (192.5 FPKM immunopanned myeloid; 22.6 nCPM snRNA aggregate; 57.9 cortex-only)". |
| `output/decisive.tsv` D09, `evidence.tsv` E21, `function_neural.tsv` F05/F06 | n: Methods 5 and 8 per group, blot panels n = 3 or 4, staining n = 4 sham and 5-7 seizure; state which panel carries each percentage. |
| `output/decisive.tsv` D15, `queries.tsv` Q18 | perimeter: 44 hits, 25 screened; add the records listed in section 6 as unscreened or screened. |
| `output/isoform_expression.tsv` HPA rows IE127-IE178 (columns age_stage, region, biological_unit) | donors "three postmortem donors (Siletti 2023 abstract)", region "11-region aggregate; cortex a 500,000-nuclei random subset (HPA page)"; remove "donor number is not stated" and "source dataset not opened". |
| `output/a3/decisive.tsv` A3D02 | say the dual-role statement is the authors' for PDK3; PDK1 1.3-fold is "marginal"; PDK2 not tested in the paper; authors expect inhibition in situ because PDK3 is scaffold-bound. |
| `output/a3/decisive.tsv` A3D05 and `repository_rows_vs_primary.tsv` "S9 typed gap" row | PDK4: do not fill with inhibitor (core-free stimulation only). PDK3: may carry the measured inhibition (IC50 0.60 uM, core-bound) with the scaffold condition and the 10-fold core-free stimulation; not comparable with the 2003 PDK1 value. |
| `output/a3/decisive.tsv` A3D06 | "four truncated constructs" -> three truncated constructs and one full-length (PDK-4, residues 1-412); PDK-4 enzyme 20 nM against 10 nM; species unnamed; residue-range hint is INFERENZA. |
| `output/a3/decisive.tsv` A3D07 | the 138-148% PDH activity is a raster read: INFERENZA. |
| `output/a3/decisive.tsv` A3D09 | add PDK4: DCA 0.25 mM lowers core-free kcat 35.1 to 2.6 min-1 (Wynn 2008 Table 3); mark "rat-isoenzyme" as inference. |
| `output/a3/decisive.tsv` A3D10 | attribute "closes the kinase" to the PDK2/PDK4 structures, not Kato's PDK1 structure. |
| `output/a3/symbol_check.tsv` SC02, `decisive.tsv` A3D11, `repository_rows_vs_primary.tsv` | CHEMBL257158 = GlcNAc-thiazoline (sulfur; C8H13NO4S), not the selenazoline. |
| `output/a3/evidence.tsv` EV10, EV11 | restore the subscript: "IC50 value of 3 nM"; "IC50 values of 266 and 55 nM". |
| both `receipts/FTR-...-96.json` sets | A2 25186741: results coverage vs Results locator; give individual analysis and event times. |

## 12. Decision lines (what changes)

1. Isoform rows of the typed inhibitors. AZD7545: PDK1 IC50 87 nM (core-bound; residual 28%; core-free 1.3-fold rise, marginal); PDK3 IC50 0.60 uM core-bound (31%
   residual) and 10-fold stimulation core-free; PDK4 core-free kcat 2.8-fold up, no core-bound measurement; PDK2 not measured in any source I opened (repository 8.19 unverified).
   VER-246608: four IC50 reproduced; species and construct numbering unverified. DCA: millimolar on every isoform with data, now including PDK4 core-free (0.25 mM, 93% fall in kcat).
   The tool-per-cell argument survives: the dominant kinase differs by class and species (mouse neurons PDK2, human neurons PDK3; mouse oligodendrocyte lineage PDK2, human oligodendrocytes PDK4).
2. The AZD7545 sign. Supported for PDK3 as the authors state it; weaker for PDK1; the in-situ (core-bound) expectation is inhibition. A "worsening" reading for AZD7545 is not shown for PDK1 or PDK3 in the scaffold-bound condition (inhibition); it is shown core-free (PDK3, PDK4, marginally PDK1); scaffold-bound PDK2 and PDK4 are unmeasured here.
3. Premise sample design. The cell-resolved premise stays justified by my re-extraction (PDK4 dominant in astrocytes of both species and human oligodendrocytes and endothelium; PDK3 dominant in human neurons and macrophages; PDK2 dominant in mouse neurons and oligodendrocyte lineage). The HPA single-nucleus design statement is now available: Siletti 2023, three postmortem donors, 11 regions, cortex subsample; use the cortex-only values or the Siletti data, not the 11-region aggregate, for a cortical premise.

## 13. Not reached or not done

Morrell 2003 (HTTP 403, one request); Sharma 2015 supplementary tables (not retried; producer's proof-of-work record); GtoPdb pages; PharmGKB ids; Table S1 of Zhang 2016 (patient identity of repeated ages); single-isoform ChEMBL rows of 2017 for the acid;
Moore 2014 supplement and Fig 1, Fig 4, Fig 5; figures of the open-access function papers (not viewed by me); full text of every gap paper named in section 6 (abstract or title only).
