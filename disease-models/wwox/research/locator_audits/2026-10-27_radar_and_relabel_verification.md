# Radar discovery decisions and F01/F02 scope relabel: independent verification (2026-10-27)

Verifier: independent (did not produce either piece of work). Public key-less routes only; no e-mail or contact. Status vocabulary: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE_SURFACE. This is a surface check (records, licences, probes, labels), not a full-text reading.

## A. Radar (merge 31205c90, commit bd44a7b1)

| Item | Check | Verdict |
|---|---|---|
| PMC12754399 identity | Europe PMC core: PMID 41380592, PMCID PMC12754399, 2026, "Activation of the ISR contributes to developmental delay and seizures caused by mitochondrial prolyl-tRNA synthetase (PARS2) deficiency". Abstract: dPARS2 knockout/knockdown in Drosophila causes seizure; genetic suppression of GCN2 and of ATF4 prevents developmental delay and seizure; V95I variant activates ISR in human cells. | SUPPORTED |
| PMC12754399 licence | Europe PMC field `cc by-nc`; article XML: "open access article under the CC BY-NC license". Field and article agree. | SUPPORTED |
| PMC12754399 decision (READ candidate) | Reasonable: it is a genetic (not pharmacological) invertebrate precedent for the ISR-in-seizure gap (Q-R-10 rests on one reading); the log already states it is not WWOX. Note: CC BY-NC permits reading and quoting for research; any redistribution of text needs the NC limit respected. Minor under-statement: the paper also has a human-cell variant arm (V95I), which the log omits. | SUPPORTED (small UNDERSHOOT: human-cell arm unmentioned) |
| PMC13537045 identity and licence | PMID 42689174, 2026, "Hyperpolarized 13C-bicarbonate production correlates with excitatory neuron distribution in the human brain"; 40 healthy individuals, bicarbonate-to-pyruvate ratio read as PDH flux. Europe PMC `cc by`; article text states CC BY 4.0. | SUPPORTED |
| PMC13537045 decision (WATCH) | Reasonable: healthy adults, imaging, no patient/WWOX/cell-assay content. "PDH flux" is the authors' reading of a ratio. | SUPPORTED |
| Ineichen-Group/ClinicalTrials_DrugDisease_Pipeline code | GitHub API `license: null`; repo root has no LICENSE file (listing: scripts, notebooks, README, core, data). Pushed 2026-04-08, 0 stars. | SUPPORTED |
| Ineichen Zenodo 19351891 | Record "A2H_Clinical_Data", licence `cc-by-4.0`, 2026-03-31, one 122.6 MB file (clinical.zip); the README links to it as the pipeline's processed output. Description: raw AACT snapshot (1 Dec 2025) plus linked drug/disease entities (disease to MONDO, drug to UMLS CUIs). | SUPPORTED |
| Ineichen decision (REJECT code, WATCH data) | Reasonable: no licence means no reuse right; data are CC-BY. Small correction: the log says the output is "trial-level drug-disease pairs"; the record describes trial metadata plus NER-linked entities (drug and disease from trial text), consistent but I did not open the zip (UNVERIFIABLE_SURFACE for pair-level content). Caveat to keep: the Zenodo record is by a different creator (ORCID listed) than the repository, and the code is unlicensed while the data are licensed: derived-data rights follow the Zenodo statement only. | SUPPORTED, content of zip UNVERIFIABLE_SURFACE |

### Gap themes in `scout_daily.py` (7)
Mapping to concrete WWOX gaps in module_blindspots_20261023.md, README "Next step" column and the 2026-10-27 handoff:
- isr-atf4-epilepsy: Q-R-10 (one reading only; handoff REPLICATE). SUPPORTED.
- residual-function-chaperone: Q-N-11, Q-N-12, Q-R-09 (handoff READ rows). SUPPORTED.
- assertion-extraction: blind spots F3 (typed assertions not reproducible by rule) and F6 (free-text ChEMBL match). SUPPORTED.
- pdh-assay: README Phase 2 "PDH activity unchanged" traced to one non-significant figure. SUPPORTED.
- dee-drug-response-data: README P7 "no gold set exists". SUPPORTED.
- neuron-perturbation-signatures: stated in gse156243/lincs_iteration2_interpretation_20261027.md (context-matched strata), not in the three named sources. SUPPORTED (source differs from the one named).
- sdr-enzyme-assay: I did not find "no activity assay or substrate" as a recorded gap in the drug-repurposing files searched (README, tool survey); it may sit in the working model or elsewhere. UNVERIFIABLE_SURFACE. Also the Europe PMC query ends with `AND TITLE_ABS:(WWOX OR SDR)`, so "SDR" alone matches any short-chain dehydrogenase paper; harmless but broad.
- Dry-run (`--discover-only --theme pdh-assay --dry-run`, `--theme sdr-enzyme-assay --dry-run`): both returned 0 new items, 0 errors, nothing written (items already seen). `--status`: RADAR OK, last run 2026-10-27T05:20Z, 0 probe errors, to examine: SigCom-LINCS. The crontab was not touched.

