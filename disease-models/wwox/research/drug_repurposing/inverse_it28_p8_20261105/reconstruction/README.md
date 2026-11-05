# Blind reconstruction: reasons to study tazemetostat and TMP269 in a WWOX-deficiency research programme

Scope: verifiable reasons from primary sources only. No doses. No spend, no registration, no contact. Nothing under the
frozen / generation / stage-table / alternatives / decomposition / verification / qualification records was opened.
Sources used: the catalogue cache (ChEMBL molecules and mechanisms, GtoPdb, DGIdb), PubMed abstracts, the working model
(read only by keyword). ChEMBL REST returned HTTP 500 for every call (retried twice). Reading level of every literature
anchor below is ABSTRACT ONLY (no full text read), so every locator is "abstract" and every quantitative claim is limited
to what the abstract states.

## 1. Identity

| Item | Tazemetostat | TMP269 |
|---|---|---|
| ChEMBL | CHEMBL3414621 (parent, max phase 4, first approval 2020, chemical_probe flag 1); salt CHEMBL4594260 (hydrobromide) | CHEMBL3110004 per the GtoPdb row for ligand 7491; NOT present in the local ChEMBL molecules/mechanisms cache, REST unreachable, so the ChEMBL record itself is UNVERIFIED here |
| GtoPdb ligand | 7011 | 7491 |
| DGIdb | drug concept rxcui:2274378 (hydrobromide rxcui:2274379) | iuphar.ligand:7491 only (approved flag FALSE) |
| InChIKey | NSQSAUGJQHDYNO-UHFFFAOYSA-N | HORXBWNTEDOVKN-UHFFFAOYSA-N |
| Synonyms | EPZ-6438, E7438, Tazverik | TMFO1, TMP 269, "compound 1" in PMID 23524983 |
| Mechanism (ChEMBL) | INHIBITOR, "Histone-lysine N-methyltransferase EZH2 inhibitor", target CHEMBL2189110 (mechanisms.jsonl.gz, molecule CHEMBL4594260) | no mechanism row in cache |
| Annotated targets | EZH2: GtoPdb pIC50 7.96 (IC50 11 nM), ref PMID 23620515; DGIdb EZH2 (ChEMBL, TTD, CGI, CIViC, OncoKB), also ARID1A, SMARCB1, SMARCA4, KDM6A, IDH1, FLT3 as oncology context genes (not binding targets) | GtoPdb, ref PMID 23524983 (Lobera 2013): HDAC4 pIC50 6.80 (IC50 157 nM), HDAC5 7.01 (97 nM), HDAC7 7.37 (43 nM), HDAC9 7.64 (23 nM). DGIdb also lists GAS2/GDF9/MSTN rows for TMP269, which are gene-symbol mismatches of the GtoPdb NCBI ids (2620, 2661, 2660 are HDAC9, HDAC7, HDAC5), not real targets |
| Assay type of the potency | The cache row does not state assay type; PMID 23620515 describes an enzymatic EZH2 inhibitor (abstract only) | The cache row says "Not Determined"; assay type must be taken from the full text of PMID 23524983 (UNKNOWN here) |

## 2. Reasons (R) that could favour studying each compound

Evidence levels: M = measured in a stated system; I = inferred (no measurement of the step in that system); A = abstract only.
"WWOX link" says whether the reason is tied to a WWOX measurement; in every row below it is NOT, unless stated.

### Tazemetostat

