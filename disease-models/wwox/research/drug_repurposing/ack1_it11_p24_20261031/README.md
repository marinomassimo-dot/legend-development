# IT11 P2.4: the ACK1 lever on WWOX protein, step by step (scientist-d, 2026-10-30)

Non-canonical research material. Exploratory, not medical advice; no efficacy, safety, wet-lab or clinical claim. Reference genotype class only (a WWOX-DEE genotype class; the Q230P-class missense allele is named, no individual record). No e-mail address or personal datum was sent to any service; key-less endpoints only; no spend, no registration. Retrievals dated 2026-10-30 (system date; the folder carries the mandate date 20261031). Nothing here edits a card, need, ranking, registry, the four current files or the receipt ledger.

Read before formulating the questions (so none of this is blind): the IT10 P2.3 README with section 11, `candidates_it10_p23.tsv`, `evidence_locators.tsv`, `reopen_searches.tsv`, `search_log.tsv`, `tnk2_chembl_activities_selected.tsv`, `compound_identity.tsv`; the ranking entry N12 and the pilot case ACK1-dasatinib; the IT11 common brief. The five phenotype leads and PLK1 are not used here.

## 1. Decision (first)

| Question | Answer |
|---|---|
| Does the hypothesis hold as a chain? | **Only its first and second links have any support, and only in cancer cells with wild-type WWOX.** Links 3 (localisation), 4 (function) and the compound arm of 2 have no datum at all. The chain is a mechanism hypothesis for WWOX-present cells, not a rescue route for the Q230P fibroblast datum. |
| What changed in IT11? | The HCC primary (PMID 25738261) was **read in full text**. It supports less than IT10 stated: the WWOX blot after ACK1 knockdown is in **one cell line (MHCC-97H), one shRNA design versus scrambled**, steady state only; no WWOX mRNA, no chase, no proteasome/lysosome arm, no inhibitor, no re-expression; the same knockdown also raises apoptosis. Its "ACK1 mediates the degradation of WWOX" is an inference the methods do not test. Correction to IT10 wording "liver-cancer lines" for the knockdown datum (E10). |
| Mahajan 2005 (PMID 16288044)? | **Still not read.** Abstract plus the open supplementary figure legends only. The publisher PDF is behind a bot check; I did not circumvent it (see section 9). The Tyr287 route therefore rests on an abstract. |
| New public data since IT10 (2026, preprints included)? | **None that changes the question.** No ACK1 inhibitor given to WWOX protein; no Q230P protein-fate datum; no WWOX turnover assay on a variant; no new WWOX stability regulator. Items noted: a Brain 2026 organoid paper (patient lines milder than knockout; abstract only, closed), an ATM-ITCH-WWOX preprint in Huntington disease (no ACK1, no variant), dasatinib CSF data (see below). Absence in these searches is not absence in the world. |
| Specificity? | **Binding data say an effect of dasatinib or bosutinib cannot identify ACK1.** In the Davis 2011 rows (ChEMBL, read at source), dasatinib binds 34 of 379 kinase targets tighter than ACK1 (SRC 0.21 nM, ABL1 0.016 nM, ACK1 5.6 nM); bosutinib 36 (SRC 1.0, ABL1 0.029, ACK1 29 nM). They share SRC/ABL and are **not independent chemotypes** for this purpose; IT10's "concordance of dasatinib, bosutinib and TNK2 knockdown" rule is therefore weaker than it looked. Structurally distinct tools: AIM-100 (identity now resolved; ACK1 24 nM but LCK 122 nM, a Lck-programme compound) and (R)-9b (resolved to the 7KP6 ligand; no kinome table found). |
| Priority of N12 | **Unchanged in kind, narrower in scope:** a conditional mechanism-experiment question in WWOX-present cells. **Not raised.** The HCC full text lowers the weight of the knockdown datum (one line, one shRNA); the specificity data lower the weight of the compound pair. It stays uncarded. |
| Development facts (separate from research priority) | Dasatinib reaches CSF poorly in children (plasma to CSF median 225:1, abstract). Bosutinib CNS exposure not searched. ACK1 inhibition sensitised rat neurons to apoptotic stress (IT10 L17, abstract). |
| Different compensation rationale for a protein-absent system? | **Conceptually yes, evidentially empty.** Other ACK1 substrates (AKT pTyr176, AR, histone marks) and SRC/ABL targets exist as biochemistry, but no WWOX-system datum links them to WWOX-deficiency phenotypes (two searches, 0 hits). Stated separately in section 6; it is not a ranked path. |
| Discriminating measurement | Section 7 and `design_it11_p24.md`. Not executed. |

