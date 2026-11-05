# IT29 P3-B: genetic and pathway perturbations of oligodendrocyte differentiation and myelination, and what they imply for drug action direction

Non-canonical research material, not medical advice. Public edition: the subject is the WWOX-DEE reference genotype class; nothing here is a finding about WWOX. Package `phenotype_first_it29_20261105/p3_B`, scientist B, 2026-11-05, event-id suffix -06. Zero spend, no contact address sent to any service.

Endpoint (Case 1): differentiation of oligodendrocyte-lineage precursors into MBP-positive / myelinating oligodendrocytes and myelin formation; favourable = more differentiation or myelination. Rows are in `evidence_it29_B.tsv` (40 rows, ids B01-B40); receipts in `receipts/` (11 drafts, not recorded).

Already known and cited, not redone: IT14 P4 (`glia_maturation_it14_p4_20261101`: RESTRICT, driver upstream of the oligodendrocyte, no compound entered), IT28 P4-A (`batch_it28_p4_isr_role_20261105/A_glia_myelin`: ISR sign depends on the node perturbed), and the frozen abstention (`SELECTION.md`: 546 associations, all `no_coupling_row`). The IT28 P3 HDAC5 batch (`B_class_iia_biology`) holds no oligodendrocyte-lineage content (grep for myelin/oligodendro found none), so HDAC4/5 are taken here from first principles of the literature found.

## 1. Decision (10 lines)

1. Most targets can now be signed on a genetic basis for the **developmental** window in the oligodendrocyte lineage: HDAC1+2, HDAC3, PRC2 (EED), TCF7L2, mTORC1 (Raptor), RXRG, THRA, Hdac4+5 (Schwann only) are needed (loss = adverse); beta-catenin gain, GPR17, LINGO1, CHRM3, BMP are negative regulators (loss or block = favourable or advancing).
2. The signs map to drug direction only partly. Where a pharmacological inhibitor was tested in the same cell it often agrees with the genetic result for **HDAC3** (B09 v B10) and **RXR** (B27, B28), but disagrees in readout or mechanism for **ERK** (MEK inhibitors block differentiation in vitro, B21; double Erk1/2 knockout differentiates on schedule and loses thickness, B23: a **discordance**), **mTOR** (rapamycin v Raptor v Rictor, B21 v B24) and **HDAC3** (loss of the catalytic activation of the NCoR complex does not reproduce the Hdac3 fate switch, B11).
3. **HDAC inhibition is adverse, not favourable, in every developmental perturbation found** (pan-inhibitors B03, class I double loss B01, HDAC3 B07-B10, Schwann class IIa B38). A class I / pan-HDAC inhibitor therefore cannot be given a pro-myelinating sign from this literature. Only an isoform-selective HDAC1 or HDAC2 inhibitor is predicted inert (B02).
4. **EZH2 is not EED.** Ezh2 loss is a delay compensated by Ezh1 (B14); loss of PRC2 core (Eed) is a block (B13). A catalytic EZH2 inhibitor sits between: no inhibitor experiment was reached, direction `undetermined`.
5. **Wnt**: beta-catenin gain blocks the lineage (B04); the effector TCF7L2 is also required (B06); Wnt inhibition rescues only on a PRC2-null background (B15) and BMP sits downstream of Wnt (B32). **GSK3B was not reached** (no GSK3 manipulation read); beta-catenin stabilisation is not equivalent to a GSK3 inhibitor.
6. **CHRM3** (B25) and **GPR17** (B17-B20) have target-controlled genetic loss that is favourable; the GPR17 effect is an earlier onset and disappears in the adult null (B18). **CHRM1** genetics, **PPAR** genetics, **ISR** (see 3.10) remain unsigned in this package.
7. **Neuronal activity is a positive, selective, axon-level modulator** (B34-B36): activation raises OPC proliferation, differentiation and myelination of the active axon; silencing lowers it by about a quarter at the silenced axons. Initiation of wrapping in zebrafish does not need activity (B36). No source shows that the effect of a pro-differentiation target requires activity; the question was not tested in any row.
8. In a seizure circuit the endpoint can rise **because of** hyperexcitability and be harmful (B37): "favourable" for the endpoint is not "favourable" for the circuit.
9. Almost nothing here is from injury context in a neuron-free purified OPC system with a target control; the cell-autonomous rows are B09, B15, B19, B20, B25, B27-B29, B32, B33.
10. Net for INV-06 ("orderable or not"): signed levers exist (CHRM3, GPR17, RXR, THRA/B, LINGO1, BMP, Notch) but each is signed against a developmental or injury readout, none in a Wwox-deficient or activity-poor setting; the class stays a **role question with a conditional lead**, and the abstention is not overturned for HDAC, EZH2 or GSK3B.

