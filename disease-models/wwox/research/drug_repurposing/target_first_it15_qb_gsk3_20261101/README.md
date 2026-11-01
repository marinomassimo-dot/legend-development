# IT15 Q-B: GSK3 mechanism classes, target-first, 2026-11-01

Scientist package (research, not the integrator). Non-canonical research material. Not medical advice; no dose, schedule or individual regimen appears. Question, criteria and cases were fixed in `PRE_REGISTRATION.md` before extraction; its Deviations section lists four operational notes (one clarifies how criterion (i) is read).

## Corrections after independent verification (2026-11-01)

Source: `../verify_it15_qb_20261101/README.md`. Verdict (partial abstention, no nomination) stands: the premise is still three single-lane pSer9 blots from one figure, no kinase-activity assay in any WWOX system, and none of the corrections supplies a WWOX-specific criterion.

1. Isoform ratio. Old: "nothing separates GSK3A from GSK3B by more than about 4-fold for any compound; isoform selectivity is not an available lever". New: ratio about 1 holds for the named compounds only. Re-derived from my own 10,881 raw rows: 773 same-document exact A/B pairs (median per compound/document/type), 86 above 10-fold (verifier: 768 and 86), e.g. PMID 22533818 (CHEMBL2062370) 185 vs 2 nM. I agree with the verifier; the small pair-count difference is grouping.
2. Tau versus beta-catenin. Old: "0 of 13 documents pair Tau phospho and beta-catenin". New: counter-example CHEMBL6153053 (PMID 39798400): p-tau Ser396 down and beta-catenin up in SH-SY5Y under a GSK-3beta inhibitor (qualitative, not a WWOX system, one compound). My scan only looked at GSK3-target rows; the beta-catenin rows sit on an unchecked target.
3. Substrate-competitive/non-ATP classes. Old: "not matched, unsearchable". New: TDZD-8 = CHEMBL284861 (13 GSK3B IC50 rows, panel CHEMBL1135834), L803-mts = CHEMBL3358804 (40 uM) and two analogues, unnamed in ChEMBL; VP3.15 not matched. TDZD-8 still fails criterion (i).
4. Tideglusib. Old: "Cys-199-dependent". New: Cys-199 modulates dissociation (C199A retains activity with lower potency, PMID 22102280); the "Cys-199-dependent" title belongs to COB-187. The kinobead censoring is uninformative either way (thiol consumption is an equal explanation). Its Wnt direction is untested (adverse report, PMID 37316860).
5. LY-2090314 vs laduviglusib. Old: "sibling", "chemotype". New: different scaffolds (bisarylmaleimide-type vs aminopyrimidine), same ATP-site class label only. Single-origin isoform figure: wild-type 1.5 vs 0.9 nM (1.67), present in three documents = one origin; the 1.15 pools mutant enzymes.
6. CHEMBL562310. Old: IWR class "by my reading". New: IWR-1-endo by identical InChIKey (TNKS1 131 nM, TNKS2 56 nM); it needs GSK3 to act, so it is NOT an orthogonal control. The pSer9-down versus Wnt-up "conflict" is weaker: Wnt signalling does not use Ser9 (PMID 15791206). The activator document CHEMBL3580635 also has Western beta-catenin Ser33/37/Thr41 rows in SW480.
7. GtoPdb figures (lithium pIC50 2.6, AZD-1080, voruciclib, CHIR-98014, SB-415286) are not re-verified (API 401 for the verifier); they are my cache reading only.

Statements below this section that conflict with it are superseded by it; the tables were corrected in place.

## 1. Decision

**Partial abstention.** No compound is nominated as a therapeutic candidate. Every GSK3-directed compound stays a TOOL for one discriminating experiment, because the premise cannot carry more: one pSer9 western in the Wwox-null brain, no kinase-activity assay in any WWOX system, an Axin-like docking mechanism shown only in RNAi SH-SY5Y cells, and an organoid Wnt direction (up) opposite to what higher GSK3 activity predicts. What the target-first retrieval adds is a graded map of which mechanism classes exist in public data, what each can and cannot discriminate, and a design for the experiment (section 6). The IT10 Q7 state (50 families, all DIAGNOSTIC_ONLY, hop0) is reconciled, not repeated: the same names now carry grades, mechanism class and identity.