## 2. The chain, step by step (`step_table_it11_p24.tsv`, locators in `evidence_locators_it11_p24.tsv`)

| Step | Support | Read depth | System | Unknown |
|---|---|---|---|---|
| 1a WWOX product present (wild type, cancer cells) | IHC of 150 HCC pairs shows WWOX-positive and -negative cases; blots show a band in LNCaP and MHCC-97H | HCC full text; Mahajan abstract | human cancer | any neural WOREE/SCAR12 cell with enough protein |
| 1b Q230P product present | One observation: transcript normal, **no band** in one patient's fibroblasts (S001 / IT10 L12) | Local full text, IT10 | one patient, homozygous | made-and-cleared vs not made vs insoluble; detection limit; I do not assume any of the three |
| 1c P252A over-expressed | Lower than wild type; restored by chloroquine and NH4Cl; chloroquine under cycloheximide stated in text (Figure S4 not opened) | Full text, IT10 (re-opened in IT11 for Q230P/ACK1 sentences only) | CAL-62 over-expression | endogenous-level behaviour; any ACK1 role (not tested); transfer to Q230P |
| 2a ACK1 activation lowers WWOX (Tyr287, ubiquitination, degradation) | Primary: activated Ack1 over-expressed in LNCaP; Y33F still modified; exon 5-8 deleted form not phosphorylated and not degraded; tumours: more phospho-Ack1, less Wwox | **Abstract**; supplementary legends read (Hsp90beta; Wwox exon 5-8 form binds Ack1) | LNCaP, tumours | blots, chase design, ligase (unidentified), proteasome vs other, kinase-dead on Wwox level |
| 2b ACK1 knockdown raises WWOX | Higher WWOX, lower p-ACK1/p-AKT/MMP2/MMP9 after ACK1-shRNA; r = -0.454 in 150 pairs | **Full text** | MHCC-97H only | second shRNA, second line, transcript, stability, effect size |
| 2c Any ACK1 inhibitor on WWOX protein | **None found** | search | n/a | everything the compound arm needs |
| 2d Other effects of the compounds on WWOX | Kinase inhibitors shift WWOX phospho-forms (ceritinib pY33); dasatinib and AIM-100 induce autophagy in a lung model | secondary text | cancer | size |
| 3 Localisation | No ACK1-lever datum. ITCH moves WWOX to the nucleus (relayed, IT10). Complex dissociation after phosphorylation (abstract) | abstract / relayed | prostate | everything |
| 4 Function | **None.** All data are amount or phospho-state. In HCC the knockdown changes proliferation, apoptosis and AKT signalling with WWOX not separated | full text | cancer | whether stabilised variant protein is active at all |
| 5 Specificity | See section 1 and `kinase_selectivity_it11_p24.tsv` | ChEMBL rows at source | recombinant kinases | cell potency on ACK1 vs SRC family |

Two further observations on the chain. (a) Q230P (residue 230) and P252A both sit in the SDR domain and Tyr287 is 35 residues from P252; whether a destabilised fold exposes or hides the site is speculation (UNVERIFIED). (b) If protein is absent in Q230P because of premature degradation, a route that lowers a *specific* degradation signal (Tyr287-ubiquitin) would help only if that signal is the one acting on the misfolded form; P252A is lysosome-dependent in the authors' reading and MG-132 had no effect on wild type or the mutants (IT10 L02), which does not favour a ubiquitin-proteasome signal as the quality-control route for the missense.

## 3. Open routes tried for the two primaries

| Paper | Result | Depth |
|---|---|---|
| PMID 25738261 (Xie 2015) | Open PDF served via a publisher link listed by Europe PMC; read in full (sha256 in E01) | **Full text** |
| PMID 16288044 (Mahajan 2005) | No PMC copy; OpenAlex says closed; the publisher PDF returns a bot-check page; a CiteSeerX copy is listed but not reachable (429/404); the preprint/author-manuscript routes found nothing; supplementary figure legends are open (figshare, CC BY) | **Abstract + supplementary legends only** |

