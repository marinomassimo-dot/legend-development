> **Correction note, IT13 follow-up (2026-10-31 evening).** The nucleus-level deposit GSE158684 became readable and was analysed (`../snrna_it13b_pv_20261031/`). It does not support 'PV-selective deficit' as a cell-level statement: read this finding as 'lower Pvalb transcript (about 0.59 of the control UMI share in the snRNA pool against log2 -1.7 in bulk), not localisable to fewer PV cells versus less Pvalb per cell at one pooled library per genotype; the larger shift in the same animals is oligodendrocyte-lineage composition (Mbp UMI share ratio 0.30)'. Body below untouched.

# IT13 P3a: the excitation/inhibition axis (Q4) without any variant WWOX protein

Scientist, task `ORCH-ROADMAP-IT13-20261031`, package P3a, branch `task/it13-p3a` (from main `dbc8e7c3`), 2026-10-31. Exploratory, non-canonical, **not medical advice**.
Reference genotype: a WWOX-DEE genotype class; no individual-level record. No contact address, account or personal datum was sent to any service (Europe PMC, ChEMBL REST and GEO, key-less; no `mailto`).
Nothing here edits a card, a need, the ranking, a registry, the four current files, the view or the receipt ledger; the edits this implies are in section 8.

## 0. Decision (first)

1. **Q4 as posed (which lever relieves the bursting/seizure phenotype) is not answerable from any datum that exists in public form.** Every functional endpoint (slice bursts, d-APV, sIPSC, ethosuximide and lithium in the PTZ pup, ECoG spike-wave, organoid firing) is a figure in one laboratory's paper with no deposited numbers (Repudi 2021: "no data deposited"; Obeid 2026: "not relevant"; Cheng 2020: raster PNG; organoid scRNA E-MTAB-14792 returns 403). Reopening condition: numeric slice/PTZ source data from the authors' public supplement, or a new measurement (section 6).
2. **One narrower question was answerable on data without any variant protein, and I answered it:** what E/I state does the deposited P17 mouse deletion transcriptome carry (GSE158681 hippocampus, GSE158682 cortex; deletions 85 to 94 percent in hippocampus), and do the Q4 engine seeds survive it? Panels were declared before values were opened (`PRE_ANALYSIS.md`, committed first). It is a **state** question at transcript level: it informs which lever class deserves a probe; it does not show a rescue.
3. **Result.** (a) *Pvalb* mRNA is lower in all four within-line deletion contrasts (log2 -1.70 hippocampus S, -0.86 N, -1.16 null, -0.59 cortex S; control-versus-control |log2| at most 0.18), animal-separated in three; *Gad1* mildly lower (-0.54, +0.05, -0.35, -0.41); the pan-interneuron panel (Gad2, Slc32a1, Dlx1/2/5, Lhx6) is flat (-0.0 to +0.2). So: a PV-selective transcript deficit without a pan-interneuron one. It cannot separate fewer PV cells from less Pvalb per cell (maturation, activity): the cell-resolved deposit GSE158684 could, and its files were not deliverable today. (b) *Npy* mRNA is **higher** in all four contrasts (log2 +2.5, +0.7, +0.7, +1.0; animal-separated in all four, but the N and null effects sit within the 0.73 background seen between control lines), against the organoid seed S116 (NPY down) and against the immunostaining counts (S066, NPY-positive cells down). Three observations, three levels, three directions: the sign of "NPY" is not transferable across systems or levels. (c) The activity-regulated set (Fos, Npas4, Arc, Egr1...) changes sign between contrasts (+0.73 hippocampus S, carried by one of three animals; -0.44, -0.68, -1.1 elsewhere): no hyperactivity-at-sampling reading. (d) NKCC1:KCC2 transcript ratio is not raised (Slc12a2 falls more than Slc12a5 in 3 of 4 contrasts), which gives no transcript support to the depolarising-GABA premise of card F03; E_GABA stays unmeasured. (e) Composition shifts are large in the same animals (myelin set -0.8 to -1.8, astrocyte set +0.3 to +0.9), larger than the PV change.
4. **Engine v4 does not fit this question** (section 5): fed with these seeds it returns proteasome/HDAC inhibitors by transcription chains (GAD1/NPY), and no ion-channel antiseizure agent is reachable. Phenotype-first entry is the route; four candidacies were qualified (section 4). **No candidate is strengthened; one new probe (Kv7 opener) is proposed for an ex vivo test only.**
5. **If a different question had to be taken:** Q3 (ISR) is not taken (IT6 P4 already ran this very deposit: flat, sign unresolved; no protein or phospho datum is public); metabolism (Q2) is not taken (P47T and HIF packages of IT10 to IT12 are done; the only public flux/metabolite candidate, MTBLS12344, is not public). Both fail the usability check at "endpoint"; the check is in section 7.

