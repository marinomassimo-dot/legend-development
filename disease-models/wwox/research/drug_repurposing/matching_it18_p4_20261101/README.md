# IT18 P4 — matching comparison (T / X / L)

Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit claim. Public edition, WWOX-DEE genotype class.

## Stage 1 — answers locked (2026-11-01)

Written before the GtoPdb reference of any EVAL compound was read (`load_gtopdb_split` drops EVAL rows on read in the `answers` and `dev` commands).

- `answers.tsv`: T/X/L labels for all 205 universe rows (186 parent compounds; 111 DEV rows, 94 EVAL rows). Columns `L_v2`/`L_v2_reason` hold the dated second rule below, fixed on DEV before the lock.
- `priors.tsv`: the X prior per target (DEV GtoPdb majority, global DEV majority DECREASE where unseen or tied).
- `answers_lock.json`: digests of the script, `direction_task.py`, `priors.tsv`, `answers.tsv`, catalogue, needs and ChEMBL target file.

Pre-lock DEV observations (ChEMBL side only, no EVAL reference read):
1. Every X prior on the three directed needs' targets is DECREASE, so X = L on every directed row (0 of 72 rows differ). The WWOX contribution to accuracy on directed needs is therefore zero by construction, before any scoring.
2. **Method defect found on DEV**: ChEMBL group-level records spread one action to all components. The 26-component "Voltage-gated calcium channel" PROTEIN COMPLEX GROUP puts bepridil, terodiline, suloctidil and phloroglucinol (BLOCKER) and the gabapentinoids (MODULATOR, an alpha2delta ligand class) onto CACNA1G/H/I, so T proposes them for the T-type need and L v1 labels the blockers compatible. Minimal fix to the L rule only (`L_v2`): abstain (`group_record_mostly_outside_module_targets`) when every ChEMBL record that reaches the need has fewer than half of its components among the module's intervention targets (all needs). A first version that used the single need's targets wrongly abstained on the T-type family record (3 components) for the seizure need, which lists only CACNA1G; it was replaced before the lock. v2 changes 8 rows (4 compounds × 2 needs), all CACNA1G/H/I. Run 1 (registered rule v1) is the primary result; run 2 (v2) is reported as a separate, dated, labelled run.

## Stage 2 — EVAL scored once (2026-11-01, run 1, registered rule v1)

`results.json` records the lock digest; `reference.tsv` carries the per-row reference category; `cases.tsv` the case table. The scorer refuses to run unless the lock digests match and `answers.tsv` / `answers_lock.json` are committed and clean.