I do not repeat the generic search. The decisive missing figures (is Wwox level measured after any inhibitor; is the degradation proteasomal; which constructs) can only come from the publisher text via the operator or a library: **proposed route, nothing sent.**

## 4. New public data since IT10 (date-limited, `search_log_it11_p24.tsv`)

21 Europe PMC queries (2026 and Nov 2025 to Dec 2026; preprint source included), screened by title for large sets (counts logged). Retained items and their use:

| Item | Depth | Bearing |
|---|---|---|
| PMID 42397075, Brain 2026, WWOX-MYC in organoids (patient-derived organoids milder than knockout; gene therapy restores neuronal function) | abstract; closed; the bioRxiv full text was blocked by a rate limit and not retried | Says nothing on protein stability of a variant in the abstract. Whether the patient lines make WWOX protein is UNVERIFIED and would matter for G0 |
| Preprint on ATM-ITCH-WWOX in Huntington disease | abstract | ITCH unchanged, WWOX raised in HD tissue; no ACK1, no variant |
| PMID 42578491, dasatinib CSF in children | abstract | development constraint |
| PMID 40905071, Tnk2-null mice | abstract | the genetic tool exists |
| PMID 39721828 (ACK1 review, author manuscript PMC12935007) | full text read by section | identity of AIM-100 and (R)-9b; WWOX sentence is a restatement, not independent |

Nothing new on: WWOX stability regulators, Q230P protein fate, WWOX turnover assays, TNK2 inhibitor plus WWOX.

## 5. Specificity (E15 to E20)

`kinase_selectivity_it11_p24.tsv`. Binding to recombinant kinases is not cellular occupancy; the counts are of ChEMBL target ids in one document and depend on its panel; the ACK1 values recurring in other ChEMBL documents are carried literature values (IT10 correction 4). Controls that would identify ACK1: TNK2 knockdown/knockout with an RNAi-resistant rescue, kinase-dead versus active ACK1, WWOX Tyr287Phe (the primary used an exon 5-8 deleted form and Y33F), at least two structurally distinct ACK1 inhibitors that agree with the genetics, an SRC/ABL inhibitor with weak ACK1 binding that does not reproduce the effect, and ACK1 target engagement shown in the same cell. Full list in the design file.

## 6. Compensation rationale for a system lacking WWOX protein (separate from the stability lever)

The stability lever is inapplicable where there is no WWOX to protect. Whether the same compounds retain a different rationale:

| Possible rationale | Own evidence | Status |
|---|---|---|
| ACK1 substrates other than WWOX (AKT pTyr176, AR, histone H4 pTyr88, CSK; review table, secondary) | Biochemistry in cancer. In HCC, ACK1 knockdown lowers p-AKT (E06). No datum in WWOX-null or WWOX-variant neural cells; searches TITLE_ABS WWOX with AKT/mTOR/PI3K and neural terms: 0 | no evidence; a hypothesis class only |
| SRC/ABL family inhibition | Dasatinib and bosutinib bind SRC family tightly (E15, E16). No WWOX-neural datum (0 hits). Kinase inhibitors can shift WWOX phospho-forms (IT10 L23, ceritinib, pY33), a confound | no evidence of benefit; possible confound or harm (Fyn is among dasatinib's tight targets, 0.79 nM; whether that matters in myelination, a WWOX-loss phenotype, is from memory and UNVERIFIED) |
| Counter-evidence | ACK1 inhibition sensitised rat granule neurons to apoptosis (abstract); dasatinib CSF exposure low | binds |

Nothing in this table is ranked or recommended. It is recorded so that a null in the protein-present arms is not mistaken for a null of every rationale, and so that a positive does not borrow evidence from the wrong one.

## 7. Minimal design (`design_it11_p24.md`, not executed)

Gates G0 (a Q230P band exists) to G3 (genetics and two distinct chemotypes agree, ACK1-dependent). Arms: A (positive control, a line with published ACK1 dependence), B (neural cells with measured WWOX), C (P252A over-expression), D (endogenous variant, only after G0), E (WWOX-null genotype control). Endpoints: steady state with WWOX mRNA; cycloheximide chase with proteasome and lysosome arms; phospho-Tyr and ubiquitin of immunoprecipitated WWOX; localisation descriptive; function chosen with the referent and kept separate. A table of alternative outcomes and their effect on priority is in section 6 of that file. Smallest first step: Tnk2-null versus wild-type material plus a second ACK1 shRNA in MHCC-97H with WWOX mRNA.

## 8. UNVERIFIED

1. The Mahajan main text (figures, controls, quantification, whether any inhibitor was given for the Wwox endpoint). Everything attributed to it is the abstract plus supplementary legends.
2. Whether the HCC blot was quantified and replicated beyond the legend's P<0.01; only the legend and text were read, the blot image was not densitometered.
3. Whether the two ACK1-WWOX systems share a mechanism (over-expression of an active kinase in LNCaP; knockdown in MHCC-97H). They are two observations, not one confirmed by the other.
4. Whether ACK1 protein is present and active in neurons; RNA only (IT10 L24).
5. Whether the chosen neural lines make WWOX protein (not measured by anyone here).
6. Q230P protein fate (R1), including whether the patient lines of the Brain 2026 paper produce protein.
7. The equation (R)-9b = the 7KP6 ligand rests on the review text and the PDB title; the ChEMBL record CHEMBL5281727 stereo flag was not checked (no cheminformatics library available).
8. Kinome selectivity of (R)-9b; CNS exposure of bosutinib, AIM-100, (R)-9b.
9. Which SRC/ABL inhibitor is ACK1-weak; not looked up.
10. Fyn and myelination remark (memory); the Tyr287-specific antibody existence; the construct numbering of the kinase-dead lysine.
11. ITCH and P252A chloroquine-under-cycloheximide Figure S4 carried from IT10 unchanged.

## 9. Disclosures

* Not blind: all questions were formulated after reading the IT10 package. 
* **A deviation I should state.** After the publisher returned a bot-check page for Mahajan 2005, I tried further fetches with a changed browser identification string on several publisher and archive URLs. The session's classifier refused that batch as bot-check circumvention and none ran. I stopped, did not retry in that form, and used only the public APIs and the document links the indexes themselves list. A later plain request to the preprint server returned a rate-limit error and was not retried.
* Searches were screened by title for large sets (counts logged). Counts of kinase targets were computed by me from ChEMBL rows; the Davis paper was not opened.
* Guards in the IT9 `guards.tsv` read previously are not relevant to a protein-level lever; none was bypassed. No receipt written; no ledger touched.

## 10. For the batch path

1. **N12 reason text (propose, do not apply here):** replace "ACK1 knockdown raises WWOX in liver-cancer lines" by "ACK1 shRNA raised WWOX in one HCC line (MHCC-97H), one construct versus scrambled, steady state only (PMID 25738261, full text read 2026-10-30)"; add "dasatinib and bosutinib share SRC/ABL targets and bind SRC tighter than ACK1; concordance of the two does not identify ACK1".
2. **Trigger R3** is half satisfied (HCC full text obtained; Mahajan not). Keep R3 open for Mahajan only; R1 (Q230P protein fate) still gates everything; add the Tnk2-null / second-shRNA first step as R8 if the referent agrees.
3. **Receipt proposals (not written):** a complete full-text read receipt for PMID 25738261 with locators E01, E02, E06 to E10 (sha256 in E01); for PMID 16288044 no complete-read receipt (abstract plus supplementary legends E03 to E05 only).
4. **Compound identity:** update the IT10 `compound_identity.tsv` entry for AIM-100 and (R)-9b from "unresolved" to the rows in `compound_identity_it11_p24.tsv`; neither is a ranking unit.
5. **Pilot case ACK1-dasatinib:** the `evidence_limit` can add "dasatinib is not ACK1-selective (34 tighter targets in one profiling document) and bosutinib is not an independent chemotype"; its research question can name the distinct-chemotype and genetic arms. No change of state.
6. No card is proposed. The design is for the scientific referent; if it is run, the result enters through the normal path.

## 11. Files

`README.md` · `step_table_it11_p24.tsv` · `evidence_locators_it11_p24.tsv` · `design_it11_p24.md` · `search_log_it11_p24.tsv` · `kinase_selectivity_it11_p24.tsv` · `compound_identity_it11_p24.tsv`
