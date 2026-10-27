# W2 therapeutic research beyond the metabolic thread (iteration 2)

Actor `scientist-c`, task `SC-IT2-THERAPEUTIC-20261027`, mandate `ORCH-ROADMAP-IT2-20261027`, 2026-10-27.
Non-canonical research material. Every non-WWOX source is **NOT WWOX EVIDENCE**. No dose, no suitability
statement, no efficacy claim, no score. Nothing here is medical advice. Statements tagged INFERENZA or IPOTESI
are **owed a blind audit by someone other than the producer** (section 7 lists the decisive ones).

Files: `organoid_panel.py` -> `organoid_panel_cpm.tsv`; `chembl_pull.py` -> `chembl_w2_rows.tsv`;
`build_cards.py` writes cards `F01`, `F02`, `F03` into `../cards/` (`check_cards.py`: 19 packets, 0 problems).
Commit candidate: `../../commit_candidates/CC-20261027-SCIENTIST-C-W2-THERAPEUTIC-01.md`.

## 1 · Threads chosen, and why these

Reading order followed the brief: the mechanism map (R-02, R-04, R-07, N-02, N-12, N-13, Chains B, F, G), the blind-spot
note, the handoff rows (`Q-R-02`, `Q-R-07`, `Q-N-13`, `Q-N-12` all still READ or AUDIT rows), the dismissal and hypothesis
surfaces through `registry_records.py`, and the paper manifests behind them, before any outside search.

| Thread | Goal covered | Why chosen (not the top historical score) | Outcome |
|---|---|---|---|
| **F01** glutamate-receptor node: NMDAR (memantine) and AMPAR (perampanel) | partial benefit / protection of function | The chain rests on one reading whose direction the record had not stratified; a 2026 cohort splits memantine response by receptor lesion sign; the AMPAR arm was never a node although it has the only direct synaptic measurement | card `F01`, status hypothesis, wet-lab spec |
| **F02** myelination: pro-myelinating agents and the activity-dependent myelination sign | broad functional recovery (developmental endpoint) | The only structural-recovery lever in the map; an assumption in DL-MECH-031 has a counter-precedent | card `F02`, **abstention** with reasons |
| **F03** bumetanide, chloride gradient (the "single experiment" ask) | partial benefit | Handoff row `Q-R-07`; premise unmeasured | card `F03`, **abstention**, experiment written out, one identity correction |

Considered and **not carded** (abstention with reasons, nothing hidden):

- **Lithium / GSK3B.** Nothing new is executable: the open item is the genotype-contrasted PTZ arm (N-02, R-04), already
  the reopening trigger. Class: non-genotype-specific anticonvulsant, direction conflicted on Wnt. No new datum found.
- **HSP70 co-inducers / chaperones (Q-N-12).** The decision turns on one measurement of a destabilised SDR missense under
  HSP70 amplification; no public analysis or reread can supply it. Stays withdrawn on an untested direction.