## 2. Evidence by target

Direction columns: loss / gain are genetic unless marked compound. Depth: F full text, P partial full text, A abstract only. "Auton." = shown in purified OPCs. "Ctx" = developmental (D), injury (I), adult-uninjured (Ad).

| Target | Loss | Gain | Stage | Ctx | Auton. | Rows | Depth |
|---|---|---|---|---|---|---|---|
| HDAC1 / HDAC2 | single: null; double: adverse, no OPC markers in vivo, OPCs stall in culture | HDAC overexpression raises the Mbp reporter ~2 fold in a line | specification to terminal | D | OPCs stall in culture; in vivo not separated | B01, B02 | F |
| pan-HDAC inhibitors (VPA, TSA) | adverse (cited) | not applicable | differentiation | D | in vitro | B03 | F (citation) |
| HDAC3 | adverse, with OPC-to-astrocyte fate switch (embryo, P5-9 and adult induction); neuronal deletion no effect | Hdac3 overexpression in astrocytes induces OL genes | OPC identity to maintenance | D, Ad | yes (Cre in purified OPCs, B09) | B07-B12 | P |
| HDAC3 compound | RGFP966 / apicidin suppress Olig2 in OPCs (adverse) | n/a | OPC | in vitro | yes | B10 | P |
| HDAC4 / HDAC5 | Schwann: myelin transcripts down with Hdac4 cKO + Hdac5 null; Hdac5 alone null | not reached | Schwann myelination | D (PNS) | not separated | B38, B39 | P |
| HDAC4 / HDAC5 in CNS oligodendroglia | not reached | not reached | | | | | |
| EZH2 | delay, restored by P3 via Ezh1 | not reached | OL generation | D | in vivo | B14 | P |
| PRC2 core (EED) | adverse, block at differentiation, Notch/Wnt/NFIA de-repressed | not reached | terminal differentiation | D | immunopanned OPCs agree | B13, B15 | P |
| EZH2 catalytic inhibitor | not reached | | | | | | |
| beta-catenin / Wnt | loss: earlier OPC markers (specification; terminal not scored) | gain: adverse, no OPCs or OLs | specification and differentiation | D | in culture ligands inhibit | B04, B05 | F |
| TCF7L2 | adverse (no myelin genes) | dominant-repressive form promotes ectopic OPCs in chick | OPC to OL | D | not separated | B06 | F |
| GSK3B | not reached | not reached | | | | | |
| mTORC1 (Raptor) / mTORC2 (Rictor) | Raptor adverse; Rictor mildly favourable | not reached | immature to mature OL | D | in vivo | B24 | A |
| mTOR compound (rapamycin) | adverse (onset of myelination delayed, systemic) | n/a | immature to mature | D | in vitro plus systemic in vivo | B21 | P |
| ERK1/2 | double: differentiation on schedule, thickness adverse; single: null | not reached | thickness / myelin growth | D, Ad | cultured OLs agree | B22, B23 | A + cited |
| MEK/ERK compound | adverse early (progenitor to late progenitor) | n/a | early | D | in vitro | B21 | P |
| CHRM3 | favourable (human OPC knockdown, adult mouse cKO) | not reached | OPC to OL commitment | I (remyelination), Ad | yes (human OPCs) | B25 | A |
| CHRM1 | not reached | not reached | | | | | |
| THRA | adverse (fewer OLs, null OPCs do not respond to TH) | overexpression accelerates in culture | OPC cell-cycle exit | D | yes | B29 | A |
| TRB agonist | favourable (compound, GC-1) | n/a | OPC | D | not separated | B30 | A |
| RXRG | transient adverse (CC1+ down at 15 dpl), no final difference | agonism favourable in culture | OPC to OL | I | yes (compound) | B26-B28 | P |
| GPR17 | favourable early onset; adult null; progenitors in vitro earlier | adverse (transgene), agonist adverse | OPC to OL timing | D | yes (culture) | B16-B20 | P / A |
| LINGO1 | favourable (dominant-negative, RNAi, Fc, KO) | adverse (overexpression and soluble ectodomain, abstract of Jepson 2012 read) | differentiation | D, coculture | neurons present in coculture | B31 | A |
| BMP | Bmpr1a/1b loss or noggin removes Wnt3a and BMP4 inhibition; noggin alone null | BMP4 adverse (in vitro) | OPC to OL | in vitro | yes | B32, B33 | P |
| PPARs | not reached (genetics) ; compound curcumin via PPARG favourable | | | | | B40 | A |
| Neuronal activity | silencing (Kir2.1, VAMP2) adverse at the axon | DREADD activation favourable | OPC proliferation, differentiation, sheath stability | D (adult weaker) | no, needs axons | B34-B36 | P / P |
| Seizure activity | | seizures raise network myelination after onset; blocking it lowers seizure burden | | epilepsy | no | B37 | P |
| ISR | see IT28 P4-A (not redone): sign depends on node and context | | | | | | cited |