| id | Step | Pharmacology required | Context and anchor | Evidence | Counter-evidence and unknowns |
|---|---|---|---|---|---|
| T1 | Direct, potent, selective inhibition of EZH2 methyltransferase lowers H3K27me3 | Direct target EZH2 (SAM-competitive), IC50 11 nM (GtoPdb, from PMID 23620515); selectivity described as "potent and selective" in PMID 23620515 and PMID 24563539 (abstracts); full selectivity panel not read | Human enzyme and cells; mouse xenograft PD with reduced H3K27me3 incl. "selected normal tissues" (PMID 24563539, abstract) | M (cancer models), A | No measurement in brain, neurons or glia. Selectivity numbers UNKNOWN (not read). |
| T2 | Premyelinating-oligodendrocyte state: Ezh2 represses neuronal and astrocytic programs; PRC2 loss in the OL lineage fails the myelin program and induces Notch genes, astrocytic features | Would require ENHANCING or restoring differentiation by EZH2 inhibition, but the literature shows loss of Ezh2 impairs OL maturation, so the direction is AGAINST inhibition | PMID 32937136 (Cell Rep 2020, mouse, PRC2 null OL lineage: no myelination, Notch up); PMID 22808153 (PLoS One 2012, Ezh2 ChIP-seq NSC/pOL: suppressing Ezh2 in pOLs derails the oligodendrocyte phenotype, apoptosis) | M (mouse genetics, rat/mouse cells), A | This is counter-evidence for a myelin rationale; no source shows that pharmacologic EZH2 inhibition improves myelin. WWOX-null hypomyelination (WM claim 003, Repudi 2021) is non-cell-autonomous, from neuronal deletion, so an OL-intrinsic epigenetic lever is not an obvious match (I). |
| T3 | Schwann cell myelination requires EZH2 | same direction as T2 (inhibition would hurt) | PMID 22821416 (Glia 2012, rat Schwann cells, EZH2 suppression lowers myelin genes, p57kip2 up); PMID 39359095 (Neural Regen Res 2024, Schwann-cell Ezh2 cKO mice with unmyelinated axons) | M, A | Counter-evidence (PNS, not CNS). |
| T4 | EZH2 as a protective factor in epileptogenesis | transient EZH2 inhibition after status epilepticus INCREASED later spontaneous seizure burden | PMID 31891591 (PLoS One 2019, rodent acquired-epilepsy models; abstract states inhibition raised seizure burden; compound used not read) | M (rodent TLE), A | Counter-evidence for an excitability rationale; a WWOX-DEE is not an acquired TLE model (UNKNOWN transfer). Also PMID 33035459 (Lancet Oncol 2020): a treatment-related serious adverse event of seizure in 1 of 62 patients (abstract); causality and denominator for CNS-disease unknown. |
| T5 | Neurodevelopmental PRC2 biology: EZH2 loss in zebrafish alters cerebellar progenitors and gives hyperlocomotion, OL specification and myelination markers preserved | genetic loss, not pharmacology | PMID 41097006 (Int J Mol Sci 2025, zebrafish ezh2 mutant, abstract) | M, A | Shows a neurodevelopmental cost of loss, no myelin cost in this model. PRC2-component germline variants cause overgrowth syndromes with epilepsy (EED, Cohen-Gibson, PMID 34533271, single case, abstract), so PRC2 hypofunction can itself be epileptogenic (I). |
| T6 | Brain exposure | needs free brain concentration at an effective level | PMID 25868794 (Int J Cancer 2015, mouse): tazemetostat (EPZ-6438) is a P-gp substrate; its brain accumulation is limited by P-gp and efflux is abolished by elacridar (abstract). Same paper calls it the most suitable of the series | M (mouse), A | Counter-evidence for CNS use; brain H3K27me3 reduction at tolerated exposure in a WWOX or any epilepsy model is UNKNOWN. |
| T7 | Epigenetic crosstalk, EZH2 inhibition raising H3K27 acetylation | pharmacology required: tazemetostat | PMID 38334611 (Cells 2024, mouse IDH1-mutant glioma and OPC-derived cells: tazemetostat lowers H3K27me3, raises H3K27ac, synergy with panobinostat) | M, A | Shows pharmacodynamic activity in OPC-derived cells in a tumour context only; says nothing about WWOX loss. |
| T8 | WWOX-EZH2 link | n/a | PubMed query "WWOX EZH2" returned 0 records; query WWOX with HDAC/polycomb/H3K27 returned only cancer papers: BMI1 (PRC1, not PRC2) binds and represses WWOX in SCLC cells (PMID 21276135, ChIP); Pc2-mediated SUMOylation of WWOX (PMID 26592150); WWOX/HDAC3/BCL9-2 (PMID 25678599) | M (cancer cell lines), A | No source ties EZH2 activity or H3K27me3 to WWOX deficiency in brain. The absence in PubMed is not evidence of absence (search is title/abstract only). |

Net for tazemetostat: the pharmacology (T1) and the identity are firm; every nervous-system anchor read points
neutral or against EZH2 inhibition (T2 to T4, T6). Any positive rationale would need a WWOX-specific H3K27me3 or EZH2
measurement that was not found (UNKNOWN).

### TMP269

