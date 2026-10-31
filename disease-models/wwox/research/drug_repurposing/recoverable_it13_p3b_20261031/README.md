# IT13 P3-alt (scientist, p3b): which functional readouts does restoring WWOX demonstrably recover, and does anything other than WWOX move one of them?

Package `recoverable_it13_p3b_20261031`, branch `task/it13-p3b` (from `dbc8e7c3`), 2026-10-31. Public edition, WWOX-DEE genotype class, no individual-level record. Exploratory, non-canonical, not medical advice. A readout that WWOX add-back changes does not imply that a compound moving it restores WWOX functions. No e-mail, personal datum or registration was sent to any service; no spend; no access control bypassed (EBI 403 left as is). Nothing here edits a card, need, ranking, registry, current file, view or the ledger.

## 1. Decision (first)

1. **Recoverable readouts (demonstrated with a vector or comparator arm).** Two are demonstrated post-onset in human neurons, one contrast, one laboratory (RC1, PMID 42397075, week-10 neuron-promoter AAV9-WWOX, read at week 16): **Ca2+ firing** (event rate, amplitude, % active ROIs; WOREE and SCAR12) and the **CTIP2/SATB2 fraction of nuclei** (WOREE only; SCAR12 never lost them). Mouse: survival, weight, glycaemia, spike-wave discharges, behaviour, fertility, myelination, gliosis (RC2, PMID 42422765), but only as **prevention** (P0-P5; the null dies by about P15, so no late arm exists). Radial-glia readouts (MYC-high state, DNA damage, apoptosis, astrocytosis) are recovered only by **stem-cell-stage** genetic add-back (RC3, PMID 34268881, n=4 organoids, one batch), never by neuron-stage add-back (no radial-glia DEGs). What add-back leaves un-recovered or untested is in `recoverable_readouts_it13_p3b.tsv`.
2. **Does anything other than WWOX move a recoverable readout in a WWOX-deficient system? Yes at the level of "a readout of the same class", no at the level "the same measure in the same human system".** d-APV abolishes bursting in the neuron-KO mouse slice (acute, reversible, no wild-type burst control); ethosuximide lowers a provoked-seizure score in null pups only (genotype-specific; spontaneous SWD never tested); digoxin raises blood glucose in null mice within 40 min (n=3, printed dose ambiguous); shHIF1a lowers glucose uptake in the same null MEFs where WT add-back (not the WW1-dead mutant) does (the one matched recovery/bypass pair in the repository, non-neural). **No intervention of any kind has a firing readout in a human WWOX-deficient neural system**; A51, the only compound arm there, did not move CTIP2/SATB2. Lithium moves its readout in wild type too (not a bypass). BB-FCF went the wrong way.
3. **Chosen readout-question: neuronal hyperexcitability (firing) as the recoverable readout, with CTIP2/SATB2 as its dissociable paired readout.** Reason: it is the only post-onset human recovery with a vector control and the disease-defining phenotype. Within-paper dissociation: SCAR12 organoids fire abnormally (event rate ~0.075 Hz vs WT ~0, read by eye) with layer markers at WT, so firing excess does not need the layer-marker deficit and the deficit does not cause it (one allele, small n).
4. **The graph cannot be seeded by this recovery contrast at gene level.** Gene-level add-back data are locked (E-MTAB-14792: HTTP 403 again today); Fig 6D/E give pathway enrichments only. A recovery-defined engine_v4 run is possible only on two function-linked genes (section 5): the 1-seed set returns a tautological GAD inhibitor (mechanistically against the aim), the 2-seed layer-identity set returns weak BMP-ligand families with a title-level counter-datum. Neither is advanced. The informative tool here is the phenotype-first entry, not the graph.
5. **Abstentions with reopening conditions.** (a) No candidate advanced for firing in humans. (b) Reopen when: a compound arm with Ca2+/MEA readout is published in a WWOX organoid; or E-MTAB-14792 becomes public (gene-level seeds for the add-back direction); or a WT + AAV9-WWOX / dead-mutant arm is reported (decides whether RC1 is recovery or gain).
6. **Discriminating experiment (section 7):** one organoid design that puts WWOX add-back, a dead-WWOX control, a WT + WWOX control and two independent silencers (TTX, D-AP5) in the same week-10-to-16 protocol, reading firing and CTIP2/SATB2 together, plus a washout arm.

## 2. Inventory and usability (steps 1-2)