## 2. Retrieved (counts from `perimeter_log.tsv`, `census`, raw bodies in the scratchpad, not committed: ChEMBL is CC BY-SA 3.0)

| Item | Result |
|---|---|
| ChEMBL single-protein targets | GSK3B human CHEMBL262, GSK3A human CHEMBL2850, Gsk3b rat CHEMBL3669, Gsk3b mouse CHEMBL1075321, Gsk3a rat CHEMBL1075224, Gsk3a mouse CHEMBL2176843 |
| Activity rows IC50/Ki/Kd (EC50 excluded by pre-registration) | 7,429 + 3,426 + 12 + 13 + 0 + 1 = 10,881; **no truncation** (every total_count equals the rows read) |
| Distinct molecules / with a pref_name | 7,173 / 442; 1,557 have a GSK3A and a GSK3B human row in one document (mostly kinase profiling sets) |
| Compound-level pulls through the adapter (all targets of the molecule) | 10 molecules, 2,384 relation rows incl. GtoPdb (49 rows on GSK3A/B) and mechanism rows; 1,407 assays with context; none truncated |
| Mechanism lists per GSK3 target | 6 molecules curated as GSK3 inhibitors (LY-2090314, tideglusib, elraglusib, lithium carbonate, lithium citrate; AZD-1080 on the family target); **no activator curated** |
| Failures | 22 failed attempts (HTTP 500 or timeout). The 1000-row page failed for 4 targets and was re-read as 200-row pages (all complete); the target request for P49841 failed 3 of 3 (CHEMBL262 known from an earlier adapter call). Failure means "not retrieved", never "no data" |
| Not in cache / not retrieved | DrugCentral file (absent from the cache, not downloaded); TDZD-8, L803-mts (adapter name search NO_MATCH_FOUND, later found unnamed by structure, see corrections), VP3.15 (not matched); EC50 rows; IMPase potency |
| PubMed (metadata and abstract only; no full text read) | PMID 22102280 (tideglusib), 11162580 (lithium, Mg2+), 12606497 (CHIR series), 15267232 (LY-2090314 series), 19125156 (Axin-pathway Wnt inhibitors) |

## 3. Verified (checked against a source in this package)