**Principal figure.** On the three directed needs, EVAL holds 33 (need, compound) rows over 29 distinct compounds. Only **2 of 33** rows have a determinate GtoPdb reference (coverage: 31 of 33, 93.9 percent, have no GtoPdb counterpart on any of the need's target genes). L labels both of those 2 compatible and both are truly compatible: precision 2/2 = 1.00, Wilson 95 percent interval **[0.342, 1.000]**. T's base rate on the same 2 determinate rows is also 2/2 = 1.00, interval [0.342, 1.000].

**Decision, by the pre-registered rules.**
- `L_vs_T`: *fewer than 40 determinate EVAL compounds (n = 2): the figure is reported with its interval and no improvement statement is made.* The registration named this outcome in advance and forbade widening the universe after the lock. **No advantage of L over target-only is measured, and none is excluded** — the evaluation has no power at this denominator.
- `L_vs_X`: *no measured WWOX contribution to accuracy on directed needs.* X and L differ on 0 of the 33 directed EVAL rows (0 of 76 directed rows overall). Every X prior over the directed needs' target genes is DECREASE, which equals the WWOX-stated direction, so the two paths are the same classifier on this slice. This is the acceptable result the registration anticipated, not a failure of the contextual path.

**Abstentions.** L abstains on 3 of 33 EVAL directed rows (9.1 percent), all `action_partial_or_unknown` (partial agonists at NMDAR: apimostinel; MODULATOR gabapentinoids at the calcium-channel group). X abstains on the same 3. No abstention falls on a row with a determinate reference, so abstention costs no measured accuracy here. Errors: 0 truly-opposite rows labelled compatible, 0 truly-compatible rows labelled opposite, on either path.

**Denominators, so the 2/33 is not read as the whole picture.** Universe: 205 rows, 186 parent compounds, across 11 needs with intervention targets (12 of the 23 needs contribute nothing: their intervention targets have no direct human ChEMBL mechanism in the catalogue — all five WWOX-restoration needs, ISR, LDH/MCT, NKCC1, PANX1 among them). Directed needs: 76 rows (43 DEV, 33 EVAL). DEV directed, descriptive only: 43 rows, 6 determinate, T base rate 6/6 = 1.00 [0.610, 1.000], L precision 4/4.

**Independence.** 0 of the EVAL directed rows share a PubMed id between the ChEMBL mechanism and the GtoPdb interaction, so on this slice the two curations do not visibly rest on the same paper. That is a partial check only: ChEMBL and GtoPdb share part of their literature, and 339 of the IT17 EVAL pairs carried no module reference at all, so agreement is not independent confirmation.

**Why the reference is so thin here, and why this is the real finding.** The compounds the module proposes for the directed needs are overwhelmingly subunit-level or group-level ChEMBL mechanism records (72 of the 76 directed rows rest only on group- or family-level records; just 4 carry a SINGLE PROTEIN record), while GtoPdb curates the named subunit (Ca_v3.1 = CACNA1G, GluN2A = GRIN2A). The join on (parent compound, UniProt) therefore misses most of them: memantine's GtoPdb human rows do not carry a GRIN UniProt accession at all, ketamine's GluN2A/2B/2C/2D rows are `Channel blocker / None`, and its GluN2C antagonist row is rat. The 2 determinate EVAL rows are tezampanel and amantadine. **The measured bottleneck is not the direction field (IT17 showed 0.997 agreement on the covered space) but reference coverage at the resolution the needs are written in.** Raising it needs a subunit-aware join (GtoPdb target id and subunit ids, `targets_and_families.csv`), not more compounds.

## Run 2 — dated second run with the repaired path L rule (2026-11-01, label `run2_lv2_20261101`)

Separate files (`results_run2_lv2_20261101.json`, `cases_run2_lv2_20261101.tsv`). The v2 rule was fixed on DEV and locked in `answers.tsv` before the EVAL reference was read; it is reported second because the registered rule is v1, and it is **not** presented as an independent result.

EVAL directed: L abstains on 5 of 33 rows (1 partial action, 4 `group_record_mostly_outside_module_targets`: bepridil and trimethadione on both the seizure and T-type needs); compatible labels fall from 24 to 22. The 2 determinate rows are untouched, so the principal figure is unchanged (2/2, [0.342, 1.000]) and `L_vs_T` stays "fewer than 40". `L_vs_X` becomes "L and X differ on directed needs but no significant accuracy difference (sign p = 1.0)": the 8 rows where the paths now diverge all have an unknown reference, so the difference cannot be scored. On DEV the rule moves 14 rows into abstention (31 compatible to 25). The repair therefore changes what the module would propose while changing nothing it can measure — the honest summary is that it removes labels that the reference cannot adjudicate either way.

## The two-part WWOX-contribution statement

The parts are stated separately and are not summed.

**(a) On directed needs: zero.** L = X on all 76 directed rows (33 EVAL). The target prior derived without WWOX already equals the WWOX-stated direction on every target gene of the three directed needs, so the WWOX record contributes no accuracy there. Under the run-2 rule the paths differ on 8 rows but no scoreable accuracy difference follows (sign p = 1.0).

**(b) On uncertain needs: an information effect, not an accuracy gain, and the reference cannot score it.** Counting (need, compound) rows that X labels compatible or opposite and L declares indeterminable because the WWOX record states the direction is uncertain, conflicting or merely "restore" (`wwox_contribution_b_information_effect` in `results.json`):

| Need | Universe rows | X compatible | X opposite | L abstains on the need direction | Counter-evidence cited |
|---|---|---|---|---|---|
| NEED-NEUROINFLAMMATION-GLIA | 52 | 51 | 0 | 51 | treats an effect: neuron-restricted rescue lowers gliosis; class-level only (6 items) |
| NEED-MYELINATION | 36 | 29 | 7 | 36 | N-13, target not causally downstream in the targeted cell; window closing (3 items) |
| NEED-MTOR-AUTOPHAGY | 27 | 26 | 1 | 27 | N-01 INSUFFICIENT: autophagy direction contradicts the mTOR direction (2 items) |
| NEED-GSK3B-DEREPRESSION | 6 | 6 | 0 | 6 | lithium suppressed PTZ seizures in all three genotypes, wild type included (4 items) |
| NEED-REDOX-NRF2 | 5 | 4 | 1 | 5 | organoid shows no cytokine-expressing cells, no coherent NRF2 signature (4 items) |
| NEED-INHIBITORY-HYPOFUNCTION | 1 | 1 | 0 | 1 | organoid GABAergic markers up at protein level; competing account (4 items) |
| NEED-PDH-PYRUVATE-AXIS | 1 | 1 | 0 | 1 | PDK1 lower in the knockout organoid; PDH activity unchanged (11 items) |
| NEED-WNT-BETA-CATENIN | 1 | 1 | 0 | 1 | maturity confound; signature reversal selects no axis (3 items) |

**128 rows in total** that a target-only or external-only path would put forward with a direction, and that the WWOX record refuses to direct. Three of them are card-linked compounds the module has already reasoned about: dimethyl fumarate and monomethyl fumarate (KEAP1 inhibition, X compatible) and omaveloxolone (NFE2L2 activation, which X calls **opposite** because its DEV-derived prior for NFE2L2 is DECREASE — an artefact of the prior, since no DEV compound acts on NFE2L2 and the global majority applies); sodium dichloroacetate on the PDK genes (X compatible). On all four L abstains, and the need's own `do_not_assume` text says why. The reference cannot adjudicate any of this: it is an information effect, listed per need, and claiming it as an accuracy gain would be unsupported.

## Contrast case table (28 cases, rule-selected before scoring)

`cases.tsv`, selected by lowest sha256 of the parent id within each contrast, never by outcome; the available count per contrast is in the last column. Contrasts 1, 3, 4, 5 and 6 have data; **contrast 2 (same compound, different or opposite actions across targets of one need) has none: 0 of 76 directed rows hold it**, which is itself a consequence of the group-record problem — one group record gives one action to every component, so a within-need action conflict cannot arise. Reported as an absence, as the registration requires.

| Contrast | Cases | What the pair shows |
|---|---|---|
| 1 same target, opposite action | C01-C04 | selurampanel (GRIA1-4 DECREASE, compatible) against pesampator (GRIA1-4 INCREASE, opposite) at the same AMPAR subunit genes; 8 such gene-need pairs exist. Both references unknown |
| 2 same compound, opposite actions within one need | — | **no data (0 rows)**; see above |
| 3 subunit-level versus complex-level mechanism | C05-C10 | talampanel (two SINGLE PROTEIN rows) against ketamine (7-component group); ABT-639 (CACNA1H single) against atagabalin (26-component group, MODULATOR, indeterminable); vigabatrin (ABAT single) against atagabalin. 2 single / 38 complex on the glutamate need, 1 / 17 on each calcium need |
| 4 partial or ambiguous action versus clean action | C11-C13 | the MODULATOR gabapentinoids (indeterminable) against suloctidil (BLOCKER, compatible); 14 ambiguous / 62 clean |
| 5 ChEMBL only, reference unknown | C14-C15 | atagabalin: kept **unknown**, never negative; 68 such rows |
| 6 card-linked versus not | C16-C28 | all 12 card-linked universe rows plus one non-card row: ethosuximide, vigabatrin, perampanel, apinocaltamide, memantine (directed, L compatible) and dimethyl/monomethyl fumarate, omaveloxolone, dichloroacetate (uncertain needs, L abstains while X labels) |

The case table is where the two paths visibly differ: every row on which X labels and L abstains is a card-linked compound on an uncertain need (C23-C27).

## P4.5 — cross-need and context scan

From the universe, looking for compounds compatible with two *different* directed needs, or carrying a documented context a target-only listing does not expose.

**Cross-need: 18 compounds appear under two or more needs, but 16 of the 18 are the trivial overlap** of NEED-SEIZURE-CONTROL-SYMPTOMATIC and NEED-T-TYPE-CALCIUM, which both list CACNA1G: the same record, counted twice, not two independent needs met. Vigabatrin spans the seizure need (ABAT, compatible) and NEED-INHIBITORY-HYPOFUNCTION (uncertain, L abstains) — the same ABAT mechanism read under two needs, one directed and one not. **One compound is a genuine two-need case: terodiline**, the only universe compound reaching a directed calcium need and the myelination need through two different mechanisms.

### IPOTESI — terodiline as a two-mechanism probe, not a candidate

- **Generating information.** Not a literature search: the universe table itself. Terodiline (CHEMBL363295) carries two distinct direct human ChEMBL mechanisms — BLOCKER at the voltage-gated calcium channel group (reaching CACNA1G/H/I, so T-type need, L compatible) and ANTAGONIST at the muscarinic receptor family (reaching CHRM1, so the myelination need). A target-only listing shows these as two unrelated rows under two needs and never as one compound.
- **Compound / action / context.** Terodiline, an antimuscarinic with calcium-channel-blocking activity, formerly marketed for urinary incontinence. Context: the catalogue gives it access category `unknown/unverified` only, with a first approval year of 1986 and no current prescription product — the coarse signal of a drug no longer marketed.
- **Need and hypothesised benefit.** It is the only universe compound whose two mechanisms address a directed need (lower T-type current, NEED-T-TYPE-CALCIUM, "down", inferred from a T-type blocker suppressing the late phase of the provoked seizure score in the null mouse) and a second, differently-directed need (NEED-MYELINATION, "restore") at once. The M1-antagonist route to oligodendrocyte differentiation is an established pro-myelinating pharmacology in other diseases.
- **WWOX evidence.** For the T-type arm: one perturbation result in the Wwox-null mouse, with genotype specificity not established by an interaction test. For the myelination arm: **none for any pharmacological route.** The need's own certainty field says myelin recovery is supported in the mouse only *after the causal rescue*, and "unknown for any pharmacological route".
- **External precedent.** An M1-antagonist pro-myelinating precedent exists in another disease; it is `OTHER_DISEASE_PRECEDENT` and carries no WWOX transfer.
- **Counter-evidence, and it is decisive.** (i) Terodiline is not a usable medicine: the catalogue's own access state is `unknown/unverified`, consistent with withdrawal, and this scan found no evidence of current availability. (ii) The calcium arm rests on the group-record defect this very package documented: the 26-component group record does not say terodiline blocks Ca_v3; under the repaired rule L abstains on it. (iii) GtoPdb has no determinate counterpart for either arm, so the reference adjudicates neither. (iv) The CHRM1 prior in the catalogue is a 3/3 tie, the weakest prior in `priors.tsv`. (v) The myelination need warns that a pro-myelinating agent may be unable to act if the neuron does not signal, and that chronic NMDAR block may itself harm activity-dependent myelination — so the two arms of a combined excitability-plus-myelin story may oppose each other.
- **Missing datum.** Whether terodiline, or any M1 antagonist, blocks Ca_v3.1/3.2/3.3 at a subunit-resolved measurement at all; and whether any pro-myelinating pharmacology acts in a WWOX-deficient neural system.
- **Discriminating next experiment.** Not a terodiline experiment. The discriminating step is the subunit-resolved join: re-run the universe with GtoPdb target and subunit ids, which decides for every group-record compound whether the action reaches the need's genes. That single change would reclassify 55 of the 76 directed rows and raise the 2/33 reference denominator — it discriminates between "the module's direction field is wrong" (IT17 says it is not) and "the module's target resolution is too coarse" (this package's evidence).
- **Downgrade / reopen conditions.** Downgrade to discarded if the subunit-resolved join shows no Ca_v3 action for terodiline, or if the access state is confirmed as withdrawn. Reopen only as a *class* question (M1 antagonism as a myelination lever in a WWOX system) with a currently available compound, never as this molecule, and only once the myelination need has any pharmacological premise at all.