## 3. Evidence by theme

### 3.1 Class I HDACs: needed, in different ways
The double loss of Hdac1 and Hdac2 in the lineage removes Pdgfra, Olig2, Mbp and Plp from the spinal cord; single mutants are normal (redundancy). Beta-catenin gain phenocopies this and HDAC1/2 compete with beta-catenin for TCF7L2 in a line (B01, B02, B04; Ye 2009, full text). Hdac3 loss gives a different lesion: OPCs become GFAP astrocytes in vivo and in purified OPCs, with loss of myelin (B07-B09; Zhang 2016). So Hdac1/2 and Hdac3 are two independent adverse routes. Inhibitors tested in the same cells agree in sign (B10) but the one catalytic-dead complex test (NS-DADm, B11) does not reproduce the fate switch, which is the clearest place where "loss of protein" and "loss of deacetylase activity" part. The pan-inhibitors VPA and TSA are cited as adverse (B03).

**Discordance D1 (HDAC3, same question: does removing HDAC3 catalytic function reproduce the genetic fate switch?).** HDAC3-directed inhibitors suppress Olig2 in OPCs (B10), Hdac3 protein loss switches fate (B09), but the NCoR/SMRT deacetylase-activation-domain mutant does not (B11). Not averaged: the three rows measure different things (marker in culture, fate in cells, fate in vivo with catalytic activation removed only inside NCoR).

### 3.2 Class IIa HDAC4/5
No oligodendrocyte-lineage genetic study was found by title and abstract search (Europe PMC, three queries). The only genetic class IIa myelination study reached is in **Schwann cells** (B38, B39): combined loss lowers myelin transcripts, Hdac5 alone does nothing. These proteins act as corepressors with minimal deacetylase activity (introduction of that paper), so a catalytic inhibitor may not act on the same function. Direction in the CNS lineage is `undetermined`; the Schwann sign is `adverse` for loss and is not transferable without a CNS test.

