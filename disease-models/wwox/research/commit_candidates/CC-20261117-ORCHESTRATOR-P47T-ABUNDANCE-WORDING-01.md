# CC-20261117-ORCHESTRATOR-P47T-ABUNDANCE-WORDING-01
- **Status: QUEUED, NOT APPLIED.** No file named below is edited by this candidate's authoring; it proposes. Propagation (if any) is a later BATCH_COMMIT by the owners; nothing here is a BATCH DISPOSITION.
- **Class:** MINOR wording correction (ORDINARY), no working-model statement contradicted: `working_model_current.md`, `claim_registry_current.md` and `paper_registry_current.md` already say "present, similar by eye, not quantified" (`BATCH_20260926_MALLARET`, `BATCH_20260928_007`); no version bump proposed. No claim created, reversed or promoted; no `Status`, `Type`, `Title` or `Summary` changes.
- **Author:** ACTOR_ID `orchestrator` (IT), task IT56-Q05 / ADV-019, 2026-11-17; written for ADV (assigner), SCI (author of the source note) and the owners of the dated analyses.
- **Source material:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/deepening_sci_20261116/P47T_ABUNDANCE_CLOSURE_NOTE_IT56_Q05_SCI_20261117.md` (sections 1 to 4; held files only); scan script `it_p47t_wording_20261117/p47t_wording_scan_it_20261117.py` and the per-line table `it_p47t_wording_20261117/p47t_hits_with_disposition_20261117.tsv` (same folder).

## The wording this candidate proposes
Replace, where a sentence asserts P47T protein abundance, "normal" / "wild-type amount" / "unchanged" by: **"present, similar to controls by the authors' wording, not quantified"** (fibroblasts: one individual, by eye; knock-in cerebellum: the input lane of a pull-down, n = 2 per genotype, mutant bands lighter by the blind audit's integration, about 0.70, rank order only; mRNA comparable at n = 6, which is quantified). Folded state, solubility and half-life were never tested. Class B label: "binding loss; protein present, level not quantified, stability untested".

## Count (script, then my reading of each line; SCI's 19 is a pointer, this is the count)
Scan rule fixed before the hits were read: a line under `analysis/` or `registries/` that names P47T (or `Pro47Thr`, `c.139C>A`) AND carries an abundance phrase (normal/wild-type/similar/comparable + protein/abundance/amount/level; `protein-normal`; `normal western`; `at normal`; `protein retained/preserved`), markdown emphasis stripped; plus a second pass for the bare word "normal" on a P47T line. **Line level only**: a statement split across two lines is not seen, and the second pass shows the phrase list is not complete (it added two stale lines and five false positives).

| Disposition | Lines | Meaning |
|---|---|---|
| STALE (asserts normal/wild-type abundance for P47T protein) | 34 | in 19 files; proposed correction below |
| LABEL (row already qualified, but the label word NORMAL stays) | 1 | `wwox_missense_stability_census_20260922.md:433`; owners' next touch |
| QUALIFIED (already says present / not quantified / by eye) | 5 | `analysis/proteostasis_rationale.md:47,89`, `analysis/mechanism_intervention_map.md:357`, `registries/paper_registry_current.md:6611`, `analysis/wwox_missense_abundance_lysis_census_20260922.md:80`; no action |
| QUOTE (the authors' own words, attributed, or a quoted earlier claim) | 4 | `nascimento_accession_and_g372r_20260922.md:369,417`, `wwox_missense_abundance_lysis_census_20260922.md:78`, `wave7_verification_mallaret_chain_20260922.md:144`; no action |
| GENERATED / LEDGER | 7 | `analysis/data/pathograph_export.jsonl` (2 lines, derived) and `registries/fulltext_read_receipts.jsonl` (5 lines, hash-chained ledger): never edited by hand; the pathograph is regenerated, the ledger is append-only |

**Live canonical surfaces: 0 stale lines.** The four registry files carry no line that asserts normal P47T protein (the only registry hit, `paper_registry_current.md:6611`, quotes the authors' wording and says "not quantified"); the three registry lines that mention "normal" near P47T concern growth, the Q230P transcript and a history row, not P47T protein. So no registry edit is proposed, and the registries do not need this candidate for correctness; SCI's 19 files are, by this count, all dated analyses (19 files here carry a STALE or LABEL line, a coincidence of number, not of membership: SCI's grep also counted qualified and quoted files).

## Proposed lines: one dated correction line per file (dated analyses are history; no sentence is rewritten)
Form, appended at the foot of each file by its owner: `[Update 2026-11-17, CC-20261117-ORCHESTRATOR-P47T-ABUNDANCE-WORDING-01: where this file says P47T protein is "normal" (lines N...), read "present, similar by the authors' wording, not quantified; stability untested". <consequence sentence if the argument depends on it>. Nothing else in this file changes.]`

| File | Lines | Layer | Argument depends on equal abundance? | Consequence sentence for the update line |
|---|---|---|---|---|
| `analysis/cerebellar_discrimination_experiments_20260922.md` | 144,150,165,178,221,405,417,441,477 | dated analysis | yes | The "function rather than abundance" contrast (P47T versus an AAV-treated null) rests on equal abundance; with abundance unquantified, and the input band lighter in the one blot that shows it, the contrast is weaker than written, not removed (binding loss at present protein stands). |
| `analysis/cerebellar_measurement_census_20260922.md` | 383 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/denominator_audit_therapeutic_portfolio_20260922.md` | 69 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/lectin_readout_domain_dependence_20260921.md` | 333,390 | dated analysis | yes | P47T as discriminator needs an abundance control; "normal abundance" is not shown, so the abundance control is not optional. |
| `analysis/legacy_reconstruction_sweep_20260922.md` | 118 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/model_horizon_and_p47t_platform_20260922.md` | 222 | dated analysis | yes | "Normal abundance, lost function" becomes "protein present, function lost"; the abundance-versus-function point stands only at the level of presence. |
| `analysis/nascimento_accession_and_g372r_20260922.md` | 388 | dated analysis | yes | "Both protein-normal" becomes "both protein present"; the burial argument is unchanged. |
| `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md` | 357,805,905 | dated analysis | yes | "Protein level is normal and Purkinje cells are lost anyway" becomes "protein present, level unquantified"; the permitted statement is binding loss with protein present. |
| `analysis/purkinje_custody_and_minimal_design_20260922.md` | 258 | dated analysis | yes | Same as the Purkinje census row: protein present, level unquantified. |
| `analysis/purkinje_existing_material_experiment_20260922.md` | 63 | dated analysis | yes | Same: the permitted statement is protein present, level unquantified, Purkinje cells lost. |
| `analysis/q230p_survival_paradox_20260921.md` | 224,298 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/q230p_true_frontier_20260922.md` | 166 | dated analysis | yes | The inversion of the ddG predictor against the six measurements used P47T as "normal in two matrices": read "present in two matrices"; the inversion is then weaker for P47T and rests on the other measured variants. |
| `analysis/sampling_frame_vs_biology_node_20260923.md` | 138 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/sdr_missense_readout_assessment_20260920.md` | 212 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/superior_node_search_20260922.md` | 125 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/wave7_verification_mallaret_chain_20260922.md` | 153,175 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/wwox_independent_downstream_rescue_20260922.md` | 310 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |
| `analysis/wwox_missense_stability_census_20260922.md` | 173,433,482,496 | dated analysis | yes | Lines 173, 433, 482, 496: "both NORMAL" becomes "present, similar by the authors' wording, not quantified"; section 6.1's ranking row for P47T changes in the same way. |
| `analysis/wwox_sdr_function_per_molecule_census_20260921.md` | 178 | dated analysis | no | Descriptive mention only; no argument in the file depends on equal abundance. |

## Sentence list (every STALE or LABEL line; sentence cut at 160 characters; full sentences in the TSV)
| File:line | Class | Phrase | Sentence (cut) |
|---|---|---|---|
| `analysis/cerebellar_discrimination_experiments_20260922.md:144` | STALE | protein level is normal | with a Purkinje marker — Wwox^P47T/P47T, calbindin, n = 3 — total protein level is normal and Purkinje cells are |
| `analysis/cerebellar_discrimination_experiments_20260922.md:150` | STALE | at normal | (P47T abolishes PPxY binding at normal abundance; a null has no protein at all), species, and |
| `analysis/cerebellar_discrimination_experiments_20260922.md:165` | STALE | at normal | - The WW-domain / PPxY interaction tradition. P47T abolishes PPxY binding at normal protein level — so C6 |
| `analysis/cerebellar_discrimination_experiments_20260922.md:178` | STALE | abundance is normal | > about to converge on the same partition. In Wwox^P47T/P47T, abundance is normal and Purkinje cells die — so |
| `analysis/cerebellar_discrimination_experiments_20260922.md:221` | STALE | normal-abundance | the "scissors": that P47T-normal-abundance-with-loss and an AAV-treated-null Purkinje |
| `analysis/cerebellar_discrimination_experiments_20260922.md:405` | STALE | at normal | (P47T abolishes PPxY binding at normal abundance; a null has no protein to bind with), species/system, and |
| `analysis/cerebellar_discrimination_experiments_20260922.md:417` | STALE | at normal | / C6 / 🎯 FUNCTION rather than ABUNDANCE / What a Purkinje cell needs is WWOX doing something — specifically, in the P47T allele, PPxY-ligand binding through WW1 |
| `analysis/cerebellar_discrimination_experiments_20260922.md:441` | STALE | normal total protein | / Function vs abundance / That abundance is not automatically the right endpoint in this gene. P47T has normal total protein and loses Purkinje cells, so a gene |
| `analysis/cerebellar_discrimination_experiments_20260922.md:477` | STALE | normal abundance | / HIGH / still reduced / Two independent systems — P47T (normal abundance, cells lost) and an AAV-treated null — reach the same partition by different routes. A |
| `analysis/cerebellar_measurement_census_20260922.md:383` | STALE | normal WWOX protein | 🔴 (i) does not transfer to (ii). A P47T knock-in mouse is a hypomorph with normal WWOX protein |
| `analysis/denominator_audit_therapeutic_portfolio_20260922.md:69` | STALE | normal protein | / TX-003 (line 64) proteostasis / The same "protein not detected", plus the allelic ranking P47T (normal protein) / G372R (barely detectable) / Q230P (absent) / |
| `analysis/lectin_readout_domain_dependence_20260921.md:333` | STALE | normal abundance | - What each outcome means. P47T is the discriminator. If P47T (normal abundance, WW1-dead) |
| `analysis/lectin_readout_domain_dependence_20260921.md:390` | STALE | normal abundance | / Experimental roadmap / YES / § 7.1 specifies the single cheapest decisive experiment, identifies P47T as the discriminator (normal abundance + WW1-dead — the  |
| `analysis/legacy_reconstruction_sweep_20260922.md:118` | STALE | normal protein | / F-2 ⭐ / P47 is described as a fold-stabilising core residue. Verbatim: "Proline 47 is a highly conserved residue that is part of the WW motif consensus sequen |
| `analysis/model_horizon_and_p47t_platform_20260922.md:222` | STALE | normal abundance | / H12 / Longitudinal biomarker trajectory; abundance ≠ function — DL-BIO-085 / months / 🔴 NO / 🟢 YES, and P47T is the proof of the point — normal abundance, los |
| `analysis/nascimento_accession_and_g372r_20260922.md:388` | STALE | protein-normal | burial-discriminates argument gets simpler: P47T and G372R both surface, both protein-normal, |
| `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md:357` | STALE | normal level | / Protein / normal level; PPxY binding abolished (P47T) / normal level; consequence "unclear at this point" / |
| `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md:805` | STALE | protein level is normal | whole literature sit on the SCAR12 allele — Wwox^P47T/P47T in a mouse — where protein level is normal |
| `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md:905` | STALE | protein level is NORMAL | > SCAR12 allele — Wwox^P47T/P47T, in a MOUSE — where WWOX protein level is NORMAL and Purkinje |
| `analysis/purkinje_custody_and_minimal_design_20260922.md:258` | STALE | protein is normal | Wwox^P47T/P47T, total protein is normal and Purkinje cells are lost anyway |
| `analysis/purkinje_existing_material_experiment_20260922.md:63` | STALE | normal total protein | / Wwox^P47T/P47T: normal total protein, Purkinje cells lost anyway — permitted statement only / purkinje_cerebellar_celltype_wwox_census_20260922.md § 4 / |
| `analysis/q230p_survival_paradox_20260921.md:224` | STALE | normal protein | which P47T has normal protein and a mild phenotype with abolished binding while Q230P has no detectable |
| `analysis/q230p_survival_paradox_20260921.md:298` | STALE | normal protein | a proxy — Q230P missense with no detectable protein; P47T missense with normal protein and mild phenotype; |
| `analysis/q230p_true_frontier_20260922.md:166` | STALE | normal protein | / SUP-2 / ThermoMPNN ΔΔG +1.514 as evidence of instability / The predictor is inverted against the six measurements that exist: the highest predicted ΔΔG (P47T, |
| `analysis/sampling_frame_vs_biology_node_20260923.md:138` | STALE | normal protein | / D6 / Abundance→severity: P47T normal protein/mild vs Q230P undetectable/severe vs G372R low/mild / CLAIM 030; DL-MECH-033; FM-014 / 🟢 YES, and explicitly: cla |
| `analysis/sdr_missense_readout_assessment_20260920.md:212` | STALE | normal protein | severe; G372R (SDR) → protein barely detectable by IF → mild; P47T (WW1) → normal protein levels, |
| `analysis/superior_node_search_20260922.md:125` | STALE | normal protein | / missense/missense / 🔴 variable, and this is the honest limit. An allele that folds and retains 388–407 retains the brake. P47T has normal protein and is mild  |
| `analysis/wave7_verification_mallaret_chain_20260922.md:153` | STALE | normal | / P47T / WW1 / 0.286 / partially exposed / β-strand / 82.3 / 51.4 Å / +2.81 / normal / mild / |
| `analysis/wave7_verification_mallaret_chain_20260922.md:175` | STALE | protein normal | the same residue, P47T (ΔΔG +2.81, the highest of all four) → mild, protein normal; and |
| `analysis/wwox_independent_downstream_rescue_20260922.md:310` | STALE | normal protein | > least in a class that retains folded protein containing 388–407. P47T has normal protein levels and |
| `analysis/wwox_missense_stability_census_20260922.md:173` | STALE | both NORMAL | (b) P47T — abundance, twice, in two matrices, both NORMAL. |
| `analysis/wwox_missense_stability_census_20260922.md:433` | LABEL | both NORMAL | / P47T / MEASURED ×2, both NORMAL — (a) human fibroblasts, passages 10/13/14 vs 4 controls, "similar amounts" (Mallaret 2014); (b) mouse cerebellum, Wwox^P47T/P |
| `analysis/wwox_missense_stability_census_20260922.md:482` | STALE | NORMAL abundance | / P47T / 🔴 +2.806 — the HIGHEST of the disease set / NORMAL abundance, twice / human fibroblasts; mouse cerebellum / Mallaret 2014; Hussain 2023 / |
| `analysis/wwox_missense_stability_census_20260922.md:496` | STALE | normal protein | (P47T, +2.81) has normal protein in two independent matrices including neural tissue. The |
| `analysis/wwox_sdr_function_per_molecule_census_20260921.md:178` | STALE | normal protein | - CLAIM 030 — the allelic series (Q230P protein absent → severe; G372R barely detectable → mild; P47T normal protein, binding defect → mild) and the non-commens |

## What is deliberately NOT done
- No registry, working-model, claim or paper-registry edit (none carries a stale line by the count above). The four scientific current files are not touched.
- No edit of any dated analysis; owners add the update line or decline it. No ledger line under BLOCK-1 is touched. `fulltext_read_receipts.jsonl` and `pathograph_export.jsonl` are not edit targets.
- The per-line decision whether a file's argument survives is the owner's; the "depends" column is my reading of the sentence, not a verdict.

## Limits
Line-level scan; the phrase list is incomplete by construction (a second pass added two lines); Italian and other-language wording ("normale") is not scanned; files outside `analysis/` and `registries/` are not scanned (SCI's own 11 files under the pilot folder are SCI's, IT and ADV one each, per the closure note); I did not re-open the Hussain or Mallaret full texts; the wording follows SCI's closure note and ADV's check of it.