**A second context signal, recorded as an observation rather than a hypothesis.** Of the 44 compounds L labels compatible on a directed need, **9 carry only the access category `unknown/unverified`** — bepridil, mibefradil, terodiline, suloctidil, paramethadione, trimethadione, phensuximide, esketamine (salt record) and CNS-5161 — while **21 are `experimental` only** and just 6 are plainly `prescription` (felbamate, perampanel, topiramate, ethosuximide, methsuximide, vigabatrin). Bepridil and mibefradil are known market withdrawals. A target-only listing ranks all 44 alike; the catalogue's access field, which the matching paths do not consult, separates them. This is a usability axis, not a pharmacological one, and it belongs in the ranking rather than in the direction label.

**What was considered and did not survive.** The 16 seizure/T-type overlaps (one record counted under two needs, no independent two-need compatibility). Vigabatrin's seizure-plus-inhibitory-hypofunction pair (one ABAT mechanism, and the second need's direction is explicitly unknown with a safety signal recorded in the map). Dextromethorphan, whose GtoPdb record adds a sigma-1 agonist action alongside the NMDAR block — a genuine second context, but it bears on no second need in the module and the NMDAR arm is already covered by better-characterised compounds. The fumarates and omaveloxolone on NEED-REDOX-NRF2, where the need itself refuses the premise (IT11 P2.3: agreement between two electrophiles does not show NRF2 dependence). No candidate promotion is proposed by this package.