| id | Step | Pharmacology required | Context and anchor | Evidence | Counter-evidence and unknowns |
|---|---|---|---|---|---|
| M1 | Class IIa HDAC (HDAC4/5/7/9) inhibition via non-chelating TFMO zinc binder | Direct target class IIa, IC50 23 to 157 nM (GtoPdb, from PMID 23524983); class selectivity shown by chemoproteomics against a hydroxamate analog (abstract) | Recombinant human enzymes and cells; the paper states catalytic-site-dependent gene regulation | M (in vitro), A | The assay type for the IC50 (substrate used) is UNKNOWN here. Class IIa enzymes have little activity on ordinary acetyl-lysine, so the cellular consequence of catalytic inhibition is uncertain; I could not retrieve the primary source for that statement via PubMed (search returned 0), so treat it as background knowledge, not an anchor. Off-target profile outside HDACs UNKNOWN (not in cache). |
| M2 | HDAC5 nuclear translocation and MEF2-dependent transcription in microglia drive NLRP3 activation, synaptic inhibitory clearance and hyperexcitability | would need inhibition of HDAC5 in microglia; but the paper's axis is "HDAC5 translocation frees MEF2A" so the direction of a catalytic inhibitor is not given | PMID 42173845 (Cell Death Dis 2026, mouse epilepsy models, abstract) | M (mouse), A | The paper targets MEF2A with parecoxib or AAV knockdown, not an HDAC inhibitor; whether TMP269 would help or hurt here is UNKNOWN. |
| M3 | HDAC5 downstream of hippocampal BDNF / synapse formation; HDAC5 knockdown reduces depressive-like behaviour | TMP269 used as pharmacological tool | PMID 38801927 (Biochem Pharmacol 2024, mouse learned-helplessness; abstract states TMP269 inhibited hippocampal HDAC5 and modulated BDNF) | M (mouse, systemic dosing), A | Indicates the compound has CNS pharmacodynamic effect in at least one mouse study (indirect brain-exposure evidence); exposure not measured in the abstract. Behavioural model, not DEE. |
| M4 | Neuroprotection in a neurotoxin model, with reversal of nuclear HDAC5 and lower microglial IBA1 counts | TMP269 itself | PMID 39842624 (Neuropharmacology 2025, rat 6-OHDA, cells and in vivo, peripheral infusion; abstract) | M (rat), A | Different disease (dopaminergic). Supports peripheral dosing reaching brain targets (I). |
| M5 | Class IIa HDAC4/5 are needed for Schwann cell myelin program | inhibition would be expected to IMPAIR myelination | PMID 29472387 (J Cell Biol 2018, conditional knockout mice: HDAC4 with HDAC5 redundantly contribute to the myelin program and myelin sheath in vivo; abstract) | M (mouse genetics, PNS), A | Counter-evidence for a myelin rationale; CNS oligodendrocyte role of class IIa HDACs not found in PubMed (search "HDAC4 AND oligodendrocyte" returned only expression papers, e.g. PMID 24657831 in stroke). |
| M6 | Class IIa HDAC expression in human epilepsy tissue | n/a | PMID 33258018 (Cell Mol Neurobiol 2020, human MTLE-HS hippocampus n=28 vs 20 post-mortem controls): HDAC4 and HDAC5 mRNA up, nuclear HDAC5 up (abstract) | M (human tissue), A | Association only, acquired adult epilepsy; says nothing on direction of benefit or on DEE/WWOX. |
| M7 | HDAC5 and metabolic or oxidative stress | HDAC5 inhibition causes iron-dependent ROS, mitophagy and metabolic reprogramming in cancer cells | PMID 28414307 (Oncogene 2017, cancer cells; abstract) | M (cancer cells), A | A cautionary signal for neurons under metabolic stress (WM claim 034 notes context-dependent WWOX-ROS sign); not shown in neurons. |
| M8 | WWOX link | n/a | no WWOX-specific HDAC4/5/7/9 evidence found; only WWOX-HDAC3 (PMID 25678599, breast cancer cells, deacetylase-independent) which is class I, not a TMP269 target | n/a | UNKNOWN. |

Net for TMP269: identity and class IIa potency are firm (GtoPdb, one primary paper); CNS pharmacodynamic activity in
mouse/rat is suggested by M3 and M4 (abstract level); excitability and glia anchors are in the right domain but the
direction is not established (M2) and the only myelin evidence (M5, PNS) argues against inhibition.

## 3. Cross-cutting counter-evidence and cautions

1. No anchor found links either compound to a measured WWOX-deficient phenotype (cell, organoid, mouse, patient).
   Every rationale is mechanistic inference from another system.
2. The working model's WWOX-DEE steps (hyperexcitability, non-cell-autonomous hypomyelination, metabolic stress) have
   their own priors; neither target (EZH2, class IIa HDAC) appears among them in the lines read by keyword (the only HDAC
   hit in the working model was a chemical-chaperone note, line 749).
3. Direction risk: for tazemetostat the myelin and epilepsy literature favours EZH2 activity (T2 to T4); for TMP269 the
   myelin literature favours class IIa activity in Schwann cells (M5).
4. Both are compounds whose published CNS evidence is predominantly abstract-level; none of the quantitative claims here
   were checked against the full text.

## 4. Data I could not obtain (UNKNOWN, not negative)

- ChEMBL REST (HTTP 500 on every call): no live activity table, no TMP269 ChEMBL record content, no selectivity panels.
- CHEMBL3110004 is named by GtoPdb but absent from the local molecules cache, so its identity as TMP269 is one-source.
- Assay type and substrate for the TMP269 IC50 values (needs full text of PMID 23524983) and for the tazemetostat 11 nM
  value (full text of PMID 23620515); tazemetostat kinase/methyltransferase selectivity panel numbers.
- TMP269 brain or CSF exposure, plasma stability and CNS penetration (PubMed query returned 0 records).
- Primary source for "class IIa HDACs have low intrinsic deacetylase activity" (not retrieved).
- Free brain exposure of tazemetostat at any tolerated schedule; paediatric CNS safety beyond the oncology phase-1 reports
  (PMID 29650362 reports adults and dose-limiting thrombocytopenia only).
- Any measurement of H3K27me3, EZH2 or class IIa HDAC localisation in Wwox-null or WWOX-variant neurons, glia or
  organoids.
- Full text of all anchors; locators are abstract-level only.