## 1. What I read first (not blind)

| Read | Depth |
|---|---|
| CLAUDE.md router, state manifest (`current_state: READY`), brief; LEGEND_CORE 21c/21d/21e via the router | named sections |
| `generation_it9_p1_20261030/questions.tsv` Q4 row in full; Q4 rows of `seeds.tsv` (S058-S076, S114-S131) | full |
| `generation_it10_p1_20261031/README.md` (head), `question_roles.tsv`, `results/phenotype_first.tsv`, `results/dispositions_Q4.tsv` (counts, first 40 rows) | read |
| Cards F01, F03, F04, H01 (`p4_fields`, assertions' heads), `cards_early/EB-ETX-01` `p4_fields`; P11 not opened (listed in questions.tsv) | partial |
| Needs `NEED-T-TYPE-CALCIUM` and the titles of the other Q4 needs; `ranking_it8_p9` units U16-U27 (cut columns), `unit_caveats.tsv` U17/U25 | read |
| `nmdar_pharmacology_it6_p9` README sections 1-2 | read |
| `figure_audit_it12_p22` README (the GIRK2 Fig 7B correction) | read |
| `wwox_data_census_it6` sections 0-1 (dataset table) | read |
| `mouse_wwox_p17_it6_p4` README sections 1-2, `set_summary.tsv` rows for `Neuro_*`, `Mk_*` | read |
| `p47t_it12` README section 0-2 | read |
| Cheng 2020 Fig 7 (PNG, **viewed**), its Results sentences on ethosuximide/lithium; Breton 2021 and Obeid 2026 data-availability statements (searched) | viewed / searched |
| Colombo 2023 (GIRK2) | **not re-read**; I rely on the IT12 audit text |

Known before looking: the IT6 P4 result that the ISR/progenitor/neuron sets sit inside their null in this deposit, and that the interneuron axis was one gene (DLX2). I had **not** seen any value for the panel genes.

## 2. Q4 inventory and usability check (brief P3.1, P3.3)

Full table: `datasets_q4.tsv`. Summary of the check (model identity, effective perturbation, contrast, units, tissue/stage, confounders, endpoint, access):

| Dataset | Verdict |
|---|---|
| Slice bursts, d-APV, sIPSC (Breton 2021) | **cannot answer**: endpoint exists, numbers do not; controls pooled; one laboratory |
| PTZ pup + ethosuximide/lithium (Cheng 2020 Fig 7) | **cannot answer**: floor effect in wt/het; two PTZ-alone null cohorts differ by about the ethosuximide effect (viewed: late-phase PTZ-alone about 1.5 to 2.7 in 7b, about 0.5 to 1.7 in 7d); no interaction test |
| AAV9 add-back (Repudi 2021, Obeid 2026), organoid add-back | not a bypass: uses wild-type WWOX; and no deposit |
| Organoid KO RNA (GSE156243) | transcripts only, composition-confounded (seed S067 demoted) |
| P17 mouse deletions GSE158681/2 | **usable for a state question**: perturbation = deletion (no WWOX protein), deletion verified, within-line controls, animals as units (2-4 per arm); limits: transcripts, tiny n, control lines differ from WT |
| GSE158684 snRNA | would be the decisive composition datum; **access failed** (below) |
| GSE215425 P47T | excluded: variant protein present |

Access defect, recorded not circumvented: for GSE158684 (six files), and today also for the GSE158681 table that had downloaded before, the GEO server answers HTTP 200 with the declared `Content-Length` and sends 0 bytes (https, ftp and the GEO download route; two retries; Python and curl). The analysis used the already-held copies whose sha256 equal `inputs/SHA256SUMS` (the IT6 P4 values). Reopening: a plain fetch that returns the bytes.

## 3. The answerable question and its result

Question: **in P17 mouse brain with Wwox deleted (no WWOX protein), is the E/I state (a) an interneuron-selective deficit, (b) a generalised neuronal/composition shift, (c) an activity-regulated signature, and (d) which channel/transporter transcripts differ?** Predictions were fixed first (`PRE_ANALYSIS.md` section 4). Script `p3a_e_i_panels.py` (numpy only, deterministic, about 3 s), outputs in `results/`: `panel_summary.tsv` (9 panels x 7 contrasts x 3 TPM thresholds), `selectivity.tsv`, `genes_individual.tsv`.

| Panel (set mean, log2, centred) | H_S (3 v 2) | H_N (2 v 2) | H_null (2 v 3) | C_S (3 v 4) | background (control v control) |
|---|---|---|---|---|---|
| PAN (pan-neuronal) | +0.17 | +0.38 | +0.04 | +0.18 | -0.31 to +0.04 |
| EXC | +0.06 | +0.37 | +0.21 | +0.15 | -0.25 to +0.06 |
| INH_ALL | +0.17 | +0.23 | +0.00 | +0.05 | -0.40 to -0.15 |
| PV (Pvalb Kcnc1 Kcnc2 Lhx6) | **-0.74** | -0.14 | **-0.38** | -0.15 | -0.10 to -0.01 |
| SST_NPY | +1.46 (one animal) | +0.05 | +0.20 | +0.45 | -0.45 to +0.23 |
| IEG | +0.73 (one animal) | -0.44 | -0.68 | -1.13 | -0.14 to -0.02 |
| ASTRO | +0.88 | +0.26 | +0.31 | +0.42 | -0.18 to +0.16 |
| MYELIN | -1.84 | -1.09 | -1.76 | -0.80 | -0.39 to +0.09 |

Selectivity (PV minus PAN): -0.91, -0.52, -0.42, -0.33; the matched-null band is about +/-0.4 to 0.8, so only H_null (just) and H_S (borderline) leave it. At 2 to 3 animals per arm no panel can reach exact p < 0.05 (minimum 0.1 to 0.167; the 3 v 4 cortex contrast reaches 0.029 for IEG and MYELIN only). All calls are therefore read as *consistency of sign across independent contrasts plus animal separation*, as in IT6 P4; none is confirmatory.

Single genes (`genes_individual.tsv`; read with the control-versus-control band beside them, because the Cre-line controls differ from wild type: Kcnq2, Hcn2, Gria1, Grin2b have background shifts as large as the deletion effect and are **not** interpretable):
* Clean (background <= 0.25) and consistent in 4 of 4: *Pvalb* down; *Kcnj9* (GIRK3) down (-0.7 to -1.7); *Npy* up (except N/null inside background).
* *Kcnj6* (GIRK2) -0.14, +0.05, -0.25, -0.23 and *Kcnj3* mixed: GIRK1/2 transcripts present (12 and 23 TPM hippocampus) and not lowered, so the target of the ethosuximide off-target action exists at mRNA level in the preparation; this says nothing about neuronal GIRK2 homomer abundance (the authors' own caveat).
* *Cacna1g* +0.08, -1.0, -0.44, -0.28; *Cacna1h* -0.53, -0.44, -0.68, -0.16: not raised. The earlier card note (Cacna1g up in adult P47T hippocampus) is a different genotype, age and region.
* *Grin2c* -1.0, -1.2, -0.8, -1.1 and *Grm3* down in 4 of 4 reproduce two engine seeds (S129, S131) in a second, deletion-verified deposit; *Kcna2* slightly down (S130).
* *Slc12a5* (KCC2) -0.55, +0.28, -0.41, -0.65; *Slc12a2* (NKCC1) -1.09, -0.82, -0.64, -0.45: ratio not raised.

What these results are, and are not. RNA is not protein is not current: no single transcript here is a measured current or a cell count. The PV result is compatible with PV-cell loss (the IHC counts S063), with less Pvalb per cell, or with delayed maturation (myelin is down 0.8 to 1.8 in the same animals; Pvalb rises steeply at this age); NPY mRNA up beside NPY-cell counts down fits seizure-induced expression in other cells, which these data do not show. Direction of change is used only as evidence for a reading and never as benefit.

## 4. Candidacies (phenotype-first entry; table in `candidacies.tsv`)

| Id | Role | Candidate | Action, context | Counter-evidence | Decisive missing datum | State |
|---|---|---|---|---|---|---|
| C1 | known reference | ethosuximide (CHEMBL696, phase 4; catalogue mechanism T-type only) | PTZ stage lowered in null pups, late phase only; T-type and GIRK actions | no interaction test, no same-day control, floor in wt/het; GIRK block would predict the opposite sign (prior knowledge, unverified here); Cacna1g/h mRNA not raised | same-day three-genotype PTZ with interaction test and exposure | REFERENCE; T-type attribution NOT SUPPORTED |
| C2 | new proposal | Kv7 opener: ezogabine (CHEMBL41355, phase 4) as probe; azetukalner (CHEMBL5095264, phase 3; no mechanism record in ChEMBL) | for the depolarised resting potential (about 5 mV, Breton) | Kcnq2 difference inside the control-line band; fewer channels lowers an opener's ceiling | resting potential and XE991-sensitive current in KO vs control neurons, then opener on bursts | PROPOSAL; ex vivo probe only; development NOT ASSESSED |
| C3 | mechanism-distinguishing | GluN2B NAM (radiprodil, CHEMBL182066, phase 2) vs d-APV | partial block gives F*; separates NMDAR gain from permissive necessity | Grin2b mRNA flat/low, Grin2c low: no transcript hint of gain | isolated NMDAR current | KNOWN (F04); only a caution added |
| C4 | counter-hypothesis | state secondary (illness, myelin/maturation, seizures); no drug | PV decline present in neuron-targeted and stem-cell-targeted deletions, not only the sick null | illness not excluded in S and N (glucose unverified); maturation predicts higher Slc12a2 (not seen) | PV-nucleus fraction and Pvalb per nucleus (GSE158684) | OPEN |

Ex vivo utility and systemic development are kept apart: C1 and C3 are usable as probes (C3 clean, same-slice concentration-response), C2 is a probe with its own tool pair (XE991); systemic requirements are only noted where a source was read (radiprodil exposure per IT6 P9; ezogabine discontinuation and azetukalner paediatric status are from prior knowledge or unsearched and are marked so). Counts: **new names 1** (the Kv7 class; two compounds), restated known 2 (ethosuximide, radiprodil/d-APV), counter-hypotheses 1. Nothing was chosen by engine rank. No transfer of evidence between molecules: the ethosuximide result is not carried to apinocaltamide or to any T-type blocker, nor to Kv7 openers.

## 5. Engine v4 on this question (where it fits)

`engine_run/Q4_p3a_mouse_deposit.tsv` (7 seed genes from section 3; NPY entered **up**, as measured in this deposit, against the organoid seed) run with `seed_engine_v4.py run --match indeg --junction on --nnull 200`: the funnel reports 4 of 7 seed units in the signed network; contribution rows come from GAD1, NPY, GRIN2C, GRM3, KCNA2 and one row from KCNJ9; PVALB contributes none. Top `opposes` families: marizomib, HDAC inhibitors (z 5.4 to 5.9), carried by GAD1 and NPY transcription-regulation chains (739 and 717 contribution rows); known ion-channel antiseizure drugs (ethosuximide, ezogabine) have no row at the top, and ethosuximide has no row at all. The IT10 Q4 table (`dispositions_Q4.tsv`) is likewise dominated by BTK inhibitors through BTK -> STAT3 -> NPY, from one origin (the organoid NPY row). I conclude that a signed-network generator is the wrong modality for synaptic/channel biology and that its Q4 lists must not be read as candidates; this is a fit judgement, not a defect in the engine for its own scope. Outputs kept in `engine_run/out/` (seeds file, proposals, contributions).

## 6. The discriminating experiment

Preparation: neuron-targeted (Synapsin-Cre) deletion, neocortical layer II/III slices, P13 to P17, with Cre-negative littermates as controls (not pooled with heterozygotes), animals as units, one perfusate defined for incubation and recording (Mg2+ stated), plus wild-type slices driven to burst by a matched trigger (E3 of IT6 P9).
Measurements, in the same slices: resting potential and Kv7 (XE991-sensitive) current; isolated NMDAR current (amplitude, decay, GluN2B sensitivity); sIPSC amplitude/frequency; burst frequency under (i) GluN2B NAM concentration-response, (ii) Kv7 opener with XE991 reversal, (iii) low-dose GABA-A potentiation as a disinhibition probe.

| Reading | Predicts |
|---|---|
| NMDAR gain | isolated NMDAR current raised; NAM stops bursts at partial block (F* well below 1); Kv7 opener weak |
| Intrinsic depolarisation | Vm depolarised with reduced XE991-sensitive current; opener stops bursts at an unchanged NMDAR current; NAM acts only near complete block; matched-trigger wild-type slices respond the same to the NAM |
| Disinhibition | sIPSC amplitude about halved confirmed; GABA-A potentiation restores part of the effect; PV counts reduced in the neuron-targeted deletion |
| Secondary/composition | burst phenotype in wild-type slices matched for activity and myelin state indistinguishable; none of the probes shows a genotype-by-drug difference |

In silico, no bench needed: GSE158684 (nucleus-resolved): PV-nucleus fraction among neurons, Pvalb per PV nucleus, cell types carrying Npy: separates fewer PV cells from less Pvalb per cell. Blocked today (access defect, section 2). The PTZ pup experiment (C1) needs the same-day control and interaction test before any channel attribution.

## 7. Check for the two alternatives (brief P3.3)

| Item | Q3 ISR | Metabolism (Q2, HIF/lactate) |
|---|---|---|
| Public perturbation in a WWOX-null neural system | GSE158681/2, GSE156243, hNPC GSE126075 (transcripts) | same deposits |
| Function endpoint | none (ATF4 protein, eIF2alpha-P, PERK/GCN2 not deposited) | none (lactate, OCR, flux not deposited; MTBLS12344 not public) |
| Already run on the same deposit | IT6 P4: all sets inside their null, sign unresolved | IT10 P2.1, IT12 P47T (broad modest shift, not HIF-selective) |
| Verdict | not taken: nothing new is readable; reopening = a protein/phospho/flux measurement | not taken: same; reopening = HIF protein or lactate in tissue fixed by perfusion |

## 8. Edits this implies (proposals only; I did not make them)

1. Q4 seed S116 (NPY, organoid, down) and S066 (NPY cell counts, down) should carry a `direction_status` of uncertain across systems/levels with this deposit's NPY mRNA up (4 of 4 contrasts) as a counter-observation; the engine's Q4 `opposes` arm for NPY rows (BTK/STAT3 chain, one origin) becomes `HELD`; question_roles Q4 stays `unknown`.
2. Card F03: add "NKCC1:KCC2 transcript ratio not raised in P17 deletion deposits (Slc12a2 -0.45 to -1.09, Slc12a5 -0.41 to -0.65, +0.28 in N); E_GABA unmeasured" to counter-evidence; the abstention stands.
3. Card EB-ETX-01/U17: add "Cacna1g/h mRNA lower or flat, Kcnj6 flat in P17 deletion hippocampus (transcript only)" and "catalogue (ChEMBL) mechanism record lists T-type only"; no change of state.
4. A new need or card candidate "resting potential / Kv7 current in neuron-deleted slices" (C2) as an ex vivo probe, `REQUIRES_QUALIFICATION`, with its own XE991 pair; no ranking change.
5. Add Pvalb mRNA lower (4 of 4) and pan-interneuron panel flat as a transcript observation beside S063; note PV vs maturation ambiguity.
6. Catalogue GSE158684 as "files declared, body not delivered on 2026-10-31".

## 9. What a verifier must check, and limits

* **Single decisive link:** the PV result needs a nucleus-resolved count (GSE158684 matrices, or immunostaining in the neuron-targeted deletion). Until then "PV-selective deficit" is a transcript statement.
* Re-run: `python3 -I p3a_e_i_panels.py <hippo.txt.gz> <cortex.txt.gz> <Ensembl92 cdna.fa.gz> results` with inputs matching `inputs/SHA256SUMS`; the output is deterministic.
* Limits: n = 2 to 4 animals per arm; Cre-line controls differ from wild type (control-versus-control band reported); the N and S line identities and control genotypes are not stated in the deposit (IT6 P4); transcripts, not protein or function; the engine was run with a hand-built seed table (not a deposited tier); ChEMBL records give identity and catalogue mechanism, not label, paediatric status or trials, which I did not search; no figure was digitised (Fig 7 values quoted by eye from a viewed PNG).
* Not shown: any rescue, any benefit, any variant-allele effect. A compatible action is not a predicted benefit.