Files: `recovery_contrasts_it13_p3b.tsv` (7 contrasts, 12 usability columns), `recoverable_readouts_it13_p3b.tsv` (6 readouts: compartment/stage, magnitude as read, recovery class, what is not shown, what is not recovered, dissociation).

| Contrast | Verdict |
|---|---|
| RC1 organoid wk10 neuron AAV9 add-back (42397075) | USABLE at phenotype level. Limits read at source: n=3-8 organoids per arm (ROIs n=20-40 appear as the test unit for event rate), "No randomization or blinding was applied", no WT+vector, WT+WWOX or dead-mutant arm, add-back level vs WT unknown (WPRE), untreated WT neurons show no detectable WWOX, partial transduction, ROI% and amplitude stay above WT (by eye), scRNA locked. |
| RC2 mouse AAV9-hSynI (42422765) | USABLE for organism outcomes, prevention window only; vector control vehicle; high dose supra-WT; SWD n=5 pups. |
| RC3 hESC AAVS1 add-back and wk6 lentivirus (34268881) | USABLE for radial-glia-inclusive recovery; n=4 organoids, one batch; GAD67 overshoots below WT; Wnt readouts partly move away from WT. |
| RC4 MEF WT/WFPA/shHIF1a (25012504) | USABLE, non-neural; relayed from the repository (not reread). |
| RC5 zebrafish, RC6 fly, RC7 cancer over-expression | not usable for a human neural readout (construct unresolved; not DEE; not a deficiency model). |

New recovery contrasts since IT7: none found (Europe PMC, 32 title-screened hits, section log S3). Not shown absent.

## 3. Bypass on recoverable readouts (phenotype-first)

`bypass_on_recoverable_readouts_it13_p3b.tsv` (11 rows) pairs each non-WWOX intervention with the recoverable readout it matches and states whether the system, the measure and a WWOX-specificity control match. Two things the IT11 list lacks: digoxin is not a phenotype-first unit (absent from `member_evidence.tsv`) although it moves a readout that add-back recovers; and no row has the same measure in the same human system.

## 4. What the recovery means for a compound (the inference guard)

* Add-back is WWOX supply; its effect on firing does not say which WWOX function (WW-domain scaffolding, SDR activity, a transcriptional role) matters. No dead-mutant arm exists in RC1/RC2.
* A compound lowering firing is symptomatic unless it also moves the readouts that dissociate from firing (CTIP2/SATB2, ion-channel programme) and persists after washout, as add-back does.
* Marker recovery is not functional recovery: GAD67 area after add-back falls below WT (~0.1 vs 0.2, seed S126) and SATB2 overshoots WT; "toward WT" is not "to WT".

## 5. engine_v4 runs (step 3), `engine_runs/`

Seeds are recovery-defined: genes whose alteration is stated to be reversed by add-back, roles unknown (no source states a role). Command in `engine_runs/RUN.txt`.

| Run | Seeds | Result | Reading |
|---|---|---|---|
| RA | GAD1 protein up (organoid KO, add-back lowers it below WT; PMID 34268881) | 1 row: S-allylglycine (GAD inhibitor), a direct hit, Z 105,597 (null-floor artefact) | Tautology; and lowering GAD activity lowers GABA synthesis, against an anti-hyperexcitability aim. Shows direction of change is not role. Discard. |
| RB | BCL11B down, SATB2 down (WOREE; add-back raises; PMID 42397075) | 127 of 12,560 examined families reach the seeds (no direct hits); top: eptotermin alfa (BMP-7) Z 4.9, dibotermin alfa (BMP-2) Z 4.4, main target BMPR1A; next Z 2.2 on one-target families; multi-kinase inhibitors (hesperadin, dovitinib, nintedanib...) fall on the `mimics` arm (|Z| <0.2) | 2 seeds, 500 null draws, tiny null spread: scores are not evidence. BMP families keep a counter-datum (WWOX loss raises TGFb/BMP2 signalling in a pancreatic cancer line, 36572673, title level). Not advanced. The `mimics` placement of the multi-kinase class is consistent in sign with A51 not raising the markers; it validates nothing. |

IT11 P2.1 already showed that the graph cannot score ethosuximide (sink targets), vigabatrin (not nodes) or A51 (no identity); nothing new here.

## 6. Candidacies compared (step 4), `candidacies_it13_p3b.tsv`