### New probes observe the relevant resource
- EveryCure-MATRIX-scores (HF dataset `everycure/matrix-scores`): the API returns cardData without a `license`, no license tag, no LICENSE file in the tree (data/, README.md, .gitattributes). The probe reads exactly the missing statement. SUPPORTED.
- EveryCure-MATRIX-code (`everycure-org/matrix`): API licence Apache-2.0, pushed 2026-10-27, default branch main; code and data licences are separate, as the probe text says. SUPPORTED.
- TxGNN-code (`mims-harvard/TxGNN`): releases list empty, latest commit 2024-05-06; latest-commit fingerprint is the right signal. SUPPORTED.
- TxGNN-explorer (txgnn.org): unreachable from here (curl HTTP 000); the availability-only probe matches the stated reopening condition. SUPPORTED.
- SigCom-LINCS: metadata-api `libraries/count` returns `{"count":431}`, matching the "libraries count" fingerprint. SUPPORTED.

## B. Scope relabel by scientist-a (commit 67159566)

Definition added to `framework/scripts/repurposing_bridge.py`: EXPERIMENT_IN_DEE_SYSTEM = "measured in a WWOX-deficient system that models the disease (patient case, patient-derived or engineered knockout cells, organoids, animals)"; OTHER_CONTEXT = "WWOX outside such a model (e.g. a fly amyloid model)".

Rows actually relabelled (OTHER_CONTEXT to EXPERIMENT_IN_DEE_SYSTEM): F01 DA-W2-001, DA-W2-002, DA-W2-003; F02 DA-W2-010, DA-W2-011. (DR-W2-001 and DR-W2-007 were already EXPERIMENT_IN_DEE_SYSTEM before the commit.) No organoid row was relabelled: DA-W2-004 and DA-W2-012 (KO organoid transcripts, GSE156243) stay COMPUTATIONAL_RESULT, and F03 and the E-series OTHER_CONTEXT rows (fly RNAi, e.g. DA-LC-ATF4-001/002) are untouched.

| Row | System | Verdict | Note |
|---|---|---|---|
| DA-W2-001 burst fraction (Breton 2021, Synapsin-Cre Wwox neuron-specific KO slices) | engineered-null mouse that reproduces the epileptiform phenotype | SUPPORTED | Fits "engineered knockout ... animals" in the definition. The label states the system, not human relevance. |
| DA-W2-002 mEPSC amplitude | same | SUPPORTED | Producer's AMPAR-weighting is flagged INFERENZA in the row; the label does not change that. |
| DA-W2-003 delayed evoked response | same | SUPPORTED for the label; supplementary figure (S3) attested from the manifest, the PMC supplement was not served: UNVERIFIABLE_SURFACE for the number itself | Not a label problem. |
| DA-W2-010 MBP reduced in Wwox-/- mouse (Obeid 2026) | full-null mouse, the standard model of the disease | SUPPORTED | Hypomyelination endpoint in a null animal; fits. |
| DA-W2-011 MBP after neonatal AAV9-hSynI-WWOX | same null model, treated | SUPPORTED for the scope; the rescue claim is qualitative only (as the row says) | Label describes the system, not the strength of rescue. |
| DA-W2-004 / DA-W2-012 organoid transcripts (not relabelled) | engineered KO organoid, third-party deposit re-analysed | consistent as COMPUTATIONAL_RESULT | Could also qualify as EXPERIMENT_IN_DEE_SYSTEM by the definition ("organoids"); keeping the COMPUTATIONAL label is defensible because the producer's panel is a re-analysis, but the definition and the practice differ. |

Overall: the relabel is SUPPORTED. Neuron-specific and full-null mouse results model the disease as the definition says; keeping them in "other context" would have understated the nearest-system evidence.

Corrections needed (all small):
1. Definition wording: the label mixes human patient and animal/organoid systems. Add that it never implies human or clinical applicability (species stays in `context`), so a reader of the handoff cannot count a mouse slice as patient evidence. Suggested clause: "...; the scope says what kind of system, never that the result transfers to patients."
2. The definition's OTHER_CONTEXT example "a fly amyloid model" is the only example; add the fly neuronal Wwox RNAi rows (DA-LC-ATF4-001/002) which are non-mammalian WWOX-deficient systems, so the boundary for invertebrate knockdown is explicit (currently ambiguous, since an RNAi fly "models" WWOX loss).
3. Organoid practice: either relabel DA-W2-004/012 or state in the definition that scope is by kind of evidence first (a re-analysed deposit is COMPUTATIONAL_RESULT regardless of system). README item 6 of the open questions (line 195) still asks to "confirm" this vocabulary; mark it resolved once 1-3 are applied.
4. Receipt hygiene: a relabel changes `input_sha256` of F01/F02 cards; the commit regenerated join outputs, so no further action, but the change is a scope decision recorded only in a commit message and README, not in the cards' own history.

Not verified: zip contents of the Ineichen Zenodo record; full text of either radar paper beyond abstract and licence statement; source figures behind the F01/F02 rows (not re-read; only labels judged).