### 3.3 PRC2 / EZH2
Loss of the PRC2 core protein Eed in the lineage blocks differentiation; OPCs are generated and proliferate normally, Notch, Wnt, BMP target sets and NFIA are de-repressed, and inhibitors of Notch (LY411575) or Wnt (XAV939) rescue Mbp in the null OPCs (B13, B15). Ezh2 alone gives a transient delay restored through Ezh1 (B14). Implication for drug direction: PRC2 inhibition at the EED level is predicted adverse; a catalytic EZH2 inhibitor is not signable (Ezh1 compensation, no inhibitor test).

**Discordance D2 (what happens on EZH2 loss: block or delay).** Eed deletion = persistent block (B13); Ezh2 deletion = delay with recovery (B14). Different alleles of the same complex; kept as different rows.

### 3.4 Wnt, GSK3B, BMP, Notch
Wnt gain is adverse (B04) but the Wnt effector TCF7L2 is required (B06), and a later paper by title argues TCF7L2 acts independent of beta-catenin (Hammond 2015, not read). BMP blockade (noggin or Bmpr1 deletion) cancels both Wnt3a and BMP4 inhibition in purified OPCs, and noggin alone does nothing (B32, B33): in culture a BMP-pathway drug is predicted to matter only when ligand is present. GSK3B itself was not reached: stabilising beta-catenin is adverse in the genetic test (B04), but a GSK3B inhibitor changes other substrates; sign `undetermined`.

### 3.5 mTOR, AKT, ERK
Stage-resolved pharmacology puts ERK before the late-progenitor stage and mTOR at immature-to-mature (B21), rapamycin delayed myelination in early postnatal mice (B21, systemic). Genetics refines this: Raptor loss is adverse, Rictor loss mildly favourable (B24, abstract), so a rapamycin-like mTORC1 inhibitor is predicted adverse and an mTORC2-directed one mildly favourable, which no compound separates cleanly. Double Erk1/2 loss does not stop differentiation; it stops thickening (B23).

