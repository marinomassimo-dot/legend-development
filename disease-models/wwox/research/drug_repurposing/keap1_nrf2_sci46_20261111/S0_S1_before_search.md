# SCI46 S0/S1 — the KEAP1/NRF2 comparison: frame, explanations and priors, written before any new reading (2026-11-11)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; no compound is promoted. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI / ESPANSIONE. Task record `ledger/tasks/orchestrator/ORCH-SCI46-20261111.json`. A later change to this file is a dated addendum, not an edit. Paths relative to `disease-models/wwox/research/drug_repurposing/`.

## S0 — state found, and the perimeter

* **Deliveries.** SCI45 P1, Q1 and N1 are consumed on `main` (IT45, 54 receipts recorded, ledger 1,787; open questions IT45-Q05..Q08; message of the IT45 Orchestrator, commit bfd5304e, record 142f6c5f). Nothing of SCI45 is repeated here.
* **Material read before the frame:** `next_batch_it45_20261111/BRIEFS.md` B1; `generation_it45_20261111/s10_dose/result_it45.md` and `selection_it45.md`; `generation_it45_20261111/verify_s10/VERDICTS.md` (the independent reader of IT45: three of eight documents in full, five abstract or ChEMBL transcription [CH]); `nrf2_inv08_20261107/output/` (README, hypotheses H1–H6, wwox_table W01–W11, experiment X0–X4). Bibliographic identity checked in PubMed (metadata only): 27031670 is Davies TG, Wixted WE, … Heightman TD, Kerns JK, J Med Chem 2016;59(8):3991-4006, DOI 10.1021/acs.jmedchem.6b00228, "Monoacidic inhibitors of KEAP1:NRF2 PPI with high cell potency identified by fragment-based discovery"; Astex and GSK authors; not in PMC and not open access (PubMed copyright tool).
* **Starting comparison (IT45):** a covalent electrophile and a non-covalent KEAP1 Kelch binder, each with and without NFE2L2 knockdown, read on a target-gene set, in neurons and astrocytes separately. It is a design proposal, not an approved one, and this package may replace a tool or narrow the question.
* **Perimeter communicated to IT46:** one central package (the binder's source, its knockdown arm, the comparators that decide the pair, neural transfer); a single queue item afterwards. Nothing of this file waits for an approval.

## What is observed in WWOX-deficient neural systems (re-stated from the held record, no new reading)

| Layer | State | Source in the repo | Label |
|---|---|---|---|
| Transcripts | NFE2L2 0.75x and NQO1 0.73x lower, HMOX1 1.67x and SRXN1 1.33x higher in a KO cerebral organoid (4 v 2 libraries, post hoc WT exclusion); NFE2L2 lower with NQO1 up in shWWOX neural cells (n = 1 per arm, progenitor arm failed the WWOX gate); Hmox1 and Srxn1 modestly up in P47T brain, composition not excluded | `nrf2_inv08_20261107/output/wwox_table.tsv` W01, W02, W05 | DATO, transcript only |
| NRF2 protein | none measured in any WWOX-deficient mammalian neural system | W08 | absence at two routes, title/abstract depth |
| Nuclear localisation | none measured; one non-neural cancer-cell abstract has WWOX activity lowering nuclear NRF2 (W07) | W07, W08 | absence |
| Target-gene activity | NQO1 enzyme activity: none; transcripts only | W01, W02 | absence |
| Redox state | higher H2O2 in fly neurons (N 9–11); late-passage MEF ROS up, early not; no mammalian neural ROS measure | W03, W04 | DATO, other systems |
| Survival | not measured against an oxidative challenge in any WWOX neural system | — | absence |
| Function | none; the neuron-specific deletion gives the phenotype, glia deletions do not (flat, underpowered) | W09 | DATO |
| GSK-3β arm | pSer9 down at P20 with total unchanged (one lane per region) | W11 | DATO, limited blot |

The measures are not equivalent: a transcript is not protein, protein is not nuclear localisation, localisation is not target activity, and activity is not function. The proposal below is conditional and says so.

## Competing explanations (H1–H6 of INV-08, unchanged) and the result that would change a choice

| Explanation | A result that favours it | The choice it changes |
|---|---|---|
| H1 insufficient response | lower nuclear NRF2 and NQO1 activity at baseline or after a challenge, genotype-dependent; activation corrects and the correction is lost under NFE2L2 knockdown | proceeds to an activation arm in that compartment |
| H2 induced, still insufficient | target activity already high; more activation changes function further or does not | a ceiling: pick an arm that acts downstream of NRF2 or on the deficit itself |
| H3 compartment | effect of an astrocytic NFE2L2 loss on neurons with intact neuronal NRF2; neuron-only loss without effect | which cell receives the genetic arm and the compound |
| H4 cell type or stage | target response differs between stages or classes | when and where the first reading is taken |
| H5 compound benefit independent of NRF2 | effect unchanged under NFE2L2 knockdown for a given compound (NF-κB, HCAR2, GAPDH, other) | that compound is not an NRF2 probe; it may still be a lever |
| H6 no benefit or worsening | viability or network worse under activation | stop; the axis is a risk arm |

Rule for this package: loss of effect under a **sufficient** knockdown favours dependence; an unchanged effect favours independence only if the knockdown is shown to be adequate (protein and target-gene loss); a partial loss is partial dependence or an inadequate knockdown, and the two are separated by the knockdown's own verification, not by the endpoint.

## Priors fixed before reading (recollection or inference; unverified; scored afterwards, may fail)

* **P1.** The Davies 2016 text is not open by any route reached by plain curl and the PubMed/PMC tools. (Basis: PubMed copyright tool, no PMC id.) Consequence if true: the knockdown arm can be read only through ChEMBL's curated assay lines, which are a transcription and keep the label [CH].
* **P2.** The lead of Davies 2016 (ChEMBL parent CHEMBL3819587) is the compound later distributed as a chemical probe and cited under another name. *Recollection, not a datum:* I recall the name KI-696 for it; this is to be checked against a document, not assumed.
* **P3.** Where a non-covalent KEAP1 binder has an NRF2-siRNA arm, the induction of target mRNAs falls strongly but not to baseline for every gene; a residual effect is reported or is visible in the figures.
* **P4.** No source reached tests a non-covalent KEAP1 binder in primary neurons or astrocytes with NRF2 loss. Absence claim: perimeter and two routes will be stated by the producer.
* **P5.** For dimethyl fumarate in neural cells, at least one source shows loss of the protective or target-gene effect in Nrf2-null cells, and at least one source shows an NRF2-independent route (HCAR2 for the monoester, NF-κB, GAPDH) for the same compound. Both can be true at once; they concern different endpoints.
* **P6.** For sulforaphane in neural cells, the target-gene induction is NRF2-dependent while some anti-inflammatory endpoints persist in Nrf2-null cells.
* **P7.** No single paper contains both a covalent modifier and a non-covalent KEAP1 binder with an NFE2L2-loss arm in one cell type. If true, the pair is built across papers and the cross-paper arithmetic is not allowed: the interpretable comparison needs a new measurement, and this package says which design makes it interpretable.
* **P8.** NQO1 alone is shown by at least one source to move without the NRF2 pathway (progesterone is named in 31411465): a single-gene readout is not a mechanism readout.

## What the producer must establish, in the order that spends effort well

1. **Identity of the binder.** Compound, salt/stereochemistry if stated, the numbering in each article it appears in (Davies 2016; Tran 2019 compound 9 per its Figure 1 legend; any later paper), the ChEMBL parent id and its relation to the catalogue's `tool_probe` row; whether a name used in a later paper (including KI-696) is that structure. Numbering is not transferred between articles without the document stating it.
2. **Source and access of the knockdown arm.** What was knocked down (NFE2L2 mRNA, protein), how verified, controls, cells, time, concentration, which endpoints fell and by how much, which effects remained. If the primary is unreachable by the one allowed route, the knockdown values are not claimed; the ChEMBL assay lines are quoted as [CH] and the limit stays.
3. **Alternatives declared by criterion, if the first binder is unusable.** A non-covalent KEAP1 binder with a documented NRF2-loss arm (siRNA, shRNA, knockout) and an accessible full text; a covalent modifier with an Nrf2-null or knockdown arm in a neural or glial cell; a genetic comparator (KEAP1 loss or NFE2L2 gain). Criteria written in the brief, not chosen by the search.
4. **Neural transfer.** What carries over from epithelial, hepatic or myeloid cells to a neuron or an astrocyte: target presence, compound action, dependence, endpoint, exposure, developmental stage. External-stress rescue is kept apart from WWOX loss, and a viability rescue is not a functional recovery.

## What no further reading can resolve (stated now)

Whether NRF2 is insufficient, already induced or compensating in a WWOX-deficient neural cell; whether any KEAP1 or NRF2 intervention helps a WWOX-relevant function; the compound's exposure in the tissue. These need the premise measurement (X0) and the arms (X1–X3); this package defines the discriminating comparison and the readings that make it interpretable, and commissions nothing.