- Lithium: Mg2+-competitive, not competitive with ATP or substrate (PMID 11162580 abstract). ChEMBL curates two mechanisms for lithium carbonate: IMPase 1 and GSK3. The active species Li+ is a separate molecule (CHEMBL1234004) with 2 rows (2 mM, copied from two review documents, one with validity comment "Outside typical range"); the salts carry none. GtoPdb pIC50 2.6 is NOT re-verified (API 401 for the verifier); the 2 mM is a review-to-review copy with unknown primary origin, counted once.
- Tideglusib: irreversible, non-competitive with ATP; Cys-199 modulates dissociation, C199A retains activity with lower potency (PMID 22102280 abstract; covalent bond "not unequivocally" shown). Within document CHEMBL4819140: 139 nM after 3 h pre-incubation vs 1,780 nM without, a 12.8-fold time dependence (one target, not a selectivity). Across 11 GSK3B rows the value ranges from 5 nM to above 10 uM; the Kd rows (kinobeads, document CHEMBL3991601) are all censored above 30 uM and that method displaces ATP-site binders, so it is blind to this class.
- Same-document grading (P6 logic imported unchanged from `../scout_it14_p6_20261101/selectivity_p6.py`; `graded_comparisons_qb.tsv`): GSK3A+GSK3B groups 22 = 3 INTERPRETABLE, 11 LIMITED, 5 PANEL_NOT_SELECTIVITY, 3 NOT_DETERMINABLE. INTERPRETABLE: laduviglusib 1.59 (CHEMBL4020814) and 1.0 (CHEMBL5728885, a patent); LY-2090314 1.15 (CHEMBL4334438; **the group pools two mutant enzymes**, the wild-type pair is 1.5 vs 0.9 nM, 1.67). LIMITED: AZD-1080 (GtoPdb A 6.9 vs B 30.9 nM), kenpaullone, 1-azakenpaullone, SB-216763 (defined complex vs single). Every cross-family kinase set is PANEL_NOT_SELECTIVITY, no ratio. The ratio of about 1 holds for the named compounds graded here only (AZD-1080's PubChem row is an unresolved at-least-25-fold B preference). ChEMBL holds many 10- to 1000-fold same-document GSK3A/GSK3B pairs (see corrections section).
- AZD-1080: isoform preference reverses between origins (GtoPdb A 6.9 nM, B 30.9 nM; PubChem kinome panel B 100 nM, A censored above 2.5 uM). Kept as unresolved.
- Substrate readouts: of 13 documents with a Tau, catenin or Wnt wording in the GSK3 rows, 12 are Tau (one with LY-2090314, 0.7 nM Ser396 in human SY5Y, next to a 1.1 nM enzyme row in document CHEMBL1138659) and 1 is a SuperTOPFlash set; my scan looked only at rows on the GSK3 targets and found no document with both; the verifier found a counter-example: CHEMBL6153053 (PMID 39798400): p-tau Ser396 down and beta-catenin up in SH-SY5Y under a GSK-3beta inhibitor (qualitative, not a WWOX system, one compound not a class comparison; found by the verifier, my scan only looked at GSK3-target rows).

## 4. Generated (hypotheses, not findings)

The chain (`chain_qb.tsv`), the four cases (`cases_qb.tsv`) and the experiment below are generated. Class labels "ATP-competitive" for LY-2090314, laduviglusib, AZD-1080, the maleimides and paullones are background knowledge: no retrieved row or abstract states the competition mode (only lithium and tideglusib are source-verified). The statement that GSK3 inhibition raises beta-catenin signalling is background knowledge and not retrieved here; the module's needs file says the same (`do_not_assume` on lithium). The common name of CHEMBL562310 (an Axin-stabilising, tankyrase-type compound) is my reading of its structure; only the document (PMID 19125156, abstract read) is verified.

## 5. The four cases, and what each adds

| Case | Compound | Verdict | Adds over known literature |
|---|---|---|---|
| C1 known reference | Lithium | reference only | the activity sits on the ion not the salts; second curated target (IMPase) is in the same curation; the only WWOX pharmacology is non-specific |
| C2 hypothesis | LY-2090314 (laduviglusib is a different scaffold, same ATP-site class label) | tool, passes (i)-(iv) | a Tau Ser396 cell assay in SY5Y (the cell line of the WWOX-Tau study) already exists for this compound with an enzyme row in the same document; isoform ratio about 1 |
| C3 alternative mechanism | Tideglusib | not deepened, fails (i) | shows why one potency is meaningless for this class and that no ChEMBL comparison can grade it |
| C4 counter / control | Axin-pathway compound CHEMBL562310; GSK3-"activator" analogues | control only | the Wnt-direction conflict has one qualitative precedent for a single inhibitor: CHEMBL6153053 (PMID 39798400): p-tau Ser396 down and beta-catenin up in SH-SY5Y under a GSK-3beta inhibitor (qualitative, not a WWOX system, one compound not a class comparison; found by the verifier, my scan only looked at GSK3-target rows); none for a class comparison or a WWOX system |

Near alternatives left, and why: elraglusib (one enzyme row, fails (i)); SB-216763, kenpaullone, 1-azakenpaullone (pass (i) as LIMITED but add no class; the paullones also hit CDK1/CDK5); AZD-1080 (unresolved isoform direction); laduviglusib (aminopyrimidine, a different scaffold from the bisarylmaleimide-type LY-2090314) kept as a comparator of C2, not a separate case; substrate-competitive and non-ATP classes are in ChEMBL under no name: TDZD-8 = CHEMBL284861 (13 GSK3B IC50 rows, same-document panel CHEMBL1135834), L803-mts = CHEMBL3358804 (one row, 40 uM) plus two analogues; VP3.15 not matched. TDZD-8 still fails (i) (no GSK3A row, cross-family panel gives no ratio) but is the better reversible-versus-irreversible contrast to tideglusib. Docking-site (Axin-site, map H-1) ligands remain unfound.

## 6. Discriminating experiment (design, no dose)

In Wwox-null (and neuron-specific) brain tissue or primary neurons, or WWOX-knockout organoid-derived neurons, with wild-type controls and AAV-WWOX re-expression as a rescue arm: (1) measure GSK3 activity directly (immunoprecipitated kinase assay or targeted phospho-proteomics of Tau S396/S404, glycogen synthase, beta-catenin phospho-S33/S37/T41) beside pSer9; (2) apply one ATP-site inhibitor, one Mg2+-competitive ion (lithium), one irreversible non-ATP inhibitor, and one Axin-pathway Wnt-lowering control, each at matched target engagement read by the substrate (not by pSer9, which lithium itself is suspected to move: background knowledge); (3) read active beta-catenin, AXIN2 and LEF1 alongside. Predictions fixed here: if GSK3 catalytic output is raised in the knockout, all three GSK3 classes lower Tau pS396/S404 more than in wild type; lithium differing from the other two at equal Tau effect points to lithium-specific actions (IMPase); beta-catenin readouts rise under the GSK3 classes and fall under the Axin control; the Axin control not moving Tau is what makes Tau and catenin separable by class. Falsifiers are in `chain_qb.tsv`.

## 7. Failed steps and what remains searchable

Failed: no GSK3 compound meets a WWOX-specific criterion; no isoform lever; no compound passes (i) with a substrate-selective readout; docking/substrate-competitive classes not found; DrugCentral file absent; IMPase potency and EC50 not read. Searchable next: (a) a kinase-activity or phospho-substrate measurement in any WWOX system (this would turn the diagnostic-only status into a ranked one); (b) a similarity search for Axin-site ligands (substrate-competitive and TDZD-type compounds were found by the verifier by structure); (c) primary-source panels for the LIMITED pairs (the assay descriptions of the kinome panel say nothing about ATP concentration).

## 8. For the independent verifier

Re-check: the pooling of mutant enzymes in the LY-2090314 INTERPRETABLE group (CHEMBL4334438); that CHEMBL562310 is the IWR-class compound and that its row sits on the Axin1-GSK3B target; that lithium rows come from reviews (documents CHEMBL3745682, CHEMBL4041480); the absence of any tau+catenin document (regex on assay descriptions, `substrate_readout_inventory_qb.tsv`); the three-way split of CHEMBL262 pages (7,000 + 429) for duplicates (deduplicated by activity_id); and that this package imported `selectivity_p6.py`, which wrote a `__pycache__` next to that file (outside this directory; no source was edited).

## Files

`PRE_REGISTRATION.md`, `perimeter_log.tsv`, `relations_qb.tsv`, `assay_context_qb.tsv`, `graded_comparisons_qb.tsv`, `identity_qb.tsv`, `identity_raw_qb.tsv`, `chain_qb.tsv`, `cases_qb.tsv`, `substrate_readout_inventory_qb.tsv`; scripts `retrieve_qb.py`, `census_qb.py`, `compound_qb.py`, `grade_qb.py`, `mechanism_qb.py` (take `--raw <dir>` for the raw bodies; rerun regenerates the tables).

## Note by the integrator on grader versions (2026-11-01)

The grades in `graded_comparisons_qb.tsv` were produced with `selectivity_p6.py` as it stood when this package ran. Afterwards the integrator changed the grader twice: (a) a two-gene list of isoforms such as `GSK3A|GSK3B` is now a group and not a defined complex (so a value measured on a ChEMBL target named for both isoforms is not attributed to either), and (b) the technique vocabulary gained "clamp" and "oocyte" (no effect on kinase assays). The GSK3A|GSK3B-labelled target rows (for example the 1-azakenpaullone row graded as a kinase-family panel) are therefore read here as group values. The table was not regenerated because the raw pulls needed by `grade_qb.py --raw` were not re-run; the conclusion (partial abstention) does not rest on those rows.

Update (same day, after the hostile review): the grader was tightened again (stimulus/holding voltage/agonist conditions, family rule) and `graded_comparisons_qb.tsv` was regraded from `relations_qb.tsv` and `assay_context_qb.tsv`: 60 groups = 3 INTERPRETABLE / 28 LIMITED / 14 PANEL_NOT_SELECTIVITY / 15 NOT_DETERMINABLE. This supersedes the paragraph above about the unregenerated table; the conclusion is unchanged.