**Discordance D3 (is ERK needed for OPC differentiation).** MEK inhibitors block differentiation in vitro (B21, cited and the authors' own stage result); single and double Erk knockouts do not (B22, B23). Not averaged; likely reasons stated by the sources are single-isoform redundancy and in vitro versus in vivo, but both double-knockout and inhibitor data are from different systems. AKT was not reached.

### 3.6 CHRM1/CHRM3, TH, RXR, GPR17, LINGO1, PPAR
- CHRM3: target-controlled favourable on loss, in human OPCs and adult mouse (B25, abstract only). The repository's muscarinic antagonists (benztropine, clemastine in IT14 P4) now have a genetic counterpart for CHRM3 only; CHRM1 genetics were not reached, so M1 versus M3 attribution of a given antagonist stays open.
- THRA / THRB: Thra loss adverse (B29); a TRB agonist favourable in development (B30). Direction of receptor modulation is activation-favourable. Thyroid hormone supply was not manipulated in vivo here.
- RXRG: agonism favourable in OPC culture, with antagonist control (B27, B28); knockout lesions show a transient deficit (B26) that is compensated.
- GPR17: loss favourable for onset, no adult effect (B17-B19); agonist adverse (B20).
- LINGO1: loss favourable including in coculture with neurons (B31).
- PPAR: no genetic result reached; one compound row (B40).

### 3.7 Neuronal activity and axonal signalling
Activation of cortical axons with DREADD raises OPC proliferation and differentiation and the probability and thickness of myelination on the stimulated axons; reducing excitability with Kir2.1 lowers it on those axons (B34, B35, Mitew 2018). In zebrafish, wrapping initiation does not require activity but sheath stability does (B36). Adult stimulation showed an effect only at 2 weeks, not at early time points (B34 effect note). In an absence-epilepsy network, seizure activity itself raises oligodendrogenesis and thickens myelin after onset, and OPC TrkB deletion blocks that and reduces seizure burden (B37). What this means for the WWOX case: the pro-differentiation targets above were mostly signed without regard to the neuronal signal; **none was tested as to whether its effect needs axonal activity**, so conditionality on the neuron-driven deficit is untested. The three-way contrast (initiation v refinement v seizure-driven excess) means a push on OPC differentiation could be present without neuronal input but may be ineffective at keeping sheaths on low-activity axons.

### 3.8 Genetic versus pharmacological, summarised
| Target | Genetic | Pharmacological | Agree? |
|---|---|---|---|
| HDAC3 | loss: fate switch, adverse (B07-B09) | inhibitor: Olig2 down (B10); catalytic-dead complex: no fate switch (B11) | partly (D1) |
| ERK | double loss: differentiation normal, thickness adverse (B23) | MEK inhibitors: differentiation adverse (B21, B22) | no (D3) |
| mTOR | Raptor adverse, Rictor mildly favourable (B24) | rapamycin adverse (B21) | partly |
| EZH2 / PRC2 | Ezh2: delay; Eed: block (B13, B14) | not reached | unknown |
| RXR | Rxrg loss: transient deficit (B26) | agonist favourable, antagonist adverse (B27, B28) | consistent in sign, differs in size |
| GPR17 | loss: early onset (B17) | agonist adverse (B20), antagonist not read | partial |
| CHRM3 | loss favourable (B25) | antagonists class: see IT14 P4 | consistent by class |
| Class I HDAC | adverse | adverse (B03, B10) | consistent |

## 4. What is not established
- The sign of a pan-HDAC or class I inhibitor on remyelination or in an injury context (the one source surfaced for HDAC1/2 in injury is **retracted**: Zheng 2017, excluded).
- CNS oligodendroglial roles of HDAC4/5 and of class IIa catalytic versus scaffold function.
- Any EZH2 catalytic inhibitor in OPCs; GSK3B; AKT; CHRM1; PPAR genetics; ISR beyond IT28 P4-A.
- Whether any of these effects depends on neuronal activity or on neuron-derived signal; whether any holds in a hypomyelinated, seizure-prone, neuron-driven deficit.
- Effect sizes beyond the quoted text for abstract-only rows (B05 for terminal differentiation, B20, B23-B25, B29-B31, B40).
- Human relevance: only B25 uses human OPCs; a clinical remyelination study of an RXR agonist and LINGO1-blocking antibody trials were seen by title only and not read.

## 5. What was not reachable and what would reopen it
- Full text not retrieved (publisher copies empty or not in the open XML): Bercury 2014, Ishii 2012, Welliver 2018, Jepson 2012, Mi 2005, Billon 2002, Simon 2016, Baxi 2014, Bernardo 2021; these are abstract-only rows, direction is taken from abstracts.
- Figures and supplements of all sources; figure values not read.
- NCBI esearch returned server errors during this session, so the search used Europe PMC titles and abstracts; coverage of the literature is not systematic.
- Would reopen: a primary-OPC study of an EZH2 catalytic inhibitor with Ezh1 status; an HDAC4/5 oligodendroglia knockout; GSK3 inhibitor with genetic control in purified OPCs; a muscarinic antagonist tested on Chrm1 and Chrm3 knockouts in the same assay; any of the pro-differentiation targets tested in neuron-OPC cocultures with activity silenced (tetrodotoxin or Kir2.1).

## 6. Interpretation guards
- A knockout is not an inhibitor: B02, B11, B13/B14, B23 are the places where this matters most.
- "Favourable" follows the task definition (more differentiation or myelination); B37 shows that this is not a statement of net benefit.
- Nothing here gives dose, schedule, route or preparation; no individual-level record is involved.

> **Note, IT29 P10 (CH-IT29-CLASSIIA-CNS-MYELIN, 2026-11-05).** The row 'HDAC4 / HDAC5 in CNS oligodendroglia' stays empty after bounded searches by three further readers (`cycle_it29_p10_20261105/p10_F`, `p10_G`, `p10_H`). The Schwann-cell source (PMID 29472387) shows a transient delay in a double mutant, recovered by P8, with a scaffold mechanism; it is not evidence that class IIa HDACs are required for myelination.