## Reproduce

```bash
cd disease-models/wwox/research/drug_repurposing
C=catalog/cache   # gitignored third-party cache; no downloads were made by this package
python3 matching_it18_p4_20261101/matching_task.py answers \
  --catalog catalog/catalog.jsonl.gz --needs needs/needs.json \
  --chembl-targets $C/chembl/targets.jsonl.gz --gtopdb-dir $C/gtopdb
python3 matching_it18_p4_20261101/matching_task.py score \
  --catalog catalog/catalog.jsonl.gz --needs needs/needs.json \
  --chembl-targets $C/chembl/targets.jsonl.gz --gtopdb-dir $C/gtopdb \
  --card-links catalog/card_links.json
python3 matching_it18_p4_20261101/test_matching_task.py   # 10 tests, verbosity=2
```

Zero network calls, zero spend, no registration, no contact address sent anywhere. ChEMBL-derived (CC BY-SA 3.0) and GtoPdb-derived (CC BY-SA 4.0) content in the committed tables is limited to identifiers, compound names and coarse direction classes; the raw third-party files stay in the gitignored cache. Wall time: about 25 s per command (the ChEMBL target file dominates).

## Limitations stated plainly

1. The principal figure rests on 2 determinate EVAL rows. It is reported because the registration required it to be, and it supports no comparison.
2. Nothing here says any compound helps in WWOX deficiency, is safe, or that the need's direction is the beneficial direction. Pharmacological compatibility only.
3. The task is retrospective on pre-existing curated data, as the registration's declared-prior-knowledge section states. Hiding the answer table does not make it prospective.
4. Unknown is kept distinct from negative throughout: 68 of the 76 directed rows (31 of 33 in EVAL) have no determinate reference and are counted as unknown, never as errors. The 129 rows on non-directed needs are not scored against the reference at all, by design.
5. The group-record defect is documented and partly repaired in a second run; it is not fixed at the source, which is a subunit-aware join and is the named next step.