- **Readthrough.** The reference genotype class is a destabilising SDR missense plus a canonical splice-acceptor allele
  (map Chain F, G); neither carries a premature stop in the stated analysis, and the acceptor allele loses the last exon
  (no downstream junction, so NMD-escape rather than a readthrough target is the open question, which is
  `splice_allele_rna_evidence_20260922.md`'s unmeasured transcript). No candidate to carry.
- **ASO / base editing of the acceptor allele.** N-10 and R-08 stand; the position rule (-2, within 5 bp) keeps the allele
  "not eligible" for a splice-correcting ASO regardless of a transcript test. Base/prime editing is the valid
  arm and is gene-editing, not repurposing; nothing executable was added.
- **SDR16C family compensation.** Transcripts of the family in the organoid are either flat (DHRS3, RDH10 within 1.5-fold)
  or near zero (SDR16C5), with composition confounding; no compensation hypothesis with a testable direction results.
  Abstain; reopening condition: a family-member measurement in a Wwox-deficient neuron.

## 2 · F01 — what the record held and what is new

**Biological need and endpoint.** Neuron-specific Wwox loss gives neocortical bursting (knockout 36 of 42 slices, wild type 0
of 11, heterozygote 4 of 23; PMID 34634460 manifest entry 0). Endpoint pursued: burst frequency/duration/amplitude/PAC under a
graded drug exposure, then a maturation endpoint. Burst control is **not** developmental recovery (N-15).

**Measured (DATO), first-hand re-read of the shared full-text XML on 2026-10-27, receipt of the paper unchanged**
(`FTR-20260810-34634460-02`):

- d-APV 50 uM, a *competitive full* NMDAR block, eliminated bursting; n = 5 slices, 3 animals (Fig 3D legend).
- mEPSC amplitude is raised in the knockout (10 cells per genotype from 4 wild-type, 5 heterozygote, 5 knockout animals; KS test on pooled events); frequency
  is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4); decay unchanged. INFERENZA
  (mine, not the paper's): at -70 mV NMDAR current is largely Mg-blocked, so the recording is probably AMPAR-weighted; it does **not** measure NMDAR current.
- A knockout-specific delayed evoked response is NMDAR-dependent (Supplementary S3, attested in the manifest).

**Slip found in the source wording (not in the repository's wording):** the paper calls d-APV "a glutamatergic blocker"
and writes "blocking glutamatergic neurotransmission with d-APV". d-APV is NMDAR-selective; the AMPAR contribution was
never tested. The map treats the dependence as NMDAR-only, which is correct, but nothing in the record says the AMPAR arm
is untested.

**INFERENZA (new).** The convergence argument DL-MECH-002 ("GRIN2A causes the same burst-suppression phenotype, so the NMDAR
is a shared node") establishes the node, **not the sign of an intervention on it**. Evidence: Karnstedt 2026, *Epilepsia*
(PMID 41489401, PMC13075606; PMC full text retrieved through the PMC API, results and Table 1 read, supplements not read,
**no receipt**): memantine benefited 14 of 19 individuals with gain-of-function GRIN variants (4 of the 14 faded, 10 sustained; variant-level
sustained-only analysis P = 0.0698, not significant) versus 3 of 15 with loss-of-function, indeterminate or no-effect
variants (the 15 include 4 non-pathogenic variants) (Fisher P = 0.0049); behaviour 12/17 vs 3/15, development 6/12 vs 1/14;
seizure-frequency reduction 7/18 vs 2/10 **not** different (P = 0.417); three gain-of-function individuals worsened. A
retrospective, unblinded, clinician- or parent-rated series. The Riccardi cohort abstract (PMID 42190144) retrieved here has
its gene symbols stripped and does not state the GRIN2A variant class, so which side of that divide the burst-suppression
GRIN2A cases sit on is **unknown** (and the registry holds the abstract only: handoff row `Q-N-03`, `NO_RECEIPT`).

**Difference from other diseases, stated.** GRIN-related disease is a receptor channelopathy with a typed lesion; WWOX loss
is a non-channel cause whose network consequence recruits NMDAR. NMDAR *dependence* of the burst is permissive and does not
show raised NMDAR function. Partial use-dependent pore block (memantine) is not the full competitive block (d-APV).

**Counter-evidence retrieved.** Alekseeva 2026 (PMID 42652189, receipt `FTR-20261019-42652189-01`, in-repo, adult rat provoked
seizures): memantine accelerated every seizure stage; perampanel delayed stage 4 but did not prevent seizures. Memantine
openFDA label (2026-10-27): paediatric safety and effectiveness not established; two controlled paediatric autism studies
failed. PubMed query "memantine neonatal rat apoptosis" returned only protective injury models (hyperoxia, hypoxia-ischaemia,
dexamethasone-excitotoxicity); the classical developmental NMDA-antagonist apoptosis literature did **not** surface for
memantine, which is a retrieval result, not a safety statement. One adult WWOX case on seven antiseizure drugs including
perampanel: "no sustained positive effect" (PMID 39507621, receipt `FTR-20261019-39507621-01`); n = 1, uninterpretable.

**Dossier in a table, the new AMPAR arm.** Perampanel: ChEMBL_37 mechanism CHEMBL1214124 "Glutamate receptor ionotropic AMPA
antagonist" (action ANTAGONIST), label for partial-onset seizures from 4 years and adjunct primary generalised tonic-clonic
seizures from 12 years (openFDA effective 2025-12-19). **The adapter label sections returned no warnings section, so the
labelled safety profile was not assessed.**

**Executable deepening (6).** Public-data analysis `organoid_panel.py` on GSE156243 (4 knockout vs 2 wild type, week 15,
one laboratory; descriptive CPM, no test): no consistent GRIN2B/GRIN2D shift; GRIN2A (0.7-5 CPM) and GRIN3A are low-count; GRIA1 is
higher in two knockouts (150, 162 vs 90-105 CPM in wild type) and overlaps wild type in the other two (103, 98); and composition (GAD1, regional markers) differs ten-fold, so this is
at most a prompt, not evidence; direction recorded UNKNOWN in the card. Transcript is not receptor function.

**ChEMBL identity and pharmacology (4, 5).** Memantine (CHEMBL807): no curated mechanism row in ChEMBL_37 (the adapter
returns "molecule without mechanism"); 37 NMDAR IC50/Ki rows (22 human, 15 Rattus norvegicus targets; organism column added) in `chembl_w2_rows.tsv`,
spanning 0.95 nM to 100000 nM across assays (the lowest looks like an outlier or unit error and is not used). Potency is
assay-, voltage- and Mg-dependent; Karnstedt's own wild-type table gives low-micromolar values for GluN2A/2B and sub-
micromolar for GluN2D under voltage clamp. No value is carried as a target exposure.

**Wet-lab spec (not done).** Question: which receptor carries the raised excitatory gain, and does a partial block that
tolerable exposure could reach reproduce the full block? System: Wwox-deficient vs parental/isogenic neurons or juvenile
slices (the authors bound the age window). Arms: vehicle, graded memantine, perampanel, d-APV, washout. Controls: wild type
and heterozygote slices (the heterozygote bursts in 17 percent), an NMDA:AMPA ratio under voltage control (not mEPSC decay).
Endpoints: burst frequency, duration, amplitude, PAC; then a maturation endpoint. Discriminating result: partial block
abolishes burst in knockout and spares wild-type activity (lever) versus only the full block works (permissive dependence;
strand closes).

## 3 · F02 — pro-myelinating agents: abstention, with two findings

1. **Assumption with a counter-precedent.** DL-MECH-031 point 2 (`IPOTESI`) reasoned that because myelination is
   activity-dependent, reducing seizure load might improve myelination. Knowles 2022, *Nat Neurosci* (PMID 35501379; abstract
   only, absence-seizure models, other disease): seizures drive oligodendrogenesis and myelination in the seizure network,
   seizure suppression prevents it, and blocking activity-dependent myelination lowers seizure burden. The Wwox-null brain is
   hypomyelinated *despite* bursting; neither sign is established. Also (PMID 27292539, title only) oligodendroglial NMDA
   receptors support axonal energy metabolism: chronic NMDAR block in F01 carries an unmeasured myelin-side cost.
2. **Precision on the neuronal-rescue myelin claim.** Manifest `PMID42422765` entries 6, 7 and 43 (receipt
   `FTR-20261019-42422765-01`): the "near-complete rescue at high dose, partial at low dose" is the authors' sentence on
   representative micrographs; the only MBP quantification in the paper is knockout vs wild type (printed labels 48/30/50/70 percent read as the size of the reduction, i.e. about 50/72/49/30 percent remaining, by
   region); the panel with the treated arms has no untreated-knockout column and no stated age; no g-ratio or electron
   microscopy. DL-MECH-031 records "MBP intensity only" but not that the treated-arm rescue is image-level. Not a wrong
   record, an under-qualified one; it matters because the "secondary to the neuron" inference leans on neuronal rescue.
   The oligodendrocyte-promoter vector gave no detectable WWOX (entry 17, 45), so that arm tests nothing about oligodendroglial relevance.

Organoid OPC-lineage transcripts (PDGFRA, OLIG1 higher in knockouts; SOX10, MOG, OLIG2 not) are very low-count and
composition-confounded; a week-15 organoid has no compact myelin. Not myelin evidence.

**Decision.** N-13 stays deprioritised. No drug is carded. Wet-lab spec in card `F02`: one chronic activity-suppression arm
and one activity-raising arm against vehicle, quantified MBP and electron-microscopy g-ratio, wild-type and neuronal-restoration
controls; the direction of the change decides which of the two myelin hypotheses survives.

## 4 · F03 — bumetanide

Identity: ChEMBL_37 curates bumetanide's mechanism as **NKCC2** only (CHEMBL1874); NKCC1 (target CHEMBL1615383) has three
activity rows (two single-concentration inhibitions of 58.8 and 71.7 percent in transfected HEK cells, one fitted IC50 of
1540 nM by rubidium uptake in HT-29 cells; documents CHEMBL5038596, CHEMBL5230131). The map's "target NKCC1" is therefore an
activity-table fact. Descriptive organoid ratio SLC12A2/SLC12A5 (`organoid_panel_cpm.tsv`): 0.24, 0.29, 0.13, 0.14
(knockouts) vs 0.29, 0.30 (wild type): no transcript hint of a more depolarising gradient; confounded; transcript is not
E_GABA. GABRB2/GABRB3 transcripts are lower in knockouts (the pattern behind DL-MECH-035). Trials: titles retrieved only
(NEMO, PMID 25765333, open-label dose-finding in newborn seizures; phase 3 and phase 2 autism programmes, PMID 35292925 and
32730977); **outcomes not read**. The single experiment, as specified in the card: gramicidin perforated-patch E_GABA in
Wwox-deficient vs parental neurons at three ages, NKCC1/KCC2 protein, GABA puff response; controls wild type, heterozygote,
gabazine, an NKCC1 knockdown arm; discriminating result a depolarised E_GABA that an NKCC1 manipulation shifts.

## 5 · Measured, inferred, hypothesis (summary)

| Statement | Tag | Basis |
|---|---|---|
| d-APV eliminates bursting; mEPSC amplitude raised; delayed response NMDAR-dependent | DATO | receipted reading, first-hand reread of text and legends |
| Karnstedt response split by receptor lesion sign | DATO (other disease) | PMC full text read, no receipt |
| NMDAR dependence is permissive, not evidence of raised NMDAR function | INFERENZA | design of the slice experiment |
| AMPAR is the better-supported untested node | INFERENZA | mEPSC at -70 mV reads AMPAR |
| Chronic NMDAR block may cost myelin | IPOTESI | other-disease titles/abstract only |
| Activity sign for myelin in Wwox-null brain | IPOTESI | unmeasured |
| Organoid transcripts | INFERENZA | descriptive, 4 vs 2, composition-confounded |

## 6 · What was not done or verified

- No wet-lab; no safety triage run (`legend-safety-triage` not invoked; BLOCK-1 unassessed for both drugs).
- Karnstedt supplements, and the full text of Knowles 2022, Saab 2016 and the bumetanide trials, were not read.
- Memantine paediatric developmental-safety literature: one retrieval attempt only, inconclusive.
- Perampanel labelled warnings not retrieved. openFDA "adverse event" counts not used.
- The cited S3 supplementary panel was not re-seen (supplement docx unserved); relied on the manifest attestation.
- ToolUniverse not used (nothing it would save).
- Time spent: about 2.5 hours of session time; no receipts staged (no new full-text read of an unreceipted paper was completed: Karnstedt was read through the API without a receipt and is declared `partial_fulltext_read` in the card).

## 7 · Conclusions that need an independent verifier

1. The Karnstedt numbers (14/19, 3/15, P values) transcribed into F01 and this note.
2. The reading of Breton section 2.3 (AMPAR-weighted recording is an inference; decay-time reading) and the "d-APV is not a glutamate-wide blocker" point.
3. The statement that DL-MECH-002 corroborates the node but not the sign (depends on the unknown GRIN2A variant class in the cohort; check the full text of PMID 42190144 once a lawful copy is held).
4. The F02 precision point on `PMID42422765` entries 6, 7, 43.
5. ChEMBL identity statements (bumetanide NKCC2-only curated mechanism; memantine no curated mechanism) as of release 37.