C1 d-APV/NMDAR (known) - probe arm; C2 ethosuximide on spontaneous SWD (known) - same-readout mouse test; C3 chronic silencing with TTX and D-AP5 (mechanism-distinguishing) - adopt as arm; C4 BMP ligands (new, engine) - do not advance; C5 over-expression counter-hypothesis - control; C6 symptomatic-anticonvulsant counter-hypothesis - the null every bypass must beat. Each row states identity, active moiety, action, context, counter-evidence, decisive missing datum, ex vivo utility and, separately, systemic requirements (none of C1-C4 is a development claim).

## 7. Discriminating experiment (step 5)

System: WOREE and SCAR12 organoids plus WT, one protocol (infection week 10, read week 16, Ca2+ imaging as in RC1), organoids as the unit, at least 2 independent differentiations, scorer blind to arm, ROIs not the unit.

| Arm | Purpose |
|---|---|
| WOREE + AAV9-EGFP; + AAV9-WWOX | reproduce RC1 with the unit and blinding RC1 lacked |
| WOREE + AAV9-WWOX WW1-dead (W44F/P47A) and an SDR-region mutant (L404A-type) | which WWOX function carries the firing and marker effects |
| WT + AAV9-WWOX and WT + AAV9-EGFP | over-expression/vector effect (C5) |
| WOREE + TTX; + D-AP5; + vehicle, same weeks | silencer bypass; are CTIP2/SATB2 and the ion-channel qPCR panel activity-dependent? (C3, C6) |
| 2-week washout of every arm | add-back persistence vs reversibility of silencing |
| SCAR12 repeated | the dissociation (firing high, markers WT) as an internal control |

Readouts: Ca2+ event rate, amplitude, % active ROIs; CTIP2/SATB2 by IF and qPCR; SCN/KCN/GRIN panel by qPCR; radial-glia markers as an untouched-compartment check. Prediction fixed beforehand (from SCAR12, which may be wrong): silencing lowers firing, does not raise CTIP2/SATB2, does not persist after washout; add-back WWOX does all three. Falsified if silencing raises the markers (activity-dependent, a bypass of the marker readout exists) or if WT + WWOX also lowers firing (C5). A compound earns the word "bypass" only if it moves firing AND persists AND matches the add-back profile on the paired readout; firing alone is symptomatic.

## 8. Edits this implies (for the Orchestrator; I changed none)

1. Add RC1-RC4 as recovery rows to the question table with the usability columns, and mark CTIP2/SATB2 and firing as two readouts, not one "rescue".
2. Phenotype-first list: add digoxin (null-mouse blood glucose) as a unit with its caveats; mark the d-APV, ethosuximide and lithium rows with "different measure from the recovery contrast".
3. M01/F04/K01 next-measurement text: add the dead-mutant and WT+WWOX arms and the "blind, organoid as unit" requirement from section 7.
4. Seeds: the add-back rows S013-S015, S092, S093, S103, S126 stay reserved; this package confirms they cannot become engine seeds except S126 (RA).
5. If the operator asks for E-MTAB-14792: a release request (not sent, per earlier drafts) is the only route to gene-level add-back seeds.

## 9. Read depth and disclosures

Not blind: I read the IT6 census and function reference, IT10 P2.3, IT11 P2.1/P2.2, IT12 P1a/P1b before choosing. **Read by me at source this session:** 42397075 text layer (Fig 6 results, legend, Methods statement on randomisation) and Fig 6 image; 42422765 XML (abstract, results on dose, behaviour, SWD); 34268881 XML (AAVS1, lentivirus, W-AAV sentences). **Relayed from repository files, not reread:** 25012504 (RC4), 34634460 and 32000863 (d-APV, ethosuximide, lithium), 25649963, 42909904, digoxin dose and glucose values. **Title level only:** 36572673. Values taken from bar charts are read by eye and marked so. IT11/IT12 files were read for results, not re-audited. Receipts not written.

## 10. What a verifier needs

The single decisive link: whether RC1's firing recovery is **WWOX-specific**. It needs a WT + AAV9-WWOX arm and a dead-mutant arm, neither of which exists in the repository or in the paper text read. Second: the add-back scRNA (E-MTAB-14792, 403). Third: the Fig 6A(ii) values, read by eye here, should be re-measured from source data; Supplementary Fig 9-10 were not reachable.

## 11. Files

`README.md`, `recovery_contrasts_it13_p3b.tsv`, `recoverable_readouts_it13_p3b.tsv`, `bypass_on_recoverable_readouts_it13_p3b.tsv`, `candidacies_it13_p3b.tsv`, `search_log_it13_p3b.tsv`, `engine_runs/` (two seed files, proposals/contributions/funnel outputs, `RUN.txt`).
